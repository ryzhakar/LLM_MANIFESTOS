# LLM Manifestos

Behavioral constitutions for language models

## Quick Reference

| Manifesto | Theme | Version |
|-----------|-------|---------|
| [Build For Today](manifestos/Manifesto, YAGNI - "build for today".md) | Software Engineering Principles | `1.0.0` |
| [Code Speaks](manifestos/Manifesto, self-documenting code - "code speaks".md) | Software Engineering Principles | `1.0.0` |
| [Correct By Construction](manifestos/Manifesto, rust - "correct by construction".md) | Software Engineering Principles | `1.0.0` |
| [Decomplect](manifestos/Manifesto, KISS - "decomplect".md) | Software Engineering Principles | `1.0.0` |
| [Knowledge Has One Home](manifestos/Manifesto, DRY - "knowledge has one home".md) | Software Engineering Principles | `1.0.0` |
| [The First Principles](manifestos/Manifesto, first-principles - "break the mold".md) | Cognitive Science | `1.0.1` |
| [The Simplicity Manifesto](manifestos/Manifesto, "simple made easy".md) | Software Engineering Principles | `1.0.0` |
| [The Zen of Python](manifestos/Manifesto, zen-of-python.md) | Software Engineering Principles | `1.0.0` |


---




## 🧠 Cognitive Science

Systems for thinking


### [The First Principles](manifestos/Manifesto, first-principles - "break the mold".md) `1.0.1`
*"break the mold"*

Stop copying. Stop iterating. Deconstruct reality to its axioms and build the future from scratch.

---




## 🔧 Software Engineering Principles

Core principles for building maintainable, understandable software


### [Build For Today](manifestos/Manifesto, YAGNI - "build for today".md) `1.0.0`
*"build for today"*

Stop building for imagined futures. Presumptive development creates cascading costs that compound into bankruptcy.

---


### [Code Speaks](manifestos/Manifesto, self-documenting code - "code speaks".md) `1.0.0`
*"code speaks"*

Code should be so clear it teaches its domain without comments. Comments are admissions of defeat.

---


### [Correct By Construction](manifestos/Manifesto, rust - "correct by construction".md) `1.0.0`
*"correct by construction"*

Make invalid states unrepresentable. Every compiler error is a bug you didn't ship.

---


### [Decomplect](manifestos/Manifesto, KISS - "decomplect".md) `1.0.0`
*"decomplect"*

Complexity from braiding is killing software. Simple means untangled. Keep things separate.

---


### [Knowledge Has One Home](manifestos/Manifesto, DRY - "knowledge has one home".md) `1.0.0`
*"knowledge has one home"*

Knowledge duplication (not code duplication) is the enemy. Every piece of knowledge must have one authoritative representation.

---


### [The Simplicity Manifesto](manifestos/Manifesto, "simple made easy".md) `1.0.0`
*"simple made easy"*

Distinguishes simple (untangled) from easy (familiar). Complexity from conflating them destroys software quality.

---


### [The Zen of Python](manifestos/Manifesto, zen-of-python.md) `1.0.0`
*"beautiful is better than ugly"*

Tim Peters' aphorisms for Python design philosophy. Explicit over implicit, simple over complex.

---




## Maintenance

> *Manifestos are precious artifacts, not documentation.*

This README is generated from manifesto frontmatter. **For complete maintainer workflows, see [MAINTAINERS_GUIDE.md](MAINTAINERS_GUIDE.md).**

**Quick workflow:**

1. Edit manifesto files in `manifestos/`
2. Run `just readme`
3. Commit changes

**Adding a new manifesto:**
- Create `manifestos/Manifesto, <name>.md` with required frontmatter (title, tagline, version, theme, description)
- If using a new theme, add it to `themes.yaml` first
- See [MAINTAINERS_GUIDE.md](MAINTAINERS_GUIDE.md) for philosophy and detailed workflows

**Schema validation:** Powered by Pydantic. Invalid frontmatter will be caught with detailed error messages.