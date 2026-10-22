"""Compile resolved documents and the session's own files into the system prompt."""

import re

from unharness.config import UnharnessError
from unharness.resolve import Document

STACK_BLOCK = re.compile(r"\A<stack>\n(.*?)\n</stack>\n*", re.S)
INTERPLAY_FILE = ".manifestos.interplay.md"
COMMITMENTS_FILE = ".manifestos.commitments.md"
WRITING_SKILL = "/compile-commitments"


def compile_prompt(documents: list[Document], preamble: str, interplay: str | None, commitments: str | None) -> str:
    """Return the system prompt: preamble, constitution, interplay, commitments; stop if a session file is stale."""
    session_files = [
        _current_body(INTERPLAY_FILE, interplay, documents),
        _current_body(COMMITMENTS_FILE, commitments, documents),
    ]
    return "\n\n".join([f"<harness>\n{preamble.strip()}\n</harness>", constitution_block(documents), *session_files])


def stack_view(documents: list[Document]) -> str:
    """Return the stack block, then the constitution: what a session binds to."""
    return f"{stack_block(documents)}\n\n{constitution_block(documents)}"


def stack_block(documents: list[Document]) -> str:
    """Return the stack block: one line per document, in order."""
    return "<stack>\n" + "\n".join(_stack_lines(documents)) + "\n</stack>"


def constitution_block(documents: list[Document]) -> str:
    """Return the constitution block: one tagged text per document, in order."""
    return "<constitution>\n" + "\n".join(_tagged(document) for document in documents) + "\n</constitution>"


def _stack_lines(documents: list[Document]) -> list[str]:
    return [f"{document.name} {document.sha256} {document.purpose or ''}".rstrip() for document in documents]


def _tagged(document: Document) -> str:
    governs = f' governs="{document.purpose}"' if document.purpose else ""
    return f"<{document.name}{governs}>\n{document.text}\n</{document.name}>"


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
