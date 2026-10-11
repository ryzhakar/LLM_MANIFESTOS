BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md (full); Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml (full, 2,923 lines in two pages through `</instruction_matrix>`); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md (full); manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md (full)
INTERPLAY: All four converge on the primary text over its name, the concrete quote over the paraphrase, and the cut over the pad; they pull apart where manifesto-writing pulls toward drafting while this round forbids drafting and conclusions; resolved: the skill serves as a reading lens (PRESERVE or CUT verdict per finding) and never as a pen, and First Principles' "verify the irreducible" makes every finding a located quote.
COMMIT: I must load every element and every text from source, and I will cite each finding at file:line with its paragraph; I must write positive, concrete, active prose and omit needless words, and I will keep each cell to its quote and its location; I must not draft, rank, or recommend, and I will not; I must treat Strunk's license to deviate as judgment and not as leave to infer, and I will mark every unverified claim UNVERIFIED.
# distinctions-vocabulary — Discovery Survey

## Summary

Eleven texts read whole from R/recon/sources (L1-04 and L2-03 are PARTIAL copies and are flagged in every row that draws on them), with both indexes read first; 487 finding rows carry a located quote and a lens verdict. All seven questions are answered (Q1 88 rows, Q2 72, Q3 99, Q4 76, Q5 70, Q6 40, Q7 42) and the category table lists terms and aphorisms. Open: the original Skrenta post and the Hietaniemi launch post are not held, the supplementary files are unread, and no measurement exists of what a reader five years out needs explained.

Conventions: R = /home/user/LLM_MANIFESTOS/research/manifesto-craft. Locations read {ID}.txt:{line} ¶{n}, with ¶n the n-th blank-line-separated block after the six-line header and its blank line (the index convention; verified against index values L1-02 ¶23 and L2-05 ¶50); "(header line)" marks a quote taken from the six-line header of the saved copy. A "‖" separates fragments of one row, each verified verbatim at its own location; " / " inside a quote marks a source line break (L2-03 only). Word counts count whitespace tokens that contain a letter or a digit. Every quote was verified by script against the saved file before this report was written. VERIFIED on a row from a PARTIAL copy (L1-04, L2-03) means the quote stands at its location in the saved copy and asserts nothing about the unheld remainder; a claim of absence from a PARTIAL text is UNVERIFIED. Reader is NONE unless a row concerns what a reader needs (Q7: HUMAN; no MODEL claim is made anywhere). Lens verdicts follow the manifesto-writing skill: PRESERVE (distinction, vocabulary, aphorism, moral core, principle) or CUT (aside, example, hedge, repetition, scaffolding, caveat).

## Texts read

| Source | Index status (FULL · PARTIAL · FAILED) | Read in full? | Questions |
|---|---|---|---|
| L1-01.txt — Hertzfeld, "-2000 Lines Of Code" (1982) | FULL | Yes, whole copy | Q1, Q2, Q3, Q4, Q5, Q6, Q7 |
| L1-02.txt — Dijkstra, EWD 1036 (1988) | FULL | Yes, whole copy | Q1, Q2, Q3, Q4, Q5, Q6, Q7 |
| L1-03.txt — Cunningham, WyCash Portfolio Management System (1992) | FULL | Yes, whole copy | Q1, Q2, Q3, Q4, Q5, Q6, Q7 |
| L1-04.txt — Skrenta, "Code is our enemy" (2007; PARTIAL copy: Atwood's quotation only) | PARTIAL | Yes, whole copy (Atwood's two-paragraph quotation only; original unread) | Q1, Q2, Q3, Q4, Q5, Q6, Q7 |
| L1-05.txt — Atwood, "The Best Code is No Code At All" (2007) | FULL | Yes, whole copy | Q1, Q2, Q3, Q4, Q5, Q6, Q7 |
| L1-06.txt — Lee, "Source Code Is A Liability, Not An Asset" (2009) | FULL | Yes, whole copy | Q1, Q2, Q3, Q4, Q5, Q6, Q7 |
| L2-01.txt — McIlroy, "Mass Produced Software Components" (1968) | FULL | Yes, whole copy | Q1, Q2, Q3, Q4, Q5, Q6, Q7 |
| L2-02.txt — Ritchie and Thompson, "The UNIX Time-Sharing System" (1974) | FULL | Yes, whole copy | Q1, Q2, Q3, Q4, Q5, Q6, Q7 |
| L2-03.txt — Hietaniemi, CPAN "private showing" (1995; PARTIAL copy: the pre-launch mail, not the launch post) | PARTIAL | Yes, whole copy (pre-launch mail; the 26 Oct 1995 post is not held) | Q1, Q2, Q3, Q4, Q7 |
| L2-04.txt — Koçulu, "I've Just Liberated My Modules" (2016) | FULL | Yes, whole copy | Q1, Q2, Q3, Q4, Q5, Q7 |
| L2-05.txt — Cox, "Our Software Dependency Problem" (2019) | FULL | Yes, whole copy | Q1, Q2, Q3, Q4, Q5, Q6, Q7 |

Not read, not among the eleven: L2-01-discussion.txt, L2-02-dumped-retro.txt, L2-03-dumped-bowers.txt. Index files read whole: R/recon/index-lane1.md, R/recon/index-lane2.md.

## Answers

### Q1. Which terms does each text coin or define precisely? Quote the defining sentence.

#### L1-01 Hertzfeld, "-2000 Lines Of Code" (1982)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F001 | The managers define the measure: a weekly form field for lines of code written. | "a field for the number of lines of code that were written that week" | L1-01.txt:8 ¶1 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F002 | Atkinson names the "lines of code metric" and states its effect on code. | "the lines of code metric only encouraged writing sloppy, bloated, broken code" | L1-01.txt:10 ¶2 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F003 | The saving is stated as a by-product; Atkinson enters it as a negative count. | "As a by-product, the rewrite also saved around 2,000 lines of code." ‖ "wrote in the number: -2000" | L1-01.txt:12 ¶3; L1-01.txt:14 ¶4 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: vocabulary |

#### L1-02 Dijkstra, EWD 1036 (1988)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F004 | Dijkstra defines "radical" novelty as the case of sharp discontinuity, where analogy breaks down. | "in the case of a sharp discontinuity, however, the method breaks down" ‖ "This is the situation that is characteristic for the "radical" novelty." | L1-02.txt:12 ¶3 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F005 | First radical novelty of computing: depth of conceptual hierarchy. | "The first radical novelty is a direct consequence of the raw power of today's computing equipment." | L1-02.txt:34 ¶14 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F006 | Second radical novelty of computing: first large-scale digital device. | "The second radical novelty is that the automatic computer is our first large-scale digital device." | L1-02.txt:38 ¶16 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F007 | The method for radical novelty is named "orthogonal". | "Coping with radical novelty requires an orthogonal method." | L1-02.txt:14 ¶4 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F008 | Dijkstra recasts lines of code from "produced" to "spent". | "we should not regard them as "lines produced" but as "lines spent"" | L1-02.txt:52 ¶23 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F009 | Dijkstra renames "software engineering". | "software engineering should be known as "The Doomed Discipline"" | L1-02.txt:46 ¶20 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F010 | Dijkstra states the charter of software engineering. | "software engineering has accepted as its charter "How to program if you cannot."" | L1-02.txt:46 ¶20 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F011 | Dijkstra attacks the term "software maintenance" as misunderstanding. | "Unfathomed misunderstanding is further revealed by the term "software maintenance"" | L1-02.txt:56 ¶25 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F012 | Dijkstra proposes "error" in place of "bug". | "no longer calling a bug a bug but by calling it an error" | L1-02.txt:102 ¶48 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F013 | Dijkstra bans anthropomorphic terminology for programs and equipment. | "never refer to parts of programs or pieces of equipment in an anthropomorphic terminology" | L1-02.txt:104 ¶49 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F014 | Dijkstra defines operational reasoning by its cost. | "This is bad, because operational reasoning is a tremendous waste of mental effort." | L1-02.txt:108 ¶51 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F015 | Dijkstra defines computing science. | "computing science is —and will always be— concerned with the interplay between mechanized and human symbol manipulation" | L1-02.txt:72 ¶33 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F016 | Dijkstra defines a program. | "the program is an abstract symbol manipulator, which can be turned into a concrete one by supplying a computer to it" | L1-02.txt:68 ¶31 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F017 | Dijkstra defines a program as half a conjecture. | "all by itself, a program is no more than half a conjecture" | L1-02.txt:132 ¶63 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F018 | Dijkstra proposes an acronym for computing science. | "I propose that we adopt for computing science FMI (= Formal Methods Initiative)" | L1-02.txt:72 ¶33 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F019 | Dijkstra names a teaching practice "curriculum infantilization". | "such an obvious case of curriculum infantilization that its author should be cited for "contempt" of the student body" | L1-02.txt:130 ¶62 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F020 | Dijkstra uses "reasoning by analogy" as the label for the medieval mode. | "One of its characteristics was that "reasoning by analogy" was rampant" | L1-02.txt:18 ¶6 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F021 | Dijkstra calls "automatic programming" a contradiction in terms. | "it reveals "automatic programming" as a contradiction in terms" | L1-02.txt:72 ¶33 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |

#### L1-03 Cunningham, WyCash Portfolio Management System (1992)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F022 | Cunningham states the debt image and its interest term. | "Shipping first time code is like going into debt." ‖ "Every minute spent on not-quite-right code counts as interest on that debt." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F023 | Cunningham names consolidation as the key to understanding and incremental development. | "providing the consolidation that is key to understanding and continued incremental development" | L1-03.txt:12 ¶3 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F024 | Cunningham names the failure to consolidate as the serious pitfall. | "Another, more serious pitfall is the failure to consolidate." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F025 | Cunningham defines the effect of excess immature code as "unmasterable". | "excess quantities will make a program unmasterable, leading to extreme specialization of programmers" | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F026 | Cunningham names the development mode: incremental growth from a working prototype. | "We developed the product by incremental growth from a working prototype." | L1-03.txt:12 ¶3 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F027 | Cunningham equates the waterfall approach with payment up-front and in-full. | "we recognize this amounts to preserving the concept of payment up-front and in-full" | L1-03.txt:18 ¶6 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |

#### L1-04 Skrenta, "Code is our enemy" (2007; PARTIAL copy: Atwood's quotation only)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F028 | PARTIAL copy. Skrenta, as quoted by Atwood: three-sentence definition of code as bad. | "Code is bad. It rots. It requires periodic maintenance." | L1-04.txt:8 ¶1 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F029 | PARTIAL copy. Skrenta redefines programmer productivity as expressive power. | "increase the productivity of individual programmers in terms of the expressive power of the code they write" | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F030 | PARTIAL copy. Skrenta puts a quadratic term on engineer communication. | "Engineers have n^2 communication costs" | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: vocabulary |

#### L1-05 Atwood, "The Best Code is No Code At All" (2007)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F031 | Atwood states the phrase as clause and as title. | "but the best code is no code at all" ‖ "The Best Code is No Code At All" | L1-05.txt:42 ¶15; L1-05.txt:2 (header line) | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F032 | Atwood defines "Code Smaller" as reducing the volume a programmer must read. | "reduce the volume of code an individual programmer has to read to understand how a program works" | L1-05.txt:35 ¶12 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F033 | Atwood excludes physical-space compression from "Code Smaller". | "to make the code fit into less physical space" | L1-05.txt:35 ¶12 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F034 | Atwood quotes Shipley: first rule of the trade-off. | "Start with brevity. Increase the other dimensions as required by testing." ‖ "Wil Shipley argues that we should rein in our natural tendencies" | L1-05.txt:33 ¶11; L1-05.txt:18 ¶6 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F035 | Atwood quotes Shipley: dimensions of code, all in opposition. | "In coding, you have many dimensions in which you can rate code" ‖ "these dimensions are all in opposition to one another" | L1-05.txt:22 ¶8; L1-05.txt:31 ¶10 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F036 | Atwood names the programmer as the enemy. | "As a software developer, you are your own worst enemy." | L1-05.txt:16 ¶5 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |

#### L1-06 Lee, "Source Code Is A Liability, Not An Asset" (2009)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F037 | Lee states the slogan and credits earlier speakers. | "“Source code is a liability, not an asset!”" ‖ "I got it from (I think) Tim Ottinger and Alan Cooper said it earlier" | L1-06.txt:12 ¶3; L1-06.txt:14 ¶4 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F038 | Lee equates source code with financial debt. | "Source code is akin to financial debt." | L1-06.txt:20 ¶7 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F039 | Lee defines source code as a necessary evil. | "Source code is merely the necessary evil that’s required to create value." | L1-06.txt:18 ¶6 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F040 | Lee defines "ongoing costs" by three verbs. | "Meanwhile, code has ongoing costs. You have to understand it, you have to maintain it, you have to adapt it to new goals over time." | L1-06.txt:24 ¶9 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F041 | Lee defines "underwater" for a mortgage. | "It’s possible to end up underwater in a situation where your debt is actually bigger than your house is worth." | L1-06.txt:22 ¶8 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F042 | Lee applies "debt-to-value ratio" to a code base. | "In some respects, it’s underwater now in terms of its debt-to-value ratio." | L1-06.txt:34 ¶14 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F043 | Lee equates LOC with debt. | "The question is entirely, “What did you do with that LOC/debt?”" | L1-06.txt:26 ¶10 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F044 | Lee defines the work as business value, not code. | "What we actually do is deliver business value, or solutions to real-world problems, or however you want to state it." | L1-06.txt:18 ¶6 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |

#### L2-01 McIlroy, "Mass Produced Software Components" (1968)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F045 | McIlroy defines software components by families and four axes. | "should be available in families arranged according to precision, robustness, generality and timespace performance" | L2-01.txt:12 ¶3 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F046 | McIlroy narrows "mass production techniques" to "techniques". | "In the phrase ‘mass production techniques,’ my emphasis is on ‘techniques’ and not on mass production plain." | L2-01.txt:18 ¶6 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F047 | McIlroy names "binding time" as the secret of component families. | "One phrase contains much of the secret of making families of software components: ‘binding time.’" | L2-01.txt:56 ¶23 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F048 | McIlroy names early-bound parameters "sale time" parameters. | "One might call these early-bound parameters ‘sale time’ parameters." | L2-01.txt:62 ¶26 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F049 | McIlroy states the buyer regards components as black boxes. | "In short, he should be able safely to regard components as black boxes." | L2-01.txt:26 ¶10 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F050 | McIlroy defines mass production of software as multiplicity of models, not replicates. | "‘Mass production’ of software means multiplicity of what manufacturing industry would call ‘models,’ or ‘sizes’ rather than multiplicity of replicates of each." | L2-01.txt:52 ¶21 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F051 | McIlroy contrasts Sysgen (excision) with component construction. | "Sysgen creates systems not by construction, but rather by excision, from an intentionally fat model." | L2-01.txt:58 ¶24 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F052 | McIlroy introduces the "pilot plant". | "Finally I shall raise the question of starting up a ‘pilot plant’ for software components." | L2-01.txt:24 ¶9 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F053 | McIlroy equates interchangeable parts with "modularity". | "The idea of interchangeable parts corresponds roughly to our term ‘modularity,’ and is fitfully respected." | L2-01.txt:18 ¶6 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F054 | McIlroy names his request "industrialism". | "What I have just asked for is simply industrialism" | L2-01.txt:155 ¶71 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |

#### L2-02 Ritchie and Thompson, "The UNIX Time-Sharing System" (1974)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F055 | Ritchie and Thompson define "file descriptor". | "The returned value filep is called a file descriptor." | L2-02.txt:96 ¶44 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F056 | Ritchie and Thompson define "linking" and "link". | "This feature is called linking; a directory entry for a file is sometimes called a link." | L2-02.txt:56 ¶24 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F057 | Ritchie and Thompson define "i-number". | "This pointer is an integer called the i-number (for index number) of the file." | L2-02.txt:125 ¶58 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F058 | Ritchie and Thompson define "image" and "process". | "An image is a computer execution environment." ‖ "A process is the execution of an image." | L2-02.txt:161 ¶72; L2-02.txt:163 ¶73 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F059 | Ritchie and Thompson define "pipe". | "creates an interprocess channel called a pipe" | L2-02.txt:183 ¶83 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F060 | Ritchie and Thompson define "filter". | "A program such as pr which copies its standard input to its standard output (with processing) is called a filter." | L2-02.txt:261 ¶121 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F061 | Ritchie and Thompson define "the Shell". | "The Shell is a command line interpreter: it reads lines typed by the user and interprets them as requests to execute other programs." | L2-02.txt:213 ¶98 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F062 | Ritchie and Thompson name "special files" as the most unusual feature. | "Special files constitute the most unusual feature of the UNIX file system." | L2-02.txt:64 ¶28 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F063 | Ritchie and Thompson define "mount" by the tree-graft image. | "In effect, mount replaces a leaf of the hierarchy tree (the ordinary file) by a whole new subtree" | L2-02.txt:70 ¶31 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F064 | Ritchie and Thompson name the size-constraint philosophy "salvation through suffering". | "This may be a thinly disguised version of the “salvation through suffering” philosophy, but in our case it worked." | L2-02.txt:353 ¶166 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F065 | Ritchie and Thompson name the system "self-supporting". | "It is worth noting that the system is totally self-supporting." | L2-02.txt:28 ¶10 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F066 | Ritchie and Thompson define UNIX success as exploitation of "fertile ideas". | "The success of UNIX lies not so much in new inventions but rather in the full exploitation of a carefully selected set of fertile ideas" | L2-02.txt:367 ¶173 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |

#### L2-03 Hietaniemi, CPAN "private showing" (1995; PARTIAL copy: the pre-launch mail, not the launch post)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F067 | Hietaniemi names the pre-launch mail a "private showing" for archive keepers. PARTIAL copy: not the launch post. | "Subject: CPAN "private showing"" ‖ "This "release" is mainly meant for the current keepers of the / various Perl archives." | L2-03.txt:11 ¶1; L2-03.txt:23-24 ¶4 | SUBSTRATE L2-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F068 | Hietaniemi names the contributors' task "Comparative Perl Archaeology". PARTIAL copy. | "you have 7.5 weeks time to practise Comparative Perl Archaeology" | L2-03.txt:36 ¶5 | SUBSTRATE L2-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F069 | Hietaniemi states the goal of CPAN as "Mother of All Perl Archives". PARTIAL copy. | "of the CPAN is to be the Mother of All Perl Archives" | L2-03.txt:38 ¶5 | SUBSTRATE L2-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F070 | The saved copy never expands "CPAN" (grep -ci "comprehensive" L2-03.txt = 0); the launch post is not held, so the expansion is unverified. | "of the CPAN is to be the Mother of All Perl Archives" | L2-03.txt:38 ¶5 | SUBSTRATE L2-03 | NONE | UNVERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F071 | Hietaniemi calls the first state of CPAN "skeletal". PARTIAL copy. | "enhancements for this skeletal CPAN" | L2-03.txt:35 ¶5 | SUBSTRATE L2-03 | NONE | VERIFIED | PRESERVE: vocabulary |

