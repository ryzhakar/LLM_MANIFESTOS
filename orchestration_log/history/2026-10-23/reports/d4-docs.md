# D4 docs fix pass

All 12 accepted docs items are applied, along with the sentences the code fixes made false. The work is in `/Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness` on `feat/unharness`, with nothing pushed.

## Commits

- 1490a61 doc(plugin): Unharness section matches the code and its evidence
- 84acf7a doc(schema): source fields, refusals, and hook renderings
- f821dd8 doc(readme): say unharness runs through uv

## Items applied

1. **Examples before publication.** The git form comes first, introduced by "Run it from git until the package is published, then from the package", and `uvx unharness` second. The package README says the same in one sentence. The session sentence now reads that `bin/unharness` runs the bundled copy, and that `UNHARNESS_FROM`, a path or a git URL, runs another source.
2. **Wrapper.** The README names the wrapper around the email line, in a user message, and says the date line sits outside it.
3. **Cache path and device.** The README gives `$XDG_CACHE_HOME/unharness/<sha256>.md`, or `~/.cache/unharness/` when unset. It says the printed command ends in the terminal's own device, and in `/dev/tty` only when neither output is a terminal.
4. **Evidence.** The README cites `orchestration_log/history/2026-10-23/verification-unharness.md` and names the captures d1-p-haiku, d1-p-opus, d1-tmux-haiku, d1-flag-keepmd, d1-flag-nohooks, d1-flag-websearch, b2-full-haiku, and a3-c5, with no ignored path. The lead of "What stays" has its verb, the modes read "interactive sessions" and "print mode", and hook output appears only in the table row.
5. **"Stripped" rows.** Attribution, auto memory, output style, and the silent-turn note read "set", with one sentence under the table saying no capture shows their text present or removed. The hook stand-down is described as implemented and tested, unshown by capture.
6. **Opening sentence.** It now says compaction cannot erase the binding because the prompt is not part of the conversation. It adds that one captured compaction left the prompt unchanged.
7. **Compile line first.** `/compile-commitments` opens the example block in both READMEs.
8. **Config location.** The schema gives hooks `$CLAUDE_PROJECT_DIR/.manifestos.yaml`, else the current folder, and `unharness` the `--config` path.
9. **YAML subset.** The paragraph states that an unplaceable line, a tab indent, a repeated key, and a list at its key's own indent stop the load with an error naming the line or key.
10. **Source section.** Any other first word stops the load and names the `file <path>` form. A table lists what each hook sentence says for `file`, `manifesto`, `skill`, and no source. The frontmatter rule is stated.
11. **Undefined terms.** The preamble file is described by what the preamble does. The `prompt` verb says it stops when a session file is missing or its `<stack>` block differs.
12. **Template.** The sentence now says unharness compiles the manifestos a project lists in `.manifestos.yaml` and runs through uv. I ran `just readme` and kept the regenerated `README.md`, which changed only by that sentence.

## Sentences the code changes made false

- The JSON description now names `directory`, `registry`, `source_type`, and `reference` in place of the raw fields, and the parsing rule for a mapping node matches.
- The `manifesto_dir` row says the path resolves to an absolute path with symlinks followed.
- The error table swaps the old legacy-source line for the load error with its full text, and adds the whitespace-name line and the YAML reader's three refusals.
- The drift hook description now says it looks up `<manifesto_dir>/manifestos/<reference>.md` exactly, and prints other elements bare.
- Element names must hold no whitespace.
- The `launch` verb has no `--config`, and the docs never gave it one.

## Items skipped

None. One point of wording differs from the triage, as you settled: the hooks render a skill source as `read it from skill <plugin>:<skill>`, not as a resolved path.

## Unverified in the docs

- The file `verification-unharness.md` did not exist when I finished, so the README cites a path and capture names that I did not read.
- The compaction claim rests on D3's recon report, `d3-e2e.md`, where the system block was identical before and after one compaction. That file is git-ignored, and I do not know whether the verification file will carry it.
- The git install line names tag `v3.5.0`, which does not exist yet.

## Validation results

- `uv run --project plugin/unharness pytest -q` from the worktree root: 111 passed.
- `python3 -I plugin/tests/test_hooks.py`: 23 passed.
- `claude plugin validate plugin` and `claude plugin validate .`: both passed.
- `just readme`: regenerated cleanly. The Unharness section has 56 lines, within the limit of 60.

Every docs item and every sentence the code fixes made false is now corrected, with the evidence cited by path and capture name only. The suite and both validations pass, and `README.md` is regenerated from its template. Three claims rest on a file not yet written, an ignored report, or a tag not yet made, and I list them above.
