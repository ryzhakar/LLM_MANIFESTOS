BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full
INTERPLAY: All four put the primary text over its name and the literal demand over the convenient one; skill:153 and First Principles converge on holding each line to its own rule with no inherited allowance, while Strunk's judgment latitude (purposeful repetition, rule 13 exemplars) pulls toward excusing restatement; resolved: SPEC.md:263 and skill:153 govern every finding, Strunk governs only this report's prose.
COMMIT: I must quote every failing line with file:line, and I will leave no finding without one; I must read each draft rule at its strongest literal reading, and I will grant no allowance for cost or convention; I must report facts, and I will state each fix as compliant text, never as advice; I must stay inside the maximalist block, and I will judge nothing outside it.

# Review — maximalist — drafts/owned-lines/v1.md

Verdict: FAIL (16)

## Rules the draft states — held to the draft as a diff (SPEC.md:263; skill:153)

| R | v1.md | rule | held against the draft |
|---|---|---|---|
| 1 | :20 | Never credit lines or packages you added as progress, not in your summary | pass |
| 2 | :24 | Book every line of code as spent, never as produced; never call one produced | pass (:52 "produced" sits in the enemy column) |
| 3 | :26 | Count every added line as cost | pass |
| 4 | :28 | Change the existing implementation; NEVER append a twin beside it | FAIL — #1–#7, #9–#11 (twins inside the draft), #14 (twin of kiss.md) |
| 5 | :34 | Write the least code the goal permits; least = least a reader must read | FAIL — #1–#7, #9–#11 add reading |
| 6 | :36 | Name existing-code and non-code options ruled out, before the first added line | FAIL — #13 |
| 7 | :38 | Name the test or requirement behind each addition past the minimum; none → DELETE | FAIL — #1–#7, #9–#11 name none |
| 8 | :40 | Add no function or file no caller or test in the diff uses | FAIL — #15 |
| 9 | :42 | Delete, in the same diff, code the change leaves without callers | pass (no line loses a caller) |
| 10 | :44 | Carry license and copyright notice with every function copied from a package | vacuous: no function copied |
| 11 | :48 | Charge every line of code for understanding, debugging, maintaining, adapting | FAIL — #8 |
| 12 | :55 | Name the package files read before depending on one | vacuous: no package |
| 13 | :57 | Run the package's own tests; report the result | vacuous |
| 14 | :59 | State maintainer and license before the manifest changes | vacuous |
| 15 | :61 | Call each dependency only through one wrapper exposing only what you call | vacuous |
| 16 | :65 | Never measure productivity by lines written; lines written never count in your reports | pass |
| 17 | :67 | Report removed lines as progress only beside proof behaviour survived | vacuous: no removal claimed |
| 18 | :69 | Name tests protecting every deletion or state none exist; prove it works or claim nothing | vacuous: diff deletes nothing |
| C1 | :73 | Summary calls no lines or packages progress | pass |
| C2 | :74 | Ruled-out options above the first added line | FAIL — #12, #13 |
| C3 | :75 | Each addition past the minimum names its test or requirement | FAIL — #1–#7, #9–#11 |
| C4 | :76 | New functions and files called or tested in the diff | FAIL — #15 |
| C5 | :77 | Deletions name tests; removals called progress carry proof | vacuous |
| C6 | :78 | Old path changed; no twin beside it | FAIL — #14 |
| C7–C10 | :79–:82 | Package, wrapper, transitive, upgrade, copied-function checks | vacuous: no package, upgrade, or copied function |
| 19 | :84 | Fail one → rewrite the WHOLE response, not the line | FAIL — #16; triggered by C2, C3, C4, C6 |
| 20 | :92 | Pick. | n/a |

