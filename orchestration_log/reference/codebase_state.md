# Codebase State

_Last verified: 2026-10-11. Generation pipeline confirmed working: `just readme` produced 12 manifestos cleanly (exit 0, no panel); `tests/test_generate.py` passes 18 of 18._

---

## Manifesto Inventory

| File | Title | Tagline | Theme | Version | Kind | Register | Reader |
|------|-------|---------|-------|---------|------|----------|--------|
| `cargo-cult-science.md` | Cargo Cult Science | "the first principle is that you must not fool yourself" | cognitive-science | 1.0.0 | canon | lecture | unspecified |
| `correct-by-construction.md` | Correct By Construction | "invalid states cannot compile" | software-engineering | 1.0.0 | manifesto | declarative | human |
| `dry.md` | Knowledge Has One Home | "knowledge has one home" | software-engineering | 1.0.0 | manifesto | declarative | human |
| `first-principles.md` | The First Principles | "atoms, not analogies" | cognitive-science | 1.0.0 | manifesto | parable | unspecified |
| `intervention.md` | Trust Nothing, Restore Everything | "roots, not canopy" | cognitive-science | 1.0.0 | manifesto | parable | unspecified |
| `kiss.md` | Decomplect | "incidental is Latin for your fault" | software-engineering | 2.0.0 | manifesto | declarative | human |
| `postgres.md` | Respect the Engine | "you use 5% of what you bought." | software-engineering | 1.0.0 | manifesto | contemptuous | human |
| `self-documenting-code.md` | Code Speaks | "comments are lies" | software-engineering | 1.0.0 | manifesto | lecture | human |
| `simple-made-easy.md` | The Simplicity Manifesto | "the confusion is killing you" | cognitive-science | 2.0.0 | manifesto | lecture | human |
| `stop-yapping.md` | Stop Yapping | "answer. shut up." | cognitive-science | 1.0.0 | manifesto | contemptuous | model |
| `yagni.md` | Build For Today | "build for today" | software-engineering | 1.0.0 | manifesto | declarative | human |
| `zen-of-python.md` | The Zen of Python | "refuse to guess" | software-engineering | 1.0.0 | canon | aphoristic | unspecified |

**Total:** 12 files. 10 `manifesto`, 2 `canon` (`cargo-cult-science.md`, `zen-of-python.md`). 7 software-engineering, 5 cognitive-science.

---

## Themes

Defined in `themes.yaml`. Two themes exist; both are in use. `design-methodology`, `ai-instructions`, and `research-protocols` were removed in `cf168d1`.

| Key | Icon | Name | In Use |
|-----|------|------|--------|
| `software-engineering` | 🔧 | Software Engineering Principles | Yes (7 files) |
| `cognitive-science` | 🧠 | Cognitive Science | Yes (5 files) |

---

## Generation Pipeline

Source: `generate.py` (182 lines). Command: `just readme`.

### Exact command

```
uv run --with pyyaml --with python-frontmatter --with pydantic --with jinja2 --with rich generate.py
```

Dependencies are injected inline via `uv run --with`; no separate virtualenv or requirements file exists.

### Steps (in order, from `generate.py`)

1. **Load config** — reads `config.yaml` and `themes.yaml` via `yaml.safe_load`
2. **Scan** — globs `manifestos/*.md` with `sorted()`, so files are processed alphabetically by filename
3. **Parse** — each file is loaded with `frontmatter.load()` (python-frontmatter library)
4. **Validate** — frontmatter dict is passed to `ManifestoMetadata(**post.metadata)` (Pydantic model)
   - Required fields: `title`, `tagline`, `version`, `theme`, `description` (all `str`)
   - Optional fields: `kind` (`manifesto` default | `canon`), `register` (`contemptuous` | `declarative` | `parable` | `lecture` | `aphoristic`), `reader` (`model` | `human` | `unspecified`)
   - `version` must match regex `^\d+\.\d+\.\d+$`; enforced by `@field_validator('version')`
   - `tagline` must hold at most 8 words unless `kind` is `canon`; enforced by `@model_validator(mode='after')`
   - Invalid files are collected into an `errors` list and skipped (graceful degradation — pipeline continues)
