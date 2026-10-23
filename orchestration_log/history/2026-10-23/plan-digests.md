# Plan: unharness 3.6.0 — digests, minified session files, signatures, doctor

Status: DONE 2026-10-23. Shipped as 3.6.0 (fb7e3ae, tag v3.6.0).
Branch: session/long-run (product work on feat/digests worktree, rebased onto session/long-run, then main on completion; tag v3.6.0).

Units (sonnet unless noted; records in history/2026-10-23/, reports in recon/2026-10-23/):
- S1 (opus): extend spec-unharness.md with §Digests, §Minified, §Signatures, §Doctor, §compile-digest from queue 27–41. → spec is the one home.
- C1: digests.py — locate single/stack digests (local then plugin), read index.json, refuse missing/stale, shortest exact cover (overlap on/off), flags wired into compile/cli; `stamp` verb. Tests.
- C2: minified session files (.min.md) under --minified; compile-commitments skill writes both. Tests.
- C3: doctor verb. Tests.
- C4 (opus): plugin skill compile-digest; (haiku) stamp the 15 shipped digests via `unharness stamp`.
- C5: docs — SCHEMA.md, plugin README Unharness section, unharness README, README.template line.
- D1: review (code/prose/spec), D2: fix pass, D3: e2e capture in digest+minified mode (prompt verbatim, sizes), D4: release 3.6.0, ship main, tag.
