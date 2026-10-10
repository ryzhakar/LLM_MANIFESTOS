# Re-cut: kiss.md, 2026-10-11

Cause: `lines-spent` ship (commit b348908). SPEC §10 "Absorbed from kiss". Kiss version stays 2.0.0; the block sat under `## Commands`, outside `## Name Your Enemy`.

## Rows moved

Old kiss lines are those before commit e3181dd (321 lines). New kiss: 311 lines. Destination lines are in `manifestos/lines-spent.md`. Content moved, not wording.

| old kiss line | row (quoted) | lines-spent line |
|---|---|---|
| :157 | `### Delete Code` | none (heading dropped) |
| :159 | "Remove dead code immediately. Delete speculative "future" code. Delete "just in case" functions." | :48 "Every addition. Test or requirement named? New symbol's caller or test in your diff?" and :49 "Code your change left uncalled. Deleted, same diff?" |
| :161 | "Every line you don't write is a line you don't maintain, test, debug, or understand." | :38 "When you pull a package, you hand a stranger the designing, writing, testing, debugging and maintaining." |
| :163 | "Less code = fewer bugs." | :27 "SPENT. Its bugs are your bugs." and :38 "I debug your outage." |
| :165 | "The best code is no code." | :34 "Name your non-code options first, starting with no code." and :47 "...no code first?" |

Lines :158, :160, :162, :164, :166 (blank separators) left with the block; `### Write Small Units` moved from :167 to :157.

## Held ground after

Kiss keeps its enemy ("Complexity is killing your software.", kiss.md:20), its tagline ("incidental is Latin for your fault"), and version 2.0.0; lines-spent holds the lines-of-code ground.
