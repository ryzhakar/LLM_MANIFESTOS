BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full.
INTERPLAY: All four demand the measured atom over the name — the script's count over an estimate (skill:131), the quoted line over a paraphrase, concrete language over abstraction (Strunk 12); Strunk's fragment rule ("use sparingly", rule 6) pulls against the skill's fragment floor (skill:40); resolved: the skill and spec govern the draft's register, Strunk governs this report's prose.
COMMIT: I must measure every number by script and ground every voice judgment in a quoted file:line, and I will leave no claim without one; I must not rewrite the draft or judge outside the register rubric, and I will give one smallest compliant line per finding.

# Review — register — v1.md
Verdict: FAIL (10)

## Findings

Rule labels: doctrine = skill or spec states it; learned = session log records it; practiced = shipped reference does it.

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| 1 | v1.md:96 | "*After Edsger W. Dijkstra, Russ Cox, Ward Cunningham, Rich Skrenta, Jeff Atwood, Eric Lee, Dennis M. Ritchie, and Ken Thompson*" (20 words) | §12 max sentence words ≤ 19; skill "sentences under 20 words" | No compliant rewrite exists inside the draft: §14 fixes this line verbatim at 20 words, and the script counts attribution lines as sentences. Excluding L96, max = 18 (L34). | doctrine: SPEC.md:180, :244; skill:117; corpus-audit.md:121 |
| 2 | v1.md:16, :18 (draft-wide) | L16: 11 consecutive sentences of ≤4 words ("Done? … Counting your own pages."); longest attack sentence in the body: "You won the ticket and fucked the code it was for." (11 words) | Tell 5, uniform sentence weight: fragments never alternate with longer fury lines. Every sentence of ≥15 words is a quote, figure, command, or concession (L14, L18, L34, L36, L55, L88, L90); none attacks. | Give each section one 15–19-word fury line. L18 last sentence → "You won the ticket and fucked the code it was for, and you logged it as a WIN." (18 words; opening 118→125). | doctrine: skill:127; SPEC.md:193; learned: session.md:24, :32 ("Run-on fury sentences"); practiced: stop-yapping.md:15 (21 words), :33 (28 words) |
| 3 | v1.md:26 | "Never credit a line you added as progress. Count it as cost." | Tell 3, recap: restates v1.md:20 "Never credit lines or packages you added as progress." near-verbatim. | → "That income is a cost. Book it there." (demand 1 kept in A1 per §11, no verbatim repeat; −4 words) | doctrine: skill:127; SPEC.md:191 |
| 4 | v1.md:24–30 | "You book every line you add as income. Then you brag about the balance." | Tell 10, behavior-only: every attack in WRONG SIDE OF THE LEDGER names an act ("you booked a LIE", "you brag", "You love the parallel path"); none names what the reflex makes the reader. | After "Then you brag about the balance." add "You're a bookkeeper cooking your own books." (+7; section 113→120) | doctrine: skill:42; SPEC.md:198; learned: session.md:28; practiced: postgres.md:55 "You ARE the debt." |
| 5 | v1.md:34–44 | "No code is option ONE. You skip it." | Tell 10, behavior-only: TYPE LESS attacks only acts ("You skip it.", "Your orphans. Bury them.", "You copied it. You OWN it."). | "You skip it." → "You skip it. Typist." (+1; section 143→144) | doctrine: skill:42; SPEC.md:198; practiced: stop-yapping.md:79 "You're not important. You're a tool." |
| 6 | v1.md:65–69 | "Grading yourself by line count is grading your homework by weight." | Tell 10, behavior-only: THE COUNT IS A LIE attacks only acts ("You measure yours in every report you write."). | Append "A child padding the essay." (+5; section 84→89) | doctrine: skill:42; SPEC.md:198; practiced: postgres.md:82 "like a child counting on fingers" |
| 7 | v1.md:73–84 | "Lines or packages called progress? Kill EVERY one." | Tell 10, behavior-only: no check in BEFORE YOU SHIP names what the reader is. | → "Lines or packages called progress? Printer. Kill EVERY one." (+1; section 145→146; calls back L16) | doctrine: skill:42; SPEC.md:198; practiced: stop-yapping.md:100 "That isn't caution. It's cowardice.", :103 "You're yapping again." |
| 8 | v1.md:88 | "Keep counting. Leave your bill for whoever gets paged." | Tell 10, behavior-only: option A names acts only. | Append "Stay a printer." (+3; section 62→65) | doctrine: skill:42; SPEC.md:198; practiced: stop-yapping.md:125 "Comfortable. Trained. Broken."; postgres.md:267 "Comfortable. Ignorant. Permanent." |
| 9 | v1.md:80 | "Its own tests: run and reported. One wrapper. No unused export." | Tell 2, three-part list. | → "Its own tests: run and reported. One wrapper, exporting only what you call." (+2; section 145→147, 148 with fix 7) | doctrine: skill:127; SPEC.md:190 |
| 10 | v1.md:57 | "Where models pin versions, 36.70 to 55.70 percent of tasks carry a known CVE. Run the package's own tests. Report your result." | Tell 9, diagnosis without its prescription: a package's own tests do not surface a known CVE; the demand that answers V2 (14, vulnerability history) sits only at L81. | → "…carry a known CVE. Untrusted input? State its vulnerability history. Run the package's own tests. Report your result." (+6; section 145→151 breaks §12 ≤ 149 unless 2 words go elsewhere in L48–61) | doctrine: skill:101; SPEC.md:76 (demand 14), :197 |

