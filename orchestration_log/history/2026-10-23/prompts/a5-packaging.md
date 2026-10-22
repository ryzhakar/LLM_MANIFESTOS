Bind to write-well (skill agent-conduct:write-well) and first-principles (/Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/first-principles.md) — show your commitments before working. Non-compliant work is rejected.

ROLE
You establish exactly how a Python command-line tool shipped inside this repo runs under uvx, from git now and from PyPI later.

CONTEXT
The package unharness (its PyPI name is free today) will live at plugin/unharness/ in the public GitHub repo ryzhakar/llm-manifestos, tagged vX.Y.Z (next v3.5.0). The owner believes uvx has a git shorthand. Here `uv` and `uvx` resolve to shims in /Users/ryzhakar/pp/offline-kit/shim/. The memento plugin runs its tool as `uvx --from git+https://github.com/ryzhakar/memento@v${VERSION} memento`.

INPUT FILES
1. uv docs, https://docs.astral.sh/uv/: the tools guide and concept, the uvx / uv tool run CLI reference, git sources, and the publishing guide.
2. /Users/ryzhakar/pp/offline-kit/shim/uv and /Users/ryzhakar/pp/offline-kit/shim/uvx.
3. /Users/ryzhakar/.claudes/meta/plugins/cache/memento/memento/0.10.0/, for the house pattern.

TASK
1. Read the shims; state what they wrap and how they behave offline.
2. From the uv docs, list every form uvx accepts for a package from git (full URL, @tag, #subdirectory=, and any shorthand such as github: or gh:), with quotes; state plainly whether a shorthand exists.
3. Build a throwaway package in /tmp/uh-a5/pkg (src layout, console script uh-a5, one .md data file inside the package that the script prints). Run it with `uvx --from /tmp/uh-a5/pkg uh-a5`; then from a local git repo with `uvx --from "git+file:///tmp/uh-a5/repo@v0.1.0#subdirectory=pkg" uh-a5`. Report the commands, the outputs, and which build backend works here (uv_build or hatchling).
4. State the PyPI publish steps with uv (uv build, uv publish, token or trusted publishing), with quotes: what the owner does once, and what per release.
5. State whether the backend includes the package's .md file by default, and how to include it otherwise.

OUTPUT PATH
/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/a5-packaging.md

REPORT FORMAT
# A5 packaging
## Shims
## uvx git forms (shorthand: yes or no, with quotes)
## Local tests: commands and outputs
## Publish steps
## Package data
## Exact working invocations: git tag form, and PyPI form
End the report, and your final message, with a three-sentence summary.

SCOPE
Experiment only under /tmp/uh-a5. Do not publish, push, or edit the repo.

TOOLS
WebFetch, Bash, Write.

PRIME DIRECTIVE
A command you ran, with its output, outranks the docs; the docs outrank memory.
