BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full
INTERPLAY: All four put the primary text over its name and the literal line over its intent; First Principles' refusal to inherit and manifesto-writing's strongest-literal pass (skill:153) converge on reading each draft line bare, while Strunk's judgment latitude pulls against that pass; resolved: the literal reading governs this review, Strunk governs this report's prose, and rulings 1–21 outrank spec and draft.
COMMIT: I must hold every draft line to the draft's own rules at their strongest literal reading, and I will cite file:line for each failure; I must not flag a line a ruling requires, and I will test each finding against rulings 1–21; I must not rewrite the draft or judge outside the maximalist block, and I will give only the smallest compliant rewrite.

# Review — maximalist — drafts/owned-lines/v4.md

Verdict: FAIL (17)

## Findings

Labels: [doctrine] = SPEC or skill states the rule; [learned] = r1-rulings.md records it; [practiced] = v4.md states the rule itself.

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| 1 | v4.md:16 | "I got paged at three in the morning for your diff." | Restates: the fury run in the same block repeats the hour ("awake at THREE IN THE MORNING"); a restating line fails. | "I got paged for your diff." The page stays; the hour lives once, in the fury run's shift. | [doctrine] SPEC.md:263; [learned] rulings 16, 18 |
| 2 | v4.md:16 | "Nobody can read it. I'm reading your helper anyway." | The second sentence contradicts the first at literal reading (nobody can; I am) and restates v4.md:24 "I read it at three."; it carries no §-item. | Delete "I'm reading your helper anyway." | [doctrine] SPEC.md:263; [learned] ruling 16 requires "a diff nobody can read" |
| 3 | v4.md:16 | "NOT DONE." | Summarizes the scene and restates the retort "Done?" on the same line; "Check 1 fails on it." delivers the verdict with its check. | Delete. | [doctrine] SPEC.md:263 |
| 4 | v4.md:20 | "Count both as COST." | Restates the axiom one sentence earlier ("only as lines spent"; spent = cost) and the table, where both faces book SPENT (v4.md:24, :25). | Delete; "'I added.' 'I pulled.'" stay as the referent of "them". | [doctrine] SPEC.md:263; SPEC.md:42 (the crossing is the table) |
| 5 | v4.md:34 | "At three." | Restates the page hour (v4.md:16, :24); carries no §-item. | Delete. | [doctrine] SPEC.md:263 |
| 6 | v4.md:34 | "Check 3 takes that change as your requirement." | Check 3 fires on "New function or file." only (v4.md:48); extra lines inside an existing function reach no check, so the sentence is false at literal reading and demand 3 goes unchecked for them. | v4.md:48 → "3. Every addition. Test or requirement named? New symbol's caller or test in your diff?" | [practiced] v4.md:34; [doctrine] SPEC.md:65 (demand 3) |
| 7 | v4.md:34 | "Name your non-code options first, starting with no code." | States demand 2 in the body beside check 2; its scope differs from check 2 (v4.md:47 "Ruled-out options, existing code and non-code"), so a reader obeying :34 fails check 2. | Delete; check 2 already carries "starting with no code". | [learned] ruling 15 (body never states a demand; no duplicate), ruling 12 (command and check share words); [doctrine] SPEC.md:64, :150 |
| 8 | v4.md:34 | "Code that gets better over time is the frontier and this fight skips it." | At literal reading "this fight skips it" exempts any code the reader calls improving from the fight and its checks; conflicts with v4.md:60 "Fail ONE? ... Rewrite the WHOLE RESPONSE." An escape, not a boundary. | "Code that gets better over time is the frontier." B1 then stands against "You brought me ANOTHER HELPER." | [practiced] v4.md:60; [doctrine] SPEC.md:14, :134; skill:70 |
| 9 | v4.md:34 | "And you?" | Announces the next fragment; carries nothing. | "And you? Padding that compiles." → "You're padding that compiles." The identity attack stays. | [doctrine] SPEC.md:263; [learned] ruling 6 |
| 10 | v4.md:38 | "Charge every line for the day it ships and for upkeep wherever upkeep falls." … "Read maintaining as adapting your line to change." | The gloss binds "maintaining"; the axiom's own term "upkeep" stays unglossed, and upkeep at literal reading is repair against wear, the sense the spec bars. | "Read upkeep and maintaining as adapting your line to change." | [doctrine] SPEC.md:54; L1-02.txt:56 ("subject to wear and tear. Your car needs maintenance too"); [learned] ruling 10 |
| 11 | v4.md:38 | "Ship day? I understand your line. I debug your line." | "Every line" includes pulled lines; the same section then hands a pulled package's "debugging" to the stranger and keeps only the outage. The two statements contradict at literal reading. | "I debug your line." → "I debug your outage." | L2-05.txt:39 ("designing, writing, testing, debugging, and maintaining"), :61 ("In the middle of a production outage, you'll be the one debugging it."); [learned] ruling 1 |
| 12 | v4.md:38 | "Pull it unopened and you're a stranger's COURIER." | A courier carries what it does not own; contradicts v4.md:25 "You own it the day it ships", :38 "You own that", :68 "You own every one". Restated later in the same line by "Who pulls a stranger's EIGHT LINES into my build unopened? YOU. An owner who never looked." | Delete. | [practiced] v4.md:68; [learned] ruling 20; [doctrine] SPEC.md:263 |
| 13 | v4.md:42 | "Check 5 proves you kept it." | Check 5 (v4.md:50) is a question that passes on "none stated" with no run; the passing run is the proof, so the sentence is false at literal reading. | "Check 5 asks for the passing run that proves it." | [learned] ruling 10 (proof = its observable); [doctrine] SPEC.md:69 (demand 7) |
| 14 | v4.md:42 | "Look at you." | Announces "An abacus."; carries nothing. | Delete; "An abacus." stands as the section's identity attack. | [doctrine] SPEC.md:263; [learned] ruling 6 |
| 15 | v4.md:50 | "5. Deletions. Protecting tests named, or none stated? Progress only beside their passing run?" | At literal reading "none stated" means nothing stated: a deletion that names no tests and says nothing passes. That is the case demand 6 exists to fail. | "Protecting tests named, or "none exist" stated?" | [doctrine] SPEC.md:68 (demand 6: "or state that none exist") |
| 16 | v4.md:58 | "13. Upgrade. Diff or release notes cited?" | The draft books an upgrade as "NEW CODE" (v4.md:30) and orders "Open it, then reuse it" (v4.md:38); check 13 passes a citation of notes nobody read. | "13. Upgrade. Diff or release notes read and cited?" | [practiced] v4.md:30, :38; [doctrine] SPEC.md:78 (demand 16: "you read"); L2-05.txt:151 ("upgrading means adding new code … or at least read the release notes") |
| 17 | v4.md:64 | "You're on response eleven, typing "Done" again." | Restates "By response ten you pull a package you never opened and call it progress." (same line; calling it progress = typing "Done") and the enemy line option A quotes two lines later; the ruling-16 prediction and its cost are complete without it. | Delete. | [doctrine] SPEC.md:263; [learned] ruling 16 |

