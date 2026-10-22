from pathlib import Path

import pytest

from unharness.config import Config, Element, UnharnessError, load


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


def test_each_source_type_is_kept_as_written_and_a_file_is_named_by_its_stem(tmp_path):
    config = load(write_config(tmp_path, (
        "you:\n"
        "  - name: write-well\n    source: skill agent-conduct:write-well\n"
        "  - name: mine\n    source: skill my-skill\n"
        "  - name: kiss\n    purpose: the code\n    source: manifesto kiss\n"
        "  - source: file notes/house-rules.md\n"
    )))

    assert config.you == [
        Element("write-well", None, "skill agent-conduct:write-well"),
        Element("mine", None, "skill my-skill"),
        Element("kiss", "the code", "manifesto kiss"),
        Element("house-rules", None, "file notes/house-rules.md"),
    ]


def test_null_items_are_dropped_and_an_empty_file_is_an_empty_stack(tmp_path):
    assert load(write_config(tmp_path, "you:\n  - ~\n  - dry\n  -\n")).you == [Element("dry", None, None)]
    assert load(write_config(tmp_path, "# nothing here\n")) == Config([], {}, "", tmp_path)


def test_an_element_with_no_name_and_no_file_source_stops_the_load(tmp_path):
    path = write_config(tmp_path, "you:\n  - purpose: orphan\n    source: skill a:b\n")

    with pytest.raises(UnharnessError, match=r"element 1 of you has no name"):
        load(path)


def test_trailing_comments_are_not_part_of_a_value(tmp_path):
    config = load(write_config(tmp_path, (
        "manifesto_dir: /plugins/manifesto  # the registry\n"
        "you:  # the stack\n  - name: \"dry\" # knowledge\n    purpose: 'one home' # why\n    source: skill a:b # where\n"
    )))

    assert config.manifesto_dir == "/plugins/manifesto"
    assert config.you == [Element("dry", "one home", "skill a:b")]
