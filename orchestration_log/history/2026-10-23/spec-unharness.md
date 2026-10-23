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

## Verbs (round 2, round 3, round 20; queue 33, 37, 41)

- `unharness prompt [--config PATH] [--digests] [--stack-digests] [--overlap] [--minified]`: prints the compiled prompt; the four mode flags pick the constitution's texts and the session files, as the 3.6.0 part below specifies.
- `unharness stack [--config PATH] [SLUG ...]`: prints the `<stack>` block and then the `<constitution>`, exactly what a session binds to; `/compile-commitments` uses it (solved 15). Given slugs, it prints the block and the constitution of those registry manifestos alone, in the given order and without purposes; `/compile-digest` uses that form. It takes no mode flag, since a session always binds to full texts.
- `unharness stamp DIGEST [--config PATH]`: writes DIGEST's entry into its digest index.
- `unharness doctor [--config PATH] [--digests] [--stack-digests] [--overlap] [--minified]`: prints one line per check and exits 1 on any FAIL.
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

`launch` sets `UNHARNESS=1`. Every hook of the manifesto plugin, session-start, post-compact, subagent-start, and the per-prompt drift reminder, stands down when it is set, since the compiled prompt already carries the binding (changed in the 3.6.0 fix pass from queue 16, after the end-to-end capture showed the drift line in every request). Other plugins' hooks are untouched.

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

# 3.6.0: digests, minified session files, signatures, doctor

The owner's answers for this part are entries 27-41 of `queue-long-run.md`, cited below as queue N. Three flags trade full manifesto texts for shorter digests, a fourth picks condensed session files, and every compiled artifact loads only against the source hashes it was made for.

Terms used below:

- The plugin folder is `manifesto_dir` when the config sets it, else the manifesto plugin's highest cached version folder; it holds `manifestos/` and `digests/`.
- A manifesto element's slug is its registry stem: the reference of `source: manifesto <slug>`, else its `name`. Digests key by slug, never by element name.
- A source hash is the `sha256` that `resolve.py` computes for a `Document`: the hash of the body after frontmatter removal and stripping, before `${CLAUDE_PLUGIN_ROOT}` replacement.
- Words are whitespace-separated tokens; characters are Python string length.

## Digest sources and resolution (queue 32, 36-38)

A digest file's stem names its member set: the member slugs, sorted, distinct, and joined by `+`. A stem with one slug names a single digest; a stem with two or more names a stack digest.

| Kind | Local, beside the config | Plugin |
|---|---|---|
| Single | `.claude/digests/<slug>.md` | `<plugin folder>/digests/<slug>.md` |
| Stack | `.claude/digests/<a+b>.md` | `<plugin folder>/digests/stacks/<a+b>.md` |
| Index | `.claude/digests/index.json` | `<plugin folder>/digests/index.json` |

- Local wins: when both places hold a stem, unharness reads the local file against the local index alone, even when the local entry is stale.
- A digest is body-only markdown; its text enters the prompt stripped of surrounding whitespace and otherwise unchanged.
- Each index maps a stem to its members' source hashes, `{"<stem>": {"<slug>": "<sha256>", ...}, ...}`, and covers the digests of its own place; the plugin index covers `stacks/` too.
- A digest is usable when its index holds an entry for its stem, the entry's slugs equal the stem's slugs, and every hash equals that manifesto's current source hash. An entry whose slugs differ from the stem's counts as missing.
- A stack file whose stem is not sorted and distinct, and a stack digest placed in the plugin's `digests/` instead of `digests/stacks/`, are no candidates and raise nothing; decision 3 binds the files a mode considers.

`unharness stamp DIGEST [--config PATH]` (queue 37) reads DIGEST's stem and resolves each slug as a registry manifesto through `resolve_stack`, the one home for hashing. It writes the entry into the index of DIGEST's place: the `index.json` in DIGEST's folder, or in that folder's parent when the folder is `stacks`. It creates a missing index, replaces the stem's entry, keeps every other entry, writes `json.dumps(index, indent=2, sort_keys=True)` and a newline, and prints `stamped <stem> in <index path>`. It refuses, each after the `unharness: ` prefix, a missing DIGEST with `no digest at <path>`, a stem with unsorted, repeated, or empty slugs with `<file name> is not named by sorted, distinct slugs joined by +`, and a slug that does not resolve with the resolver's message.

A digest mode refuses with these messages, verbatim after the `unharness: ` prefix, each naming its fix:

    no digest for <slug>: tried <local path> and <plugin path>; run /compile-digest <slug>
    <digest path> has no entry in <index path>; run unharness stamp <digest path>
    <digest path> is stale (changed: <slug>, <slug>); run /compile-digest <every slug of the stem, space-separated>
    <index path> is not a JSON object of stems to slug hashes; fix or delete it, then run unharness stamp on each digest it covers

