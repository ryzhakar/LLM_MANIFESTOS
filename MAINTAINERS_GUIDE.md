# Maintainers Guide

> *Manifestos are precious artifacts, not documentation.*

## Philosophy

### What Manifestos Are

Manifestos are **behavioral constitutions**: timeless principles that define how systems operate. They are philosophical frameworks distilled into actionable principles, boundary conditions for acceptable behavior, and standards against which decisions are measured.

Manifestos are NOT implementation guides, technical specifications, temporary notes, or living documents that change frequently.

### Species

The **writing standard** is the `manifesto:manifesto-writing` skill. It governs substrate reading, drafting, review, and shipping of every `kind: manifesto` file. This guide repeats none of it.

The frontmatter field `kind` sets the species of each file in `manifestos/`.

| | `kind: manifesto` (default) | `kind: canon` |
|---|---|---|
| Content | Source material transformed under the writing standard | One text kept verbatim for extraction |
| Form rules | The writing standard governs | Exempt, tagline length included |
| Entry bar | The entry gate | Never counted against the entry bar |
| Attribution line | `*After [authors]*` | `*by [author], [year]*` |

Attribution is mandatory for both species.

### The Curator's Responsibility

You are a **curator-archivist**, not an editor-writer.

- **Evaluate** what deserves manifesto status: run the entry gate.
- **Preserve** provenance through metadata: frontmatter is the artifact record.
- **Organize** for discovery: themes, descriptions, navigation.
- **Protect** integrity through validation: the schema is the quality gate.

---

## Architecture

### The Single Source of Truth

```
manifestos/*.md
    ↓
frontmatter (authoritative metadata)
    ↓
generate.py (validation → transformation)
    ↓
README.md (derived navigation artifact)
```

Frontmatter is the source of truth for metadata. NEVER edit `README.md` by hand; `just readme` regenerates it.

### Design

- Metadata lives in frontmatter. No separate index exists.
- A Pydantic schema validates every file. A file that fails is skipped and reported in an error panel.
- `README.md` renders from `README.template.md`.
- Each manifesto carries exactly one theme. Theme display metadata lives in `themes.yaml`.
- `generate.py` scans `manifestos/*.md` only. `drafts/`, `resources/`, `archive/`, and `research/` stay out of the README.

---

## Maintainer Roles

### 1. Curator (What enters the collection?)

- Run the entry gate. Admit a candidate only when the artifact of every stage exists.
- Decide per change: edit, re-cut, or version.
- Reject implementation details, temporary best practices, project-specific rules, and unproven theories.

### 2. Navigator (How do users find manifestos?)

- Write each description as one sentence that answers "Why should I read this?" for a reader five years out.
- Keep every tagline within the schema limit (see *Frontmatter Schema*) and clear every duplicate-tagline warning.
- Choose themes by fundamental domain, not current trends.

### 3. Validator (Is the collection intact?)

- Run `just readme` before every commit.
- Fix schema violations at once.
- Match `themes.yaml` to theme usage.
- Run `tests/test_generate.py` after any change to `generate.py`.

**Red flags:** validation errors, theme warnings, duplicate-tagline warnings, manual README edits.

---

## Workflows

### The Entry Gate

**When:** A candidate principle asks to join `manifestos/` as `kind: manifesto`.

Run the stages in order. Start a stage only after the previous stage's artifact exists on disk. Stop at the first failed stage.

| # | Stage | Artifact |
|---|-------|----------|
| 1 | Substrate: 2–11 primary texts, saved verbatim, with an index | `resources/<date>-<slug>/` |
| 2 | Discovery tree | `orchestration_log/history/<date>/discovery-research/` |
| 3 | Gate test, then spec | `drafts/<slug>/SPEC.md` |
| 4 | Draft by a writer bound to the writing standard and a register reference | `drafts/<slug>/v1.md` |
| 5 | Review: five unbiased reviewers, a register reviewer, a maximalist self-pass | `drafts/<slug>/reviews/`, `drafts/<slug>/v2.md` |
| 6 | Ship | `manifestos/<slug>.md` |

**Stage 2** holds four artifacts:
1. Ground-truth audits of the collection.
2. Surveys by focus, never by source.
3. Verification of every axiom against the texts, with a rating per axiom.
4. A candidates report.

