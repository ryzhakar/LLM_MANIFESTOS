# C2 launch

The `launch` verb works as written, and the plugin launcher `plugin/bin/unharness` runs through uvx. All work is in `/Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness` on `feat/unharness`, with nothing pushed.

## Commits

- 5c6c437 feat(launch): print the launch command
- 9129fce feat(launch): refuse an empty prompt
- 26c95c9 feat(launch): keep and no-hooks flags
- a529b4e feat(launch): run the launcher through a seam
- 8187a87 feat(launch): reopen stdin on the terminal
- 7fc4cdb feat(launch): the launch verb and shell fallback
- 4b5e9f3 test(launch): a real shell function as launcher
- e66b897 feat(plugin): bin/unharness launcher through uvx

## The printed command for the default flags

Verbatim, from `unharness launch "You are bound."` with `XDG_CACHE_HOME=/tmp/c2/cache2`:

```
env CLAUDE_CODE_ATTRIBUTION_HEADER=0 CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1 CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 CLAUDE_CODE_SILENT_TURN_REMINDER=0 UNHARNESS=1 claude --system-prompt-file /tmp/c2/cache2/unharness/148ba4c4082524f03e62415a9468a1e1f33292b23cbcde8ae0f5e2526606eb83.md --disallowedTools WebSearch --settings '{"includeGitInstructions":false,"attribution":{"commit":"","pr":""},"autoMemoryEnabled":false,"outputStyle":"default"}' </dev/tty
```

## Tests

All 51 core tests pass, 17 of them new for this unit. The whole worktree collects 82 tests, and all pass. The 18 hook tests and both plugin validations also pass.

In `tests/test_launch.py`, calls go through the function with fakes:
- Without a launcher, the default command is printed and nothing runs.
- The prompt is cached under its sha256 with file mode 0600 and folder mode 0700, even under umask 0.
- An empty prompt stops before anything is written.
- `--keep-claude-md` omits only the CLAUDE_MDS variable.
- `--keep-web-search` drops the disallow.
- `--no-hooks` adds `disableAllHooks` to the settings.
- All three flags together give the expected command.
- With a launcher, stdin is reopened first, then the launcher runs with the stripped environment added to the inherited one, and its status returns.
- Stdin is redirected onto the terminal through the `os.dup2` seam.
- Without a terminal, stdin stays as it is.

In `tests/test_launch_cli.py`, subprocess runs:
- A fake launcher on PATH replaces the process; it dumps its arguments and environment, and its exit status 3 comes back.
- The prompt comes from stdin when no argument gives it, and `--keep-claude-md` is honored end to end.
- An empty prompt prints one line on stderr and exits 1.
- Without a launcher the verb prints the command and runs nothing.
- A launcher not on PATH runs through `$SHELL -ic` with the quoted command. This test uses a fake shell script that records its arguments, so it checks the constructed argv and the status without a real shell.
- A real `/bin/bash` with a `claude@meta` function in a throwaway `.bashrc` runs as the launcher. I also ran zsh by hand with the same result, and left it out of the suite.

The launcher script has only the smoke test you asked for: `UNHARNESS_FROM=<worktree>/plugin/unharness plugin/bin/unharness stack --config <worktree>/.manifestos.yaml` printed the stack block, starting with the write-well line.

## Deviations with reasons

- **No terminal.** When `/dev/tty` cannot be opened, stdin stays as it was. A hard error would break headless runs such as CI, and tests run without a terminal.
- **Inherited variable.** `--keep-claude-md` omits the variable the launch adds but does not unset one already in the caller's environment.
- **Separator.** The first `--` splits the command line only for `launch`; the other verbs never see it.
- **Cache on print.** The printed form also writes the cache file, because the printed command names it.
- **Prompt text.** The hash and the cached file hold the prompt exactly as received, including a trailing newline from `unharness prompt`.
- **Shell default.** With `SHELL` unset, the fallback uses `/bin/sh`.
- **Smoke test side effect.** The smoke run of `launch` wrote one small prompt file into the real `~/.cache/unharness`.

## Open questions

- Should `unharness launch` skip the terminal reopen when stdin is already a terminal? Today the reopen is harmless in that case.
- Bash prints `no job control in this shell` on stderr when `-ic` runs without a terminal. Should the fallback silence it?

The launch verb prints or runs the stripped command from the strip table, and caches the prompt privately by hash. It passes 17 new tests, including a real bash function as launcher, and the plugin launcher passes its smoke test. The whole suite and both plugin validations pass, so only the two open questions remain.