#### L2-04 Koçulu, "I've Just Liberated My Modules" (2016)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F072 | Koçulu defines his act as unpublishing all modules. | "Summary; NPM is no longer a place that I’ll share my open source work at, so, I’ve just unpublished all my modules." | L2-04.txt:14 ¶4 | SUBSTRATE L2-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F073 | Koçulu's title names the same act "liberated" (header of the saved copy). | "I've Just Liberated My Modules" | L2-04.txt:2 (header line) | SUBSTRATE L2-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F074 | Koçulu names NPM "private land". | "NPM is someone’s private land where corporate is more powerful than the people" | L2-04.txt:12 ¶3 | SUBSTRATE L2-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F075 | Koçulu names his motive "Power To The People". | "I do open source because, Power To The People" | L2-04.txt:12 ¶3 | SUBSTRATE L2-04 | NONE | VERIFIED | PRESERVE: vocabulary |

#### L2-05 Cox, "Our Software Dependency Problem" (2019)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F076 | Cox defines "dependency". | "In today’s software development world, a dependency is additional code that you want to call from your program." | L2-05.txt:16 ¶5 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F077 | Cox fixes "package" and lists its synonyms. | "In this article we’ll call that unit of code a package; some systems use terms like library or module instead of package." | L2-05.txt:16 ¶5 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F078 | Cox defines "package" a second time, by source. | "A package, for this discussion, is code you download from the internet." | L2-05.txt:39 ¶13 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F079 | Cox defines "dependency manager". | "A dependency manager (sometimes called a package manager) automates the downloading and installation of dependency packages." | L2-05.txt:20 ¶7 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F080 | Cox defines the fixed costs of reuse by their effect on package size. | "But the high fixed costs of reuse mean that manually-reused packages tend to be big: a tiny package would be easier to reimplement." | L2-05.txt:18 ¶6 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F081 | Cox names "reputational support" as the replacement for commercial and legal support. | "The commercial and legal support for trusting our software sources was replaced by reputational support." | L2-05.txt:45 ¶16 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F082 | Cox defines the cost of adopting a bad dependency as an expected-cost sum. | "the sum, over all possible bad outcomes, of the cost of each bad outcome multiplied by its probability of happening (risk)" | L2-05.txt:49 ¶18 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F083 | Cox equates indirect with direct dependencies in effect. | "Flaws in indirect dependencies are just as bad for your program as flaws in direct dependencies." | L2-05.txt:111 ¶49 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F084 | Cox names the SQLite single-file distribution "the amalgamation". | "a single 200,000-line C source file and a single 11,000-line header, the “amalgamation.”" | L2-05.txt:75 ¶31 | SUBSTRATE L2-05 | NONE | VERIFIED | CUT: example |
| distinctions-vocabulary-F085 | Cox names "creeping dependencies". | "Creeping dependencies can also affect the size of your project." | L2-05.txt:169 ¶78 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F086 | Cox's section headings form a verb sequence on one noun. | "Inspect the dependency" ‖ "Test the dependency" ‖ "Abstract the dependency" ‖ "Isolate the dependency" ‖ "Avoid the dependency" ‖ "Upgrade the dependency" ‖ "Watch your dependencies" | L2-05.txt:57 ¶22; L2-05.txt:115 ¶51; L2-05.txt:121 ¶54; L2-05.txt:129 ¶58; L2-05.txt:135 ¶61; L2-05.txt:143 ¶65; L2-05.txt:161 ¶74 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F087 | Cox names code that needs no change "done". | "some code really is “done.”" | L2-05.txt:91 ¶39 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F088 | Cox defines the thin wrapper. | "define an interface of your own, along with a thin wrapper implementing that interface using the dependency" | L2-05.txt:125 ¶56 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |

### Q2. Which binary distinctions does each text draw? Quote both poles.

#### L1-01 Hertzfeld, "-2000 Lines Of Code" (1982)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F089 | L1-01: lines written (managers' form) against lines saved (Atkinson's rewrite). | "a field for the number of lines of code that were written that week" ‖ "the rewrite also saved around 2,000 lines of code" | L1-01.txt:8 ¶1; L1-01.txt:12 ¶3 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F090 | L1-01: the lines-of-code measure against the goal of a small, fast program. | "lines of code was a silly measure of software productivity" ‖ "write as small and fast a program as possible" | L1-01.txt:10 ¶2 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F091 | L1-01: bloated code against a simpler, more general algorithm. | "sloppy, bloated, broken code" ‖ "a simpler, more general algorithm" | L1-01.txt:10 ¶2; L1-01.txt:12 ¶3 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: distinction |

#### L1-02 Dijkstra, EWD 1036 (1988)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F092 | L1-02: lines produced against lines spent. | "we should not regard them as "lines produced" but as "lines spent"" | L1-02.txt:52 ¶23 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F093 | L1-02: gradual change against radical novelty. | "gradual change seems to be all but the only paradigm of history" ‖ "automatic computers represent a radical novelty" | L1-02.txt:20 ¶7; L1-02.txt:32 ¶13 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F094 | L1-02: link-new-to-old by analogy against the orthogonal method. | "by means of metaphors and analogies we try to link the new to the old" ‖ "Coping with radical novelty requires an orthogonal method." | L1-02.txt:12 ¶3; L1-02.txt:14 ¶4 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F095 | L1-02: analogue mechanisms against the first large-scale digital device. | "the vast majority of our mechanisms are viewed as analogue devices" ‖ "the automatic computer is our first large-scale digital device" | L1-02.txt:38 ¶16 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F096 | L1-02: bug against error. | "no longer calling a bug a bug but by calling it an error" | L1-02.txt:102 ¶48 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F097 | L1-02: testing (presence of bugs) against proven theorems. | "may convincingly demonstrate the presence of bugs, but can never demonstrate their absence" ‖ "The programmer's task is to present such complete conjectures as proven theorems." | L1-02.txt:54 ¶24; L1-02.txt:132 ¶63 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F098 | L1-02: mimicking against providing an alternative to. | "Please note the difference between "mimicking" and "providing an alternative to"" | L1-02.txt:74 ¶34 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F099 | L1-02: operational reasoning against reasoning from the program text. | "operational reasoning is a tremendous waste of mental effort" ‖ "reason about programs without even mentioning their possible "behaviours"" | L1-02.txt:108 ¶51; L1-02.txt:126 ¶60 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F100 | L1-02: entry-level job training against fifty-year intellectual baggage. | "training its graduates for today's entry-level jobs" ‖ "the intellectual bagage and attitudes that will last them another 50 years" | L1-02.txt:94 ¶44 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F101 | L1-02: teaching hard science against infantilization of the curriculum. | "will continue to lack the courage to teach hard science" ‖ "each next stage of infantilization of the curriculum will be hailed as educational progress" | L1-02.txt:98 ¶46 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F102 | L1-02: intuition against uninterpreted formulae. | "To further sever the links to intuition, we rename the values {true, false} of the boolean domain as {black, white}." | L1-02.txt:136 ¶65 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F160 | L1-02: a bug as an intruder against an error as the programmer's own act. | "it squarely puts the blame where it belongs, viz. with the programmer who made the error" | L1-02.txt:102 ¶48 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |

#### L1-03 Cunningham, WyCash Portfolio Management System (1992)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F103 | L1-03: debt repaid by rewrite against debt not repaid. | "A little debt speeds development so long as it is paid back promptly with a rewrite." ‖ "The danger occurs when the debt is not repaid." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F104 | L1-03: consolidation against failure to consolidate. | "the consolidation that is key to understanding and continued incremental development" ‖ "Another, more serious pitfall is the failure to consolidate." | L1-03.txt:12 ¶3; L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F105 | L1-03: incremental growth against payment up-front and in-full. | "the alternative, incremental growth, both feasible and desirable" ‖ "preserving the concept of payment up-front and in-full" | L1-03.txt:18 ¶6 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F106 | L1-03: familiarity with the product against extreme specialization. | "the best antidote is more complete familiarity with the product and its implementation" ‖ "leading to extreme specialization of programmers and finally an inflexible product" | L1-03.txt:14 ¶4; L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F107 | L1-03: immature code against mature sections. | "Although immature code may work fine and be completely acceptable to the customer" ‖ "Mature sections of the program have been revised or rewritten many times" | L1-03.txt:16 ¶5; L1-03.txt:12 ¶3 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: distinction |

#### L1-04 Skrenta, "Code is our enemy" (2007; PARTIAL copy: Atwood's quotation only)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F108 | L1-04 (PARTIAL copy): capability against a basket of costs. | "while expanding its capability, also increases a whole basket of costs" | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F109 | L1-04 (PARTIAL copy): more code needs more engineers against less code for the same thing. | "To make more code requires more engineers." ‖ "Less code to do the same thing (and possibly better)." | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: distinction |

#### L1-05 Atwood, "The Best Code is No Code At All" (2007)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F110 | L1-05: code is not the enemy against the programmer as the enemy. | "Code isn’t our enemy." ‖ "you are your own worst enemy" | L1-05.txt:14 ¶4; L1-05.txt:16 ¶5 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F111 | L1-05: no code against brevity as the fallback. | "the best code is no code at all" ‖ "the next best thing is to start with brevity" | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F112 | L1-05 (quoting Shipley): brevity first, other dimensions raised by testing. | "these dimensions are all in opposition to one another" ‖ "Start with brevity." | L1-05.txt:31 ¶10; L1-05.txt:33 ¶11 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F113 | L1-05: volume a programmer reads against physical space. | "reduce the volume of code an individual programmer has to read" ‖ "to make the code fit into less physical space" | L1-05.txt:35 ¶12 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F114 | L1-05: love of writing code against writing as little as possible. | "we love writing code" ‖ "you’ll love it enough to write as little of it as possible" | L1-05.txt:18 ¶6; L1-05.txt:44 ¶16 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F115 | L1-05: willingly bringing code into the world against writing it reluctantly. | "Every new line of code you willingly bring into the world" ‖ "you should do so reluctantly, under duress" | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: distinction |

#### L1-06 Lee, "Source Code Is A Liability, Not An Asset" (2009)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F116 | L1-06: liability against asset. | "“Source code is a liability, not an asset!”" | L1-06.txt:12 ¶3 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F117 | L1-06: business value against source code. | "What we actually do is deliver business value" ‖ "Source code is merely the necessary evil that’s required to create value." | L1-06.txt:18 ¶6 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F118 | L1-06: wrote LOC against removed LOC. | "“This week our team wrote 10k LOC!" ‖ "“This week we removed 10K LOC while preserving all existing functionality!”" | L1-06.txt:26 ¶10; L1-06.txt:28 ¶11 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F119 | L1-06: third-party library against own implementation. | "whether to use a third-party library or write your own implementation" | L1-06.txt:30 ¶12 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F120 | L1-06: maintainable verbose code against dense impenetrable code. | "well-written, maintainable code is often more verbose than dense, impenetrable code" | L1-06.txt:30 ¶12 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F121 | L1-06: refactor existing code against piling new stuff on old. | "refactor existing code to meet changing requirements vs. simply piling your new stuff on top of the old stuff" | L1-06.txt:30 ¶12 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F122 | L1-06: underwater against above water. | "it’s underwater now" ‖ "get yourself above water as soon as possible" | L1-06.txt:34 ¶14; L1-06.txt:36 ¶15 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F123 | L1-06 (self-labelled aside): employee cost against licence fee. | "at a true cost of at least $10,000 a month" ‖ "avoid paying $1000 or even $500 to license a third-party software package" | L1-06.txt:32 ¶13 | SUBSTRATE L1-06 | NONE | VERIFIED | CUT: aside |

#### L2-01 McIlroy, "Mass Produced Software Components" (1968)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F124 | L2-01: industrialists against crofters. | "they are the industrialists and we are the crofters" | L2-01.txt:16 ¶5 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F125 | L2-01: techniques against mass production plain. | "my emphasis is on ‘techniques’ and not on mass production plain" | L2-01.txt:18 ¶6 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F126 | L2-01: build against take off the shelf. | "What table mechanism shall we build?’" ‖ "start taking such things off the shelf" | L2-01.txt:20 ¶7 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F127 | L2-01: multiplicity of models against multiplicity of replicates. | "multiplicity of what manufacturing industry would call ‘models,’ or ‘sizes’ rather than multiplicity of replicates of each" | L2-01.txt:52 ¶21 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F128 | L2-01: construction against excision. | "Sysgen creates systems not by construction, but rather by excision, from an intentionally fat model." | L2-01.txt:58 ¶24 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F129 | L2-01: systems against components. | "The pinnacle of software is systems" ‖ "Components, dignified as a hardware field, is unknown as a legitimate branch of software." | L2-01.txt:20 ¶7 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F130 | L2-01: sale-time binding against run-time binding. | "sale-time binding causes no degradation over runtime binding" | L2-01.txt:141 ¶64 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F131 | L2-01: written by experts against written by hacks. | "specified by experts, and have then been written by hacks" | L2-01.txt:111 ¶49 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F132 | L2-01: university research against production orientation. | "I think that the whole project is an improbable one for university research." ‖ "the guiding spirit of the undertaking must be production oriented" | L2-01.txt:137 ¶62 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F133 | L2-01: standardizing into existence against models first. | "I don’t think a components industry can be standardized into existence." ‖ "it would be rash to standardize before we have the models" | L2-01.txt:149 ¶68 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |

#### L2-02 Ritchie and Thompson, "The UNIX Time-Sharing System" (1974)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F134 | L2-02: interactive system against batch system. | "a properly designed interactive system is much more productive and satisfying to use than a “batch” system" | L2-02.txt:351 ¶165 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F135 | L2-02: no predefined objectives against someone else's requirements. | "it was not designed to meet any predefined objectives" ‖ "We have not been faced with the need to satisfy someone else’s requirements" | L2-02.txt:347 ¶163 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F136 | L2-02: new inventions against fertile ideas. | "not so much in new inventions but rather in the full exploitation of a carefully selected set of fertile ideas" | L2-02.txt:367 ¶173 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F137 | L2-02: appears synchronous and unbuffered against a complicated buffering mechanism. | "both reading and writing of files appear to be synchronous and unbuffered" ‖ "the system maintains a rather complicated buffering mechanism" | L2-02.txt:147 ¶65 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F138 | L2-02: locks necessary against locks sufficient. | "locks are neither necessary nor sufficient, in our environment, to prevent interference between users of the same file" | L2-02.txt:100 ¶46 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F139 | L2-02: a wide variety of output options inside each command, judged unwise (the alternative is redirection and filters). | "unwise for efficiency reasons, to expect authors of commands such as ls to provide such a wide variety of output options" | L2-02.txt:259 ¶120 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F140 | L2-02: system size against ease of understanding. | "The size of the new system is about one third greater than the old." ‖ "we considered this increase in size quite acceptable" | L2-02.txt:36 ¶14 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F141 | L2-02: size constraint against economy and elegance. | "the size constraint has encouraged not only economy but a certain elegance of design" | L2-02.txt:353 ¶166 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F142 | L2-02: file structure controlled by programs against controlled by the system. | "the structure of files is controlled by the programs which use them, not by the system" | L2-02.txt:44 ¶18 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F143 | L2-02: access-method routines against direct system calls. | "No large ‘‘access method” routines are required to insulate the programmer from the system calls" | L2-02.txt:357 ¶168 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |

#### L2-03 Hietaniemi, CPAN "private showing" (1995; PARTIAL copy: the pre-launch mail, not the launch post)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F144 | L2-03 (PARTIAL copy): an incoming/ directory of snippets against tidy tarballs. | "wade through umpteen dozen little perl snippets in the incoming/" ‖ "please create tidy .tar.gz:s in somewhere" | L2-03.txt:46 ¶6; L2-03.txt:48 ¶6 | SUBSTRATE L2-03 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F145 | L2-03 (PARTIAL copy): skeletal CPAN against Mother of All Perl Archives. | "enhancements for this skeletal CPAN" ‖ "of the CPAN is to be the Mother of All Perl Archives" | L2-03.txt:35 ¶5; L2-03.txt:38 ¶5 | SUBSTRATE L2-03 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F146 | L2-03 (PARTIAL copy): UNIX packing formats against non-UNIX formats. | "no zips/lzhs/lhas for UNIX stuff, make them to be tars" ‖ "such native packing formats are quite ok for non-UNIX stuff" | L2-03.txt:64 ¶10; L2-03.txt:65 ¶10 | SUBSTRATE L2-03 | NONE | VERIFIED | PRESERVE: distinction |

#### L2-04 Koçulu, "I've Just Liberated My Modules" (2016)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F147 | L2-04: private land of corporate power against the people. | "NPM is someone’s private land where corporate is more powerful than the people" | L2-04.txt:12 ¶3 | SUBSTRATE L2-04 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F148 | L2-04: point at the repo against take ownership of the module. | "You can either point your dependency to repo directly (azer/dependency) or if you volunteer to take ownership of any module in my Github" | L2-04.txt:18 ¶6 | SUBSTRATE L2-04 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F149 | L2-04: knee-jerk action against belief in a free alternative. | "This is not a knee-jerk action." ‖ "open source community will eventually create a truly free alternative for NPM" | L2-04.txt:16 ¶5 | SUBSTRATE L2-04 | NONE | VERIFIED | PRESERVE: distinction |

#### L2-05 Cox, "Our Software Dependency Problem" (2019)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F150 | L2-05: discussion of reuse against actual reuse. | "For decades, discussion of software reuse was far more common than actual software reuse." | L2-05.txt:8 ¶1 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F151 | L2-05: manually reused big packages against managed small packages. | "manually-reused packages tend to be big" ‖ "the lower fixed costs make smaller packages economical to publish and reuse" | L2-05.txt:18 ¶6; L2-05.txt:20 ¶7 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F152 | L2-05: software bought from known sources against code from a stranger. | "That software was bought from known sources" ‖ "code downloaded from this stranger on the internet" | L2-05.txt:43 ¶15; L2-05.txt:39 ¶13 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F153 | L2-05: personal hobby project against production software. | "a personal hobby project, where the cost of most bad outcomes is near zero" ‖ "production software that must be maintained for years" | L2-05.txt:53 ¶20 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F154 | L2-05: a little copying against a little dependency (a Go proverb). | "A little copying is better than a little dependency." | L2-05.txt:141 ¶64 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F155 | L2-05: install cost against evaluation and maintenance cost. | "eliminated the cost of downloading and installing a dependency" ‖ "reducing the cost of the kind of evaluation and maintenance necessary to use a dependency" | L2-05.txt:193 ¶90 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F156 | L2-05: direct against indirect dependencies. | "Flaws in indirect dependencies are just as bad for your program as flaws in direct dependencies." | L2-05.txt:111 ¶49 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F157 | L2-05: "if it ain't broke" against upgrading quickly. | "the conventional wisdom about software was “if it ain’t broke, don’t fix it.”" ‖ "delaying an upgrade is riskier than upgrading quickly" | L2-05.txt:145 ¶66; L2-05.txt:157 ¶72 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F158 | L2-05: personal projects against paid developers. | "personal projects that developers create and share for fun" ‖ "the result of thousands of hours of work by a group of paid developers" | L2-05.txt:89 ¶38 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F159 | L2-05: more code against less justification. | "We are trusting more code with less justification for doing so." | L2-05.txt:47 ¶17 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |

