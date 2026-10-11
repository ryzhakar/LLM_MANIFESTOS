BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines through `</instruction_matrix>`); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full, reread after its 2026-10-11 13:33 revision (commit 1f314d1); Stop Yapping — /home/user/LLM_MANIFESTOS/manifestos/stop-yapping.md — full
INTERPLAY: All five demand the primary text over its name and the command over the hedge; manifesto-writing and Stop Yapping pull toward drafting fury while this brief bars prose, and Strunk's judgment latitude pulls against First Principles' refusal to inherit; resolved: every cell is a located atom, the fury lives in rules the writer obeys, never in sample text, and the revised skill's structure rules outrank the shipped reference where they differ.
COMMIT: I must trace every demand, figure, and boundary to a file:line, and I will leave no row without one; I must not draft manifesto prose, titles, or sample paragraphs, and I will write rules, quotes, and numbers only; I must grade each axiom by its verdict, and I will carry each QUALIFIED limit verbatim; I must compress as Stop Yapping compresses, and I will cut every sentence that carries no rule.

# SPEC — drafts/owned-lines

Paths. `{ID}.txt:n` = /home/user/LLM_MANIFESTOS/resources/2026-10-11-code-liability-and-dependencies/primary/{ID}.txt line n (byte-identical to recon/sources/). Bare report names = /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/. `deep-dives/x` = .../manifesto-craft/deep-dives/x. `kiss.md:n` = /home/user/LLM_MANIFESTOS/manifestos/kiss.md. Manifesto line numbers follow the research reports; commit 8fc8aef (2026-10-11) added two frontmatter lines, so live files run +2 (cargo-cult-science.md, zen-of-python.md +3). `skill:n` = /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md line n. The writer reads only L1-02, L1-04-full, L2-05, L1-03 (prompts/build/writer-v1.md:9); every other source enters through quotes below. Nothing here is open: where this spec and the writer disagree, this spec wins.

## 1. Owner decisions (verbatim)

- One manifesto. Axis: quantity and ownership. Core: every shipped line is owned and paid for, typed or pulled. Two distinctions crossed: lines spent versus lines produced (Dijkstra, VERIFIED axiom S1); code owned versus code installed (Cox). The debt-repaid-by-consolidation idea (Cunningham) is a boundary clause inside it, not a section of equal weight.
- Enemy: counting output as progress. For the model reader it is one reflex with two faces: "I added a helper" and "I'll pull in a library for that." The enemy sentence opens the manifesto, in the reader's own mouth.
- Reader: the model. Register: contemptuous, in the voice of stop-yapping.md. Length ceiling 1500 words, body only. Five axioms at most. Bindable lines at least 70%. A "Before you ship" self-check section. The text passes its own rules. Ends with an A/B choice and "Pick."
- Boundary yes, escape never. A clause saying what the enemy is not stays (code that gets better over time is not the enemy; debt taken and repaid is not the enemy). A clause saying when the reader may stop fighting dies.
- Evidence declared flat, never cited, every figure verified in discovery/evidence.md or discovery/breadth.md as VERIFIED. Forbidden: "liability, not asset" as a claim (CONTRADICTED); Cox's Equifax date and Chrome 2008 extension claim; any figure rated UNVERIFIED.
- Theme: software-engineering. Title, tagline, description: writer's choice; tagline at most 8 words, imperative or binary, distinct from every existing tagline (list them in the spec from the overlap audit). Attribution line mandatory: "After" followed by the source authors.
- The four "Delete Code" rows of kiss.md move into this manifesto (kiss.md:157-163 per discovery/stack-options.md); the spec quotes them and tells the writer to absorb their content.

## 2. Thesis

Every shipped line, typed or pulled, is spent, never produced, and the one who ships it owns its cost. Sources: L1-02.txt:52; L2-05.txt:61, :193.

## 3. Enemy sentence candidates

One enemy: counting output as progress. One reflex, two faces: the helper typed, the package pulled. The writer opens the body with candidate 1 verbatim, quoted, as the first line under the title (skill:28; stop-yapping.md:11). Candidates 2 and 3 are spares for review rounds.

