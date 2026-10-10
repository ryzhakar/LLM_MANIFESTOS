Loaded in full from source: manifestos/first-principles.md; instructions/strunk_spr_v3_complete.xml (2923 lines); manifesto/skills/manifesto-oath/SKILL.md; binding protocol run on all three.
Interplay: First Principles and Strunk converge on atoms over analogy (a finding is a quote with a location; a sentence is concrete, positive, active); they pull apart where economy meets a format that demands completeness, and clarity wins.
Commitments: I must report only located, quoted facts, and I will name no author a source does not name; I must not mistake a name for a source, and I will not fill a blank with a guess; I must write active, positive, concrete prose, and I will omit needless words.

# Close open items

Outcome: 3 of 4 attribution lines landed. The fourth (self-documenting-code.md) is blocked: the archive source names no author. QuickDraw removed. Deferred items edited. Pushed. Label for every finding below: practiced (the shipped files and commits show it) unless marked otherwise.

## Attribution lines — file | line added | source of the names

| file | line added | source of the names |
|---|---|---|
| manifestos/intervention.md | `*Original, 2026*` at :99, after `---` at :97 | No names. Year from `git log --diff-filter=A --format=%ad --date=short -- manifestos/intervention.md` = 2026-04-22. |
| manifestos/postgres.md | `*After the maintainer's raw materials, 2026-05-11*` at :275, after `---` at :273 | Text given by owner ruling (a). Provenance check (learned): orchestration_log/history/2026-05-11/session.md:18 reads "Invoked /spec-chef on user-prepared substrate (`postgres-manifesto-raw-materials.md`, 504 lines)". The file entered git on 2026-05-11 (`git log --diff-filter=A`). |
| manifestos/cargo-cult-science.md | byline at :14 now `*by RICHARD P. FEYNMAN, 1974*` (was `*by RICHARD P. FEYNMAN*`) | Year 1974 given by owner; manifestos/cargo-cult-science.md:16 reads "Caltech's 1974 commencement address". |
| manifestos/self-documenting-code.md | NOT ADDED | Blocked. archive/software_building_principles/SELF_DOCUMENTING_CODE.md holds 459 lines and names no author: :1 reads "# The Self-Documenting Code Manifesto"; :459 reads "Remember: Every line of code you write is teaching someone about your domain. Make it a good teacher."; a case-insensitive search for martin, beck, fowler, hunt, thomas, knuth, mcconnell, hickey, kernighan, plauger, ousterhout, evans, author, credit, source returns no author name (the hits are code identifiers such as `credit_score` and the code comment at :66 "TODO: Remove after customers migrate off v1 API"). The only provenance records are learned, not names: orchestration_log/history/2026-10-10/manifesto-definition.md:127 marks the file "transformed"; :168 reads "Four files carry none (intervention, self-documenting-code, postgres, zen) | Inconsistent; no rule for user-authored substrate". The archive file entered git in 7f3aa49 (2025-12-16, "chore: archival docs"). The task text says "[the authors the archive source names, in its order]"; that list is empty. No line written; no name invented. |

Body edits: none beyond the lines above. `git diff` showed 9 insertions, 1 deletion across the three files.

Generator and tests: bare `python3 generate.py` fails (`ModuleNotFoundError: No module named 'frontmatter'`). Ran the same scripts through the justfile's dependency set: `uv run --with pyyaml --with python-frontmatter --with pydantic --with jinja2 --with rich python3 generate.py` printed "Generated README.md from 12 manifesto(s)"; the same prefix with `python3 tests/test_generate.py` ended "0 failed" (14 PASS lines in the tail, including `test_every_shipped_manifesto_validates`). README.md did not change; no regenerate commit. Deleted the `__pycache__` directories the run created.

## QuickDraw — path removed, file count, README rows changed

- Path removed (`git rm -r`): resources/2026-10-11-code-liability-and-dependencies/secondary/breadth/chm-quickdraw/102658076_quickdraw_acc/ — the directory holding COPYRIGHT.TXT. Its parent chm-quickdraw/ held nothing else and no longer exists.
- File count: 38 (COPYRIGHT.TXT plus 37 files under `QuickDraw Source/`). `find resources -iname 'COPYRIGHT*'` now returns nothing.
- Licence text: COPYRIGHT.TXT:3 read "This Material is Copyright � 1984 Apple Inc. and is made available only for non-commercial use."
- README (resources/2026-10-11-code-liability-and-dependencies/README.md), 77 lines changed:
  - 38 rows in the `## secondary/` table (were :137-174): the preview cell now reads `removed: non-commercial license; sha256 kept`; path and survey cells unchanged.
  - 38 rows in the `## sha256 pairs` table (were :394-431): note appended to the first cell after the path (`` `secondary/...` — removed: non-commercial license; sha256 kept ``); origin and both sha256 values unchanged.
  - 1 line, the `secondary/` row of the folder table (:10): "(209 files; ...)" became "(209 files at copy time; the 38 QuickDraw files under `breadth/chm-quickdraw/` were removed later: non-commercial license; sha256 kept; ...)". Added so the count stays true.
