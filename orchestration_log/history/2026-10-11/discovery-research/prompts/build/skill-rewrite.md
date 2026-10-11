CONSTITUTION BINDING — do this before the task body. Load each element completely from source, run the binding protocol in element 3 (deconstruct, map convergence and tension, activate), write the binding as the first lines of your report, then proceed. You rebind from source on this dispatch.
1. First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md
2. Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml
3. Binding protocol — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md
4. Stop Yapping — /home/user/LLM_MANIFESTOS/manifestos/stop-yapping.md
5. Ethos — /home/user/claude-skills/ETHOS.md
6. Skill-writing standard — /home/user/claude-skills/memento/skills/skill-creation/SKILL.md

ROLE: You are rewriting the manifesto-writing skill so it states the standard the collection actually practices, as commands the writer follows, with nothing deferred to another file.

CONTEXT: Repository /home/user/claude-skills. Another agent is editing hooks in that checkout on another branch, so you work in your own worktree: `git -C /home/user/claude-skills worktree add /home/user/claude-skills-skill -b manifesto-writing-standard main`, then do everything under /home/user/claude-skills-skill. Push that branch (`git push -u origin manifesto-writing-standard`). Never touch /home/user/claude-skills directly. Current skill: /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md. The practiced standard is recorded in /home/user/LLM_MANIFESTOS/orchestration_log/reference/conventions.md lines 21-53, /home/user/LLM_MANIFESTOS/orchestration_log/history/2026-05-01/session.md (Decisions and Failures tables), /home/user/LLM_MANIFESTOS/orchestration_log/history/2026-05-11/session.md (Narrative phases 4-11, Decisions, Failures), /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/verify-axioms.md (the shape of an axiom test), /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/corpus-audit.md (measured register numbers for stop-yapping and postgres), and /home/user/LLM_MANIFESTOS/orchestration_log/history/2026-10-10/manifesto-definition.md sections 5-7 (the convergence spine, as hypotheses; verify each against the logs before stating it).

OWNER DECISIONS (binding; the skill states each as a command, never as rationale):
- The reader is the model. The enemy is the reader's own trained reflex, stated in the reader's mouth, in the first line.
- Register follows enemy type: reflex → contemptuous; framework → declarative; environment → parable. The skill names the three and the test for choosing.
- Boundary yes, escape never: a clause that says what the enemy is not stays; a clause that says when the reader may stop fighting dies. State the test.
- Bindable lines ≥ 70% (a bindable line is a demand checkable at a literal reading; examples and table rows count as demands). At most five axioms, each stated as one sentence. A "Before you ship" self-check section. The text passes its own rules.
- Evidence: declare, never cite. Every figure verified by a reviewer who did not write the text. Forbid any figure a verifier rated UNVERIFIED or CONTRADICTED.
- Length ≤ 1500 words body. Sentences under 20 words; sections under 150; aphorisms under 15.
- Anti-Claude checklist inlined: lexical (delve, nuanced, robust, leverage, tapestry), structural (three-part lists, summary paragraphs, parallel overuse, uniform sentence weight, zero fragments), tonal (performed enthusiasm, hedging, "I'd be happy"), and the rule that a prompt's register sets the output's register.
- Process: oath-bind to this skill and to a register reference before reading substrate; 2-4 sources; write to a fresh path; full rewrite for a register change, never an edit; five unbiased reviewers (accuracy, completeness, boundaries, scope-facts, precision) plus a register reviewer and a maximalist self-pass; the orchestrator edits register, the writer produces structure.
- Frontmatter: title, tagline (≤8 words, imperative or binary, distinct in the collection, re-binds alone), version, theme, description, kind, register, reader; attribution line "After [authors]".
- Keep the current skill's Preserve/Cut/Transform table and its three example transformations; drop every sentence that argues for a rule.

TASK:
1. Measure the current skill: `just tokens manifesto/skills/manifesto-writing/SKILL.md` from the worktree root (read the justfile for the exact recipe; if `just` is absent, use the recipe's command directly).
2. Rewrite SKILL.md in place. Frontmatter: keep `name`; rewrite `description` as trigger phrases plus one line of what it does; no version field. Body in XML lifecycle tags as the skill-writing standard prescribes (read it), each tag holding commands only. Order: bind → read substrate → find the enemy and the reader → choose the register → extract (preserve/cut/transform) → structure → write → self-check → review → ship (frontmatter, attribution). Inline everything; no references to other files except the oath skill by name.
3. Token ceiling: 2,600 tokens by the repo's measure. Measure after writing; compress until under.
4. Run the prompt-eval rubric yourself against the result if the repo holds one at /home/user/claude-skills/prompt-engineering/ (read its skill file; apply its scoring; record the score). 
5. Commit: `feat(manifesto-writing): practiced standard — model reader, register by enemy, bindable floor, self-check`. One commit for the skill file. Then regenerate the plugin README if the generator covers skill descriptions (`just readme` or `python3 generate.py`) and commit `doc(readme): regenerate for manifesto-writing` if it changed. Push `git push -u origin manifesto-writing-standard` with retries (2s, 4s, 8s, 16s).

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/skill-rewrite-report.md

REPORT FORMAT:
(binding lines)
# manifesto-writing rewrite
## Tokens — before, after
## Five core points — the spine you kept most prominent, each with its tag
## Prompt-eval score — if run
## Commits — hash | message
## Open

SCOPE: SKILL.md of manifesto-writing, the README regeneration, nothing else. No attribution lines in commits. Do not touch the oath skill or the hooks.

TOOLS: Read; Edit; Write; Bash; Grep.

End with a 3-sentence summary for a notification: token counts, eval score, push result.
