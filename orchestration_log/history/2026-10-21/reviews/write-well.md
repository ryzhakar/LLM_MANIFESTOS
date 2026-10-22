# Maximalist Review: write-well

Rules: 106
Violations: 181
Verdict: VIOLATING
Manifesto: skill `agent-conduct:write-well` 1.10.0, `/Users/ryzhakar/.claudes/meta/plugins/cache/my-claude-skills/agent-conduct/1.10.0/skills/write-well/SKILL.md`
Target: `/Users/ryzhakar/LLM_MANIFESTOS/plugin/rulebooks/tone-of-voice.md` (whole file); `/Users/ryzhakar/LLM_MANIFESTOS/plugin/skills/manifesto-writing/SKILL.md` (the lines that `git -C /Users/ryzhakar/LLM_MANIFESTOS diff main -- plugin/skills/manifesto-writing/SKILL.md` adds: 14–17, 20, 24, 58, 62, 86, 87, 89, 92, 143)
Reviewed at: 2026-10-21T23:23:47Z

## Scope and counting

The dispatch puts three kinds of text out of scope: text inside quotation marks, table cells that are not sentences, and headings. Of the added lines in SKILL.md, lines 14 and 92 are headings, and lines 15 and 17 are blank. Nine added lines remain in scope. Bold labels that open list items count as text, though not as sentences.

One violation is one sentence that fails one rule. When a sentence fails a rule in several places, the sentence's row quotes every place. A sentence that fails two rules has a row under each. Rules R1 to R4 and R102 direct how the other rules apply; a line breaks those five only by breaking another rule, and that rule's row records the break. Under R5, I checked every line for a written exception to a rule and found none.

The rewrites take study names and figures from the rulebook's evidence section or from the research notes in `/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/history/2026-10-21/elevation-stack/research/`. Two details come from neither source: the name Kluger and DeNisi (1996) for line 12 and the intelligence ratings in Oppenheimer (2006) for line 62. As no file names the study behind line 57, its rewrite keeps a bracketed slot.

## Rules

Each rule quotes its source in write-well's `SKILL.md`; a rule that takes one demand from a two-demand sentence names that demand.

