# r4 closure — drafts/owned-lines/v5.md

v5 = v4 with the three r4-accuracy fixes and nothing else (owner's final ruling: facts only, no further round). `diff v4.md v5.md | grep -c '^[<>]'` = 6.

## Edits

| r4-accuracy finding | v5 line | v4 text | v5 text |
|---|---|---|---|
| 1 — third behavior claim (ruling 3) | v5:38 | "Who pulls a stranger's EIGHT LINES into my build unopened? YOU. An owner who never looked." | "Pulled unopened, a stranger's EIGHT LINES are yours. An owner who never looked." |
| 2 — reader identified with the V3 agent | v5:42 | "That agent is you." | "You are an AI coding agent." |
| 3 — "I pulled." not verbatim to the enemy line | v5:20 | `"I added." "I pulled."` | `"I added." "Pulled in."` |

## Measures (v5)

Script: scratch copy of corpus_metrics.py, MANIFESTO_DIR set to a temp dir holding only v5.md. Grep runs on the body (file lines 11 to the end).

| metric | v5 | floor | pass |
|---|---|---|---|
| body words | 909 | < 1500 | yes |
| section words | opening 123 (title included), 134, 119, 123, 119, 144, 126 | < 145 | yes |
| max sentence | 29 (one fury run, v5:16). Attribution 20 (ruling 5). All others ≤ 19 | ruling 18 | yes |
| 2nd person /1k | 70.4 (64) | ≥ 70 | yes |
| fragments /1k, file | 66.0 | ≥ 50 | yes |
| fragments /1k by section | 82.6, 52.2, 58.8, **48.8** (YOU OWN WHAT YOU PULL, 6/123), 75.6, 83.3, 71.4 | ≥ 50 each | **no: shortfall** |
| ALL-CAPS, body text without headings | 45 caps. 50.8 /1k on the 886 non-heading words. **49.5 /1k** on all 909 body words, the base the r3 register reviewer led with | ≥ 50 | yes on the non-heading base. **Shortfall of 0.5** on the all-words base |
| imperative % (heuristic) | 22.0 (28/127) | ≥ 21.5 | yes |
| hedges | 0 | 0 | yes |
| semicolons (grep) | 0 | 0 | yes |
| colons (grep) | 0 | ≤ 2 /1k | yes |
| comma + and/which/until (grep) | 1 (attribution, v5:74) | ≤ 2 /1k | yes |
| multi-word shouts (grep, headings excluded) | 12 | ≥ 8 | yes |
| bindable ratio (precision count, ruling 11) | 25/35 = 0.714. Numerator: v5:20, 24–30, 34, 42, 46–58, 60, 68. Line count unchanged; v5:20 and v5:42 keep their counted heads | ≥ 0.70 | yes |

## Shortfalls (kept: facts win)

- **YOU OWN WHAT YOU PULL fragments: 48.8 /1k against 50.** Edit 1 removed the fragment "YOU." (v4:38). One more fragment in that section would restore the floor. The owner's ruling bars any further edit, so none is made.
- **Body caps: 49.5 /1k on the all-words base.** Edit 1 removed the caps word "YOU". The non-heading base reads 50.8 and passes.

## v6

v6 = v5 with the three r4-precision fixes and nothing else. `diff v5.md v6.md | grep -c '^[<>]'` = 6.

### Edits

| r4-precision finding | v6 line | v5 text | v6 text |
|---|---|---|---|
| 1 — check 12 drops "from a package"; "Its" binds to function | v6:57 | `12. Copy of a function. Its license and copyright notice carried?` | `12. Function copied from a package. Package's license and copyright notice carried?` |
| 2 — check 2 "starting with no code" orders only the non-code subset | v6:47 | `2. Ruled-out options, existing code and non-code starting with no code, named before any added line?` | `2. Ruled-out options, existing code and non-code, named before any added line, no code first?` |
| 3 — "Same tests?" loses the pass observable | v6:34 | `Two versions. Same tests?` | `Two versions pass the same tests?` |

### Measures (v6)

Script: scratch copy of corpus_metrics.py, MANIFESTO_DIR set to a temp dir holding only v6.md. Grep runs on the body (file lines 11 to the end).

| metric | v6 | floor | pass |
|---|---|---|---|
| body words | 911 | < 1500 | yes |
| section words | opening 123 (title included), 134, 121, 123, 119, 144, 126 | < 145 | yes |
| max sentence | 29 (one fury run, v6:16). Attribution 20 (ruling 5). All others ≤ 19 | ruling 18 | yes |
| 2nd person /1k | 70.3 (64) | ≥ 70 | yes |
| fragments /1k, file | 62.6 | ≥ 50 | yes |
| fragments /1k by section | 82.6, 52.2, **41.3** (THE LEAST YOU CAN DO, 5/121), **48.8** (YOU OWN WHAT YOU PULL, 6/123), 75.6, 76.4, 71.4 | ≥ 50 each | **no: two shortfalls** |
| ALL-CAPS, body text without headings | 45 caps. 50.7 /1k on the 888 non-heading words. **49.4 /1k** on all 911 body words | ≥ 50 | yes on the non-heading base. **Shortfall of 0.6** on the all-words base |
| imperative % (heuristic) | **21.4** (27/126) | ≥ 21.5 | **no: shortfall of 0.1** |
| hedges | 0 | 0 | yes |
| semicolons (grep) | 0 | 0 | yes |
| colons (grep) | 0 | ≤ 2 /1k | yes |
| comma + and/which/until (grep) | 1 (attribution, v6:74) | ≤ 2 /1k | yes |
| multi-word shouts (grep, headings excluded) | 12 | ≥ 8 | yes |
| bindable ratio (precision count, ruling 11) | 25/35 = 0.714. Numerator: v6:20, 24–30, 34, 42, 46–58, 60, 68. The three edits change no line's status | ≥ 0.70 | yes |

### Shortfalls (kept: facts win)

- **THE LEAST YOU CAN DO fragments: 41.3 /1k against 50.** Edit 3 merged the fragments "Two versions." and "Same tests?" into one 6-word sentence.
- **YOU OWN WHAT YOU PULL fragments: 48.8 /1k.** Carried over from v5.
- **Imperative heuristic: 21.4 % against 21.5.** Edit 1 removed "Copy of a function.", which the heuristic counted as an imperative.
- **Body caps: 49.4 /1k on the all-words base.** Carried over from v5. The non-heading base reads 50.7.

## v7

v7 = v6 with the rule-correctness fixes for r4-maximalist #6, #8, #10, #11, #12, #13, #15 and #16, using the reviewer's own fixes, and nothing else. #8 ends at "frontier." #12 is replaced, not deleted, per the owner. #1–#5, #9, #14 and #17 are skipped (restatements; voice stays by owner ruling). `diff v6.md v7.md | grep -c '^[<>]'` = 12 (≤ 16).

### Edits

| r4-maximalist finding | v7 line | v6 text | v7 text |
|---|---|---|---|
| 6 — check 3 misses additions inside existing functions | v7:48 | `3. New function or file. Test or requirement named? Caller or test in your diff?` | `3. Every addition. Test or requirement named? New symbol's caller or test in your diff?` |
| 8 — "this fight skips it" is an escape | v7:34 | "Code that gets better over time is the frontier and this fight skips it." | "Code that gets better over time is the frontier." |
| 10 — "upkeep" unglossed | v7:38 | "Read maintaining as adapting your line to change." | "Read upkeep and maintaining as adapting your line to change." |
| 11 — "I debug your line" vs the stranger's debugging | v7:38 | "I debug your line." | "I debug your outage." |
| 12 — COURIER carries what it does not own (ruling 20) | v7:38 | "Pull it unopened and you're a stranger's COURIER." | "Pull it unopened and you ship a stranger's code as yours. A RUBBER STAMP." Ownership stays on the reader ("as yours"). The identity attack is "A RUBBER STAMP." (what the reader is, no job-title noun) |
| 13 — "Check 5 proves you kept it" false at literal reading | v7:42 | "Check 5 proves you kept it." | "Check 5 asks for the passing run that proves it." |
| 15 — "none stated" passes silence | v7:50 | `Protecting tests named, or none stated?` | `Protecting tests named, or "none exist" stated?` |
| 16 — check 13 passes unread notes | v7:58 | `13. Upgrade. Diff or release notes cited?` | `13. Upgrade. Diff or release notes read and cited?` |

### Measures (v7)

Script: scratch copy of corpus_metrics.py, MANIFESTO_DIR set to a temp dir holding only v7.md. Grep runs on the body (file lines 11 to the end).

| metric | v7 | floor | pass |
|---|---|---|---|
| body words | 921 | < 1500 | yes |
| section words | opening 123 (title included), 134, 116, 131, 123, **147** (BEFORE YOU SHIP), 126 | < 145 | **no: checklist 147** |
| max sentence | 29 (one fury run, v7:16). Attribution 20 (ruling 5). All others ≤ 19 | ruling 18 | yes |
| 2nd person /1k | **68.4** (63/921) | ≥ 70 | **no** |
| fragments /1k, file | 63.0 | ≥ 50 | yes |
| fragments /1k by section | 82.6, 52.2, **43.1** (THE LEAST YOU CAN DO, 5/116), 53.4, 73.2, 74.8, 71.4 | ≥ 50 each | **no: one section** |
| ALL-CAPS, body text without headings | 46 caps. 51.2 /1k on the 898 non-heading words. **49.9 /1k** on all 921 body words | ≥ 50 | yes on the non-heading base. **Shortfall of 0.1** on the all-words base |
| imperative % (heuristic) | **21.3** (27/127) | ≥ 21.5 | **no: shortfall of 0.2** |
| hedges | 0 | 0 | yes |
| semicolons (grep) | 0 | 0 | yes |
| colons (grep) | 0 | ≤ 2 /1k | yes |
| comma + and/which/until (grep) | 1 (attribution, v7:74) | ≤ 2 /1k | yes |
| multi-word shouts (grep, headings excluded) | 13 (adds RUBBER STAMP) | ≥ 8 | yes |
| identity attack, YOU OWN WHAT YOU PULL | "A RUBBER STAMP." and "An owner who never looked." | ≥ 1 | yes |
| bindable ratio (precision count, ruling 11) | 25/35 = 0.714. Numerator: v7:20, 24–30, 34, 42, 46–58, 60, 68. No line changes status | ≥ 0.70 | yes |

### Shortfalls (kept: facts win)

- **BEFORE YOU SHIP: 147 words against < 145.** Fix #15 adds "exist" and fix #16 adds "read and".
- **2nd person: 68.4 /1k against 70.** Fix #13 removed "you" ("proves you kept it" became "proves it"), and the fixes added 10 words.
- **THE LEAST YOU CAN DO fragments: 43.1 /1k.** Carried over from v6; fix #8 shortened the section but added no fragment.
- **Imperative heuristic: 21.3 %.** Carried over from v6, diluted by the new sentence "A RUBBER STAMP."
- **Body caps: 49.9 /1k on the all-words base.** The non-heading base reads 51.2.
- **Cleared since v6:** YOU OWN WHAT YOU PULL fragments are now 53.4 /1k, because fix #12 added the fragment "A RUBBER STAMP."
