Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it.

ROLE: You are extracting every rule two projects state about what a manifesto is, how it is written, how it enters a collection, and how it is consumed.

CONTEXT: Project A, LLM_MANIFESTOS, curates manifesto files. Project B, claude-skills, holds the plugin that writes them and binds a model to them. A later synthesis needs every rule as a numbered row with its location, so conflicts and gaps are checkable.

INPUT FILES (read each in full):
1. /home/user/LLM_MANIFESTOS/MAINTAINERS_GUIDE.md
2. /home/user/LLM_MANIFESTOS/README.template.md
3. /home/user/LLM_MANIFESTOS/generate.py
4. /home/user/LLM_MANIFESTOS/themes.yaml
5. /home/user/LLM_MANIFESTOS/orchestration_log/reference/conventions.md
6. /home/user/LLM_MANIFESTOS/orchestration_log/reference/codebase_state.md
7. /home/user/LLM_MANIFESTOS/orchestration_log/reference/deferred_items.md
8. /home/user/LLM_MANIFESTOS/orchestration_log/history/2026-04-29/session.md
9. /home/user/LLM_MANIFESTOS/orchestration_log/history/2026-05-01/session.md
10. /home/user/LLM_MANIFESTOS/orchestration_log/history/2026-05-11/session.md
11. /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md
12. /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md
13. /home/user/claude-skills/manifesto/agents/maximalist-reviewer.md
14. /home/user/claude-skills/manifesto/SCHEMA.md
15. /home/user/claude-skills/manifesto/README.md
16. /home/user/claude-skills/ETHOS.md
17. /home/user/claude-skills/CLAUDE.md
Also run `git -C /home/user/LLM_MANIFESTOS log --format='%h %ad %s' --date=short` and `git -C /home/user/claude-skills log --format='%h %ad %s' --date=short -- manifesto` and treat commit subjects as practiced rules where they state one.

TASK:
1. From each input, extract every statement that constrains a manifesto: what it is or is not, what it contains, its form, its register, its reader, its length, its metadata, how it is reviewed, how it enters, how it versions, how it is loaded or bound or audited at runtime, how it is written (process). One row per statement.
2. For each row record: ID (D-001…); the rule as a verbatim quote of at most 25 words; file:line; project (A or B); class — one of entry, metadata, form, register, reader, length, evidence, boundary, runtime, process, review; status — doctrine, learned, or practiced.
3. Conflicts: list every pair of rows that cannot both hold, quoting both and naming the axis of conflict in at most eight words.
4. Silences: list questions about manifestos that no row answers, as questions only, one line each.
5. Write the report.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/doctrine-audit.md

REPORT FORMAT:
# Doctrine Audit — rules stated by both projects
(three binding lines)
## Rules — table: ID | rule (quote) | file:line | project | class | status
## Conflicts — table: pair | rule 1 (quote) | rule 2 (quote) | axis
## Silences — bullet list of questions
## Counts — rows per class, rows per status, rows per project

SCOPE: Extract and locate. Do not judge which side of a conflict is right. Do not recommend. Do not read the manifesto bodies themselves; another agent measures those.

TOOLS: Read for files; Grep to locate lines; Bash for the two git log commands; Write for the report.

End with a 3-sentence summary for a notification: row count, conflict count, the one silence you judge largest.
