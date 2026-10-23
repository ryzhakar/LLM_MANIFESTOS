# C5 — documentation for unharness 3.6.0

1. Role: you update the plugin's documentation to match the 3.6.0 code and spec.
2. Context: unharness 3.6.0 adds `--digests`, `--stack-digests`, `--overlap`, `--minified` on `prompt`/`stack`, the `stamp` and `doctor` verbs, the `index.json` digest sidecar, the `.min.md` session files, and the `/compile-digest` skill. Work in /Users/ryzhakar/LLM_MANIFESTOS.worktrees/digests (branch feat/digests). Start only after `git log --oneline feat/digests` shows commits for digest sources, minified session files, doctor verb, and compile-digest; if any is missing, wait and re-check.
3. Inputs: the spec part "3.6.0" in /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/spec-unharness.md; the code in plugin/unharness/src/unharness/ (read cli.py, digests.py, doctor.py for the real flags and messages); plugin/README.md ("Unharness" section); plugin/unharness/README.md; plugin/SCHEMA.md; README.template.md; plugin/skills/compile-digest/SKILL.md.
4. Task: update each document so every flag, verb, file name, and message it states matches the code verbatim (run `uv run --project plugin/unharness unharness --help` and each verb's `--help` to check). Add: digest mode and the cover rule in one paragraph; the four flags; `stamp` and `doctor` with one example each; the index sidecar shape; the `.min.md` pair; the compile-digest skill in the skills list. Keep each addition as short as a true statement allows; delete nothing that is still true. Bump nothing (versions are bumped at release).
5. Output: the edited docs; report at /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/c5-report.md listing each file and what changed.
6. Commit: `doc(plugin): unharness 3.6.0 digests, minified files, doctor`.
7. Scope: docs only.
8. Tools: Read, Edit, Grep, Glob, Bash.
9. Strunk: definite, active, no padding. End with a 3-sentence summary.
