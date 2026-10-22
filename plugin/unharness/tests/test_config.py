from pathlib import Path

from unharness.config import Config, Element, load


def write_config(folder: Path, text: str) -> Path:
    path = folder / ".manifestos.yaml"
    path.write_text(text)
    return path


def test_a_bare_string_names_a_registry_manifesto(tmp_path):
    config = load(write_config(tmp_path, "you:\n  - dry\n  - name: kiss\n    purpose: the code\n"))

    assert config == Config(
        you=[Element("dry", None, None), Element("kiss", "the code", None)],
        subagents={},
        manifesto_dir="",
        directory=tmp_path,
    )