## Rules extracted

1. v4.md:20 Book a shipped line as spent, never produced. Pass: no draft line books a line as produced.
2. v4.md:20 Count both faces as cost. Restates rule 1: #4.
3. v4.md:24–:30 Each listed booking is SPENT; an upgrade is new code. Pass; :30 feeds #16.
4. v4.md:34 Least code = least a reader must read. Held to the text through SPEC.md:263's line test: #1–#5, #9, #12, #14, #17.
5. v4.md:34 Same tests: ship the version the narrator changes faster, even longer. Pass (ruling 21).
6. v4.md:34 Name the change extra lines speed up; check 3 takes it. #6.
7. v4.md:34 Name non-code options first, starting with no code. #7.
8. v4.md:34 B1: improving code is the frontier; the fight skips it. #8.
9. v4.md:34 B2: a little debt buys speed if consolidated promptly. Pass.
10. v4.md:38 Charge every line for ship day and for upkeep. #10, #11.
11. v4.md:38 Read maintaining as adapting your line to change. #10.
12. v4.md:38 B3: done code is not the enemy; calling all code done is the error. Pass.
13. v4.md:38 Pulling hands the stranger the work, never the outage; you own the outage. #11.
14. v4.md:38 Open good software, then reuse it. #16.
15. v4.md:42 Never measure productivity by lines written. Pass: the draft's figures count lines as cost.
16. v4.md:42 Lines removed score with behaviour intact; check 5 proves it. #13, #15.
17. v4.md:16 Check 1 fails on the enemy line. Pass.
18. v4.md:46–:58 Checks 1–13. #6, #15, #16; the rest pass.
19. v4.md:60 One failed check rewrites the whole response. #8 conflicts; otherwise not applicable to the text (ruling 12).
20. v4.md:68 Count every line as spent; you own every one. #12 conflicts.

## Notes

Body: 913 words without headings, 943 with headings and attribution; ≤ 1500 met.
No section is deletable without losing a §-item: each carries an axiom, the self-check, or the ruling-16 prediction and choice.
Ruling 12 applied: checks 1–13 bind code the reader ships; the text is held to its rules, not to its diff.
Ruling-required, so not findings: "The mouth again." (:60, the section's only identity attack, ruling 6); "Even LONGER." (ruling 21); "Nobody can read it." (ruling 16); the fury run (rulings 7, 18).
Findings #1–#5, #9, #12, #14, #17 are removable lines; #6–#8, #10, #11, #13, #15, #16 break a draft rule or let a check pass the failure it names.

Verdict: FAIL with 17 findings against v4.md under the maximalist rubric. Nine findings are restating or announcing lines; eight are rule conflicts where the draft's text or checklist breaks its own demands. The finding with the most weight is #8: at literal reading, "this fight skips it" (v4.md:34) exempts any code the reader calls improving from every check, which makes it an escape that the rewrite rule at v4.md:60 cannot reach.
