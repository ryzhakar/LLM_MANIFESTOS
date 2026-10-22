"""Read a project's .manifestos.yaml into a Config, with the YAML subset reader the file needs."""

from dataclasses import dataclass
from pathlib import Path

LIST_MARKER = "- "
FILE_SOURCE = "file"
YAML_NULLS = ("", "~", "null")


class UnharnessError(Exception):
    """A failure whose one-line message tells the owner what to fix."""


@dataclass(frozen=True)
class Element:
    name: str
    purpose: str | None
    source: str | None


@dataclass(frozen=True)
class Config:
    you: list[Element]
    subagents: dict[str, list[Element]]
    manifesto_dir: str
    directory: Path


def load(path: Path) -> Config:
    """Read the config file at path into a Config."""
    root = _parse_yaml(path.read_text())
    if isinstance(root, list):
        root = {"you": root}
    root = root or {}
    return Config(
        you=_elements(root.get("you") or [], "you"),
        subagents={
            role: _elements(items or [], f"subagents.{role}") for role, items in (root.get("subagents") or {}).items()
        },
        manifesto_dir=root.get("manifesto_dir") or "",
        directory=path.parent,
    )


def _elements(items: list, list_label: str) -> list[Element]:
    present = [item for item in items if item is not None]
    return [_element(item, f"element {number} of {list_label}") for number, item in enumerate(present, 1)]


def _element(item: str | dict, label: str) -> Element:
    fields = item if isinstance(item, dict) else {"name": item}
    source = fields.get("source")
    name = fields.get("name") or _file_stem(source)
    if not name:
        raise UnharnessError(f"{label} has no name; add name: or a file source")
    return Element(name, fields.get("purpose"), source)


def _file_stem(source: str | None) -> str | None:
    kind, _, reference = (source or "").partition(" ")
    return Path(reference).stem if kind == FILE_SOURCE else None


def _parse_yaml(text: str):
    lines = [line.rstrip() for line in text.split("\n") if line.strip() and not line.lstrip().startswith("#")]
    if not lines:
        return None
    value, _ = _parse_block(lines, 0, _indent(lines[0]))
    return value


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _scalar(text: str) -> str | None:
    text = text.strip()
    if text in YAML_NULLS:
        return None
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        return text[1:-1]
    return text


def _parse_block(lines: list[str], i: int, indent: int):
    if lines[i].lstrip().startswith(LIST_MARKER):
        return _parse_list(lines, i, indent)
    return _parse_mapping(lines, i, indent)


def _parse_list(lines: list[str], i: int, indent: int):
    result = []
    item_indent = indent + len(LIST_MARKER)
    while i < len(lines) and _indent(lines[i]) == indent and lines[i].lstrip().startswith(LIST_MARKER):
        content = lines[i].lstrip()[len(LIST_MARKER):]
        if ":" not in content:
            result.append(_scalar(content))
            i += 1
            continue
        block = [" " * item_indent + content]
        i += 1
        while i < len(lines) and _indent(lines[i]) >= item_indent:
            block.append(lines[i])
            i += 1
        result.append(_parse_block(block, 0, item_indent)[0])
    return result, i


def _parse_mapping(lines: list[str], i: int, indent: int):
    result = {}
    while i < len(lines) and _indent(lines[i]) == indent and not lines[i].lstrip().startswith(LIST_MARKER):
        key, _, rest = lines[i].lstrip().partition(":")
        key = _scalar(key)
        if rest.strip():
            result[key] = _scalar(rest)
            i += 1
        elif i + 1 < len(lines) and _indent(lines[i + 1]) > indent:
            result[key], i = _parse_block(lines, i + 1, _indent(lines[i + 1]))
        else:
            result[key] = None
            i += 1
    return result, i
