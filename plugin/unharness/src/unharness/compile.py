"""Compile resolved documents and the session's own files into the system prompt."""

import re
from collections.abc import Sequence
from dataclasses import dataclass

from unharness.config import UnharnessError
from unharness.resolve import Document

STACK_BLOCK = re.compile(r"\A<stack>\n(.*?)\n</stack>\n*", re.S)
INTERPLAY_FILE = ".manifestos.interplay.md"
COMMITMENTS_FILE = ".manifestos.commitments.md"
DOUBLE_QUOTE = '"'
SINGLE_QUOTE = "'"
WRITING_SKILL = "/compile-commitments"


@dataclass(frozen=True)
class Block:
    name: str
    purpose: str | None
    text: str


def compile_prompt(
    documents: list[Document], preamble: str, interplay: str | None, commitments: str | None,
    constitution: Sequence[Block | Document] | None = None,
) -> str:
    """Return the system prompt: preamble, constitution, interplay, commitments; stop if a session file is stale."""
    session_files = [
        _current_body(INTERPLAY_FILE, interplay, documents),
        _current_body(COMMITMENTS_FILE, commitments, documents),
    ]
    return "\n\n".join([f"<harness>\n{preamble.strip()}\n</harness>", constitution_block(documents if constitution is None else constitution), *session_files])


def stack_view(documents: list[Document]) -> str:
    """Return the stack block, then the constitution: what a session binds to."""
    return f"{stack_block(documents)}\n\n{constitution_block(documents)}"


def stack_block(documents: list[Document]) -> str:
    """Return the stack block: one line per document, in order."""
    return "<stack>\n" + "\n".join(_stack_lines(documents)) + "\n</stack>"


def constitution_block(blocks: Sequence[Block | Document]) -> str:
    """Return the constitution block: one tagged text per block, in order."""
    return "<constitution>\n" + "\n".join(_tagged(block) for block in blocks) + "\n</constitution>"


def _stack_lines(documents: list[Document]) -> list[str]:
    return [f"{document.name} {document.sha256} {document.purpose or ''}".rstrip() for document in documents]


def _tagged(block: Block | Document) -> str:
    governs = f' governs="{block.purpose.replace(DOUBLE_QUOTE, SINGLE_QUOTE)}"' if block.purpose else ""
    return f"<{block.name}{governs}>\n{block.text}\n</{block.name}>"


def _current_body(file_name: str, text: str | None, documents: list[Document]) -> str:
    """Return the session file without its stack block, or stop if the file is missing or stale."""
    if text is None:
        raise UnharnessError(f"{file_name} is missing; run {WRITING_SKILL}")
    recorded = STACK_BLOCK.match(text)
    if not recorded:
        raise UnharnessError(f"{file_name} has no <stack> block; run {WRITING_SKILL}")
    current_lines = _stack_lines(documents)
    recorded_lines = recorded.group(1).split("\n")
    if recorded_lines != current_lines:
        raise UnharnessError(f"{file_name} is stale ({_difference(recorded_lines, current_lines)}); run {WRITING_SKILL}")
    return text[recorded.end():].strip()


def _difference(recorded_lines: list[str], current_lines: list[str]) -> str:
    changed = sorted({line.split(" ")[0] for line in set(recorded_lines) ^ set(current_lines)})
    return f"changed: {', '.join(changed)}" if changed else "reordered"