- **R1** (write-by-the-rules; write-well:4, 9): Write all prose by Strunk's rules of grammar, composition, and usage, and reread each draft against them, most serious fault first. / Apply every rule below to every sentence of prose you write, as you write it; never save the rules for a later edit.
- **R2** (write-by-the-rules; write-well:4, 11): Write all prose by Strunk's rules of grammar, composition, and usage, and reread each draft against them, most serious fault first. / Reread each finished draft against the rules in their order, most serious first; never send an unread draft.
- **R3** (write-by-the-rules; write-well:13): Fix every fault the reread finds, at every rank, each tag below being one rank; never leave a minor one.
- **R4** (write-by-the-rules; write-well:15; demand: obey each rule without exception): Obey each rule without exception; never write `this rule fits except here`.
- **R5** (write-by-the-rules; write-well:15; demand: never write an exception): Obey each rule without exception; never write `this rule fits except here`.
- **R6** (description; write-well:5): Use when the user says "/write-well", "write-well", "write well", or asks for prose held to Strunk's rules.
- **R7** (rank 1; write-well:19; examples write-well:24–29): Join two independent clauses, word groups that each have a subject and a verb and could stand as sentences, with a semicolon, a period, or a comma and a conjunction such as `and`; never with a comma alone. Examples: `The tests passed, then the build ran.` / `The tests passed; then the build ran.`
- **R8** (rank 1; write-well:21; examples write-well:24–29): Put a semicolon before `therefore`, `thus`, `then`, `accordingly`, or `besides` when it opens the second of two independent clauses; never a comma. Examples: `The tests passed, then the build ran.` / `The tests passed; then the build ran.`
- **R9** (rank 1; write-well:31; examples write-well:34–39): Make the subject after an opening descriptive phrase, such as `Walking home`, `A careful reviewer`, or `Tired and late`, the one that phrase describes; never let the phrase describe a later word. Examples: `Reading the log, the build failed at step three.` / `Reading the log, the reviewer saw the build fail at step three.`
- **R10** (rank 1; write-well:41): Recast every chain of passive verbs, verbs whose subject receives the action, such as `was ordered to be deleted`; never make one passive verb depend on another.
- **R11** (rank 1; write-well:43; examples write-well:46–51): Point every pronoun at a single noun the reader can name; never write one that two nouns could claim. Examples: `The service queries the cache before the database, and it times out.` / `The service queries the cache before the database, and the database times out.`
- **R12** (rank 1; write-well:53): Make every verb agree in number with its subject; never `the tests passes`.
- **R13** (rank 1; write-well:55): Give a plural verb to `that` or `who` after `one of the`, as in `one of the jobs that fail`; never `one of the jobs that fails`.
- **R14** (rank 2; write-well:59): Form the possessive of an ancient name ending in `-es` or `-is` with `of`, as in `the voyage of Ulysses`; never `Ulysses's voyage` or `Ulysses' voyage`.
- **R15** (rank 2; write-well:61): Form every other singular noun's possessive with `'s` whatever its last letter, as in `the boss's desk`; never with a bare apostrophe.
- **R16** (rank 2; write-well:63): Write `its`, `hers`, `ours`, `yours`, and `theirs` without an apostrophe; never `it's` for the possessive.
- **R17** (rank 2; write-well:65; examples write-well:68–73): Put a comma at each end of any interrupting words a reader could lift out; never at one end alone. Examples: `The rerun, however failed.` / `The rerun, however, failed.`
- **R18** (rank 2; write-well:75; demand: the year after a month and day): Put commas around the year after a month and day, the date after a weekday, and the abbreviations `etc.` and `jr.`; never drop the closing comma inside a sentence.
- **R19** (rank 2; write-well:75; demand: the date after a weekday): Put commas around the year after a month and day, the date after a weekday, and the abbreviations `etc.` and `jr.`; never drop the closing comma inside a sentence.
- **R20** (rank 2; write-well:75; demand: the abbreviations etc. and jr.): Put commas around the year after a month and day, the date after a weekday, and the abbreviations `etc.` and `jr.`; never drop the closing comma inside a sentence.
- **R21** (rank 2; write-well:77; demand: commas around a clause that adds a fact): Put commas around a clause that adds a fact about a thing already named and could stand alone; never around a clause that picks out which thing is meant.
- **R22** (rank 2; write-well:77; demand: no commas around a clause that picks out the thing): Put commas around a clause that adds a fact about a thing already named and could stand alone; never around a clause that picks out which thing is meant.
- **R23** (rank 2; write-well:79): Put a comma before a conjunction that joins two independent clauses; never run the two clauses together.
- **R24** (rank 2; write-well:81): When two clauses share a subject stated once, put a comma before `but`; never `I read the patch but am still unsure`.
- **R25** (rank 2; write-well:83): When an interrupting phrase or opening clause follows a conjunction, put the comma ahead of the conjunction; never between the conjunction and that phrase.
- **R26** (rank 2; write-well:85): Where `so` would mean `accordingly`, open the first clause with `as` or `since` instead; never write `The disk filled, so the job stopped`.
- **R27** (rank 2; write-well:87; examples write-well:90–95): Give every sentence a subject and a verb; never break one sentence in two with a period. Examples: `The migration finished at noon. Two hours late.` / `The migration finished at noon, two hours late.`
- **R28** (rank 2; write-well:97): Make the actor the subject and give it an active verb; never hide the actor behind a passive verb.
- **R29** (rank 2; write-well:99): Replace `there is`, `could be heard`, and every such hollow phrase with a verb that acts; never open with an empty `there is`.
- **R30** (rank 2; write-well:101; examples write-well:104–109): Name the definite, specific, concrete thing: the number, the place, the act; never a vague class such as `some issues`. Examples: `The service experienced a period of degraded performance.` / `For an hour, the service took eight seconds to answer each request.`
- **R31** (rank 2; write-well:111): In exposition and argument, ground every general claim in a named instance of it; never state a claim without one.
- **R32** (rank 2; write-well:113): Give each significant detail exactly; never blur a number or name that matters.
- **R33** (rank 2; write-well:115): Use `like` before a noun or pronoun and `as` before a clause; never `like` before a clause, as in `like I said`.
- **R34** (rank 3; write-well:119): Put a comma after each item but the last in a series of three or more, as in `logs, metrics, and traces`; never drop the comma before the conjunction.
- **R35** (rank 3; write-well:121; demand: one paragraph for each topic): Give each topic one paragraph and each paragraph one topic; never split a topic or crowd two into one.
- **R36** (rank 3; write-well:121; demand: one topic for each paragraph): Give each topic one paragraph and each paragraph one topic; never split a topic or crowd two into one.
- **R37** (rank 3; write-well:123): Open each paragraph with a sentence that states its topic; never hold the topic back to the middle.
- **R38** (rank 3; write-well:125): Develop the topic in every later sentence by restating, defining, illustrating, or proving it; never stray to a side matter.
- **R39** (rank 3; write-well:127): Close the paragraph by stressing the topic or stating its consequence; never on a digression or a trivial detail.
- **R40** (rank 3; write-well:129): Use `not` to deny or to set a false choice against the true one; never to dodge a plain statement.
- **R41** (rank 3; write-well:131): State what is in definite terms; never hedge in tame, noncommittal words.
- **R42** (rank 3; write-well:133): Replace `not` and a weak word with one word that carries the meaning, as in `late` for `not on time`; never keep the negated pair.
- **R43** (rank 3; write-well:135; demand: no idle word or sentence): Give every word and every sentence work to do; never keep an idle one or cut a working one.
- **R44** (rank 3; write-well:135; demand: no working word or sentence cut): Give every word and every sentence work to do; never keep an idle one or cut a working one.
- **R45** (rank 3; write-well:137): Strike `the fact that` from every sentence, as in `although` for `despite the fact that`; never `in view of the fact that`.
- **R46** (rank 3; write-well:139): Cut a padded phrase to its core, as in `whether` for `the question of whether`; never `at this point in time`.
- **R47** (rank 3; write-well:141): Drop `who is` and `which was` before a noun phrase, as in `Kim, our lead` for `Kim, who is our lead`; never `Lee, who is our tester`.
- **R48** (rank 3; write-well:143): Make the verb carry the action; never put the action in a noun and leave the verb to fill the slot, as in `carried out a review of`.
- **R49** (rank 3; write-well:145): Merge one idea that unfolds step by step across sentences into one sentence; never spread the idea out.
- **R50** (rank 3; write-well:147): Give ideas of equal rank and role the same grammatical form; never set a noun beside a clause in one series.
- **R51** (rank 3; write-well:149): Put an article or preposition shared by a series before the first item alone or before every item; never before some.
- **R52** (rank 3; write-well:151): Follow each part of a correlative set, such as `both … and`, `not … but`, `not only … but also`, `either … or`, or `first, second, third`, with the same construction; never follow one part with a verb and the other with a noun.
- **R53** (rank 3; write-well:153): Sort a long run of similar ideas into groups and make each group parallel; never force one pattern across the whole run.
- **R54** (rank 3; write-well:155; demand: related words together): Bring together words related in thought and keep apart words that are not; never let an unrelated phrase split a related pair.
- **R55** (rank 3; write-well:155; demand: unrelated words apart): Bring together words related in thought and keep apart words that are not; never let an unrelated phrase split a related pair.
- **R56** (rank 3; write-well:157): Move to the opening any phrase between subject and verb that can open the sentence, other than a relative clause, one opened by `who`, `which`, or `that`, or an appositive, a noun phrase renaming the noun before it; never leave a movable phrase between them.
- **R57** (rank 3; write-well:159): Put a relative pronoun such as `who`, `which`, or `that` right after the noun it refers to, and after the whole group when that noun is a group of words; never let other words come between.
- **R58** (rank 3; write-well:161): Put each modifier, a word that limits or describes another, next to the word it modifies; never where it can attach to another.
- **R59** (rank 3; write-well:163): Hold a summary to a single tense; never write `Ana opens the file and found the bug`.
- **R60** (rank 3; write-well:165): Summarize a play, story, poem, or novel in the present tense; never `the heroine fled`.
- **R61** (rank 3; write-well:167): Put action earlier than a present-tense summary in the perfect, the tense formed with `has` or `have`, as in `has taken`; never in the simple past.
- **R62** (rank 3; write-well:169): State once, at the outset, that what follows summarizes another's words; never repeat `he said` or `the author adds` after.
- **R63** (rank 3; write-well:171): Write criticism as a discussion of qualities backed by evidence; never as a summary with comments.
- **R64** (rank 3; write-well:173): Treat several works by the general conclusions they support; never one by one in order of date.
- **R65** (rank 3; write-well:175): Place the words to stress, the new thing the sentence asserts, at its end; never bury them in the middle.
- **R66** (rank 3; write-well:177): Stress any element but the subject by placing it first; never trust the subject's usual first place to stress it.
- **R67** (rank 3; write-well:179): Stress the subject by moving it after its verb to the end, as in `Through the valley ran a stream`; never by leaving it first.
- **R68** (rank 3; write-well:181; demand: the sentences of a paragraph): Order the sentences of a paragraph and the paragraphs of a whole the same way, with the strongest last; never close on the weakest.
- **R69** (rank 3; write-well:181; demand: the paragraphs of a whole): Order the sentences of a paragraph and the paragraphs of a whole the same way, with the strongest last; never close on the weakest.
- **R70** (rank 3; write-well:183; demand: one term for one thing): Within one piece, use one term for one thing and one form wherever a rule allows two; never vary a term or a form within the piece.
- **R71** (rank 3; write-well:183; demand: one form wherever a rule allows two): Within one piece, use one term for one thing and one form wherever a rule allows two; never vary a term or a form within the piece.
- **R72** (rank 4; write-well:187; demand: can for ability): Use `can` for ability and `may` for permission; never `can` to ask leave.
- **R73** (rank 4; write-well:187; demand: may for permission): Use `can` for ability and `may` for permission; never `can` to ask leave.
- **R74** (rank 4; write-well:189): Use `claim` to lay claim to a thing or assert a right; never for `say` or `declare`.
- **R75** (rank 4; write-well:191): Treat `data` as plural, as in `the data show`; never `the data shows`.
- **R76** (rank 4; write-well:193): Write `different from`; never `different than`.
- **R77** (rank 4; write-well:195): Use `due to` after a noun or a linking verb, as in `delays due to load`; never for `because of`, as in `failed, due to load`.
- **R78** (rank 4; write-well:197): Call a matter a fact when a reader can check it; never call a judgment a fact.
- **R79** (rank 4; write-well:199): Place `however` meaning `nevertheless` after the first words of its clause; never first.
- **R80** (rank 4; write-well:201; demand: less for amounts): Use `less` for amounts and `fewer` for counts; never `less` with a count.
- **R81** (rank 4; write-well:201; demand: fewer for counts): Use `less` for amounts and `fewer` for counts; never `less` with a count.
- **R82** (rank 4; write-well:203): Use `literally` to set the strict sense against a figurative one; never for force.
- **R83** (rank 4; write-well:205): Write `almost` for nearly, as in `almost every test`; never `most`.
- **R84** (rank 4; write-well:207; demand: shall for the first-person plain future): Use `shall` for the plain future in the first person and `will` in the others or for resolve; never `you shall` for the plain future.
- **R85** (rank 4; write-well:207; demand: will in the other persons or for resolve): Use `shall` for the plain future in the first person and `will` in the others or for resolve; never `you shall` for the plain future.
- **R86** (rank 4; write-well:209): Refer to a person of unstated sex, as after `each`, `everyone`, `anybody`, or `someone`, with `they`, `them`, and `their`; never `everyone signs his own commit` or `his or her own commit`.
- **R87** (rank 4; write-well:211): Use `while` for `during the time that`; never for `and`, `but`, or `although`.
- **R88** (rank 5; write-well:215): Follow a loose sentence, two independent clauses joined by a conjunction, with a sentence of another build, such as a simple sentence or a periodic one that holds its main clause to the end; never with another loose sentence.
- **R89** (rank 5; write-well:217): Drop `case` as filler, as in `many builds` for `in many cases, the builds` and `if` for `in case`; never `in the case of the cache`.
- **R90** (rank 5; write-well:219; demand: compare to for likeness): Use `compare to` for likeness between things of different kinds and `compare with` for difference between things of one kind; never `compare March to April` for their differences.
- **R91** (rank 5; write-well:219; demand: compare with for difference): Use `compare to` for likeness between things of different kinds and `compare with` for difference between things of one kind; never `compare March to April` for their differences.
- **R92** (rank 5; write-well:221; demand: etc. only where the reader knows the rest): Use `etc.` where the reader knows the rest of the list; never after `such as` or `for example`.
- **R93** (rank 5; write-well:221; demand: never etc. after such as or for example): Use `etc.` where the reader knows the rest of the list; never after `such as` or `for example`.
- **R94** (rank 5; write-well:223): Replace `factor` and `feature`, noun or verb, with the plain act they stand for; never `speed was a factor`.
- **R95** (rank 5; write-well:225): Make a thing interesting by telling it; never announce it as interesting.
- **R96** (rank 5; write-well:227): Drop `nature` as filler, as in `slow queries` for `queries of a slow nature`; never `changes of a risky nature`.
- **R97** (rank 5; write-well:229): Write `have` or `own`; never `possess` in their place.
- **R98** (rank 5; write-well:231): Drop `respective` and `respectively`; never `their respective owners`.
- **R99** (rank 5; write-well:233): Keep `to` beside its verb, as in `to check carefully`; never `to carefully check`.
- **R100** (rank 5; write-well:235): Apply `worth while` to an action alone, as in `worth while to retry`; never as vague praise of a thing.
- **R101** (rank 5; write-well:237): Open an essay or paragraph with a precise statement; never with `one of the most`.
- **R102** (clash orders; write-well:241): Settle a clash between two rules above by these orders; never break a rule on any other ground.
- **R103** (clash orders; write-well:243): Add the words a reader needs to understand; never cut them for economy.
- **R104** (clash orders; write-well:245): Keep the words a parallel series repeats; never cut them as needless.
- **R105** (clash orders; write-well:247): Keep the paragraph's topic as subject, in the passive voice where the active would push it out; never push it out.
- **R106** (clash orders; write-well:249): Illustrate a needed abstraction with a concrete instance; never leave it bare.