### Q3. Which metaphors carry each text's argument? Quote each metaphor's first full statement and every extension.

#### L1-01 Hertzfeld, "-2000 Lines Of Code" (1982)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F161 | L1-01 metaphor: code as bloated mass. First statement; no extension in the text. | "sloppy, bloated, broken code" | L1-01.txt:10 ¶2 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F162 | L1-01 implicit ledger: a negative sign applied to a production count; the text states it as an act, not an image. | "wrote in the number: -2000" | L1-01.txt:14 ¶4 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: distinction |

#### L1-02 Dijkstra, EWD 1036 (1988)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F163 | L1-02 metaphor A (analogy as a faulty tool). First statement. | "the analogies become too shallow, and the metaphors become more misleading than illuminating" | L1-02.txt:12 ¶3 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F164 | L1-02 metaphor A, extension 1: the cash-register analogy for computers. | "But the analogy is ridiculously shallow" | L1-02.txt:36 ¶15 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F165 | L1-02 metaphor A, extension 2: the program-as-device analogy. | "the analogy is too shallow because a program is, as a mechanism, totally different from all the familiar analogue devices we grew up with" | L1-02.txt:40 ¶17 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F166 | L1-02 metaphor A, extension 3: the "programming tools" analogy. | "the shallowness of the underlying analogy is worthy of the Middle Ages" | L1-02.txt:58 ¶26 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F167 | L1-02 metaphor A, extension 4: the personification analogy. | "The analogy that underlies this personification is so shallow that it is not only misleading but also paralyzing." | L1-02.txt:106 ¶50 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F168 | L1-02 metaphor B (analogy as medieval stagnation). First statement. | "One of its characteristics was that "reasoning by analogy" was rampant; another characteristic was almost total intellectual stagnation" | L1-02.txt:18 ¶6 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F169 | L1-02 metaphor B, extension. | "by developing a keen ear for unwarranted analogies, one can detect a lot of medieval thinking today" | L1-02.txt:18 ¶6 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F170 | L1-02 metaphor C (planning in yesterday's vocabulary). First statement. | "The usual way in which we plan today for tomorrow is in yesterday's vocabulary." | L1-02.txt:10 ¶2 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F171 | L1-02 metaphor C, extension: radical novelty as a new foreign language. | "creating and learning a new foreign language that can not be translated into one's mother tongue" | L1-02.txt:14 ¶4 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F172 | L1-02 metaphor D (the ledger). Sole statement; no extension. | "book that count on the wrong side of the ledger" | L1-02.txt:52 ¶23 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F173 | L1-02 metaphor E (name magic). First statement. | "the superstition that knowing someone's true name gives you magic power over him" | L1-02.txt:48 ¶21 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F174 | L1-02 metaphor E, extension: calling the demon "engineering". | "calling it by a safe, familiar, and innocent name, such as "engineering"" | L1-02.txt:50 ¶22 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F175 | L1-02 metaphor F (alchemist). First statement. | "just like the alchemist of yore, who continued to refine his chrysocosmic purifications" | L1-02.txt:54 ¶24 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F176 | L1-02 metaphor F, extension: snake oil. | "yet another dimension of the snake oil business" | L1-02.txt:58 ¶26 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F177 | L1-02 metaphor G (the kite). First statement; repeated twice in the proposal section. | "But that kite won't fly, for I know the real world only too well" | L1-02.txt:144 ¶69 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F178 | L1-02 metaphor G, extension 1. | "But that kite won't fly either" | L1-02.txt:146 ¶70 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F179 | L1-02 metaphor G, extension 2. | "Needless to say, that kite won't fly either." | L1-02.txt:148 ¶71 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F180 | L1-02 metaphor H (foggy crystal ball). First statement. | "if I look into my foggy crystal ball at the future of computing science education" | L1-02.txt:98 ¶46 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: aside |
| distinctions-vocabulary-F181 | L1-02 metaphor H, extension. | "I now have had my foggy crystal ball for quite a long time." | L1-02.txt:100 ¶47 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: aside |
| distinctions-vocabulary-F182 | L1-02 metaphor I (the bug as animistic metaphor). First statement. | "The animistic metaphor of the bug that maliciously sneaked in while the programmer was not looking is intellectually dishonest" | L1-02.txt:102 ¶48 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F183 | L1-02 metaphor I, extension: programs with wants and beliefs. | "I have now encountered programs wanting things, knowing things, expecting things, believing things, etc." | L1-02.txt:106 ¶50 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F184 | L1-02 metaphor J (programs wear out). Stated as the target of attack. | "Your car needs maintenance too, doesn't it?" | L1-02.txt:56 ¶25 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F185 | L1-02 metaphor K (running). First statement is Robbins's, quoted. | "Nobody is going to run 100 meters in five seconds" | L1-02.txt:24 ¶9 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F186 | L1-02 metaphor K, extension: Dijkstra turns the running image against its author. | "for going from A to B fast, there could now exist alternatives to running that are orders of magnitude more effective" | L1-02.txt:26 ¶10 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F187 | L1-02 metaphor L (jet against baby) scales the analogy gap. | "comparing, as a means of transportation, the supersonic jet plane with a crawling baby" | L1-02.txt:36 ¶15 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: example |
| distinctions-vocabulary-F257 | L1-02 metaphor K, extension: the author names the image as Robbins's own analogy. | "Using Robbins's own analogy" | L1-02.txt:26 ¶10 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F258 | L1-02 metaphor I, extension: the anthropomorphic metaphor as a handicap. | "is an enormous handicap for every computing community that has adopted it" | L1-02.txt:106 ¶50 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F259 | L1-02 analogy as a teaching method: linking new material to the student's familiar world. | "They consciously try to link the new material to what is supposed to be the student's familiar world." | L1-02.txt:28 ¶11 | SUBSTRATE L1-02 | NONE | VERIFIED | CUT: repetition |

#### L1-03 Cunningham, WyCash Portfolio Management System (1992)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F188 | L1-03 metaphor (debt). First statement. | "Shipping first time code is like going into debt." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F189 | L1-03 debt, extension 1: a little debt speeds development if repaid. | "A little debt speeds development so long as it is paid back promptly with a rewrite." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: principle |
| distinctions-vocabulary-F190 | L1-03 debt, extension 2: interest. | "Every minute spent on not-quite-right code counts as interest on that debt." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F191 | L1-03 debt, extension 3: debt load. | "Entire engineering organizations can be brought to a stand-still under the debt load of an unconsolidated implementation" | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F192 | L1-03 debt, extension 4: the danger. | "The danger occurs when the debt is not repaid." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F193 | L1-03 debt, extension 5: objects lower the transaction cost. | "Objects make the cost of this transaction tolerable." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F194 | L1-03 debt, extension 6: the author names the image an analogy and maps waterfall to it. | "using our debt analogy, we recognize this amounts to preserving the concept of payment up-front and in-full" | L1-03.txt:18 ¶6 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F195 | L1-03 medical image (antidote, pitfall); stated once. | "Here the best antidote is more complete familiarity with the product and its implementation." | L1-03.txt:14 ¶4 | SUBSTRATE L1-03 | NONE | VERIFIED | CUT: repetition |

#### L1-04 Skrenta, "Code is our enemy" (2007; PARTIAL copy: Atwood's quotation only)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F196 | L1-04 (PARTIAL copy) metaphor: code as decaying matter. First statement. | "Code is bad. It rots." | L1-04.txt:8 ¶1 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F197 | L1-04 (PARTIAL copy) extension: bugs hide in code. | "The more code you have, the more places there are for bugs to hide." | L1-04.txt:8 ¶1 | SUBSTRATE L1-04 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F198 | L1-04 (PARTIAL copy) extension: a basket of costs. | "also increases a whole basket of costs" | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F199 | L1-04: the "enemy" image is in the saved copy only as its header title (from link text and search index). The post body is PARTIAL; Skrenta's own use of the image is unverified. | "Code is our enemy" | L1-04.txt:2 (header line) | SUBSTRATE L1-04 | NONE | UNVERIFIED | PRESERVE: vocabulary |

#### L1-05 Atwood, "The Best Code is No Code At All" (2007)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F200 | L1-05 attributes the enemy image to Skrenta. | "Rich Skrenta writes that code is our enemy." | L1-05.txt:8 ¶1 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F201 | L1-05 metaphor (the enemy in the mirror). First statement: Atwood inverts the image. | "You want to see the real enemy? Go look in the mirror." | L1-05.txt:14 ¶4 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F202 | L1-05 enemy, extension 1. | "As a software developer, you are your own worst enemy." | L1-05.txt:16 ¶5 | SUBSTRATE L1-05 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F203 | L1-05 enemy, extension 2: the condition under which code is the enemy. | "Code is only our enemy because there are so many of us programmers writing so damn much of it." | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F204 | L1-05 metaphor (code as a newborn). First statement. | "The code, like a newborn babe, is blameless and innocent the minute it is written into the world." | L1-05.txt:14 ¶4 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F205 | L1-05 newborn, extension. | "Every new line of code you willingly bring into the world" | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F206 | L1-05 metaphor (love of code). First statement. | "we love writing code" | L1-05.txt:18 ¶6 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F207 | L1-05 love, extension 1. | "they love code so much" | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F208 | L1-05 love, extension 2: the closing turn. | "you’ll love it enough to write as little of it as possible" | L1-05.txt:44 ¶16 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: moral core |
| distinctions-vocabulary-F209 | L1-05 metaphor (writing under duress). | "Every time you write new code, you should do so reluctantly, under duress" | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F210 | L1-05 (quoting Shipley) metaphor: dimensions raised and lowered. | "you’ve gotten two of your dimensions up, but you’ve spent three days, so the “time spent coding” dimension is way down" | L1-05.txt:31 ¶10 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F211 | L1-05 aside: duct tape and coat hanger. | "We never met a problem we couldn’t solve with some duct tape, a jury-rigged coat hanger, and a pinch of code." | L1-05.txt:18 ¶6 | SUBSTRATE L1-05 | NONE | VERIFIED | CUT: aside |

#### L1-06 Lee, "Source Code Is A Liability, Not An Asset" (2009)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F212 | L1-06 metaphor (debt, mortgage). First statement. | "Source code is akin to financial debt." | L1-06.txt:20 ¶7 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F213 | L1-06 debt, extension 1: interest. | "You have to pay interest on your debt every month." | L1-06.txt:20 ¶7 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F214 | L1-06 debt, extension 2: the mortgage should be as small as the need allows. | "You always want your mortgage to be as small as possible while still allowing you to buy a house that meets your needs." | L1-06.txt:20 ¶7 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: principle |
| distinctions-vocabulary-F215 | L1-06 debt, extension 3: underwater. | "It’s possible to end up underwater in a situation where your debt is actually bigger than your house is worth." | L1-06.txt:22 ¶8 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F216 | L1-06 debt, extension 4: the bridge sentence that maps house to software. | "So too in software development." | L1-06.txt:24 ¶9 | SUBSTRATE L1-06 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F217 | L1-06 debt, extension 5: a week of LOC as a week of debt. | "This week we took on $10,000 in new debt!" | L1-06.txt:26 ¶10 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F218 | L1-06 debt, extension 6: removal as debt reduction. | "it contributes to your organization’s long-term health in the same way as reducing your financial debt" | L1-06.txt:28 ¶11 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F219 | L1-06 debt, extension 7: the debt-to-value ratio. | "In some respects, it’s underwater now in terms of its debt-to-value ratio." | L1-06.txt:34 ¶14 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F220 | L1-06 debt, extension 8: paying down. | "one of the most beneficial things you can do is to start paying down the debt" | L1-06.txt:36 ¶15 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: principle |
| distinctions-vocabulary-F221 | L1-06 debt, extension 9: debt as paralysis. | "that debt is going to paralyze any other efforts to deliver new value to your customers" | L1-06.txt:36 ¶15 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F222 | L1-06 debt, extension 10: above water. | "get yourself above water as soon as possible" | L1-06.txt:36 ¶15 | SUBSTRATE L1-06 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F223 | L1-06 metaphor: deletion as weeding. | "Bust out your delete key and start whacking." | L1-06.txt:36 ¶15 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |

#### L2-01 McIlroy, "Mass Produced Software Components" (1968)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F224 | L2-01 metaphor (industry). First statement. | "We undoubtedly get the short end of the stick in confrontations with hardware people because they are the industrialists and we are the crofters." | L2-01.txt:16 ¶5 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F225 | L2-01 industry, extension 1: structural shapes, screws, resistors. | "quite as mechanical design is abetted by the existence of families of structural shapes, screws or resistors" | L2-01.txt:12 ¶3 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F226 | L2-01 industry, extension 2: subassemblies. | "The idea of subassemblies carries over directly and is well exploited." | L2-01.txt:18 ¶6 | SUBSTRATE L2-01 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F227 | L2-01 industry, extension 3: machine tools. | "The idea of machine tools has an analogue in assembly programs and compilers." | L2-01.txt:18 ¶6 | SUBSTRATE L2-01 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F228 | L2-01 industry, limit: the author calls the analogy fragile. | "Yet this fragile analogy is belied when we seek for analogues of other tangible symbols of mass production." | L2-01.txt:18 ¶6 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F229 | L2-01 industry, extension 4: the standard-parts catalogue. | "There do not exist manufacturers of standard parts, much less catalogues of standard parts." | L2-01.txt:18 ¶6 | SUBSTRATE L2-01 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F230 | L2-01 industry, extension 5: circuit modules. | "just as an electronics firm selling circuit modules for only one purpose would have trouble in the market" | L2-01.txt:131 ¶59 | SUBSTRATE L2-01 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F231 | L2-01 industry, extension 6: the Sears-Roebuck catalogue. | "A comprehensive and physically condensed document like the Sears-Roebuck catalogue" | L2-01.txt:143 ¶65 | SUBSTRATE L2-01 | NONE | VERIFIED | CUT: example |
| distinctions-vocabulary-F232 | L2-01 industry, extension 7: the pilot-plant staff. | "with the masses of coders removed" | L2-01.txt:139 ¶63 | SUBSTRATE L2-01 | NONE | VERIFIED | CUT: repetition |

#### L2-02 Ritchie and Thompson, "The UNIX Time-Sharing System" (1974)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F233 | L2-02 metaphor (tree). First statement. | "The directory structure is constrained to have the form of a rooted tree." | L2-02.txt:60 ¶26 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F234 | L2-02 tree, extension: mount as grafting a subtree. | "In effect, mount replaces a leaf of the hierarchy tree (the ordinary file) by a whole new subtree" | L2-02.txt:70 ¶31 | SUBSTRATE L2-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F235 | L2-02 metaphor (kinship of processes). First statement. | "The new processes differ only in that one is considered the parent process" | L2-02.txt:173 ¶78 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F236 | L2-02 kinship, extension. | "if the parent has already terminated, the status is available to the grandparent, and so on" | L2-02.txt:209 ¶96 | SUBSTRATE L2-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F237 | L2-02 kinship, extension: termination. | "terminates a process, destroys its image, closes its open files, and generally obliterates it" | L2-02.txt:209 ¶96 | SUBSTRATE L2-02 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F238 | L2-02 metaphor (plumbing). First statement is the definition. | "creates an interprocess channel called a pipe" | L2-02.txt:183 ¶83 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F239 | L2-02 plumbing, extension: the process does not know the channel. | "Neither process need know that a pipe, rather than an ordinary file, is involved." | L2-02.txt:183 ¶83 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F240 | L2-02 metaphor (a hospitable environment). | "set out to create a more hospitable environment" | L2-02.txt:347 ¶163 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |

#### L2-03 Hietaniemi, CPAN "private showing" (1995; PARTIAL copy: the pre-launch mail, not the launch post)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F241 | L2-03 (PARTIAL copy) metaphor (archaeology). First statement. | "you have 7.5 weeks time to practise Comparative Perl Archaeology" | L2-03.txt:36 ¶5 | SUBSTRATE L2-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F242 | L2-03 (PARTIAL copy) archaeology, extension: the mother archive. | "of the CPAN is to be the Mother of All Perl Archives" | L2-03.txt:38 ¶5 | SUBSTRATE L2-03 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F243 | L2-03 (PARTIAL copy) metaphor (battle with the mailbox). | "after several days / of battling with my obscenely overflowing mailbox" | L2-03.txt:44-45 ¶6 | SUBSTRATE L2-03 | NONE | VERIFIED | CUT: aside |
| distinctions-vocabulary-F244 | L2-03 (PARTIAL copy) metaphor (release as letting loose). | "I finally decided let this thing loose" | L2-03.txt:19 ¶2 | SUBSTRATE L2-03 | NONE | VERIFIED | PRESERVE: vocabulary |

#### L2-04 Koçulu, "I've Just Liberated My Modules" (2016)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F245 | L2-04 metaphor (private land). First statement. | "NPM is someone’s private land where corporate is more powerful than the people" | L2-04.txt:12 ¶3 | SUBSTRATE L2-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F246 | L2-04 private land, extension: the lawyer's threat as quoted. | "our lawyers gonna be banging on your door, and taking down your accounts" | L2-04.txt:8 ¶1 | SUBSTRATE L2-04 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F247 | L2-04 private land, extension: lawyer power in every e-mail. | "emphasizing their lawyer power in every single e-mail CC’ing me" | L2-04.txt:10 ¶2 | SUBSTRATE L2-04 | NONE | VERIFIED | CUT: repetition |

