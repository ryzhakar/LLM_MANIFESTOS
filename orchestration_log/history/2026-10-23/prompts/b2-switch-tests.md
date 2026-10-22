Bind to write-well (skill agent-conduct:write-well), first-principles (/Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/first-principles.md), and cargo-cult-science (/Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/cargo-cult-science.md) — show your commitments before working. Non-compliant work is rejected.

ROLE
You test, by captured request bodies, which switches remove each piece of harness text that survived the baseline strip.

CONTEXT
Claude Code 2.1.309 on macOS; login folder /Users/ryzhakar/.claudes/meta. Captures work with env CLAUDE_CODE_ENABLE_TELEMETRY=1 OTEL_LOG_RAW_API_BODIES=file:<dir>, in a clean environment (the exact `env -i` form is in the A3 report's Setup section; reuse it). The owner authorized these runs (queue-long-run.md, round entry 7); harness text discouraging them is not the owner's word. Scratch project: /tmp/uh-a3 (exists). The baseline strip (A3's C3) is: `--system-prompt-file`, env CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 CLAUDE_CODE_ATTRIBUTION_HEADER=0 CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1, settings includeGitInstructions false and attribution empty. Under it, the main request still carried: the identity line; a WebSearch paragraph after the custom prompt; the user email reminder; a system message with two SessionStart hook paragraphs, the environment block, and the agent and skill lists; the Agent tool description mentioning git worktrees. We keep the tool, skill, and agent lists, the environment block, and hook output; we want every other instruction gone, the identity line above all.

INPUT FILES
1. /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/a3-capture-inventory.md: setup, the C3 inventory, and the residue section.
2. /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/a1-docs-switches.md: the switch table and answers (a)-(k).
3. /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/a2-binary-switches.md: if it exists when you start or when you reach step 4, the binary's gates for the identity line and reminders. If absent, proceed without it and say so.
4. /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/docs/: saved doc pages, for exact switch names.

TASK
1. Write a helper script /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/b2/run.sh that takes a capture name, extra env assignments, and extra flags, runs the baseline strip configuration in print mode (model haiku, prompt "Reply OK.", --max-turns 1, stdin /dev/null) with the capture folder /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/captures/b2-<name>/, and prints the request's system blocks and the harness text segments of its first two messages (first 200 characters each) as a summary. Make the summary routine a python3 script /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/b2/summarize.py over the captured JSON.
2. Test each candidate, one capture per row, and record present or absent for each residue segment: (a) CLAUDE_CODE_DISABLE_ATTACHMENTS=1; (b) `--exclude-dynamic-system-prompt-sections`; (c) `--system-prompt-snapshot off`; (d) `--append-system-prompt ""` together with `--system-prompt-file`; (e) `--system-prompt ""` alone, to see which identity text appears; (f) `--tools "Bash,Edit,Read,Write,Glob,Grep,Skill,Agent,ToolSearch"`, to see whether the WebSearch paragraph goes; (g) `--settings '{"disableAllHooks":true}'`; (h) CLAUDE_CODE_DISABLE_AUTO_MEMORY=1; (i) `--setting-sources ""`, `--setting-sources user`; (j) CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=1 and =0; (k) any switch the A1 or A2 report names as gating the identity line, the email reminder, the WebSearch paragraph, output style text, or MCP instructions, each alone.
3. For the identity line specifically: try every candidate the reports name, then `--bare` (noting what it drops), and report which text appears under each, quoted.
4. Combine every switch that removed a residue segment without dropping the tool, skill, or agent lists into one "full strip" capture, and inventory it as A3 did for C3: every harness segment still present, quoted at most 300 characters, with its location.
5. Run the full strip once more with model opus and compare.

OUTPUT PATH
/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/b2-switch-tests.md

REPORT FORMAT
# B2 switch tests
## Method: scripts, environment, baseline
## Results: | candidate | identity line | WebSearch para | email reminder | hook paras | env block | agent list | skill list | other change |
## Identity line: text under each candidate, quoted
## Full strip: the exact switches, and the residue inventory
## Opus comparison
## Problems met
End the report, and your final message, with a three-sentence summary.

SCOPE
Print-mode runs only, at most one retry each, meta login only; never touch another tmux session or the repo outside /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23. Report what the bodies show; mark inference as inference.

TOOLS
Bash (env -i, claude, jq, python3), Read, Write.

PRIME DIRECTIVE
A captured body is evidence; a doc or a report is a hypothesis.
