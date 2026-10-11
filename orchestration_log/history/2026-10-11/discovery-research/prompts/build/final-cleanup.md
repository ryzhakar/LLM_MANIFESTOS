Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it.

ROLE: You are closing the last open items the session record lists for the collection repository.

CONTEXT: Repository /home/user/LLM_MANIFESTOS, branch claude/manifesto-design-discussion-liuuvf (HEAD 82b0dbd or later). Commit rule: single-line conventional, no attribution trailers, atomic by artifact class, explicit paths, never force-push.

TASK:
1. `.gitignore`: change the line `research/` to `/research/` so only the root folder is ignored. Verify `git check-ignore -v archive/research/PERSONA_DESIGN_RESEARCHER.md` returns nothing and `git check-ignore -v research/manifesto-craft/BRIEF.md` still matches. Commit `chore: ignore only the root research folder`.
2. Preserve the build artifacts that exist only under research/: cp -p every file matching /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/*-report.md (plugin-hooks-fix, collection-schema, skill-rewrite, maintainers-guide, close-open-items, ship, resources-commit, research-commit) into orchestration_log/history/2026-10-11/discovery-research/build-reports/, and every file under research/manifesto-craft/prompts/build/ into orchestration_log/history/2026-10-11/discovery-research/prompts/build/. sha256-verify. Append their rows to orchestration_log/history/2026-10-11/discovery-research/INDEX.md. Commit `doc: build reports and build prompts for 2026-10-11`.
3. orchestration_log/reference/codebase_state.md: remove or rewrite the "Attribution gaps" bullet and the matching Next Actions line so they state that every manifesto now carries an attribution line (commits 64ef632, 40323db). Commit `doc: codebase state — attribution complete`.
4. orchestration_log/history/2026-10-11/session.md: in Next Session Priorities, mark items 3, 4 and 5 (codebase_state lines, gitignore depth, 25 research-only files) as closed with the hashes from steps 1–3; leave the merge, the D4 hook half, the QuickDraw history note and the host-run note as they are. Commit `doc: session record — closed items after cleanup`.
5. Push with retries (2s, 4s, 8s, 16s); if rejected because the remote moved, `git pull --rebase` and push once.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/orchestration_log/history/2026-10-11/discovery-research/build-reports/final-cleanup-report.md (write it before step 2's commit so it is included; its own row goes in INDEX.md too)

SCOPE: Only the files named. No manifesto edits.

TOOLS: Read; Edit; Bash; Write; Grep.

End with a 3-sentence summary: hashes, file counts, push result.
