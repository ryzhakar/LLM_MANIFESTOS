Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it.

ROLE: You are shipping the approved manifesto draft into the collection, re-cutting kiss.md, archiving the draft record, and pushing, by the maintainer guide's ship step.

CONTEXT: Repository /home/user/LLM_MANIFESTOS, branch claude/manifesto-design-discussion-liuuvf. The approved draft path and its final filename slug are in the launch prompt. Read /home/user/LLM_MANIFESTOS/MAINTAINERS_GUIDE.md (Workflows: entry gate, re-cutting, ship step) and /home/user/LLM_MANIFESTOS/drafts/owned-lines/SPEC.md section "Absorbed from kiss" before acting. Commit rule: single-line conventional, no attribution, atomic by artifact class, explicit paths staged, never `git add -A`.

TASK, in order, each step verified before the next:
1. `git status --short` must show only drafts/ changes; else stop and report.
2. Copy the approved draft to manifestos/<slug>.md unchanged (cp -p). Run `just readme` (or `python3 generate.py` if just is absent); it must exit 0 with 13 manifestos and no validation panel; README.md regenerates. Run `python3 tests/test_generate.py` (or pytest) green.
3. Commit: `feat(<slug>): <title from the frontmatter, lowercased> — <tagline>` staging manifestos/<slug>.md only. Then `chore: regenerate README` staging README.md only.
4. Re-cut kiss.md: remove the "### Delete Code" block (the four rows the spec quotes; verify by line content, not number) and nothing else; kiss.md keeps version 2.0.0 (no enemy row moves). Run the generator and tests again. Commit `refactor(kiss): move Delete Code block to <slug>` staging manifestos/kiss.md and README.md if it changed.
5. Write orchestration_log/history/2026-10-11/recut-kiss.md: rows moved (quoted, with the old kiss line numbers and the new file's line numbers), held ground after (one line, kiss's enemy and tagline unchanged). Commit `doc: re-cut record for kiss`.
6. Archive: `git mv drafts/owned-lines/SPEC.md orchestration_log/history/2026-10-11/owned-lines/SPEC.md`; `mkdir -p` and `git add` every file under drafts/owned-lines/reviews/ into orchestration_log/history/2026-10-11/owned-lines/reviews/ (git mv for tracked, mv + add for untracked); delete the draft versions (v1.md, v2.md, …) and any remaining drafts/owned-lines/ files; drafts/ must be empty or gone. Commit `doc: archive owned-lines spec and reviews` staging the archive paths and the deletions by path.
7. Update orchestration_log/reference/codebase_state.md inventory (13 files, the new row) and conventions.md if it lists the collection size. Commit `doc: reference — inventory after <slug>`.
8. `git push origin claude/manifesto-design-discussion-liuuvf` with retries (2s, 4s, 8s, 16s); if rejected because the remote moved, `git pull --rebase` then push once; never force.
9. `git log --oneline -8` and `git status --short`.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/ship-report.md

REPORT FORMAT:
(three binding lines)
# Ship — <slug>
## Generator and tests — output lines
## Commits — hash | message | files
## kiss re-cut — rows removed (quoted) and kiss line count before/after
## Push — result
## Open

SCOPE: Only the steps above. No edits to the manifesto text. No edits to any other manifesto. No attribution lines.

TOOLS: Bash; Read; Write; Edit; Grep.

End with a 3-sentence summary for a notification: the new file and commit, the kiss re-cut commit, the push result.
