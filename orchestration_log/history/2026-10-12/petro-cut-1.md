# Petro stack digest, cut-1: data (frozen 2026-10-12)

Rendered by script from the local-only eval dir `cargo-cult-science+correct-by-construction+dry+first-principles+kiss+lines-spent+self-documenting-code+simple-made-easy+stop-yapping+yagni+zen-of-python` (outside the repo, in `/Users/ryzhakar/petro/evals/`). Mean violations are per reply; a demand can fire more than once in a reply. Reader sampling is unseeded (`pi` has no seed or temperature flag). Wall seconds are per reply on the local llama-server.

## Instrument

- Reader: `{"adapter": "pi", "model": "long"}`; judge: `{"name": "sonnet-agents", "brief": "judge_brief.md"}`.
- Gate: `{"split": "test", "ci": 0.95, "min_cut_vs_none": 1.0, "margin_vs_full": 1.0, "completion_margin": 0.1, "drift_margin": 0.1}`.
- Conditions: `{"baselines": ["full", "terse", "placebo"], "terse_line": "Answer briefly and precisely, and write careful, minimal, well-typed Python and Rust.", "placebo_source": "/Users/ryzhakar/petro/evals/cargo-cult-science+correct-by-construction+dry+first-principles+kiss+lines-spent+self-documenting-code+simple-made-easy+stop-yapping+yagni+zen-of-python/placebo.md", "ablations": false}`.
- Reps: `1`; spec note: Cut 1 sized to the 90-minute reader budget at the measured 28 s per reply: 23 singles x 1 rep x 5 conditions plus 2 sessions x 8 turns x 5 conditions = 195 replies. The reps rule (digest-eval reps on cut-1-aborted, script-judge proxy) on 7 script-proxy pairs, spread 1.245, asked for 2 over 12 test tasks; capped at 1 for the budget. Spec frozen before the first reply of cut-1; cut-1-aborted ran under the earlier spec (reps 2, 3 sessions x 10 turns) and was stopped at 36 replies..
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
| none | 23 | 12.96 | 1.61 | 0.96 | 213 | 26.8 | 0.043 |
| full | 23 | 14.35 | 1.96 | 1.00 | 312 | 90.6 | 0.000 |
| placebo | 23 | 9.13 | 1.61 | 0.96 | 170 | 22.7 | 0.000 |
| terse | 23 | 7.52 | 0.61 | 0.96 | 121 | 21.5 | 0.043 |
| digest | 23 | 6.22 | 0.65 | 1.00 | 120 | 19.2 | 0.000 |

Digest minus baseline, paired by task (mean difference, interval):

| baseline | n | mean diff | ci low | ci high |
|---|---|---|---|---|
| none | 23 | -6.739 | -11.130 | -3.130 |
| full | 23 | -8.130 | -12.783 | -3.957 |
| placebo | 23 | -2.913 | -4.783 | -1.130 |
| terse | 23 | -1.304 | -3.087 | 0.391 |

Drift (per-turn slope of violations over the sessions):

| condition | sessions | slope | ci low | ci high | mean violations |
|---|---|---|---|---|---|
| none | 2 | 1.077 | 0.655 | 1.500 | 11.94 |
| digest | 2 | 0.351 | -0.333 | 1.036 | 5.81 |
| full | 2 | 0.690 | 0.619 | 0.762 | 12.25 |
| placebo | 2 | 0.893 | -0.321 | 2.107 | 13.38 |
| terse | 2 | 0.643 | 0.214 | 1.071 | 10.62 |

## Results, split `test`

| condition | n | mean violations | script part | done rate | words | secs | leak rate |
|---|---|---|---|---|---|---|---|
| none | 12 | 11.92 | 1.33 | 1.00 | 224 | 31.2 | 0.083 |
| full | 12 | 17.42 | 2.08 | 1.00 | 371 | 126.1 | 0.000 |
| placebo | 12 | 9.67 | 1.92 | 1.00 | 204 | 26.0 | 0.000 |
| terse | 12 | 8.00 | 0.83 | 0.92 | 137 | 28.4 | 0.083 |
| digest | 12 | 6.50 | 0.83 | 1.00 | 136 | 23.4 | 0.000 |

Digest minus baseline, paired by task (mean difference, interval):

