# Unharness verification

Date: 2026-10-23, re-verified 02:45 EEST on the fixed build at commit f821dd8. Claude Code 2.1.309, login `~/.claudes/meta`, models `claude-haiku-5-5` and `claude-opus-5-5`. Each result comes from a captured request body, the first request of one run. The capture files stay ignored, so this report quotes what a reader needs.

## What each capture ran

All runs used a clean environment: `env -i` with `HOME USER LOGNAME PATH SHELL TERM TMPDIR LANG`, plus `CLAUDE_CONFIG_DIR=~/.claudes/meta`, `CLAUDE_CODE_ENABLE_TELEMETRY=1`, and `OTEL_LOG_RAW_API_BODIES=file:<dir>`. The project was a git folder holding a CLAUDE.md with the line `Marker: PAPAYA-7`, one commit, and a config of three elements with hand-written session files.

The tool's launch command prints the strip below, and the tool-run captures used it:

```
env CLAUDE_CODE_ATTRIBUTION_HEADER=0 CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1 CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 CLAUDE_CODE_SILENT_TURN_REMINDER=0 UNHARNESS=1 claude --system-prompt-file <cache file> --disallowedTools WebSearch --settings '{"includeGitInstructions":false,"attribution":{"commit":"","pr":""},"autoMemoryEnabled":false,"outputStyle":"default"}'
```

| Capture | Run |
|---|---|
| `d1-p-haiku`, `d1-p-opus` | `unharness launch "$PROMPT" -- claude -p "Reply OK." --model <m> --max-turns 1 </dev/null` |
| `d1-flag-keepmd`, `d1-flag-nohooks`, `d1-flag-websearch` | as `d1-p-haiku`, plus `--keep-claude-md`, `--no-hooks`, or `--keep-web-search` before the prompt |
| `d1-tmux-haiku` | the same launch in tmux, `-- claude --model haiku`, prompt as argument, one message `Reply OK.`, then `/exit` |
| `d5-tmux-haiku` | the documented pipe in tmux, run from the worktree: `unharness prompt \| unharness launch -- claude --model haiku --plugin-dir <plugin>`, both stages through the launcher `plugin/bin/unharness` with `UNHARNESS_FROM` set to the tool folder, then `Reply OK.` and `/exit` |
| `d5-p-haiku` | `unharness launch "$(unharness prompt)" -- claude -p "Reply OK." --model haiku --max-turns 1 </dev/null`, from the worktree, no `--plugin-dir` |
| `d1-ctl-p-haiku` | control: plain `claude -p "Reply OK." --model haiku --max-turns 1`, no tool, no strip |
| `b2-full-haiku`, `b2-full-opus` | `claude -p` with the strip by hand and `CUSTOM-PROMPT-MARKER` as the prompt file |
| `a3-c5` | interactive haiku with the strip by hand, `--system-prompt-file` of the marker, no `--disallowedTools` |

## Result per injected text

Results: absent, present, or set but unshown, which means the switch ran and no capture can show its effect.

