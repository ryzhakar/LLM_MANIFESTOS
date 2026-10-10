Elements loaded in full: First Principles (/home/user/LLM_MANIFESTOS/manifestos/first-principles.md, v1.0.1); Strunk SPR v3 (/home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml, 2924 lines); binding protocol (/home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md).
Interplay: First Principles and Strunk converge on cutting inherited claims and padding down to what is verified, concrete, and brief; they pull apart where Strunk permits purposeful deviation and First Principles permits none; resolved by quoting exact text, stating verdicts positively, and granting no rating on inheritance.
Commitments: I must test each AXIOM against the primary text, and I will quote at most 25 words with file:line; I must not recommend, draft, or add candidates, and I will not state a verdict without a located quote.

# Axiom Verification

Scope. Read whole: L1-01 to L1-06, L2-01 to L2-05, and skrenta-wayback.txt (Skrenta's fuller post, ADJACENT, same author as L1-04, no twelfth author). Rated rows read from the five reports' "Rated statements" sections only. Lane 1 = L1-01..06; lane 2 = L2-01..05. Authors: Hertzfeld (Atkinson, L1-01), Dijkstra (L1-02), Cunningham (L1-03), Skrenta (L1-04, wayback), Atwood (L1-05; quotes Skrenta and Shipley), Lee (L1-06), McIlroy (L2-01), Ritchie and Thompson (L2-02), Hietaniemi (L2-03), Koçulu (L2-04), Cox (L2-05). Labels: [D] the text states it as a claim or rule; [L] the text recounts an event or experience; [P] the text does it. The supplement L2-02-dumped-retro.txt, cited by three reports, lies outside the eleven; it is named once and never counted.

## Statements

Ten AXIOM rows exist across the five reports (enemies 2, tensions 2, demands 3, distinctions-vocabulary 2, collection-fit 1). They merge into six distinct statements.

| # | Merged statement | Rated AXIOM by (report:R-id) |
|---|---|---|
| S1 | Book a line of code as spent, never as produced. | enemies:R01 "Count lines of code as spent, never as produced."; tensions:R01 "Treat a line of code as spent, not produced."; distinctions-vocabulary:R01 "Book lines of code as lines spent, not lines produced." |
| S2 | Count lines of code as cost, never as output, productivity, or asset. | demands:R01 "Count lines of code as cost, never as output, productivity, or asset." |
| S3 | Do not measure programmer productivity by lines of code. | tensions:R02 "Do not measure programmer productivity by lines of code written."; collection-fit:R01 "Do not measure programmer productivity in lines of code." |
| S4 | Write the least code the goal permits. | enemies:R02 "Write the least code that does the job."; demands:R02 "Write as little code as the goal permits." |
| S5 | Repay code debt by rewriting or deleting the code. | demands:R03 "Repay code debt by rewriting or deleting the code." |
| S6 | Charge every line of code for understanding, debugging, maintaining, and adapting it. | distinctions-vocabulary:R08 "Charge every line of code for understanding, debugging, maintaining, and adapting it." |

S2 stays apart from S1 because it adds three limbs (output, productivity, asset); S1 carries the ledger sense only.

## Per statement

### S1 Book a line of code as spent, never as produced

Supports
- L1-02.txt:52 [D] Dijkstra: "if we wish to count lines of code, we should not regard them as "lines produced" but as "lines spent"". States it verbatim.
- L1-06.txt:26 [D] Lee: "LOC (lines of code) numbers should never be taken as an asset measurement." Same paragraph: "This week we took on $10,000 in new debt!" stands for a LOC count. Entails.
- L1-06.txt:24 [D] Lee: "code has ongoing costs. You have to understand it, you have to maintain it, you have to adapt it to new goals over time." Entails.
- L1-05.txt:42 [D] Atwood: "is code that has to be debugged, code that has to be read and understood, code that has to be supported." Subject: "Every new line of code". Entails.
- L1-04.txt:10 [D] Skrenta: "all that code they add to the system, while expanding its capability, also increases a whole basket of costs." Same at skrenta-wayback.txt:25-26. Entails.
- L1-01.txt:12, :14 [L] Hertzfeld (Atkinson): "the rewrite also saved around 2,000 lines of code." Atkinson then "wrote in the number: -2000." Entails: removed lines count as credit.
- L1-03.txt:16 [D] Cunningham: "Every minute spent on not-quite-right code counts as interest on that debt." Entails for immature code only.

Contradicts or limits
- None denies the booking. No text calls a line count an output figure.
- Boundary, not denial: L1-06.txt:24 "Writing code is the means we use to realize that value." and L1-03.txt:16 "A little debt speeds development so long as it is paid back promptly with a rewrite." Lines spent can buy value or speed.
- Boundary, not denial: L2-02.txt:157 "for a rate of 212 lines per sec". A line count appears as machine throughput, not as a booking.

Lanes: lane 1 only. Six authors: Dijkstra (states), Lee (states by analogy), Skrenta, Atwood, Hertzfeld, Cunningham (entail). No lane-2 text states or entails it. The supplement L2-02-dumped-retro.txt is not counted.

Verdict: VERIFIED.

Strictest literal reading: every count of lines of code in any text sits on the cost side, and no text counts lines as produced, achieved, or accomplished.

Texts that would violate it: none clearly. Two counts could be read as lines on the production side: L2-02.txt:157 (212 lines per second) and L1-01.txt:14 (-2000 entered in the weekly lines-written field).

### S2 Count lines of code as cost, never as output, productivity, or asset

Supports
- Cost limb: the S1 quotes (L1-02.txt:52; L1-06.txt:24, :26; L1-05.txt:42; L1-04.txt:10).
- Not productivity: L1-02.txt:52 [D] "This is a very costly measuring unit because it encourages the writing of insipid code".
- Not productivity: L1-01.txt:10 [L] "lines of code was a silly measure of software productivity".
- Not productivity: L1-06.txt:26 [D] "that number doesn’t say anything about whether you’re being productive".
- Not asset: L1-06.txt:26 [D] "LOC (lines of code) numbers should never be taken as an asset measurement."

Contradicts or limits
- L1-06.txt:18 [D] Lee, the source of the asset limb, concedes the exception: "With few exceptions, source code itself is not a valuable commodity."
- L1-06.txt:24 [D] "the code itself is not intrinsically valuable except as tool to accomplish some goal".
- skrenta-wayback.txt:76, :78 [D] Skrenta lists a third curve: "Code that gets better over time." and "This is the frontier." Examples at :80-86: Google's spelling corrector, rule sets improved by people. Also :61-62 "The MD5 function is just great and it always does what we want."
- skrenta-wayback.txt:25-26 [D] code adds "capability" while it adds cost. The L1-04 copy omits :76-86.
- L2-01.txt:133 [D] McIlroy: "It will take some time to develop a useful inventory, and during that time money and talent will be needed."
- L2-01.txt:50 [D] "the cost of offering such an ‘inventory’ need not be nearly 300 times the cost of keeping one routine."
- L2-05.txt:18 [D] Cox: "These packages contain high-quality, debugged code that required significant expertise to develop."
- L2-05.txt:195 [D] "There’s a lot of good software out there."
- L1-06.txt:28 [D] Lee: "one of the most productive statements a team can make is, “This week we removed 10K LOC while preserving all existing functionality!”" A LOC figure serves as a productivity statement.
- Unit note: L2-01 and L2-05 count routines and packages. No lane-2 text counts lines of code as an asset.

Lanes: supporters lane 1 only (Dijkstra, Lee, Hertzfeld, Atwood, Skrenta). Limiting texts: lane 1 (Lee, Skrenta) and lane 2 (McIlroy, Cox).

Verdict: CONTRADICTED on the limbs "never as asset" and "never as output". Lee writes "With few exceptions", which denies "never"; Skrenta's fuller text names code that gains value; McIlroy books routines as stock. The cost limb stands as S1. The "not productivity" limb stands as S3.

Strictest literal reading: no text describes any code, in any unit, as output, productive result, or asset; all code is cost without exception.

Texts that would violate it: L2-01 (:12 "ways of producing useful inventories"; :50, :133); L2-05 (:18, :177, :195); L2-03.txt:38 "the goal of the CPAN is to be the Mother of All Perl Archives"; L2-04.txt:18 (modules whose removal breaks dependents' "stuff"); L2-02.txt:28 "All of these programs were written locally."; L1-03.txt:10 "saving us considerable effort in coding"; L1-06 (:18, :24, :28); L1-04 full text (skrenta-wayback.txt:76-78).

### S3 Do not measure programmer productivity by lines of code

Supports
- L1-01.txt:10 [L] Hertzfeld (Atkinson): "the lines of code metric only encouraged writing sloppy, bloated, broken code." Managers wanted progress "in terms of the amount of code that they wrote" (:8).
- L1-02.txt:52 [D] Dijkstra: "From there it is only a small step to measuring "programmer productivity" in terms of "number of lines of code produced per month"." Followed by "a very costly measuring unit".
- L1-06.txt:26 [D] Lee: "that number doesn’t say anything about whether you’re being productive".
- L1-04.txt:10 [D] Skrenta (entails): "increase the productivity of individual programmers in terms of the expressive power of the code they write." Same at L1-05.txt:12.
- L1-05.txt:35 [D] Atwood (entails): "reduce the volume of code an individual programmer has to read to understand how a program works".
- Supplement, not counted: L2-02-dumped-retro.txt:196 "we do not measure productivity by lines of code".

Contradicts or limits
- L1-06.txt:28 [D] "one of the most productive statements a team can make is, “This week we removed 10K LOC while preserving all existing functionality!”" Lee reports productivity in lines removed.
- L1-02.txt:52 [D] "if we wish to count lines of code, we should not regard them as "lines produced" but as "lines spent"". Counting stays permitted if booked as spent.
- L1-06.txt:26 [D] "The question is entirely, “What did you do with that LOC/debt?”" The count is insufficient; the text does not ban it.
- L1-01.txt:14 [P] Atkinson answers the form in its own unit: "-2000".
- skrenta-wayback.txt:43-44 [D] "re-implement a 10k line solution into a 1k line solution". Lines serve as the unit of improvement.
- No text defends lines written as a productivity measure.

Lanes: supporters lane 1 only. Three authors state it (Hertzfeld, Dijkstra, Lee); two entail it (Skrenta, Atwood). Lane 2 appears only through the uncounted supplement.

Verdict: QUALIFIED. Limit as the texts state it: the ban targets lines produced or written per period; the texts accept lines booked as spent or removed (L1-02.txt:52; L1-06.txt:28). The wording "lines of code written" (tensions:R02) meets VERIFIED. The wording "in lines of code" (collection-fit:R01) meets QUALIFIED.

Strictest literal reading: no text measures, expresses, or reports any programmer's productivity in any count of lines of code, written, removed, or net.

Texts that would violate it: L1-06.txt:28; L1-01.txt:14 and :12; arguably L1-04.txt:10 and skrenta-wayback.txt:43-44 (productivity as less code for the same function); arguably L1-05.txt:35.

### S4 Write the least code the goal permits

Supports
- L1-06.txt:24 [D] Lee: "It’s in our best interest to have as little source code as possible while still being able to accomplish our business goals."
- L1-05.txt:44 [D] Atwood: "you’ll love it enough to write as little of it as possible."
- L1-05.txt:42 [D] "Every time you write new code, you should do so reluctantly, under duress, because you completely exhausted all your other options."
- L1-05.txt:33 [D] Shipley, quoted by Atwood: "Start with brevity. Increase the other dimensions as required by testing."
- L1-04.txt:10 [D] Skrenta: "Less code to do the same thing (and possibly better)."
- L1-01.txt:10 [L] Hertzfeld (Atkinson): "his goal was to write as small and fast a program as possible".
- L1-02.txt:52 [D] Dijkstra (entails via "lines spent").
- L2-02.txt:353 [L] Ritchie and Thompson (weak): "the size constraint has encouraged not only economy but a certain elegance of design".
- L2-05.txt:16 [D] Cox (entails): "Adding a dependency avoids repeating work already done: designing, writing, testing, debugging, and maintaining a specific unit of code."
- L2-01.txt:20 [D] McIlroy (entails): "I claim we have done enough of this to start taking such things off the shelf."

Contradicts or limits
- L1-06.txt:30 [D] "well-written, maintainable code is often more verbose than dense, impenetrable code, but you should always favor maintainability."
- L1-05.txt:35 [D] "I’m not talking about a reductio ad absurdum contest". Brevity is measured by what a reader must read.
- L1-05.txt:31, :33 [D] Shipley: "these dimensions are all in opposition to one another". Brevity is where to start; other dimensions rise "as required by testing".
- L2-02.txt:36 [L] "The size of the new system is about one third greater than the old" and "we considered this increase in size quite acceptable." Reason given: "much easier to understand and to modify".
- skrenta-wayback.txt:47-48 [L] "I’m convinced that it’s harder to write something short and robust than something big and brittle."
- skrenta-wayback.txt:35-37 [D] "The shorter solutions are often better".
- L1-03.txt:16 [D] "A little debt speeds development so long as it is paid back promptly with a rewrite." First-time code ships larger and gets rewritten.
- L2-05.txt:141 [D] "it may be simplest to make a copy of what you need"; :139 "Later we rewrote the execution engine as well, so that no dependencies were left"; :125 "a thin wrapper". Each adds owned code to cut dependency risk.

Lanes: lane 1 states it (Lee, Atwood, Shipley as quoted, Skrenta, Hertzfeld); lane 1 entails it (Dijkstra). Lane 2 entails it in part (McIlroy, Cox through reuse; Ritchie and Thompson through economy).

Verdict: QUALIFIED. Limits as the texts state them: "you should always favor maintainability" (L1-06.txt:30); brevity first, other dimensions "as required by testing" (L1-05.txt:33); a larger system "quite acceptable" when easier to understand and modify (L2-02.txt:36).

Strictest literal reading: for every task the author writes the minimum possible amount of code, by lines, bytes, or tokens, with no allowance for readability, safety, testing, or effort.

Texts that would violate it: L2-02.txt:36; L1-06.txt:30; L1-05.txt:33 and :35; L1-03.txt:16; L2-05.txt:117, :125, :139, :141; arguably L2-01.txt:50 (an inventory of 300 routines).

### S5 Repay code debt by rewriting or deleting the code

Supports
- L1-03.txt:16 [D] Cunningham: "A little debt speeds development so long as it is paid back promptly with a rewrite."
- L1-03.txt:12 [L] "Mature sections of the program have been revised or rewritten many times providing the consolidation".
- L1-06.txt:36 [D] Lee: "start paying down the debt. Bust out your delete key and start whacking."
- L1-06.txt:28 [D] Lee: removing 10K LOC "contributes to your organization’s long-term health in the same way as reducing your financial debt."
- L1-01.txt:12 [L] Hertzfeld (Atkinson): "completely rewritten the region engine using a simpler, more general algorithm". Rewrite and deletion, no debt vocabulary.
- L2-02.txt:355 [L] Ritchie and Thompson: "we were willing to revise and rewrite the system and its software when new ideas were invented". Rewrite practice, no debt vocabulary; also :36 "it was rewritten in C".
- skrenta-wayback.txt:50 [D] Skrenta: "I've been looking for ways to get code out of the code." Removal, no debt vocabulary.

Contradicts or limits
- L1-03.txt:16 [D] debt may be carried: "A little debt speeds development"; the deadline is "promptly". Also "Objects make the cost of this transaction tolerable."
- L1-06.txt:36 [D] "it’s got to be done very carefully, especially if you don’t have the safety net of unit or automated acceptance tests".
- L1-06.txt:28 [D] deletion "while preserving all existing functionality".
- L1-06.txt:30 [D] repayment may be "refactor existing code to meet changing requirements", not deletion.
- Object of "debt" differs: L1-03.txt:16 "Although immature code may work fine" (immature code); L1-06.txt:20 "Source code is akin to financial debt." (all code).
- L1-03.txt:18 "using our debt analogy" and L1-06.txt:20 "akin to" label the frame an analogy; L1-02.txt:12 "the analogies become too shallow, and the metaphors become more misleading than illuminating".
- L2-05.txt:113 [L] "the author of left-pad deleted that package from NPM, inadvertently breaking most Node.js users’ builds"; L2-04.txt:14 "I’ve just unpublished all my modules." Deletion carries a cost to dependents.
- No text denies repaying by rewriting or deleting.

Lanes: the debt vocabulary comes from lane 1 only (Cunningham, Lee). Lane 2 shows the act of rewriting (Ritchie and Thompson) without the debt frame.

Verdict: QUALIFIED. Limits as the texts state them: repay "promptly" (L1-03.txt:16); "very carefully" (L1-06.txt:36); "while preserving all existing functionality" (L1-06.txt:28).

Strictest literal reading: every instance of code debt is repaid only by rewriting or deleting the debt-bearing code, promptly, with no exception.

Texts that would violate it: L1-03.txt:16 (carries debt by design); L1-06.txt:30, :36 (refactor; tests first); L2-05.txt:123-141 (abstract, isolate, or copy in place of rewriting; no debt vocabulary); L1-02.txt:12 (rejects the analogy); L2-01, L2-03, L2-04 (no debt frame).

### S6 Charge every line of code for understanding, debugging, maintaining, and adapting it

Supports
- L1-06.txt:24 [D] Lee: "You have to understand it, you have to maintain it, you have to adapt it to new goals over time." Also "The more code you have, the larger those ongoing costs will be."
- L1-05.txt:42 [D] Atwood: "Every new line of code you willingly bring into the world" is code "that has to be debugged", "read and understood", "supported". Only text with the quantifier "every line".
- L1-04.txt:8 [D] Skrenta: "It requires periodic maintenance. It has bugs that need to be found. New features mean old code has to be adapted." Also "The longer it takes a new employee to make sense of your system."
- L2-05.txt:16 [D] Cox: "designing, writing, testing, debugging, and maintaining a specific unit of code".
- L2-05.txt:39 [D] "outsources the work of developing that code—designing, writing, testing, debugging, and maintaining—to someone else".
- L2-05.txt:61 [D] "In the middle of a production outage, you’ll be the one debugging it."
- L1-03.txt:16 [D] Cunningham (partial): "Every minute spent on not-quite-right code counts as interest on that debt."

Contradicts or limits
- L2-05.txt:91 [D] "some code really is “done.” For example, NPM’s escape-string-regexp, shown earlier, may never need to be modified again."
- skrenta-wayback.txt:61-63 [D] "The MD5 function is just great and it always does what we want. We act like all code is like this but most of the interesting parts of the system really aren't." Some code has no upkeep; "most", not all, needs it.
- L1-03.txt:16 [D] interest accrues on "not-quite-right code"; :12 mature sections are consolidated.
- L2-01.txt:26, :28 [D] McIlroy: "he should be able safely to regard components as black boxes"; "therewith consider it done". The user bears no understanding or debugging cost; the supplier does.
- L1-02.txt:56 [D] Dijkstra: "the term “software maintenance”, as a result of which many people continue to believe that programs ... are subject to wear and tear". Opposes Skrenta's "It rots" (L1-04.txt:8) and the "maintaining" limb read as upkeep against wear.

Lanes: supporters from both lanes. Lane 1: Lee, Atwood, Skrenta. Lane 2: Cox. Four authors.

Verdict: QUALIFIED. Limits as the texts state them: "some code really is “done”" (L2-05.txt:91); "most of the interesting parts", not all (skrenta-wayback.txt:62-63).

Strictest literal reading: each line of code, with no exception, incurs an ongoing cost in each of four activities: understanding, debugging, maintaining, adapting.

Texts that would violate it: L2-05.txt:91; skrenta-wayback.txt:61-63; L2-01.txt:26, :28; L1-03.txt:12, :16; L1-02.txt:56 on the word "maintaining".

## Summary table

| # | Verdict | Supporting authors | Limiting text |
|---|---|---|---|
| S1 | VERIFIED | Dijkstra, Lee, Skrenta, Atwood, Hertzfeld, Cunningham (lane 1) | none; boundary L1-03.txt:16 |
| S2 | CONTRADICTED | Dijkstra, Lee, Hertzfeld, Atwood, Skrenta (lane 1) | L1-06.txt:18; skrenta-wayback.txt:76-78; L2-01.txt:50, :133 |
| S3 | QUALIFIED | Hertzfeld, Dijkstra, Lee (state); Skrenta, Atwood (entail); lane 1 | L1-06.txt:28; L1-02.txt:52 |
| S4 | QUALIFIED | Lee, Atwood (with Shipley), Skrenta, Hertzfeld (state); Dijkstra, McIlroy, Cox, Ritchie and Thompson (entail); both lanes | L1-06.txt:30; L1-05.txt:33; L2-02.txt:36 |
| S5 | QUALIFIED | Cunningham, Lee (debt vocabulary); Hertzfeld, Ritchie and Thompson (rewrite practice) | L1-03.txt:16; L1-06.txt:36, :28 |
| S6 | QUALIFIED | Lee, Atwood, Skrenta, Cox; both lanes | L2-05.txt:91; skrenta-wayback.txt:62-63 |
