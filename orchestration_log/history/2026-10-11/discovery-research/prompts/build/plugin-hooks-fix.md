CONSTITUTION BINDING — do this before the task body. Load each element completely from source, run the binding protocol in element 3 (deconstruct, map convergence and tension, activate), write the binding as the first lines of your report, then proceed. You rebind from source on this dispatch.
1. First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md
2. Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml
3. Binding protocol — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md
4. TDD — /home/user/claude-skills/dev-discipline/skills/tdd/SKILL.md
5. Ethos — /home/user/claude-skills/ETHOS.md

ROLE: You are repairing the manifesto plugin's binding channel so the text the model receives at session start, after compaction, and at subagent start is complete and under the host's cap.

CONTEXT: Repository /home/user/claude-skills (HEAD detached at main). Verified defects, with evidence in /home/user/LLM_MANIFESTOS/research/manifesto-craft/resolutions/runtime-defects-verification.md and deep-dives/runtime-audit.md (read both whole first): (A) Claude Code persists hook stdout over 10,000 characters and shows the model a 2KB preview; session-start.sh emits 10,758 characters, cut before the oath body. (B) PostCompact is not an event in the host's hookSpecificOutput schema; post-compact.sh output never reaches the model. (C) The SessionStart matcher `startup|resume` misses source `compact`, the host's post-compaction SessionStart.
Owner decisions: hooks never inline the oath skill text; they name it and command the model to load it (the skill is installed). Hook stdout stays under 8,000 characters with a two-element config. Delete the PostCompact hook. SessionStart matcher becomes `startup|resume|compact`. Subagent hook gets the same treatment. Versions live in plugin.json only; bump minor (3.2.0 → 3.3.0). Conventional single-line commits, no attribution, atomic by artifact class: shell scripts and hooks.json in one commit; templates in one; SCHEMA.md and README text in one; plugin.json bump in one.

INPUT FILES: everything under /home/user/claude-skills/manifesto/hooks/, /home/user/claude-skills/manifesto/SCHEMA.md, /home/user/claude-skills/manifesto/.claude-plugin/plugin.json, /home/user/claude-skills/manifesto/README.md, /home/user/claude-skills/.manifestos.yaml, /home/user/claude-skills/justfile, /home/user/claude-skills/generate.py (how plugin READMEs are generated).

TASK:
1. `git -C /home/user/claude-skills checkout -b manifesto-binding-channel main`.
2. Write a test script /home/user/claude-skills/manifesto/hooks/test_hooks.sh (bash, no new dependencies) that runs each hook with the live .manifestos.yaml as config, MANIFESTO_DIR pointed at /home/user/LLM_MANIFESTOS, the stdin JSON the host sends (source startup, resume, compact for SessionStart; an agent_type for SubagentStart; a prompt for UserPromptSubmit), and asserts: stdout parses as JSON; hookSpecificOutput.hookEventName is one the host accepts; additionalContext length < 8000 characters; the text contains the literal command to load the manifesto-oath skill and contains every element name and purpose from the config; no oath skill body text is present (grep for a distinctive sentence from the skill, e.g. "You are a knight receiving an oath"). Run it first; it must fail on the current code for the length and inline-text assertions. Record the failing output in the report.
3. Change the shell scripts and templates so the tests pass: replace the inlined oath text with a load command naming the skill (`manifesto:manifesto-oath`) and the steps the model must then run (resolve, read whole, interplay, commit, verify) in at most 25 lines; keep element names, purposes, sources, manifesto dir, plugin cache path; keep the SUBAGENT BINDING REINFORCEMENT footer. Delete post-compact.sh and its hooks.json entry and its template part; set the SessionStart matcher to `startup|resume|compact`; make the session-start preamble say which source fired (startup, resume, compact) in one line. Keep drift-reminder.sh unchanged.
4. Run the tests until green. Then run the real harness once from a scratch dir: `claude -p --plugin-dir /home/user/claude-skills/manifesto --output-format json 'reply with the single word ok'` with any debug flag that shows hook output; record whether the SessionStart text now arrives whole (no persisted-output wrapper). Do not use bypassPermissions; if denied, record it and continue.
5. Update SCHEMA.md's Hook behavior section and README text to match; regenerate the plugin README with the repo's generator if it covers it (`just readme` or `python3 generate.py`; read the justfile).
6. Bump plugin.json to 3.3.0.
7. Commit in the atomic order given. `git push -u origin manifesto-binding-channel` with up to 4 retries (2s, 4s, 8s, 16s).

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/plugin-hooks-fix-report.md

REPORT FORMAT:
(binding lines)
# Plugin Hooks Fix
## Red — the failing test output before changes
## Green — the passing output after, with character counts per hook
## Harness run — command, result, whether the text arrived whole
## Commits — table: hash | message | files
## Open — anything not done and why

SCOPE: Hooks, templates, SCHEMA.md, README, plugin.json only. Do not touch the skills or the agent. No attribution lines in commits.

TOOLS: Read; Edit; Write; Bash; Grep.

End with a 3-sentence summary for a notification: test status, SessionStart character count after, push result.
