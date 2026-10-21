# Queue: taking over the `manifesto` plugin

Owner order (2026-10-21): this repo is the home, name kept, everything ships together; contact stewards freely. Owner is away by default. Facts: `orchestration_log/recon/2026-10-21/plugin-takeover-facts.md`.

## Unsolved (irreversible, the owner's)

1. **Push the marketplace to the public repo.** Publishing `.claude-plugin/marketplace.json` and `plugin/` to `origin/main` makes them installable and is not cheaply undone. Work waits locally on a branch; nothing is pushed.
2. **Final marketplace name.** Provisional `llm-manifestos`; fixed once published. Waits on item 1.
3. **Owner acts.** `/plugin marketplace add`, uninstall the old `manifesto@my-claude-skills`, install the new, `/reload-plugins`, clear the stale project-scope 3.1.4 record. I cannot run these.
4. **Retiring the claude-skills copy.** The `claude-skills` scribe drops its entry and directory only after the new install is verified. Waits on item 3.
5. **Release.** Version bump and tag in one step with the push (memento lesson: an untagged release stayed installed about 30 hours). Waits on item 1.

## Solved (reversible, acted on)

1. **Where the work happens:** a worktree and branch `plugin/move-manifesto` in this repo, plugin copied to `plugin/`, local commits only. Alternative: a new repo for the plugin.
2. **Manifest shape:** repo-root `.claude-plugin/marketplace.json` with `"source": "./plugin"`, as memento and peers do. Alternative: `"source": "./"` caching the whole repo.
3. **How the plugin finds manifestos:** keep the tier-1 clone mechanism (`.claude/manifesto-repo/`) unchanged for now. Alternative: bundle `manifestos/` inside `plugin/`.
4. **Version:** 3.2.0 unchanged on the branch; the bump comes with the release (unsolved 5). Alternative: bump to 3.3.0 on the branch.
5. **Claiming the stewardship:** card `stewards` edit plus `[notice]` with the owner's order as `[quote]`, after the new install is verified. Alternative: claim now.
6. **Decoupling with `instruction-eval`:** their change list confirmed (messages 2026-10-21T12:48+0300); skill name `manifesto:manifesto-oath` stays; I owe them the final marketplace id before the move. Alternative: keep the hard dependency and the `@my-claude-skills` suffix.
7. **Old marketplace entry stays** in `claude-skills` until verification. Alternative: remove it with the copy.
- Unsolved, the owner's: claude-skills CLAUDE.md names the old local clone path `.claude/manifesto-repo/LLM_MANIFESTOS/manifestos/`; its header forbids edits by anyone but the owner. Waits for the owner.
- Unsolved, the owner's (replaces the CLAUDE.md item above): claude-skills CLAUDE.md was edited by the instruction-eval session in 9f879a0 (lines 15-16 repointed) against its own no-edit header; confirm the owner authorized it, else revert 9f879a0. I did not ask them; the owner was not shown the diff.
- Withdrawn (2026-10-21, owner: "claude-skills is not your concern, at all."): the claude-skills CLAUDE.md, PITCH.md and instruction-writer.md items; nothing of mine remains open there.
