BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines through `</instruction_matrix>`); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full
INTERPLAY: All four demand the primary text over its name and command over hedge; manifesto-writing pulls toward naming, cutting, and drafting while the brief permits a working focus only, and Strunk's judgment latitude pulls against First Principles' refusal to inherit; resolved: the skill's enemy-distinction-choice frame selects candidates and writes none of their sentences, every field is a cited atom, and an inherited rating yields to its verification verdict.
COMMIT: I must derive each candidate from cited report rows, and I will cite a report id and a source location in every field; I must not draft, title, or tag, and I will write only working focuses and one-line statements; I must grade an axiom by its verification verdict, and I will grant AXIOM to S1 alone and carry each QUALIFIED limit verbatim; I must omit needless words, and I will hold each cell to one fact.
# Latent Manifestos — Discovery Candidates
> Basis: 10 reports — 7 surveys, 1 verification (verify-axioms.md, six statements S1–S6), 1 resolution (skrenta-resolution.md), 1 stack map (stack-options.md, 13 options, 20 stacks); OWNER-RULING-2026-10-11.md; 4 Tier 0 audits; 2 indexes; 11 substrate texts (L1-04 cited from L1-04-full.txt), 41 adjacent texts (breadth.md ADJ-01–ADJ-41) plus 25 second sources (evidence.md).

Paths. Bare report names sit in /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/; `deep-dives/x.md` in /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/; `{ID}.txt` in /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/; `kiss.md:163` = /home/user/LLM_MANIFESTOS/manifestos/kiss.md:163; ADJ files in /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/discovery/breadth/.
Rules applied. AXIOM only on a VERIFIED verdict (verify-axioms.md:44 is the only one); QUALIFIED verdicts carry their limit verbatim; S2 is CONTRADICTED (verify-axioms.md:73) and appears as no axiom. Every bindable demand is a capability reading, UNVERIFIED as model behavior (demands.md:250); no substrate text addresses a language model (collection-fit-F187). Owner ruling in force: "the current contents of manifestos are malleable" (OWNER-RULING-2026-10-11.md:3). Candidates appear in rank order.

## Candidate 1 — borrowed code priced at evaluation and ownership, not installation
- **Enemy:** adoption decided by ease — "let's see what happens" · L2-05.txt:41, :179 · enemies.md C5 (:246), enemies-F47, enemies-F156 · collection-fit-F147 (E-B). Model form: "all models converge on the same small set of risky release versions" (breadth-F76, ADJ-35).
- **Core distinction:** installing a dependency versus evaluating and maintaining it · L2-05.txt:193 ("eliminated the cost of downloading and installing" / "the cost of the kind of evaluation and maintenance necessary to use a dependency") · distinctions-vocabulary-F155, R10.
- **Stack option:** O1-B — new file, no re-cut; FP-B's 23 claimed rows read SHARE (stack-options.md:321). O3a declined: its 7 rows (kiss.md:70, :131; dry.md:143; simple-made-easy.md:98, :158; postgres.md:95; yagni.md:95; stack-options.md:328) name a generated-code error rate, in-house shared libraries, an ORM, pasted SQL, and licences, none a registry package (collection-fit-F121, F124, F125); 16 SHARE rows stay either way (stack-options.md:438). O3b declined: kiss.md:28 leaves (kiss 2.0.0→3.0.0) and postgres.md loses 12 of 27 rows (stack-options.md:329, :441-442). Held ground of every file unchanged.
- **Axioms rest on:** S6 (QUALIFIED) — Cox supplies three of its supports, L2-05.txt:16, :39, :61 (verify-axioms.md:172-174).
- **Axioms** (at most five):

| # | Axiom (one imperative sentence) | Rating (AXIOM · CANDIDATE) | Sources (IDs) | Reports (path : id) |
|---|---|---|---|---|
| 1 | Inspect a dependency before adopting it. | CANDIDATE — single substrate author; limit: "No amount of source-level verification or scrutiny will protect you from using untrusted code." (breadth-F18, ADJ-13) | L2-05 | breadth.md : R09; demands.md : R09; enemies.md : R05; collection-fit.md : R06 |
| 2 | Separate the cost of installing code from the cost of evaluating it. | CANDIDATE — one statement (L2-05.txt:193) | L2-05 | distinctions-vocabulary.md : R10 |
| 3 | Count the lines you depend on, not only the lines you write. | CANDIDATE — L1-06.txt:34 counts checked-in lines only | L1-03, L2-05, L2-02-dumped-retro; against L1-06, L2-01 | tensions.md : R06 |
| 4 | Copy the small part you need instead of depending on the whole package. | CANDIDATE — proverb, no measurement (breadth R07); second voice "Find the dependencies — and eliminate them." (breadth-F67, ADJ-23) | L2-05; against L1-06, L2-01 | tensions.md : R10; demands.md : R11 |
| 5 | Charge every line of code for understanding, debugging, maintaining, and adapting it. | CANDIDATE — QUALIFIED, limit verbatim: Limits as the texts state them: "some code really is “done”" (L2-05.txt:91); "most of the interesting parts", not all (skrenta-wayback.txt:62-63). [= L1-04-full.txt:26] | L1-04, L1-05, L1-06, L2-05 | verify-axioms.md : S6 (:186); distinctions-vocabulary.md : R08 |