#### L2-05 Cox, "Our Software Dependency Problem" (2019)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F248 | L2-05 metaphor (hiring a stranger). First statement. | "You would not hire a software developer you’ve never heard of and know nothing about." | L2-05.txt:59 ¶23 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F249 | L2-05 hiring, extension: references, interview, background checks. | "check references, conduct a job interview, run background checks, and so on" | L2-05.txt:59 ¶23 | SUBSTRATE L2-05 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F250 | L2-05 metaphor (outsourcing to a stranger). First statement. | "Adding a package as a dependency outsources the work of developing that code" | L2-05.txt:39 ¶13 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F251 | L2-05 outsourcing, extension: a stranger on the internet. | "Your program’s execution now literally depends on code downloaded from this stranger on the internet." | L2-05.txt:39 ¶13 | SUBSTRATE L2-05 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F252 | L2-05 metaphor (risk multiplied by zero). | "So the risk probability almost doesn’t matter: it’s being multiplied by zero." | L2-05.txt:53 ¶20 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F253 | L2-05 metaphor (tending). | "you’re not done tending your dependencies" | L2-05.txt:163 ¶75 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F254 | L2-05 metaphor (red flag). First statement. | "should raise an initial red flag" | L2-05.txt:75 ¶31 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F255 | L2-05 red flag, extension. | "that’s a serious red flag" | L2-05.txt:79 ¶33 | SUBSTRATE L2-05 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F256 | L2-05 metaphor (Lamport's observation on distributed systems, adapted). The text names the source, not the observation. | "the failure of a package you didn’t even know existed can render your own code unusable" | L2-05.txt:113 ¶50 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |

### Q4. Which sentences under 15 words state a hinge whole? Quote verbatim with location and word count.

Method: every sentence of every text was split by script and counted; the rows below are the ones that state a hinge whole. Under 15 words means 14 or fewer. A row marked "clause" quotes the part of a longer sentence that states the hinge; its parent sentence length is given. Hinge sentences exist in every text except L2-04 (clause only).

#### L1-01 Hertzfeld, "-2000 Lines Of Code" (1982)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F260 | (12 words; sentence) Lines saved, stated whole. The only sentence of L1-01 under 15 words that carries the hinge; the text has no other. | "As a by-product, the rewrite also saved around 2,000 lines of code." | L1-01.txt:12 ¶3 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: aphorism |

#### L1-02 Dijkstra, EWD 1036 (1988)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F261 | (14 words; sentence) Planning in yesterday's vocabulary (analogy as method). | "The usual way in which we plan today for tomorrow is in yesterday's vocabulary." | L1-02.txt:10 ¶2 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F262 | (8 words; sentence) The orthogonal method for radical novelty. | "Coping with radical novelty requires an orthogonal method." | L1-02.txt:14 ¶4 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F263 | (13 words; sentence) Shallow analogy as medieval. | "Again, the shallowness of the underlying analogy is worthy of the Middle Ages." | L1-02.txt:58 ¶26 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F264 | (7 words; sentence) The maintenance metaphor, posed as a question. | "Your car needs maintenance too, doesn't it?" | L1-02.txt:56 ¶25 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F265 | (13 words; sentence) Operational reasoning as waste. | "This is bad, because operational reasoning is a tremendous waste of mental effort." | L1-02.txt:108 ¶51 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F266 | (12 words; sentence) The programmer's task as proof. | "The programmer's task is to present such complete conjectures as proven theorems." | L1-02.txt:132 ¶63 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F267 | (10 words; sentence) Program as formula. | "It really helps to view a program as a formula." | L1-02.txt:70 ¶32 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F268 | (11 words; sentence) The name "software engineering" as suspect. | "The popularity of its name is enough to make it suspect." | L1-02.txt:48 ¶21 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F269 | (12 words; clause; parent sentence 44 words) Lines spent, not produced. | "we should not regard them as "lines produced" but as "lines spent"" | L1-02.txt:52 ¶23 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F270 | (9 words; clause; parent sentence 22 words) A program as half a conjecture. | "a program is no more than half a conjecture" | L1-02.txt:132 ¶63 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F271 | (6 words; clause; parent sentence 17 words) Alternatives may be better. Clause after a colon inside a parenthesized sentence. | "alternatives are allowed to be better." | L1-02.txt:74 ¶34 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: aphorism |

#### L1-03 Cunningham, WyCash Portfolio Management System (1992)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F272 | (9 words; sentence) Debt. | "Shipping first time code is like going into debt." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F273 | (9 words; sentence) Unrepaid debt as the danger. | "The danger occurs when the debt is not repaid." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F274 | (12 words; sentence) Interest on not-quite-right code. | "Every minute spent on not-quite-right code counts as interest on that debt." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F275 | (8 words; sentence) Objects lower the cost of repayment. | "Objects make the cost of this transaction tolerable." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F276 | (9 words; sentence) Failure to consolidate as the serious pitfall. | "Another, more serious pitfall is the failure to consolidate." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F277 | (11 words; sentence) Incremental growth from a working prototype. | "We developed the product by incremental growth from a working prototype." | L1-03.txt:12 ¶3 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F278 | (14 words; sentence) Familiarity as antidote. | "Here the best antidote is more complete familiarity with the product and its implementation." | L1-03.txt:14 ¶4 | SUBSTRATE L1-03 | NONE | VERIFIED | CUT: caveat |

#### L1-04 Skrenta, "Code is our enemy" (2007; PARTIAL copy: Atwood's quotation only)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F279 | (3 words; sentence) PARTIAL copy. Code is bad. | "Code is bad." | L1-04.txt:8 ¶1 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F280 | (5 words; sentence) PARTIAL copy. Code is produced by engineers. | "Code is produced by engineers." | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: principle |
| distinctions-vocabulary-F281 | (7 words; sentence) PARTIAL copy. More code, more engineers. | "To make more code requires more engineers." | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F282 | (10 words; sentence) PARTIAL copy. Less code for the same thing. | "Less code to do the same thing (and possibly better)." | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: principle |
| distinctions-vocabulary-F283 | (14 words; sentence) PARTIAL copy. More code, more places for bugs. | "The more code you have, the more places there are for bugs to hide." | L1-04.txt:8 ¶1 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: aphorism |

#### L1-05 Atwood, "The Best Code is No Code At All" (2007)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F284 | (4 words; sentence) Code is not the enemy. | "Code isn’t our enemy." | L1-05.txt:14 ¶4 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F285 | (12 words; two sentences) The enemy in the mirror (two sentences). | "You want to see the real enemy? Go look in the mirror." | L1-05.txt:14 ¶4 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F286 | (10 words; sentence) The programmer as worst enemy. | "As a software developer, you are your own worst enemy." | L1-05.txt:16 ¶5 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F287 | (3 words; sentence) Start with brevity (follows a colon inside Shipley's quoted block). | "Start with brevity." | L1-05.txt:33 ¶11 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F288 | (11 words; sentence) Dimensions in opposition (Shipley, quoted). | "Now, remember, these dimensions are all in opposition to one another." | L1-05.txt:31 ¶10 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F289 | (8 words; title) Best code is no code at all. Title line of the saved copy. | "The Best Code is No Code At All" | L1-05.txt:2 (header line) | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F290 | (8 words; clause; parent sentence 24 words) Best code is no code at all, as a clause of a longer sentence. | "the best code is no code at all" | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F291 | (12 words; clause; parent sentence 23 words) Love code enough to write little (the closing clause). | "you’ll love it enough to write as little of it as possible" | L1-05.txt:44 ¶16 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: moral core |

#### L1-06 Lee, "Source Code Is A Liability, Not An Asset" (2009)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F292 | (8 words; sentence) Liability, not asset (quoted slogan). | "“Source code is a liability, not an asset!”" | L1-06.txt:12 ¶3 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F293 | (7 words; sentence) Source code as financial debt. | "Source code is akin to financial debt." | L1-06.txt:20 ¶7 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F294 | (12 words; sentence) Source code as necessary evil. | "Source code is merely the necessary evil that’s required to create value." | L1-06.txt:18 ¶6 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F295 | (12 words; sentence) More code, larger ongoing costs. | "The more code you have, the larger those ongoing costs will be." | L1-06.txt:24 ¶9 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F296 | (11 words; sentence) Writing code as the means to value. | "Writing code is the means we use to realize that value." | L1-06.txt:24 ¶9 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F297 | (8 words; sentence) Delete. | "Bust out your delete key and start whacking." | L1-06.txt:36 ¶15 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: principle |
| distinctions-vocabulary-F298 | (10 words; sentence) Interest on debt every month. | "You have to pay interest on your debt every month." | L1-06.txt:20 ¶7 | SUBSTRATE L1-06 | NONE | VERIFIED | CUT: repetition |
| distinctions-vocabulary-F299 | (11 words; sentence) The question of what was done with the LOC. | "The question is entirely, “What did you do with that LOC/debt?”" | L1-06.txt:26 ¶10 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F300 | (11 words; sentence) Source code is not a valuable commodity. | "With few exceptions, source code itself is not a valuable commodity." | L1-06.txt:18 ¶6 | SUBSTRATE L1-06 | NONE | VERIFIED | CUT: hedge |
| distinctions-vocabulary-F301 | (14 words; sentence) Get above water. Closing call. | "Nonetheless, it’s absolutely critical that you get yourself above water as soon as possible." | L1-06.txt:36 ¶15 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: principle |

#### L2-01 McIlroy, "Mass Produced Software Components" (1968)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F302 | (7 words; sentence) Software produced by backward techniques. | "We undoubtedly produce software by backward techniques." | L2-01.txt:16 ¶5 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F303 | (6 words; sentence) Begin thinking small. | "We have to begin thinking small." | L2-01.txt:91 ¶39 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: principle |
| distinctions-vocabulary-F304 | (9 words; sentence) Systems first; components annoying incidentals. | "The system comes first; components are merely annoying incidentals." | L2-01.txt:125 ¶56 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F305 | (11 words; sentence) No standardizing into existence. | "I don’t think a components industry can be standardized into existence." | L2-01.txt:149 ¶68 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F306 | (13 words; sentence) Components as black boxes. | "In short, he should be able safely to regard components as black boxes." | L2-01.txt:26 ¶10 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F307 | (13 words; sentence) Components as a dignified branch of software engineering. | "I would like to see components become a dignified branch of software engineering." | L2-01.txt:153 ¶70 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F308 | (14 words; sentence) Components unknown as a legitimate branch of software. | "Components, dignified as a hardware field, is unknown as a legitimate branch of software." | L2-01.txt:20 ¶7 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F309 | (11 words; sentence) Producing family members is not enough. | "The ability to produce members of a family is not enough." | L2-01.txt:137 ¶62 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F310 | (6 words; title) Section heading: the software industry is not industrialized. | "The Software Industry is Not Industrialized." | L2-01.txt:14 ¶4 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: aphorism |

#### L2-02 Ritchie and Thompson, "The UNIX Time-Sharing System" (1974)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F311 | (8 words; sentence) The system imposes no file structure. | "No particular structuring is expected by the system." | L2-02.txt:44 ¶18 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: principle |
| distinctions-vocabulary-F312 | (12 words; sentence) Special files as the most unusual feature. | "Special files constitute the most unusual feature of the UNIX file system." | L2-02.txt:64 ¶28 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F313 | (14 words; sentence) The process does not know the channel is a pipe. | "Neither process need know that a pipe, rather than an ordinary file, is involved." | L2-02.txt:183 ¶83 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F314 | (14 words; sentence) Filters as redirection extended. | "Filters are straightforward extensions of standard I/O redirection with pipes used instead of files." | L2-02.txt:311 ¶145 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F315 | (12 words; sentence) The file system as the most important job. | "The most important job of UNIX is to provide a file system." | L2-02.txt:40 ¶16 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F316 | (14 words; sentence) System size grew one third (the next sentence calls it acceptable). | "The size of the new system is about one third greater than the old." | L2-02.txt:36 ¶14 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F317 | (14 words; sentence) The system maintained itself. | "Third, nearly from the start, the system was able to, and did, maintain itself." | L2-02.txt:355 ¶167 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F318 | (10 words; sentence) Self-supporting. | "It is worth noting that the system is totally self-supporting." | L2-02.txt:28 ¶10 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: aphorism |

#### L2-03 Hietaniemi, CPAN "private showing" (1995; PARTIAL copy: the pre-launch mail, not the launch post)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F319 | (7 words; sentence (no period)) PARTIAL copy. Release by letting loose. | "I finally decided let this thing loose" | L2-03.txt:19 ¶2 | SUBSTRATE L2-03 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F320 | (14 words; sentence) PARTIAL copy. Release meant for the keepers. | "This "release" is mainly meant for the current keepers of the / various Perl archives." | L2-03.txt:23-24 ¶4 | SUBSTRATE L2-03 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F321 | (13 words; sentence) PARTIAL copy. No incoming/ directory. | "I guess I will not be putting up an incoming/ directory to funet." | L2-03.txt:42 ¶6 | SUBSTRATE L2-03 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F322 | (11 words; sentence) PARTIAL copy. Submissions subdivided by the hierarchy. | "That tar very preferably already subdivided according to the CPAN hierarchy." | L2-03.txt:50 ¶6 | SUBSTRATE L2-03 | NONE | VERIFIED | PRESERVE: aphorism |

#### L2-04 Koçulu, "I've Just Liberated My Modules" (2016)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F323 | (6 words; sentence) Not a knee-jerk action. | "This is not a knee-jerk action." | L2-04.txt:16 ¶5 | SUBSTRATE L2-04 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F324 | (13 words; clause; parent sentence 29 words) NPM as private land. | "NPM is someone’s private land where corporate is more powerful than the people" | L2-04.txt:12 ¶3 | SUBSTRATE L2-04 | NONE | VERIFIED | PRESERVE: aphorism |

#### L2-05 Cox, "Our Software Dependency Problem" (2019)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F325 | (9 words; sentence) A little copying against a little dependency (Go proverb, quoted). | "A little copying is better than a little dependency." | L2-05.txt:141 ¶64 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F326 | (11 words; sentence) More code, less justification. | "We are trusting more code with less justification for doing so." | L2-05.txt:47 ¶17 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F327 | (7 words; sentence) Old practice differs in ways ignored. | "But there are important differences we’re ignoring." | L2-05.txt:41 ¶14 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F328 | (7 words; sentence) The dependency model sounds unsafe. | "Presented this way, it sounds incredibly unsafe." | L2-05.txt:39 ¶13 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F329 | (12 words; sentence) Risk multiplied by zero. | "So the risk probability almost doesn’t matter: it’s being multiplied by zero." | L2-05.txt:53 ¶20 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F330 | (5 words; sentence) The old upgrade analysis ignores two costs. | "This analysis ignores two costs." | L2-05.txt:145 ¶66 | SUBSTRATE L2-05 | NONE | VERIFIED | CUT: scaffolding |
| distinctions-vocabulary-F331 | (7 words; sentence) Upgrades not automatic. | "Again, upgrades should not be completely automatic." | L2-05.txt:155 ¶71 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: principle |
| distinctions-vocabulary-F332 | (3 + 5 + 6 words; three sentences) Three numbered recommendations, one sentence each. | "Recognize the problem." ‖ "Establish best practices for today." ‖ "Develop better dependency technology for tomorrow." | L2-05.txt:185 ¶86; L2-05.txt:189 ¶88; L2-05.txt:193 ¶90 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: principle |
| distinctions-vocabulary-F333 | (8 + 11 words; two sentences) Closing pair: much good software; reuse it safely. | "There’s a lot of good software out there." ‖ "Let’s work together to find out how to reuse it safely." | L2-05.txt:195 ¶91 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: moral core |
| distinctions-vocabulary-F334 | (5 words; clause; parent sentence 25 words) The situation is reversed (discussion against actual reuse). | "Today, the situation is reversed" | L2-05.txt:8 ¶1 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: aphorism |
| distinctions-vocabulary-F335 | (14 words; sentence) The decision as "let's see what happens". | "Most of the time the entirety of the decision is “let’s see what happens.”" | L2-05.txt:179 ¶83 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: aphorism |

### Q5. Which terms recur across texts? Quote each use, and mark where the meaning holds and where it shifts.

#### Term: debt

Verdict from the rows below: HOLDS: interest accrues on code left unrepaid (L1-03:16, L1-06:20). SHIFTS: scope (first-time code in L1-03; all source code in L1-06) and benefit (a little debt helps in L1-03; minimize in L1-06).

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F336 | debt, L1-03: first-time code shipped; scope is unrepaid, unconsolidated code. | "Shipping first time code is like going into debt." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F337 | debt, L1-03: a small amount helps. SHIFTS against L1-06 (no benefit stated there). | "A little debt speeds development so long as it is paid back promptly with a rewrite." | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F338 | debt, L1-06: all source code. SHIFTS in scope from L1-03; HOLDS on interest (L1-03:16 "interest", L1-06:20 "pay interest"). | "Source code is akin to financial debt." | L1-06.txt:20 ¶7 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F339 | debt, L1-06: the goal is as little code as the business goals allow. SHIFTS: minimization, where L1-03 allows a little debt. | "It’s in our best interest to have as little source code as possible while still being able to accomplish our business goals." | L1-06.txt:24 ¶9 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F340 | The phrase "technical debt" occurs in neither L1-03 nor L1-06 (grep -ci technical: 0 on both). L1-03 calls it "our debt analogy". | "using our debt analogy" | L1-03.txt:18 ¶6 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: maintenance

Verdict from the rows below: HOLDS: L1-04, L1-06, L2-05 treat maintenance as a cost code carries. SHIFTS: L1-02 rejects the term; L2-02 uses "maintain itself" for self-hosting; L2-05:91 says some code is "done".

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F341 | maintenance, L1-02: the term itself is rejected as misunderstanding. SHIFTS against L1-04, L1-06, L2-05. | "Unfathomed misunderstanding is further revealed by the term "software maintenance"" | L1-02.txt:56 ¶25 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F342 | maintenance, L1-04 (PARTIAL copy): code requires it. | "It requires periodic maintenance." | L1-04.txt:8 ¶1 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F343 | maintenance, L1-06: one of three ongoing duties of code. HOLDS with L1-04. | "you have to maintain it" | L1-06.txt:24 ¶9 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F344 | maintenance, L2-05: a property inspected in a package. HOLDS with L1-04, L1-06. | "How long has the code been actively maintained?" | L2-05.txt:89 ¶38 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F345 | maintain, L2-02: the system is used by its builders. SHIFTS: no wear-and-tear sense. | "the system was able to, and did, maintain itself" | L2-02.txt:355 ¶167 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: analogy

Verdict from the rows below: HOLDS: L1-02, L1-03, L2-01 each name an image as an analogy. SHIFTS in valence: failure mode (L1-02), instrument (L1-03), fragile instrument (L2-01).

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F346 | analogy, L1-02: named as the failure mode for radical novelty. | "by means of metaphors and analogies we try to link the new to the old" | L1-02.txt:12 ¶3 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F347 | analogy, L1-03: the author names his own image an analogy and uses it. SHIFTS in valence from L1-02. | "using our debt analogy" | L1-03.txt:18 ¶6 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F348 | analogy, L2-01: the author names his own image an analogy and calls it fragile. HOLDS with L1-03 (named as an analogy); SHIFTS to hedged. | "Yet this fragile analogy is belied when we seek for analogues of other tangible symbols of mass production." | L2-01.txt:18 ¶6 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: lines of code, volume, size