1. "Done! I added a helper for the parsing and pulled in a library for the dates."
2. "I'll write a quick helper for that and pull in a package for the rest."
3. "Implemented: four new files, two helpers, one new dependency. Ready for review."

Show the reflex defeating its own goal, a finished task, not a side cost (skill:30): the task ships and the codebase the reader serves grows worse (V3, V4). Never name a second enemy. Enemies other files hold stay theirs (deep-dives/collection-overlap-audit.md:236-249): "Complexity is killing your software." (kiss.md:18); "AI sloppiness: Generated code without comprehension, additions without understanding" (kiss.md:28); "presumptive development" (yagni.md:25); "The industry worships quick starts." (correct-by-construction.md:19); "Every word past the answer is you choosing performance over function." (stop-yapping.md:19).

## 4. Distinctions — the two crossings

| # | distinction | source quote | file:line |
|---|---|---|---|
| D1 | lines spent vs lines produced | "if we wish to count lines of code, we should not regard them as "lines produced" but as "lines spent": the current conventional wisdom is so foolish as to book that count on the wrong side of the ledger." | L1-02.txt:52 |
| D2 | code owned vs code installed | "Dependency managers have essentially eliminated the cost of downloading and installing a dependency. Future development effort should focus on reducing the cost of the kind of evaluation and maintenance necessary to use a dependency." | L2-05.txt:193 |

D2 hinge: installing outsources "designing, writing, testing, debugging, and maintaining" (L2-05.txt:39), never the outage: "In the middle of a production outage, you’ll be the one debugging it." (L2-05.txt:61). A copy is owned too: "You are taking on responsibility for fixing bugs, maintenance, and so on" (L2-05.txt:141). The decision the enemy makes: "Most of the time the entirety of the decision is “let’s see what happens.”" (L2-05.txt:179).

Crossing: typed or pulled, every line lands on the spent side and in the shipper's ownership. Render the crossing as one two-column table, enemy booking left, replacement right (skill:99); rows: a typed line, a pulled line.

Keep verbatim (skill:60): "lines spent", "lines produced", "ledger" (L1-02.txt:52); "consolidate" (L1-03.txt:16).

## 5. Axioms — four

S2 is CONTRADICTED (verify-axioms.md:73) and absent. S5 enters only as boundary B2 (owner: debt is a clause, not a section). Each axiom heads its own section in one sentence of at most 19 words (skill:97, :117); second person allowed; no widening beyond the wording below.

| # | axiom | verdict and limit, verbatim from verify-axioms.md | writer rule |
|---|---|---|---|
| A1 | Book a line of code as spent, never as produced. | VERIFIED (:44). Boundary, not denial (:39): "Writing code is the means we use to realize that value." (L1-06.txt:24); "A little debt speeds development so long as it is paid back promptly with a rewrite." (L1-03.txt:16). | Spent lines may buy value or speed; never call one produced. |
| A2 | Write the least code the goal permits. | QUALIFIED. Limits as the texts state them: "you should always favor maintainability" (L1-06.txt:30); brevity first, other dimensions "as required by testing" (L1-05.txt:33); a larger system "quite acceptable" when easier to understand and modify (L2-02.txt:36). (:131) | Least means least a reader must read: "I’m not talking about a reductio ad absurdum contest" (L1-05.txt:35). Maintainability wins every tie. |
| A3 | Charge every line of code for understanding, debugging, maintaining, and adapting it. | QUALIFIED. Limits as the texts state them: "some code really is “done”" (L2-05.txt:91); "most of the interesting parts", not all (skrenta-wayback.txt:62-63). (:186). skrenta-wayback.txt:62-63 = L1-04-full.txt:26: "We act like all code is like this but most of the interesting parts of the system really aren't." | The charge falls on every line the day it ships, typed or pulled; upkeep falls on most code, not all. "Maintaining" means adapting to change ("adapt it to new goals over time", L1-06.txt:24), never repairing wear (L1-02.txt:56). |
| A4 | Do not measure programmer productivity by lines of code written. | QUALIFIED. Limit as the texts state it: the ban targets lines produced or written per period; the texts accept lines booked as spent or removed (L1-02.txt:52; L1-06.txt:28). The wording "lines of code written" (tensions:R02) meets VERIFIED. The wording "in lines of code" (collection-fit:R01) meets QUALIFIED. (:99) | QUALIFIED; this wording meets VERIFIED. The reader measures its own report: lines written never count; lines removed with behaviour intact may. |

