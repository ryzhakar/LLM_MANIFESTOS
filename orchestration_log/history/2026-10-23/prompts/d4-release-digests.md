# D4 — release 3.6.0

1. Role: you cut the release of the manifesto plugin 3.6.0 in /Users/ryzhakar/LLM_MANIFESTOS.worktrees/digests (branch feat/digests).
2. Context: 3.5.0 was released by commit 002db33 (`git show 002db33 --stat` shows the files a release touches: plugin/.claude-plugin/plugin.json, .claude-plugin/marketplace.json, plugin/unharness/pyproject.toml, any README version strings). The owner's git rules: one line `type(scope): subject` ≤ 10 words, no body, no trailer, no attribution.
3. Inputs: the files above; `git log --oneline 9e91351..feat/digests`.
4. Task: bump every version string from 3.5.0 to 3.6.0 (grep for `3.5.0` across plugin/ and .claude-plugin/ and the READMEs; leave historical mentions in orchestration_log alone); run `claude plugin validate plugin`; run `uv run --project plugin/unharness pytest -q plugin/unharness`; run `uv build --no-sources plugin/unharness` and confirm the wheel's name carries 3.6.0, then delete plugin/unharness/dist; commit `chore(plugin): release 3.6.0, digests and doctor`. Do not push, tag, or move main.
5. Output: /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/d4-release-report.md: files changed, the three commands' last lines, the commit sha.
6. Report: a 3-sentence summary.
7. Scope: version strings only; no other edits.
8. Tools: Bash, Read, Edit, Grep, Glob.
9. Nothing beyond what the commands show.
