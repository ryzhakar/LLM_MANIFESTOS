"""Load the switch registry, the one home of every switch launch passes, and print its strip table."""

import json
import re
from dataclasses import dataclass
from importlib.resources import files
from typing import Any

from unharness.config import TEXT_ENCODING, UnharnessError

REGISTRY_FILE = "switches.json"
KINDS = ("env", "flag", "settings")
OPTIONS = ("--keep-claude-md", "--keep-web-search", "--no-hooks")
KEYS = ("name", "kind", "value", "removes", "documented", "control", "verified", "default", "option")
BOOLEAN_KEYS = ("documented", "control", "default")
SHARED_ROW_KEYS = ("control", "default", "option")
VERSION_PATTERN = re.compile(r"\d+\.\d+\.\d+")
VERSIONS_PROBLEM = "must be a non-empty array of distinct X.Y.Z strings in ascending order"


@dataclass(frozen=True)
class Switch:
    name: str
    kind: str
    value: Any
    removes: str
    documented: bool
    control: bool
    verified: tuple[str, ...]
    default: bool
    option: str | None


def shipped_switches() -> list[Switch]:
    """Return the registry unharness ships, refused when it breaks the schema."""
    return parse_switches(files("unharness").joinpath(REGISTRY_FILE).read_text(encoding=TEXT_ENCODING))


def parse_switches(text: str) -> list[Switch]:
    """Return the entries of a registry text in order, refusing a text that breaks the schema."""
    try:
        entries = json.loads(text)
    except json.JSONDecodeError as error:
        raise UnharnessError(f"{REGISTRY_FILE} is not JSON: {error}") from error
    if not isinstance(entries, list):
        raise UnharnessError(f"{REGISTRY_FILE} is not one JSON array")
    switches = [_switch(index, entry) for index, entry in enumerate(entries)]
    _refuse_repeats(switches)
    return switches


def version_key(version: str) -> tuple[int, ...]:
    """Return the version's numbers, so versions compare as numbers and not as text."""
    return tuple(int(part) for part in version.split("."))


def _switch(index: int, entry: Any) -> Switch:
    if not isinstance(entry, dict):
        raise _refusal(index, "is not an object")
    for key in KEYS:
        if key not in entry:
            raise _refusal(index, f"{key} is missing")
    for key in entry:
        if key not in KEYS:
            raise _refusal(index, f"{key} is not a key of an entry")
    if entry["kind"] not in KINDS:
        raise _refusal(index, 'kind must be "env", "flag", or "settings"')
    return Switch(
        name=_text(index, entry, "name"),
        kind=entry["kind"],
        value=_value(index, entry),
        removes=_text(index, entry, "removes"),
        documented=_boolean(index, entry, "documented"),
        control=_boolean(index, entry, "control"),
        verified=_versions(index, entry["verified"]),
        default=_boolean(index, entry, "default"),
        option=_option(index, entry["option"]),
    )


def _refusal(index: int, problem: str) -> UnharnessError:
    return UnharnessError(f"{REGISTRY_FILE} entry {index}: {problem}")


def _text(index: int, entry: dict, key: str) -> str:
    if not isinstance(entry[key], str) or not entry[key]:
        raise _refusal(index, f"{key} must be a non-empty string")
    return entry[key]


def _boolean(index: int, entry: dict, key: str) -> bool:
    if not isinstance(entry[key], bool):
        raise _refusal(index, f"{key} must be true or false")
    return entry[key]


def _value(index: int, entry: dict) -> Any:
    value, kind = entry["value"], entry["kind"]
    if kind == "env" and not isinstance(value, str):
        raise _refusal(index, "value must be a string")
    if kind == "flag" and not (isinstance(value, str) or value is None):
        raise _refusal(index, "value must be a string or null")
    return value


def _option(index: int, option: Any) -> str | None:
    if option is not None and option not in OPTIONS:
        raise _refusal(index, 'option must be null, "--keep-claude-md", "--keep-web-search", or "--no-hooks"')
    return option


def _versions(index: int, versions: Any) -> tuple[str, ...]:
    well_formed = isinstance(versions, list) and bool(versions) and all(
        isinstance(version, str) and VERSION_PATTERN.fullmatch(version) for version in versions
    )
    if not well_formed or [version_key(version) for version in versions] != sorted({version_key(version) for version in versions}):
        raise _refusal(index, f"verified {VERSIONS_PROBLEM}")
    return tuple(versions)


def _refuse_repeats(switches: list[Switch]) -> None:
    for index, switch in enumerate(switches):
        for earlier_index, earlier in enumerate(switches[:index]):
            if (earlier.kind, earlier.name) == (switch.kind, switch.name):
                raise _refusal(index, f"name repeats entry {earlier_index}, which has the same kind")
            if earlier.removes == switch.removes:
                for key in SHARED_ROW_KEYS:
                    if getattr(earlier, key) != getattr(switch, key):
                        raise _refusal(index, f"{key} differs from entry {earlier_index}, which has the same removes")