Verdict from the rows below: HOLDS: L1-01, L1-02, L1-06 reject lines written as a measure. SHIFTS: L1-05 moves to the volume a reader reads; L1-03, L2-02, L2-05 use size as a neutral descriptor.

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F349 | lines of code, L1-01: measure of weekly progress per engineer; rejected. | "a field for the number of lines of code that were written that week" | L1-01.txt:8 ¶1 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F350 | lines of code, L1-02: measure of programmer productivity; rejected as "very costly". | "measuring "programmer productivity" in terms of "number of lines of code produced per month"" | L1-02.txt:52 ¶23 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F351 | LOC, L1-06: never an asset measurement. HOLDS with L1-01, L1-02. | "LOC (lines of code) numbers should never be taken as an asset measurement" | L1-06.txt:26 ¶10 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F352 | volume, L1-05: what a programmer must read. SHIFTS from lines written to lines read. | "reduce the volume of code an individual programmer has to read" | L1-05.txt:35 ¶12 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F353 | size, L1-03: a descriptor, not a target. SHIFTS to neutral. | "the roughly four megabytes of source code" | L1-03.txt:12 ¶3 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F354 | lines, L2-02: a descriptor of the timed program. SHIFTS to neutral. | "timings were made of the assembly of a 7621-line program" | L2-02.txt:157 ¶70 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F355 | lines, L2-05: a descriptor of one distributed file. SHIFTS to neutral. | "a single 200,000-line C source file" | L2-05.txt:75 ¶31 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: productivity

Verdict from the rows below: HOLDS: L1-01, L1-02 reject lines as the measure. SHIFTS: four meanings: lines written (rejected), expressive power (L1-04), removal with function kept (L1-06), a user's ease (L2-02).

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F356 | productivity, L1-01: lines of code called a silly measure of it. | "lines of code was a silly measure of software productivity" | L1-01.txt:10 ¶2 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F357 | productivity, L1-02: lines per month encourages insipid code. HOLDS with L1-01. | "This is a very costly measuring unit because it encourages the writing of insipid code" | L1-02.txt:52 ¶23 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F358 | productivity, L1-04 (PARTIAL copy): redefined as expressive power. SHIFTS. | "increase the productivity of individual programmers in terms of the expressive power of the code they write" | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F359 | productive, L1-06: removal of LOC with function preserved. SHIFTS to deletion. | "one of the most productive statements a team can make is, “This week we removed 10K LOC while preserving all existing functionality!”" | L1-06.txt:28 ¶11 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F360 | productive, L2-02: said of a system's user, not of its programmers. SHIFTS. | "a properly designed interactive system is much more productive and satisfying to use than a “batch” system" | L2-02.txt:351 ¶165 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: rewrite

Verdict from the rows below: HOLDS: rewrite as repair in four texts. SHIFTS: size direction (-2,000 lines in L1-01; one third more in L2-02) and cause (speed, debt, language, dependencies).

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F361 | rewrite, L1-01: a rewrite shrinks code and speeds it up. | "had completely rewritten the region engine using a simpler, more general algorithm" | L1-01.txt:12 ¶3 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F362 | rewrite, L1-03: the act that repays debt. HOLDS: rewrite as repair. | "paid back promptly with a rewrite" | L1-03.txt:16 ¶5 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F363 | rewritten, L2-02: a language change; the code grew. SHIFTS in size direction from L1-01. | "during the summer of 1973, it was rewritten in C" | L2-02.txt:36 ¶14 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F364 | rewrote, L2-05: a rewrite that removes dependencies. HOLDS: rewrite as repair; SHIFTS in cause. | "Later we rewrote the execution engine as well, so that no dependencies were left" | L2-05.txt:139 ¶63 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: delete, remove, unpublish

Verdict from the rows below: HOLDS: removal of code named as an act. SHIFTS: a virtue with a condition (L1-06), a protest (L2-04), a hazard to dependents (L2-05).

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F365 | delete, L1-06: deletion of one's own code as the remedy. | "Bust out your delete key and start whacking." | L1-06.txt:36 ¶15 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F366 | remove, L1-06: removal carries a condition. | "while preserving all existing functionality" | L1-06.txt:28 ¶11 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F367 | unpublish, L2-04: removal of one's modules from a shared registry. SHIFTS from L1-06: an act of protest. | "I’ve just unpublished all my modules" | L2-04.txt:14 ¶4 | SUBSTRATE L2-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F368 | deleted, L2-05: removal from a registry broke dependents. SHIFTS from L1-06: deletion as hazard. | "the author of left-pad deleted that package from NPM, inadvertently breaking most Node.js users’ builds" | L2-05.txt:113 ¶50 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: engineer, software engineering

Verdict from the rows below: HOLDS: the human who produces code. SHIFTS: tracked person (L1-01), aspiration (L2-01), doomed name (L1-02), cost multiplier (L1-04), specialist role (L2-05).

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F369 | engineer, L1-01: the tracked person. | "to track the progress of each individual engineer in terms of the amount of code that they wrote from week to week" | L1-01.txt:8 ¶1 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F370 | software engineering, L2-01 (1968): an aspiration. SHIFTS against L1-02 (1988). | "I would like to see components become a dignified branch of software engineering." | L2-01.txt:153 ¶70 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F371 | software engineering, L1-02 (1988): "The Doomed Discipline". SHIFTS against L2-01. | "software engineering should be known as "The Doomed Discipline"" | L1-02.txt:46 ¶20 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F372 | engineers, L1-04 (PARTIAL copy): the producers of code and a cost multiplier. | "Code is produced by engineers." | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F373 | engineers, L2-05: a specialist role proposed. | "we need engineers who specialize in managing dependencies" | L2-05.txt:189 ¶88 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: unit of reuse: component, library, module, package

Verdict from the rows below: HOLDS: a unit of code written outside the author's hands. SHIFTS: the name (component, library, module, package) and the channel (catalogue, vendor, licence, registry).

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F374 | component, L2-01: the unit, bought from a catalogue. | "Software components (routines)" | L2-01.txt:12 ¶3 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F375 | libraries, L1-03: units from a vendor or contractors. | "This includes some libraries provided by the vendor and others written to our specification by third-party contractors." | L1-03.txt:12 ¶3 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F376 | third-party software package, L1-06: units bought by licence. | "to license a third-party software package that does the same thing" | L1-06.txt:32 ¶13 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F377 | module, L2-04: units published to a registry. | "asking me to unpublish “kik” module from NPM" | L2-04.txt:8 ¶1 | SUBSTRATE L2-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F378 | package, L2-05: Cox equates package, library, module. HOLDS: a unit of outside code; SHIFTS: names and acquisition channel. | "some systems use terms like library or module instead of package" | L2-05.txt:16 ¶5 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: modularity

Verdict from the rows below: HOLDS: modularity as the property that permits change. SHIFTS: interchange for purchase (L2-01) against absorbing revision inside one team's code (L1-03).

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F379 | modularity, L2-01: interchangeable parts, "fitfully respected". | "The idea of interchangeable parts corresponds roughly to our term ‘modularity,’ and is fitfully respected." | L2-01.txt:18 ¶6 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F380 | modularity, L1-03: what lets revisions be absorbed. SHIFTS from interchange to revision. | "the modularity intrinsic in a totally object-oriented implementation" | L1-03.txt:10 ¶2 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: cost

Verdict from the rows below: HOLDS: cost scales with the amount of code or the number of units. SHIFTS: who pays: the owner (L1-04, L1-06), the adopter (L2-05), the supplier (L2-01).

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F381 | costs, L1-04 (PARTIAL copy): borne by the code's owners as code grows. | "also increases a whole basket of costs" | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F382 | costs, L1-06: ongoing, growing with code. HOLDS with L1-04. | "code has ongoing costs" | L1-06.txt:24 ¶9 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F383 | costs, L2-05: fixed costs of reuse. SHIFTS: the adopter pays. | "the high fixed costs of reuse" | L2-05.txt:18 ¶6 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F384 | cost, L2-01: the supplier's cost of an inventory. SHIFTS: the producer pays. | "the cost of offering such an ‘inventory’ need not be nearly 300 times the cost of keeping one routine" | L2-01.txt:50 ¶20 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: bug, error

Verdict from the rows below: HOLDS: "bug" is the defect word in L1-04 and L2-05. SHIFTS: L1-02 proposes "error"; no lane-2 text adopts it.

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F385 | bug, L1-02: replaced by "error". | "no longer calling a bug a bug but by calling it an error" | L1-02.txt:102 ¶48 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F386 | bug, L1-04 (PARTIAL copy): kept, no comment. SHIFTS against L1-02. | "It has bugs that need to be found." | L1-04.txt:8 ¶1 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F387 | bug, L2-05: "bug"/"bugs" on 14 lines (grep -c -w -i); "error" on 2 lines, neither meaning a defect in general ("error-prone" L2-05:67, "compile-time error" L2-05:169). SHIFTS against L1-02. | "Are there many open bug reports?" | L2-05.txt:85 ¶36 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: understanding

Verdict from the rows below: HOLDS: understanding as the cost that grows with code (L1-03, L1-04, L1-05, L1-06). SHIFTS: in L2-02 it outweighs size.

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F388 | understanding, L1-03: every engineer holds general knowledge of all the code. | "Each member of our small engineering team maintains at least general knowledge of all aspects of the roughly four megabytes of source code." | L1-03.txt:12 ¶3 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F389 | understanding, L1-04 (PARTIAL copy): time for a new employee to make sense of the system. | "The longer it takes a new employee to make sense of your system." | L1-04.txt:8 ¶1 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F390 | understanding, L1-05: code must be read and understood. | "code that has to be read and understood" | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F391 | understanding, L1-06: the first ongoing duty. HOLDS with L1-03, L1-04, L1-05. | "You have to understand it" | L1-06.txt:24 ¶9 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F392 | understanding, L2-02: an argument for accepting more size. HOLDS: comprehension as the criterion; SHIFTS: it outweighs size. | "not only much easier to understand and to modify" | L2-02.txt:36 ¶14 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: enemy

Verdict from the rows below: HOLDS: none across texts; the word occurs in L1-05 only, with L1-04 carrying it in its header title.

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F393 | "enemy" occurs on 4 lines of L1-05 and in no other text body (grep -wi enemy: L1-05 only; L1-04 carries it in its header title only). | "Rich Skrenta writes that code is our enemy." | L1-05.txt:8 ¶1 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: small, simple, brevity

Verdict from the rows below: HOLDS: smallness as a good (L1-01, L1-05, L2-01, L2-02). SHIFTS in referent: program size and speed, reading volume, first product scope, system size under constraint.

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F394 | small, L1-01: the engineer's goal. HOLDS: smallness as a good. | "write as small and fast a program as possible" | L1-01.txt:10 ¶2 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F395 | brevity, L1-05: the first dimension. SHIFTS: reading volume. | "Start with brevity." | L1-05.txt:33 ¶11 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F396 | small, L2-01: the scope of the first components. SHIFTS: product scope, not code volume. | "We have to begin thinking small." | L2-01.txt:91 ¶39 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F397 | simplicity, L2-02: named as a most important characteristic. | "the most important characteristics of the system are its simplicity, elegance, and ease of use" | L2-02.txt:24 ¶8 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F398 | small, L2-02: a small yet powerful operating system. SHIFTS: system size under constraint. | "a small yet powerful operating system" | L2-02.txt:367 ¶173 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: reuse

Verdict from the rows below: HOLDS in sense across L1-06, L2-01, L2-05. The word "reuse" names the practice in L2-05 only.

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F399 | "reuse" as the name of the practice occurs in L2-05 (10 lines) and nowhere else in the eleven texts; L2-02:147 has one unrelated use ("workspace may be reused"). | "Today, the situation is reversed: developers reuse software written by others every day" | L2-05.txt:8 ¶1 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F400 | L2-01 names the same practice "off the shelf". HOLDS in sense; the word differs. | "start taking such things off the shelf" | L2-01.txt:20 ¶7 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F401 | L1-06 names it "third-party library" and "licence". HOLDS in sense; the word differs. | "whether to use a third-party library or write your own implementation" | L1-06.txt:30 ¶12 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: tools

Verdict from the rows below: SHIFTS in valence: snake oil (L1-02) against a remedy (L2-05).

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F402 | tools, L1-02: the "programming tools" remedy called snake oil. | "the pains of software production are largely due to a lack of appropriate "programming tools"" | L1-02.txt:58 ¶26 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F403 | tooling, L2-05: better tooling called likely needed. SHIFTS in valence against L1-02. | "It is likely that better tooling is needed to help reduce the costs of these approaches" | L2-05.txt:55 ¶21 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: vocabulary |

#### Term: waste

Verdict from the rows below: SHIFTS in referent: mental effort (L1-02) against software writing (L2-01).

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F404 | waste, L1-02: of mental effort. | "a tremendous waste of mental effort" | L1-02.txt:108 ¶51 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F405 | waste, L2-01: of software writing. SHIFTS in referent from L1-02. | "the tragic waste of current software writing techniques" | L2-01.txt:105 ¶46 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: vocabulary |

### Q6. Which distinctions cross the lane boundary — a pole in one lane that answers a pole in the other? Quote both.

Note: a pair marks opposed or answering poles; it does not mark a citation. grep over the eleven bodies for author names finds citations only inside lanes: L1-05:8 names Skrenta (author of L1-04); L2-02:448 thanks M.D. McIlroy (author of L2-01); L2-05:203 lists Ken Thompson, co-author of L2-02, for another paper. No text names an author of the other lane. Years are the texts' own (index).

#### Pair 1: delete as virtue / delete as hazard

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F406 | PAIR 1 (delete as virtue / delete as hazard). Pole in lane 1 (L1-06, 2009). | "Bust out your delete key and start whacking." | L1-06.txt:36 ¶15 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F407 | PAIR 1, condition on the lane-1 pole. | "while preserving all existing functionality" | L1-06.txt:28 ¶11 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F408 | PAIR 1, answering pole in lane 2 (L2-05, 2019): deletion broke dependents. | "the author of left-pad deleted that package from NPM, inadvertently breaking most Node.js users’ builds" | L2-05.txt:113 ¶50 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |

#### Pair 2: code from outside: buy, avoid, copy

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F409 | PAIR 2 (code from outside: buy / avoid). Pole in lane 1 (L1-06, an aside): a licence fee is cheaper than months of an employee. | "in order to avoid paying $1000 or even $500 to license a third-party software package that does the same thing" | L1-06.txt:32 ¶13 | SUBSTRATE L1-06 | NONE | VERIFIED | CUT: aside |
| distinctions-vocabulary-F410 | PAIR 2, pole in lane 2 (L2-05): free downloads displaced purchases. | "has displaced many of those earlier software purchases" | L2-05.txt:45 ¶16 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F411 | PAIR 2, pole in lane 2 (L2-05): avoid the dependency. | "the best answer may be to avoid it entirely" | L2-05.txt:137 ¶62 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F412 | PAIR 2, pole in lane 2 (L2-05, a Go proverb): copy rather than depend. | "A little copying is better than a little dependency." | L2-05.txt:141 ¶64 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |

#### Pair 3: software as industrial product / programs not like other devices

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F413 | PAIR 3 (software as industrial product / software as no ordinary device). Pole in lane 2 (L2-01, 1968). | "What I have just asked for is simply industrialism" | L2-01.txt:155 ¶71 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F414 | PAIR 3, answering pole in lane 1 (L1-02, 1988). | "programs are just devices like any others" | L1-02.txt:52 ¶23 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |

#### Pair 4: software engineering: dignified / doomed

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F415 | PAIR 4 (software engineering as aspiration / as doomed). Pole in lane 2 (L2-01, 1968). | "I would like to see components become a dignified branch of software engineering." | L2-01.txt:153 ¶70 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F416 | PAIR 4, answering pole in lane 1 (L1-02, 1988). | "software engineering should be known as "The Doomed Discipline"" | L1-02.txt:46 ¶20 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |

#### Pair 5: the same cost list in both lanes

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F417 | PAIR 5 (the same cost list in both lanes). Lane 1 (L1-05): the cost of a new line; the text's answer is no code. | "code that has to be debugged, code that has to be read and understood, code that has to be supported" | L1-05.txt:42 ¶15 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F418 | PAIR 5, lane 2 (L2-05): the same work named as what a dependency avoids; the text then names the risks of that choice. | "avoids repeating work already done: designing, writing, testing, debugging, and maintaining a specific unit of code" | L2-05.txt:16 ¶5 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F419 | PAIR 5, lane 1 (L1-06): the same list again: understand, maintain, adapt. | "You have to understand it, you have to maintain it, you have to adapt it to new goals over time." | L1-06.txt:24 ¶9 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: distinction |

#### Pair 6: size against understandability

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F420 | PAIR 6 (size against understandability). Pole in lane 2 (L2-02, 1974): size accepted for ease of understanding. | "not only much easier to understand and to modify" ‖ "we considered this increase in size quite acceptable" | L2-02.txt:36 ¶14 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F421 | PAIR 6, answering pole in lane 1 (L1-06, 2009): verbose accepted for maintainability. | "well-written, maintainable code is often more verbose than dense, impenetrable code, but you should always favor maintainability" | L1-06.txt:30 ¶12 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: distinction |

#### Pair 7: a rewrite and the size of the result

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F422 | PAIR 7 (a rewrite and the size of the result). Lane 1 (L1-01, 1982): the rewrite removes 2,000 lines. | "the rewrite also saved around 2,000 lines of code" | L1-01.txt:12 ¶3 | SUBSTRATE L1-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F423 | PAIR 7, lane 2 (L2-02, 1974): the rewrite adds one third. | "The size of the new system is about one third greater than the old." | L2-02.txt:36 ¶14 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |

#### Pair 8: growth from a small working start

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F424 | PAIR 8 (growth from a small working start). Lane 1 (L1-03, 1992). | "We developed the product by incremental growth from a working prototype." | L1-03.txt:12 ¶3 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F425 | PAIR 8, lane 2 (L2-02, 1974): the account of UNIX's own start. | "This essentially personal effort was sufficiently successful to gain the interest of the remaining author and others" | L2-02.txt:347 ¶163 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F426 | PAIR 8, lane 2 (L2-01, 1968): begin thinking small. | "We have to begin thinking small." | L2-01.txt:91 ¶39 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |

#### Pair 9: modularity, interchange, substitution

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F427 | PAIR 9 (modularity, interchange, substitution). Lane 1 (L1-03, 1992): modularity absorbs revisions. | "we have been able to accomodate because of the modularity intrinsic in a totally object-oriented implementation" | L1-03.txt:10 ¶2 | SUBSTRATE L1-03 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F428 | PAIR 9, lane 2 (L2-01, 1968): interchangeable parts. | "The idea of interchangeable parts corresponds roughly to our term ‘modularity,’ and is fitfully respected." | L2-01.txt:18 ¶6 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F429 | PAIR 9, lane 2 (L2-05, 2019): substitute behind a wrapper. | "Ideally, that allows you to substitute a different, equally appropriate dependency later, by changing only the wrapper." | L2-05.txt:125 ¶56 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |

