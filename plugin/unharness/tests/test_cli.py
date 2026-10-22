import subprocess
import sys
from importlib.resources import files
from pathlib import Path

import pytest
from helpers import write
from unharness.compile import compile_prompt, stack_block, stack_view
from unharness.config import load
from unharness.resolve import resolve_stack

CONFIG = "you:\n  - name: dry\n    purpose: one home\n  - name: write-well\n    source: skill agent-conduct:write-well\n"


@pytest.fixture
def project(tmp_path) -> Path:
    folder = tmp_path / "project"
    write(folder / ".manifestos.yaml", CONFIG)
    return folder


def unharness(login: Path, *arguments: str, cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "unharness.cli", *arguments],
        capture_output=True, text=True, cwd=cwd, env={"CLAUDE_CONFIG_DIR": str(login)},
    )


def documents_of(project: Path, login: Path):
    config = load(project / ".manifestos.yaml")
    return resolve_stack(config.you, config.directory, config.manifesto_dir, login)


def test_the_stack_verb_prints_the_stack_block_and_the_constitution_of_the_config(login, project, tmp_path):
    run = unharness(login, "stack", "--config", str(project / ".manifestos.yaml"), cwd=tmp_path)

    assert run.returncode == 0
    assert run.stdout == stack_view(documents_of(project, login)) + "\n"


def write_session_files(project: Path, login: Path) -> None:
    stack = stack_block(documents_of(project, login))
    write(project / ".manifestos.interplay.md", f"{stack}\n\n<interplay>\nAgree.\n</interplay>\n")
    write(project / ".manifestos.commitments.md", f"{stack}\n\n<commitments>\nI must, and I will.\n</commitments>\n")


def test_the_prompt_verb_prints_the_compiled_prompt_with_the_shipped_preamble(login, project, tmp_path):
    write_session_files(project, login)
    documents = documents_of(project, login)
    shipped_preamble = files("unharness").joinpath("preamble.md").read_text()

    run = unharness(login, "prompt", "--config", str(project / ".manifestos.yaml"), cwd=tmp_path)

    assert run.returncode == 0
    assert run.stdout == compile_prompt(
        documents, shipped_preamble,
        (project / ".manifestos.interplay.md").read_text(), (project / ".manifestos.commitments.md").read_text(),
    ) + "\n"
    assert run.stdout.startswith(f"<harness>\n{shipped_preamble.strip()}\n</harness>\n\n<constitution>\n")
    assert run.stdout.endswith("<commitments>\nI must, and I will.\n</commitments>\n")


def test_a_project_preamble_replaces_the_shipped_one(login, project):
    write_session_files(project, login)
    write(project / ".manifestos.preamble.md", "My own preamble.\n")

    run = unharness(login, "prompt", cwd=project)

    assert run.stdout.startswith("<harness>\nMy own preamble.\n</harness>\n")


def test_a_failure_prints_one_line_on_stderr_and_exits_1_with_nothing_on_stdout(login, project):
    run = unharness(login, "prompt", cwd=project)

    assert (run.returncode, run.stdout) == (1, "")
    assert run.stderr == "unharness: .manifestos.interplay.md is missing; run /compile-commitments\n"
