from pathlib import Path

import pytest

CACHE = Path("plugins") / "cache" / "marketplace"


def write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


@pytest.fixture
def login(tmp_path) -> Path:
    """A fake login folder: two cached versions of two plugins, and one user skill."""
    folder = tmp_path / "login"
    for version in ("3.3.0", "3.4.0"):
        plugin = folder / CACHE / "manifesto" / version
        write(plugin / "manifestos" / "dry.md", f"---\ntitle: Dry\n---\n\n# Dry {version}\n\nRoot is ${{CLAUDE_PLUGIN_ROOT}}.\n")
        write(plugin / "skills" / "manifesto-writing" / "SKILL.md", f"---\nname: manifesto-writing\n---\nWriting {version} at ${{CLAUDE_PLUGIN_ROOT}}/manifestos/raise-the-bar.md\n")
    for version in ("1.9.0", "1.10.0"):
        write(folder / CACHE / "agent-conduct" / version / "skills" / "write-well" / "SKILL.md", f"---\nname: write-well\n---\nWell {version}\n")
    write(folder / "skills" / "my-skill" / "SKILL.md", "---\nname: my-skill\n---\nMine\n")
    return folder