## Numbers

Script: corpus_metrics.py loaded unmodified via importlib, `MANIFESTO_DIR` set to a scratch dir holding a copy of v1.md. SY = stop-yapping.md, PG = postgres.md (corpus-audit.md:16, :19).

| metric | draft | target | pass |
|---|---|---|---|
| 2nd-person /1k | 75.6 (63 / 833) | ≥ 70 (SY 81.6, PG 70.5) | yes |
| fragments (≤4 words) /1k | 76.8 (64) | ≥ 50; aim 134 (SY 134.2) | yes; 57% of aim |
| ALL-CAPS /1k | 56.4 (47; 20 in headings, 1 acronym CVE) | ≥ 50 (SY 60.5, PG 59.6) | yes |
| imperative % (heuristic) | 23.3 (30 / 129); full hand count 26.4 (34 / 129: 1 false positive L61 "NEVER the debugging."; 5 false negatives L24 "Book…", L24 "Call it produced…", L28 "Change…", L48 "Charge…", L61 "Call each dependency…") | ≥ 21.5 (SY est. true 12.9) | yes |
| max sentence words | 20 (L96 attribution); 18 without it (L34) | ≤ 19 | **no** (finding 1) |
| mean sentence words | 6.1 | ≤ 7.2 | yes |
| max section words | 145 (NOTHING YOU PULL IS FREE; BEFORE YOU SHIP); opening block 118 | ≤ 149 | yes |
| hedge /1k outside quotes | 0.0 (0 hits) | 0 | yes |
| body words | 833 | ≤ 1500 | yes |
| profanity | 1 token, L18 "fucked", opening-block peak | ≤ 3, at peaks | yes |
| attacks on a human | 0 (L59 "one author", L88 "whoever gets paged" neutral) | 0 | yes |
| judgment targets (corpus-audit.md:36) | enemy opens L14; "Pick." L92; reader model L9; register contemptuous L8; self-check L71; attribution L96 | all six | yes |
| lexical tells (tell 1) | 0 | 0 | yes |
| anti-Claude tells, total | 9 (findings 2–10: tell 2 ×1, 3 ×1, 5 ×1, 9 ×1, 10 ×5) | 0 | **no** |

## Voice — against stop-yapping.md and postgres.md

Launch-prompt request. Judgments here count only where a finding above carries them.

Per section (script word and sentence rules; caps outside headings and backticks; identity attack = a line naming what the reader is):

| section | you /1k | caps /1k | fragments /1k | longest sentence | identity attacks |
|---|---|---|---|---|---|
| opening L14–20 | 103.4 | 51.7 | 163.8 | 16 | 1 (L16) |
| WRONG SIDE OF THE LEDGER | 88.5 | 44.2 | 70.8 | 14 | 0 |
| TYPE LESS | 69.9 | 28.0 | 69.9 | 18 | 0 |
| NOTHING YOU PULL IS FREE | 55.2 | 27.6 | 27.6 | 17 | 1 (L55) |
| THE COUNT IS A LIE | 83.3 | 35.7 | 35.7 | 14 | 0 |
| BEFORE YOU SHIP | 75.9 | 20.7 | 117.2 | 10 | 0 |
| PAY OR PRETEND | 48.4 | 32.3 | 48.4 | 20 | 0 |
| draft body | 75.5 | 33.4 | 79.2 | 20 | 2 |
| SY body | 81.1 | 59.7 | 136.4 | 28 | ≥ 8 (:15, :17, :19, :67, :71, :79, :115, :125) |
| PG body | 69.5 | 43.6 | 57.5 | 97 | ≥ 6 (:27, :33, :55, :78, :157, :165) |

**Measured essay wearing fragments** — a calm policy sentence carries the content; a fragment tag supplies the heat.