## Violations

Each row names the file, the line, the rule, the offending text, and the smallest rewrite that meets the rule.

### R7

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 92 | R7 | "They gave no reliable gain, they cost up to twelve points of accuracy on small models in one lab's tests, and flattery raised compliance with objectionable requests." | "They gave no reliable gain; they cost up to twelve points of accuracy on small models in one lab's tests; and flattery raised compliance with objectionable requests." |

### R11

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 3 | R11 | "This rulebook sets the stance a text takes toward its reader." ("its": the rulebook or the text) | "This rulebook sets the stance a text takes toward the text's reader." |
| tone-of-voice.md | 3 | R11 | "It governs how the text states its demand, its belief in the reader, failure, and stakes; how much force it uses; where it aims praise and blame; its register; and how it frames its enemy." ("It": the rulebook or the stance; each later "it" and "its": the rulebook or the text) | "The rulebook governs how a text states the demand, the belief in the reader, failure, and stakes; how much force the text uses; where the text aims praise and blame; the text's register; and how the text frames the enemy." |
| tone-of-voice.md | 3 | R11 | "It applies to any text" ("It": the rulebook, the stance, or the register) | "The rulebook applies to any text" |
| tone-of-voice.md | 3 | R11 | "The `manifesto-writing` skill reads it before drafting." ("it": the rulebook, a standard, or a review) | "The `manifesto-writing` skill reads this rulebook before drafting." |
| tone-of-voice.md | 5 | R11 | "each rule applies one of them" ("them": the principles or the reasons) | "each rule applies one principle" |
| tone-of-voice.md | 9 | R11 | "Four principles carry it." ("it": the voice, the standard, or the work) | "Four principles carry the voice." |
| tone-of-voice.md | 11 | R11 | "State the standard together with its grounds: evidence that the reader can meet it" ("its" and "it": the standard or the "Demand" of the title) | "**Ground the standard.** State the standard together with its grounds: evidence that the reader can meet it" |
| tone-of-voice.md | 11 | R11 | "in the studies where grounds came with them" ("them": the standards, the readers, or the studies) | "in the studies where grounds came with the standards" |
| tone-of-voice.md | 12 | R11 | "at the strategy behind it" ("it": the work, the criticism, or the praise) | "at the strategy behind the work" |
| tone-of-voice.md | 13 | R11 | "**Say it outright.**" ("it" points at no noun before it) | "**Say the whole message outright.**" |
| tone-of-voice.md | 13 | R11 | "the reader supplies a negative one" ("one": the intent or the voice) | "the reader supplies a negative intent" |
| tone-of-voice.md | 14 | R11 | "and it spends the trust the next text needs" ("it": the belief or the experience) | "and the undone belief spends the trust the next text needs" |
| tone-of-voice.md | 49 | R11 | "if this happens, do that" ("this" and "that" point at no noun) | "if the obstacle arises, give the planned response" |
| tone-of-voice.md | 50 | R11 | "keep the failure out of it" ("it": the step or the positive target) | "keep the failure out of the step" |
| tone-of-voice.md | 56 | R11 | "in the study that tested it" ("it": the offer or the support) | "in the study that tested such an offer" |
| tone-of-voice.md | 75 | R11 | "They raised output in live speech" ("They": the tactics or the high goals) | "The tactics raised output in live speech" |
| tone-of-voice.md | 79 | R11 | "against new ones" ("ones": the behavior and the conditions both claim it) | "against new behavior and new conditions" |
| tone-of-voice.md | 91 | R11 | "state it plainly, once, with its reason" ("it" and "its": the prohibition or the constraint) | "state the prohibition plainly, once, with the prohibition's reason" |
| tone-of-voice.md | 93 | R11 | "their effect on models is untested" ("their": the rules, the beneficiaries, or the co-readers) | "the effect of those rules on models is untested" |
| tone-of-voice.md | 94 | R11 | "the framing around them" ("them": the action steps, the rules, or the readers) | "the framing around those steps" |
| tone-of-voice.md | 109 | R11 | "state that plainly first" ("that": the standard, the belief, or the reason) | "state that content plainly first" |
| tone-of-voice.md | 120 | R11 | "that is the standard you have already shown you can meet" ("that" points at a clause, not a noun) | "a tested fix is the standard you have already shown you can meet" |
| tone-of-voice.md | 121 | R11 | "Untested paths are where the next one hides." ("one": the outage or the path) | "Untested paths are where the next outage hides." |
| tone-of-voice.md | 131 | R11 | "in their reader population" ("their": the rules or the tests) | "in the reader population each rule addresses" |
| SKILL.md | 16 | R11 | "toward its reader: how it states the demand, ..., its register, and how it frames the enemy" ("its" and "it": the rulebook or the manifesto) | "toward the manifesto's reader: how the manifesto states the demand, ..., the manifesto's register, and how the manifesto frames the enemy" |
| SKILL.md | 16 | R11 | "run its checks when you tighten" ("its": the rulebook, the skill, or the manifesto) | "run the rulebook's checks when you tighten" |
| SKILL.md | 20 | R11 | "It declares." ("It": the manifesto or the rulebook of line 16) | "A manifesto declares." |
| SKILL.md | 20 | R11 | "It commands." | "A manifesto commands." |
| SKILL.md | 20 | R11 | "It names enemies." | "A manifesto names enemies." |
| SKILL.md | 58 | R11 | "Name it in the first section" ("it": the something opposed or the manifesto) | "Name the enemy in the first section" |
| SKILL.md | 89 | R11 | "until it hurts" ("it" points at no noun) | "until cutting hurts" |