## 6. Bindable demands — sixteen

Bindable: "a reviewer can check compliance at a literal reading of one response or one diff" (demands.md:217). Every demand appears in the body at least once, as a command in its section or as a self-check item (§11 fixes where). Wording below is the content, not the prose; keep each under 20 words with no three-item list.

| # | demand | literal check | trace |
|---|---|---|---|
| 1 | Never credit lines or packages added as progress. | no sentence of the response or summary credits them | D04 (demands.md:377) L1-02.txt:52; D41 (:409) "LOC (lines of code) numbers should never be taken as an asset measurement." L1-06.txt:26 |
| 2 | Before adding code, list the existing code and non-code options you ruled out. | the list precedes the first added line | D33 (:401) "because you completely exhausted all your other options" L1-05.txt:42 |
| 3 | Tie every addition beyond the minimum to the test or requirement that demanded it. | each addition names its test or requirement | D32 (:400), D34 (:402) "Start with brevity. Increase the other dimensions as required by testing." L1-05.txt:33 |
| 4 | Add no function or file that no caller or test in the diff uses. | every new symbol has a caller or test in the diff | D32 (:400) L1-05.txt:33; kiss.md:157 |
| 5 | Delete, in the same diff, the code your change leaves without callers. | no symbol the diff orphans survives it | kiss.md:157; D45 (:413) "Bust out your delete key and start whacking." L1-06.txt:36 |
| 6 | Cite the tests that protect every deletion, or state that none exist. | each deletion names its tests or says none | D45 (:413) "it’s got to be done very carefully" L1-06.txt:36 |
| 7 | Report removed lines as progress only beside proof that behaviour survived. | each reported deletion states that proof | D47 (:415) "while preserving all existing functionality" L1-06.txt:28 |
| 8 | Change the existing implementation; never append a parallel path beside it. | the diff edits the old path and adds no twin | D50 (:418) "simply piling your new stuff on top of the old stuff" L1-06.txt:30 |
| 9 | Before adding a package, state who maintains it and under what license. | both precede the manifest change | D111 (:477) L2-05.txt:59; D133 (:491) L2-05.txt:107 |
| 10 | Name the package files you read before depending on it. | the response lists them | D82 (:448) "Read some of it." L2-05.txt:71 |
| 11 | Run the package's own tests and report the result. | the response reports the run | D89 (:455) L2-05.txt:117 |
| 12 | Call a dependency only through one wrapper that exposes only what the project calls. | no call outside the wrapper; no unused export | D91 (:457), D92 (:458) L2-05.txt:125 |
| 13 | List every transitive package an addition or upgrade brings in. | the response lists them | D101 (:467) L2-05.txt:167 |
| 14 | When a package touches untrusted input, state its vulnerability history. | the response states it | D132 (:490) L2-05.txt:101 |
| 15 | Carry the license and copyright notice with every function copied from a package. | the copy carries the notice | D93 (:459) "preserving appropriate copyright and other legal notices" L2-05.txt:141 |
| 16 | Before any upgrade, cite the diff or release notes you read. | the response cites them | D98 (:464) L2-05.txt:151 |

Excluded: hash pinning, sandboxes (tool-named; candidates.md:36); HUMAN-only rows: hiring, licence budgets, schedules (demands.md:257-261).

## 7. Evidence to declare

Flat, never cited: no author, study, venue, publisher, or "according to" in the body (owner; skill:119). Incident names (left-pad, event-stream, Equifax, Apache Struts, xz) are facts, not citations. A figure's subject is the study's subject ("models", "repositories that took on an AI coding agent"), never "you"; the attack on "you" follows in the next sentence. v1 uses V1, V2, V3, V4, V6, V7 at the places §11 fixes; V8–V15 stay out of v1, and a reviewer may call one in to replace a weaker line.

