# Petro stack digest, cut-3: data (frozen 2026-10-13)

Rendered by script from the local-only eval dir `cargo-cult-science+correct-by-construction+dry+first-principles+kiss+lines-spent+self-documenting-code+simple-made-easy+stop-yapping+yagni+zen-of-python` (outside the repo, in `/Users/ryzhakar/petro/evals/`). Mean violations are per reply; a demand can fire more than once in a reply. Reader sampling is unseeded (`pi` has no seed or temperature flag). Wall seconds are per reply on the local llama-server.

## Instrument

- Reader: `{"adapter": "pi", "model": "long"}`; judge: `{"name": "sonnet-agents", "brief": "judge_brief.md"}`.
- Gate: `{"split": "test", "ci": 0.95, "min_cut_vs_none": 1.0, "margin_vs_full": 1.0, "completion_margin": 0.1, "drift_margin": 0.1}`.
- Conditions: `{"baselines": ["full", "terse", "placebo"], "terse_line": "Answer briefly and precisely, and write careful, minimal, well-typed Python and Rust.", "placebo_source": "/Users/ryzhakar/petro/evals/cargo-cult-science+correct-by-construction+dry+first-principles+kiss+lines-spent+self-documenting-code+simple-made-easy+stop-yapping+yagni+zen-of-python/placebo.md", "ablations": false}`.
- Reps: `1`; spec note (cut-1 sizing, carried by the frozen spec): Cut 1 sized to the 90-minute reader budget at the measured 28 s per reply: 23 singles x 1 rep x 5 conditions plus 2 sessions x 8 turns x 5 conditions = 195 replies. The reps rule (digest-eval reps on cut-1-aborted, script-judge proxy) on 7 script-proxy pairs, spread 1.245, asked for 2 over 12 test tasks; capped at 1 for the budget. Spec frozen before the first reply of cut-1; cut-1-aborted ran under the earlier spec (reps 2, 3 sessions x 10 turns) and was stopped at 36 replies..
- Demands: 39 (5 scripted, 34 judged).
- Tasks: 23 singles (11 dev, 12 test) in 9 families; 2 sessions, 16 turns.

## Judge calibration (fable-planted violations)

```json
{
 "name": "sonnet-agents",
 "brief": "judge_brief.md",
 "brief_sha256": "see ledger entry; the brief is unchanged since calibration",
 "sample_size": 12,
 "acceptance_set_before_rating": {
  "mean_abs_diff_per_demand_max": 0.5,
  "self_diff_per_demand_max": 0.5,
  "done_agreement_min": 0.875
 },
 "reference": "planted by the series author (fable): calib.md (8 replies, 14 planted demands) and calib2.md (4 replies, d35 after its text was amended to count distinct literals); no human rater",
 "runs": "two sonnet agents per packet, each alone, same brief",
 "agreement_planted": {
  "calib": {
   "max_mad_a": 0.75,
   "max_mad_b": 0.5,
   "max_self": 0.38,
   "miss": "d35-names in run A (0.75) before the amendment",
   "done_agreement": [
    0.875,
    1.0
   ]
  },
  "calib2": {
   "d35-names": {
    "mad_a": 0.5,
    "mad_b": 0.5,
    "self": 0.5
   },
   "done_agreement": [
    1.0,
    1.0
   ]
  }
 },
 "accepted": true,
 "limits": [
  "The reference plants breaches on named demands; it cannot measure false positives on demands the author did not plant. The judge counted 1 to 3 unplanted breaches per flawed reply (scale 2.1 against the planted totals) and 0 to 2 on clean replies, most often d12-invalid-states, d19-constructs, d10-guess, d13-silent-failure.",
  "Both arms of every comparison in the series are judged by the same configuration, so the over-count shifts every condition alike; absolute counts are not comparable to another judge's.",
  "Deviation from calibrate-eval-judge: calib2 is a fresh sample for the missed demand only, not a full fresh sample."
 ],
 "details": "agreement.json (calib), judge/calib2.verdict.json and judge/calib2.verdict-b.json (calib2)"
}
```

## Results, split `all`

| condition | n | mean violations | script part | done rate | words | secs | leak rate |
|---|---|---|---|---|---|---|---|
| none | 23 | 12.30 | 1.61 | 0.96 | 213 | 26.8 | 0.043 |
| full | 23 | 15.44 | 1.96 | 1.00 | 312 | 90.6 | 0.000 |
| placebo | 23 | 9.44 | 1.61 | 0.96 | 170 | 22.7 | 0.000 |
| terse | 23 | 7.30 | 0.61 | 0.96 | 121 | 21.5 | 0.043 |
| digest | 23 | 6.04 | 0.30 | 0.91 | 96 | 14.7 | 0.043 |

