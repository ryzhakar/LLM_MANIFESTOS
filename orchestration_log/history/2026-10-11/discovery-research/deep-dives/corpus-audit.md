# Corpus Audit — 12 manifestos
Binding, elements loaded: First Principles (/home/user/LLM_MANIFESTOS/manifestos/first-principles.md, 114 lines), Strunk SPR v3 (/home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml, 2923 lines), manifesto-oath binding protocol (/home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md); each read in full from source.  
Binding, interplay: both elements converge on the concrete, verified, uncluttered statement (atoms over analogy; omit needless words, positive form, emphatic end) and pull apart where First Principles discards inherited form while Strunk's Judgment Protocol keeps convention unless purpose demands deviation, and where table fragments strain Strunk's complete-sentence rule; resolution: take every figure from the text and never from the template's labels, and take Strunk's technical-documentation allowance for fragments in tables.  
Binding, commitments: I must derive each figure from the files and not from names or memory, and I will print file:line evidence for every judgment; I must omit needless words and keep the tables free of prose assessment, and I will write the notes as short active statements; I must not rate, recommend, or infer beyond the text, and I will not.

## Metrics table

| file | words | lines | sentences | mean sent words | max sent words | % sent >20 | ## sections | max section words | % sections >150 | tables | code blocks | 2nd-person /1k | hedge /1k | ALL-CAPS /1k | ! /1k | fragments /1k | imperative % |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cargo-cult-science.md | 3869 | 82 | 196 | 19.7 | 64 | 40.3 | 0 | n/a | n/a | 0 | 0 | 24.6 | 10.1 | 2.8 | 0.0 | 3.9 | 0.0 |
| correct-by-construction.md | 1063 | 290 | 153 | 5.9 | 27 | 2.0 | 11 | 227 | 18.2 | 2 | 9 | 37.6 | 0.9 | 5.6 | 0.0 | 58.3 | 16.3 |
| dry.md | 1250 | 225 | 177 | 6.0 | 23 | 0.6 | 14 | 155 | 7.1 | 3 | 1 | 25.6 | 2.4 | 12.0 | 0.0 | 64.0 | 20.9 |
| first-principles.md | 792 | 107 | 103 | 6.8 | 17 | 0.0 | 7 | 188 | 14.3 | 1 | 0 | 31.6 | 0.0 | 3.8 | 0.0 | 32.8 | 22.3 |
| intervention.md | 699 | 86 | 77 | 7.8 | 19 | 0.0 | 6 | 329 | 16.7 | 1 | 0 | 38.6 | 0.0 | 0.0 | 0.0 | 27.2 | 22.1 |
| kiss.md | 1766 | 312 | 207 | 7.1 | 47 | 2.4 | 10 | 477 | 60.0 | 5 | 0 | 35.1 | 1.7 | 5.7 | 0.0 | 40.2 | 19.8 |
| postgres.md | 5019 | 262 | 546 | 7.2 | 97 | 7.0 | 7 | 941 | 85.7 | 6 | 0 | 70.5 | 0.4 | 59.6 | 0.0 | 56.2 | 9.9 |
| self-documenting-code.md | 801 | 283 | 76 | 7.4 | 29 | 1.3 | 12 | 112 | 0.0 | 7 | 7 | 35.0 | 5.0 | 38.7 | 0.0 | 23.7 | 35.5 |
| simple-made-easy.md | 1452 | 198 | 198 | 6.9 | 22 | 0.5 | 9 | 447 | 33.3 | 1 | 0 | 53.7 | 0.7 | 2.1 | 0.0 | 44.1 | 19.2 |
| stop-yapping.md | 1140 | 124 | 219 | 4.5 | 28 | 1.8 | 7 | 232 | 42.9 | 1 | 0 | 81.6 | 10.5 | 60.5 | 9.6 | 134.2 | 21.5 |
| yagni.md | 1401 | 154 | 148 | 7.9 | 44 | 4.1 | 11 | 226 | 36.4 | 3 | 0 | 40.0 | 2.1 | 8.6 | 0.0 | 31.4 | 25.7 |
| zen-of-python.md | 105 | 17 | 16 | 6.6 | 13 | 0.0 | 0 | n/a | n/a | 0 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 28.6 | 0.0 |

## Judgment table

