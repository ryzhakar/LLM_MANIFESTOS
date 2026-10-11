# Deferred Items

_First session — 2026-04-29. Updated 2026-10-11: OQ-001 and OQ-002 resolved; OQ-004 and OQ-005 opened from the 2026-10-11 build log._

---

## Open Questions

### OQ-001 — Unused theme cleanup
**Status:** Resolved (2026-10-11, `cf168d1`)  
**Source:** `themes.yaml` inspection  
`design-methodology`, `ai-instructions`, and `research-protocols` had zero manifestos. `cf168d1` (`chore: drop themes with no manifestos`) removed them. `software-engineering` and `cognitive-science` remain.

### OQ-002 — Patch version on `first-principles.md`
**Status:** Resolved (2026-10-11, `12ba3f1`)  
**Source:** Manifesto inventory  
`12ba3f1` (`chore: set first-principles version to 1.0.0`) removed the patch segment. MAINTAINERS_GUIDE now forbids minor and patch versions; versions are `N.0.0`.

### OQ-003 — Theme fit for compression manifesto
**Status:** Resolved (2026-05-01)  
**Source:** Manifesto inventory; `themes.yaml`  
`only-fluff-die.md` replaced by `stop-yapping.md`. Theme stays `cognitive-science`. The `ai-instructions` theme was explicitly rejected: all manifestos in LLM_MANIFESTOS are AI instructions by definition, so the theme fails to differentiate within the collection. The compression manifesto addresses communication discipline — a cognitive framework — not tool configuration.

### OQ-004 — ETHOS.md names PostCompact
**Status:** Open (deferred to the owner)  
**Source:** Build log 2026-10-11, plugin track (B1)  
`/home/user/claude-skills/ETHOS.md` line 37 lists PostCompact among the one-time hooks. The manifesto plugin deleted PostCompact in `a390757` (plugin 3.3.0).  
**Action needed:** The owner edits the line in ETHOS.md.

### OQ-005 — Two manifesto-dir paths
**Status:** Open (deferred to the owner)  
**Source:** Build log 2026-10-11, plugin track (B1)  
The manifesto-oath skill names `.claude/manifesto-repo/LLM_MANIFESTOS/manifestos/` (project-relative). The hook text names `manifesto_dir` on its `Manifesto repo:` line.  
**Action needed:** The owner decides which path governs and aligns the other.

---

## Known Structural Debt

### SD-001 — No `archive/deprecated/` directory
**Status:** Not blocking  
MAINTAINERS_GUIDE documents an archival workflow that moves files to `archive/deprecated/`. The path does not exist. The `archive/` directory currently holds pre-collection source materials only.  
**Action needed:** Create `archive/deprecated/` when the first manifesto is archived. No action needed until then.

### SD-002 — README drift risk (no automated enforcement)
**Status:** Low risk, accepted  
`just readme` is a manual step. No hook or CI job prevents committing a manifesto without regenerating README. The MAINTAINERS_GUIDE notes this as a maintainer responsibility but does not enforce it mechanically.  
**Action needed:** Add a pre-commit hook or CI check if README drift becomes a recurring problem.

---

## Future Work (Not Yet Scoped)

- Consider a `just validate` command that runs `generate.py` in a dry-run mode (validate without writing) — useful for pre-commit hooks.
- Assess whether the `archive/design/`, `archive/dieter_rams/`, `archive/research/`, and `archive/software_building_principles/` materials are candidates for formal manifesto extraction.
