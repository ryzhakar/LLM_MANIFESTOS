# Source Index — lane2
Elements loaded in full from source: First Principles (/home/user/LLM_MANIFESTOS/manifestos/first-principles.md); Strunk SPR v3 (/home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml); binding protocol (/home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md).
Interplay: First Principles demands the irreducible text over its name, and Strunk demands concrete, positive, economical prose; they converge on facts over form and pull apart nowhere in this task, so each dump framing is checked against the fetched text and every mismatch is reported as a fact.
Commitments: I must verify each source from its own text, and I will record every URL tried and every discrepancy; I must not summarize or interpret the arguments, and I will not; I must quote verbatim with a location, and I will; I must write definite, positive, brief prose, and I will.

Conventions. Words = whitespace-delimited tokens below the 6-line header of the saved file. P{n} = n-th blank-line-separated block of the saved file below its header and the blank line after it (a heading, list, code block, or table is one block). In quotes, " / " marks a source line break inside one block. Quotes are generated from the saved files by script and match them character for character. Type of every finding: primary text (quoted from the saved copy). Source dump: /home/user/LLM_MANIFESTOS/research/manifesto-craft/sources.md, lane 2.

## Fetch table

| ID | title | author | year | URL fetched | status | words | local path | discrepancy with dump |
|---|---|---|---|---|---|---|---|---|
| L2-01 | Mass Produced Software Components (NATO report section 8.2; printed report pp. 138-150) | M. D. McIlroy | 1968 (talk, 7-11 Oct 1968; report dated January 1969) | http://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1968.PDF | FULL | 4018 | /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-01.txt | Dumped Scribd URL serves HTTP 200 text/html, 1,680,822 B: a viewer wrapper around the whole NATO report, not the paper. Paper extracted from the Newcastle PDF (PDF pp. 79-85 of 136). Conference discussion (printed pp. 151-155) saved apart: /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-01-discussion.txt (1816 words). |
| L2-02 | The UNIX Time-Sharing System (Comm. ACM 17(7), July 1974, pp. 365-375) | Dennis M. Ritchie and Ken Thompson | 1974 | https://dsf.berkeley.edu/cs262/unix.pdf | FULL | 9458 | /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-02.txt | Dumped nokia.com retro.pdf URL returns HTTP 403 (Akamai Access Denied). Its Wayback copy is a different document: Ritchie's sole-author "The UNIX Time-sharing System: A Retrospective" (HICSS-10, January 1977), saved apart: /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-02-dumped-retro.txt (9027 words). The 1974 text comes from Eric A. Brewer's electronic recreation (UC Berkeley), not an ACM scan. |
| L2-03 | CPAN "private showing" (CPAN.ANNOUNCE) | Jarkko Hietaniemi | 1995 (1 Aug 1995 per Bowers 2015; file Last-Modified 26 Jul 1995) | https://www.cpan.org/misc/CPAN.ANNOUNCE | PARTIAL | 638 | /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-03.txt | Dumped URL is a 2015 blog post by Neil Bowers, not Hietaniemi's text (saved apart: /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-03-dumped-bowers.txt, 391 words). Bowers dates Hietaniemi's public announcement to comp.lang.perl.announce 26 Oct 1995; that post was NOT obtained. The saved text is his earlier mail to perl-packrats. |
| L2-04 | I've Just Liberated My Modules | Azer Koçulu | 2016 (page date Mar 23, 2016) | https://azerkoculu.com/posts/i-ve-just-liberated-my-modules | FULL | 233 | /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-04.txt | Dump note calls it the primary account of the left-pad deletion; the text contains no occurrence of "left-pad" and names the module "kik". Medium original (Wayback snapshot 2017-01-04) is dated Mar 22, 2016 and carries one extra line, "Note: Thank you for all the support". Body text identical. |
| L2-05 | Our Software Dependency Problem | Russ Cox | 2019 (posted Wednesday, January 23, 2019) | https://research.swtch.com/deps | FULL | 5444 | /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-05.txt | None found. Text names the later versions: ACM Queue (March-April 2019) and CACM (August 2019) as "Surviving Software Dependencies". Word count includes References and Coda. |

## Per-source

### L2-01 — Mass Produced Software Components (M. D. McIlroy, NATO 1968)

URLs tried:
- https://www.scribd.com/doc/184279203/software-eng-nato1968-pdf — HTTP 200, text/html; charset=utf-8, 1,680,822 B. Scribd viewer page titled "Software Eng Nato1968 PDF | PDF" (embedded data lists "page_count":136, the length of the whole report; the string "pinnacle of software" occurs once in the HTML) around the whole report; not the named paper alone; not used.
- http://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1968.PDF — HTTP 200, application/pdf, 2,474,464 B, 136 pages. USED. Newcastle University (Brian Randell) copy of the report.
- https://www.cs.dartmouth.edu/~doug/components.txt — HTTP 200, text/plain; charset=UTF-8, 38,151 B (redirect to https://mcilroy.cs.dartmouth.edu/components.txt). McIlroy's own scan of pp. 138-155 (paper plus discussion). Cross-check only.
- https://www.cs.dartmouth.edu/~doug/ — HTTP 200, text/html, 5,956 B (redirect to https://mcilroy.cs.dartmouth.edu/). Probe of McIlroy's page.

Saved copies:
- /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-01.txt — 4018 words, 71 blocks; paper only; PDF pp. 79 (from the 8.2 heading) to 85 (end of "Summary"); printed pp. 138-150.
- /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-01-discussion.txt — 1816 words, 19 blocks; supplementary: "8.2.1. DISCUSSION", PDF pp. 85-87, printed pp. 151-155; not indexed below.

