# Source Index — lane1
Loaded in full from source: First Principles manifesto v1.0.1 (/home/user/LLM_MANIFESTOS/manifestos/first-principles.md), Strunk SPR v3.0 (/home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml, 2923 lines), manifesto-oath protocol (/home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md).
Interplay: First Principles ("Doubt the Form", "Dump the Apple Basket") and Strunk ("Use definite, specific, concrete language", "Omit needless words") converge on atoms over labels, so each dumped link is a claim to verify and each finding is a located quote; the tension between Strunk's judgment protocol and the research rule against interpretation resolves to recording text and no judgment.
Commitments: I must verify each dumped link against the text itself, and I will record every URL tried; I must not paraphrase where a quote exists, and I will not report a fact without a paragraph and file:line; I must omit needless words, and I will keep each entry to its verbatim quote and its location.

Location convention: P{n} is the nth body paragraph of the local copy (blank-line separated, after the 6-line header and one blank line); the parenthesis gives file:line in /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/. Word count is `wc -w` of the body with the ">" and "- " markers removed. Quantified claims list explicit numerals, number words, multipliers, fractions, percentages, dates and formulas; ordinals, "one" as a pronoun, and vague quantifiers (several, many, few) are omitted.

## Fetch table

| ID | title | author | year | URL fetched | status | words | local path | discrepancy with dump |
|---|---|---|---|---|---|---|---|---|
| L1-01 | -2000 Lines Of Code | Andy Hertzfeld | 1982 | https://www.folklore.org/Negative_2000_Lines_Of_Code.html | FULL | 275 | /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L1-01.txt | Title: page shows "-2000 Lines Of Code" (slug Negative_2000_Lines_Of_Code). Author, year, subject match (page fields: Author Andy Hertzfeld; Date February 1982; Characters Bill Atkinson). |
| L1-02 | On the cruelty of really teaching computing science (EWD 1036) | Edsger W. Dijkstra | 1988 | https://www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1036.html | FULL | 6125 | /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L1-02.txt | Author, year match (signed "Austin, 2 December 1988"). Source is a transcription by Javier Smaldone (revised 12 May 2009); the PDF is a 30-page scan with no text layer. "lines spent" sentence present at P23. |
| L1-03 | The WyCash Portfolio Management System | Ward Cunningham | 1992 | https://c2.com/doc/oopsla92.html | FULL | 544 | /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L1-03.txt | Year matches (page byline "March 26, 1992"; OOPSLA '92 Experience Report). The phrase "technical debt" occurs 0 times in the text; text says "Shipping first time code is like going into debt." (P5). |
| L1-04 | Code is our enemy | Rich Skrenta | 2007 | https://blog.codinghorror.com/the-best-code-is-no-code-at-all/ (Atwood quotation; original http://www.skrenta.com/2007/05/code_is_our_enemy.html not served) | PARTIAL | 148 | /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L1-04.txt | Dumped link does not serve the post: 301 to https://www.linkedin.com/in/skrenta/ (HTTP 999). Text held is Atwood's two-paragraph quotation only. Year from URL path /2007/05/ and L1-05, not from the text. Dump note says "Physical volume of code"; "physical" occurs 0 times in the quotation. |
| L1-05 | The Best Code is No Code At All | Jeff Atwood | 2007 | https://blog.codinghorror.com/the-best-code-is-no-code-at-all/ | FULL | 728 | /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L1-05.txt | Author, year match (page: Jeff Atwood, 30 May 2007). Page article:modified_time 2025-09-28; text is the current page, not a 2007 capture. Dump note says "Amplifies Skrenta"; text states "Code isn’t our enemy." (P4) and "Code is only our enemy because there are so many of us programmers writing so damn much of it." (P15). |
| L1-06 | Source Code Is A Liability, Not An Asset | Eric Lee | 2009 | https://saintgimp.org/2009/03/11/source-code-is-a-liability-not-an-asset/ | FULL | 951 | /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L1-06.txt | Year matches page date March 11, 2009 (page updated December 14, 2018; P1 says "I originally posted this on my MSDN blog"; MSDN date not obtained). Dump note says "permanent"; "permanent" occurs 0 times; text says "Source code is akin to financial debt" and "mortgage" (P7-P8). |