**Stage 3.** Write the spec only for a candidate that meets all three tests:
1. One axiom the verification rated VERIFIED, stated by at least two authors.
2. One precise enemy.
3. Ground the collection does not hold, or can re-cut by named rows (see *Re-cutting an existing manifesto*).

State the axiom with its authors, the enemy, and the ground in `SPEC.md`.

**Stage 5.** Save each revision at the next fresh path, `v<N>.md`. Store reviewer output in `reviews/`. The writing standard defines the reviewers' lenses and rules.

**Stage 6.**
1. Move the final version to `manifestos/<slug>.md`. A draft enters the collection only by moving there.
2. Complete the frontmatter as the writing standard states.
3. If the theme is new, add it first (see *Adding a New Theme*).
4. Run `just readme`. Require exit 0 and no warning panel.
5. Commit: `git add manifestos/ themes.yaml README.md`, then `git commit -m "feat: add <slug> manifesto"`.

**Orchestrators:** Check that the artifact path exists before dispatching the next stage.

**Worked example (2026-10-11):**

```
resources/2026-10-11-code-liability-and-dependencies/
├── README.md        index of every fetched file
├── index/           source tables
├── primary/         the 11 primary texts (L1-01…L1-06, L2-01…L2-05), plus supplementary copies
└── secondary/
orchestration_log/history/2026-10-11/discovery-research/
├── INDEX.md         origin path and sha256 of every file
├── deep-dives/      audits: corpus, collection overlap, doctrine, runtime
├── discovery/       surveys: enemies, tensions, distinctions-vocabulary, demands, collection-fit
│                    verify-axioms.md, candidates.md
└── briefs/  prompts/  resolutions/
```

---

### Updating a Manifesto

**When:** Fixing typos, improving clarity, adding examples: changes that keep the thesis.

1. Edit the file (content and/or frontmatter). The version stays.
2. Run `just readme`.
3. Commit: `git add manifestos/ README.md`, then `git commit -m "docs: improve clarity in <slug>"`.

---

### Re-cutting an existing manifesto

**When:** The resulting stack is sharper. The contents of existing manifestos are malleable.

A **row** is one claim a manifesto holds, cited as `file:line`.

1. Name every row that moves as `file:line`, with its destination.
2. State the held ground of each affected manifesto after the move.
3. Record both in the `SPEC.md` of the draft that causes the re-cut.
4. Apply the version rule:

| Re-cut | Version |
|---|---|
| Removes a row from a manifesto's enemy section | Raise that manifesto's major version |
| Moves other rows | Unchanged |

5. Run `just readme`, then commit.

Re-cut `kind: manifesto` files only; canon stays verbatim.

---

### Versioning a Manifesto (Major Evolution)

**When:** The core thesis changes (paradigm shift, major expansion, fundamental reframing), or a re-cut removes an enemy-section row.

Versions are `N.0.0`. Raise `N` and nothing else.

| Change | Version |
|---|---|
| Thesis change | `1.0.0 → 2.0.0` |
| Re-cut that removes an enemy-section row | `1.0.0 → 2.0.0` |
| Any other edit | Unchanged |
| Minor or patch segment (`1.1.0`, `1.0.1`) | Forbidden |

`generate.py` accepts any `x.y.z`; the major-only rule belongs to the maintainer.

**Steps:**
1. Set `version: "2.0.0"` and update the content to the new thesis.
2. Optionally preserve the old text: `git mv "manifestos/<slug>.md" "archive/<slug>-v1.0.0.md"`, then create the new `manifestos/<slug>.md`.
3. Run `just readme`, then `git add manifestos/ archive/ README.md` and `git commit -m "feat: version <slug> to 2.0.0"`.

---

### Adding a New Theme

**When:** At least two manifestos in a new domain warrant their own grouping.

1. Add the key to `themes.yaml`:
   ```yaml
   quantum-mechanics:
     icon: "⚛️"
     name: "Quantum Mechanics Principles"
     description: "Principles for quantum system design"
   ```
2. Set `theme: "quantum-mechanics"` in each manifesto's frontmatter.
3. Run `just readme`; the theme section appears automatically.
4. Commit: `git add themes.yaml manifestos/ README.md`, then `git commit -m "feat: add quantum-mechanics theme"`.

