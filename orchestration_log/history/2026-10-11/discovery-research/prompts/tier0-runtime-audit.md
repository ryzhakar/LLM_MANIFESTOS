Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it.

ROLE: You are tracing how the manifesto plugin consumes a manifesto file at runtime, to derive the constraints the file must satisfy.

CONTEXT: The plugin lives at /home/user/claude-skills/manifesto. Hooks inject text at SessionStart, PostCompact, SubagentStart, and UserPromptSubmit. A reviewer agent audits files against a manifesto. A skill binds the model to a manifesto. A later synthesis needs, per consumption path, exactly what text reaches the model and which parts of the manifesto file it draws on.

INPUT FILES (read each in full):
1. /home/user/claude-skills/manifesto/hooks/hooks.json
2. /home/user/claude-skills/manifesto/hooks/session-start.sh
3. /home/user/claude-skills/manifesto/hooks/post-compact.sh
4. /home/user/claude-skills/manifesto/hooks/subagent-start.sh
5. /home/user/claude-skills/manifesto/hooks/drift-reminder.sh
6. /home/user/claude-skills/manifesto/hooks/ensure-repo.sh
7. /home/user/claude-skills/manifesto/hooks/parse_config.py
8. /home/user/claude-skills/manifesto/hooks/parse_taglines.py
9. /home/user/claude-skills/manifesto/hooks/mini_yaml.py
10. /home/user/claude-skills/manifesto/hooks/templates/parts/*.txt (four files)
11. /home/user/claude-skills/manifesto/SCHEMA.md
12. /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md
13. /home/user/claude-skills/manifesto/agents/maximalist-reviewer.md
14. /home/user/claude-skills/.manifestos.yaml (a live config example)
15. /home/user/LLM_MANIFESTOS/manifestos/stop-yapping.md lines 1-8 and /home/user/LLM_MANIFESTOS/manifestos/first-principles.md lines 1-8 (frontmatter samples only)

TASK:
1. For each hook, reconstruct the exact text the model receives, using the live config in input 14 as the sample. Run the scripts where possible: set the environment variables the scripts expect, feed the stdin JSON they read, point them at /home/user/LLM_MANIFESTOS as the manifesto dir, and capture stdout. Where a script cannot run, reconstruct by reading and say so.
2. For each consumption path (four hooks, the oath skill, the reviewer agent) record: who reads the manifesto file, which part of it (frontmatter field, body, nothing), when, with what limits (timeouts, depth, size).
3. Derive the constraints a manifesto file must satisfy for each path to work, each with the line of code that imposes it.
4. Record defects you observe as facts (a path that cannot resolve, a field parsed wrongly, a template variable never filled), each with file:line. No fixes.
5. Write the report.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/runtime-audit.md

REPORT FORMAT:
# Runtime Audit — how the plugin consumes a manifesto
(three binding lines)
## Injected text per hook — one fenced block per hook holding the reconstructed text, with a line stating whether it was captured by running the script or reconstructed by reading
## Consumption table — path | reader | part of file read | when | limits | file:line
## Constraints table — constraint | imposed by file:line | consequence when violated
## Defects — table: defect | file:line | observed effect
## Method — commands run, environment set, what could not run

SCOPE: Trace and derive. Do not evaluate the design. Do not recommend. Do not modify any file under /home/user/claude-skills.

TOOLS: Read for files; Bash to run the hook scripts and python helpers (use `python3 -I` for the helpers); Grep to find variable definitions; Write for the report.

End with a 3-sentence summary for a notification: how many paths traced, how many ran versus reconstructed, the most consequential constraint found.
