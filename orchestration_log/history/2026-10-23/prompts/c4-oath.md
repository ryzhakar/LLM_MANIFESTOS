Bind to write-well (skill agent-conduct:write-well), manifesto-writing (skill manifesto:manifesto-writing, whose tone manifesto Raise the Bar is /Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/raise-the-bar.md), lines-spent (/Users/ryzhakar/LLM_MANIFESTOS/plugin/manifestos/lines-spent.md), and the skill memento:skill-creation — show your commitments before working. Non-compliant work is rejected.

ROLE
You write two texts whose wording is the product: the shipped preamble of a compiled system prompt, and the skill /compile-commitments that a session runs to write its interplay and commitments files.

CONTEXT
The spec is the one home of the design: /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/spec-unharness.md; read it whole, above all the sections Purpose, Compiled prompt, Strip set (its residue list), Shipped preamble, and `/compile-commitments`. Your worktree is /Users/ryzhakar/LLM_MANIFESTOS.worktrees/oath on branch feat/unharness-oath; work and commit there only. The owner's reading of the whole prompt: one instruction flow in the agent's own voice, no artificial isolation, no seam that names how the prompt was produced. The commitments format is the oath protocol's paired lines in /Users/ryzhakar/LLM_MANIFESTOS/plugin/skills/manifesto-oath/SKILL.md (sections 3 and 4); the files the skill writes are read by `unharness prompt`, which strips their opening `<stack>` block and inlines the rest verbatim, so the body of each file is exactly what the model will read as its own words.

INPUT FILES
1. The spec above.
2. /Users/ryzhakar/LLM_MANIFESTOS/plugin/skills/manifesto-oath/SKILL.md: the binding protocol (Deep Interplay Analysis, Activate Identity-Mode).
3. /Users/ryzhakar/LLM_MANIFESTOS/plugin/skills/manifesto-writing/SKILL.md and plugin/skills/manifesto-oath/SKILL.md: house examples of skill files; follow memento:skill-creation for the new skill's shape.
4. /Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/binding-long-run.md: a real binding report, for the register of interplay and commitments.

TASK
1. Write plugin/unharness/src/unharness/preamble.md: at most 25 lines, no heading, no tag of its own (the compiler wraps it in <harness>), plain words, the agent's voice (first person or imperative, one voice throughout), covering each residue the spec lists and nothing else. Run the five checks of Raise the Bar and the write-well reread on it.
2. Write plugin/skills/compile-commitments/SKILL.md by memento:skill-creation: frontmatter name `compile-commitments`, description one sentence plus the phrases that trigger it ("/compile-commitments", "compile the commitments", "precompile the oath", a stack change); body in XML tags, each an imperative verb phrase; the procedure: run `unharness stack --config <path>` (the plugin ships `bin/unharness`; outside a session the owner runs `uvx unharness stack`) into a temporary file and read it whole; deconstruct each element to its axioms; map convergence and tension; resolve each tension with an explicit rule and a priority order; write `.manifestos.interplay.md` beside the config, opening with the `<stack>` block copied verbatim, then `<interplay>` ... `</interplay>` holding the analysis in the session's own voice; write `.manifestos.commitments.md` the same way with `<commitments>` ... `</commitments>` holding one "I must ..., and I will ..." and one "I must not ..., and I will not ..." pair per element, in the stack's order; then run `unharness prompt --config <path> > /dev/null` and report its exit; never print the files to the conversation; never paraphrase an element from memory. Include one `<never_do_this>`/`<do_exactly_this>` pair showing a seam to avoid (a commitment that names the file or the tool) against a clean one.
3. Commit each file on feat/unharness-oath, messages `type(scope): subject` of at most ten words, no body, no trailer. Do not push.

OUTPUT PATH
/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-23/reports/c4-oath.md

REPORT FORMAT
# C4 oath
## Commits
## Preamble: line count, the residues covered, the checks run and what they caught
## Skill: tags in order, one line each
## Deviations from the spec with reasons
End the report, and your final message, with a three-sentence summary.

SCOPE
Only the two files named, in your worktree. Do not edit the spec, the oath skill, or any other file; do not push.

TOOLS
Read, Write, Edit, Bash (git), Skill.

PRIME DIRECTIVE
Raise the bar, not the voice: the preamble hands the model the facts it needs to weigh harness text, and the skill leaves the session no decision about shape and every decision about content.
