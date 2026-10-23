"""Write the prompt to the cache and run the launcher with the harness text stripped."""

import json
import os
import shlex
import shutil
import subprocess
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import IO

from unharness.config import TEXT_ENCODING, UnharnessError

CACHE_FOLDER = "unharness"
CACHE_VARIABLE = "XDG_CACHE_HOME"
DEFAULT_SHELL = "/bin/sh"
FOLDER_MODE = 0o700
FILE_MODE = 0o600
DEFAULT_LAUNCHER = "claude"
CONTROLLING_TERMINAL = "/dev/tty"
STDIN_DESCRIPTOR = 0
OUTPUT_DESCRIPTORS = (1, 2)
CLAUDE_MD_VARIABLE = "CLAUDE_CODE_DISABLE_CLAUDE_MDS"
STRIP_ENVIRONMENT = {
    "CLAUDE_CODE_ATTRIBUTION_HEADER": "0",
    CLAUDE_MD_VARIABLE: "1",
    "CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS": "1",
    "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
    "CLAUDE_CODE_SILENT_TURN_REMINDER": "0",
    "CLAUDE_CODE_TODO_REMINDER_MODE": "off",
    "CLAUDE_CODE_TOTAL_TOKENS_REMINDER": "off",
}
STAND_DOWN_MARKER = {"UNHARNESS": "1"}
STRIP_SETTINGS = {
    "includeGitInstructions": False,
    "attribution": {"commit": "", "pr": ""},
    "autoMemoryEnabled": False,
    "outputStyle": "default",
}


@dataclass(frozen=True)
class Options:
    keep_claude_md: bool
    keep_web_search: bool
    no_hooks: bool
    launcher: list[str]


def launch(
    prompt: str,
    options: Options,
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
    assignments = [f"{name}={value}" for name, value in _strip_environment(options).items()]
    arguments = _strip_arguments(prompt_file, options)
    if not options.launcher:
        print(shlex.join(["env", *assignments, DEFAULT_LAUNCHER, *arguments]), f"<{terminal}")
        return 0
    reopen_stdin(terminal)
    return execute([*options.launcher, *arguments], {**environ, **_strip_environment(options)})


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


def _strip_environment(options: Options) -> dict[str, str]:
    kept = [CLAUDE_MD_VARIABLE] if options.keep_claude_md else []
    return {**{name: value for name, value in STRIP_ENVIRONMENT.items() if name not in kept}, **STAND_DOWN_MARKER}


def _strip_arguments(prompt_file: Path, options: Options) -> list[str]:
    settings = {**STRIP_SETTINGS, **({"disableAllHooks": True} if options.no_hooks else {})}
    web_search = [] if options.keep_web_search else ["--disallowedTools", "WebSearch"]
    return ["--system-prompt-file", str(prompt_file), *web_search, "--settings", json.dumps(settings, separators=(",", ":"))]


def _write_prompt(prompt: str, cache_home: Path) -> Path:
    folder = cache_home / CACHE_FOLDER
    folder.mkdir(mode=FOLDER_MODE, parents=True, exist_ok=True)
    path = folder / f"{sha256(prompt.encode()).hexdigest()}.md"
    with os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, FILE_MODE), "w", encoding=TEXT_ENCODING) as file:
        file.write(prompt)
    return path
