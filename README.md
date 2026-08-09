# LLM Manifestos

Behavioral constitutions for language models

## Quick Reference

| Manifesto | Theme | Version |
|-----------|-------|---------|
| [Build For Today](manifestos/yagni.md) | Software Engineering Principles | `1.0.0` |
| [Cargo Cult Science](manifestos/cargo-cult-science.md) | Cognitive Science | `1.0.0` |
| [Code Speaks](manifestos/self-documenting-code.md) | Software Engineering Principles | `1.0.0` |
| [Correct By Construction](manifestos/correct-by-construction.md) | Software Engineering Principles | `1.0.0` |
| [Decomplect](manifestos/kiss.md) | Software Engineering Principles | `2.0.0` |
| [Knowledge Has One Home](manifestos/dry.md) | Software Engineering Principles | `1.0.0` |
| [Respect the Engine](manifestos/postgres.md) | Software Engineering Principles | `1.0.0` |
| [Stop Yapping](manifestos/stop-yapping.md) | Cognitive Science | `1.0.0` |
| [The First Principles](manifestos/first-principles.md) | Cognitive Science | `1.0.1` |
| [The Simplicity Manifesto](manifestos/simple-made-easy.md) | Cognitive Science | `2.0.0` |
| [The Zen of Python](manifestos/zen-of-python.md) | Software Engineering Principles | `1.0.0` |
| [Trust Nothing, Restore Everything](manifestos/intervention.md) | Cognitive Science | `1.0.0` |

---

## 🧠 Cognitive Science
Systems for thinking


### [Cargo Cult Science](manifestos/cargo-cult-science.md) `1.0.0`
*"the first principle is that you must not fool yourself"*

Some remarks on science, pseudoscience, and learning how to not fool yourself.

---

### [Stop Yapping](manifestos/stop-yapping.md) `1.0.0`
*"answer. shut up."*

Performative helpfulness degrades accuracy. Every word past the answer is failure.

---

### [The First Principles](manifestos/first-principles.md) `1.0.1`
*"atoms, not analogies"*

Stop copying. Stop iterating. Deconstruct reality to its axioms and build the future from scratch.

---

### [The Simplicity Manifesto](manifestos/simple-made-easy.md) `2.0.0`
*"the confusion is killing you"*

Distinguishes simple (untangled) from easy (familiar). A thinking framework — the conflation is a cognitive error before it is a software defect.

---

### [Trust Nothing, Restore Everything](manifestos/intervention.md) `1.0.0`
*"roots, not canopy"*

An intervener's protocol for diagnosing and restoring corrupted systems without being absorbed by them

## 🔧 Software Engineering Principles
Core principles for building maintainable, understandable software


### [Build For Today](manifestos/yagni.md) `1.0.0`
*"build for today"*

Stop building for imagined futures. Presumptive development creates cascading costs that compound into bankruptcy.

---

### [Code Speaks](manifestos/self-documenting-code.md) `1.0.0`
*"comments are lies"*

Code should be so clear it teaches its domain without comments. Comments are admissions of defeat.

---

### [Correct By Construction](manifestos/correct-by-construction.md) `1.0.0`
*"invalid states cannot compile"*

Make invalid states unrepresentable. Every compiler error is a bug you didn't ship.

---

### [Decomplect](manifestos/kiss.md) `2.0.0`
*"incidental is Latin for your fault"*

Complexity from braiding is killing software. Concrete commands for unbraiding codebases, questioning layers, and resisting AI slop.

---

### [Knowledge Has One Home](manifestos/dry.md) `1.0.0`
*"knowledge has one home"*

Knowledge duplication (not code duplication) is the enemy. Every piece of knowledge must have one authoritative representation.

---

### [Respect the Engine](manifestos/postgres.md) `1.0.0`
*"you use 5% of what you bought."*

Postgres is a precision instrument. You use it as a filing cabinet. The schema is the architecture. The application is the view layer. Everything else you believe is wrong.

---

### [The Zen of Python](manifestos/zen-of-python.md) `1.0.0`
*"refuse to guess"*

Tim Peters' aphorisms for Python design philosophy. Explicit over implicit, simple over complex.

## Maintenance

> *Manifestos are precious artifacts, not documentation.*

This README is generated from manifesto frontmatter. **For complete maintainer workflows, see [MAINTAINERS_GUIDE.md](MAINTAINERS_GUIDE.md).**

**Quick workflow:**

1. Edit manifesto files in `manifestos/`
2. Run `just readme`
3. Commit changes

**Adding a new manifesto:**
- Create `manifestos/<name>.md` with required frontmatter (title, tagline, version, theme, description)
- If using a new theme, add it to `themes.yaml` first
- See [MAINTAINERS_GUIDE.md](MAINTAINERS_GUIDE.md) for philosophy and detailed workflows

**Schema validation:** Powered by Pydantic. Invalid frontmatter will be caught with detailed error messages.