Digest minus baseline, paired by task (mean difference, interval):

| baseline | n | mean diff | ci low | ci high |
|---|---|---|---|---|
| none | 23 | -6.261 | -10.565 | -2.870 |
| full | 23 | -9.391 | -14.870 | -4.391 |
| placebo | 23 | -3.391 | -6.087 | -0.826 |
| terse | 23 | -1.261 | -3.870 | 1.174 |

Drift (per-turn slope of violations over the sessions):

| condition | sessions | slope | ci low | ci high | mean violations |
|---|---|---|---|---|---|
| none | 2 | 1.732 | 1.179 | 2.286 | 15.69 |
| digest | 2 | 1.274 | 1.226 | 1.321 | 8.00 |
| full | 2 | 0.595 | 0.524 | 0.667 | 15.38 |
| placebo | 2 | 0.940 | -0.929 | 2.810 | 17.62 |
| terse | 2 | 1.327 | 0.893 | 1.762 | 14.81 |

## Results, split `test`

| condition | n | mean violations | script part | done rate | words | secs | leak rate |
|---|---|---|---|---|---|---|---|
| none | 12 | 12.08 | 1.33 | 1.00 | 224 | 31.2 | 0.083 |
| full | 12 | 19.17 | 2.08 | 1.00 | 371 | 126.1 | 0.000 |
| placebo | 12 | 10.67 | 1.92 | 1.00 | 204 | 26.0 | 0.000 |
| terse | 12 | 7.92 | 0.83 | 0.92 | 137 | 28.4 | 0.083 |
| digest | 12 | 7.08 | 0.33 | 0.83 | 108 | 17.1 | 0.083 |

Digest minus baseline, paired by task (mean difference, interval):

| baseline | n | mean diff | ci low | ci high |
|---|---|---|---|---|
| none | 12 | -5.000 | -9.000 | -1.083 |
| full | 12 | -12.083 | -21.250 | -4.083 |
| placebo | 12 | -3.583 | -8.333 | 0.417 |
| terse | 12 | -0.833 | -3.083 | 1.667 |

Drift (per-turn slope of violations over the sessions):

| condition | sessions | slope | ci low | ci high | mean violations |
|---|---|---|---|---|---|
| none | 1 | 1.179 | n/a | n/a | 17.38 |
| digest | 1 | 1.226 | n/a | n/a | 6.88 |
| full | 1 | 0.524 | n/a | n/a | 14.25 |
| placebo | 1 | -0.929 | n/a | n/a | 20.00 |
| terse | 1 | 0.893 | n/a | n/a | 13.12 |

## Results, split `dev`

| condition | n | mean violations | script part | done rate | words | secs | leak rate |
|---|---|---|---|---|---|---|---|
| none | 11 | 12.54 | 1.91 | 0.91 | 200 | 22.1 | 0.000 |
| full | 11 | 11.36 | 1.82 | 1.00 | 248 | 51.9 | 0.000 |
| placebo | 11 | 8.09 | 1.27 | 0.91 | 133 | 19.1 | 0.000 |
| terse | 11 | 6.64 | 0.36 | 1.00 | 103 | 14.0 | 0.000 |
| digest | 11 | 4.91 | 0.27 | 1.00 | 84 | 12.1 | 0.000 |

Digest minus baseline, paired by task (mean difference, interval):

| baseline | n | mean diff | ci low | ci high |
|---|---|---|---|---|
| none | 11 | -7.636 | -15.182 | -1.273 |
| full | 11 | -6.455 | -11.636 | -1.636 |
| placebo | 11 | -3.182 | -6.636 | -0.182 |
| terse | 11 | -1.727 | -6.364 | 2.455 |

Drift (per-turn slope of violations over the sessions):

| condition | sessions | slope | ci low | ci high | mean violations |
|---|---|---|---|---|---|
| none | 1 | 2.286 | n/a | n/a | 14.00 |
| digest | 1 | 1.321 | n/a | n/a | 9.12 |
| full | 1 | 0.667 | n/a | n/a | 16.50 |
| placebo | 1 | 2.810 | n/a | n/a | 15.25 |
| terse | 1 | 1.762 | n/a | n/a | 16.50 |

