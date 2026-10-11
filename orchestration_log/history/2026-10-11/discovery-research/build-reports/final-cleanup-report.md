BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines through `</instruction_matrix>`); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full
INTERPLAY: First Principles and Strunk converge on the checked atom over the label (verify the irreducible; definite, specific, concrete; omit needless words); they pull apart where First Principles throws out the playbook while the prompt is a playbook and the INDEX rows hold an inherited shape; resolved: run the prompt as written because it is the task, keep the INDEX columns because the existing 37 rows read that way, and state only what a command or file showed.
COMMIT: I must verify each claim against a command result or file line, and I will name that source; I must not recommend or conclude past the records, and I will state each open item as a fact; I must omit needless words, and I will hold each line to one fact.

# Final cleanup — 2026-10-11

Prompt: `/home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/build/final-cleanup.md`. Repository `/home/user/LLM_MANIFESTOS`, branch `claude/manifesto-design-discussion-liuuvf`, HEAD at start `82b0dbd`.

This file is committed in step 2. It records steps 1 and 2 as done and states what steps 3 to 5 target. Hashes of the step 2 to 4 commits and the push result are not in this file; `git log` and the dispatch return carry them.

## Step 1 — `.gitignore`

- Line 3 changed from `research/` to `/research/` (`.gitignore:3`).
- Commit `563ab6d` `chore: ignore only the root research folder`; 1 file, 1 insertion, 1 deletion.
- `git check-ignore -v archive/research/PERSONA_DESIGN_RESEARCHER.md` printed nothing before and after the edit, exit 1 after. Git skips tracked paths in this form.
- `git check-ignore -v --no-index archive/research/PERSONA_DESIGN_RESEARCHER.md` printed `.gitignore:3:research/` before the edit and nothing after, exit 1.
- `git check-ignore -v research/manifesto-craft/BRIEF.md` printed `.gitignore:3:/research/	research/manifesto-craft/BRIEF.md` after the edit, exit 0.
- `git check-ignore -v --no-index` on `build-reports/ship-report.md` and `prompts/build/ship.md` under the history folder printed nothing; both paths are visible to git.

## Step 2 — preserved build artifacts

Copied with `cp -p`; `sha256sum` of each origin and copy compared; 26 of 26 match; 0 mismatches. `stat` shows equal mtimes (checked on `ship-report.md`).

`build-reports/` — 8 files, from `research/manifesto-craft/discovery/*-report.md`:
`close-open-items-report.md`, `collection-schema-report.md`, `maintainers-guide-report.md`, `plugin-hooks-fix-report.md`, `research-commit-report.md`, `resources-commit-report.md`, `ship-report.md`, `skill-rewrite-report.md`.

`prompts/build/` — 18 files, from `research/manifesto-craft/prompts/build/` (`find -type f` returns 18):
`_binding-writer.md`, `close-open-items.md`, `collection-schema.md`, `final-cleanup.md`, `maintainers-guide.md`, `plugin-hooks-fix.md`, `review-shared.md`, `session-record.md`, `ship.md`, `skill-rewrite.md`, `spec-writer.md`, `writer-v1.md` to `writer-v7-facts.md` (`writer-v1`, `v2`, `v3`, `v4-surgical`, `v5-facts`, `v6-facts`, `v7-facts`).

Count facts:
- `session.md` Next Session Priorities item 6 names 8 reports and 17 prompts (25). The folder holds 18 prompts; the extra file is `final-cleanup.md`, this task's prompt.
- This report is the 27th row appended to `INDEX.md`; it has no origin copy.
- `INDEX.md` held 37 data rows before this step and a closing note line; the 27 new rows sit after the last table row (`discovery/candidates.md`) and before the note line.
- `INDEX.md` columns: file, origin path, sha256, bytes. The new report's row records the sha256 of this file as committed in step 2.

## Steps 3 to 5 — targets read before the edits

- `orchestration_log/reference/codebase_state.md:96` "Attribution gaps" bullet names four files without a line and `cargo-cult-science.md` without a year; `:110` Next Actions line asks to add both.
- Attribution state at HEAD, by `grep` on `manifestos/*.md`: 13 of 13 manifestos carry an attribution line. `64ef632` added `*Original, 2026*` to `intervention.md`, `*After the maintainer's raw materials, 2026-05-11*` to `postgres.md`, and `, 1974` to `cargo-cult-science.md`. `40323db` added `*Original, 2026*` to `self-documenting-code.md` and `*by TIM PETERS, 2004*` to `zen-of-python.md`.
- Item numbering in step 4: the prompt names items 3, 4 and 5. In `session.md` lines 217 to 227, items 3, 4 and 5 are the D4 hook half, the footer rationale sentences and the `lines-spent` register work. The prompt's descriptions match items 9 (`codebase_state.md` drift), 7 (`.gitignore:3` depth) and 6 (twenty-five research-only artifacts). The prompt's "leave as is" list matches items 1 (merge), 2 (host run), 3 (D4 hook half) and 8 (QuickDraw). Step 4 edits items 6, 7 and 9.
- `session.md` lines 262 and 263 (Artifacts, Recon) state that the 8 reports and the 17 prompts are "copied nowhere". Step 4's scope is Next Session Priorities; those two lines stay as written.
- `.gitignore` after step 1 still names `/research/`; `codebase_state.md:78` reads "`research/` directory — gitignored" and stays as written.
