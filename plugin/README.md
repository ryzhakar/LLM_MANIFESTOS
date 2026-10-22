# manifesto

Create concentrated manifesto declarations and bind Claude behavior to user-provided manifestos through identity-assumption protocols.

`manifesto` `behavioral-binding` `identity` `writing` 
## Skills

### [compile-commitments](skills/compile-commitments/SKILL.md)

Write the interplay file and the commitments file that a session's system prompt carries, from the stack the session binds to. Use it as `/compile-commitments`, or after any change to the stack.


---

### [manifesto-oath](skills/manifesto-oath/SKILL.md)

Binds Claude's operating identity to constitutions, manifestos, and principle sets through identity construction — not theatrical oaths. Triggers on oath/binding requests or when hooks inject constitution elements at session boundaries.


---

### [manifesto-writing](skills/manifesto-writing/SKILL.md)

Trigger when users request manifestos or manifesto tone. Name the enemy, strip hedging, compress to sharp distinctions, end with stark choice.


---

## Agents

### [maximalist-reviewer](agents/maximalist-reviewer.md)

Review a set of files against one manifesto at the manifesto's strongest literal reading, with no allowance for cost, convention, or proportion, and write a report file listing every violation with a compliant rewrite. Use it for an ad-hoc review against a chosen manifesto, outside any mandatory review loop. Examples:

<example>
Context: The user wants a module held to the DRY manifesto without exceptions.
user: "Review src/billing against the dry manifesto, maximally"
assistant: "I'll launch the maximalist-reviewer agent with the dry manifesto and the billing paths."
</example>

<example>
Context: A diff should be checked against a writing standard at full strictness.
user: "Hold this diff to Strunk, no mercy"
assistant: "I'll launch the maximalist-reviewer agent with the Strunk source and the diff range."
</example>


**Model:** `inherit` · **Tools:** Read, Write, Grep, Glob, Bash

---

## Unharness

The system prompt carries the stack, its interplay, and its commitments; since the prompt is not part of the conversation, compaction cannot erase the binding, and one captured compaction left the prompt unchanged. Launch switches off the instructions Claude Code adds around it, and `unharness` compiles the prompt and launches Claude Code with it.

Beside `.manifestos.yaml`, whose schema is in [SCHEMA.md](SCHEMA.md), a project keeps three files:

- `.manifestos.interplay.md` and `.manifestos.commitments.md`, written by `/compile-commitments`, each opening with a `<stack>` block that lists every element with its sha256.
- `.manifestos.preamble.md`, optional, which replaces the preamble that tells the model what each text the application adds is, and how to weigh it.

```
/compile-commitments
uvx unharness prompt | uvx unharness launch -- claude
```

The launcher's input is reopened on the terminal, so the session reads the keyboard after the pipe. Any launcher goes after `--`; a name that is not a program on PATH, such as the zsh function `claude@meta`, runs through `$SHELL -ic`. With nothing after `--`, `launch` prints the command it would run and runs nothing.

- `unharness prompt [--config PATH]` prints the compiled prompt; it stops when the interplay or commitments file is missing or its `<stack>` block differs from the current stack.
- `unharness stack [--config PATH]` prints the `<stack>` block and the constitution, exactly what a session binds to.
- `unharness launch [--keep-claude-md] [--keep-web-search] [--no-hooks] [PROMPT] [-- LAUNCHER [ARGS...]]` caches the prompt in `$XDG_CACHE_HOME/unharness/<sha256>.md`, or `~/.cache/unharness/` when unset, and runs the launcher with the switches below. The printed command ends in the terminal's own device, and in `/dev/tty` only when neither output is a terminal.

`/compile-commitments` reads `unharness stack`, reduces each element to its axioms, and writes the interplay and commitments files.
Run it once after each change to the stack; `unharness prompt` stops until the files match.

| Injected text | Switch | Default |
|---|---|---|
| Default system prompt | `--system-prompt-file` the cached prompt | replaced |
| Billing header block | env `CLAUDE_CODE_ATTRIBUTION_HEADER=0` | stripped |
| Every CLAUDE.md | env `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1` | stripped; `--keep-claude-md` keeps |
| Git status snapshot; commit and PR text in the Bash tool description | env `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1`, setting `includeGitInstructions: false` | stripped |
| Co-Authored-By trailer and PR footer | setting `attribution: {commit: "", pr: ""}` | set |
| Auto memory section | env `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, setting `autoMemoryEnabled: false` | set |
| Output style text | setting `outputStyle: "default"` | set |
| "The user hasn't heard from you in a while" note | env `CLAUDE_CODE_SILENT_TURN_REMINDER=0` | set |
| WebSearch paragraph | `--disallowedTools WebSearch` | stripped; `--keep-web-search` keeps it |
| Hook output | setting `disableAllHooks: true` under `--no-hooks` | kept |

The four rows marked "set" are implemented per the Claude Code docs and the binary; no capture shows their text present or removed. Launch also sets `UNHARNESS=1`, so this plugin's session-start and post-compact hooks stand down because the compiled prompt already carries their binding; their tests cover this, and no capture shows it.

**What stays.** The harness adds each item below, and either no switch removes it or the only switch drops something kept on purpose. The evidence is in `orchestration_log/history/2026-10-23/verification-unharness.md`, with the captures d1-p-haiku and d1-p-opus (print mode), d1-tmux-haiku (interactive sessions), d1-flag-keepmd, d1-flag-nohooks, d1-flag-websearch, b2-full-haiku, and a3-c5.

- The identity line: `You are Claude Code, Anthropic's official CLI for Claude.` in interactive sessions, `You are a Claude agent, built on Anthropic's Claude Agent SDK.` in print mode.
- The context wrapper around the email line, in a user message; the date line sits outside it.
- Task-list nudges and file-changed notes: their one switch, `CLAUDE_CODE_DISABLE_ATTACHMENTS`, also drops the skill list.
- The Agent tool's worktree sentence and the other tool descriptions.
- MCP server instructions when MCP servers are configured.
- The tool, skill, and agent lists and the environment block, kept on purpose.

Run it from git until the package is published, then from the package:

```
uvx --from "git+https://github.com/ryzhakar/llm-manifestos@v3.5.0#subdirectory=plugin/unharness" unharness
uvx unharness
```

Inside a session, `bin/unharness` runs the copy bundled with the plugin; `UNHARNESS_FROM`, a path or a git URL, runs another source.

## Install

```
/plugin marketplace add ryzhakar/llm-manifestos
/plugin install manifesto@llm-manifestos
```

## Tests

Run from the repository root:

```
python3 -I plugin/tests/test_hooks.py
uv run --project plugin/unharness pytest -q
```
