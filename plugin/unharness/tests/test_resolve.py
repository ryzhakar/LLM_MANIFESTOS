from hashlib import sha256

from unharness.config import Element
from unharness.resolve import Document, resolve_stack


def test_a_legacy_name_resolves_to_the_registry_of_the_highest_cached_manifesto_plugin(login, tmp_path):
    plugin_root = login / "plugins" / "cache" / "marketplace" / "manifesto" / "3.4.0"

    documents = resolve_stack([Element("dry", "one home", None)], tmp_path, "", login)

    body = f"# Dry 3.4.0\n\nRoot is {plugin_root}."
    assert documents == [Document("dry", "one home", body, sha256("# Dry 3.4.0\n\nRoot is ${CLAUDE_PLUGIN_ROOT}.".encode()).hexdigest())]
