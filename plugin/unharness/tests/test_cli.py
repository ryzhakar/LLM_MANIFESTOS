import subprocess
import sys
from importlib.resources import files
from pathlib import Path

import pytest
from helpers import write
from unharness.compile import stack_view
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
