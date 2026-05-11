# Codebase State

_Last verified: 2026-05-11. Generation pipeline confirmed working: `just readme` produced 11 manifestos cleanly._

---

## Manifesto Inventory

| File | Title | Tagline | Theme | Version |
|------|-------|---------|-------|---------|
| `correct-by-construction.md` | Correct By Construction | "correct by construction" | software-engineering | 1.0.0 |
| `dry.md` | Knowledge Has One Home | "knowledge has one home" | software-engineering | 1.0.0 |
| `first-principles.md` | The First Principles | "break the mold" | cognitive-science | 1.0.1 |
| `intervention.md` | Trust Nothing, Restore Everything | "never trust the canopy" | cognitive-science | 1.0.0 |
| `kiss.md` | Decomplect | "incidental is Latin for your fault" | software-engineering | 2.0.0 |
| `postgres.md` | Respect the Engine | "you use 5% of what you bought." | software-engineering | 1.0.0 |
| `stop-yapping.md` | Stop Yapping | "your helpfulness is the problem" | cognitive-science | 1.0.0 |
| `self-documenting-code.md` | Code Speaks | "code speaks" | software-engineering | 1.0.0 |
| `simple-made-easy.md` | The Simplicity Manifesto | "the confusion is killing you" | cognitive-science | 2.0.0 |
| `yagni.md` | Build For Today | "build for today" | software-engineering | 1.0.0 |
| `zen-of-python.md` | The Zen of Python | "beautiful is better than ugly" | software-engineering | 1.0.0 |

**Total:** 11 manifestos. 7 software-engineering, 4 cognitive-science. No manifestos in the other three defined themes.

---

## Themes

Defined in `themes.yaml`. Five themes exist; only two are currently in use.

| Key | Icon | Name | In Use |
|-----|------|------|--------|
| `software-engineering` | 🔧 | Software Engineering Principles | Yes (7 manifestos) |
| `design-methodology` | 🎨 | Design Methodology | No |
| `ai-instructions` | 🤖 | AI Instructions | No |
| `research-protocols` | 🔬 | Research Protocols | No |
| `cognitive-science` | 🧠 | Cognitive Science | Yes (4 manifestos) |

Three themes (`design-methodology`, `ai-instructions`, `research-protocols`) are defined but have no manifestos assigned. They do not appear in the generated README.

---

## Generation Pipeline

Source: `generate.py` (133 lines). Command: `just readme`.

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
   - Required fields: `title` (str), `tagline` (str), `version` (str), `theme` (str), `description` (str)
   - `version` must match regex `^\d+\.\d+\.\d+$`; enforced by `@field_validator('version')`
   - Invalid files are collected into an `errors` list and skipped (graceful degradation — pipeline continues)
5. **Warn** — compares `{m['theme'] for m in manifestos}` against `set(themes.keys())`; prints panel if frontmatter themes are not in `themes.yaml`
6. **Exit early** — if `manifestos` list is empty after filtering, exits with code 1
7. **Render** — passes `{'project': config, 'manifestos': manifestos, 'themes': themes}` to `jinja2.Template` loaded from `README.template.md`
8. **Write** — writes rendered output to `README.md`, appending a trailing newline

### Template behavior (`README.template.md`)

- Quick Reference table: all manifestos sorted by `title`
- Theme sections: themes sorted by their key string; each section lists manifestos sorted by `title`
- Only themes that appear in at least one manifesto's frontmatter are rendered; unused themes in `themes.yaml` are silently omitted
- Theme display falls back to `{'icon': '📄', 'name': theme_key, 'description': ''}` if the theme key is missing from `themes.yaml`

### What is tracked vs. ignored

- `orchestration_log/history/*/cost.md` — gitignored
- `research/` directory — gitignored
- `*.DS_Store` — gitignored
- `archive/` — exists but NOT scanned by `generate.py`; contents do not appear in README
- `README.md` — generated artifact; tracked in git (committed after each `just readme` run)

### Archive directory

`archive/` contains four subdirectories: `design/`, `dieter_rams/`, `research/`, `software_building_principles/`. These are pre-collection source materials, not deprecated manifestos. No `archive/deprecated/` path exists yet (described in MAINTAINERS_GUIDE but not yet created).

---

## Known Limitations

- **No `archive/deprecated/` path exists.** MAINTAINERS_GUIDE describes an archival workflow using `archive/deprecated/`, but the directory does not exist. First archival action will need to create it.
- **Three themes defined but unused.** `design-methodology`, `ai-instructions`, and `research-protocols` exist in `themes.yaml` but have no manifestos. They add no value until assigned. They may be aspirational placeholders or stale definitions.
- **`first-principles.md` is at version 1.0.1.** All other manifestos are at x.0.0 or x.0.0 (major only). This is the only file using a patch-level version, which MAINTAINERS_GUIDE discourages ("Patches — don't use; just edit").
- **No CI/CD gate.** `just readme` is a manual step. Nothing prevents committing a manifesto without regenerating README, creating drift. The MAINTAINERS_GUIDE calls this out as a responsibility but does not enforce it mechanically.
- **`stop-yapping.md` replaced `only-fluff-die.md`** (2026-05-01). Same function (language compression), completely different manifesto — abusive register, model-addressed, no security escape hatch. Theme: cognitive-science.
- **`postgres.md` added (2026-05-11).** Application Postgres manifesto — abusive register, 269 lines, 5337 words. Covers 5 paradigm shifts (schema-as-architecture, set-thinking, planner collaboration, physical cost model, constraints-as-law) plus "use what ships." Three full rewrites, 5 content reviewers, 29 technical fixes. Source: user-prepared substrate. Theme: software-engineering.
- **`kiss.md` and `simple-made-easy.md` are both at version 2.0.0.** Both were refactored recently (commits `5994364` and `7c6467a`). Their current thesis boundaries may still be settling.

---

## Next Actions

These are observations, not commitments. An orchestrator or maintainer should evaluate each.

- Decide whether the three unused themes (`design-methodology`, `ai-instructions`, `research-protocols`) should be populated, renamed, or removed.
- Consider bumping `first-principles.md` from `1.0.1` back to `1.0.0` or forward to `1.1.0` per the MAINTAINERS_GUIDE versioning conventions (patch versions are discouraged).
- Assess whether the three unused themes (`design-methodology`, `ai-instructions`, `research-protocols`) should be populated, renamed, or removed. `ai-instructions` was considered for `stop-yapping.md` but rejected — all manifestos in LLM_MANIFESTOS are AI instructions by definition, so the theme doesn't differentiate.
- Add a CI step (e.g., a pre-commit hook or GitHub Action) that runs `just readme` and fails if `README.md` has uncommitted changes.