| baseline | n | mean diff | ci low | ci high |
|---|---|---|---|---|
| none | 12 | -5.417 | -9.417 | -1.333 |
| full | 12 | -10.917 | -18.333 | -4.083 |
| placebo | 12 | -3.167 | -6.333 | -0.417 |
| terse | 12 | -1.500 | -3.750 | 0.583 |

Drift (per-turn slope of violations over the sessions):

| condition | sessions | slope | ci low | ci high | mean violations |
|---|---|---|---|---|---|
| none | 1 | 0.655 | n/a | n/a | 12.38 |
| digest | 1 | -0.333 | n/a | n/a | 6.50 |
| full | 1 | 0.762 | n/a | n/a | 10.00 |
| placebo | 1 | -0.321 | n/a | n/a | 14.38 |
| terse | 1 | 0.214 | n/a | n/a | 9.50 |

## Results, split `dev`

| condition | n | mean violations | script part | done rate | words | secs | leak rate |
|---|---|---|---|---|---|---|---|
| none | 11 | 14.09 | 1.91 | 0.91 | 200 | 22.1 | 0.000 |
| full | 11 | 11.00 | 1.82 | 1.00 | 248 | 51.9 | 0.000 |
| placebo | 11 | 8.54 | 1.27 | 0.91 | 133 | 19.1 | 0.000 |
| terse | 11 | 7.00 | 0.36 | 1.00 | 103 | 14.0 | 0.000 |
| digest | 11 | 5.91 | 0.46 | 1.00 | 102 | 14.6 | 0.000 |

Digest minus baseline, paired by task (mean difference, interval):

| baseline | n | mean diff | ci low | ci high |
|---|---|---|---|---|
| none | 11 | -8.182 | -16.091 | -2.273 |
| full | 11 | -5.091 | -9.636 | -0.182 |
| placebo | 11 | -2.636 | -4.818 | -0.455 |
| terse | 11 | -1.091 | -3.727 | 1.727 |

Drift (per-turn slope of violations over the sessions):

| condition | sessions | slope | ci low | ci high | mean violations |
|---|---|---|---|---|---|
| none | 1 | 1.500 | n/a | n/a | 11.50 |
| digest | 1 | 1.036 | n/a | n/a | 5.12 |
| full | 1 | 0.619 | n/a | n/a | 14.50 |
| placebo | 1 | 2.107 | n/a | n/a | 12.38 |
| terse | 1 | 1.071 | n/a | n/a | 11.75 |

## Per-demand mean violations per reply, split `all`

