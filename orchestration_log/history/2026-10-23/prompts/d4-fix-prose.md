Bind to write-well (skill agent-conduct:write-well), manifesto-writing (skill manifesto:manifesto-writing; tone manifesto /Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/raise-the-bar.md), lines-spent (/Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/lines-spent.md), and the skill memento:skill-creation — show your commitments before working. Non-compliant work is rejected.

ROLE
You apply the accepted prose fixes to the shipped preamble and the compile-commitments skill.

CONTEXT
Worktree /Users/ryzhakar/LLM_MANIFESTOS.worktrees/oath on branch feat/unharness-oath, at 07d1f0f; work and commit there only. The spec's sections "Shipped preamble" and "/compile-commitments" in /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/spec-unharness.md govern; the owner demands one instruction flow with no seam. The triage's decision (d): hook output and skill text are the owner's standing instructions carried by the application; harness notices are neither.

INPUT FILES
1. /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/reviews/triage.md, sections Decisions and "Accepted: prose".
2. plugin/unharness/src/unharness/preamble.md and plugin/skills/compile-commitments/SKILL.md in your worktree.
3. /Users/ryzhakar/.claudes/meta/plugins/cache/memento/memento/0.10.0/skills/skill-creation/SKILL.md, the rules the skill must meet.

TASK
1. Apply each accepted prose item in order; keep the preamble within 25 lines and the agent's voice.
2. Reread both files against write-well, the five checks of Raise the Bar (preamble), and skill-creation (skill); fix what the reread finds.
3. Run `claude plugin validate plugin` from the worktree root.
4. Commit each file on feat/unharness-oath; no push.

OUTPUT PATH
/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/reports/d4-prose.md

REPORT FORMAT
# D4 prose: items applied (number, how), items skipped with reasons, reread findings, commits, validation. End with a three-sentence summary.

SCOPE
Only the two files; no push; edit no other file.

TOOLS
Read, Write, Edit, Bash (git, claude plugin validate), Skill.

PRIME DIRECTIVE
Every change restores a truth or removes a seam; none adds a line that nothing needs.
