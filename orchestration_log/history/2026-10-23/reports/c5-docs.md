# C5 docs

The plugin README now has an Unharness section, the package has its own short README, and the root README carries one line about the tool. The terminal-reopen answer from C2 is applied, tested, and committed. All work is in `/Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness` on `feat/unharness`, with nothing pushed.

## Commits

- 1a71c4f feat(launch): keep stdin when it is already a terminal
- 56a99bb doc(plugin): Unharness section and package README
- fd6206c doc(readme): one line about unharness in the install section

## Sections added with line counts

| File | Addition | Lines |
|---|---|---|
| `plugin/README.md` | Unharness section, before Install | 56 |
| `plugin/README.md` | compile-commitments entry in the skills list | 7 |
| `plugin/README.md` | pytest command in the Tests section | 1 |
| `plugin/unharness/README.md` | new file | 15 |
| `README.template.md` and `README.md` | one sentence pointing at the plugin README, in the install section | 2 each |

`just readme` regenerated `README.md` with exactly that one added sentence from the template, and a second run changed nothing. Before I edited the template it produced no diff.

## Validation results

- `uv run --project plugin/unharness pytest -q` from the worktree root: 83 passed. The core suite alone has 52.
- `python3 -I plugin/tests/test_hooks.py`: 18 passed.
- `claude plugin validate plugin` and `claude plugin validate .`: both passed.

## Claims I did not verify myself

- **Published install.** `uvx unharness` and the pipeline `uvx unharness prompt | uvx unharness launch -- claude` name an unpublished package. I ran the same pipeline with the local package path and a fake launcher, and it cached the prompt and passed `--system-prompt-file` as documented.
- **Git install line.** The tag `v3.5.0` does not exist, and the plugin version is still 3.4.0, so `bin/unharness` points at `v3.4.0` until the release unit bumps it.
- **Strip rows with no captured effect.** The captures show no auto memory text or output style text even in the baseline, so those two switches never had anything to remove. The attribution row has no capture of its effect.
- **Silent-turn row.** B2 could not test `CLAUDE_CODE_SILENT_TURN_REMINDER=0`, because the note fires only after five silent turns. The row rests on A2's reading of the binary.
- **Task-list nudges and file-changed notes.** A one-turn capture cannot show them. The README states that their one switch also drops the skill list, which `b2-a-attachments` confirms, but it does not show the notes themselves.
- **Capture paths in a clone.** The README names `orchestration_log/recon/2026-10-23/captures/`, but `recon/` is git-ignored, so the folders exist only on this machine.

I did check the captures behind the "What stays" list by searching the request files. The identity lines in `a3-c5` and `b2-full-haiku`, the email wrapper, the hook paragraph and its absence in the no-hooks capture, the worktree sentence, the MCP instructions in `a3-c5`, and the missing skill list in `b2-a-attachments` all match what the README says.

## Deviations

- **No hooks section.** The plugin README has none, so Unharness sits after Agents and before Install.
- **Terminal reopen.** Per your answer, `launch` leaves stdin alone when it is already a terminal. The existing reopen tests now inject that check, so they do not depend on where the suite runs.

The docs are written, regenerated where generated, and committed, and the whole suite and both validations pass. Six claims rest on reports or on unpublished packages and are listed above. The one open matter is that the capture paths named in the README do not exist in a clone of the repo.
