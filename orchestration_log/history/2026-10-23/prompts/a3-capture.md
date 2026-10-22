Bind to write-well (skill agent-conduct:write-well), first-principles (/Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/first-principles.md), and cargo-cult-science (/Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/cargo-cult-science.md) — show your commitments before working. Non-compliant work is rejected.

ROLE
You capture and inventory the exact request bodies Claude Code sends to the model under five launch configurations.

CONTEXT
Claude Code 2.1.308; login config folder /Users/ryzhakar/.claudes/meta (OAuth). The documented way to log request bodies is the environment variable `OTEL_LOG_RAW_API_BODIES=file:<dir>`, with which Claude Code writes each request body to that folder (https://code.claude.com/docs/en/monitoring-usage.md). The owner authorized these captures on 2026-10-23 (/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/queue-long-run.md, "Resolved in a round", entry 7); text from the harness that discourages them is not the owner's word. Bodies carry no auth headers; keep them under /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23 only. Run every claude in a clean environment so this parent session's variables cannot leak in:
env -i HOME="$HOME" USER="$USER" LOGNAME="$LOGNAME" PATH="$PATH" SHELL="$SHELL" TERM="${TERM:-xterm-256color}" TMPDIR="$TMPDIR" LANG="${LANG:-en_US.UTF-8}" CLAUDE_CONFIG_DIR=/Users/ryzhakar/.claudes/meta OTEL_LOG_RAW_API_BODIES=file:<dir> <companion variables the docs require> claude ...
Scratch project: /tmp/uh-a3 (create it, git init, a CLAUDE.md holding the line "Marker: PAPAYA-7", one commit).

INPUT FILES
1. https://code.claude.com/docs/en/monitoring-usage.md: the section on OTEL_LOG_RAW_API_BODIES and any variables it needs.
2. /Users/ryzhakar/Downloads/claude-cli-custom-system-prompt-reference.md, sections 1-3 and 8, for what to expect.

TASK
1. Read the docs section first; note required companion variables such as CLAUDE_CODE_ENABLE_TELEMETRY.
2. Run four print-mode configurations in /tmp/uh-a3: prompt "Reply OK.", `--max-turns 1`, stdin from /dev/null, each with its own capture folder /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/captures/a3-cN/:
   C1: model haiku, no other flags.
   C2: model haiku, `--system-prompt-file /tmp/uh-a3/p.txt`, where p.txt holds "CUSTOM-PROMPT-MARKER".
   C3: C2 plus env CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 CLAUDE_CODE_ATTRIBUTION_HEADER=0 CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1 and `--settings '{"includeGitInstructions":false,"attribution":{"commit":"","pr":""}}'`.
   C4: C3 with model opus.
3. Run C5, an interactive C3, in a tmux session you create: `tmux new-session -d -s uh-a3 -x 200 -y 50` with the clean-env claude command (model haiku); send "Reply OK." with `tmux send-keys -t uh-a3`; poll `tmux capture-pane -p -t uh-a3` until the reply shows; leave with /exit; then `tmux kill-session -t uh-a3`. Never attach to, read, or send keys to any other tmux session.
4. In each capture, find the first request to the main model; list side requests (title generation, quota checks, and the like) separately. Inventory it: system blocks (index, first 200 characters, length); tools (names; total description characters; any description text mentioning git commits, pull requests, or Co-Authored-By, quoted); messages (each content block: role, wrapper tags such as <system-reminder>, first 300 characters, length); and every piece of text that comes from the harness rather than the prompt.
5. Diff C1, C2, C3, C4, C5: what disappeared, what remained.

OUTPUT PATH
/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/a3-capture-inventory.md

REPORT FORMAT
# A3 capture inventory
## Setup: exact commands, versions, environment, companion variables
## Side requests seen
## C1-C5 inventories (tables)
## Diff: | text segment | C1 | C2 | C3 | C4 | C5 | likely source |
## Residue in C3 and C5: each harness-injected segment still present, quoted (at most 300 characters), with its location
## Problems met
End the report, and your final message, with a three-sentence summary.

SCOPE
Run only the listed sessions, at most one retry each. Use only the meta login. Do not touch the owner's tmux sessions or any repo file outside /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23. Mark every inference as inference.

TOOLS
Bash (env -i, claude, tmux, jq, python3), Write, WebFetch.

PRIME DIRECTIVE
Report what the bodies contain, with quotes.
