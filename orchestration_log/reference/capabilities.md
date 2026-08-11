# Capabilities

**Holds:** inventory, system surface, vocabulary, limits, dated measured facts.
**Does not hold:** working rules (`conventions.md`), fixed constraints (`ground-truth.md`), rulings (`decisions.md`).
**Mutability:** updated in the turn a merge or capability change lands.

---

## Inventory (measured 2026-08-10)

12 manifestos: 7 software-engineering, 5 cognitive-science.

| File | Title | Tagline | Theme | Version |
|------|-------|---------|-------|---------|
| `cargo-cult-science.md` | Cargo Cult Science | "the first principle is that you must not fool yourself" | cognitive-science | 1.0.0 |
| `correct-by-construction.md` | Correct By Construction | "invalid states cannot compile" | software-engineering | 1.0.0 |
| `dry.md` | Knowledge Has One Home | "knowledge has one home" | software-engineering | 1.0.0 |
| `first-principles.md` | The First Principles | "atoms, not analogies" | cognitive-science | 1.0.1 |
| `intervention.md` | Trust Nothing, Restore Everything | "roots, not canopy" | cognitive-science | 1.0.0 |
| `kiss.md` | Decomplect | "incidental is Latin for your fault" | software-engineering | 2.0.0 |
| `postgres.md` | Respect the Engine | "you use 5% of what you bought." | software-engineering | 1.0.0 |
| `self-documenting-code.md` | Code Speaks | "comments are lies" | software-engineering | 1.0.0 |
| `simple-made-easy.md` | The Simplicity Manifesto | "the confusion is killing you" | cognitive-science | 2.0.0 |
| `stop-yapping.md` | Stop Yapping | "answer. shut up." | cognitive-science | 1.0.0 |
| `yagni.md` | Build For Today | "build for today" | software-engineering | 1.0.0 |
| `zen-of-python.md` | The Zen of Python | "refuse to guess" | software-engineering | 1.0.0 |

## Themes (measured 2026-08-10)

Defined in `themes.yaml`. Five defined, two in use.

| Key | Icon | Name | In use |
|-----|------|------|--------|
| `software-engineering` | 🔧 | Software Engineering Principles | yes (7) |
| `cognitive-science` | 🧠 | Cognitive Science | yes (5) |
| `design-methodology` | 🎨 | Design Methodology | no |
| `ai-instructions` | 🤖 | AI Instructions | no |
| `research-protocols` | 🔬 | Research Protocols | no |

Unused themes do not render in the generated README. Their fate is an open owner item (`user_deferred_items.md`).

## Generation pipeline

Command: `just readme` → `uv run --with pyyaml --with python-frontmatter --with pydantic --with jinja2 --with rich generate.py`. Dependencies are injected inline; no virtualenv or requirements file exists.

Behavior (verified 2026-08-10 against `generate.py`):

- Scans `manifestos/*.md` alphabetically, parses frontmatter, validates each against the Pydantic `ManifestoMetadata` model.
- Invalid files are skipped with an error panel; the pipeline continues with the rest. Empty result exits 1.
- Frontmatter themes missing from `themes.yaml` print a warning panel but still render, falling back to a bare 📄 icon and the raw key.
- Renders `README.template.md` (Jinja2) into `README.md`. Quick Reference sorts by title; theme sections sort by theme key; themes with no manifestos are omitted.

## Frontmatter vocabulary

Required fields, all strings: `title`, `tagline`, `version`, `theme`, `description`. `version` must match `^\d+\.\d+\.\d+$`. Extra fields are silently ignored (no `extra='forbid'` on the model). Authority: `ManifestoMetadata` in `generate.py`.

## Tracked vs ignored

- Gitignored: `orchestration_log/recon/`, `orchestration_log/history/*/cost.md`, `research/`, `.DS_Store`.
- `archive/` — tracked, never scanned. Four subdirectories of pre-collection source materials: `design/`, `dieter_rams/`, `research/`, `software_building_principles/`.
- `README.md` — generated artifact, tracked, committed after each `just readme` run.

## Limits (as of 2026-08-10)

- No `archive/deprecated/` path exists; the archival workflow in `MAINTAINERS_GUIDE.md` will create it on first use.
- No CI or pre-commit gate runs `just readme`; README sync is manual discipline.
- `first-principles.md` sits at 1.0.1, the collection's only patch version — open owner item (`user_deferred_items.md`).