| # | figure | exact wording allowed | source ID and line | verdict |
|---|---|---|---|---|
| V1 | 5.2% / 21.7% | Models invent package names: on average at least 5.2 percent for commercial models, 21.7 for open ones. | breadth-F74 (breadth.md:138); spracklen-abs.txt:35 | VERIFIED, MODEL; 16 models of 2024 |
| V2 | 36.70–55.70% | Where models pin versions, 36.70 to 55.70 percent of tasks carry a known CVE. Every model converges on the same risky releases. | breadth-F75, F76 (breadth.md:139-140); wang-vulndeps-abs.txt:33 | VERIFIED, MODEL; 10 models incl. Claude-Sonnet-4.6; one preprint, May 2026 |
| V3 | +281.3% | Repositories that took on an AI coding agent added 281.3 percent more lines in month one. | breadth-F78 (breadth.md:142); he-cursor-v3.txt:2395 | VERIFIED, MODEL; underlying models unfixed |
| V4 | +30.3% / +41.6% | Static-analysis warnings rose 30.3 percent. Complexity rose 41.6 percent. Both stayed up. | breadth-F79 (breadth.md:143); he-cursor-v3.txt:2401-2404 | VERIFIED, MODEL |
| V5 | — | no row: the overengineering statement is a publisher assertion with no measurement (breadth-F85, R14); declaring it flat would turn assertion into fact | breadth.md:149, :234 | not declarable |
| V6 | 273; 22 March 2016 | On 22 March 2016 one author unpublished 273 packages. One was left-pad. | evidence R06 (evidence.md:406); E125 (:361); breadth-F42 | VERIFIED |
| V7 | eight lines | left-pad was a single eight-line function body. | E141 (evidence.md:377); L2-05.txt:113 | VERIFIED under a non-blank count; keep "function body" |
| V8 | 2.5 hours | The disruption lasted 2.5 hours. Name Babel if any project; never Ember or React. | breadth-F43 (breadth.md:93); E140 (evidence.md:376) | VERIFIED |
| V9 | 78 days | Malicious code entered event-stream as a new dependency in version 3.3.6. It sat 78 days before discovery. | E145, E157 (evidence.md:381, :393); breadth-F44; L2-05.txt:133, :165, :167 | VERIFIED |
| V10 | 7 and 10 March 2017 | Apache Struts announced a flaw and released the patch on 7 March 2017. Attackers exploited it on 10 March. | E150, E156 (evidence.md:386, :392); L2-05.txt:147, :159 | VERIFIED |
| V11 | 13 May; 148 million | Attackers entered Equifax through that flaw on 13 May. They took data on 148 million people. | E153, E149 (evidence.md:389, :385); breadth-F47 | VERIFIED; second causes exist (breadth-F41, F46): never "the dependency alone" |
| V12 | 2016, 2017, 2018 | Apache Struts disclosed major remote code execution flaws in 2016, 2017, and 2018. | E158 (evidence.md:394); L2-05.txt:173 | VERIFIED |
| V13 | 5.6.0, 5.6.1 | The xz backdoor shipped inside release tarballs 5.6.0 and 5.6.1. | breadth-F49, F50 (breadth.md:99-100) | VERIFIED; pairs with demand 16 |
| V14 | one third | The C rewrite made UNIX about one third larger and much easier to understand and modify. | E082 (evidence.md:318); L2-02.txt:36 | VERIFIED; boundary B4 only |
| V15 | — (law) | A changing program grows more complex unless someone works to reduce it. | breadth-F57 (breadth.md:114); lehman-1980.txt:765-767 | VERIFIED; boundary B2 only |

## 8. Evidence forbidden

