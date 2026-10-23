"""Write the prompt to the cache and run the launcher with the harness text stripped."""

import json
import os
import shlex
import shutil
import subprocess
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import IO

from unharness.config import TEXT_ENCODING, UnharnessError
from unharness.switches import Switch, version_key

CACHE_FOLDER = "unharness"
CACHE_VARIABLE = "XDG_CACHE_HOME"
DEFAULT_SHELL = "/bin/sh"
FOLDER_MODE = 0o700
FILE_MODE = 0o600
DEFAULT_LAUNCHER = "claude"
CONTROLLING_TERMINAL = "/dev/tty"
STDIN_DESCRIPTOR = 0
OUTPUT_DESCRIPTORS = (1, 2)
STAND_DOWN_MARKER = {"UNHARNESS": "1"}
SYSTEM_PROMPT_FLAG = "--system-prompt-file"
SETTINGS_FLAG = "--settings"
OPTION_ATTRIBUTES = {"--keep-claude-md": "keep_claude_md", "--keep-web-search": "keep_web_search", "--no-hooks": "no_hooks"}


@dataclass(frozen=True)
class Options:
    keep_claude_md: bool
    keep_web_search: bool
    no_hooks: bool
    launcher: list[str]


def launch(
    prompt: str,
    options: Options,
    switches: Sequence[Switch],
    environ: Mapping[str, str],
    cache_home: Path,
    terminal: str,
    reopen_stdin: Callable[[str], None],
    execute: Callable[[list[str], dict[str, str]], int],
) -> int:
    """Cache the prompt, then print the launch command, or run the launcher and return its status."""
    if not prompt.strip():
        raise UnharnessError("the prompt is empty")
    prompt_file = _write_prompt(prompt, cache_home)
    passed = _passed_switches(switches, options)
    variables = _strip_environment(passed)
    arguments = _strip_arguments(prompt_file, passed)
    assignments = [f"{name}={value}" for name, value in variables.items()]
    if not options.launcher:
        print(shlex.join(["env", *assignments, DEFAULT_LAUNCHER, *arguments]), f"<{terminal}")
        return 0
    reopen_stdin(terminal)
    return execute([*options.launcher, *arguments], {**environ, **variables})


def cache_home(environ: Mapping[str, str], home: Path) -> Path:
    """Return XDG_CACHE_HOME, else .cache in the home folder."""
    return Path(environ[CACHE_VARIABLE]) if environ.get(CACHE_VARIABLE) else home / ".cache"


def execute_launcher(argv: list[str], env: dict[str, str]) -> int:
    """Replace this process with the launcher when it is on PATH; else run it through the interactive shell."""
    if shutil.which(argv[0], path=env.get("PATH")):
        os.execvpe(argv[0], argv, env)
    return subprocess.run([env.get("SHELL", DEFAULT_SHELL), "-ic", shlex.join(argv)], env=env).returncode


def terminal_device(descriptors: tuple[int, ...] = OUTPUT_DESCRIPTORS) -> str:
    """Return the device of the first descriptor that is a terminal, else the controlling terminal, /dev/tty."""
    for descriptor in descriptors:
        try:
            return os.ttyname(descriptor)
        except OSError:
            continue
    return CONTROLLING_TERMINAL


def reopen_terminal(
    device: str,
    stdin_is_terminal: Callable[[], bool] = lambda: os.isatty(STDIN_DESCRIPTOR),
    open_terminal: Callable[[str], IO] = open,
    redirect: Callable[[int, int], None] = os.dup2,
) -> None:
    """Point stdin at the device, so an interactive session survives a piped prompt; keep stdin if it is a terminal or the device will not open."""
    if stdin_is_terminal():
        return
    try:
        with open_terminal(device) as terminal:
            redirect(terminal.fileno(), STDIN_DESCRIPTOR)
    except OSError:
        pass


def _passed_switches(switches: Sequence[Switch], options: Options) -> list[Switch]:
    """Return the switches verified at the newest registry version whose default, inverted by its given option, is true."""
    newest = max((version for switch in switches for version in switch.verified), key=version_key, default=None)
    return [switch for switch in switches if newest in switch.verified and switch.default != _option_given(switch, options)]


def _option_given(switch: Switch, options: Options) -> bool:
    return switch.option is not None and getattr(options, OPTION_ATTRIBUTES[switch.option])


def _strip_environment(passed: Sequence[Switch]) -> dict[str, str]:
    return {**{switch.name: switch.value for switch in passed if switch.kind == "env"}, **STAND_DOWN_MARKER}


def _strip_arguments(prompt_file: Path, passed: Sequence[Switch]) -> list[str]:
    flags = [word for switch in passed if switch.kind == "flag" for word in _flag_words(switch)]
    settings = {switch.name: switch.value for switch in passed if switch.kind == "settings"}
    settings_words = [SETTINGS_FLAG, json.dumps(settings, separators=(",", ":"))] if settings else []
    return [SYSTEM_PROMPT_FLAG, str(prompt_file), *flags, *settings_words]


def _flag_words(switch: Switch) -> list[str]:
    return [switch.name] if switch.value is None else [switch.name, switch.value]


def _write_prompt(prompt: str, cache_home: Path) -> Path:
    folder = cache_home / CACHE_FOLDER
    folder.mkdir(mode=FOLDER_MODE, parents=True, exist_ok=True)
    path = folder / f"{sha256(prompt.encode()).hexdigest()}.md"
    with os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, FILE_MODE), "w", encoding=TEXT_ENCODING) as file:
        file.write(prompt)
    return path
