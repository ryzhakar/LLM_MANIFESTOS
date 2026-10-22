---
name: compile-commitments
description: >
  Write the interplay file and the commitments file that a session's system prompt carries, from the stack the session binds to.
  "/compile-commitments", "compile the commitments", "precompile the oath", or a change to the stack.
---

<read-the-stack>
Run `${CLAUDE_PLUGIN_ROOT}/bin/unharness stack --config <path>` into a temporary file, where `<path>` is the config, the working folder's `.manifestos.yaml`, which lists the stack, the ordered elements, each a manifesto, a skill, or a file, that the session binds to; never send the command's output into the conversation.

Read the temporary file whole, the `<stack>` block and then the full text of every element; never read a part of it.

Take each element's demands from its text in that file; never paraphrase an element from memory.
</read-the-stack>

<deconstruct-each-element>
Reduce each element to its axioms, the demands on behavior that remain once you strip its prose; never carry the prose forward as a demand.
</deconstruct-each-element>

<map-convergence-and-tension>
Mark each convergence, a demand two or more elements share, as a constraint that governs first; never leave a shared demand unmarked.

List each tension, a point where two elements pull in opposing directions, with the conflicting sentence quoted from each element; never list a tension without both quotations.

Resolve each tension with an explicit rule that states which demand governs and when; never leave a tension for the moment to settle.

Where no rule resolves a tension, set a priority order among the elements in conflict; never leave two elements level.
</map-convergence-and-tension>

<write-the-interplay-file>
Write `.manifestos.interplay.md` beside the config; never write it elsewhere.

Open the file with the `<stack>` block copied verbatim from the temporary file; never alter, drop, or reorder a line of it.

After the block, write `<interplay>` ... `</interplay>` holding the axioms, the convergences, the tensions, the rules, and the priority order, in the session's own voice, the first person; never in a voice that reports on the session from outside.

Keep every seam, a sentence that names the config, the file, the tool, or the way the prompt was made, out of the analysis; never let one in.
</write-the-interplay-file>

<write-the-commitments-file>
Write `.manifestos.commitments.md` beside the config; never write it elsewhere.

Open the file with the same `<stack>` block copied verbatim; never open it with anything else.

After the block, write `<commitments>` ... `</commitments>` holding, for each element in the stack's order, one `I must ..., and I will ...` line and one `I must not ..., and I will not ...` line; never skip an element or change the order.

Fill each line with the element's own demand and the behavior that meets it; never with a seam.

<never_do_this reason="the commitment names the config and the tool that made the prompt">
I must read every element in .manifestos.yaml, and I will run unharness stack before each compile.
</never_do_this>

<do_exactly_this>
I must count every line I ship as spent, and I will write the least that does the task.
</do_exactly_this>
</write-the-commitments-file>

<report-the-files>
After writing each file, report its path; never print its content to the conversation.
</report-the-files>

<confirm-the-compile>
Run `${CLAUDE_PLUGIN_ROOT}/bin/unharness prompt --config <path> > /dev/null`; never report the files as done without that run.

Report the exit code of that run; never report a pass on a code other than 0.

On a code other than 0, correct the file that the printed message names and run the command again; never stop at a failing run.
</confirm-the-compile>
