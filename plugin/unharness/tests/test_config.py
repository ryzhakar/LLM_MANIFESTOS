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


def test_subagent_roles_and_manifesto_dir_load_beside_the_you_stack(tmp_path):
    config = load(write_config(tmp_path, (
        "manifesto_dir: /plugins/manifesto\n"
        "you:\n  - dry\n"
        "subagents:\n  implementer:\n    - kiss\n    - name: yagni\n  other:\n    - dry\n"
    )))

    assert config.manifesto_dir == "/plugins/manifesto"
    assert config.subagents == {
        "implementer": [Element("kiss", None, None), Element("yagni", None, None)],
        "other": [Element("dry", None, None)],
    }


def test_a_root_list_is_the_you_stack(tmp_path):
    config = load(write_config(tmp_path, "- dry\n- kiss\n"))

    assert [element.name for element in config.you] == ["dry", "kiss"]
    assert config.subagents == {}
    assert config.manifesto_dir == ""