## Per-source

### L1-01 — -2000 Lines Of Code — Andy Hertzfeld (1982) — FULL

**URLs tried**
- https://www.folklore.org/Negative_2000_Lines_Of_Code.html -> HTTP 200, text/html, 10285 bytes (final URL unchanged).

**Authorship and year, from the text or hosting page**
- Page fields: "Author: Andy Hertzfeld"; "Date: February 1982"; "Characters: Bill Atkinson"; "Topics: Software Design, Management, Lisa"; "Summary: It's hard to measure progress by lines of code". Body opens "In early 1982".

**Section headings in order**
- None. The text has no internal headings.

**First sentence (verbatim)**
- "In early 1982, the Lisa software team was trying to buckle down for the big push to ship the software within the next six months."

**Last sentence (verbatim)**
- "I'm not sure how the managers reacted to that, but I do know that after a couple more weeks, they stopped asking Bill to fill out the form, and he gladly complied."

**Quantified claims (verbatim; location = paragraph and file:line)**
- P1 (L1-01.txt:8): "In early 1982, the Lisa software team was trying to buckle down for the big push to ship the software within the next six months."
- P1 (L1-01.txt:8): "They devised a form that each engineer was required to submit every Friday, which included a field for the number of lines of code that were written that week."
- P3 (L1-01.txt:12): "made region operations almost six times faster"
- P3 (L1-01.txt:12): "the rewrite also saved around 2,000 lines of code"
- P4 (L1-01.txt:14): "wrote in the number: -2000"
- P5 (L1-01.txt:16): "after a couple more weeks, they stopped asking Bill to fill out the form"

### L1-02 — On the cruelty of really teaching computing science (EWD 1036) — Edsger W. Dijkstra (1988) — FULL

**URLs tried**
- https://www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1036.html -> HTTP 200, text/html (declared charset iso-8859-1; all bytes ASCII, entities &quot; and &#x2014; decoded), 39868 bytes.
- https://www.cs.utexas.edu/~EWD/ewd10xx/EWD1036.PDF -> HTTP 200, application/pdf, 918082 bytes, 30 pages, CCITT stencil page images (pdfimages), `pdftotext -layout` returns page numbers only. Not used as text source.

**Authorship and year, from the text or hosting page**
- Hosting page: archive "E.W. Dijkstra Archive ... (EWD 1036)"; text signed "Austin, 2 December 1988" and "prof. dr. Edsger W. Dijkstra, Department of Computer Sciences, The University of Texas at Austin"; footer "Transcription by Javier Smaldone. Revised Tue, 12 May 2009."

**Section headings in order**
- None. Structural markers in the text: P1 announces "The second part of this talk ... the first part of this talk"; P29 opens "And now comes the second —and hardest— part of my talk"; seven numbered items "(0)" through "(6)" at P36-P42.

**First sentence (verbatim)**
- "The second part of this talk pursues some of the scientific and educational consequences of the assumption that computers represent a radical novelty."

**Last sentence (verbatim)**
- "Their willingness to do so is our main safeguard against dictatorships, be they of the proletariat, of the scientific establishment, or of the corporate elite."
- The copy then ends with the sign-off: "Austin, 2 December 1988" and the signature block "prof. dr. Edsger W. Dijkstra ... USA".

