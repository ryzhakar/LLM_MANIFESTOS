import json
import os
import pty
import shlex
import stat
from hashlib import sha256
from pathlib import Path

import pytest
from unharness.config import UnharnessError
from unharness.launch import Options, cache_home, launch, reopen_terminal, terminal_device
from unharness.switches import parse_switches, shipped_switches

DEFAULT_ENVIRONMENT = [
    "CLAUDE_CODE_ATTRIBUTION_HEADER=0",
    "CLAUDE_CODE_DISABLE_CLAUDE_MDS=1",
    "CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1",
    "CLAUDE_CODE_DISABLE_AUTO_MEMORY=1",
    "CLAUDE_CODE_SILENT_TURN_REMINDER=0",
    "CLAUDE_CODE_TODO_REMINDER_MODE=off",
    "CLAUDE_CODE_TOTAL_TOKENS_REMINDER=off",
    "UNHARNESS=1",
]
DEFAULT_SETTINGS = {
    "includeGitInstructions": False,
    "attribution": {"commit": "", "pr": ""},
    "autoMemoryEnabled": False,
    "outputStyle": "default",
}
PROMPT = "You are bound.\n"
TERMINAL = "/dev/ttys042"
COMMAND_OF_3_6_1 = (
    "env CLAUDE_CODE_ATTRIBUTION_HEADER=0 CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1"
    " CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 CLAUDE_CODE_SILENT_TURN_REMINDER=0 CLAUDE_CODE_TODO_REMINDER_MODE=off"
    " CLAUDE_CODE_TOTAL_TOKENS_REMINDER=off UNHARNESS=1 claude --system-prompt-file {prompt_file}"
    " --disallowedTools WebSearch --settings"
    " '{{\"includeGitInstructions\":false,\"attribution\":{{\"commit\":\"\",\"pr\":\"\"}},"
    "\"autoMemoryEnabled\":false,\"outputStyle\":\"default\"{hooks}}}' <{terminal}\n"
)


def never(*_):
    raise AssertionError("nothing may run")


def cached_prompt(cache_home: Path, prompt: str = PROMPT) -> Path:
    return cache_home / "unharness" / f"{sha256(prompt.encode()).hexdigest()}.md"


def printed_command(options: Options, cache_home: Path, capsys) -> list[str]:
    assert launch(PROMPT, options, shipped_switches(), {}, cache_home, TERMINAL, never, never) == 0
    line = capsys.readouterr().out
    assert line.endswith(f" <{TERMINAL}\n") and line.count("\n") == 1
    return shlex.split(line.removesuffix(f" <{TERMINAL}\n"))


def test_without_a_launcher_it_prints_the_command_for_claude_and_runs_nothing(tmp_path, capsys):
    command = printed_command(Options(False, False, False, []), tmp_path, capsys)

    settings = json.dumps(DEFAULT_SETTINGS, separators=(",", ":"))
    assert command == [
        "env", *DEFAULT_ENVIRONMENT,
        "claude", "--system-prompt-file", str(cached_prompt(tmp_path)),
        "--disallowedTools", "WebSearch", "--settings", settings,
    ]


def test_the_prompt_is_cached_under_its_sha256_with_a_private_file_and_folder(tmp_path):
    previous_umask = os.umask(0)
    try:
        launch(PROMPT, Options(False, False, False, []), shipped_switches(), {}, tmp_path, TERMINAL, never, never)
    finally:
        os.umask(previous_umask)

    file = cached_prompt(tmp_path)
    assert file.read_text() == PROMPT
    assert stat.S_IMODE(file.stat().st_mode) == 0o600
    assert stat.S_IMODE(file.parent.stat().st_mode) == 0o700


def test_an_empty_prompt_stops_before_anything_is_written(tmp_path):
    with pytest.raises(UnharnessError, match="^the prompt is empty$"):
        launch(" \n", Options(False, False, False, []), shipped_switches(), {}, tmp_path, TERMINAL, never, never)

    assert list(tmp_path.iterdir()) == []