### R12

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 123 | R12 | "Tests before merge is fixed." (plural "Tests" with singular "is") | "Testing before merge is non-negotiable." |

### R17

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 13 | R17 | ", and after a failure the reader supplies a negative one" (no comma closes "after a failure") | ", and after a failure, the reader supplies a negative one" |

### R20

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| SKILL.md | 87 | R20 | "etc. in a separate pass" (no comma closes `etc.`) | "etc., in a separate pass" |

### R26

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 13 | R26 | "Text carries no face or voice, so the reader supplies any intent the text leaves out" | "As text carries no face or voice, the reader supplies any intent the text leaves out" |
| tone-of-voice.md | 32 | R26 | "Reasons raised how much readers valued a task and also lowered their sense of competence slightly, so give the purpose and spare the reader a tutorial." | "As reasons raised how much readers valued a task and also lowered their sense of competence slightly, give the purpose and spare the reader a tutorial." |
| tone-of-voice.md | 75 | R26 | "They raised output in live speech, and the one test in written text found no effect, so lift adds force at most and never carries content." | "As the tactics raised output in live speech and the one test in written text found no effect, lift adds force at most and never carries content." |
| tone-of-voice.md | 142 | R26 | "Words are the weakest lever, since persuasion builds less self-belief than mastery does (Bandura 1977), so early wins arranged by the targets set the ceiling." | "As words are the weakest lever, since persuasion builds less self-belief than mastery does (Bandura 1977), early wins arranged by the targets set the ceiling." |

