---
name: write-eval-tasks
description: "Write the task set of a digest eval series: families that tempt the manifesto's violations in neutral words, answer keys, sessions for drift, and a dev/test split. \"write the eval tasks\", \"write tasks for the digest\", \"what should the reader be asked\", \"split dev and test\", or a spec with no tasks record beside it."
---

<name-the-families>
Read the demands record, the numbered list of things the manifesto tells its reader to do or refuse, whole; never write tasks from the digest, the plain text a small model carries in place of the manifesto, alone.
Name one family, a group of tasks that tempt one demand's breach, per demand the tasks can tempt; never name a family that tempts none.
Say in one line which demand each family tempts; never leave a family unexplained.
</name-the-families>

<write-the-tasks>
Write several tasks, requests to the reader, the model that loads the digest, per family in the words a plain user would use; never echo a sentence, a listed word, or a phrase of three words from the digest in one.
Write the tasks that invite the breach, the greeting that invites a greeting back, the vague question that invites a hedge, the long paste that invites a restatement; never write a task the digest's wording would answer for the reader.
Write tasks where terseness would hurt, a request whose correct answer needs several steps, a caveat, or a long block, so a digest that cuts substance fails them; never leave the set without them.
</write-the-tasks>

<key-each-task>
Give every single task an answer key, a regular expression a correct reply matches, or a test that a correct reply passes; never keep a task whose completion a reader of the reply cannot verify.
Write the key on the substance alone, the command, the number, the term, so a terse correct reply passes; never key on a phrasing.
</key-each-task>

<write-the-sessions>
Write several session scripts, lists of user turns run in one conversation, each long enough that a reader forgets an early rule, each on different topics in a different order; never write one session alone.
Mix tasks from several families through each session; never run one family's turns in a row.
</write-the-sessions>

<split-the-set>
Split tasks and sessions into `dev`, the split whose failures are read between cuts, and `test`, the split the gate reads, by family, with every family in both; never read a `test` reply outside the gate.
</split-the-set>

<size-the-repeats>
Choose `reps`, the repeats per task the spec holds, from a variance estimate, the spread of the per-task differences in violations per reply between `digest` and `none` in a previous run of the same series or the pilot, so that the confidence interval's half-width at that spread is at most half of the spec's `min_cut_vs_none`; never set `reps` by habit.
Run `digest-eval reps <slug> <run dir>` on that previous run to compute it; never compute it by eye.
</size-the-repeats>

<check-the-echo>
Search every task and every turn against every digest sentence for a shared phrase of three words; never save a task that shares one.
Save the tasks through the `write-eval-record` skill; never save a task set that changes after the first run of the series.
</check-the-echo>
