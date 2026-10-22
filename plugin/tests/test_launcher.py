"""Tests for plugin/bin/unharness: which uvx command it builds, seen through a stub uvx on PATH."""

import os
import subprocess
import tempfile
import unittest

PLUGIN_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAUNCHER = os.path.join(PLUGIN_ROOT, "bin", "unharness")
STUB = '#!/bin/sh\nprintf "%s\\n" "$@" > "$STUB_OUTPUT"\n'
GIT_SOURCE = "git+https://example.com/repo@v1#subdirectory=plugin/unharness"


def uvx_arguments(**environment):
    """Run the launcher with a stub uv and uvx first on PATH; return the arguments uvx received."""
    with tempfile.TemporaryDirectory() as folder:
        for name in ("uv", "uvx"):
            path = os.path.join(folder, name)
            with open(path, "w") as stub:
                stub.write(STUB)
            os.chmod(path, 0o755)
        output = os.path.join(folder, "arguments")
        env = {"PATH": folder + ":/usr/bin:/bin", "STUB_OUTPUT": output, **environment}
        run = subprocess.run(["bash", LAUNCHER, "stack", "--config", "x"], env=env, capture_output=True, text=True)
        assert run.returncode == 0, run.stderr
        with open(output) as recorded:
            return recorded.read().splitlines()


class Launcher(unittest.TestCase):
    def test_by_default_it_runs_the_copy_bundled_with_the_plugin_without_the_uvx_cache(self):
        bundled = os.path.realpath(os.path.join(PLUGIN_ROOT, "unharness"))
        arguments = uvx_arguments()
        for position in (2, 4):
            arguments[position] = os.path.realpath(arguments[position])
        self.assertEqual(
            arguments,
            ["--no-cache", "--from", bundled, "--with-editable", bundled, "unharness", "stack", "--config", "x"],
        )

    def test_a_directory_source_is_built_fresh_every_time(self):
        with tempfile.TemporaryDirectory() as source:
            arguments = uvx_arguments(UNHARNESS_FROM=source)
        self.assertEqual(arguments[:4], ["--no-cache", "--from", source, "--with-editable"])

    def test_a_git_source_keeps_the_uvx_cache(self):
        arguments = uvx_arguments(UNHARNESS_FROM=GIT_SOURCE)
        self.assertEqual(arguments, ["--from", GIT_SOURCE, "unharness", "stack", "--config", "x"])


if __name__ == "__main__":
    unittest.main()
