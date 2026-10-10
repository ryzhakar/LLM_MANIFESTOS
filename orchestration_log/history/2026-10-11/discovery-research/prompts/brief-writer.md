Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it, with two more elements loaded and bound the same way:
4. manifesto-writing skill — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md
5. Agent dispatch rule — the "Agent dispatch" section of /home/user/claude-skills/CLAUDE.md

ROLE: You are authoring the shared research brief and the dispatch roster that every later research agent in this project reads as its instructions.

CONTEXT: An orchestrator is about to run a research tree on the question below. Sources will arrive as a user-supplied list written to /home/user/LLM_MANIFESTOS/research/manifesto-craft/sources.md (not yet present). Three ground-truth audits are running now and will land in /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/ as corpus-audit.md, doctrine-audit.md, runtime-audit.md. Agents cannot read skill files from the orchestrator's context; everything they need must be in the brief.

THE RESEARCH QUESTION (verbatim; carry it into the brief unchanged):
"Based on both projects, how does a new manifesto enter the collection and how does it function once there? What makes a manifesto functionally and aesthetically effective as a behavioral constitution for a language model? What is a good one; what constitutes a bad one?"

INPUT FILES (read each in full):
1. /root/.claude/plugins/synced/8340b9b5-4d3a-4099-958d-7dcb0a0aed42_8d6d5cd5-db00-47f0-898f-d48cbd3ed2b1/orchestration/skills/research-tree/SKILL.md — the tier system, prime directive, prompt templates, report templates
2. /root/.claude/plugins/synced/8340b9b5-4d3a-4099-958d-7dcb0a0aed42_8d6d5cd5-db00-47f0-898f-d48cbd3ed2b1/orchestration/skills/agentic-delegation/SKILL.md — the nine-section prompt rule and model tiers
3. /home/user/claude-skills/orchestration_log/history/2026-10-05/briefs/preamble.md — a prior binding preamble, as a form example
4. /home/user/LLM_MANIFESTOS/orchestration_log/history/2026-10-10/manifesto-definition.md — the orchestrator's preparation synthesis; take from it the need-categories and the list of primary files; treat its sections 5–8 as hypotheses to test, never as findings
5. /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md — the binding block in force

TASK:
1. Write BRIEF.md with these sections, in this order:
   a. Binding preamble — the block from input 5 extended with element 4 (manifesto-writing) for surveyors and verifiers; the synthesizer additionally binds the manifesto-oath skill as element 3 already does.
   b. The research question, verbatim.
   c. Need-categories — six, one per decision the design discussion must make: entry-gate (candidacy, species, provenance, attribution); binding-function (axioms, bindable lines, composition with sibling manifestos, tagline as drift atom); reader-register (whom the text addresses, voice, when contempt versus declarative versus parable); form-aesthetics (skeleton, rhythm, length, devices: enemy, binary, table, choice, aphorism); boundary-evidence (exceptions versus escape clauses, declare versus cite, accuracy); failure-modes (what a bad manifesto is and the checks that detect it). For each: the decision it serves, five to eight questions the surveyor must answer from sources, and the slug of its report file.
   d. Prime directive adapted to this domain — primary source means the original text of a manifesto, essay, speech, paper, or the project file; a claim about human readers is not a claim about a language model and must be labelled; a claim about instruction-following must cite the study or the project log that measured it; rhetoric described in secondary commentary is unverified until quoted from the primary text.
   e. Report templates — survey report, verification report, contradiction-resolution report, synthesis report — adapted from input 1 to this domain. Replace the adopt/evaluate/skip scale with: RULE (evidence supports stating it as a rule for this collection), CANDIDATE (plausible, needs a test or an exemplar), REJECT (contradicted or out of scope). Keep VERIFIED/UNVERIFIED/CONTRADICTED for claims. Every template requires file:line or URL citations and the three binding lines at the top.
   f. Primary files — the list of project files surveyors may cite as ground truth, taken from input 4 section 1, plus the three Tier 0 report paths.
   g. Scope boundaries — what surveyors do and do not do; no proposals, no rewriting of any manifesto, no edits under either project.
2. Write DISPATCH.md: a roster for tiers 1 through 5 as a table — tier | agent | model (haiku, sonnet, opus per input 2's rules) | inputs (paths; sources.md where relevant) | output path | blocked by. Tier 1: one index parser over sources.md. Tier 2: six surveyors, one per need-category, plus one breadth expander. Tier 3: verifiers to be added by the orchestrator per finding; give the row template. Tier 4: resolver row template. Tier 5: one synthesizer. Add under the table the exact three-line launch prompt the orchestrator sends per agent: "Read {BRIEF path} for instructions. Your category/target: {X}. Write to {output path}."
3. Keep BRIEF.md under 450 lines and DISPATCH.md under 80 lines. Strunk governs the prose.

OUTPUT PATHS:
- /home/user/LLM_MANIFESTOS/research/manifesto-craft/BRIEF.md
- /home/user/LLM_MANIFESTOS/research/manifesto-craft/DISPATCH.md

SCOPE: Author instructions. Do not research the question. Do not read the manifesto bodies. Do not modify any file outside the two output paths.

TOOLS: Read for inputs; Write for the two outputs.

End with a 3-sentence summary for a notification: the two paths written, line counts, the one place you departed from input 1's templates and why.
