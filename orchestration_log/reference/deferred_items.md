# Deferred Items

_First session — 2026-04-29. Items below are derived from static analysis of the repository; no orchestration sessions have run yet._

---

## Open Questions

### OQ-001 — Unused theme cleanup
**Status:** Open  
**Source:** `themes.yaml` inspection  
Three themes are defined but have zero manifestos: `design-methodology`, `ai-instructions`, `research-protocols`. It is unclear whether these are forward declarations (new manifestos planned for these domains) or stale artifacts from an earlier schema.  
**Action needed:** Decide — populate, remove, or annotate as planned.

### OQ-002 — Patch version on `first-principles.md`
**Status:** Open  
**Source:** Manifesto inventory  
`first-principles.md` is at version `1.0.1`. MAINTAINERS_GUIDE explicitly states "Patches — don't use; just edit." This is the only manifesto using a patch segment.  
**Action needed:** Either amend the version to `1.0.0` (if the patch was a minor edit) or advance to `1.1.0` with justification. Low urgency.

### OQ-003 — Theme fit for `only-fluff-die.md`
**Status:** Open  
**Source:** Manifesto inventory; `themes.yaml`  
`only-fluff-die.md` is about compressing machine-generated language — it sits in `cognitive-science`. The unused `ai-instructions` theme might be a better fit. Alternatively, `only-fluff-die` may be the seed manifesto that justifies populating `ai-instructions`.  
**Action needed:** Deliberate when a second AI-instructions-class manifesto is being considered.

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

- Populate or formally retire the three unused themes.
- Consider a `just validate` command that runs `generate.py` in a dry-run mode (validate without writing) — useful for pre-commit hooks.
- Assess whether the `archive/design/`, `archive/dieter_rams/`, `archive/research/`, and `archive/software_building_principles/` materials are candidates for formal manifesto extraction.
