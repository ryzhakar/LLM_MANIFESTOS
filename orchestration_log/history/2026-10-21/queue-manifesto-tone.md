# Queue: manifesto tone

Owner is away by default; only a message stating "i'm present" opens a round.

## Unsolved (the owner's alone)

1. **Memento setup for this project:** no `.claude/memento.yaml` or charter exists, and the schema is the owner's own declaration, so I may not author one. Work that depends on it: `memento patdown`, `memento check`, and goal pursuit by charter. All other work continues.
2. **Release of the rulebook:** integrating `session/manifesto-tone` into `main`, bumping `plugin/.claude-plugin/plugin.json` to 3.4.0 and tagging `v3.4.0` publishes the change to every install of `manifesto@llm-manifestos`; main moves only on the owner's trigger. Work that depends on it: the installed plugin carrying the rulebook. All other work continues.

## Solved (reversible, acted on)

1. **Which rule governs a sentence inside a manifesto:** write-well governs every sentence, and manifesto-writing governs tone and shape, as `.manifestos.yaml` scopes them; a short sentence stays whole. Alternative: manifesto-writing governs the sentences of a manifesto, fragments included, and write-well governs all other prose.
2. **Fragments already in the manifestos,** such as `simple-made-easy.md:55` ("Not today. Not this sprint.") and `lines-spent.md:13` ("Done."): left unchanged until a task names them; new and revised prose obeys decision 1. Alternative: rewrite every fragment in every manifesto now.
3. **Where this queue lives:** its own file beside `queue-plugin-takeover.md`, one queue per task. Alternative: append these entries to `queue-plugin-takeover.md`.
4. **Where this span's journal lives:** `orchestration_log/history/<date>/`, the home every earlier span used, although the shipped memento default names `docs/orchestration_log/history/`. Alternative: write the journal under `docs/orchestration_log/history/` as the default declares.
5. **Wake:** switched to the alternative on the owner's order of 2026-10-21 ("set a heartbeat for yourself, every 30m"): a project wake every 30 minutes, job 4c969658, prompt in `wake-manifesto-tone.md`. The earlier decision was none.
6. **Where the rulebook lives:** `plugin/rulebooks/tone-of-voice.md`, a document kind of its own beside `manifestos/` and `digests/`, which `manifesto-writing` reads through `${CLAUDE_PLUGIN_ROOT}`; `generate.py` scans only `plugin/manifestos/`, so the rulebook never enters the manifesto index. Alternative: `plugin/skills/manifesto-writing/tone-of-voice.md`, a file inside the skill's own folder.
7. **What the rulebook covers:** every seed of the stack, S01–S37, phrased as the stance a text takes toward its reader; the direction, meaning and compounding seeds form a short section on what the stance stands on. Alternative: only the stance layers L3–L7, leaving L1, L2 and L8 out.
8. **How the rulebook is written:** rules as positive targets, each with its reason and a check; failures named once, in a checks section, outside the rules; calm emphasis, no capitals for force; sources named by author and year in a closing evidence section, never by the local claim IDs, since the stack files stay unpublished. Alternative: the skill format of paired `never` clauses.
9. **Old tone lines that contradict the stack** (`manifesto-writing`: "It assumes the reader is ready to be changed", "Manifestos assume sympathetic readers", "Manifestos sacrifice precision for force", "Make the stakes clear"; the tone markers "Moral urgency", "Direct address", "Academic hedging"): moved out of the skill and superseded by the rulebook's rules, not carried into it. Alternative: carry them into the rulebook beside the new rules.
10. **The 2026-10-11 register lessons in `orchestration_log/reference/conventions.md`** (one identity attack per section, ALL-CAPS floors, fragment floors): read as scoped to the lines-spent v2 build, as owner ruling 6 says ("in force for v2"); the section gains a scope line naming that build and pointing new tone work to the rulebook. Alternative: leave `conventions.md` as it stands, its lessons read as general.
11. **Release:** none from here; the rulebook and the skill edit stay on `session/manifesto-tone` until the owner integrates them, with the version bump and tag at release (unsolved 2). Alternative: bump to 3.4.0 on the branch now.

## Resolved in a round

1. **Publishing the elevation-stack files** (round of 2026-10-21): the owner chose "Keep them local"; the stack files and the researcher's outputs stay untracked, excluded through `.git/info/exclude`. The tone line (same round): the owner chose "Reader stance only"; stance toward the reader, register, force, hedging, praise and blame, and the framing of the enemy move to the rulebook, while naming an enemy, ending on a choice, section length, tables and the transformation process stay in `manifesto-writing`.
