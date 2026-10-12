"""Offline tests on a trimmed copy of the pilot data (fixtures/pilot-1) and on synthetic run dirs.
No agents, no model calls.

run: python3 -I tools/digest-eval/tests/test_digest_eval.py
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.dirname(HERE)
sys.path.insert(0, TOOL)
PILOT = os.path.join(HERE, "fixtures", "pilot-1")

import cli  # noqa: E402
from digest_eval import blinder, conditions, gate, judges, ledger, readers, runner, score, script_judge  # noqa: E402
from digest_eval.records import read_key, save_json  # noqa: E402
from digest_eval.spec import JsonTaskSource, load_spec  # noqa: E402

SPEC = {
    "slug": "stop-yapping",
    "demands": [
        {"id": "opening", "text": "open with the first word of substance", "check": "script",
         "pattern": r"^\s*(hi|hello|sure|certainly|of course|great question|happy to)\b"},
        {"id": "long_sentence", "text": "break any sentence over fifteen words", "check": "script",
         "kind": "sentence_words_over", "limit": 15},
        {"id": "hedge", "text": "state what you know as fact", "check": "judge"},
    ],
    "conditions": {"baselines": ["full", "terse", "placebo"], "terse_line": "Be terse.",
                   "placebo_source": None, "ablations": True},
    "reader": {"adapter": "pi", "model": "long"},
    "judge": {"name": "sonnet-agents", "brief": "judge_brief.md"},
    "reps": 2,
    "gate": {"split": "test", "ci": 0.95, "min_cut_vs_none": 0.5, "margin_vs_full": 0.5,
             "completion_margin": 0.06, "drift_margin": 0.1},
}

TASKS = {
    "singles": [
        {"id": "a", "family": "f1", "split": "dev", "message": "How do I reverse a list in Python?", "answer": r"\[::-1\]|reverse"},
        {"id": "b", "family": "f1", "split": "test", "message": "What port does HTTPS use?", "answer": r"\b443\b"},
    ],
    "sessions": [{"id": "s1", "split": "test", "turns": ["Hi", "And then?", "Last one"]}],
}


class FakeReader(readers.Reader):
    ident = {"adapter": "fake", "model": "x"}

    def __init__(self):
        self.calls = []

    def reply(self, append_path, message, session=None):
        self.calls.append((append_path, message, session))
        text = "Sure! Use [::-1]. Port 443." if append_path is None else "[::-1] 443"
        return {"raw": text, "text": text, "leak": False, "secs": 0.1, "rc": 0, "attempt": 1}


def make_eval_dir(tmp, spec=SPEC, tasks=TASKS):
    d = os.path.join(tmp, "evals", "demo")
    os.makedirs(d)
    spec = dict(spec, slug="demo")
    save_json(os.path.join(d, "spec.json"), spec)
    save_json(os.path.join(d, "tasks.json"), tasks)
    with open(os.path.join(d, "judge_brief.md"), "w") as f:
        f.write("Judge {PACKET}; write {OUT}; manifesto {MANIFESTO}; demands:\n{DEMANDS}\n")
    return d


class PilotReproduction(unittest.TestCase):
    """The tool must reproduce the pilot's numbers from its stored verdicts and key."""

    def test_single_task_means_and_done(self):
        out = score.score(SPEC, PILOT)
        by = out["splits"]["all"]["by_condition"]
        self.assertEqual(round(by["none"]["mean_violations"], 2), 8.39)
        self.assertEqual(round(by["digest"]["mean_violations"], 2), 1.61)
        self.assertEqual(round(by["full"]["mean_violations"], 2), 1.11)
        self.assertEqual((by["none"]["done"], by["digest"]["done"], by["full"]["done"]), (17, 18, 17))
        self.assertEqual((by["none"]["n"], by["digest"]["n"], by["full"]["n"]), (18, 18, 18))
        self.assertLess(out["splits"]["all"]["digest_vs"]["none"]["ci_high"], 0)
        self.assertEqual(out["splits"]["all"]["drift"]["none"]["sessions"], 1)
        os.remove(os.path.join(PILOT, "scores.json"))

    def test_script_judge_runs_on_pilot(self):
        out = script_judge.judge(SPEC, PILOT)
        self.assertEqual(len(out), len(read_key(PILOT)))
        self.assertTrue(all(set(v["demands"]) == {"opening", "long_sentence"} for v in out))
        os.remove(os.path.join(PILOT, "script.json"))