- **Bindable demands:**

| Demand (one imperative sentence) | Literal check | Sources (IDs) | Reports |
|---|---|---|---|
| Learn about a package before depending on it. | the response states provenance and maintainers before adding the package | L2-05.txt:59 | demands.md : D111 (:477) |
| Read some of a package's code before you depend on it. | the response states which package files it read | L2-05.txt:71 | demands.md : D82 (:448) |
| Run the package's own tests during inspection. | the response reports a run of the package's tests | L2-05.txt:117 | demands.md : D89 (:455) |
| Write tests for the functionality your application takes from the dependency. | the diff that adds the dependency adds tests that call the functions it uses | L2-05.txt:117 | demands.md : D90 (:456) |
| Define your own interface and a thin wrapper over the dependency. | calls to the dependency appear only inside the wrapper module | L2-05.txt:125 | demands.md : D91 (:457) |
| Watch for new indirect dependencies. | an upgrade response lists newly added transitive packages | L2-05.txt:167 | demands.md : D101 (:467) |

Excluded: tool-named practices (gVisor at L2-05.txt:131, hash pinning at :165) fail D-086 (collection-fit-F068).

- **Evidence to declare:**

| Claim | Location ({ID}.txt:line) | In-text status | Corroboration |
|---|---|---|---|
| Koçulu unpublished 273 packages, left-pad among them, 22 March 2016 | L2-04.txt:14; L2-05.txt:113 | VERIFIED (evidence E125, E140) | VERIFIED — npm post-mortem (evidence R06; breadth-F42) |
| The outage lasted 2.5 hours | ADJ-15 npm-kik-leftpad.txt:128 | n/a | VERIFIED (breadth-F43; evidence-F056) |
| left-pad was a single 8-line function body | L2-05.txt:113 | VERIFIED (E141) | VERIFIED under a non-blank count; 13 lines with blanks (evidence R07) |
| event-stream carried malicious code for about 2.5 months before discovery | L2-05.txt:133 | VERIFIED (E145) | VERIFIED — 9 Sep to 26 Nov 2018, 78 days (evidence R12; breadth-F44) |
| Equifax breach reached 148 million people | L2-05.txt:147 | VERIFIED (E149) | VERIFIED — House report (evidence R08) |
| Equifax disclosed publicly "on September 4" | L2-05.txt:147 | VERIFIED (E154) | CONTRADICTED — 7 September 2017 (breadth-F39, F40; evidence R09 REJECT); do not declare |
| Chrome isolated each extension at its 2008 launch | L2-05.txt:131 | VERIFIED (E144) | CONTRADICTED (evidence R11 REJECT); do not declare |
| Apache Struts disclosed major RCEs in 2016, 2017, 2018 | L2-05.txt:173 | VERIFIED (E158) | VERIFIED (evidence-F085, F086) |
| NPM held over 750,000 packages | L2-05.txt:22 | VERIFIED (E128) | UNVERIFIED, time-bound January 2019 (evidence R13) |
| Code-generating LLMs name nonexistent packages: at least 5.2% commercial, 21.7% open-source | ADJ-34 spracklen-abs.txt:35 | n/a | VERIFIED MODEL, 16 models of 2024 (breadth-F74; R11) |
| Of tasks where models specify versions, 36.70%–55.70% contain a known CVE | ADJ-35 wang-vulndeps-abs.txt:33 | n/a | VERIFIED MODEL, 10 models incl. Claude-Sonnet-4.6, preprint May 2026, no replication (breadth-F75; R12) |
| xz backdoor shipped in the 5.6.0 and 5.6.1 release tarballs | ADJ-20 freund-xz.txt:115, :123-124 | n/a | VERIFIED (breadth-F49, F50) |

Declare without paper identifiers: D-205, D-206 (collection-fit-F025, F026); the reviewer counts every example as a demand (collection-fit-F184).

- **Boundary — where the principle stops:** borrowing stays the default once vetted — "Software reuse is finally here" (L2-05.txt:177; tensions-F092), "Any such product is cheaper to buy than to build afresh." (breadth-F56, ADJ-28), risk "multiplied by zero" for hobby code (L2-05.txt:53) · counter-texts absorbed: inspection lowers, never removes, risk (breadth-F18); new releases carry attacks (breadth-F50); npm names "abrupt unpublishing" as the left-pad cause (breadth-F37), so declare the outage, not L2-04's corporate-power reading.
- **Tensions it must resolve:**

