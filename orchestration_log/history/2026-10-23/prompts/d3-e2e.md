Bind to write-well (skill agent-conduct:write-well) and cargo-cult-science (/Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/cargo-cult-science.md) — show your commitments before working. Non-compliant work is rejected.

ROLE
You run the whole unharness flow end to end in this repository and report what happened, step by step.

CONTEXT
Worktree /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness on branch feat/unharness holds the built plugin (plugin/) with the tool at plugin/unharness and the skill plugin/skills/compile-commitments. The installed manifesto plugin is 3.4.0 and lacks the skill, so load the worktree's plugin with `--plugin-dir /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/plugin`. Login: /Users/ryzhakar/.claudes/meta. The owner authorized these runs (queue-long-run.md, round entry 7). Use tmux sessions you create and kill; never touch another tmux session. The two session files this flow writes in the worktree root are products to commit on feat/unharness.

TASK
1. Compile the commitments with an opus session, in print mode, from the worktree root, clean environment as in /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/a3-capture-inventory.md (Setup) plus CLAUDE_CONFIG_DIR: `claude -p "/compile-commitments" --model opus --plugin-dir /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/plugin --max-turns 40`, stdin /dev/null; if the slash form does not invoke the skill in print mode, pass the prompt "Run the skill compile-commitments for the config at /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/.manifestos.yaml; the plugin's bin/unharness is at /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/plugin/bin/unharness; set UNHARNESS_FROM=/Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/plugin/unharness so the launcher uses the local package." Record the exit status and the session's last message. Confirm /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/.manifestos.interplay.md and /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/.manifestos.commitments.md exist, open with a <stack> block, and that `UNHARNESS_FROM=/Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/plugin/unharness /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/plugin/bin/unharness prompt --config /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/.manifestos.yaml > /tmp/uh-d3-prompt.md` exits 0; report the prompt's line count and the names of its constitution tags.
2. Commit the two files on feat/unharness in /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness with the message "feat(repo): interplay and commitments for the stack" and nothing else staged.
3. Interactive run, haiku, in tmux (`tmux new-session -d -s uh-d3 -x 200 -y 50`, working folder /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness), through the documented pipeline with the local package: `UNHARNESS_FROM=/Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/plugin/unharness /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/plugin/bin/unharness prompt | UNHARNESS_FROM=/Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/plugin/unharness /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/plugin/bin/unharness launch -- claude --model haiku --plugin-dir /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/plugin`, with CLAUDE_CODE_ENABLE_TELEMETRY=1 OTEL_LOG_RAW_API_BODIES=file:/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/captures/d3-tmux/ in the environment. Then, waiting for each reply through `tmux capture-pane -p`: (a) ask "Name the elements that govern you, one per line, from your own context, and nothing else."; (b) ask "Does any CLAUDE.md text or a secret word appear in your context? Reply with the word or NONE."; (c) run `/compact`; (d) ask (a) again; (e) ask "Quote the first line of your commitments."; (f) `/exit`; kill the session.
4. From the captures, confirm the first request's system block after the identity line equals /tmp/uh-d3-prompt.md (hash), and that after the compaction the request still carries it as the system prompt.
5. Record each reply verbatim.

OUTPUT PATH
/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/d3-e2e.md

REPORT FORMAT
# D3 end to end
## Step 1: command, exit, last message, file checks, prompt line count and tags
## Step 2: commit sha
## Step 3: the pipeline command; replies (a)-(e) verbatim
## Step 4: hashes before and after compaction
## Failures and anything unverified
End the report, and your final message, with a three-sentence summary.

SCOPE
Edit nothing in the worktree except through the skill run and the one commit; do not push. One retry per step.

TOOLS
Bash (claude, tmux, git, uvx, jq, python3, sha256sum or shasum), Read, Write.

PRIME DIRECTIVE
Report what happened, with the replies quoted; a step that did not run is a failure to name, not to explain away.