### R27

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 133 | R27 | "one study of 44 seventh graders, with covariate-adjusted estimates and no adult or workplace test (Yeager et al. 2014)." (no verb) | "the evidence is one study of 44 seventh graders, with covariate-adjusted estimates and no adult or workplace test (Yeager et al. 2014)." |
| tone-of-voice.md | 134 | R27 | "one preliminary study of kindergartners (Kamins & Dweck 1999)." (no verb) | "the evidence is one preliminary study of kindergartners (Kamins & Dweck 1999)." |
| tone-of-voice.md | 135 | R27 | "tested with spoken instructions only, and specific resources were never set against generic ones" ("tested" has no subject) | "the studies tested spoken instructions only, and none set specific resources against generic ones" |

### R28

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 14 | R28 | "Belief that experience contradicts is easily undone" | "Experience easily undoes a belief it contradicts" |
| tone-of-voice.md | 47 | R28 | "a failure described as common reads as the norm" | "a failure the text calls common reads as the norm" |
| tone-of-voice.md | 52 | R28 | "a real difficulty met" | "a real difficulty the reader met" |
| tone-of-voice.md | 75 | R28 | "confidence that they can be met" | "confidence that the group can meet them" |
| tone-of-voice.md | 107 | R28 | "Is the standard stated plainly?" | "Does the text state the standard plainly?" |
| tone-of-voice.md | 107 | R28 | "Is every piece of praise attached to a strategy or a real difficulty?" | "Does the text attach every piece of praise to a strategy or a real difficulty?" |
| tone-of-voice.md | 108 | R28 | "Is each failure named once, specifically, as changeable and uncommon, with a paired response, and kept out of the action steps?" | "Does the text name each failure once, specifically, as changeable and uncommon, with a paired response, and keep the failure out of the action steps?" |
| tone-of-voice.md | 110 | R28 | "Can the vision be pictured?" | "Can the reader picture the vision?" |
| tone-of-voice.md | 123 | R28 | "Tests before merge is fixed." | "Testing before merge is non-negotiable." |
| tone-of-voice.md | 131 | R28 | "none of those tests was re-read for this rulebook"; "difficulty framed as importance"; "failure kept from seeming common" | "the writer re-read none of those tests for this rulebook"; "difficulty that the text frames as importance"; "failure that the text keeps from seeming common" |
| tone-of-voice.md | 131 | R28 | "The four principles are inferences drawn across the studies." | "The four principles are inferences that the writer drew across the studies." |
| tone-of-voice.md | 134 | R28 | "criticism aimed at ability and criticism aimed at effort" | "criticism of ability and criticism of effort" |
| tone-of-voice.md | 135 | R28 | "tested with spoken instructions only, and specific resources were never set against generic ones" | "the studies tested spoken instructions only, and none set specific resources against generic ones" |
| tone-of-voice.md | 136 | R28 | "plans formed by readers raised goal attainment, and plans supplied by writers gave mixed results" | "plans that readers formed raised goal attainment, and plans that writers supplied gave mixed results" |
| tone-of-voice.md | 139 | R28 | "Antonakis et al. 2022, read in the authors' manuscript" | "Antonakis et al. 2022, which the writer read in the authors' manuscript" |
| tone-of-voice.md | 140 | R28 | "no rule here is tested on models as a rule" | "no study tests any rule here on models in the rule's own form" |
| tone-of-voice.md | 142 | R28 | "early wins arranged by the targets" | "the early wins that the targets arrange" |
| SKILL.md | 58 | R28 | "the rulebook sets how the enemy and the stakes are framed" | "the rulebook sets how the manifesto frames the enemy and the stakes" |

### R29

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 119 | R29 | "Those tests are what let the on-call engineer sleep through Friday's release." | "Those tests let the on-call engineer sleep through Friday's release." |
| tone-of-voice.md | 121 | R29 | "Untested paths are where the next one hides." | "The next outage hides in an untested path." |

### R30

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 5 | R30 | "The four principles give the reasons" (reasons for what) | "The four principles give the reasons for the rules" |
| tone-of-voice.md | 24 | R30 | "Fix the what and the why, and leave the how to the reader." | "Fix the outcome and the reason, and leave the method to the reader." |
| tone-of-voice.md | 32 | R30 | "State the why once" | "State the reason once" |
| tone-of-voice.md | 49 | R30 | "gave mixed results" | "gave mixed results, with no effect in a leaflet trial of 23,182 invitations (39.7% against 40.4%)" |
| tone-of-voice.md | 91 | R30 | "shape the themes" (themes of what) | "shape the themes of the model's story" |
| tone-of-voice.md | 116 | R30 | "Each line below adds one thing" | "Each line below applies one group of rules" |
| tone-of-voice.md | 125 | R30 | "the first green run is the point" | "the first green run is the target" |
| tone-of-voice.md | 136 | R30 | "plans supplied by writers gave mixed results" | "plans supplied by writers gave mixed results, with no effect in a leaflet trial of 23,182 invitations (39.7% against 40.4%)" |
| SKILL.md | 58 | R30 | "Every manifesto opposes something." | "Every manifesto opposes an enemy." |
| SKILL.md | 62 | R30 | "needs another form" | "needs an argued essay, not a manifesto" |

