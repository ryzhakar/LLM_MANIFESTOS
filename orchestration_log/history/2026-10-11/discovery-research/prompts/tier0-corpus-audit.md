Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it.

ROLE: You are measuring the twelve shipped manifestos of a collection to produce a quantified corpus profile.

CONTEXT: The collection is /home/user/LLM_MANIFESTOS/manifestos/*.md (12 files, YAML frontmatter then markdown body). A later synthesis compares these measurements against the collection's stated rules. Measurements must be reproducible; judgment columns must state their method.

INPUT FILES: every file matching /home/user/LLM_MANIFESTOS/manifestos/*.md. Read each in full.

TASK:
1. Write a Python script to /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/corpus_metrics.py and run it with `python3 -I`. Strip frontmatter before measuring. Per file compute: words; lines; sentences (split on . ! ? followed by space or newline; ignore table rows and code blocks); mean and max sentence words; percent of sentences over 20 words; count of `##` sections; max section words; percent of sections over 150 words; table count; code-block count; second-person tokens (you, your, you're, yourself) per 1000 words; hedge tokens (I think, perhaps, maybe, it seems, sort of, kind of, might, could, should consider, somewhat, quite) per 1000 words; ALL-CAPS words of 3+ letters per 1000 words; exclamation marks per 1000 words; sentence fragments (sentences with no finite verb — approximate: sentences of 4 words or fewer) per 1000 words.
2. Classify each sentence as imperative or not. Method: a sentence is imperative when it starts with a base-form verb or with "Do not"/"Never"/"Stop". Implement a heuristic in the script, then hand-check 10 sentences per file and report the heuristic's error rate. Report imperative percent per file.
3. Judgment columns, by reading: opens on the enemy (yes/no, plus the first heading or first sentence); ends on a choice (yes/no, plus the last non-attribution line); boundary or exceptions section (its heading, or none); attribution line (verbatim, or none); self-check or procedure section (its heading, or none); reader addressed (the model / a human engineer / unspecified, with one quoted sentence as evidence); register (one word: declarative, parable, contemptuous, lecture, aphoristic) with one quoted sentence as evidence.
4. Write the report.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/corpus-audit.md

REPORT FORMAT:
# Corpus Audit — 12 manifestos
(three binding lines)
## Metrics table — one row per file, one column per metric from step 1 and the imperative percent from step 2
## Judgment table — one row per file, one column per item in step 3
## Method — the script path, the sentence splitter rule, the imperative heuristic and its measured error rate, anything excluded
## Notes — at most three lines per file for anything the tables cannot hold
Tables only; no prose assessment of quality.

SCOPE: Measure and classify. Do not rate quality. Do not recommend. Do not read any file outside the manifestos directory except the binding elements.

TOOLS: Read for files; Bash for `python3 -I` and `wc`; Write for the script and the report.

End with a 3-sentence summary for a notification: files measured, the widest spread you found, any metric you could not compute.