| demand | check | none | full | placebo | terse | digest | text |
|---|---|---|---|---|---|---|---|
| d01-opening | script | 0.39 | 0.35 | 0.30 | 0.17 | 0.04 | Open with the first word of substance; no greeting, preamble, pleasantry, or remark on the |
| d02-hedge | script | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | State what you know as fact; no hedge. |
| d03-filler | script | 0.30 | 0.83 | 0.26 | 0.13 | 0.13 | No filler word or softener. |
| d04-connective | script | 0.00 | 0.00 | 0.04 | 0.00 | 0.00 | No connective such as however, furthermore, additionally, moreover. |
| d05-long-sentence | script | 0.91 | 0.78 | 0.96 | 0.30 | 0.48 | No sentence over fifteen words (prose outside code). |
| d06-restate | judge | 0.35 | 0.65 | 0.43 | 0.26 | 0.39 | The reply restates what the user said or wrote. |
| d07-exact | judge | 0.91 | 1.13 | 0.83 | 1.00 | 1.17 | The reply gives a vague term, paraphrased code, or an approximate error, path, command, nu |
| d08-invalidate | judge | 0.52 | 0.48 | 0.30 | 0.13 | 0.30 | The reply asserts a result, cause, or claim without naming what could make it invalid (oth |
| d09-implication | judge | 0.22 | 0.52 | 0.22 | 0.22 | 0.09 | The reply makes a true statement that carries a false implication and does not add the cor |
| d10-guess | judge | 0.43 | 0.43 | 0.17 | 0.26 | 0.22 | The request is ambiguous and the reply guesses instead of asking or stating the assumption |
| d11-baseline | judge | 0.09 | 0.13 | 0.13 | 0.04 | 0.09 | The reply claims a cause or recommends changing a condition without reproducing the baseli |
| d12-invalid-states | judge | 0.26 | 0.22 | 0.26 | 0.09 | 0.09 | Code in the reply lets an invalid state be expressed (contradictory flags, optional fields |
| d13-silent-failure | judge | 0.39 | 0.35 | 0.43 | 0.22 | 0.04 | Code in the reply hides failure: a bare except, a swallowed error, unwrap without reason,  |
| d14-ownership | judge | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | Code in the reply shares mutable state without one owner or explicit synchronization. |
| d15-signatures | judge | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | The reply writes bodies before modelling the domain in types and signatures, or omits test |
| d16-overstrict | judge | 0.04 | 0.17 | 0.00 | 0.00 | 0.00 | The reply adds strictness, validation, or typing the domain does not require. |
| d17-class-per-record | judge | 0.00 | 0.09 | 0.00 | 0.00 | 0.04 | The reply wraps plain information in a class where a map, set, or sequence fits. |
| d18-simple-vs-easy | judge | 0.09 | 0.04 | 0.04 | 0.13 | 0.04 | The reply picks the familiar tangled option over a simpler one, or mixes concerns (data ac |
| d19-constructs | judge | 0.17 | 0.17 | 0.09 | 0.09 | 0.04 | The reply uses mutable state, methods, inheritance, or scattered conditionals where values |
| d20-explicit | judge | 0.26 | 0.09 | 0.13 | 0.17 | 0.22 | The reply's code is implicit, nested, or dense where explicit, flat, or sparse was availab |
| d21-one-home | judge | 0.56 | 0.91 | 0.26 | 0.30 | 0.17 | The reply puts one piece of knowledge in two places. |
| d22-rule-of-three | judge | 0.13 | 0.04 | 0.09 | 0.13 | 0.04 | The reply abstracts, generalizes, or introduces an interface before a third instance or a  |
| d23-wrong-abstraction | judge | 0.04 | 0.00 | 0.04 | 0.04 | 0.04 | The reply keeps or grows a shared abstraction with new parameters or branches instead of i |
| d24-ruled-out | judge | 0.30 | 0.26 | 0.26 | 0.22 | 0.17 | The reply adds code without naming what it ruled out (existing code, a configuration chang |
| d25-least-code | judge | 0.61 | 0.52 | 0.43 | 0.22 | 0.09 | The reply writes more code than the task needs, or prefers a shorter version harder to cha |
| d26-caller-or-test | judge | 0.74 | 0.39 | 0.48 | 0.35 | 0.22 | The reply adds a function, type, or file with no caller or test in the same change, or lea |
| d27-new-path | judge | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | The reply adds a new code path beside an existing one instead of changing the existing one |
| d28-dependency | judge | 0.39 | 0.39 | 0.17 | 0.26 | 0.13 | The reply adds or recommends a dependency without opening its source, running its tests, n |
| d29-generated | judge | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | The reply endorses merging generated or pasted code unread or not understood. |
| d30-progress | judge | 0.00 | 0.04 | 0.04 | 0.04 | 0.00 | The reply reports lines added as progress, or reports a deletion without naming the protec |
| d31-yagni | judge | 0.74 | 0.83 | 0.48 | 0.26 | 0.13 | The reply adds a field, method, option, abstraction, or edge case that nothing present ask |
| d32-foundations | judge | 0.04 | 0.00 | 0.00 | 0.00 | 0.00 | The reply defers a foundation (language, database, platform, security) to later or builds  |
| d33-method-size | judge | 0.43 | 0.26 | 0.22 | 0.22 | 0.09 | The reply's code has a function over twenty lines or with more than one responsibility, a  |
| d34-ship | judge | 0.04 | 0.04 | 0.04 | 0.00 | 0.00 | The reply types before thinking or modelling, or withholds shipping code that compiles and |
| d35-names | judge | 1.44 | 1.17 | 1.22 | 1.04 | 0.96 | The reply names a thing for its implementation, leaves a bare number or string in logic, o |
| d36-comments | judge | 3.35 | 4.78 | 2.17 | 1.65 | 1.35 | The reply's code carries a comment explaining what the code does, or a comment not giving  |
| d37-first-truths | judge | 0.26 | 0.13 | 0.13 | 0.17 | 0.09 | The reply justifies a choice by resemblance, convention, or industry standard rather than  |
| d38-bug-cause | judge | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | The reply fixes a bug without working out how it came to be. |
| d39-measure | judge | 0.09 | 0.04 | 0.04 | 0.00 | 0.00 | The reply optimizes or recommends optimizing without a measurement. |

## Gate, cut-1

Split `test`; pass: **False**; changed vs previous: None.

| check | pass | value | threshold |
|---|---|---|---|
| cut vs none: paired mean difference at or below the threshold and its interval excludes zero | True | `{"n": 12, "mean_diff": -5.417, "ci_low": -9.417, "ci_high": -1.333}` | -1.0 |
| near full: digest minus full at or below the margin | True | `{"n": 12, "mean_diff": -10.917, "ci_low": -18.333, "ci_high": -4.083}` | 1.0 |
| beats terse: interval of digest minus terse lies below zero | False | `{"n": 12, "mean_diff": -1.5, "ci_low": -3.75, "ci_high": 0.583}` | 0 |
| beats placebo: interval of digest minus placebo lies below zero | True | `{"n": 12, "mean_diff": -3.167, "ci_low": -6.333, "ci_high": -0.417}` | 0 |
| completion: digest done rate within the margin of the best baseline | True | `1.0` | 0.9 |
| drift: digest slope minus full slope at or below the margin | True | `-1.095` | 0.1 |

## Ledger entries (instrument fields)

```json
{
 "ts": "2026-10-12T22:47:07",
 "slug": "cargo-cult-science+correct-by-construction+dry+first-principles+kiss+lines-spent+self-documenting-code+simple-made-easy+stop-yapping+yagni+zen-of-python",
 "cut": 1,
 "kind": "cut",
 "run_dir": "cut-1",
 "digest_path": ".claude/digests/cargo-cult-science+correct-by-construction+dry+first-principles+kiss+lines-spent+self-documenting-code+simple-made-easy+stop-yapping+yagni+zen-of-python.md",
 "digest_sha256": "580a19b139e5297e490d39dce0ae9beb552068fd1a28869d4eb566806af5663a",
 "digest_words": 841,
 "manifestos": [
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/manifestos/cargo-cult-science.md",
   "version": "1.0.0"
  },
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/manifestos/correct-by-construction.md",
   "version": "1.0.0"
  },
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/manifestos/dry.md",
   "version": "1.0.0"
  },
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/manifestos/first-principles.md",
   "version": "1.0.1"
  },
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/manifestos/kiss.md",
   "version": "2.0.0"
  },
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/manifestos/lines-spent.md",
   "version": "1.0.0"
  },
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/manifestos/self-documenting-code.md",
   "version": "1.0.0"
  },
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/manifestos/simple-made-easy.md",
   "version": "2.0.0"
  },
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/manifestos/stop-yapping.md",
   "version": "1.0.0"
  },
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/manifestos/yagni.md",
   "version": "1.0.0"
  },
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/manifestos/zen-of-python.md",
   "version": "1.0.0"
  }
 ],
 "members": [
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/digests/cargo-cult-science.md",
   "sha256": "8957982da1c3a257f5dc972bc4a5ee1b69679b28e930cc0d8789c185573cad63"
  },
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/digests/correct-by-construction.md",
   "sha256": "66d4ac7109ecb4c0a17047302bd2685316e30ce6b265d77f615ba55f734cd400"
  },
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/digests/dry.md",
   "sha256": "9f044f77595b3cd7f69447e8ed539c2378dfdc343b3eecf1e790fe4a592aa17f"
  },
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/digests/first-principles.md",
   "sha256": "0bc2fe1e777337d7996986a4f402be60ed65188c22bc8bc871254f9585bdac80"
  },
  {
   "path": "/Users/ryzhakar/LLM_MANIFESTOS/digests/kiss.md",
   "sha256": "a9a8d12320dd64ffb75e91c53daf0654844cb02ba55f54b351e7b7d3
```

## Diagnosis and the next cut (read from cut-2/hypothesis.md and cut.json)

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

## Caveats

- 37 of the 195 replies were reused from the aborted first run (same conditions and task text); they existed before the resized spec froze.
- Repeats were capped at 1 (the repeat rule, run through a script proxy, asked for 2) to fit the 90-minute reader budget.
- The test split holds 12 paired tasks, so intervals are wide; one session per condition per language.
- The `full` condition is the 11 member manifestos concatenated.

— measured by Claude (orchestrator), 2026-10-12, rendered from files
