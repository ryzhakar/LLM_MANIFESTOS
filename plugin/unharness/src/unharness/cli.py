"""The unharness command: print the compiled prompt, print the stack a session binds to, or launch a session."""

import argparse
import os
import sys
from pathlib import Path

from unharness.compile import FULL_FILES, MINIFIED_FILES, compile_prompt, stack_view
from unharness.config import EMPTY_STACK_MESSAGE, UnharnessError, fail, load
from unharness.digests import DIGESTS_FLAG, OVERLAP_FLAG, STACK_DIGESTS_FLAG, constitution_blocks, digest_mode, stamp_digest
from unharness.doctor import Modes, claude_version, doctor, has_failed
from unharness.launch import Options, cache_home, execute_launcher, launch, reopen_terminal, terminal_device
from unharness.resolve import login_dir, manifesto_elements, manifesto_plugin_dir, resolve_stack
from unharness.session import load_preamble, read_if_present

DEFAULT_CONFIG = Path(".manifestos.yaml")
PROMPT_VERB = "prompt"
STACK_VERB = "stack"
STAMP_VERB = "stamp"
LAUNCH_VERB = "launch"
DOCTOR_VERB = "doctor"
MINIFIED_FLAG = "--minified"
MODE_FLAGS = (DIGESTS_FLAG, STACK_DIGESTS_FLAG, OVERLAP_FLAG, MINIFIED_FLAG)
LAUNCHER_SEPARATOR = "--"


def main(argv: list[str] | None = None) -> int:
    """Run the verb named in argv; print its output, or fail in one line with exit status 1."""
    argv = sys.argv[1:] if argv is None else argv
    argv, launcher = _split_launcher(argv)
    parser = argparse.ArgumentParser(prog="unharness")
    verbs = parser.add_subparsers(dest="verb", required=True)
    prompt_parser = verbs.add_parser(PROMPT_VERB)
    stack_parser = verbs.add_parser(STACK_VERB)
    stack_parser.add_argument("slugs", nargs="*")
    for parser_of_verb in (prompt_parser, stack_parser):
        parser_of_verb.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    for flag in MODE_FLAGS:
        prompt_parser.add_argument(flag, action="store_true")
    stamp_parser = verbs.add_parser(STAMP_VERB)
    stamp_parser.add_argument("digest", type=Path)
    stamp_parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    launch_parser = verbs.add_parser(LAUNCH_VERB)
    launch_parser.add_argument("prompt", nargs="?")
    for flag in ("--keep-claude-md", "--keep-web-search", "--no-hooks"):
        launch_parser.add_argument(flag, action="store_true")
    doctor_parser = verbs.add_parser(DOCTOR_VERB)
    doctor_parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    for flag in MODE_FLAGS:
        doctor_parser.add_argument(flag, action="store_true")
    arguments = parser.parse_args(argv)
    try:
        if arguments.verb == LAUNCH_VERB:
            return _launch(arguments, launcher)
        if arguments.verb == DOCTOR_VERB:
            return _doctor(arguments)
        login = login_dir(os.environ, Path.home())
        print(_stamp(arguments, login) if arguments.verb == STAMP_VERB else _output(arguments, login))
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
    if arguments.prompt is None and sys.stdin.isatty():
        raise UnharnessError("no prompt: pass PROMPT or pipe unharness prompt")
    prompt = arguments.prompt if arguments.prompt is not None else sys.stdin.read()
    options = Options(arguments.keep_claude_md, arguments.keep_web_search, arguments.no_hooks, launcher)
    return launch(prompt, options, os.environ, cache_home(os.environ, Path.home()), terminal_device(), reopen_terminal, execute_launcher)


def _stamp(arguments: argparse.Namespace, login: Path) -> str:
    index = stamp_digest(arguments.digest, load(arguments.config).registry, login)
    return f"stamped {arguments.digest.stem} in {index}"


def _doctor(arguments: argparse.Namespace) -> int:
    modes = Modes(arguments.digests, arguments.stack_digests, arguments.overlap, arguments.minified)
    findings = doctor(arguments.config, modes, login_dir(os.environ, Path.home()), os.environ, claude_version)
    print("\n".join(finding.line for finding in findings))
    return 1 if has_failed(findings) else 0


def _output(arguments: argparse.Namespace, login: Path) -> str:
    verb = arguments.verb
    config = load(arguments.config)
    if verb == STACK_VERB and arguments.slugs:
        return stack_view(resolve_stack(manifesto_elements(arguments.slugs), config.directory, config.registry, login))
    if not config.you:
        raise UnharnessError(EMPTY_STACK_MESSAGE)
    documents = resolve_stack(config.you, config.directory, config.registry, login)
    if verb == STACK_VERB:
        return stack_view(documents)
    mode = digest_mode(arguments.digests, arguments.stack_digests, arguments.overlap)
    session_files = MINIFIED_FILES if arguments.minified else FULL_FILES
    return compile_prompt(
        documents,
        load_preamble(config.directory).text,
        read_if_present(config.directory / session_files.interplay),
        read_if_present(config.directory / session_files.commitments),
        constitution_blocks(config.you, documents, config.directory, manifesto_plugin_dir(config.registry, login), mode),
        session_files,
    )


if __name__ == "__main__":
    sys.exit(main())
