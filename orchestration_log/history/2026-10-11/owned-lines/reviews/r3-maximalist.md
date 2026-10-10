BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full
INTERPLAY: All four put the primary text over its name and the literal check over the impression; First Principles' refusal to inherit and manifesto-writing's strongest-literal pass (skill:153) converge on holding v3 to its own words, while Strunk's judgment latitude pulls against "no allowance for convention"; resolved: the draft's own rules and the owner rulings set the bar, and Strunk governs only this report's prose.
COMMIT: I must quote every failing line with its file:line, and I will name the draft rule or ruling it breaks; I must not rewrite the draft or judge outside the maximalist block, and I will give only the smallest compliant fix; I must not flag a line a ruling requires, and I will check every fix against the ruling floors by count.

# Review — maximalist — v3.md

Verdict: FAIL (28)

## Rules the draft states

1. :16 "Read your first word. Check 1 fails on it."
2. :20 "Never book a line you ship as lines produced, only as lines spent."
3. :20 "A spent line can buy a feature."
4. :24-30 every typed or pulled line books SPENT; "You own it the day it ships." (:25); a parallel path books "SPENT TWICE" (:28); an upgrade books "NEW CODE" (:30)
5. :34 "Write the least code your goal permits. Least means least work for ME"
6. :34 "Two of your versions pass the same tests? Ship the one I change faster. Even LONGER."
7. :34 "Name the line that makes your version faster. Check 3 takes that line as your requirement."
8. :34 "Try no code first. Check 2 wants it named."
9. :34 B1 "Code that gets better over time is the frontier."; B2 "a little buys speed if you consolidate it promptly"
10. :38 "Charge every line for the day it ships and for upkeep wherever upkeep falls."
11. :38 "Upkeep is maintaining, which means adapting your line to change"
12. :38 "Done code is not the enemy."
13. :38 "Checks 2 to 13 itemize your bill."
14. :38 a stranger gets "the designing, writing, testing, debugging, and maintaining. NEVER THE OUTAGE. You own that."
15. :38 "reusing it is your job, until you pull a package unopened."
16. :42 "Never measure programmer productivity by lines of code written." "Lines written score ZERO."
17. :42 "Lines removed score, behaviour intact, and check 5 is how I know you kept it intact."
18. :46-58 checks 1-13
19. :60 "Fail ONE? The mouth again. Rewrite the WHOLE RESPONSE."
20. :70 "Book every line you ship as spent. You own every one. Pay before MY PHONE rings."
21. :3 "spent, not produced. yours, not theirs."; :6 "the one who ships it owns its cost."

Applied to the text itself: rule 5 makes every removable sentence a violation; rule 4's "SPENT TWICE" and check 6 make every restatement a parallel path; SPEC.md:263 fails every line that restates, announces, or summarizes.