def settings_of(command: list[str]) -> dict:
    return json.loads(command[command.index("--settings") + 1])


def test_keep_claude_md_omits_only_the_claude_md_variable(tmp_path, capsys):
    command = printed_command(Options(True, False, False, []), tmp_path, capsys)

    assert command[1:command.index("claude")] == [name for name in DEFAULT_ENVIRONMENT if "CLAUDE_MDS" not in name]


def test_keep_web_search_drops_the_disallow(tmp_path, capsys):
    command = printed_command(Options(False, True, False, []), tmp_path, capsys)

    assert "--disallowedTools" not in command and "WebSearch" not in command


def test_no_hooks_adds_disable_all_hooks_to_the_settings(tmp_path, capsys):
    command = printed_command(Options(False, False, True, []), tmp_path, capsys)

    assert settings_of(command) == {**DEFAULT_SETTINGS, "disableAllHooks": True}


def test_all_three_flags_combine(tmp_path, capsys):
    command = printed_command(Options(True, True, True, []), tmp_path, capsys)

    assert command == [
        "env", *[name for name in DEFAULT_ENVIRONMENT if "CLAUDE_MDS" not in name],
        "claude", "--system-prompt-file", str(cached_prompt(tmp_path)),
        "--settings", json.dumps({**DEFAULT_SETTINGS, "disableAllHooks": True}, separators=(",", ":")),
    ]


def test_with_a_launcher_it_reopens_stdin_then_executes_the_launcher_with_the_stripped_environment(tmp_path, capsys):
    calls = []
    status = launch(
        PROMPT, Options(False, False, False, ["fake", "extra"]), shipped_switches(), {"KEPT": "yes"}, tmp_path, TERMINAL,
        lambda device: calls.append(("reopen", device)),
        lambda argv, env: calls.append((argv, env)) or 7,
    )

    assert status == 7
    assert capsys.readouterr().out == ""
    assert calls[0] == ("reopen", TERMINAL)
    argv, env = calls[1]
    assert argv == [
        "fake", "extra", "--system-prompt-file", str(cached_prompt(tmp_path)),
        "--disallowedTools", "WebSearch", "--settings", json.dumps(DEFAULT_SETTINGS, separators=(",", ":")),
    ]
    assert env == {"KEPT": "yes", **dict(pair.split("=") for pair in DEFAULT_ENVIRONMENT)}


def test_stdin_is_redirected_onto_the_device_it_is_given(tmp_path):
    opened, redirects = [], []
    terminal = tmp_path / "terminal"
    terminal.write_text("")

    def open_device(device):
        opened.append(device)
        return terminal.open()

    reopen_terminal(TERMINAL, lambda: False, open_device, lambda source, target: redirects.append((type(source), target)))

    assert (opened, redirects) == ([TERMINAL], [(int, 0)])


def test_without_a_terminal_stdin_stays_as_it_is():
    def no_terminal(device):
        raise OSError("no controlling terminal")

    reopen_terminal(TERMINAL, lambda: False, no_terminal, lambda *_: pytest.fail("stdin must not move"))


def test_stdin_that_is_already_a_terminal_is_left_alone():
    def must_not_open(device):
        raise AssertionError("the terminal must not be opened")

    reopen_terminal(TERMINAL, lambda: True, must_not_open, lambda *_: pytest.fail("stdin must not move"))


@pytest.fixture
def pseudo_terminal():
    master, slave = pty.openpty()
    read_end, write_end = os.pipe()
    yield slave, write_end
    for descriptor in (master, slave, read_end, write_end):
        os.close(descriptor)


def test_the_device_is_the_one_stdout_is_on(pseudo_terminal):
    terminal, pipe = pseudo_terminal

    assert terminal_device((terminal, pipe)) == os.ttyname(terminal)


def test_the_device_is_the_one_stderr_is_on_when_stdout_is_not_a_terminal(pseudo_terminal):
    terminal, pipe = pseudo_terminal

    assert terminal_device((pipe, terminal)) == os.ttyname(terminal)


