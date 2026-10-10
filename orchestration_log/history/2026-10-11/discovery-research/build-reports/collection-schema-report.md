Binding, elements loaded: First Principles (/home/user/LLM_MANIFESTOS/manifestos/first-principles.md, 114 lines, v1.0.1 at load), Strunk SPR v3 (/home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml, 2923 lines), manifesto-oath protocol (/home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md), TDD (/home/user/claude-skills/dev-discipline/skills/tdd/SKILL.md); each read in full from source.
Binding, interplay: First Principles and TDD converge on building from verified atoms (a test run verifies; the owner's decisions bound the schema, not the template's habits); Strunk converges on omission and concrete statement. Tension: TDD forbids a second test before the first passes and forbids comments, while the dispatch orders the full named test set first and generate.py already holds comments; resolution: write the dispatch's named tests as one batch, fill bodies one at a time, add no comment, leave existing ones. Second tension: Strunk's complete-sentence rule against table fragments; resolution: technical-documentation allowance.
Binding, commitments: I must verify each claim against files and runs, and I will print command output, not recollection; I must write tests through the public surface before code and run red, and I will read each failure before filling a body; I must not edit bodies, MAINTAINERS_GUIDE.md, or values outside the owner's decisions unnamed, and I will not; every deviation sits under Open.

# Collection Schema

Repository /home/user/LLM_MANIFESTOS, branch claude/manifesto-design-discussion-liuuvf. Test file: /home/user/LLM_MANIFESTOS/tests/test_generate.py (plain asserts; runs under `python3` and under `pytest`). Runner: `uv run --with pytest --with pyyaml --with python-frontmatter --with pydantic --with jinja2 --with rich python tests/test_generate.py`.

## Red / Green — test output before and after

### Red — 16 tests written first, generate.py unchanged

```
FAIL test_kind_defaults_to_manifesto: AttributeError: 'ManifestoMetadata' object has no attribute 'kind'
FAIL test_kind_accepts_canon: AttributeError: 'ManifestoMetadata' object has no attribute 'kind'
FAIL test_kind_rejects_unknown_value: AssertionError: 
PASS test_tagline_of_eight_words_is_accepted
FAIL test_tagline_of_nine_words_is_rejected: AssertionError: 
FAIL test_duplicate_tagline_warns_naming_both_files: AttributeError: module 'generate' has no attribute 'tagline_warnings'
FAIL test_duplicate_tagline_ignores_case_and_punctuation: AttributeError: module 'generate' has no attribute 'tagline_warnings'
FAIL test_distinct_taglines_raise_no_warning: AttributeError: module 'generate' has no attribute 'tagline_warnings'
FAIL test_register_accepts_each_listed_value: AttributeError: 'ManifestoMetadata' object has no attribute 'register'
FAIL test_register_rejects_unknown_value: AssertionError: 
FAIL test_register_is_optional: AttributeError: 'ManifestoMetadata' object has no attribute 'register'
FAIL test_reader_accepts_each_listed_value: AttributeError: 'ManifestoMetadata' object has no attribute 'reader'
FAIL test_reader_rejects_unknown_value: AssertionError: 
FAIL test_reader_is_optional: AttributeError: 'ManifestoMetadata' object has no attribute 'reader'
FAIL test_file_with_only_the_five_original_fields_validates: AttributeError: 'ManifestoMetadata' object has no attribute 'kind'
PASS test_every_shipped_manifesto_validates
14 failed
```

Reasons read: 10 fail on the missing field or function (`kind`, `register`, `reader`, `tagline_warnings`); 4 fail because the model silently accepts an unknown enum value or a 10-word tagline. The 2 passes are expected: an 8-word tagline passes while no rule exists, and the shipped corpus validates against a schema with no rule.

### Red — 17th test added after the first green run

Pydantic emitted `UserWarning: Field name "register" in "ManifestoMetadata" shadows an attribute in parent "BaseModel"` (`register` is `ABCMeta.register`; instance access works). Test `test_importing_the_generator_emits_no_warning` first run:

```
FAIL test_importing_the_generator_emits_no_warning: AssertionError: 
1 failed
```

### Red — first green attempt, shipped corpus

After the schema landed, `test_every_shipped_manifesto_validates` failed on cargo-cult-science.md (see Open 1):

```
FAIL test_every_shipped_manifesto_validates: ValidationError: 1 validation error for ManifestoMetadata
tagline
  Value error, Tagline must be at most 8 words, got 10: the first principle is that you must not fool yourself
1 failed
```