A stale digest names `/compile-digest` and not `unharness stamp`, because its manifesto changed under it and its text needs rewriting; `/compile-digest` stamps after it writes.

## Cover selection (queue 27, 28, 33, 35)

- No digest flag: every element enters in full, as in 3.5.0.
- `--digests`: every manifesto element enters as its single digest.
- `--stack-digests`, which implies `--digests`: the candidates add every stack digest whose slugs all belong to the stack's manifestos. Without `--overlap`, chosen stack digests share no slug; with it, they may. Single digests cover exactly the slugs that no chosen stack digest covers.
- `--overlap` without `--stack-digests` stops with `--overlap requires --stack-digests`.
- A manifesto counts as covered when a usable single digest or a usable candidate stack digest covers it (queue 28). A digest mode refuses only when some manifesto has neither, with the missing-digest message naming that slug. Under `--digests` alone only singles count, so each manifesto needs its single.
- Every digest file a mode considers, single or stack, must be usable; an unusable one stops the compile with its message.
- Without `--overlap`, a stack whose every manifesto is covered but which no disjoint choice covers stops with `no cover without overlap; add --overlap or run /compile-digest <slug> for each of: <slugs with no single digest, comma-separated>`.
- Every digest mode refuses a stack that names one slug twice: `manifesto <slug> appears twice in the stack; digest modes need each once`.
- The cover is the one with the fewest total characters across the chosen digest texts. A tie goes to fewer files, then to the lexicographically smaller sorted list of stems. unharness returns exactly this optimum; how it searches is its own, and a stack of twelve manifestos with a digest for every pair of them compiles in seconds.
- Skills and `file` elements enter in full in every mode (queue 28).

The constitution keeps one block per element, in config order, with two changes:

- A single digest renders in the shape of the full text: `<{name} governs="{purpose}">`, the digest text, `</{name}>`.
- A stack digest renders as one block at the position of its first member in config order; its other members render nothing at their own positions. Two stack blocks that fall at one position follow stem order.

      <{name1}+{name2} governs="{purpose1}; {purpose2}">
      {stack digest text}
      </{name1}+{name2}>

The tag joins the members' element names with `+` in config order. `governs` joins the purposes present, in the same order, with `; `; it is omitted when no member has a purpose, and a double quote in a purpose becomes a single quote. Under `--overlap`, a member that two chosen stack digests share appears in both tags. No tag or attribute names a digest, a stack, or a summary (round 1).

## Minified session files (queue 30, 40)

- `--minified` makes `prompt` read `.manifestos.interplay.min.md` and `.manifestos.commitments.min.md` in place of the full pair, and combines with every digest flag.
- Each min file opens with the same `<stack>` block as the full pair and goes stale by the same rule. A missing or stale min file stops `prompt` with the 3.5.0 message under the min file's name, naming `/compile-commitments`.
- `/compile-commitments` writes all four files in one run: the full pair unchanged, then the min pair condensed from it. Each min body, the text after the `<stack>` block, holds at most one third of the words of its full counterpart's body. One third scales with the stack, where a fixed 150 words would starve a stack of eleven elements.
- The min interplay keeps the rules that resolve tensions and the priority order, and drops the axioms, the convergences, and the quotations. The min commitments hold one `I must ..., and I will ...` line per element in stack order, with the prohibition folded in. Both keep the `<interplay>` and `<commitments>` tags and the session's first-person voice.
- The skill ends by running `unharness prompt > /dev/null` and `unharness prompt --minified > /dev/null`, and reports both exit codes.

## Signatures (queue 31, 32)

Every compiled artifact records the source hash of each source it was made for, and loads only when each recorded hash equals the current source hash. The session files, all four, record their sources in the `<stack>` block, one `name sha256 purpose` line per element in config order; a change to an element's text, its purpose, or the order makes them stale. A digest's index entry records one `slug: sha256` pair per member; only a change to a member manifesto's text makes it stale, since a digest carries no purpose. No mode changes a signature: `stack` prints one block in every mode, `prompt` checks the session files against that block in every mode, and no hash covers a digest's own text. Commitments compiled against the full stack therefore load under every digest flag.

## `unharness doctor` (queue 41)

`unharness doctor [--config PATH] [--digests] [--stack-digests] [--overlap] [--minified]` prints one line per check, `OK|WARN|FAIL <check>: <detail>`, in the order below. It exits 1 on any FAIL and 0 otherwise. It reads files and runs `claude --version`, and makes no network call. A finding about an artifact that `prompt` would load under the given flags is a FAIL; the same finding about an artifact `prompt` would not load is a WARN.

