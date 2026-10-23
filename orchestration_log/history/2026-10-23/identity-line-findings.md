# X1: identity line and reminder switches

Date: 2026-10-23. Claude Code 2.1.309, the binary at `~/.local/share/claude/versions/2.1.309`, login `~/.claudes/meta`, model `claude-haiku-5-5`, print mode only. Every capture ran under `env -i` with the unharness strip, a one-line prompt file holding `X1-PROMPT-MARKER: you are a test responder.`, and `disableAllHooks: true` added to the strip's settings so that no hook steered the multi-turn runs. Each capture changed one switch from that base. The capture folders sit in `orchestration_log/recon/2026-10-23/captures-x1/`, named below without that prefix. The capture script and analyzers stayed in `/tmp/x1run/`.

Verdict: the identity block cannot be removed, and every other piece can. The client always adds the identity block, and the API refuses a request whose system array lacks it. The billing block, the silent-turn note, the task nudge, and the token-count line each have a switch that a capture confirms. The no-visible-output nudge has no switch, but it fires only after a reply that holds thinking and no text.

## Pieces

### Identity block

| Field | Finding |
|---|---|
| Exact text | Print mode: `You are a Claude agent, built on Anthropic's Claude Agent SDK.` (sha256 `0d7062851dd7bd7e66d4be4f12ac4951e3d2f587ec408295333a49963bd3f6b7`). Interactive: `You are Claude Code, Anthropic's official CLI for Claude.` (sha256 `2719b7a469d904b3281d8488976f33103944211279bddf04c05bca44d184dae6`). Print mode with a non-empty `--append-system-prompt`: `You are Claude Code, Anthropic's official CLI for Claude, running within the Claude Agent SDK.` |
| Where it lands | `system[0]` under `CLAUDE_CODE_ATTRIBUTION_HEADER=0`; `system[1]` when the billing block is present |
| Documented switch | None. The docs quote none of the three texts. The nearest sentence names a reason to write a custom prompt, "Different identity: the agent shouldn't present itself as Claude Code." (https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts) |
| Capture | Every capture carries the block with the same sha, including `x1-base`, `x1-ablate`, `x1-disable-attach`, and `x1-tokens-off`. `x1-ablate` set `CLAUDE_CODE_REMOVE_PROMPT_STRINGS` to a list holding the print-mode text; the block stayed, and the variable's other string vanished from the Agent tool's description. |
| Binary evidence | The chooser returns a text on every path: `function E6n(e){if(xe()==="vertex")return ie;if(e?.recorded!==void 0)return e.recorded;if(e?.isNonInteractive){if(e.hasAppendSystemPrompt)return Ue;return Pe}return ie}`. The main loop always passes its result: `YNe=E6n({isNonInteractive:Q.isNonInteractiveSession,hasAppendSystemPrompt:Q.hasAppendSystemPrompt,recorded:Q.recordedCliPrefix})` and then `n=rNs(n,YNe,{...})`, where `rNs` builds `[s,n,...e].filter(Boolean)`. A recorded prefix from a resumed session passes only if it is one of the three texts: `cliPrefix:s.cliPrefix!==void 0&&w6n(s.cliPrefix)?s.cliPrefix:void 0`, with `w6n` testing membership in the set of three. Only side calls skip the block, through `skipSystemPromptPrefix`. The ablation variable cannot reach the block, since it edits tool descriptions and default prompt sections before `rNs` adds the identity. |
| Server check | `x1-extra-body-system` and `x1-extra-body-system2` used `CLAUDE_CODE_EXTRA_BODY` to send a system array holding only the marker, with `CLAUDE_CODE_MAX_RETRIES=0`. Both failed with `API Error: Server is temporarily limiting requests (not your usage limit)`. `x1-extra-body-control`, run between them with the print-mode identity block first and the same marker second, answered `ok`. I made no further attempt past that check. |

### Billing block

| Field | Finding |
|---|---|
| Exact text | `x-anthropic-billing-header: cc_version=2.1.309.<suffix>; cc_entrypoint=sdk-cli; cch=00000; ...`, followed by per-conversation fields |
| Where it lands | `system[0]`, ahead of the identity block |
| Documented switch | `CLAUDE_CODE_ATTRIBUTION_HEADER=0`, https://code.claude.com/docs/en/llm-gateway-protocol#system-prompt-attribution-block: "If your gateway must reshape system content, set `CLAUDE_CODE_ATTRIBUTION_HEADER=0` so Claude Code omits the block." |
| Capture | Works. `x1-ctl-billing` has three system blocks with the billing block first; `x1-base` has two, and its `system[0]` is the identity block. |
| Note | The same page says "The `api.anthropic.com` endpoint strips the block before processing when it arrives unchanged as the first system block". On this login the model never read the block, so the switch changes the wire and not the model's context. The variable's name says "attribution", but the code gates the billing block alone: `function R(){return cs(process.env.CLAUDE_CODE_ATTRIBUTION_HEADER)}`, and the builder returns `""` when `R()` holds. |

