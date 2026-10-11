import importlib
import sys
import warnings
from pathlib import Path

import frontmatter
from pydantic import ValidationError

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

import generate

MAX_TAGLINE_WORDS = 8
REGISTERS = ('contemptuous', 'declarative', 'parable', 'lecture', 'aphoristic')
READERS = ('model', 'human', 'unspecified')
ORIGINAL_FIELDS = {
    'title': 'Sample',
    'tagline': 'one two three',
    'version': '1.0.0',
    'theme': 'cognitive-science',
    'description': 'A sample.',
}
ORIGINAL_FRONTMATTER = '''---
title: "Sample"
tagline: "one two three"
version: "1.0.0"
theme: "cognitive-science"
description: "A sample."
---

Body.
'''


def metadata(**overrides) -> generate.ManifestoMetadata:
    """Build metadata from the five original fields with overrides applied."""
    return generate.ManifestoMetadata(**{**ORIGINAL_FIELDS, **overrides})


def is_rejected(**overrides) -> bool:
    """Report whether the schema rejects the original fields with overrides applied."""
    try:
        metadata(**overrides)
    except ValidationError:
        return True
    return False


def entry(path: str, tagline: str) -> dict:
    """Build the per-file record that tagline_warnings reads."""
    return {'path': path, 'tagline': tagline}


def test_kind_defaults_to_manifesto():
    assert metadata().kind == 'manifesto'


def test_kind_accepts_canon():
    assert metadata(kind='canon').kind == 'canon'


def test_kind_rejects_unknown_value():
    assert is_rejected(kind='scripture')


def test_tagline_of_eight_words_is_accepted():
    assert not is_rejected(tagline=' '.join(['word'] * MAX_TAGLINE_WORDS))


def test_tagline_of_nine_words_is_rejected():
    assert is_rejected(tagline=' '.join(['word'] * (MAX_TAGLINE_WORDS + 1)))


def test_canon_tagline_of_nine_words_is_accepted():
    assert not is_rejected(kind='canon', tagline=' '.join(['word'] * (MAX_TAGLINE_WORDS + 1)))


def test_duplicate_tagline_warns_naming_both_files():
    warnings = generate.tagline_warnings([
        entry('manifestos/a.md', 'build for today'),
        entry('manifestos/b.md', 'build for today'),
    ])
    assert len(warnings) == 1
    assert 'manifestos/a.md' in warnings[0]
    assert 'manifestos/b.md' in warnings[0]


def test_duplicate_tagline_ignores_case_and_punctuation():
    warnings = generate.tagline_warnings([
        entry('manifestos/a.md', 'Build for today'),
        entry('manifestos/b.md', 'build for today.'),
    ])
    assert len(warnings) == 1


def test_distinct_taglines_raise_no_warning():
    warnings = generate.tagline_warnings([
        entry('manifestos/a.md', 'build for today'),
        entry('manifestos/b.md', 'atoms, not analogies'),
    ])
    assert warnings == []


def test_register_accepts_each_listed_value():
    assert [metadata(register=value).register for value in REGISTERS] == list(REGISTERS)


def test_register_rejects_unknown_value():
    assert is_rejected(register='lyrical')


def test_register_is_optional():
    assert metadata().register is None


def test_reader_accepts_each_listed_value():
    assert [metadata(reader=value).reader for value in READERS] == list(READERS)


def test_reader_rejects_unknown_value():
    assert is_rejected(reader='robot')


def test_reader_is_optional():
    assert metadata().reader is None


def test_file_with_only_the_five_original_fields_validates():
    post = frontmatter.loads(ORIGINAL_FRONTMATTER)
    parsed = generate.ManifestoMetadata(**post.metadata)
    assert parsed.title == 'Sample'
    assert (parsed.kind, parsed.register, parsed.reader) == ('manifesto', None, None)


def test_every_shipped_manifesto_validates():
    for md_file in sorted((REPO_ROOT / 'manifestos').glob('*.md')):
        generate.ManifestoMetadata(**frontmatter.load(md_file).metadata)


def test_importing_the_generator_emits_no_warning():
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        importlib.reload(generate)
    assert caught == []


def run_all() -> int:
    """Run every test_ function in this module and return the failure count."""
    failures = 0
    for name, test in list(globals().items()):
        if not (name.startswith('test_') and callable(test)):
            continue
        try:
            test()
        except Exception as error:
            failures += 1
            print(f'FAIL {name}: {type(error).__name__}: {error}')
        else:
            print(f'PASS {name}')
    print(f'{failures} failed')
    return failures


if __name__ == '__main__':
    sys.exit(1 if run_all() else 0)
