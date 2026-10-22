"""The unharness command: print the compiled prompt or the stack a session binds to."""

import argparse
import os
import sys
from importlib.resources import files
from pathlib import Path

from unharness.compile import COMMITMENTS_FILE, INTERPLAY_FILE, compile_prompt, stack_view
from unharness.config import UnharnessError, fail, load
from unharness.resolve import login_dir, resolve_stack

DEFAULT_CONFIG = Path(".manifestos.yaml")
PREAMBLE_OVERRIDE_FILE = ".manifestos.preamble.md"
PROMPT_VERB = "prompt"
STACK_VERB = "stack"


def main(argv: list[str] | None = None) -> int:
    """Run the verb named in argv; print its output, or fail in one line with exit status 1."""
    parser = argparse.ArgumentParser(prog="unharness")
    verbs = parser.add_subparsers(dest="verb", required=True)
    for verb in (PROMPT_VERB, STACK_VERB):
        verbs.add_parser(verb).add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    arguments = parser.parse_args(argv)
    try:
        print(_output(arguments.verb, arguments.config, login_dir(os.environ, Path.home())))
    except UnharnessError as error:
        return fail(error)
    return 0


def _output(verb: str, config_path: Path, login: Path) -> str:
    config = load(config_path)
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