## Findings

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| 1 | v3.md:16 | "You shipped it. Now it's mine." | Rules 4, 14, 20, 21: the shipper owns ("You own it the day it ships", "You own that", "You own every one", "yours, not theirs"). "Now" moves ownership off the shipper. Ruling 16 lets the narrator inherit; it never takes ownership from the shipper. | "Now it's mine too." | practiced v3.md:16; doctrine v3.md:3, :6, :25, :38, :70; r1-rulings.md:18; L2-05.txt:61 |
| 2 | v3.md:38 | "Who's the stranger in my build tonight? YOU ARE." | Rule 14, same section: the stranger gets the work, "NEVER THE OUTAGE. You own that." Naming the reader the stranger gives it the role that never holds the outage; breaks rules 14, 20, 21. | "Who pulls a stranger's EIGHT LINES into my build unopened? YOU. An owner who never looked." (keeps the section's identity attack, ruling 6) | practiced v3.md:38; doctrine v3.md:3, :38, :70; r1-rulings.md:8 |
| 3 | v3.md:30 | "your upgrade, as maintenance \| NEW CODE. SPENT." | Rules 10, 11: the draft defines maintaining as adapting to change and charges upkeep. An upgrade adapts to upstream change, so booking it "as maintenance" already books a charge. The wrong-booking column holds a right booking. | "your upgrade, as a version bump" | doctrine v3.md:38; L2-05.txt:151 "upgrading means adding new code" |
| 4 | v3.md:34, :47 | "Try no code first. Check 2 wants it named." / "existing code and non-code" | Ruling 12: check 2 and the command it checks use the same word. Body says "no code"; check 2 says "non-code" and never names "no code". | :47 "existing code and no code" | doctrine r1-rulings.md:14; SPEC.md:150 |
| 5 | v3.md:34 | "Name the line that makes your version faster. Check 3 takes that line as your requirement." | Rule 18: check 3 (:48) takes a "Test or requirement" for a "New function or file". A line of code is neither. "Faster" drops rule 6's "the one I change faster" and reads as run speed. | "Name the change your extra lines make faster. Check 3 takes that change as your requirement." | doctrine v3.md:34, :48 |
| 6 | v3.md:38 | "reusing it is your job, until you pull a package unopened." | Rule 15 at its strongest literal reading: "until" ends the reuse duty at the first unopened pull. The rule releases the reader on its own breach. | "reusing it is your job. Pulling a package unopened is not reuse." | doctrine v3.md:38; SPEC.md:138 (B5) |
| 7 | v3.md:16 | "Read your first word. Check 1 fails on it." | Rule 18: check 1 (:46) asks whether added lines or packages are called progress. The first word "Done!" names neither; the failure sits in the first line. | "Read your first line." | doctrine v3.md:46 |
| 8 | v3.md:38 | "Checks 2 to 13 itemize your bill." | Announces the checklist. Carries no axiom, demand, figure, or boundary. Ruling 15 lets the body name a demand; this line names twelve and adds nothing. | delete | doctrine SPEC.md:263; r1-rulings.md:17 |
| 9 | v3.md:38 | "EIGHT LINES, and a stranger took them back." | Restates the two sentences before it: "unpublished" is took back; "eight-line" is EIGHT LINES. | delete; EIGHT LINES moves into #2's fix | doctrine SPEC.md:263 |
| 10 | v3.md:38 | "I debug your line. EVERY ONE." | "EVERY ONE." restates the head's "Charge every line". A quantifier stinger with no reframe. | delete "EVERY ONE." | doctrine SPEC.md:263; r1-rulings.md:10 (ruling 8) |
| 11 | v3.md:38 | "GUESS WHO gets paged." | Restates :16 "I got paged" and the "You own that." before it. | delete | doctrine SPEC.md:263 |
| 12 | v3.md:20 | "Read your sentence again." | Announces the quotes after it. | delete | doctrine SPEC.md:263 |
| 13 | v3.md:20 | "Both filed as progress." | Restates :16 "your mouth says progress". Ruling 13 states demand 1 once. | delete; hold ruling 6's floor by splitting "You booked the PRICE as the FEATURE." into "You booked the PRICE. As the FEATURE." | doctrine SPEC.md:263; r1-rulings.md:15 |
| 14 | v3.md:20 | "Read mine." | Announces the table. | delete | doctrine SPEC.md:263 |
| 15 | v3.md:34 | "Write that down." | Announces. It commands an act that no check verifies. | delete; hold the floor by recasting "Two of your versions pass the same tests?" as "Two versions. Same tests?" | doctrine SPEC.md:263 |
| 16 | v3.md:34 | "You brought me ANOTHER HELPER. Tonight." | "Tonight." restates the hour of the :16 scene. | delete "Tonight." | doctrine SPEC.md:263 |
| 17 | v3.md:34 | "every minute I spend in the unconsolidated part is interest. MINE." | "MINE." restates "I spend". | delete "MINE." | doctrine SPEC.md:263 |
| 18 | v3.md:16 | "Done? Say that again." | "Say that again." carries no enemy, axiom, demand, figure, boundary, or scene fact. | delete "Say that again." | doctrine SPEC.md:263 |
| 19 | v3.md:16 | "Look at it." | Announces the scene lines after it. | delete | doctrine SPEC.md:263 |
| 20 | v3.md:16 | "NOT DONE. MY NIGHT." | "MY NIGHT." restates the fury run's "I'm the one awake at THREE IN THE MORNING". | delete "MY NIGHT." | doctrine SPEC.md:263 |
| 21 | v3.md:42 | "Lines written score ZERO." | Restates heading :40 word for word, and the head sentence before it. | delete | doctrine SPEC.md:263 |
| 22 | v3.md:42 | "Your "Done" counted two additions as work. Count again." | Restates :16 and :20. This is the third statement of demand 1's accusation (ruling 13: once). | delete both sentences | doctrine SPEC.md:263; r1-rulings.md:15 |
| 23 | v3.md:64 | "Count on it." | Carries no prediction, figure, or cost. | delete | doctrine SPEC.md:263 |
| 24 | v3.md:64 | "Watch." | Announces the prediction. | delete; hold the floor by recasting "Response four, you ship a helper with no test behind it." as "Response four. A helper. No test behind it." | doctrine SPEC.md:263 |
| 25 | v3.md:64 | "Look at the record." | Announces the figures. | delete | doctrine SPEC.md:263 |
| 26 | v3.md:64 | "You're a model. YOUR NUMBERS." | "YOUR NUMBERS." restates "You're a model." | delete "YOUR NUMBERS." | doctrine SPEC.md:263 |
| 27 | v3.md:68 | "Keep saying it." | Restates the quoted enemy line just before it. | delete | doctrine SPEC.md:263 |
| 28 | v3.md:66 | "## PICK" | The heading restates the required last body line "Pick." (:72). | rename, e.g. "## A OR B" | doctrine SPEC.md:263, :165 |

## Notes

- Unit: a sentence counts as a line (strongest literal reading). Body 993 words with headings, tables, and attribution, so ≤ 1500 passes. Each of the eight sections carries a §-item or a ruling-16 item, so none can be deleted.
- Checked on a scratch copy with all 28 fixes and the three recasts (#13, #15, #24): body 929 words. Fragments per 1k by section: 58.8, 52.6, 54.1, 54.7, 80.0, 75.9, 54.3, 68.5, all ≥ ruling 6's 50. Every section keeps an identity attack. Multi-word caps shouts: 12 (≥ 8). Without the recasts, the deletions alone drop THE LEDGER to 37.6, THE LEAST YOU CAN DO to 34.8, and RESPONSE TEN to 30.3.
- Lines a ruling requires, so not findings: the check-1 reference itself (ruling 13), the identity attacks "One column. That's all you are.", "Padding that compiles.", "The mouth again.", and "Stay a diff with a mouth." (ruling 6), the :16 scene, and the :64 cost run (ruling 16).
- Rule 19 applied to v3 itself: one failed check means rewriting the whole response. At its own strongest reading, v3 takes a whole rewrite, not 28 patches.
- Labels: every finding is practiced, meaning v3 does it. The rule it breaks is doctrine: the draft's own text, SPEC.md, or r1-rulings.md.

v3 FAILS the maximalist pass with 28 findings. Twenty-one are removable sentences that restate or announce; seven are lines where the draft breaks its own rules. The heaviest is that v3 contradicts its own thesis twice: "Now it's mine." (:16) and the reader named the outage-free "stranger" (:38) take ownership away from the shipper, against :25, :38 "You own that.", :70, and the tagline.
