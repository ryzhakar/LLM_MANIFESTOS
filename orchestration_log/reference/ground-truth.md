# Ground Truth

**Holds:** task, success criterion, data, protocol, fixed constraints.
**Does not hold:** working rules (`conventions.md`), inventory and surface (`capabilities.md`), rulings (`decisions.md`), open owner items (`user_deferred_items.md`).
**Mutability:** changes only on owner override.

---

## Task

Curate LLM_MANIFESTOS: a collection of behavioral constitutions — timeless, actionable principles that bind LLM agent behavior. The maintainer is a curator-archivist, not an editor-writer. Full charter: `MAINTAINERS_GUIDE.md`.

## Success criterion

`just readme` exits green: every file in `manifestos/` passes frontmatter validation and `README.md` is regenerated. A manifesto ships only when schema-valid, theme-assigned, and README-synced.

## Data

- `manifestos/*.md` — the collection; frontmatter is the metadata source of truth
- `themes.yaml`, `config.yaml`, `README.template.md` — display configuration and template
- `archive/` — pre-collection source materials; never scanned by the pipeline
- `instructions/` — writing methodology loaded as technique guidance for writer agents
- `research/` — gitignored working area for source-material research

## Protocol

- Session memory: ARRIVE / WORK / LEAVE per the `agentic-delegation` skill; close via `session-close`.
- Manifesto lifecycle (add, update, version, archive): workflows in `MAINTAINERS_GUIDE.md`.

## Fixed constraints

- Manifestos are precious artifacts, not living documentation. High bar for entry; adding one is a significant event; frequent small edits signal an uncrystallized principle.
- `README.md` is generated, never hand-edited.
- Each manifesto has exactly one theme; a theme exists only when 2+ manifestos use it.
- Versions move only on major thesis change (`x.0.0 → x+1.0.0`). Ordinary edits don't bump versions; patch versions are never used.
