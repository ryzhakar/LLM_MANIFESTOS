import json
import os
import shlex
import stat
from hashlib import sha256
from pathlib import Path

import pytest
from unharness.config import UnharnessError
from unharness.launch import Options, launch

DEFAULT_ENVIRONMENT = [
    "CLAUDE_CODE_ATTRIBUTION_HEADER=0",
    "CLAUDE_CODE_DISABLE_CLAUDE_MDS=1",
    "CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1",
    "CLAUDE_CODE_DISABLE_AUTO_MEMORY=1",
    "CLAUDE_CODE_SILENT_TURN_REMINDER=0",
    "UNHARNESS=1",
]
DEFAULT_SETTINGS = {
    "includeGitInstructions": False,
    "attribution": {"commit": "", "pr": ""},
    "autoMemoryEnabled": False,
    "outputStyle": "default",
}
PROMPT = "You are bound.\n"


def never(*_):
    raise AssertionError("nothing may run")


def cached_prompt(cache_home: Path, prompt: str = PROMPT) -> Path:
    return cache_home / "unharness" / f"{sha256(prompt.encode()).hexdigest()}.md"


def printed_command(options: Options, cache_home: Path, capsys) -> list[str]:
    assert launch(PROMPT, options, {}, cache_home, never, never) == 0
    line = capsys.readouterr().out
    assert line.endswith(" </dev/tty\n") and line.count("\n") == 1
    return shlex.split(line.removesuffix(" </dev/tty\n"))


def test_without_a_launcher_it_prints_the_command_for_claude_and_runs_nothing(tmp_path, capsys):
    command = printed_command(Options(False, False, False, []), tmp_path, capsys)

    settings = json.dumps(DEFAULT_SETTINGS, separators=(",", ":"))
    assert command == [
        "env", *DEFAULT_ENVIRONMENT,
        "claude", "--system-prompt-file", str(cached_prompt(tmp_path)),
        "--disallowedTools", "WebSearch", "--settings", settings,
    ]


def test_the_prompt_is_cached_under_its_sha256_with_a_private_file_and_folder(tmp_path, capsys):
    previous_umask = os.umask(0)
    try:
        launch(PROMPT, Options(False, False, False, []), {}, tmp_path, never, never)
    finally:
        os.umask(previous_umask)

    file = cached_prompt(tmp_path)
    assert file.read_text() == PROMPT
    assert stat.S_IMODE(file.stat().st_mode) == 0o600
    assert stat.S_IMODE(file.parent.stat().st_mode) == 0o700


def test_an_empty_prompt_stops_before_anything_is_written(tmp_path):
    with pytest.raises(UnharnessError, match="^the prompt is empty$"):
        launch(" \n", Options(False, False, False, []), {}, tmp_path, never, never)

    assert list(tmp_path.iterdir()) == []