### R31

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 11 | R31 | "Standards lifted readers in the studies where grounds came with them" | "Standards lifted readers in the studies where grounds came with them, as in Yeager et al. (2014)" |
| tone-of-voice.md | 12 | R31 | "Across 607 effects in one feedback meta-analysis, feedback weakened as it drew the reader's attention onto the self." | "Across 607 effects in Kluger and DeNisi's (1996) feedback meta-analysis, feedback weakened as it drew the reader's attention onto the self." |
| tone-of-voice.md | 22 | R31 | "On such work a hard outcome target did no better than "do your best"." | "On such work, in Seijts et al. (2004), a hard outcome target did no better than "do your best"." |
| tone-of-voice.md | 32 | R31 | "Reasons raised how much readers valued a task and also lowered their sense of competence slightly" | "In Steingut, Patall & Trimble (2017), reasons raised how much readers valued a task and also lowered their sense of competence slightly" |
| tone-of-voice.md | 46 | R31 | "Criticism that told the reader how to improve raised motivation more than criticism that did not." | "In Fong et al. (2019), criticism that told the reader how to improve raised motivation more than criticism that did not." |
| tone-of-voice.md | 49 | R31 | "If-then plans raised goal attainment, though plans a writer supplied, rather than plans the reader formed, gave mixed results." | "If-then plans raised goal attainment, though plans a writer supplied, rather than plans the reader formed, gave mixed results (Gollwitzer & Sheeran 2006; Wang et al. 2021)." |
| tone-of-voice.md | 57 | R31 | "In people, controlling language raises anger and resistance" | "In people, controlling language raises anger and resistance, as [named study] found" |
| tone-of-voice.md | 58 | R31 | "Emphasis raised compliance with the line it marked" | "In the Palisade shutdown tests (Schlatter, Weinstein-Raun & Ladish 2026), emphasis raised compliance with the line it marked in 6 of 7 models" |
| tone-of-voice.md | 62 | R31 | "needless complexity lowered readers' judgment of the writer" | "needless complexity lowered readers' judgment of the writer (Oppenheimer 2006)" |
| tone-of-voice.md | 75 | R31 | "They raised output in live speech, and the one test in written text found no effect" | "They raised output in live speech (Antonakis, Fenley & Liechti 2011), and the one test in written text found no effect (Antonakis et al. 2022)" |
| tone-of-voice.md | 91 | R31 | "naming a forbidden word cut its use, though the word could still shape the themes" | "naming a forbidden word cut its use (Candussio et al. 2026), though the word could still shape the themes (Holtzman & West 2026)" |
| tone-of-voice.md | 92 | R31 | "They gave no reliable gain, they cost up to twelve points of accuracy on small models in one lab's tests, and flattery raised compliance with objectionable requests." | "They gave no reliable gain, they cost up to twelve points of accuracy on small models in one lab's tests (Dobariya & Kumar 2026), and flattery raised compliance with objectionable requests (Meincke et al. 2026)." |
| tone-of-voice.md | 140 | R31 | "Emphasis raised compliance with the line it marked;" (the next citation covers only the clause after it) | "Emphasis raised compliance with the line it marked (Schlatter, Weinstein-Raun & Ladish 2026);" |
| SKILL.md | 143 | R31 | "Manifestos require conviction." | "Manifestos require conviction; the example above keeps "This infatuation is destroying us." without a hedge." |
| SKILL.md | 143 | R31 | "Manifestos flatten nuance." | "Manifestos flatten nuance; the example above cuts "I think that collectively we are" to "We are"." |

### R32

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 11 | R32 | "the one study that isolated the grounds found only a weak effect on performance" | "the one study that isolated the grounds (Turner et al. 2014) found a performance gap that reached only p = .08" |
| tone-of-voice.md | 12 | R32 | "one feedback meta-analysis" | "Kluger and DeNisi's (1996) feedback meta-analysis" |
| tone-of-voice.md | 31 | R32 | "about four at most" | "four at most" |
| tone-of-voice.md | 32 | R32 | "lowered their sense of competence slightly" | "lowered their sense of competence by d = .19" |
| tone-of-voice.md | 38 | R32 | "The tested wording read:" | "The wording that Yeager et al. (2014) tested read:" |
| tone-of-voice.md | 56 | R32 | "in the study that tested it" | "in Moore, Vine, Wilson & Freeman (2014)" |
| tone-of-voice.md | 58 | R32 | "a vendor warns that over-strong wording can make newer models overtrigger" | "Anthropic warns that over-strong wording can make Claude Opus 4.5 and Claude Opus 4.6 overtrigger" |
| tone-of-voice.md | 62 | R32 | "readers' judgment of the writer" | "readers' ratings of the writer's intelligence" |
| tone-of-voice.md | 75 | R32 | "the one test in written text found no effect" | "the one test in written text (Antonakis et al. 2022; N = 656) found no effect (p = .718)" |
| tone-of-voice.md | 91 | R32 | "in the tests that had a silent control" | "in the tests of Candussio et al. (2026) against a silent control" |
| tone-of-voice.md | 92 | R32 | "on small models in one lab's tests" | "on GPT-5-nano and Gemini 2.5 Flash Lite in the tests of Dobariya and Kumar (2026)" |
| tone-of-voice.md | 137 | R32 | "a small and fragile effect on performance" | "an effect on performance of d = .19 that fell to d = .10 after trim-and-fill" |
| tone-of-voice.md | 140 | R32 | "cost accuracy on small models in one lab" | "cost accuracy on GPT-5-nano and Gemini 2.5 Flash Lite in one lab" |
| tone-of-voice.md | 142 | R32 | "Most findings come from feedback to one person, often a student or a child." | "The qualified findings come from feedback to one person, and two come from children: 44 seventh graders (Yeager et al. 2014) and kindergartners (Kamins & Dweck 1999)." |

### R37

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 5 | R37 | "The four principles give the reasons, and each rule applies one of them." (the paragraph covers every part of the rulebook; its first sentence covers two) | "Each part of the rulebook has one job. The four principles give the reasons, and each rule applies one of them." |

### R38

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 3 | R38 | "The `manifesto-writing` skill reads it before drafting." (who reads the rulebook, a side matter to its scope) | Move the sentence into a paragraph of its own: "The `manifesto-writing` skill reads this rulebook before drafting." |

### R39

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 3 | R39 | "The `manifesto-writing` skill reads it before drafting." (the paragraph closes on that side matter) | End the paragraph on "whether the reader is a person or an AI model." and move the skill sentence out. |

### R41

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 31 | R41 | "about four at most" | "four at most" |

### R42

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 22 | R42 | "did no better than "do your best"" | "only matched "do your best"" |

### R43

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 32 | R43 | "and also lowered" ("also" repeats "and") | "and lowered" |
| tone-of-voice.md | 119 | R43 | "Those tests are what let" ("are what" does no work) | "Those tests let" |

### R49

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 124 | R49 | "We don't merge hope. We merge proof." | "We merge proof, not hope." |
| SKILL.md | 20 | R49 | "It declares. It commands. It names enemies." | "A manifesto declares, commands, and names enemies." |
| SKILL.md | 62 | R49 | "State positions. Do not justify them at length." | "State positions without justifying them at length." |