| Check | OK detail | Finding |
|---|---|---|
| `config` | the config path | FAIL with the load error; doctor then runs only `claude`, `uv`, and `manifesto plugin` |
| `element <name>` | the resolved path | FAIL with the resolver's message; the `digest`, `cover`, session-file, and `prompt size` checks, which need the whole stack, are left out while any element fails |
| `skill <plugin>:<skill>` | the resolved version | WARN when it differs from the version in `<login>/plugins/installed_plugins.json`, or no record exists |
| `digest <stem>` | `local` or `plugin`, current | the refusal message; one line per manifesto's single digest, then one per candidate stack digest |
| `cover` | stems in render order and their total words | the refusal message; the flags' digest mode, else `--stack-digests --overlap` |
| `.manifestos.interplay.md`, `.manifestos.commitments.md`, and the min pair | current | the missing or stale message, one line per file |
| `preamble` | `shipped` or `.manifestos.preamble.md` | none |
| `claude` | path and version | WARN when not on PATH, since a shell function can launch, when it prints no version, or when the version differs from the tested 2.1.309 |
| `uv` | the paths of `uv` and `uvx` | FAIL when `uvx` is not on PATH |
| `manifesto plugin` | the installed version | FAIL when absent from `installed_plugins.json` or below 3.6.0, whose hooks do not all stand down |
| `prompt size` | `full <n> words; shortest <n> words` | WARN when the shortest mode cannot compile, with its message |

The `prompt size` check counts the preamble in its `<harness>` tags, the constitution, and whichever session files exist, ignoring staleness; full means no flag, and shortest means `--stack-digests --overlap --minified`. An excerpt of `unharness doctor --minified`:

    OK config: /work/proj/.manifestos.yaml
    OK element dry: /cache/llm-manifestos/manifesto/3.6.0/manifestos/dry.md
    WARN digest raise-the-bar: no digest for raise-the-bar: tried ...; run /compile-digest raise-the-bar
    FAIL .manifestos.commitments.min.md: .manifestos.commitments.min.md is missing; run /compile-commitments
    WARN claude: /usr/local/bin/claude 2.1.312, tested with 2.1.309

## `/compile-digest` (queue 39)

Plugin skill `manifesto:compile-digest` at `plugin/skills/compile-digest/SKILL.md`, invoked as `/compile-digest <slug> [<slug>...]`, written to the memento:skill-creation rules by a fable agent, as `/compile-commitments` was.

1. Sort and dedupe the slugs; the stem joins them with `+`.
2. Run `${CLAUDE_PLUGIN_ROOT}/bin/unharness stack --config <path> <slugs>` into a temporary file and read it whole, never sending it into the conversation.
3. Bind to the manifestos in that file through `manifesto-oath`.
4. For one slug, write by the method the skill itself carries (3.6.1): each demand as one plain sentence, the manifesto's order kept, boundaries folded in, one standing line, Strunk applied, the draft checked against the source, under 350 words. For several, add the rules of write-stack-digest: converging demands merged, each tension replaced by its resolution, rules in priority order, each sentence scoped to its object, under 850 words. The skill carries these rules in its own text, since the repo's skills do not ship.
5. Write the body alone, with no header, frontmatter, or title, to `.claude/digests/<stem>.md` beside the config, creating the folder.
6. Run `${CLAUDE_PLUGIN_ROOT}/bin/unharness stamp .claude/digests/<stem>.md --config <path>` and report its exit code; on a failure, fix what the message names and run it again.

The skill composes a stack digest from the full manifestos, not from their single digests, because the signature hashes the manifestos. It writes no eval record and checks no gate, since the owner set digest quality aside (queue 29).

## CLI synopsis

The Verbs section above carries the 3.6.0 synopsis. `--stack-digests` implies `--digests`; `--overlap` requires `--stack-digests` (queue 35). `prompt` and `doctor` accept the four mode flags; `stack`, `stamp`, and `launch` accept none.

## Tests

Each test builds a plugin folder, a login, and a project under `tmp_path`; no test reads the real login.

