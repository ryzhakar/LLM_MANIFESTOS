# Decisions

**Holds:** append-only rulings: decision, one-line why, license tag, evidence.
**Does not hold:** open questions (`user_deferred_items.md`), standing rules (`conventions.md`).
**Mutability:** appended in the turn a decision lands; entries are never edited or deleted.

---

## 2026-04-29 — Manifesto filenames are kebab-case

Plain kebab-case matches the pipeline glob and the existing files; the `Manifesto, X.md` examples in MAINTAINERS_GUIDE are illustrative, not prescriptive.
License: orchestrator-call.
Evidence: commit 67542f2; `manifestos/` listing.

## 2026-05-01 — `only-fluff-die.md` replaced by `stop-yapping.md`

Same function (assistant language compression), rebuilt in a harsher, model-addressed register at owner direction after seven failed drafts.
License: owner-ruling.
Evidence: commit d94e962; `orchestration_log/history/2026-05-01/`.

## 2026-05-01 — `ai-instructions` theme rejected for the compression manifesto

Every manifesto in this collection is an AI instruction by definition, so the theme cannot differentiate; `cognitive-science` holds.
License: orchestrator-call.
Evidence: commit d94e962; `manifestos/stop-yapping.md` frontmatter.

## 2026-05-11 — `postgres.md` v3 promoted, prior drafts removed

The third full rewrite carried the required register; editorial passes on measured prose had plateaued (register ceiling).
License: owner-ruling.
Evidence: commits f281691, e76616e, 02a5668; `orchestration_log/history/2026-05-11/`.

## 2026-08-10 — `cargo-cult-science.md` ships Feynman's address verbatim

Owner directive: absolute minimum changes to content, so only transfer artifacts were repaired (HTML italics spacing, a soft hyphen, curl progress noise spliced into "teaching"); the Caltech transcription's own typos stay pending an owner call. Theme `cognitive-science`; tagline and description drawn from Feynman's own words.
License: owner-ruling.
Evidence: `manifestos/cargo-cult-science.md`; source https://calteches.library.caltech.edu/51/2/CargoCult.htm.

## 2026-08-10 — Memory layer reshaped to the five-file contract

Owner directive; the `agentic-delegation` 4.2.0 ARRIVE protocol reads `ground-truth.md`, `user_deferred_items.md`, `decisions.md`, `capabilities.md`, `conventions.md`. `codebase_state.md` folded into `capabilities.md`; `deferred_items.md` folded into `user_deferred_items.md`; both originals deleted.
License: owner-ruling.
Evidence: `orchestration_log/reference/` tree; `~/.claude/plugins/cache/my-claude-skills/orchestration/4.2.0/skills/agentic-delegation/SKILL.md`.
