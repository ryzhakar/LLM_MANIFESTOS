Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it.

ROLE: You are independently verifying two defect claims about a Claude Code plugin's hooks. Do not read the report that made the claims.

CONTEXT: Plugin at /home/user/claude-skills/manifesto. Local Claude Code CLI is installed (`claude --version`). Manifesto repo for the hooks: /home/user/LLM_MANIFESTOS. Live config example: /home/user/claude-skills/.manifestos.yaml.

CLAIMS TO TEST:
A. Claude Code caps injected hook text at 10,000 characters; the SessionStart hook of this plugin emits more than that, so the model receives only a truncated preview that ends before the oath protocol body.
B. The PostCompact hook's JSON output fails Claude Code's hook-output schema validation, so no plugin text reaches the model after compaction.

INPUT FILES: /home/user/claude-skills/manifesto/hooks/hooks.json, session-start.sh, post-compact.sh, templates/parts/*.txt, parse_config.py, mini_yaml.py.

TASK:
1. Run session-start.sh and post-compact.sh directly with the environment and stdin they expect (read the scripts to find both; set the manifesto dir to /home/user/LLM_MANIFESTOS; cwd /home/user/claude-skills). Capture stdout and stderr; record byte and character counts of stdout; validate any JSON stdout with `python3 -I -c 'import json,sys; json.load(sys.stdin)'` and record the exact field names at the top level and under hookSpecificOutput.
2. Find the primary source for the 10,000-character cap: search the installed Claude Code CLI bundle (locate it via `which claude`, then grep the JS for strings near "10000", "truncat", "hook", "additionalContext") and quote the matching line with its file and byte offset. If no such cap exists in the bundle, say so.
3. Find the primary source for the hook-output schema the CLI validates (same bundle; grep for "hookSpecificOutput", "additionalContext", "PostCompact", "SessionStart", "zod" or "parse"), and quote the fields it accepts for PostCompact and SessionStart.
4. Run the real harness once without elevated permissions: `claude -p --plugin-dir /home/user/claude-skills/manifesto --output-format json 'reply with the single word ok'` from /home/user/claude-skills, with any debug or verbose flag the CLI offers for hook output, and record what hook text, if any, appears. If the run is refused or hangs past 120 seconds, record that and move on; never retry with bypassPermissions.
5. Write the verdict per claim: VERIFIED, CONTRADICTED, or UNVERIFIED, each with the quoted evidence lines.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/resolutions/runtime-defects-verification.md

REPORT FORMAT:
# Runtime Defects — Independent Verification
(three binding lines)
## Claim A — verdict, then evidence: stdout character count, cap source quote with file and offset, what the truncated text ends with
## Claim B — verdict, then evidence: the JSON emitted, the validator result, the schema quote with file and offset
## Harness run — command, exit code, what appeared
## Method — every command run, in order

SCOPE: Verify these two claims only. Do not modify any file under /home/user/claude-skills; delete any __pycache__ you create. No recommendations.

TOOLS: Bash for running scripts, grep over the CLI bundle, python validation; Read for the hook files; Write for the report.

End with a 3-sentence summary for a notification: the two verdicts and the single strongest evidence line.
