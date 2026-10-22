# unharness

Compile a project's manifesto stack into a Claude Code session's system prompt, and launch the session with the harness's own instructions switched off.

```
/compile-commitments
uvx unharness prompt | uvx unharness launch -- claude
```

Until the package is published, run `uvx --from "git+https://github.com/ryzhakar/llm-manifestos@v3.5.0#subdirectory=plugin/unharness" unharness` in place of `uvx unharness`. The launcher's input is reopened on the terminal.

- `unharness prompt [--config PATH]` prints the compiled prompt.
- `unharness stack [--config PATH]` prints the `<stack>` block and the constitution.
- `unharness launch [--keep-claude-md] [--keep-web-search] [--no-hooks] [PROMPT] [-- LAUNCHER [ARGS...]]` caches the prompt and runs the launcher, or prints the command when none follows `--`.

The config schema is in `plugin/SCHEMA.md`. The strip table and the text that stays are in the Unharness section of `plugin/README.md`.

Test with `uv run --project plugin/unharness pytest -q` from the repository root.
