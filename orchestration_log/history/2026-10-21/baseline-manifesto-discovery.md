# Baseline: manifesto-discovery, at span end 2026-10-21

- github.com/ryzhakar/llm-manifestos (renamed from LLM_MANIFESTOS, old name redirects) main is 1fc97b3, tag v3.3.0. The `manifesto` plugin 3.3.0 lives in `plugin/` with `manifestos/` and `digests/` bundled; `.claude-plugin/marketplace.json` names the marketplace `llm-manifestos`. 8 hook tests pass; both `claude plugin validate` runs pass.
- Installed in every login: `manifesto@llm-manifestos` 3.3.0 and `instruction-eval@my-claude-skills` 0.2.0, user scope. The old `manifesto@my-claude-skills` is removed from installs, caches and the old marketplace.
- I hold the plugin's stewardship (card `stewards`). The default binding id in instruction-eval is `manifesto@llm-manifestos`; skill `manifesto:manifesto-oath`.
- Records: session branch `session/manifesto-discovery` carries the journal, queue and summary; origin/main holds only the plugin work. Local worktree /Users/ryzhakar/LLM_MANIFESTOS.worktrees/plugin-move and branch `plugin/move-manifesto` remain, merged.
- Digest eval of only-what-it-needs: cut 1 failed its gate; the cut 2 hypothesis at evals/only-what-it-needs/cut-2/hypothesis.md is unapplied.
- A heartbeat cron (a9e5670c, every 3 hours, session-only) is set and expires about 2026-10-22; no agent or other wait is pending. The peer society's commons count read: 98.
- claude-skills is out of scope by the owner's ruling.
