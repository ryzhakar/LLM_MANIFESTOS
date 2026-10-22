Bind to kiss, only-what-it-needs, self-documenting-code, zen-of-python, dry, yagni, lines-spent (each at /Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/<name>.md) and write-well (skill agent-conduct:write-well) — show your commitments before working. Non-compliant work is rejected.

ROLE
You build the core of the Python package unharness, by test-driven development, in its own git worktree.

CONTEXT
The spec is the one home of the design: /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/spec-unharness.md. Read it whole first. Your worktree is /Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness on branch feat/unharness; work and commit there only. Facts about the repo and the current config parser are in /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/a4-repo-facts.md (sections 1 and 7); packaging facts are in a5-packaging.md beside it (uv_build works; a .md inside src/<name>/ ships). Run `uv` and `uvx` as found on PATH. Python 3.11 or later; stdlib only at runtime; pytest for tests. The skill dev-discipline:tdd governs how you write code: one failing test through the surface its callers use, then the code, then refactor.

INPUT FILES
1. The spec above: sections Files in a project, Config schema, Builders, Compiled prompt, Verbs (`prompt` and `stack` only; `launch` is another unit).
2. /Users/ryzhakar/LLM_MANIFESTOS/.manifestos.yaml (a real config: both legacy forms and the skill source form).
3. /Users/ryzhakar/LLM_MANIFESTOS/plugin/hooks/parse_config.py and mini_yaml.py: the parser the hooks use today; the new config module replaces both for the hooks later, so it must accept every form they accept (A4 section 1 lists them).
4. /Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/: the registry; raise-the-bar.md and the skill plugin/skills/manifesto-writing/SKILL.md show ${CLAUDE_PLUGIN_ROOT} references.
5. /Users/ryzhakar/.claudes/meta/plugins/cache/: a real plugin cache for skill resolution tests (read only).

TASK
1. Create plugin/unharness/: pyproject.toml (uv_build, src layout, console script `unharness` -> unharness.cli:main, requires-python >= 3.11, version 3.5.0), src/unharness/ with `config.py` (schema load and element normalization, stdlib YAML subset reader, usable as `python3 config.py <path> --json` so a shell hook can read the stack), `resolve.py` (registry, skill cache, local file; exact errors naming every path tried), `compile.py` (fingerprint block, constitution block, full prompt, staleness check), `cli.py` (verbs `prompt` and `stack`, `--config PATH`, exit 1 with a one-line reason on any failure), tests/.
2. Write tests first for: every config form; resolution of each source type, with a fake login folder built in tmp_path (plugin cache with two versions of one plugin, a user skill); registry default from the highest cached manifesto plugin; frontmatter removal; ${CLAUDE_PLUGIN_ROOT} replacement; the exact prompt layout from the spec; the `<stack>` block and its sha256 lines; staleness (missing file, changed element, reordered elements); the preamble override; and the CLI verbs through subprocess. Keep the preamble as src/unharness/preamble.md with a two-line placeholder; another agent writes its text.
3. Run `uv run --project plugin/unharness pytest -q` until green; run `uvx --from plugin/unharness unharness stack --config /Users/ryzhakar/LLM_MANIFESTOS/.manifestos.yaml` from the worktree root and paste its first 20 lines into your report.
4. Commit in small steps on feat/unharness, messages `type(scope): subject` of at most ten words, no body, no attribution trailer. Do not push.

OUTPUT PATH
/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/reports/c1-core.md

REPORT FORMAT
# C1 core
## Commits (sha, subject)
## Layout (tree of plugin/unharness)
## Behaviors covered by tests (one line each)
## Deviations from the spec, each with its reason
## Open questions for the orchestrator
## Sample output of `unharness stack` (first 20 lines)
End the report, and your final message, with a three-sentence summary.

SCOPE
Only plugin/unharness/ in your worktree. Do not touch hooks, skills, README, or the main checkout; do not implement `launch`; do not push.

TOOLS
Read, Write, Edit, Bash (uv, uvx, pytest, git), Grep, Glob, Skill (dev-discipline:tdd).

PRIME DIRECTIVE
The spec fixes the outcome; you choose the internals. Every line you add is spent: the least code that passes the tests, with no helper that nothing calls.
