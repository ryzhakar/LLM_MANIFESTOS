# D1 — reviews of unharness 3.6.0 (three reviewers, one brief)

Role: you review one aspect of the 3.6.0 change set on branch feat/digests in /Users/ryzhakar/LLM_MANIFESTOS.worktrees/digests. Read-only on product files; you write one report.

Context: unharness 3.5.0 shipped; 3.6.0 adds digest-mode compilation (`--digests`, `--stack-digests`, `--overlap`), `--minified` session files, `stamp` and `doctor` verbs, the `index.json` digest sidecar, the `/compile-digest` skill, this repo's `.min.md` pair, docs. The spec is the law: /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/spec-unharness.md, part "3.6.0". The owner's answers are in queue-long-run.md entries 27–41 (same folder). Diff to review: `git -C /Users/ryzhakar/LLM_MANIFESTOS.worktrees/digests diff 9e91351..feat/digests`.

Aspects (one per reviewer; the launch message names yours):
- code: correctness against the spec, cover algorithm (exact cover, minimal characters, tie-break, overlap on/off), index staleness, refusal messages verbatim, flag implication, doctor exit codes, test coverage of each spec test item (section (h)), stdlib only, duplication (knowledge with two homes), dead code. Run the suite: `uv run --project plugin/unharness pytest -q plugin/unharness`.
- prose: the compile-digest skill, the compile-commitments skill changes, the docs (plugin/README.md Unharness section, plugin/unharness/README.md, plugin/SCHEMA.md), the repo's `.min.md` pair: Strunk's rules, every stated flag/verb/file/message matches the code verbatim (check with `--help` and grep), no padding, no claim the code does not back.
- spec: every spec statement in the 3.6.0 part is implemented or tested, and every implemented behavior is in the spec; list each mismatch with spec line and code line; list each of the 11 spec decisions and whether the code honors it.

Report: /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/reviews/digests-<aspect>.md with sections Blocking (must fix before release), Should fix, Nits; each finding: file:line, what, why, the fix in one line. No praise. End your reply with a 3-sentence summary and the counts.
Tools: Read, Grep, Glob, Bash (git diff, pytest, --help). Do not edit product files.
