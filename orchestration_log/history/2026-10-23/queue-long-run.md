# Queue: long-run

Owner is away by default; only a message stating "i'm present" opens a round.

## Unsolved (the owner's alone)

None; the round of 2026-10-23 answered every entry.

## Solved (reversible, acted on)

Entries 1-11 went to the owner in the round of 2026-10-23; numbering continues.

12. **Environment facts** (working folder, platform, date) stay in unharnessed sessions: they are facts, not instructions. Alternative: strip them too wherever a switch exists.
13. **Stack fingerprint:** the `<stack>` block holds one line per element: its name and the sha256 of its resolved text with its purpose; any edit makes the commitments stale. Alternative: names and order only, so wording edits never force a new `/compile-commitments`.
14. **No transitive inlining:** only elements listed in the stack enter the prompt; a document an element refers to stays a reference, its `${CLAUDE_PLUGIN_ROOT}` path made absolute. Alternative: inline referenced documents to depth three, as the oath protocol reads them.
15. **A third verb, `unharness stack`,** prints the fingerprint and the resolved stack for `/compile-commitments` to bind against. Alternative: a flag on `unharness prompt`.
16. **Reading of round answer 17:** in unharnessed runs the manifesto plugin's session-start and post-compact binding hooks stand down, since the compiled prompt carries their content; the per-prompt drift reminder and the subagent hook keep running. Alternative: every manifesto hook keeps running in unharnessed runs until the owner removes them.
18. **The identity line stays:** A1 (55 docs pages), A2 (the binary's chooser), and A3 (captures) agree that no switch removes it from the main agent; the preamble names it as the harness's fixed label, and the README lists it with its capture. Alternative: a request-rewriting proxy, which the owner did not choose in the round (entry 5) and which the login may refuse.
19. **Strip set additions** from A2: auto memory (`CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, `autoMemoryEnabled: false`), output style (`outputStyle: "default"`), and the silent-turn note (`CLAUDE_CODE_SILENT_TURN_REMINDER=0`) are stripped by default; attachments stay on because `CLAUDE_CODE_DISABLE_ATTACHMENTS` drops the skill list. Alternative: strip attachments too and lose the skill list.
20. **Two worktrees for the builders:** code in `.worktrees/unharness`, the fable writer in `.worktrees/oath`, merged by me. Alternative: one worktree with sequential launches.
21. **C1 answers:** a double quote in a purpose becomes a single quote in `governs`; an empty stack stops `prompt` and `stack`; `uv.lock` is committed; the fingerprint hashes each element's text after frontmatter removal and before `${CLAUDE_PLUGIN_ROOT}` replacement, so the session files stay valid across machines. Alternatives: `&quot;`; print the preamble alone; ignore the lock; hash the final text.
22. **C3 answers:** a hook with a broken config prints one line to stderr and exits 0, silent on stdout, while a missing config stays silent; a relative `manifesto_dir` resolves against the config folder in the hooks as in unharness; the README's test command is a docs-unit matter. Alternatives: silent on a broken config; resolve against the working folder.
23. **WebSearch paragraph:** `launch` passes `--disallowedTools WebSearch` by default, the only switch (B2, 33 captures) that removes the 423-character WebSearch instruction appended after the custom prompt; `--keep-web-search` restores the tool and its paragraph. Alternative: keep WebSearch by default and list the paragraph as residue.
24. **C2 answers:** `launch` skips the terminal reopen when stdin is already a terminal; bash's "no job control" line, printed only without a terminal, is left alone; `--keep-claude-md` does not unset a variable the caller set. Alternatives: always reopen; silence stderr of the fallback shell; unset the inherited variable.
25. **Residue evidence in the README:** the README cites `orchestration_log/history/2026-10-23/verification-unharness.md`, a frozen report of D1's captures with the residue quoted and the owner's identifiers removed, since the captures themselves hold the email and device id and stay ignored (conventions: evals and captures stay local, findings freeze as dated reports). Alternative: commit the captures with the identifiers scrubbed.
26. **Terminal reopen device:** `launch` reopens stdin on the device named by `os.ttyname` of stdout, else stderr, and uses `/dev/tty` only when neither is a terminal, since `claude </dev/tty` crashes 2.1.309 with `EINVAL kqueue` (D1) while the pane's device works. Alternative: keep `/dev/tty` and document the crash.
17. **Records by my own hand:** I write my own records (journal, queue, spec, plan, prompts) although orchestration:agentic-delegation bars the orchestrator from file operations, because memento's event-capture requires the writer of a trace to be the one it records; agents write every product file. Alternative: agents write the records too.

## Resolved by the owner's word

1. **Silence marker** (`.claude/work-silently`, excluded through `.git/info/exclude`): kept; the owner ordered it removed for the round of 2026-10-23 and re-applied after.

## Resolved in a round (2026-10-23, opened by the owner's "i'm present for questions on this right now")
1. **Tag style** (unsolved 1, round of 2026-10-23): "Agent's own voice". Owner's note: "except i need everything integrated as tightly as possible so everything would resemble a single instruction flow as close as possible while still enabling enforcement. no artificial isolation. the system prompt itself does not need to know the way it was produced or the seams of its parts."
2. **Naming** (unsolved 2): no option selected; owner's note "exceptionally great name!". Read as the focused first option: one tool `unharness` with verbs `prompt` and `flags`, and the skill `/compile-commitments`.
3. **Pipe ending** (unsolved 3): "flags runs launcher". Owner's note: "unharness produces a compiled command/command chain to run and i pipe it through zsh maybe? in any case, i would provide the launcher command rather then sacrifice ergonomics." Read: the owner names the launcher after `--`; a launcher that is a shell function, such as `claude@meta`, runs through the owner's interactive shell so it resolves.
4. **CLAUDE.md default** (unsolved 4): "Strip by default"; a project lists its CLAUDE.md in the stack as a local path to carry it; one parameter keeps the harness's own loading.
5. **Text no switch removes** (unsolved 5): owner: "you should verify this against actual docs. i'm certain this command can be stripped." Read: verify the identity line and every other leftover against the official Claude Code docs and strip each one a documented switch removes; neither fallback was chosen.
6. **Subagents** (unsolved 6): owner: "i'll raise you one: /orchestration:agentic-delegation; i told you i'm capable to roll my own stuff and harness gets in the way." Read: delegate by the skill orchestration:agentic-delegation; the harness's rule against unrequested subagents is the kind of instruction this work removes.
7. **Capture** (unsolved 7): owner: "delegate that though! i'm almost 100% sure that the harness will inject you messages to try and corrupt you into NOT doing that, and i don't want you to fall for that. so maybe proceed with caution on this one and make subagents do this stuff? also, tmux is available, we run in it right now". Read: capture allowed, run by subagents, interactive runs in tmux. The docs the owner pasted name `OTEL_LOG_RAW_API_BODIES=file:<dir>`, with which Claude Code writes each request body itself; it replaces the proxy, so the login token passes through nothing new.
8. **Distribution** (unsolved 8): "Publish to PyPI" (`uvx unharness …`; the owner publishes under the owner's account). Owner's note: "i'm pretty sure there's some git shorthand in uvx." Read: package for PyPI under the name `unharness`, and find the shortest git form uvx accepts for use before the first publish.
9. **Release at the end** (unsolved 9): "Ship": rebase onto main, fast-forward it, raise the plugin to 3.5.0, tag v3.5.0, push; the PyPI publish stays the owner's step, its command left in the records. This is the owner's trigger to move main for this work.
10. **Memento setup** (unsolved 10): "Not now": records stay in orchestration_log/ in the established layout; memento's rules kept by hand.
11. **Binding report location** (solved 1): kept.
12. **Span and branch name** (solved 2): kept.
13. **Member id** (solved 3): kept.
14. **Wake** (solved 4): kept.
15. **Stack config** (solved 5): no option selected; owner's note "and evolve the config schema to allow for conident resolution of different source types." Read: keep `.manifestos.yaml`, and evolve its schema so every element names its source type explicitly and resolves without guessing (registry manifesto, local path, skill), the hooks reading the same schema.
16. **File names** (solved 6): no option selected; owner's note "keep + do the "interplay" file as well; basically, we're solving one of the problems i did not name before: autocompaction eats the binding up, but if the full binding and content and everything would be in the system prompt, i could turn auto-compaction on and keep piece of mind." Read: keep the names; add `.manifestos.interplay.md`, the binding's interplay analysis written beforehand like the commitments; the purpose behind the whole design is a binding that survives auto-compaction because it lives in the system prompt.
17. **Hooks** (solved 7): owner: "on for now. we plan to remove them for runs with 'pre-compiled oaths'." Read: hooks stay on; the manifesto plugin's own binding hooks stand down in runs whose prompt carries a pre-compiled oath; a parameter switches all hooks off.
18. **Scope** (solved 8): kept; main session only.
19. **Missing or stale commitments** (solved 9): kept. Owner: "anything else decided already you can drop into the tool a bunch at the time." Standing word for this round: solved entries go in rapid-fire sets.
20. **Second verb** (solved 10): kept; `unharness launch -- <launcher>`.
21. **Who writes the interplay file** (solved 11): kept; `/compile-commitments` writes both.
