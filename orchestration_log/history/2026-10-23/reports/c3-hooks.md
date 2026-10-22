# C3 hooks

The hooks now read the stack through the unharness config module alone, and the two old parsers are deleted. All work is in `/Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness` on `feat/unharness`, with nothing pushed. For this repo's own `.manifestos.yaml`, every hook prints byte for byte what it printed before, under the system Python 3.9 as well as 3.14.

## Commits

The first commit settles your three answers on the core; the rest are the hooks unit.

- e506b72 feat(unharness): quotes in governs, empty stack stops
- d8a6920 feat(unharness): a colon without a space stays in a name
- 709aa3e fix(unharness): config.py runs on Python 3.9 for hooks
- 082cc86 feat(hooks): read config through unharness, stand down under it
- 9424e6e doc(schema): the evolved config schema

The merge left the suite green, because the core tests compare against the shipped preamble and never pinned the placeholder. `uv.lock` was already committed.

## What each hook reads and prints now

All four hooks source `ensure-repo.sh`, whose `detect_manifestos` runs `python3 <plugin>/unharness/src/unharness/config.py <project>/.manifestos.yaml --json` and splits the JSON into the same variables as before, with one new variable for the config folder. A failing config leaves the stack empty, so the hooks stay silent as before.

- **session-start.sh:** exits 0 with no output when UNHARNESS is set and not "0". Otherwise it prints the same preamble, binding core, oath skill, and footer as before.
- **post-compact.sh:** the same stand-down, then the same JSON wrapper as before.
- **subagent-start.sh:** unchanged in behavior and still running under UNHARNESS. It reads the `subagents` section from the JSON.
- **drift-reminder.sh:** unchanged in behavior and still running under UNHARNESS. Its tagline script reads manifesto frontmatter through the config module's public `parse_yaml`.
- **Element sentences:** the three copies of the sentence code are replaced by one script, `hooks/describe_elements.py`. A `file` source prints `read it from <absolute path beside the config>`. A `manifesto` source prints `read it from <registry>/manifestos/<ref>.md`. A `skill` source and every other form print as before.
- **Colon items:** `- agent-conduct:write-well` is now the name `agent-conduct:write-well`, as real YAML reads it, and crashes nothing.

## Tests

Hook tests, run with `python3 -I plugin/tests/test_hooks.py`: 15 pass, the 8 old ones and 7 new.

- A file source is read from its absolute path beside the config.
- A manifesto source is read from the registry file of that name.
- A skill source is read as written.
- A bare item with a colon is a name in session-start, post-compact, and drift-reminder.
- Session-start and post-compact print nothing under UNHARNESS=1.
- UNHARNESS=0 leaves both running.
- Drift-reminder and subagent-start keep running under UNHARNESS=1.

Core tests, run with `uv run --project plugin/unharness pytest -q plugin/unharness`: 34 pass. The new ones cover a double quote in a purpose becoming a single quote in `governs`, the empty stack error on both verbs, the colon rule, and the `directory` key in the JSON. From the worktree root the same command collects 62 tests and all pass.

## Validation results

- `claude plugin validate plugin`: passed.
- `claude plugin validate .`: passed.
- Before-and-after capture of all four hooks over this repo's config, including four subagent types: identical on Python 3.14 and on `/usr/bin/python3` 3.9.6.
- A project with no config prints nothing. A project with only a CLAUDE.md section binds as before.

## Deviations with reasons

- **Script path.** The hooks find the config module beside themselves, `hooks/../unharness/src/unharness/config.py`, where your prompt named `${CLAUDE_PLUGIN_ROOT}`. The other hook files locate siblings the same way, and the two paths are one folder in an installed plugin.
- **Colon rule.** The core now treats a colon as a mapping marker only when a space or the line end follows it. This reverses my earlier error for `- agent-conduct:write-well`, which you asked to stop crashing.
- **Manifesto source.** I read "today's registry read" as an explicit registry path, so an element whose name differs from its reference binds to the right file.
- **Python 3.9.** The config module gained a postponed-annotations import, because the stock macOS `python3` failed on `str | None`. I checked this by hand and added no test, since the suite runs one Python.
- **JSON shape.** `config.py --json` gained a `directory` key, which the hooks need to resolve file sources.
- **Incidental schema fixes.** While rewriting the schema document I corrected three stale claims: the subagent match order now includes the suffix step, the drift hook is described as matching by slug and title, and the examples use evolved source forms. I also removed the legacy path and URL examples, which `unharness` refuses.
- **Silent errors.** A config error still leaves the hooks silent, as the old parser did. A typo that empties the stack gives no message.

## Open questions

- Should the hooks print a config error, such as a flow list, instead of staying silent? A missing config must stay silent, so the hooks would need to tell it apart from a broken one.
- `plugin/README.md` still documents only the unittest command in its Tests section. Should the README unit add the pytest command for the unharness package?
- Should a relative `manifesto_dir` resolve against the config folder in the hooks, as it does in `unharness`? Today the hooks use it as written.

Both validation commands pass, and every hook prints exactly what it printed before for this repo's config. The hooks now read the stack only through the unharness config module, the two old parsers are deleted, and session-start and post-compact stand down under UNHARNESS. The schema document is rewritten for the evolved forms, and three open questions remain for the orchestrator.

## Follow-up

All three of your answers are applied in commit `feat(hooks): report broken config, resolve relative manifesto_dir`. The hook suite now has 18 tests and the core suite 35, and all pass. The plugin validates, and this repo's config still gives byte-identical hook output on Python 3.14 and 3.9.

- **Broken config.** Every hook prints one line to stderr, such as `unharness: you must be a list of elements`, and exits 0 with nothing on stdout. A missing config stays silent. To tell the two apart, `config.py` exits 2 for a missing config and 1 for a broken one. The command-line verbs still exit 1 for both. Tests cover a broken and a missing config in all four hooks, and both exit statuses of the script.
- **Relative manifesto_dir.** The hooks resolve it against the config folder to an absolute path, so the binding text, the manifesto source sentence, and the drift lookup all use it. A session-start test covers it. This also normalizes a trailing slash in an absolute `manifesto_dir`, which the repo's own config does not have.
- **README.** Left for the later unit, as you said.
- **Schema doc.** `plugin/SCHEMA.md` now describes the stderr line, the exit status 2, and the relative `manifesto_dir`.

Nothing is pushed, and I am stopping here until the launch verb arrives.