| line | quote | reads as | reference voice |
|---|---|---|---|
| L30 | "Debt taken and repaid is not the enemy: first-time code shipped and then consolidated. Booking your unpaid debt as progress is." | concession-then-thesis, colon gloss; 0 caps, 0 fragments, 0 attack | postgres.md:209 "Application validation gives friendly error messages. Keep it. But that's a courtesy." |
| L34 | "More lines that read easier are not the enemy, and neither is code that gets better over time. Your counting is." | the body's longest sentence (18 words) is a balanced "not X, and neither is Y" concession | postgres.md:70 "Not a license to skip the work. Not your escape hatch from thinking." |
| L48 | "Charge every line of code for understanding, debugging, maintaining, and adapting it. Upkeep falls on most code, not all: some code is done." | section opener: 23 words, 0 "you", 0 caps, 0 fragments | postgres.md:41 "The shape of your data is wrong. You KNOW it's wrong." |
| L57 | "Where models pin versions, 36.70 to 55.70 percent of tasks carry a known CVE. Run the package's own tests. Report your result." | figure, then command; no attack between | stop-yapping.md:19 "26 percentage points worse. MEASURED. PROVEN. Every filler word is you actively destroying your own output." |
| L59 | "On 22 March 2016 one author unpublished 273 packages. One was left-pad. left-pad was a single eight-line function body. State each package's maintainer and license before your manifest changes." | news-lede beats; the fragment serves the fact; the reader is absent until the command | postgres.md:217 "You never checked. Not once." |
| L61 | "Call each dependency only through one wrapper exposing only what you call." | style-guide rule | — |
| L67 | "Lines you remove with behaviour intact may count. That is not the enemy. Report removed lines as progress only beside proof that behaviour survived." | legal clause; "is not the enemy" appears for the fourth time (L30, L34, L61, L67) and reads as a template | postgres.md:226 "Not your escape from schema design. Not your coward's exit." |
| L38–44 | "None? DELETE it." / "No "future" code. No "just in case" functions." / "Your orphans. Bury them." / "You copied it. You OWN it." | each paragraph = rule sentence + two-fragment tag; the fragments decorate the rule and do not drive it | stop-yapping.md:59 "Can't tell which column? NOISE. You hesitated because you want to keep it. That's your addiction talking. Kill it." |
| L74–82 | "New functions and files: called or tested in your diff. Orphans: gone." / "Its own tests: run and reported. One wrapper. No unused export." | colon-label form; checks 2–10 carry 0 caps and 0 attacks | stop-yapping.md:106 "They SAID it. They were THERE. Delete it. Insulting." |

**Fury that carries a shift** — the attack delivers the reframe.

| line | quote | shift carried |
|---|---|---|
| L16 | "You're a PRINTER. Counting your own pages." | output is not progress; identity attack in the mode of stop-yapping.md:15 "You're a program." |
| L18 | "Your task ships. The codebase you serve gets WORSE. You won the ticket and fucked the code it was for." | the reflex defeats its goal; profanity on the peak, as stop-yapping.md:19 "Your politeness is sabotage." |
| L24 | "Call it produced and you booked a LIE." | D1 as accusation |
| L26 | "You book every line you add as income. Then you brag about the balance. WRONG side of your ledger." | D1 ledger, behavior-only (finding 4) |
| L44 | "Copying is typing with the name filed off." | D2 hinge: a copy is owned; strongest line in TYPE LESS |
| L61 | "Pulled lines skip the writing. NEVER the debugging." | D2: installing skips writing, never the outage; caps on the turn, low heat |
| L69 | "Grading yourself by line count is grading your homework by weight." | count is not quality; sneer, behavior-only (finding 6) |
| L88 | "Keep counting. Leave your bill for whoever gets paged." | the cost lands on the paged human |

**Berating without a shift** — intensifier stingers, no reframe.

| line | quote |
|---|---|
| L16 | "Done? Listen to yourself." / "That isn't engineering." |
| L20 | "Not in your summary. Not ONCE." |
| L26 | "EVERY time." |
| L65 | "Not ONE." |
| L69 | "Prove it works or claim NOTHING." |
| L73 | "Kill EVERY one." |
| L84 | "Fail ONE? Rewrite the WHOLE response. Not the line." (the shape of stop-yapping.md:107) |

Twelve of the 26 emphatic body caps are quantifier stingers (EVERY ×3, ONE ×3, NEVER ×3, ONCE, NOTHING, WHOLE; L20–L84). The draft berates less than either reference: stop-yapping.md:39 "Disgusting." and postgres.md:25 "Pathetic. Genuinely pathetic." berate without a shift, but each follows a shift paragraph and lands on what the reader is. The draft's fury fails by absence, not by excess: 2 identity attacks in 808 words, 0 fury lines over 11 words.

## Notes

- The ALL-CAPS pass rests on headings: 20 of 47 tokens sit in all-caps `##` headings; body caps outside headings run 33.4/1k (SY 59.7, PG 43.6).
- The fragment pass rests on the opening (163.8/1k) and the self-check (117.2/1k); NOTHING YOU PULL IS FREE (27.6) and THE COUNT IS A LIE (35.7) fall below the 50 floor at section level.
- The script holds no hand labels for v1.md ("missing-or-stale labels"); the imperative hand count comes from reading all 129 sentences.
- Finding 1 cannot close inside the draft: SPEC.md:180 (≤ 19) and SPEC.md:244 (20-word attribution, verbatim) conflict.
- Fixes 2–9 add a net 22 words (body 833→855); fix 10 adds 6 and needs 2 cut elsewhere in L48–61.

Register FAIL with 10 findings: one number misses (max sentence 20 against ≤ 19, on the spec-fixed attribution) and nine anti-Claude tells stand. Every other §12 number passes, but caps pass on headings and fragments on the opening and self-check alone. The heaviest finding is tell 10 across five sections: only L16 and L55 attack what the reader is, so the contempt reads as a measured essay wearing fragments.