**Quantified claims (verbatim; location = paragraph and file:line)**
- P9 (L1-02.txt:24): "Nobody is going to run 100 meters in five seconds"
- P9 (L1-02.txt:24): "The human mind is no different now from what it was five thousand years ago."
- P10 (L1-02.txt:26): "alternatives to running that are orders of magnitude more effective"
- P11 (L1-02.txt:28): "Instead of teaching 2 + 3 = 5 ,"
- P11 (L1-02.txt:28): "Spain's problems in the century that followed"
- P12 (L1-02.txt:30): "For decades, the former two gave rise to a torrent of religious, philosophical, or otherwise quasi-scientific tracts."
- P13 (L1-02.txt:32): "automatic computers embody not only one radical novelty but two of them"
- P14 (L1-02.txt:34): "From a bit to a few hundred megabytes, from a microsecond to a half an hour of computing confronts us with completely baffling ratio of 10^9!"
- P15 (L1-02.txt:36): "it is orders of magnitude worse than comparing, as a means of transportation, the supersonic jet plane with a crawling baby, for that speed ratio is only a thousand."
- P18 (L1-02.txt:42): "a million dollars a day seems a modest guess"
- P22 (L1-02.txt:50): "as one of the US computer manufacturers proved a few years ago when it hired, one night, hundreds of new "software engineers""
- P23 (L1-02.txt:52): ""number of lines of code produced per month""
- P23 (L1-02.txt:52): "if we wish to count lines of code, we should not regard them as "lines produced" but as "lines spent""
- P24 (L1-02.txt:54): "It is now two decades since it was pointed out that program testing may convincingly demonstrate the presence of bugs, but can never demonstrate their absence."
- P30 (L1-02.txt:66): "both the number of symbols involved and the amount of manipulation performed are many orders of magnitude larger than we can envisage"
- P32 (L1-02.txt:70): "We know of only one reliable way of doing that"
- P36 (L1-02.txt:78): "(0) the mathematical guild"
- P38 (L1-02.txt:82): "one silly idea and a month of frantic coding should suffice to make him a life-long millionaire"
- P40 (L1-02.txt:86): "mutate billion-dollar budgets into the illusion of automatic safety"
- P42 (L1-02.txt:90): "(6) the educational business"
- P43 (L1-02.txt:92): "And with this sixth example I have reached"
- P44 (L1-02.txt:94): "will last them another 50 years"
- P48 (L1-02.txt:102): "a program with only one bug used to be "almost correct""
- P49 (L1-02.txt:104): "say a quarter for undergraduates, two quarters for graduate students, and five dollars for faculty members: by the end of the first semester of the new regime, you will have collected enough money for two scholarships"
- P53 (L1-02.txt:112): "defined as the 8 by 8 square from which, at two opposite corners, two 1 by 1 squares have been removed"
- P53 (L1-02.txt:112): "The area of Q is 62, which equals the combined area of 31 dominos of 1 by 2."
- P53 (L1-02.txt:112): "The theorem is that the figure Q cannot be covered by 31 of such dominos."
- P54 (L1-02.txt:114): "no placement of 31 dominos will yield the figure Q"
- P56 (L1-02.txt:118): "covers 1 white and 1 black square"
- P56 (L1-02.txt:118): "the number of white squares and the number of black squares differ by 2"
- P57 (L1-02.txt:120): "many orders of magnitude shorter than the exhaustive investigation of the possible placements of 31 dominos"
- P57 (L1-02.txt:120): "replacing the original 8 by 8 square by any rectangle with sides of even length"
- P63 (L1-02.txt:132): "a program is no more than half a conjecture"
- P70 (L1-02.txt:146): "since the early 80's, such an introductory programming course has successfully been given to hundreds of college freshmen each year"
- P70 (L1-02.txt:146): "the previous sentence should be repeated at least another two times"
- P71 (L1-02.txt:148): "deviate so much from what 18-year old students are used to"
- P73 (L1-02.txt:152): "Austin, 2 December 1988"
- Note: "10^9" is the HTML <sup>9</sup> after "10" in the source. The Q figure, 8 by 8 square, and domino counts (P53-P57) form one arithmetic example.

### L1-03 — The WyCash Portfolio Management System — Ward Cunningham (1992) — FULL

**URLs tried**
- https://c2.com/doc/oopsla92.html -> HTTP 200, text/html, 4311 bytes. The page holds the complete experience report (title, byline, six body paragraphs, 2009 video addendum).