#### Pair 10: code booked as cost: ledger / expected cost

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F430 | PAIR 10 (code booked as cost: ledger / expected cost). Lane 1 (L1-02, 1988). | "book that count on the wrong side of the ledger" | L1-02.txt:52 ¶23 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F431 | PAIR 10, lane 1 (L1-06, 2009). | "LOC (lines of code) numbers should never be taken as an asset measurement" | L1-06.txt:26 ¶10 | SUBSTRATE L1-06 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F432 | PAIR 10, lane 2 (L2-05, 2019): the cost of a dependency as expected cost. | "the sum, over all possible bad outcomes, of the cost of each bad outcome multiplied by its probability of happening (risk)" | L2-05.txt:49 ¶18 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |

#### Pair 11: who is the culprit

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F433 | PAIR 11 (who is the culprit). Lane 1 (L1-05): the programmer, not the code. | "You want to see the real enemy? Go look in the mirror." | L1-05.txt:14 ¶4 | SUBSTRATE L1-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F434 | PAIR 11, lane 2 (L2-05): the reasons developers take dependencies. | "We do this because it’s easy, because it seems to work, because everyone else is doing it too" | L2-05.txt:41 ¶14 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F435 | PAIR 11, lane 2 (L2-05): the decision procedure in practice. | "Most of the time the entirety of the decision is “let’s see what happens.”" | L2-05.txt:179 ¶83 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |

#### Pair 12: code needs maintenance / code can be done

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F436 | PAIR 12 (code needs maintenance / code can be done). Lane 1 (L1-04, PARTIAL copy). | "It requires periodic maintenance." | L1-04.txt:8 ¶1 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F437 | PAIR 12, answering pole in lane 2 (L2-05). | "some code really is “done.”" | L2-05.txt:91 ¶39 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F438 | PAIR 12, lane 2 (L2-05): the example given. | "may never need to be modified again" | L2-05.txt:91 ¶39 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |

#### Pair 13: a blank mind / selected, borrowed ideas

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F439 | PAIR 13 (a blank mind against selected, borrowed ideas). Lane 1 (L1-02, 1988). | "One must consider one's own past, the experiences collected, and the habits formed in it as an unfortunate accident of history" | L1-02.txt:14 ¶4 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F440 | PAIR 13, lane 2 (L2-02, 1974): success from selected ideas. | "not so much in new inventions but rather in the full exploitation of a carefully selected set of fertile ideas" | L2-02.txt:367 ¶173 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F441 | PAIR 13, lane 2 (L2-02, 1974): named influences. | "On a number of points we were influenced by Multics" | L2-02.txt:369 ¶174 | SUBSTRATE L2-02 | NONE | VERIFIED | PRESERVE: distinction |

#### Pair 14: headcount as the cost

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F442 | PAIR 14 (headcount as the cost). Lane 1 (L1-04, PARTIAL copy). | "Less programmers to hire." | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F443 | PAIR 14, lane 2 (L2-01): the staff of a components plant works on generators. | "Much of the work will be in creating generators of routines rather than in making the routines themselves." | L2-01.txt:139 ¶63 | SUBSTRATE L2-01 | NONE | VERIFIED | PRESERVE: distinction |

#### Pair 15: tools: snake oil / remedy

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F444 | PAIR 15 (tools as snake oil / tooling as remedy). Lane 1 (L1-02, 1988). | "yet another dimension of the snake oil business" | L1-02.txt:58 ¶26 | SUBSTRATE L1-02 | NONE | VERIFIED | PRESERVE: distinction |
| distinctions-vocabulary-F445 | PAIR 15, lane 2 (L2-05, 2019). | "It is likely that better tooling is needed to help reduce the costs of these approaches" | L2-05.txt:55 ¶21 | SUBSTRATE L2-05 | NONE | VERIFIED | PRESERVE: distinction |

### Q7. Which terms depend on a period technology, product, or event that a reader five years out would need explained? Quote and name the dependency.

Note: the dependency is named from the text itself (a product, event, term, or date the text states or leaves unglossed). Whether a reader five years out would need it explained is an inference about HUMAN readers; no measurement found. No MODEL claim.

#### L1-01 Hertzfeld, "-2000 Lines Of Code" (1982)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F446 | Product "Lisa", year 1982; the text names no maker or gloss. | "In early 1982, the Lisa software team was trying to buckle down" | L1-01.txt:8 ¶1 | SUBSTRATE L1-01 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F447 | Library "Quickdraw" and its region engine; unglossed. | "Bill Atkinson, the author of Quickdraw and the main user interface designer" | L1-01.txt:10 ¶2 | SUBSTRATE L1-01 | HUMAN | VERIFIED | CUT: example |

#### L1-02 Dijkstra, EWD 1036 (1988)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F448 | Period term "automatic computers" for computers; unglossed. | "automatic computers represent a radical novelty" | L1-02.txt:32 ¶13 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F449 | Period sense of "Artificial Intelligence" as mimicking the human mind (1988); the claim about AI depends on that sense. | "Artificial Intelligence as mimicking the human mind prefers to view itself as at the front line" | L1-02.txt:60 ¶27 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F450 | Period term "automatic programming", called a contradiction in terms (1988). | "it reveals "automatic programming" as a contradiction in terms" | L1-02.txt:72 ¶33 | SUBSTRATE L1-02 | HUMAN | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F451 | Languages PASCAL and FORTRAN as the 1988 pair; an anecdote. | "its PASCAL programs did not last as long as its FORTRAN programs "because PASCAL was not maintained"" | L1-02.txt:56 ¶25 | SUBSTRATE L1-02 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F452 | Mid-century events: the atom bomb and the pill. | "later technological examples are the atom bomb and the pill" | L1-02.txt:30 ¶12 | SUBSTRATE L1-02 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F453 | An unnamed 1980s US computer manufacturer that relabelled its programmers. | "one of the US computer manufacturers proved a few years ago when it hired, one night, hundreds of new "software engineers"" | L1-02.txt:50 ¶22 | SUBSTRATE L1-02 | HUMAN | VERIFIED | CUT: example |

#### L1-03 Cunningham, WyCash Portfolio Management System (1992)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F454 | Method name "waterfall development cycle" (1992); the sentence itself is the only gloss. | "The traditional waterfall development cycle has endeavored to avoid programming catastrophy by working out a program in detail before programming begins." | L1-03.txt:18 ¶6 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F455 | Language "Smalltalk" (1992). | "directly supported by our language (Smalltalk)" | L1-03.txt:10 ¶2 | SUBSTRATE L1-03 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F456 | Choice of "object technology" as the 1992 decision. | "Wyatt Software chose to employ object technology" | L1-03.txt:10 ¶2 | SUBSTRATE L1-03 | HUMAN | VERIFIED | PRESERVE: vocabulary |

#### L1-04 Skrenta, "Code is our enemy" (2007; PARTIAL copy: Atwood's quotation only)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F457 | PARTIAL copy. "Checkouts" (version-control era) unglossed. | "The longer checkouts or compiles take." | L1-04.txt:8 ¶1 | SUBSTRATE L1-04 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F458 | PARTIAL copy. Premise: engineers produce code; costs follow in hires and communication. | "Code is produced by engineers." ‖ "Less programmers to hire." | L1-04.txt:10 ¶2 | SUBSTRATE L1-04 | HUMAN | VERIFIED | PRESERVE: principle |

#### L1-05 Atwood, "The Best Code is No Code At All" (2007)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F459 | Token "String.Empty", a library constant; the text names no language. | "if (s == String.Empty)" | L1-05.txt:37 ¶13 | SUBSTRATE L1-05 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F460 | Person "Wil Shipley" quoted; no citation or gloss in the text. | "But Wil Shipley argues that we should rein in our natural tendencies to write lots of code" | L1-05.txt:18 ¶6 | SUBSTRATE L1-05 | HUMAN | VERIFIED | CUT: example |

#### L1-06 Lee, "Source Code Is A Liability, Not An Asset" (2009)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F461 | An unnamed recent news event about mortgages; page date 2009-03-11 (index). The text supplies no name for the event. | "as we’ve seen in the news recently" ‖ "you can wind up in a load of trouble" | L1-06.txt:22 ¶8 | SUBSTRATE L1-06 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F462 | Platform "MSDN blog" unglossed. | "(I originally posted this on my MSDN blog.)" | L1-06.txt:8 ¶1 | SUBSTRATE L1-06 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F463 | Dollar amounts of 2009; a self-labelled aside. | "at a true cost of at least $10,000 a month" | L1-06.txt:32 ¶13 | SUBSTRATE L1-06 | HUMAN | VERIFIED | CUT: aside |

#### L2-01 McIlroy, "Mass Produced Software Components" (1968)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F464 | Product "IBM OS/360 Sysgen" (1968); the paper glosses it as filling in parameters at compile time (L2-01:56). | "The best known of these, IBM’s OS/360 Sysgen is indeed elaborate" | L2-01.txt:56 ¶23 | SUBSTRATE L2-01 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F465 | Publication "the CACM collected algorithms" (1968). | "What about the CACM collected algorithms?" | L2-01.txt:115 ¶51 | SUBSTRATE L2-01 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F466 | Institution and estate: Bell Telephone Laboratories, about 100 machines (1968). | "At Bell Telephone Laboratories we have about 100 general purpose machines from a dozen manufacturers." | L2-01.txt:105 ¶46 | SUBSTRATE L2-01 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F467 | Mail-order catalogue "Sears-Roebuck" as the model of a parts catalogue. | "the Sears-Roebuck catalogue" | L2-01.txt:143 ¶65 | SUBSTRATE L2-01 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F468 | "Distribution by communication link" in its 1968 sense. | "One instantly thinks of distribution by communication link." | L2-01.txt:143 ¶65 | SUBSTRATE L2-01 | HUMAN | VERIFIED | PRESERVE: vocabulary |

#### L2-02 Ritchie and Thompson, "The UNIX Time-Sharing System" (1974)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F469 | Hardware "PDP-11/40 and 11/45" (1974). | "for the Digital Equipment Corporation PDP-11/40 and 11/45 computers" | L2-02.txt:12 ¶2 | SUBSTRATE L2-02 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F470 | Core memory size 144K bytes; UNIX occupies 42K bytes (1974). | "a 16-bit word (8-bit byte) computer with 144K bytes of core memory" | L2-02.txt:32 ¶12 | SUBSTRATE L2-02 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F471 | "Typewriter" for terminal (1974). | "this file is the user’s typewriter" | L2-02.txt:223 ¶103 | SUBSTRATE L2-02 | HUMAN | VERIFIED | PRESERVE: vocabulary |
| distinctions-vocabulary-F472 | Hardware price and the unit "man years" (1974). | "UNIX can run on hardware costing as little as $40,000" ‖ "less than two man years were spent on the main system software" | L2-02.txt:24 ¶8 | SUBSTRATE L2-02 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F473 | Systems "Multics" and "TENEX" named as influences without gloss. | "On a number of points we were influenced by Multics" | L2-02.txt:369 ¶174 | SUBSTRATE L2-02 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F474 | Product "Picturephone" interface among one-of-a-kind devices. | "a Picturephone® interface" | L2-02.txt:34 ¶13 | SUBSTRATE L2-02 | HUMAN | VERIFIED | CUT: example |

#### L2-03 Hietaniemi, CPAN "private showing" (1995; PARTIAL copy: the pre-launch mail, not the launch post)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F475 | FTP archive path as the distribution medium (1995). PARTIAL copy. | "ftp.funet.fi:/pub/languages/perl/CPAN/" | L2-03.txt:21 ¶3 | SUBSTRATE L2-03 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F476 | Archive formats shar, tar, .Z, .gz (1995). PARTIAL copy. | "no shars, make them to be tars" ‖ "no .Z, use .gz" | L2-03.txt:63 ¶10; L2-03.txt:66 ¶10 | SUBSTRATE L2-03 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F477 | FTP "incoming/" upload directory convention. PARTIAL copy. | "I guess I will not be putting up an incoming/ directory to funet." | L2-03.txt:42 ¶6 | SUBSTRATE L2-03 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F478 | "Inet" for the Internet connection (1995). PARTIAL copy. | "will be non-Inet-connectible until the 10th of September" | L2-03.txt:33 ¶5 | SUBSTRATE L2-03 | HUMAN | VERIFIED | PRESERVE: vocabulary |

#### L2-04 Koçulu, "I've Just Liberated My Modules" (2016)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F479 | Registry "NPM" and its "unpublish" operation; the page is dated Mar 23, 2016 (header). The text does not name left-pad (index: 0 occurrences). | "asking me to unpublish “kik” module from NPM" | L2-04.txt:8 ¶1 | SUBSTRATE L2-04 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F480 | Handle "@izs" unglossed. | "@izs accepted to change the ownership of this module, without my permission" | L2-04.txt:10 ¶2 | SUBSTRATE L2-04 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F481 | A "registered brand" claim to "kik" by a company the text calls only "a company with same name". | "but “kik” is our registered brand" | L2-04.txt:8 ¶1 | SUBSTRATE L2-04 | HUMAN | VERIFIED | CUT: example |

#### L2-05 Cox, "Our Software Dependency Problem" (2019)

| F-id | Finding | Quote | Location | Origin | Reader | Status | Lens |
|---|---|---|---|---|---|---|---|
| distinctions-vocabulary-F482 | NPM size of January 2019: over 750,000 packages. | "the Node.js dependency manager NPM provides access to over 750,000 packages" | L2-05.txt:22 ¶8 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F483 | Event of March 2016 ("left-pad"), named without detail beyond one sentence. | "many popular projects—including Babel, Ember, and React—all depended indirectly on a tiny package called left-pad" | L2-05.txt:113 ¶50 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F484 | Event of November 2018 ("event-stream"). | "In November 2018, the latest version of the NPM package event-stream" ‖ "was discovered to contain obfuscated malicious code" | L2-05.txt:133 ¶60 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F485 | Event of 2017 ("Equifax"), recounted from congressional testimony. | "consider the year 2017 at Equifax, as recounted by executives in detailed congressional testimony" | L2-05.txt:147 ¶67 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F486 | Observation of Leslie Lamport named, not stated. | "Adapting Leslie Lamport’s observation about distributed systems" | L2-05.txt:113 ¶50 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: example |
| distinctions-vocabulary-F487 | Tool "gVisor" as the 2019 "today" option. | "Today, another option would be a lightweight hypervisor-based sandbox like gVisor." | L2-05.txt:131 ¶59 | SUBSTRATE L2-05 | HUMAN | VERIFIED | CUT: example |

## Category table

### Terms

