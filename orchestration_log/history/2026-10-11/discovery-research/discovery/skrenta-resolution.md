Loaded in full from source: First Principles manifesto v1.0.1 (/home/user/LLM_MANIFESTOS/manifestos/first-principles.md), Strunk SPR v3.0 (/home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml, 2923 lines through `</instruction_matrix>`), manifesto-oath SKILL.md (/home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md).
Interplay: First Principles ("Verify the Irreducible", "Doubt the Form") and Strunk ("definite, specific, concrete"; "omit needless words") converge on the atom over the label, so each report becomes a claim to re-derive from the bytes; the pull between Strunk's judgment protocol and the research rule against conclusions resolves to quoted evidence with file:line and a verdict that names only what the checks show.
Commitments: I must re-fetch and re-check before I credit either report, and I will record every status, byte count, and quote with its location; I must not infer a cause I did not test, and I will not write a recommendation; I must omit needless words, and I will state each result in active, positive, concrete form.

# L1-04 Skrenta — Contradiction Resolution

Paths: S = /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/; EV = /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/discovery/evidence/; BR = /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/discovery/breadth/. Location convention: P{n} is the nth body paragraph; P{n} sits at line 6+2n of S/L1-04-full.txt.

## The contradiction — both claims as reported

**Lane-1 fetcher** (learned; /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/index-lane1.md:137-138, 205). Web.archive.org is blocked.
- Two curl URLs, both `http://` with the `id_` flag: `http://web.archive.org/web/20070602152648id_/http://www.skrenta.com:80/2007/05/code_is_our_enemy.html` and `http://web.archive.org/web/20230330091854id_/http://www.skrenta.com/2007/05/code_is_our_enemy.html` -> "HTTP 403, body "Blocked by egress policy", header x-block-reason: hostname_blocked" (index-lane1.md:137).
- WebFetch of the `https://` snapshot URL -> "Claude Code is unable to fetch from web.archive.org" (index-lane1.md:138).
- Summary: "web.archive.org returns HTTP 403 'Blocked by egress policy' ... to curl and WebFetch" (index-lane1.md:205).
- Result: S/L1-04.txt holds Atwood's two-paragraph quotation; status PARTIAL; 148 words (index-lane1.md:15).
- The index records no curl attempt on the `https://` non-`id_` URL.

**Evidence surveyor** (learned; /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/evidence.md:46, 157, 446).
- Fetched `https://web.archive.org/web/20070602152648/http://www.skrenta.com/2007/05/code_is_our_enemy.html`; saved as EV/skrenta-wayback.txt (evidence.md:46, kind "ADJACENT (archive of author page)").
- Reports a paragraph the L1-04 copy omits: "Furthermore, more code often means less flexibility and functionality." (evidence.md:157; EV/skrenta-wayback.txt:18).
- Holds the page apart from L1-04: "the archived Skrenta page (skrenta-wayback.txt) is a separate text, not a repair of the L1-04 copy" (evidence.md:446).
- evidence.md carries no fetch-method note near line 46, 157, or 446; its summary says only "fetched 25 second-source texts" (evidence.md:7). EV/skrenta-wayback.txt has no header.

## Checks — table: check | result | evidence

Every row is practiced: observed in the files or in my own fetch.