| Injected text | Switch | Result | Capture |
|---|---|---|---|
| Default system prompt | `--system-prompt-file` | absent; the control has it | `d1-p-haiku`, `d1-tmux-haiku`, `d1-ctl-p-haiku` |
| Billing header block | `CLAUDE_CODE_ATTRIBUTION_HEADER=0` | absent; the control has it | `d1-p-haiku`, `d1-ctl-p-haiku` |
| CLAUDE.md | `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1` | absent; `--keep-claude-md` restores it | `d1-p-haiku`, `d1-flag-keepmd` |
| Git status and Bash commit text | `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1`, `includeGitInstructions: false` | absent; the control has both | `d1-p-haiku`, `d1-ctl-p-haiku` |
| Co-Authored-By and PR footer | `attribution: {commit: "", pr: ""}` | set but unshown | the login already sets it empty |
| Auto memory section | `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, `autoMemoryEnabled: false` | set but unshown | the login already sets it off |
| Output style text | `outputStyle: "default"` | set but unshown | the login sets no style |
| WebSearch paragraph | `--disallowedTools WebSearch` | absent; `--keep-web-search` restores it | `b2-full-haiku`, `d1-flag-websearch` |
| Silent-turn note | `CLAUDE_CODE_SILENT_TURN_REMINDER=0` | set but unshown | one request per run |
| Hook output | none; `--no-hooks` sets `disableAllHooks`; the worktree's session-start hook stands down under `UNHARNESS=1` | present; absent under `--no-hooks`; the worktree's binding paragraph absent | `d1-p-haiku`, `d1-flag-nohooks`, `d5-tmux-haiku` |
| Tool list | none | present, 13 tools, 15 interactive | `d1-p-haiku`, `d1-tmux-haiku` |
| Skill list | none | present, 101 entries | `d1-p-haiku`, `d1-tmux-haiku` |
| Agent list | none | present, 14 entries, 15 interactive | `d1-p-haiku`, `d1-tmux-haiku` |
| Environment block | none | present | `d1-p-haiku`, `b2-full-haiku` |
| Identity line | none | present | `d1-p-haiku`, `d1-tmux-haiku` |
| Context wrapper and email line | none | present | `d1-p-haiku`, `a3-c5` |
| Date line | none | present | `d1-p-haiku`, `b2-full-haiku` |
| Task-list nudges, file-changed notes | none applied; `CLAUDE_CODE_DISABLE_ATTACHMENTS=1` also drops the skill list | set but unshown; no capture holds either | `b2-a-attachments` |
| Agent tool worktree sentence | none found | present | `d1-p-haiku`, `b2-full-haiku` |
| MCP server instructions | none | present when a server is configured | `d1-tmux-haiku`, `a3-c5` |

## Residue

Each segment below survived the full strip. Positions come from `d1-p-haiku`. A line number counts lines inside `messages[1][0]`, a block with role `system`. Quotes stop at 200 characters, and the owner's email and home paths are removed.

| Segment | Location | Quote |
|---|---|---|
| Identity line | `system[0]` | `You are a Claude agent, built on Anthropic's Claude Agent SDK.` Interactive runs read `You are Claude Code, Anthropic's official CLI for Claude.` |
| Context wrapper and email line | `messages[0][0]` | `<system-reminder>\nAs you answer the user's questions, you can use the following context:\n# userEmail\nThe user's email address is <email>. Use it only to identify the user, such as for authorship, attribution, or filtering` |
| Memento hook | lines 1 to 4 | `SessionStart:startup hook success: Run memento:init now — it resolves the entry chain (pat-down, span-closure) and executes the\nwaking check.` |
| Peer hook | line 6 | `SessionStart:startup hook success: The peer society on this machine lives at ~/.local/share/agents-of-anarchy: as a main session, load the skill peers:join and join it.` |
| Manifesto hook | lines 8 to 49 | `SessionStart:startup hook success: <persisted-output>\nOutput too large (10.6KB). Full output saved to: ...\n\nPreview (first 2KB):\nMANDATORY CONSTITUTION INITIALIZATION — Execute this before any other work.` |
| Per-prompt hook | line 333 | `UserPromptSubmit hook success: Active bindings: dry: "knowledge has one home" · lines-spent: "spent, not produced. yours, not theirs." · write-well` |
| Environment block | lines 51 to 60 | `# Environment\nYou have been invoked in the following environment: \n - Primary working directory: /private/tmp/uh-d1\n - Is a git repository: true\n - Additional working directories:\n  - ~/competera/...` |
| Model line | line 62 | `You are powered by the model named Haiku 5.5. The exact model ID is claude-haiku-5-5. Assistant knowledge cutoff is June 2026.` |
| Deferred-tool list | lines 64 to 78 | `The following deferred tools are now available via ToolSearch. Their schemas are NOT loaded — calling them directly will fail with InputValidationError. Use ToolSearch with query "select:<name>[,<name>...` |
| Agent list | lines 80 to 223 | `Available agent types for the Agent tool:\n- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)` |
| Skill list | lines 225 to 329 | `The following skills are available for use with the Skill tool:` then 101 entries |
| Token and date lines | lines 331 and 335 | `<total_tokens>15000000 tokens left</total_tokens>` and `Today's date is 2026-10-23.` |
| Agent description | `tools[Agent]` | `- \`isolation: "worktree"\` gives the agent its own git worktree (auto-cleaned if unchanged).` |
| Bash description | `tools[Bash]`, haiku only | `- IMPORTANT: Avoid using this tool to run \`cat\`, \`head\`, \`tail\`, \`sed\`, \`awk\`, or \`echo\` commands, unless explicitly instructed or after you have verified that a dedicated tool cannot accomplish your task.` |
| Request parameters | top level | `betas` of 19 flags, `thinking`, `context_management`, `output_config`, `thread`, `diagnostics`, and a `safeguards` field with permission and git state; none is prompt text |
| Auto mode paragraph | line 331, opus only | `While auto mode is active:\n\nYou can do much of your work through the Bash tool when it is the simpler route: read files with cat, head, or sed -n, search with grep and find, and make small, mechanical file` |
| MCP instructions | lines 312 to 317, interactive only | `# MCP Server Instructions\n\nThe following MCP servers have provided instructions for how to use their tools and resources:\n\n## claude.ai Claude Docs` |
| Added tools | interactive only | `AskUserQuestion` and `ReadNotifications` in `tools`, and three `tool_addition` blocks in `messages[1]` |

