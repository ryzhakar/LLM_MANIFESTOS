---
name: write-eval-spec
description: "Turn a digest's demand list into the spec, the frozen instrument of an eval series, with a per-demand checklist, the conditions, the reader and judge, and the gate, before any run. \"write the eval spec\", \"spec the digest eval\", \"fix the gate\", \"set the thresholds\", \"which demands are scripted\", or a demands record with no spec beside it."
---

<take-the-demands>
Read the demands record, the numbered list of things the manifesto tells its reader to do or refuse, whole; never write a spec from the digest alone.
Give every demand one row with an `id` and its text; never fold two demands into one row.
</take-the-demands>

<sort-each-demand>
Mark a demand `script` when a regular expression or a sentence-length count detects its breach in a reply's prose outside code blocks; never mark one `script` whose breach needs reading.
Write the pattern or the limit on every `script` row; never leave one without it.
Mark every other demand `judge`, a breach a bound model counts; never leave a demand unmarked.
</sort-each-demand>

<fix-the-conditions>
List the conditions, the texts loaded into the system prompt of the reader, the model that loads the digest, beside each other; never run a cut, one numbered revision of the digest, without `none`, `full`, `terse`, and `placebo`.
List `none`, nothing loaded; never drop it.
List `digest`; never run a condition set without it.
List `full`, the manifesto's body; never load its frontmatter.
List `terse`, one plain line stating the manifesto's aim, in words the digest does not use; never echo a digest sentence in it.
List `placebo`, a text of the digest's word count carrying no demand, cycled from a named source file; never let its source carry a demand.
List the ablations, the digest with one sentence removed, one per sentence; never remove two sentences in one.
</fix-the-conditions>

<choose-the-instrument>
Name the reader by adapter and model; never let a series, the cuts run under one spec, change reader.
Name the judge configuration, the agent model and the brief the `calibrate-eval-judge` skill fixed, by name and brief; never mix two judge configurations in one series.
Name the task split the gate reads, `test`, and the split failures are read on, `dev`; never let the gate read `dev`.
</choose-the-instrument>

<set-the-gate>
Set the interval level, the share of resamples, means of the per-task differences drawn again with replacement, that the confidence interval covers, as `ci`; never gate on a mean without its interval.
Set `min_cut_vs_none`, the least drop in mean violations per reply the digest shows against `none`, with the interval below zero; never pass a digest whose interval against `none` crosses zero.
Set `margin_vs_full`, the most the digest may exceed `full` in mean violations; never set it from one run's noise.
Set `completion_margin`, the most the digest's done rate may fall below that of the best baseline, a condition other than the digest; never gate completion on a judge's opinion where a task carries an answer key.
Set `drift_margin`, the most the digest's per-turn slope of violations may exceed the full text's across the sessions; never gate drift on one session.
Count a cut as changed against the previous cut when the interval of the per-task differences excludes zero; never count a change inside the interval.
Write every threshold with one sentence naming the demand or the baseline it protects; never carry a threshold inherited from a pilot.
</set-the-gate>

<freeze-the-spec>
Save the spec through the `write-eval-record` skill before the first reply of the series is run; never change it after.
Start a new series, with a new spec and a fresh cut count, when a demand, a condition, the reader, the judge, or a threshold changes; never compare cuts across two specs.
</freeze-the-spec>