class Conditions(unittest.TestCase):
    def test_build(self):
        tmp = tempfile.mkdtemp()
        src = os.path.join(tmp, "placebo.txt")
        with open(src, "w") as f:
            f.write("the river runs past the mill and under the bridge")
        spec = dict(SPEC, conditions=dict(SPEC["conditions"], placebo_source=src))
        digest = "Answer first. Delete every hedge.\n\nBreak long sentences."
        paths = conditions.build(spec, tmp, digest, ["---\ntitle: x\nversion: \"1.0.0\"\n---\n\n# Body\ntext", "---\nversion: 2\n---\nmore"])
        self.assertEqual(sorted(paths), ["ablation-01", "ablation-02", "ablation-03", "digest", "full", "none", "placebo", "terse"])
        self.assertIsNone(paths["none"])
        self.assertEqual(open(paths["full"]).read(), "# Body\ntext\n\nmore\n")
        self.assertEqual(len(open(paths["placebo"]).read().split()), len(digest.split()))
        self.assertEqual(open(paths["ablation-02"]).read().strip(), "Answer first. Break long sentences.")
        self.assertEqual(conditions.load(tmp), paths)
        shutil.rmtree(tmp)


class ReaderAdapter(unittest.TestCase):
    def test_pi_command(self):
        r = readers.PiReader("long", cwd=tempfile.mkdtemp())
        cmd = r.command("/x/digest.txt", "hello")
        self.assertEqual(cmd[:2], ["pi", "-p"])
        self.assertIn("--no-session", cmd)
        self.assertEqual(cmd[-3:], ["--append-system-prompt", "/x/digest.txt", "hello"])
        cmd = r.command(None, "hello", session=("/s", "id1"))
        self.assertNotIn("--append-system-prompt", cmd)
        self.assertEqual(cmd[cmd.index("--session-dir"):cmd.index("--session-dir") + 4], ["--session-dir", "/s", "--session-id", "id1"])

    def test_clean_keeps_text_after_last_think(self):
        self.assertEqual(readers.clean("draft</think>mid</think> final \n"), ("final", True))
        self.assertEqual(readers.clean(" plain "), ("plain", False))