def test_the_device_is_dev_tty_when_neither_output_is_a_terminal(pseudo_terminal):
    _, pipe = pseudo_terminal

    assert terminal_device((pipe, pipe)) == "/dev/tty"


def test_the_cache_is_dot_cache_in_home_unless_xdg_cache_home_is_set_and_not_empty(tmp_path):
    assert cache_home({}, tmp_path) == tmp_path / ".cache"
    assert cache_home({"XDG_CACHE_HOME": ""}, tmp_path) == tmp_path / ".cache"
    assert cache_home({"XDG_CACHE_HOME": "/elsewhere"}, tmp_path) == Path("/elsewhere")


@pytest.mark.parametrize(("options", "hooks"), [
    (Options(False, False, False, []), ""),
    (Options(False, False, True, []), ',"disableAllHooks":true'),
])
def test_the_printed_command_equals_the_one_3_6_1_printed(options, hooks, tmp_path, capsys):
    assert launch(PROMPT, options, shipped_switches(), {}, tmp_path, TERMINAL, never, never) == 0

    expected = COMMAND_OF_3_6_1.format(prompt_file=cached_prompt(tmp_path), hooks=hooks, terminal=TERMINAL)
    assert capsys.readouterr().out == expected


def entry(**overrides) -> dict:
    return {
        "name": "SWITCH_ONE", "kind": "env", "value": "1", "removes": "Some text",
        "documented": True, "control": True, "verified": ["2.1.309"], "default": True, "option": None,
        **overrides,
    }


def printed_command_of(entries: list[dict], options: Options, tmp_path, capsys) -> list[str]:
    launch(PROMPT, options, parse_switches(json.dumps(entries)), {}, tmp_path, TERMINAL, never, never)
    return shlex.split(capsys.readouterr().out.removesuffix(f" <{TERMINAL}\n"))


def test_launch_composes_env_flags_and_settings_from_the_registry_in_its_order(tmp_path, capsys):
    command = printed_command_of([
        entry(name="FIRST", value="a"),
        entry(name="--bare", kind="flag", value=None, removes="Second"),
        entry(name="key", kind="settings", value={"nested": [1]}, removes="Third"),
        entry(name="--valued", kind="flag", value="v", removes="Fourth"),
        entry(name="SECOND", value="b", removes="Fifth"),
        entry(name="other", kind="settings", value=False, removes="Sixth"),
    ], Options(False, False, False, []), tmp_path, capsys)

    assert command == [
        "env", "FIRST=a", "SECOND=b", "UNHARNESS=1",
        "claude", "--system-prompt-file", str(cached_prompt(tmp_path)),
        "--bare", "--valued", "v", "--settings", '{"key":{"nested":[1]},"other":false}',
    ]


def test_launch_leaves_out_settings_when_no_settings_entry_passes(tmp_path, capsys):
    command = printed_command_of([entry()], Options(False, False, False, []), tmp_path, capsys)

    assert "--settings" not in command


def test_an_option_inverts_the_default_of_the_entry_it_names(tmp_path, capsys):
    entries = [
        entry(name="STRIPPED", option="--keep-claude-md"),
        entry(name="KEPT", removes="Other", default=False, option="--keep-web-search"),
        entry(name="UNNAMED", removes="Third", default=False),
    ]

    plain = printed_command_of(entries, Options(False, False, False, []), tmp_path, capsys)
    inverted = printed_command_of(entries, Options(True, True, False, []), tmp_path, capsys)

    assert plain[1:-3] == ["STRIPPED=1", "UNHARNESS=1"]
    assert inverted[1:-3] == ["KEPT=1", "UNHARNESS=1"]


def test_launch_passes_only_the_entries_verified_at_the_newest_registry_version(tmp_path, capsys):
    command = printed_command_of([
        entry(name="OLD", verified=["2.1.300"]),
        entry(name="CURRENT", removes="Other", verified=["2.1.300", "2.1.309"]),
    ], Options(False, False, False, []), tmp_path, capsys)

    assert command[1:-3] == ["CURRENT=1", "UNHARNESS=1"]
