# D1 code review of unharness 3.6.0 (feat/digests, 9e91351..8378fd2)

Method: read the 3.6.0 spec part and queue 27-41; read every changed source and test file; ran the suite (166 passed); ran the CLI against scratch fixtures in /tmp/d1code (renamed elements, malformed host files, a timing probe, the repo's own config and shipped index). Paths below are relative to `plugin/unharness/` unless they start with `plugin/` or `.`.

## Blocking

None found. Every refusal message matches the spec byte for byte, the cover search returns the spec's optimum with the spec's tie-break, flag implication works, doctor exits 1 only on FAIL, and the shipped `plugin/digests/index.json` is current for all 14 digests (doctor reported each as `plugin, current` against the worktree's manifestos).

## Should fix

1. `tests/test_digests.py`, `tests/test_cli.py`: no test combines `--minified` with a digest flag. The spec's Minified list ends with "session files compiled against the full stack load under `--stack-digests --overlap --minified`". Only `prompt --minified` alone is tested. I ran the combination by hand and it exits 0, so the code holds and the test is missing. Fix: add one cli test that writes the full and min pair for a World with digests and runs `prompt --stack-digests --overlap --minified`.

2. `tests/test_digests.py:21-80`: no test gives an element a name that differs from its slug. Spec decision 1 and the Terms section say digests key by slug, never by element name. The World fixture always uses `name: <slug>`. A run with `name: first-rule` and `source: manifesto alpha` works (tag `first-rule+second-rule`, digest found by slug), so the code honors the decision and nothing pins it. Fix: add a World variant with renamed elements and assert both the lookup and the tag.

3. `tests/test_digests.py:121-130`: the "local wins" test covers singles only. `src/unharness/digests.py:105-109` implements local-over-plugin for stack stems through dict overwrite order, and no test exercises it. Reordering the two folders in that tuple would pass the suite. Fix: add a stack-stem twin of the single test, with a stale local entry and a current plugin copy.

4. `src/unharness/doctor.py:241-253`: `_installed_versions` crashes with a traceback on a malformed `installed_plugins.json`. A top-level list raises `TypeError`, a null `plugins` raises `AttributeError`, and an entry without `version` raises `KeyError`; the `except` covers only `OSError`, `ValueError`, `KeyError` around the first read. I reproduced all five shapes. Doctor exists to report a broken setup, so it must print a FAIL or WARN line here. Fix: read defensively, treat any non-conforming shape as "no record", and add a test per shape.

5. `src/unharness/digests.py:125-137`, `:198-199`: the exhaustive subset search is 2^n in the number of candidate stack digests, and doctor runs it twice (`doctor.py:165`, `:178`). Measured with chained pair digests: 16 candidates 0.24 s, 18 candidates 1.0 s; growth is 4x per two candidates, so 26 candidates takes about 16 s and 40 about a day. A user who writes pair digests for an eleven-element stack (55 candidates) hangs with no message. The spec says "searches every subset", but the same optimum is reachable without it. Fix: depth-first search over candidates sorted by stem, skipping any branch that already overlaps (no-overlap mode) or already covers every slug, and keep the cost key unchanged; or document a candidate cap with a refusal message.

6. `plugin/unharness/pyproject.toml:3`, `plugin/unharness/uv.lock:68`, `plugin/.claude-plugin/plugin.json:3`, `.claude-plugin/marketplace.json:11`: all four still say 3.5.0 on a 3.6.0 change set. Queue 34 says tag 3.6.0 on completion. Fix: bump the four before tagging, and run `claude plugin validate` after.

7. `.manifestos.yaml:1`: `manifesto_dir` points at the main checkout `/Users/ryzhakar/LLM_MANIFESTOS/plugin`, which tracks the 14 digests but has no `index.json` until this branch merges. In the worktree, `unharness prompt --stack-digests --overlap --minified` exits 1 (`first-principles.md has no entry in .../index.json`), and doctor reports the same FAIL. The spec's end-to-end test ("in this repo ... exits 0") passes only after the merge, or with `manifesto_dir` overridden. Fix: run that check after fast-forwarding main, or via a config copy that points at the worktree's `plugin/`; do not run it from the worktree as is.

8. `src/unharness/digests.py:73` and `src/unharness/doctor.py:147`: the same comprehension (`{slug: document.sha256 ... if (slug := manifesto_slug(element))}`) lives in two files, and the slug list has two derivations (`digests.py:74`, `doctor.py:263-264`, the latter de-duplicated). That is one piece of knowledge, "the stack's slugs and their source hashes", with two homes. Fix: expose one `stack_hashes(elements, documents)` in `digests.py` and call it from both.

9. `src/unharness/digests.py:95-97` and `:162-163`: where a single digest lives is written twice, once in `locate_single` and once in `missing_message`. A change to the folder layout must touch both, and the message could name a path the search never tried. Fix: build the two candidate paths in one helper that both call.

## Nits

- `src/unharness/doctor.py:226`: with `uvx` present and `uv` absent, the OK line prints `None /path/uvx`. Fix: print only the paths found.
- `src/unharness/doctor.py:104`: `OK config:` prints the path as given (`.manifestos.yaml`), while the spec excerpt shows an absolute path and every `element` line is absolute. Fix: print `config_path.resolve()`.
- `src/unharness/doctor.py:188`: `pair is (MINIFIED_FILES if ...)` compares dataclass instances by identity. Fix: use `==`.
- `src/unharness/doctor.py:169`: a stack with no manifesto elements prints `OK cover: ; 0 words`. Fix: print a word such as `none` for the empty list.
- `src/unharness/doctor.py:97`, `:102`: one unresolved element suppresses the digest, cover, session-file, and size checks for the manifestos that did resolve. The spec fixes the config-FAIL case only. Fix: run the stack-free parts of these checks, or state the suppression in the README.
- `src/unharness/doctor.py:256-260` and `:161-163`: two try/except blocks around `digest_mode`. Fix: compute the mode once in `doctor()` and pass the result or the error down.
- `src/unharness/doctor.py:22`: doctor imports `manifesto_slug` from `unharness.digests`, which only re-exports it from `resolve`. Fix: import from `unharness.resolve`.
- `src/unharness/digests.py:108`: a local stack digest with unsorted or repeated slugs in its stem is skipped without a word, although decision 3 says no digest drops out unseen. Fix: have doctor report a WARN line for each `.md` under `.claude/digests` whose stem names several slugs but is not sorted and distinct.
- `src/unharness/digests.py:122`, `:164`, `:222`: `/compile-digest` appears as a bare literal three times, while `compile.py:17` holds `/compile-commitments` as a constant. Fix: one constant.
- `src/unharness/cli.py:99-102`: `digest_mode` runs after `resolve_stack`, so an unresolvable element hides the `--overlap requires --stack-digests` message. Fix: validate the flags before resolving.
- `src/unharness/cli.py:22-23`: `MINIFIED_FLAG` lives in `cli.py` while the other three flag names live in `digests.py`. Fix: put all four beside `MODE_FLAGS`.
- `src/unharness/compile.py:20` and `src/unharness/resolve.py:15`: `Block` and `Document` share `name`, `purpose`, `text`, and `constitution_block` accepts both by duck typing. Fix: let `Block` be the shared shape, or document why two types stay.
- `tests/test_digests.py:108`: the mode-flag rejection test for `stack` omits `--minified`, and nothing tests `launch`. The spec's Tests list names `stack` and `stamp` only, so this is a hardening gap. Fix: add `--minified` to the parameter list.

## Spec checks that held

- Refusals: the four digest messages, the no-cover message, the duplicate-slug message, and `--overlap requires --stack-digests` match the spec verbatim; the tests assert each as a whole string.
- Cover: ranking is (characters, file count, sorted stems); singles cover exactly the slugs no chosen stack covers; a stack with an outside slug never enters; local beats plugin per stem; `<plugin>/digests/<a+b>.md` is no candidate.
- Layout: a stack block sits at its first member, tag and `governs` join in config order, quotes become apostrophes, two blocks at one position follow stem order, overlapping stacks both name the shared member.
- Stamp: hashes come from `resolve_stack`, the one hashing home; JSON is `indent=2, sort_keys=True` plus a newline; the index goes to the parent of `stacks/`; a malformed index is refused, not overwritten.
- Doctor: check order, FAIL/WARN flip by flags, exit codes, config-FAIL reduction to three checks, no network call, stubbed `claude --version`.
- Stdlib only: no import outside the standard library; `dependencies = []`.
- Min pair in this repo: stack blocks equal the full pair's; interplay body is 0.236 and commitments body 0.325 of the full word counts, under one third; commitments hold one `I must` line per element.
