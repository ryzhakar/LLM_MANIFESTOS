BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines through `</instruction_matrix>`); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full
INTERPLAY: First Principles and manifesto-writing converge on the verified boundary (keep what the enemy is not, cut what releases the reader), while Strunk's judgment latitude and positive-form rule pull against a flat "never" on every conditional; resolved: a clause naming a class of code is a boundary, a clause naming a circumstance that releases the reader is an escape, and every verdict carries a file:line quote.
COMMIT: I must test every B-clause and every sentence of the draft against the Boundaries block at its literal reading, and I will quote the draft line for each failure; I must not rewrite the draft or judge outside the rubric, and I will report located facts only.

# Review — boundaries — v4.md
Verdict: PASS

## Findings

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| — | — | none | — | — | — |

## Notes
- B1-B6 present (practiced). B1 v4.md:34 "Code that gets better over time is the frontier and this fight skips it." B2 :34 two sentences, no heading, carries "a little", "promptly", "consolidate" (L1-03.txt:16). B3 :38 "Done code is not the enemy. You call ALL of yours done when change lands on most of it." (L1-04-full.txt:26; L2-05.txt:91). B4 :34 "Same tests? Ship the one I change faster. Even LONGER." (L1-06.txt:30). B5 :38 "Good software is out there. Open it, then reuse it." (L2-05.txt:195). B6 :42 "Lines removed score, behaviour intact." (L1-06.txt:28).
- A2 carries maintainability as the change-speed test (:34; rulings 10, 21). A3 carries "most, not all" (:38; ruling 4). "not the enemy" appears once (:38; ruling 6). Grep for user, request, small, prototype, hobby, deadline, unless, except found no release clause.
- Conditionals :34 "if you consolidate it promptly", :50 "or none stated", :56 "touching untrusted input" restate SPEC §9 B2 and §6 demands 6, 14 as limits; none names a circumstance that releases the reader.
- Unscored: B3 reuses the enemy's quoted word "Done" (:14, :16, :34, :64) for the exempt class (:38); the limit sentence follows in the same line. Check 3 (:48) scopes to "New function or file"; SPEC §6 demand 3 reads "every addition beyond the minimum"; ruling 10 permits the observable definition.
