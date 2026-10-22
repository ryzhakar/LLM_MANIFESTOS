# Brief: write the manifesto Raise the Bar

## Bind before you write

Bind to these three elements through the skill `manifesto:manifesto-oath`, and show your commitments before you write a line of the manifesto. In the binding output, name for each element the lines you read and whether any tool output was capped.

1. **The tone-of-voice rulebook**, `plugin/rulebooks/tone-of-voice.md` in your worktree, as committed at a889713. It is both your source and the tone you write in: the manifesto must pass every check the rulebook teaches.
2. **write-well**, the skill `agent-conduct:write-well`. It governs every sentence you write, the manifesto's and your report's.
3. **The definition and shape in this brief**, the sections "What the manifesto is" and "The shape". For this manifesto they replace the `manifesto-writing` skill, which you leave unbound, because that skill imports the rulebook you are rewriting and carries a register this manifesto rejects.

## The task

Rewrite the rulebook as one manifesto at `plugin/manifestos/raise-the-bar.md`. A writer, person or model, reads it before writing any text that asks a reader to meet a standard. The rulebook stays where it is; the steward removes it once your manifesto lands.

## What the manifesto is

The manifesto tells a writer how to address a reader so that the reader rises to a high standard. The demand comes with its grounds, belief in the reader is stated and true, failure is named as fixable, and stakes and resources carry the pressure instead of contempt or threat.

- **It covers** the stance toward the reader: how the text states the demand, belief, and stakes; where the text aims praise and blame; how hard the text pushes; its register; and how it frames the enemy.
- **It leaves out** grammar, which belongs to write-well; a manifesto's shape, which belongs to `manifesto-writing`; the text's content, since the instruction arrives settled; and the evidence, which lives in a companion file the steward keeps.
- **Its reader** is the writer, person or model. **Its target** is whoever reads the finished text, people and models alike.
- **It succeeds** when the reader of the finished text takes the standard seriously and acts on it, and the original instruction survives intact.

## What to carry over, and what to leave

Carry over every rule of the rulebook, each stated once:

- the four principles: Ground the standard, Aim at the work, State everything outright, Calibrate;
- the rules on the demand; the reason and the stakes; belief in the reader; failure, praise, and blame; pressure and force; register, certainty, and lift; the enemy and the choice; sequence and voice;
- the rules for readers who are models, including the rule that, where people and models read one text, the rules for models govern the action steps;
- the order of work, content first and wording second;
- the five faults with their checks, Brimstone, Velvet, Omen, Fanfare, and Fog, and the two closing checks;
- the worked example, "Write tests before you merge."

Leave out every citation, author name, year, effect size, and support tag, and the whole "Evidence and limits" section. The writer never needs them, and the companion file holds them. Keep a reason only where it changes how the writer applies a rule, and state it in plain words: "praise for an easy win reads as low expectations" stays, while "(Meyer et al. 1979)" goes.

Add no rule the rulebook lacks. Where two rules say the same thing, merge them, and report each merge.

## The shape

Build the manifesto to these seven requirements, which set how far it follows the manifestos of this collection.

1. **Frontmatter**, in the five fields `generate.py` validates:
   ```yaml
   title: "Raise the Bar"
   tagline: "raise the bar, not the voice"
   version: "1.0.0"
   theme: "cognitive-science"
   description: "<one sentence telling a writer why to read it>"
   ```
2. **Attribution**, as the last line: "*After Yeager, Cohen, Kluger and DeNisi, Locke and Latham, and Bandura*".
3. **Voice**: declarations and commands in the present tense, with no hedges and no tutorial.
4. **Skeleton**:
   - Name the enemy in the first section. The enemy is a method, pressure through contempt and threat, and never a kind of reader or a person.
   - Give each section one point, in under 150 words; the checks table and the worked example are exempt from the limit.
   - Put mappings in tables.
   - Close on the checks, as the closing checklist, and then on a choice between two behaviors: raising the voice or raising the bar.
5. **Vocabulary**: keep the five fault names as the manifesto's coined terms, and the tagline as its one aphorism. Use at most one sharp image. Write no narrator and no scene. Keep the manifesto as short as the rules allow; about 1,000 to 1,600 words should carry them.
6. **Register**: write in the rulebook's own register. This collection's 2026-10-11 house register, the one in `lines-spent.md` with its identity attacks, capital and fragment quotas, and fury runs, is the Brimstone the manifesto names as its enemy, so take nothing from it.
7. **One home per rule**: state each rule once in the body, and let the closing checks test the rules without restating them.

## Your worktree and your limits

- Work only in `/Users/ryzhakar/LLM_MANIFESTOS.worktrees/raise-the-bar`, on branch `feat/raise-the-bar`, which the steward created from `session/manifesto-tone`. Another session owns `/Users/ryzhakar/LLM_MANIFESTOS`; keep every read and write inside your worktree, except this brief, which you read at its path in that checkout.
- Write two files: `plugin/manifestos/raise-the-bar.md`, and the root `README.md`, which `just readme` regenerates from the frontmatter. Leave every other file as it is, the rulebook, the skills, and the other manifestos included.
- Run `just readme` from the worktree root as the validation gate. If it fails, fix the frontmatter and run it again.
- Commit on `feat/raise-the-bar` at the end of each pass below, naming only the files you changed, with a one-line message of at most ten words and no attribution trailer. Push nothing, and leave every other branch alone; the steward integrates your branch.
- The sources are all on disk, so use no web access. Send your reports to the steward alone, by SendMessage to `team-lead`; message no other session, and ask the owner nothing, since the owner is away. Where this brief leaves a question open, settle it by the rulebook and write-well, and name the question in your report.

## Three passes, three reports

Work in three passes, one round each, and report after each. The owner's usage budget is nearly spent, so finish each pass in one round and stop after the third.

1. **Write.** Write the manifesto, run `just readme`, and confirm that every rule of the rulebook appears once. Commit as `feat(manifestos): raise the bar, first draft`. Send report 1 to `team-lead`: the file path and the word count; a rule map naming each rule group of the rulebook and the manifesto section where it landed; every merge you made; every open question you settled, and how.
2. **Review against the manifesto itself.** Run the manifesto's own five checks and two closing checks on every line once, and apply every fix at once. Commit as `fix(manifestos): raise the bar, own checks applied`. Send report 2 to `team-lead`: the count of lines each check caught, and each fix in one line.
3. **Review against write-well.** Reread the whole manifesto once against write-well, rank by rank, most serious fault first, and apply every fix at once. Run `just readme` again. Commit as `fix(manifestos): raise the bar, write-well pass`. Make report 3 your final message: the count of faults by rank, the final word count, and the three commit hashes.

Keep each report to at most fifteen lines.

## Done means

The work is done when all of these hold:

- `plugin/manifestos/raise-the-bar.md` exists with valid frontmatter, and `just readme` passes.
- Every rule of the rulebook appears exactly once.
- The text holds no citation, effect size, or support tag.
- Both review passes ran once, and their fixes are committed.
- Three commits sit on `feat/raise-the-bar`, and three reports reached the steward.
