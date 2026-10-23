"""Tests for sweep.py. Run with `python3 -m pytest` or `python3 test_sweep.py` from this folder.

No test touches npm or the network; each run uses --tarball and --docs.
"""

import contextlib
import importlib.util
import io
import json
import tarfile
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("sweep", HERE / "sweep.py")
sweep = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sweep)

CLI_JS = (
    'var a=process.env.CLAUDE_CODE_ALPHA;var b=process.env["OTHER_READ"];'
    'var c=x.CLAUDE_CODE_BETA_ALIAS;'
    'var s={alphaKey:z.boolean(),betaKey:z.string(),docKey:zz.enum(["a"])};'
    'var l={lazyKey:()=>O().optional().describe("x"),lazyDoc:()=>Q().min(1).optional().describe("y")};'
)
ENV_PAGE = "| `CLAUDE_CODE_ALPHA` | on |\n| `OTHER_READ=1` | read |\n"
SETTINGS_PAGE = "| `docKey` | documented |\n| `lazyDoc` | documented |\n| `attribution.pr` | text |\n"
REGISTRY = [
    {"name": "CLAUDE_CODE_ALPHA", "kind": "env"},
    {"name": "CLAUDE_CODE_GONE", "kind": "env"},
    {"name": "alphaKey", "kind": "settings"},
    {"name": "goneKey", "kind": "settings"},
    {"name": "--presentFlag", "kind": "flag"},
    {"name": "--goneFlag", "kind": "flag"},
]