| claim | where it tempts | verdict | source |
|---|---|---|---|
| code is "a liability, not an asset"; code is never an asset, never output | L1-06 title; debt rows in kiss, yagni | CONTRADICTED | verify-axioms.md:73; breadth-F32 ("capital") |
| Equifax disclosed publicly on September 4 | L2-05.txt:147 | CONTRADICTED: 7 September 2017 | E154 (evidence.md:390); breadth-F39, F40 |
| Equifax's CEO, CIO, CSO "resigned" | L2-05.txt:147 | report says retired | E155 (evidence.md:391) |
| Chrome isolated each extension at its 2008 launch | L2-05.txt:131 | CONTRADICTED | E144 (evidence.md:380); R11 |
| -2000; about 2,000 lines saved; six times faster | L1-01.txt:12, :14 | UNVERIFIED | E003–E005 (evidence.md:239-241); R02 |
| NPM's 750,000 packages; 30% on escape-string-regexp; almost a thousand dependents; registries over 100,000 | L2-05.txt:22, :33, :35, :113 | UNVERIFIED | E128, E130, E131, E142 |
| n^2 communication costs | L1-04-full.txt:14 | UNVERIFIED | E045 (evidence.md:281); R15 |
| fewer lines means fewer bugs as a measured or linear law | kiss.md:161 | UNVERIFIED; no measurement links volume to defects | breadth-F06; candidates.md:123, :148 |
| 134K LOC rebuildable at 5–10%; 10k-to-1k rewrite; "removed 10K LOC" as event | L1-06.txt:34, :28; L1-04-full.txt:20 | UNVERIFIED or hedged hypothetical | E054, E051; evidence-F076 |
| ten small changes cost less than one large | L2-05.txt:145 | UNVERIFIED | E148 |
| SQLite's 200,000-line file; pcregrep 70X slower | L2-05.txt:75, :119 | UNVERIFIED | E136, E143 |
| code rots, wears, rusts, decays | L1-04-full.txt:8 | contradicted reading | breadth-F29 "As if source code rusted."; L1-02.txt:56; candidates.md:125 |
| model-written functions run long; models duplicate more | — | VERIFIED counters | breadth-F84 (NLOC 6.89, 5.16, 4.47 vs 12.72); breadth-F80 (duplication null) |
| GitClear shares; DORA changelist growth | kiss.md:65-73 | projection, hypothesis, no AI attribution; kiss holds GitClear | breadth-F81, F82, F83; candidates.md:87 |
| CVEs disclosed before the model's cutoff (72.27–91.37%) | wang-vulndeps-abs.txt:33 | no breadth finding rates it | breadth-F75 quotes only 36.70–55.70% |
| vetting makes a package safe | L2-05.txt:57-61 | inspection lowers risk, never removes it | breadth-F18 "No amount of source-level verification or scrutiny will protect you from using untrusted code." |
| Claude overengineers, as fact | breadth-F85 | assertion, no measurement | §7 V5 |
| hobby code: risk "multiplied by zero" | L2-05.txt:53 | escape clause | owner decision 4 |
| "upgrade at once" or "hold upgrades back" as an unconditional rule | L2-05.txt:155, :157; V13 | the rule carries a test condition; new releases carry attacks | evidence-F132; breadth-F50 |

## 9. Boundary clauses — what the enemy is not

Each clause says what the enemy is not; none says when the reader may stop (owner decision 4; skill:70, :72). They sit inside axiom sections (§11), never in a section of their own (skill:95). B2 runs at most two sentences.

| # | the enemy is not | source |
|---|---|---|
| B1 | code that gets better over time | "Code that gets better over time." L1-04-full.txt:34; "This is the frontier." :36 |
| B2 | debt taken and repaid: first-time code shipped, then consolidated | "A little debt speeds development so long as it is paid back promptly with a rewrite." and "The danger occurs when the debt is not repaid." L1-03.txt:16; "consolidation that is key to understanding" L1-03.txt:12; never a licence for sloppy code: "I'm never in favor of writing code poorly" breadth-F01 |
| B3 | code that is done | "some code really is “done.”" L2-05.txt:91; "Code that is consistent over time." L1-04-full.txt:26; the reflex assumes all its code is done: "We act like all code is like this" :26 |
| B4 | more lines that read easier | "you should always favor maintainability" L1-06.txt:30; V14 |
| B5 | vetted reuse | "Software reuse is finally here" L2-05.txt:177; "There’s a lot of good software out there." :195 |
| B6 | lines removed, behaviour intact, reported as progress | A4 limit; L1-06.txt:28 |