- Flags: `--stack-digests` alone admits stack candidates; `--overlap` alone exits 1 with its message; `stack` and `stamp` reject mode flags.
- Resolution: a local stem wins over the plugin's; a stale local entry refuses even when the plugin copy is current; each of the four refusals prints its text verbatim; an entry with an extra slug counts as missing; a stack digest at `<plugin folder>/digests/<a+b>.md` is no candidate.
- Stamp: it creates an index; it replaces one entry and keeps the rest; it writes a plugin stack digest's entry in the parent of `stacks/`; it refuses unsorted and repeated stems and an unresolved slug; its hashes equal the `<stack>` block's for the same manifestos.
- Cover: `--digests` picks singles alone; a shorter stack digest beats its singles and a longer one loses; chosen stack digests stay disjoint without `--overlap` and share with it; ties go by file count, then by stem order; a stack digest with a slug outside the stack never enters; a stack digest alone covers a manifesto that has no single; a manifesto with neither refuses, naming its slug; under `--digests` a manifesto that only a stack digest covers refuses; coverage that only overlapping stack digests reach refuses without `--overlap` with the no-cover message; skills and files stay full; a repeated slug refuses.
- Rendering: a single digest block has the full block's shape; a stack block sits at its first member's position, with tag and `governs` joined in config order, `governs` omitted without purposes, and quotes replaced; two overlapping stack blocks both name the shared member.
- Minified: `--minified` reads the min pair; a missing and a stale min file each refuse, naming `/compile-commitments`; session files compiled against the full stack load under `--stack-digests --overlap --minified`.
- Stack slugs: `stack dry kiss` prints the block and constitution of those two manifestos alone, without purposes.
- Doctor: a fixture for each check yields its OK, WARN, and FAIL lines; one finding flips between FAIL and WARN with the flags; one FAIL exits 1 and WARNs alone exit 0; a config FAIL leaves only the three config-free checks; the suite stubs `claude --version` and runs doctor with sockets patched to raise.
- Skills: `claude plugin validate` passes with `compile-digest` and the four-file `compile-commitments`; end to end in this repo, `/compile-digest` writes and stamps a local digest, and `unharness prompt --stack-digests --overlap --minified` exits 0.

## Decisions made in the spec

1. The plugin folder holds both `manifestos/` and `digests/`, and digests key by registry slug, never by element name.
2. Without `--overlap`, a stack whose manifestos are each covered, but by no disjoint choice, stops with its own message, naming `--overlap` and the slugs that lack singles.
3. Every digest file a mode considers, single or stack, must be usable; an unusable one stops the compile instead of dropping out unseen.
4. Local wins per stem even when the local entry is stale.
5. A stale digest names `/compile-digest`; only a missing entry names `unharness stamp`.
6. A stack digest renders at its first member's position, its tag joining element names by `+` and its `governs` joining purposes by `; `, both in config order.
7. `unharness stack` takes slugs for `/compile-digest`, and takes no mode flag.
8. `/compile-digest` composes stack digests from full manifestos and writes no eval record.
9. A min body holds at most one third of its full body's words, and the min commitments hold one line per element.
10. Doctor FAILs on what the flags load and WARNs on the rest; a missing `claude` is a WARN; the `cover` line falls back to `--stack-digests --overlap`.
11. Stamp writes sorted, two-space-indented JSON and prints one line.

# 3.6.1: reminder switches, quiet pipes, one block type, doctor range, digest method

Source of the first item: `identity-line-findings.md`, "What unharness should change". The deferred items come from `reviews/digests-triage.md`: code N12 and the end-to-end `BrokenPipeError` line.

1. **Reminder switches.** `launch` adds `CLAUDE_CODE_TODO_REMINDER_MODE=off`, which removes the task-list and TodoWrite nudges and keeps the skill list, and `CLAUDE_CODE_TOTAL_TOKENS_REMINDER=off`, which removes the token-count line. The printed command shows both. The docs name neither, so a release may drop them; the strip table, `plugin/README.md`, the unharness README, and `plugin/SCHEMA.md` say so. The preamble sentence on the task nudge stays, since the nudge may return.
2. **Quiet pipes.** Every verb, when its reader closes stdout early as in `unharness stack | head`, exits 0 with no traceback and no message.
3. **One block type.** `Block` and `Document` become one type when the merge changes no output: the constitution renders the same text for every mode.
4. **Doctor range.** One constant records the range of `claude` versions the package has been tested with; both ends read 2.1.309 today. `claude` WARNs with `claude: <path> <version>, outside the tested range <lo>–<hi>` when `claude --version` falls outside it; inside it the OK line is unchanged. This replaces the `claude` row's third WARN cause in the table above.
5. **`/compile-digest` method.** The plugin skill carries the digest method in its own voice: list every distinct demand, collapse restatements, write one plain complete sentence per demand, fold each boundary into the sentence it limits, keep the manifesto's own order, apply Strunk, check that every demand stands present or deliberately dropped, and name a drop in the stamp commit. It refers to no repo-local skill.
6. **Versions.** Package and plugin read 3.6.1. Doctor's floor for the manifesto plugin stays 3.6.0.