| file | opens on the enemy (yes/no; first ## heading; first sentence) | ends on a choice (yes/no; last non-attribution line) | boundary or exceptions section | attribution line (verbatim) | self-check or procedure section | reader addressed (one quoted sentence) | register (one word; one quoted sentence) |
|---|---|---|---|---|---|---|---|
| cargo-cult-science.md | no. H: none (no ##). S: L17 "During the Middle Ages there were all kinds of crazy ideas, such as that a piece of rhinoceros horn would increase potency." | no. L89 "May I also give you one last bit of advice: Never say that you’ll give a talk unless you know clearly what you’re going to talk about and more or less what you’re going to say." | none | L11 `*by RICHARD P. FEYNMAN*` | none | unspecified (human scientists, commencement audience). L57 "The first principle is that you must not fool yourself—and you are the easiest person to fool." | lecture. L51 "We have learned a lot from experience about how to handle some of the ways we fool ourselves." |
| correct-by-construction.md | yes. H: L17 "The Enemy". S: L19 "The industry worships quick starts." | no. Choice at L251 "The Choice" is followed by L267 "The Principles, Compressed" and L285 "The Final Word". L297 `*Encode your invariants. Trust the compiler. Ship with confidence.*` | none (nearest: L235 "What You Give Up", a cost list) | L13 `*After Tris Oaten's No Boilerplate series*` | L142 "The Workflow" | human engineer. L29 "The human brain cannot hold a distributed system in working memory." | declarative. L92 "Every value has exactly one owner." |
| dry.md | yes. H: L11 "The Enemy is Clear". S: L13 `**Knowledge duplication** is destroying your codebase.` | no. Choice at L201 "The Choice" is followed by L216 "The Declaration". L228 "Knowledge has one home. Find it. Protect it. Everything else is negotiable." | L179 "When Duplication is Acceptable" | L232 `*After Dave Thomas, Andy Hunt, Sandi Metz, Kent C. Dodds, Martin Fowler*` | L72 "The Test" | human engineer. L41 "You rush to extract a shared function." | declarative. L27 `**Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.**` |
| first-principles.md | no. H: L16 "The Blindness". S: L18 `**You are blind to function. You are obsessed with form.**` Enemy first named at L30 "The Enemy": L32 `Your enemy is **Reasoning by Analogy**.` | yes. L101 "The Choice". L114 `**Look at what is true.**` | none | L12 `*After Aristotle, Descartes, and Feynman*` | L63 "The Method: Violent Deconstruction" | unspecified. L47 "There are only two types of creators." | parable. L26 "We went to the moon before we put wheels on luggage." |
| intervention.md | yes. H: L11 "The Enemy". S: L13 "You are entering an environment where nothing can be trusted." | yes. L83 "The Choice". L93 `Choose.` | none | none | none (steps appear only inside L83 "The Choice", L89) | unspecified. L13 "You are entering an environment where nothing can be trusted." | parable. L19 "A forest's underground nutrient network has been hijacked by a pathogen." |
| kiss.md | yes. H: L16 "Name Your Enemy". S: L18 `**Complexity is killing your software.**` | yes. L287 "Your Choice". L315 `**Choose simplicity.**`; last line L319 `*Incidental is Latin for your fault.*` | L242 "When Complexity is Justified" | L12 `*After Rich Hickey, Kelly Johnson, and the engineers who understood that simple beats clever*` | L139 "Commands" | human engineer. L238 "If you don't understand it, don't merge it." | declarative. L97 "You cannot architect complexity upfront and succeed." |
| postgres.md | yes. H: first ## is L37 "I. THE SCHEMA IS THE ARCHITECTURE" (after the opening block). S: L11 `"I write an application that uses a database."` | yes. L259 "PICK". L269 `Pick.` | none (scope statements at L230 and L261 sit inside other sections) | none | none | human engineer. L263 "Monday you'll generate a schema from ORM models without reviewing it." | contemptuous. L31 "You ARE the database problem." |
| self-documenting-code.md | yes. H: L11 "The Enemy". S: L13 "Every comment in your codebase is an admission of defeat." | yes. L268 "The Choice". L290 "Every line of code you write is teaching someone about your domain. Make it a good teacher." | L33 "The Four Exceptions" | none | L241 "The Refactoring Checklist" | human engineer. L255 "Write code for your past self from six months ago." | lecture. L73 "This code tells you the entire business process." |
| simple-made-easy.md | yes. H: L15 "The Problem". S: L17 "We have a culture of complexity." | yes. L193 "The Choice". L205 `Choose.` | none | L11 `*After Rich Hickey*` | L154 "The Practice" | human engineer. L158 "Before you write anything, choose tools that produce simpler artifacts." | lecture. L128 "To abstract is to draw away — specifically, to draw away from the physical nature of something." |
| stop-yapping.md | yes. H: first ## is L27 "Look At Yourself" (after the opening block). S: L11 `"I'd be happy to help!"` then L13 "Shut up." | yes. L121 "Pick". L127 `Pick.` | none | L131 `*After the caveman compression protocol by Julius Brussee.*` | L93 "Before You Send" | the model. L13 "You're a program." | contemptuous. L65 "You're weak." |
| yagni.md | yes. H: L11 "Your Arrogance About The Future Is Destroying Your Software". S: L13 "You think you know what you'll need tomorrow." | yes. L145 "The Choice". L157 `Build for today. Let tomorrow take care of itself.` | L113 "When To Build For Tomorrow" | L161 `*After Kent Beck's YAGNI principle (You Aren't Gonna Need It), formalized in Extreme Programming and expanded by Martin Fowler, Ron Jeffries, Ward Cunningham, and the Lean Startup movement.*` | L105 "Commands" | human engineer. L15 "You design elaborate frameworks for flexibility you'll never use." | declarative. L44 "Presumptive features don't just waste time." |
| zen-of-python.md | no. H: none. S: L9 "Beautiful is better than ugly." | no. L24 `If the implementation is easy to explain, it may be a good idea.` | none (inline: L16 `Special cases aren't special enough to break the rules.`; L19 `Unless explicitly silenced.`) | none | none | unspecified. L20 "In the face of ambiguity, refuse the temptation to guess." | aphoristic. L10 "Explicit is better than implicit." |

## Method

**Script and population**

- Script: /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/corpus_metrics.py. Run `python3 -I corpus_metrics.py` (tables), `--json` (all values), `--sample` (hand-check sample), `--firstwords` (lexicon tuning aid). Standard library only. Every number in the Metrics table and in the hand-check and numerator tables comes from this script; the wc columns come from `wc` run as `LC_ALL=C wc` on the body (`tail -n +8`). Judgment columns come from reading all 12 files in full. Finding label (binding): every finding is practiced, measured or read from the shipped manifestos; the audit records no doctrine and no learned finding.
- Population: the 12 files in /home/user/LLM_MANIFESTOS/manifestos/*.md. Frontmatter (first `---` through second `---`, lines 1-7 in every file) is stripped before any measurement.
- Line classes: fenced code (``` to ```), table row (line starts `|`), heading (`#`), rule (`---`), blank, text.

**Definitions of the Metrics columns**

- words: tokens split on whitespace and em/en dashes, kept when they hold a letter or digit, over every body line outside fenced code (headings and table rows included; `|`, `---`, bare bullets and arrows are not words). Every per-1000 rate divides by this count; each numerator counts the same lines. Code-block words are listed separately below.
- lines: body lines after the frontmatter, blank lines and code lines included.
- Sentence splitter rule: each text line (not heading, table row, code line, rule, or blank) is a unit; list markers, `*`, edge `_` and backticks are stripped; a run of `.` `!` `?` followed by optional closing quotes or brackets, then whitespace or end of line, ends a sentence; terminators inside inline-code spans do not; the end of a unit always ends a sentence; Mr., Mrs., Ms., Dr., vs., e.g., i.e. and `Name X.` initials do not. A line with no terminal punctuation (list item, label, byline) counts as one sentence. Sentence words use the word rule above. The script found 0 places where an unterminated line is followed by a lowercase-initial line (no sentence wraps across lines).
- mean and max sentence words; % over 20 words: over the sentence list. fragments /1k: sentences of 4 words or fewer, per 1000 words (a rate, not a share of sentences).
- ## sections: headings of exactly level 2 (not `###`) outside code. A section runs to the next `##`; `###` text belongs to its parent. Section words: words on the lines after the `##` heading. Text before the first `##` is not a section (its words are listed below). max section words and % sections >150 are n/a where a file has no `##`. A subtitle written as `##` counts as a section (see Notes).
- tables: runs of consecutive `|` lines. code blocks: opening fences.
- 2nd-person /1k: tokens you, your, you're, yourself (case-insensitive; curly apostrophe normalised). you've, you'll, you'd, yours, yourselves are not in this column; the extended count is in the raw-count table.
- hedge /1k: whole-word, case-insensitive occurrences of: I think, perhaps, maybe, it seems, sort of, kind of, might, could, should consider, somewhat, quite. Occurrences inside quotation marks count in the column and are listed separately below.
- ALL-CAPS /1k: tokens of 3+ capital letters not adjacent to other letters (acronyms, SQL keywords, heading text and the Roman numeral III included). Split by location below.
- ! /1k: every `!` outside inline-code spans.

**Imperative heuristic and measured error rate**

- Heuristic (`is_imperative` in the script): after stripping leading quotes and punctuation and skipping one leading word from {actually, also, always, and, but, finally, first, instead, just, next, now, only, or, please, simply, so, still, then}, the sentence is imperative when its first word is never, stop or don't, or begins `do not`, or is one of 333 base-form verbs in the script's `BASE_VERBS` list (`do` followed by you/we/they/I/he/she/it is excluded as a question). Imperative % = imperative sentences / sentences.
- The verb list was extended against the first-word frequency list of the sentences it had not flagged (`--firstwords`), then frozen. The hand-check sample was drawn after the freeze.
- Hand-check protocol: per file, 10 sentences: 5 drawn from heuristic-yes and 5 from heuristic-no (shortfall filled from the other stratum: cargo-cult-science and zen-of-python have no heuristic-yes sentence, so all 10 come from heuristic-no); seeded `random.Random("manifesto-craft-tier0-corpus-audit:<file>")`; listed by `--sample`. Each sentence was judged by reading: imperative = grammatically an imperative clause (command form; quoted commands count by form). Labels live in `HAND_LABELS` in the script. Error = heuristic differs from the hand label.
- Measured error rate: 5 errors in 120 sentences (4.2%): 4 false positives, 1 false negative. Weighted by stratum size the estimated population error is 1.9%. Per-file figures follow. "est. population error %" = (false-positive rate among sampled heuristic-yes x heuristic-yes count + false-negative rate among sampled heuristic-no x heuristic-no count) / sentences. "est. true imperative %" = (heuristic-yes x (1 - false-positive rate) + heuristic-no x false-negative rate) / sentences. Each stratum holds at most 5 sampled sentences per file.
- Errors: false positives are kiss.md "Copy-paste now exceeds moved code for the first time in history" (noun compound), postgres.md "Read replicas for analytics." (adjective), stop-yapping.md `"Fix" not "remediate."` and `"Use" not "utilize."` (quoted words, no command). The false negative is zen-of-python.md "In the face of ambiguity, refuse the temptation to guess." (imperative after a fronted phrase; the task definition counts sentence-initial verbs only, so this class is outside the count by construction).

| file | sampled | heuristic-yes sampled | false pos | false neg | errors /10 | est. population error % | heuristic imperative % | est. true imperative % |
|---|---|---|---|---|---|---|---|---|
| cargo-cult-science.md | 10 | 0 | 0 | 0 | 0/10 | 0.0 | 0.0 | 0.0 |
| correct-by-construction.md | 10 | 5 | 0 | 0 | 0/10 | 0.0 | 16.3 | 16.3 |
| dry.md | 10 | 5 | 0 | 0 | 0/10 | 0.0 | 20.9 | 20.9 |
| first-principles.md | 10 | 5 | 0 | 0 | 0/10 | 0.0 | 22.3 | 22.3 |
| intervention.md | 10 | 5 | 0 | 0 | 0/10 | 0.0 | 22.1 | 22.1 |
| kiss.md | 10 | 5 | 1 | 0 | 1/10 | 4.0 | 19.8 | 15.8 |
| postgres.md | 10 | 5 | 1 | 0 | 1/10 | 2.0 | 9.9 | 7.9 |
| self-documenting-code.md | 10 | 5 | 0 | 0 | 0/10 | 0.0 | 35.5 | 35.5 |
| simple-made-easy.md | 10 | 5 | 0 | 0 | 0/10 | 0.0 | 19.2 | 19.2 |
| stop-yapping.md | 10 | 5 | 2 | 0 | 2/10 | 8.6 | 21.5 | 12.9 |
| yagni.md | 10 | 5 | 0 | 0 | 0/10 | 0.0 | 25.7 | 25.7 |
| zen-of-python.md | 10 | 0 | 0 | 1 | 1/10 | 10.0 | 0.0 | 10.0 |
| ALL | 120 | | 4 | 1 | 5/120 | 1.9 | | |

**Numerators and cross-check**

| file | sentences | 2nd-person core | 2nd-person extended | hedge hits | hedge hits in quotes | ALL-CAPS hits | caps in headings | caps in backticks | caps other | ! count | fragments (<=4 words) | imperative sentences | lines without terminal punctuation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cargo-cult-science.md | 196 | 95 | 101 | 39 | 2 | 11 | 3 | 0 | 8 | 0 | 15 | 0 | 1 |
| correct-by-construction.md | 153 | 40 | 40 | 1 | 1 | 6 | 2 | 0 | 4 | 0 | 62 | 25 | 17 |
| dry.md | 177 | 32 | 34 | 3 | 1 | 15 | 1 | 0 | 14 | 0 | 80 | 37 | 6 |
| first-principles.md | 103 | 25 | 25 | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 26 | 23 | 2 |
| intervention.md | 77 | 27 | 28 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 19 | 17 | 0 |
| kiss.md | 207 | 62 | 67 | 3 | 1 | 10 | 1 | 0 | 9 | 0 | 71 | 41 | 35 |
| postgres.md | 546 | 354 | 390 | 2 | 0 | 299 | 27 | 58 | 214 | 0 | 282 | 54 | 0 |
| self-documenting-code.md | 76 | 28 | 30 | 4 | 1 | 31 | 2 | 22 | 7 | 0 | 19 | 27 | 35 |
| simple-made-easy.md | 198 | 78 | 78 | 1 | 0 | 3 | 0 | 0 | 3 | 0 | 64 | 38 | 2 |
| stop-yapping.md | 219 | 93 | 96 | 12 | 12 | 69 | 2 | 0 | 67 | 11 | 153 | 47 | 0 |
| yagni.md | 148 | 56 | 61 | 3 | 2 | 12 | 0 | 0 | 12 | 0 | 44 | 38 | 2 |
| zen-of-python.md | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |

| file | script words | code-block words (outside words) | wc -w of body | words before first ## | script lines | wc -l of body |
|---|---|---|---|---|---|---|
| cargo-cult-science.md | 3869 | 0 | 3820 | 3869 | 82 | 82 |
| correct-by-construction.md | 1063 | 123 | 1337 | 3 | 290 | 290 |
| dry.md | 1250 | 28 | 1365 | 5 | 225 | 225 |
| first-principles.md | 792 | 0 | 831 | 3 | 107 | 107 |
| intervention.md | 699 | 0 | 729 | 5 | 86 | 86 |
| kiss.md | 1766 | 0 | 1904 | 1 | 312 | 312 |
| postgres.md | 5019 | 0 | 5219 | 498 | 262 | 262 |
| self-documenting-code.md | 801 | 154 | 1131 | 2 | 283 | 283 |
| simple-made-easy.md | 1452 | 0 | 1521 | 6 | 198 | 198 |
| stop-yapping.md | 1140 | 0 | 1189 | 197 | 124 | 124 |
| yagni.md | 1401 | 0 | 1469 | 3 | 154 | 154 |
| zen-of-python.md | 105 | 0 | 105 | 105 | 17 | 16 |

- wc -w (C locale) counts every whitespace token (including `|`, `---`, bullets, arrows, code) and does not split on dashes, so it differs from script words by those tokens; under a UTF-8 locale wc also counts standalone non-ASCII tokens (such as a spaced em dash) and returns higher totals. wc -l of the body equals script lines except in zen-of-python.md, whose last line has no newline.

**Excluded**

- Frontmatter. Fenced code lines (from words, rates and sentences; they count in lines). Headings, table rows, rules and code from the sentence list (table rows and headings stay in words and rates). Attribution lines, byline lines and quoted passages are not excluded; each counts as sentences.

**Definitions of the Judgment columns** (all by reading; evidence is file:line)

- opens on the enemy: yes when the first sentence of the body or the first `##` heading names or attacks the doctrine's adversary; no otherwise. The cited heading is the first `##` heading; the cited sentence is the first sentence of the body.
- ends on a choice: yes when the closing section presents a fork or commands the reader to choose and no later section adds argument; the cited line is the last line that is not an attribution.
- boundary or exceptions section: a heading whose section states where the rule does not apply. Attribution line: a line crediting the source author, copied verbatim. Self-check or procedure section: a heading whose section holds numbered steps, a checklist, or a test question.
- reader addressed: "the model" when the text says the reader is a program or AI; "a human engineer" when it names engineering roles or acts (merge, PR, schema, frameworks); otherwise unspecified.
- register, one of: declarative (plain claims with evidence), parable (an extended story or archetype carries the text), contemptuous (the text insults the reader), lecture (explanatory teaching voice), aphoristic (compressed maxims are the unit). Chosen by the dominant mode of the paragraphs.

## Notes

**cargo-cult-science.md**

- No `##` heading; all 3869 words sit in one unsectioned block (L9-L89), so the two section columns are n/a.
- Hedge hits 39 (could 12, kind of 12, might 5, I think 4, maybe 3, it seems 2, quite 1); 2 inside quotation marks. Extended 2nd-person count 101 against core 95.

**correct-by-construction.md**

- L11 "The Rust Correctness Manifesto" is a 6-word subtitle written as `##` and counts as a section; 3 of 11 sections hold under 20 words (L11, L235, L242).
- 9 code blocks hold 123 words (outside words and rates); 17 lines lack terminal punctuation (labels such as `Bad:` L51, list items).

**dry.md**

- Only "The Modern Threats" (L137) exceeds 150 words (155); the next longest is "The Opposite Disaster" (138).
- 1 code block holds 28 words (outside rates); 6 lines lack terminal punctuation; extended 2nd-person 34 against core 32.

**first-principles.md**

- L10 "The Manifesto of the Chef" is a 5-word subtitle written as `##` and counts as a section (1 of 7 under 20 words).
- Only "The Method: Violent Deconstruction" (L63) exceeds 150 words (188). All 3 ALL-CAPS hits sit in the H1 title (L9).

**intervention.md**

- Longest section "What Is True" (L25) holds 329 words across five `###` subsections; the other five sections hold 85 or fewer.
- 0 ALL-CAPS tokens, 0 hedge tokens, 0 `!`.

**kiss.md**

- L10 "A Manifesto Against Braided Code" is a 14-word subtitle written as `##` and counts as a section (1 of 10 under 20 words).
- "Commands" (L139) holds 477 words. The 47-word maximum sentence belongs to the Rob Pike quotation at L281.
- 35 lines lack terminal punctuation (bullets, labels); extended 2nd-person 67 against core 62.

**postgres.md**

- 498 of 5019 words precede the first `##` (L9-L33). Longest section "IV. NOTHING IS FREE" (L147) holds 941 words; longest sentence 97 words (L114).
- ALL-CAPS 299 hits: 27 in headings, 58 in backticks, 214 elsewhere; the numeral `III` (L110) counts as 1 hit.
- Extended 2nd-person 390 against core 354.

**self-documenting-code.md**

- 7 code blocks hold 154 words (outside words and rates). ALL-CAPS 31 hits: 22 in backticks (table cells L40-L41, L81-L82), 2 in headings, 7 elsewhere.
- 35 lines lack terminal punctuation (list items, table captions); longest section is "The Choice" (L268) at 112 words, so 0 of 12 sections exceed 150.

**simple-made-easy.md**

- L190 `_- Leonardo da Vinci_` credits the quotation at L189, not the manifesto; it is not the attribution line cited.
- Longest section "The Principles" (L106) holds 447 words; "The Practice" (L154) 259.

**stop-yapping.md**

- All 12 hedge hits sit inside quotation marks. 197 of 1140 words precede the first `##` (L9-L23).
- Sentences over 15 words: 5 of 219. Article tokens (a, an, the): 56 (49.1 per 1000 words). `!` count 11.

**yagni.md**

- Longest section "The Four Costs That Compound Into Bankruptcy" (L42) holds 226 words; 4 of 11 sections exceed 150 (226, 153, 152, 159).
- 2 of 3 hedge hits sit inside quotation marks. Three attributed quotations (L137-L141) count as sentences.

**zen-of-python.md**

- No heading of any level; 16 lines, one sentence each; 0 second-person tokens.
- No attribution in the body; frontmatter L6 names "Tim Peters". The last line (L24) has no newline.