### Green — final run, 17 tests

```
PASS test_kind_defaults_to_manifesto
PASS test_kind_accepts_canon
PASS test_kind_rejects_unknown_value
PASS test_tagline_of_eight_words_is_accepted
PASS test_tagline_of_nine_words_is_rejected
PASS test_duplicate_tagline_warns_naming_both_files
PASS test_duplicate_tagline_ignores_case_and_punctuation
PASS test_distinct_taglines_raise_no_warning
PASS test_register_accepts_each_listed_value
PASS test_register_rejects_unknown_value
PASS test_register_is_optional
PASS test_reader_accepts_each_listed_value
PASS test_reader_rejects_unknown_value
PASS test_reader_is_optional
PASS test_file_with_only_the_five_original_fields_validates
PASS test_every_shipped_manifesto_validates
PASS test_importing_the_generator_emits_no_warning
0 failed
```

`python -m pytest -q tests/test_generate.py`: `17 passed in 0.15s`.

Generator run after the last commit: `✓ Generated README.md from 12 manifesto(s)`, exit 0, no error panel, no warning panel, no Python warning.

`git diff --stat` before the README commit: `README.md | 55 ++++++++++++++++++++++++++++---------------------------`, 28 insertions, 27 deletions.

## Backfill table — file | kind | register | reader | source row

Source: /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/corpus-audit.md, Judgment table; the line is the table row. Register and reader values are the row's words, verbatim; every register word was already in the enum. Kind: `manifesto` is the default and no key is written; `canon` is written for the two files of owner decision 4.

| file | kind | register | reader | source row |
|---|---|---|---|---|
| cargo-cult-science.md | canon | lecture | unspecified | corpus-audit.md:27 (reader "unspecified (human scientists, commencement audience)"; register "lecture") |
| correct-by-construction.md | manifesto (default) | declarative | human | corpus-audit.md:28 (reader "human engineer") |
| dry.md | manifesto (default) | declarative | human | corpus-audit.md:29 (reader "human engineer") |
| first-principles.md | manifesto (default) | parable | unspecified | corpus-audit.md:30 |
| intervention.md | manifesto (default) | parable | unspecified | corpus-audit.md:31 |
| kiss.md | manifesto (default) | declarative | human | corpus-audit.md:32 (reader "human engineer") |
| postgres.md | manifesto (default) | contemptuous | human | corpus-audit.md:33 (reader "human engineer") |
| self-documenting-code.md | manifesto (default) | lecture | human | corpus-audit.md:34 (reader "human engineer") |
| simple-made-easy.md | manifesto (default) | lecture | human | corpus-audit.md:35 (reader "human engineer") |
| stop-yapping.md | manifesto (default) | contemptuous | model | corpus-audit.md:36 (reader "the model") |
| yagni.md | manifesto (default) | declarative | human | corpus-audit.md:37 (reader "human engineer") |
| zen-of-python.md | canon | aphoristic | unspecified | corpus-audit.md:38 |

Body check: the backfill diff is 26 insertions, 0 deletions across 12 files; every hunk sits inside the frontmatter. Reader mapping: "human engineer" to `human`, "the model" to `model`, "unspecified" to `unspecified`.

Other edits: themes.yaml lost design-methodology, ai-instructions, research-protocols (15 deletions; zero files used them; software-engineering and cognitive-science remain). first-principles.md version `1.0.1` to `1.0.0`. MAINTAINERS_GUIDE.md untouched; its "Patches (don't use; just edit)" wording stays.

## Commits — hash | message | files

Pushed: `git push -u origin claude/manifesto-design-discussion-liuuvf` succeeded on the first attempt (no retry needed); c47d5f4..c1a7834; local HEAD equals origin HEAD (c1a783471e38866295063ab2ab97b9907f375f51).

