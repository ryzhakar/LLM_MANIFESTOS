Bind to write-well (skill agent-conduct:write-well) and first-principles (/Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/first-principles.md) — show your commitments before working. Non-compliant work is rejected.

ROLE
You record the facts about the manifesto plugin that a new Python tool and changed hooks must fit.

CONTEXT
Repo /Users/ryzhakar/LLM_MANIFESTOS, branch session/long-run; the plugin manifesto@llm-manifestos 3.4.0 lives in plugin/. A new package, unharness, will live in plugin/unharness/ and read `.manifestos.yaml`, whose `you:` list the plugin's hooks read today. The schema will evolve so that each element states its source type (manifesto, skill, file), and the hooks will stand down when the environment variable UNHARNESS=1 is set.

INPUT FILES
1. /Users/ryzhakar/LLM_MANIFESTOS/plugin/: hooks/*.sh, hooks/*.py, hooks/hooks.json, hooks/templates/, skills/, agents/, references/, tests/, SCHEMA.md, README.md, .claude-plugin/plugin.json.
2. /Users/ryzhakar/LLM_MANIFESTOS/.manifestos.yaml.
3. /Users/ryzhakar/LLM_MANIFESTOS/justfile, generate.py, config.yaml, README.template.md, .claude-plugin/marketplace.json, .gitignore.
4. /Users/ryzhakar/LLM_MANIFESTOS/MAINTAINERS_GUIDE.md: only its sections on the plugin, hooks, release, and versions.
5. /Users/ryzhakar/.claudes/meta/plugins/cache/memento/memento/0.10.0/: bin/memento and how that plugin's Python package is laid out.

TASK
1. Document the `.manifestos.yaml` schema as the parser implements it: every key, element form, `source` form, default, and error, with file:line.
2. Document each hook: event, script, what it prints, the config it reads, the environment variables it reads, how it resolves elements, and the templates it uses, with file:line.
3. Document the tests: framework, run command, and what each covers; run them and report the result.
4. Document validation and release: `claude plugin validate` usage, `just readme`, and every place a version is written.
5. Document how README.md and plugin/README.md are produced, and which sections mention hooks, config, or skills.
6. Document memento's launcher and package layout: pyproject, build backend, entry points.
7. List, with file:line, the places to edit for: (a) a package folder plugin/unharness/; (b) a skill plugin/skills/compile-commitments/; (c) a launcher in plugin/bin/; (d) the evolved schema; (e) a hook stand-down variable.

OUTPUT PATH
/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/a4-repo-facts.md

REPORT FORMAT
# A4 repo facts, one section per task step 1-7. End the report, and your final message, with a three-sentence summary.

SCOPE
Read, and run the tests. Do not edit any file. Do not propose designs; list edit points as locations only.

TOOLS
Read, Grep, Glob, Bash.

PRIME DIRECTIVE
Give file:line for every claim.
