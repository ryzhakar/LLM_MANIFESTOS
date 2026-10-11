Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it, with one more element loaded and bound the same way:
4. manifesto-writing skill — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md

ROLE: You are mapping how the existing manifesto collection's claims would redistribute under each candidate focus point, so a later synthesis can judge which stack is sharpest.

CONTEXT: The owner has ruled that existing manifestos may be bent: /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/OWNER-RULING-2026-10-11.md (read it). Six focus points FP-A..FP-F are defined in discovery/collection-fit.md. The overlap audit holds every existing claim on volume, debt, dependencies, reuse with file:line.

INPUT FILES (read each in full):
1. /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/OWNER-RULING-2026-10-11.md
2. /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/collection-overlap-audit.md
3. /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/collection-fit.md — the Fit table and the six focus points only; skip its rated statements
4. /home/user/LLM_MANIFESTOS/manifestos/kiss.md, yagni.md, dry.md, simple-made-easy.md, correct-by-construction.md, self-documenting-code.md (whole)
5. /home/user/LLM_MANIFESTOS/orchestration_log/history/2026-04-29/session.md lines 72-84 and `git -C /home/user/LLM_MANIFESTOS show 5994364 --stat` (the one prior re-cut of two manifestos, for the precedent's shape)

TASK:
1. For each focus point FP-A..FP-F: list every overlap-audit row that a manifesto on that focus would claim, by file:line, and mark each row MOVE (leaves its current file), SHARE (stays and is restated), or STAY (not claimed).
2. For each existing manifesto touched: state its held ground before (one line, quoting its enemy and tagline) and after each focus point's moves (one line), and the row count it keeps.
3. Enumerate stack options as rows: option | focus points written as new files | existing files re-cut and how (rows moved, section removed, split, merged) | files whose thesis changes (major version per MAINTAINERS_GUIDE) | resulting enemy of each file in one quote-length line. Include at minimum: one new file with no re-cut; one new file plus re-cut of kiss and yagni; two new files (volume, dependencies) plus re-cuts; a merge option if any two focus points share four or more rows.
4. For each option, list the facts for and against from the inputs only, as located quotes. No verdict.
5. Write the report.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/stack-options.md

REPORT FORMAT:
(three binding lines)
# Stack Options — redistribution of held ground under each focus point
## Row map — table: row (file:line) | quote | FP-A | FP-B | FP-C | FP-D | FP-E | FP-F (each cell MOVE / SHARE / STAY)
## Held ground before and after — per manifesto
## Options — table as in step 3
## Facts for and against — per option, located quotes
## Precedent — what the 2026-04-22 re-cut of kiss and simple-made-easy changed, from the diff stat and the session log

SCOPE: Map and enumerate. No recommendation, no ranking, no drafting, no edits to any manifesto.

TOOLS: Read; Grep; Bash for the git commands; Write for the report.

End with a 3-sentence summary for a notification: option count, the manifesto that loses the most rows under any option, the option with the fewest thesis changes.
