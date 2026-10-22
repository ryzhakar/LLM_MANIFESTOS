"""Compile resolved documents and the session's own files into the system prompt."""

import re

from unharness.resolve import Document

STACK_BLOCK = re.compile(r"\A<stack>\n.*?\n</stack>\n*", re.S)


def compile_prompt(documents: list[Document], preamble: str, interplay: str, commitments: str) -> str:
    """Return the system prompt: preamble, constitution, interplay, commitments."""
    return "\n\n".join([
        f"<harness>\n{preamble.strip()}\n</harness>",
        constitution_block(documents),
        _without_stack(interplay),
        _without_stack(commitments),
    ])


def stack_view(documents: list[Document]) -> str:
    """Return the stack block, then the constitution: what a session binds to."""
    return f"{stack_block(documents)}\n\n{constitution_block(documents)}"


def stack_block(documents: list[Document]) -> str:
    """Return one line per document, in order: name, sha256 of its text, purpose."""
    lines = (f"{document.name} {document.sha256} {document.purpose or ''}".rstrip() for document in documents)
    return "<stack>\n" + "\n".join(lines) + "\n</stack>"


def constitution_block(documents: list[Document]) -> str:
    """Return the constitution block: one tagged text per document, in order."""
    return "<constitution>\n" + "\n".join(_tagged(document) for document in documents) + "\n</constitution>"


def _tagged(document: Document) -> str:
    governs = f' governs="{document.purpose}"' if document.purpose else ""
    return f"<{document.name}{governs}>\n{document.text}\n</{document.name}>"


def _without_stack(session_file: str) -> str:
    return STACK_BLOCK.sub("", session_file).strip()
