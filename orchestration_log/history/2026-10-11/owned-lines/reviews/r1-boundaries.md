BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full.
INTERPLAY: All four demand the verified source over the inherited claim and the command over the hedge; the skill's "boundary yes, escape never" meets First Principles' refusal to inherit a convention unverified and Strunk's latitude to deviate; resolved: a clause passes as boundary only when it names what the enemy is not and a source line backs it, and Strunk's latitude grants no exit.
COMMIT: I must test each caveat as boundary or escape at its literal reading, and I will quote the draft line for every failure; I must not rewrite the draft or judge outside the boundaries rubric, and I will leave the draft untouched; I must give every fix its source line, and I will leave no finding without one.

# Review — boundaries — v1.md
Verdict: FAIL (2)

Rubric (SPEC §15, Boundaries): every B-clause says what the enemy is not; no sentence tells the reader when it may stop (hobby code, deadlines, prototypes, small diffs, a user's request); B2 at most 2 sentences, no heading; A2 carries maintainability; A3 carries "most, not all"; pass = B1–B6 present, zero escape clauses.

## Findings

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| 1 | v1.md:30 (B2) | "Debt taken and repaid is not the enemy: first-time code shipped and then consolidated. Booking your unpaid debt as progress is." | Zero escape clauses; carry the limit as the substrate states it (skill:70, :72). "Repaid" has no deadline: "I will consolidate later" lets any shipped prototype or deadline cut pass as debt. The source limit is "promptly". Sentence count (2) and heading (none) pass. | "Debt taken and repaid promptly is not the enemy: first-time code shipped and then consolidated. Booking your unpaid debt as progress is." | L1-03.txt:16 "A little debt speeds development so long as it is paid back promptly with a rewrite."; discovery/verify-axioms.md:160 (limits: repay "promptly"); SPEC §9 B2. Doctrine. |
| 2 | v1.md:48 (B3) | "Upkeep falls on most code, not all: some code is done." | Every B-clause says what the enemy is not. This clause names no enemy; it limits the upkeep claim. It also leaves the reader to rule which of its own lines are "done", so "done" becomes the exit from the charge. "Most, not all" itself is present and passes. | "Done code is not the enemy: upkeep falls on most code, not all. You treat all yours as done." | L2-05.txt:91 "some code really is “done.”"; L1-04-full.txt:26 "We act like all code is like this but most of the interesting parts of the system really aren't."; SPEC §9 B3 (the reflex assumes all its code is done). Doctrine. |

Clause audit, no finding: B1 v1.md:34 "neither is code that gets better over time" (L1-04-full.txt:34, verbatim) passes. B4 v1.md:34 "More lines that read easier are not the enemy" passes. B5 v1.md:61 "Vetted reuse is not the enemy" passes; the next lines keep the charge ("NEVER the debugging", one wrapper). B6 v1.md:67 "Lines you remove with behaviour intact may count. That is not the enemy." passes; proof is required in the next sentence. A2 maintainability v1.md:34 "Maintainability wins EVERY tie." present. Placement: B2 in the A1 section, B1 and B4 in A2, B3 and B5 in A3, B6 in A4; none holds a section or heading of its own.

## Numbers
Not run: register reviewer only.

## Notes
- Escape scan: grep for hobby, prototype, deadline, small, user, request, unless, except returns zero hits in the body; every conditional ("Untrusted input?", "Upgrade:", "Copied function:", "New package:") scopes a demand to its event and releases nothing.
- v1.md:24 "Your spent line may buy value. It may buy speed." passes: SPEC §5 A1 requires it, and "Call it produced and you booked a LIE" keeps the spent booking.
- v1.md:38, :69, :77 ("requirement", "state that none exist", "say none") pass: each is a duty to name, not an exit from the enemy; SPEC §6 demands 3 and 6 fix the wording.
- B1 and B3 both let the reader classify its own code (gets better over time; done); SPEC §9 mandates both; only B3 fails, on form and on the missing reflex half.
- Not counted: breadth-F01 guard ("never in favor of writing code poorly", SPEC §9 B2 source column) is absent from B2; the rubric does not require it.
