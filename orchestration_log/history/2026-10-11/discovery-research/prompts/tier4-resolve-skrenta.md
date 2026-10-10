Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it.

ROLE: You are resolving a contradiction between two research agents about the Skrenta 2007 text (source L1-04) and, if the fuller copy is authentic, promoting it to the primary copy.

THE CONTRADICTION: The lane-1 fetcher reported web.archive.org blocked by egress policy (HTTP 403, hostname_blocked) and saved only Atwood's two-paragraph quotation as recon/sources/L1-04.txt (PARTIAL). The evidence surveyor later reported fetching a Wayback copy of Skrenta's original, dated 30 May 2007, saved at recon/discovery/evidence/skrenta-wayback.txt, containing paragraphs L1-04.txt omits.

INPUT FILES:
1. /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L1-04.txt
2. /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/discovery/evidence/skrenta-wayback.txt
3. /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/index-lane1.md — the L1-04 section only
4. /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/evidence.md — grep "skrenta-wayback" and read only those lines and the fetch-method note near them

TASK:
1. Establish how the Wayback copy was obtained (URL, method, date) from input 4 and from any header in input 2. Try the same fetch once yourself with `curl -sSL --max-time 60`; record status. Do not try other routes.
2. Check authenticity: the two Atwood-quoted paragraphs must appear verbatim inside the fuller copy; the page must carry Skrenta's byline and the 2007 date; record each check.
3. If authentic: write /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L1-04-full.txt with the standard 6-line header (ID L1-04, title, author, year, URL fetched, extraction method) and the full body; record word count, section headings, first and last sentence, and every quantified claim verbatim with paragraph index. Leave L1-04.txt untouched.
4. Write the resolution.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/skrenta-resolution.md

REPORT FORMAT:
(three binding lines)
# L1-04 Skrenta — Contradiction Resolution
## The contradiction — both claims as reported
## Checks — table: check | result | evidence
## Verdict — which report is right about reachability, and whether L1-04-full.txt is now the primary copy
## L1-04-full index entry — the same fields the lane index carries, or "not promoted" with the reason

SCOPE: This source only. No interpretation of the text's argument.

TOOLS: Read; Bash for curl, wc; Write.

End with a 3-sentence summary for a notification: verdict, whether the full copy was promoted, its word count.
