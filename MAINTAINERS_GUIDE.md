# Maintainers Guide

> *Manifestos are precious artifacts, not documentation.*

## Philosophy

### What Manifestos Are

Manifestos are **behavioral constitutions**—timeless principles that define how systems should operate. They are:

- Philosophical frameworks distilled into actionable principles
- Boundary conditions for acceptable behavior
- Artifacts that preserve hard-won insights
- Standards against which decisions are measured

They are **NOT**:
- Implementation guides (those belong in docs/)
- Technical specifications (those belong in requirements/)
- Temporary notes (those belong in scratch/)
- Living documents that change frequently

### The Curator's Responsibility

As a maintainer, you are a **curator-archivist**, not an editor-writer. Your role mirrors museum stewardship:

- **Evaluate** what deserves manifesto status (high bar for entry)
- **Preserve** provenance through metadata (frontmatter as artifact record)
- **Organize** for discovery (themes, descriptions, navigation)
- **Protect** integrity through validation (schema as quality gate)

Adding a manifesto is a significant event. Manifestos are rare and precious.

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

**Critical principle:** Frontmatter is the source of truth for metadata. The README is always generated, never manually edited.

### Why This Design

**Frontmatter over separate index:**
- Eliminates knowledge duplication (DRY manifesto)
- Prevents drift (metadata lives with content)
- Single edit point (change once, propagates everywhere)

**Validation gate:**
- Pydantic schema catches malformed metadata before it corrupts the collection
- Rich terminal feedback makes errors actionable
- Invalid manifestos cannot enter the collection

**Generated README:**
- Navigation is always current (no manual sync burden)
- Presentation consistency (template enforces structure)
- Zero maintenance overhead (automation serves curation)

**Theme organization:**
- Themes are editorial groupings, not rigid taxonomy
- Each manifesto has exactly one theme (forces clarity)
- Theme metadata lives in `themes.yaml` (separate concern)

---

## Maintainer Roles

### 1. Curator (What enters the collection?)

**Responsibilities:**
- Evaluate whether a principle deserves manifesto status
- Ensure new manifestos meet quality bar
- Decide when to version vs. when to edit

**Questions to ask:**
- Is this principle timeless or temporary?
- Does it define behavior or describe implementation?
- Is it actionable or merely aspirational?
- Will this still matter in 5 years?

### 2. Navigator (How do users find manifestos?)

**Responsibilities:**
- Write clear, compelling descriptions (one sentence that conveys essence)
- Choose appropriate themes (software-engineering, design-methodology, etc.)
- Ensure taglines capture the manifesto's core insight

**Quality criteria:**
- Description answers: "Why should I read this?"
- Theme groups related principles coherently
- Tagline is memorable and distinctive

### 3. Validator (Is the collection intact?)

**Responsibilities:**
- Run `just readme` before committing (validation gate)
- Fix schema violations immediately (no invalid manifestos)
- Address theme discrepancies (themes.yaml should match usage)

**Red flags:**
- Validation errors (schema violation)
- Theme warnings (frontmatter theme not in themes.yaml)
- Manual README edits (breaks automation)

---

## Workflows

### Adding a New Manifesto

**When:** A new behavioral principle has crystallized and deserves preservation.

**Steps:**

1. **Create the file:**
   ```bash
   touch "manifestos/Manifesto, <principle> - \"<tagline>\".md"
   ```

2. **Add frontmatter:**
   ```yaml
   ---
   title: "The Principle Name"
   tagline: "memorable hook"
   version: "1.0.0"
   theme: "software-engineering"
   description: "One sentence explaining why this matters."
   ---
   ```

3. **Write the manifesto content** (the actual principle, evidence, practice)

4. **If using a new theme:**
   ```bash
   # Edit themes.yaml first
   new-theme:
     icon: "📐"
     name: "New Theme Display Name"
     description: "What this theme encompasses"
   ```

5. **Validate and generate:**
   ```bash
   just readme
   ```

   - ✓ **Success:** Green checkmark, theme breakdown
   - ❌ **Errors:** Fix frontmatter, re-run

