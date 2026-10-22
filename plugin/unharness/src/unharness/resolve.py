"""Resolve each config element to the text it contributes, by its explicit source type."""

import re
from collections.abc import Mapping
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

from unharness.config import FILE_SOURCE, MANIFESTO_SOURCE, SKILL_SOURCE, Element, UnharnessError

PLUGIN_ROOT_PLACEHOLDER = "${CLAUDE_PLUGIN_ROOT}"
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
LOGIN_VARIABLE = "CLAUDE_CONFIG_DIR"
MANIFESTO_PLUGIN = "manifesto"
PLUGIN_SKILL_SEPARATOR = ":"


@dataclass(frozen=True)
class Document:
    name: str
    purpose: str | None
    text: str
    sha256: str


def login_dir(environ: Mapping[str, str], home: Path) -> Path:
    """Return the login folder: CLAUDE_CONFIG_DIR, else .claude in the home folder."""
    return Path(environ[LOGIN_VARIABLE]) if LOGIN_VARIABLE in environ else home / ".claude"


def resolve_stack(elements: list[Element], directory: Path, manifesto_dir: str, login: Path) -> list[Document]:
    """Resolve each element, in order, to its Document; stop at the first that does not resolve."""
    return [_resolve_element(element, directory, manifesto_dir, login) for element in elements]


def _resolve_element(element: Element, directory: Path, manifesto_dir: str, login: Path) -> Document:
    path, plugin_root = _locate(element, directory, manifesto_dir, login)
    if not path.is_file():
        raise UnharnessError(f"element {element.name} did not resolve; tried {path}")
    body = FRONTMATTER.sub("", path.read_text()).strip()
    return Document(
        element.name,
        element.purpose,
        body.replace(PLUGIN_ROOT_PLACEHOLDER, str(plugin_root)) if plugin_root else body,
        sha256(body.encode()).hexdigest(),
    )


def _locate(element: Element, directory: Path, manifesto_dir: str, login: Path) -> tuple[Path, Path | None]:
    """Return the file the element names, and the plugin folder that ${CLAUDE_PLUGIN_ROOT} stands for, if any."""
    kind, _, reference = (element.source or f"manifesto {element.name}").partition(" ")
    if kind == MANIFESTO_SOURCE:
        plugin_root = directory / manifesto_dir if manifesto_dir else _highest_version_dir(login, MANIFESTO_PLUGIN)
        return plugin_root / "manifestos" / f"{reference}.md", plugin_root
    if kind == SKILL_SOURCE and PLUGIN_SKILL_SEPARATOR in reference:
        plugin, _, skill = reference.partition(PLUGIN_SKILL_SEPARATOR)
        plugin_root = _highest_version_dir(login, plugin)
        return plugin_root / "skills" / skill / "SKILL.md", plugin_root
    if kind == SKILL_SOURCE:
        return login / "skills" / reference / "SKILL.md", None
    if kind == FILE_SOURCE:
        return directory / reference, None
    raise UnharnessError(
        f"element {element.name} has source type '{kind}' that is none of {MANIFESTO_SOURCE}, {SKILL_SOURCE}, or {FILE_SOURCE}"
    )


def _highest_version_dir(login: Path, plugin: str) -> Path:
    """Return the plugin's highest cached version folder, or the pattern that matched none."""
    pattern = f"plugins/cache/*/{plugin}/*"
    return max(login.glob(pattern), key=_version_key, default=login / pattern)


def _version_key(version_dir: Path) -> tuple[int, ...]:
    return tuple(int(number) for number in re.findall(r"\d+", version_dir.name))
