import json
import os
import shlex
import subprocess
import sys
from hashlib import sha256
from pathlib import Path

from helpers import write

PROMPT = "You are bound.\n"
FAKE_LAUNCHER = '#!/bin/sh\nprintf "%s\\n" "$@" > "$DUMP/argv"\nenv > "$DUMP/env"\nexit 3\n'
FAKE_SHELL = '#!/bin/sh\nprintf "%s\\n" "$@" > "$DUMP/shell-argv"\nexit 5\n'


def run_launch(tmp_path: Path, *arguments: str, stdin: str = "", **extra_env: str) -> subprocess.CompletedProcess:
    env = {
        "PATH": f"{tmp_path / 'bin'}:/usr/bin:/bin", "XDG_CACHE_HOME": str(tmp_path / "cache"),
        "DUMP": str(tmp_path), **extra_env,
    }
    return subprocess.run(
        [sys.executable, "-m", "unharness.cli", "launch", *arguments],
        input=stdin, capture_output=True, text=True, env=env,
    )


def fake_launcher(tmp_path: Path, name: str = "fakeclaude") -> None:
    script = write(tmp_path / "bin" / name, FAKE_LAUNCHER)
    script.chmod(0o755)


def cached(tmp_path: Path, prompt: str = PROMPT) -> Path:
    return tmp_path / "cache" / "unharness" / f"{sha256(prompt.encode()).hexdigest()}.md"


def test_a_launcher_on_the_path_replaces_the_process_and_its_status_comes_back(tmp_path):
    fake_launcher(tmp_path)

    run = run_launch(tmp_path, PROMPT, "--", "fakeclaude", "extra", "--flag")

    assert run.returncode == 3
    argv = (tmp_path / "argv").read_text().splitlines()
    assert argv[:2] == ["extra", "--flag"]
    assert argv[2:5] == ["--system-prompt-file", str(cached(tmp_path)), "--disallowedTools"]
    assert json.loads(argv[-1])["outputStyle"] == "default"
    launcher_environment = (tmp_path / "env").read_text().splitlines()
    assert "UNHARNESS=1" in launcher_environment
    assert "CLAUDE_CODE_DISABLE_CLAUDE_MDS=1" in launcher_environment


def test_the_prompt_comes_from_stdin_when_no_argument_gives_it(tmp_path):
    fake_launcher(tmp_path)

    run = run_launch(tmp_path, "--keep-claude-md", "--", "fakeclaude", stdin=PROMPT)

    assert run.returncode == 3
    assert cached(tmp_path).read_text() == PROMPT
    assert "CLAUDE_CODE_DISABLE_CLAUDE_MDS=1" not in (tmp_path / "env").read_text().splitlines()


def test_an_empty_prompt_fails_in_one_line_with_status_1(tmp_path):
    run = run_launch(tmp_path, stdin="")

    assert (run.returncode, run.stdout, run.stderr) == (1, "", "unharness: the prompt is empty\n")


def test_without_a_launcher_the_verb_prints_the_command_and_runs_nothing(tmp_path):
    run = run_launch(tmp_path, PROMPT)

    assert run.returncode == 0
    line = shlex.split(run.stdout.removesuffix(" </dev/tty\n"))
    assert line[0] == "env" and "claude" in line and str(cached(tmp_path)) in line


def test_a_launcher_not_on_the_path_runs_through_the_shell_with_the_quoted_command(tmp_path):
    shell = write(tmp_path / "fake-shell", FAKE_SHELL)
    shell.chmod(0o755)

    run = run_launch(tmp_path, PROMPT, "--", "claude@meta", "--model", "opus", SHELL=str(shell))

    assert run.returncode == 5
    flag, command = (tmp_path / "shell-argv").read_text().split("\n", 1)
    assert flag == "-ic"
    assert shlex.split(command)[:3] == ["claude@meta", "--model", "opus"]
    assert shlex.split(command)[3:5] == ["--system-prompt-file", str(cached(tmp_path))]
