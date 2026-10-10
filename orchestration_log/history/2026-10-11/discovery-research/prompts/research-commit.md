Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it.

ROLE: You are making the finished research reports durable by copying them, unchanged, into a tracked folder and committing on the current branch.

CONTEXT: Repository /home/user/LLM_MANIFESTOS, branch claude/manifesto-design-discussion-liuuvf (confirm). research/ is gitignored. Commit rule: single-line conventional message, no body, no attribution trailers. The synthesizer is still writing discovery/candidates.md; do not copy it, and do not copy resources-commit-report.md.

INPUT FILES (copy each byte-for-byte with cp -p):
1. /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/corpus-audit.md, corpus_metrics.py, doctrine-audit.md, runtime-audit.md, collection-overlap-audit.md
2. /home/user/LLM_MANIFESTOS/research/manifesto-craft/resolutions/runtime-defects-verification.md
3. /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/enemies.md, distinctions-vocabulary.md, evidence.md, demands.md, tensions.md, collection-fit.md, breadth.md, stack-options.md, verify-axioms.md, skrenta-resolution.md, OWNER-RULING-2026-10-11.md
4. /home/user/LLM_MANIFESTOS/research/manifesto-craft/BRIEF.md, DISPATCH.md, DISCOVERY-BRIEF.md, DISCOVERY-DISPATCH.md, sources.md, and the whole prompts/ folder

TASK:
1. Create /home/user/LLM_MANIFESTOS/orchestration_log/history/2026-10-11/research/ with subfolders deep-dives/, resolutions/, discovery/, briefs/, prompts/. Copy inputs 1–3 into the matching subfolder; input 4's five files into briefs/ and prompts/* into prompts/.
2. sha256-verify every copy against its origin.
3. Write orchestration_log/history/2026-10-11/research/INDEX.md: one table, file | origin path | sha256 | bytes; one line stating that recon/ texts live under resources/2026-10-11-code-liability-and-dependencies/ (commits 9e8c738, c1bae5e) and that candidates.md follows in a later commit. No summaries of content.
4. `git check-ignore -v orchestration_log/history/2026-10-11/research/` must return nothing; else stop and report.
5. `git add orchestration_log/history/2026-10-11/research/`; commit with exactly: `doc: discovery research reports — audits, surveys, verifications, briefs`
6. `git push -u origin claude/manifesto-design-discussion-liuuvf`; retry up to 4 times on network failure with 2s, 4s, 8s, 16s waits.
7. Report `git log --oneline -1`, `git status --short`, file count.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/research-commit-report.md

REPORT FORMAT:
(three binding lines)
# Research Commit
## Files copied — table: destination | origin | sha256 match | bytes
## Commit — hash, message, branch, push result
## Skipped — anything not copied and why

SCOPE: Copy, verify, commit, push. Touch nothing else. No attribution lines. No new branch.

TOOLS: Bash for cp, sha256sum, git; Write for INDEX.md and the report.

End with a 3-sentence summary for a notification: files committed, hash, anything skipped.