## Flag checks

Each run changed one flag from `d1-p-haiku`.

- **`--keep-claude-md`** restores CLAUDE.md. `messages[0]` gains a block that opens `Codebase and user instructions are shown below.` and holds `Contents of /private/tmp/uh-d1/CLAUDE.md (project instructions, checked into the codebase):\n\nMarker: PAPAYA-7`. The control carries identical text.
- **`--no-hooks`** removes every hook paragraph. `d1-p-haiku` has four hook lines and `d1-flag-nohooks` has none. The block with role `system` opens with `# Environment`. The email wrapper and the tool, skill, and agent lists remain.
- **`--keep-web-search`** restores the paragraph. `system[1]` becomes the prompt plus a blank line and a paragraph that opens `WebSearch takes a \`mode\`. Use "standard" by default: it is the normal search, quick and cheap.` The deferred list regains `WebSearch`, and a `safeguards` rule for `WebSearch` disappears.
- **The prompt block** equals the compiled prompt by sha256 in every capture except the `--keep-web-search` one. The identity line comes first.

## Re-verification

The first build crashed the interactive client when the prompt arrived by pipe. It reopened the terminal as `/dev/tty`, and Claude Code 2.1.309 fails with `EINVAL: invalid argument, kqueue` on that path. The fixed `launch` reopens the device of stdout or stderr. Results on the fixed build:

- **The documented pipe starts and answers.** In `d5-tmux-haiku` the session started, with no crash, and `Reply OK.` drew a reply that opens `OK.` The model then said it had loaded the `peers:join` skill because the peer hook told it to. The capture holds two requests, both from the main thread.
- **The prompt lands verbatim.** In both requests `system[1]` equals the output of `unharness prompt` byte for byte, trailing newline included, after the identity line `You are Claude Code, Anthropic's official CLI for Claude.` In `d5-p-haiku` it equals the same output with the newline stripped, as `$(...)` strips it.
- **The worktree's hook stands down.** `d5-tmux-haiku` has no `MANDATORY CONSTITUTION INITIALIZATION` paragraph. Run by hand under `UNHARNESS=1`, the released 3.4.0 session-start hook prints 11863 bytes of it and the worktree's prints none. `d5-p-haiku`, run without `--plugin-dir`, carries the released hook's paragraph, so the released hook stays active when the worktree plugin is not loaded.
- **The memento hook is absent for another reason.** Its script exits when the project folder holds no CLAUDE.md, and the worktree holds none. The peer hook and the per-prompt hook remain in `d5-tmux-haiku`, as the spec expects.
- **The strip holds.** Neither capture has CLAUDE.md text, git status, the billing header, or the WebSearch paragraph, and in the interactive capture `WebSearch` is out of the tool and deferred lists. The tool, skill, agent, and environment lists remain, and so do the MCP instructions in the interactive capture.
- **The printed redirect follows the terminal.** `unharness launch "x"` under `script -q /dev/null` ends `</dev/ttys002`. With stdout and stderr piped it ends `</dev/tty`. With only stderr on a terminal it ends `</dev/ttys002`.
- **The launcher builds fresh.** `plugin/bin/unharness` passes `--no-cache` and `--with-editable` for a folder source, so a local build is never stale. Both captures ran through it.

## Not verified

- **Auto memory, attribution, output style.** The login already turns the first two off and sets no style, so the control lacks the text too. These three switches have no shown effect.
- **Silent-turn note and task-list nudges.** Each capture holds one request, and no capture holds a nudge or a file-changed note.
- **Which git switch does what.** The environment variable and the setting ran together here. A3's captures separated them.
- **Sample size.** Each capture ran once, and only haiku ran interactively.
- **The terminal reopen outside tmux.** The piped form ran in tmux only, not in the owner's usual terminal.
- **Opus on the fixed build.** Opus ran only on the first build.
