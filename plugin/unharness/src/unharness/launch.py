"""Write the prompt to the cache and run the launcher with the harness text stripped."""

import json
import os
import shlex
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

from unharness.config import UnharnessError

CACHE_FOLDER = "unharness"
FOLDER_MODE = 0o700
FILE_MODE = 0o600
DEFAULT_LAUNCHER = "claude"
TERMINAL_REDIRECT = "</dev/tty"
STRIP_ENVIRONMENT = {
    "CLAUDE_CODE_ATTRIBUTION_HEADER": "0",
    "CLAUDE_CODE_DISABLE_CLAUDE_MDS": "1",
    "CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS": "1",
    "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
    "CLAUDE_CODE_SILENT_TURN_REMINDER": "0",
    "UNHARNESS": "1",
}
CLAUDE_MD_VARIABLE = "CLAUDE_CODE_DISABLE_CLAUDE_MDS"
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
    reopen_stdin: Callable[[], None],
    execute: Callable[[list[str], dict[str, str]], int],
) -> int:
    """Cache the prompt, then print the launch command, or run the launcher and return its status."""
    if not prompt.strip():
        raise UnharnessError("the prompt is empty")
    prompt_file = _write_prompt(prompt, cache_home)
    assignments = [f"{name}={value}" for name, value in _strip_environment(options).items()]
    arguments = _strip_arguments(prompt_file, options)
    if not options.launcher:
        print(shlex.join(["env", *assignments, DEFAULT_LAUNCHER, *arguments]), TERMINAL_REDIRECT)
        return 0
    reopen_stdin()
    return execute([*options.launcher, *arguments], {**environ, **_strip_environment(options)})


def _strip_environment(options: Options) -> dict[str, str]:
    kept = [CLAUDE_MD_VARIABLE] if options.keep_claude_md else []
    return {name: value for name, value in STRIP_ENVIRONMENT.items() if name not in kept}


def _strip_arguments(prompt_file: Path, options: Options) -> list[str]:
    settings = {**STRIP_SETTINGS, **({"disableAllHooks": True} if options.no_hooks else {})}
    web_search = [] if options.keep_web_search else ["--disallowedTools", "WebSearch"]
    return ["--system-prompt-file", str(prompt_file), *web_search, "--settings", json.dumps(settings, separators=(",", ":"))]


def _write_prompt(prompt: str, cache_home: Path) -> Path:
    folder = cache_home / CACHE_FOLDER
    folder.mkdir(mode=FOLDER_MODE, parents=True, exist_ok=True)
    path = folder / f"{sha256(prompt.encode()).hexdigest()}.md"
    with os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, FILE_MODE), "w") as file:
        file.write(prompt)
    return path
