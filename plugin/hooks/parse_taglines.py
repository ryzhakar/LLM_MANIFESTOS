#!/usr/bin/env python3
"""Print the active bindings: each YOU_STACK element, with the tagline of its registry manifesto when it has one."""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "unharness", "src", "unharness"))
from config import MANIFESTO_SOURCE, TEXT_ENCODING, UnharnessError, parse_yaml

FRONTMATTER_FENCE = "---"


def tagline_of(path):
    """Return the tagline in the frontmatter of the manifesto at path; empty when the file or the tagline is absent."""
    try:
        with open(path, encoding=TEXT_ENCODING) as manifesto:
            content = manifesto.read()
    except FileNotFoundError:
        return ""
    if not content.startswith(FRONTMATTER_FENCE + "\n"):
        return ""
    end = content.find("\n" + FRONTMATTER_FENCE, len(FRONTMATTER_FENCE))
    frontmatter = parse_yaml(content[len(FRONTMATTER_FENCE) + 1:end]) if end != -1 else None
    return frontmatter.get("tagline", "") if isinstance(frontmatter, dict) else ""


def binding(element, manifesto_dir):
    """Return the element's name, with its manifesto's tagline when the element is a registry manifesto that has one."""
    name = element["name"]
    if element["source_type"] not in (None, MANIFESTO_SOURCE):
        return name
    path = os.path.join(manifesto_dir, "manifestos", (element["reference"] or name) + ".md")
    try:
        tagline = tagline_of(path)
    except UnharnessError as error:
        print(f"unharness: {path}: {error}", file=sys.stderr)
        return name
    return f'{name}: "{tagline}"' if tagline else name


def main():
    stack = json.loads(os.environ.get("YOU_STACK") or "[]")
    manifesto_dir = os.environ["MANIFESTO_DIR"]
    if stack:
        print("Active bindings: " + " · ".join(binding(element, manifesto_dir) for element in stack))


if __name__ == "__main__":
    main()