5. **Warn** — theme panel if frontmatter themes are not in `themes.yaml`; duplicate-tagline panel (`tagline_warnings`) naming each file
6. **Exit early** — if `manifestos` list is empty after filtering, exits with code 1
7. **Render** — passes `{'project': config, 'manifestos': manifestos, 'themes': themes}` to `jinja2.Template` loaded from `README.template.md`
8. **Write** — writes rendered output to `README.md`, appending a trailing newline

### Template behavior (`README.template.md`)

- Quick Reference table: all manifestos sorted by `title`, with Theme, Version, Register, and Reader columns; `kind: canon` files carry a `canon` badge
- Theme sections: themes sorted by their key string; each section lists manifestos sorted by `title`; each entry heading reads `version · register · reader`
- Only themes that appear in at least one manifesto's frontmatter are rendered; unused themes in `themes.yaml` are silently omitted
- Theme display falls back to `{'icon': '📄', 'name': theme_key, 'description': ''}` if the theme key is missing from `themes.yaml`

### What is tracked vs. ignored

- `orchestration_log/history/*/cost.md` — gitignored
- `research/` directory — gitignored
- `*.DS_Store` — gitignored
- `drafts/` — not scanned by `generate.py`; at ship, `SPEC.md` and `reviews/` move to `orchestration_log/history/<date>/<slug>/` and the draft versions are deleted
- `orchestration_log/history/<date>/recut-<slug>.md` — re-cut records for re-cuts without a draft
- `resources/` — tracked; not scanned by `generate.py`
- `archive/` — exists but NOT scanned by `generate.py`; contents do not appear in README
- `README.md` — generated artifact; tracked in git (committed after each `just readme` run)

### Archive directory

`archive/` contains four subdirectories: `design/`, `dieter_rams/`, `research/`, `software_building_principles/`. These are pre-collection source materials, not deprecated manifestos. No `archive/deprecated/` path exists yet (described in MAINTAINERS_GUIDE; created on first archival).

---

## Known Limitations

- **No `archive/deprecated/` path exists.** MAINTAINERS_GUIDE describes an archival workflow using `archive/deprecated/`, but the directory does not exist. First archival action will need to create it.
- **`generate.py` accepts any `x.y.z` version.** MAINTAINERS_GUIDE forbids minor and patch segments; the generator does not enforce it. All 12 files hold `N.0.0`.
- **Attribution gaps.** MAINTAINERS_GUIDE makes the attribution line mandatory. `intervention.md`, `postgres.md`, `self-documenting-code.md`, and `zen-of-python.md` carry none. `cargo-cult-science.md` carries `*by RICHARD P. FEYNMAN*` without a year.
- **`reader` below the standard.** Only `stop-yapping.md` declares `reader: model`; 7 files declare `human` and 4 declare `unspecified`.
- **No CI/CD gate.** `just readme` is a manual step. Nothing prevents committing a manifesto without regenerating README, creating drift. The MAINTAINERS_GUIDE calls this out as a responsibility but does not enforce it mechanically.
- **`stop-yapping.md` replaced `only-fluff-die.md`** (2026-05-01). Same function (language compression), completely different manifesto — abusive register, model-addressed, no security escape hatch. Theme: cognitive-science.
- **`postgres.md` added (2026-05-11).** Application Postgres manifesto — abusive register, 269 lines, 5337 words. Covers 5 paradigm shifts (schema-as-architecture, set-thinking, planner collaboration, physical cost model, constraints-as-law) plus "use what ships." Three full rewrites, 5 content reviewers, 29 technical fixes. Source: user-prepared substrate. Theme: software-engineering.
- **`kiss.md` and `simple-made-easy.md` are both at version 2.0.0.** Both were refactored recently (commits `5994364` and `7c6467a`). Their current thesis boundaries may still be settling.

---

## Next Actions

These are observations, not commitments. An orchestrator or maintainer should evaluate each.

- Add a CI step (e.g., a pre-commit hook or GitHub Action) that runs `just readme` and fails if `README.md` has uncommitted changes.
- Add the missing attribution lines and the missing year (see Known Limitations). Each edit touches a manifesto body.
- Decide whether to migrate `reader` values on pre-standard manifestos through re-cuts.