| check | result | evidence |
|---|---|---|
| 1. Method, URL, date of the surveyor's copy | URL known; client unrecorded; time recovered from the Wayback footer | URL: evidence.md:46. Footer in EV/skrenta-wayback.html:483-484: "FILE ARCHIVED ON 15:26:48 Jun 02, 2007 AND RETRIEVED FROM THE INTERNET ARCHIVE ON 10:56:42 Oct 11, 2026." File mtimes: .html 10:56:42, .txt 10:56:49 on 11 Oct 2026. EV/skrenta-wayback.txt starts "Code is our enemy (Skrentablog)" with no header. |
| 2. My fetch, same URL, once | HTTP 200 | `curl -sSL --max-time 60 https://web.archive.org/web/20070602152648/http://www.skrenta.com/2007/05/code_is_our_enemy.html` at 2026-10-11T11:21:29Z: http_code=200, size_download=28705, content_type "text/html; charset=ISO-8859-1", num_redirects=0, curl exit 0. Headers: "memento-datetime: Sat, 02 Jun 2007 15:26:48 GMT"; "x-archive-orig-date: Sat, 02 Jun 2007 15:26:48 GMT"; "x-archive-src: 42_0_20070602103233_crawl30-c/42_0_20070602152607_crawl29.arc.gz". No other route tried. |
| 3. Stored copy against my copy | same page | `cmp` of EV/skrenta-wayback.html (28704 bytes) and my 28705-byte file differs at two places only: the retrieval stamp (line 484: 10:56:42 against 11:21:30) and the playback-timing comment (lines 492-500). The entry-body extract (21 paragraphs, 825 words) is identical. BR/skrenta-2007-wayback.html (retrieved 11:02:15 per its line 484; cited at discovery/breadth.md:56, 158, 179; read for comparison only, not fetched) yields the same 21 paragraphs. |
| 4. Atwood paragraph 1 (S/L1-04.txt:8) verbatim inside the full copy | PASS, one character differs | The text equals P1 + " " + P2 (S/L1-04-full.txt:8, 10). 9 of 9 sentences found. One character differs: "there’s" with U+2019 in S/L1-04.txt:8 against "there's" with U+0027 in EV/skrenta-wayback.txt:16. |
| 5. Atwood paragraph 2 (S/L1-04.txt:10) verbatim inside the full copy | PASS, exact | The text equals P4 + " " + P5 (S/L1-04-full.txt:14, 16), character for character. 7 of 7 sentences found. The archived HTML italicises "in terms of the expressive power of the code they write" (EV/skrenta-wayback.html:104); S/L1-04.txt carries no markup. |
| 6. What L1-04.txt omits | P3 and P6-P21, no ellipsis | S/L1-04.txt body = 148 words = P1 + P2 + P4 + P5 (26 + 44 + 37 + 41). P3 (S/L1-04-full.txt:12) sits between Atwood's two quoted paragraphs: "Furthermore, more code often means less flexibility and functionality." `grep -c Furthermore S/L1-04.txt` = 0. Atwood's link text "code is our enemy" targets the fetched URL (EV/atwood-links.html:289: `href="https://web.archive.org/web/20070602152648/http://www.skrenta.com/2007/05/code_is_our_enemy.html"`). |
| 7. Skrenta's byline | PARTIAL: blog name and host present; personal name absent | "Rich" occurs 0 times in EV/skrenta-wayback.html (`grep -c -i -w rich`); "Skrenta" occurs in the page only as "Skrentablog" (`<title>Code is our enemy (Skrentablog)</title>`, h1 banner, EV/skrenta-wayback.txt:1, 3) and in host www.skrenta.com; `dc:creator=""` (EV/skrenta-wayback.html:41). The name "Rich Skrenta" comes from S/L1-05.txt:8: "Rich Skrenta writes that code is our enemy." |
| 8. 2007 date | PASS | "Posted on May 30, 2007  3:11 PM" (EV/skrenta-wayback.html:217; EV/skrenta-wayback.txt:103); `dc:date="2007-05-30T15:11:17-08:00"` (EV/skrenta-wayback.html:42); capture 2 June 2007 15:26:48 GMT (check 2); comment stamps run May 30, 2007 4:41 PM to June 1, 2007 1:14 PM (EV/skrenta-wayback.txt:124, 188). |

## Verdict — which report is right about reachability, and whether L1-04-full.txt is now the primary copy

**Reachability.** Web.archive.org served the snapshot over `https://` with HTTP 200 on 11 Oct 2026 at 10:56:42 (surveyor), 11:02:15 (breadth scout), and 11:21:30 (this fetch); lane 2 also reached it over `https://` with HTTP 200 at 10:42-10:50 (/home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/index-lane2.md:80, 86). The surveyor's report stands. The lane-1 record stands for the routes it names: two `http://` `id_` URLs returned 403, and WebFetch refused. Its general statement that web.archive.org returns 403 "to curl" (index-lane1.md:205) fails for `https://` without `id_`. The cause of lane 1's 403 stays undetermined: scheme, `id_` flag, client, and time of day all differ between the failed and the successful fetches, and I tested only the `https://` route, as instructed.