- Left as is: README rows for evidence/chm-quickdraw.html, evidence/chm-quickdraw.txt, breadth/chm-macpaint.html (web pages, not the source tree); the `chm-quickdraw.zip` row in "Not copied" (:259; the zip never entered the repository); references in research/ and orchestration_log/ notes (outside the named files).
- Fact: the files remain in git history (added in 9e8c738). The commit removes them from the tree only; no history rewrite.

## Deferred — items and their resolution text

File: orchestration_log/reference/deferred_items.md.

- Header line: "Updated 2026-10-11: OQ-001, OQ-002, OQ-004, and OQ-005 resolved; OQ-006 narrowed to two files."
- OQ-004: `**Status:** Resolved (2026-10-11, on claude-skills branch manifesto-binding-channel)`. Body keeps the finding in past tense; "Action needed" line removed. The branch claim comes from the task text; I did not open the plugin branch.
- OQ-005: `**Status:** Resolved (2026-10-11, on claude-skills branch manifesto-binding-channel)`. Same treatment; same source for the claim.
- OQ-006: `**Status:** Partly resolved (2026-10-11, `64ef632`)`. Body: "`64ef632` (`chore: attribution lines on three manifestos`) added `*Original, 2026*` to `intervention.md` and `*After the maintainer's raw materials, 2026-05-11*` to `postgres.md`, and set the `cargo-cult-science.md` byline to `*by RICHARD P. FEYNMAN, 1974*`. Open: `self-documenting-code.md` carries no attribution line; its archive source `archive/software_building_principles/SELF_DOCUMENTING_CODE.md` names no author. `zen-of-python.md` carries no attribution line; it lay outside the closing scope. **Action needed:** The owner rules the attribution line for both files."
- Departure from the task text: the task says mark OQ-006 resolved. The item named five files; this work fixed three. manifestos/zen-of-python.md still has no `*After ...*`, `*by ...*`, or `*Original ...*` line (`grep -L` over manifestos/*.md lists zen-of-python.md and self-documenting-code.md as the only files without one). Marking "Resolved" would record a false state, so the status reads "Partly resolved" and the commit message says "narrowed".

## Commits — hash | message

| hash | message |
|---|---|
| 64ef632 | chore: attribution lines on three manifestos |
| 8a43fe5 | chore(resources): remove QuickDraw source, non-commercial license |
| 98462cf | doc: deferred items — OQ-004, OQ-005 resolved, OQ-006 narrowed |

Two messages differ from the task text: "four manifestos" became "three" (three files changed); "OQ-006 resolved" became "OQ-006 narrowed" (see Deferred). No "chore: regenerate README" commit (README unchanged). Messages are single-line, no trailers, explicit paths; drafts/ untouched (drafts/owned-lines/reviews/ and v1.md remain untracked, owned by the other agent).

## Push

`git push origin claude/manifesto-design-discussion-liuuvf` succeeded on the first attempt: `79b4954..98462cf`. No retry, no rebase, no force. `git status -sb` shows the branch level with origin.

## Open for the owner

1. self-documenting-code.md: no author in the archive source. Options the owner can rule: name the authors, or `*Original, 2026*` (first commit 2026-04-22), or another line.
2. zen-of-python.md: no attribution line; outside this task's file list.

Summary for notification: Attribution lines landed on intervention, postgres, and cargo-cult-science; self-documenting-code is blocked because its archive source names no author, and zen-of-python lies outside scope. The QuickDraw tree (38 files) left the repository with 77 README lines marked "removed: non-commercial license; sha256 kept", and OQ-004 and OQ-005 are marked resolved on the plugin branch while OQ-006 reads partly resolved at 64ef632. Three commits are pushed (79b4954..98462cf) without retries.

## Addendum — coordinator rulings after the first push

Supersedes the "NOT ADDED" row, the OQ-006 "Partly resolved" text, and "Open for the owner".
- manifestos/self-documenting-code.md: `*Original, 2026*` appended after `---` (ruling: archive source names no author).
- manifestos/zen-of-python.md: `---` and `*by TIM PETERS, 2004*` appended (ruling: canon; PEP 20 date). The file had no trailing newline; the diff shows its last line re-terminated.
- Generator via uv: "Generated README.md from 12 manifesto(s)"; tests "0 failed". README.md unchanged; no regenerate commit.
- OQ-006: `**Status:** Resolved (2026-10-11, `64ef632`, `40323db`)`; header line lists OQ-006 resolved.

| hash | message |
|---|---|
| 40323db | chore: attribution lines on self-documenting-code and zen-of-python |
| e5f7223 | doc: deferred items — OQ-006 resolved |

Push: `98462cf..e5f7223` on the first attempt; branch level with origin. All five attribution targets and OQ-004, OQ-005, OQ-006 are closed.
