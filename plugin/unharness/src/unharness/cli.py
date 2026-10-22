"""The unharness command: print the compiled prompt, print the stack a session binds to, or launch a session."""

import argparse
import os
import sys
from importlib.resources import files
from pathlib import Path

from unharness.compile import COMMITMENTS_FILE, INTERPLAY_FILE, compile_prompt, stack_view
from unharness.config import UnharnessError, fail, load
from unharness.launch import Options, cache_home, execute_launcher, launch, reopen_terminal
from unharness.resolve import login_dir, resolve_stack

DEFAULT_CONFIG = Path(".manifestos.yaml")
PREAMBLE_OVERRIDE_FILE = ".manifestos.preamble.md"
PROMPT_VERB = "prompt"
STACK_VERB = "stack"
LAUNCH_VERB = "launch"
LAUNCHER_SEPARATOR = "--"


def main(argv: list[str] | None = None) -> int:
    """Run the verb named in argv; print its output, or fail in one line with exit status 1."""
    argv = sys.argv[1:] if argv is None else argv
    argv, launcher = _split_launcher(argv)
    parser = argparse.ArgumentParser(prog="unharness")
    verbs = parser.add_subparsers(dest="verb", required=True)
    for verb in (PROMPT_VERB, STACK_VERB):
        verbs.add_parser(verb).add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    launch_parser = verbs.add_parser(LAUNCH_VERB)
    launch_parser.add_argument("prompt", nargs="?")
    for flag in ("--keep-claude-md", "--keep-web-search", "--no-hooks"):
        launch_parser.add_argument(flag, action="store_true")
    arguments = parser.parse_args(argv)
    try:
        if arguments.verb == LAUNCH_VERB:
            return _launch(arguments, launcher)
        print(_output(arguments.verb, arguments.config, login_dir(os.environ, Path.home())))
    except UnharnessError as error:
        return fail(error)
    return 0


def _split_launcher(argv: list[str]) -> tuple[list[str], list[str]]:
    """Split a launch command line at its first --, into the verb's own arguments and the launcher with its arguments."""
    if argv[:1] != [LAUNCH_VERB] or LAUNCHER_SEPARATOR not in argv:
        return argv, []
    separator = argv.index(LAUNCHER_SEPARATOR)
    return argv[:separator], argv[separator + 1:]


def _launch(arguments: argparse.Namespace, launcher: list[str]) -> int:
    prompt = arguments.prompt if arguments.prompt is not None else sys.stdin.read()
    options = Options(arguments.keep_claude_md, arguments.keep_web_search, arguments.no_hooks, launcher)
    return launch(prompt, options, os.environ, cache_home(os.environ, Path.home()), reopen_terminal, execute_launcher)


def _output(verb: str, config_path: Path, login: Path) -> str:
    config = load(config_path)
    if not config.you:
        raise UnharnessError("the stack is empty")
    documents = resolve_stack(config.you, config.directory, config.manifesto_dir, login)
    if verb == STACK_VERB:
        return stack_view(documents)
    return compile_prompt(
        documents,
        _preamble(config.directory),
        _read_if_present(config.directory / INTERPLAY_FILE),
        _read_if_present(config.directory / COMMITMENTS_FILE),
    )


def _preamble(directory: Path) -> str:
    override = _read_if_present(directory / PREAMBLE_OVERRIDE_FILE)
    return override if override is not None else files("unharness").joinpath("preamble.md").read_text()


def _read_if_present(path: Path) -> str | None:
    return path.read_text() if path.is_file() else None


if __name__ == "__main__":
    sys.exit(main())
