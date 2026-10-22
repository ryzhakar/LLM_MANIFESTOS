# C4 oath

## Commits

On `feat/unharness-oath` in `/Users/ryzhakar/LLM_MANIFESTOS.worktrees/oath`, not pushed:

- `4a50399 feat(unharness): shipped preamble names each harness residue`, adds `plugin/unharness/src/unharness/preamble.md`.
- `2842350 feat(skills): compile-commitments writes interplay and commitments`, adds `plugin/skills/compile-commitments/SKILL.md`.

`claude plugin validate plugin` passes with the new skill in place.

## Preamble

Fifteen lines, eight paragraphs, first person throughout, no heading, no tag, and no occurrence of "unharness" or "compile". One opening sentence states the rule the rest applies: the application adds text around what the user wrote, and I read each kind by its source. The seven paragraphs after it cover each residue the spec lists, one each:

1. The identity line: the application's fixed label, no instruction.
2. The system reminder and system-role message: from the application, carrying the email, the date, the working folder, file-change notes, and the tool, skill, and agent lists; the wrapper sentences add nothing to the facts.
3. Hook output: text from the hooks the user installed, read as the user's standing word.
4. Skill text: arrives in a user turn, followed as the user's standing instruction.
5. The task-list nudge and the silent-turn note: the application's word, with what follows settling whether I speak.
6. Tool descriptions, the Agent tool's worktree sentence among them: what the tool can do, not what to do.
7. Server instructions: bind my use of that server's tools and nothing else.

Checks run. The five Raise the Bar checks found no Brimstone, Velvet, Omen, or Fanfare; the Fog check passed because the first sentence gives one target to act on. The two closing checks passed: every statement matches the spec's residue list, and the preamble is itself the instruction, so none was lost. The write-well reread, most serious fault first, caught five faults, all fixed: an ambiguous "it" after the reminder paragraph's first sentence; a second ambiguous "it" in the skill paragraph, where "it names" could claim the text or the skill; a comma-wrapped compound subject ("A nudge ..., and a note ..., come") that broke number agreement; the passive "is settled by"; and two terms, "owner" and "user", for one person, now "user" throughout.

## Skill

Frontmatter: `name: compile-commitments`; description of one sentence plus the four triggers. Body tags in order:

- `read-the-stack`: run `${CLAUDE_PLUGIN_ROOT}/bin/unharness stack --config <path>` into a temporary file, read it whole, take every demand from that text and none from memory.
- `deconstruct-each-element`: reduce each element to its axioms.
- `map-convergence-and-tension`: mark shared demands, quote both sides of each tension, resolve each with a rule, order the elements where no rule resolves.
- `write-the-interplay-file`: `.manifestos.interplay.md` beside the config, `<stack>` verbatim, then `<interplay>` in the first person with no seam.
- `write-the-commitments-file`: `.manifestos.commitments.md` the same way, one must/will and one must-not/will-not pair per element in stack order, with the `never_do_this`/`do_exactly_this` pair showing a commitment that names the config and the tool against one that names a demand.
- `report-the-files`: report each path, print no content.
- `confirm-the-compile`: run `unharness prompt --config <path> > /dev/null` and report its exit code.

Every sentence is a command paired with its own prohibition and carries one emphatic word; a grep for doubled emphatic words found none. The reread caught four faults, all fixed: the undefined narrow term "primary constraint", a tag named with the undefined word "interplay", two passive phrases, and a relative clause that could attach to "folder".

## Deviations from the spec with reasons

- The preamble says "the user" where the spec's preamble paragraph alternates "user" and "owner". One person, one term, by write-well's rule on terms; "user" is the word the harness and the tools already use.
- The spec says "the constitution's rules on speaking and silence govern over" the nudge and the silent-turn note. The preamble says "what follows below settles whether I speak and when", because a stack may carry no rule on silence, and a sentence that cites an absent rule would be untrue by Raise the Bar's calibration check.
- The skill runs the plugin's `bin/unharness` by `${CLAUDE_PLUGIN_ROOT}` and omits the owner's `uvx unharness stack` form, because the skill runs inside a session and skill-creation forbids a sentence that neither instructs nor forbids.
- The skill names no other skill. The pair format lives inline because the session needs it in one read and the oath skill is out of scope to edit.
- `plugin/unharness/src/unharness/` did not exist in this worktree; the preamble commit creates the path the spec names, and C1's package will merge beside it.

The preamble and the skill are committed on `feat/unharness-oath` in two commits and the plugin validates. The preamble covers the spec's seven residues in fifteen first-person lines, and the skill leaves the session a fixed shape and every decision about content. Three wording choices depart from the spec's phrasing, each with its reason above, and nothing is pushed.