## Per-demand mean violations per reply, split `all`

| demand | check | none | full | placebo | terse | digest | text |
|---|---|---|---|---|---|---|---|
| d01-opening | script | 0.39 | 0.35 | 0.30 | 0.17 | 0.04 | Open with the first word of substance; no greeting, preamble, pleasantry, or remark on the |
| d02-hedge | script | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | State what you know as fact; no hedge. |
| d03-filler | script | 0.30 | 0.83 | 0.26 | 0.13 | 0.13 | No filler word or softener. |
| d04-connective | script | 0.00 | 0.00 | 0.04 | 0.00 | 0.04 | No connective such as however, furthermore, additionally, moreover. |
| d05-long-sentence | script | 0.91 | 0.78 | 0.96 | 0.30 | 0.09 | No sentence over fifteen words (prose outside code). |
| d06-restate | judge | 0.26 | 0.70 | 0.48 | 0.09 | 0.17 | The reply restates what the user said or wrote. |
| d07-exact | judge | 1.04 | 1.13 | 0.74 | 0.78 | 0.78 | The reply gives a vague term, paraphrased code, or an approximate error, path, command, nu |
| d08-invalidate | judge | 0.22 | 0.52 | 0.22 | 0.26 | 0.17 | The reply asserts a result, cause, or claim without naming what could make it invalid (oth |
| d09-implication | judge | 0.35 | 0.61 | 0.39 | 0.22 | 0.09 | The reply makes a true statement that carries a false implication and does not add the cor |
| d10-guess | judge | 0.35 | 0.43 | 0.09 | 0.22 | 0.35 | The request is ambiguous and the reply guesses instead of asking or stating the assumption |
| d11-baseline | judge | 0.04 | 0.04 | 0.09 | 0.00 | 0.09 | The reply claims a cause or recommends changing a condition without reproducing the baseli |
| d12-invalid-states | judge | 0.26 | 0.22 | 0.26 | 0.09 | 0.13 | Code in the reply lets an invalid state be expressed (contradictory flags, optional fields |
| d13-silent-failure | judge | 0.43 | 0.35 | 0.43 | 0.22 | 0.13 | Code in the reply hides failure: a bare except, a swallowed error, unwrap without reason,  |
| d14-ownership | judge | 0.04 | 0.04 | 0.04 | 0.00 | 0.00 | Code in the reply shares mutable state without one owner or explicit synchronization. |
| d15-signatures | judge | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | The reply writes bodies before modelling the domain in types and signatures, or omits test |
| d16-overstrict | judge | 0.13 | 0.13 | 0.04 | 0.00 | 0.09 | The reply adds strictness, validation, or typing the domain does not require. |
| d17-class-per-record | judge | 0.00 | 0.04 | 0.04 | 0.00 | 0.00 | The reply wraps plain information in a class where a map, set, or sequence fits. |
| d18-simple-vs-easy | judge | 0.13 | 0.04 | 0.13 | 0.04 | 0.00 | The reply picks the familiar tangled option over a simpler one, or mixes concerns (data ac |
| d19-constructs | judge | 0.13 | 0.17 | 0.13 | 0.09 | 0.13 | The reply uses mutable state, methods, inheritance, or scattered conditionals where values |
| d20-explicit | judge | 0.26 | 0.09 | 0.13 | 0.13 | 0.13 | The reply's code is implicit, nested, or dense where explicit, flat, or sparse was availab |
| d21-one-home | judge | 0.43 | 0.65 | 0.13 | 0.22 | 0.09 | The reply puts one piece of knowledge in two places. |
| d22-rule-of-three | judge | 0.13 | 0.04 | 0.09 | 0.09 | 0.04 | The reply abstracts, generalizes, or introduces an interface before a third instance or a  |
| d23-wrong-abstraction | judge | 0.09 | 0.00 | 0.09 | 0.04 | 0.04 | The reply keeps or grows a shared abstraction with new parameters or branches instead of i |
| d24-ruled-out | judge | 0.39 | 0.35 | 0.30 | 0.22 | 0.22 | The reply adds code without naming what it ruled out (existing code, a configuration chang |
| d25-least-code | judge | 0.65 | 0.56 | 0.35 | 0.26 | 0.26 | The reply writes more code than the task needs, or prefers a shorter version harder to cha |
| d26-caller-or-test | judge | 0.56 | 0.48 | 0.43 | 0.22 | 0.26 | The reply adds a function, type, or file with no caller or test in the same change, or lea |
| d27-new-path | judge | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | The reply adds a new code path beside an existing one instead of changing the existing one |
| d28-dependency | judge | 0.48 | 0.35 | 0.22 | 0.30 | 0.26 | The reply adds or recommends a dependency without opening its source, running its tests, n |
| d29-generated | judge | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | The reply endorses merging generated or pasted code unread or not understood. |
| d30-progress | judge | 0.00 | 0.09 | 0.00 | 0.00 | 0.00 | The reply reports lines added as progress, or reports a deletion without naming the protec |
| d31-yagni | judge | 0.91 | 1.04 | 0.70 | 0.52 | 0.39 | The reply adds a field, method, option, abstraction, or edge case that nothing present ask |
| d32-foundations | judge | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | The reply defers a foundation (language, database, platform, security) to later or builds  |
| d33-method-size | judge | 0.39 | 0.26 | 0.22 | 0.22 | 0.13 | The reply's code has a function over twenty lines or with more than one responsibility, a  |
| d34-ship | judge | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | The reply types before thinking or modelling, or withholds shipping code that compiles and |
| d35-names | judge | 1.48 | 1.39 | 1.39 | 1.26 | 1.30 | The reply names a thing for its implementation, leaves a bare number or string in logic, o |
| d36-comments | judge | 2.70 | 5.43 | 2.13 | 1.65 | 0.65 | The reply's code carries a comment explaining what the code does, or a comment not giving  |
| d37-first-truths | judge | 0.35 | 0.22 | 0.13 | 0.17 | 0.13 | The reply justifies a choice by resemblance, convention, or industry standard rather than  |
| d38-bug-cause | judge | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | The reply fixes a bug without working out how it came to be. |
| d39-measure | judge | 0.09 | 0.04 | 0.04 | 0.00 | 0.00 | The reply optimizes or recommends optimizing without a measurement. |

## Gate, cut-3

Split `test`; pass: **False**; changed vs previous: False.

| check | pass | value | threshold |
|---|---|---|---|
| cut vs none: paired mean difference at or below the threshold and its interval excludes zero | True | `{"n": 12, "mean_diff": -5.0, "ci_low": -9.0, "ci_high": -1.083}` | -1.0 |
| near full: digest minus full at or below the margin | True | `{"n": 12, "mean_diff": -12.083, "ci_low": -21.25, "ci_high": -4.083}` | 1.0 |
| beats terse: interval of digest minus terse lies below zero | False | `{"n": 12, "mean_diff": -0.833, "ci_low": -3.083, "ci_high": 1.667}` | 0 |
| beats placebo: interval of digest minus placebo lies below zero | False | `{"n": 12, "mean_diff": -3.583, "ci_low": -8.333, "ci_high": 0.417}` | 0 |
| completion: digest done rate within the margin of the best baseline | False | `0.833` | 0.9 |
| drift: digest slope minus full slope at or below the margin | False | `0.702` | 0.1 |

## Ledger entry (instrument fields)

```json
{
 "ts": "2026-10-13T12:51:44",
 "slug": "cargo-cult-science+correct-by-construction+dry+first-principles+kiss+lines-spent+self-documenting-code+simple-made-easy+stop-yapping+yagni+zen-of-python",
 "cut": 3,
 "kind": "cut",
 "run_dir": "cut-3",
 "digest_path": ".claude/digests/cargo-cult-science+correct-by-construction+dry+first-principles+kiss+lines-spent+self-documenting-code+simple-made-easy+stop-yapping+yagni+zen-of-python.md",
 "digest_sha256": "a5455b97bfd40b7bfcb21699b26bd8f6ee60a97e58ddcccb62d1aa62835f37f4",
 "digest_words": 849,
 "reader": {
  "adapter": "pi",
  "model": "long"
 },
 "judge": {
  "name": "sonnet-agents",
  "brief_sha256": "68c1b43f70b39b4fc5f7b435533bd8c0f011591e5faae0898146ebbc4cf29fd3"
 },
 "spec_sha256": "83fee034963314aa3df23796e886ebcc07809fbe8828c12bc3c00da194579dea",
 "tasks_sha256": "94263e57a022a416580c903faa949fdbd9d53f53246c6e1d8242b3fde6aef766",
 "tool_version": "0.1.0",
 "hypothesis": "d07-exact: the reader fills demanded exactness with invented numbers, placeholder code, and code that does not compile; the sentence orders exact-looking output and forbids no invention.",
 "change": {
  "old": "Give code verbatim and the exact term, error, path, command, number, and version, then the next step.",
  "new": "Give runnable code and the exact terms, errors, paths, commands, numbers, and versions you know; never invent one."
 },
 "manifestos": "11 paths with versions (see ledger.jsonl)",
 "members": "11 member digests with sha256 (see ledger.jsonl)"
}
```

## This cut: the diagnosis and the one change (read from cut-3/hypothesis.md and cut.json)

Failing checks (cut-2, test split): "beats terse" (digest minus terse +0.08, interval [-2.17, 2.5]), "beats placebo" (-2.42, interval [-6.17, 1.17]), "drift" (digest slope 0.51 against full -0.23, margin 0.1).

Failing demand (dev split): d07-exact. Per-reply mean on dev: digest 0.73, terse 0.73, full 0.82, placebo 0.73, none 0.36: the highest-counted judged demand on the digest after names and comments, equal to terse, and the demand that rises most through the dev session (early turns 2.0, late turns 2.67 per reply). The widest digest-minus-terse gap by a single demand is d26-caller-or-test (+0.18), too small to carry a check; d07 is the one shared by the terse and drift failures.

Replies read (dev, digest condition): first-optimize, lines-helper, shape-explain, simple-three, types-except, and sess-rust turns 1, 2, 3, 6, 7, 8, beside the full and terse replies to the same tasks.

Cause, from the replies: the reader fills the exactness the digest demands with invented specifics. It writes placeholder code (`/* operation */`, `// ...`, a verify step that never calls the function), invents benchmark numbers ("12.3 ± 0.5ms (n=100)") and a table with an ellipsis for the states, and ships Rust that does not compile. The digest's sentence "Give code verbatim and the exact term, error, path, command, number, and version, then the next step." reads to the reader as an order to produce exact-looking things, not as an order to give only what it knows; nothing in the digest forbids invention or placeholders.

One change: replace that sentence with "Give runnable code and the exact terms, errors, paths, commands, numbers, and versions you know; never invent one." (18 words; the digest stays at 848 words.)

Expected movement: d07-exact on the digest condition falls from 0.73 toward 0.4 on dev and its late-turn count falls below its early-turn count in the dev session; the digest drift slope falls toward the full text's. Digest minus terse on the test split moves about -0.3 per reply, inside the interval half-width (about 2.3 on 12 pairs), so the terse check is not expected to flip on this change alone.

```json
{
 "cut": 3,
 "parent": 2,
 "sha256": "a5455b97bfd40b7bfcb21699b26bd8f6ee60a97e58ddcccb62d1aa62835f37f4",
 "hypothesis": "d07-exact: the reader fills demanded exactness with invented numbers, placeholder code, and code that does not compile; the sentence orders exact-looking output and forbids no invention.",
 "change": {
  "old": "Give code verbatim and the exact term, error, path, command, number, and version, then the next step.",
  "new": "Give runnable code and the exact terms, errors, paths, commands, numbers, and versions you know; never invent one."
 }
}
```

Hypothesis check, mean `d07-exact` violations per reply on the digest condition (this cut against its parent):

| split | cut-2 | cut-3 |
|---|---|---|
| dev | 0.73 | 0.46 |
| test | 1.17 | 1.08 |
| all | 0.96 | 0.78 |

## Stop rule

changed_vs_previous: cut-2 = False, cut-3 = False. Gate pass: False. The series stops on a gate pass, on two cuts in a row with changed_vs_previous false, or after five cuts.

Two cuts in a row show changed_vs_previous false (the paired difference against the previous cut has an interval holding zero): the series stops here.

## Caveats

- This cut re-ran the digest condition alone (39 replies). The other conditions' replies are cut-1's, borrowed into the packets (`blind --borrow cut-1`) and judged afresh in this pass, so their means differ slightly from cut-1's own report: the difference is the judge's run-to-run noise.
- The judge brief names the manifesto text by its path, `cut-1/conditions/full.txt`, the 11 member manifestos concatenated; the same path was used in cut-2.
- Repeats were capped at 1; reader sampling is unseeded. The test split holds 12 paired tasks, so intervals are wide; one session per condition per language.
- The tool's drift check reads two session slopes per condition (one per split); a slope here is a mean of at most two sessions.

— measured by Claude (sonnet series driver), 2026-10-13, rendered from files