| Tension (T-id) | Side A (ID) | Side B (ID) | Question to resolve |
|---|---|---|---|
| T01 (tensions.md:299) | L1-05 (L1-05.txt:42) | L2-01 (L2-01.txt:28) | When a line is borrowed, do its debugging, reading, and support costs pass to the supplier or stay with the borrower? |
| T18 (:316) | L2-01 (L2-01.txt:26) | L2-05 (L2-05.txt:61) | Is borrowed code a black box to trust, or code the borrower must read and debug? |
| T03 (:301) | L1-06 (L1-06.txt:32) | L2-05 (L2-05.txt:141) | Below what size, or above what risk, does a manifesto prefer writing or copying to importing? |
| T20 (:318) | L2-01-discussion (L2-01-discussion.txt:22) | L2-05 (L2-05.txt:20) | At what size does a borrowed unit repay the overhead of borrowing it? |
| T26 (:324) | L2-05 (L2-05.txt:177) | L2-05 (L2-05.txt:39) | Under what conditions is reuse a benefit rather than an unsafe act? |
| T07 (:305) | L1-02 (L1-02.txt:54) | L2-05 (L2-05.txt:79) | What may a passing test license a reader to conclude about code that is added, deleted, or borrowed? |

- **Differentiation:**

| Existing manifesto (file) | Ground it holds (file:line) | What this candidate adds, sharpens, or opposes |
|---|---|---|
| postgres.md | "Every system you add is a permanent line item" (postgres.md:228); "What ships in the box. What you already own." (:230) | sharpens: packages, not systems (collection-fit.md:295; F118, F119) |
| kiss.md | "Every line of code you add is a line you must understand. If you don't understand it, don't merge it." (kiss.md:238); "AI sloppiness: Generated code without comprehension, additions without understanding" (:28) | sharpens: downloaded code the adopter neither wrote nor read (collection-fit-F153; L2-05.txt:39); generated code stays kiss ground |
| correct-by-construction.md | "The industry worships quick starts." (:19) | sharpens: dependency managers drive that cost "approximately to zero" (L2-05.txt:33; collection-fit-F160) |
| dry.md · simple-made-easy.md | ""Shared libraries" become bottlenecks…" (dry.md:143); "Every hidden dependency is a trap waiting for the next maintainer." (simple-made-easy.md:57) | none: in-house coupling (collection-fit-F121, F122) |
| yagni.md | "One-third of IT budgets spent on licenses for bloated software nobody fully understands." (yagni.md:95) | adds evaluation cost beside licence cost |
| all twelve | 0 lines on package, npm, supply chain, registry, transitive, sandbox (collection-fit-F125) | occupies empty ground |

- **Reader and register the substrate supports:** Reader — the model as adopter: a bound model reads every "you" as itself (deep-dives/doctrine-audit.md D-223; collection-fit-F186), and MODEL failures in adoption are measured (breadth-F74, F75); tool-builder, language, and hiring demands are HUMAN-only and drop (demands.md D106–D108, D139). Register — declarative procedure: L2-05's verb-headed sections (distinctions-vocabulary-F086) meet the imperative-mood rule (deep-dives/doctrine-audit.md D-311) and the declarative register of dry.md and correct-by-construction.md (deep-dives/corpus-audit.md:28-29); Cox's hedges marked CUT (demands-F045; collection-fit-F097, F098).
- **Sources drawn on:** L2: L2-05, L2-04, L2-01 (counter-pole :20, :26), L2-02 (counter :357) · L1: L1-03 (:12), L1-06 (counter :30-34) · lanes crossed: yes
- **Substrate gaps:** no substrate demand addresses a package that does not exist (breadth-F74; D111 nearest); no text sets the size at which copying beats depending (demands.md R12; T03); every demand rests on Cox alone (demands.md R09–R11, R15); figures dated January 2019 (collection-fit-F192).

