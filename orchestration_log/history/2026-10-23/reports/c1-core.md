# C1 core

The core of unharness is built by test-driven development in the worktree `/Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness` on branch `feat/unharness`, with nothing pushed. The suite passes with 31 tests under `uv run --project plugin/unharness pytest -q`. Run from the worktree root, that command collects 52 tests, because it also picks up the repo's other test files, and all pass.

## Commits (sha, subject)

- 27a429a chore(unharness): package skeleton with uv_build
- b6878ec feat(unharness): load the you stack from the config
- 4f997f4 feat(unharness): subagent roles, manifesto_dir, root list
- 3159cca feat(unharness): source forms and file-stem names
- 12a6be0 feat(unharness): trailing comments stay out of values
- 9bd8380 feat(unharness): strict config shapes and the CLAUDE.md fallback
- aba745c feat(unharness): config.py prints the stack as JSON
- 2834ae0 feat(unharness): resolve registry manifestos from the plugin cache
- d46ed2e feat(unharness): resolve plugin skills
- a4fae9b feat(unharness): resolve user skills, files, manifesto_dir
- e24e6d4 feat(unharness): name the element and path when resolution fails
- 0c70b6f feat(unharness): find the login folder
- d0b27c1 feat(unharness): compile the prompt layout
- da95bc7 feat(unharness): the stack view
- b013f6f feat(unharness): stale and missing session files stop the prompt
- 186d487 feat(unharness): the stack verb
- d063926 refactor(unharness): the schema's source types live in config

## Layout (tree of plugin/unharness)

```
plugin/unharness/
  .gitignore
  pyproject.toml          uv_build, src layout, version 3.5.0, script unharness -> unharness.cli:main
  uv.lock
  src/unharness/
    __init__.py
    config.py             schema, YAML subset reader, `python3 config.py <path> --json`
    resolve.py            login folder, registry, skill cache, user skill, local file
    compile.py            stack block, constitution block, prompt, staleness check
    cli.py                verbs prompt and stack
    preamble.md           two-line placeholder
  tests/
    conftest.py           fake login folder: two versions of two plugins, one user skill
    helpers.py
    test_config.py  test_resolve.py  test_compile.py  test_cli.py
```

## Behaviors covered by tests (one line each)

- A bare string and a mapping without source load as registry elements.
- Subagent roles and manifesto_dir load beside the you stack.
- A root list is the you stack.
- Each source type is kept as written, and a file element is named by its stem.
- Null items drop, and an empty file is an empty stack.
- An element with no name and no file source stops the load, naming its place in the list.
- Trailing comments, quoted or not, stay out of values, including after a key that opens a block.
- A non-list you, a non-list role, and a non-mapping subagents stop the load.
- A bare item with a colon stops the load instead of vanishing.
- Without a config file, the Active Manifestos section of CLAUDE.md is the config.
- A missing config names every place it looked.
- `python3 config.py <path> --json` prints the stack as JSON, run by path under `-I`.
- A failing script run prints one line on stderr and exits 1.
- A legacy name resolves in the registry of the highest cached manifesto plugin, with frontmatter removed and `${CLAUDE_PLUGIN_ROOT}` replaced by that plugin folder.
- A plugin skill resolves at the highest version by number, so 1.10.0 beats 1.9.0, with the version folder as plugin root.
- A user skill and a local file, relative to the config folder, resolve and keep the placeholder as written.
- manifesto_dir replaces the cached registry, resolves against the config folder, and is the plugin root; `source: manifesto <name>` reads the same registry.
- An element that does not resolve names itself and the path tried, for the registry, a file, and a skill with no cached plugin.
- An unknown source type is refused, listing the three that exist.
- The login is CLAUDE_CONFIG_DIR, else `.claude` in the home folder.
- The prompt has the exact layout of the spec: harness, constitution with `governs` only where a purpose exists, interplay, commitments.
- The stack view is the stack block, with one name, sha256, and purpose line per element, then the constitution.
- A missing session file stops the prompt and names `/compile-commitments`.
- A session file for another stack names each changed, added, or removed element.
- The same elements in another order are reported as reordered.
- A session file with no stack block is reported.
- The stack verb prints the stack view through a subprocess with a fake login.
- The prompt verb prints the compiled prompt with the shipped preamble, through a subprocess.
- A project preamble file replaces the shipped preamble.
- A failing verb prints one line on stderr, nothing on stdout, and exits 1.

## Deviations from the spec, each with its reason

