# Fetched texts: code liability and dependencies (2026-10-11)

`research/` is gitignored and vanishes with the container. These copies are the durable record.

Every file below was copied unchanged with `cp -p` and verified with `sha256sum` against its origin. Origin paths are relative to `research/manifesto-craft/`.

| folder | origin |
|---|---|
| `primary/` | `recon/sources/*.txt` (15 files) |
| `secondary/` | `recon/discovery/**` text files (194 files; subfolders `evidence/` and `breadth/` kept) |
| `index/` | `recon/index-lane1.md`, `recon/index-lane2.md`, `sources.md` (3 files) |

## primary/

file, ID, title, author, year, and URL fetched come from the header lines of each copy. Status and words come from the fetch tables in `index/index-lane1.md` and `index/index-lane2.md`.

| file | ID | title | author | year | URL fetched | status | words |
|---|---|---|---|---|---|---|---|
| L1-01.txt | L1-01 | -2000 Lines Of Code (URL slug: Negative_2000_Lines_Of_Code) | Andy Hertzfeld (character: Bill Atkinson) | 1982 (page field "Date: February 1982") | https://www.folklore.org/Negative_2000_Lines_Of_Code.html | FULL | 275 |
| L1-02.txt | L1-02 | On the cruelty of really teaching computing science (EWD 1036) | Edsger W. Dijkstra (transcription: Javier Smaldone, rev. 12 May 2009) | 1988 (text signed "Austin, 2 December 1988") | https://www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1036.html | FULL | 6125 |
| L1-03.txt | L1-03 | The WyCash Portfolio Management System (OOPSLA '92 Experience Report) | Ward Cunningham | 1992 (page byline "March 26, 1992") | https://c2.com/doc/oopsla92.html | FULL | 544 |
| L1-04-full.txt | L1-04 | Code is our enemy (page title "Code is our enemy (Skrentablog)"; page h2 "Code is our enemy") | Rich Skrenta (name from L1-05: "Rich Skrenta writes that code is our enemy."; the archived page prints no personal byline: banner "Skrentablog", host www.skrenta.com, RDF dc:creator empty) | 2007 (post footer "Posted on May 30, 2007 3:11 PM"; RDF dc:date 2007-05-30T15:11:17-08:00; Wayback capture 2 June 2007 15:26:48 GMT) | https://web.archive.org/web/20070602152648/http://www.skrenta.com/2007/05/code_is_our_enemy.html | not in fetch table | not in fetch table |
| L1-04.txt | L1-04 | Code is our enemy (Skrentablog; title from link text in L1-05 and search-index title) | Rich Skrenta (attribution: "Rich Skrenta writes that code is our enemy" in L1-05) | 2007 (URL path /2007/05/; L1-05 dated 30 May 2007 cites a 2 June 2007 archive snapshot) | https://blog.codinghorror.com/the-best-code-is-no-code-at-all/ (Atwood's block quotation of Skrenta; original http://www.skrenta.com/2007/05/code_is_our_enemy.html redirects to linkedin.com, HTTP 999) | PARTIAL | 148 |
| L1-05.txt | L1-05 | The Best Code is No Code At All | Jeff Atwood | 2007 (page date "30 May 2007"; article:published_time 2007-05-30) | https://blog.codinghorror.com/the-best-code-is-no-code-at-all/ | FULL | 728 |
| L1-06.txt | L1-06 | Source Code Is A Liability, Not An Asset | Eric Lee | 2009 (page date "March 11, 2009"; updated December 14, 2018; "originally posted on my MSDN blog") | https://saintgimp.org/2009/03/11/source-code-is-a-liability-not-an-asset/ | FULL | 951 |
| L2-01-discussion.txt | L2-01-discussion | 8.2.1 Discussion following Mass Produced Software Components (supplementary; not part of the named paper) | Conference participants (Ross, McIlroy, Opler, Perlis, d'Agapeyeff, Endres, Kjeldaas, Kolence, Naur, Gill, Barton, Fraser, Graham, Bemer and others) | 1968 | http://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1968.PDF | not in fetch table | 1816 |
| L2-01.txt | L2-01 | Mass Produced Software Components (section 8.2 of Software Engineering: Report on a conference sponsored by the NATO Science Committee, Garmisch, Germany, 7th to 11th October 1968) | M. D. McIlroy | 1968 (conference 7-11 Oct 1968; report published 1969) | http://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1968.PDF | FULL | 4018 |
| L2-02-dumped-retro.txt | L2-02-dumped-retro | The UNIX Time-sharing System: A Retrospective (the document the dumped URL retro.pdf actually serves; supplementary, NOT the named 1974 paper) | Dennis M. Ritchie (sole author) | 1977 (version presented at the Tenth Hawaii International Conference on the System Sciences, Honolulu, January 1977, per the text's footnote; the text cites July-August 1978 BSTJ papers) | https://web.archive.org/web/2016/https://www.nokia.com/bell-labs/about/dennis-m-ritchie/retro.pdf (Wayback snapshot 20250615233346 of the dumped nokia.com URL, which returns 403 live) | not in fetch table | 9027 |
| L2-02.txt | L2-02 | The UNIX Time-Sharing System | Dennis M. Ritchie and Ken Thompson | 1974 (Communications of the ACM 17(7), July 1974, pp. 365-375) | https://dsf.berkeley.edu/cs262/unix.pdf (electronic version recreated by Eric A. Brewer, UC Berkeley; also https://people.eecs.berkeley.edu/~brewer/cs262/unix.pdf) | FULL | 9458 |
| L2-03-dumped-bowers.txt | L2-03-dumped-bowers | CPAN is 20! (the secondary blog post the dumped URL serves; supplementary, NOT Hietaniemi's announcement) | Neil Bowers | 2015 (posted August 16, 2015) | https://blogs.perl.org/users/neilb/2015/08/cpan-is-20.html | not in fetch table | 391 |
| L2-03.txt | L2-03 | CPAN "private showing" (CPAN.ANNOUNCE; Hietaniemi's pre-launch announcement to perl-packrats; NOT the 26 Oct 1995 comp.lang.perl.announce launch post) | Jarkko Hietaniemi | 1995 (dated 1 August 1995 by Bowers 2015; file Last-Modified 26 Jul 1995) | https://www.cpan.org/misc/CPAN.ANNOUNCE | PARTIAL | 638 |
| L2-04.txt | L2-04 | I've Just Liberated My Modules | Azer Koçulu | 2016 (page date: Mar 23, 2016) | https://azerkoculu.com/posts/i-ve-just-liberated-my-modules | FULL | 233 |
| L2-05.txt | L2-05 | Our Software Dependency Problem | Russ Cox | 2019 (posted 2019-01-23) | https://research.swtch.com/deps | FULL | 5444 |

## secondary/

Title or URL is the `<title>` element (HTML files with a title) or the first non-blank lines (other files; up to 3 lines joined by ` / ` until 40 characters) of each copy, with a URL from the first 12 lines or the canonical link appended when present. Values longer than 200 characters end in `…`.

| file | title or URL as given in its own header or first lines | survey |
|---|---|---|
| `breadth/anthropic-prompting.html` | `Prompting best practices - Claude Platform Docs — URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices` | breadth |
| `breadth/anthropic-prompting.txt` | ` / Copy page / ` | breadth |
| `breadth/atwood-depavoid.html` | `Dependency Avoidance — URL: https://blog.codinghorror.com/dependency-avoidance/` | breadth |
| `breadth/atwood-depavoid.txt` | `Have you ever worked with developers that were` | breadth |
| `breadth/atwood-diseconomies.html` | `Diseconomies of Scale and Lines of Code — URL: https://blog.codinghorror.com/diseconomies-of-scale-and-lines-of-code/` | breadth |
| `breadth/atwood-diseconomies.txt` | `Steve McConnell on / diseconomies of scale / in software development:` | breadth |
| `breadth/atwood-smaller.html` | `Code Smaller — URL: https://blog.codinghorror.com/code-smaller/` | breadth |
| `breadth/atwood-smaller.txt` | `Unless you’ve been living under a rock for the last few years, you’ve probably heard about the game` | breadth |
| `breadth/atwood-wheel.html` | `Don’t Reinvent The Wheel, Unless You Plan on Learning More About Wheels — URL: https://blog.codinghorror.com/dont-reinvent-the-wheel-unless-you-plan-on-learning-more-about-wheels/` | breadth |
| `breadth/atwood-wheel.txt` | `The introduction to / Head First Design Patterns` | breadth |
| `breadth/bentley-knuth-mcilroy-1986-raw.txt` | `by jot1 Be~~tley / with Special Guest Oysters` | breadth |
| `breadth/bentley-knuth-mcilroy-1986.txt` | `by jot1 Be~~tley programming / with Special Guest Oysters` | breadth |
| `breadth/bowers-history.md` | `# CPAN History / ### Version 0.3 / This document is a history of the Comprehensive Perl Archive Network, — URL: http://www.cpan.org` | breadth |
| `breadth/brooks-nsb-raw.txt` | `No Silver Bullet / —Essence and Accident in Software Engineering` | breadth |
| `breadth/brooks-nsb.txt` | `No Silver Bullet / —Essence and Accident in Software Engineering` | breadth |
| `breadth/c2-debt-page.txt` | `WardCunningham posted a video explaining Debt Metaphor (see TechnicalDebt, for example) himself, clearing some confusion in the blogosphere about it. — URL: http://www.youtube.com/watch?v=pqeJFYwnkjE` | breadth |
| `breadth/c2-debt.json` | `{ / "date": "January 22, 2011", / "text": "WardCunningham posted a video explaining Debt Metaphor (see TechnicalDebt, for example) himself, clearing some confusion in the blogosphere about it.\r\n----… — URL: http://www.youtube.com/watch?v=pqeJFYwnkjE` | breadth |
| `breadth/c2-debt.txt` | `This site uses features not available in older browsers.` | breadth |
| `breadth/c2-oopsla92.html` | `<body bgcolor=white> / OOPSLA '92 <br> / Experience Report <P>` | breadth |
| `breadth/c2-oopsla92.txt` | `OOPSLA '92 / Experience Report / The WyCash Portfolio Management System` | breadth |
| `breadth/chm-macpaint.html` | `MacPaint and QuickDraw Source Code - CHM — URL: https://computerhistory.org/blog/macpaint-and-quickdraw-source-code/` | breadth |
| `breadth/chm-macpaint.txt` | `Skip to main content / Home / CHM BLOG` | breadth |
| `breadth/chm-oral-accession.html` | `MacPaint oral history with Bill Atkinson and Andy Hertzfeld - 102658007 - CHM — URL: https://www.computerhistory.org/collections/catalog/102658007` | breadth |
| `breadth/cotroneo-abs.html` | `[2508.21634] Human-Written vs. AI-Generated Code: A Large-Scale Study of Defects, Vulnerabilities, and Complexity — URL: https://arxiv.org/abs/2508.21634` | breadth |
| `breadth/cotroneo-abs.txt` | `Computer Science > Software Engineering / arXiv:2508.21634` | breadth |
| `breadth/cotroneo.txt` | `Human-Written vs. AI-Generated Code: A Large-Scale` | breadth |
| `breadth/demillo-1979.txt` | `Reports and Articles / Social Processes and Proofs of Theorems` | breadth |
| `breadth/dora2024.txt` | `2024 / Accelerate / State of DevOps` | breadth |
| `breadth/equifax-8k-ex99.html` | `Exhibit` | breadth |
| `breadth/equifax-8k-ex99.txt` | `EX-99.1 / 2 / exhibit99120170907.htm` | breadth |
| `breadth/equifax-house.txt` | `U.S. House of Representatives / Committee on Oversight and Government Reform` | breadth |
| `breadth/ewd1305.html` | `E.W. Dijkstra Archive: Answers to questions from students of Software Engineering (EWD1305)` | breadth |
| `breadth/ewd1305.txt` | `EWD 1305 / Answers to questions from students of Software Engineering` | breadth |
| `breadth/ewd340.html` | `E.W.Dijkstra Archive: The Humble Programmer (EWD 340)` | breadth |
| `breadth/ewd340.txt` | `ACM Turing Lecture 1972 / EWD340 / The Humble Programmer` | breadth |
| `breadth/ewd667.html` | `E.W.Dijkstra Archive: On the foolishness of &quot;natural language programming&quot;. (EWD 667)` | breadth |
| `breadth/ewd667.txt` | `EWD 667 / On the foolishness of "natural language programming"` | breadth |
| `breadth/freund-xz.html` | `oss-security - backdoor in upstream xz/liblzma leading to ssh server compromise` | breadth |
| `breadth/freund-xz.txt` | `Products / Openwall GNU/*/Linux / server OS` | breadth |
| `breadth/gabriel-worse.html` | `Rise of Worse Is Better` | breadth |
| `breadth/gabriel-worse.txt` | `The Rise of Worse is Better / Richard P. Gabriel` | breadth |
| `breadth/gitclear-2024.html` | `Coding on Copilot: 2023 Data Suggests Downward Pressure on Code Quality (incl 2024 projections) - GitClear` | breadth |
| `breadth/gitclear-2024.txt` | `Home / » / Measurement and Research` | breadth |
| `breadth/gitclear-2025.html` | `AI Copilot Code Quality: 2025 Data Suggests 4x Growth in Code Clones - GitClear` | breadth |
| `breadth/gitclear-2025.txt` | `Home / » / Measurement and Research` | breadth |
| `breadth/go-proverbs.html` | `Go Proverbs` | breadth |
| `breadth/go-proverbs.txt` | `Go Proverbs / Simple, Poetic, Pithy / Don't communicate by sharing memory, share memory by communicating.` | breadth |
| `breadth/he-cursor-abs.html` | `[2511.04427] Speed at the Cost of Quality: How Cursor AI Increases Short-Term Velocity and Long-Term Complexity in Open-Source Projects — URL: https://arxiv.org/abs/2511.04427` | breadth |
| `breadth/he-cursor-abs.txt` | `Computer Science > Software Engineering / arXiv:2511.04427` | breadth |
| `breadth/he-cursor-v3.html` | `Speed at the Cost of Quality` | breadth |
| `breadth/he-cursor-v3.txt` | `Speed at the Cost of Quality / Conference: / 23rd International Conference on Mining Software Repositories; April 13–14, 2026; Rio de Janeiro, Brazil` | breadth |
| `breadth/lehman-1980.txt` | `PROCEEDINGS OF THE IEEE, VOL. 68, NO. 9 , SEPTEMBER 1980` | breadth |
| `breadth/mcilroy-components.txt` | `Scanned from P. Naur and B. Randell, "Software Engineering, Report on — URL: http://homepages.cs.ncl.ac.uk/brian.randell/NATO.` | breadth |
| `breadth/mcilroy-home.html` | `M. Douglas McIlroy` | breadth |
| `breadth/mcilroy-home.txt` | `M. Douglas McIlroy, Adjunct Professor / Department of Computer Science` | breadth |
| `breadth/mcilroy-pubs.html` | `Publications` | breadth |
| `breadth/naur-theory.txt` | `(file has no non-blank line)` | breadth |
| `breadth/npm-eventstream.html` | `npm Blog Archive: Details about the event-stream incident` | breadth |
| `breadth/npm-eventstream.txt` | `The npm blog has been discontinued. / Updates from the npm team are now published on the` | breadth |
| `breadth/npm-kik-leftpad.html` | `npm Blog Archive: kik, left-pad, and npm` | breadth |
| `breadth/npm-kik-leftpad.txt` | `The npm blog has been discontinued. / Updates from the npm team are now published on the` | breadth |
| `breadth/parnas-aging.txt` | `Software Aging / Invited Plenary Talk / David Lorge Parnas` | breadth |
| `breadth/pike-catv.html` | `UNIX Style, or cat -v Considered Harmful` | breadth |
| `breadth/pike-catv.txt` | `UNIX Style, or cat -v Considered Harmful` | breadth |
| `breadth/pike-kernighan-1984.txt` | `Program design in the UNIX† environment / Rob Pike` | breadth |
| `breadth/pike-less-exp.html` | `command center: Less is exponentially more — URL: https://commandcenter.blogspot.com/2012/06/less-is-exponentially-more.html` | breadth |
| `breadth/pike-less-exp.txt` | `Monday, June 25, 2012 / Less is exponentially more` | breadth |
| `breadth/ritchie-evolution-raw.txt` | `The Evolution of the Unix Time-sharing System*` | breadth |
| `breadth/ritchie-evolution.txt` | `The Evolution of the Unix Time-sharing System*` | breadth |
| `breadth/skrenta-2007-wayback.html` | `Code is our enemy (Skrentablog)` | breadth |
| `breadth/skrenta-2007-wayback.txt` | `Skrentablog / « 'tie' considered harmful / \|` | breadth |
| `breadth/spolsky-never.html` | `Things You Should Never Do, Part I &#8211; Joel on Software — URL: https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/` | breadth |
| `breadth/spolsky-never.txt` | `Top 10 / , / CEO` | breadth |
| `breadth/spolsky-nih.html` | `In Defense of Not-Invented-Here Syndrome &#8211; Joel on Software — URL: https://www.joelonsoftware.com/2001/10/14/in-defense-of-not-invented-here-syndrome/` | breadth |
| `breadth/spolsky-nih.txt` | `CEO / , / News` | breadth |
| `breadth/spracklen-abs.html` | `[2406.10279] We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs — URL: https://arxiv.org/abs/2406.10279` | breadth |
| `breadth/spracklen-abs.txt` | `Computer Science > Software Engineering / arXiv:2406.10279` | breadth |
| `breadth/spracklen-v3.html` | `We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs` | breadth |
| `breadth/spracklen-v3.txt` | `We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs` | breadth |
| `breadth/struts-s2045.html` | `S2-045 - Apache Struts 2 Wiki - Apache Software Foundation — URL: https://cwiki.apache.org/confluence/spaces/WW/pages/68717257/S2-045` | breadth |
| `breadth/struts-s2045.txt` | `A / t / tachments (0)` | breadth |
| `breadth/swtch-bell-labs.html` | `research!rsc: Computing History at Bell Labs` | breadth |
| `breadth/swtch-bell-labs.txt` | `research!rsc / Thoughts and links about programming,` | breadth |
| `breadth/swtch-xz-script.html` | `research!rsc: The xz attack shell script` | breadth |
| `breadth/swtch-xz-script.txt` | `research!rsc / Thoughts and links about programming,` | breadth |
| `breadth/swtch-xz-timeline.html` | `research!rsc: Timeline of the xz open source attack` | breadth |
| `breadth/swtch-xz-timeline.txt` | `research!rsc / Thoughts and links about programming,` | breadth |
| `breadth/thompson-trust-raw.txt` | `TURING AWARD LECTURE / Reflections on Trusting Trust` | breadth |
| `breadth/thompson-trust.txt` | `TURING AWARD LECTURE / Reflections on Trusting Trust` | breadth |
| `breadth/unixhaters.txt` | `The / UNIXHATERS / Handbook` | breadth |
| `breadth/wang-deprecated-abs.html` | `[2406.09834] LLMs Meet Library Evolution: Evaluating Deprecated API Usage in LLM-based Code Completion — URL: https://arxiv.org/abs/2406.09834` | breadth |
| `breadth/wang-deprecated-abs.txt` | `Computer Science > Software Engineering / arXiv:2406.09834` | breadth |
| `breadth/wang-vulndeps-abs.html` | `[2605.06279] Correct Code, Vulnerable Dependencies: A Large Scale Measurement Study of LLM-Specified Library Versions — URL: https://arxiv.org/abs/2605.06279` | breadth |
| `breadth/wang-vulndeps-abs.txt` | `Computer Science > Software Engineering / arXiv:2605.06279` | breadth |
| `breadth/wang-vulndeps.html` | `Correct Code, Vulnerable Dependencies: A Large Scale Measurement Study of LLM-Specified Library Versions` | breadth |
| `breadth/wang-vulndeps.txt` | `Correct Code, Vulnerable Dependencies: A Large Scale Measurement Study of LLM-Specified Library Versions` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/COPYRIGHT.TXT` | `Copyright / This Material is Copyright � 1984 Apple Inc. and is made available only for non-commercial use.` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Angles.a` | `.INCLUDE GrafTypes.text / .FUNC AngleFromSlope,1` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Arcs.a` | `.INCLUDE GRAFTYPES.TEXT / ;-----------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/BitBlt.a` | `.INCLUDE GRAFTYPES.TEXT / ;---------------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Bitmaps.a` | `.INCLUDE GRAFTYPES.TEXT / ;-----------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/DrawArc.a` | `.INCLUDE GRAFTYPES.TEXT / ;-----------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/DrawLine.a` | `.INCLUDE GRAFTYPES.TEXT / ;-----------------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/DrawText.a` | `.INCLUDE GRAFTYPES.TEXT / ;--------------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/FixMove.p` | `PROGRAM FixMove; / { Assembler restrictions require procedure Move to assembled as MQVE. }` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Graf3D.p` | `{$S Graf } / UNIT Graf3D; / { three-dimensional graphics routines layered on top of QuickDraw }` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/GrafAsm.a` | `.INCLUDE GRAFTYPES.TEXT / ;------------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/GrafTypes.a` | `;-----------------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/GrafUtil.p` | `UNIT GrafUtil; / INTERFACE / USES {$U obj:QuickDraw } QuickDraw;` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/LCursor.a` | `.INCLUDE GRAFTYPES.TEXT / ;------------------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Lines.a` | `.INCLUDE GRAFTYPES.TEXT / ;-----------------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Ovals.a` | `.INCLUDE GRAFTYPES.TEXT / ;-----------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PackRgn.a` | `.INCLUDE GRAFTYPES.TEXT / .PROC PACKRGN,3 / .REF SETSIZE` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PicFormat.txt` | `QUICKDRAW INTERNAL PICTURE FORMAT: / OPCODE NAME ADDITIONAL PARAMS TOTAL BYTES` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Pictures.a` | `.INCLUDE GRAFTYPES.TEXT / ;-----------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Polygons.a` | `.INCLUDE GRAFTYPES.TEXT / ;--------------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PutLine.a` | `.INCLUDE GRAFTYPES.TEXT / ;-----------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PutOval.a` | `.INCLUDE GRAFTYPES.TEXT / ;-----------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PutRgn.a` | `.INCLUDE GRAFTYPES.TEXT / .PROC PUTRGN,4 / .REF SETSIZE` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/QDPatch.a` | `; / ; QuickDraw patch program / ;` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/QuickDraw.p` | `UNIT QuickDraw; / { Copyright 1983 Apple Computer Inc. }` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/QuickDraw2.p` | `{ QuickDraw2.text: Implementation part of QuickDraw }` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/QuickGlue.a` | `; File: QuickGlue.TEXT / ;------------------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/RRects.a` | `.INCLUDE GRAFTYPES.TEXT / ;-----------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Rects.a` | `.INCLUDE GRAFTYPES.TEXT / ;-----------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Regions.a` | `.INCLUDE GRAFTYPES.TEXT / ;-----------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/RgnBlt.a` | `.INCLUDE GRAFTYPES.TEXT / ;------------------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/RgnOp.a` | `.INCLUDE GRAFTYPES.TEXT / .FUNC RgnOp,7 / .REF SectScan,DiffScan,UnionScan,XorScan,InsetScan,SetSize` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/SeekRgn.a` | `.INCLUDE GRAFTYPES.TEXT / ;------------------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/SortPoints.a` | `.INCLUDE GRAFTYPES.TEXT / ;------------------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Stretch.a` | `;------------------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/TestGraf.p` | `PROGRAM TestGraf; / { Quick Checkout for QuickDraw }` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Text.a` | `.INCLUDE GRAFTYPES.TEXT / ;---------------------------------------------------------` | breadth |
| `breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Util.a` | `.INCLUDE GRAFTYPES.TEXT / ;-------------------------------------------------------------` | breadth |
| `evidence/atwood-links.html` | `The Best Code is No Code At All — URL: https://blog.codinghorror.com/the-best-code-is-no-code-at-all/` | evidence |
| `evidence/c2-ward-debt.json` | `{ / "date": "January 22, 2011", / "text": "WardCunningham posted a video explaining Debt Metaphor (see TechnicalDebt, for example) himself, clearing some confusion in the blogosphere about it.\r\n----… — URL: http://www.youtube.com/watch?v=pqeJFYwnkjE` | evidence |
| `evidence/c2-ward-debt.txt` | `WardCunningham posted a video explaining Debt Metaphor (see TechnicalDebt, for example) himself, clearing some confusion in the blogosphere about it. — URL: http://www.youtube.com/watch?v=pqeJFYwnkjE` | evidence |
| `evidence/c2try.html` | `404 Not Found` | evidence |
| `evidence/c2try.txt` | `This site uses features not available in older browsers.` | evidence |
| `evidence/chm-quickdraw.html` | `MacPaint and QuickDraw Source Code - CHM — URL: https://computerhistory.org/blog/macpaint-and-quickdraw-source-code/` | evidence |
| `evidence/chm-quickdraw.txt` | `MacPaint and QuickDraw Source Code - CHM` | evidence |
| `evidence/chrome-stable-2010-01-25.html` | `Chrome Releases: Stable Channel Update — URL: https://chromereleases.googleblog.com/2010/01/stable-channel-update_25.html` | evidence |
| `evidence/chrome-stable-2010-01-25.txt` | `The stable channel has been updated to 4.0.249.78 for Windows, and includes the following features and security fixes (since 3.0):` | evidence |
| `evidence/chromium-ext-2009-06.html` | `Chromium Blog: Important Updates for Extension Developers — URL: https://blog.chromium.org/2009/06/important-updates-for-extension.html` | evidence |
| `evidence/chromium-ext-2009-06.txt` | `We're excited to see many people are experimenting with the upcoming extension features of Chrome in the dev channel. We're getting a lot of great feedback and are working hard to bring extensions to …` | evidence |
| `evidence/chromium-multiproc-body.txt` | `Chromium Blog: Multi-process Architecture (Charlie Reis, Thursday, September 11, 2008)` | evidence |
| `evidence/chromium-multiproc.html` | `Chromium Blog: Multi-process Architecture — URL: https://blog.chromium.org/2008/09/multi-process-architecture.html` | evidence |
| `evidence/chromium-multiproc.txt` | `Chromium Blog: Multi-process Architecture` | evidence |
| `evidence/cpan-history.md` | `# CPAN History / ### Version 0.3 / This document is a history of the Comprehensive Perl Archive Network, — URL: http://www.cpan.org` | evidence |
| `evidence/equifax.txt` | `U.S. House of Representatives / Committee on Oversight and Government Reform` | evidence |
| `evidence/ewd249.html` | `404 Not Found` | evidence |
| `evidence/ewd249.txt` | `(file has no non-blank line)` | evidence |
| `evidence/go-proverbs.html` | `Go Proverbs` | evidence |
| `evidence/go-proverbs.txt` | `Go Proverbs / Go Proverbs / Simple, Poetic, Pithy` | evidence |
| `evidence/gpl1.txt` | `GNU GENERAL PUBLIC LICENSE / Version 1, February 1989 — URL: https://fsf.org/` | evidence |
| `evidence/hertzfeld-folklore.html` | `Folklore.org: -2000 Lines Of Code` | evidence |
| `evidence/hertzfeld-folklore.txt` | `Folklore.org: -2000 Lines Of Code / Home \| About Folklore \| Quotes` | evidence |
| `evidence/lapack-notes.html` | `LAPACK RELEASE NOTES` | evidence |
| `evidence/lapack-notes.txt` | `LAPACK RELEASE NOTES / LAPACK RELEASE NOTES` | evidence |
| `evidence/leftpad-index.js` | `'use strict'; / module.exports = leftPad; / var cache = [` | evidence |
| `evidence/nato1969.txt` | `SOFTWARE ENGINEERING TECHNIQUES / Report on a conference sponsored by the` | evidence |
| `evidence/npm-event-stream.html` | `npm Blog Archive: Details about the event-stream incident` | evidence |
| `evidence/npm-event-stream.txt` | `npm Blog Archive: Details about the event-stream incident` | evidence |
| `evidence/npm-kik-leftpad.html` | `npm Blog Archive: kik, left-pad, and npm` | evidence |
| `evidence/npm-kik-leftpad.txt` | `npm Blog Archive: kik, left-pad, and npm` | evidence |
| `evidence/oopsla92.html` | `<body bgcolor=white> / OOPSLA '92 <br> / Experience Report <P>` | evidence |
| `evidence/oopsla92.txt` | `OOPSLA '92 / Experience Report / The WyCash Portfolio Management System` | evidence |
| `evidence/ritchie-cacm-bstj.html` | `BSTJ version of C.ACM Unix paper` | evidence |
| `evidence/ritchie-cacm-bstj.txt` | `BSTJ version of C.ACM Unix paper / The UNIX` | evidence |
| `evidence/ritchie84evolution.txt` | `The Evolution of the Unix Time-sharing System*` | evidence |
| `evidence/shipley-live.html` | `Call Me Fishmeal. — URL: http://blog.wilshipley.com//blog/2007/05/pimp-my-code-part-14-be-inflexible.html` | evidence |
| `evidence/shipley-pmc14.html` | `Call Me Fishmeal.: Pimp My Code, Part 14: Be Inflexible!` | evidence |
| `evidence/shipley-pmc14.txt` | `Call Me Fishmeal.: Pimp My Code, Part 14: Be Inflexible!` | evidence |
| `evidence/skrenta-wayback.html` | `Code is our enemy (Skrentablog)` | evidence |
| `evidence/skrenta-wayback.txt` | `Code is our enemy (Skrentablog) / Skrentablog` | evidence |
| `evidence/snyk-1m.html` | `npm passes the 1 millionth package milestone! What can we learn? \| Snyk — URL: https://snyk.io/blog/npm-passes-the-1-millionth-package-milestone-what-can-we-learn/` | evidence |
| `evidence/snyk-1m.txt` | `npm passes the 1 millionth package milestone! What can we learn? \| Snyk` | evidence |
| `evidence/sqlite-amalg-2019.html` | `The SQLite Amalgamation` | evidence |
| `evidence/sqlite-amalg-2019.txt` | `The SQLite Amalgamation / Small. Fast. Reliable.` | evidence |
| `evidence/sqlite-testing-2019.html` | `How SQLite Is Tested` | evidence |
| `evidence/sqlite-testing-2019.txt` | `How SQLite Is Tested / Small. Fast. Reliable.` | evidence |
| `evidence/sqlite-testing.html` | `How SQLite Is Tested` | evidence |
| `evidence/sqlite-testing.txt` | `How SQLite Is Tested / Small. Fast. Reliable.` | evidence |
| `evidence/struts-s2-032.html` | `S2-032 - Apache Struts 2 Wiki - Apache Software Foundation — URL: https://cwiki.apache.org/confluence/spaces/WW/pages/62693266/S2-032` | evidence |
| `evidence/struts-s2-032.txt` | `S2-032 - Apache Struts 2 Wiki - Apache Software Foundation` | evidence |
| `evidence/struts-s2-057.html` | `S2-057 - Apache Struts 2 Wiki - Apache Software Foundation — URL: https://cwiki.apache.org/confluence/spaces/WW/pages/89068553/S2-057` | evidence |
| `evidence/struts-s2-057.txt` | `S2-057 - Apache Struts 2 Wiki - Apache Software Foundation` | evidence |
| `evidence/ward-debt.html` | `<html> / <head> / <meta charset="utf-8">` | evidence |
| `evidence/ward-debt.txt` | `This site uses features not available in older browsers.` | evidence |
| `evidence/zlib-changelog.txt` | `ChangeLog file for zlib / Changes in 1.3.2 (17 Feb 2026)` | evidence |
| `evidence/lp003/package/.npmignore` | `test / test.js / example` | evidence |
| `evidence/lp003/package/README.md` | `## left-pad / String left pad / ## Install` | evidence |
| `evidence/lp003/package/index.js` | `module.exports = leftpad; / function leftpad (str, len, ch) {` | evidence |
| `evidence/lp003/package/package.json` | `{ / "name": "left-pad", / "version": "0.0.3",` | evidence |

## Not copied

34 binary files under `recon/discovery/` (extensions `.pdf`, `.png`, `.zip`, `.tgz`) are not copied. Origin path, bytes, sha256:

| origin | bytes | sha256 |
|---|---|---|
| `recon/discovery/breadth/bentley-knuth-mcilroy-1986.pdf` | 1298645 | `ed3fc2593dacf5b3ee2fcac8af22b61fcccc8bc87f8448dc92f9ba7f8d59588e` |
| `recon/discovery/breadth/brooks-nsb.pdf` | 266288 | `fcbd318dbaa31c5b14b782b02ae25f53fc8aa33779d18ba1b4f126994c99b9ae` |
| `recon/discovery/breadth/chm-quickdraw.zip` | 166390 | `fd609319e4a530995673440dadf0a6b75fc8322f2b96fec1d37ed890c2275b46` |
| `recon/discovery/breadth/cocomo2-manual.pdf` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `recon/discovery/breadth/cotroneo.pdf` | 339091 | `2abfc7631d0b88f2c732be5379c11f09579dc6f3f8ddf0e7e5a2dd6dd70f8004` |
| `recon/discovery/breadth/demillo-1979.pdf` | 1121423 | `9acf7003e467786e38e783e70493e75d59cdc66b824d2b8fec49fe0570dfb308` |
| `recon/discovery/breadth/dora2024.pdf` | 38970381 | `45a1b62564c603e0e356a951e4553d01eafaa200de801480feed5a4c4685e40e` |
| `recon/discovery/breadth/equifax-house.pdf` | 2545932 | `d59b6463f2c3e197836946e72112e69dcc896a055e900cf0138729192851fc17` |
| `recon/discovery/breadth/lehman-1980.pdf` | 1887238 | `71f1d6793741114ce808080295967b03e902233a3fd03cc8dd0718ae5139da24` |
| `recon/discovery/breadth/naur-theory.pdf` | 908308 | `0bcd908a5862694cd228527edaf7a4b5a1f118da8c7edfaf8ad34c1e5fcbc9c4` |
| `recon/discovery/breadth/parnas-aging.pdf` | 933476 | `5f1f89b966e92367fb44d144ace46f366cff3e88fa84b7346d7147cb17e256b9` |
| `recon/discovery/breadth/pike-kernighan-1984.pdf` | 25998 | `c58e6c8e3cb6c0974720084f819ef0e307292ab78b6162abab4d285c2145f757` |
| `recon/discovery/breadth/ritchie-evolution.pdf` | 30159 | `075482a570140e93720c99f5b49939fb3b78a9b375798ce037c44ff0de3adaab` |
| `recon/discovery/breadth/thompson-trust.pdf` | 225044 | `8ab9d339a2c2781382e6aa4c3c472a94edfcc05d10e3eedf63cbaac9530e9932` |
| `recon/discovery/breadth/unixhaters.pdf` | 3639172 | `ff9c923728d9653e4babdec3b05731543054f932241f267df6232d7a7e1e68ba` |
| `recon/discovery/breadth/naur-pages/p-01.png` | 130439 | `d733477d2a339f0be729bfcb81e37bd5dae0be358a80045bf2538a36b712eb3f` |
| `recon/discovery/breadth/naur-pages/p-02.png` | 175822 | `21858de4879a471cc5cfbfb6307885168b2121fac379cb5332288edc64482d74` |
| `recon/discovery/breadth/naur-pages/p-03.png` | 144029 | `dcde8a3c3ae5d8b6fa23b285d8561c122ba62ce02878de5df4cb16f70be27900` |
| `recon/discovery/breadth/naur-pages/p-04.png` | 171525 | `289be39ce2904e8de70017f31fa1b35476e66ae3b84bbf0869b688ca01391668` |
| `recon/discovery/breadth/naur-pages/p-05.png` | 142640 | `a55157992081df65652f1a3b7fca252752381a28a8a5f24304103948a4ecfd79` |
| `recon/discovery/breadth/naur-pages/p-06.png` | 170352 | `b4d3514e405a3b6507874cd55a01541c44ea6b81b00d50c03e9e9aefd976172a` |
| `recon/discovery/breadth/naur-pages/p-07.png` | 148406 | `cbbecf557e733efdc2f08a032bab2b0277cb3a9590021430b1e618ca573c06a0` |
| `recon/discovery/breadth/naur-pages/p-08.png` | 175932 | `0f162c6150e936c89f41d15e0b0588bb50530bfc6f09aee6341ace7702d2204b` |
| `recon/discovery/breadth/naur-pages/p-09.png` | 156271 | `0c81f3077eb90282cda0c85e5a3be62ddb934413da9ee860b7c00da9f227eec6` |
| `recon/discovery/breadth/naur-pages/p-10.png` | 173850 | `d65d774c7bd5575d0d0abb6a2cacc53c6f784a8650853623749b75842c42f7c5` |
| `recon/discovery/breadth/naur-pages/p-11.png` | 141217 | `232e0cd3bfb49c6016730539406d250d308e34197de950e84a1a299537d318cc` |
| `recon/discovery/breadth/naur-pages/p-12.png` | 147812 | `dd0217184e544df76fbe0bed8316ca0eae6f5e62e60ac53c3824ea928d708bc6` |
| `recon/discovery/breadth/naur-pages/p-13.png` | 137776 | `1dcb6519e8a11550fd71f26e7850b9bdcedca40632423dca4a1caa265df81a87` |
| `recon/discovery/breadth/naur-pages/p-14.png` | 122846 | `3792b35ddfaa05c4c8fe0a2e7fbbfa6608b891e866e3f3d12710ceb29ac38d87` |
| `recon/discovery/evidence/equifax-house-report.pdf` | 2545932 | `d59b6463f2c3e197836946e72112e69dcc896a055e900cf0138729192851fc17` |
| `recon/discovery/evidence/ewd249.pdf` | 2103476 | `77f1ef68c6514f4b2cb577bdb1203ca156e9c12e802c361bebe553613b7c6f43` |
| `recon/discovery/evidence/leftpad-0.0.3.tgz` | 664 | `d074b43a3bfb595c93e5da9eeb58c726a1e547ce358afdbfc0e1db27a20c641d` |
| `recon/discovery/evidence/nato1969.pdf` | 3450000 | `4430584e87ef186cc6ff3b8c5d73a420b2cd2c4a5b05be89e96a09f9a4778122` |
| `recon/discovery/evidence/ritchie84evolution.pdf` | 30159 | `075482a570140e93720c99f5b49939fb3b78a9b375798ce037c44ff0de3adaab` |

## sha256 pairs

Origin and copy hashes are equal in every row.

| destination | origin | sha256 of origin | sha256 of copy |
|---|---|---|---|
| `primary/L1-01.txt` | `recon/sources/L1-01.txt` | `b92c5153013b8bb84a8f40ac1199b1cd711c6fa2bf506da95fcbd9e109cc722c` | `b92c5153013b8bb84a8f40ac1199b1cd711c6fa2bf506da95fcbd9e109cc722c` |
| `primary/L1-02.txt` | `recon/sources/L1-02.txt` | `05bda4e8405205d330d2bae36116696061299b96eea4f9323268fd5259611121` | `05bda4e8405205d330d2bae36116696061299b96eea4f9323268fd5259611121` |
| `primary/L1-03.txt` | `recon/sources/L1-03.txt` | `3ec833b6c3d003b84c857129e3140c5faf701e02230211796bd7ef56e32c728a` | `3ec833b6c3d003b84c857129e3140c5faf701e02230211796bd7ef56e32c728a` |
| `primary/L1-04-full.txt` | `recon/sources/L1-04-full.txt` | `5af707eaa576810bd8d3520e789cbe2ad9a22915ff1291ab652bbb0146923d17` | `5af707eaa576810bd8d3520e789cbe2ad9a22915ff1291ab652bbb0146923d17` |
| `primary/L1-04.txt` | `recon/sources/L1-04.txt` | `7acad9d098059c8278744fca8990665ace802b8ac6bb76463d09219038efe07e` | `7acad9d098059c8278744fca8990665ace802b8ac6bb76463d09219038efe07e` |
| `primary/L1-05.txt` | `recon/sources/L1-05.txt` | `36efb95fc7863f5f6fba9bea0358735ba5881a9b32e942d833d602000d556e01` | `36efb95fc7863f5f6fba9bea0358735ba5881a9b32e942d833d602000d556e01` |
| `primary/L1-06.txt` | `recon/sources/L1-06.txt` | `264e13a48ed1345170433a8f00b7dc177f143c541394097edc137fc07ef51646` | `264e13a48ed1345170433a8f00b7dc177f143c541394097edc137fc07ef51646` |
| `primary/L2-01-discussion.txt` | `recon/sources/L2-01-discussion.txt` | `1e36f16b93243206f52e8d93b079260c6137c0b29bfc60510ca5353c55ad5197` | `1e36f16b93243206f52e8d93b079260c6137c0b29bfc60510ca5353c55ad5197` |
| `primary/L2-01.txt` | `recon/sources/L2-01.txt` | `5ce077691022376c65e8571ec516b651264b7efcfffa7d7ad8490df52a31bd64` | `5ce077691022376c65e8571ec516b651264b7efcfffa7d7ad8490df52a31bd64` |
| `primary/L2-02-dumped-retro.txt` | `recon/sources/L2-02-dumped-retro.txt` | `d3af8a9c01f2a65901e0baa09dacfc38891ae87ce5d06848922ebd96cfc1cd11` | `d3af8a9c01f2a65901e0baa09dacfc38891ae87ce5d06848922ebd96cfc1cd11` |
| `primary/L2-02.txt` | `recon/sources/L2-02.txt` | `75d3f708e167262e653a3df70bdab15b04482dd485204488d5e60237bdc816e7` | `75d3f708e167262e653a3df70bdab15b04482dd485204488d5e60237bdc816e7` |
| `primary/L2-03-dumped-bowers.txt` | `recon/sources/L2-03-dumped-bowers.txt` | `520e2ef02f31564aeea9d049047e7d79ad3e418872735c8f1ec8d0c090041a23` | `520e2ef02f31564aeea9d049047e7d79ad3e418872735c8f1ec8d0c090041a23` |
| `primary/L2-03.txt` | `recon/sources/L2-03.txt` | `9e520b55a2fd93e27635030653ab3401a6c6722a90d49c84d5cec756a53e7f4c` | `9e520b55a2fd93e27635030653ab3401a6c6722a90d49c84d5cec756a53e7f4c` |
| `primary/L2-04.txt` | `recon/sources/L2-04.txt` | `a6836e14b4aa22aa69979e49b790e091f2716a4398418fbf651fb4fa3f164faf` | `a6836e14b4aa22aa69979e49b790e091f2716a4398418fbf651fb4fa3f164faf` |
| `primary/L2-05.txt` | `recon/sources/L2-05.txt` | `abdd1a1ddff95272f4f89cab4c91e8367cd4d476a8ac96b0fa346c45b23b1a9c` | `abdd1a1ddff95272f4f89cab4c91e8367cd4d476a8ac96b0fa346c45b23b1a9c` |
| `secondary/breadth/anthropic-prompting.html` | `recon/discovery/breadth/anthropic-prompting.html` | `af3774e3d70a5f0700d97f36abc6746e7191969cb6bdd521afa6ddd1f073d4e8` | `af3774e3d70a5f0700d97f36abc6746e7191969cb6bdd521afa6ddd1f073d4e8` |
| `secondary/breadth/anthropic-prompting.txt` | `recon/discovery/breadth/anthropic-prompting.txt` | `6c0087c266198905b1eec455fbb12db1f04bc325009d93297fdc7a01dda3f386` | `6c0087c266198905b1eec455fbb12db1f04bc325009d93297fdc7a01dda3f386` |
| `secondary/breadth/atwood-depavoid.html` | `recon/discovery/breadth/atwood-depavoid.html` | `aef590644ca152258361c1c8c743558ab37bece3234383cc74ab2571cab02fcd` | `aef590644ca152258361c1c8c743558ab37bece3234383cc74ab2571cab02fcd` |
| `secondary/breadth/atwood-depavoid.txt` | `recon/discovery/breadth/atwood-depavoid.txt` | `4590cd75ea8f388e92c03b07015109e9af5ad2a8ef1e1ac6b7e2748f8b3701e1` | `4590cd75ea8f388e92c03b07015109e9af5ad2a8ef1e1ac6b7e2748f8b3701e1` |
| `secondary/breadth/atwood-diseconomies.html` | `recon/discovery/breadth/atwood-diseconomies.html` | `f9a940b77b58160594ab09c6c829d781b06ee35a2a35ebd70a033d9c94d99c05` | `f9a940b77b58160594ab09c6c829d781b06ee35a2a35ebd70a033d9c94d99c05` |
| `secondary/breadth/atwood-diseconomies.txt` | `recon/discovery/breadth/atwood-diseconomies.txt` | `3a5216793ed6c97deedb47799ac592b5dcd7f33af37315027803d0002355ca91` | `3a5216793ed6c97deedb47799ac592b5dcd7f33af37315027803d0002355ca91` |
| `secondary/breadth/atwood-smaller.html` | `recon/discovery/breadth/atwood-smaller.html` | `6f61fbef5dd11e26143bf4001791e7cdfc01689efdf6e16185d8281cd0eca71b` | `6f61fbef5dd11e26143bf4001791e7cdfc01689efdf6e16185d8281cd0eca71b` |
| `secondary/breadth/atwood-smaller.txt` | `recon/discovery/breadth/atwood-smaller.txt` | `a2776519bef2e0d55f724eeb3489303342f7f9e0a0c958032df4bbe463aa7170` | `a2776519bef2e0d55f724eeb3489303342f7f9e0a0c958032df4bbe463aa7170` |
| `secondary/breadth/atwood-wheel.html` | `recon/discovery/breadth/atwood-wheel.html` | `eea0320aba93c9cc81c6067b33d9f378eb9bcb1ff9380615ea5761f66d9f9fde` | `eea0320aba93c9cc81c6067b33d9f378eb9bcb1ff9380615ea5761f66d9f9fde` |
| `secondary/breadth/atwood-wheel.txt` | `recon/discovery/breadth/atwood-wheel.txt` | `91f10956fca0e03b712d70ede5c83d0faad26f721143fb97b740274e57289cf4` | `91f10956fca0e03b712d70ede5c83d0faad26f721143fb97b740274e57289cf4` |
| `secondary/breadth/bentley-knuth-mcilroy-1986-raw.txt` | `recon/discovery/breadth/bentley-knuth-mcilroy-1986-raw.txt` | `26b63b8db12e7483b71160ec5b4093ae131dc4688cd03eeb26f4cc8ea73bdbb2` | `26b63b8db12e7483b71160ec5b4093ae131dc4688cd03eeb26f4cc8ea73bdbb2` |
| `secondary/breadth/bentley-knuth-mcilroy-1986.txt` | `recon/discovery/breadth/bentley-knuth-mcilroy-1986.txt` | `e0563aeb4c9b40b04159f0604d1d2ea8fba87e0f2763e5cfa860892ad950e07b` | `e0563aeb4c9b40b04159f0604d1d2ea8fba87e0f2763e5cfa860892ad950e07b` |
| `secondary/breadth/bowers-history.md` | `recon/discovery/breadth/bowers-history.md` | `6cf0980275b9ec5d53ccf0ed37c700953a4621ceabdc8e3c4475a3fa4f2e7bfd` | `6cf0980275b9ec5d53ccf0ed37c700953a4621ceabdc8e3c4475a3fa4f2e7bfd` |
| `secondary/breadth/brooks-nsb-raw.txt` | `recon/discovery/breadth/brooks-nsb-raw.txt` | `060ecdf67a0ad195f172c162b12ed07e5f1307425889c51b23c0e774228da44b` | `060ecdf67a0ad195f172c162b12ed07e5f1307425889c51b23c0e774228da44b` |
| `secondary/breadth/brooks-nsb.txt` | `recon/discovery/breadth/brooks-nsb.txt` | `50b7b5aaf80c1e0cf58608636773d7cc672132137e496f16fab647684a73af6c` | `50b7b5aaf80c1e0cf58608636773d7cc672132137e496f16fab647684a73af6c` |
| `secondary/breadth/c2-debt-page.txt` | `recon/discovery/breadth/c2-debt-page.txt` | `a879502839ff8f402c490c298af75440df3266ce0157a786bc4959255f718bc0` | `a879502839ff8f402c490c298af75440df3266ce0157a786bc4959255f718bc0` |
| `secondary/breadth/c2-debt.json` | `recon/discovery/breadth/c2-debt.json` | `e18b7498340878fee721cfe87022bfe8a681a3cc4db9ac45aea4337e5065cef2` | `e18b7498340878fee721cfe87022bfe8a681a3cc4db9ac45aea4337e5065cef2` |
| `secondary/breadth/c2-debt.txt` | `recon/discovery/breadth/c2-debt.txt` | `2c07f8e923537c795c2bb43833f0dffb7fa2e771a8ca199fb2254d9349ea101e` | `2c07f8e923537c795c2bb43833f0dffb7fa2e771a8ca199fb2254d9349ea101e` |
| `secondary/breadth/c2-oopsla92.html` | `recon/discovery/breadth/c2-oopsla92.html` | `7bb0ebbd6e99b96cb15229de39e810dd7644ea56a755a22668663f68b09de5d5` | `7bb0ebbd6e99b96cb15229de39e810dd7644ea56a755a22668663f68b09de5d5` |
| `secondary/breadth/c2-oopsla92.txt` | `recon/discovery/breadth/c2-oopsla92.txt` | `5a3777caa8ddc83638697e5b4d1dba62312095466eb5022256c440117982a291` | `5a3777caa8ddc83638697e5b4d1dba62312095466eb5022256c440117982a291` |
| `secondary/breadth/chm-macpaint.html` | `recon/discovery/breadth/chm-macpaint.html` | `731cbd5a4adc729ab96023ba9bd9af420c921f7d7c01c76bc21b667c2a47b1f7` | `731cbd5a4adc729ab96023ba9bd9af420c921f7d7c01c76bc21b667c2a47b1f7` |
| `secondary/breadth/chm-macpaint.txt` | `recon/discovery/breadth/chm-macpaint.txt` | `e9e39319672d6119a38e83f6a53507e131ea336f08ffd5c97576154a3409e801` | `e9e39319672d6119a38e83f6a53507e131ea336f08ffd5c97576154a3409e801` |
| `secondary/breadth/chm-oral-accession.html` | `recon/discovery/breadth/chm-oral-accession.html` | `54d1ca059c5cd68d529d877b9f8d7fb655985931b23c6df40ec8378e3ad3835d` | `54d1ca059c5cd68d529d877b9f8d7fb655985931b23c6df40ec8378e3ad3835d` |
| `secondary/breadth/cotroneo-abs.html` | `recon/discovery/breadth/cotroneo-abs.html` | `ffca67f6528aa5477e524db0e68aabb6c48ba65cebd43faae17caf468f404a8d` | `ffca67f6528aa5477e524db0e68aabb6c48ba65cebd43faae17caf468f404a8d` |
| `secondary/breadth/cotroneo-abs.txt` | `recon/discovery/breadth/cotroneo-abs.txt` | `999d595261e9d1620da6d5e79c772cfb6db3a4f7a793eed74fdfa425d1fa8e1e` | `999d595261e9d1620da6d5e79c772cfb6db3a4f7a793eed74fdfa425d1fa8e1e` |
| `secondary/breadth/cotroneo.txt` | `recon/discovery/breadth/cotroneo.txt` | `e6d962c7956943ea211b23e4a370fd35276796c6ba17c38245cd3ae57ec2be74` | `e6d962c7956943ea211b23e4a370fd35276796c6ba17c38245cd3ae57ec2be74` |
| `secondary/breadth/demillo-1979.txt` | `recon/discovery/breadth/demillo-1979.txt` | `9cfcc499f04e48a68e9c9405460ab3fa8f91b303a92a0711cbac36a0c32217c1` | `9cfcc499f04e48a68e9c9405460ab3fa8f91b303a92a0711cbac36a0c32217c1` |
| `secondary/breadth/dora2024.txt` | `recon/discovery/breadth/dora2024.txt` | `e86195bc55a277b8614e4015891321ff42120c01d152e447f9bbbe0017c8e8d3` | `e86195bc55a277b8614e4015891321ff42120c01d152e447f9bbbe0017c8e8d3` |
| `secondary/breadth/equifax-8k-ex99.html` | `recon/discovery/breadth/equifax-8k-ex99.html` | `c632d7e4378aa68d535ebade0ce7e9588d0192d13b581c3fc51abd94f5a84333` | `c632d7e4378aa68d535ebade0ce7e9588d0192d13b581c3fc51abd94f5a84333` |
| `secondary/breadth/equifax-8k-ex99.txt` | `recon/discovery/breadth/equifax-8k-ex99.txt` | `8f687d41e7ab00577d2df90ebd56ecffefb3f3affd360b9d61064bf030fc5a1c` | `8f687d41e7ab00577d2df90ebd56ecffefb3f3affd360b9d61064bf030fc5a1c` |
| `secondary/breadth/equifax-house.txt` | `recon/discovery/breadth/equifax-house.txt` | `47b9753e8d343be9f6f041fb86fed53be7c1dcd06c41819fc5ef7834450241b3` | `47b9753e8d343be9f6f041fb86fed53be7c1dcd06c41819fc5ef7834450241b3` |
| `secondary/breadth/ewd1305.html` | `recon/discovery/breadth/ewd1305.html` | `53a9614acd77e86555d6c02fdde3de11c96314e3c0e67e052223175dba92cb59` | `53a9614acd77e86555d6c02fdde3de11c96314e3c0e67e052223175dba92cb59` |
| `secondary/breadth/ewd1305.txt` | `recon/discovery/breadth/ewd1305.txt` | `00899adb57db72cba891c7ef2c110b0a26938351f482260b9a58e954ae5338b5` | `00899adb57db72cba891c7ef2c110b0a26938351f482260b9a58e954ae5338b5` |
| `secondary/breadth/ewd340.html` | `recon/discovery/breadth/ewd340.html` | `320abd9a7bf81feb99577b1e582b6b0a53f11045f95a0d33a81b8731095a392d` | `320abd9a7bf81feb99577b1e582b6b0a53f11045f95a0d33a81b8731095a392d` |
| `secondary/breadth/ewd340.txt` | `recon/discovery/breadth/ewd340.txt` | `f8ad124524c0d23da4ba413c7159f868c3d18f1c496357d30cbd6e1741cccaa7` | `f8ad124524c0d23da4ba413c7159f868c3d18f1c496357d30cbd6e1741cccaa7` |
| `secondary/breadth/ewd667.html` | `recon/discovery/breadth/ewd667.html` | `d7b7faf1aa3ba37163485d35852eada27296288da1b3968f0f75bc407c965735` | `d7b7faf1aa3ba37163485d35852eada27296288da1b3968f0f75bc407c965735` |
| `secondary/breadth/ewd667.txt` | `recon/discovery/breadth/ewd667.txt` | `3e2e67b2ca7ec9de5a16b17f2b37a7cb283e7a5cc807c679a72ea57de70ee679` | `3e2e67b2ca7ec9de5a16b17f2b37a7cb283e7a5cc807c679a72ea57de70ee679` |
| `secondary/breadth/freund-xz.html` | `recon/discovery/breadth/freund-xz.html` | `1a117fd0cac898fcad8e62698e3849c8644cb281cd4a2a1850b4daabb4e13bfb` | `1a117fd0cac898fcad8e62698e3849c8644cb281cd4a2a1850b4daabb4e13bfb` |
| `secondary/breadth/freund-xz.txt` | `recon/discovery/breadth/freund-xz.txt` | `b9a65aa7abcb0dbf0a7a26f7d2c6698d88fc6d96913a5bc92e0814660773c4c7` | `b9a65aa7abcb0dbf0a7a26f7d2c6698d88fc6d96913a5bc92e0814660773c4c7` |
| `secondary/breadth/gabriel-worse.html` | `recon/discovery/breadth/gabriel-worse.html` | `2103391d2eda6a4a2d8f11483b040ceea4fa4eb449e8fb88c09f21d880c7653f` | `2103391d2eda6a4a2d8f11483b040ceea4fa4eb449e8fb88c09f21d880c7653f` |
| `secondary/breadth/gabriel-worse.txt` | `recon/discovery/breadth/gabriel-worse.txt` | `77034bdef3f134e27ff178263a4af47722c3d04fc83a563e36b021357732e15c` | `77034bdef3f134e27ff178263a4af47722c3d04fc83a563e36b021357732e15c` |
| `secondary/breadth/gitclear-2024.html` | `recon/discovery/breadth/gitclear-2024.html` | `b9dd90ad757ecf178274207febdabb10a49cb0f676cb52ed0f2526c2a1689727` | `b9dd90ad757ecf178274207febdabb10a49cb0f676cb52ed0f2526c2a1689727` |
| `secondary/breadth/gitclear-2024.txt` | `recon/discovery/breadth/gitclear-2024.txt` | `6ce86d1dc98842d4c96055bf5bb8bb11b07a06b4b17c3bb064c9a8217312598f` | `6ce86d1dc98842d4c96055bf5bb8bb11b07a06b4b17c3bb064c9a8217312598f` |
| `secondary/breadth/gitclear-2025.html` | `recon/discovery/breadth/gitclear-2025.html` | `7f3f8304bb8abd1fe335a6922cd194ee9b39464bcf7d5ef80c93cf61ee445729` | `7f3f8304bb8abd1fe335a6922cd194ee9b39464bcf7d5ef80c93cf61ee445729` |
| `secondary/breadth/gitclear-2025.txt` | `recon/discovery/breadth/gitclear-2025.txt` | `25949e2d7bf2030c0d660f6c1245140364f66a2b71f8ea55c5d10942e0aabc90` | `25949e2d7bf2030c0d660f6c1245140364f66a2b71f8ea55c5d10942e0aabc90` |
| `secondary/breadth/go-proverbs.html` | `recon/discovery/breadth/go-proverbs.html` | `ea52bf96684c527a9c0cf6c25f9bd6d1aa60245e26151eaba2ea46c1abff4949` | `ea52bf96684c527a9c0cf6c25f9bd6d1aa60245e26151eaba2ea46c1abff4949` |
| `secondary/breadth/go-proverbs.txt` | `recon/discovery/breadth/go-proverbs.txt` | `937973aeea6b8959ad891ab88feaff93346b2b599522664315c9f5139e884049` | `937973aeea6b8959ad891ab88feaff93346b2b599522664315c9f5139e884049` |
| `secondary/breadth/he-cursor-abs.html` | `recon/discovery/breadth/he-cursor-abs.html` | `f08ac4e28b16a8ff3eaf1f3cfb600b8e4c7bcfbdcf6860c593196a8fdeccb53e` | `f08ac4e28b16a8ff3eaf1f3cfb600b8e4c7bcfbdcf6860c593196a8fdeccb53e` |
| `secondary/breadth/he-cursor-abs.txt` | `recon/discovery/breadth/he-cursor-abs.txt` | `63d41b44be9fa3d09ff4be630e89db4169accb5b72dd5fca7867c2b5401d7bad` | `63d41b44be9fa3d09ff4be630e89db4169accb5b72dd5fca7867c2b5401d7bad` |
| `secondary/breadth/he-cursor-v3.html` | `recon/discovery/breadth/he-cursor-v3.html` | `e3bc197278793687df93cfcd74cde84e9c38faa6fd09f0bfcf5c1561eb37edc1` | `e3bc197278793687df93cfcd74cde84e9c38faa6fd09f0bfcf5c1561eb37edc1` |
| `secondary/breadth/he-cursor-v3.txt` | `recon/discovery/breadth/he-cursor-v3.txt` | `b2dccd1efe96fff9bfaed5037d0014f7dadb10f0666e91e06d0b5c89bc1a4151` | `b2dccd1efe96fff9bfaed5037d0014f7dadb10f0666e91e06d0b5c89bc1a4151` |
| `secondary/breadth/lehman-1980.txt` | `recon/discovery/breadth/lehman-1980.txt` | `d618c825c0ab4d3f3f2aff49227c3b5b911e72f6bd8f6da160e5496c67bd0c05` | `d618c825c0ab4d3f3f2aff49227c3b5b911e72f6bd8f6da160e5496c67bd0c05` |
| `secondary/breadth/mcilroy-components.txt` | `recon/discovery/breadth/mcilroy-components.txt` | `a02a35d461cd9ec0bf633bcec9da6664a53a2a205d5e955ab5ed0461b802411e` | `a02a35d461cd9ec0bf633bcec9da6664a53a2a205d5e955ab5ed0461b802411e` |
| `secondary/breadth/mcilroy-home.html` | `recon/discovery/breadth/mcilroy-home.html` | `7b83d4ff72a7661a676a959c859de708d4371b5bdcb10793287496da84bd8a54` | `7b83d4ff72a7661a676a959c859de708d4371b5bdcb10793287496da84bd8a54` |
| `secondary/breadth/mcilroy-home.txt` | `recon/discovery/breadth/mcilroy-home.txt` | `6dfae9b03390a72ed4e5dee063c5257b311b28c6594a6c752602871b9caa23bf` | `6dfae9b03390a72ed4e5dee063c5257b311b28c6594a6c752602871b9caa23bf` |
| `secondary/breadth/mcilroy-pubs.html` | `recon/discovery/breadth/mcilroy-pubs.html` | `6268368f74192d84fa2d01b3c2299541c3f38cce9e8e1bb3696ad0c2addc80e1` | `6268368f74192d84fa2d01b3c2299541c3f38cce9e8e1bb3696ad0c2addc80e1` |
| `secondary/breadth/naur-theory.txt` | `recon/discovery/breadth/naur-theory.txt` | `bac73e8e5d0502cae3490d5e2a0617d2a437fb20599903f18494f207e4f80cdc` | `bac73e8e5d0502cae3490d5e2a0617d2a437fb20599903f18494f207e4f80cdc` |
| `secondary/breadth/npm-eventstream.html` | `recon/discovery/breadth/npm-eventstream.html` | `0385796be8013bde14a50175fb4e3aa2b9f1fb0bad6524550a269578b6660f98` | `0385796be8013bde14a50175fb4e3aa2b9f1fb0bad6524550a269578b6660f98` |
| `secondary/breadth/npm-eventstream.txt` | `recon/discovery/breadth/npm-eventstream.txt` | `942f715167b1b8a01c03b6cacd105a1386e020ed1d58ecb0b606096fc1efc6e2` | `942f715167b1b8a01c03b6cacd105a1386e020ed1d58ecb0b606096fc1efc6e2` |
| `secondary/breadth/npm-kik-leftpad.html` | `recon/discovery/breadth/npm-kik-leftpad.html` | `c8c7f13a9b419cb6a19a70a8103b869a04c19322174ba8456173af56c54949c3` | `c8c7f13a9b419cb6a19a70a8103b869a04c19322174ba8456173af56c54949c3` |
| `secondary/breadth/npm-kik-leftpad.txt` | `recon/discovery/breadth/npm-kik-leftpad.txt` | `f6d8ad5d2f152d9e14971ef48ac45b50a7e1d07fa891177957825c97750e886b` | `f6d8ad5d2f152d9e14971ef48ac45b50a7e1d07fa891177957825c97750e886b` |
| `secondary/breadth/parnas-aging.txt` | `recon/discovery/breadth/parnas-aging.txt` | `1f0bc0416fcc831ba17201744de0193d6a116d29c741557c84f45ae759c611d6` | `1f0bc0416fcc831ba17201744de0193d6a116d29c741557c84f45ae759c611d6` |
| `secondary/breadth/pike-catv.html` | `recon/discovery/breadth/pike-catv.html` | `2f8648f1ea41ae78a2d8cf868f1d2c7f1a3f785f44d5689ee2a4fd4df95c34b9` | `2f8648f1ea41ae78a2d8cf868f1d2c7f1a3f785f44d5689ee2a4fd4df95c34b9` |
| `secondary/breadth/pike-catv.txt` | `recon/discovery/breadth/pike-catv.txt` | `38e24199be4bc571747317f778bc2924e74c99a044fb2a863e94ba0f5302ccbe` | `38e24199be4bc571747317f778bc2924e74c99a044fb2a863e94ba0f5302ccbe` |
| `secondary/breadth/pike-kernighan-1984.txt` | `recon/discovery/breadth/pike-kernighan-1984.txt` | `600b85ab599e35dfd9bc848a989201afa0df0e20580dbe517225f94e04ca1a20` | `600b85ab599e35dfd9bc848a989201afa0df0e20580dbe517225f94e04ca1a20` |
| `secondary/breadth/pike-less-exp.html` | `recon/discovery/breadth/pike-less-exp.html` | `23ea330555f03883a5ca35049c1ee055628c80bbd06944eb2d20c9934b882cda` | `23ea330555f03883a5ca35049c1ee055628c80bbd06944eb2d20c9934b882cda` |
| `secondary/breadth/pike-less-exp.txt` | `recon/discovery/breadth/pike-less-exp.txt` | `a28ce16d38e063c22169d612a92dbfb57fd6ee19e8ba3e2e335407b4a909c9fc` | `a28ce16d38e063c22169d612a92dbfb57fd6ee19e8ba3e2e335407b4a909c9fc` |
| `secondary/breadth/ritchie-evolution-raw.txt` | `recon/discovery/breadth/ritchie-evolution-raw.txt` | `97101bf7bc19fdaf406b0cc96892cffec5d8b2bef09e766e25a37dea0da14bdd` | `97101bf7bc19fdaf406b0cc96892cffec5d8b2bef09e766e25a37dea0da14bdd` |
| `secondary/breadth/ritchie-evolution.txt` | `recon/discovery/breadth/ritchie-evolution.txt` | `d5f2a8e0819a81e9cae440679873f4b30c8158ee8c815cd7accf7f54ff5e4c25` | `d5f2a8e0819a81e9cae440679873f4b30c8158ee8c815cd7accf7f54ff5e4c25` |
| `secondary/breadth/skrenta-2007-wayback.html` | `recon/discovery/breadth/skrenta-2007-wayback.html` | `44c9bc7d96231bfa115ff5bc10dfe7cf977f81dff0b7c0ac6d37653d55a67896` | `44c9bc7d96231bfa115ff5bc10dfe7cf977f81dff0b7c0ac6d37653d55a67896` |
| `secondary/breadth/skrenta-2007-wayback.txt` | `recon/discovery/breadth/skrenta-2007-wayback.txt` | `be14efe293dd57a64457b611d4a5b3ad21b232f9a0e6eae552352bcec617911e` | `be14efe293dd57a64457b611d4a5b3ad21b232f9a0e6eae552352bcec617911e` |
| `secondary/breadth/spolsky-never.html` | `recon/discovery/breadth/spolsky-never.html` | `6a29fa6b2e9caeadd1c30b9ae5a0e7daedc14ad6a2a741c599d84955750072a6` | `6a29fa6b2e9caeadd1c30b9ae5a0e7daedc14ad6a2a741c599d84955750072a6` |
| `secondary/breadth/spolsky-never.txt` | `recon/discovery/breadth/spolsky-never.txt` | `41ebc132c75f40ef61140e80fc39c37e570a0f30f49c062fcf12354e2870a891` | `41ebc132c75f40ef61140e80fc39c37e570a0f30f49c062fcf12354e2870a891` |
| `secondary/breadth/spolsky-nih.html` | `recon/discovery/breadth/spolsky-nih.html` | `7a03f907fe16fba475e01648882423639bcb6178f5f9b4f0618f5674c8c85cd0` | `7a03f907fe16fba475e01648882423639bcb6178f5f9b4f0618f5674c8c85cd0` |
| `secondary/breadth/spolsky-nih.txt` | `recon/discovery/breadth/spolsky-nih.txt` | `6d0bedd7881c37309c8e7585f206bb71cd74b11b566efc257e87dba80966f1e5` | `6d0bedd7881c37309c8e7585f206bb71cd74b11b566efc257e87dba80966f1e5` |
| `secondary/breadth/spracklen-abs.html` | `recon/discovery/breadth/spracklen-abs.html` | `0c6b4e908b5433022768122f68591f7127bf4003e27e3920fd76c201be26bf5c` | `0c6b4e908b5433022768122f68591f7127bf4003e27e3920fd76c201be26bf5c` |
| `secondary/breadth/spracklen-abs.txt` | `recon/discovery/breadth/spracklen-abs.txt` | `86ba5a55ebed6868731c76372ba36b376a7966ef78c5c05a7163117d2a12ecd4` | `86ba5a55ebed6868731c76372ba36b376a7966ef78c5c05a7163117d2a12ecd4` |
| `secondary/breadth/spracklen-v3.html` | `recon/discovery/breadth/spracklen-v3.html` | `a93adde20ad8a3ddd5b8fe3fa28a4ee51ef672a677eaa23283413e67a5f24f5e` | `a93adde20ad8a3ddd5b8fe3fa28a4ee51ef672a677eaa23283413e67a5f24f5e` |
| `secondary/breadth/spracklen-v3.txt` | `recon/discovery/breadth/spracklen-v3.txt` | `e14e77883ed34eeae84913644e145c68c0c23c005c3eb7fcfaaaff1a106466a0` | `e14e77883ed34eeae84913644e145c68c0c23c005c3eb7fcfaaaff1a106466a0` |
| `secondary/breadth/struts-s2045.html` | `recon/discovery/breadth/struts-s2045.html` | `401aac18aebbf4a75b6daf05090d4ed5aebac417897fa95cd0f4ecb04e27b67f` | `401aac18aebbf4a75b6daf05090d4ed5aebac417897fa95cd0f4ecb04e27b67f` |
| `secondary/breadth/struts-s2045.txt` | `recon/discovery/breadth/struts-s2045.txt` | `283f4241221020ae7601d92470fc754e886c33e0020146f74ab2925523fb9fd0` | `283f4241221020ae7601d92470fc754e886c33e0020146f74ab2925523fb9fd0` |
| `secondary/breadth/swtch-bell-labs.html` | `recon/discovery/breadth/swtch-bell-labs.html` | `75db92bf065aa33f755ff6afc5d6f4f825ffee77a52b3994bd06354785e0c3b5` | `75db92bf065aa33f755ff6afc5d6f4f825ffee77a52b3994bd06354785e0c3b5` |
| `secondary/breadth/swtch-bell-labs.txt` | `recon/discovery/breadth/swtch-bell-labs.txt` | `79185259c0c820247535353e1527c8b578783ee07cfbb3e679e7886548de2e9f` | `79185259c0c820247535353e1527c8b578783ee07cfbb3e679e7886548de2e9f` |
| `secondary/breadth/swtch-xz-script.html` | `recon/discovery/breadth/swtch-xz-script.html` | `7b8e640e083addb05399f6540a6aee43b3b0f1aeb1b6549dd9cf59a7d3c5a0e5` | `7b8e640e083addb05399f6540a6aee43b3b0f1aeb1b6549dd9cf59a7d3c5a0e5` |
| `secondary/breadth/swtch-xz-script.txt` | `recon/discovery/breadth/swtch-xz-script.txt` | `0bd0db8227822d2456ab4d0e626137b56dfa5ac52d3c32270c339429b215931b` | `0bd0db8227822d2456ab4d0e626137b56dfa5ac52d3c32270c339429b215931b` |
| `secondary/breadth/swtch-xz-timeline.html` | `recon/discovery/breadth/swtch-xz-timeline.html` | `2fa9c2a7193c17fcc2eb84eb07fc5b9252b2e5bb6be3be6e361f68b34fde15c6` | `2fa9c2a7193c17fcc2eb84eb07fc5b9252b2e5bb6be3be6e361f68b34fde15c6` |
| `secondary/breadth/swtch-xz-timeline.txt` | `recon/discovery/breadth/swtch-xz-timeline.txt` | `a6055c273a0f044d1aec7e53d5e3b4ee50c99ba32a2bde49715f207d99e4284d` | `a6055c273a0f044d1aec7e53d5e3b4ee50c99ba32a2bde49715f207d99e4284d` |
| `secondary/breadth/thompson-trust-raw.txt` | `recon/discovery/breadth/thompson-trust-raw.txt` | `e9b150a65e5c148397908772c877f64e16bf08ee18b641a497d198bd6ec7d1bc` | `e9b150a65e5c148397908772c877f64e16bf08ee18b641a497d198bd6ec7d1bc` |
| `secondary/breadth/thompson-trust.txt` | `recon/discovery/breadth/thompson-trust.txt` | `1c4cc1a9d65810143357475c884db7de866e6068fe711f8128cf936c95891f3b` | `1c4cc1a9d65810143357475c884db7de866e6068fe711f8128cf936c95891f3b` |
| `secondary/breadth/unixhaters.txt` | `recon/discovery/breadth/unixhaters.txt` | `b8b23685e1ed22c0c5e1975fda65a2a0a413facd55be8df5c4b5e6532ac81c81` | `b8b23685e1ed22c0c5e1975fda65a2a0a413facd55be8df5c4b5e6532ac81c81` |
| `secondary/breadth/wang-deprecated-abs.html` | `recon/discovery/breadth/wang-deprecated-abs.html` | `19130dbc249fdfaa01c32947a8dfcd7591345ab6fea2b4c9f38f4aba9c3f7930` | `19130dbc249fdfaa01c32947a8dfcd7591345ab6fea2b4c9f38f4aba9c3f7930` |
| `secondary/breadth/wang-deprecated-abs.txt` | `recon/discovery/breadth/wang-deprecated-abs.txt` | `b51ae6d1b392412e69701a3dd94eb6717afcd493f80a646d52122dae31d17fe0` | `b51ae6d1b392412e69701a3dd94eb6717afcd493f80a646d52122dae31d17fe0` |
| `secondary/breadth/wang-vulndeps-abs.html` | `recon/discovery/breadth/wang-vulndeps-abs.html` | `f07373ac3fab7a3978a9a647c6998505d470cba7b2f4c179c3487c93f26b63de` | `f07373ac3fab7a3978a9a647c6998505d470cba7b2f4c179c3487c93f26b63de` |
| `secondary/breadth/wang-vulndeps-abs.txt` | `recon/discovery/breadth/wang-vulndeps-abs.txt` | `393c10c0c40cfae2b66fee0e9f87c11e44a815dc58fd1c5c1d9bdec8b52706bf` | `393c10c0c40cfae2b66fee0e9f87c11e44a815dc58fd1c5c1d9bdec8b52706bf` |
| `secondary/breadth/wang-vulndeps.html` | `recon/discovery/breadth/wang-vulndeps.html` | `2cba4f2c88d9a7b78059a2fd56c1c44d56fda5a7d31f1613836070ec93223c43` | `2cba4f2c88d9a7b78059a2fd56c1c44d56fda5a7d31f1613836070ec93223c43` |
| `secondary/breadth/wang-vulndeps.txt` | `recon/discovery/breadth/wang-vulndeps.txt` | `1377fe33f9d8ae6c7ec564b14b11149c7f1b772c7aca5175badc83e5f39c8b97` | `1377fe33f9d8ae6c7ec564b14b11149c7f1b772c7aca5175badc83e5f39c8b97` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/COPYRIGHT.TXT` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/COPYRIGHT.TXT` | `4d7a98ac9439bfb5ca9cd48928f62f9354de5073b1dfe8f14266015d57a19aaa` | `4d7a98ac9439bfb5ca9cd48928f62f9354de5073b1dfe8f14266015d57a19aaa` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Angles.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Angles.a` | `4ccfa8521f5f20fb34145804988df4a93d6970e906015d4cb9fb150d4e080922` | `4ccfa8521f5f20fb34145804988df4a93d6970e906015d4cb9fb150d4e080922` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Arcs.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Arcs.a` | `f37e4219669e8328dd44838382b106188d8e75e307f8288ad07421dee16abf50` | `f37e4219669e8328dd44838382b106188d8e75e307f8288ad07421dee16abf50` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/BitBlt.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/BitBlt.a` | `331e8a5299c646fc5bde0dc7a6facff514230bbb061678b2e02514f9702aa0e8` | `331e8a5299c646fc5bde0dc7a6facff514230bbb061678b2e02514f9702aa0e8` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Bitmaps.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Bitmaps.a` | `745f6e7fd58de49e41e5644df319363959cb9b5689dee9a3193329678a53647e` | `745f6e7fd58de49e41e5644df319363959cb9b5689dee9a3193329678a53647e` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/DrawArc.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/DrawArc.a` | `f4a46b9d9435103c0eb71e732a73c84da6ea562b6c8d776da00bde86d4c04d3d` | `f4a46b9d9435103c0eb71e732a73c84da6ea562b6c8d776da00bde86d4c04d3d` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/DrawLine.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/DrawLine.a` | `1f8495f78b975c36c446faa231e8151d85048bdcc91a76260b07f4e9f9dd78ae` | `1f8495f78b975c36c446faa231e8151d85048bdcc91a76260b07f4e9f9dd78ae` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/DrawText.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/DrawText.a` | `d8277a573475e26f8483201728a776cb5de8207d893757021f2189e469ceb753` | `d8277a573475e26f8483201728a776cb5de8207d893757021f2189e469ceb753` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/FixMove.p` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/FixMove.p` | `6177e69739436e7b3f0916625f53c62562d787474603519daa579293bfc7d9e2` | `6177e69739436e7b3f0916625f53c62562d787474603519daa579293bfc7d9e2` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Graf3D.p` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Graf3D.p` | `6148d0c4a6a8730a773af0279932f3c0844f52a2e35c60a508da0c8d391b6d54` | `6148d0c4a6a8730a773af0279932f3c0844f52a2e35c60a508da0c8d391b6d54` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/GrafAsm.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/GrafAsm.a` | `91dddce61f4f4d8fe543ff6685f93674a443ebd32d1508536e5a6d801c249b0f` | `91dddce61f4f4d8fe543ff6685f93674a443ebd32d1508536e5a6d801c249b0f` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/GrafTypes.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/GrafTypes.a` | `2d621b5233dd1f61c47e00514bf572c99b9338b66232b92aec04cbc4921e974e` | `2d621b5233dd1f61c47e00514bf572c99b9338b66232b92aec04cbc4921e974e` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/GrafUtil.p` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/GrafUtil.p` | `a0fb83167ff50b34a65ee85456701f12c448f54d79bbe925e3094465988bc65c` | `a0fb83167ff50b34a65ee85456701f12c448f54d79bbe925e3094465988bc65c` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/LCursor.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/LCursor.a` | `be67d3132661697ca49d56e05490b5e4e0d5b49039c948c3bda8dce322f17a6d` | `be67d3132661697ca49d56e05490b5e4e0d5b49039c948c3bda8dce322f17a6d` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Lines.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Lines.a` | `8799cb28ea9405f61ae3880af67ba4cc5660914640242c4a9403fc2d668db89b` | `8799cb28ea9405f61ae3880af67ba4cc5660914640242c4a9403fc2d668db89b` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Ovals.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Ovals.a` | `770ffa8d74854b61a3860b1f46ba4068c1efc7d325589807bf408d5d329cfb45` | `770ffa8d74854b61a3860b1f46ba4068c1efc7d325589807bf408d5d329cfb45` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PackRgn.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PackRgn.a` | `67a0efddbd84ef5beaeb2adddfe53f0dbe19b4ac6b21dd68820226e7605b0727` | `67a0efddbd84ef5beaeb2adddfe53f0dbe19b4ac6b21dd68820226e7605b0727` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PicFormat.txt` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PicFormat.txt` | `5132d72616e042e24de35c5affaa34e2b8f8f76e8eb827e7e44653911808822c` | `5132d72616e042e24de35c5affaa34e2b8f8f76e8eb827e7e44653911808822c` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Pictures.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Pictures.a` | `cf5ca90eb0b6435790498b7ed96ffd743457e08ea488325c1137966469789040` | `cf5ca90eb0b6435790498b7ed96ffd743457e08ea488325c1137966469789040` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Polygons.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Polygons.a` | `dc7666c1566c44329f135c8a3d534ef6487468ee85c84268dc600ef0d1befcb4` | `dc7666c1566c44329f135c8a3d534ef6487468ee85c84268dc600ef0d1befcb4` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PutLine.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PutLine.a` | `9c3a42e79c9fc9f3c636a205a314a24192a862222eb6e6e9b18a89ac063f17e4` | `9c3a42e79c9fc9f3c636a205a314a24192a862222eb6e6e9b18a89ac063f17e4` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PutOval.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PutOval.a` | `71a1d6370e73dbb9a810121d3583194a3aa058f7460d66ebffde7a3d152cdca9` | `71a1d6370e73dbb9a810121d3583194a3aa058f7460d66ebffde7a3d152cdca9` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PutRgn.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/PutRgn.a` | `a5fa7c115e648b9d6ecda08900538d439bbe0bf9cf7fd3b8a54d9add2dccb076` | `a5fa7c115e648b9d6ecda08900538d439bbe0bf9cf7fd3b8a54d9add2dccb076` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/QDPatch.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/QDPatch.a` | `b107411e6c0ae48bcbe1d3f3bad54ba933bb8afdc1e0df4dc5956a2ea9f36758` | `b107411e6c0ae48bcbe1d3f3bad54ba933bb8afdc1e0df4dc5956a2ea9f36758` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/QuickDraw.p` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/QuickDraw.p` | `c1d3590c448e4e0ed536cf701e0d1f23acaa39e054cb185dfbb91929fc96a63d` | `c1d3590c448e4e0ed536cf701e0d1f23acaa39e054cb185dfbb91929fc96a63d` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/QuickDraw2.p` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/QuickDraw2.p` | `0804e7bf8f880906d90300ae454a97fe415696210e113853786ee3f527554c51` | `0804e7bf8f880906d90300ae454a97fe415696210e113853786ee3f527554c51` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/QuickGlue.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/QuickGlue.a` | `e6011b810672dda1ac8e2241589965539507848392f0b8b1cf39be48ae9d34b5` | `e6011b810672dda1ac8e2241589965539507848392f0b8b1cf39be48ae9d34b5` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/RRects.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/RRects.a` | `d73b0e74e5be5225a6910428c47772bedf96676c34dfb71ea95fb0d7ef6fb47b` | `d73b0e74e5be5225a6910428c47772bedf96676c34dfb71ea95fb0d7ef6fb47b` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Rects.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Rects.a` | `ac1b8e6544daddfb8c4ae7272e8803be1c73ce3a0bb5f4d9a18e030505fcc9b0` | `ac1b8e6544daddfb8c4ae7272e8803be1c73ce3a0bb5f4d9a18e030505fcc9b0` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Regions.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Regions.a` | `e673b7a31f029541ccfbe0415d6cf52fd60dd17cd2f936c5e8605e24baae2748` | `e673b7a31f029541ccfbe0415d6cf52fd60dd17cd2f936c5e8605e24baae2748` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/RgnBlt.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/RgnBlt.a` | `16c400510330c67c6db2b0e96601c3d9358e5ed2f13ee3c1319e7e765b06ea7f` | `16c400510330c67c6db2b0e96601c3d9358e5ed2f13ee3c1319e7e765b06ea7f` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/RgnOp.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/RgnOp.a` | `900364197e48f0445361d50839d844afc632b4942ac163cc55783a476f0abb6c` | `900364197e48f0445361d50839d844afc632b4942ac163cc55783a476f0abb6c` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/SeekRgn.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/SeekRgn.a` | `066b2e232133bebb8e6110479423f0d4f476924136ec9a0ea9e20d37685edf67` | `066b2e232133bebb8e6110479423f0d4f476924136ec9a0ea9e20d37685edf67` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/SortPoints.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/SortPoints.a` | `c5577066a4db2532baed1e2a4272eca4d8e1e633971c97e8fb8d9ac5559bd7d3` | `c5577066a4db2532baed1e2a4272eca4d8e1e633971c97e8fb8d9ac5559bd7d3` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Stretch.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Stretch.a` | `30aea46aa01dc3e7401da37a5dd045033e82654fbe5159ae14f823d633b9d20c` | `30aea46aa01dc3e7401da37a5dd045033e82654fbe5159ae14f823d633b9d20c` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/TestGraf.p` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/TestGraf.p` | `b804e3c05c7617a301bdbfcbcb4baa563008c3f4f9f444d9f31dc4c125246765` | `b804e3c05c7617a301bdbfcbcb4baa563008c3f4f9f444d9f31dc4c125246765` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Text.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Text.a` | `791a6a5da37573549b9963e8331c0faaffa02816a81ef98f12f0710ecb47ae18` | `791a6a5da37573549b9963e8331c0faaffa02816a81ef98f12f0710ecb47ae18` |
| `secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Util.a` | `recon/discovery/breadth/chm-quickdraw/102658076_quickdraw_acc/QuickDraw Source/Util.a` | `114b3b1aac65ba456b0014cf0c0714e139bf39e4fa0d9b5184be7fc13f4658cf` | `114b3b1aac65ba456b0014cf0c0714e139bf39e4fa0d9b5184be7fc13f4658cf` |
| `secondary/evidence/atwood-links.html` | `recon/discovery/evidence/atwood-links.html` | `6e7fcfc3a04337f31eb375557553304ebdd4d7ce0b01cfc97170a1560f24a5cc` | `6e7fcfc3a04337f31eb375557553304ebdd4d7ce0b01cfc97170a1560f24a5cc` |
| `secondary/evidence/c2-ward-debt.json` | `recon/discovery/evidence/c2-ward-debt.json` | `e18b7498340878fee721cfe87022bfe8a681a3cc4db9ac45aea4337e5065cef2` | `e18b7498340878fee721cfe87022bfe8a681a3cc4db9ac45aea4337e5065cef2` |
| `secondary/evidence/c2-ward-debt.txt` | `recon/discovery/evidence/c2-ward-debt.txt` | `bfb582e333d8e086ae021062cbb4a6d7a4e4b0b07c79fcd53a3991802157497d` | `bfb582e333d8e086ae021062cbb4a6d7a4e4b0b07c79fcd53a3991802157497d` |
| `secondary/evidence/c2try.html` | `recon/discovery/evidence/c2try.html` | `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` |
| `secondary/evidence/c2try.txt` | `recon/discovery/evidence/c2try.txt` | `d2e671d8620c82f5ea5d70ef5eae5d5af824a8c8c364aa4313bba7750ffe8980` | `d2e671d8620c82f5ea5d70ef5eae5d5af824a8c8c364aa4313bba7750ffe8980` |
| `secondary/evidence/chm-quickdraw.html` | `recon/discovery/evidence/chm-quickdraw.html` | `731cbd5a4adc729ab96023ba9bd9af420c921f7d7c01c76bc21b667c2a47b1f7` | `731cbd5a4adc729ab96023ba9bd9af420c921f7d7c01c76bc21b667c2a47b1f7` |
| `secondary/evidence/chm-quickdraw.txt` | `recon/discovery/evidence/chm-quickdraw.txt` | `d79892a91ac65ebcf91cc7e9efe6fc0c6bb016fe07cef5d7728cc8fc9d1bde37` | `d79892a91ac65ebcf91cc7e9efe6fc0c6bb016fe07cef5d7728cc8fc9d1bde37` |
| `secondary/evidence/chrome-stable-2010-01-25.html` | `recon/discovery/evidence/chrome-stable-2010-01-25.html` | `a2c9e6f8165c35751a601bd2de7fcef258feea789c927d10f63531abc368bd70` | `a2c9e6f8165c35751a601bd2de7fcef258feea789c927d10f63531abc368bd70` |
| `secondary/evidence/chrome-stable-2010-01-25.txt` | `recon/discovery/evidence/chrome-stable-2010-01-25.txt` | `c616544d43ab11b0d8143c03ac9c166d8478fa7cf2ab1a909f89c90093137e71` | `c616544d43ab11b0d8143c03ac9c166d8478fa7cf2ab1a909f89c90093137e71` |
| `secondary/evidence/chromium-ext-2009-06.html` | `recon/discovery/evidence/chromium-ext-2009-06.html` | `39a73db21278ad32c18ea386abb29ba300973320fc641aa1f2d13235b382abe7` | `39a73db21278ad32c18ea386abb29ba300973320fc641aa1f2d13235b382abe7` |
| `secondary/evidence/chromium-ext-2009-06.txt` | `recon/discovery/evidence/chromium-ext-2009-06.txt` | `bed235800404dab0e29d94e59da9fce3959f796a2de473ab46547bda9ccdf3f7` | `bed235800404dab0e29d94e59da9fce3959f796a2de473ab46547bda9ccdf3f7` |
| `secondary/evidence/chromium-multiproc-body.txt` | `recon/discovery/evidence/chromium-multiproc-body.txt` | `1d38173f744a6fe66274cecd9ac80d6ae4c20a0a7996fcf898ca50b7b3138bc1` | `1d38173f744a6fe66274cecd9ac80d6ae4c20a0a7996fcf898ca50b7b3138bc1` |
| `secondary/evidence/chromium-multiproc.html` | `recon/discovery/evidence/chromium-multiproc.html` | `61890989ff4bc80b60f52f406ff3719ebf144918ef9f85adfd4a9fd04371ba90` | `61890989ff4bc80b60f52f406ff3719ebf144918ef9f85adfd4a9fd04371ba90` |
| `secondary/evidence/chromium-multiproc.txt` | `recon/discovery/evidence/chromium-multiproc.txt` | `58c590084b9e89a263764568193ad6d721c283da5e5b5b4efb0ef51f5c3eb70c` | `58c590084b9e89a263764568193ad6d721c283da5e5b5b4efb0ef51f5c3eb70c` |
| `secondary/evidence/cpan-history.md` | `recon/discovery/evidence/cpan-history.md` | `6cf0980275b9ec5d53ccf0ed37c700953a4621ceabdc8e3c4475a3fa4f2e7bfd` | `6cf0980275b9ec5d53ccf0ed37c700953a4621ceabdc8e3c4475a3fa4f2e7bfd` |
| `secondary/evidence/equifax.txt` | `recon/discovery/evidence/equifax.txt` | `c13b5ca2f3fa38c2059efc326161025910a9368e54ef9200138426f0f88fbe53` | `c13b5ca2f3fa38c2059efc326161025910a9368e54ef9200138426f0f88fbe53` |
| `secondary/evidence/ewd249.html` | `recon/discovery/evidence/ewd249.html` | `b23a003306d2680c95603d8da8f5fae0aa1312b9ec75fcd720ec69215ed31e3a` | `b23a003306d2680c95603d8da8f5fae0aa1312b9ec75fcd720ec69215ed31e3a` |
| `secondary/evidence/ewd249.txt` | `recon/discovery/evidence/ewd249.txt` | `240fc706cd3d7f52b2b0eb6960eede2311fdad9d4de82d37405625b7b3da9a86` | `240fc706cd3d7f52b2b0eb6960eede2311fdad9d4de82d37405625b7b3da9a86` |
| `secondary/evidence/go-proverbs.html` | `recon/discovery/evidence/go-proverbs.html` | `ea52bf96684c527a9c0cf6c25f9bd6d1aa60245e26151eaba2ea46c1abff4949` | `ea52bf96684c527a9c0cf6c25f9bd6d1aa60245e26151eaba2ea46c1abff4949` |
| `secondary/evidence/go-proverbs.txt` | `recon/discovery/evidence/go-proverbs.txt` | `c30b3f3ba5ee5f4c0c5df8ee0c09db8ee35e64be467fb0a8b3a930a5715ed3e0` | `c30b3f3ba5ee5f4c0c5df8ee0c09db8ee35e64be467fb0a8b3a930a5715ed3e0` |
| `secondary/evidence/gpl1.txt` | `recon/discovery/evidence/gpl1.txt` | `49c007bafb5ad6dd9f9d4dae4d3ac0461975498150c05d684c551f0914ab486c` | `49c007bafb5ad6dd9f9d4dae4d3ac0461975498150c05d684c551f0914ab486c` |
| `secondary/evidence/hertzfeld-folklore.html` | `recon/discovery/evidence/hertzfeld-folklore.html` | `1a1268a9c81a3a8bd988c8aa8bfff0848c35ef27898e7154aa40c233df8bca3f` | `1a1268a9c81a3a8bd988c8aa8bfff0848c35ef27898e7154aa40c233df8bca3f` |
| `secondary/evidence/hertzfeld-folklore.txt` | `recon/discovery/evidence/hertzfeld-folklore.txt` | `58ca217176c01ad18015648c782920cd092234ff432792b69d7cc0460625fe3a` | `58ca217176c01ad18015648c782920cd092234ff432792b69d7cc0460625fe3a` |
| `secondary/evidence/lapack-notes.html` | `recon/discovery/evidence/lapack-notes.html` | `fb4124b01d957a290bf1cea32451f2b1139f6f848337b475db310dc6fd2d877e` | `fb4124b01d957a290bf1cea32451f2b1139f6f848337b475db310dc6fd2d877e` |
| `secondary/evidence/lapack-notes.txt` | `recon/discovery/evidence/lapack-notes.txt` | `9ad8e306f4aec0686abdd8b9fce2955ae6464580d8d35e0349179c5ba8788aa9` | `9ad8e306f4aec0686abdd8b9fce2955ae6464580d8d35e0349179c5ba8788aa9` |
| `secondary/evidence/leftpad-index.js` | `recon/discovery/evidence/leftpad-index.js` | `23b347feea1ad99fbe171fe3839f29230312d85c74880ad018a5cae20ad34397` | `23b347feea1ad99fbe171fe3839f29230312d85c74880ad018a5cae20ad34397` |
| `secondary/evidence/nato1969.txt` | `recon/discovery/evidence/nato1969.txt` | `7a723cd50e8ecaf2f86dbee1ccf1cf74d7c557db38dabfa02162928f80d0276e` | `7a723cd50e8ecaf2f86dbee1ccf1cf74d7c557db38dabfa02162928f80d0276e` |
| `secondary/evidence/npm-event-stream.html` | `recon/discovery/evidence/npm-event-stream.html` | `0385796be8013bde14a50175fb4e3aa2b9f1fb0bad6524550a269578b6660f98` | `0385796be8013bde14a50175fb4e3aa2b9f1fb0bad6524550a269578b6660f98` |
| `secondary/evidence/npm-event-stream.txt` | `recon/discovery/evidence/npm-event-stream.txt` | `2656fea7c4db3f2d15effe189b6a598582e18201a5d5abf95d81599ebd41f27e` | `2656fea7c4db3f2d15effe189b6a598582e18201a5d5abf95d81599ebd41f27e` |
| `secondary/evidence/npm-kik-leftpad.html` | `recon/discovery/evidence/npm-kik-leftpad.html` | `c8c7f13a9b419cb6a19a70a8103b869a04c19322174ba8456173af56c54949c3` | `c8c7f13a9b419cb6a19a70a8103b869a04c19322174ba8456173af56c54949c3` |
| `secondary/evidence/npm-kik-leftpad.txt` | `recon/discovery/evidence/npm-kik-leftpad.txt` | `5107cb9dfea339544b7cef4e873a782ac513738a9c5428823d819daeb5a91e98` | `5107cb9dfea339544b7cef4e873a782ac513738a9c5428823d819daeb5a91e98` |
| `secondary/evidence/oopsla92.html` | `recon/discovery/evidence/oopsla92.html` | `7bb0ebbd6e99b96cb15229de39e810dd7644ea56a755a22668663f68b09de5d5` | `7bb0ebbd6e99b96cb15229de39e810dd7644ea56a755a22668663f68b09de5d5` |
| `secondary/evidence/oopsla92.txt` | `recon/discovery/evidence/oopsla92.txt` | `954b373aac55a2401524053aa31af56c1c751bcf0159b947789b8ea4e9a51938` | `954b373aac55a2401524053aa31af56c1c751bcf0159b947789b8ea4e9a51938` |
| `secondary/evidence/ritchie-cacm-bstj.html` | `recon/discovery/evidence/ritchie-cacm-bstj.html` | `15478412e7e2f3f1627a9ae62cf3535ea10ba33ed3022f6490f917c8349bbbf9` | `15478412e7e2f3f1627a9ae62cf3535ea10ba33ed3022f6490f917c8349bbbf9` |
| `secondary/evidence/ritchie-cacm-bstj.txt` | `recon/discovery/evidence/ritchie-cacm-bstj.txt` | `988512b1511e660c6c5062c4b441aba481bcfd50a240a0d56af82e0d718c05ca` | `988512b1511e660c6c5062c4b441aba481bcfd50a240a0d56af82e0d718c05ca` |
| `secondary/evidence/ritchie84evolution.txt` | `recon/discovery/evidence/ritchie84evolution.txt` | `d5f2a8e0819a81e9cae440679873f4b30c8158ee8c815cd7accf7f54ff5e4c25` | `d5f2a8e0819a81e9cae440679873f4b30c8158ee8c815cd7accf7f54ff5e4c25` |
| `secondary/evidence/shipley-live.html` | `recon/discovery/evidence/shipley-live.html` | `62cffe06eda1c210a744d01b45dfd664f6db4f3f2a2cb912a96c92a9140826a5` | `62cffe06eda1c210a744d01b45dfd664f6db4f3f2a2cb912a96c92a9140826a5` |
| `secondary/evidence/shipley-pmc14.html` | `recon/discovery/evidence/shipley-pmc14.html` | `f0bc6213e501e7517f7b6bed6a2b705294ca67df716da432d72dc8b1b1e428ff` | `f0bc6213e501e7517f7b6bed6a2b705294ca67df716da432d72dc8b1b1e428ff` |
| `secondary/evidence/shipley-pmc14.txt` | `recon/discovery/evidence/shipley-pmc14.txt` | `c2c69e1401cba698e9552d03a9a98b2e99df3ce89600ac4bafaf4fc8d9ac1d36` | `c2c69e1401cba698e9552d03a9a98b2e99df3ce89600ac4bafaf4fc8d9ac1d36` |
| `secondary/evidence/skrenta-wayback.html` | `recon/discovery/evidence/skrenta-wayback.html` | `eab7489e22aeb016fc0ebab3c22850b32fa866886968ea3d5107f173981e892b` | `eab7489e22aeb016fc0ebab3c22850b32fa866886968ea3d5107f173981e892b` |
| `secondary/evidence/skrenta-wayback.txt` | `recon/discovery/evidence/skrenta-wayback.txt` | `0f90d3de2b5df25ac1e474d5c4188f6575ba09886d768ef1c1c817899cce14e4` | `0f90d3de2b5df25ac1e474d5c4188f6575ba09886d768ef1c1c817899cce14e4` |
| `secondary/evidence/snyk-1m.html` | `recon/discovery/evidence/snyk-1m.html` | `f219d51b75ff140e4c27e9f6a2d218bf72edd85acef2ed7b2c07ae0683473b56` | `f219d51b75ff140e4c27e9f6a2d218bf72edd85acef2ed7b2c07ae0683473b56` |
| `secondary/evidence/snyk-1m.txt` | `recon/discovery/evidence/snyk-1m.txt` | `9162d48a19123c6856571e0b7aeb5f9cc3fdccf7445c9183a64d44c7147d0b33` | `9162d48a19123c6856571e0b7aeb5f9cc3fdccf7445c9183a64d44c7147d0b33` |
| `secondary/evidence/sqlite-amalg-2019.html` | `recon/discovery/evidence/sqlite-amalg-2019.html` | `008496f18e3dcaa8213691f7fae72db751ba64fc5aadae7ae2f9ffaa2fb8d1f8` | `008496f18e3dcaa8213691f7fae72db751ba64fc5aadae7ae2f9ffaa2fb8d1f8` |
| `secondary/evidence/sqlite-amalg-2019.txt` | `recon/discovery/evidence/sqlite-amalg-2019.txt` | `3ae4ee4dd154d0a3e4477713ce3ebf538dfd702fe4bd02bd980e15f75655dc93` | `3ae4ee4dd154d0a3e4477713ce3ebf538dfd702fe4bd02bd980e15f75655dc93` |
| `secondary/evidence/sqlite-testing-2019.html` | `recon/discovery/evidence/sqlite-testing-2019.html` | `17bca940b7f596cc93071262acf0660a7f05e18727d4953b7c3c4f26f5b4e24b` | `17bca940b7f596cc93071262acf0660a7f05e18727d4953b7c3c4f26f5b4e24b` |
| `secondary/evidence/sqlite-testing-2019.txt` | `recon/discovery/evidence/sqlite-testing-2019.txt` | `cce7904773933fa499330d05ec191fc0214c74740570b7822209ef4ba752b306` | `cce7904773933fa499330d05ec191fc0214c74740570b7822209ef4ba752b306` |
| `secondary/evidence/sqlite-testing.html` | `recon/discovery/evidence/sqlite-testing.html` | `d1a8b5c43a42e573f7165483fdf02b91c605076b869a823d924241fb308feb97` | `d1a8b5c43a42e573f7165483fdf02b91c605076b869a823d924241fb308feb97` |
| `secondary/evidence/sqlite-testing.txt` | `recon/discovery/evidence/sqlite-testing.txt` | `7b09985ebb9037fbc7956f7a59567b84521a49e9e02ead369f80eced91d06f77` | `7b09985ebb9037fbc7956f7a59567b84521a49e9e02ead369f80eced91d06f77` |
| `secondary/evidence/struts-s2-032.html` | `recon/discovery/evidence/struts-s2-032.html` | `829ec9b9cde81af5418b819a27dad1c39978e5892bb7f768e37d335cbb0ecaaf` | `829ec9b9cde81af5418b819a27dad1c39978e5892bb7f768e37d335cbb0ecaaf` |
| `secondary/evidence/struts-s2-032.txt` | `recon/discovery/evidence/struts-s2-032.txt` | `a49713c95c06cba9d48023eb5ca8a5ee3f2e4d4019c643f7daebe3be6028696d` | `a49713c95c06cba9d48023eb5ca8a5ee3f2e4d4019c643f7daebe3be6028696d` |
| `secondary/evidence/struts-s2-057.html` | `recon/discovery/evidence/struts-s2-057.html` | `2927dfbd4e746693866e8731cb7682c25a98866f8bbaf89b54fa3c5db5d3bc18` | `2927dfbd4e746693866e8731cb7682c25a98866f8bbaf89b54fa3c5db5d3bc18` |
| `secondary/evidence/struts-s2-057.txt` | `recon/discovery/evidence/struts-s2-057.txt` | `024c14bf8325b0f2abbeb601a6b4489b3e6cc2fd0a9389010b3a6fb334e24961` | `024c14bf8325b0f2abbeb601a6b4489b3e6cc2fd0a9389010b3a6fb334e24961` |
| `secondary/evidence/ward-debt.html` | `recon/discovery/evidence/ward-debt.html` | `319606335c20e33571204c0ea1744ec9c6a58900ccc3bc87af6498f235114af4` | `319606335c20e33571204c0ea1744ec9c6a58900ccc3bc87af6498f235114af4` |
| `secondary/evidence/ward-debt.txt` | `recon/discovery/evidence/ward-debt.txt` | `d2e671d8620c82f5ea5d70ef5eae5d5af824a8c8c364aa4313bba7750ffe8980` | `d2e671d8620c82f5ea5d70ef5eae5d5af824a8c8c364aa4313bba7750ffe8980` |
| `secondary/evidence/zlib-changelog.txt` | `recon/discovery/evidence/zlib-changelog.txt` | `c6f42df0f27486db922d633e7a70757b56c6cd9f742f21af419d232649efbede` | `c6f42df0f27486db922d633e7a70757b56c6cd9f742f21af419d232649efbede` |
| `secondary/evidence/lp003/package/.npmignore` | `recon/discovery/evidence/lp003/package/.npmignore` | `09461718e3e1584c24329fbf7022cde09edf18944a5f11ce3b50dc1d6da74991` | `09461718e3e1584c24329fbf7022cde09edf18944a5f11ce3b50dc1d6da74991` |
| `secondary/evidence/lp003/package/README.md` | `recon/discovery/evidence/lp003/package/README.md` | `788d156d0e150364984f597baafdcead7594072fb2b6716e0c006ae79a70b1c5` | `788d156d0e150364984f597baafdcead7594072fb2b6716e0c006ae79a70b1c5` |
| `secondary/evidence/lp003/package/index.js` | `recon/discovery/evidence/lp003/package/index.js` | `c4c210acf158e2ba60fc0febc2eb689a0138646f8cf391c09d925423b44bbf9e` | `c4c210acf158e2ba60fc0febc2eb689a0138646f8cf391c09d925423b44bbf9e` |
| `secondary/evidence/lp003/package/package.json` | `recon/discovery/evidence/lp003/package/package.json` | `959865191c4bb4e3fd4ee0d10273e79aceef0a98d74ac19b111f647904aa9c26` | `959865191c4bb4e3fd4ee0d10273e79aceef0a98d74ac19b111f647904aa9c26` |
| `index/index-lane1.md` | `recon/index-lane1.md` | `0d53379c382c79f9a65063be1623ac15f08686e2843588242425a26ba5eec18b` | `0d53379c382c79f9a65063be1623ac15f08686e2843588242425a26ba5eec18b` |
| `index/index-lane2.md` | `recon/index-lane2.md` | `e6a1463572883b3b8c4095a6e913f5531c92746b117088ca3445d797dccfe02c` | `e6a1463572883b3b8c4095a6e913f5531c92746b117088ca3445d797dccfe02c` |
| `index/sources.md` | `sources.md` | `58fbf68ec5d07fe990a543fb79fba3416b408828a6015a446457dcfb578e7a8d` | `58fbf68ec5d07fe990a543fb79fba3416b408828a6015a446457dcfb578e7a8d` |