6. **Commit:**
   ```bash
   git add manifestos/ themes.yaml README.md
   git commit -m "feat: add <principle> manifesto"
   ```

**Common mistakes:**
- Forgetting version field (schema violation)
- Using theme not in themes.yaml (warning)
- Invalid semver format (validation error)

---

### Updating a Manifesto

**When:** Fixing typos, improving clarity, adding examples—changes that don't alter core thesis.

**Steps:**

1. **Edit the manifesto file** (content and/or frontmatter)

2. **If metadata changed** (title, description, theme):
   - Update frontmatter
   - Version stays the same (minor edits don't version)

3. **Regenerate README:**
   ```bash
   just readme
   ```

4. **Commit:**
   ```bash
   git add manifestos/ README.md
   git commit -m "docs: improve clarity in <manifesto>"
   ```

**Do NOT version for:**
- Typo fixes
- Wording improvements
- Formatting changes
- Example additions that don't change thesis

---

### Versioning a Manifesto (Major Evolution)

**When:** The manifesto's core thesis has fundamentally changed. This is rare.

**Examples of version-worthy changes:**
- Paradigm shift (new evidence disproves original premise)
- Major expansion (principle now covers broader domain)
- Fundamental reframing (different lens on same problem)

**Steps:**

1. **Update version in frontmatter:**
   ```yaml
   version: "2.0.0"  # Major change
   ```

2. **Update content** to reflect new thesis

3. **Optionally preserve old version:**
   ```bash
   # Move v1 to archive with version in name
   git mv "manifestos/Manifesto, X.md" "archive/Manifesto, X - v1.0.0.md"

   # Create v2 in manifestos/
   # (new file with version: "2.0.0")
   ```

4. **Regenerate and commit:**
   ```bash
   just readme
   git add manifestos/ archive/ README.md
   git commit -m "feat: version <manifesto> to 2.0.0"
   ```

**Semantic versioning:**
- `1.0.0 → 1.1.0`: Minor enhancements (rare, usually just edit without versioning)
- `1.0.0 → 2.0.0`: Major thesis change (rare and significant)
- `1.0.0 → 1.0.1`: Patches (don't use; just edit)

---

### Adding a New Theme

**When:** Multiple manifestos in a new domain warrant their own grouping.

**Steps:**

1. **Edit `themes.yaml`:**
   ```yaml
   quantum-mechanics:
     icon: "⚛️"
     name: "Quantum Mechanics Principles"
     description: "Principles for quantum system design"
   ```

2. **Update manifesto frontmatter** to use new theme:
   ```yaml
   theme: "quantum-mechanics"
   ```

3. **Regenerate README:**
   ```bash
   just readme
   ```

   New theme section will appear automatically.

4. **Commit:**
   ```bash
   git add themes.yaml manifestos/ README.md
   git commit -m "feat: add quantum-mechanics theme"
   ```

**Theme design principles:**
- Themes are editorial groupings, not rigid taxonomy
- Each theme should contain 2+ manifestos (don't create single-manifesto themes)
- Theme names are kebab-case (`software-engineering`, not `Software Engineering`)
- Descriptions explain what unifies the theme

---

### Archiving a Manifesto

**When:** A manifesto is superseded, deprecated, or no longer relevant.

**Steps:**

1. **Move to archive:**
   ```bash
   git mv "manifestos/Manifesto, X.md" "archive/deprecated/Manifesto, X - deprecated.md"
   ```

2. **Regenerate README** (manifesto automatically disappears):
   ```bash
   just readme
   ```

3. **Commit:**
   ```bash
   git add manifestos/ archive/ README.md
   git commit -m "chore: archive deprecated <manifesto>"
   ```

**Note:** Archive is NOT scanned by `generate.py`. Only `manifestos/*.md` appears in README.

---

## Troubleshooting

### Validation Errors

**Error: Missing frontmatter**
```
❌ Missing Frontmatter: Manifesto, example.md
Missing key: 'title'
```

**Fix:** Add missing field to frontmatter:
```yaml
---
title: "The Missing Title"
```

---

**Error: Invalid semver**
```
❌ Schema Validation: Manifesto, example.md
Version must be semver (e.g., 1.0.0), got: 1.0
```

**Fix:** Use proper semver format:
```yaml
version: "1.0.0"  # Not "1.0" or "v1.0.0"
```

---

### Theme Discrepancies

**Warning: Theme not in themes.yaml**
```
⚠️  Theme Discrepancy
Themes in frontmatter but not in themes.yaml:
  • quantum-physics

Add these to themes.yaml or they'll render without icons/names
```

**Fix:** Add theme to `themes.yaml`:
```yaml
quantum-physics:
  icon: "⚛️"
  name: "Quantum Physics"
  description: "Quantum mechanics principles"
```

Or change frontmatter to use existing theme.

---

### Generation Failures

**No manifestos found:**
```
Error: manifestos/ directory not found
```

**Fix:** Ensure manifestos are in `manifestos/` directory, not root.

---

**README not updating:**

**Check:**
1. Did you run `just readme`?
2. Did generation succeed (green checkmark)?
3. Did you commit `README.md`?

**Fix:** Regenerate and verify:
```bash
just readme
git add README.md
git commit -m "docs: regenerate README"
```

---

## Reference

### Frontmatter Schema

**Required fields:**

```yaml
---
title: string          # Human-readable name
tagline: string        # Memorable hook/quote
version: string        # Semver (e.g., "1.0.0")
theme: string          # Must exist in themes.yaml
description: string    # One sentence, no period needed
---
```

**Validation rules:**
- `title`: any string
- `tagline`: any string
- `version`: must match `\d+\.\d+\.\d+` (e.g., `1.0.0`)
- `theme`: any string (warns if not in themes.yaml)
- `description`: any string (best as single sentence)

---

### File Structure

```
manifestos/                    # Active manifestos (scanned)
├── Manifesto, X.md
└── Manifesto, Y.md

config.yaml                    # Project metadata
themes.yaml                    # Theme display config
README.template.md             # Jinja2 template
generate.py                    # Validation + generation
justfile                       # Task commands

README.md                      # Generated (DO NOT EDIT)

archive/                       # Historical (NOT scanned)
└── deprecated/
```

---

### Generation Pipeline

1. **Scan:** `manifestos/*.md` files
2. **Parse:** Extract frontmatter with `python-frontmatter`
3. **Validate:** Pydantic schema check
4. **Warn:** Theme discrepancies (informational)
5. **Render:** Jinja2 template with data
6. **Write:** `README.md`

**Dependencies:**
- `pyyaml` - YAML parsing
- `python-frontmatter` - Frontmatter extraction
- `pydantic` - Schema validation
- `jinja2` - Template rendering
- `rich` - Terminal feedback

**Command:**
```bash
just readme  # Runs: uv run --with <deps> generate.py
```

---

## Philosophy Revisited

### The Maintainer's Oath

As curator of this collection, you are:

- **Guardian of quality:** Not everything deserves manifesto status
- **Preserver of integrity:** Validation catches corruption before it spreads
- **Navigator of discovery:** Good descriptions and themes make principles findable
- **Steward of evolution:** Manifestos can evolve, but version changes are significant events

### When to Say No

**Not every principle is a manifesto.**

Reject:
- Implementation details (those go in docs)
- Temporary best practices (those go in guides)
- Project-specific rules (those go in CONTRIBUTING)
- Unproven theories (those need evidence first)

Accept:
- Timeless behavioral principles
- Distilled wisdom with evidence
- Frameworks that shape decisions
- Boundaries that prevent known failure modes

### The Long View

Manifestos are meant to last. Write frontmatter descriptions as if explaining to someone 5 years from now why this principle mattered. Choose themes that organize by fundamental domain, not current trends.

The collection should age like wine, not milk.

---

**Questions? Issues?**

If this guide doesn't answer your question, the system design may have a gap. Consider whether the workflow needs refinement—or whether you're trying to do something manifestos weren't designed for.
