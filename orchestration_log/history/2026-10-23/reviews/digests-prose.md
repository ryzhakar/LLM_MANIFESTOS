# Review of unharness 3.6.0: prose

Scope: the compile-digest skill, the compile-commitments skill change, plugin/README.md, plugin/unharness/README.md, plugin/SCHEMA.md, README.md and README.template.md, and the repo's `.min.md` pair, on feat/digests at 8378fd2.
Paths below are relative to /Users/ryzhakar/LLM_MANIFESTOS.worktrees/digests.

Checked against the code: every flag, verb, and refusal message in the docs was compared with `unharness --help` for each verb, with `digests.py`, `doctor.py`, and `cli.py`, and by running `stamp`, `doctor --digests`, and `prompt --overlap` in a scratch project. All nine new SCHEMA message rows match the code verbatim. The stamp output, the doctor line format, the doctor exit code, and the index shape match. The README index sample hashes for dry and kiss equal the real source hashes. Both min bodies fit the one-third budget (437 of 1853 words, 135 of 415 words). I did not run the test suite, which belongs to the code reviewer.

## Blocking

1. `plugin/unharness/README.md:10`: the install line pins `@v3.5.0`, and the same README now documents `stamp`, `doctor`, and four flags that tag lacks. `plugin/.claude-plugin/plugin.json:3` and `plugin/unharness/pyproject.toml:3` also still read 3.5.0, and this diff bumps none of them. A reader who follows the README runs a binary without the verbs it describes. Fix: at the 3.6.0 tag, change the pin to `v3.6.0` and bump both version fields in the same commit.

2. `plugin/README.md:66`: the min pair "holds at most a third of the words of its full counterpart". Counted on the whole files, the commitments pair is 249 against 529 words, almost half, and the interplay pair is 551 against 1967, 28 percent. The budget in the skill covers the body after the `<stack>` block only. Fix: write "at most a third of the words of its full counterpart's body, the text after the `<stack>` block".

## Should fix

1. `plugin/README.md:83`: "`/compile-commitments` ... writes the interplay and commitments files" omits the min pair, and "`unharness prompt` stops until the files match" is false under `--minified` until the min pair matches. The skill description at line 10 and the bullet at line 66 already say four files. Fix: write "writes the interplay and commitments files and their min pair".

2. `plugin/unharness/README.md:12`: "The four flags swap full manifesto texts for digests and load the `.min.md` session files." Only `--digests` and `--stack-digests` swap texts; `--overlap` alone exits 1 and only widens the cover; `--minified` swaps session files and touches no manifesto text. Fix: "`--digests` and `--stack-digests` swap manifesto texts for digests, `--overlap` lets stack digests share a manifesto, and `--minified` loads the `.min.md` session files."

3. `plugin/skills/compile-digest/SKILL.md:9`: the slug rule says to take "the word after `source: manifesto` in a config line; never take an element's `name` in its place". With no `source:` line, the name is the slug (SCHEMA.md, Source types table, first row; `manifesto_slug` in resolve.py). Every manifesto element in this repo's own `.manifestos.yaml` has no source line, so the rule names no slug for them, and its prohibition is wrong for them. The sentence also joins two definitions of a slug with "and", which a reader can take as one. Fix: "the reference of `source: manifesto <slug>`, else the element's `name`; never the `name` of an element whose source names another reference."

4. `plugin/skills/compile-digest/SKILL.md:33` and `:42`: "under 350 words; never exceed that" allows exactly 350, which "under" forbids. The skill also gives no way to count words, though it requires a word count in the report. The sibling skill states the count (`sed ... | wc -w`) and the unit. Fix: "at most 349 words, counted with `wc -w`", likewise 849, and give the count command in check-against-the-source.

5. `plugin/README.md:86`: "reads singles from `.claude/digests/` beside the config, then from the plugin's `digests/`" does not say that the local file wins per stem even when its index entry is stale, so a current plugin copy does not rescue it (spec, Resolution, first bullet). A reader meets a refusal the text does not explain. Fix: add "the local file wins for its stem, even when its entry is stale".

6. Term drift for one thing, the condensed session pair. plugin/README.md names it "the condensed pair" (line 66), "the min pair" (line 91),; the compile-commitments skill says "minified pair", "condensed variants", "condensed body"; SCHEMA.md:124 says "the `.min.md` pair". Fix: use "min pair" everywhere, defined once at plugin/README.md:66.

7. `plugin/skills/compile-digest/SKILL.md`, confirm-the-compile: the failure rules cover a message naming the stem, another slug, or a session file. Two refusals fit none: `manifesto <slug> appears twice in the stack; digest modes need each once`, and `no cover without overlap`, which names slugs that lack singles and may name the stem. Fix: add one clause each, report the first as a config fault outside this digest, and for the second run the compile again with `--overlap` or report it.

8. `plugin/skills/compile-digest/SKILL.md`, write-the-sentences: the skill lists six of Strunk's rules; spec line "Strunk applied" asks for the whole set, and a fresh agent loads no write-well. Fix: add one sentence ordering the agent to bind to `agent-conduct:write-well` when it is installed and to reread the draft against its rules.

## Nits

1. `plugin/README.md:100`: "Each place keeps one `index.json` ... and it covers every digest of that place". "It" can point at the place or the index. Fix: "and that index covers".

2. `plugin/README.md:112`: the doctor excerpt opens with `$`; the stamp example above it and the other blocks do not. Fix: drop the `$`, or add one to the stamp block.

3. `plugin/README.md:86`: "each manifesto element enters as its digest" holds for `--digests` only; under `--stack-digests` a manifesto may enter inside a stack digest. The cover rule also omits the third tie-break the code applies, the smaller sorted stem list. Fix: "as its digest or inside a stack digest" and add "then to the smaller list of stems".

4. `plugin/README.md:66`: the list opens "a project keeps these files" and its last bullet is a folder. Fix: "these files and folders".

5. `plugin/SCHEMA.md:123`: "`unharness prompt` or `stack` with no element in `you`" is wrong for `stack` with slugs, which prints the named manifestos before the empty check (cli.py `_output`, checked by reading). Fix: "`unharness prompt`, or `stack` with no slug, with no element in `you`".

6. `plugin/SCHEMA.md:128`: the cause "its index lacks its stem" omits that an entry whose slugs differ from the stem also raises this message. Fix: "its index lacks its stem, or holds an entry for other slugs".

7. `plugin/SCHEMA.md:131`: the cause names overlapping stack digests but not the premise, a manifesto with no single digest. Fix: "stack digests cover a manifesto that has no single digest, and every choice of them overlaps".

8. `plugin/unharness/README.md:13`: "prints the `<stack>` block and the constitution, of the given manifestos alone when slugs follow" strands the modifier. Fix: "prints the `<stack>` block and the constitution; given slugs, it prints those manifestos alone."

9. `plugin/skills/compile-digest/SKILL.md:21`: "figures" can mean numbers or figures of speech, and "closing choice" names a section of one manifesto. Fix: "numbers, figures of speech, names, examples, and any closing call to choose a path".

10. `.manifestos.interplay.min.md:15`: "and I give every doubt" reads oddly beside the full file's "with every doubt given". Fix: "and I state every doubt".

11. `.manifestos.commitments.min.md:16`: the line opens "I must not fool myself", while the skill pattern for the min file is "I must ..., and I will ...". Fix: "I must report what could undo my result, and I will reproduce the baseline first."

12. `README.md:151` and `README.template.md`: "the shorter digests in `digests/`" omits the local `.claude/digests/`. Fix: "the shorter digests in `digests/` and `.claude/digests/`". The two files agree with each other.
