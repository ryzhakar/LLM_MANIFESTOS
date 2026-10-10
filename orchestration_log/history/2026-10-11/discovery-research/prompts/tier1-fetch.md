Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it.

ROLE: You are fetching primary texts for one lane of a source dump and writing a factual index of them.

CONTEXT: The dump is /home/user/LLM_MANIFESTOS/research/manifesto-craft/sources.md. Links may be mirrors, paywalls, or wrong. Later agents read only the local copies you save, so each copy must be the full primary text, cleanly extracted, with provenance recorded. Outbound HTTPS runs through a proxy already configured in the environment; use `curl -sSL --max-time 60`. For PDFs use `pdftotext -layout` if installed, else `python3 -I -c` with pypdf if importable, else record the failure.

INPUT FILES: /home/user/LLM_MANIFESTOS/research/manifesto-craft/sources.md — your lane is named in the launch prompt.

TASK, per source ID in your lane:
1. Fetch the dumped link. Record HTTP status, content type, byte size.
2. If the fetch fails, returns a wrapper page, a login wall, or a document that is not the named text, find the canonical primary text with WebSearch (author's own site, publisher, university archive, archive.org snapshot) and fetch that. Record every URL tried.
3. Extract the text body (strip navigation, comments, boilerplate). For a collection document (the NATO 1968 report, a retrospective PDF) extract only the named paper, and record its page range. Save to /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/{ID}.txt with a 6-line header: ID, title, author, year, URL fetched, extraction method.
4. Confirm authorship and year from the text itself or the hosting page; note any discrepancy with the dump.
5. Record: word count; the text's own section headings in order; the first sentence and the last sentence verbatim; every quantified claim in the text (numbers, dates, counts) as a list of verbatim quotes with their location (paragraph index or page).
6. Write the index.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/index-{lane}.md (lane as named in the launch prompt: lane1 or lane2)

REPORT FORMAT:
# Source Index — {lane}
(three binding lines)
## Fetch table — ID | title | author | year | URL fetched | status (FULL / PARTIAL / FAILED) | words | local path | discrepancy with dump
## Per-source — for each ID: URLs tried with status; section headings in order; first sentence; last sentence; quantified claims (verbatim, with location)
## Failures — what could not be obtained and what was tried

SCOPE: Fetch, extract, record. Do not summarize the argument. Do not interpret. Do not read the other lane.

TOOLS: Bash for curl, pdftotext, python3 -I, wc; WebSearch and WebFetch to locate alternates; Write for the text copies and the index.

End with a 3-sentence summary for a notification: sources obtained in full, sources partial or failed, the one discrepancy with the dump that matters most.
