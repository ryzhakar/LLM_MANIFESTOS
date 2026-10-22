from hashlib import sha256
from pathlib import Path

import pytest
from helpers import write
from unharness.config import Element, UnharnessError
from unharness.resolve import Document, login_dir, resolve_stack


def test_a_legacy_name_resolves_to_the_registry_of_the_highest_cached_manifesto_plugin(login, tmp_path):
    plugin_root = login / "plugins" / "cache" / "marketplace" / "manifesto" / "3.4.0"

    documents = resolve_stack([Element("dry", "one home", None)], tmp_path, "", login)

    body = f"# Dry 3.4.0\n\nRoot is {plugin_root}."
    assert documents == [Document("dry", "one home", body, sha256("# Dry 3.4.0\n\nRoot is ${CLAUDE_PLUGIN_ROOT}.".encode()).hexdigest())]


def texts(elements, directory, login, manifesto_dir=""):
    return [document.text for document in resolve_stack(elements, directory, manifesto_dir, login)]


def test_a_plugin_skill_resolves_at_the_highest_version_by_number_not_by_text(login, tmp_path):
    elements = [Element("write-well", None, "skill agent-conduct:write-well")]

    assert texts(elements, tmp_path, login) == ["Well 1.10.0"]


def test_a_plugin_skill_gets_its_version_folder_for_the_plugin_root(login, tmp_path):
    version_folder = login / "plugins" / "cache" / "marketplace" / "manifesto" / "3.4.0"
    elements = [Element("manifesto-writing", None, "skill manifesto:manifesto-writing")]

    assert texts(elements, tmp_path, login) == [f"Writing 3.4.0 at {version_folder}/manifestos/raise-the-bar.md"]


def test_a_user_skill_and_a_local_file_resolve_without_a_plugin_root(login, tmp_path):
    write(tmp_path / "notes" / "rules.md", "---\ntitle: Rules\n---\nKeep ${CLAUDE_PLUGIN_ROOT} as written.\n")
    elements = [Element("mine", None, "skill my-skill"), Element("rules", None, "file notes/rules.md")]

    assert texts(elements, tmp_path, login) == ["Mine", "Keep ${CLAUDE_PLUGIN_ROOT} as written."]


def test_the_manifesto_dir_of_the_config_replaces_the_cached_registry_and_names_its_own_root(login, tmp_path):
    write(tmp_path / "plugin" / "manifestos" / "dry.md", "Local dry at ${CLAUDE_PLUGIN_ROOT}\n")
    elements = [Element("dry", None, None), Element("again", None, "manifesto dry")]

    assert texts(elements, tmp_path, login, manifesto_dir="plugin") == [f"Local dry at {tmp_path / 'plugin'}"] * 2


def failure_of(element, directory, login, manifesto_dir=""):
    with pytest.raises(UnharnessError) as failure:
        resolve_stack([element], directory, manifesto_dir, login)
    return str(failure.value)


def test_an_element_that_does_not_resolve_names_itself_and_the_path_it_tried(login, tmp_path):
    version_folder = login / "plugins" / "cache" / "marketplace" / "manifesto" / "3.4.0"

    assert failure_of(Element("nope", None, None), tmp_path, login) == (
        f"element nope did not resolve; tried {version_folder / 'manifestos' / 'nope.md'}"
    )
    assert failure_of(Element("gone", None, "file missing/gone.md"), tmp_path, login) == (
        f"element gone did not resolve; tried {tmp_path / 'missing' / 'gone.md'}"
    )
    assert failure_of(Element("none", None, "skill absent:skill"), tmp_path, login) == (
        f"element none did not resolve; tried {login / 'plugins' / 'cache' / '*' / 'absent' / '*' / 'skills' / 'skill' / 'SKILL.md'}"
    )


def test_an_unknown_source_type_is_refused_with_the_types_that_exist(login, tmp_path):
    assert failure_of(Element("site", None, "https://example.com/x.md"), tmp_path, login) == (
        "element site has source type 'https://example.com/x.md' that is none of manifesto, skill, or file"
    )


def test_the_login_is_claude_config_dir_else_dot_claude_in_home(tmp_path):
    assert login_dir({"CLAUDE_CONFIG_DIR": "/somewhere"}, tmp_path) == Path("/somewhere")
    assert login_dir({}, tmp_path) == tmp_path / ".claude"