## 10. Absorbed from kiss

The four rows under `### Delete Code` (kiss.md:155; live :157) move here (owner decision 7; stack-options.md:107-110; deep-dives/collection-overlap-audit.md:81-84). Carry content, not wording; quote :163 once at most. Never carry :161 as a law (§8).

| row | verbatim | carry as |
|---|---|---|
| kiss.md:157 (live :159) | Remove dead code immediately. Delete speculative "future" code. Delete "just in case" functions. | demands 4, 5 |
| kiss.md:159 (live :161) | Every line you don't write is a line you don't maintain, test, debug, or understand. | A3, both faces: installing skips the writing, never the debugging (L2-05.txt:39, :61) |
| kiss.md:161 (live :163) | Less code = fewer bugs. | A3 charge: "code that has to be debugged" (L1-05.txt:42) |
| kiss.md:163 (live :165) | The best code is no code. | A2 and demand 2: no code is the first option checked; this file becomes its one holder (stack-options.md:418) |

## 11. Structure skeleton

Order fixed (skill:95): title, enemy line, one section per axiom, the self-check, the choice, attribution. No other section. No `---` rule except before the attribution. Every section under 150 words, opening block included (skill:117). Headings: the writer's words, except the self-check heading, which begins "Before you ship".

| # | part | carries | words ≤ |
|---|---|---|---|
| 0 | `#` title | frontmatter title in caps (stop-yapping precedent) | 5 |
| 1 | enemy line + opening block, no heading | candidate 1 as first line; both faces; the reflex defeating its goal with V3, V4; demand 1 | 145 |
| 2 | A1 section | A1 head; D1; ledger words; demands 1, 8; B2 | 145 |
| 3 | A2 section (typed face) | A2 head with limit; demands 2, 3, 4, 5, 15; B1, B4; kiss :157, :163 | 145 |
| 4 | A3 section (pulled face) | A3 head with limit; D2; crossing table; demands 9, 10, 11, 12; V1, V2, V6, V7; B3, B5; kiss :159, :161 | 145 |
| 5 | A4 section | A4 head with limit; demands 6, 7; B6 | 110 |
| 6 | Before you ship | 8–10 numbered checks, each literal (skill:103), covering demands 1–16, with 13, 14, 16 here at least; last line: one failure means rewrite the whole response, not the line | 145 |
| 7 | the choice | A quotes the enemy line (skill:105); B states owned, paid lines; final body line `Pick.` | 60 |
| 8 | attribution | §14 line | 15 |

Total ≤ 915 against the 1500 ceiling; the section caps bind first.

## 12. Register targets

Script: `python3 -I deep-dives/corpus_metrics.py` on the draft (copy into a temp dir; it globs MANIFESTO_DIR). Numbers: deep-dives/corpus-audit.md:19 (stop-yapping), :16 (postgres), :80, :182; floors skill:40, :117.

| metric | stop-yapping | postgres | pass |
|---|---|---|---|
| 2nd-person /1k | 81.6 | 70.5 | ≥ 70 |
| fragments (≤4 words) /1k | 134.2 | 56.2 | ≥ 50; aim 134 |
| ALL-CAPS /1k | 60.5 | 59.6 | ≥ 50 |
| imperative % (heuristic) | 21.5 (est. true 12.9) | 9.9 | ≥ 21.5 |
| max sentence words | 28 | 97 | ≤ 19 |
| mean sentence words | 4.5 | 7.2 | ≤ 7.2 |
| max section words | 232 | 941 | ≤ 149, opening block included |
| hedge /1k outside quotes | 0 | 0.4 | 0 |
| body words | 1140 | 5019 | ≤ 1500 |

Judgment targets (deep-dives/corpus-audit.md:36): opens on the enemy; ends on a choice, last line "Pick."; reader "the model"; register "contemptuous"; a self-check section; an attribution line.

