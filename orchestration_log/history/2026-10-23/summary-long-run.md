# Summary: long-run (unharness), 2026-10-23

Condenses this stretch. Written at closure.

## Narrative

- The owner handed over one long-running task: take a session's instructional foundation back from the harness. A round of 21 questions settled the design (`queue-long-run.md`); the spec (`spec-unharness.md`) became the one home of it; the owner said go, and the work ran by orchestration:agentic-delegation to completion.
- Phase A, five research agents: the docs (55 pages), the binary, baseline captures through `OTEL_LOG_RAW_API_BODIES`, the repo, and uvx packaging. They agreed that no switch removes the identity line from the main agent, that `CLAUDE_CODE_DISABLE_ATTACHMENTS` also drops the skill list, and that no uvx git shorthand exists; B2's 33 captures found `--disallowedTools WebSearch` the only switch for the WebSearch paragraph.
- Phase C, one sonnet agent built the package by TDD (config, resolve, compile, cli with `prompt`, `stack`, `launch`; the plugin launcher; the hooks reading the stack through the one config module; docs), and a fable agent wrote the preamble and the `/compile-commitments` skill.
- Phase D: three reviews (55 findings, 47 accepted as 38 items), a capture verification, and an end-to-end run that wrote this repo's interplay and commitments files and showed the compiled prompt unchanged across `/compact`. The pipe form crashed (`claude </dev/tty`, EINVAL kqueue); the fix reopens stdin on the terminal device of stdout or stderr. Re-verification passed.
- Shipped 3.5.0 on the owner's standing word: `origin/main` 43a1e3e..002db33, tag v3.5.0; the git install line runs.

## For the owner

- Update the installed plugin (`/plugin marketplace update`, `/reload-plugins`); the installed 3.4.0 hooks still inject the binding until then.
- Publish to PyPI, once (trusted publisher or token on the account), then per release: `uv build --no-sources plugin/unharness && uv publish plugin/unharness/dist/*`; after that `uvx unharness` works without the git form.
- Belief not supported: no documented or binary switch removes the identity line (round entry 5); it stays as residue the preamble names.
- One B2 test (Vertex provider) sent a request to Google outside the meta login; noted in `recon/2026-10-23/b2-switch-tests.md`.

## Closing block

- Ended on: origin/main 002db33 (tag v3.5.0), then this records commit on `session/long-run`, fast-forwarded into main.
- State: `manifesto@llm-manifestos` 3.5.0 ships `plugin/unharness` (verbs `prompt`, `stack`, `launch`), `plugin/bin/unharness`, the skill `compile-commitments`, hooks that read `.manifestos.yaml` through the package's config module and stand down under `UNHARNESS=1`; this repo carries `.manifestos.interplay.md` and `.manifestos.commitments.md`.
- Open: PyPI publish (owner); the prior deferrals in `reference/user_deferred_items.md`; a raise-the-bar digest and eval; the three manifestos that fail the Brimstone check.
- First step next: in the owner's shell, `uvx --from "git+https://github.com/ryzhakar/llm-manifestos@v3.5.0#subdirectory=plugin/unharness" unharness prompt | uvx --from "git+https://github.com/ryzhakar/llm-manifestos@v3.5.0#subdirectory=plugin/unharness" unharness launch -- claude@meta` from this repo.