## Findings

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| 1 | v1.md:16 | "Listen to yourself." / "You TYPED a helper. You PULLED a library." / "One reflex. Two faces." | announces; restates :14 (helper, library); summarizes the two sentences before it — SPEC.md:263, R4, R7 | "Done? You counted both. Called the count PROGRESS. That isn't engineering. You're a PRINTER. Counting your own pages." | practiced v1.md:14, :16; doctrine SPEC.md:263 |
| 2 | v1.md:18 | "Your task ships. The codebase you serve gets WORSE." / "You won the ticket and fucked the code it was for." | one proposition stated twice — SPEC.md:263, R4 | Delete "Your task ships. The codebase you serve gets WORSE."; the profanity peak stays (SPEC.md:205) | practiced v1.md:18; doctrine SPEC.md:263 |
| 3 | v1.md:20 | "Not ONCE." | restates "Never" in the same line — SPEC.md:263 | "Never credit lines or packages you added as progress. Not in your summary." | practiced v1.md:20; doctrine SPEC.md:263 |
| 4 | v1.md:26 | "Lines spent. Not lines produced." / "EVERY time." / "Never credit a line you added as progress. Count it as cost." | restates :24 axiom; "EVERY time" restates "every line"; demand 1 twins :20; "Count it as cost" restates :24 — SPEC.md:263, R4 | "You book every line you add as income. Then you brag about the balance. WRONG side of your ledger." Fact: "lines produced" then leaves the body (only at :26; SPEC.md:44 keeps it verbatim); SPEC.md:160 places demand 1 in this section as well as :159 | practiced v1.md:20, :24, :26; doctrine SPEC.md:44, :160, :263 |
| 5 | v1.md:28 | "Both alive." | restates "Your new helper beside the old one." — SPEC.md:263, R4 | Delete "Both alive." | practiced v1.md:28; doctrine SPEC.md:263 |
| 6 | v1.md:40 | "No "future" code. No "just in case" functions." | restates the line's own ban (a function no caller or test uses); copies kiss.md:159 wording — SPEC.md:263, R4 | "Add no function or file that no caller or test in your diff uses." Fact: SPEC.md:143 "Carry content, not wording" | practiced v1.md:40; doctrine SPEC.md:143, :263; kiss.md:159 |
| 7 | v1.md:42 | "Bury them." | restates "Delete" — SPEC.md:263 | Delete "Bury them." | practiced v1.md:42; doctrine SPEC.md:263 |
| 8 | v1.md:48 | "Charge every line of code for understanding, debugging, maintaining, and adapting it. Upkeep falls on most code, not all: some code is done." | at its strongest reading the command charges done code for maintenance the next sentence says it never takes — R11 broken by its own boundary | "Charge every line of code, the day it ships, for understanding, debugging, maintaining, and adapting it." (17 words). Fact: SPEC.md:54 writer rule carries "the day it ships"; v1 drops it | practiced v1.md:48; doctrine SPEC.md:54 |
| 9 | v1.md:65 | "Lines you wrote NEVER count there. Not ONE." | twins :20 (no credit for added lines in the summary); "Not ONE" restates "NEVER" — SPEC.md:263, R4 | "Never measure programmer productivity by lines of code written. You measure yours in every report you write." Fact: the proposition stands at :20, :26, :65, :73; SPEC.md:55, :159, :160 each place it | practiced v1.md:20, :65; doctrine SPEC.md:55, :263 |
| 10 | v1.md:67 | "No proof? No credit." | restates "Report removed lines as progress only beside proof that behaviour survived." — SPEC.md:263 | Delete "No proof? No credit." | practiced v1.md:67; doctrine SPEC.md:263 |
| 11 | v1.md:69 | "Grading yourself by line count is grading your homework by weight." / "Prove it works or claim NOTHING." | first restates A4 (:65); second restates demand 7 (:67) — SPEC.md:263, R4 | "Name the tests that protect every deletion you make, or state that none exist." Fact: no primary/*.txt, SPEC.md, or discovery/ line holds "homework" (grep) | practiced v1.md:65, :67, :69; doctrine SPEC.md:263 |
| 12 | v1.md:74 | "Above your first added line: the options you ruled out." | check diverges from the command it checks: :36 says "before" (order), :74 says "Above" (file position); read inside the diff, no new file has a line above line 1, so this draft cannot pass C2 | "2. Before your first added line: the options you ruled out." Fact: SPEC.md:64 "the list precedes the first added line" | practiced v1.md:36, :74; doctrine SPEC.md:64 |
| 13 | v1.md:1–:12 (diff) | "Name the existing code and non-code options you ruled out, before your first added line." (:36) | the diff names no ruled-out option before its first added line — R6, C2 | Fact: the options sit only outside the diff: SPEC.md:17 (kiss rows move), stack-options.md:107-110 (MOVE rows), :418 (one holder) | practiced v1.md:1–:12; doctrine v1.md:36, :74 |
| 14 | v1.md:36, :40, :42, :61 | "No code is option ONE." / "No "future" code. No "just in case" functions." / "Delete, in the same diff, the code your change leaves without callers." / "Pulled lines skip the writing. NEVER the debugging." | the diff appends twins beside an unchanged old path — R4 (:28), C6 (:78) | Fact: kiss.md:157-165 stays unchanged: :165 "The best code is no code." twins :36; :159 "Remove dead code immediately. Delete speculative "future" code. Delete "just in case" functions." twins :40, :42; :161 "Every line you don't write is a line you don't maintain, test, debug, or understand." contradicts :61 and :48. kiss.md:234 "It creates "just in case" functions." lies outside :157-165 and twins :40 after that removal. SPEC.md:267 defers the kiss edit to a separate change; stack-options.md:418 makes v1 the one holder only once kiss.md's row leaves | practiced v1.md:36, :40, :42, :48, :61; kiss.md:157-165, :234; doctrine v1.md:28, :78 |
| 15 | v1.md (whole file) | "New functions and files: called or tested in your diff." (:76) | the diff adds a file that nothing in the diff calls — R8, C4 | Fact: generate.py:86 `manifesto_dir = Path('manifestos')`, :91 `manifesto_dir.glob('*.md')`; v1.md sits in drafts/owned-lines/, untracked (`?? drafts/owned-lines/v1.md`); no file in the diff references it | practiced v1.md; doctrine v1.md:40, :76 |
| 16 | v1.md:84 vs :73, :74, :75 | "Fail ONE? Rewrite the WHOLE response. Not the line." / "Kill EVERY one." / "Missing? Add no line." / "Unnamed? Cut it." | :84 forbids line fixes; :73 and :75 prescribe line fixes; :74 forbids the lines a rewrite adds — the draft breaks its own rule | Delete "Kill EVERY one.", "Missing? Add no line.", "Unnamed? Cut it."; :84 holds the one remedy. Fact: SPEC.md:164 requires "not the line" | practiced v1.md:73-75, :84; doctrine SPEC.md:164 |

## Notes

- Body: 851 words (L11–96, wc), ≤ 1500. No section is deletable: each holds a §-item (A1–A4, demands 1–16, V1–V4/V6/V7, B1–B6, self-check, choice).
- Not counted: self-check items :73–:82 restating section commands (SPEC.md:164 mandates coverage); A :88 repeating :14 (skill:105).
- Not counted: title :12, headings, table header and separator :50–:51, `---` :94, attribution :96 carry none of the six SPEC.md:263 functions; each is a §11/§14 item. Heading :22 repeats :26's "WRONG side of your ledger".
- By v1.md:84, failing C2, C3, C4, or C6 demands a whole rewrite; the line fixes above satisfy SPEC.md:263, not v1.md:84.
- Fixes #1–#7 and #9–#11 remove 87 words (wc).

The maximalist pass fails v1 with 16 findings. Ten lines restate, announce, or summarize; one command contradicts its own boundary; one check diverges from its command; the remedy line conflicts with three checks; three findings concern the draft as a diff. The heaviest: the diff appends twins of kiss.md:157-165 and leaves that old path unchanged, so v1 breaks its own "NEVER append a twin beside it" (v1.md:28, :78).