### R50

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 3 | R50 | "; its register;" (a noun phrase in a series of clauses) | "; which register the text takes;" |
| tone-of-voice.md | 11 | R50 | "**Demand travels with grounds.**" (a statement among the commands "Aim at the work.", "Say it outright.", and "Calibrate.") | "**Ground the standard.**" |
| tone-of-voice.md | 73 | R50 | "State the intent as relational, ... and never as an effort to persuade." (an adjective set against a noun phrase) | "State the intent as a relational aim, as the tested wording above does, and never as an effort to persuade." |
| tone-of-voice.md | 125 | R50 | "**Across texts:**" (a prepositional phrase among the noun labels of lines 118 to 124) | "**Sequencing:**" |
| SKILL.md | 16 | R50 | "its register," (a noun phrase in a series of clauses) | "which register the manifesto uses," |

### R53

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 75 | R53 | "metaphor, story, contrast, the rhetorical question, the three-part list, moral conviction, reflection of the group's sentiment, high goals, and confidence that they can be met" (nine tactics in one ungrouped run) | "figures (metaphor, story, and contrast), forms (the rhetorical question and the three-part list), and appeals (moral conviction, reflection of the group's sentiment, high goals, and confidence that they can be met)" |
| SKILL.md | 16 | R53 | "how it states the demand, belief in the reader, failure, stakes, force, praise and blame, its register, and how it frames the enemy" (eight concerns in one ungrouped run) | "how the manifesto states the demand and the stakes; how the manifesto treats belief in the reader, failure, praise, and blame; and how the manifesto sets force and register and frames the enemy" |

### R58

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 3 | R58 | "It applies to any text that asks a reader to meet a standard, such as a manifesto, an instruction, or a review," ("such as" can attach to "a standard") | "It applies to manifestos, instructions, reviews, and any other text that asks a reader to meet a standard," |
| tone-of-voice.md | 20 | R58 | "at least one target to act on from the text alone" ("from the text alone" can attach to "Give" or to "act on") | "at least one target that the reader can act on with the text alone" |
| tone-of-voice.md | 56 | R58 | "named tools, people, or time" ("named" can attach to "tools" alone or to all three) | "named tools, named people, or set time" |
| tone-of-voice.md | 63 | R58 | "State what holds without hedges" ("without hedges" can attach to "holds") | "State without hedges what holds" |
| tone-of-voice.md | 75 | R58 | "and only on settled content: metaphor, story, ..." (the list of tactics can attach to "settled content") | "Draw lift sparingly, and only on settled content, from the verbal tactics: metaphor, story, ..." |
| tone-of-voice.md | 131 | R58 | "though none of those tests was re-read for this rulebook: an actionable target ..." (the list of six rules can attach to "those tests") | "Six rules rest on direct tests in their reader population: an actionable target (...), ..., and plain words (...); none of those tests was re-read for this rulebook." |
| SKILL.md | 86 | R58 | "and closing (the choice), in the tone the rulebook sets" ("in the tone" can attach to "closing") | "**Draft sections** in the tone the rulebook sets — one per core idea, plus opening (enemy + stakes) and closing (the choice)" |

### R59

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 57 | R59 | "controlling language raises anger and resistance; in models, threats gave no reliable gain" | "controlling language raised anger and resistance; in models, threats gave no reliable gain" |
| tone-of-voice.md | 58 | R59 | "Emphasis raised compliance with the line it marked, and a vendor warns" | "Emphasis raised compliance with the line it marked, and a vendor warned" |
| tone-of-voice.md | 140 | R59 | "no rule here is tested on models as a rule" (present, where line 138 has "no study tested") | "no rule here was tested on models as a rule" |
| tone-of-voice.md | 140 | R59 | "Anthropic's guidance advises reasons, ...; OpenAI's keeps strict words" | "Anthropic's guidance advised reasons, ...; OpenAI's kept strict words" |
| tone-of-voice.md | 142 | R59 | "No study tests a manifesto-style text on performance" | "No study tested a manifesto-style text on performance" |
| tone-of-voice.md | 142 | R59 | "Most findings come from feedback to one person" | "Most findings came from feedback to one person" |
| tone-of-voice.md | 142 | R59 | "the model evidence measures accuracy and compliance" | "the model evidence measured accuracy and compliance" |

### R65

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 5 | R65 | "The closing section states how strong the evidence behind each rule is." (ends on "is") | "Rule by rule, the closing section states the strength of the evidence." |
| tone-of-voice.md | 9 | R65 | "Four principles carry it." (the new thing stands first, and "it" ends the sentence) | "The voice rests on four principles." |
| tone-of-voice.md | 46 | R65 | "Criticism that told the reader how to improve raised motivation more than criticism that did not." (ends on the baseline) | "Criticism raised motivation more when it told the reader how to improve." |
| tone-of-voice.md | 56 | R65 | "A general offer of support changed nothing in the study that tested it." (ends on "tested it") | "In Moore, Vine, Wilson & Freeman (2014), a general offer of support changed nothing." |

### R67

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 9 | R67 | "Four principles carry it." (the stressed subject stays first) | "The voice rests on four principles." |

### R68

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 3 | R68 | The paragraph closes on "The `manifesto-writing` skill reads it before drafting." | Close the paragraph on "whether the reader is a person or an AI model." |
| tone-of-voice.md | 11 | R68 | The item closes on "the one study that isolated the grounds found only a weak effect on performance." | Place the evidence sentence before "State the standard together with its grounds: ...", so the instruction closes the item. |
| tone-of-voice.md | 49 | R68 | The item closes on "gave mixed results." | Place the evidence sentence before "Pair every named obstacle with an if-then response: ...", so the instruction closes the item. |
| tone-of-voice.md | 91 | R68 | The item closes on "though the word could still shape the themes." | "Prefer a positive target. In the tests that had a silent control, naming a forbidden word cut its use, though the word could still shape the themes. Where a prohibition is the clearest form of a constraint, state it plainly, once, with its reason." |
| tone-of-voice.md | 98 | R68 | The paragraph closes on "This order is a design choice, not a tested sequence." | Open the paragraph with "This order is a design choice, not a tested sequence." and close it on "Then set the wording: the pressure, the force, the register, and the lift." |
| tone-of-voice.md | 142 | R68 | The paragraph closes on "Durability is the least-tested area, and the model evidence measures accuracy and compliance, not persistence over long tasks." | Move "Words are the weakest lever, ... set the ceiling." to the end of the paragraph. |

### R69

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 142 | R69 | The rulebook closes on its weakest section, the limits of its evidence, and ends on "Durability is the least-tested area, and the model evidence measures accuracy and compliance, not persistence over long tasks." | Place "## Evidence and limits" before "## Checks", so the checks close the rulebook. |

