# D2 — fix pass for 3.6.0

1. Role: you triage three review reports and apply the accepted findings to the code, skills, and docs on feat/digests in /Users/ryzhakar/LLM_MANIFESTOS.worktrees/digests, and the e2e findings.
2. Context: spec is law (/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/spec-unharness.md, part "3.6.0"); owner answers in queue-long-run.md 27–41. Suite: `uv run --project plugin/unharness pytest -q plugin/unharness` from the worktree.
3. Inputs: /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/reviews/digests-code.md, digests-prose.md, digests-spec.md; /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/verification-digests.md (FAIL rows).
4. Task: (1) write the triage to /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/reviews/digests-triage.md: every finding, one line each, with ACCEPT / REJECT (reason: contradicts spec or owner answer, or not true) / DEFER (name why), blocking first. (2) Apply every ACCEPT by TDD where behavior changes (failing test first), in commits grouped by what reverts together: `fix(unharness): ...`, `fix(skill): ...`, `doc(plugin): ...`, each subject ≤ 10 words, no body, no trailer. (3) Where a finding reveals a spec error, fix the spec in the same pass and say so in the triage. (4) Run the full suite, `claude plugin validate plugin`, and `unharness doctor --config .manifestos.yaml` last; paste the last lines into the triage.
5. Output: the triage file, the commits.
6. Report: counts (accepted/rejected/deferred), the commit shas, a 3-sentence summary.
7. Scope: no new features; no version bump.
8. Tools: Read, Edit, Write, Grep, Glob, Bash.
9. Strunk for prose; the code's existing style for code.