**Theme rules:**
- Each theme holds at least two files.
- A theme separates files within the collection. Rejected: `ai-instructions`.
- Theme keys are kebab-case (`software-engineering`).
- The description names what unifies the theme.

---

### Archiving a Manifesto

**When:** A manifesto is superseded, deprecated, or no longer relevant.

1. Create `archive/deprecated/` on first use, then move the file: `git mv "manifestos/<slug>.md" "archive/deprecated/<slug>.md"`.
2. Run `just readme`. The manifesto leaves the README.
3. Commit: `git add manifestos/ archive/ README.md`, then `git commit -m "chore: archive deprecated <slug>"`.

`generate.py` never scans `archive/`.

---

## Troubleshooting

An error skips its file; the run continues with the rest. A warning keeps the file.

| Output | Fix |
|---|---|
| `❌ Schema Validation` … `title` … `Field required` | Add the field to the frontmatter. |
| `Version must be semver (e.g., 1.0.0), got: 1.0` | Write `version: "1.0.0"`, not `"1.0"` or `"v1.0.0"`. |
| `Tagline must be at most 8 words, got 9: …` | Cut the tagline to 8 words or fewer. `kind: canon` is exempt. |
| `Input should be 'manifesto' or 'canon'` (also `register`, `reader`) | Use a listed value (see *Frontmatter Schema*). |
| `⚠️ Theme Discrepancy`: theme not in `themes.yaml` | Add the theme to `themes.yaml`, or use an existing theme. The file renders without icon or name until then. |
| `⚠️ Duplicate Tagline`: `"…" appears in: a.md, b.md` | Rewrite one tagline. The check ignores case and punctuation. |
| `manifestos/ directory not found` | Run from the repository root. |
| README not updating | Run `just readme`; confirm the green checkmark; commit `README.md`. |

---

## Reference

### Frontmatter Schema

| Field | Required | Rule | On failure |
|---|---|---|---|
| `title` | yes | any string | file skipped |
| `tagline` | yes | any string; at most 8 words unless `kind: canon` | file skipped |
| `version` | yes | matches `^\d+\.\d+\.\d+$`; write `N.0.0` | file skipped |
| `theme` | yes | any string; key in `themes.yaml` | warning |
| `description` | yes | any string; one line | file skipped |
| `kind` | no | `manifesto` (default) or `canon` | file skipped |
| `register` | no | `contemptuous`, `declarative`, `parable`, `lecture`, or `aphoristic` | file skipped |
| `reader` | no | `model`, `human`, or `unspecified` | file skipped |
| any other key | n/a | ignored | none |

`register` and `reader` are frontmatter facts. The writing standard chooses their values.

Two files with the same tagline (lowercase, punctuation ignored) trigger a warning that names both.

---

### File Structure

```
manifestos/                    # scanned; <slug>.md, kebab-case, no spaces, no prefix
drafts/<slug>/                 # not scanned: SPEC.md, v1.md, v2.md, reviews/
resources/<date>-<slug>/       # substrate, verbatim; not scanned
orchestration_log/             # history/<date>/, reference/
archive/                       # not scanned
research/                      # gitignored working area
tests/test_generate.py         # schema tests
config.yaml                    # project metadata
themes.yaml                    # theme display config
README.template.md             # Jinja2 template
generate.py                    # validation + generation
justfile                       # task commands
README.md                      # generated (DO NOT EDIT)
```

---

### Generation Pipeline

1. **Scan:** `manifestos/*.md`
2. **Parse:** extract frontmatter with `python-frontmatter`
3. **Validate:** Pydantic schema check
4. **Warn:** theme discrepancies, duplicate taglines
5. **Render:** Jinja2 template with data
6. **Write:** `README.md`

The run exits 1 when no file validates.

**Dependencies:** `pyyaml` (YAML parsing), `python-frontmatter` (frontmatter extraction), `pydantic` (schema validation), `jinja2` (template rendering), `rich` (terminal feedback).

**Commands:**
```bash
just readme  # uv run --with <deps> generate.py
uv run --with pytest --with pyyaml --with python-frontmatter --with pydantic --with jinja2 --with rich python tests/test_generate.py
```