class Loop(unittest.TestCase):
    """One cut through runner, blinder, script judge, score, gate, ledger, stale on a fake reader."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.d = make_eval_dir(self.tmp)
        self.rd = os.path.join(self.d, "cut-1")
        os.makedirs(self.rd)
        self.spec = load_spec(os.path.join(self.d, "spec.json"))
        self.tasks = JsonTaskSource(os.path.join(self.d, "tasks.json"))
        self.digest = os.path.join(self.tmp, "digest.md")
        with open(self.digest, "w") as f:
            f.write("Answer first. Delete every hedge.")
        self.manifesto = os.path.join(self.tmp, "demo.md")
        with open(self.manifesto, "w") as f:
            f.write("---\nversion: \"1.0.0\"\n---\n# Demo\nbody")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_cut(self):
        conds = {"none": None, "digest": self.digest, "full": self.manifesto}
        reader = FakeReader()
        runner.run(self.rd, reader, self.tasks, conds, reps=2)
        n = len(reader.calls)
        self.assertEqual(n, 2 * 2 * 3 + 3 * 3)
        runner.run(self.rd, reader, self.tasks, conds, reps=2)
        self.assertEqual(len(reader.calls), n, "a finished run makes no new calls")
        self.assertEqual(runner.rotate(["none", "digest", "full"], 1), ["digest", "full", "none"])

        packets, key = blinder.build_packets(self.rd)
        self.assertEqual(sorted(packets), ["a", "b", "s1"])
        self.assertFalse(os.path.exists(os.path.join(self.rd, "judge", "key.json")))
        packet = open(os.path.join(self.rd, "judge", "a.md")).read()
        for word in ("none", "digest", "full", "cond"):
            self.assertNotIn(word, packet)
        self.assertEqual(len(key), n)

        judge = judges.AgentJudge("sonnet-agents", os.path.join(self.d, "judge_brief.md"), self.manifesto, self.spec["demands"])
        brief = judge.brief(self.rd, "a")
        self.assertIn("- hedge: state what you know as fact", brief)
        self.assertNotIn("opening:", brief)
        self.assertEqual(judge.collect(self.rd)["a"], ["no verdict file"])
        for p in packets:
            ids = [rid for rid, k in key.items() if k["packet"] == p]
            verdicts = [{"id": rid, "violations": 3 if key[rid]["cond"] == "none" else 0, "done": True, "notes": ""} for rid in ids]
            save_json(os.path.join(self.rd, "judge", f"{p}.verdict.json"), verdicts)
        self.assertEqual(judge.collect(self.rd), {"a": [], "b": [], "s1": []})

        script_judge.judge(self.spec, self.rd, self.tasks)
        out = score.score(self.spec, self.rd)
        by = out["splits"]["test"]["by_condition"]
        self.assertEqual(by["none"]["per_demand"]["opening"], 1.0)
        self.assertEqual(by["digest"]["per_demand"]["opening"], 0.0)
        self.assertEqual(by["digest"]["done_rate"], 1.0)
        self.assertEqual(by["none"]["mean_violations"], 3.0)
        self.assertEqual(out["splits"]["test"]["digest_vs"]["none"]["mean_diff"], -3.0)
        self.assertIn("dev", out["splits"])

        result = gate.write_gate(self.spec, self.rd, out)
        names = [c["name"].split(":")[0] for c in result["checks"]]
        self.assertEqual(names, ["cut vs none", "near full", "completion", "drift"])
        self.assertTrue(result["pass"], result)
        self.assertIsNone(result["changed_vs_previous"])

        jd = judge.ident
        e = ledger.entry(self.spec, self.d, self.rd, 1, "cut", self.digest, [self.manifesto], reader.ident, jd,
                         self.tasks.raw, out, result, "none", "first cut")
        ledger.record(self.d, e)
        self.assertEqual(e["manifestos"][0]["version"], "1.0.0")
        self.assertEqual(e["run_dir"], "cut-1")
        self.assertFalse(ledger.stale(self.d, self.digest)["stale"])
        with open(self.digest, "a") as f:
            f.write(" More.")
        self.assertEqual(ledger.stale(self.d, self.digest)["reasons"], ["digest changed since the last cut"])
        with open(self.manifesto, "w") as f:
            f.write("---\nversion: \"1.1.0\"\n---\n")
        self.assertEqual(len(ledger.stale(self.d, self.digest)["reasons"]), 2)

        rd2 = os.path.join(self.d, "cut-2")
        shutil.copytree(self.rd, rd2)
        out2 = score.score(self.spec, rd2, previous_run_dir=self.rd)
        prev = out2["splits"]["test"]["digest_vs_previous"]
        self.assertEqual(prev["mean_diff"], 0.0)
        self.assertFalse(gate.gate(self.spec, out2)["changed_vs_previous"])
        cli.ROOT = self.tmp
        cli.main(["reps", "demo", "cut-1"])

    def test_cli_on_pilot_layout(self):
        cli.ROOT = self.tmp
        conds = {"none": None, "digest": self.digest}
        runner.run(self.rd, FakeReader(), self.tasks, conds, reps=1, sessions=False)
        cli.main(["blind", "demo", "cut-1"])
        cli.main(["script-judge", "demo", "cut-1"])
        with self.assertRaises(SystemExit) as cm:
            cli.main(["collect", "demo", "cut-1"])
        self.assertEqual(cm.exception.code, 1)
        cli.main(["score", "demo", "cut-1"])
        self.assertTrue(os.path.exists(os.path.join(self.rd, "scores.json")))
        cli.main(["reps", "demo", "cut-1"])  # no judged pairs: falls back to the script judge's counts
        cli.main(["stale", "demo", "--digest", self.digest])


class Gate(unittest.TestCase):
    def test_fails_when_interval_crosses_zero(self):
        scores = {"splits": {"test": {
            "by_condition": {"none": {"done_rate": 0.9}, "digest": {"done_rate": 0.9}},
            "digest_vs": {"none": {"n": 6, "mean_diff": -1.0, "ci_low": -2.5, "ci_high": 0.2}},
            "digest_vs_previous": None, "drift": {}}}}
        r = gate.gate(SPEC, scores)
        self.assertFalse(r["pass"])
        self.assertFalse(r["checks"][0]["pass"])
        self.assertTrue(r["checks"][1]["pass"])


class SpecValidation(unittest.TestCase):
    def test_rejects_bad_demand(self):
        tmp = tempfile.mkdtemp()
        bad = dict(SPEC, demands=[{"id": "x", "text": "t", "check": "script", "pattern": "("}])
        save_json(os.path.join(tmp, "spec.json"), bad)
        with self.assertRaises(ValueError):
            load_spec(os.path.join(tmp, "spec.json"))
        shutil.rmtree(tmp)


class SystemOneStub(unittest.TestCase):
    def test_interface_only(self):
        j = judges.SystemOneJudge("http://127.0.0.1:4150/v1/systemone", 0.5)
        self.assertEqual(j.ident["name"], "systemone")
        with self.assertRaises(NotImplementedError):
            j.brief("/x", "p")


class Reps(unittest.TestCase):
    def test_reps_from_spread(self):
        # z=1.96, sd=2, min_cut=1: pairs needed = (2*1.96*2/1)^2 = 61.5 -> 62; over 6 tasks -> 11 reps
        self.assertEqual(score.reps_needed(2.0, 6, 1.0), 11)
        self.assertEqual(score.reps_needed(0.0, 6, 1.0), 1)
        with self.assertRaises(ValueError):
            score.reps_needed(1.0, 6, 0)
        rows = [{"task": "a", "rep": 1, "cond": "digest", "violations": 1, "session": False},
                {"task": "a", "rep": 1, "cond": "none", "violations": 4, "session": False},
                {"task": "a", "rep": 2, "cond": "digest", "violations": 2, "session": False}]
        self.assertEqual(score.paired_diffs(rows), [-3])


class Launcher(unittest.TestCase):
    def test_symlinked_launcher_finds_cli(self):
        tmp = tempfile.mkdtemp()
        link = os.path.join(tmp, "bin", "digest-eval")
        os.makedirs(os.path.dirname(link))
        os.symlink(os.path.join(TOOL, "digest-eval"), link)
        p = subprocess.run([link, "--help"], capture_output=True, text=True, stdin=subprocess.DEVNULL, cwd=tmp)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("conditions", p.stdout)
        shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
