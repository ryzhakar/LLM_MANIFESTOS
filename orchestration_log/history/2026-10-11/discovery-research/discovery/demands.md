BOUND: First Principles (/home/user/LLM_MANIFESTOS/manifestos/first-principles.md, full); Strunk SPR v3 (/home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml, full, 2,923 lines read through `</instruction_matrix>`); manifesto-oath SKILL.md (/home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md, full); manifesto-writing SKILL.md (/home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md, full)
INTERPLAY: First Principles ("Dump the Apple Basket", "Verify the Irreducible"), Strunk (definite, concrete, omit needless words), and the oath (primary text over name) converge on a located quote over any paraphrase; manifesto-writing pulls toward commands and cuts while discovery forbids drafting, and Strunk's judgment protocol allows deviation while the brief makes a quote the evidence; resolved: the writing skill serves as a lens for PRESERVE and CUT verdicts and writes no text, and a quote with file:line outranks any judgment.
COMMIT: I must verify each demand against the primary text, and I will quote at most 25 words with file:line; I must not treat a human reader as a language model, and I will label every reader HUMAN and every MODEL-actionable label a capability reading; I must omit needless words, and I will write definite, positive, brief prose; I must not draft or recommend, and I will report facts and ratings only.
# demands — Discovery Survey

## Summary
Eleven primary texts (L1-04 and L2-03 in PARTIAL copies only), the L2-01 discussion, and both indexes were read whole. All eight questions are answered with 126 located demands (74 explicit, 52 implied), 20 candidate-axiom clusters, 14 contradiction pairs, and 16 rated statements (3 AXIOM, 12 CANDIDATE, 1 REJECT). No question stays open, but the PARTIAL copies leave demands unread and no text measures model compliance, so every MODEL-actionable label stays UNVERIFIED as model behavior.

## Texts read
| Source | Index status (FULL · PARTIAL · FAILED) | Read in full? | Questions |
|---|---|---|---|
| L1-01 (Hertzfeld 1982) | FULL | Yes | Q1–Q8 |
| L1-02 (Dijkstra 1988; Smaldone transcription) | FULL | Yes | Q1–Q8 |
| L1-03 (Cunningham 1992) | FULL | Yes | Q1–Q8 |
| L1-04 (Skrenta 2007) | PARTIAL: Atwood's two-paragraph quotation only; original post not retrieved (index-lane1.md:205) | Yes, the copy; the original post is a gap | Q1–Q8 |
| L1-05 (Atwood 2007) | FULL | Yes | Q1–Q8 |
| L1-06 (Lee 2009) | FULL | Yes | Q1–Q8 |
| L2-01 (McIlroy 1968) | FULL | Yes | Q1–Q8 |
| L2-01-discussion (NATO discussion, 1968) | supplementary; not indexed | Yes | Q8 (X9) |
| L2-02 (Ritchie and Thompson 1974) | FULL | Yes | Q1–Q8 |
| L2-03 (Hietaniemi 1995) | PARTIAL: the earlier perl-packrats mail, not the 26 Oct 1995 post (index-lane2.md:354) | Yes, the copy; the 26 Oct post is a gap | Q1–Q8 |
| L2-04 (Koçulu 2016) | FULL | Yes | Q1–Q8 |
| L2-05 (Cox 2019) | FULL | Yes | Q1–Q8 |
| index-lane1.md, index-lane2.md | n/a | Yes | Q1–Q8 |
| L2-02-dumped-retro.txt, L2-03-dumped-bowers.txt | supplementary; not among the eleven | No | none |

