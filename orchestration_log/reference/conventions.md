# Conventions

_Established: 2026-04-29, first session. Updated 2026-10-11: writing standard by reference, schema facts, entry gate._

---

## Model Tiers

These are dispatch guidelines for multi-model orchestration on this project. They are not enforced by the tooling; they are working conventions for the orchestrator.

| Tier | Model | Appropriate Work |
|------|-------|-----------------|
| Haiku | Fast/cheap | Frontmatter extraction, schema validation checks, git log parsing, file listing, cost tracking, metric counting |
| Sonnet | Mid-tier | Assessment of manifesto quality, drafting frontmatter fields, reading and reasoning about source code, theme assignment recommendations, reference doc updates |
| Opus | Flagship | Writing manifesto body text, synthesis across multiple sources, strategic judgment (versioning decisions, archival decisions, theme taxonomy redesign) |

**Rationale:** Manifestos are precious artifacts (per MAINTAINERS_GUIDE). Manifesto body writing is a high-stakes task that warrants the most capable model. Mechanical extraction and bookkeeping do not.

---

## Manifesto Writing Process

The writing standard is the `manifesto:manifesto-writing` skill (`manifesto/skills/manifesto-writing/SKILL.md` in the claude-skills marketplace). The entry gate is in `MAINTAINERS_GUIDE.md`, Workflows. This section restates neither.

Dispatch lessons the standard does not carry:

- **Delete the old draft before reusing its path.** The Write tool requires reading an existing file first; the read carries the old draft into the writer's context.
- **Read "diagnosis thorough, prescription thin" as structural failure.** Fix the structure, not the register.
- **Fix register before evaluating structure.** Register problems mask structural problems.
- **Plan 2-3 rounds of requester escalation ("HARDER").** The orchestrator hits a register ceiling that editorial passes do not break.
- **Load `instructions/strunk_spr_v3_complete.xml` and `instructions/sparse-priming-representations.md` as writing technique** for the writer, never as content.

---

## Dispatch Rules

### When to use a sub-agent

- Reading multiple manifesto files in parallel to extract frontmatter: parallelize with Haiku agents
- Git history analysis: Haiku
- Drafting a new manifesto description/tagline for human review: Sonnet
- Writing a full manifesto body: Opus
- Assessing whether a candidate meets the gate tests: Opus or Sonnet with the entry-gate criteria from MAINTAINERS_GUIDE

### When NOT to use a sub-agent

- Simple single-file reads: do it inline
- Running `just readme`: run in the main session, inspect output directly
- Committing changes: always in the main session, never delegated

### Parallelization opportunities

- Frontmatter extraction across all 13 files can be done in a single parallel batch
- Theme discrepancy checks can run concurrently with manifesto reads
- Research across archive subdirectories can be parallelized

---

## Forbidden Patterns

Treat violations as blockers.

- **Never manually edit `README.md`.** `just readme` regenerates it.
- **Never commit a manifesto without running `just readme`.**
- **Never write a minor or patch version.** Versions are `N.0.0`. `first-principles.md` returned to `1.0.0` in `12ba3f1`; no violation remains.
- **Never create a single-file theme.** Each theme holds at least two files.
- **Never add a manifesto without a theme entry in `themes.yaml`.** Fix `themes.yaml` first.
- **Never treat a manifesto as living documentation.**
- **Never place a draft in `manifestos/`.** Drafts live under `drafts/<slug>/`; a draft enters the collection through the entry gate.

---

## Frontmatter Schema

Source: `generate.py`, `ManifestoMetadata` (Pydantic model). Tests: `tests/test_generate.py`, 18 tests.

```yaml
---
title: string        # required. Any string.
tagline: string      # required. At most 8 words unless kind is canon.
version: string      # required. ^\d+\.\d+\.\d+$; write N.0.0.
theme: string        # required. Key in themes.yaml.
description: string  # required. One line.
kind: string         # optional. manifesto (default) | canon
register: string     # optional. contemptuous | declarative | parable | lecture | aphoristic
reader: string       # optional. model | human | unspecified
---
```

**Validation behavior:**
- Missing required field, invalid `version`, unknown `kind`, `register`, or `reader`, or a tagline over 8 words on a non-canon file: file skipped with error panel; pipeline continues with remaining files.
- The tagline rule is a model validator; it runs only after every field validates.
- Theme not in `themes.yaml`: warning panel; file included, rendered without icon or name.
- Duplicate tagline (lowercase, punctuation stripped): warning panel naming each file; never rejects.
- Extra frontmatter keys: ignored (`ManifestoMetadata` sets no `extra` policy; verified 2026-10-11).
- `register` shadows `ABCMeta.register`; `generate.py` filters that single Pydantic warning by message.
- `README.md` shows `kind: canon` as a `canon` badge, and `register` and `reader` in the Quick Reference table and each entry heading.

**Species:** `kind: manifesto` obeys the writing standard. `kind: canon` is verbatim, exempt from form rules (tagline length included), carries register and reader, and carries `*by [author], [year]*`.

**Version conventions:**
- Major only. `N.0.0 → (N+1).0.0` on a thesis change, or when a re-cut removes an enemy-section row.
- Minor and patch segments are forbidden. `generate.py` accepts any `x.y.z`.
- Current major-version manifestos: `kiss.md` (2.0.0), `simple-made-easy.md` (2.0.0).

---

## File Naming

**Manifestos:** kebab-case `<slug>.md` files in `manifestos/`. No spaces. No `Manifesto,` prefix (for example `correct-by-construction.md`).

**Drafts:** `drafts/<slug>/` holding `SPEC.md`, `v1.md`, `v2.md`, `reviews/`. At ship, `SPEC.md` and `reviews/` move to `orchestration_log/history/<date>/<slug>/`; the draft versions are deleted.

**Re-cut records:** `orchestration_log/history/<date>/recut-<slug>.md` (`<slug>` names the cut; for one file, the file's base name), for a re-cut without a draft.

**Substrate:** `resources/<date>-<slug>/`.

**Themes:** kebab-case keys in `themes.yaml` (e.g., `software-engineering`, `cognitive-science`).

**Archive materials:** No enforced naming convention observed. Existing archive subdirectories use underscore-separated names (`software_building_principles/`) and uppercase names (`DIETER_RAMS_FORENSIC_REPORT.md`). These are source materials, not manifestos.

**Orchestration log:** Date-keyed directories (`YYYY-MM-DD`) under `history/` and `recon/`. Reference docs live in `reference/` (flat, no date subdirectory).

---

## Orchestration Log Structure

```
orchestration_log/
├── history/
│   └── YYYY-MM-DD/     # Session logs, cost.md (gitignored)
├── recon/
│   └── YYYY-MM-DD/     # Reconnaissance outputs (e.g., git_history.md)
└── reference/          # Living reference docs (this file and siblings)
    ├── codebase_state.md
    ├── deferred_items.md
    └── conventions.md
```

Entry-gate discovery trees live under `history/<date>/discovery-research/`; shipped specs and reviews under `history/<date>/<slug>/`; re-cut records at `history/<date>/recut-<slug>.md`. `orchestration_log/history/*/cost.md` is gitignored per `.gitignore`. All other orchestration log content is tracked.
