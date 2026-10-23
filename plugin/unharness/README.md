# unharness

Compile a project's manifesto stack into a Claude Code session's system prompt, and launch the session with the harness's own instructions switched off.

```
/compile-commitments
uvx unharness prompt | uvx unharness launch -- claude
```

Until the package is published, run `uvx --from "git+https://github.com/ryzhakar/llm-manifestos@v3.5.0#subdirectory=plugin/unharness" unharness` in place of `uvx unharness`. The launcher's input is reopened on the terminal.

- `unharness prompt [--config PATH] [--digests] [--stack-digests] [--overlap] [--minified]` prints the compiled prompt. `--digests` and `--stack-digests` swap manifesto texts for digests, `--overlap` lets stack digests share a manifesto, and `--minified` loads the min pair, the two `.min.md` session files; the Unharness section of `plugin/README.md` states the cover rule.
- `unharness stack [--config PATH] [SLUG ...]` prints the `<stack>` block and the constitution; given slugs, it prints those manifestos alone.
- `unharness stamp DIGEST [--config PATH]` writes the digest's entry into its `index.json`, as in `unharness stamp .claude/digests/dry.md`.
- `unharness doctor [--config PATH] [--digests] [--stack-digests] [--overlap] [--minified]` prints one `OK`, `WARN`, or `FAIL` line per check and exits 1 on any FAIL.
- `unharness launch [--keep-claude-md] [--keep-web-search] [--no-hooks] [PROMPT] [-- LAUNCHER [ARGS...]]` caches the prompt and runs the launcher, or prints the command when none follows `--`.

The config schema is in `plugin/SCHEMA.md`. The strip table and the text that stays are in the Unharness section of `plugin/README.md`.

Test with `uv run --project plugin/unharness pytest -q` from the repository root.