**Authorship and year, from the text or hosting page**
- Hosting page: "OOPSLA '92 Experience Report", "The WyCash Portfolio Management System", "Ward Cunningham, March 26, 1992". Footer addendum (2009 YouTube video link, transcription link) excluded from the copy.

**Section headings in order**
- None. The text has no internal headings.

**First sentence (verbatim)**
- "U.S. pension funds, corporations, and banks invest billions of dollars in the "cash" markets."

**Last sentence (verbatim)**
- "The modularity offered by objects and the practice of consolidation make the alternative, incremental growth, both feasible and desirable (but not always comfortable) in the competitive financial software market."

**Quantified claims (verbatim; location = paragraph and file:line)**
- P1 (L1-03.txt:8): "invest billions of dollars in the "cash" markets"
- P1 (L1-03.txt:8): "a remaining term to maturity of less than one year, but can include those with maturities as long as five years"
- P2 (L1-03.txt:10): "Objects help in two ways."
- P3 (L1-03.txt:12): "the roughly four megabytes of source code"

### L1-04 — Code is our enemy — Rich Skrenta (2007) — PARTIAL

**URLs tried**
- http://www.skrenta.com/2007/05/code_is_our_enemy.html -> HTTP 301 (Location https://www.linkedin.com/in/skrenta/) -> HTTP 999, text/html, 1530 bytes (LinkedIn script wrapper, no post text). FAILED.
- http://skrenta.com/2007/05/code_is_our_enemy.html -> same 301 -> LinkedIn HTTP 999. FAILED.
- http://www.skrenta.com/2007/05/ and http://www.skrenta.com/ -> HTTP 301 to the same LinkedIn URL. FAILED.
- https://www.skrenta.com/2007/05/code_is_our_enemy.html -> curl exit 60, TLS certificate name mismatch for www.skrenta.com, no body. FAILED.
- WebFetch http://www.skrenta.com/2007/05/code_is_our_enemy.html (two calls) -> HTTP 503. FAILED.
- https://archive.org/wayback/available?url=... -> HTTP 200 application/json; lists snapshots 20070602152648 and 20230330091854 of the original URL.
- http://web.archive.org/web/20070602152648id_/http://www.skrenta.com:80/2007/05/code_is_our_enemy.html and http://web.archive.org/web/20230330091854id_/http://www.skrenta.com/2007/05/code_is_our_enemy.html -> HTTP 403, body "Blocked by egress policy", header x-block-reason: hostname_blocked. FAILED. Not retried or routed around.
- WebFetch https://web.archive.org/web/20070602152648/http://www.skrenta.com/2007/05/code_is_our_enemy.html -> "Claude Code is unable to fetch from web.archive.org". FAILED.
- WebSearch, six queries (title, exact phrases "Code is bad. It rots. It requires periodic maintenance.", "Engineers have n^2 communication costs", "expressive power of the code they write", Skrentablog): the search index lists "Code is our enemy (Skrentablog)" at the original URL; the only retrievable text copy is Atwood's quotation in L1-05 (https://blog.codinghorror.com/the-best-code-is-no-code-at-all/ -> HTTP 200). That quotation is saved as the L1-04 copy.

**Authorship and year, from the text or hosting page**
- Authorship from L1-05 only: "Rich Skrenta writes that code is our enemy." Year not stated in the quotation; L1-05 dated 30 May 2007; the archive snapshot URL cited in L1-05 and the URL path /2007/05/ place the post in May 2007 (unverified against the original).

**Section headings in order**
- None.

**First sentence (verbatim)**
- "Code is bad."

**Last sentence (verbatim)**
- "Less organizational communication costs."

**Quantified claims (verbatim; location = paragraph and file:line)**
- P2 (L1-04.txt:10): "Engineers have n^2 communication costs"

### L1-05 — The Best Code is No Code At All — Jeff Atwood (2007) — FULL

**URLs tried**
- https://blog.codinghorror.com/the-best-code-is-no-code-at-all/ -> HTTP 200, text/html; charset=utf-8, 55110 bytes.

