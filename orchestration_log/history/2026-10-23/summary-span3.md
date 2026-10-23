# Summary: span 3 (2026-10-23) — releases 3.6.1–3.7.2, PyPI, discovery

Closed at the owner's order after the 3.7.2 patch. main 335fae6; tags v3.6.1, v3.7.0, v3.7.1, v3.7.2 and their pypi- twins; every pypi- tag published by the trusted-publisher workflow; PyPI serves unharness 3.7.2. 290 tests.

## Shipped
- 3.6.0 (earlier span): digests, minified session files, signatures, doctor, compile-digest.
- PyPI: MIT license, package metadata, first upload by the owner's token; `.github/workflows/publish.yml` on `pypi-<semver>` tags by trusted publishing; convention in MAINTAINERS_GUIDE.md "Releasing".
- 3.6.1: `CLAUDE_CODE_TODO_REMINDER_MODE=off` and `CLAUDE_CODE_TOTAL_TOKENS_REMINDER=off` (from X1's findings); BrokenPipe fix; Block/Document merge; doctor `claude` version range; compile-digest carries the digest method; every hook stands down under UNHARNESS=1.
- 3.7.0: `switches.json` registry (one home), `unharness switches` table, README table generated and pinned by test; launch output byte-identical.
- 3.7.1: launch detects the launcher's Claude Code version and selects verified switches; `--claude-version`; doctor registry lines.
- 3.7.2: silent-turn switch marked undocumented; a test ties registry flags to the baseline sweep.
- Repo-local skill `sweep-switches` with `sweep.py` and the baseline `.claude/switch-sweeps/2.1.309.json`.
- Preamble paragraph on harness nudges (owner order).

## Findings
- identity-line-findings.md: the identity block is not removable (API refuses without it); task nudge and token line have undocumented switches; silent-turn switch confirmed.
- Sweep baseline: 858 undocumented env names; candidates for capture in queue 56 (REMOVE_PROMPT_STRINGS, APPEND_PROMPT_HEAD, subagent-prompt names, reminder tunables).

## Open for the owner
- Queue 56: capture pass on the sweep candidates (may touch the identity line and subagent binding).
- Queue 48: `--settings` merge (3.8.0) and `stack --diff` (3.9.0), not started.
- Queue 45: subagents get no plugin binding under unharness (owner's agentic-delegation covers it).
- Conduct: repeated padding calls on harness nudges despite three owner corrections; logged in events-long-run.md. The shipped preamble names the rule; this session did not keep it.
