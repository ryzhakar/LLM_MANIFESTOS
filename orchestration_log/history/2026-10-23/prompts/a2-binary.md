Bind to write-well (skill agent-conduct:write-well) and first-principles (/Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/first-principles.md) — show your commitments before working. Non-compliant work is rejected.

ROLE
You extract from the installed Claude Code binary every environment variable, settings key, and literal text that governs what the harness injects into a model request.

CONTEXT
Claude Code 2.1.308 is a Bun-compiled Mach-O at /Users/ryzhakar/.local/bin/claude; resolve links with `readlink -f` and check ~/.local/share/claude/versions/. Its JavaScript is embedded and minified; follow string literals, not identifiers. We need: environment variable names; settings keys; both identity-line texts and the code that chooses between them or omits them; the texts of system reminders (task-list nudges, file-changed notes, "The user hasn't heard from you in a while", the skill list header, the agent list header, the line that introduces CLAUDE.md, the git status context, the user email context, output style text, auto memory text); and the condition that gates each.

INPUT FILES
1. The binary above.
2. /Users/ryzhakar/Downloads/claude-cli-custom-system-prompt-reference.md, for hypotheses only.

TASK
1. Run `strings -n 8` on the binary into /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/a2/strings.txt.
2. List every unique environment variable name the code reads (CLAUDE_CODE_*, CLAUDE_*, DISABLE_*, ANTHROPIC_*, OTEL_*); save the list to /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/a2/env-vars.txt.
3. For each identity-line text, extract about 1500 characters around it and state the gating conditions (entrypoint, flags, environment, auth method, model).
4. For each reminder text named above, find it, extract the surrounding code, and name the variable or setting that gates it.
5. Map each injected text to the switch that removes it, or "none found", with a code excerpt of at most 20 lines as evidence.

OUTPUT PATH
/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/a2-binary-switches.md

REPORT FORMAT
# A2 binary switches
## Environment variables (full list, grouped by prefix)
## Identity line: texts, gating logic, excerpts, removal switch if any
## Reminders: | text | gate | switch | excerpt ref |
## Settings keys bearing on injected text
## Unknowns
End the report, and your final message, with a three-sentence summary.

SCOPE
Read the binary. Do not run claude, patch anything, or write outside /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23. Mark every inference as inference.

TOOLS
Bash (strings; use /usr/bin/grep or rg with absolute paths, since `grep` in this shell is a function that skips ignored files), Write.

PRIME DIRECTIVE
A code excerpt is evidence; a name alone is not.
