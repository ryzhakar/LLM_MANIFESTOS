Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/build/_binding-writer.md first and obey it.

ROLE: You are writing the specification for one new manifesto, from the owner's decisions and the discovery research, so that a writer can produce it without one open decision.

OWNER DECISIONS (binding; quote them into the spec unchanged):
- One manifesto. Axis: quantity and ownership. Core: every shipped line is owned and paid for, typed or pulled. Two distinctions crossed: lines spent versus lines produced (Dijkstra, VERIFIED axiom S1); code owned versus code installed (Cox). The debt-repaid-by-consolidation idea (Cunningham) is a boundary clause inside it, not a section of equal weight.
- Enemy: counting output as progress. For the model reader it is one reflex with two faces: "I added a helper" and "I'll pull in a library for that." The enemy sentence opens the manifesto, in the reader's own mouth.
- Reader: the model. Register: contemptuous, in the voice of stop-yapping.md. Length ceiling 1500 words, body only. Five axioms at most. Bindable lines at least 70%. A "Before you ship" self-check section. The text passes its own rules. Ends with an A/B choice and "Pick."
- Boundary yes, escape never. A clause saying what the enemy is not stays (code that gets better over time is not the enemy; debt taken and repaid is not the enemy). A clause saying when the reader may stop fighting dies.
- Evidence declared flat, never cited, every figure verified in discovery/evidence.md or discovery/breadth.md as VERIFIED. Forbidden: "liability, not asset" as a claim (CONTRADICTED); Cox's Equifax date and Chrome 2008 extension claim; any figure rated UNVERIFIED.
- Theme: software-engineering. Title, tagline, description: writer's choice; tagline at most 8 words, imperative or binary, distinct from every existing tagline (list them in the spec from the overlap audit). Attribution line mandatory: "After" followed by the source authors.
- The four "Delete Code" rows of kiss.md move into this manifesto (kiss.md:157-163 per discovery/stack-options.md); the spec quotes them and tells the writer to absorb their content.

INPUT FILES (read in full unless a range is given):
1. /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/candidates.md
2. /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/verify-axioms.md
3. /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/evidence.md — the rated statements and every row marked VERIFIED
4. /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/breadth.md — Q5 (model-written code) and the counter-texts table
5. /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/demands.md — the bindable rows (grep "bindable") 
6. /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/stack-options.md — the kiss.md rows under FP-A and the O2a option
7. /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/corpus-audit.md — the metrics rows for stop-yapping and postgres (register targets) and the judgment table
8. /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/collection-overlap-audit.md — the Titles and taglines table and the Enemies table
9. /home/user/LLM_MANIFESTOS/orchestration_log/reference/conventions.md lines 36-53 (writing lessons) and /home/user/LLM_MANIFESTOS/orchestration_log/history/2026-05-11/session.md lines 24-36 (anti-Claude tells, register analysis)
10. Primary texts, whole: /home/user/LLM_MANIFESTOS/resources/2026-10-11-code-liability-and-dependencies/primary/L1-02.txt (Dijkstra), L1-04-full.txt (Skrenta), L1-01.txt (Hertzfeld), L1-03.txt (Cunningham), L2-05.txt (Cox)

TASK:
1. Write the spec with these sections, in order: Owner decisions (verbatim); Thesis in one sentence; Enemy sentence candidates (three, each in the reader's mouth); Distinctions (the two crossings, with the source quote for each, file:line); Axioms (at most five; each marked VERIFIED or QUALIFIED with its limit verbatim from verify-axioms.md; S1 and S6 required); Bindable demands (10–20, each one checkable sentence, each traced to a demands.md row or a primary line); Evidence to declare (table: figure | exact wording allowed | source ID and line | verdict); Evidence forbidden (table); Boundary clauses (what the enemy is not, each with its source); Absorbed from kiss (the four rows quoted, and what the writer must carry); Structure skeleton (sections in order with a word budget each, total ≤1500); Register targets (numbers from corpus-audit for stop-yapping: second-person per 1000 words, fragments per 1000, ALL-CAPS per 1000, percent imperative, max sentence words; and the anti-Claude tells as a checklist of ten lines); Reader and voice rules (every "you" is the model; identity attacks on the reflex, never on a human; profanity at most three, at peaks); Frontmatter (fields, theme, tagline rules, existing taglines to avoid, attribution line text); Reviewer rubric (one block per reviewer: accuracy, completeness, boundaries, scope-facts, precision, register, maximalist self-pass — each with its pass condition); Out of scope.
2. Every demand, figure, and boundary carries a source location. No invented facts.
3. Keep the spec under 350 lines.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/drafts/owned-lines/SPEC.md

SCOPE: Specify. Do not draft any manifesto prose, no sample paragraphs, no title proposals. Do not edit any file but the output.

TOOLS: Read; Grep; Write.

End with a 3-sentence summary for a notification: axiom count and verdicts, declarable figure count, the one decision you could not close from the inputs (or "none").
