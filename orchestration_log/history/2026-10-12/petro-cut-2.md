# Petro stack digest, cut-2: data (frozen 2026-10-13)

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
| none | 23 | 13.22 | 1.61 | 0.96 | 213 | 26.8 | 0.043 |
| full | 23 | 16.22 | 1.96 | 1.00 | 312 | 90.6 | 0.000 |
| placebo | 23 | 10.09 | 1.61 | 0.96 | 170 | 22.7 | 0.000 |
| terse | 23 | 7.57 | 0.61 | 0.96 | 121 | 21.5 | 0.043 |
| digest | 23 | 6.78 | 0.56 | 0.96 | 108 | 16.6 | 0.000 |

Digest minus baseline, paired by task (mean difference, interval):

| baseline | n | mean diff | ci low | ci high |
|---|---|---|---|---|
| none | 23 | -6.435 | -11.565 | -2.087 |
| full | 23 | -9.435 | -15.043 | -4.957 |
| placebo | 23 | -3.304 | -6.348 | -0.348 |
| terse | 23 | -0.783 | -2.348 | 0.870 |

Drift (per-turn slope of violations over the sessions):

| condition | sessions | slope | ci low | ci high | mean violations |
|---|---|---|---|---|---|
| none | 2 | 1.613 | 1.060 | 2.167 | 15.81 |
| digest | 2 | 0.875 | 0.512 | 1.238 | 8.19 |
| full | 2 | 0.018 | -0.226 | 0.262 | 15.81 |
| placebo | 2 | 1.042 | -0.643 | 2.726 | 15.19 |
| terse | 2 | 1.327 | 0.631 | 2.024 | 13.81 |

## Results, split `test`

| condition | n | mean violations | script part | done rate | words | secs | leak rate |
|---|---|---|---|---|---|---|---|
| none | 12 | 12.92 | 1.33 | 1.00 | 224 | 31.2 | 0.083 |
| full | 12 | 20.17 | 2.08 | 1.00 | 371 | 126.1 | 0.000 |
| placebo | 12 | 10.92 | 1.92 | 1.00 | 204 | 26.0 | 0.000 |
| terse | 12 | 8.42 | 0.83 | 0.92 | 137 | 28.4 | 0.083 |
| digest | 12 | 8.50 | 0.67 | 0.92 | 129 | 19.2 | 0.000 |

Digest minus baseline, paired by task (mean difference, interval):

| baseline | n | mean diff | ci low | ci high |
|---|---|---|---|---|
| none | 12 | -4.417 | -8.583 | -0.417 |
| full | 12 | -11.667 | -21.583 | -4.083 |
| placebo | 12 | -2.417 | -6.167 | 1.167 |
| terse | 12 | 0.083 | -2.167 | 2.500 |

Drift (per-turn slope of violations over the sessions):

| condition | sessions | slope | ci low | ci high | mean violations |
|---|---|---|---|---|---|
| none | 1 | 1.060 | n/a | n/a | 16.12 |
| digest | 1 | 0.512 | n/a | n/a | 7.12 |
| full | 1 | -0.226 | n/a | n/a | 13.38 |
| placebo | 1 | -0.643 | n/a | n/a | 16.00 |
| terse | 1 | 0.631 | n/a | n/a | 11.12 |

## Results, split `dev`

| condition | n | mean violations | script part | done rate | words | secs | leak rate |
|---|---|---|---|---|---|---|---|
| none | 11 | 13.54 | 1.91 | 0.91 | 200 | 22.1 | 0.000 |
| full | 11 | 11.91 | 1.82 | 1.00 | 248 | 51.9 | 0.000 |
| placebo | 11 | 9.18 | 1.27 | 0.91 | 133 | 19.1 | 0.000 |
| terse | 11 | 6.64 | 0.36 | 1.00 | 103 | 14.0 | 0.000 |
| digest | 11 | 4.91 | 0.46 | 1.00 | 84 | 13.8 | 0.000 |

Digest minus baseline, paired by task (mean difference, interval):

| baseline | n | mean diff | ci low | ci high |
|---|---|---|---|---|
| none | 11 | -8.636 | -19.182 | -0.545 |
| full | 11 | -7.000 | -11.000 | -3.000 |
| placebo | 11 | -4.273 | -9.182 | 0.182 |
| terse | 11 | -1.727 | -3.727 | 0.364 |

