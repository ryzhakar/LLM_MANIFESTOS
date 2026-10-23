# Baseline: long-run, at closure 2026-10-23

Replaces baseline-manifesto-tone.md of 2026-10-22.

- github.com/ryzhakar/llm-manifestos `main` is 002db33 plus this records commit, tag v3.5.0; `plugin/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` read 3.5.0; `plugin/unharness/pyproject.toml` reads 3.5.0.
- `plugin/unharness/` is the package (72 pytest tests under its tests/); `plugin/hooks/parse_config.py` and `mini_yaml.py` no longer exist; the hook suite (`python3 -m unittest discover -s plugin/tests`) passes; both `claude plugin validate` runs and `just readme` pass.
- `.manifestos.interplay.md` and `.manifestos.commitments.md` sit in the repo root and match the stack in `.manifestos.yaml`.
- Captures and recon stay local under `orchestration_log/recon/2026-10-23/` (ignored); the frozen evidence is `history/2026-10-23/verification-unharness.md`.
- No wake, agent, worktree, or wait remains; the member's card is in `departed/`, and the stewardship is open.

## After span 2 (digests), 2026-10-23
main fb7e3ae + records 16ccf1d; tag v3.6.0; plugin 3.6.0; 190 tests; no worktrees, no feature branches, no wake. Open for the owner: queue 44 (digest word-cap drop rule), plugin update to 3.6.0 in the logins, PyPI publish. Summary: summary-digests.md.