Authorship and year, from the text or hosting page: Title line in the text: "8.2. MASS PRODUCED SOFTWARE COMPONENTS, BY M.D. MCILROY". Year: the report covers the conference of 7-11 October 1968 and is dated January 1969; the dump's 1968 matches the talk, and the printed edition is 1969.

Section headings in order:
- P1: 8.2. MASS PRODUCED SOFTWARE COMPONENTS, BY M.D. MCILROY
- P2: ABSTRACT
- P4: The Software Industry is Not Industrialized.
- P8: Software Components
- P12: A Familiar Example
- P22: Parameterized Families of Components
- P38: Application Areas
- P45: The Market
- P50: Present Day Suppliers
- P57: A Components Factory
- P67: Touching on Standards
- P69: Summary
- Run-in labels inside "Parameterized Families of Components" (paragraphs opening with a label, not separate headings): P28 Choice of Precision.; P29 Choice of Robustness.; P30 Choice of Generality.; P31 Choice of Time-space behavior.; P32 Choice of Algorithm.; P33 Choice of Interfaces.; P36 Choice of Accessing method.; P37 Choice of Data structures.
- Run-in labels inside "Application Areas": P40 Numerical approximation routines.; P41 Input-output conversion.; P42 Two and three dimensional geometry.; P43 Text processing.; P44 Storage management.

