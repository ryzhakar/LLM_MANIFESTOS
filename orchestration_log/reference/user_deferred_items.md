# User Deferred Items

**Holds:** the owner's open deferrals, in the owner's words where spoken; derived items are marked as such.
**Does not hold:** rulings (`decisions.md`), structural limits (`capabilities.md`).
**Mutability:** entry added on deferral; entry deleted on resolution.

---

## Source typos in `cargo-cult-science.md` — fix or keep

Deferred 2026-08-10. Owner directive was "make this into a manifesto with absolute minimum changes to the content"; whether the Caltech transcription's own errors count as content is unruled. Kept verbatim meanwhile: "he" for "be" twice ("it would he just about as difficult", "it would he better in some other state"), "When I was at Cornell." with a period, "A‑Number‑l" with a lowercase L.

## Unused themes — populate, rename, or remove

Derived 2026-04-29 from `themes.yaml` inspection; no owner ruling yet. `design-methodology` and `research-protocols` have zero manifestos: forward declarations or stale artifacts? (`ai-instructions` was rejected for the compression manifesto — see `decisions.md` 2026-05-01 — but the key still exists.)

## `first-principles.md` patch version

Derived 2026-04-29; no owner ruling yet. The file sits at 1.0.1 against the no-patch-versions constraint. Amend to 1.0.0 or advance to 1.1.0 with justification. Low urgency.

## README drift enforcement

Derived 2026-04-29; accepted risk. Add a pre-commit hook or CI check running `just readme` only if drift becomes a recurring problem.

## Archive extraction candidates

Derived 2026-04-29; not yet scoped. Assess whether `archive/design/`, `archive/dieter_rams/`, `archive/research/`, and `archive/software_building_principles/` hold material for formal manifesto extraction.

## Digest eval under the instruction-eval plugin — run, adopt, adapt local extensions

Deferred 2026-10-16. Owner: "defer the digest run under new plugin and your adoption and adapting local extensions of it." Held: running a series of digests/only-what-it-needs.md through instruction-eval@my-claude-skills (0.1.0, main 91d2def), adopting the plugin here, and adapting the local .claude/skills and tools/digest-eval extensions to it. Needs the owner's /plugin install and reader /login. Derived: cut 1 of the old tool failed its gate; its cut 2 hypothesis is unapplied at evals/only-what-it-needs/cut-2/hypothesis.md.
