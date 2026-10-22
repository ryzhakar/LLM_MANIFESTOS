from hashlib import sha256

from helpers import write
from unharness.config import Element
from unharness.resolve import Document, resolve_stack


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