### Project instructions (CLAUDE.md)

| Field | Finding |
|---|---|
| Exact text | Opens `Codebase and user instructions are shown below.` and then the file contents |
| Where it lands | `messages[0]`, role `user`, inside `<system-reminder>` |
| Documented switch | `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1`, https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts: "Every CLAUDE.md file | Set `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1`" |
| Capture | Works. In a folder whose CLAUDE.md holds `Marker: X1-MD-MARKER`, `x1-md-on` carries the marker in `messages[0]` and `x1-md-off` does not. |

### Output style instructions

| Field | Finding |
|---|---|
| Exact text | Opens `# Output Style: <name>` and then the style body |
| Where it lands | `messages[1]`, role `system` |
| Documented switch | `outputStyle: "default"`, https://code.claude.com/docs/en/output-styles: "Default means no output style is selected. Claude Code adds no style instructions" |
| Capture | Works. `x1-style-on`, with `outputStyle: "Explanatory"`, carries `# Output Style: Explanatory` in `messages[1]`; `x1-base2`, with `"default"`, carries none. |

### Commit and pull request attribution

| Field | Finding |
|---|---|
| Exact text | Opens `Attribution for git commits and pull requests you create from here on` and lists `- End git commit messages with:` and `- End pull request descriptions with:`, each followed by the configured text |
| Where it lands | `messages[0]`, role `user`, inside `<system-reminder>`. The Bash tool's description adds `End git commit messages and PR bodies with the attribution lines given in the conversation's system-reminder, when one is present.` while git instructions are on. |
| Documented switch | `attribution.commit` and `attribution.pr` set to `""`, https://code.claude.com/docs/en/settings-reference#attribution: "Set it to an empty string to hide commit attribution." |
| Capture | Works. With git instructions on, `x1-attr-on2` carries both markers in `messages[0]`, and `x1-attr-empty2`, with empty strings, carries neither. The Bash sentence stays in both and leaves only under `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1`, as in `x1-base`. |

### Hook output

| Field | Finding |
|---|---|
| Exact text | Each hook's text, opened by its event name, such as `SessionStart:startup hook success:` |
| Where it lands | `messages[1]`, role `system` |
| Documented switch | `disableAllHooks: true`, https://code.claude.com/docs/en/hooks-guide: "To disable hooks, set `"disableAllHooks": true` in your settings file." |
| Capture | Every X1 capture ran with the switch and holds no hook text. I took no X1 control with hooks on; `d1-p-haiku` and `d1-flag-nohooks` in `captures/` show the difference. |

### Available skills

| Field | Finding |
|---|---|
| Exact text | `The following skills are available for use with the Skill tool:` and one entry per skill |
| Where it lands | `messages[1]`, role `system` |
| Documented switch | `CLAUDE_CODE_DISABLE_ATTACHMENTS=1`, https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts: "Task list nudges, file-changed notes, and the skill list | Set `CLAUDE_CODE_DISABLE_ATTACHMENTS=1`" |
| Capture | Works, and reaches further than the docs say. `x1-disable-attach` lacks the skill list, the deferred-tool list, the token-count line, and the `advisor` tool, and it keeps the agent list, the environment block, the model line, and the date line. |

### Available subagents

| Field | Finding |
|---|---|
| Exact text | `Available agent types for the Agent tool:` and one entry per agent |
| Where it lands | `messages[1]`, role `system` |
| Documented switch | None that keeps the Agent tool. The docs state: "The list of available subagents and background task notifications still arrive." (https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts) |
| Capture | `x1-disable-attach` still carries the list. |
| Binary evidence | Under the attachments switch the collector returns only `[...Rt,...await kEe(n,H),...lon(n.options.tools,h),...await oTo(n,h)]`, behind `if(EQe(n))`, and the agent list survives through that path. |

### Task list nudges

| Field | Finding |
|---|---|
| Exact text | `The task tools haven't been used recently. If you're working on tasks that would benefit from tracking progress, consider using TaskCreate to add new tasks and TaskUpdate to update task status (set to in_progress when starting, completed when done). Also consider cleaning up the task list if it has become stale. Only use these if relevant to the current work. This is just a gentle reminder - ignore if not applicable.` The `TodoWrite` form opens `The TodoWrite tool hasn't been used recently.` |
| Where it lands | A new message with role `system`, in the request after the tenth tool turn that skipped the task tools |
| Documented switch | `CLAUDE_CODE_DISABLE_ATTACHMENTS=1`, quoted under the skill list, which also drops the skill list. The docs add a precondition at https://code.claude.com/docs/en/tools-reference#task-tool-availability: "The task-tracking tools ... are available by default only on Opus 4.7, Sonnet 4.6, Haiku 4.5, and earlier models." |
| Undocumented switch | `CLAUDE_CODE_TODO_REMINDER_MODE=off`. The binary reads it in `function Axn(){let e=i.CLAUDE_CODE_TODO_REMINDER_MODE;if(e!==void 0)return e;return k("tengu_soft_slate_nudge","baseline")==="off"?"off":"baseline"}`, and both nudge builders return `[]` when `Axn()==="off"`. |
| Capture | Works. All four multi-turn captures set `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` and asked for thirteen silent `echo step` calls. `x1-mt-both` and `x1-mt-taskonly` carry the nudge once; `x1-mt-silentonly` and `x1-mt-neither`, both with `CLAUDE_CODE_TODO_REMINDER_MODE=off`, carry none. Without the opt-in, `x1-base` and `x1-teams` list no `TaskCreate`, even under `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, so the nudge cannot fire there. |

### File-changed notes

| Field | Finding |
|---|---|
| Exact text | Opens `Note: <file> changed on disk since you last read it`, per the a2 report; no X1 capture holds one |
| Where it lands | A reminder message after the change |
| Documented switch | `CLAUDE_CODE_DISABLE_ATTACHMENTS=1`, quoted under the skill list |
| Capture | Not taken. The `changed_files` generator sits in the branch that `EQe` skips: `function EQe(e){return Boolean(i.CLAUDE_CODE_DISABLE_ATTACHMENTS||i.CLAUDE_CODE_SIMPLE||e.options.bareFork)}`. |

### Silent-turn note

| Field | Finding |
|---|---|
| Exact text | On the wire: `The user hasn't heard from you in a while — say in a few words what you're doing, then continue.` The binary default differs, `The user hasn't heard from you in a while. As you continue, keep them updated when there's something to tell — a finding, a change of plan.`, and a server flag replaces it: `k("tengu_hushed_lark_text",KCn)`. |
| Where it lands | A new message with role `system`, after the fifth silent tool turn, then again after six more |
| Documented switch | None. The docs never mention the note. |
| Undocumented switch | `CLAUDE_CODE_SILENT_TURN_REMINDER=0`. The variable is a three-state boolean (`on=H.triBool()`, where `0` parses to false), and the gate returns it before any default: `function KN(e,n,r,l){if(l!==void 0)return l;...}`, called as `KN("silent_turn_reminder",n,e,i.CLAUDE_CODE_SILENT_TURN_REMINDER)`. |
| Capture | Works. `x1-mt-both` and `x1-mt-silentonly`, run with `1`, carry the note twice each. `x1-mt-taskonly` and `x1-mt-neither`, run with `0`, carry none. |

### No-visible-output nudge

| Field | Finding |
|---|---|
| Exact text | `[Your previous response had no visible output. Please continue and produce a user-visible response.]` A sibling fires at the output limit: `[Your previous response reached the output limit with no visible output. Please continue and produce a brief user-visible response or tool call right away.]` |
| Where it lands | A meta message with role `user` that the loop appends before it retries; no X1 capture holds one |
| Documented switch | None. The 2.1 changelog records its origin: "Fixed turns silently completing with no visible output when the model returned only a thinking block; Claude now re-prompts once". |
| Binary evidence | The query loop fires it on an `end_turn` or `stop_sequence` reply whose blocks hold no non-blank text, outside compaction, once per turn: `if((be==="end_turn"||be==="stop_sequence")&&!C?.isApiErrorMessage&&T!=="compact"&&!wWe(T)&&!PRr(j)&&!oe.some((ge)=>ge.message.content.some((ee)=>ee.type==="text"&&ee.text.trim().length>0))&&!Z(j)){if(!li){...Oe({content:rSn,isMeta:!0,...})`. No term in the condition reads the environment or the settings. |

### Token-count line

| Field | Finding |
|---|---|
| Exact text | `<total_tokens>15000000 tokens left</total_tokens>`, counting down |
| Where it lands | The end of `messages[1]` and of every later reminder message |
| Documented switch | None in the public docs. The binary's settings schema marks the key `@internal`: `totalTokensReminder:()=>B(["off","infinite","fixed","countdown","padded-countdown"])`. |
| Undocumented switch | `CLAUDE_CODE_TOTAL_TOKENS_REMINDER=off`, or the settings key `totalTokensReminder: "off"`. The builder returns nothing when the mode is off: `function RUr(e,n,r,s,h,y,b){let w=$Z(r,y);if(w==="off")return[];...`. |
| Capture | Works. `x1-tokens-off` lacks the line, and `x1-base` has it. |

## Earlier records corrected

- **verification-unharness.md, results table, "Silent-turn note".** The row reads `set but unshown`. The switch now shows its effect: with `CLAUDE_CODE_SILENT_TURN_REMINDER=0` the note is absent from a thirteen-turn run, and with `1` it appears twice.
- **verification-unharness.md, results table, "Task-list nudges, file-changed notes".** The row reads `none applied; CLAUDE_CODE_DISABLE_ATTACHMENTS=1 also drops the skill list`. A narrower switch exists for the task nudge: `CLAUDE_CODE_TODO_REMINDER_MODE=off` removes it and leaves the skill list. The nudge also needs the task tools, which Haiku 5.5 and Opus 5.5 lack by default.
- **verification-unharness.md, residue table, "Token and date lines".** The row lists the token line among text that survived with no switch. `CLAUDE_CODE_TOTAL_TOKENS_REMINDER=off` removes it. The date line still has no known switch.
- **verification-unharness.md, results table, "Billing header block".** The row reads `absent; the control has it`, which holds for the wire. The gateway page says the first-party endpoint strips the block before processing, so the model never read it, with or without the switch.
- **a2-binary-switches.md, "Silent turn" row.** The row quotes the binary default text. On this login a server flag replaces it, and the wire carries `The user hasn't heard from you in a while — say in a few words what you're doing, then continue.`
- **a2-binary-switches.md, "Reminders", master gate.** The report says that under `CLAUDE_CODE_DISABLE_ATTACHMENTS` alone "the agent list, sandbox instructions, and an untraced helper `oTo` also survive". The capture shows more. The switch also drops the deferred-tool list, the token-count line, and the `advisor` tool, and it keeps the environment block, the model line, and the date line.
- **a2-binary-switches.md, "Task nudge" row.** The row offers `CLAUDE_CODE_DISABLE_ATTACHMENTS`, SIMPLE, and `CLAUDE_CODE_ENABLE_TASKS=false`, and it misses `CLAUDE_CODE_TODO_REMINDER_MODE`, which both nudge builders read.
- **a1-docs-switches.md, line 306.** The line calls the claim that no switch removes the identity line "unconfirmed". The binary confirms it: the chooser returns a text on every path, and the assembler always receives it.
- **b2-switch-tests.md, line 86.** The line infers that "either the client or the server" requires the identity block. The requests without it reached the API and failed there with `Server is temporarily limiting requests (not your usage limit)`, while the same body with the block first succeeded between the two failures, so the server enforces it.

## What unharness should change

- **Add `CLAUDE_CODE_TODO_REMINDER_MODE=off`** to the launch environment. It removes the task-list and TodoWrite nudges and leaves the skill list. The docs do not name the variable, so a release may drop it.
- **Add `CLAUDE_CODE_TOTAL_TOKENS_REMINDER=off`** to the launch environment, or `"totalTokensReminder":"off"` to the `--settings` JSON. It removes the token-count line. The binary marks the settings key `@internal`.
- **Keep `CLAUDE_CODE_SILENT_TURN_REMINDER=0`.** The capture confirms it works.
- **Keep `CLAUDE_CODE_ATTRIBUTION_HEADER=0`**, knowing that it changes the wire and not what the model reads on the first-party endpoint.
- **Do not add `CLAUDE_CODE_DISABLE_ATTACHMENTS=1`.** It drops the skill list, the deferred-tool list, and the `advisor` tool along with the nudges.
- **Leave the identity block alone.** No flag, setting, or variable removes it, and the API rejects a request without it. Do not route around it with `CLAUDE_CODE_EXTRA_BODY`.
- **Accept the no-visible-output nudge.** No switch exists, and it fires only after a reply with no text.
- **Optional:** `CLAUDE_CODE_REMOVE_PROMPT_STRINGS='["<exact sentence>", ...]'` deletes exact strings from built-in tool descriptions and default prompt sections. In `x1-ablate` it removed ` (auto-cleaned if unchanged)` from the Agent tool. It cannot touch the identity block, and the docs do not name it.

The launch line would then read:

```
env CLAUDE_CODE_ATTRIBUTION_HEADER=0 CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1 CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 CLAUDE_CODE_SILENT_TURN_REMINDER=0 CLAUDE_CODE_TODO_REMINDER_MODE=off CLAUDE_CODE_TOTAL_TOKENS_REMINDER=off UNHARNESS=1 claude --system-prompt-file <compiled> --settings '{"includeGitInstructions":false,"attribution":{"commit":"","pr":""},"autoMemoryEnabled":false,"outputStyle":"default"}'
```

## Not verified

- **Interactive runs.** The brief allowed print mode only. The interactive identity text comes from the chooser and from the earlier tmux captures.
- **File-changed notes and the no-visible-output nudge.** No X1 capture triggered either one. Their rows rest on the docs and the binary.
- **Opus.** Every X1 capture used Haiku 5.5.