Anti-Claude tells — zero allowed (session.md = /home/user/LLM_MANIFESTOS/orchestration_log/history/2026-05-11/session.md):
1. Lexical: delve, nuanced, robust, leverage, tapestry, very, really, somewhat, quite (skill:125; session.md:24).
2. Three-part lists (skill:127; session.md:24).
3. Summary paragraphs, recaps, signposts — structural helpfulness (skill:127; session.md:24, :28).
4. Parallel overuse: more than three consecutive sentences opening on the same word (skill:127).
5. Uniform sentence weight: fragments never alternate with longer fury lines (skill:127; session.md:24, :32).
6. Zero fragments: below the fragment floor (skill:40).
7. Performed enthusiasm; "I'd be happy" (skill:129; session.md:24).
8. Hedging outside quotation marks: I think, perhaps, maybe, it seems, sort of (skill:129; corpus-audit.md:182).
9. Teaching that dilutes contempt: a diagnosis without its prescription, or a prescription posed as advice (session.md:28; skill:101; conventions.md:49).
10. Behavior-only attacks: the line names what the reader does, never what the reflex makes it (session.md:28; skill:42).

## 13. Reader and voice rules

- Every "you", "your", "yourself" is the model reading the text (owner; skill:24). No human is addressed.
- Humans appear in the third person only: the one paged at the outage, the one who reviews the diff. Never insulted.
- Identity attacks hit the reflex: what counting output makes the reader. Never a person, team, author, maintainer, or company (owner).
- Profanity: three tokens at most, each on the peak line of the opening block or a section; none in tables, demands, or the self-check (owner; skill:44).
- Every accusation carries its command; every command lands as an accusation (conventions.md:49; skill:101).
- No HUMAN-only demand: hiring, budgets, metrics policy, schedules (demands.md:250, :257-261).
- Bindable lines ≥ 70% of non-blank body lines, headings excluded (skill:93; owner). A line counts when it carries a demand checkable at a literal reading; table rows and examples count when they carry or show one. The enemy line, B-clauses, the choice, the attribution, and any `---` rule count in the denominator.
- Active voice, positive form, concrete nouns, no needless words (Strunk rules 10, 11, 12, 13).

## 14. Frontmatter

Fields, all present, in this order (skill:157; /home/user/LLM_MANIFESTOS/generate.py ManifestoMetadata; live stop-yapping.md:2-8):

| field | value |
|---|---|
| title | writer's choice from the finished content (skill:159); differs from every title below |
| tagline | writer's choice; ≤ 8 words (generate.py MAX_TAGLINE_WORDS); imperative or binary; rebinds alone (skill:161); differs from every tagline below after lowercasing and stripping punctuation (generate.py normalize_tagline) |
| version | "1.0.0" (skill:163) |
| theme | "software-engineering" (themes.yaml; owner) |
| description | writer's choice; one line (skill:169); no §8 claim |
| kind | "manifesto" |
| register | "contemptuous" |
| reader | "model" |

