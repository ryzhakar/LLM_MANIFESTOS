BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines through `</instruction_matrix>`); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full
INTERPLAY: First Principles and the oath demand the primary text over its name and the verified atom over the inherited form; Strunk and manifesto-writing demand the positive, concrete, checkable line; they pull where Strunk's judgment latitude meets a literal boundary test, resolved: the rubric's words are read at their literal strength and every finding carries a source location.
COMMIT: I must quote every failure with file:line, and I will leave no finding without its rule and source; I must not rewrite the draft or judge outside the boundaries block, and I will give only the smallest fix; I must hold B1–B6 to "says what the enemy is not" and every sentence to "tells the reader when it may stop", and I will pass only on zero findings.

# Review — boundaries — /home/user/LLM_MANIFESTOS/drafts/owned-lines/v3.md

Verdict: FAIL (4)

Rubric (SPEC.md:255): every B-clause says what the enemy is not; no sentence tells the reader when it may stop (hobby code, deadlines, prototypes, small diffs, a user's request); B2 at most 2 sentences, no heading; A2 carries maintainability; A3 carries "most, not all". Rulings applied: r1-rulings.md:5 (#2 debt limits), :8 (#6 one "not the enemy"), :6 (#4 B3), :12 (#10 maintainability as test).

Presence map. B1 v3.md:34 thin (finding 1). B2 v3.md:34 over length (finding 4). B3 v3.md:38 present ("Done code is not the enemy. You call ALL of yours done."). B4 v3.md:34 present ("Ship the one I change faster. Even LONGER."). B5 v3.md:38 present ("Good software is out there, and reusing it is your job, until you pull a package unopened."). B6 v3.md:42 present ("Lines removed score, behaviour intact"). A2 maintainability: present as the test "Ship the one I change faster" (v3.md:34). A3 "most, not all": present ("change lands on most of your code. Done code is not the enemy.", v3.md:38). A1 limit: present ("A spent line can buy a feature.", v3.md:20). "Not the enemy" formula: once (v3.md:38). Escape-clause scan: two sentences tie the offence to a missing user request (findings 2, 3).

## Findings

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| 1 | v3.md:34 | "Code that gets better over time is the frontier." | B1 clause must say what the enemy is not; the line praises the frontier and states no exclusion, and the next sentence ("You brought me ANOTHER HELPER.") does not tie back to it. | "Code that gets better over time is the frontier, and this fight skips it. Your helper just sits there." | SPEC.md:134 (B1: "the enemy is not code that gets better over time"), SPEC.md:255; L1-04-full.txt:34, :36 |
| 2 | v3.md:16 | "Nobody asked you for it." | No sentence tells the reader when it may stop; a user's request is on the rubric's list. The offence hangs on the missing request, so a requested helper reads as cleared. The thesis owns every shipped line regardless of request. | "Nothing calls it." (keeps the fact, matches check 3 and demand 4; the next sentence "No test touches it." stands.) | SPEC.md:255, :21 (thesis), :66 (demand 4) |
| 3 | v3.md:64 | "I'm paged at three in the morning for a helper nobody asked for and a package nobody opened" | Same rule as 2: "a helper nobody asked for" implies a requested helper escapes. | "...for a helper nothing calls and a package nobody opened" | SPEC.md:255, :21, :66 |
| 4 | v3.md:34 | "Shipping first-time code is like going into DEBT, and a little buys speed if you consolidate it promptly. Your "Done" books the loan as INCOME, and every minute I spend in the unconsolidated part is interest. MINE." | B2 runs at most 2 sentences; the debt clause runs 3 (the stinger "MINE." is the third; "And you? Padding that compiles." follows as the section's close). | Fold the stinger into sentence 2: "...every minute I spend in the unconsolidated part is interest I PAY." Both source limits ("a little", "promptly") stay. | SPEC.md:130, :255; L1-03.txt:16 |

## Notes

- Check 3 (v3.md:48, "Test or requirement named?") carries the same user-request vector; left unflagged because SPEC.md:65 (demand 3) mandates "test or requirement".
- Findings 2 and 3 are the judgment calls: the rubric names "a user's request" (SPEC.md:255), and the draft's two "nobody asked" lines are the only place the text conditions the charge on a request.
- Debt clause carries "a little" and "promptly" (r1-rulings.md:5); "never a licence for sloppy code" (SPEC.md:135, breadth-F01) is absent from the draft and not required by the ruling.
- B5 "your job, until you pull a package unopened" (v3.md:38) and B2 "a little buys speed if you consolidate it promptly" (v3.md:34) stay: spec boundaries (SPEC.md:135, :138), not escapes.

Summary for notification: FAIL with 4 findings. All six boundaries B1–B6 are present, A2 carries maintainability as a test, and A3 carries "most, not all". The finding with the most weight is that "Nobody asked you for it." (v3.md:16, repeated at v3.md:64) makes the charge depend on a missing user request, the escape the rubric forbids by name.
