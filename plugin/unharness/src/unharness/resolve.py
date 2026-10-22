"""Resolve each config element to the text it contributes, by its explicit source type."""

import re
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

from unharness.config import Element

PLUGIN_ROOT_PLACEHOLDER = "${CLAUDE_PLUGIN_ROOT}"
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
MANIFESTO_PLUGIN = "manifesto"


@dataclass(frozen=True)
class Document:
    name: str
    purpose: str | None
    text: str
    sha256: str


def resolve_stack(elements: list[Element], directory: Path, manifesto_dir: str, login: Path) -> list[Document]:
    """Resolve each element, in order, to its Document; stop at the first that does not resolve."""
    return [_resolve_element(element, directory, manifesto_dir, login) for element in elements]


def _resolve_element(element: Element, directory: Path, manifesto_dir: str, login: Path) -> Document:
    kind, _, reference = (element.source or f"manifesto {element.name}").partition(" ")
    plugin_root: Path | None
    if kind == "skill" and ":" in reference:
        plugin, _, skill = reference.partition(":")
        plugin_root = _highest_version_dir(login, plugin)
        path = plugin_root / "skills" / skill / "SKILL.md"
    elif kind == "skill":
        plugin_root = None
        path = login / "skills" / reference / "SKILL.md"
    elif kind == "file":
        plugin_root = None
        path = directory / reference
    else:
        plugin_root = directory / manifesto_dir if manifesto_dir else _highest_version_dir(login, MANIFESTO_PLUGIN)
        path = plugin_root / "manifestos" / f"{reference}.md"
    body = FRONTMATTER.sub("", path.read_text()).strip()
    return Document(
        element.name,
        element.purpose,
        body.replace(PLUGIN_ROOT_PLACEHOLDER, str(plugin_root)) if plugin_root else body,
        sha256(body.encode()).hexdigest(),
    )


def _highest_version_dir(login: Path, plugin: str) -> Path:
    return max(login.glob(f"plugins/cache/*/{plugin}/*"), key=_version_key)


def _version_key(version_dir: Path) -> tuple[int, ...]:
    return tuple(int(number) for number in re.findall(r"\d+", version_dir.name))
