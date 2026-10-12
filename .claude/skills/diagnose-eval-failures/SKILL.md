---
name: diagnose-eval-failures
description: "Trace a cut's failing replies to one failing demand and write the one-change hypothesis for the next cut before it runs. \"diagnose the failures\", \"why did the digest fail\", \"read the failing replies\", \"what should cut two change\", or a gate result that fails on a cut with no hypothesis for the next."
---

<read-dev-alone>
Read the scores record's rows of split `dev`, the split whose failures are read between cuts; never open a `test` row.
Read the gate result for the failed checks; never diagnose a passed check.
</read-dev-alone>

<find-the-failing-demand>
Compare the per-demand means of `digest` against `full` and `none`, the conditions, the texts loaded beside the reader's prompt; never compare a demand that passed.
Take the demand with the widest gap on a failed check; never take two.
Read the ablation results, the digest with one sentence removed; never read them for a demand that passed.
Note the sentence whose removal moves that demand least; never note one for a passed demand.
Read the drift slopes, the per-turn rise of violations across a session, when the drift check failed; never read a session's late turns alone.
Take the demand whose late-turn breaches rise most as the failing demand of a drift failure; never take one from early turns.
</find-the-failing-demand>

<read-the-replies>
Open the failing replies under that demand from the run dir's `runs/` through the key, the map from reply id to origin, each whole; never read a judge's notes in place of the reply.
Read the `full` replies to the same tasks beside them; never diagnose without the comparison.
</read-the-replies>

<name-the-cause>
Name what in the digest's sentence lets the reader breach, a demand absent, a boundary unfolded, a metaphor unexplained, a word the reader reads another way, or a sentence buried too far from the standing line, the sentence that applies the rules to every reply; never name the reader's size as the cause.
Name the cause from the replies; never name it from the numbers alone.
</name-the-cause>

<write-the-hypothesis>
Write the hypothesis, the one sentence or demand to change, the change, and the expected movement of that demand's mean against the previous cut's interval, the confidence interval of the paired difference; never write two changes.
Save it as the next cut's hypothesis record through the `write-eval-record` skill before the `recut-digest` skill runs; never cut before it is saved.
</write-the-hypothesis>
