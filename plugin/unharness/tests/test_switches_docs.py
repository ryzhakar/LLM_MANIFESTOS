from pathlib import Path

import pytest
from unharness.switches import shipped_switches, strip_table

PLUGIN_FOLDER = Path(__file__).resolve().parents[2]
PLUGIN_README = PLUGIN_FOLDER / "README.md"
PACKAGE_README = PLUGIN_FOLDER / "unharness" / "README.md"
SCHEMA = PLUGIN_FOLDER / "SCHEMA.md"
OPENING_MARKER = "<!-- switches -->"
CLOSING_MARKER = "<!-- /switches -->"
TABLE_POINTER = "strip table in the Unharness section of"


def between_markers(text: str) -> tuple[str, str]:
    """Return the table the markers enclose and the text after the closing marker."""
    before, rest = text.split(f"{OPENING_MARKER}\n")
    table, after = rest.split(f"\n{CLOSING_MARKER}\n")
    return table, after


def test_the_readme_table_between_the_markers_equals_the_output_of_the_switches_verb():
    table, _ = between_markers(PLUGIN_README.read_text())

    assert table == strip_table(shipped_switches())


def test_the_sentence_above_the_markers_names_the_system_prompt_flag():
    above = PLUGIN_README.read_text().split(OPENING_MARKER)[0].rstrip().splitlines()[-1]

    assert "`--system-prompt-file`" in above


def test_the_paragraph_below_the_markers_names_no_switch_and_defines_the_table_words():
    _, after = between_markers(PLUGIN_README.read_text())
    paragraph = after.lstrip().split("\n\n")[0]

    assert not [switch.name for switch in shipped_switches() if switch.name in paragraph]
    assert all(word in paragraph for word in ("stripped", "set", "undocumented", "a release may drop"))


@pytest.mark.parametrize("document", [PACKAGE_README, SCHEMA])
def test_the_package_readme_and_the_schema_point_at_the_table_and_name_no_variable(document):
    text = document.read_text()

    assert TABLE_POINTER in text
    assert not [switch.name for switch in shipped_switches() if switch.name.startswith("CLAUDE_CODE_") and switch.name in text]