- **Hash scope.** The sha256 covers the text after frontmatter removal and before the placeholder is replaced. Hashing the replaced text would make committed session files differ from machine to machine and from plugin version to plugin version.
- **Stricter than the hooks.** A flow list in `you`, a non-list role, a bare item with a colon, and a missing config raise a one-line error; the hooks returned an empty stack silently. An empty-string name is also refused. The zen rule that errors never pass silently decided this.
- **Looser than the hooks in one place.** A trailing `# comment` is stripped from a value; the hooks kept it inside the value, which would corrupt a `source:` line.
- **Legacy sources.** A path or URL source, which the hooks pass through unread, loads and prints in the JSON, but fails at resolution naming its source type. The spec says nothing is guessed, so I did not map it to `file`.
- **Names.** Only a file source supplies a default name. A skill or manifesto mapping without a name is refused, as the spec states the default for files alone.
- **Paths tried.** Resolution picks exactly one path per element, so the error names that one path. When no cached plugin matches, it names the glob pattern.
- **Plugin root.** A user skill and a local file have no plugin folder, so `${CLAUDE_PLUGIN_ROOT}` stays as written in them.
- **JSON shape.** `config.py --json` prints one JSON object with `you`, `subagents`, and `manifesto_dir`, each element carrying `name`, `purpose`, and `source`, where the hooks' script printed three lines. The shell side in C3 reads this object.
- **TDD slips.** The prompt verb and the preamble override were written together with the stack verb, so their tests passed on the first run. Some tests were also written two at a time. The red run was read in every other case.

## Open questions for the orchestrator

- Should the preamble and the session files reject an element purpose containing a double quote, which breaks the `governs` attribute? I left it unescaped.
- Should an empty `you` stack stop `prompt` and `stack`? Today both print an empty constitution.
- The sha256 definition above affects the `/compile-commitments` skill and the hook tests; confirm the pre-replacement choice.
- `uv.lock` is committed; say if the repo prefers it ignored.

## Sample output of `unharness stack` (first 20 lines)

Command: `uvx --from plugin/unharness unharness stack --config /Users/ryzhakar/LLM_MANIFESTOS/.manifestos.yaml`, exit 0, 1132 lines in all.

```
<stack>
write-well 8ba8fcf72f8a987e4b6cc8b5ed2636bdb1415363dcaa1071776a727c62fcf93d every sentence of prose, in manifestos, skills, records, commits, and this conversation
manifesto-writing ea51ba55d29bf3f7a8b8c2caf2a9c4906b25b20ddad89ad23de1190a73cfaf86 the tone and shape of every manifesto this repo holds
first-principles 3a6dd008c2a2392a1db5c5200f26e434de5737ed1f2cdf2edca7f9fcf19dd8f8 reasoning about what a manifesto, digest, or hook must do
cargo-cult-science bfde6690242f614ef914c63b57efe7d6ab8f951fe6a8738cf73a22445a574fa6 every eval, judge, gate, and claim that a digest or manifesto works
dry 5dd350b8de9f7dcd91f6c9cf41296d0b9fc2f1055bc72ab8580a7b6ddcb0de84 one home for each piece of knowledge across manifestos, digests, skills, the README, and the plugin
simple-made-easy 8e551cb85c111b167a949a82dcf159453fcad67252f6d4d13daf74649a5fe508 the organisation of the repo, the plugin, and the work itself
lines-spent 7c91ac5cba70ba8dfcdf50f9918e0c5ec70612bf24978b4699c666be6f077be2 the length of every manifesto, digest, skill, and file this session writes or loads
decide-while-away ba2dde6e9f806b9fcb62d34459d6134360bbdb4dc6dd6fef6c4065d4d5db1242 the owner's decisions, settled or queued while the owner is away
</stack>

<constitution>
<write-well governs="every sentence of prose, in manifestos, skills, records, commits, and this conversation">
<write-by-the-rules>
Apply every rule below to every sentence of prose you write, as you write it; never save the rules for a later edit.

Reread each finished draft against the rules in their order, most serious first; never send an unread draft.

Fix every fault the reread finds, at every rank, each tag below being one rank; never leave a minor one.

```

The core is built and green: configuration loading, resolution of every source type, the prompt layout with its staleness checks, and the `prompt` and `stack` verbs all pass their tests on 17 small commits in the feature worktree. The real repo config compiles into a stack of eight elements through `uvx`, and the wheel ships the preamble file. The deviations above and four open questions need the orchestrator's answer before the hooks, the skill, and `launch` build on this.