class SweepTest(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.docs = self.root / "docs"
        self.docs.mkdir()
        (self.docs / "env-vars.md").write_text(ENV_PAGE)
        (self.docs / "settings-reference.md").write_text(SETTINGS_PAGE)
        registry = self.root / "switches.json"
        registry.write_text(json.dumps(REGISTRY))
        self.sweeps = self.root / "sweeps"
        self.patches = (
            (sweep, "SWEEPS", sweep.SWEEPS), (sweep, "REGISTRY", sweep.REGISTRY),
        )
        sweep.SWEEPS, sweep.REGISTRY = self.sweeps, registry
        self.addCleanup(self.restore)

    def restore(self):
        for module, name, value in self.patches:
            setattr(module, name, value)

    def tarball(self, files, name="pkg.tgz"):
        source = self.root / "pkgsrc"
        source.mkdir(exist_ok=True)
        path = self.root / name
        with tarfile.open(path, "w:gz") as archive:
            for member, content in files.items():
                file = source / member.replace("/", "_")
                file.write_bytes(content if isinstance(content, bytes) else content.encode())
                archive.add(file, arcname=f"package/{member}")
        return path

    def run_sweep(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = sweep.main(list(args))
        return code, out.getvalue(), err.getvalue()

    def standard(self, version="2.1.309", extra=()):
        tarball = self.tarball({"cli.js": CLI_JS + " --presentFlag"})
        return self.run_sweep(version, "--tarball", str(tarball), "--docs", str(self.docs), *extra)

    def test_json_fields(self):
        code, _, _ = self.standard()
        self.assertEqual(code, 0)
        record = json.loads((self.sweeps / "2.1.309.json").read_text())
        self.assertEqual(sorted(record), ["documented_env", "documented_settings", "env", "literals",
                                          "settings_candidates", "version"])
        self.assertEqual(record["version"], "2.1.309")
        self.assertEqual(record["env"], ["CLAUDE_CODE_ALPHA", "OTHER_READ"])
        self.assertEqual(record["literals"], ["CLAUDE_CODE_ALPHA", "CLAUDE_CODE_BETA_ALIAS"])
        self.assertEqual(record["settings_candidates"], ["alphaKey", "betaKey", "docKey", "lazyDoc", "lazyKey"])
        self.assertEqual(record["documented_env"], ["CLAUDE_CODE_ALPHA", "OTHER_READ"])
        self.assertEqual(record["documented_settings"], ["attribution", "docKey", "lazyDoc"])

    def test_report_sections(self):
        _, out, _ = self.standard()
        undocumented_env = out.split("## Undocumented env names")[1].split("##")[0]
        self.assertIn("`CLAUDE_CODE_BETA_ALIAS`", undocumented_env)
        self.assertNotIn("CLAUDE_CODE_ALPHA", undocumented_env)
        undocumented_settings = out.split("## Undocumented settings candidates")[1].split("##")[0]
        self.assertIn("`alphaKey`", undocumented_settings)
        self.assertIn("`betaKey`", undocumented_settings)
        self.assertIn("`lazyKey`", undocumented_settings)
        self.assertNotIn("docKey", undocumented_settings)
        self.assertIn("no previous sweep", out)
        absent = out.split("## Registry switches absent from this version")[1]
        for name in ("CLAUDE_CODE_GONE (env)", "goneKey (settings)", "--goneFlag (flag)"):
            self.assertIn(name, absent)
        for name in ("CLAUDE_CODE_ALPHA", "alphaKey", "--presentFlag"):
            self.assertNotIn(name, absent)

    def test_previous_diff_defaults_to_newest_other_file(self):
        self.sweeps.mkdir()
        for version, names in (("2.1.100", ["OLD_ONLY", "CLAUDE_CODE_ALPHA"]), ("2.1.200", ["CLAUDE_CODE_ALPHA", "NEWER_GONE"])):
            record = {"version": version, "env": names, "literals": [], "settings_candidates": [],
                      "documented_env": [], "documented_settings": []}
            (self.sweeps / f"{version}.json").write_text(json.dumps(record))
        _, out, _ = self.standard()
        new = out.split("## New since 2.1.200")[1].split("##")[0]
        gone = out.split("## Gone since 2.1.200")[1].split("##")[0]
        self.assertIn("`OTHER_READ`", new)
        self.assertNotIn("CLAUDE_CODE_ALPHA", new)
        self.assertIn("`NEWER_GONE`", gone)
        self.assertNotIn("OLD_ONLY", gone)

    def test_explicit_previous(self):
        previous = self.root / "prev.json"
        previous.write_text(json.dumps({"version": "1.0.0", "env": ["ONLY_BEFORE"], "literals": [],
                                        "settings_candidates": [], "documented_env": [],
                                        "documented_settings": []}))
        _, out, _ = self.standard(extra=("--previous", str(previous)))
        self.assertIn("## Gone since prev", out)
        self.assertIn("`ONLY_BEFORE`", out)

    def test_native_fallback_scans_large_files(self):
        blob = b"\x00\xff" * 600_000 + b" process.env.NATIVE_READ CLAUDE_CODE_NATIVE x{boolKey:q.boolean(" + b"\x00" * 10
        tarball = self.tarball({"bin/claude": blob, "README.md": "small"})
        code, out, _ = self.run_sweep("2.1.309", "--tarball", str(tarball), "--docs", str(self.docs))
        self.assertEqual(code, 0)
        record = json.loads((self.sweeps / "2.1.309.json").read_text())
        self.assertIn("NATIVE_READ", record["env"])
        self.assertIn("CLAUDE_CODE_NATIVE", record["literals"])
        self.assertIn("boolKey", record["settings_candidates"])

    def test_refusals(self):
        code, _, err = self.run_sweep("2.1", "--docs", str(self.docs))
        self.assertEqual(code, 1)
        self.assertIn("not X.Y.Z", err)
        code, _, err = self.run_sweep("2.1.309", "--tarball", str(self.root / "none.tgz"))
        self.assertEqual(code, 1)
        self.assertIn("not a file", err)
        empty = self.tarball({"README.md": "small"}, "empty.tgz")
        code, _, err = self.run_sweep("2.1.309", "--tarball", str(empty), "--docs", str(self.docs))
        self.assertEqual(code, 1)
        self.assertIn("no package/cli.js", err)
        (self.docs / "env-vars.md").unlink()
        code, _, err = self.standard()
        self.assertEqual(code, 1)
        self.assertIn("--docs DIR needs", err)
        self.assertFalse((self.sweeps / "2.1.309.json").exists())


if __name__ == "__main__":
    unittest.main()