First sentence: "Software components (routines), to be widely applicable to different machines and users, should be available in families arranged according to precision, robustness, generality and timespace performance." (P3, first sentence of the paper's abstract). First sentence after the abstract: "We undoubtedly produce software by backward techniques." (P5).

Last sentence: "I think there are considerable areas of software ready, if not overdue, for this approach." (P71).

Printed-page map (the Newcastle edition marks each original page break with the page number; page N begins in the block shown): p.139 in P5; p.140 in P9; p.141 in P15; p.142 in P21; p.143 in P26; p.144 in P35; p.145 in P41; p.146 in P46; p.147 in P50; p.148 in P56; p.149 in P62; p.150 in P67. Printed p.138 begins before the paper's title line (the paper starts mid-page). The paper ends on printed p.150; "8.2.1. DISCUSSION" opens printed p.151.
Cross-check against McIlroy's own scan (https://www.cs.dartmouth.edu/~doug/components.txt, headed "Scanned from P. Naur and B. Randell, 'Software Engineering, Report on a conference sponsored by the NATO Science Committee, Garmisch, Germany, 7th to 11th October 1968', Scientific Affairs Division, NATO, Brussels, 1969, 138-155. ... Isolated misprints in the original have been corrected, and a hodge-podge of English and American spellings has been resolved in favor of American."): word-level diff of the paper = 30 hunks, all spelling, punctuation, or misprint; every numeral identical except Dartmouth "O-2pi" (letter O) for Newcastle "0-2π" (P14). One lexical difference: Newcastle "microprocessors" (P46), Dartmouth "macroprocessors". Newcastle edition's own note: scanned from the original, OCR converted, "it is almost certain that some errors have crept in" (Robert M. McClure, 2001); extraction keeps the OCR text (for example "subassemblles" in P40).
Hosting document: report cover reads "SOFTWARE ENGINEERING / Report on a conference sponsored by the NATO SCIENCE COMMITTEE / Garmisch, Germany, 7th to 11th October 1968 / ... Editors: Peter Naur and Brian Randell / January 1969".

Quantified claims (verbatim, with location):
- P3: "Existing sources of components — manufacturers, software houses, users’ groups and algorithm collections — lack the breadth of interest or coherence of purpose to assemble more than one or two members of such families, yet software production in the large would be enormously helped by the availability of spectra of high quality routines, quite as mechanical design is abetted by the existence of families of structural shapes, screws or resistors."
- P11: "Thus the builder of an assembler will be able to say ‘I will use a String Associates A4 symbol table, in size 500x8,’ and therewith consider it done."
- P14: "Precision, for which perhaps ten different approximating functions might suffice"
- P14: "Argument ranges 0-π/2, 0-2π, also -π/2 to π/2, -π to π, -big to +big"
- P15: "We have here 10 precisions, 2 scalings, 5 ranges and 3 robustnesses."
- P15: "This gives us a basic inventory of 300 sine routines."
- P20: "A company setting out to write 300 sine routines one at a time and hoping to recoup on volume sales would certainly go broke."
- P20: "Fortunately the cost of offering such an ‘inventory’ need not be nearly 300 times the cost of keeping one routine."
- P23: "Sysgen differs, though, in a couple of ways from what I have in mind as the way a software components industry might operate." [vague count]
- P26: "One could not stock 300 sine routines unless they were all in some sense instances of just a few models, highly parameterized, in which all but a few parameters were intended to be permanently bound before run time."
- P42: "One can easily list a few dozen fundamental routines for geometry."
- P46: "At Bell Telephone Laboratories we have about 100 general purpose machines from a dozen manufacturers."
- P47: "To construct these systems of high-class componentry we would have to surround each of some 50 machines with a permanent coterie of software specialists."
- P59: "Our purveyor of 300 sine routines would probably go broke waiting for customers if that’s all he offered, just as an electronics firm selling circuit modules for only one purpose would have trouble in the market."
- P61: "Even before founding a pilot plant, one would be wise to have demonstrated techniques for creating a parameterized family of routines for a couple of familiar purposes, say a sine routine and a Fortran I/O module." [vague count]
- P70: "I want the different types of routine in the catalogue that are similar in purpose to be engineered uniformly, so that two similar routines should be available with similar options and two options of the same routine should be interchangeable in situations indifferent to that option." [small counts]

### L2-02 — The UNIX Time-Sharing System (Ritchie and Thompson, 1974)

URLs tried:
- https://www.nokia.com/bell-labs/about/dennis-m-ritchie/retro.pdf — HTTP 403, text/html, 437 B (Akamai "Access Denied"). Dumped link; not used.
- https://web.archive.org/web/2016/https://www.nokia.com/bell-labs/about/dennis-m-ritchie/retro.pdf — HTTP 200, application/pdf, 59,400 B, 13 pages (final URL snapshot 20250615233346). Content: "The UNIX Time-sharing System: A Retrospective", Dennis M. Ritchie (sole author). Saved as supplementary, not the named paper.
- http://cm.bell-labs.co/who/dmr/retro.pdf — HTTP 503, text/plain, 48 B ("DNS resolution failed (transient resolver error)").
- https://www.bell-labs.com/usr/dmr/www/retro.pdf — HTTP 410, 0 B.
- https://dsf.berkeley.edu/cs262/unix.pdf — HTTP 200, application/pdf, 158,746 B, 11 pages. USED. Title page: "The UNIX Time-Sharing System, Dennis M. Ritchie and Ken Thompson, Bell Laboratories"; footers "Communications of the ACM, July 1974, Volume 17, Number 7" and page numbers 365-375; "The electronic version was recreated by Eric A. Brewer, University of California at Berkeley ... I have left errors in the original unchanged."
- https://www.cs.berkeley.edu/~brewer/cs262/unix.pdf — HTTP 200, application/pdf, 158,746 B (redirect to https://people.eecs.berkeley.edu/~brewer/cs262/unix.pdf); same file.
- https://dl.acm.org/doi/pdf/10.1145/361011.361061 — HTTP 403, text/html, 5,467 B (the ACM copy is not reachable).
- https://web.archive.org/web/2016/https://www.bell-labs.com/usr/dmr/www/cacm.html — HTTP 200, text/html, 61,577 B (snapshot 20170218050938). Ritchie's own page, headed "BSTJ version of C.ACM Unix paper": the 1978 Bell System Technical Journal revision ("four versions", "over 600 installations"), not the 1974 text; not saved.
- https://www.read.seas.harvard.edu/~kohler/class/aosref/ritchie84evolution.pdf — HTTP 200, application/pdf, 30,159 B: "The Evolution of the Unix Time-sharing System" (Ritchie, 1979/1984); a different paper; not saved.
- https://www.cs.princeton.edu/courses/archive/fall03/cs318/unix.pdf — HTTP 404, 139 B.

Saved copies:
- /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-02.txt — 9458 words, 192 blocks; PDF pp. 1-11 = CACM pp. 365-375; page-1 copyright and recreation notice and running headers/footers removed (not counted).
- /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-02-dumped-retro.txt — 9027 words; supplementary: what the dumped URL serves; approximate paragraphing; not indexed below.

Authorship and year, from the text or hosting page: "Dennis M. Ritchie and Ken Thompson / Bell Laboratories"; "Copyright © 1974, Association for Computing Machinery"; footers "July 1974 Volume 17 Number 7"; page-1 note: "This is a revised version of a paper presented at the Fourth ACM Symposium on Operating Systems Principles, IBM Thomas J. Watson Research Center, Yorktown Heights. New York, October 15–17, 1973." Matches the dump's authors, title, and year; does not match the dump's URL (see Fetch table).

Section headings in order:
- P1: title block ("The UNIX Time-Sharing System / Dennis M. Ritchie and Ken Thompson / Bell Laboratories"); P2: abstract (unlabeled); P3: "Key Words and Phrases"; P4: "CR Categories"
- P5: 1. Introduction
- P11: 2. Hardware and Software Environment
- P15: 3. The File System
- P17: 3.1 Ordinary Files
- P19: 3.2 Directories
- P27: 3.3 Special Files
- P30: 3.4 Removable File Systems
- P33: 3.5 Protection
- P38: 3.6 I/O Calls
- P56: 3.6.1 Other I/O Calls. (run-in heading at the start of the paragraph)
- P57: 4. Implementation of the File System
- P69: 4.1 Efficiency of the File System
- P71: 5. Processes and Images
- P75: 5.1 Processes
- P80: 5.2 Pipes
- P85: 5.3 Execution of Programs
- P89: 5.4 Process Synchronization
- P93: 5.5 Termination
- P97: 6. The Shell
- P102: 6.1 Standard I/O
- P114: 6.2 Filters
- P122: 6.3 Command Separators: Multitasking
- P134: 6.4 The Shell as a Command: Command files
- P141: 6.5 Implementation of the Shell
- P149: 6.6 Initialization
- P152: 6.7 Other Programs as Shell
- P157: 7. Traps
- P162: 8. Perspective
- P172: 8.1 Influences
- P175: 9. Statistics
- P177: 9.1 Overall
- P179: 9.2 Per day (24-hour day, 7-day week basis)
- P182: 9.3 Command CPU Usage (cut off at 1%)
- P184: 9.4 Command Accesses (cut off at 1%)
- P186: 9.5 Reliability
- P190: Acknowledgments. (run-in label opening the paragraph)
- P191: References

First sentence: "UNIX is a general-purpose, multi-user, interactive operating system for the Digital Equipment Corporation PDP-11/40 and 11/45 computers." (P2).

Last sentence: "We are particularly appreciative of the inventiveness, thoughtful criticism, and constant support of R. Morris, M.D. McIlroy, and J.F. Ossanna." (P190; last prose sentence). Last sentence of section 9.5: "Total up time has been about 98 percent of our 24-hour, 365-day schedule." (P189). The file ends with the reference list (P192).

Not itemized: section-number lines, code and command lines containing digits (for example "ls | pr –2 | opr" in P116), file-descriptor identifiers, cross-reference marks, citation numbers, and the reference list (P192) with its years and page numbers.
Pipe and filter text, for locating: P114 (heading "6.2 Filters"), P115-P121; P80-P84 ("5.2 Pipes").

Quantified claims (verbatim, with location):
- P2: "It offers a number of features seldom found even in larger operating systems, including: (1) a hierarchical file system incorporating demountable volumes; (2) compatible file, device, and inter-process I/O; (3) the ability to initiate asynchronous processes; (4) system command language selectable on a per-user basis; and (5) over 100 subsystems including a dozen languages."
- P6: "There have been three versions of UNIX."
- P6: "The earliest version (circa 1969–70) ran on the Digital Equipment Corporation PDP-7 and -9 computers."
- P7: "Since PDP-11 UNIX became operational in February 1971, about 40 installations have been put into service; they are generally smaller than the system described here."
- P8: "Perhaps the most important achievement of UNIX is to demonstrate that a powerful operating system for interactive use need not be expensive either in equipment or in human effort: UNIX can run on hardware costing as little as $40,000, and less than two man years were spent on the main system software."
- P12: "The PDP-11/45 on which our UNIX installation is implemented is a 16-bit word (8-bit byte) computer with 144K bytes of core memory; UNIX occupies 42K bytes."
- P12: "This system, however, includes a very large number of device drivers and enjoys a generous allotment of space for I/O buffers and system tables; a minimal system capable of running the software mentioned above can require as little as 50K bytes of core altogether."
- P13: "The PDP-11 has a 1M byte fixed-head disk, used for file system storage and swapping, four moving-head disk drives which each provide 2.5M bytes on removable disk cartridges, and a single moving-head disk drive which uses removable 40M byte disk packs."
- P13: "There are also a high-speed paper tape reader-punch, nine-track magnetic tape, and D-tape (a variety of magnetic tape facility in which individual records may be addressed and rewritten)."
- P13: "Besides the console typewriter, there are 14 variable-speed communications interfaces attached to 100-series datasets and a 201 dataset interface used primarily for spooling printout to a communal line printer."
- P14: "Early versions of the operating system were written in assembly language, but during the summer of 1973, it was rewritten in C."
- P14: "The size of the new system is about one third greater than the old."
- P16: "From the point of view of the user, there are three kinds of files: ordinary disk files, directories, and special files."
- P22: "Files are named by sequences of 14 or fewer characters."
- P25: "Each directory always has at least two entries."
- P31: "There is a mount system request which has two arguments: the name of an existing ordinary file, and the name of a direct-access special file whose associated storage volume (e.g. disk pack) should have the structure of an independent file system containing its own directory hierarchy."
- P31: "In our installation, for example, the root directory resides on the fixed-head disk, and the large disk drive, which contains user’s files, is mounted by the system initialization program, the four smaller disk drives are available to users for mounting their own disk packs."
- P34: "Also given for new files is a set of seven protection bits."
- P34: "Six of these specify independently read, write, and execute permission for the owner of the file and for all other users."
- P45: "To create a new file or completely rewrite an old one, there is a create system call which creates the given file if it does not exist, or truncates it to zero length if it does exist."
- P46: "There are no user-visible locks in the file system, nor is there any restriction on the number of users who may have a file open for reading or writing; although it is possible for the contents of a file to become scrambled when two users write on it simultaneously, in practice, difficulties do not arise."
- P47: "It should be said that the system has sufficient internal interlocks to maintain the logical consistency of the file system when two users engage simultaneously in such inconvenient activities as writing on the same file, creating files in the same directory or deleting each other’s open files."
- P51: "If the read pointer is so near the end of the file that reading count characters would cause reading beyond the end, only sufficient bytes are transmitted to reach the end of the file; also, typewriter-like devices never return more than one line of input."
- P51: "When a read call returns with n equal to zero, it indicates the end of the file."
- P61: "If the link-count drops to 0, any disk blocks in the file are freed and the i-node is deallocated."
- P62: "The space on all fixed or removable disks which contain a file system is divided into a number of 512-byte blocks logically addressed from 0 up to a limit which depends on the device."
- P62: "There is space in the i-node of each file for eight device addresses."
- P62: "A small (nonspecial) file fits into eight or fewer blocks; in this case the addresses of the blocks themselves are stored."
- P62: "For large (nonspecial) files, each of the eight device addresses may point to an indirect block of 256 addresses of blocks constituting the file itself."
- P62: "These files may be as large as 8⋅256⋅512, or l,048,576 (220) bytes." [PDF text layer flattens the superscript: source form 2^20 appears as (220); "l,048,576" as in the file]
- P63: "When an I/O request is made to a file whose i-node indicates that it is special, the last seven device address words are immaterial, and the list is interpreted as a pair of bytes which constitute an internal device name."
- P64: "This table is searched for each (i-number, device)-pair which turns up while a path name is being scanned during an open or create; if a match is found, the i-number is replaced by 1 (which is the i-number of the root directory on all file systems), and the device name is replaced by the table value."
- P67: "A program which reads or writes files in units of 512 bytes has an advantage over a program which reads or writes a single byte at a time, but the gain is not immense; it comes mainly from the avoidance of system overhead."
- P70: "To provide an indication of the overall efficiency of UNIX and of the file system in particular, timings were made of the assembly of a 7621-line program."
- P70: "The assembly was run alone on the machine; the total clock time was 35.9 sec, for a rate of 212 lines per sec. The time was divided as follows: 63.5 percent assembler execution time, 16.5 percent system overhead, 20.0 percent disk wait time." [one extracted span; two source sentences]
- P74: "The user-core part of an image is divided into three logical segments."
- P74: "The program text segment begins at location 0 in the virtual address space."
- P74: "At the first 8K byte boundary above the program text segment in the virtual address space begins a non-shared, writable data segment, the size of which may be extended by a system call."
- P78: "When fork is executed by a process, it splits into two independently executing processes."
- P78: "The two processes have independent copies of the original core image, and share any open files."
- P83: "At this point, data are passed between the images of the two processes."
- P103: "Programs executed by the Shell, however, start off with two open files which have file descriptors 0 and 1."
- P137: "Thus if the three lines above were typed on the console, source would be assembled, the resulting program named testprog, and testprog executed."
- P164: "Three considerations which influenced the design of UNIX are visible in retrospect."
- P168: "The aspects of UNIX discussed in this paper exhibit clearly at least the first two of these design considerations."
- P168: "No large ‘‘access method” routines are required to insulate the programmer from the system calls; in fact, all user programs either call the system directly or use a small library program, only tens of instructions long, which buffers a number of characters and reads or writes them all at once."
- P178 (block of 5 lines, verbatim): "72 user population" ; "14 maximum simultaneous users" ; "300 directories" ; "4400 files" ; "34000 512-byte secondary storage blocks used"
- P180: "It has been used to produce a million-digit approximation to the constant e – 2, and is now generating composite pseudoprimes (base 2)."
- P181 (block of 5 lines, verbatim): "1800 commands" ; "4.3 CPU hours (aside from background)" ; "70 connect hours" ; "30 different users" ; "75 logins"
- P183 (block of 18 lines, verbatim): "15.7% C compiler" ; "15.2% users’ programs" ; "11.7% editor" ; "5.8% Shell (used as a command, including command times)" ; "5.3% chess" ; "3.3% list directory" ; "3.1% document formatter" ; "1.6% backup dumper" ; "1.8% assembler" ; "1.7% Fortran compiler" ; "1.6% remove file" ; "1.6% tape archive" ; "1.6% file system consistency check" ; "1.4% library maintainer" ; "1.3% concatenate/print files" ; "1.3% paginate and print file" ; "1.1% print disk usage" ; "1.0% copy file"
- P185 (block of 23 lines, verbatim): "15.3% editor" ; "9.6% list directory" ; "6.3% remove file" ; "6.3% C compiler" ; "6.0% concatenate/print file" ; "6.0% users’ programs" ; "3.3% list people logged on system" ; "3.2% rename/move file" ; "3.1% file status" ; "1.8% library maintainer" ; "1.8% document formatter" ; "1.6% execute another command conditionally" ; "1.6% debugger" ; "1.6% Shell (used as a command)" ; "1.5% print disk availability" ; "1.4% list processes executing" ; "1.4% assembler" ; "1.4% print arguments" ; "1.2% copy file" ; "1.1% paginate and print file" ; "1.1% print current date/time" ; "1.1% file system consistency check" ; "1.0% tape archive"
- P187: "The time span is over one year with a very early vintage 11/45."
- P188: "There has been one loss of a file system (one disk out of five) caused by software inability to cope with a hard ware problem causing repeated power fail traps."
- P188: "Files on that disk were backed up three days."
- P189: "There is about one crash every other day; about two-thirds of them are caused by hardware-related difficulties such as power dips and inexplicable processor interrupts to random locations."
- P189: "The longest uninterrupted up time was about two weeks."
- P189: "Service calls average one every three weeks, but are heavily clustered."
- P189: "Total up time has been about 98 percent of our 24-hour, 365-day schedule."

### L2-03 — CPAN announcement (Hietaniemi, 1995)

URLs tried:
- https://blogs.perl.org/users/neilb/2015/08/cpan-is-20.html — HTTP 200, text/html, 13,681 B. Dumped link. "CPAN is 20!" by Neil Bowers, posted August 16, 2015. A secondary summary; saved as supplementary.
- https://groups.google.com/forum/#!msg/comp.lang.perl.announce/1qlLHdviZlY/hU90ubJHrf4J — HTTP 200, text/html, 21,218 B: JavaScript shell with no message text. This is the link Bowers gives for "officially announced CPAN on 26th October 1995".
- https://groups.google.com/g/comp.lang.perl.announce/c/1qlLHdviZlY — HTTP 429, 142 B. Same with /m/hU90ubJHrf4J — 429; with ?hl=en — 429; http://groups.google.com/groups?selm=46o5va$33f%40maureen.teleport.com (Message-ID cited in Bowers' history) — 429 after redirect; https://groups.google.com/d/msg/comp.lang.perl.announce/1qlLHdviZlY/hU90ubJHrf4J — 429. WebFetch on the /g/ URL — 429.
- https://groups.google.com/forum/message/raw?msg=comp.lang.perl.announce/1qlLHdviZlY/hU90ubJHrf4J — HTTP 404, 1,652 B. https://groups.google.com/group/comp.lang.perl.announce/msg/hU90ubJHrf4J?dmode=source&output=gplain — HTTP 400, 1,695 B.
- https://web.archive.org/web/2016/https://groups.google.com/forum/#!msg/... — HTTP 200, 230,555 B, resolves to the Google Groups front page ("To use Google Groups Discussions, please enable JavaScript"). https://web.archive.org/web/2008/http://groups.google.com/groups?selm=46o5va$33f%40maureen.teleport.com — HTTP 200, 220,038 B, same front page. https://web.archive.org/web/2020/https://groups.google.com/g/comp.lang.perl.announce/c/1qlLHdviZlY — 404, 4,688 B. https://web.archive.org/web/2012/http://groups.google.com/group/comp.lang.perl.announce/msg/hU90ubJHrf4J — 404, 4,704 B. http://archive.org/wayback/available?url=groups.google.com/groups?selm=... — 200, {"archived_snapshots": {}}.
- https://raw.githubusercontent.com/neilbowers/history-of-cpan/master/history.md — HTTP 200, text/plain, 28,491 B. Bowers' CPAN history (secondary); lists "Oct 26th: JHI announced CPAN to c.l.p.a" with the selm link above, and "1st August, JHI announced the 'CPAN private showing'". Not saved.
- https://www.cpan.org/misc/CPAN.ANNOUNCE — HTTP 200, 4,282 B (Last-Modified Wed, 26 Jul 1995 18:46:05 GMT). USED. Mirror https://erised.las.iastate.edu/CPAN/misc/CPAN.ANNOUNCE — HTTP 200, message/news, 4,282 B; byte-identical (cmp).
- https://www.cpan.org/misc/cpan-faq.html — HTTP 200, 52,674 B (no announcement text). https://www.cpan.org/misc/jhi-announce.txt — HTTP 404, 272 B. https://www.cpan.org/misc/ — HTTP 200, 3,958 B (directory index; CPAN.ANNOUNCE is its only announcement-named file).
- WebSearch, three queries (Hietaniemi + comp.lang.perl.announce + October 1995; the Message-ID; the announcement wording): none returned the text of a 26 October 1995 post; they returned the Bowers post, the cpan.org mirror of CPAN.ANNOUNCE, and secondary pages.

Saved copies:
- /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-03.txt — 638 words, 36 blocks; the whole message verbatim including its mail headers; this is NOT the 26 Oct 1995 post.
- /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-03-dumped-bowers.txt — 391 words; supplementary: what the dumped URL serves; not indexed below.

Authorship and year, from the text or hosting page: "Reply-to: Jarkko.Hietaniemi@hut.fi", "Organization: Helsinki University of Technology, Finland", sign-off "++jhi;", "Subject: CPAN \"private showing\"", "To: perl-packrats@feenix.metronet.com". Year: the message carries no Date header; its MIRRORING.FROM block is dated 1995; Bowers (not the text) dates the "private showing" 1 August 1995; HTTP Last-Modified of the file is 26 Jul 1995. The dumped URL is dated 2015 and written by Bowers.

Section headings in order:
- No section headings. Block P1 = mail headers (Organization, To, Cc, Subject, Reply-to, FCC, MIME-Version, Content-Type, Content-Transfer-Encoding, "--text follows this line--"); P14 starts the quoted MIRRORING.FROM file.

First sentence: "I finally decided let this thing loose" (P2; followed in P3 by "ftp.funet.fi:/pub/languages/perl/CPAN/").

Last sentence: "++jhi;" (P36, signature). Last prose sentence before the MIRRORING.FROM listing: "This the MIRRORING.FROM as it now stands:" (P13).

Not itemized: mail-header version number "MIME-Version: 1.0" and path and host strings.

Quantified claims (verbatim, with location):
- P5: "I will be leaving for a _long_ holiday starting the 7th of October, / will be non-Inet-connectible until the 10th of September."
- P5: "you have 7.5 weeks time to practise Comparative Perl Archaeology"
- P6: "like the idea of returning from the holiday AND after several days / of battling with my obscenely overflowing mailbox I would have to / wade through umpteen dozen little perl snippets in the incoming/." [vague quantifiers: "several days", "umpteen dozen"]
- P14 (block of 3 lines, verbatim): "---" ; "# Perl scripts from metronet" ; "# daily: last update Wed Jul 26 21:26:08 EET DST 1995"
- P16 (block of 2 lines, verbatim): "# CPAN ANLpasswd" ; "# weekly: last update Sat Jun 17 14:56:07 EET DST 1995"
- P18 (block of 2 lines, verbatim): "# CPAN Perl Byacc" ; "# weekly: last update Tue Jun 20 10:51:29 EET DST 1995"
- P20 (block of 2 lines, verbatim): "# CPAN Berkeley DB" ; "# weekly: last update Sun Jul  2 07:11:52 EET DST 1995"
- P22 (block of 2 lines, verbatim): "# CPAN FAQ" ; "# weekly: last update Wed Jul 26 07:06:45 EET DST 1995"
- P24 (block of 2 lines, verbatim): "# CPAN GNU DBM" ; "# weekly: last update Sun Jul  2 07:11:52 EET DST 1995"
- P26 (block of 2 lines, verbatim): "# CPAN metaFAQ" ; "# weekly: last update Wed Jul 26 07:06:45 EET DST 1995"
- P28 (block of 2 lines, verbatim): "# CPAN MSDOS Perl" ; "# weekly: last update Wed Jul 26 07:06:00 EET DST 1995"
- P30 (block of 2 lines, verbatim): "# CPAN O'Reilly" ; "# weekly: last update Sun Jul  2 07:12:58 EET DST 1995"
- P32 (block of 2 lines, verbatim): "# CPAN DBPerl" ; "# daily: last update Wed Jul 26 02:02:28 EET DST 1995"
- P34 (block of 2 lines, verbatim): "# CPAN MacPerl" ; "# weekly: last update Sun Jul 23 02:01:38 EET DST 1995"

### L2-04 — I've Just Liberated My Modules (Koçulu, 2016)

URLs tried:
- https://azerkoculu.com/posts/i-ve-just-liberated-my-modules — HTTP 200, text/html; charset=UTF-8, 11,786 B. USED. The author's own site; page shows "Azer Koçulu / Mar 23, 2016 / I've Just Liberated My Modules".
- https://medium.com/@azerbike/i-ve-just-liberated-my-modules-9045c06be67c — HTTP 403, text/html, 5,019 B.
- https://web.archive.org/web/2016/https://medium.com/@azerbike/i-ve-just-liberated-my-modules-9045c06be67c — first attempt: curl (35) connection reset by peer; second attempt: HTTP 200, text/html, 62,227 B (snapshot 20170104075253). Medium original, "Azer Koçulu / Mar 22, 2016", plus the line "Note: Thank you for all the support"; body word-for-word identical to the saved copy (233 tokens each). Cross-check only.
- https://github.com/azer — HTTP 403, application/json, 249 B (probe).

Saved copies:
- /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-04.txt — 233 words, 7 blocks.

Authorship and year, from the text or hosting page: Hosting page byline "Azer Koçulu" and date "Mar 23, 2016"; Medium snapshot byline "Azer Koçulu", "Homepage: http://azer.bike", date "Mar 22, 2016". Matches the dump's author and year 2016. The word "left-pad" does not occur in the text; it occurs in L2-05 (P50: "...a tiny package called left-pad, consisting of a single 8-line function body. They discovered this when the author of left-pad deleted that package from NPM...").

Section headings in order:
- No section headings. Blocks: P1-P7 are seven paragraphs; P7 is "Cheers.".

First sentence: "A few weeks ago a patent lawyer sent me an e-mail asking me to unpublish “kik” module from NPM." (P1).

Last sentence: "Cheers." (P7). Last substantive sentence: "You can either point your dependency to repo directly (azer/dependency) or if you volunteer to take ownership of any module in my Github, I’ll happily transfer the ownership." (P6).

No digits occur in the text. Scope statement without a number, for the record: "Summary; NPM is no longer a place that I’ll share my open source work at, so, I’ve just unpublished all my modules." (P4).

Quantified claims (verbatim, with location):
- P1: "A few weeks ago a patent lawyer sent me an e-mail asking me to unpublish “kik” module from NPM." [vague quantifier; the only time reference in the text]

### L2-05 — Our Software Dependency Problem (Cox, 2019)

URLs tried:
- https://research.swtch.com/deps — HTTP 200, text/html; charset=utf-8, 52,122 B. USED. Page header block: "Our Software Dependency Problem / Russ Cox / January 23, 2019 / research.swtch.com/deps"; "Posted on Wednesday, January 23, 2019."
- https://research.swtch.com/deps-cost.png — HTTP 200, image/png, 7,681 B, 383x95. The equation figure that follows P18; viewed and transcribed by hand into the saved copy as P19.

Saved copies:
- /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L2-05.txt — 5444 words, 117 blocks; includes References (P93-P115, one block per entry) and Coda (P116-P117); footnote-reference markers removed from running text; code listing in P9 kept.

Authorship and year, from the text or hosting page: Hosting page: byline "Russ Cox" (link rel=author to https://swtch.com/~rsc/), date "January 23, 2019". Matches the dump's author and year.

Section headings in order:
- P4: What is a dependency? (h2 in the page HTML)
- P12: What could go wrong? (h2 in the page HTML)
- P22: Inspect the dependency (h2 in the page HTML)
- P26: Design (h3 in the page HTML)
- P28: Code Quality (h3 in the page HTML)
- P32: Testing (h3 in the page HTML)
- P35: Debugging (h3 in the page HTML)
- P37: Maintenance (h3 in the page HTML)
- P40: Usage (h3 in the page HTML)
- P43: Security (h3 in the page HTML)
- P46: Licensing (h3 in the page HTML)
- P48: Dependencies (h3 in the page HTML)
- P51: Test the dependency (h2 in the page HTML)
- P54: Abstract the dependency (h2 in the page HTML)
- P58: Isolate the dependency (h2 in the page HTML)
- P61: Avoid the dependency (h2 in the page HTML)
- P65: Upgrade the dependency (h2 in the page HTML)
- P74: Watch your dependencies (h2 in the page HTML)
- P81: Conclusion (h2 in the page HTML)
- P92: References (h2 in the page HTML)
- P116: Coda (h2 in the page HTML)

First sentence: "For decades, discussion of software reuse was far more common than actual software reuse." (P1).

Last sentence: "Let’s work together to find out how to reuse it safely." (P91; last sentence of the body, before References). Last sentence of the file: "A version of this post was published in ACM Queue (March-April 2019) and then Communications of the ACM (August 2019) under the title “Surviving Software Dependencies.”" (P117).

Not itemized: list numbering, the 23 reference entries (P93-P115: titles, months and years, volume and page numbers, and URLs), and the figure transcription.

Quantified claims (verbatim, with location):
- P1: "For decades, discussion of software reuse was far more common than actual software reuse."
- P2: "My own background includes a decade of working with Google’s internal source code system, which treats software dependencies as a first-class concept, and also developing support for dependencies in the Go programming language."
- P8: "For example, the Node.js dependency manager NPM provides access to over 750,000 packages."
- P10: "Before dependency managers, publishing an eight-line code library would have been unthinkable: too much overhead for too little benefit."
- P10: "But NPM has driven the overhead approximately to zero, with the result that nearly-trivial functionality can be packaged and reused."
- P10: "In late January 2019, the escape-string-regexp package is explicitly depended upon by almost a thousand other NPM packages, not to mention all the packages developers write for their own use and don’t share."
- P11: "Maven Central (Java), Nuget (.NET), Packagist (PHP), PyPI (Python), and RubyGems (Ruby) each host over 100,000 packages."
- P11: "The arrival of this kind of fine-grained, widespread software reuse is one of the most consequential shifts in software development over the past two decades."
- P15: "Decades ago, most developers already trusted others to write software they depended on, such as operating systems and compilers."
- P16: "Many common early packages still enjoy good reputations: consider BLAS (published 1979), Netlib (1987), libjpeg (1991), LAPACK (1992), HP STL (1994), and zlib (1995)."
- P20: "At one end of the spectrum is a personal hobby project, where the cost of most bad outcomes is near zero: you’re just having fun, bugs have no real impact other than wasting some time, and even debugging them can be fun."
- P20: "So the risk probability almost doesn’t matter: it’s being multiplied by zero."
- P31: "For example, the SQLite library ships as a single 200,000-line C source file and a single 11,000-line header, the “amalgamation.”"
- P31: "The sheer size of these files should raise an initial red flag, but closer investigation would turn up the actual development source code, a traditional file tree with over a hundred C source files, tests, and support scripts."
- P33: "For example, the SQLite development tree has an incredibly thorough test suite with over 30,000 individual test cases as well as developer documentation explaining the testing strategy."
- P38: "Others are the result of thousands of hours of work by a group of paid developers."
- P45: "For example, when Jeff Dean and I started work on Google Code Search—grep over public source code—in 2006, the popular PCRE regular expression library seemed like an obvious choice."
- P50: "For example, in March 2016 the NPM user community discovered that many popular projects—including Babel, Ember, and React—all depended indirectly on a tiny package called left-pad, consisting of a single 8-line function body."
- P50: "For example, 30% of the 750,000 packages published on NPM depend—at least indirectly—on escape-string-regexp."
- P53: "When we found that, for one basic test case, pcregrep was 70X slower than the fastest grep available, we started to rethink our plan to use PCRE."
- P59: "When Chrome launched in 2008, it introduced the critical feature (now standard in all browsers) of isolating each extension in a sandbox running in a separate operating-system process."
- P60: "In November 2018, the latest version of the NPM package event-stream, which provided a functional streaming API for JavaScript events, was discovered to contain obfuscated malicious code that had been added two and a half months earlier."
- P63: "Later we rewrote the execution engine as well, so that no dependencies were left, and we open-sourced the result: RE2." [zero count]
- P66: "This analysis ignores two costs."
- P66: "In software, the difficulty of making code changes does not scale linearly: making ten small changes is less work and easier to get right than making one equivalent large change."
- P67: "For example, consider the year 2017 at Equifax, as recounted by executives in detailed congressional testimony."
- P67: "On March 7, a new vulnerability in Apache Struts was disclosed, and a patched version was released."
- P67: "On March 8, Equifax received a notice from US-CERT about the need to update any uses of Apache Struts."
- P67: "Equifax ran source code and network scans on March 9 and March 15, respectively; neither scan turned up a particular group of public-facing web servers."
- P67: "On May 13, attackers found the servers that Equifax’s security teams could not."
- P67: "They used the Apache Struts vulnerability to breach Equifax’s network and then steal detailed personal and financial information about 148 million people over the next two months."
- P67: "Equifax finally noticed the breach on July 29 and publicly disclosed it on September 4."
- P73: "In the aftermath of the Equifax breach, forensic security teams found evidence that attackers (perhaps different ones) had successfully exploited the Apache Struts vulnerability on the affected servers on March 10, only three days after it was publicly disclosed, but they’d only run a single whoami command."
- P76: "These kinds of checks prevented the event-stream attacker, described earlier, from silently inserting malicious code in the already-released version 3.3.5."
- P76: "Instead, the attacker had to create a new version, 3.3.6, and wait for people to upgrade (without looking closely at the changes)."
- P80: "For example, Apache Struts disclosed different major remote code execution vulnerabilities in 2016, 2017, and 2018."
- P84: "I offer three broad recommendations."
- P117: "A version of this post was published in ACM Queue (March-April 2019) and then Communications of the ACM (August 2019) under the title “Surviving Software Dependencies.”"

## Failures

- L2-03, the 26 October 1995 announcement by Hietaniemi to comp.lang.perl.announce (Message-ID <46o5va$33f@maureen.teleport.com>; Google Groups id 1qlLHdviZlY/hU90ubJHrf4J): NOT obtained. Tried: Google Groups /forum/#!msg, /g/, /d/msg, /groups?selm, forum/message/raw, ?output=gplain (results 200-JavaScript shell, 429, 404, 400); Wayback snapshots 2008, 2012, 2016, 2020 (Groups front page only, or 404); archive.org availability API (no snapshot); cpan.org/misc/ listing and cpan-faq.html; three WebSearch queries. Substitute saved: CPAN.ANNOUNCE, Hietaniemi's earlier mail to perl-packrats. The saved substitute carries no Date header; its date of 1 August 1995 comes from Bowers.
- L2-02, ACM original: https://dl.acm.org/doi/pdf/10.1145/361011.361061 returned 403; the copy used is Brewer's recreation, which states it keeps the original's errors. Visible artifacts kept in the saved text: "[l]" for "[1]" (P6), "l,048,576 (220)" (P62), "open flies" (P83), "‘to a command" (P104), "tile time" (P142), "tile password file" (P154), "Given the partiality antagonistic desires" (P166), "hard ware" (P188). The PDF text layer encoded ">" and "<" as U+232A and U+2329; the saved copy uses ">" and "<". Two line-break artifacts were repaired: "with- out" to "without" (P36) and "I/ O" to "I/O" (P63). Section 9 tables (P178-P185) were retyped from PDF coordinates.
- L2-02, dumped URL: nokia.com retro.pdf returned 403 live; only its Wayback copy was retrieved, and that copy is the Retrospective, not the 1974 paper.
- L2-01, Scribd wrapper (JavaScript viewer, 1.6 MB) not parsed; replaced by the Newcastle PDF. The Newcastle edition is an OCR reformatting of the 1969 report; the saved text keeps its OCR readings.
- L2-04, Medium original: live URL 403; Wayback snapshot fetched on the second attempt (first: connection reset by peer; the agent proxy logged ws_closed_mid_exchange for web.archive.org).
- No source in lane 2 failed outright; one (L2-03) is PARTIAL.
