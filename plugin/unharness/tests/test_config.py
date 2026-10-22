import json
import subprocess
import sys
from pathlib import Path

import pytest

from unharness.config import Config, Element, UnharnessError, load

CONFIG_SCRIPT = Path(__file__).parent.parent / "src" / "unharness" / "config.py"


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


def test_a_config_that_is_not_a_list_of_elements_stops_the_load(tmp_path):
    with pytest.raises(UnharnessError, match=r"you must be a list"):
        load(write_config(tmp_path, "you: [dry, kiss]\n"))
    with pytest.raises(UnharnessError, match=r"subagents.other must be a list"):
        load(write_config(tmp_path, "subagents:\n  other: dry\n"))
    with pytest.raises(UnharnessError, match=r"subagents must be a mapping of role to list"):
        load(write_config(tmp_path, "subagents: dry\n"))


def test_a_colon_in_a_bare_item_stops_the_load_instead_of_dropping_the_element(tmp_path):
    with pytest.raises(UnharnessError, match=r"element 1 of you has no name"):
        load(write_config(tmp_path, "you:\n  - agent-conduct:write-well\n"))


def test_without_a_config_file_the_active_manifestos_section_of_claude_md_is_the_config(tmp_path):
    (tmp_path / "CLAUDE.md").write_text("# Notes\n\n## Active Manifestos\n- dry\n- kiss\n\n## Other\n- yagni\n")

    assert [element.name for element in load(tmp_path / ".manifestos.yaml").you] == ["dry", "kiss"]


def test_a_missing_config_names_every_place_it_looked(tmp_path):
    with pytest.raises(UnharnessError) as failure:
        load(tmp_path / ".manifestos.yaml")

    assert str(failure.value) == (
        f"no config: tried {tmp_path / '.manifestos.yaml'} and the Active Manifestos section of {tmp_path / 'CLAUDE.md'}"
    )


def run_config_script(*arguments: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-I", str(CONFIG_SCRIPT), *arguments], capture_output=True, text=True
    )


def test_a_shell_hook_reads_the_stack_as_json_by_running_the_module_by_path(tmp_path):
    path = write_config(tmp_path, "manifesto_dir: /m\nyou:\n  - dry\nsubagents:\n  other:\n    - name: kiss\n      purpose: p\n")

    run = run_config_script(str(path), "--json")

    assert run.returncode == 0
    assert json.loads(run.stdout) == {
        "you": [{"name": "dry", "purpose": None, "source": None}],
        "subagents": {"other": [{"name": "kiss", "purpose": "p", "source": None}]},
        "manifesto_dir": "/m",
    }


def test_a_script_run_that_fails_prints_one_line_and_exits_1(tmp_path):
    run = run_config_script(str(tmp_path / ".manifestos.yaml"), "--json")

    assert run.returncode == 1
    assert run.stdout == ""
    assert run.stderr.startswith("unharness: no config: tried ")
    assert len(run.stderr.splitlines()) == 1
