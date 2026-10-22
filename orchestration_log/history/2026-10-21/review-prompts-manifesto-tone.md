# Review prompts for the tone-of-voice rulebook

## Review 1: write-well, maximal

Agent: manifesto:maximalist-reviewer.

Bind to write-well through the skill `manifesto:manifesto-oath`, its source the skill `agent-conduct:write-well`; show your commitments before working, naming the lines you read and whether any tool output was capped.

Review these two files against write-well at its strongest literal reading:
- /Users/ryzhakar/LLM_MANIFESTOS/plugin/rulebooks/tone-of-voice.md (whole file)
- /Users/ryzhakar/LLM_MANIFESTOS/plugin/skills/manifesto-writing/SKILL.md (only the lines `git -C /Users/ryzhakar/LLM_MANIFESTOS diff main -- plugin/skills/manifesto-writing/SKILL.md` shows as added)

Quoted source text, table cells that are not sentences, and headings are out of scope. Write the report to /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-21/reviews/write-well.md: one row per violation with file, line, the rule, the text, and a compliant rewrite. End with the count of violations. Run no git command that writes, and edit no reviewed file.

## Review 2: the rulebook against its own checks and its evidence

Agent: manifesto:maximalist-reviewer.

Bind to cargo-cult-science through the skill `manifesto:manifesto-oath`; show your commitments before working, naming the lines you read and whether any tool output was capped.

Read in full:
- /Users/ryzhakar/LLM_MANIFESTOS/plugin/rulebooks/tone-of-voice.md
- /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-21/elevation-stack/handover/elevation-stack-handover.md (§6 seeds, §4.3 checks, §7 worked example)
- /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-21/elevation-stack/research/seed-basis.md
- /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-21/elevation-stack/research/model-readers.md

Find, at the strictest reading: every rule stated more strongly than seed-basis.md allows; every seed S01–S37 the rulebook drops or changes in meaning; every rule with no seed behind it; every sentence of the rulebook that fails one of its own five checks or its two closing checks; and every claim in its evidence section that seed-basis.md, model-readers.md, or the handover does not support. Write the report to /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-21/elevation-stack/reviews/fidelity.md (a local folder, never committed, since it quotes the unpublished stack): one row per finding with the rulebook line, the finding, its evidence (file and line), and a compliant rewrite. End with the count of findings. Run no git command that writes, and edit no reviewed file.
