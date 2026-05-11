# Conventions

_Established: 2026-04-29, first session. Items tagged [ORCHESTRATOR: verify] require confirmation from session history or the human maintainer before being treated as settled._

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

Established in the 2026-04-29 session (only-fluff-die.md). Verified by execution.

1. **Research tree** — clone/read source material. Dispatch parallel haiku agents across content facets (philosophy, behavioral spec, implementation, external context). Each writes a structured report to `research/{topic}/categories/`.
2. **Curated extraction** — Opus subagent reads all category reports + the manifesto-writing skill spec + existing manifestos for calibration. Produces a selective extraction brief: what crosses the manifesto threshold, what doesn't, where the hard decisions lie.
3. **Deep-dives** — targeted Tier 3 agents (sonnet for reasoning, haiku for mechanical extraction) on specific gaps: writing methodology, operational rules extraction, binding effectiveness analysis.
4. **Final writer brief** — Opus subagent reads ALL prior reports (pointed to file paths, never relayed content). Produces writer-ready brief organized by the manifesto-writing skill's process.
5. **Oath-bound writing** — Opus subagent reads manifesto-oath protocol and manifesto-writing skill, executes the binding ceremony (identity-mode), then writes the manifesto under constitutional constraint. Runs self-referential checklist before delivery.
6. **Validation** — run `just readme` to confirm schema compliance. Commit.

**Critical convention:** The writer agent must always be oath-bound to `/manifesto-writing` via `/manifesto-oath` before receiving source material.

**Writing methodology references:** `instructions/strunk_spr_v3_complete.xml` and `instructions/sparse-priming-representations.md` are loaded as writing technique guidance (not content) for the writer agent.

**Lessons from 2026-05-01 session (7 failed drafts before success):**

- **Constrain fury aggressively, structure minimally.** All dispatched agents front-loaded 10+ structural constraints with emotional instruction last. The constraints won every time. Invert: lead with the emotional mandate, give minimal structural requirements.
- **Prompt register determines output register.** The writer mirrors the orchestrator's tone. A measured prompt produces measured output regardless of "write with fury" instructions.
- **2-4 source files, not 15.** Information overload → skimming → measured output. Depth over breadth.
- **The orchestrator edits, not rewrites.** The agent produces the base content (structure, tables, rules). The orchestrator edits the register and form. This is cheaper and more effective than re-dispatching. The $15 orchestrator cost in the 2026-05-01 session was mostly learning what to ask for — the actual value was in two direct edit passes on agent output.
- **Write tool requires reading existing files → contamination.** Write to a FRESH path when the writer must not inherit from previous drafts. Delete the old file first if reusing the path.
- **Do not pre-decide branding.** Let the writer choose title, tagline, theme, description unless the user specifies.

**Lessons from 2026-05-11 session (3 rewrites, register breakthrough):**

- **Full rewrites beat editorial passes for register changes.** Editing measured prose produces measured edits. Write to a fresh path when the register must break. The existing file's voice bleeds through edits.
- **Unbiased reviewers override orchestrator judgment.** Dispatch 5 specialized reviewers (accuracy, completeness, boundaries, scope, precision) against the substrate. Their findings are authoritative — the orchestrator is biased toward its own output.
- **Prescription and diagnosis must share the same voice.** Teaching and attacking are not separate passes. Every explanation is something the reader should already know, delivered as an accusation. The feedback "diagnosis thorough, prescription thin" signals structural failure, not register failure.
- **Anti-Claude patterns are a checklist, not a mindset.** Document them (`anti-claude-patterns.md`), check against them mechanically. The orchestrator cannot self-detect its own patterns by introspection — it needs an external list.
- **Register ceiling is real.** The orchestrator will hit a register ceiling where editorial passes stop improving. User escalation ("HARDER") is the mechanism that breaks through. Plan for 2-3 rounds of user-driven escalation, not one-shot delivery.
- **External feedback on structure comes AFTER register work.** Register problems mask structural problems. Fix register first, then evaluate whether the structure serves the audience.

---

## Dispatch Rules