**Authorship and year, from the text or hosting page**
- Hosting page: byline "Jeff Atwood", date "30 May 2007", meta article:published_time 2007-05-30T12:00:00.000Z, article:modified_time 2025-09-28T07:05:39.000Z. One embedded image (storage.ghost.io ... /2025/09/) excluded.

**Section headings in order**
- None inside the post (page h1 is the title only). Bold phrases inside the post body: "As a software developer, you are your own worst enemy. The sooner you realize that, the better off you’ll be."; "the best code is no code at all"; "start with brevity".

**First sentence (verbatim)**
- "Rich Skrenta writes that code is our enemy."

**Last sentence (verbatim)**
- "If you love writing code – really, truly love to write code – you’ll love it enough to write as little of it as possible."

**Quantified claims (verbatim; location = paragraph and file:line)**
- P3 (L1-05.txt:12): "Engineers have n^2 communication costs"
- P10 (L1-05.txt:31): "You can spend three days writing a routine which is really beautiful and fast, so you’ve gotten two of your dimensions up, but you’ve spent three days, so the “time spent coding” dimension is way down."
- Note: P9 (L1-05.txt:24-29) is a six-item list inside Wil Shipley's quoted block, introduced at P8 (L1-05.txt:22) by "In coding, you have many dimensions in which you can rate code:"; items: Brevity of code; Featurefulness; Speed of execution; Time spent coding; Robustness; Flexibility.

### L1-06 — Source Code Is A Liability, Not An Asset — Eric Lee (2009) — FULL

**URLs tried**
- https://saintgimp.org/2009/03/11/source-code-is-a-liability-not-an-asset/ -> HTTP 200, text/html; charset=UTF-8, 91595 bytes.

**Authorship and year, from the text or hosting page**
- Hosting page: "Author Eric Lee", "Posted on March 11, 2009", updated December 14, 2018; body P1 "(I originally posted this on my MSDN blog.)". Six comment-area entries are pingbacks only; no reader comments.

**Section headings in order**
- None inside the post (page h1 is the title only).

**First sentence (verbatim)**
- "(I originally posted this on my MSDN blog.)"

**Last sentence (verbatim)**
- "Nonetheless, it’s absolutely critical that you get yourself above water as soon as possible."

**Quantified claims (verbatim; location = paragraph and file:line)**
- P10 (L1-06.txt:26): "“This week our team wrote 10k LOC!"
- P10 (L1-06.txt:26): "“This week we took on $10,000 in new debt!”"
- P11 (L1-06.txt:28): "“This week we removed 10K LOC while preserving all existing functionality!”"
- P13 (L1-06.txt:32): "at a true cost of at least $10,000 a month"
- P13 (L1-06.txt:32): "in order to avoid paying $1000 or even $500 to license a third-party software package that does the same thing?"
- P14 (L1-06.txt:34): "It has 134K LOC checked in to source control, and it could likely be implemented in about 10% of that, maybe 5%"

## Failures

- L1-04 (Skrenta, "Code is our enemy"): the primary text was not obtained. The dumped URL 301-redirects to a LinkedIn profile (HTTP 999 wrapper); https on www.skrenta.com fails TLS name verification; the Wayback snapshots (20070602152648, 20230330091854) are listed by the archive.org availability API but web.archive.org returns HTTP 403 "Blocked by egress policy" (x-block-reason: hostname_blocked) to curl and WebFetch; WebFetch on the original returns HTTP 503; six WebSearch queries found no other copy. The L1-04 file holds the two paragraphs that Atwood (L1-05) presents as a blockquote of Skrenta; the full post length and its date are unverified.
- L1-02 PDF (https://www.cs.utexas.edu/~EWD/ewd10xx/EWD1036.PDF): fetched, but a 30-page scan with no text layer; the HTML transcription is the text copy, so locations are paragraph indexes and not manuscript page numbers.
- L1-06 original MSDN post: not fetched; the dumped saintgimp.org repost is the copy. L1-05 and L1-06 pages were captured in 2026 and carry later modification dates (L1-05 2025-09-28; L1-06 2018-12-14).
