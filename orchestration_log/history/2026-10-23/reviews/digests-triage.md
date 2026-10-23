# Triage of the 3.6.0 reviews (feat/digests, 8378fd2)

Inputs: `digests-code.md`, `digests-prose.md`, `digests-spec.md`. Each line below carries the review (code, prose, spec), the rank (B blocking, S should fix, N nit, T a row of the spec review's tables), and the number the review gave it. I checked each finding against the spec, queue 27-41, and the code before ruling.

Rulings: ACCEPT is applied. REJECT is applied nowhere, with the reason. DEFER is left for a named later step. Where a finding showed the spec wrong, the spec is fixed and the line says so; the spec fixes are listed at the end.

The lead's ruling for this pass: every version pin and version field stays at 3.5.0 until the release unit bumps it.

## Blocking

- prose B1 DEFER (to release): `plugin/unharness/README.md` pins `@v3.5.0`; the release unit sets the pin with the version fields in one commit.
- prose B2 ACCEPT: `plugin/README.md` says the min pair holds a third of its full counterpart's words; the spec and the skill budget the body after the `<stack>` block only. Counted on whole files the claim is false.

## Should fix

- code S1 ACCEPT: no test combines `--minified` with a digest flag; the code holds, so a test only.
- spec S1 ACCEPT: the same finding as code S1.
- code S2 ACCEPT: no test names an element differently from its slug; decision 1 rests on it.
- spec S2 ACCEPT: the same finding as code S2.
- code S3 ACCEPT: local-over-plugin is tested for singles only; add the stack twin.
- code S4 ACCEPT: doctor crashes on a malformed `installed_plugins.json`; I will reproduce each shape in a failing test first.
- code S5 ACCEPT: the subset search doubles with every candidate stack digest and doctor runs it twice. The spec's "returns exactly this optimum" stands; its "searches every subset" is the spec error, fixed below. The search becomes a table over covered slugs, which keeps the cost key unchanged.
- code S6 DEFER (to release): the four version fields still read 3.5.0; same ruling as prose B1.
- spec S5 DEFER (to release): the same finding as code S6; the floor of 3.5.0 in doctor is the manifesto plugin's floor and stays.
- code S7 DEFER (to the end-to-end step): `manifesto_dir` in `.manifestos.yaml` names the main checkout, so the repo-wide run passes after the merge; the end-to-end record runs it from a config that points at the branch.
- code S8 ACCEPT: the hash map and the slug list have two homes, `digests.py` and `doctor.py`; one function serves both.
- code S9 ACCEPT: the single digest's two candidate paths are written in `locate_single` and again in `missing_message`; one helper serves both.
- spec S3 ACCEPT: the skill's confirm-the-compile section runs `prompt` after the stamp; the spec's six steps and the skill's own "Stop at the digest and its stamp" end at the stamp. The section goes.
- spec S4 REJECT (spec error, fixed in spec): doctor drops the four stack checks when an element fails to resolve, and a test asserts it; the spec row now says so, and the README sentence on doctor says so.
- prose S1 ACCEPT: `plugin/README.md` says `/compile-commitments` writes two files and that `prompt` stops until they match; it writes four, and the min pair gates `--minified`.
- prose S2 ACCEPT: `plugin/unharness/README.md` says all four flags swap texts; only two do.
- prose S3 ACCEPT: the slug rule in the skill names `source: manifesto` alone, while an element with no source line takes its name as the slug.
- prose S4 ACCEPT: "under 350 words" admits exactly 350, and the skill gives no count command although it requires a count.
- prose S5 ACCEPT: the README does not say that a local file wins for its stem even when its entry is stale.
- prose S6 ACCEPT: three names for the condensed pair across the README, the skills, and SCHEMA; one name, "min pair", defined once.
- prose S7 REJECT (moot): the clauses it asks for belong to confirm-the-compile, which spec S3 removes.
- prose S8 ACCEPT: the skill names six of Strunk's rules; it adds one sentence binding to `agent-conduct:write-well` when installed.
- spec N7 ACCEPT: the same finding as prose S8.

## Nits

- code N1 ACCEPT: with `uvx` present and `uv` absent, doctor prints `None /path/uvx`.
- spec N1 ACCEPT: the same finding as code N1.
- code N2 ACCEPT: `OK config` prints the path as given; every element line is absolute, and the spec excerpt shows an absolute path.
- code N3 ACCEPT: `pair is (...)` compares by identity; use equality.
- code N4 ACCEPT: an empty cover prints `OK cover: ; 0 words`.
- code N5 REJECT (spec error, fixed in spec): the suppression of checks is deliberate; same fix as spec S4.
- code N6 ACCEPT: two try blocks around `digest_mode` in doctor; compute it once.
- code N7 ACCEPT: doctor imports `manifesto_slug` from `digests`, which re-exports it; import from `resolve`.
- code N8 REJECT (spec error, fixed in spec): a local stack file with an unsorted or repeated stem is no candidate, as a plugin file at `<plugin>/digests/<a+b>.md` is none. Decision 3 binds files a mode considers, and the spec now says which files it considers. `stamp` refuses such a name, and the skill sorts.
- spec N3 REJECT (spec error, fixed in spec): the same finding as code N8.
- code N9 ACCEPT: `/compile-digest` appears as a bare literal three times.
- code N10 ACCEPT: an unresolvable element hides `--overlap requires --stack-digests`; validate the flags first.
- code N11 REJECT: `MINIFIED_FLAG` lives beside the session files it selects and the digest flags beside the digests; moving it would join two meanings, and no behavior changes.
- code N12 DEFER (to a later refactor): `Block` and `Document` share three fields; merging them touches every module and is no part of 3.6.0.
- code N13 ACCEPT: add `--minified` to the mode-flag rejection test for `stack`, and add `stamp` beside it, which the spec's test list names. The `launch` case stays untested: argparse rejects an unknown flag there.
- spec N2 REJECT (spec error, fixed in spec): a `claude` that prints no version warns; the spec row now lists that cause.
- spec N4 REJECT (spec error, fixed in spec): the two stamp refusals and the empty-slug case lacked spec text; they now have it.
- spec N5 ACCEPT: the min commitments open a line with `I must not fool myself`; the spec asks for `I must ..., and I will ...` per element.
- prose N11 ACCEPT: the same finding as spec N5, with the reviewer's wording.
- spec N6 ACCEPT: the compile-commitments skill counts the min body but never the full body's third.
- prose N1 ACCEPT: "it" in the index sentence can point at the place or the index.
- prose N2 ACCEPT: the doctor excerpt opens with `$`; no other block does.
- prose N3 ACCEPT: "each manifesto element enters as its digest" holds for `--digests` only; the cover rule omits the third tie-break.
- prose N4 ACCEPT: the list opens "these files" and ends with a folder.
- prose N5 ACCEPT: SCHEMA says `stack` with no element in `you` is empty; `stack` with slugs prints before that check.
- prose N6 ACCEPT: SCHEMA's cause for "has no entry" omits an entry whose slugs differ from the stem.
- prose N7 ACCEPT: SCHEMA's cause for the no-cover line omits its premise, a manifesto with no single digest.
- prose N8 ACCEPT: the unharness README strands a modifier in the `stack` line.
- prose N9 ACCEPT: "figures" and "closing choice" in the skill read ambiguously.
- prose N10 ACCEPT: "and I give every doubt" in the min interplay.
- prose N12 ACCEPT: the root README and its template omit the local digest folder.

## Rows of the spec review's tables

- spec T1 REJECT: the shipped plugin index is current for all 14 digests, and spec line 148 already describes the plugin index; shipping it is the release unit's act.
- spec T2 REJECT: the `launch` verb's refusal of mode flags is argparse's; the spec's test list names `stack` and `stamp` only.
- spec T3 DEFER (to the end-to-end record): a live `/compile-digest` run has no pytest form.

## Spec fixes made in this pass

All in `orchestration_log/history/2026-10-23/spec-unharness.md`, part 3.6.0:

1. Cover selection: the search method is the code's; the spec keeps the optimum and its ranking.
2. `unharness doctor`: an element that fails to resolve leaves out the digest, cover, session-file, and prompt-size checks; the `claude` row adds the third WARN cause.
3. `unharness doctor`, `prompt size`: the count includes the `<harness>` tags of the preamble block, so the line equals `wc -w` of the prompt it names.
4. Digest sources: a stack file whose stem is not sorted and distinct, or whose place the table does not name, is no candidate and raises nothing; the two stamp refusals and the empty-slug case carry their text.

## End-to-end record (`verification-digests.md`)

The record scores 35 rows, 35 PASS and 0 FAIL, so no FAIL row needed a fix. Its findings and observations are ruled here.

- e2e premise REJECT: the stack lacks `raise-the-bar`, so no mode refuses in this repo; a fact about the brief, not a defect.
- e2e meta login REJECT: the `meta` login holds manifesto plugin 3.4.0, so doctor's FAIL is correct; an environment fact.
- e2e version strings DEFER (to release): the three version fields read 3.5.0; same ruling as code S6.
- e2e skill counting rule ACCEPT: the skill gave a cap and no count rule; the same finding as prose S4, fixed there with `wc -w`.
- e2e skill drop order DEFER (to the owner): the cap forces dropped demands, and neither the spec nor the repo's write-digest skill that it follows says which to drop first; the rule is a product decision.
- e2e subagent binding REJECT: spec step 3 orders the bind through `manifesto-oath`; whether a start hook already bound the subagent is the harness's matter.
- e2e idioms in a manifesto REJECT: the skill already bans idioms and its check step covers them; the record says the rewrite worked.
- e2e doctor word count ACCEPT: I traced the two-word gap to the `<harness>` tags that the compiled prompt wraps round the preamble and the count left out. A test now compares doctor's sizes with `wc -w` of both prompts, and the count includes the tags. The spec line is fixed to say so.
- e2e `BrokenPipeError` on `stack | head` DEFER (to a later unit): no spec line covers it, and every verb shares it.
- e2e ten names in the first reply, and the hook line REJECT: model behavior and the login's older plugin, not scored and not a product fault.

## Commits on feat/digests

| Sha | Subject | Findings |
|---|---|---|
| 34ec254 | fix(unharness): pin slug keys, local stacks, minified flags | code S1, S2, S3, N13 |
| 00029fb | fix(unharness): doctor survives malformed records, prints plain lines | code S4, N1, N2, N3, N4 |
| 46e6b79 | fix(unharness): cover search scales with slugs, not stack digests | code S5 |
| 579e1bc | fix(unharness): one home for slugs, hashes, and digest paths | code S8, S9, N6, N7, N9, N10 |
| 2e979f6 | fix(unharness): test every mode flag against stamp once | code N13, spec test row |
| c2ca1b1 | fix(skill): slug rule, word counts, write-well; drop extra compile | prose S3, S4, S8, N9; spec S3, N6, N7 |
| ecf43a9 | doc(plugin): min pair, slug and cover wording, doctor omissions | prose B2, S1, S2, S5, S6, N1-N8, N10-N12; spec S4, N5 |
| 8b6fb06 | fix(unharness): prompt size counts the harness tags too | e2e doctor word count |

The spec edits sit in `spec-unharness.md` in the main checkout, uncommitted. The `.min.md` files and the root README changed inside the doc commit.

## Counts

| Source | Accept | Reject | Defer | FAIL rows |
|---|---|---|---|---|
| code review | 16 | 3 | 3 | n/a |
| spec review | 7 | 6 | 2 | n/a |
| prose review | 20 | 1 | 1 | n/a |
| end-to-end record | 2 | 5 | 3 | 0 |
| Total | 45 | 15 | 9 | 0 |

Of the 69 lines, 9 repeat a finding that another review or the record made; each repeat is ruled as its twin.

## Last lines of the final runs

Suite, from the worktree:

```
$ uv run --project plugin/unharness pytest -q plugin/unharness
..............................................                           [100%]
190 passed in 7.93s
```

Plugin and marketplace:

```
$ claude plugin validate plugin
✔ Validation passed
$ claude plugin validate .
✔ Validation passed
```

Doctor with the repo's own config exits 1 from two causes outside this pass. The config's `manifesto_dir` names the main checkout, which has no `index.json` until the merge (code S7), and the login holds manifesto plugin 3.4.0. Last lines:

```
$ plugin/bin/unharness doctor --config .manifestos.yaml
OK .manifestos.commitments.min.md: current
OK preamble: shipped
OK claude: /Users/ryzhakar/.local/bin/claude 2.1.309
OK uv: /Users/ryzhakar/pp/offline-kit/shim/uv /Users/ryzhakar/pp/offline-kit/shim/uvx
FAIL manifesto plugin: 3.4.0 is below 3.5.0, whose hooks do not stand down
WARN prompt size: shortest mode cannot compile: .../LLM_MANIFESTOS/plugin/digests/first-principles.md has no entry in .../LLM_MANIFESTOS/plugin/digests/index.json; run unharness stamp ...
```

The same run from a temporary copy of the config that points `manifesto_dir` at the branch's `plugin` folder, with `--stack-digests --overlap --minified`, shows only the login FAIL; `unharness prompt` with the same flags exits 0:

```
OK uv: /Users/ryzhakar/pp/offline-kit/shim/uv /Users/ryzhakar/pp/offline-kit/shim/uvx
FAIL manifesto plugin: 3.4.0 is below 3.5.0, whose hooks do not stand down
OK prompt size: full 14888 words; shortest 5581 words
```

The temporary copy is deleted.
