# Shared brief for code units C1–C3 (unharness 3.6.0)

Role: you implement one unit of the unharness Python package by TDD, inside the worktree /Users/ryzhakar/LLM_MANIFESTOS.worktrees/digests (branch feat/digests). Work there only.

Context: unharness is a stdlib-only Python ≥ 3.11 package at plugin/unharness (uv_build backend, tests in plugin/unharness/tests, run with `uv run --project plugin/unharness pytest -q plugin/unharness`). It compiles a system prompt from `.manifestos.yaml`. Version 3.5.0 is shipped; you add the 3.6.0 features. The spec is the one home of the design: /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/spec-unharness.md, part "3.6.0". Read the whole part, then the existing code: src/unharness/{config.py,resolve.py,compile.py,cli.py,launch.py}. Follow the code's existing style: small pure functions, dataclasses, errors as UnharnessError subclasses with the message text the spec gives verbatim, no third-party imports.

Rules:
- TDD: write the failing test first for each behavior the spec names for your unit, then the code, then refactor. Keep every existing test green.
- Knowledge has one home: hashing lives in resolve.py (reuse it), digest logic in src/unharness/digests.py, doctor in src/unharness/doctor.py, CLI wiring in cli.py.
- No comments that restate code; docstrings only where the name does not say it.
- Commit on feat/digests when your unit is green: one commit per unit, subject `type(scope): subject` ≤ 10 words, no body, no trailer, no attribution. Do not push. Do not touch files outside your unit's list (another agent may be editing them); if you must change a shared file (cli.py, compile.py), keep the change minimal and additive.
- Write a report to /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/<unit>-report.md: what you built, test count before/after, the exact commands you ran with their last lines, any spec gap you met and how you resolved it (name the choice and its closest alternative). End your reply with a 3-sentence summary.

Tools: Read, Write, Edit, Grep, Glob, Bash (for pytest, git). Run the full suite before committing.