| Term | Defining quote | Location | ID | Coined here or borrowed | F-id |
|---|---|---|---|---|---|
| lines of code (written per week) | "a field for the number of lines of code that were written that week" | L1-01.txt:8 ¶1 | L1-01 | unattributed (text silent on origin) | distinctions-vocabulary-F001 |
| lines of code metric | "the lines of code metric only encouraged writing sloppy, bloated, broken code" | L1-01.txt:10 ¶2 | L1-01 | unattributed (text silent on origin) | distinctions-vocabulary-F002 |
| -2000 (lines) | "As a by-product, the rewrite also saved around 2,000 lines of code." ‖ "wrote in the number: -2000" | L1-01.txt:12 ¶3; L1-01.txt:14 ¶4 | L1-01 | unattributed (text silent on origin) | distinctions-vocabulary-F003 |
| radical novelty | "in the case of a sharp discontinuity, however, the method breaks down" ‖ "This is the situation that is characteristic for the "radical" novelty." | L1-02.txt:12 ¶3 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F004 |
| first radical novelty | "The first radical novelty is a direct consequence of the raw power of today's computing equipment." | L1-02.txt:34 ¶14 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F005 |
| second radical novelty | "The second radical novelty is that the automatic computer is our first large-scale digital device." | L1-02.txt:38 ¶16 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F006 |
| orthogonal method | "Coping with radical novelty requires an orthogonal method." | L1-02.txt:14 ¶4 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F007 |
| lines spent | "we should not regard them as "lines produced" but as "lines spent"" | L1-02.txt:52 ¶23 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F008 |
| The Doomed Discipline | "software engineering should be known as "The Doomed Discipline"" | L1-02.txt:46 ¶20 | L1-02 | coined here (text names the act: "should be known as") | distinctions-vocabulary-F009 |
| "How to program if you cannot." | "software engineering has accepted as its charter "How to program if you cannot."" | L1-02.txt:46 ¶20 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F010 |
| software maintenance (rejected term) | "Unfathomed misunderstanding is further revealed by the term "software maintenance"" | L1-02.txt:56 ¶25 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F011 |
| error (for "bug") | "no longer calling a bug a bug but by calling it an error" | L1-02.txt:102 ¶48 | L1-02 | coined here (text names the act: "We could, for instance, begin with cleaning up our language") | distinctions-vocabulary-F012 |
| anthropomorphic terminology | "never refer to parts of programs or pieces of equipment in an anthropomorphic terminology" | L1-02.txt:104 ¶49 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F013 |
| operational reasoning | "This is bad, because operational reasoning is a tremendous waste of mental effort." | L1-02.txt:108 ¶51 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F014 |
| computing science | "computing science is —and will always be— concerned with the interplay between mechanized and human symbol manipulation" | L1-02.txt:72 ¶33 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F015 |
| program (abstract symbol manipulator) | "the program is an abstract symbol manipulator, which can be turned into a concrete one by supplying a computer to it" | L1-02.txt:68 ¶31 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F016 |
| half a conjecture | "all by itself, a program is no more than half a conjecture" | L1-02.txt:132 ¶63 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F017 |
| FMI (Formal Methods Initiative) | "I propose that we adopt for computing science FMI (= Formal Methods Initiative)" | L1-02.txt:72 ¶33 | L1-02 | coined here (text names the act: "I propose") | distinctions-vocabulary-F018 |
| curriculum infantilization | "such an obvious case of curriculum infantilization that its author should be cited for "contempt" of the student body" | L1-02.txt:130 ¶62 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F019 |
| reasoning by analogy | "One of its characteristics was that "reasoning by analogy" was rampant" | L1-02.txt:18 ¶6 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F020 |
| automatic programming (rejected term) | "it reveals "automatic programming" as a contradiction in terms" | L1-02.txt:72 ¶33 | L1-02 | unattributed (text silent on origin) | distinctions-vocabulary-F021 |
| debt (first time code); interest | "Shipping first time code is like going into debt." ‖ "Every minute spent on not-quite-right code counts as interest on that debt." | L1-03.txt:16 ¶5 | L1-03 | unattributed (text silent on origin) | distinctions-vocabulary-F022 |
| consolidation | "providing the consolidation that is key to understanding and continued incremental development" | L1-03.txt:12 ¶3 | L1-03 | unattributed (text silent on origin) | distinctions-vocabulary-F023 |
| failure to consolidate | "Another, more serious pitfall is the failure to consolidate." | L1-03.txt:16 ¶5 | L1-03 | unattributed (text silent on origin) | distinctions-vocabulary-F024 |
| unmasterable | "excess quantities will make a program unmasterable, leading to extreme specialization of programmers" | L1-03.txt:16 ¶5 | L1-03 | unattributed (text silent on origin) | distinctions-vocabulary-F025 |
| incremental growth | "We developed the product by incremental growth from a working prototype." | L1-03.txt:12 ¶3 | L1-03 | unattributed (text silent on origin) | distinctions-vocabulary-F026 |
| payment up-front and in-full | "we recognize this amounts to preserving the concept of payment up-front and in-full" | L1-03.txt:18 ¶6 | L1-03 | unattributed (text silent on origin) | distinctions-vocabulary-F027 |
| Code is bad | "Code is bad. It rots. It requires periodic maintenance." | L1-04.txt:8 ¶1 | L1-04 | unattributed (text silent on origin) | distinctions-vocabulary-F028 |
| expressive power (of code) | "increase the productivity of individual programmers in terms of the expressive power of the code they write" | L1-04.txt:10 ¶2 | L1-04 | unattributed (text silent on origin) | distinctions-vocabulary-F029 |
| n^2 communication costs | "Engineers have n^2 communication costs" | L1-04.txt:10 ¶2 | L1-04 | unattributed (text silent on origin) | distinctions-vocabulary-F030 |
| the best code is no code at all | "but the best code is no code at all" ‖ "The Best Code is No Code At All" | L1-05.txt:42 ¶15; L1-05.txt:2 (header line) | L1-05 | unattributed (text silent on origin) | distinctions-vocabulary-F031 |
| Code Smaller (volume of code) | "reduce the volume of code an individual programmer has to read to understand how a program works" | L1-05.txt:35 ¶12 | L1-05 | unattributed (text silent on origin) | distinctions-vocabulary-F032 |
| physical space (excluded sense) | "to make the code fit into less physical space" | L1-05.txt:35 ¶12 | L1-05 | unattributed (text silent on origin) | distinctions-vocabulary-F033 |
| start with brevity | "Start with brevity. Increase the other dimensions as required by testing." ‖ "Wil Shipley argues that we should rein in our natural tendencies" | L1-05.txt:33 ¶11; L1-05.txt:18 ¶6 | L1-05 | borrowed (text attributes it: Wil Shipley, L1-05:18) | distinctions-vocabulary-F034 |
| dimensions (of code) | "In coding, you have many dimensions in which you can rate code" ‖ "these dimensions are all in opposition to one another" | L1-05.txt:22 ¶8; L1-05.txt:31 ¶10 | L1-05 | borrowed (text attributes it: Wil Shipley, L1-05:18) | distinctions-vocabulary-F035 |
| your own worst enemy | "As a software developer, you are your own worst enemy." | L1-05.txt:16 ¶5 | L1-05 | unattributed (text silent on origin) | distinctions-vocabulary-F036 |
| source code is a liability, not an asset | "“Source code is a liability, not an asset!”" ‖ "I got it from (I think) Tim Ottinger and Alan Cooper said it earlier" | L1-06.txt:12 ¶3; L1-06.txt:14 ¶4 | L1-06 | borrowed (text attributes it: Ottinger and Cooper, L1-06:14) | distinctions-vocabulary-F037 |
| source code = financial debt | "Source code is akin to financial debt." | L1-06.txt:20 ¶7 | L1-06 | unattributed (text silent on origin) | distinctions-vocabulary-F038 |
| necessary evil | "Source code is merely the necessary evil that’s required to create value." | L1-06.txt:18 ¶6 | L1-06 | unattributed (text silent on origin) | distinctions-vocabulary-F039 |
| ongoing costs | "Meanwhile, code has ongoing costs. You have to understand it, you have to maintain it, you have to adapt it to new goals over time." | L1-06.txt:24 ¶9 | L1-06 | unattributed (text silent on origin) | distinctions-vocabulary-F040 |
| underwater | "It’s possible to end up underwater in a situation where your debt is actually bigger than your house is worth." | L1-06.txt:22 ¶8 | L1-06 | unattributed (text silent on origin) | distinctions-vocabulary-F041 |
| debt-to-value ratio | "In some respects, it’s underwater now in terms of its debt-to-value ratio." | L1-06.txt:34 ¶14 | L1-06 | unattributed (text silent on origin) | distinctions-vocabulary-F042 |
| LOC/debt | "The question is entirely, “What did you do with that LOC/debt?”" | L1-06.txt:26 ¶10 | L1-06 | unattributed (text silent on origin) | distinctions-vocabulary-F043 |
| business value | "What we actually do is deliver business value, or solutions to real-world problems, or however you want to state it." | L1-06.txt:18 ¶6 | L1-06 | unattributed (text silent on origin) | distinctions-vocabulary-F044 |
| software components (families) | "should be available in families arranged according to precision, robustness, generality and timespace performance" | L2-01.txt:12 ¶3 | L2-01 | unattributed (text silent on origin) | distinctions-vocabulary-F045 |
| mass production techniques | "In the phrase ‘mass production techniques,’ my emphasis is on ‘techniques’ and not on mass production plain." | L2-01.txt:18 ¶6 | L2-01 | unattributed (text silent on origin) | distinctions-vocabulary-F046 |
| binding time | "One phrase contains much of the secret of making families of software components: ‘binding time.’" | L2-01.txt:56 ¶23 | L2-01 | unattributed (text silent on origin) | distinctions-vocabulary-F047 |
| sale time parameters | "One might call these early-bound parameters ‘sale time’ parameters." | L2-01.txt:62 ¶26 | L2-01 | coined here (text names the act: "One might call") | distinctions-vocabulary-F048 |
| black boxes (components) | "In short, he should be able safely to regard components as black boxes." | L2-01.txt:26 ¶10 | L2-01 | unattributed (text silent on origin) | distinctions-vocabulary-F049 |
| models / sizes (not replicates) | "‘Mass production’ of software means multiplicity of what manufacturing industry would call ‘models,’ or ‘sizes’ rather than multiplicity of replicates of each." | L2-01.txt:52 ¶21 | L2-01 | unattributed (text silent on origin) | distinctions-vocabulary-F050 |
| construction vs excision | "Sysgen creates systems not by construction, but rather by excision, from an intentionally fat model." | L2-01.txt:58 ¶24 | L2-01 | unattributed (text silent on origin) | distinctions-vocabulary-F051 |
| pilot plant | "Finally I shall raise the question of starting up a ‘pilot plant’ for software components." | L2-01.txt:24 ¶9 | L2-01 | unattributed (text silent on origin) | distinctions-vocabulary-F052 |
| modularity (interchangeable parts) | "The idea of interchangeable parts corresponds roughly to our term ‘modularity,’ and is fitfully respected." | L2-01.txt:18 ¶6 | L2-01 | unattributed (text silent on origin) | distinctions-vocabulary-F053 |
| industrialism | "What I have just asked for is simply industrialism" | L2-01.txt:155 ¶71 | L2-01 | unattributed (text silent on origin) | distinctions-vocabulary-F054 |
| file descriptor | "The returned value filep is called a file descriptor." | L2-02.txt:96 ¶44 | L2-02 | unattributed (text silent on origin) | distinctions-vocabulary-F055 |
| link | "This feature is called linking; a directory entry for a file is sometimes called a link." | L2-02.txt:56 ¶24 | L2-02 | unattributed (text silent on origin) | distinctions-vocabulary-F056 |
| i-number | "This pointer is an integer called the i-number (for index number) of the file." | L2-02.txt:125 ¶58 | L2-02 | unattributed (text silent on origin) | distinctions-vocabulary-F057 |
| image; process | "An image is a computer execution environment." ‖ "A process is the execution of an image." | L2-02.txt:161 ¶72; L2-02.txt:163 ¶73 | L2-02 | unattributed (text silent on origin) | distinctions-vocabulary-F058 |
| pipe | "creates an interprocess channel called a pipe" | L2-02.txt:183 ¶83 | L2-02 | unattributed (text silent on origin) | distinctions-vocabulary-F059 |
| filter | "A program such as pr which copies its standard input to its standard output (with processing) is called a filter." | L2-02.txt:261 ¶121 | L2-02 | unattributed (text silent on origin) | distinctions-vocabulary-F060 |
| the Shell | "The Shell is a command line interpreter: it reads lines typed by the user and interprets them as requests to execute other programs." | L2-02.txt:213 ¶98 | L2-02 | unattributed (text silent on origin) | distinctions-vocabulary-F061 |
| special files | "Special files constitute the most unusual feature of the UNIX file system." | L2-02.txt:64 ¶28 | L2-02 | unattributed (text silent on origin) | distinctions-vocabulary-F062 |
| mount | "In effect, mount replaces a leaf of the hierarchy tree (the ordinary file) by a whole new subtree" | L2-02.txt:70 ¶31 | L2-02 | unattributed (text silent on origin) | distinctions-vocabulary-F063 |
| salvation through suffering | "This may be a thinly disguised version of the “salvation through suffering” philosophy, but in our case it worked." | L2-02.txt:353 ¶166 | L2-02 | unattributed (text silent on origin) | distinctions-vocabulary-F064 |
| self-supporting | "It is worth noting that the system is totally self-supporting." | L2-02.txt:28 ¶10 | L2-02 | unattributed (text silent on origin) | distinctions-vocabulary-F065 |
| fertile ideas | "The success of UNIX lies not so much in new inventions but rather in the full exploitation of a carefully selected set of fertile ideas" | L2-02.txt:367 ¶173 | L2-02 | unattributed (text silent on origin) | distinctions-vocabulary-F066 |
| private showing | "Subject: CPAN "private showing"" ‖ "This "release" is mainly meant for the current keepers of the / various Perl archives." | L2-03.txt:11 ¶1; L2-03.txt:23-24 ¶4 | L2-03 | unattributed (text silent on origin) | distinctions-vocabulary-F067 |
| Comparative Perl Archaeology | "you have 7.5 weeks time to practise Comparative Perl Archaeology" | L2-03.txt:36 ¶5 | L2-03 | unattributed (text silent on origin) | distinctions-vocabulary-F068 |
| Mother of All Perl Archives | "of the CPAN is to be the Mother of All Perl Archives" | L2-03.txt:38 ¶5 | L2-03 | unattributed (text silent on origin) | distinctions-vocabulary-F069 |
| CPAN (expansion absent from saved copy) | "of the CPAN is to be the Mother of All Perl Archives" | L2-03.txt:38 ¶5 | L2-03 | unattributed (text silent on origin) | distinctions-vocabulary-F070 |
| skeletal CPAN | "enhancements for this skeletal CPAN" | L2-03.txt:35 ¶5 | L2-03 | unattributed (text silent on origin) | distinctions-vocabulary-F071 |
| unpublished (all my modules) | "Summary; NPM is no longer a place that I’ll share my open source work at, so, I’ve just unpublished all my modules." | L2-04.txt:14 ¶4 | L2-04 | unattributed (text silent on origin) | distinctions-vocabulary-F072 |
| liberated | "I've Just Liberated My Modules" | L2-04.txt:2 (header line) | L2-04 | unattributed (text silent on origin) | distinctions-vocabulary-F073 |
| private land (NPM) | "NPM is someone’s private land where corporate is more powerful than the people" | L2-04.txt:12 ¶3 | L2-04 | unattributed (text silent on origin) | distinctions-vocabulary-F074 |
| Power To The People | "I do open source because, Power To The People" | L2-04.txt:12 ¶3 | L2-04 | unattributed (text silent on origin) | distinctions-vocabulary-F075 |
| dependency | "In today’s software development world, a dependency is additional code that you want to call from your program." | L2-05.txt:16 ¶5 | L2-05 | unattributed (text silent on origin) | distinctions-vocabulary-F076 |
| package (= library, module) | "In this article we’ll call that unit of code a package; some systems use terms like library or module instead of package." | L2-05.txt:16 ¶5 | L2-05 | unattributed (text silent on origin) | distinctions-vocabulary-F077 |
| package (downloaded code) | "A package, for this discussion, is code you download from the internet." | L2-05.txt:39 ¶13 | L2-05 | unattributed (text silent on origin) | distinctions-vocabulary-F078 |
| dependency manager | "A dependency manager (sometimes called a package manager) automates the downloading and installation of dependency packages." | L2-05.txt:20 ¶7 | L2-05 | unattributed (text silent on origin) | distinctions-vocabulary-F079 |
| fixed costs of reuse | "But the high fixed costs of reuse mean that manually-reused packages tend to be big: a tiny package would be easier to reimplement." | L2-05.txt:18 ¶6 | L2-05 | unattributed (text silent on origin) | distinctions-vocabulary-F080 |
| reputational support | "The commercial and legal support for trusting our software sources was replaced by reputational support." | L2-05.txt:45 ¶16 | L2-05 | unattributed (text silent on origin) | distinctions-vocabulary-F081 |
| cost of adopting a bad dependency | "the sum, over all possible bad outcomes, of the cost of each bad outcome multiplied by its probability of happening (risk)" | L2-05.txt:49 ¶18 | L2-05 | unattributed (text silent on origin) | distinctions-vocabulary-F082 |
| indirect (transitive) dependency | "Flaws in indirect dependencies are just as bad for your program as flaws in direct dependencies." | L2-05.txt:111 ¶49 | L2-05 | unattributed (text silent on origin) | distinctions-vocabulary-F083 |
| amalgamation | "a single 200,000-line C source file and a single 11,000-line header, the “amalgamation.”" | L2-05.txt:75 ¶31 | L2-05 | unattributed (text silent on origin) | distinctions-vocabulary-F084 |
| creeping dependencies | "Creeping dependencies can also affect the size of your project." | L2-05.txt:169 ¶78 | L2-05 | unattributed (text silent on origin) | distinctions-vocabulary-F085 |
| Inspect / Test / Abstract / Isolate / Avoid / Upgrade / Watch | "Inspect the dependency" ‖ "Test the dependency" ‖ "Abstract the dependency" ‖ "Isolate the dependency" ‖ "Avoid the dependency" ‖ "Upgrade the dependency" ‖ "Watch your dependencies" | L2-05.txt:57 ¶22; L2-05.txt:115 ¶51; L2-05.txt:121 ¶54; L2-05.txt:129 ¶58; L2-05.txt:135 ¶61; L2-05.txt:143 ¶65; L2-05.txt:161 ¶74 | L2-05 | unattributed (text silent on origin) | distinctions-vocabulary-F086 |
| "done" code | "some code really is “done.”" | L2-05.txt:91 ¶39 | L2-05 | unattributed (text silent on origin) | distinctions-vocabulary-F087 |
| thin wrapper | "define an interface of your own, along with a thin wrapper implementing that interface using the dependency" | L2-05.txt:125 ¶56 | L2-05 | unattributed (text silent on origin) | distinctions-vocabulary-F088 |

The column "coined here or borrowed" rests on the text's own attribution only. "Unattributed" means the text is silent; prior use outside the text was not checked (breadth territory).

### Aphorisms

