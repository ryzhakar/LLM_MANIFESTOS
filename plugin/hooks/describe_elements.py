#!/usr/bin/env python3
"""Print the sentences telling a model which elements bind it and where to read each.

Reads the elements as JSON on stdin; takes the config folder and the manifesto folder as arguments.
"""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "unharness", "src", "unharness"))
from config import FILE_SOURCE, MANIFESTO_SOURCE

COUNT_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight"}
TIERED_RESOLUTION = "resolve its location via the tiered protocol before binding"


def where_to_read(element, config_dir, manifesto_dir):
    source_type, reference = element["source_type"], element["reference"]
    if source_type == FILE_SOURCE:
        return "read it from " + os.path.abspath(os.path.join(config_dir, reference))
    if source_type == MANIFESTO_SOURCE:
        return "read it from " + os.path.join(manifesto_dir, "manifestos", reference + ".md")
    if source_type:
        return f"read it from {source_type} {reference}"
    return TIERED_RESOLUTION


def describe(element, config_dir, manifesto_dir):
    purpose = element.get("purpose")
    subject = f'"{element["name"]}" governs your {purpose}' if purpose else f'"{element["name"]}" is part of your constitution'
    return f"{subject} \u2014 {where_to_read(element, config_dir, manifesto_dir)}."


def main(config_dir, manifesto_dir):
    elements = json.load(sys.stdin)
    count = len(elements)
    sentences = [f"Your constitution has {COUNT_WORDS.get(count, str(count))} element{'s' if count != 1 else ''}."]
    sentences += [describe(element, config_dir, manifesto_dir) for element in elements]
    print(" ".join(sentences))


if __name__ == "__main__":
    main(*sys.argv[1:3])
