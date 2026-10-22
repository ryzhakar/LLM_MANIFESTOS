"""Read a project's .manifestos.yaml into a Config, with the YAML subset reader the file needs."""

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

LIST_MARKER = "- "
MANIFESTO_SOURCE = "manifesto"
SKILL_SOURCE = "skill"
FILE_SOURCE = "file"
CLAUDE_MD = "CLAUDE.md"
ACTIVE_MANIFESTOS_SECTION = re.compile(r"^## Active Manifestos\n(.*?)(?=^## |\Z)", re.M | re.S)
MAPPING_ENTRY = re.compile(r":(?:\s|$)")
YAML_NULLS = ("", "~", "null")
QUOTED_SCALAR = re.compile(r"""^(["'])(.*?)\1(?:\s+#.*)?$""")
TRAILING_COMMENT = re.compile(r"(?:^|\s+)#.*$")


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


def fail(error: UnharnessError) -> int:
    """Print the failure as one line on stderr and return the exit status 1."""
    print(f"unharness: {error}", file=sys.stderr)
    return 1


def main(argv: list[str]) -> int:
    """Print the config at argv's path as JSON for a shell hook, or fail in one line."""
    parser = argparse.ArgumentParser(description="Print a .manifestos.yaml as JSON.")
    parser.add_argument("path", type=Path)
    parser.add_argument("--json", action="store_true", required=True)
    try:
        config = load(parser.parse_args(argv).path)
    except UnharnessError as error:
        return fail(error)
    print(json.dumps({
        "you": [asdict(element) for element in config.you],
        "subagents": {role: [asdict(element) for element in elements] for role, elements in config.subagents.items()},
        "manifesto_dir": config.manifesto_dir,
        "directory": str(config.directory),
    }))
    return 0


def load(path: Path) -> Config:
    """Read the config file at path into a Config."""
    root = parse_yaml(_config_text(path))
    if isinstance(root, list):
        root = {"you": root}
    root = root or {}
    roles = root.get("subagents") or {}
    if not isinstance(roles, dict):
        raise UnharnessError("subagents must be a mapping of role to list of elements")
    return Config(
        you=_elements(root.get("you") or [], "you"),
        subagents={role: _elements(items or [], f"subagents.{role}") for role, items in roles.items()},
        manifesto_dir=root.get("manifesto_dir") or "",
        directory=path.parent,
    )


def _config_text(path: Path) -> str:
    if path.is_file():
        return path.read_text()
    claude_md = path.parent / CLAUDE_MD
    section = ACTIVE_MANIFESTOS_SECTION.search(claude_md.read_text()) if claude_md.is_file() else None
    if not section:
        raise UnharnessError(f"no config: tried {path} and the Active Manifestos section of {claude_md}")
    return section.group(1)


def _elements(items: list, list_label: str) -> list[Element]:
    if not isinstance(items, list):
        raise UnharnessError(f"{list_label} must be a list of elements")
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


def parse_yaml(text: str):
    """Return the structure of block-style YAML text: mappings, lists, and string scalars; None if empty."""
    lines = [line.rstrip() for line in text.split("\n") if line.strip() and not line.lstrip().startswith("#")]
    if not lines:
        return None
    value, _ = _parse_block(lines, 0, _indent(lines[0]))
    return value


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _scalar(text: str) -> str | None:
    text = text.strip()
    quoted = QUOTED_SCALAR.match(text)
    if quoted:
        return quoted.group(2)
    text = TRAILING_COMMENT.sub("", text)
    return None if text in YAML_NULLS else text


def _split_entry(text: str) -> tuple[str, str]:
    entry = MAPPING_ENTRY.search(text)
    return (text[:entry.start()], text[entry.end():]) if entry else (text, "")


def _parse_block(lines: list[str], i: int, indent: int):
    if lines[i].lstrip().startswith(LIST_MARKER):
        return _parse_list(lines, i, indent)
    return _parse_mapping(lines, i, indent)


def _parse_list(lines: list[str], i: int, indent: int):
    result = []
    item_indent = indent + len(LIST_MARKER)
    while i < len(lines) and _indent(lines[i]) == indent and lines[i].lstrip().startswith(LIST_MARKER):
        content = lines[i].lstrip()[len(LIST_MARKER):]
        if not MAPPING_ENTRY.search(content):
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
        key, rest = _split_entry(lines[i].lstrip())
        key = _scalar(key)
        value = _scalar(rest)
        if value is not None:
            result[key] = value
            i += 1
        elif i + 1 < len(lines) and _indent(lines[i + 1]) > indent:
            result[key], i = _parse_block(lines, i + 1, _indent(lines[i + 1]))
        else:
            result[key] = None
            i += 1
    return result, i


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
