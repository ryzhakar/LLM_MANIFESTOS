Bind to write-well (skill agent-conduct:write-well) and first-principles (/Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/first-principles.md) — show your commitments before working. Non-compliant work is rejected.

ROLE
You survey Anthropic's official Claude Code documentation for every switch that removes or changes text Claude Code puts into a model request.

CONTEXT
Claude Code 2.1.308 on macOS. We launch it with a fully custom system prompt (`--system-prompt-file`) and must strip every other piece of instructional text the harness injects: default prompt sections, the identity line, system reminders, CLAUDE.md, git instructions, commit attribution, task-list nudges, file-changed notes, output style text, auto memory text, MCP server instructions, hook framing, and notices such as "The user hasn't heard from you in a while". The tool list, skill list, and agent list must stay. The owner is certain a documented switch removes the identity line ("You are a Claude agent, built on Anthropic's Claude Agent SDK." or "You are Claude Code, Anthropic's official CLI for Claude ..."); find it, or show which pages are silent. The docs index is https://code.claude.com/docs/llms.txt.

INPUT FILES
1. /Users/ryzhakar/Downloads/claude-cli-custom-system-prompt-reference.md: a third-party reference verified on 2.1.308; treat each claim as a hypothesis to confirm against the docs.
2. https://code.claude.com/docs/llms.txt and the pages it lists. Start with: agent-sdk/modifying-system-prompts, env-vars, settings (and any settings reference page), cli-reference, headless (bare mode), output-styles, memory, hooks, monitoring-usage, llm-gateway-protocol, agent-sdk/claude-code-features.

TASK
1. Fetch llms.txt. List every page bearing on system prompts, reminders, settings, environment variables, CLI flags, bare or simple mode, memory, output styles, hook output, attribution, git instructions, or attachments.
2. Fetch each such page in its .md form and save its text under /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/docs/<slug>.md.
3. From the saved pages, extract every switch (CLI flag, environment variable, settings key, frontmatter key) that adds, removes, or changes text the model receives: exact name, values, documented effect, minimum version if stated, source URL, and a verbatim quote of at most two sentences.
4. Answer each: (a) any documented way to remove or replace the identity line; (b) switches for task-list nudges, file-changed notes, and the skill list, and whether any switch drops one without the others; (c) output style text under a custom prompt; (d) auto memory text; (e) MCP server instructions; (f) the effects of `--bare`, `CLAUDE_CODE_SIMPLE`, and `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT`, above all on skills, agents, hooks, plugins, and login; (g) exact usage of `OTEL_LOG_RAW_API_BODIES` and any variables it needs; (h) whether settings `env` applies to variables read at startup; (i) `disableAllHooks`; (j) `--system-prompt-snapshot` and resume; (k) any other list of system reminders.

OUTPUT PATH
/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/a1-docs-switches.md

REPORT FORMAT
# A1 docs switches
## Pages read (URL, saved path)
## Switch table: | switch | kind | values | documented effect on model-visible text | version | URL | quote |
## Answers (a)-(k): each an answer with URL and quote, or "docs silent" with the pages checked
## Contradictions with the reference file: claim, what the docs say, URL
End the report, and your final message, with a three-sentence summary.

SCOPE
Read and quote the docs. Do not run claude, edit any repo file, or propose designs. Mark every inference as inference.

TOOLS
WebFetch for pages (for example https://code.claude.com/docs/en/env-vars.md); Write to save pages and the report; Bash for mkdir -p.

PRIME DIRECTIVE
Documented text outranks memory and third-party claims; quote it.
