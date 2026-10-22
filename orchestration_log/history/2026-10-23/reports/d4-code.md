# D4 code fix pass

All 17 accepted code items are applied by TDD in `/Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness` on `feat/unharness`, with nothing pushed. The triage held a D1 addendum, folded into items 1 and 4. I did not touch the preamble, the compile-commitments skill, or the docs.

## Items, commits, and tests

| Item | Commit | Test names |
|---|---|---|
| 1 terminal device | a06da30 | `test_the_device_is_the_one_stdout_is_on`, `test_the_device_is_the_one_stderr_is_on_when_stdout_is_not_a_terminal`, `test_the_device_is_dev_tty_when_neither_output_is_a_terminal`, `test_stdin_is_redirected_onto_the_device_it_is_given`; the printed-line tests now end in the chosen device |
| 2 YAML reader | f88c2eb | `test_a_line_the_reader_cannot_place_stops_the_load_and_is_named` (three cases), `test_a_tab_in_the_indent_stops_the_load`, `test_a_repeated_key_stops_the_load` |
| 3 bundled copy | e44f90e | `Launcher.test_by_default_it_runs_the_copy_bundled_with_the_plugin_without_the_uvx_cache` in `plugin/tests/test_launcher.py` |
| 4 `--no-cache` | e44f90e | `Launcher.test_a_directory_source_is_built_fresh_every_time`, `Launcher.test_a_git_source_keeps_the_uvx_cache` |
| 5 source grammar | 3eb8898, b180d1d | `test_a_source_that_is_not_manifesto_skill_or_file_with_a_reference_stops_the_load` (five cases); `ConfigProblems.test_a_legacy_source_is_refused_in_one_line_in_every_hook` |
| 6 registry once | 8fe314f, 7c58f2d | `test_a_relative_manifesto_dir_resolves_once_against_the_config_folder`; the hook test for a relative `manifesto_dir` now expects the resolved path |
| 7 frontmatter | 849cebe | `test_a_block_between_two_rules_is_prose_unless_it_opens_with_a_key` |
| 8 utf-8 | cd64dbf | `test_every_read_decodes_utf_8_whatever_the_locale`, `test_the_cached_prompt_is_utf_8_whatever_the_locale` |
| 9 whitespace name | 5d67bb7 | `test_a_name_with_whitespace_stops_the_load` |
| 10 login variable | 83a486b | the empty case added to `test_the_login_is_claude_config_dir_else_dot_claude_in_home` |
| 11 drift hook | 294ff88 | `DriftReminder.test_a_name_is_matched_to_its_manifesto_file_exactly_and_never_by_title`, `test_a_manifesto_source_names_the_file_whatever_the_element_is_called`, `test_a_skill_or_a_file_element_prints_its_bare_name` |
| 12 stderr and JSON | 35cc764 | `ConfigProblems.test_python_chatter_on_stderr_does_not_corrupt_a_valid_config` |
| 13 no prompt on a terminal | 28944fa | `test_without_a_prompt_and_with_a_terminal_on_stdin_it_stops_with_a_message` |
| 14 preamble limits | 93596e2 | `test_the_shipped_preamble_stays_within_25_lines_and_names_no_tool` |
| 15 cache default | dfa6bee | `test_the_cache_is_dot_cache_in_home_unless_xdg_cache_home_is_set_and_not_empty` |
| 16 switch names | e5de14f | covered by the existing printed-command tests |
| 17 dead code | e5de14f | none needed |

Items 14 and 15 add coverage for behavior that already held, so their tests passed on the first run. For item 8 I tested the stdin-free reads and the cache write; the launch prompt read from stdin still uses the locale, since the triage did not list it.

## Skipped or changed, with reasons

- **Item 11, the `sys.path` edit.** I kept it in `parse_taglines.py`, because the hook still needs the one YAML reader to read frontmatter. Dropping it would copy the reader into the hook. For the same reason `describe_elements.py` imports the two source-type names from `config.py`, which is how it avoids type-name literals.
- **Item 6, the raw `manifesto_dir`.** I removed the raw field from `Config` and the JSON, rather than keep it beside `registry`. A second field would hold the same fact in two places. Element JSON now carries `source_type` and `reference` in place of the raw `source`, by the same reasoning.
- **Item 12, the test.** `PYTHONWARNINGS=always` provokes no warning from the config script, so the test uses `PYTHONVERBOSE=1`, which writes to stderr and, before the fix, corrupted the JSON.
- **Hook output for skills.** The hooks print `read it from skill <plugin>:<skill>` as before. The docs item that says a skill gives "its resolved path" does not match this, so the docs agent should not promise it.
- **Registry paths in hooks.** The registry is now resolved with symlinks followed, so a hook prints the real path of a `manifesto_dir` that sits behind a symlink.

## The printed command

The command in your prompt fails as written: `unharness launch` has no `--config` option, so it exits 2 with "unrecognized arguments". I ran it without that flag on `launch`, which does not need a config because the prompt arrives as the argument. Its stdout and stderr were not terminals, so the line ends in `/dev/tty`:

```
env CLAUDE_CODE_ATTRIBUTION_HEADER=0 CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1 CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 CLAUDE_CODE_SILENT_TURN_REMINDER=0 UNHARNESS=1 claude --system-prompt-file /Users/ryzhakar/.cache/unharness/0f94670794bf00e789b9e849d31fc9e811605e6b5b37a180949fb2def1e44947.md --disallowedTools WebSearch --settings '{"includeGitInstructions":false,"attribution":{"commit":"","pr":""},"autoMemoryEnabled":false,"outputStyle":"default"}' </dev/tty
```

Run under `script`, which gives the command a terminal for its output, the same line ends in `</dev/ttys002`. The prompt it cached has 89773 bytes and mode 0600.

## Results

- `uv run --project plugin/unharness pytest -q` from the worktree root: 111 passed. The core suite alone has 72.
- `python3 -I plugin/tests/test_hooks.py`: 23 passed.
- `python3 -I plugin/tests/test_launcher.py`: 3 passed.
- `claude plugin validate plugin` and `claude plugin validate .`: both passed.
- Hook output for this repo's config matches the pre-change baseline byte for byte, rechecked after the last commit, for all four hooks.

Seventeen accepted items are applied with tests, and the one blocking terminal crash is fixed with the device chosen from stdout, then stderr, then `/dev/tty`. Four points deviate from the triage text, each for a stated reason, and the launch command you gave needs its `--config` removed. Everything passes and validates, and nothing is pushed.
