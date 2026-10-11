CONSTITUTION BINDING — do this before the task body. Load each element completely from source, run the binding protocol in element 3 (deconstruct, map convergence and tension, activate), write the binding as the first lines of your report, then proceed. You rebind from source on this dispatch.
1. First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md
2. Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml
3. Binding protocol — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md
4. TDD — /home/user/claude-skills/dev-discipline/skills/tdd/SKILL.md

ROLE: You are extending the manifesto collection's schema and cleaning its metadata per the owner's decisions.

CONTEXT: Repository /home/user/LLM_MANIFESTOS, branch claude/manifesto-design-discussion-liuuvf. Generation: `just readme` runs generate.py with uv (check `uv --version`; if uv is absent, run `python3 -m pip install --user pyyaml python-frontmatter pydantic jinja2 rich` and `python3 generate.py`). Owner decisions: (1) new optional frontmatter fields: `kind` (manifesto | canon; default manifesto), `register` (contemptuous | declarative | parable | lecture | aphoristic), `reader` (model | human | unspecified); (2) tagline validation: at most 8 words, warn when a tagline duplicates another file's; (3) README shows kind for canon entries and register per entry; (4) zen-of-python.md and cargo-cult-science.md become `kind: canon`; (5) every other file gets register and reader from the judgment table in /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/corpus-audit.md (use its values verbatim; map its register words to the enum; its reader column to model|human|unspecified); (6) themes.yaml loses the three themes with zero files; (7) first-principles.md version becomes 1.0.0; (8) MAINTAINERS_GUIDE's "Patches (don't use; just edit)" wording stays. Commits: single-line conventional, no attribution, atomic: generate.py + README.template.md (schema) in one; frontmatter backfill of the 12 files in one; themes.yaml in one; first-principles version in one; README regeneration in one.

INPUT FILES: /home/user/LLM_MANIFESTOS/generate.py, README.template.md, themes.yaml, justfile, MAINTAINERS_GUIDE.md (Reference section), manifestos/*.md frontmatter (first 8 lines each), the corpus-audit judgment table.

TASK:
1. Write tests first: /home/user/LLM_MANIFESTOS/tests/test_generate.py (pytest or plain assert script runnable with python3) covering: kind default, kind enum rejection, tagline over 8 words rejected, duplicate tagline warning, register and reader enums, backward compatibility of a file with only the five original fields. Run; record red.
2. Implement in generate.py (Pydantic model + warnings) and README.template.md (kind badge for canon, register shown after version). Run tests green. Run the generator; README.md regenerates without errors.
3. Backfill frontmatter per decisions 4–5. Do not touch bodies.
4. themes.yaml: remove design-methodology, ai-instructions, research-protocols.
5. first-principles.md: version "1.0.0".
6. Regenerate README.md; `git diff --stat`.
7. Commit in the atomic order; `git push -u origin claude/manifesto-design-discussion-liuuvf` with retries (2s, 4s, 8s, 16s).

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/collection-schema-report.md

REPORT FORMAT:
(binding lines)
# Collection Schema
## Red / Green — test output before and after
## Backfill table — file | kind | register | reader | source row
## Commits — hash | message | files
## Open

SCOPE: Schema, frontmatter, themes, version, README. No body edits. No MAINTAINERS_GUIDE edits (another agent owns it).

TOOLS: Read; Edit; Write; Bash; Grep.

End with a 3-sentence summary for a notification: tests, files backfilled, push result.
