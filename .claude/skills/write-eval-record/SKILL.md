---
name: write-eval-record
description: "Write one record of the digest eval, the demand list, the resolutions, the spec, the tasks, the judge brief, the calibration, the hypothesis, the cut, a reply, the key, a verdict, the scores, the gate, or a ledger entry, in its fixed shape at its fixed place. \"save the demand list\", \"record the cut\", \"write the ledger entry\", \"where does the verdict go\", \"what shape is a reply record\", or any skill of the digest eval about to write a file under evals/."
---

<find-the-eval-dir>
Write every record of one digest, the plain text a small model carries in place of a manifesto or a stack of manifestos, under `evals/<slug>/` in the repository that holds the digest, where `slug` is the digest's file name without its extension; never write one elsewhere.
Write every record of one cut, one numbered revision of the digest, under the run dir `evals/<slug>/cut-<n>/`; never mix two cuts in one run dir.
Write every record of a transfer run, the same cut on a second reader model, under `evals/<slug>/cut-<n>-<model>/`; never mix two readers in one run dir.
</find-the-eval-dir>

<write-the-series-records>
Write the demand list, one line per demand, a thing the manifesto tells its reader to do or refuse, numbered in the manifesto's order, as `evals/<slug>/demands.md`; never number two demands alike.
Write the resolutions of a stack, one line per tension naming the two member demands that pull apart and the one rule that replaces them, as `evals/<slug>/resolutions.md`; never write a resolution without both demands it replaces.
Write the spec, the frozen instrument of a series, the cuts run under one spec, as `evals/<slug>/spec.json`; never write it elsewhere.
Give the spec the fields `slug`, `demands`, `conditions`, `reader`, `judge`, `reps`, and `gate`; never omit one.
Give each demand `id`, `text`, and `check`, `script` or `judge`; never give two demands one `id`.
Give each `script` demand a `pattern`, or a `kind` of `sentence_words_over` with a `limit`; never give a `judge` demand either.
Give `conditions` the fields `baselines`, `terse_line`, `placebo_source`, and `ablations`; never omit one.
Give `reader` the fields `adapter` and `model`, `judge` the fields `name` and `brief`, and `reps` the repeats per task; never leave one empty.
Give `gate` the fields `split`, `ci`, `min_cut_vs_none`, `margin_vs_full`, `completion_margin`, and `drift_margin`; never omit one.
Write the tasks as `evals/<slug>/tasks.json` with the fields `singles` and `sessions`; never write them elsewhere.
Give each single task `id`, `family`, `split` of `dev` or `test`, `message`, and `answer`, a regular expression a done reply matches, or null; never give two tasks one `id`.
Give each session `id`, `split`, and `turns`, a list of user messages; never give two sessions one `id`.
Write the judge brief as `evals/<slug>/judge_brief.md` carrying the placeholders `{PACKET}`, `{OUT}`, `{MANIFESTO}`, and `{DEMANDS}`; never name a condition in it.
Write the calibration, the measured agreement between a judge configuration and reference raters, as `evals/<slug>/calibration.json`; never write it after the spec names the judge.
Give the calibration the judge `name`, the brief's sha256, the sample size, the acceptance level set before rating, and the agreement per demand and for done; never omit one.
</write-the-series-records>

<write-the-cut-records>
Write the hypothesis, the one change the next cut makes and the movement expected, as `evals/<slug>/cut-<n>/hypothesis.md`; never write it after that cut's replies exist.
Name in the hypothesis the failing demand, the reply ids read, the one sentence or demand to change, and the expected direction and size against the interval; never omit one.
Write the cut record as `evals/<slug>/cut-<n>/cut.json` with `cut`, `parent`, the digest's `sha256`, `hypothesis`, and `change`, the exact old and new sentence; never write a cut record carrying two changes.
Write each reply record as `runs/<cond>/<task>/r<rep>.json` for a single task or `runs/<cond>/<session>/t<turn>.json` for a session turn; never save one over an existing file.
Give each reply record `cond`, `task`, `split`, `message`, `reader`, `raw`, `text`, `leak`, `secs`, `rc`, `attempt`, `words`, and `rep` or `turn`; never omit one.
Write the key, the map from a reply's random id to its origin, as `key.json` at the run dir root; never write it under `judge/`.
Give each key entry `packet`, the blind file of replies a judge reads, `cond`, `task`, `rep` or `turn`, `leak`, and `split`; never omit one.
Write each verdict as one object in the list `judge/<packet>.verdict.json`; never write a verdict with an id outside the key.
Give each verdict `id`, `violations`, a count, `done`, true, false, or null, `notes`, and `demands`, a map from demand id to count, where the judge gives one; never omit `id`, `violations`, `done`, or `notes`.
Write the script judge's verdicts in the same shape as `script.json`; never merge them into an agent's file.
Write the scores as `scores.json` with `rows`, one per keyed reply, and `splits`; never edit a row by hand.
Give each split `by_condition`, `digest_vs`, `digest_vs_previous`, and `drift`; never omit one.
Write the gate result as `gate.json` with `split`, `pass`, `checks`, and `changed_vs_previous`; never write it before `scores.json`.
</write-the-cut-records>

<write-the-ledger-entry>
Append one line to `evals/<slug>/ledger.jsonl` per run dir after its gate; never rewrite a line.
Give the line the cut, the kind, the run dir, the digest's sha256 and word count, each manifesto's path and version, each member digest's path and sha256, the reader, the judge name and brief sha256, the spec and tasks sha256, the tool version, the hypothesis, the change, the numbers, and the gate; never omit one.
Keep the cut number, the digest hash, the instrument versions, and the last cut's numbers in the ledger alone; never put one of them in the digest, which carries no header.
Run `digest-eval ledger <slug> <run dir> --digest <path> --manifesto <paths>` to append the entry; never compose the line by hand.
</write-the-ledger-entry>
