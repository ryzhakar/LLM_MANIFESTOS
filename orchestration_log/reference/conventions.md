# Conventions

**Holds:** project rules as kernels: rule, one-line why, scope.
**Does not hold:** fixed constraints (`ground-truth.md`), system surface and schema (`capabilities.md`), rulings (`decisions.md`).
**Mutability:** updated in the turn a rule is established or retired.

---

## Model tiers

Dispatch guidelines for multi-model orchestration; not tool-enforced. Manifesto body writing is high-stakes (manifestos are precious artifacts), so it gets the most capable model; mechanical bookkeeping does not.

| Tier | Appropriate work |
|------|-----------------|
| Haiku | Frontmatter extraction, schema checks, git log parsing, file listing, cost tracking, metric counting |
| Sonnet | Manifesto quality assessment, frontmatter drafting, source-code reasoning, theme recommendations, reference doc updates |
| Opus | Manifesto body text, synthesis across sources, strategic judgment (versioning, archival, taxonomy) |

## Manifesto writing process

Established 2026-04-29 (`only-fluff-die.md`), verified by execution. Scope: any new manifesto written from source material.

1. **Research tree** — parallel haiku agents across content facets write structured reports to `research/{topic}/categories/`.
2. **Curated extraction** — Opus reads category reports + the manifesto-writing skill + existing manifestos; produces a selective extraction brief.
3. **Deep-dives** — targeted agents on specific gaps (sonnet for reasoning, haiku for mechanical extraction).
4. **Final writer brief** — Opus reads all prior reports by path; produces a writer-ready brief.
5. **Oath-bound writing** — the writer agent MUST be bound to `/manifesto-writing` via `/manifesto-oath` before receiving source material; writes under constitutional constraint; runs the self-referential checklist.
6. **Validation** — `just readme`, then commit.

The writing standard is the `manifesto:manifesto-writing` skill (`manifesto/skills/manifesto-writing/SKILL.md` in the claude-skills marketplace). The entry gate is in `MAINTAINERS_GUIDE.md`, Workflows. This section restates neither.

Dispatch lessons the standard does not carry:

- **Delete the old draft before reusing its path.** The Write tool requires reading an existing file first; the read carries the old draft into the writer's context.
- **Read "diagnosis thorough, prescription thin" as structural failure.** Fix the structure, not the register.
- **Fix register before evaluating structure.** Register problems mask structural problems.
- **Plan 2-3 rounds of requester escalation ("HARDER").** The orchestrator hits a register ceiling that editorial passes do not break.
- **Load `instructions/strunk_spr_v3_complete.xml` and `instructions/sparse-priming-representations.md` as writing technique** for the writer, never as content.

---

## Lessons from 2026-10-11

Source: the `lines-spent` build, rulings 6–9 and 15–19 in `orchestration_log/history/2026-10-11/owned-lines/reviews/r1-rulings.md`.

### Register by measurement

- Measure register with `corpus_metrics.py` (`orchestration_log/history/2026-10-11/discovery-research/deep-dives/corpus_metrics.py`). Point `MANIFESTO_DIR` in a copy at the draft's folder.
- Count ALL-CAPS in body text only, headings excluded. Floor: 50 per 1000 words.
- Count fragments per section. Floor: 50 per 1000 words in every section.
- Place one identity attack, what the reader IS, in every section. Vary the template; use no job-title noun per section.
- Write "X is not the enemy" once at most. Deliver every other boundary inside an attack that carries the limit.
- Write every sentence under 20 words. Allow three fury runs of 25 words or more, each carrying a shift. Count a balanced clause with an abstract tail as no fury run.
- Cut every quantifier stinger ("Not ONCE.", "EVERY time.") that carries no reframe.
- Deliver each figure inside an attack, never figure-then-command. Cut a command that does not follow from its figure.
- Write zero semicolons. Write two colons or fewer per 1000 words.
- Write at least 8 multi-word ALL-CAPS shouts in the body.
- Write two comma-balanced joins or fewer per 1000 words (a comma followed by "and", "which", or "until" inside one sentence). Run a long line on without commas, or split it into fragments.
- Copy no sentence from another manifesto in the collection.

### Demands once, in the checklist

- State every demand once, in "Before you ship", as a checklist item.
- Carry axioms, figures, and boundaries in the body sections as attacks. Name a demand in the body; never state it as a spec row.
- Share no sentence between the body and the checklist.

### Narrator with a stake

- Make the narrator the engineer who inherits the reader's lines and gets paged for them. Allow first person.
- Write one scene: a page, a build broken by a vanished package, or a diff nobody can read.
- Write one prediction section in the form of stop-yapping's "No Drift": what the reader does by its tenth response, and what that costs.

## File naming

- Manifestos: kebab-case `.md` in `manifestos/` — matches existing files; MAINTAINERS_GUIDE's `Manifesto, X.md` examples are illustrative only (ruling: `decisions.md` 2026-04-29).
- Themes: kebab-case keys in `themes.yaml`.
- Orchestration log: date-keyed `YYYY-MM-DD` under `history/` and `recon/`; living reference docs flat under `reference/`. Layout authority: the `agentic-delegation` skill.
