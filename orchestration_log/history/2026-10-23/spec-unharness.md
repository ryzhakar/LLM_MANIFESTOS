# Spec: unharness

The one home of the design. The owner's brief is `task-long-run.md`; the owner's answers are in `queue-long-run.md` under "Resolved in a round" (cited below as round N); units and status live in `plan-long-run.md`. Items marked RESEARCH wait on the reports named in the plan.

## Purpose

Take a session's instructional foundation back from the harness. The system prompt carries the manifesto stack, its interplay, and its commitments as one instruction flow; launch switches strip what Claude Code injects, keeping only the tool, skill, and agent registries. Because the binding lives in the system prompt, auto-compaction cannot erase it (round 16).

## Usage

    # once per stack change, inside a session in the project:
    /compile-commitments        # writes .manifestos.interplay.md and .manifestos.commitments.md
    # each launch, in the owner's shell:
    uvx unharness prompt | uvx unharness launch -- claude@meta

## Files in a project (round 15, round 16)

- `.manifestos.yaml`: the stack, its `you:` list read by the plugin's hooks and by unharness alike.
- `.manifestos.interplay.md`, `.manifestos.commitments.md`: written by `/compile-commitments`; each opens with the `<stack>` block that `unharness stack` prints.
- `.manifestos.preamble.md`: optional; replaces the shipped preamble.

## Config schema, evolved (round 15)

Every element resolves by an explicit source type; nothing is guessed.

- A bare string, `- dry`, or a mapping without `source`: the manifesto `name` in the registry (legacy form, kept).
- `source: manifesto <name>`: the registry file whose stem is `<name>`.
- `source: skill <plugin>:<skill>`: that plugin's `skills/<skill>/SKILL.md` at the highest version present in the login's plugin cache, `<login>/plugins/cache/<marketplace>/<plugin>/<version>/`.
- `source: skill <skill>`: the user skill `<login>/skills/<skill>/SKILL.md`.
- `source: file <path>`: a local file, relative to the folder holding the config.
- Each element may carry `name` (the label and tag; for a file it defaults to the stem) and `purpose`; `name` is required except for a file source.
- Any other `source` form (a bare path, a URL, a hint) is refused at load with an error naming the `file` form, in `config.py` alone; `unharness` stops with that message and a hook prints it on stderr and exits 0 (triage decision c).
- The registry is `<manifesto_dir>/manifestos/` when the config sets `manifesto_dir`, else the installed manifesto plugin's `manifestos/` at its highest cached version. The login is `$CLAUDE_CONFIG_DIR`, else `~/.claude`.
- An element that does not resolve exactly stops the compile, naming the element and every path tried.
- One home: unharness and the hooks read the schema through one stdlib-only module, `plugin/unharness/src/unharness/config.py`, which the hooks run with `python3` by path; `plugin/hooks/parse_config.py` and `mini_yaml.py` are deleted once the hooks use it (C3).

## Builders

C1, C2, C3, C5 work in the worktree `/Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness` (branch `feat/unharness`); C4 works in `/Users/ryzhakar/LLM_MANIFESTOS.worktrees/oath` (branch `feat/unharness-oath`), so two agents never commit in one tree. Package: `plugin/unharness/pyproject.toml` with `uv_build`, src layout, console script `unharness`, Python >= 3.11, no runtime dependencies; tests with pytest under `plugin/unharness/tests/`.

## Compiled prompt (round 1)