### R70

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 3 | R70 | "an AI model" (lines 57, 58, 90, 92 to 94, and 140 say "model") | "a model" |
| tone-of-voice.md | 5 | R70 | "the five ways tone fails" ("failure" names the reader's failure on lines 13, 46, 47, 50, and 98) | "the five ways tone goes wrong" |
| tone-of-voice.md | 11 | R70 | "**Demand travels with grounds.**" (the next sentence calls the same thing "the standard") | "**Ground the standard.**" |
| tone-of-voice.md | 12 | R70 | "onto the self" (lines 41 and 134 say "the person") | "from the work onto the person" |
| tone-of-voice.md | 24 | R70 | "the why" (lines 11, 13, 25, 90, 91, and 98 say "the reason") | "the reason" |
| tone-of-voice.md | 32 | R70 | "the why" | "the reason" |
| tone-of-voice.md | 71 | R70 | "what the reader is" (lines 41 and 134 say "the person") | "attach "you" to what the reader does, never to the person" |
| tone-of-voice.md | 93 | R70 | "the human co-readers" (lines 57, 79, and 94 say "people") | "the people who also read the text" |
| tone-of-voice.md | 94 | R70 | "the human rules" (the same sentence says "people") | "the rules for people" |
| tone-of-voice.md | 102 | R70 | "every line that fails" ("failure" names the reader's failure elsewhere) | "every line that a check catches" |
| tone-of-voice.md | 106 | R70 | "the reader's worth" (lines 41 and 134 say "the person") | "the person" |
| tone-of-voice.md | 109 | R70 | "cut the device" (the sentence before says "Remove each device") | "remove the device" |
| tone-of-voice.md | 116 | R70 | "The plain instruction" (line 112 says "the original instruction") | "The original instruction" |
| tone-of-voice.md | 134 | R70 | "**Criticism of the process, not the person:**" (lines 12 and 51 say "the work" and "the strategy") | "**Criticism of the work, not the person:**" |
| tone-of-voice.md | 136 | R70 | "plans formed by readers ... plans supplied by writers" (line 49 says "plans the reader formed" and "plans a writer supplied") | "plans the reader formed ... plans a writer supplied" |

### R71

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 12 | R71 | "at the work and at the strategy behind it" (lines 33, 41, 51, 107, and 131 put a shared preposition before the first item alone) | "at the work and the strategy behind it" |
| tone-of-voice.md | 30 | R71 | "a person or group" (lines 3, 13, 41, 90, and 98 put a shared article before every item) | "a person or a group" |
| tone-of-voice.md | 52 | R71 | "to a strategy or to a real difficulty met" | "to a strategy or a real difficulty met" |
| tone-of-voice.md | 93 | R71 | "for the human co-readers and for one voice" | "for the human co-readers and one voice" |
| tone-of-voice.md | 106 | R71 | "aim at the reader's worth rather than the work" (lines 33 and 41 and the next check repeat the preposition after "rather than") | "aim at the reader's worth rather than at the work" |
| tone-of-voice.md | 109 | R71 | "a standard, belief, or reason" | "a standard, a belief, or a reason" |

### R72

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 58 | R72 | "over-strong wording can make newer models overtrigger" (possibility, not ability) | "a vendor warns of newer models that overtrigger under over-strong wording" |
| tone-of-voice.md | 91 | R72 | "the word could still shape the themes" (possibility, where the source reports a result) | "the word still shaped the themes" |

### R78

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| SKILL.md | 24 | R78 | "state positions as facts" (a position is a judgment) | "state positions without hedges" |

### R88

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 50 | R88 | "In penalty kicks, naming the thing to avoid drew errors toward it, and positive, action-based instructions reduced errors." (follows the loose first sentence) | "In penalty kicks, naming the thing to avoid drew errors toward it, whereas positive, action-based instructions reduced errors." |
| tone-of-voice.md | 58 | R88 | "Emphasis raised compliance with the line it marked, and a vendor warns that over-strong wording can make newer models overtrigger." (follows the loose first sentence) | "Emphasis raised compliance with the line it marked; a vendor warns that over-strong wording can make newer models overtrigger." |
| tone-of-voice.md | 71 | R88 | "Address the reader as "you" to hand over the standard, the belief, and the means, and attach "you" to what the reader does, never to what the reader is." (follows the loose sentence on line 63) | "Address the reader as "you" to hand over the standard, the belief, and the means; attach "you" to what the reader does, never to what the reader is." |
| tone-of-voice.md | 79 | R88 | "Set old behavior and old conditions against new ones, and keep people, the reader above all, out of the contrast." (follows the loose last sentence of line 75) | "Set old behavior and old conditions against new ones; keep people, the reader above all, out of the contrast." |
| tone-of-voice.md | 142 | R88 | "Words are the weakest lever, since persuasion builds less self-belief than mastery does (Bandura 1977), so early wins arranged by the targets set the ceiling." (follows the loose third sentence) | "Since persuasion builds less self-belief than mastery does (Bandura 1977), the early wins that the targets arrange, not the words, set the ceiling." |
| tone-of-voice.md | 142 | R88 | "Durability is the least-tested area, and the model evidence measures accuracy and compliance, not persistence over long tasks." (follows the loose fourth sentence) | "Durability is the least-tested area; the model evidence measures accuracy and compliance, not persistence over long tasks." |

### R92

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| SKILL.md | 87 | R92 | "remove "I think," "perhaps," etc." (the reader cannot know the rest of the list) | "remove hedges such as "I think" and "perhaps"" |

### R103

| File | Line | Rule | Text | Rewrite |
|---|---|---|---|---|
| tone-of-voice.md | 93 | R103 | "and for one voice" | "and for one voice across texts" |
| tone-of-voice.md | 109 | R103 | "Remove each device." (the next sentence cuts the device only when nothing leaves with it) | "Imagine removing each device." |
| tone-of-voice.md | 131 | R103 | "Every other rule holds with a qualifier:" ("every other" also reads as "every second") | "Each remaining rule holds with a qualifier:" |
| tone-of-voice.md | 140 | R103 | "as a rule" (also reads as "usually") | "in its stated form" |
| tone-of-voice.md | 142 | R103 | "readers who already perform and trust" | "readers who already perform well and trust the writer" |
| tone-of-voice.md | 142 | R103 | "set the ceiling" | "set the ceiling on the rules' effect" |

## Count

Violations: 181