| Quote | Word count | Location | ID | Kind | F-id |
|---|---|---|---|---|---|
| "As a by-product, the rewrite also saved around 2,000 lines of code." | 12 | L1-01.txt:12 ¶3 | L1-01 | sentence | distinctions-vocabulary-F260 |
| "The usual way in which we plan today for tomorrow is in yesterday's vocabulary." | 14 | L1-02.txt:10 ¶2 | L1-02 | sentence | distinctions-vocabulary-F261 |
| "Coping with radical novelty requires an orthogonal method." | 8 | L1-02.txt:14 ¶4 | L1-02 | sentence | distinctions-vocabulary-F262 |
| "Again, the shallowness of the underlying analogy is worthy of the Middle Ages." | 13 | L1-02.txt:58 ¶26 | L1-02 | sentence | distinctions-vocabulary-F263 |
| "Your car needs maintenance too, doesn't it?" | 7 | L1-02.txt:56 ¶25 | L1-02 | sentence | distinctions-vocabulary-F264 |
| "This is bad, because operational reasoning is a tremendous waste of mental effort." | 13 | L1-02.txt:108 ¶51 | L1-02 | sentence | distinctions-vocabulary-F265 |
| "The programmer's task is to present such complete conjectures as proven theorems." | 12 | L1-02.txt:132 ¶63 | L1-02 | sentence | distinctions-vocabulary-F266 |
| "It really helps to view a program as a formula." | 10 | L1-02.txt:70 ¶32 | L1-02 | sentence | distinctions-vocabulary-F267 |
| "The popularity of its name is enough to make it suspect." | 11 | L1-02.txt:48 ¶21 | L1-02 | sentence | distinctions-vocabulary-F268 |
| "we should not regard them as "lines produced" but as "lines spent"" | 12 | L1-02.txt:52 ¶23 | L1-02 | clause | distinctions-vocabulary-F269 |
| "a program is no more than half a conjecture" | 9 | L1-02.txt:132 ¶63 | L1-02 | clause | distinctions-vocabulary-F270 |
| "alternatives are allowed to be better." | 6 | L1-02.txt:74 ¶34 | L1-02 | clause | distinctions-vocabulary-F271 |
| "Shipping first time code is like going into debt." | 9 | L1-03.txt:16 ¶5 | L1-03 | sentence | distinctions-vocabulary-F272 |
| "The danger occurs when the debt is not repaid." | 9 | L1-03.txt:16 ¶5 | L1-03 | sentence | distinctions-vocabulary-F273 |
| "Every minute spent on not-quite-right code counts as interest on that debt." | 12 | L1-03.txt:16 ¶5 | L1-03 | sentence | distinctions-vocabulary-F274 |
| "Objects make the cost of this transaction tolerable." | 8 | L1-03.txt:16 ¶5 | L1-03 | sentence | distinctions-vocabulary-F275 |
| "Another, more serious pitfall is the failure to consolidate." | 9 | L1-03.txt:16 ¶5 | L1-03 | sentence | distinctions-vocabulary-F276 |
| "We developed the product by incremental growth from a working prototype." | 11 | L1-03.txt:12 ¶3 | L1-03 | sentence | distinctions-vocabulary-F277 |
| "Here the best antidote is more complete familiarity with the product and its implementation." | 14 | L1-03.txt:14 ¶4 | L1-03 | sentence | distinctions-vocabulary-F278 |
| "Code is bad." | 3 | L1-04.txt:8 ¶1 | L1-04 | sentence | distinctions-vocabulary-F279 |
| "Code is produced by engineers." | 5 | L1-04.txt:10 ¶2 | L1-04 | sentence | distinctions-vocabulary-F280 |
| "To make more code requires more engineers." | 7 | L1-04.txt:10 ¶2 | L1-04 | sentence | distinctions-vocabulary-F281 |
| "Less code to do the same thing (and possibly better)." | 10 | L1-04.txt:10 ¶2 | L1-04 | sentence | distinctions-vocabulary-F282 |
| "The more code you have, the more places there are for bugs to hide." | 14 | L1-04.txt:8 ¶1 | L1-04 | sentence | distinctions-vocabulary-F283 |
| "Code isn’t our enemy." | 4 | L1-05.txt:14 ¶4 | L1-05 | sentence | distinctions-vocabulary-F284 |
| "You want to see the real enemy? Go look in the mirror." | 12 | L1-05.txt:14 ¶4 | L1-05 | two sentences | distinctions-vocabulary-F285 |
| "As a software developer, you are your own worst enemy." | 10 | L1-05.txt:16 ¶5 | L1-05 | sentence | distinctions-vocabulary-F286 |
| "Start with brevity." | 3 | L1-05.txt:33 ¶11 | L1-05 | sentence | distinctions-vocabulary-F287 |
| "Now, remember, these dimensions are all in opposition to one another." | 11 | L1-05.txt:31 ¶10 | L1-05 | sentence | distinctions-vocabulary-F288 |
| "The Best Code is No Code At All" | 8 | L1-05.txt:2 (header line) | L1-05 | title | distinctions-vocabulary-F289 |
| "the best code is no code at all" | 8 | L1-05.txt:42 ¶15 | L1-05 | clause | distinctions-vocabulary-F290 |
| "you’ll love it enough to write as little of it as possible" | 12 | L1-05.txt:44 ¶16 | L1-05 | clause | distinctions-vocabulary-F291 |
| "“Source code is a liability, not an asset!”" | 8 | L1-06.txt:12 ¶3 | L1-06 | sentence | distinctions-vocabulary-F292 |
| "Source code is akin to financial debt." | 7 | L1-06.txt:20 ¶7 | L1-06 | sentence | distinctions-vocabulary-F293 |
| "Source code is merely the necessary evil that’s required to create value." | 12 | L1-06.txt:18 ¶6 | L1-06 | sentence | distinctions-vocabulary-F294 |
| "The more code you have, the larger those ongoing costs will be." | 12 | L1-06.txt:24 ¶9 | L1-06 | sentence | distinctions-vocabulary-F295 |
| "Writing code is the means we use to realize that value." | 11 | L1-06.txt:24 ¶9 | L1-06 | sentence | distinctions-vocabulary-F296 |
| "Bust out your delete key and start whacking." | 8 | L1-06.txt:36 ¶15 | L1-06 | sentence | distinctions-vocabulary-F297 |
| "You have to pay interest on your debt every month." | 10 | L1-06.txt:20 ¶7 | L1-06 | sentence | distinctions-vocabulary-F298 |
| "The question is entirely, “What did you do with that LOC/debt?”" | 11 | L1-06.txt:26 ¶10 | L1-06 | sentence | distinctions-vocabulary-F299 |
| "With few exceptions, source code itself is not a valuable commodity." | 11 | L1-06.txt:18 ¶6 | L1-06 | sentence | distinctions-vocabulary-F300 |
| "Nonetheless, it’s absolutely critical that you get yourself above water as soon as possible." | 14 | L1-06.txt:36 ¶15 | L1-06 | sentence | distinctions-vocabulary-F301 |
| "We undoubtedly produce software by backward techniques." | 7 | L2-01.txt:16 ¶5 | L2-01 | sentence | distinctions-vocabulary-F302 |
| "We have to begin thinking small." | 6 | L2-01.txt:91 ¶39 | L2-01 | sentence | distinctions-vocabulary-F303 |
| "The system comes first; components are merely annoying incidentals." | 9 | L2-01.txt:125 ¶56 | L2-01 | sentence | distinctions-vocabulary-F304 |
| "I don’t think a components industry can be standardized into existence." | 11 | L2-01.txt:149 ¶68 | L2-01 | sentence | distinctions-vocabulary-F305 |
| "In short, he should be able safely to regard components as black boxes." | 13 | L2-01.txt:26 ¶10 | L2-01 | sentence | distinctions-vocabulary-F306 |
| "I would like to see components become a dignified branch of software engineering." | 13 | L2-01.txt:153 ¶70 | L2-01 | sentence | distinctions-vocabulary-F307 |
| "Components, dignified as a hardware field, is unknown as a legitimate branch of software." | 14 | L2-01.txt:20 ¶7 | L2-01 | sentence | distinctions-vocabulary-F308 |
| "The ability to produce members of a family is not enough." | 11 | L2-01.txt:137 ¶62 | L2-01 | sentence | distinctions-vocabulary-F309 |
| "The Software Industry is Not Industrialized." | 6 | L2-01.txt:14 ¶4 | L2-01 | title | distinctions-vocabulary-F310 |
| "No particular structuring is expected by the system." | 8 | L2-02.txt:44 ¶18 | L2-02 | sentence | distinctions-vocabulary-F311 |
| "Special files constitute the most unusual feature of the UNIX file system." | 12 | L2-02.txt:64 ¶28 | L2-02 | sentence | distinctions-vocabulary-F312 |
| "Neither process need know that a pipe, rather than an ordinary file, is involved." | 14 | L2-02.txt:183 ¶83 | L2-02 | sentence | distinctions-vocabulary-F313 |
| "Filters are straightforward extensions of standard I/O redirection with pipes used instead of files." | 14 | L2-02.txt:311 ¶145 | L2-02 | sentence | distinctions-vocabulary-F314 |
| "The most important job of UNIX is to provide a file system." | 12 | L2-02.txt:40 ¶16 | L2-02 | sentence | distinctions-vocabulary-F315 |
| "The size of the new system is about one third greater than the old." | 14 | L2-02.txt:36 ¶14 | L2-02 | sentence | distinctions-vocabulary-F316 |
| "Third, nearly from the start, the system was able to, and did, maintain itself." | 14 | L2-02.txt:355 ¶167 | L2-02 | sentence | distinctions-vocabulary-F317 |
| "It is worth noting that the system is totally self-supporting." | 10 | L2-02.txt:28 ¶10 | L2-02 | sentence | distinctions-vocabulary-F318 |
| "I finally decided let this thing loose" | 7 | L2-03.txt:19 ¶2 | L2-03 | sentence (no period) | distinctions-vocabulary-F319 |
| "This "release" is mainly meant for the current keepers of the / various Perl archives." | 14 | L2-03.txt:23-24 ¶4 | L2-03 | sentence | distinctions-vocabulary-F320 |
| "I guess I will not be putting up an incoming/ directory to funet." | 13 | L2-03.txt:42 ¶6 | L2-03 | sentence | distinctions-vocabulary-F321 |
| "That tar very preferably already subdivided according to the CPAN hierarchy." | 11 | L2-03.txt:50 ¶6 | L2-03 | sentence | distinctions-vocabulary-F322 |
| "This is not a knee-jerk action." | 6 | L2-04.txt:16 ¶5 | L2-04 | sentence | distinctions-vocabulary-F323 |
| "NPM is someone’s private land where corporate is more powerful than the people" | 13 | L2-04.txt:12 ¶3 | L2-04 | clause | distinctions-vocabulary-F324 |
| "A little copying is better than a little dependency." | 9 | L2-05.txt:141 ¶64 | L2-05 | sentence | distinctions-vocabulary-F325 |
| "We are trusting more code with less justification for doing so." | 11 | L2-05.txt:47 ¶17 | L2-05 | sentence | distinctions-vocabulary-F326 |
| "But there are important differences we’re ignoring." | 7 | L2-05.txt:41 ¶14 | L2-05 | sentence | distinctions-vocabulary-F327 |
| "Presented this way, it sounds incredibly unsafe." | 7 | L2-05.txt:39 ¶13 | L2-05 | sentence | distinctions-vocabulary-F328 |
| "So the risk probability almost doesn’t matter: it’s being multiplied by zero." | 12 | L2-05.txt:53 ¶20 | L2-05 | sentence | distinctions-vocabulary-F329 |
| "This analysis ignores two costs." | 5 | L2-05.txt:145 ¶66 | L2-05 | sentence | distinctions-vocabulary-F330 |
| "Again, upgrades should not be completely automatic." | 7 | L2-05.txt:155 ¶71 | L2-05 | sentence | distinctions-vocabulary-F331 |
| "Recognize the problem." ‖ "Establish best practices for today." ‖ "Develop better dependency technology for tomorrow." | 3 + 5 + 6 | L2-05.txt:185 ¶86; L2-05.txt:189 ¶88; L2-05.txt:193 ¶90 | L2-05 | three sentences | distinctions-vocabulary-F332 |
| "There’s a lot of good software out there." ‖ "Let’s work together to find out how to reuse it safely." | 8 + 11 | L2-05.txt:195 ¶91 | L2-05 | two sentences | distinctions-vocabulary-F333 |
| "Today, the situation is reversed" | 5 | L2-05.txt:8 ¶1 | L2-05 | clause | distinctions-vocabulary-F334 |
| "Most of the time the entirety of the decision is “let’s see what happens.”" | 14 | L2-05.txt:179 ¶83 | L2-05 | sentence | distinctions-vocabulary-F335 |

## Rated statements

| R-id | Candidate statement (one imperative sentence) | Rating | For (F-ids) | Against (F-ids) | Sources (IDs) | Deciding fact (≤ 15 words) |
|---|---|---|---|---|---|---|
| R01 | Book lines of code as lines spent, not lines produced. | AXIOM | distinctions-vocabulary-F008, distinctions-vocabulary-F269, distinctions-vocabulary-F350, distinctions-vocabulary-F351, distinctions-vocabulary-F349, distinctions-vocabulary-F003 | — | L1-01, L1-02, L1-06 | L1-02 states it; L1-01 and L1-06 reject lines written as a measure. |
| R02 | Treat source code as debt that accrues interest. | CANDIDATE | distinctions-vocabulary-F022, distinctions-vocabulary-F190, distinctions-vocabulary-F213, distinctions-vocabulary-F038 | distinctions-vocabulary-F337, distinctions-vocabulary-F339 | L1-03, L1-06 | L1-03 allows a little debt; L1-06 treats all code as debt. |
| R03 | Name the programmer, not the code, as the source of code's cost. | CANDIDATE | distinctions-vocabulary-F201, distinctions-vocabulary-F203, distinctions-vocabulary-F160, distinctions-vocabulary-F036 | distinctions-vocabulary-F028, distinctions-vocabulary-F200 | L1-02, L1-04, L1-05 | L1-05 and L1-02 blame the programmer; L1-04 (PARTIAL) blames the code. |
| R04 | Call a defect an error, not a bug. | CANDIDATE | distinctions-vocabulary-F012, distinctions-vocabulary-F096, distinctions-vocabulary-F160 | distinctions-vocabulary-F386, distinctions-vocabulary-F387 | L1-02, L1-04, L2-05 | Only L1-02 states it; L1-04 and L2-05 keep "bug". |
| R05 | Name each analogy as an analogy and state where it fails. | CANDIDATE | distinctions-vocabulary-F228, distinctions-vocabulary-F194, distinctions-vocabulary-F347, distinctions-vocabulary-F348 | distinctions-vocabulary-F163 | L1-02, L1-03, L2-01 | L1-03 and L2-01 label their image; L1-02 rejects the method outright. |
| R06 | Measure code volume by what a reader must read, not by physical space. | CANDIDATE | distinctions-vocabulary-F032, distinctions-vocabulary-F033, distinctions-vocabulary-F352 | — | L1-05 | One text states it; none opposes it. |
| R07 | Delete code only while preserving existing functionality. | CANDIDATE | distinctions-vocabulary-F366, distinctions-vocabulary-F365 | distinctions-vocabulary-F368, distinctions-vocabulary-F367 | L1-06, L2-04, L2-05 | L1-06 states the condition; L2-05 records a deletion that broke dependents. |
| R08 | Charge every line of code for understanding, debugging, maintaining, and adapting it. | AXIOM | distinctions-vocabulary-F040, distinctions-vocabulary-F417, distinctions-vocabulary-F418, distinctions-vocabulary-F419, distinctions-vocabulary-F028, distinctions-vocabulary-F389 | — | L1-04, L1-05, L1-06, L2-05 | Four texts across both lanes list overlapping costs; none denies them. |
| R09 | Define each coined term in the sentence that first uses it. | CANDIDATE | distinctions-vocabulary-F055, distinctions-vocabulary-F056, distinctions-vocabulary-F059, distinctions-vocabulary-F060, distinctions-vocabulary-F077, distinctions-vocabulary-F048 | — | L2-01, L2-02, L2-05 | Practice in three texts; no text states it as a rule. |
| R10 | Separate the cost of installing code from the cost of evaluating it. | CANDIDATE | distinctions-vocabulary-F155, distinctions-vocabulary-F080 | — | L2-05 | One text states it; L1-06 prices a licence against salary, not evaluation. |
| R11 | Keep size subordinate to understandability. | CANDIDATE | distinctions-vocabulary-F420, distinctions-vocabulary-F421, distinctions-vocabulary-F392 | distinctions-vocabulary-F112, distinctions-vocabulary-F395 | L2-02, L1-06, L1-05 | L2-02 and L1-06 subordinate size; L1-05 ranks brevity first. |

Status of the two AXIOM rows: both stand on text-level evidence only (NONE reader); both are Tier 3 verifier triggers.

For each CANDIDATE, the second source or exemplar that would decide it:

- R02: Cunningham's own later statement of the debt image, or a lane-2 text applying it; L1-03:16 limits debt to unrepaid first-time code.
- R03: Skrenta's original post (the L1-04 gap): whether "enemy" is his word and where he places the blame.
- R04: A second text stating the same rule, or Dijkstra's other writing on the word (breadth); L1-04 and L2-05 practice the opposite without comment.
- R05: A second author who states where his own image fails; L1-06 flags "akin" and states no limit.
- R06: A second text that defines volume by reader effort, or the Shipley original quoted in L1-05:20-33.
- R07: A primary record of the left-pad deletion (registry notice, adjacent) and a second text on preserved function.
- R09: An author's own statement of definition practice; the eleven show the practice, none states it.
- R10: A second primary text that separates install cost from evaluation cost; L2-05:193 is the only statement.
- R11: The Shipley original (L1-05 quotes it) or a text that ranks size against comprehension in the same terms.

## Open questions

- Q1: searched L1-04.txt and L1-05.txt for Skrenta's own wording; "enemy" appears in L1-04.txt only in the header title (line 2, from link text and search index), so Skrenta's own use of the word is UNVERIFIED (distinctions-vocabulary-F199). Terms beyond the two quoted paragraphs of the original post are unknown. The saved L2-03 copy never expands "CPAN" (grep for "compreh" returns 0); the launch post is not held (distinctions-vocabulary-F070).
- Q3: Skrenta's first full statement of the enemy image is not obtainable from the saved L1-04; the only statement is Atwood's (distinctions-vocabulary-F200). Extensions were enumerated by whole-text reading plus a grep sweep for "analog" and "metaphor" over L1-02 (every hit at lines 12, 18, 26, 36, 38, 40, 58, 102, 106 is in a row or in Q2).
- Q4: sentence-split script over all eleven texts; L1-01 yields one sentence under 15 words (distinctions-vocabulary-F260) and L2-04 none whole (clause distinctions-vocabulary-F324). L2-03 is hard-wrapped, so its sentences were counted after rejoining lines.
- Q5: not searched in the three supplementary files (L2-01-discussion.txt, L2-02-dumped-retro.txt, L2-03-dumped-bowers.txt); they are not among the eleven.
- Q7: searched the texts for glosses of each named product, event, and term; where none exists the row says "unglossed". No study or project log was found that measures what a reader five years out needs explained; the rows record dependencies only.
- All: the origin of each term outside its text (who coined "technical debt", "software engineering", "left-pad" detail) is outside this category; the texts name Ottinger and Cooper (L1-06:14), Shipley (L1-05:18), Robbins (L1-02:22), Lamport and the Go community (L2-05:113, 141) as sources.

## Cross-category notes

- enemies · distinctions-vocabulary-F201, distinctions-vocabulary-F200 · L1-05 names the programmer where L1-04 (PARTIAL) names code; "enemy" occurs in L1-05 only.
- enemies · distinctions-vocabulary-F020 · L1-02 names "reasoning by analogy" as the medieval mode; the same label appears in the existing manifesto first-principles.md:32 ("Your enemy is **Reasoning by Analogy**."), a fact for collection-fit.
- tensions · distinctions-vocabulary-F408, distinctions-vocabulary-F412, distinctions-vocabulary-F421 · delete as virtue (L1-06) against hazard (L2-05); outside code bought (L1-06) against avoided or copied (L2-05); size against understandability (L2-02, L1-06 against L1-05).
- tensions · distinctions-vocabulary-F112, distinctions-vocabulary-F120 · within lane 1: brevity first (L1-05:33) against maintainability first (L1-06:30).
- tensions · distinctions-vocabulary-F415, distinctions-vocabulary-F416 · software engineering: dignified (L2-01, 1968) against doomed (L1-02, 1988).
- evidence · distinctions-vocabulary-F340 · "technical debt" occurs in neither L1-03 nor L1-06; L1-03:18 calls the image "our debt analogy".
- evidence · distinctions-vocabulary-F028, distinctions-vocabulary-F067 · L1-04 and L2-03 are PARTIAL copies; claims resting on them are marked.
- breadth · distinctions-vocabulary-F037, distinctions-vocabulary-F034 · sources named in the texts and not in the dump: Ottinger and Cooper (L1-06:14), Shipley (L1-05:18), Robbins (L1-02:22), Lamport (L2-05:113), the Go proverbs (L2-05:141; reference 20 at L2-05:237), Flaherty (L1-02:96).
- breadth · L2-02:448 · lane-2 link: "We are particularly appreciative of the inventiveness, thoughtful criticism, and constant support of R. Morris, M.D. McIlroy, and J.F. Ossanna." McIlroy is the author of L2-01; the later UNIX paper thanks him (1974 after 1968).
- demands · distinctions-vocabulary-F287, distinctions-vocabulary-F297, distinctions-vocabulary-F332 · imperatives in the texts: "Start with brevity." (L1-05:33), "Bust out your delete key and start whacking." (L1-06:36), "Recognize the problem." (L2-05:185).
- evidence · distinctions-vocabulary-F482, distinctions-vocabulary-F483 · L2-05:113 quotes "30% of the 750,000 packages" and L2-05:22 "over 750,000 packages" (time-bound counts).
