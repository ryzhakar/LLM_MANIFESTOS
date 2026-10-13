---
name: test-digest
description: "Run one cut of a digest through the eval loop, spec, tasks, conditions, reader, judges, scores, gate, ledger, and decide whether to stop or diagnose and re-cut. \"test the digest\", \"run the digest against qwen\", \"gate the digest\", \"iterate the cut\", \"does the digest work\", or an access point handed with a digest path."
---

<check-the-ledger>
Run `digest-eval stale <slug> --digest <path>` from the project that holds the digest to compare the ledger, the file that gains one line per run, with the manifesto versions, the digest, and the member digests on disk; never run a cut, one numbered revision of the digest, that the ledger already covers.
Report a missing `digest-eval` command, the launcher `just install-digest-eval` in the manifesto repo puts on the PATH; never substitute another way of running the tool.
Stop at that report; never run a stage without the command.
</check-the-ledger>

<prepare-the-series>
Write the spec through the `write-eval-spec` skill, the tasks through the `write-eval-tasks` skill, and the judge through the `calibrate-eval-judge` skill when the eval dir, `evals/<slug>/`, lacks one; never run a reply before all three are frozen.
Take the cut number from the ledger's last entry plus one, or one for a fresh series; never reuse a number.
</prepare-the-series>

<build-the-conditions>
Run `digest-eval conditions <slug> cut-<n> --digest <path> --manifesto <paths>` to write every condition's text, the texts loaded beside the prompt of the reader, the model that loads the digest, with the members' manifestos as the paths for a stack; never load a condition text the tool did not write.
</build-the-conditions>

<run-the-reader>
Run `digest-eval run <slug> cut-<n>` with stdin from `/dev/null`, serial, on the series' reader, for the `reps` the spec holds; never run two readers in one invocation.
Run a cut after the first with `--only digest`; never re-run a baseline the series already holds.
Judge such a cut with the first cut's baselines borrowed into its packets; never judge it against the first cut's verdicts.
Start the run detached, and wait on a background shell loop that exits when `progress.log` gains `DONE`, a `Traceback`, or `Killed`, or when the reply count stands still for ten minutes; never wait on a watcher that reports progress alone.
Run the transfer check, the same cut on a second reader into `cut-<n>-<model>`, as its own block after the first reader finishes; never interleave the two.
Resume an interrupted run by the same command; never delete a finished reply to re-run it.
</run-the-reader>

<judge-the-replies>
Judge every run dir through the `judge-by-agents` skill; never judge under a configuration the spec does not name.
</judge-the-replies>

<score-and-gate>
Run `digest-eval score <slug> cut-<n> --previous cut-<n-1>` and then `digest-eval gate <slug> cut-<n>`; never read the gate on `dev`, the split read between cuts.
Record each run dir's ledger entry through the `write-eval-record` skill; never leave a scored run unrecorded.
</score-and-gate>

<stop-or-continue>
Stop when the gate passes; never cut past a pass.
Stop when two cuts in a row show `changed_vs_previous` false, their difference inside the interval, the confidence interval of the paired difference; never cut a third.
Stop at the fifth cut of a series; never cut a sixth under one spec.
Write the next hypothesis through the `diagnose-eval-failures` skill; never change the digest for the numbers alone.
Cut through the `recut-digest` skill; never cut without a saved hypothesis.
Start this loop again at the conditions for the new cut; never skip a stage for the second cut.
</stop-or-continue>