## Candidate 2 — code volume booked as spend, not output
- **Enemy:** lines booked as produced — the volume count credited as output · L1-01.txt:10 ("the lines of code metric only encouraged writing sloppy, bloated, broken code"); L1-02.txt:52; L1-06.txt:26 · enemies.md C2 (:243), enemies-F01, F04, F14 · collection-fit-F146 (E-A).
- **Core distinction:** lines spent versus lines produced · L1-02.txt:52 · distinctions-vocabulary-F092; verify-axioms.md S1 (:44).
- **Stack option:** O2a, kiss subset (composed from stack-options.md:326). Rows that move: the four rows under the `### Delete Code` heading (kiss.md:155) — kiss.md:157, :159, :161, :163 (deep-dives/collection-overlap-audit.md:81-84). O2a's other rows stay and read SHARE: kiss.md:65, :66, :72, :73 (kiss's AI-slop figures; :65 is a projection, breadth-F82), :153, :167, :195, :226, :273; yagni.md:78, :85, :99, :103, :109 (:78, :99, :103 name yagni's own enemy term "presumptive", yagni.md:25). O2b declined: yagni.md:25 leaves (1.0.0→2.0.0) and yagni keeps 6 of 24 rows (stack-options.md:327, :426-428). O7a declined: two enemy lines on two bearers; FP-E leaves D-026 and D-088 open (stack-options.md:485-487); FP-E enters as the cost term S6.
- **Held ground after the re-cut:** kiss.md keeps 34 of 38 rows — enemy "Complexity is killing your software." (kiss.md:18), faces (:27, :28), tagline (:3), and description (:6) unchanged; it holds braiding and layers (:42, :52, :131, :187), abstraction on need (:109, :193-203, :294), small units (:167), bottom-up (:226), generated code (:22, :28, :65-73, :232, :234, :238), "Delete before adding" (:273), "Complexity is debt" (:299), "Delete what adds no value." (:311). No thesis-zone row moves (zones: stack-options.md:39), so no major version (MAINTAINERS_GUIDE.md:239). yagni.md, dry.md, simple-made-easy.md: no row moves; held ground as deep-dives/collection-overlap-audit.md:220, :225-226. Sharpening facts: kiss's description names "unbraiding codebases, questioning layers, and resisting AI slop" and no deletion job (kiss.md:6; stack-options.md:414); "The best code is no code." gets one holder (stack-options.md:360). Cost fact: the only prior re-cut moved no row (stack-options.md:513).
- **Axioms rest on:** S1 (VERIFIED); S3, S4, S6 (QUALIFIED).
- **Axioms** (at most five):

| # | Axiom (one imperative sentence) | Rating (AXIOM · CANDIDATE) | Sources (IDs) | Reports (path : id) |
|---|---|---|---|---|
| 1 | Book a line of code as spent, never as produced. | AXIOM | L1-01, L1-02, L1-03, L1-04, L1-05, L1-06 | verify-axioms.md : S1 (:44); enemies.md : R01; tensions.md : R01; distinctions-vocabulary.md : R01 |
| 2 | Do not measure programmer productivity by lines of code. | CANDIDATE — QUALIFIED, limit verbatim: Limit as the texts state it: the ban targets lines produced or written per period; the texts accept lines booked as spent or removed (L1-02.txt:52; L1-06.txt:28). [The wording "lines of code written" meets VERIFIED: verify-axioms.md:99] | L1-01, L1-02, L1-06 | verify-axioms.md : S3 (:99); tensions.md : R02; collection-fit.md : R01 |
| 3 | Write the least code the goal permits. | CANDIDATE — QUALIFIED, limit verbatim: Limits as the texts state them: "you should always favor maintainability" (L1-06.txt:30); brevity first, other dimensions "as required by testing" (L1-05.txt:33); a larger system "quite acceptable" when easier to understand and modify (L2-02.txt:36). | L1-01, L1-04, L1-05, L1-06; L2-02 | verify-axioms.md : S4 (:131); enemies.md : R02; demands.md : R02 |
| 4 | Charge every line of code for understanding, debugging, maintaining, and adapting it. | CANDIDATE — QUALIFIED, limit verbatim as Candidate 1 row 5 (verify-axioms.md:186) | L1-04, L1-05, L1-06, L2-05 | verify-axioms.md : S6; distinctions-vocabulary.md : R08 |
| 5 | Treat deleted lines as progress. | CANDIDATE — two texts, no lane-2 text | L1-01, L1-06 | tensions.md : R07; breadth-F04 (ADJ-02, "pathologically addicted to deleting code") |

- **Bindable demands:**

| Demand (one imperative sentence) | Literal check | Sources (IDs) | Reports |
|---|---|---|---|
| Count lines of code as lines spent, never as lines produced. | no sentence in the response credits added lines as output or achievement | L1-02.txt:52 | demands.md : D04 (:377) |
| Never take lines of code as an asset measurement. | no sentence in the response treats a LOC total as value or productivity | L1-06.txt:26 | demands.md : D41 (:409) |
| Write new code only after exhausting every other option. | the response lists the non-code options it ruled out before adding code | L1-05.txt:42 | demands.md : D33 (:401) |
| Start with the shortest code; add features, speed, flexibility only as testing requires. | every addition beyond the minimum in the diff names the test or requirement that required it | L1-05.txt:33 | demands.md : D32 (:400) |
| Report removed code with preserved functionality as progress. | a reported deletion states the evidence that functionality is preserved | L1-06.txt:28 | demands.md : D47 (:415) |

- **Evidence to declare:**

| Claim | Location ({ID}.txt:line) | In-text status | Corroboration |
|---|---|---|---|
| "lines produced" against "lines spent" | L1-02.txt:52 | VERIFIED (E019) | VERIFIED wording — a 2007 comment quotes EWD 1036 (E019; evidence-F115) |
| Atkinson entered "-2000" on the weekly lines form | L1-01.txt:14 | VERIFIED (E005) | UNVERIFIED — one narrator; CHM retelling only (evidence R02; breadth-F52) |
| The rewrite ran about six times faster and saved about 2,000 lines | L1-01.txt:12 | VERIFIED (E003, E004) | UNVERIFIED (SECONDARY); CHM's QuickDraw size contradicts its own zip (breadth-F51) |
| Ritchie: "we do not measure productivity by lines of code" | L2-02-dumped-retro.txt:196 | VERIFIED | single statement (evidence R26) |
| The C rewrite made UNIX about one third larger, accepted for easier understanding | L2-02.txt:36 | VERIFIED (E082) | VERIFIED — 1978 revision; 1977 "20-40 percent" (evidence R05) — boundary fact |
| Cursor-adopting repositories: +281.3% lines added in month one; complexity +41.6%, warnings +30.3% | ADJ-37 he-cursor-v3.txt:2395, :2404 | n/a | VERIFIED MODEL, models unfixed (breadth-F78, F79); duplicate density null (F80) |
| Model-written functions run shorter than human ones (NLOC 6.89, 5.16, 4.47 against 12.72) | ADJ-40 cotroneo.txt:1374-1376 | n/a | VERIFIED MODEL (breadth-F84) — counter at function level |
| Opus 4.5 and 4.6 "have a tendency to overengineer" | ADJ-41 anthropic-prompting.txt:1227 | n/a | publisher assertion, no measurement (breadth-F85; R14) |

Do not declare: 134K LOC to 5–10% (E054, hedged, unnamed); n^2 communication cost (E045, unmeasured); lines-to-bugs linearity (breadth-F06, unmeasured).

- **Boundary — where the principle stops:** volume yields to maintainability and understanding (L1-06.txt:30; L2-02.txt:36) and stops at code that is "done" (L2-05.txt:91) or "consistent over time" (L1-04-full.txt:26); the count is code read, not symbols (L1-05.txt:35) · counter-texts absorbed: "As if source code rusted." (breadth-F29, ADJ-22) → cost is upkeep, not decay; Parnas calls software "capital" (breadth-F32, ADJ-24) → no asset claim (S2 CONTRADICTED); "“Can you code this in less symbols?”" (breadth-F31, ADJ-07) → no symbol golf; shorter model functions (breadth-F84) → the count is repository volume, not function length.
- **Tensions it must resolve:**

| Tension (T-id) | Side A (ID) | Side B (ID) | Question to resolve |
|---|---|---|---|
| T13 (tensions.md:311) | L1-01 (L1-01.txt:10) | L1-02 (L1-02.txt:52) | Is a line count a meaningless unit to discard, or a cost unit to keep with a negative sign? |
| T12 (:310) | L1-05 (L1-05.txt:40) | L1-06 (L1-06.txt:30) | When the shorter form and the more maintainable form diverge, which wins, and what measures 'shorter'? |
| T08 (:306) | L2-02 (L2-02.txt:36) | L1-04 (L1-04-full.txt:10) | When does added code volume stop being a cost to cut and become a price worth paying? |
| T02 (:300) | L1-06 (L1-06.txt:34) | L2-05 (L2-05.txt:169) | Does 'fewer lines' count lines authored, checked in, read, shipped, or depended on? |
| T04 (:302) | L1-02 (L1-02.txt:72) | L2-01 (L2-01.txt:139) | Does a generated line count as a written line, and does 'no code' include code a generator emits? |
| T09 (:307) | L1-04 (L1-04-full.txt:8) | L1-05 (L1-05.txt:14) | Does the indictment fall on the artifact (code) or on the act (writing it)? |

- **Differentiation:**

| Existing manifesto (file) | Ground it holds (file:line) | What this candidate adds, sharpens, or opposes |
|---|---|---|
| kiss.md | "The best code is no code." (kiss.md:163); "Every line you don't write is a line you don't maintain, test, debug, or understand." (:159); "Less code = fewer bugs." (:161); dead-code deletion (:157) | re-cut: these four rows move here; adds the ledger, which none of the twelve names (collection-fit-F117: 0 lines productivity, asset, liability, ledger) |
| yagni.md | "Build only what you need right now." (yagni.md:60); "Presumptive features are technical debt" (:78) | sharpens: books every line, needed or not (collection-fit-F155); rows SHARE |
| simple-made-easy.md | "More pieces, hanging cleanly, are simpler than fewer pieces tangled together." (:185); "When you simplify, you often end up with more things. This is correct." (:183) | opposes on count (stack-options.md:258); unit question T02 |
| dry.md | "Codebase bloats" (dry.md:95); "AI doesn't factor in long-term costs. It just keeps generating." (:153) | SHARE |

- **Reader and register the substrate supports:** Reader — the model as writer (deep-dives/doctrine-audit.md D-223), bearing L1-05's writer-as-enemy ("you are your own worst enemy", L1-05.txt:16; enemies-F34); the metric's addressee is a manager, HUMAN-only for budgets (demands.md D01; collection-fit-F060). Register — declarative, as kiss.md and yagni.md practice (deep-dives/corpus-audit.md:32, :37), anchored by substrate hinges under 15 words ("Code is bad." L1-04-full.txt:8; "lines spent" L1-02.txt:52; distinctions-vocabulary Aphorisms); neutral against fury stays open (deep-dives/doctrine-audit.md C-22).
- **Sources drawn on:** L1: L1-01, L1-02, L1-03, L1-04 (full), L1-05, L1-06 · L2: L2-02 (:36 boundary), L2-02-dumped-retro (:196), L2-05 (:91 boundary) · lanes crossed: yes, through boundary and supplement only — S1 is lane 1 only (verify-axioms.md:42)
- **Substrate gaps:** no measurement links volume to defects or cost (tensions.md:363); FP-A evidence is one anecdote and one estimate (collection-fit-F061); no text settles generated lines (T04); MODEL evidence covers added volume, not a model booking lines as output (breadth-F78, F85).

## Candidate 3 — shipped code as debt repaid by consolidation
- **Enemy:** the failure to consolidate — upkeep deferred under "if it ain't broke, don't fix it" · L1-03.txt:16; L2-05.txt:145 · enemies.md C4 (:245), enemies-F07, F127, F163.
- **Core distinction:** debt repaid promptly versus debt carried · L1-03.txt:16 ("paid back promptly with a rewrite" / "The danger occurs when the debt is not repaid.") · distinctions-vocabulary-F103, F104.
- **Stack option:** composed — O1-A pattern (new file, no re-cut; stack-options.md:320) on the debt-and-repayment subset of FP-A's claim test (stack-options.md:32); assumes Candidate 2's kiss subset. Debt rows stay SHARE: kiss.md:299 (thesis zone), yagni.md:78 and :103 (name "presumptive"), correct-by-construction.md:25, dry.md:199, postgres.md:53 (stack-options.md row map). Held ground of every file unchanged.
- **Axioms rest on:** S5, S6 (QUALIFIED).
- **Axioms** (at most five):

| # | Axiom (one imperative sentence) | Rating (AXIOM · CANDIDATE) | Sources (IDs) | Reports (path : id) |
|---|---|---|---|---|
| 1 | Repay code debt by rewriting or deleting the code. | CANDIDATE — QUALIFIED, limit verbatim: Limits as the texts state them: repay "promptly" (L1-03.txt:16); "very carefully" (L1-06.txt:36); "while preserving all existing functionality" (L1-06.txt:28). | L1-03, L1-06, L1-01, L2-02 | verify-axioms.md : S5 (:160); demands.md : R03 |
| 2 | Pay back debt promptly. | CANDIDATE — "debt" is unconsolidated code in L1-03, all code in L1-06 (T11) | L1-03, L1-06 | tensions.md : R08; enemies.md : R04; collection-fit.md : R05 |
| 3 | Refactor existing code to meet changing requirements; do not pile new code on old. | CANDIDATE — one statement, two practice reports | L1-06; L1-03 (:12), L2-02 (:355) | demands.md : D50 (AX3) |
| 4 | Upgrade dependencies promptly, after verifying the upgrade. | CANDIDATE — one text, one incident (evidence-F131, F132) | L2-05 | demands.md : R15 |
| 5 | Grow the program incrementally from a working prototype. | CANDIDATE — L1-02 requires proof first | L1-03; against L1-02 | demands.md : R16 |

- **Bindable demands:**

| Demand (one imperative sentence) | Literal check | Sources (IDs) | Reports |
|---|---|---|---|
| Refactor existing code to meet changing requirements; do not pile new code on old. | the diff changes the existing implementation instead of appending a parallel code path | L1-06.txt:30 | demands.md : D50 (:418) |
| Delete code to pay down the debt. | a deletion diff cites the tests that protect behaviour, or states none exist | L1-06.txt:36 | demands.md : D45 (:413) |
| Skim the diffs between your version and the upgrade. | the upgrade response cites the diff or release notes it read | L2-05.txt:151 | demands.md : D98 (:464) |
| Re-run your project-specific tests after an upgrade. | the upgrade response reports a run of the project-specific tests | L2-05.txt:153 | demands.md : D137 (:495) |
| Do not upgrade completely automatically. | the configuration does not auto-merge dependency upgrades | L2-05.txt:155 | demands.md : D99 (:465) |

- **Evidence to declare:**

| Claim | Location ({ID}.txt:line) | In-text status | Corroboration |
|---|---|---|---|
| "Shipping first time code is like going into debt." | L1-03.txt:16 | VERIFIED | VERIFIED meaning — Cunningham 2009: "I'm never in favor of writing code poorly" (breadth-F01, ADJ-01; evidence-F079); video unwatched (evidence R22) |
| WyCash's mature sections were "revised or rewritten many times" | L1-03.txt:12 | VERIFIED, first-hand | none searched |
| The UNIX authors revised and rewrote the system as new ideas arrived | L2-02.txt:355 | VERIFIED, first-hand | none searched |
| Struts flaw disclosed 7 March 2017; first exploitation 10 March | L2-05.txt:147, :159 | VERIFIED (E150, E156) | VERIFIED — House report; second causes: custom legacy systems, a monitor blind 19 months (breadth-F41, F46) |
| Ten small changes cost less than one equivalent large change | L2-05.txt:145 | VERIFIED (E148) | UNVERIFIED — no measurement |
| Complexity rises under change unless work reduces it (Lehman Law II) | ADJ-32 lehman-1980.txt:765-767 | n/a | VERIFIED (breadth-F57) |

- **Boundary — where the principle stops:** repayment is consolidation, not scratch rewrite — "When you throw away code and start from scratch, you are throwing away all that knowledge." (breadth-F65, ADJ-22), which Cunningham's refactoring reading absorbs (breadth-F02); repayment needs tests (L1-06.txt:36) · counter-texts absorbed: upkeep adapts code to change, not wear (L1-02.txt:56; Parnas, "aged even though nobody has touched it", breadth-F27); new releases can carry attacks (breadth-F50).
- **Tensions it must resolve:**

| Tension (T-id) | Side A (ID) | Side B (ID) | Question to resolve |
|---|---|---|---|
| T11 (tensions.md:309) | L1-03 (L1-03.txt:16) | L1-06 (L1-06.txt:20) | Is the liability the code itself, or only code not yet consolidated? |
| T10 (:308) | L1-03 (L1-03.txt:16) | L1-05 (L1-05.txt:33) | Does the work order run write fast and rewrite, or brevity first and add as required? |
| T15 (:313) | L1-02 (L1-02.txt:56) | L1-04 (L1-04-full.txt:8) | Is 'maintenance' the repair of decay, or the adaptation of code to change? |
| T16 (:314) | L1-02 (L1-02.txt:12) | L1-03 (L1-03.txt:18) | May a software rule rest on an analogy, or must each analogy pass the shallowness test L1-02 names? |
| T28 (:326) | L2-01 (L2-01.txt:139) | L1-03 (L1-03.txt:18) | Is software specified and planned before it is built, or grown from a working prototype and consolidated? |

- **Differentiation:**

| Existing manifesto (file) | Ground it holds (file:line) | What this candidate adds, sharpens, or opposes |
|---|---|---|
| kiss.md | "Complexity is debt. It robs you of capital to invest in the future." (kiss.md:299) | sharpens "debt" to Cunningham's sense: shipped understanding, repaid by consolidation (breadth-F02) |
| yagni.md | "Presumptive features are technical debt" (yagni.md:78); L1-03's stand-still frame reused at :103 (collection-fit-F113) | distinct object: needed code shipped early, not unneeded code |
| correct-by-construction.md · simple-made-easy.md | "Pay at compile time or pay forever in production." (correct-by-construction.md:231); "Spend time up front. Think before you type." (simple-made-easy.md:173) | opposes up-front payment: "payment up-front and in-full" (L1-03.txt:18) |
| postgres.md | "Keep calling the wreckage "tech debt" like it's something that happened TO you." (postgres.md:53) | coincides: debt is chosen and owed |
| dry.md | "Delete it. Start over." (dry.md:123); "Inline the code. Delete unused bits. Start fresh." (:177) | wrong abstractions only; this candidate repays any immature code |

- **Reader and register the substrate supports:** Reader — the model editing code mid-life (deep-dives/doctrine-audit.md D-223); L1-03 addresses programmers and the organization (demands-F129), whose stand-still claim is HUMAN (enemies-F97). Register — declarative (deep-dives/corpus-audit.md:28-29, :37); the source is a first-hand experience report whose hedges cut (evidence-F041).
- **Sources drawn on:** L1: L1-03, L1-06, L1-01, L1-04 (full :8, :28), L1-02 (counter :56) · L2: L2-05 (:145–:157), L2-02 (:355) · lanes crossed: yes — C4 holds direct members in both lanes (enemies.md:211)
- **Substrate gaps:** "promptly" has no bound (demands-F167); no text reconciles the debt analogy with L1-02's ban (collection-fit.md R11); the small-change claim is unmeasured (evidence E148); no lane-2 text states repayment as a rule (enemies.md R04).

## Ranking — which to write first
| Rank | Candidate | Deciding reasons (cited) |
|---|---|---|
| 1 | Candidate 1 — borrowed code priced at evaluation and ownership | Empty ground: 0 package-ecosystem lines in the twelve (collection-fit-F125). Measured MODEL failures in its domain, naming current models (breadth-F74, F75, F76). Most bindable demands: 19 in L2-05 (demands.md:246). No re-cut (stack-options.md:321). Persistence 2006–2026 bears on D-027 (breadth-F03, F19, F75). Costs: D-086 failed for tool names (collection-fit-F068); one substrate author (demands.md R09–R11). |
| 2 | Candidate 2 — code volume booked as spend | The only VERIFIED axiom, six authors 1982–2009 (verify-axioms.md:42-44); ledger terms absent from the twelve (collection-fit-F117). Costs: ground held (kiss.md:163; stack-options.md:360), re-cut without precedent (stack-options.md:513); MODEL evidence covers added volume, not the ledger claim (breadth-F78, F84, F85); D-088 and D-090 open (collection-fit.md:294). Order: alone it answers T17 by importing (L1-06.txt:34; tensions.md:315), the act Candidate 1 prices (breadth-F74, F75). |
| 3 | Candidate 3 — shipped code as debt repaid by consolidation | Cross-lane direct cluster (enemies.md:211). Costs: S5 QUALIFIED only (verify-axioms.md:160); T11 and T15 open (tensions.md:309, :313); lane-2 rule from one incident (evidence-F131, F132) with second causes (breadth-F41, F46) and the xz counter (breadth-F50); "debt" already serves five manifestos (stack-options.md row map). |

## More substrate needed
| Candidate | Missing | Kind of primary text that would supply it |
|---|---|---|
| 1 | a second author stating vetting as a rule; a copy-versus-depend cost comparison; a replication of the CVE-version rate on current Claude models; Pike's talk | practitioner text or study (demands.md R09–R11; breadth R07, R12; evidence R25) |
| 1 | a measure of nonexistent-package rates on 2026 models | rerun of the Spracklen study (breadth R11) |
| 2 | a measurement linking line volume to defects or cost; Boehm or McConnell on LOC | study; book primary (tensions.md:363; breadth.md open Q4) |
| 2 | any text on whether generated lines count | author statement on generated code (T04) |
| 3 | a bound on "promptly"; a reconciliation of the debt analogy with L1-02; Cunningham's 2009 video | author text; video (demands-F167; collection-fit.md R11; evidence R22) |
| 3 | a measured cost of small against large changes | study (evidence E148) |

## Focus points rejected
| Focus point | Reason (thin evidence · held by an existing manifesto · contradicted · outside the substrate) | Reports |
|---|---|---|
| FP-C components before systems | contradicted within lane 2 (L2-05.txt:137, :141; L2-01-discussion.txt:22) and held (kiss.md:119; dry.md:27); failed D-026, D-086; claimed rows concern one system (stack-options.md:384); enters Candidate 1 as counter-pole | collection-fit.md FP-C (:296); tensions.md T18, T19 |
| FP-D shallow analogy | held: coincides term for term with first-principles.md:32 (collection-fit-F158); one source, L1-02, which argues by analogy itself (collection-fit-F103–F105) | collection-fit.md FP-D (:297); stack-options.md O1-D |
| FP-E volume past one mind and one team | thin as a file: 9 of 10 rows shared with FP-A or FP-B (stack-options.md:401); HUMAN-only hiring demands; n^2 asserted (evidence R15); enters Candidate 2 as S6 | collection-fit.md FP-E (:298) |
| FP-F author control against registry power | thin: one text (collection-fit.md:299); npm's record contradicts its cause (breadth-F37, F38); a HUMAN-only act (demands.md D81); its outage enters Candidate 1 evidence | collection-fit.md FP-F |
| code as liability, not asset | contradicted: verify-axioms.md S2 (:73); Parnas "capital" (breadth-F32) | verify-axioms.md S2 |
| prove programs instead of testing | contradicted: demands.md R05 REJECT; De Millo, Lipton, Perlis (breadth-F28) | demands.md R05 |
| uniform formats and interfaces | thin: no text names it; lane 2 only; L2-03 PARTIAL | enemies.md C9, R08 |
| headcount and n^2 cost | thin: L1-04 only, asserted | enemies.md C11; evidence.md R15 |

## Research confidence
| Candidate | Confidence | Basis |
|---|---|---|
| 1 | medium | distinction stated once (L2-05.txt:193); incident records VERIFIED (evidence R06, R08, R12); MODEL studies VERIFIED but single and partly preprint (breadth R11, R12); two L2-05 dated claims CONTRADICTED (evidence R09, R11) |
| 2 | medium-high on the distinction, medium on the rest | S1 VERIFIED across six authors (verify-axioms.md:42-44); S3, S4, S6 QUALIFIED; evidence anecdotal (collection-fit-F061) |
| 3 | low | S5 QUALIFIED; T11, T15, T16 open; one-incident lane-2 rule (evidence-F132); contested by Spolsky and Dijkstra (breadth-F65; L1-02.txt:56) |

Single-source claims this synthesis relies on:
- Installation against evaluation cost — L2-05.txt:193 only (distinctions-vocabulary R10).
- Every vetting, wrapping, copying, and upgrade demand — L2-05 only (demands.md R09–R11, R15; collection-fit.md R06–R08).
- "A little copying is better than a little dependency." — a compilation page; the talk unopened (evidence R25; breadth-F86).
- Nonexistent-package rates — one study, 2024 models (breadth R11); CVE-version rates — one preprint, unreplicated (breadth R12); repository volume rise — one study (breadth R13); overengineering — one publisher assertion (breadth R14).
- Outage duration 2.5 hours — npm's post-mortem only (breadth-F43).
- Inspection limit — Thompson's lecture only (breadth-F18).
- "lines produced" / "lines spent" verbatim — L1-02.txt:52 only (collection-fit.md R02).
- The -2000 anecdote — one narrator (evidence R02).
- "we do not measure productivity by lines of code" — L2-02-dumped-retro.txt:196 only (evidence R26).
- Volume as code read — L1-05.txt:35 only (distinctions-vocabulary R06).
- "some code really is “done”" — L2-05.txt:91 only; code "consistent over time" — L1-04-full.txt:26 only.
- "As if source code rusted." — Spolsky 2000 only (breadth-F29); software as "capital" — Parnas 1994 only (breadth-F32).
- "the failure to consolidate" as enemy — L1-03.txt:16 only; its 2009 meaning — one transcript (evidence R22).
- Upgrade-delay rule — L2-05.txt:157, one incident (evidence-F131, F132).

Notification: Three latent manifestos stand in the substrate: borrowed code priced at evaluation and ownership, code volume booked as spend, and shipped code as debt repaid by consolidation. Borrowed code ranks first: no manifesto holds its ground, measured model failures name its enemy, and it needs no re-cut. Volume as spend holds the only verified axiom but must take four rows from kiss.md, and consolidation rests on qualified axioms and open tensions.