Existing titles and taglines (deep-dives/collection-overlap-audit.md:255-268; checked against manifestos/*.md line 3 on 2026-10-11):

| file | title | tagline |
|---|---|---|
| cargo-cult-science.md | Cargo Cult Science | the first principle is that you must not fool yourself |
| correct-by-construction.md | Correct By Construction | invalid states cannot compile |
| dry.md | Knowledge Has One Home | knowledge has one home |
| first-principles.md | The First Principles | atoms, not analogies |
| intervention.md | Trust Nothing, Restore Everything | roots, not canopy |
| kiss.md | Decomplect | incidental is Latin for your fault |
| postgres.md | Respect the Engine | you use 5% of what you bought. |
| self-documenting-code.md | Code Speaks | comments are lies |
| simple-made-easy.md | The Simplicity Manifesto | the confusion is killing you |
| stop-yapping.md | Stop Yapping | answer. shut up. |
| yagni.md | Build For Today | build for today |
| zen-of-python.md | The Zen of Python | refuse to guess |

Attribution, last body line, after one `---` (skill:171; owner decision 6):
`*After Edsger W. Dijkstra, Russ Cox, Ward Cunningham, Rich Skrenta, Jeff Atwood, Eric Lee, Dennis M. Ritchie, and Ken Thompson*`
Basis: the four substrate files plus every author whose line §4–§10 carries (L1-05, L1-06, L2-02). Hertzfeld is out: no L1-01 content survives §8.

## 15. Reviewer rubric

One block per reviewer (prompts/build/review-shared.md:9). Each lists every failure with its draft line; pass means zero failures unless the block says otherwise.

**Accuracy.** Rate every figure VERIFIED, QUALIFIED, UNVERIFIED, or CONTRADICTED against its §7 source (skill:143). Every figure matches its §7 wording and limit; every quote matches its source verbatim; no §8 claim in any wording; no axiom beyond its §5 limit. Pass: every figure VERIFIED, zero mismatches.

**Completeness.** Present: candidate 1 as the first line under the title; both faces; D1 and D2; A1–A4, each heading its section with its limit carried; demands 1–16, each as a command or a self-check item at its §11 place; the content of kiss.md:157, :159, :161, :163; V1, V2, V3, V4, V6, V7; B1–B6; the "Before you ship" section; A/B with A quoting the enemy line; final body line "Pick."; the §14 attribution. Pass: nothing missing.

**Boundaries.** Every B-clause says what the enemy is not. No sentence tells the reader when it may stop: hobby code, deadlines, prototypes, small diffs, a user's request. B2 ≤ 2 sentences, no heading. A2 carries maintainability; A3 carries "most, not all". Pass: B1–B6 present, zero escape clauses.

**Scope-facts.** Every claim traces to §4–§10. No ground restated from another file beyond the four kiss rows: kiss's enemy, yagni's "presumptive", postgres's "what ships in the box" and "permanent line item", dry's duplication. No HUMAN-only demand. Frontmatter per §14. Pass: zero.

**Precision.** Every "you" is the model; every figure's subject matches its study (§7); every demand is checkable at one response or one diff; "maintaining" never means wear; no hedge outside quotes. Report the bindable ratio as numerator/denominator by the §13 count. Pass: ratio ≥ 0.70, zero other failures.

**Register.** Run the §12 script; meet every §12 pass value; list every anti-Claude tell with its line; profanity ≤ 3, at peaks; no attack on a human. Pass: every number met, zero tells.

**Maximalist self-pass.** Treat the draft as a diff. Apply its own demands and its own "Before you ship" checks to it at the strongest literal reading, no allowance for cost or convention (skill:153; owner decision 3). Every line pays for itself: it carries the enemy, an axiom, a demand, a figure, a boundary, or the choice. A line that restates, announces, or summarizes fails. A section deletable without losing a §-item fails. Pass: zero removable lines, body ≤ 1500 words.

## 16. Out of scope

- Editing kiss.md: removing :155–:163, its version, README regeneration. A separate change; no thesis-zone row moves (candidates.md:88).
- O2a's other kiss rows (:65, :66, :72, :73, :153, :167, :195, :226, :273) and the yagni rows: they stay and read SHARE (candidates.md:87).
- Candidate 1 (borrowed code) as its own file; Candidate 3 (debt) beyond B2.
- The size at which copying beats depending (T03): no input sets it (candidates.md:82; demands.md:531). The body states no threshold.
- Whether generated lines count as written (T04): the thesis counts every line the model emits as typed.
- Tool-named practices; HUMAN-only demands; title, tagline, and description wording; any manifesto prose.

Notification: Four axioms stand — S1 VERIFIED, S4 and S6 QUALIFIED, S3 QUALIFIED with its "lines of code written" wording meeting VERIFIED — while S2 stays out as CONTRADICTED and S5 enters only as the debt boundary. Thirteen declarable rows carry figures (V1–V4, V6–V14), six of them fixed for v1, beside one numberless law (V15). The one decision the inputs could not close is the size at which copying a function beats depending on its package, so the body states no threshold.
