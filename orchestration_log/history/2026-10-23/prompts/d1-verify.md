Bind to write-well (skill agent-conduct:write-well) and cargo-cult-science (/Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/cargo-cult-science.md) — show your commitments before working. Non-compliant work is rejected.

ROLE
You verify, by captured request bodies, what the model receives when Claude Code is started through the built unharness tool.

CONTEXT
Claude Code 2.1.309; login /Users/ryzhakar/.claudes/meta. The tool lives in the worktree /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/plugin/unharness (run it as `uvx --from <that path> unharness ...`; do not edit it). Its config for this test is the repo's /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/.manifestos.yaml, but `unharness prompt` stops without the session files .manifestos.interplay.md and .manifestos.commitments.md, which no session has written yet; for this verification create a scratch project /tmp/uh-d1 (git init, a CLAUDE.md with "Marker: PAPAYA-7", one commit) with a small .manifestos.yaml (manifesto_dir pointing at /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/plugin, elements: dry and lines-spent, plus `source: skill agent-conduct:write-well`), run `unharness stack` there, and write the two session files by hand in the shape the skill /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness/plugin/skills/compile-commitments/SKILL.md prescribes, with placeholder sentences such as "I must give each piece of knowledge one home, and I will point to it." Captures: env CLAUDE_CODE_ENABLE_TELEMETRY=1 OTEL_LOG_RAW_API_BODIES=file:<dir>, in the clean environment described in /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/a3-capture-inventory.md (Setup). The owner authorized these runs (queue-long-run.md, round entry 7). Never touch another tmux session.

INPUT FILES
1. /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/b2-switch-tests.md, section "Full strip", the expected residue.
2. /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/b2/summarize.py, a request summarizer you may reuse.
3. The worktree's plugin/README.md section "Unharness" if it exists by the time you read it; otherwise the spec's Strip set in /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/spec-unharness.md.

TASK
1. In /tmp/uh-d1: `unharness prompt > /tmp/uh-d1/prompt.md`; `unharness launch "$(cat prompt.md)"` with no launcher, and record the printed command.
2. Print-mode capture (haiku): `unharness prompt | unharness launch -- claude -p "Reply OK." --model haiku --max-turns 1` with the capture variables in the environment, stdin for the pipeline from the prompt (launch reads the prompt from stdin, so for -p pass the prompt as the PROMPT argument instead and let stdin be /dev/null); capture to /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/captures/d1-p-haiku/.
3. The same with opus, to /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/captures/d1-p-opus/.
4. Interactive capture (haiku) in a tmux session you create (`tmux new-session -d -s uh-d1 -x 200 -y 50`), with the pipeline form `unharness prompt | unharness launch -- claude --model haiku`, then send "Reply OK." and later "/exit"; capture to /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/captures/d1-tmux-haiku/; kill the session after.
5. For each capture, inventory the first main request: system blocks (the custom prompt must be system block after the identity line, verbatim: compare its text with prompt.md by hash); whether CLAUDE.md, git instructions, attribution, auto memory, output style, the WebSearch paragraph, and the silent-turn note are absent; whether the tool list, skill list, agent list, environment block, and hook paragraphs are present; and every other harness segment, quoted at most 300 characters.
6. Compare with B2's full strip: list every difference.
7. Verify the flags: `--keep-claude-md` brings CLAUDE.md back (one haiku print capture); `--no-hooks` removes the hook paragraphs (one capture); `--keep-web-search` brings the paragraph back (one capture).

OUTPUT PATH
/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/d1-verification.md

REPORT FORMAT
# D1 verification
## Setup and commands (verbatim)
## Printed command (verbatim)
## Captures: one inventory table per capture
## Residue list with locations
## Differences from B2's full strip
## Flag checks
## Failures and anything unverified
End the report, and your final message, with a three-sentence summary.

SCOPE
Do not edit the worktree or the main checkout; write only under /tmp/uh-d1 and /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23. One retry per capture.

TOOLS
Bash (uvx, claude, tmux, jq, python3), Read, Write.

PRIME DIRECTIVE
Report what the bodies contain; a README claim is a hypothesis until a capture shows it.
