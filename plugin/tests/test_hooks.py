"""Tests for the four hook scripts: a happy path and a missing-manifesto-file case each."""

import json
import os
import subprocess
import tempfile
import unittest

PLUGIN_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOOKS = os.path.join(PLUGIN_ROOT, "hooks")
FIRST_PRINCIPLES = os.path.join(PLUGIN_ROOT, "manifestos", "first-principles.md")


def tagline_of(path):
    with open(path) as f:
        for line in f:
            if line.startswith("tagline:"):
                return line.split(":", 1)[1].strip().strip("\"'")
    raise AssertionError("no tagline in " + path)


def run_hook(script, config, stdin="", plugin_root=PLUGIN_ROOT):
    with tempfile.TemporaryDirectory() as project:
        with open(os.path.join(project, ".manifestos.yaml"), "w") as f:
            f.write(config)
        env = dict(os.environ, CLAUDE_PLUGIN_ROOT=plugin_root, CLAUDE_PROJECT_DIR=project)
        return subprocess.run(
            ["bash", os.path.join(HOOKS, script)],
            input=stdin, capture_output=True, text=True, env=env, timeout=30,
        )


HAPPY = "you:\n  - first-principles\n"
MISSING = "you:\n  - no-such-manifesto\n"
SUBAGENTS = "subagents:\n  other:\n    - {name}\n"


class SessionStart(unittest.TestCase):
    def test_happy_path_points_at_bundled_manifestos(self):
        r = run_hook("session-start.sh", HAPPY)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('"first-principles"', r.stdout)
        self.assertIn("Manifestos: " + PLUGIN_ROOT + "/manifestos/", r.stdout)

    def test_missing_manifesto_file_still_binds_without_cloning(self):
        r = run_hook("session-start.sh", MISSING)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('"no-such-manifesto"', r.stdout)
        self.assertFalse(os.path.exists(os.path.join(PLUGIN_ROOT, "manifestos", "no-such-manifesto.md")))


class PostCompact(unittest.TestCase):
    def test_happy_path_emits_postcompact_json(self):
        r = run_hook("post-compact.sh", HAPPY)
        self.assertEqual(r.returncode, 0, r.stderr)
        out = json.loads(r.stdout)["hookSpecificOutput"]
        self.assertEqual(out["hookEventName"], "PostCompact")
        self.assertIn("first-principles", out["additionalContext"])

    def test_missing_manifesto_file_still_emits_json(self):
        r = run_hook("post-compact.sh", MISSING)
        self.assertEqual(r.returncode, 0, r.stderr)
        out = json.loads(r.stdout)["hookSpecificOutput"]
        self.assertIn("no-such-manifesto", out["additionalContext"])


class SubagentStart(unittest.TestCase):
    def test_happy_path_emits_subagent_json(self):
        r = run_hook("subagent-start.sh", SUBAGENTS.format(name="first-principles"),
                     stdin=json.dumps({"agent_type": "worker"}))
        self.assertEqual(r.returncode, 0, r.stderr)
        out = json.loads(r.stdout)["hookSpecificOutput"]
        self.assertEqual(out["hookEventName"], "SubagentStart")
        self.assertIn("first-principles", out["additionalContext"])

    def test_missing_manifesto_file_still_emits_json(self):
        r = run_hook("subagent-start.sh", SUBAGENTS.format(name="no-such-manifesto"),
                     stdin=json.dumps({"agent_type": "worker"}))
        self.assertEqual(r.returncode, 0, r.stderr)
        out = json.loads(r.stdout)["hookSpecificOutput"]
        self.assertIn("no-such-manifesto", out["additionalContext"])


class DriftReminder(unittest.TestCase):
    def test_happy_path_prints_tagline_from_bundled_file(self):
        r = run_hook("drift-reminder.sh", HAPPY)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Active bindings: first-principles", r.stdout)
        self.assertIn(tagline_of(FIRST_PRINCIPLES), r.stdout)

    def test_missing_manifesto_file_prints_bare_name(self):
        r = run_hook("drift-reminder.sh", MISSING)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout.strip(), "Active bindings: no-such-manifesto")


if __name__ == "__main__":
    unittest.main()
