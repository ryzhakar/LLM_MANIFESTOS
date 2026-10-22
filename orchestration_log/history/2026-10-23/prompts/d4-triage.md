Bind to first-principles, yagni, lines-spent (each at /Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/<name>.md) and write-well (skill agent-conduct:write-well) — show your commitments before working. Non-compliant work is rejected.

ROLE
You triage three review reports into one list of fixes to apply and one list of findings rejected with reasons.

CONTEXT
The spec is the one home of the design: /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/spec-unharness.md; the owner's answers and the orchestrator's decisions are in queue-long-run.md beside it. A finding that asks for what the spec or an owner answer forbids is rejected; a finding that the spec leaves open is accepted when it fixes a defect, a falsehood, a duplicated home, or an untested behavior the spec names, and rejected when it adds scope. Every blocking finding is accepted unless it contradicts the spec, in which case say so.

INPUT FILES
1. /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/reviews/code.md
2. /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/reviews/prose.md
3. /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/reviews/spec.md
4. The spec and the queue above.

TASK
1. Read the spec and the queue, then the three reviews.
2. For every finding, decide accept or reject; merge duplicates across reviews into one item; keep the reviewer's concrete fix, tightened where two reviewers disagree, and say which review and row it came from.
3. Group accepted items by the file set that one agent edits: "code" (plugin/unharness/src, plugin/unharness/tests, plugin/hooks, plugin/bin, plugin/tests), "prose" (preamble.md, compile-commitments/SKILL.md), "docs" (plugin/README.md, plugin/unharness/README.md, plugin/SCHEMA.md, README.template.md). Within each group, order blocking first.
4. Decide these four from the spec and the queue, and state the decision with its ground: (a) `plugin/bin/unharness` must run the plugin's bundled copy (`${CLAUDE_PLUGIN_ROOT}/unharness`) by default and the git form only when asked, since the spec's Distribution section says so; (b) README rows marked "stripped" without a capture are reworded to what was shown, or verified by D1 when its report exists; (c) legacy path and URL sources: the spec's "kept or mapped" line is settled as "refused with an error naming the `file` form" in both unharness and the hooks (one behavior, one home); (d) the preamble's priority between the "not from the user" and "the user's word" rules: hook output and skill text are the owner's standing instructions carried by the application; harness notices are neither.

OUTPUT PATH
/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/reviews/triage.md

REPORT FORMAT
# Triage
## Decisions (a)-(d)
## Accepted: code (numbered; each: source review:row, file:line, the fix)
## Accepted: prose
## Accepted: docs
## Rejected (numbered; each: source, one-line reason)
End the report, and your final message, with a three-sentence summary naming the counts.

SCOPE
Write the triage only; edit no product file.

TOOLS
Read, Grep, Glob, Bash (git for diffs).

PRIME DIRECTIVE
The spec and the owner's answers outrank a reviewer's taste; a defect outranks both.