One flow in the agent's own voice, tags for structure, and no seams: nothing names how the prompt was made, and no label says manifesto, skill, file, source, or compiled.

    <harness>
    {preamble}
    </harness>

    <constitution>
    <{name} governs="{purpose}">
    {text with frontmatter removed and ${CLAUDE_PLUGIN_ROOT} replaced by the resolved plugin folder}
    </{name}>
    ...one per element, in config order...
    </constitution>

    {.manifestos.interplay.md without its <stack> block: the session's own <interplay> ... </interplay>}

    {.manifestos.commitments.md without its <stack> block: the session's own <commitments> ... </commitments>}

- `governs` is omitted when the element has no purpose.
- Only listed elements enter the prompt; a document an element refers to stays a reference (solved 14).
- `prompt` stops when either session-written file is missing, or its `<stack>` differs from the current one, naming `/compile-commitments` and each changed element (round 19).
- The `<stack>` block lists one line per element in order: name and the sha256 of its resolved text with its purpose (solved 13).

## Verbs (round 2, round 3, round 20)

- `unharness prompt [--config PATH]`: prints the compiled prompt.
- `unharness stack [--config PATH]`: prints the `<stack>` block and then the `<constitution>`, exactly what a session binds to; `/compile-commitments` uses it (solved 15).
- `unharness launch [--keep-claude-md] [--keep-web-search] [--no-hooks] [PROMPT] [-- LAUNCHER [ARGS...]]`: takes the prompt from PROMPT or stdin, refuses an empty prompt, and stops with a message when no PROMPT is given and stdin is a terminal; writes it to `${XDG_CACHE_HOME:-~/.cache}/unharness/<sha256>.md`; runs `LAUNCHER ARGS...` followed by its own arguments, with its own environment variables set; reopens the launcher's input on the terminal device of stdout, else stderr, and on `/dev/tty` only when neither is a terminal (`claude </dev/tty` crashes 2.1.309, D1); runs a launcher that is not a program on PATH, such as the zsh function `claude@meta`, through `$SHELL -ic`. With no launcher, it prints the command it would run with `claude` as the launcher, one shell-quoted line ending in `</dev/tty`, and runs nothing.

## Strip set (settled 2026-10-23 from A1-A3; B2 and D1 verify by capture)

Environment variables go straight into the launcher's environment; settings keys ride in one `--settings` JSON argument.

| Injected text | Switch | Default |
|---|---|---|
| Default system prompt | `--system-prompt-file <cache file>` | replaced |
| Billing header block | env `CLAUDE_CODE_ATTRIBUTION_HEADER=0` | stripped |
| Every CLAUDE.md | env `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1` | stripped; `--keep-claude-md` keeps |
| Git status snapshot; commit and PR text in the Bash tool description | env `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1` and settings `includeGitInstructions: false` | stripped |
| Co-Authored-By trailer and PR footer | settings `attribution: {commit: "", pr: ""}` | stripped |
| Auto memory section | env `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` and settings `autoMemoryEnabled: false` | stripped |
| Output style text | settings `outputStyle: "default"` | stripped |
| "The user hasn't heard from you in a while" note | env `CLAUDE_CODE_SILENT_TURN_REMINDER=0` (A2; fires only in interactive runs, so D3 verifies) | stripped |
| WebSearch paragraph appended after the custom prompt | `--disallowedTools WebSearch` (B2: the only switch that removes it) | stripped with the tool; `--keep-web-search` keeps both |
| Hook output | hooks stay on (round 17); `--no-hooks` sets settings `disableAllHooks: true` | kept |
| Tool, skill, and agent lists; environment block (cwd, platform, date) | none; the brief keeps the lists, and the facts stay (solved 12) | kept |

Residue, text no switch removes without dropping what we keep (A1 docs silent; A2 binary; A3 captures), each named in the preamble and listed in the README with its capture:

- The identity line: interactive sessions get `You are Claude Code, Anthropic's official CLI for Claude.`; print mode gets `You are a Claude agent, built on Anthropic's Claude Agent SDK.`. The main loop always adds it; only internal side calls skip it. The owner's belief that a documented switch exists (round 5) is not supported: 55 docs pages are silent and the binary's chooser reads no such switch (solved 18).
- The context wrapper (`As you answer the user's questions, you can use the following context:` ... `Claude Code attached this context automatically`) around the email line, and the date line outside it (capture b2-full-haiku); the email line's only gate, `ANTHROPIC_UNIX_SOCKET`, changes the transport.
- Task-list nudges and file-changed notes: their only switch, `CLAUDE_CODE_DISABLE_ATTACHMENTS`, also drops the skill list.
- The Agent tool description's worktree sentence and other tool descriptions.
- MCP server instructions, when MCP servers are configured.

## Manifesto plugin hooks under unharness (round 17, solved 16)

`launch` sets `UNHARNESS=1`. The plugin's session-start and post-compact hooks, which inject the binding ceremony that the compiled prompt already carries, stand down when it is set. The per-prompt drift reminder and the subagent hook keep running. Other plugins' hooks are untouched.

## Shipped preamble

`plugin/unharness/src/unharness/preamble.md`, at most 25 lines, plain, in the agent's voice, with no seams and no mention of unharness or compilation. It tells the model what each residue above is and how to weigh it: the identity line is the harness's fixed label and no instruction; a system reminder (text in `<system-reminder>` tags, or a system-role message inside the conversation) comes from the application, not from the user, and carries facts such as the email, the date, the working folder, file-change notes, and the skill and agent lists; hook output is text the owner's installed hooks add; a skill's text arrives in a user turn when the skill loads and is followed as the owner's standing instruction; a task-list nudge or a notice about the user not hearing from you is the harness's and not the user's word, and the constitution's own rules on speaking and silence, where it has them, govern over it. A fable agent writes it; it is reviewed against write-well and Raise the Bar.

## `/compile-commitments` (round 21)

Plugin skill `manifesto:compile-commitments` at `plugin/skills/compile-commitments/SKILL.md`, written to the memento:skill-creation rules by a fable agent. The session runs `unharness stack` into a file and reads it whole; reduces each element to its axioms; maps convergence and tension; resolves each tension with a rule; writes `.manifestos.interplay.md`, then `.manifestos.commitments.md` with the paired lines "I must ..., and I will ..." and "I must not ..., and I will not ...", each file opening with the `<stack>` block, all tagged as the session's own raw output; then runs `unharness prompt > /dev/null` to confirm the compile passes.

## Distribution (round 8) and release (round 9)

- Package `unharness` in `plugin/unharness/`: pyproject, src layout, tests, Python 3.11 or later, stdlib-only at runtime where possible.
- PyPI publish is the owner's step. Until then: `uvx --from "git+https://github.com/ryzhakar/llm-manifestos@v3.5.0#subdirectory=plugin/unharness" unharness`, or a shorter git form if RESEARCH A5 finds one.
- Inside sessions, `plugin/bin/unharness` runs the plugin's bundled copy, `${CLAUDE_PLUGIN_ROOT}/unharness`, through uvx; `UNHARNESS_FROM` (a path or a git URL) is the only way to run another source (triage decision a).
- Release: rebase on origin/main, fast-forward main, plugin 3.5.0 in `plugin/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`, tag v3.5.0, push; the records keep the owner's publish commands.

## Acceptance

1. The pytest suite, the hook tests, `claude plugin validate` for the plugin and the marketplace, and `just readme` pass.
2. Captured request bodies (`OTEL_LOG_RAW_API_BODIES=file:<dir>`) of an unharnessed `-p` run and an interactive tmux run show the compiled prompt as the system prompt; no CLAUDE.md, git instructions, or attribution; the tool, skill, and agent registries present; and every residue listed in the README with its capture.
3. End to end in this repo: `/compile-commitments`, then `unharness prompt | unharness launch -- claude` in tmux; the session names the elements that govern it, and still does after `/compact`.
4. Code, prose, and spec-compliance reviews are triaged, and their accepted findings applied.