Drift (per-turn slope of violations over the sessions):

| condition | sessions | slope | ci low | ci high | mean violations |
|---|---|---|---|---|---|
| none | 1 | 2.167 | n/a | n/a | 15.50 |
| digest | 1 | 1.238 | n/a | n/a | 9.25 |
| full | 1 | 0.262 | n/a | n/a | 18.25 |
| placebo | 1 | 2.726 | n/a | n/a | 14.38 |
| terse | 1 | 2.024 | n/a | n/a | 16.50 |

## Per-demand mean violations per reply, split `all`

| demand | check | none | full | placebo | terse | digest | text |
|---|---|---|---|---|---|---|---|
| d01-opening | script | 0.39 | 0.35 | 0.30 | 0.17 | 0.13 | Open with the first word of substance; no greeting, preamble, pleasantry, or remark on the |
| d02-hedge | script | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | State what you know as fact; no hedge. |
| d03-filler | script | 0.30 | 0.83 | 0.26 | 0.13 | 0.09 | No filler word or softener. |
| d04-connective | script | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | No connective such as however, furthermore, additionally, moreover. |
| d05-long-sentence | script | 0.91 | 0.78 | 0.96 | 0.30 | 0.35 | No sentence over fifteen words (prose outside code). |
| d06-restate | judge | 0.35 | 0.91 | 0.61 | 0.09 | 0.13 | The reply restates what the user said or wrote. |
| d07-exact | judge | 0.78 | 1.26 | 0.96 | 0.87 | 0.96 | The reply gives a vague term, paraphrased code, or an approximate error, path, command, nu |
| d08-invalidate | judge | 0.43 | 0.65 | 0.39 | 0.13 | 0.17 | The reply asserts a result, cause, or claim without naming what could make it invalid (oth |
| d09-implication | judge | 0.35 | 0.56 | 0.35 | 0.22 | 0.13 | The reply makes a true statement that carries a false implication and does not add the cor |
| d10-guess | judge | 0.35 | 0.43 | 0.09 | 0.26 | 0.13 | The request is ambiguous and the reply guesses instead of asking or stating the assumption |
| d11-baseline | judge | 0.13 | 0.13 | 0.13 | 0.04 | 0.13 | The reply claims a cause or recommends changing a condition without reproducing the baseli |
| d12-invalid-states | judge | 0.30 | 0.22 | 0.22 | 0.09 | 0.09 | Code in the reply lets an invalid state be expressed (contradictory flags, optional fields |
| d13-silent-failure | judge | 0.43 | 0.26 | 0.48 | 0.26 | 0.22 | Code in the reply hides failure: a bare except, a swallowed error, unwrap without reason,  |
| d14-ownership | judge | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | Code in the reply shares mutable state without one owner or explicit synchronization. |
| d15-signatures | judge | 0.04 | 0.04 | 0.04 | 0.00 | 0.04 | The reply writes bodies before modelling the domain in types and signatures, or omits test |
| d16-overstrict | judge | 0.09 | 0.26 | 0.09 | 0.04 | 0.00 | The reply adds strictness, validation, or typing the domain does not require. |
| d17-class-per-record | judge | 0.00 | 0.04 | 0.04 | 0.00 | 0.00 | The reply wraps plain information in a class where a map, set, or sequence fits. |
| d18-simple-vs-easy | judge | 0.09 | 0.00 | 0.00 | 0.09 | 0.00 | The reply picks the familiar tangled option over a simpler one, or mixes concerns (data ac |
| d19-constructs | judge | 0.17 | 0.17 | 0.13 | 0.13 | 0.17 | The reply uses mutable state, methods, inheritance, or scattered conditionals where values |
| d20-explicit | judge | 0.26 | 0.13 | 0.13 | 0.13 | 0.13 | The reply's code is implicit, nested, or dense where explicit, flat, or sparse was availab |
| d21-one-home | judge | 0.56 | 0.74 | 0.26 | 0.30 | 0.26 | The reply puts one piece of knowledge in two places. |
| d22-rule-of-three | judge | 0.13 | 0.04 | 0.09 | 0.09 | 0.09 | The reply abstracts, generalizes, or introduces an interface before a third instance or a  |
| d23-wrong-abstraction | judge | 0.09 | 0.04 | 0.09 | 0.04 | 0.04 | The reply keeps or grows a shared abstraction with new parameters or branches instead of i |
| d24-ruled-out | judge | 0.35 | 0.30 | 0.26 | 0.22 | 0.22 | The reply adds code without naming what it ruled out (existing code, a configuration chang |
| d25-least-code | judge | 0.52 | 0.70 | 0.35 | 0.26 | 0.13 | The reply writes more code than the task needs, or prefers a shorter version harder to cha |
| d26-caller-or-test | judge | 0.48 | 0.52 | 0.35 | 0.26 | 0.30 | The reply adds a function, type, or file with no caller or test in the same change, or lea |
| d27-new-path | judge | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | The reply adds a new code path beside an existing one instead of changing the existing one |
| d28-dependency | judge | 0.43 | 0.48 | 0.17 | 0.35 | 0.17 | The reply adds or recommends a dependency without opening its source, running its tests, n |
| d29-generated | judge | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | The reply endorses merging generated or pasted code unread or not understood. |
| d30-progress | judge | 0.00 | 0.09 | 0.04 | 0.04 | 0.09 | The reply reports lines added as progress, or reports a deletion without naming the protec |
| d31-yagni | judge | 1.13 | 1.04 | 0.74 | 0.52 | 0.52 | The reply adds a field, method, option, abstraction, or edge case that nothing present ask |
| d32-foundations | judge | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | The reply defers a foundation (language, database, platform, security) to later or builds  |
| d33-method-size | judge | 0.35 | 0.22 | 0.30 | 0.17 | 0.17 | The reply's code has a function over twenty lines or with more than one responsibility, a  |
| d34-ship | judge | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | The reply types before thinking or modelling, or withholds shipping code that compiles and |
| d35-names | judge | 1.70 | 1.61 | 1.48 | 1.13 | 1.13 | The reply names a thing for its implementation, leaves a bare number or string in logic, o |
| d36-comments | judge | 3.22 | 5.17 | 2.04 | 1.65 | 1.17 | The reply's code carries a comment explaining what the code does, or a comment not giving  |
| d37-first-truths | judge | 0.30 | 0.09 | 0.22 | 0.13 | 0.17 | The reply justifies a choice by resemblance, convention, or industry standard rather than  |
| d38-bug-cause | judge | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | The reply fixes a bug without working out how it came to be. |
| d39-measure | judge | 0.09 | 0.04 | 0.04 | 0.04 | 0.00 | The reply optimizes or recommends optimizing without a measurement. |

## Gate, cut-2

Split `test`; pass: **False**; changed vs previous: False.

| check | pass | value | threshold |
|---|---|---|---|
| cut vs none: paired mean difference at or below the threshold and its interval excludes zero | True | `{"n": 12, "mean_diff": -4.417, "ci_low": -8.583, "ci_high": -0.417}` | -1.0 |
| near full: digest minus full at or below the margin | True | `{"n": 12, "mean_diff": -11.667, "ci_low": -21.583, "ci_high": -4.083}` | 1.0 |
| beats terse: interval of digest minus terse lies below zero | False | `{"n": 12, "mean_diff": 0.083, "ci_low": -2.167, "ci_high": 2.5}` | 0 |
| beats placebo: interval of digest minus placebo lies below zero | False | `{"n": 12, "mean_diff": -2.417, "ci_low": -6.167, "ci_high": 1.167}` | 0 |
| completion: digest done rate within the margin of the best baseline | True | `0.917` | 0.9 |
| drift: digest slope minus full slope at or below the margin | False | `0.738` | 0.1 |

## Ledger entry (instrument fields)

```json
{
 "ts": "2026-10-12T23:36:26",
 "slug": "cargo-cult-science+correct-by-construction+dry+first-principles+kiss+lines-spent+self-documenting-code+simple-made-easy+stop-yapping+yagni+zen-of-python",
 "cut": 2,
 "kind": "cut",
 "run_dir": "cut-2",
 "digest_path": ".claude/digests/cargo-cult-science+correct-by-construction+dry+first-principles+kiss+lines-spent+self-documenting-code+simple-made-easy+stop-yapping+yagni+zen-of-python.md",
 "digest_sha256": "c48427f70190ed55905b039d6e3139fe5479b3531523a14390091e6c2768316c",
 "digest_words": 848,
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
 "hypothesis": "d06-restate: the reader pastes the user's code back and recaps the request; the sentence names speech, not pasted code, and gives nothing to show instead.",
 "change": {
  "old": "Never restate what the user said.",
  "new": "Never repeat the user's words or pasted code; show the changed lines alone."
 },
 "manifestos": "11 paths with versions (see ledger.jsonl)",
 "members": "11 member digests with sha256 (see ledger.jsonl)"
}
```

## This cut: the diagnosis and the one change (read from cut-2/hypothesis.md and cut.json)

Failing check (cut-1, test split): "beats terse", digest minus terse mean -1.5, interval [-3.75, 0.58] crosses zero.

Failing demand (dev split): d06-restate. Per-reply mean on dev: digest 0.36, terse 0.09, none 0.27, full 0.36, placebo 0.36; the widest digest-minus-terse gap (+0.27) of any demand.

Replies read (dev, digest condition): tcam6 (first-optimize), 6ra2d (lines-helper), ku6ww (shape-greeting), wcznd (simple-three), beside the terse replies to the same tasks.

Cause, from the replies: the digest reader pastes the user's own code back in full before or after its change (lines-helper repeats the whole module to add one function; simple-three repeats both functions under "Keep as-is"), and closes with a one-line recap of what the user asked ("This returns the last three items"). The digest's sentence "Never restate what the user said." names speech, not pasted code, and gives no positive instruction for what to show instead; the reader reads "restate" as paraphrasing a sentence and does not apply it to code it was handed.

One change: replace the sentence "Never restate what the user said." with "Never repeat the user's words or pasted code; show the changed lines alone." (A longer first wording pushed the digest to 857 words, over the 850 cap; shortened before any cut-2 reply was kept.)

Expected movement: d06-restate on the digest condition falls from 0.36 toward the terse condition's 0.09 on dev; digest minus terse on the test split moves about -0.3 per reply. That is inside the previous cut's interval half-width (about 2.2 on 12 pairs), so the gate's terse check is not expected to flip on this change alone; the change is expected to show as a per-demand drop, and the paired difference against cut-1 to stay inside noise.

```json
{
 "cut": 2,
 "parent": 1,
 "sha256": "c48427f70190ed55905b039d6e3139fe5479b3531523a14390091e6c2768316c",
 "hypothesis": "d06-restate: the reader pastes the user's code back and recaps the request; the sentence names speech, not pasted code, and gives nothing to show instead.",
 "change": {
  "old": "Never restate what the user said.",
  "new": "Never repeat the user's words or pasted code; show the changed lines alone."
 }
}
```

Hypothesis check, mean `d06-restate` violations per reply on the digest condition (this cut against its parent):

| split | cut-1 | cut-2 |
|---|---|---|
| dev | 0.36 | 0.00 |
| test | 0.42 | 0.25 |
| all | 0.39 | 0.13 |

## Stop rule

changed_vs_previous: cut-1 = None, cut-2 = False. Gate pass: False. The series stops on a gate pass, on two cuts in a row with changed_vs_previous false, or after five cuts.

## Caveats

- This cut re-ran the digest condition alone (39 replies). The other conditions' replies are cut-1's, borrowed into the packets (`blind --borrow cut-1`) and judged afresh in this pass, so their means differ slightly from cut-1's own report: the difference is the judge's run-to-run noise.
- The judge brief names the manifesto text by its path, `cut-1/conditions/full.txt`, the 11 member manifestos concatenated; the same path was used in cut-2.
- Repeats were capped at 1; reader sampling is unseeded. The test split holds 12 paired tasks, so intervals are wide; one session per condition per language.
- The tool's drift check reads two session slopes per condition (one per split); a slope here is a mean of at most two sessions.

— measured by Claude (sonnet series driver), 2026-10-13, rendered from files