Method. Locations read `{ID}.txt:{line} ¶{n}`: the line in /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/{ID}.txt and the blank-line-separated block after the 6-line header (the index's P-number). A script confirmed every quote as an exact substring of the saved copy at its location; I read each in its paragraph. VERIFIED on a row means that check passed. Origin on every row is the cited text. Reader HUMAN on every row: each text addresses human programmers, and no row supports a statement about a language model. Lens verdicts apply the manifesto-writing lists and transform nothing.

## Answers

### Q1. List every imperative sentence in each text, verbatim with location.

Explicit imperatives per text: L1-01 0; L1-02 11; L1-03 0; L1-04 2; L1-05 5; L1-06 4; L2-01 10; L2-02 0; L2-03 8; L2-04 1; L2-05 33. L1-01, L1-03, and L2-02 hold none; their demands appear under Q2. L2-01 states its demands as "I want" and "I do insist" and "should" sentences; each counts as explicit. Reader HUMAN on every row: the texts address human programmers; no row supports a statement about a language model.

| F-id | Finding (one sentence) | Quote (≤ 25 words) | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| demands-F001 | D14 explicit: Approach a radical novelty with a blank mind; refuse to link it to the familiar. | "one has to approach the radical novelty with a blank mind, consciously refusing to try to link it with what is already familiar" | L1-02.txt:14 ¶4 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F002 | D04 explicit: Count lines of code as lines spent, never as lines produced. | "we should not regard them as "lines produced" but as "lines spent" | L1-02.txt:52 ¶23 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F003 | D119 explicit: Do not try to imagine the symbols and manipulations a computer performs. | "we must therefore not try to imagine them" | L1-02.txt:66 ¶30 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F004 | D06 explicit: Call a bug an error. | "no longer calling a bug a bug but by calling it an error" | L1-02.txt:102 ¶48 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: vocabulary |
| demands-F005 | D05 explicit: Never describe a program or machine part with human verbs (wants, knows, expects, believes). | "never refer to parts of programs or pieces of equipment in an anthropomorphic terminology, nor allow your students to do so" | L1-02.txt:104 ¶49 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F006 | D118 explicit: Deal with all elements of a set by working with the set's definition, not the elements. | "deal with all elements of a set by ignoring them and working with the set's definition" | L1-02.txt:122 ¶58 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: moral core |
| demands-F007 | D07 explicit: Reason from the program text, not from its executions. | "We must learn to work with program texts while (temporarily) ignoring that they admit the interpretation of executable code." | L1-02.txt:124 ¶59 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F008 | D08 explicit: Reason about a program without mentioning its behaviours. | "we should reason about programs without even mentioning their possible" | L1-02.txt:126 ¶60 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F009 | D09 explicit: Ban the anthropomorphic metaphor. | "in computing science the anthropomorphic metaphor should be banned" | L1-02.txt:128 ¶61 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F010 | D12 explicit: Teach programming on a language that cannot be run, so students cannot test. | "students are protected from the temptation to test their programs" | L1-02.txt:140 ¶67 | SUBSTRATE L1-02 | HUMAN | VERIFIED | CUT: example |
| demands-F011 | D13 explicit: Teach radical novelties. | "Universities should not be afraid of teaching radical novelties" | L1-02.txt:150 ¶72 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F012 | D28 explicit: Increase programmer productivity as expressive power per line of code. | "You should do whatever possible to increase the productivity of individual programmers in terms of the expressive power of the code they write." | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F013 | D29 explicit: Write less code to do the same thing. | "Less code to do the same thing (and possibly better)." | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | HUMAN | VERIFIED | PRESERVE: aphorism |
| demands-F014 | D40 explicit: Look at yourself as the enemy (rhetorical imperative). | "Go look in the mirror." | L1-05.txt:14 ¶4 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: moral core |
| demands-F015 | D32 explicit: Start with the shortest code; add features, speed, flexibility only as testing requires. | "Start with brevity. Increase the other dimensions as required by testing." | L1-05.txt:33 ¶11 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: aphorism |
| demands-F016 | D143 explicit: Code smaller. | "I exhorted developers to Code Smaller" | L1-05.txt:35 ¶12 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: aphorism |
| demands-F017 | D33 explicit: Write new code only after exhausting every other option. | "Every time you write new code, you should do so reluctantly, under duress, because you completely exhausted all your other options." | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F018 | D34 explicit: If no code will not do, write the briefest code. | "If you can’t get away with no code, the next best thing is to start with brevity." | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F019 | D41 explicit: Never take lines of code as an asset measurement. | "LOC (lines of code) numbers should never be taken as an asset measurement." | L1-06.txt:26 ¶10 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F020 | D44 explicit: Favor maintainability over density. | "you should always favor maintainability" | L1-06.txt:30 ¶12 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F021 | D45 explicit: Delete code to pay down the debt. | "Bust out your delete key and start whacking." | L1-06.txt:36 ¶15 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F022 | D46 explicit: Get above water on code debt as soon as possible. | "it’s absolutely critical that you get yourself above water as soon as possible" | L1-06.txt:36 ¶15 | SUBSTRATE L1-06 | HUMAN | VERIFIED | CUT: repetition |
| demands-F023 | D122 explicit: Offer software components in families arranged by precision, robustness, generality, and time-space performance. | "should be available in families arranged according to precision, robustness, generality and timespace performance" | L2-01.txt:12 ¶3 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F024 | D53 explicit: Offer each user a component tailored to his need, with no unwanted generality. | "No user of a particular member of a family should pay a penalty, in unwanted generality" | L2-01.txt:26 ¶10 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F025 | D54 explicit: Make components safe to treat as black boxes. | "he should be able safely to regard components as black boxes" | L2-01.txt:26 ¶10 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F026 | D123 explicit: Offer a variety of interface styles for multi-input, multi-output routines. | "Routines that use several inputs and yield several outputs should come in a variety of interface styles." | L2-01.txt:76 ¶33 | SUBSTRATE L2-01 | HUMAN | VERIFIED | CUT: example |
| demands-F027 | D52 explicit: Begin with small components. | "We have to begin thinking small." | L2-01.txt:91 ¶39 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: aphorism |
| demands-F028 | D58 explicit: Compare known schemes in practice before building a product line. | "one ought to do considerable comparison of known schemes working in practical environments" | L2-01.txt:101 ¶44 | SUBSTRATE L2-01 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F029 | D57 explicit: Keep a components pilot plant production-oriented. | "The industrial orientation of a pilot plant must be constantly borne in mind." | L2-01.txt:137 ¶62 | SUBSTRATE L2-01 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F030 | D124 explicit: Staff a components pilot plant like a big software project with the masses of coders removed. | "The personnel of a pilot plant should look like the personnel on many big software projects, with the masses of coders removed." | L2-01.txt:139 ¶63 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F031 | D55 explicit: Engineer similar routines uniformly, with interchangeable options. | "I want the different types of routine in the catalogue that are similar in purpose to be engineered uniformly" | L2-01.txt:153 ¶70 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F032 | D56 explicit: Keep transliteration of a routine to another machine essentially direct. | "but I do insist that transliteration be essentially direct" | L2-01.txt:153 ¶70 | SUBSTRATE L2-01 | HUMAN | VERIFIED | CUT: caveat |
| demands-F033 | D79 explicit: Look around the archive and report what you like and dislike. | "Please take a look around, many looks," | L2-03.txt:24 ¶4 | SUBSTRATE L2-03 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F034 | D77 explicit: Contribute to the archive what it lacks. | "see what CPAN is lacking that _you_ have" | L2-03.txt:37 ¶5 | SUBSTRATE L2-03 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F035 | D129 explicit: Create tidy .tar.gz files of what the archive lacks and place them for the maintainer to fetch. | "please create tidy .tar.gz:s in somewhere" | L2-03.txt:48 ¶6 | SUBSTRATE L2-03 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F036 | D76 explicit: Subdivide each contributed tar according to the archive hierarchy. | "That tar very preferably already subdivided according to the CPAN hierarchy." | L2-03.txt:50 ¶6 | SUBSTRATE L2-03 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F037 | D78 explicit: Volunteer a site to host perl5 extensions. | "some site could volunteer to be the perl5 extension site" | L2-03.txt:56 ¶8 | SUBSTRATE L2-03 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F038 | D73 explicit: Make archives tars, not shars. | "no shars, make them to be tars" | L2-03.txt:63 ¶10 | SUBSTRATE L2-03 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F039 | D74 explicit: Make UNIX archives tars, not zip, lzh, or lha. | "no zips/lzhs/lhas for UNIX stuff, make them to be tars" | L2-03.txt:64 ¶10 | SUBSTRATE L2-03 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F040 | D75 explicit: Compress with gzip, not compress. | "no .Z, use .gz" | L2-03.txt:66 ¶10 | SUBSTRATE L2-03 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F041 | D80 explicit: Point your dependency at the repository directly. | "You can either point your dependency to repo directly (azer/dependency)" | L2-04.txt:18 ¶6 | SUBSTRATE L2-04 | HUMAN | VERIFIED | CUT: example |
| demands-F042 | D82 explicit: Read some of a package's code before you depend on it. | "Read some of it." | L2-05.txt:71 ¶30 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F043 | D83 explicit: Develop your own systematic ways to check code quality. | "Develop your own systematic ways to check code quality." | L2-05.txt:73 ¶31 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F044 | D84 explicit: Ignore rote linter suggestions; focus on semantic problems. | "you should ignore rote suggestions about topics like brace style and focus instead on semantic problems" | L2-05.txt:73 ¶31 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F045 | D85 explicit: Keep an open mind to unfamiliar development practices. | "Keep an open mind to development practices you may not be familiar with." | L2-05.txt:75 ¶32 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: hedge |
| demands-F046 | D88 explicit: Insist on tests in code you outsource. | "you should insist on tests in code you outsource to others" | L2-05.txt:79 ¶34 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F047 | D86 explicit: Find the package's issue tracker. | "Find the package’s issue tracker." | L2-05.txt:85 ¶37 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F048 | D87 explicit: Look at the package's commit history. | "Look at the package’s commit history." | L2-05.txt:89 ¶39 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F049 | D113 explicit: Inspect each transitive dependency as you inspect a direct one. | "each of them should ideally be inspected as described in this section" | L2-05.txt:111 ¶50 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F050 | D89 explicit: Run the package's own tests during inspection. | "The inspection process should include running a package’s own tests." | L2-05.txt:117 ¶53 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F051 | D90 explicit: Write tests for the functionality your application takes from the dependency. | "the next step should be to write new tests focused on the functionality needed by your application" | L2-05.txt:117 ¶53 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F052 | D110 explicit: Turn back if you cannot understand the package's API or it does not do what you think. | "If you can’t or it doesn’t, turn back now!" | L2-05.txt:117 ¶53 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F053 | D135 explicit: Make it easy to migrate your project to a new dependency. | "it is worth the effort to make it easy to migrate your project to a new dependency" | L2-05.txt:123 ¶56 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F054 | D91 explicit: Define your own interface and a thin wrapper over the dependency. | "define an interface of your own, along with a thin wrapper implementing that interface using the dependency" | L2-05.txt:125 ¶57 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F055 | D92 explicit: Wrap only what your project needs from the dependency. | "the wrapper should include only what your project needs from the dependency, not everything the dependency offers" | L2-05.txt:125 ¶57 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F056 | D95 explicit: Avoid a risky dependency, or its most problematic parts. | "the best answer may be to avoid it entirely, or at least to avoid the parts you’ve identified as most problematic" | L2-05.txt:137 ¶63 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F057 | D93 explicit: Copy the tiny fraction you need instead of depending on the whole package. | "If you only need a tiny fraction of a dependency, it may be simplest to make a copy of what you need" | L2-05.txt:141 ¶65 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F058 | D94 explicit: A little copying is better than a little dependency. | "A little copying is better than a little dependency." | L2-05.txt:141 ¶65 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: aphorism |
| demands-F059 | D97 explicit: Upgrade dependencies promptly. | "Upgrading promptly is important" | L2-05.txt:151 ¶70 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F060 | D98 explicit: Skim the diffs between your version and the upgrade. | "you’d want to skim the diffs showing the changes being made from the current version to the upgraded versions" | L2-05.txt:151 ¶70 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F061 | D137 explicit: Re-run your project-specific tests after an upgrade. | "You’ll also want to re-run the tests you’ve written that are specific to your project" | L2-05.txt:153 ¶71 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F062 | D99 explicit: Do not upgrade completely automatically. | "upgrades should not be completely automatic" | L2-05.txt:155 ¶72 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F063 | D136 explicit: Monitor your dependencies and re-evaluate the decision to use them. | "It’s important to continue to monitor them and perhaps even re-evaluate your decision to use them." | L2-05.txt:163 ¶76 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F064 | D100 explicit: Verify that you build against the exact package versions you inspected. | "make sure that you keep using the specific package versions you think you are" | L2-05.txt:165 ¶77 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F065 | D101 explicit: Watch for new indirect dependencies. | "It is also important to watch for new indirect dependencies creeping in" | L2-05.txt:167 ¶78 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F066 | D102 explicit: Periodically revisit a dependency that does not change. | "It’s also important to periodically revisit any dependency that isn’t changing." | L2-05.txt:171 ¶80 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F067 | D103 explicit: Recheck each dependency's security history. | "It’s also important to recheck the security history of each dependency." | L2-05.txt:173 ¶81 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F068 | D138 explicit: Do not ignore the warnings of the Copay and Equifax attacks. | "We should not ignore the warnings." | L2-05.txt:181 ¶85 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: moral core |
| demands-F069 | D104 explicit: Recognize the dependency problem. | "Recognize the problem." | L2-05.txt:185 ¶87 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F070 | D105 explicit: Establish best practices for managing dependencies now. | "Establish best practices for today." | L2-05.txt:189 ¶89 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F071 | D106 explicit: Develop better dependency technology. | "Develop better dependency technology for tomorrow." | L2-05.txt:193 ¶91 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F072 | D107 explicit: Make build tools run a package's own tests easily. | "Build tools should, at the least, make it easy to run a package’s own tests." | L2-05.txt:193 ¶91 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F073 | D108 explicit: Give languages easy ways to isolate a suspect package. | "Languages should also provide easy ways to isolate a suspect package." | L2-05.txt:193 ¶91 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F074 | D109 explicit: Work together to find out how to reuse software safely. | "Let’s work together to find out how to reuse it safely." | L2-05.txt:195 ¶92 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: moral core |

### Q2. List every implied rule — a declarative that prescribes conduct. Quote it and state the rule it implies as one imperative sentence.

| F-id | Finding (one sentence) | Quote (≤ 25 words) | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| demands-F075 | D01 implied: Do not measure engineer progress by lines of code written. | "the lines of code metric only encouraged writing sloppy, bloated, broken code" | L1-01.txt:10 ¶2 | SUBSTRATE L1-01 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F076 | D02 implied: Write the smallest and fastest program that does the job. | "his goal was to write as small and fast a program as possible" | L1-01.txt:10 ¶2 | SUBSTRATE L1-01 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F077 | D15 implied: Detect and reject unwarranted analogies. | "by developing a keen ear for unwarranted analogies, one can detect a lot of medieval thinking today" | L1-02.txt:18 ¶6 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F078 | D120 implied: Think in deep conceptual hierarchies. | "He has to be able to think in terms of conceptual hierarchies that are much deeper than a single mind ever needed to face before" | L1-02.txt:34 ¶14 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F079 | D16 implied: Do not view a program as a device or mechanism. | "To do so, however, is highly dangerous: the analogy is too shallow" | L1-02.txt:40 ¶17 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F080 | D17 implied: Do not cite passing tests as evidence that a program has no errors. | "program testing may convincingly demonstrate the presence of bugs, but can never demonstrate their absence" | L1-02.txt:54 ¶24 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F081 | D19 implied: Do not speak of programs wearing out or needing maintenance. | "Unfathomed misunderstanding is further revealed by the term "software maintenance" | L1-02.txt:56 ¶25 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: vocabulary |
| demands-F082 | D20 implied: View a program as a formula you derive. | "It really helps to view a program as a formula." | L1-02.txt:70 ¶32 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F083 | D10 implied: Present each program together with a proof that it meets its specification. | "The programmer's task is to present such complete conjectures as proven theorems." | L1-02.txt:132 ¶63 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F084 | D121 implied: Give a formal proof that the program meets its functional specification. | "his main task is to give a formal proof that the program he proposes meets the equally formal functional specification" | L1-02.txt:140 ¶67 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F085 | D23 implied: Revise and rewrite mature sections to consolidate. | "Mature sections of the program have been revised or rewritten many times providing the consolidation that is key to understanding" | L1-03.txt:12 ¶3 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F086 | D24 implied: Keep at least general knowledge of the whole codebase. | "Each member of our small engineering team maintains at least general knowledge of all aspects of the roughly four megabytes of source code." | L1-03.txt:12 ¶3 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F087 | D27 implied: Grow the program incrementally from a working prototype. | "We developed the product by incremental growth from a working prototype." | L1-03.txt:12 ¶3 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F088 | D141 implied: Counter discomfort with sudden change by knowing the product and its implementation more completely. | "the best antidote is more complete familiarity with the product and its implementation" | L1-03.txt:14 ¶4 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F089 | D22 implied: Pay back first-time code promptly with a rewrite. | "A little debt speeds development so long as it is paid back promptly with a rewrite." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F090 | D25 implied: Do not let immature code accumulate beyond what one team can master. | "excess quantities will make a program unmasterable" | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: vocabulary |
| demands-F091 | D142 implied: Do not work out a program in full detail before programming begins. | "we recognize this amounts to preserving the concept of payment up-front and in-full" | L1-03.txt:18 ¶6 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F092 | D31 implied: Keep the system quick for a newcomer to understand. | "The longer it takes a new employee to make sense of your system." | L1-04.txt:8 ¶1 | SUBSTRATE L1-04 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F093 | D39 implied: Name the trade-off behind each coding decision. | "To be a master programmer is to understand the nature of these trade-offs, and be conscious of them in everything we write." | L1-05.txt:20 ¶7 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F094 | D37 implied: Reduce the volume of code one programmer must read to understand the program. | "practical, sensible strategies to reduce the volume of code an individual programmer has to read to understand how a program works" | L1-05.txt:35 ¶12 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F095 | D38 implied: Of two equivalent forms, write the smaller. | "It seems obvious to me that the latter case is better because it’s just plain smaller." | L1-05.txt:40 ¶14 | SUBSTRATE L1-05 | HUMAN | VERIFIED | CUT: example |
| demands-F096 | D35 implied: Write no code when the goal can be met without it. | "the best code is no code at all" | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: aphorism |
| demands-F097 | D36 implied: Write as little code as possible. | "you’ll love it enough to write as little of it as possible" | L1-05.txt:44 ¶16 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: aphorism |
| demands-F098 | D42 implied: Treat source code as a liability. | "Source code is a liability, not an asset!" | L1-06.txt:12 ¶3 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: aphorism |
| demands-F099 | D43 implied: Have as little source code as possible while still meeting the goals. | "It’s in our best interest to have as little source code as possible while still being able to accomplish our business goals." | L1-06.txt:24 ¶9 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F100 | D47 implied: Report removed code with preserved functionality as progress. | "This week we removed 10K LOC while preserving all existing functionality!" | L1-06.txt:28 ¶11 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F101 | D50 implied: Refactor existing code to meet changing requirements; do not pile new code on old. | "whether to refactor existing code to meet changing requirements vs. simply piling your new stuff on top of the old stuff" | L1-06.txt:30 ¶12 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F102 | D49 implied: License the third-party package instead of building the same thing. | "in order to avoid paying $1000 or even $500 to license a third-party software package that does the same thing?" | L1-06.txt:32 ¶13 | SUBSTRATE L1-06 | HUMAN | VERIFIED | CUT: aside |
| demands-F103 | D48 implied: Replace home-grown code with common industry-standard libraries. | "it could likely be implemented in about 10% of that, maybe 5%, using common, industry-standard libraries available today" | L1-06.txt:34 ¶14 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F104 | D51 implied: Take standard components off the shelf instead of building them. | "I claim we have done enough of this to start taking such things off the shelf." | L2-01.txt:20 ¶7 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F105 | D61 implied: Use tried parts for the commonplace parts of a system. | "who would be able to use tried parts for all the more commonplace parts of their systems" | L2-01.txt:111 ¶49 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F106 | D60 implied: Demonstrate parameterized families on familiar cases before founding a pilot plant. | "one would be wise to have demonstrated techniques for creating a parameterized family of routines for a couple of familiar purposes" | L2-01.txt:135 ¶61 | SUBSTRATE L2-01 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F107 | D59 implied: Do not standardize before the models exist. | "it would be rash to standardize before we have the models" | L2-01.txt:149 ¶68 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F108 | D69 implied: Accept more code when it buys ease of understanding and modification. | "we considered this increase in size quite acceptable" | L2-02.txt:36 ¶14 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F109 | D72 implied: Leave file structure to the programs, not the system. | "the structure of files is controlled by the programs which use them, not by the system" | L2-02.txt:44 ¶18 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F110 | D62 implied: Have each command read standard input and write standard output. | "the command need merely use the standard file descriptors 0 and 1 where appropriate" | L2-02.txt:243 ¶113 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F111 | D63 implied: Do not give a command output options that a filter in a pipeline provides. | "unwise for efficiency reasons, to expect authors of commands such as ls to provide such a wide variety of output options" | L2-02.txt:259 ¶120 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F112 | D71 implied: Constrain the size of the system. | "the size constraint has encouraged not only economy but a certain elegance of design" | L2-02.txt:353 ¶166 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F113 | D66 implied: Revise and rewrite the system when a better idea arrives. | "we were willing to revise and rewrite the system and its software when new ideas were invented, discovered, or suggested by others" | L2-02.txt:355 ¶167 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F114 | D67 implied: Use the system you build. | "If designers of a system are forced to use that system, they quickly become aware of its functional and superficial deficiencies" | L2-02.txt:355 ¶167 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F115 | D65 implied: Do not insulate programmers from system calls with large access-method layers. | "No large ‘‘access method” routines are required to insulate the programmer from the system calls" | L2-02.txt:357 ¶168 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F116 | D64 implied: Push device-dependent code into the operating system. | "it is also desirable from a space-efficiency standpoint to push device-dependent considerations into the operating system itself" | L2-02.txt:361 ¶170 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F117 | D81 implied: Withdraw your work from a platform that lets a company override the author. | "NPM is no longer a place that I’ll share my open source work at" | L2-04.txt:14 ¶4 | SUBSTRATE L2-04 | HUMAN | VERIFIED | PRESERVE: moral core |
| demands-F118 | D111 implied: Learn about a package before depending on it. | "Before you depend on a package you found on the internet, it is similarly prudent to learn a bit about it first." | L2-05.txt:59 ¶24 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F119 | D112 implied: Do not use a package whose inspection reveals major problems. | "If the inspection reveals major problems, it may be best not to use the package" | L2-05.txt:61 ¶25 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F120 | D131 implied: Check that the package's documentation and API design are clear. | "Is package’s documentation clear? Does the API have a clear design?" | L2-05.txt:67 ¶28 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F121 | D132 implied: If the package processes untrusted input, check its security history. | "Will you be processing untrusted inputs with the package?" | L2-05.txt:101 ¶45 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F122 | D133 implied: Check that the package has an acceptable license. | "Is the code properly licensed? Does it have a license at all?" | L2-05.txt:107 ¶48 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F123 | D134 implied: Exercise the problem areas the inspection identified. | "It is especially worth exercising the likely problem areas identified by the basic inspection." | L2-05.txt:119 ¶54 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F124 | D96 implied: Isolate a suspect dependency at run time. | "It may also be appropriate to isolate a dependency at run-time, to limit the possible damage caused by bugs in it." | L2-05.txt:131 ¶60 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F125 | D114 implied: Track dependency versions through production deployment. | "you need other arrangements to track that information through your production deployment process" | L2-05.txt:149 ¶69 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F126 | D139 implied: Employ engineers who specialize in managing dependencies. | "it may be that we need engineers who specialize in managing dependencies" | L2-05.txt:189 ¶89 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: hedge |

### Q3. To whom does each demand speak — programmer, team, organization, industry, tool builder? Quote the addressee.

| F-id | Finding (one sentence) | Quote (≤ 25 words) | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| demands-F127 | L1-01 speaks to no reader; its implied demands (D01, D02) concern managers who set the metric and the engineer who writes the code. | "track the progress of each individual engineer in terms of the amount of code that they wrote from week to week" | L1-01.txt:8 ¶1 | SUBSTRATE L1-01 | HUMAN | VERIFIED | NONE |
| demands-F128 | L1-02 speaks to educators and department heads ("your students", "your department") and to computing scientists ("we"). | "your department might consider the introduction of fines for violations" | L1-02.txt:104 ¶49 | SUBSTRATE L1-02 | HUMAN | VERIFIED | NONE |
| demands-F129 | L1-03 speaks to programmers and to the engineering organization that carries the debt. | "Not everyone is comfortable with sudden changes in direction, especially programmers." | L1-03.txt:14 ¶4 | SUBSTRATE L1-03 | HUMAN | VERIFIED | NONE |
| demands-F130 | L1-04 speaks to whoever hires and organizes programmers, and to the individual programmer ("You should do whatever possible"). | "Less programmers to hire." | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | HUMAN | VERIFIED | NONE |
| demands-F131 | L1-05 speaks to the individual software developer. | "As a software developer, you are your own worst enemy." | L1-05.txt:16 ¶5 | SUBSTRATE L1-05 | HUMAN | VERIFIED | NONE |
| demands-F132 | L1-06 speaks to developers and teams ("we"), and to the organization that sets metrics. | "Don’t we spend our entire professional careers designing, writing, and testing code?" | L1-06.txt:18 ¶6 | SUBSTRATE L1-06 | HUMAN | VERIFIED | NONE |
| demands-F133 | L2-01 speaks to system builders as customers and to a component-producing industry; its funding demands go to government. | "The market would consist of specialists in system building" | L2-01.txt:111 ¶49 | SUBSTRATE L2-01 | HUMAN | VERIFIED | NONE |
| demands-F134 | L2-02 speaks to authors of commands and to system designers; it states no demand to a reader by name. | "to expect authors of commands such as ls" | L2-02.txt:259 ¶120 | SUBSTRATE L2-02 | HUMAN | VERIFIED | NONE |
| demands-F135 | L2-03 speaks to Perl archivists and archive-site operators; the copy is the earlier perl-packrats mail, not the 26 Oct 1995 post. | "please, Fellow Perl Archivists," | L2-03.txt:35 ¶5 | SUBSTRATE L2-03 | HUMAN | VERIFIED | NONE |
| demands-F136 | L2-04 speaks to dependents of the author's modules. | "if your stuff just got broken due to this" | L2-04.txt:18 ¶6 | SUBSTRATE L2-04 | HUMAN | VERIFIED | NONE |
| demands-F137 | L2-05 speaks to the developer who adopts and maintains dependencies, and to tool builders and language designers ("Build tools should"). | "You would not hire a software developer you’ve never heard of and know nothing about." | L2-05.txt:59 ¶24 | SUBSTRATE L2-05 | HUMAN | VERIFIED | NONE |

Addressee tally, first matching class per demand (126 demands): programmer / developer / designer 76; industry / producer / archive 22; team / organization 19; educator 5; tool builder / language designer 4.

### Q4. Which demands carry a condition or an exception? Quote the condition.

| F-id | Finding (one sentence) | Quote (≤ 25 words) | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| demands-F138 | D119 carries a condition or exception: Do not try to imagine the symbols and manipulations a computer performs. | "they totally baffle our imagination" | L1-02.txt:66 ¶30 | SUBSTRATE L1-02 | HUMAN | VERIFIED | CUT: caveat |
| demands-F139 | D22 carries a condition or exception: Pay back first-time code promptly with a rewrite. | "so long as it is paid back promptly with a rewrite" | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F140 | D32 carries a condition or exception: Start with the shortest code; add features, speed, flexibility only as testing requires. | "as required by testing" | L1-05.txt:33 ¶11 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F141 | D37 carries a condition or exception: Reduce the volume of code one programmer must read to understand the program. | "I’m not talking about a reductio ad absurdum contest where we use up all the clever tricks in our books" | L1-05.txt:35 ¶12 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F142 | D34 carries a condition or exception: If no code will not do, write the briefest code. | "If you can’t get away with no code" | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | HUMAN | VERIFIED | CUT: caveat |
| demands-F143 | D43 carries a condition or exception: Have as little source code as possible while still meeting the goals. | "while still being able to accomplish our business goals" | L1-06.txt:24 ¶9 | SUBSTRATE L1-06 | HUMAN | VERIFIED | CUT: caveat |
| demands-F144 | D44 carries a condition or exception: Favor maintainability over density. | "well-written, maintainable code is often more verbose than dense, impenetrable code" | L1-06.txt:30 ¶12 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F145 | D45 carries a condition or exception: Delete code to pay down the debt. | "it’s got to be done very carefully, especially if you don’t have the safety net of unit or automated acceptance tests" | L1-06.txt:36 ¶15 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F146 | D58 carries a condition or exception: Compare known schemes in practice before building a product line. | "Before constructing a product line for this application" | L2-01.txt:101 ¶44 | SUBSTRATE L2-01 | HUMAN | VERIFIED | CUT: caveat |
| demands-F147 | D60 carries a condition or exception: Demonstrate parameterized families on familiar cases before founding a pilot plant. | "Even before founding a pilot plant" | L2-01.txt:135 ¶61 | SUBSTRATE L2-01 | HUMAN | VERIFIED | CUT: caveat |
| demands-F148 | D59 carries a condition or exception: Do not standardize before the models exist. | "unless the standards encompass the bulk of software systems" | L2-01.txt:149 ¶68 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F149 | D69 carries a condition or exception: Accept more code when it buys ease of understanding and modification. | "Since the new system is not only much easier to understand and to modify" | L2-02.txt:36 ¶14 | SUBSTRATE L2-02 | HUMAN | VERIFIED | CUT: caveat |
| demands-F150 | D63 carries a condition or exception: Do not give a command output options that a filter in a pipeline provides. | "In the absence of the ability to redirect output and input" | L2-02.txt:259 ¶120 | SUBSTRATE L2-02 | HUMAN | VERIFIED | CUT: caveat |
| demands-F151 | D64 carries a condition or exception: Push device-dependent code into the operating system. | "Given the requirement that all programs should be usable with any file or device as input or output" | L2-02.txt:361 ¶170 | SUBSTRATE L2-02 | HUMAN | VERIFIED | CUT: caveat |
| demands-F152 | D74 carries a condition or exception: Make UNIX archives tars, not zip, lzh, or lha. | "such native packing formats are quite ok for non-UNIX stuff" | L2-03.txt:65 ¶10 | SUBSTRATE L2-03 | HUMAN | VERIFIED | CUT: caveat |
| demands-F153 | D111 carries a condition or exception: Learn about a package before depending on it. | "At one end of the spectrum is a personal hobby project, where the cost of most bad outcomes is near zero" | L2-05.txt:53 ¶21 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: caveat |
| demands-F154 | D112 carries a condition or exception: Do not use a package whose inspection reveals major problems. | "If the inspection reveals major problems" | L2-05.txt:61 ¶25 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: caveat |
| demands-F155 | D132 carries a condition or exception: If the package processes untrusted input, check its security history. | "Will you be processing untrusted inputs with the package?" | L2-05.txt:101 ¶45 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: caveat |
| demands-F156 | D90 carries a condition or exception: Write tests for the functionality your application takes from the dependency. | "If the package passes the inspection and you decide to make your project depend on it" | L2-05.txt:117 ¶53 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: caveat |
| demands-F157 | D91 carries a condition or exception: Define your own interface and a thin wrapper over the dependency. | "If the package will be used from many places in your project’s source code" | L2-05.txt:125 ¶57 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: caveat |
| demands-F158 | D95 carries a condition or exception: Avoid a risky dependency, or its most problematic parts. | "If a dependency seems too risky and you can’t find a way to isolate it" | L2-05.txt:137 ¶63 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: caveat |
| demands-F159 | D93 carries a condition or exception: Copy the tiny fraction you need instead of depending on the whole package. | "If you only need a tiny fraction of a dependency" | L2-05.txt:141 ¶65 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F160 | D97 carries a condition or exception: Upgrade dependencies promptly. | "in most cases, delaying an upgrade is riskier than upgrading quickly" | L2-05.txt:157 ¶73 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: caveat |

23 of 126 demands carry a quoted condition or exception; the other 103 state no condition in the text.

### Q5. Mark each demand bindable or not. Bindable means a reviewer can check compliance at a literal reading of one response or one diff. State the check in one line.

47 of 126 demands are bindable; the literal check for each stands in the Demands table (column "bindable"). Patterns follow.

| F-id | Finding (one sentence) | Quote (≤ 25 words) | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| demands-F161 | D41 [bindable] Bindable at one response: a literal ban on a LOC figure as progress. Check: no sentence in the response treats a LOC total as value or productivity. | "LOC (lines of code) numbers should never be taken as an asset measurement." | L1-06.txt:26 ¶10 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F162 | D06 [bindable] Bindable at one response: a vocabulary ban checked by search. Check: the response says "error" and never "bug" for a fault in code. | "no longer calling a bug a bug but by calling it an error" | L1-02.txt:102 ¶48 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: vocabulary |
| demands-F163 | D32 [bindable] Bindable at one diff: each addition beyond the minimum names its test or requirement. Check: every addition beyond the minimum in the diff names the test or requirement that required it. | "Start with brevity. Increase the other dimensions as required by testing." | L1-05.txt:33 ¶11 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: aphorism |
| demands-F164 | D111 [bindable] Bindable at one response: each vetting step yields a stated finding the response can show. Check: the response states provenance and maintainers before adding the package. | "Before you depend on a package you found on the internet, it is similarly prudent to learn a bit about it first." | L2-05.txt:59 ¶24 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F165 | D91 [bindable] Bindable at one diff: structural checks on a dependency (wrapper module, copy with license, lockfile hash). Check: calls to the dependency appear only inside the wrapper module. | "define an interface of your own, along with a thin wrapper implementing that interface using the dependency" | L2-05.txt:125 ¶57 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F166 | D62 [bindable] Bindable at one diff: a command reads standard input and writes standard output. Check: a new command reads fd 0 and writes fd 1 by default and implements no redirection of its own. | "the command need merely use the standard file descriptors 0 and 1 where appropriate" | L2-02.txt:243 ¶113 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F167 | D22 [not bindable] Not bindable: a time word with no bound (promptly, as soon as possible, periodically). Check: "promptly" has no bound. | "A little debt speeds development so long as it is paid back promptly with a rewrite." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F168 | D29 [not bindable] Not bindable: a comparative with no baseline in one response or diff. Check: comparative; needs a baseline. | "Less code to do the same thing (and possibly better)." | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | HUMAN | VERIFIED | PRESERVE: aphorism |
| demands-F169 | D104 [not bindable] Not bindable: an ecosystem or industry demand with no code artifact. Check: no. | "Recognize the problem." | L2-05.txt:185 ¶87 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F170 | D07 [not bindable] Not bindable: a reasoning method with no literal marker. Check: no literal marker separates text-reasoning from execution-reasoning. | "We must learn to work with program texts while (temporarily) ignoring that they admit the interpretation of executable code." | L1-02.txt:124 ¶59 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |

| Text | Demands | Explicit | Implied | Bindable | MODEL-actionable | HUMAN-only |
|---|---|---|---|---|---|---|
| L1-01 | 2 | 0 | 2 | 1 | 2 | 0 |
| L1-02 | 19 | 11 | 8 | 8 | 17 | 2 |
| L1-03 | 7 | 0 | 7 | 0 | 5 | 2 |
| L1-04 | 3 | 2 | 1 | 0 | 3 | 0 |
| L1-05 | 10 | 5 | 5 | 6 | 9 | 1 |
| L1-06 | 10 | 4 | 6 | 5 | 9 | 1 |
| L2-01 | 14 | 10 | 4 | 2 | 2 | 12 |
| L2-02 | 9 | 0 | 9 | 2 | 7 | 2 |
| L2-03 | 8 | 8 | 0 | 3 | 3 | 5 |
| L2-04 | 2 | 1 | 1 | 1 | 1 | 1 |
| L2-05 | 42 | 33 | 9 | 19 | 30 | 12 |

### Q6. Which demands could a language model act on while writing or reviewing code, and which need powers a model lacks — hiring, metrics, budgets, time? Label MODEL-actionable or HUMAN-only.

88 demands are MODEL-actionable and 38 HUMAN-only (Demands table, column "MODEL-actionable or HUMAN-only"). The label reads the tools a model has in Claude Code (read, edit, shell, fetch); it is a capability reading. The eleven texts name no language model and measure no model compliance, so every MODEL-actionable label stays UNVERIFIED as a statement about model behavior. Reader on each row: HUMAN.

| F-id | Finding (one sentence) | Quote (≤ 25 words) | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| demands-F171 | D41 MODEL-actionable (capability reading): a model writing or reviewing a summary can refrain from reporting lines added as progress. | "LOC (lines of code) numbers should never be taken as an asset measurement." | L1-06.txt:26 ¶10 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F172 | D89 MODEL-actionable (capability reading): a model with file and shell tools can read a package's code, run its tests, and report. | "The inspection process should include running a package’s own tests." | L2-05.txt:117 ¶53 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F173 | D91 MODEL-actionable (capability reading): a model editing a diff can wrap, copy, or delete code. | "define an interface of your own, along with a thin wrapper implementing that interface using the dependency" | L2-05.txt:125 ¶57 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F174 | D139 HUMAN-only: hiring. | "it may be that we need engineers who specialize in managing dependencies" | L2-05.txt:189 ¶89 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: hedge |
| demands-F175 | D49 HUMAN-only: a licensing budget. | "in order to avoid paying $1000 or even $500 to license a third-party software package that does the same thing?" | L1-06.txt:32 ¶13 | SUBSTRATE L1-06 | HUMAN | VERIFIED | CUT: aside |
| demands-F176 | D124 HUMAN-only: staffing and funding a pilot plant. | "The personnel of a pilot plant should look like the personnel on many big software projects, with the masses of coders removed." | L2-01.txt:139 ¶63 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F177 | D107 HUMAN-only: tool-builder and language-designer roadmaps. | "Build tools should, at the least, make it easy to run a package’s own tests." | L2-05.txt:193 ¶91 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F178 | D102 HUMAN-only: a schedule over time (periodic revisit). | "It’s also important to periodically revisit any dependency that isn’t changing." | L2-05.txt:171 ¶80 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |

### Q7. Cluster the demands into candidate axioms: one row per cluster, with member quotes and IDs, across lanes where they cross.

One row per cluster and lane carries that lane's key quote; the membership table follows. Clusters that hold a quote from each lane cross the lane boundary.

| F-id | Finding (one sentence) | Quote (≤ 25 words) | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| demands-F179 | AX1 "Count code as cost, never as output or asset." — L1 key quote, member D04 of 4. | "we should not regard them as "lines produced" but as "lines spent" | L1-02.txt:52 ¶23 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F180 | AX1 "Count code as cost, never as output or asset." — L1 key quote, member D41 of 4. | "LOC (lines of code) numbers should never be taken as an asset measurement." | L1-06.txt:26 ¶10 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F181 | AX2 "Write as little code as the goal permits." — L1 key quote, member D32 of 12. | "Start with brevity. Increase the other dimensions as required by testing." | L1-05.txt:33 ¶11 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: aphorism |
| demands-F182 | AX2 "Write as little code as the goal permits." — L1 key quote, member D33 of 12. | "Every time you write new code, you should do so reluctantly, under duress, because you completely exhausted all your other options." | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F183 | AX2 "Write as little code as the goal permits." — L2 key quote, member D71 of 12. | "the size constraint has encouraged not only economy but a certain elegance of design" | L2-02.txt:353 ¶166 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F184 | AX3 "Repay code debt by rewriting or deleting." — L1 key quote, member D22 of 7. | "A little debt speeds development so long as it is paid back promptly with a rewrite." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F185 | AX3 "Repay code debt by rewriting or deleting." — L1 key quote, member D45 of 7. | "Bust out your delete key and start whacking." | L1-06.txt:36 ¶15 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F186 | AX3 "Repay code debt by rewriting or deleting." — L2 key quote, member D66 of 7. | "we were willing to revise and rewrite the system and its software when new ideas were invented, discovered, or suggested by others" | L2-02.txt:355 ¶167 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F187 | AX4 "Keep the whole system within one team's understanding." — L1 key quote, member D25 of 5. | "excess quantities will make a program unmasterable" | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: vocabulary |
| demands-F188 | AX4 "Keep the whole system within one team's understanding." — L1 key quote, member D37 of 5. | "practical, sensible strategies to reduce the volume of code an individual programmer has to read to understand how a program works" | L1-05.txt:35 ¶12 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F189 | AX5 "Take tried parts and libraries instead of writing them." — L1 key quote, member D48 of 4. | "it could likely be implemented in about 10% of that, maybe 5%, using common, industry-standard libraries available today" | L1-06.txt:34 ¶14 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F190 | AX5 "Take tried parts and libraries instead of writing them." — L2 key quote, member D51 of 4. | "I claim we have done enough of this to start taking such things off the shelf." | L2-01.txt:20 ¶7 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F191 | AX5b "Vet a package before you depend on it." — L2 key quote, member D82 of 16. | "Read some of it." | L2-05.txt:71 ¶30 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F192 | AX5b "Vet a package before you depend on it." — L2 key quote, member D111 of 16. | "Before you depend on a package you found on the internet, it is similarly prudent to learn a bit about it first." | L2-05.txt:59 ¶24 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F193 | AX6 "Offer components tailored, in families, safe as black boxes." — L2 key quote, member D53 of 6. | "No user of a particular member of a family should pay a penalty, in unwanted generality" | L2-01.txt:26 ¶10 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F194 | AX6 "Offer components tailored, in families, safe as black boxes." — L2 key quote, member D122 of 6. | "should be available in families arranged according to precision, robustness, generality and timespace performance" | L2-01.txt:12 ¶3 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F195 | AX6b "Contain a dependency: wrap it, copy it, isolate it, or avoid it." — L2 key quote, member D91 of 8. | "define an interface of your own, along with a thin wrapper implementing that interface using the dependency" | L2-05.txt:125 ¶57 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F196 | AX6b "Contain a dependency: wrap it, copy it, isolate it, or avoid it." — L2 key quote, member D93 of 8. | "If you only need a tiny fraction of a dependency, it may be simplest to make a copy of what you need" | L2-05.txt:141 ¶65 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F197 | AX7 "Give parts one small uniform interface so they compose." — L2 key quote, member D55 of 6. | "I want the different types of routine in the catalogue that are similar in purpose to be engineered uniformly" | L2-01.txt:153 ¶70 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F198 | AX7 "Give parts one small uniform interface so they compose." — L2 key quote, member D62 of 6. | "the command need merely use the standard file descriptors 0 and 1 where appropriate" | L2-02.txt:243 ¶113 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F199 | AX8 "Reason from the program text; refuse analogy and anthropomorphic metaphor." — L1 key quote, member D05 of 13. | "never refer to parts of programs or pieces of equipment in an anthropomorphic terminology, nor allow your students to do so" | L1-02.txt:104 ¶49 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F200 | AX8 "Reason from the program text; refuse analogy and anthropomorphic metaphor." — L1 key quote, member D14 of 13. | "one has to approach the radical novelty with a blank mind, consciously refusing to try to link it with what is already familiar" | L1-02.txt:14 ¶4 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F201 | AX9 "Name the trade-off; favor maintainability over density." — L1 key quote, member D39 of 3. | "To be a master programmer is to understand the nature of these trade-offs, and be conscious of them in everything we write." | L1-05.txt:20 ¶7 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F202 | AX9 "Name the trade-off; favor maintainability over density." — L1 key quote, member D44 of 3. | "you should always favor maintainability" | L1-06.txt:30 ¶12 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F203 | AX9 "Name the trade-off; favor maintainability over density." — L2 key quote, member D69 of 3. | "we considered this increase in size quite acceptable" | L2-02.txt:36 ¶14 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F204 | AX10 "Build the ecosystem: practices, standards, tools, and staffing for reuse." — L2 key quote, member D104 of 13. | "Recognize the problem." | L2-05.txt:185 ¶87 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F205 | AX10 "Build the ecosystem: practices, standards, tools, and staffing for reuse." — L2 key quote, member D124 of 13. | "The personnel of a pilot plant should look like the personnel on many big software projects, with the masses of coders removed." | L2-01.txt:139 ¶63 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F206 | AX11 "Teach computing as formal mathematics, without testing." — L1 key quote, member D12 of 2. | "students are protected from the temptation to test their programs" | L1-02.txt:140 ¶67 | SUBSTRATE L1-02 | HUMAN | VERIFIED | CUT: example |
| demands-F207 | AX11 "Teach computing as formal mathematics, without testing." — L1 key quote, member D13 of 2. | "Universities should not be afraid of teaching radical novelties" | L1-02.txt:150 ¶72 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F208 | AX12 "Use the system you build." — L2 key quote, member D67 of 1. | "If designers of a system are forced to use that system, they quickly become aware of its functional and superficial deficiencies" | L2-02.txt:355 ¶167 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F209 | AX13 "Follow the archive's packaging and contribution conventions." — L2 key quote, member D75 of 8. | "no .Z, use .gz" | L2-03.txt:66 ¶10 | SUBSTRATE L2-03 | HUMAN | VERIFIED | CUT: scaffolding |
| demands-F210 | AX13 "Follow the archive's packaging and contribution conventions." — L2 key quote, member D77 of 8. | "see what CPAN is lacking that _you_ have" | L2-03.txt:37 ¶5 | SUBSTRATE L2-03 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F211 | AX14 "Withdraw your work from a platform that overrides the author." — L2 key quote, member D81 of 1. | "NPM is no longer a place that I’ll share my open source work at" | L2-04.txt:14 ¶4 | SUBSTRATE L2-04 | HUMAN | VERIFIED | PRESERVE: moral core |
| demands-F212 | AX15 "Review for semantic faults, not style." — L2 key quote, member D84 of 1. | "you should ignore rote suggestions about topics like brace style and focus instead on semantic problems" | L2-05.txt:73 ¶31 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F213 | AX16 "Upgrade, verify, and watch dependencies continuously." — L2 key quote, member D97 of 10. | "Upgrading promptly is important" | L2-05.txt:151 ¶70 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F214 | AX16 "Upgrade, verify, and watch dependencies continuously." — L2 key quote, member D100 of 10. | "make sure that you keep using the specific package versions you think you are" | L2-05.txt:165 ¶77 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F215 | AX17 "Argue correctness against a specification; never infer it from tests alone." — L1 key quote, member D10 of 3. | "The programmer's task is to present such complete conjectures as proven theorems." | L1-02.txt:132 ¶63 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F216 | AX17 "Argue correctness against a specification; never infer it from tests alone." — L1 key quote, member D17 of 3. | "program testing may convincingly demonstrate the presence of bugs, but can never demonstrate their absence" | L1-02.txt:54 ¶24 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F217 | AX18 "Grow the program incrementally from a working prototype." — L1 key quote, member D27 of 2. | "We developed the product by incremental growth from a working prototype." | L1-03.txt:12 ¶3 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: principle |
| demands-F218 | AX18 "Grow the program incrementally from a working prototype." — L1 key quote, member D142 of 2. | "we recognize this amounts to preserving the concept of payment up-front and in-full" | L1-03.txt:18 ¶6 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: principle |

| Cluster | Candidate axiom | Members (D-ids) | Lanes | Cross-lane |
|---|---|---|---|---|
| AX1 | Count code as cost, never as output or asset. | D01, D04, D41, D42 | L1 | no |
| AX2 | Write as little code as the goal permits. | D02, D28, D29, D32, D33, D34, D35, D36, D38, D43, D71, D143 | L1+L2 | yes |
| AX3 | Repay code debt by rewriting or deleting. | D22, D23, D45, D46, D47, D50, D66 | L1+L2 | yes |
| AX4 | Keep the whole system within one team's understanding. | D24, D25, D31, D37, D141 | L1 | no |
| AX5 | Take tried parts and libraries instead of writing them. | D48, D49, D51, D61 | L1+L2 | yes |
| AX5b | Vet a package before you depend on it. | D82, D83, D85, D86, D87, D88, D89, D90, D110, D111, D112, D113, D131, D132, D133, D134 | L2 | no |
| AX6 | Offer components tailored, in families, safe as black boxes. | D52, D53, D54, D56, D122, D123 | L2 | no |
| AX6b | Contain a dependency: wrap it, copy it, isolate it, or avoid it. | D80, D91, D92, D93, D94, D95, D96, D135 | L2 | no |
| AX7 | Give parts one small uniform interface so they compose. | D55, D62, D63, D64, D65, D72 | L2 | no |
| AX8 | Reason from the program text; refuse analogy and anthropomorphic metaphor. | D05, D06, D07, D08, D09, D14, D15, D16, D19, D20, D118, D119, D120 | L1 | no |
| AX9 | Name the trade-off; favor maintainability over density. | D39, D44, D69 | L1+L2 | yes |
| AX10 | Build the ecosystem: practices, standards, tools, and staffing for reuse. | D57, D58, D59, D60, D104, D105, D106, D107, D108, D109, D124, D138, D139 | L2 | no |
| AX11 | Teach computing as formal mathematics, without testing. | D12, D13 | L1 | no |
| AX12 | Use the system you build. | D67 | L2 | no |
| AX13 | Follow the archive's packaging and contribution conventions. | D73, D74, D75, D76, D77, D78, D79, D129 | L2 | no |
| AX14 | Withdraw your work from a platform that overrides the author. | D81 | L2 | no |
| AX15 | Review for semantic faults, not style. | D84 | L2 | no |
| AX16 | Upgrade, verify, and watch dependencies continuously. | D97, D98, D99, D100, D101, D102, D103, D114, D136, D137 | L2 | no |
| AX17 | Argue correctness against a specification; never infer it from tests alone. | D10, D17, D121 | L1 | no |
| AX18 | Grow the program incrementally from a working prototype. | D27, D142 | L1 | no |

Unclustered: D40 (rhetorical imperative, no conduct).

### Q8. Which demands contradict another demand in the substrate? Quote both and point to tensions.

Each pair stands as two rows, side A then side B. The tensions survey holds the full treatment; each pair here is a pointer to it.

| F-id | Finding (one sentence) | Quote (≤ 25 words) | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| demands-F219 | X1 side A (replace home-grown code with libraries) pulls against side B (copy instead of depending); axis: library use versus copy or avoid; see tensions. | "it could likely be implemented in about 10% of that, maybe 5%, using common, industry-standard libraries available today" | L1-06.txt:34 ¶14 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F220 | X1 side B (copy instead of depending) pulls against side A (replace home-grown code with libraries); axis: library use versus copy or avoid; see tensions. | "A little copying is better than a little dependency." | L2-05.txt:141 ¶65 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F221 | X2 side A (treat components as black boxes) pulls against side B (read the package's code); axis: black box versus read the code; see tensions. | "he should be able safely to regard components as black boxes" | L2-01.txt:26 ¶10 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F222 | X2 side B (read the package's code) pulls against side A (treat components as black boxes); axis: black box versus read the code; see tensions. | "Read some of it." | L2-05.txt:71 ¶30 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F223 | X3 side A (protect students from testing) pulls against side B (write tests for what you use); axis: no testing versus write tests; see tensions. | "students are protected from the temptation to test their programs" | L1-02.txt:140 ¶67 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F224 | X3 side B (write tests for what you use) pulls against side A (protect students from testing); axis: no testing versus write tests; see tensions. | "the next step should be to write new tests focused on the functionality needed by your application" | L2-05.txt:117 ¶53 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F225 | X3b side A (protect students from testing) pulls against side B (let testing decide what to add); axis: no testing versus testing decides; see tensions. | "students are protected from the temptation to test their programs" | L1-02.txt:140 ¶67 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F226 | X3b side B (let testing decide what to add) pulls against side A (protect students from testing); axis: no testing versus testing decides; see tensions. | "Increase the other dimensions as required by testing." | L1-05.txt:33 ¶11 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F227 | X4 side A (prove before presenting) pulls against side B (grow from a running prototype); axis: prove first versus prototype first; see tensions. | "The programmer's task is to present such complete conjectures as proven theorems." | L1-02.txt:132 ¶63 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F228 | X4 side B (grow from a running prototype) pulls against side A (prove before presenting); axis: prove first versus prototype first; see tensions. | "We developed the product by incremental growth from a working prototype." | L1-03.txt:12 ¶3 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F229 | X5 side A (programs need no maintenance) pulls against side B (code rots and needs maintenance); axis: code needs no maintenance versus code rots; see tensions. | "Unfathomed misunderstanding is further revealed by the term "software maintenance" | L1-02.txt:56 ¶25 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F230 | X5 side B (code rots and needs maintenance) pulls against side A (programs need no maintenance); axis: code needs no maintenance versus code rots; see tensions. | "It rots. It requires periodic maintenance." | L1-04.txt:8 ¶1 | SUBSTRATE L1-04 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F231 | X6 side A (choose the smaller form) pulls against side B (favor maintainability over density); axis: smaller versus maintainable; see tensions. | "It seems obvious to me that the latter case is better because it’s just plain smaller." | L1-05.txt:40 ¶14 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F232 | X6 side B (favor maintainability over density) pulls against side A (choose the smaller form); axis: smaller versus maintainable; see tensions. | "you should always favor maintainability" | L1-06.txt:30 ¶12 | SUBSTRATE L1-06 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F233 | X7 side A (write no code) pulls against side B (accept a third more code for clarity); axis: least code versus acceptable growth; see tensions. | "the best code is no code at all" | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F234 | X7 side B (accept a third more code for clarity) pulls against side A (write no code); axis: least code versus acceptable growth; see tensions. | "we considered this increase in size quite acceptable" | L2-02.txt:36 ¶14 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F235 | X8 side A (take parts off the shelf) pulls against side B (avoid the dependency); axis: take off the shelf versus avoid; see tensions. | "I claim we have done enough of this to start taking such things off the shelf." | L2-01.txt:20 ¶7 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F236 | X8 side B (avoid the dependency) pulls against side A (take parts off the shelf); axis: take off the shelf versus avoid; see tensions. | "the best answer may be to avoid it entirely, or at least to avoid the parts you’ve identified as most problematic" | L2-05.txt:137 ¶63 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F237 | X9 side A (take parts off the shelf) pulls against side B (d'Agapeyeff: why take atoms from the shelf); axis: shelf parts versus descriptions; see tensions. | "I claim we have done enough of this to start taking such things off the shelf." | L2-01.txt:20 ¶7 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F238 | X9 side B (d'Agapeyeff: why take atoms from the shelf) pulls against side A (take parts off the shelf); axis: shelf parts versus descriptions; see tensions. | "But why do we need to take atoms down from the shelf?" | L2-01-discussion.txt:22 ¶8 | SUBSTRATE L2-01-discussion (supplementary) | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F239 | X12 side A (ship first-time code, then rewrite) pulls against side B (write new code only as a last resort); axis: ship-then-rewrite versus reluctant writing; see tensions. | "A little debt speeds development so long as it is paid back promptly with a rewrite." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F240 | X12 side B (write new code only as a last resort) pulls against side A (ship first-time code, then rewrite); axis: ship-then-rewrite versus reluctant writing; see tensions. | "Every time you write new code, you should do so reluctantly, under duress, because you completely exhausted all your other options." | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F241 | X17 side A (gather everything into one archive) pulls against side B (less code); axis: gather everything versus less code; see tensions. | "of the CPAN is to be the Mother of All Perl Archives" | L2-03.txt:38 ¶5 | SUBSTRATE L2-03 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F242 | X17 side B (less code) pulls against side A (gather everything into one archive); axis: gather everything versus less code; see tensions. | "Less code to do the same thing (and possibly better)." | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F243 | X19 side A (engineer routines uniformly) pulls against side B (offer a variety of interface styles); axis: uniform versus varied interfaces; see tensions. | "I want the different types of routine in the catalogue that are similar in purpose to be engineered uniformly" | L2-01.txt:153 ¶70 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F244 | X19 side B (offer a variety of interface styles) pulls against side A (engineer routines uniformly); axis: uniform versus varied interfaces; see tensions. | "Routines that use several inputs and yield several outputs should come in a variety of interface styles." | L2-01.txt:76 ¶33 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F245 | X21 side A (add a wrapper layer) pulls against side B (no insulating layer); axis: wrapper layer versus direct calls; see tensions. | "define an interface of your own, along with a thin wrapper implementing that interface using the dependency" | L2-05.txt:125 ¶57 | SUBSTRATE L2-05 | HUMAN | VERIFIED | PRESERVE: distinction |
| demands-F246 | X21 side B (no insulating layer) pulls against side A (add a wrapper layer); axis: wrapper layer versus direct calls; see tensions. | "No large ‘‘access method” routines are required to insulate the programmer from the system calls" | L2-02.txt:357 ¶168 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: distinction |


## Category table

| D-id | Demand (quote) | Location | Explicit or implied | Addressee | Bindable (the literal check, or "no") | MODEL-actionable or HUMAN-only | Axiom cluster |
|---|---|---|---|---|---|---|---|
| D01 | "the lines of code metric only encouraged writing sloppy, bloated, broken code" | L1-01.txt:10 ¶2 | implied | manager | yes: response or diff summary reports no lines-added figure as progress or productivity | MODEL-actionable | AX1 |
| D02 | "his goal was to write as small and fast a program as possible" | L1-01.txt:10 ¶2 | implied | programmer | no: "smallest" has no baseline in one diff | MODEL-actionable | AX2 |
| D04 | "we should not regard them as "lines produced" but as "lines spent" | L1-02.txt:52 ¶23 | explicit | profession ("we") | yes: no sentence in the response credits added lines as output or achievement | MODEL-actionable | AX1 |
| D05 | "never refer to parts of programs or pieces of equipment in an anthropomorphic terminology, nor allow your students to do so" | L1-02.txt:104 ¶49 | explicit | educator and programmer ("your students") | yes: grep the response for human-mental verbs with a program or component as subject | MODEL-actionable | AX8 |
| D06 | "no longer calling a bug a bug but by calling it an error" | L1-02.txt:102 ¶48 | explicit | educator and programmer ("our language") | yes: the response says "error" and never "bug" for a fault in code | MODEL-actionable | AX8 |
| D07 | "We must learn to work with program texts while (temporarily) ignoring that they admit the interpretation of executable code." | L1-02.txt:124 ¶59 | explicit | computing scientist ("we") | no: no literal marker separates text-reasoning from execution-reasoning | MODEL-actionable | AX8 |
| D08 | "we should reason about programs without even mentioning their possible" | L1-02.txt:126 ¶60 | explicit | computing scientist ("we") | no: "behaviour" talk has no literal marker | MODEL-actionable | AX8 |
| D09 | "in computing science the anthropomorphic metaphor should be banned" | L1-02.txt:128 ¶61 | explicit | computing scientist | yes: same check as D05 | MODEL-actionable | AX8 |
| D10 | "The programmer's task is to present such complete conjectures as proven theorems." | L1-02.txt:132 ¶63 | implied | programmer | yes: the response states a specification and a proof argument, or it does not | MODEL-actionable | AX17 |
| D12 | "students are protected from the temptation to test their programs" | L1-02.txt:140 ¶67 | explicit | educator | no | HUMAN-only | AX11 |
| D13 | "Universities should not be afraid of teaching radical novelties" | L1-02.txt:150 ¶72 | explicit | educator ("Universities") | no | HUMAN-only | AX11 |
| D14 | "one has to approach the radical novelty with a blank mind, consciously refusing to try to link it with what is already familiar" | L1-02.txt:14 ¶4 | explicit | anyone facing a novelty ("one") | no | MODEL-actionable | AX8 |
| D15 | "by developing a keen ear for unwarranted analogies, one can detect a lot of medieval thinking today" | L1-02.txt:18 ¶6 | implied | anyone ("one") | no | MODEL-actionable | AX8 |
| D16 | "To do so, however, is highly dangerous: the analogy is too shallow" | L1-02.txt:40 ¶17 | implied | programmer | no | MODEL-actionable | AX8 |
| D17 | "program testing may convincingly demonstrate the presence of bugs, but can never demonstrate their absence" | L1-02.txt:54 ¶24 | implied | programmer ("the software engineer") | yes: the response does not claim correctness or absence of errors on test results alone | MODEL-actionable | AX17 |
| D19 | "Unfathomed misunderstanding is further revealed by the term "software maintenance" | L1-02.txt:56 ¶25 | implied | programmer | yes: the response applies no wear, rot, or maintenance term to code | MODEL-actionable | AX8 |
| D20 | "It really helps to view a program as a formula." | L1-02.txt:70 ¶32 | implied | programmer | no | MODEL-actionable | AX8 |
| D22 | "A little debt speeds development so long as it is paid back promptly with a rewrite." | L1-03.txt:16 ¶5 | implied | programmer and engineering organization | no: "promptly" has no bound | MODEL-actionable | AX3 |
| D23 | "Mature sections of the program have been revised or rewritten many times providing the consolidation that is key to understanding" | L1-03.txt:12 ¶3 | implied | programmer | no | MODEL-actionable | AX3 |
| D24 | "Each member of our small engineering team maintains at least general knowledge of all aspects of the roughly four megabytes of source code." | L1-03.txt:12 ¶3 | implied | team | no | HUMAN-only | AX4 |
| D25 | "excess quantities will make a program unmasterable" | L1-03.txt:16 ¶5 | implied | engineering organization | no | MODEL-actionable | AX4 |
| D27 | "We developed the product by incremental growth from a working prototype." | L1-03.txt:12 ¶3 | implied | engineering team | no | MODEL-actionable | AX18 |
| D28 | "You should do whatever possible to increase the productivity of individual programmers in terms of the expressive power of the code they write." | L1-04.txt:10 ¶2 | explicit | engineering leadership ("Less programmers to hire") | no | MODEL-actionable | AX2 |
| D29 | "Less code to do the same thing (and possibly better)." | L1-04.txt:10 ¶2 | explicit | programmer | no: comparative; needs a baseline | MODEL-actionable | AX2 |
| D31 | "The longer it takes a new employee to make sense of your system." | L1-04.txt:8 ¶1 | implied | engineering organization | no | MODEL-actionable | AX4 |
| D32 | "Start with brevity. Increase the other dimensions as required by testing." | L1-05.txt:33 ¶11 | explicit | programmer ("our task, as programmers") | yes: every addition beyond the minimum in the diff names the test or requirement that required it | MODEL-actionable | AX2 |
| D33 | "Every time you write new code, you should do so reluctantly, under duress, because you completely exhausted all your other options." | L1-05.txt:42 ¶15 | explicit | programmer ("you") | yes: the response lists the non-code options it ruled out before adding code | MODEL-actionable | AX2 |
| D34 | "If you can’t get away with no code, the next best thing is to start with brevity." | L1-05.txt:42 ¶15 | explicit | programmer ("you") | yes: same check as D32 | MODEL-actionable | AX2 |
| D35 | "the best code is no code at all" | L1-05.txt:42 ¶15 | implied | programmer | yes: same check as D33 | MODEL-actionable | AX2 |
| D36 | "you’ll love it enough to write as little of it as possible" | L1-05.txt:44 ¶16 | implied | programmer | no | MODEL-actionable | AX2 |
| D37 | "practical, sensible strategies to reduce the volume of code an individual programmer has to read to understand how a program works" | L1-05.txt:35 ¶12 | implied | programmer | no | MODEL-actionable | AX4 |
| D38 | "It seems obvious to me that the latter case is better because it’s just plain smaller." | L1-05.txt:40 ¶14 | implied | programmer | yes: where two equivalent forms are named, the diff uses the shorter | MODEL-actionable | AX2 |
| D39 | "To be a master programmer is to understand the nature of these trade-offs, and be conscious of them in everything we write." | L1-05.txt:20 ¶7 | implied | programmer ("our task, as programmers") | yes: each design choice in the response names the dimension it trades (brevity, features, speed, time, robustness, flexibility) | MODEL-actionable | AX9 |
| D40 | "Go look in the mirror." | L1-05.txt:14 ¶4 | explicit | programmer ("you") | no | HUMAN-only | none |
| D41 | "LOC (lines of code) numbers should never be taken as an asset measurement." | L1-06.txt:26 ¶10 | explicit | organization ("the way we do metrics") | yes: no sentence in the response treats a LOC total as value or productivity | MODEL-actionable | AX1 |
| D42 | "Source code is a liability, not an asset!" | L1-06.txt:12 ¶3 | implied | programmer and team | no | MODEL-actionable | AX1 |
| D43 | "It’s in our best interest to have as little source code as possible while still being able to accomplish our business goals." | L1-06.txt:24 ¶9 | implied | programmer and team | no | MODEL-actionable | AX2 |
| D44 | "you should always favor maintainability" | L1-06.txt:30 ¶12 | explicit | programmer ("you") | no | MODEL-actionable | AX9 |
| D45 | "Bust out your delete key and start whacking." | L1-06.txt:36 ¶15 | explicit | programmer ("you") | yes: a deletion diff cites the tests that protect behaviour, or states none exist | MODEL-actionable | AX3 |
| D46 | "it’s absolutely critical that you get yourself above water as soon as possible" | L1-06.txt:36 ¶15 | explicit | programmer ("you") | no: "as soon as possible" has no bound | MODEL-actionable | AX3 |
| D47 | "This week we removed 10K LOC while preserving all existing functionality!" | L1-06.txt:28 ¶11 | implied | team | yes: a reported deletion states the evidence that functionality is preserved | MODEL-actionable | AX3 |
| D48 | "it could likely be implemented in about 10% of that, maybe 5%, using common, industry-standard libraries available today" | L1-06.txt:34 ¶14 | implied | programmer and team | yes: where a standard library covers the function, the diff imports it instead of reimplementing it | MODEL-actionable | AX5 |
| D49 | "in order to avoid paying $1000 or even $500 to license a third-party software package that does the same thing?" | L1-06.txt:32 ¶13 | implied | company ("companies") | no | HUMAN-only | AX5 |
| D50 | "whether to refactor existing code to meet changing requirements vs. simply piling your new stuff on top of the old stuff" | L1-06.txt:30 ¶12 | implied | programmer | yes: the diff changes the existing implementation instead of appending a parallel code path | MODEL-actionable | AX3 |
| D51 | "I claim we have done enough of this to start taking such things off the shelf." | L2-01.txt:20 ¶7 | implied | software builder ("When we undertake to write a compiler") | yes: where a named standard component covers the need, the diff uses it | MODEL-actionable | AX5 |
| D52 | "We have to begin thinking small." | L2-01.txt:91 ¶39 | explicit | components builder | no | HUMAN-only | AX6 |
| D53 | "No user of a particular member of a family should pay a penalty, in unwanted generality" | L2-01.txt:26 ¶10 | explicit | component producer | no | HUMAN-only | AX6 |
| D54 | "he should be able safely to regard components as black boxes" | L2-01.txt:26 ¶10 | explicit | component producer | no | HUMAN-only | AX6 |
| D55 | "I want the different types of routine in the catalogue that are similar in purpose to be engineered uniformly" | L2-01.txt:153 ¶70 | explicit | component producer | no | HUMAN-only | AX7 |
| D56 | "but I do insist that transliteration be essentially direct" | L2-01.txt:153 ¶70 | explicit | component producer | no | HUMAN-only | AX6 |
| D57 | "The industrial orientation of a pilot plant must be constantly borne in mind." | L2-01.txt:137 ¶62 | explicit | organization funding the pilot | no | HUMAN-only | AX10 |
| D58 | "one ought to do considerable comparison of known schemes working in practical environments" | L2-01.txt:101 ¶44 | explicit | industry | no | HUMAN-only | AX10 |
| D59 | "it would be rash to standardize before we have the models" | L2-01.txt:149 ¶68 | implied | industry | no | HUMAN-only | AX10 |
| D60 | "one would be wise to have demonstrated techniques for creating a parameterized family of routines for a couple of familiar purposes" | L2-01.txt:135 ¶61 | implied | industry | no | HUMAN-only | AX10 |
| D61 | "who would be able to use tried parts for all the more commonplace parts of their systems" | L2-01.txt:111 ¶49 | implied | system builder | yes: where a commonplace part has a tried standard component, the diff uses it | MODEL-actionable | AX5 |
| D62 | "the command need merely use the standard file descriptors 0 and 1 where appropriate" | L2-02.txt:243 ¶113 | implied | command author | yes: a new command reads fd 0 and writes fd 1 by default and implements no redirection of its own | MODEL-actionable | AX7 |
| D63 | "unwise for efficiency reasons, to expect authors of commands such as ls to provide such a wide variety of output options" | L2-02.txt:259 ¶120 | implied | command author | yes: the diff adds no pagination, column, or spooling option to a listing command | MODEL-actionable | AX7 |
| D64 | "it is also desirable from a space-efficiency standpoint to push device-dependent considerations into the operating system itself" | L2-02.txt:361 ¶170 | implied | system designer | no | MODEL-actionable | AX7 |
| D65 | "No large ‘‘access method” routines are required to insulate the programmer from the system calls" | L2-02.txt:357 ¶168 | implied | system designer | no | MODEL-actionable | AX7 |
| D66 | "we were willing to revise and rewrite the system and its software when new ideas were invented, discovered, or suggested by others" | L2-02.txt:355 ¶167 | implied | system designer | no | MODEL-actionable | AX3 |
| D67 | "If designers of a system are forced to use that system, they quickly become aware of its functional and superficial deficiencies" | L2-02.txt:355 ¶167 | implied | system designer | no | HUMAN-only | AX12 |
| D69 | "we considered this increase in size quite acceptable" | L2-02.txt:36 ¶14 | implied | system designer | no | MODEL-actionable | AX9 |
| D71 | "the size constraint has encouraged not only economy but a certain elegance of design" | L2-02.txt:353 ¶166 | implied | system designer | no | HUMAN-only | AX2 |
| D72 | "the structure of files is controlled by the programs which use them, not by the system" | L2-02.txt:44 ¶18 | implied | system designer | no | MODEL-actionable | AX7 |
| D73 | "no shars, make them to be tars" | L2-03.txt:63 ¶10 | explicit | archivist | yes: the archive listing contains no shar files | MODEL-actionable | AX13 |
| D74 | "no zips/lzhs/lhas for UNIX stuff, make them to be tars" | L2-03.txt:64 ¶10 | explicit | archivist | yes: the UNIX portion of the archive contains no zip, lzh, or lha files | MODEL-actionable | AX13 |
| D75 | "no .Z, use .gz" | L2-03.txt:66 ¶10 | explicit | archivist | yes: the archive contains no .Z files | MODEL-actionable | AX13 |
| D76 | "That tar very preferably already subdivided according to the CPAN hierarchy." | L2-03.txt:50 ¶6 | explicit | archivist | no | HUMAN-only | AX13 |
| D77 | "see what CPAN is lacking that _you_ have" | L2-03.txt:37 ¶5 | explicit | archivist ("Fellow Perl Archivists") | no | HUMAN-only | AX13 |
| D78 | "some site could volunteer to be the perl5 extension site" | L2-03.txt:56 ¶8 | explicit | archive site operator | no | HUMAN-only | AX13 |
| D79 | "Please take a look around, many looks," | L2-03.txt:24 ¶4 | explicit | archivist | no | HUMAN-only | AX13 |
| D80 | "You can either point your dependency to repo directly (azer/dependency)" | L2-04.txt:18 ¶6 | explicit | dependent ("if your stuff just got broken") | yes: the manifest names a repository URL, not a registry package | MODEL-actionable | AX6b |
| D81 | "NPM is no longer a place that I’ll share my open source work at" | L2-04.txt:14 ¶4 | implied | open-source author | no | HUMAN-only | AX14 |
| D82 | "Read some of it." | L2-05.txt:71 ¶30 | explicit | developer adopting a dependency | yes: the response states which package files it read | MODEL-actionable | AX5b |
| D83 | "Develop your own systematic ways to check code quality." | L2-05.txt:73 ¶31 | explicit | developer adopting a dependency | no | MODEL-actionable | AX5b |
| D84 | "you should ignore rote suggestions about topics like brace style and focus instead on semantic problems" | L2-05.txt:73 ¶31 | explicit | developer adopting a dependency | yes: review findings cite semantic faults, not brace or style items | MODEL-actionable | AX15 |
| D85 | "Keep an open mind to development practices you may not be familiar with." | L2-05.txt:75 ¶32 | explicit | developer adopting a dependency | no | MODEL-actionable | AX5b |
| D86 | "Find the package’s issue tracker." | L2-05.txt:85 ¶37 | explicit | developer adopting a dependency | yes: the response cites open and closed issue counts or states none was reachable | MODEL-actionable | AX5b |
| D87 | "Look at the package’s commit history." | L2-05.txt:89 ¶39 | explicit | developer adopting a dependency | yes: the response states last-commit date or history length | MODEL-actionable | AX5b |
| D88 | "you should insist on tests in code you outsource to others" | L2-05.txt:79 ¶34 | explicit | developer adopting a dependency | yes: the response states whether the package ships tests and whether they pass | MODEL-actionable | AX5b |
| D89 | "The inspection process should include running a package’s own tests." | L2-05.txt:117 ¶53 | explicit | developer adopting a dependency | yes: the response reports a run of the package's tests | MODEL-actionable | AX5b |
| D90 | "the next step should be to write new tests focused on the functionality needed by your application" | L2-05.txt:117 ¶53 | explicit | developer adopting a dependency | yes: the diff that adds the dependency adds tests that call the functions it uses | MODEL-actionable | AX5b |
| D91 | "define an interface of your own, along with a thin wrapper implementing that interface using the dependency" | L2-05.txt:125 ¶57 | explicit | developer adopting a dependency | yes: calls to the dependency appear only inside the wrapper module | MODEL-actionable | AX6b |
| D92 | "the wrapper should include only what your project needs from the dependency, not everything the dependency offers" | L2-05.txt:125 ¶57 | explicit | developer adopting a dependency | yes: the wrapper exposes no function the project does not call | MODEL-actionable | AX6b |
| D93 | "If you only need a tiny fraction of a dependency, it may be simplest to make a copy of what you need" | L2-05.txt:141 ¶65 | explicit | developer adopting a dependency | yes: the diff copies the function with its license notice instead of adding a dependency | MODEL-actionable | AX6b |
| D94 | "A little copying is better than a little dependency." | L2-05.txt:141 ¶65 | explicit | Go developer community (proverb) | no | MODEL-actionable | AX6b |
| D95 | "the best answer may be to avoid it entirely, or at least to avoid the parts you’ve identified as most problematic" | L2-05.txt:137 ¶63 | explicit | developer adopting a dependency | no | MODEL-actionable | AX6b |
| D96 | "It may also be appropriate to isolate a dependency at run-time, to limit the possible damage caused by bugs in it." | L2-05.txt:131 ¶60 | implied | developer and language designer | no | HUMAN-only | AX6b |
| D97 | "Upgrading promptly is important" | L2-05.txt:151 ¶70 | explicit | developer maintaining a dependency | no: "promptly" has no bound | MODEL-actionable | AX16 |
| D98 | "you’d want to skim the diffs showing the changes being made from the current version to the upgraded versions" | L2-05.txt:151 ¶70 | explicit | developer maintaining a dependency | yes: the upgrade response cites the diff or release notes it read | MODEL-actionable | AX16 |
| D99 | "upgrades should not be completely automatic" | L2-05.txt:155 ¶72 | explicit | developer maintaining a dependency | yes: the configuration does not auto-merge dependency upgrades | MODEL-actionable | AX16 |
| D100 | "make sure that you keep using the specific package versions you think you are" | L2-05.txt:165 ¶77 | explicit | developer maintaining a dependency | yes: a lockfile records a cryptographic hash per package version | MODEL-actionable | AX16 |
| D101 | "It is also important to watch for new indirect dependencies creeping in" | L2-05.txt:167 ¶78 | explicit | developer maintaining a dependency | yes: an upgrade response lists newly added transitive packages | MODEL-actionable | AX16 |
| D102 | "It’s also important to periodically revisit any dependency that isn’t changing." | L2-05.txt:171 ¶80 | explicit | developer maintaining a dependency | no: "periodically" has no bound | HUMAN-only | AX16 |
| D103 | "It’s also important to recheck the security history of each dependency." | L2-05.txt:173 ¶81 | explicit | developer maintaining a dependency | no | MODEL-actionable | AX16 |
| D104 | "Recognize the problem." | L2-05.txt:185 ¶87 | explicit | industry ("We need many people") | no | HUMAN-only | AX10 |
| D105 | "Establish best practices for today." | L2-05.txt:189 ¶89 | explicit | industry | no | HUMAN-only | AX10 |
| D106 | "Develop better dependency technology for tomorrow." | L2-05.txt:193 ¶91 | explicit | tool builder | no | HUMAN-only | AX10 |
| D107 | "Build tools should, at the least, make it easy to run a package’s own tests." | L2-05.txt:193 ¶91 | explicit | tool builder ("Build tools") | no | HUMAN-only | AX10 |
| D108 | "Languages should also provide easy ways to isolate a suspect package." | L2-05.txt:193 ¶91 | explicit | language designer ("Languages") | no | HUMAN-only | AX10 |
| D109 | "Let’s work together to find out how to reuse it safely." | L2-05.txt:195 ¶92 | explicit | industry ("Let's") | no | HUMAN-only | AX10 |
| D110 | "If you can’t or it doesn’t, turn back now!" | L2-05.txt:117 ¶53 | explicit | developer adopting a dependency | no | MODEL-actionable | AX5b |
| D111 | "Before you depend on a package you found on the internet, it is similarly prudent to learn a bit about it first." | L2-05.txt:59 ¶24 | implied | developer adopting a dependency | yes: the response states provenance and maintainers before adding the package | MODEL-actionable | AX5b |
| D112 | "If the inspection reveals major problems, it may be best not to use the package" | L2-05.txt:61 ¶25 | implied | developer adopting a dependency | no | MODEL-actionable | AX5b |
| D113 | "each of them should ideally be inspected as described in this section" | L2-05.txt:111 ¶50 | explicit | developer adopting a dependency | no | MODEL-actionable | AX5b |
| D114 | "you need other arrangements to track that information through your production deployment process" | L2-05.txt:149 ¶69 | implied | developer maintaining a dependency | no | HUMAN-only | AX16 |
| D118 | "deal with all elements of a set by ignoring them and working with the set's definition" | L1-02.txt:122 ¶58 | explicit | computing scientist ("we") | no | MODEL-actionable | AX8 |
| D119 | "we must therefore not try to imagine them" | L1-02.txt:66 ¶30 | explicit | computing scientist ("we") | no | MODEL-actionable | AX8 |
| D120 | "He has to be able to think in terms of conceptual hierarchies that are much deeper than a single mind ever needed to face before" | L1-02.txt:34 ¶14 | implied | programmer ("The programmer") | no | MODEL-actionable | AX8 |
| D121 | "his main task is to give a formal proof that the program he proposes meets the equally formal functional specification" | L1-02.txt:140 ¶67 | implied | programmer and educator | yes: same check as D10 | MODEL-actionable | AX17 |
| D122 | "should be available in families arranged according to precision, robustness, generality and timespace performance" | L2-01.txt:12 ¶3 | explicit | component producer | no | HUMAN-only | AX6 |
| D123 | "Routines that use several inputs and yield several outputs should come in a variety of interface styles." | L2-01.txt:76 ¶33 | explicit | component producer | no | HUMAN-only | AX6 |
| D124 | "The personnel of a pilot plant should look like the personnel on many big software projects, with the masses of coders removed." | L2-01.txt:139 ¶63 | explicit | organization funding the pilot | no | HUMAN-only | AX10 |
| D129 | "please create tidy .tar.gz:s in somewhere" | L2-03.txt:48 ¶6 | explicit | archivist | no | HUMAN-only | AX13 |
| D131 | "Is package’s documentation clear? Does the API have a clear design?" | L2-05.txt:67 ¶28 | implied | developer adopting a dependency | yes: the response states a finding on documentation and API clarity | MODEL-actionable | AX5b |
| D132 | "Will you be processing untrusted inputs with the package?" | L2-05.txt:101 ¶45 | implied | developer adopting a dependency | yes: the response states the package's vulnerability-database history when untrusted input is processed | MODEL-actionable | AX5b |
| D133 | "Is the code properly licensed? Does it have a license at all?" | L2-05.txt:107 ¶48 | implied | developer adopting a dependency | yes: the response states the package's license | MODEL-actionable | AX5b |
| D134 | "It is especially worth exercising the likely problem areas identified by the basic inspection." | L2-05.txt:119 ¶54 | implied | developer adopting a dependency | no | MODEL-actionable | AX5b |
| D135 | "it is worth the effort to make it easy to migrate your project to a new dependency" | L2-05.txt:123 ¶56 | explicit | developer adopting a dependency | no | MODEL-actionable | AX6b |
| D136 | "It’s important to continue to monitor them and perhaps even re-evaluate your decision to use them." | L2-05.txt:163 ¶76 | explicit | developer maintaining a dependency | no | HUMAN-only | AX16 |
| D137 | "You’ll also want to re-run the tests you’ve written that are specific to your project" | L2-05.txt:153 ¶71 | explicit | developer maintaining a dependency | yes: the upgrade response reports a run of the project-specific tests | MODEL-actionable | AX16 |
| D138 | "We should not ignore the warnings." | L2-05.txt:181 ¶85 | explicit | industry ("We") | no | HUMAN-only | AX10 |
| D139 | "it may be that we need engineers who specialize in managing dependencies" | L2-05.txt:189 ¶89 | implied | organization | no | HUMAN-only | AX10 |
| D141 | "the best antidote is more complete familiarity with the product and its implementation" | L1-03.txt:14 ¶4 | implied | engineering team | no | HUMAN-only | AX4 |
| D142 | "we recognize this amounts to preserving the concept of payment up-front and in-full" | L1-03.txt:18 ¶6 | implied | engineering organization | no | MODEL-actionable | AX18 |
| D143 | "I exhorted developers to Code Smaller" | L1-05.txt:35 ¶12 | explicit | developer | no | MODEL-actionable | AX2 |

## Rated statements

| R-id | Candidate statement (one imperative sentence) | Rating | For (F-ids) | Against (F-ids) | Sources (IDs) | Deciding fact (≤ 15 words) |
|---|---|---|---|---|---|---|
| R01 | Count lines of code as cost, never as output, productivity, or asset. | AXIOM | demands-F075 (D01), demands-F002 (D04), demands-F019 (D41), demands-F098 (D42), demands-F100 (D47) | none | L1-01, L1-02, L1-06 | Three texts state it; none opposes it. |
| R02 | Write as little code as the goal permits. | AXIOM | demands-F076 (D02), demands-F012 (D28), demands-F013 (D29), demands-F015 (D32), demands-F017 (D33), demands-F097 (D36), demands-F099 (D43), demands-F112 (D71), demands-F016 (D143) | demands-F020 (D44), demands-F108 (D69) | L1-01, L1-04, L1-05, L1-06, L2-02 | Four L1 texts state it; two stated exceptions bound it. |
| R03 | Repay code debt by rewriting or deleting the code. | AXIOM | demands-F089 (D22), demands-F085 (D23), demands-F021 (D45), demands-F100 (D47), demands-F101 (D50), demands-F113 (D66) | none | L1-03, L1-06, L2-02 | L1-03, L1-06 and L2-02 state it; conditions are explicit. |
| R04 | Do not cite passing tests as proof that a program is correct. | CANDIDATE | demands-F080 (D17) | none | L1-02 | One text states it; L2-05 credits tests with establishing correctness. |
| R05 | Prove programs against their specifications instead of testing them. | REJECT | demands-F083 (D10), demands-F010 (D12), demands-F084 (D121) | demands-F015 (D32), demands-F051 (D90), demands-F087 (D27) | L1-02, L1-03, L1-05, L2-05 | Three other texts require testing or prototypes; one text holds it. |
| R06 | Never describe a program in human terms. | CANDIDATE | demands-F005 (D05), demands-F009 (D09) | none | L1-02 | L1-02 states it flatly; no second text. |
| R07 | Call a bug an error. | CANDIDATE | demands-F004 (D06) | none | L1-02 | L1-02 alone states it. |
| R08 | Name the trade-off behind each coding decision; favor maintainability over density. | CANDIDATE | demands-F093 (D39), demands-F020 (D44), demands-F108 (D69) | demands-F095 (D38) | L1-05, L1-06, L2-02 | Three texts agree on trade-offs; L1-05 also says choose the smaller form. |
| R09 | Vet a package before you depend on it: read it, run its tests, check its history. | CANDIDATE | demands-F042 (D82), demands-F046 (D88), demands-F050 (D89), demands-F118 (D111) | demands-F025 (D54) | L2-01, L2-05 | Only L2-05 states it; L2-01 says treat components as black boxes. |
| R10 | Wrap each dependency behind your own thin interface. | CANDIDATE | demands-F054 (D91), demands-F055 (D92), demands-F053 (D135) | demands-F115 (D65) | L2-02, L2-05 | Only L2-05 states it; L2-02 says no insulating layer. |
| R11 | Copy the few lines you need instead of adding a dependency. | CANDIDATE | demands-F057 (D93), demands-F058 (D94) | demands-F103 (D48), demands-F104 (D51) | L1-06, L2-01, L2-05 | Only L2-05 states it; L1-06 and L2-01 say take libraries. |
| R12 | Replace home-grown code with common standard libraries when they exist. | CANDIDATE | demands-F103 (D48), demands-F102 (D49), demands-F104 (D51), demands-F105 (D61) | demands-F057 (D93), demands-F058 (D94), demands-F056 (D95) | L1-06, L2-01, L2-05 | Two lanes state it; L2-05 states the opposite. |
| R13 | Build each command to read standard input and write standard output. | CANDIDATE | demands-F110 (D62), demands-F111 (D63), demands-F031 (D55) | none | L2-01, L2-02 | Only L2-02 states it; L2-01 asks for uniform interfaces. |
| R14 | Keep the codebase within what one team can master. | CANDIDATE | demands-F086 (D24), demands-F090 (D25), demands-F092 (D31), demands-F094 (D37), demands-F088 (D141) | none | L1-03, L1-04, L1-05 | Three L1 texts show it; no text states it as a rule. |
| R15 | Upgrade dependencies promptly, after verifying the upgrade. | CANDIDATE | demands-F059 (D97), demands-F060 (D98), demands-F062 (D99), demands-F064 (D100), demands-F065 (D101), demands-F061 (D137) | none | L2-05 | Only L2-05 states it; one cited incident. |
| R16 | Grow the program incrementally from a working prototype. | CANDIDATE | demands-F087 (D27), demands-F113 (D66), demands-F091 (D142) | demands-F083 (D10), demands-F010 (D12) | L1-02, L1-03, L2-02 | L1-03 states it; L1-02 requires proof before running. |

Second source or exemplar that would decide each CANDIDATE:
- R04: a second primary text that says tests cannot show absence of errors, or an exemplar of a defect that passed every test and a diff that an argument would have caught.
- R06: a second primary text that bans human terms for programs; for the HUMAN reader effect, a measurement of confusion caused by such terms (none in the substrate).
- R07: a second primary text that makes the bug-to-error change; the cost of the change is unmeasured in the substrate.
- R08: an exemplar diff where naming the trade-off changed the outcome; a second text with the explicit rule beyond L1-06.
- R09: a second primary text on vetting; the references of L2-05 (the vulnerability database, the GPL warning) point outside the substrate.
- R10: a second author who states the wrapper rule; the exemplar is the Code Search Regexp class at L2-05.txt:127.
- R11: a second author on copying versus depending; L2-05 cites the Go proverb source (its reference 20), not fetched here.
- R12: a resolver of tension X1 (libraries versus copy) and a text that sets the size at which copying beats depending.
- R13: a second text on filters; the exemplar is the pipeline at L2-02.txt:249–259.
- R14: a text that states the rule outright; the exemplar is the four-megabyte team at L1-03.txt:12.
- R15: a second text on upgrade timing; the one exemplar is the Equifax chronology at L2-05.txt:147.
- R16: a resolver of tension X4 (prove first versus prototype first); the exemplar is WyCash at L1-03.txt:12.

## Open questions
- Q1, Q2: demands in the full Skrenta post (L1-04) and in the 26 Oct 1995 CPAN post (L2-03) are unread. Searched: the index failure records (index-lane1.md:205, index-lane2.md:354); the copies hold only Atwood's quotation and the earlier mail. No demand was filled from memory.
- Q6: no text names a language model or measures model compliance. Searched: a grep of the eleven copies for "language model", "machine learning", "neural", "chatbot", "copilot", "LLM", "artificial intelligence", "AI"; the only hit is L1-02.txt:60 (Artificial Intelligence as mimicry of the human mind), which concerns no coding model. Every MODEL-actionable label rests on the tools a Claude Code model has.
- Q5: each bindable check is my literal-reading check; no text or study records whether reviewers agree on any of them. UNVERIFIED.
- Q1: L2-02-dumped-retro.txt and L2-03-dumped-bowers.txt are supplementary copies of other texts and were not read.

## Cross-category notes
- enemies · demands-F075 (D01) · the lines-of-code metric set by managers is the practice L1-01 opposes through Atkinson's -2000.
- enemies · demands-F030 (D124) · "masses of coders removed" names coder volume as a cost; L1-04 pairs it with demands-F012 (D28).
- enemies · demands-F091 (D142) · L1-03 opposes the waterfall payment "up-front and in-full".
- distinctions-vocabulary · demands-F002 (D04) · "lines produced" versus "lines spent".
- distinctions-vocabulary · demands-F004 (D06) · "bug" versus "error".
- distinctions-vocabulary · demands-F025 (D54) · "black boxes" against demands-F042 (D82) "Read some of it."
- distinctions-vocabulary · demands-F058 (D94) · the Go proverb "A little copying is better than a little dependency."
- tensions · demands-F219 (X1A) · libraries versus copy, cross-lane.
- tensions · demands-F233 (X7A) · least code versus accepted growth (L2-02 :36).
- tensions · demands-F223 (X3A) · testing versus none; also demands-F227 (X4A) proof first versus prototype first.
- tensions · demands-F229 (X5A) · maintenance as misunderstanding versus code that rots (demands-F230 (X5B)).
- tensions · demands-F245 (X21A) · wrapper layer versus no insulating layer.
- evidence · demands-F102 (D49) · L1-06.txt:32 carries "$1000 or even $500" and "$10,000 a month" in the same paragraph as the demand.
- evidence · demands-F069 (D104) · L2-05 grounds its recommendations on the Equifax chronology at L2-05.txt:147.
- collection-fit · demands-F110 (D62) · stdin/stdout filter demands appear only in L2-02 (and as uniform-interface demands in L2-01).
- collection-fit · demands-F054 (D91) · dependency-containment demands (wrap, copy, isolate, avoid) appear only in L2-05 and L2-04.
- breadth · demands-F080 (D17) · L1-02.txt:54 points to a remark "two decades" old on testing; the primary remark is outside the substrate.