### When to use a sub-agent

- Reading multiple manifesto files in parallel to extract frontmatter: parallelize with Haiku agents
- Git history analysis: Haiku
- Drafting a new manifesto description/tagline for human review: Sonnet
- Writing a full manifesto body: Opus
- Assessing whether a candidate principle meets the manifesto quality bar: Opus or Sonnet with explicit criteria from MAINTAINERS_GUIDE

### When NOT to use a sub-agent

- Simple single-file reads: do it inline
- Running `just readme`: run in the main session, inspect output directly
- Committing changes: always in the main session, never delegated

### Parallelization opportunities

- Frontmatter extraction across all 10 manifestos can be done in a single parallel batch
- Theme discrepancy checks can run concurrently with manifesto reads
- Research across archive subdirectories can be parallelized

---

## Forbidden Patterns

These are anti-patterns derived from the project's own philosophy and structure. Treat violations as blockers.

**Never manually edit `README.md`.** It is a generated artifact. MAINTAINERS_GUIDE states this explicitly. Any edit will be overwritten on the next `just readme` run and will cause confusion in the interim.

**Never commit a manifesto without running `just readme`.** README drift is silent corruption of the collection's navigation layer.

**Never use patch versions (`x.y.z` where z > 0).** MAINTAINERS_GUIDE states: "Patches — don't use; just edit." The one existing violation (`first-principles.md` at `1.0.1`) is noted as debt in `deferred_items.md`.

**Never create a single-manifesto theme.** MAINTAINERS_GUIDE: "Each theme should contain 2+ manifestos." Do not add a theme until at least two manifestos will use it.

**Never add a manifesto without a theme entry in `themes.yaml`.** The pipeline will warn and render the manifesto without icon or display name. Fix `themes.yaml` first.

**Never treat a manifesto as living documentation.** Manifestos are behavioral constitutions — rare, significant artifacts. Frequent small edits signal the principle has not crystallized yet.

---

## Frontmatter Schema

Source: `generate.py` `ManifestoMetadata` Pydantic model (lines 20–34) and MAINTAINERS_GUIDE Reference section.

```yaml
---
title: string       # Human-readable name. Any string. Required.
tagline: string     # Memorable hook. Any string. Required.
version: string     # Semver. Must match ^\d+\.\d+\.\d+$ (e.g., "1.0.0"). Required.
theme: string       # Must be a key in themes.yaml (warns if missing, does not fail). Required.
description: string # One sentence explaining why this matters. Any string. Required.
---
```

**Validation behavior:**
- Missing any required field: file is skipped with error panel; pipeline continues with remaining files
- Invalid `version` format: same as above
- Theme not in `themes.yaml`: warning panel printed, but file IS included in output (degrades gracefully — renders without icon/name)
- Extra fields in frontmatter: not validated; Pydantic ignores them by default [ORCHESTRATOR: verify — `ManifestoMetadata` does not set `model_config = ConfigDict(extra='forbid')`, so extra fields are silently ignored]

**Version conventions (from MAINTAINERS_GUIDE):**
- `x.0.0 → x+1.0.0`: Major thesis change. Rare and significant.
- Minor/patch bumps: discouraged. Just edit the file without incrementing.
- Current major-version manifestos: `kiss.md` (2.0.0), `simple-made-easy.md` (2.0.0)

---

## File Naming

**Manifestos:** kebab-case `.md` files in `manifestos/`. No spaces. No `Manifesto,` prefix (despite MAINTAINERS_GUIDE examples showing `Manifesto, <principle>.md` — actual files use plain kebab-case like `correct-by-construction.md`).

> Note: MAINTAINERS_GUIDE workflow examples show `touch "manifestos/Manifesto, <principle>.md"` with a comma and capital M. Actual files in the repo do NOT follow this pattern. Treat the kebab-case convention (matching existing files) as authoritative. The MAINTAINERS_GUIDE examples are illustrative, not prescriptive.

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

`orchestration_log/history/*/cost.md` is gitignored per `.gitignore`. All other orchestration log content is tracked.
