#!/usr/bin/env python3
"""Print the sentences telling a model which elements bind it and where to read each.

Reads the elements as JSON on stdin; takes the config folder and the manifesto folder as arguments.
"""

import json
import os
import sys

COUNT_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight"}
TIERED_RESOLUTION = "resolve its location via the tiered protocol before binding"


def where_to_read(source, config_dir, manifesto_dir):
    kind, _, reference = source.partition(" ")
    if kind == "file":
        return "read it from " + os.path.abspath(os.path.join(config_dir, reference))
    if kind == "manifesto":
        return "read it from " + os.path.join(manifesto_dir, "manifestos", reference + ".md")
    return ("fetch it from " if source.startswith("http") else "read it from ") + source


def describe(element, config_dir, manifesto_dir):
    purpose = element.get("purpose")
    source = element.get("source")
    subject = f'"{element["name"]}" governs your {purpose}' if purpose else f'"{element["name"]}" is part of your constitution'
    where = where_to_read(source, config_dir, manifesto_dir) if source else TIERED_RESOLUTION
    return f"{subject} — {where}."


def main(config_dir, manifesto_dir):
    elements = json.load(sys.stdin)
    count = len(elements)
    sentences = [f"Your constitution has {COUNT_WORDS.get(count, str(count))} element{'s' if count != 1 else ''}."]
    sentences += [describe(element, config_dir, manifesto_dir) for element in elements]
    print(" ".join(sentences))


if __name__ == "__main__":
    main(*sys.argv[1:3])
