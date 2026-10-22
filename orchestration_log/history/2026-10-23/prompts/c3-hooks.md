Continue in your worktree /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness on feat/unharness. I merged feat/unharness-oath into it: the real preamble (15 lines) and plugin/skills/compile-commitments/SKILL.md are now there; rerun the suite first and fix any test that assumed the placeholder preamble.

Answers to your open questions, all settled:
- A double quote in a purpose becomes a single quote in `governs`; test it.
- An empty stack stops `prompt` and `stack` with the one-line error "the stack is empty"; test it.
- Commit `uv.lock`.
- Your hash scope (after frontmatter, before ${CLAUDE_PLUGIN_ROOT} replacement) stands. The stricter errors stand. Legacy path and URL sources failing at resolution stands.

Next unit, C3, the hooks, same binding, same worktree. Read /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/a4-repo-facts.md sections 2, 3, and 7, and the spec sections "Config schema, evolved" and "Manifesto plugin hooks under unharness" in /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/spec-unharness.md.

1. Make the hooks read the stack through your config module alone: each shell hook calls `python3 "${CLAUDE_PLUGIN_ROOT}/unharness/src/unharness/config.py" <config> --json` (or the shape your CLI exposes) and renders from that; delete plugin/hooks/parse_config.py and plugin/hooks/mini_yaml.py and every call to them. Keep the hooks' rendered output identical for this repo's .manifestos.yaml except where the evolved schema adds a source type: render `source: file <path>` as a read of the absolute path, `source: manifesto <name>` as today's registry read, and `source: skill ...` as today. A list item containing a colon must no longer crash a hook.
2. Stand-down: when the environment variable UNHARNESS is set and not "0", session-start.sh and post-compact.sh print nothing and exit 0; drift-reminder.sh and subagent-start.sh keep running. Keep the session-start hook's repo check (ensure-repo.sh) behavior unchanged otherwise.
3. Add tests in plugin/tests/ for: the three source types rendered by session-start, the colon item, the stand-down for both hooks, and that drift-reminder still prints under UNHARNESS=1. Run the existing 8 hook tests and yours; run `claude plugin validate plugin` and `claude plugin validate .` from the worktree root.
4. Update plugin/SCHEMA.md to the evolved schema (every element form, source form, default, and error, as the parser implements them) and plugin/hooks/hooks.json only if a path changed.
5. Commit in small steps, same message rules, no push.

Write the report to /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/reports/c3-hooks.md with sections: Commits; What each hook reads and prints now; Tests (names, result); Validation results; Deviations with reasons; Open questions. End with a three-sentence summary.
