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
3. Digest sources: a stack file whose stem is not sorted and distinct, or whose place the table does not name, is no candidate and raises nothing; the two stamp refusals and the empty-slug case carry their text.

## Counts before the end-to-end rows

Findings ruled: 59 lines across the three reviews, of which 8 repeat another review's finding. Per review:

| Review | Accept | Reject | Defer |
|---|---|---|---|
| code | 16 | 3 | 3 |
| spec | 7 | 6 | 2 |
| prose | 20 | 1 | 1 |
