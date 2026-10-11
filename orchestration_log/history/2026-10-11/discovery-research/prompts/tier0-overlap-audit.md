Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it.

ROLE: You are extracting every claim the existing manifesto collection already makes about code volume, code as cost or debt, dependencies, reuse, components, and ownership of borrowed code.

CONTEXT: A new manifesto is being discovered from substrate on those topics. The collection's rule is that a new manifesto must differentiate within the collection. The synthesis needs to know exactly what ground is already held, with locations.

INPUT FILES (read each in full): every file matching /home/user/LLM_MANIFESTOS/manifestos/*.md (12 files). Also /home/user/LLM_MANIFESTOS/archive/software_building_principles/*.md (4 files, pre-collection sources) for claims that were cut when the manifestos were made.

TASK:
1. For each file, extract every sentence or table row that asserts something about: code volume or line count; code as cost, debt, liability, or asset; deleting code; dependencies, packages, libraries, imports; reuse or components; ownership or trust of code one did not write; the economics of maintenance. One row per claim, verbatim quote of at most 25 words, file:line.
2. Tag each row with a topic from that list and with the manifesto's own stance in one word: for, against, conditional.
3. For each manifesto that holds three or more rows, state in one line what it already claims on these topics, as the text says it.
4. List the named enemies of all 12 manifestos (the thing each opposes, quoted from its enemy section or first section) with file:line.
5. List the taglines and titles of all 12 (frontmatter).
6. Write the report.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/collection-overlap-audit.md

REPORT FORMAT:
# Collection Overlap Audit — volume, debt, dependencies, reuse
(three binding lines)
## Claims — table: file | line | quote | topic | stance
## Held ground — one line per manifesto with 3+ rows
## Enemies — table: file | enemy (quote) | file:line
## Titles and taglines — table: file | title | tagline
## Counts — rows per topic, rows per file

SCOPE: Extract and locate. Do not judge whether a new manifesto would overlap. Do not recommend.

TOOLS: Read for files; Grep to locate lines; Write for the report.

End with a 3-sentence summary for a notification: row count, which manifesto holds the most ground on these topics, which topic no manifesto touches.
