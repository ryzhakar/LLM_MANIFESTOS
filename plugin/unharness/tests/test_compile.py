from unharness.compile import compile_prompt, constitution_block, stack_view
from unharness.resolve import Document

DRY = Document("dry", "one home", "DRY TEXT", "a" * 64)
KISS = Document("kiss", None, "KISS TEXT\nsecond line", "b" * 64)
STACK = f"<stack>\ndry {'a' * 64} one home\nkiss {'b' * 64}\n</stack>"
INTERPLAY = f"{STACK}\n\n<interplay>\nThe elements agree.\n</interplay>\n"
COMMITMENTS = f"{STACK}\n\n<commitments>\nI must, and I will.\n</commitments>\n"


def test_the_prompt_is_the_preamble_the_constitution_and_the_two_session_files_without_their_stack_blocks():
    prompt = compile_prompt([DRY, KISS], "PREAMBLE", INTERPLAY, COMMITMENTS)

    assert prompt == (
        "<harness>\nPREAMBLE\n</harness>\n\n"
        "<constitution>\n"
        '<dry governs="one home">\nDRY TEXT\n</dry>\n'
        "<kiss>\nKISS TEXT\nsecond line\n</kiss>\n"
        "</constitution>\n\n"
        "<interplay>\nThe elements agree.\n</interplay>\n\n"
        "<commitments>\nI must, and I will.\n</commitments>"
    )


def test_the_stack_view_is_the_stack_block_with_one_sha256_line_per_element_then_the_constitution():
    view = stack_view([DRY, KISS])

    assert view == STACK + "\n\n" + constitution_block([DRY, KISS])