| hash | message | files |
|---|---|---|
| 56a8727 | fix: shorten cargo-cult-science tagline to 8 words or fewer | manifestos/cargo-cult-science.md |
| 1fa3f28 | feat: add kind, register, reader fields and tagline checks to schema | generate.py, README.template.md |
| 613f75f | test: cover manifesto schema and tagline checks | tests/test_generate.py |
| 8fc8aef | chore: backfill kind, register, reader frontmatter | manifestos/*.md (12 files) |
| cf168d1 | chore: drop themes with no manifestos | themes.yaml |
| 12ba3f1 | chore: set first-principles version to 1.0.0 | manifestos/first-principles.md |
| c1a7834 | chore: regenerate README | README.md |

The owner's five commits are 1fa3f28, 8fc8aef, cf168d1, 12ba3f1, c1a7834 in that order. 56a8727 and 613f75f are additions (Open 1 and 2).

## Open

1. Tagline conflict. The 8-word rule rejects cargo-cult-science.md, whose tagline held 10 words ("the first principle is that you must not fool yourself"); the generator would skip the file and drop it from the README. I shortened it to "you must not fool yourself" (a verbatim substring, 5 words) in its own commit, 56a8727, placed first so every commit state validates. Revert 56a8727 and exempt `kind: canon` from the length rule if the owner wants the full quotation.
2. Tests need their own commit: CLAUDE.md puts tests and product code in separate commits and the owner's list names none. 613f75f follows the schema commit so no commit state is red.
3. Reading of decision 5: "every other file" read as all 12 files, so the two canon files also carry register and reader (judgment-table rows exist for both). Delete those four lines in cargo-cult-science.md and zen-of-python.md if the owner meant the ten non-canon files only.
4. first-principles.md version moved down (1.0.1 to 1.0.0) per decision 7; no change-log record of the 1.0.1 text exists in this task's scope.
5. Pydantic warns that field `register` shadows `ABCMeta.register`. generate.py filters that one warning by message (`REGISTER_SHADOW_WARNING`); the field name stays as the owner specified. Renaming the field to an alias would remove the filter at the cost of `register_` in the model.
6. Duplicate-tagline check compares lowercase, punctuation-stripped words; it warns, never rejects. No two current taglines match.
7. README.template.md gained one line under "Adding a new manifesto" naming the 8-word limit and the three optional fields, and a Register column in Quick Reference. The `reader` field is validated and stored; no README output shows it (decision 3 names kind and register only).
8. Not committed: this report (research/ is in .gitignore) and any `__pycache__` (runs used PYTHONDONTWRITEBYTECODE=1). justfile unchanged: no `test` recipe added.

Tests: 17 written, red recorded (14 of 16 failing at first run), green 17 of 17 under the script runner and under pytest. Files: 12 manifestos backfilled with register and reader (2 as canon), plus themes.yaml, first-principles version, and the regenerated README. Push: succeeded on the first attempt, origin and local HEAD both at c1a7834.

## Follow-up

Owner ruling on Open items: canon is exempt from form rules; keep register and reader on canon files (Open 3); keep the shadow-warning filter (Open 5); show reader in the README. Open 1 is closed by the revert below.

### Red — canon exemption test, before the fix

```
FAIL test_canon_tagline_of_nine_words_is_accepted: AssertionError: 
1 failed
```

The tagline rule moved from a field validator to a model validator (`validate_tagline_length`, `mode='after'`) because `kind` is validated after `tagline` and a field validator cannot read it. The rule rejects a tagline over 8 words unless `kind` is `canon`.

### Green — 18 tests

```
PASS test_every_shipped_manifesto_validates
PASS test_importing_the_generator_emits_no_warning
0 failed
```

`python -m pytest -q tests/test_generate.py`: `18 passed in 0.20s`. Generator: `✓ Generated README.md from 12 manifesto(s)`, exit 0, no panel, no warning. cargo-cult-science.md again carries "the first principle is that you must not fool yourself" (10 words) and validates as canon.

### Commits — hash | message | files

Pushed on the first attempt: c1a7834..628881c; local and origin HEAD both 628881c660e4d5dec753c736d5f7f0039c97923d.

| hash | message | files |
|---|---|---|
| 531e955 | test: canon exempt from tagline length | tests/test_generate.py |
| 4fdf61b | fix: exempt canon from tagline length check | generate.py |
| 804973a | revert: restore cargo-cult-science tagline | manifestos/cargo-cult-science.md |
| d892729 | doc: note canon tagline exemption in README template | README.template.md |
| bfbbabd | chore: show reader in README | README.template.md |
| 628881c | chore: regenerate README | README.md |

804973a reverts 56a8727 with git's subject trimmed to the owner's wording. d892729 is an addition: the template line "Tagline: at most 8 words" became wrong once canon was exempt, so it now reads "at most 8 words (`kind: canon` exempt)"; it is a separate commit because documentation and the reader column revert independently.

README: Quick Reference gained a Reader column after Register; each entry heading reads `version · register · reader`.