**Authenticity.** The Atwood paragraphs sit verbatim in the page (checks 4, 5; one apostrophe glyph differs); Atwood links to this exact snapshot (check 6); the page carries the date 30 May 2007 (check 8). The byline check passes at the level of the blog name and host and fails at the level of a personal name (check 7); the personal name rests on L1-05.txt:8.

**Primary copy.** S/L1-04-full.txt is written and is now the primary copy of L1-04 text: 825 words against 148, a superset of S/L1-04.txt. S/L1-04.txt is untouched (md5 3bfb7855514c265f1e3f5c7bb40be7a1 before and after), so every existing `L1-04.txt:8` and `L1-04.txt:10` reference stays valid. The surveyor's reading that the archived page "is a separate text, not a repair of the L1-04 copy" (evidence.md:446) no longer holds: the page contains the L1-04 text in full and is the same post.

## L1-04-full index entry — the same fields the lane index carries, or "not promoted" with the reason

Fetch-table row:

| ID | title | author | year | URL fetched | status | words | local path | discrepancy with dump |
|---|---|---|---|---|---|---|---|---|
| L1-04 | Code is our enemy | Rich Skrenta | 2007 | https://web.archive.org/web/20070602152648/http://www.skrenta.com/2007/05/code_is_our_enemy.html | FULL (post body; 5 reader comments dropped) | 825 | /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L1-04-full.txt | Dumped link http://www.skrenta.com/2007/05/code_is_our_enemy.html still 301s to LinkedIn (index-lane1.md:131); the Wayback capture of that URL serves the post. Page prints no personal byline (banner "Skrentablog"); name from L1-05. Year from the page footer, not the URL path. Dump note "Physical volume of code": "physical" occurs 0 times in the full body. |

### L1-04-full — Code is our enemy — Rich Skrenta (2007) — FULL

**URLs tried**
- https://web.archive.org/web/20070602152648/http://www.skrenta.com/2007/05/code_is_our_enemy.html -> HTTP 200, text/html; charset=ISO-8859-1, 28705 bytes, 0 redirects (curl -sSL --max-time 60, 2026-10-11T11:21:29Z). One fetch; no other route tried.
- Earlier retrievals of the same URL by other agents, method unrecorded: EV/skrenta-wayback.html 28704 bytes (10:56:42), BR/skrenta-2007-wayback.html 28703 bytes (11:02:15). Bodies identical to this fetch.

**Authorship and year, from the text or hosting page**
- Page: `<title>` "Code is our enemy (Skrentablog)"; banner "Skrentablog"; no personal byline; `dc:creator=""`. Name "Rich Skrenta" from S/L1-05.txt:8.
- Date: "Posted on May 30, 2007 3:11 PM"; `dc:date="2007-05-30T15:11:17-08:00"`; Wayback capture 2 June 2007 15:26:48 GMT.

**Section headings in order**
- None inside the post (page h2 is the title only). P9 (L1-04-full.txt:24) "Code has three lifetime performance curves:" introduces list items P10 (:26), P11 (:28), P14 (:34); P19 (:44) "Related:" introduces link-text items P20 (:46), P21 (:48).

**First sentence (verbatim)**
- "Code is bad."

**Last sentence (verbatim)**
- "I need to bake this some more but I think it's promising." (P18, L1-04-full.txt:42). The file closes with "Related:" and the link text "Kevin Burton", "be inflexibile".

**Quantified claims (verbatim; location = paragraph and file:line)**
- P4 (L1-04-full.txt:14): "Engineers have n^2 communication costs"
- P7 (L1-04-full.txt:20): "Maybe you can re-implement a 10k line solution into a 1k line solution"
- P9 (L1-04-full.txt:24): "Code has three lifetime performance curves:"
- P13 (L1-04-full.txt:32): "RAID is going to generate m management events for n disks."
- P13 (L1-04-full.txt:32): "As n grows, m grows."
- P13 (L1-04-full.txt:32): "10X the disk cluster, 10X the management events."
