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


def run_hook(script, config, stdin="", plugin_root=PLUGIN_ROOT, **extra_env):
    """Run one hook in a fresh project folder, with no config file when config is None; the folder's path rides on the result as `project`."""
    with tempfile.TemporaryDirectory() as project:
        if config is not None:
            with open(os.path.join(project, ".manifestos.yaml"), "w") as f:
                f.write(config)
        env = {k: v for k, v in os.environ.items() if k != "UNHARNESS"}
        env.update(CLAUDE_PLUGIN_ROOT=plugin_root, CLAUDE_PROJECT_DIR=project, **extra_env)
        result = subprocess.run(
            ["bash", os.path.join(HOOKS, script)],
            input=stdin, capture_output=True, text=True, env=env, timeout=30,
        )
        result.project = project
        return result


HAPPY = "you:\n  - first-principles\n"
MISSING = "you:\n  - no-such-manifesto\n"
ALL_HOOKS = ("session-start.sh", "post-compact.sh", "subagent-start.sh", "drift-reminder.sh")
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


class SessionStartSources(unittest.TestCase):
    def test_a_file_source_is_read_from_its_absolute_path_beside_the_config(self):
        r = run_hook("session-start.sh", "you:\n  - name: notes\n    purpose: house rules\n    source: file notes/rules.md\n")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('"notes" governs your house rules \u2014 read it from ' + r.project + "/notes/rules.md.", r.stdout)

    def test_a_manifesto_source_is_read_from_the_registry_file_of_that_name(self):
        r = run_hook("session-start.sh", "you:\n  - name: again\n    source: manifesto first-principles\n")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('"again" is part of your constitution \u2014 read it from ' + FIRST_PRINCIPLES + ".", r.stdout)

    def test_a_skill_source_is_read_from_the_skill_as_written(self):
        r = run_hook("session-start.sh", "you:\n  - name: write-well\n    source: skill agent-conduct:write-well\n")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('"write-well" is part of your constitution \u2014 read it from skill agent-conduct:write-well.', r.stdout)

    def test_a_bare_item_with_a_colon_is_a_name_and_crashes_nothing(self):
        for script in ("session-start.sh", "post-compact.sh", "drift-reminder.sh"):
            r = run_hook(script, "you:\n  - agent-conduct:write-well\n")
            self.assertEqual(r.returncode, 0, script + r.stderr)
            self.assertIn("agent-conduct:write-well", r.stdout, script)


class SessionStartRegistry(unittest.TestCase):
    def test_a_relative_manifesto_dir_resolves_against_the_config_folder(self):
        r = run_hook("session-start.sh", "manifesto_dir: reg\nyou:\n  - name: again\n    source: manifesto first-principles\n")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("read it from " + r.project + "/reg/manifestos/first-principles.md.", r.stdout)
        self.assertIn("Manifestos: " + r.project + "/reg/manifestos/", r.stdout)


class ConfigProblems(unittest.TestCase):
    def test_a_broken_config_prints_one_line_on_stderr_and_nothing_on_stdout_in_every_hook(self):
        for script in ALL_HOOKS:
            r = run_hook(script, "you: [first-principles]\n", stdin=json.dumps({"agent_type": "worker"}))
            self.assertEqual((r.returncode, r.stdout), (0, ""), script)
            self.assertEqual(r.stderr, "unharness: you must be a list of elements\n", script)

    def test_a_legacy_source_is_refused_in_one_line_in_every_hook(self):
        for source in ("https://example.com/x.md", "./a.md", "some hint"):
            for script in ALL_HOOKS:
                r = run_hook(script, "you:\n  - name: x\n    source: " + source + "\n", stdin=json.dumps({"agent_type": "worker"}))
                self.assertEqual((r.returncode, r.stdout), (0, ""), script)
                self.assertEqual(len(r.stderr.splitlines()), 1, script)
                self.assertIn("write a path as file <path>", r.stderr, script)

    def test_a_missing_config_stays_silent_in_every_hook(self):
        for script in ALL_HOOKS:
            r = run_hook(script, None, stdin=json.dumps({"agent_type": "worker"}))
            self.assertEqual((r.returncode, r.stdout, r.stderr), (0, "", ""), script)


class StandDownUnderUnharness(unittest.TestCase):
    def test_session_start_and_post_compact_print_nothing_when_unharness_is_set(self):
        for script in ("session-start.sh", "post-compact.sh"):
            r = run_hook(script, HAPPY, UNHARNESS="1")
            self.assertEqual((r.returncode, r.stdout, r.stderr), (0, "", ""), script)

    def test_unharness_zero_leaves_them_running(self):
        for script in ("session-start.sh", "post-compact.sh"):
            r = run_hook(script, HAPPY, UNHARNESS="0")
            self.assertIn("first-principles", r.stdout, script)

    def test_drift_reminder_and_subagent_start_keep_running_when_unharness_is_set(self):
        drift = run_hook("drift-reminder.sh", HAPPY, UNHARNESS="1")
        self.assertIn("Active bindings: first-principles", drift.stdout)
        subagent = run_hook("subagent-start.sh", SUBAGENTS.format(name="first-principles"),
                            stdin=json.dumps({"agent_type": "worker"}), UNHARNESS="1")
        self.assertIn("first-principles", json.loads(subagent.stdout)["hookSpecificOutput"]["additionalContext"])


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
