Elements loaded: First Principles (/home/user/LLM_MANIFESTOS/manifestos/first-principles.md), Strunk SPR v3 (/home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml, 2,923 lines), manifesto-oath (/home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md), manifesto-writing (/home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md); each read whole from source.
Interplay: all four demand the primary text over its name and the count over the impression; Strunk's latitude for rhetorical fragments pulls against manifesto-writing's hard floors, and First Principles' refusal of inherited form pulls against judging by a reference register; resolved: the references set the numbers, the rule text sets pass or fail, an owner ruling outranks the spec, taste decides nothing.
Commitments: I must quote every failing line with file:line and measure every number by script or count, and I will print each; I must not rewrite the draft, judge outside the register rubric and rulings 16–18, or recommend, and I will not.

# Review — register — drafts/owned-lines/v3.md

Verdict: FAIL (17)

Labels: doctrine = SPEC.md or skill states it; learned = r1-rulings.md or session.md records it; practiced = a shipped reference does it.

## Findings

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| 1 | v3.md:16 | "It's three in the morning, I got paged, and your diff is open on my screen." | Tell 2: three-part list (clause tricolon, scene set by inventory) | "I got paged at three in the morning for your diff." | doctrine: SPEC.md:190; skill:127 |
| 2 | v3.md:16 | "Your date library dragged in a package that is GONE, unpublished by its author." | Tell 3: explanatory gloss; v3.md:38 states the unpublishing again | "Your date library dragged in a package that is GONE." | doctrine: SPEC.md:191; learned: session.md:24 ("writes for coverage, not for effect") |
| 3 | v3.md:16 | "I'm reading it line by line." | Ruling 16: the scene holds "a diff nobody can read"; here the narrator reads it | "Nobody can read it. I'm reading it anyway." | learned: r1-rulings.md:18 |
| 4 | v3.md:16 | "You're a diff with a mouth, and your mouth says progress." | Human-or-Claude test: the image explains itself in its own tail (abstract noun "progress") | "You're a diff with a mouth." | learned: session.md:24, :34 |
| 5 | v3.md:20 | "A spent line can buy a feature." | Ruling 17 / ruling 6: A1 limit stands as a neutral concession, outside any attack | Merge with the next sentence: "You booked the PRICE as the FEATURE it bought." | learned: r1-rulings.md:19, :8; doctrine: SPEC.md:52 |
| 6 | v3.md:20 | "One column. That's all you are." | Human-or-Claude test: fragment with no referent; identity asserted by fiat | "One column. INCOME. That's all you are." | learned: session.md:34 |
| 7 | v3.md:34 | "Code that gets better over time is the frontier." | Ruling 17 / ruling 6: B1 stands outside the attack that follows it; abstract tail | "You brought me ANOTHER HELPER, not code that gets better over time." | learned: r1-rulings.md:19, :8; doctrine: SPEC.md:134 |
| 8 | v3.md:34 | "Shipping first-time code is like going into DEBT, and a little buys speed if you consolidate it promptly." | Ruling 17 / ruling 6: B2 delivered as neutral simile-plus-compound, no attack | "Your "Done" books first-time code as INCOME when a little DEBT buys speed only if you consolidate it promptly." (19 words; keeps "a little", "promptly", "consolidate") | learned: r1-rulings.md:19, :8, :4; doctrine: SPEC.md:135, :44 |
| 9 | v3.md:34 | "Your "Done" books the loan as INCOME, and every minute I spend in the unconsolidated part is interest." | Human-or-Claude test: comma-and compound closing on an abstract predicate ("is interest"); essay cadence | "Every unconsolidated line charges interest." (with #8 carrying INCOME) | learned: session.md:34; practiced: stop-yapping.md and postgres.md hold 0.0 and 0.2 comma-compounds per 1000 words |
| 10 | v3.md:38 | "Upkeep is maintaining, which means adapting your line to change, and change lands on most of your code." | Human-or-Claude test: lecture gloss ("which means"); ruling 17: the "most, not all" limb sits outside the attack | "Maintaining means adapting your line to change. Done code is not the enemy. You call ALL of yours done when change lands on most of it." | learned: r1-rulings.md:19, :6, :12 |
| 11 | v3.md:38 | "Good software is out there, and reusing it is your job, until you pull a package unopened." | Human-or-Claude test: concession, comma, hinge; two commas in a 17-word turn | "Reusing good software is your job until you pull a package unopened." | learned: session.md:34 |
| 12 | v3.md:42 | "Lines removed score, behaviour intact, and check 5 is how I know you kept it intact." | Human-or-Claude test: comma-and compound plus explanatory clause ("is how I know"); "intact" twice | "Lines removed score, behaviour intact. Check 5 proves you kept it." | learned: session.md:34 |
| 13 | v3.md:16, :38, :42, :64 | "You're a diff with a mouth" / "YOU ARE." / "You ARE the tally." / "You're the agent in that sentence." / "You're a habit with write access." | Ruling 17: identity attacks follow one template, copular "you are [noun]" as the closing line of 4 of 6 prose sections; :16 and :64 share the frame "You're a [noun] with [noun]" | v3.md:42 "You ARE the tally." → "Look at you. An abacus."; v3.md:64 "You're a habit with write access." → "Write access on a habit." | learned: r1-rulings.md:19 |
| 14 | v3.md:64 | "You're going to drift. Count on it." | Human-or-Claude test: first sentence lifted verbatim from the reference; second a stock idiom | "You drift. Guaranteed." (keeps two fragments and the "you" token) | practiced: stop-yapping.md:113 "You're going to drift." |
| 15 | v3.md:64 | "Look at the record." | Tell 3: signpost announcing the figures | Delete; the figures follow "call it progress." directly | doctrine: SPEC.md:191; practiced: stop-yapping.md:56 "Announcing what you're about to do." |
| 16 | v3.md:64 | "You're the agent in that sentence." | Tell 3: meta-textual pointer to the document's own sentence | "That agent is you." | doctrine: SPEC.md:191 |
| 17 | v3.md:64 | "By response ten I'm paged at three in the morning for a helper nobody asked for and a package nobody opened, and you're on response eleven, typing "Done" again." (29 words) | Ruling 18 / ruling 7: run of 25+ words carrying no shift (it replays v3.md:16's scene); tell 3: recap | "By response ten I'm paged at three in the morning. You're on response eleven, typing "Done" again." | learned: r1-rulings.md:20, :9; doctrine: SPEC.md:191 |

## Numbers

Script: `python3 -I corpus_metrics.py` on a scratchpad copy holding v3.md alone (MANIFESTO_DIR repointed). Per-section, body-caps, shout, colon and run counts: same tokenizer, by count.

| metric | draft | target | pass |
|---|---|---|---|
| 2nd-person /1k | 72.5 (72/993) | ≥ 70 | yes |
| fragments /1k | 66.5 (66) | ≥ 50; aim 134 | yes |
| fragments /1k per section (ruling 6) | opening 78.0, LEDGER 56.7, LEAST 58.3, OWN 63.4, ZERO 95.2, SHIP 76.4, RESPONSE TEN 56.3, PICK 78.9 | ≥ 50 each | yes |
| ALL-CAPS /1k, script (headings in) | 76.5 (76; 23 in headings) | ≥ 50 | yes |
| ALL-CAPS /1k, body only (ruling 6) | 53.4 (53/993); 54.7 with heading words out of the base | ≥ 50 | yes |
| imperative % (heuristic) | 22.4 (30/134) | ≥ 21.5 | yes |
| max sentence words | 29 (v3.md:16, :64); attribution 20, exempt (ruling 5) | ≤ 19, or ≤ 3 fury runs ≥ 25 each with a shift (rulings 7, 18) | no (v3.md:64) |
| fury runs ≥ 25 words (ruling 18) | 2: v3.md:16 shift yes (a word typed at five becomes the narrator's three a.m.); v3.md:64 shift no | ≤ 3, each with a shift | no |
| mean sentence words | 6.5 | ≤ 7.2 | yes |
| max section words | 144 (BEFORE YOU SHIP); opening block 143 | ≤ 149 | yes |
| hedge /1k outside quotes | 0.0 | 0 | yes |
| body words | 993 | ≤ 1500 | yes |
| lexical tells | 0 | 0 | yes |
| profanity | 1 ("fucking", v3.md:16, opening peak) | ≤ 3, at peaks | yes |
| attack on a human | 0 | 0 | yes |
| semicolons (ruling 17) | 0 | 0 | yes |
| colons /1k (ruling 17) | 1.0 (1, v3.md:64, spec wording V1) | ≤ 2 | yes |
| multi-word ALL-CAPS shouts (ruling 17) | 17 (THREE IN THE MORNING, NOT DONE, MY NIGHT, WRONG SIDE OF THE LEDGER, SPENT TWICE, SPENT AGAIN, NEW CODE, ANOTHER HELPER, EVERY ONE, NEVER THE OUTAGE, GUESS WHO, EIGHT LINES, YOU ARE, WHOLE RESPONSE, YOUR NUMBERS, MY NIGHTS, MY PHONE) | ≥ 8 | yes |
| identity attack per section (ruling 6) | 8 of 8 | ≥ 1 each | yes |
| identity attacks off one template (ruling 17) | 4 of 6 prose sections close on copular "you are [noun]" | no template | no |
| boundaries inside an attack (ruling 17) | inside: B3 formula, B4, B5, B6; outside: A1 limit (:20), B1 (:34), B2 (:34), B3 "most" limb (:38) | all inside | no |
| "X is not the enemy" (ruling 6) | 1 (v3.md:38) | ≤ 1 | yes |
| quantifier stingers (ruling 8) | "EVERY ONE." (:38) carries A3's every-line charge; "Fail ONE?" (:60) carries the rewrite rule | each carries a reframe | yes |
| narrator with a stake (ruling 16) | first person at :16, :20, :34, :38, :42, :64, :68, :70 | present | yes |
| one scene (ruling 16) | 1 (v3.md:16): page yes; build broken by vanished package yes; diff nobody can read no | page, broken build, unreadable diff | no |
| one prediction section, No Drift form (ruling 16) | 1 (RESPONSE TEN, v3.md:62–64): response four, response ten, cost | present | yes |
| opens on enemy; ends "Pick."; self-check; attribution | yes; yes; yes; yes | present | yes |
| anti-Claude tells and human-or-Claude lines | 13 lines (findings 1, 2, 4, 6, 9–17) | 0 | no |

## Voice — human or Claude

Line by line; "Claude" names each sentence that answers Claude. Signposts to check numbers are named but uncounted: ruling 15 (r1-rulings.md:17) lets the body name a demand.

| line | answer | Claude sentences | human sentences |
|---|---|---|---|
| 14 | human | — | the enemy line |
| 16 | mixed | #1 tricolon; #2 gloss; "Check 1 fails on it." (uncounted); #4 tail | "Done? Say that again."; "You shipped it. Now it's mine."; the 29-word run; "Nobody asked you for it." |
| 20 | mixed | #5; #6 | "You booked them on the WRONG SIDE OF THE LEDGER."; "COST." |
| 22–30 | human | — | every SPENT row |
| 34 | Claude | "Check 3 takes…", "Check 2 wants it named." (uncounted); #7; #8; #9 | "Ship the one I change faster."; "Even LONGER."; "And you? Padding that compiles." |
| 38 | mixed | #10; "Checks 2 to 13 itemize your bill." (uncounted); #11; "Who's the stranger in my build tonight? YOU ARE." (#13, a term pivoted to land a closer) | "I understand your line. I debug your line. EVERY ONE."; "NEVER THE OUTAGE. You own that. GUESS WHO gets paged."; "EIGHT LINES, and a stranger took them back." |
| 42 | mixed | #12; "You ARE the tally." (#13) | "You least of all."; "No check 5? Then your deletion is a hole I fall into at three." |
| 46–58 | neither | checklist form | — |
| 60 | human | — | "Fail ONE? The mouth again. Rewrite the WHOLE RESPONSE." |
| 64 | Claude | #14; #15; #16; #17; "You're a habit with write access." (#13); V1–V4 figures are spec wording, uncounted | "Response four, you ship a helper with no test behind it."; "You're a model. YOUR NUMBERS." |
| 68–72 | human | — | A, B, "Pick." |

Fury that carries a shift: :16 "You shipped it. Now it's mine." and the 29-word run; :20 the ledger line; :24–30 every row; :34 "Ship the one I change faster. Even LONGER."; :38 "NEVER THE OUTAGE…GUESS WHO gets paged." and "EIGHT LINES, and a stranger took them back."; :42 "Then your deletion is a hole I fall into at three."; :60.

Fury that berates without one: :16 "NOT DONE. MY NIGHT." (echoes the run before it); :20 "One column. That's all you are."; :34 "Tonight.", "MINE."; :38 "YOU ARE."; :42 "You ARE the tally."; :64 the 29-word run and "You're the agent in that sentence."

Measured essay wearing fragments: :34 from "Code that gets better over time" to "is interest" (9, 5, 1, 18, 18 words; the two 18s are comma-and compounds, "Tonight." and "MINE." decorate the gaps); :38 from "Upkeep is maintaining" to "a package unopened" (18, 6, 6, 7, 16, 3, 3, 4, 17; three comma-compounds carry the argument, the caps fragments carry volume); :64 figure block (17, 14, 16; spec wording). Against the references: v3 holds 12 prose sentences joined by ", and / which / until" (14.1 per 1000 words) against 0.0 in stop-yapping.md and 0.2 in postgres.md; commas per sentence of 12+ words 1.45 against 0.18 and 0.66; sentences of 12–19 words 14.2% against 3.2% and 9.1%. The references' long lines run comma-free on "and … and … and" (postgres.md:21, :43); v3's long lines balance on a comma.

## Notes

- Imperative heuristic: 6 false positives ("Check 1/3/2…" as nouns, "Ship day?", "NEVER THE OUTAGE.", "Test or requirement named?"), 2 false negatives ("Charge every line…" :38, "Book every line…" :70); hand count 26/134 = 19.4%, above stop-yapping's est. true 12.9 (corpus-audit.md:80).
- Slack: 2nd-person needs 70 tokens at 993 words and holds 72; RESPONSE TEN and THE LEDGER each hold one fragment above the section floor. Fixes #8, #12, #13, #14 keep their "you" tokens; fix #4 drops one.
- "three" recurs 6 times (:16 twice, :24, :34, :42, :64); session.md:62 records an overused refrain as a failure; no rule caps it; uncounted.
- SPEC.md:197 cites conventions.md:49; the live /home/user/LLM_MANIFESTOS/orchestration_log/reference/conventions.md no longer holds that line at :49; tell 9 judged from SPEC.md's own wording.
- Script output: words 993, sentences 134, sections 7, 1 table, 0 code blocks, `!` 2 (both inside the quoted enemy line), 1 unterminated unit (attribution).

Verdict FAIL with 17 findings: every number on the script passes, and the failures sit in voice, ruling 17 and ruling 18. The weightiest finding is the essay cadence: 12 comma-joined compounds (14.1 per 1000 words against 0.0 and 0.2 in the references). They cluster where boundaries arrive as neutral concessions outside an attack (v3.md:20, :34, :38), and where the 29-word run at v3.md:64 replays the opening scene without a shift.
