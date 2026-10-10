# What Makes a Good Manifesto — Cross-Project Synthesis

_Preparation for the manifesto design discussion. Derived from the two projects' own texts and logs; nothing here is a proposal yet._

---

## 1. Where each project defines it

| Project | Artifact | Role |
|---|---|---|
| LLM_MANIFESTOS | `MAINTAINERS_GUIDE.md` | Curator's bar: what enters the collection |
| LLM_MANIFESTOS | `generate.py` + `themes.yaml` | Schema: the five fields every manifesto carries |
| LLM_MANIFESTOS | `orchestration_log/reference/conventions.md` | Production lessons: how a shipping manifesto is actually made |
| LLM_MANIFESTOS | `orchestration_log/history/*/session.md` | Decision and failure logs: candidacy tests, reader, register, escape hatch |
| LLM_MANIFESTOS | `manifestos/*.md` (12 files) | Practice: the form as shipped |
| claude-skills | `manifesto/skills/manifesto-writing/SKILL.md` | Writer's spec: the source → manifesto transformation |
| claude-skills | `manifesto/skills/manifesto-oath/SKILL.md` | Binder's spec: what a manifesto must be to construct an operating identity |
| claude-skills | `manifesto/agents/maximalist-reviewer.md` | Reviewer's spec: every line is a checkable demand |
| claude-skills | `manifesto/hooks/*` + `SCHEMA.md` | Runtime: self-contained primary text; tagline as per-prompt drift atom |
| claude-skills | `ETHOS.md` | Writing stance the skill inherits (core-point spine, directive language, self-containment) |

---

## 2. LLM_MANIFESTOS — the curator's definition

**Thesis.** "Behavioral constitutions" — timeless principles defining how a system operates. "Precious artifacts, not documentation." Rare; adding one is a significant event.

| A manifesto is | A manifesto is not |
|---|---|
| A philosophical framework distilled into actionable principles | An implementation guide |
| A boundary condition on acceptable behavior | A technical specification |
| An artifact preserving a hard-won insight | A temporary note |
| A standard decisions are measured against | A living document edited often |

**Entry bar (curator questions).** Timeless or temporary? Defines behavior or describes implementation? Actionable or aspirational? Still matters in five years?

| Accept | Reject |
|---|---|
| Timeless behavioral principles | Implementation details |
| Distilled wisdom with evidence | Temporary best practices |
| Frameworks that shape decisions | Project-specific rules |
| Boundaries that prevent known failure modes | Unproven theories |

**Schema as definition.** Five required fields; each carries a quality rule.

| Field | Rule |
|---|---|
| `title` | Emerges from content, never pre-decided. Short; contains action, target, distinction. Must sit beside existing titles (the "works alongside Decomplect?" test). |
| `tagline` | The deepest counterintuitive claim. Memorable, distinctive, creates dissonance. Operationally: the drift-reminder atom injected on every prompt, so it must re-bind alone. Sharpened for that purpose on 2026-05-01. |
| `description` | One sentence answering "why read this", written for a reader five years out. |
| `theme` | Exactly one. Editorial, not taxonomic. Must differentiate *within* the collection — `ai-instructions` rejected because every manifesto here is an AI instruction. Never a single-manifesto theme. |
| `version` | Major only. Bump on thesis change. Frequent small edits mean the principle has not crystallized. |

**Learned in production** (three sessions, two shipped manifestos, ten failed drafts):

| Lesson | Source |
|---|---|
| Candidacy passes on three grounds: measured evidence, a principle that knows its own exceptions, a precise binary taxonomy rather than a fuzzy guideline | 2026-04-29 decision log |
| Name the enemy with precision ("performative noise", not "verbosity") | 2026-04-29 |
| Declare, do not cite. "A manifesto is a tool for crystallization and transmission, not for discovery or persuasion." | 2026-04-29 |
| Do not write in the source's novelty voice; voice appears in title and one line | 2026-04-29 |
| Target 70%+ bindable lines, under 200 lines, and the text passes its own rules (self-referential check) | 2026-04-29 final-writer brief |
| Structural patterns that bind: imperative commands, binary distinctions, decision procedures, checklists. Patterns that only decorate: rhetoric | 2026-04-29 binding-effectiveness analysis |
| The model IS the reader. Every "you" is the model when bound | 2026-05-01 |
| No escape hatch. "If everything is important, every response escapes" | 2026-05-01 |
| Fury is a binding force multiplier, not decoration. Anger must be grammatical and lexical, not only semantic | 2026-05-01 |
| Core frame: the behavior constituting "success" IS the failure mode (helpfulness paradox) | 2026-05-01 |
| Skill defaults produce a measured essay; the writer mirrors the prompt's register; lead with the emotional mandate, constrain structure minimally | conventions.md |
| Prescription and diagnosis share one voice; teaching happens inside the attack | 2026-05-11 |
| Register before structure; full rewrite to a fresh path when register must break; unbiased reviewers override the orchestrator; anti-Claude patterns as a mechanical checklist | conventions.md |
| Closing calls back the opening enemy sentence; tables are indictments, introduced ("Read this table slowly") | 2026-05-11 |
| Factual accuracy still binds: 29 technical fixes from five reviewers before ship | 2026-05-11 |

---

## 3. claude-skills — the writer's and the binder's definition

### 3a. `manifesto-writing` (producer side)

**Thesis.** "Concentrated declarations of principle that command rather than explain. It declares. It commands. It names enemies. It assumes the reader is ready to be changed."

| Preserve | Cut | Transform |
|---|---|---|
| Core distinctions (the hinges) | Audience asides | "I believe X" → "X." |
| Sharp vocabulary the author coined | Extended examples | "Consider Y" → "Y." |
| Aphorisms under 15 words | Hedging | "Possibly Z" → "Z." or delete |
| The moral core (stakes) | Repetition for emphasis | Buildup → lead with the blade |
| Actionable principles | Scaffolding, pre-answered objections | Extended analogy → one image |
| | Qualifications, unless they are the point | |

**Structure.** Enemy named in the first section. Declarations, not arguments. Imperative mood. Sentences under 20 words, sections under 150. Tables for mappings. End with a stark choice. Attribute as "After [Author]".

**Tone.** Include: moral urgency, "you", present tense, active voice, concrete nouns. Exclude: hedging, passive, future promises, abstract nouns, weasel words.

**Length.** One sitting. 1500–2500 words from a 45-minute talk; shorter is better.

**Prerequisites.** Requires conviction. Flattens nuance. Assumes sympathetic readers. Sacrifices precision for force. "Crystallization and transmission, not discovery or persuasion" — the same sentence the curator's decision log quotes.

### 3b. `manifesto-oath`, hooks, `maximalist-reviewer` (consumer side)

The binder defines a manifesto by what it must survive:

| Demand on the text | Where |
|---|---|
| It is a primary text. A name is not a source; binding to a summary or memory is "worse than not binding" | oath, Constitution Stack |
| It is self-contained: hooks carry names, purposes, sources — never content. Transitive references resolve to depth three at most | SCHEMA.md, binding-core.txt |
| It reduces to irreducible axioms: "strip prose — identify core behavioral demands" | oath, Deconstruct |
| It composes: convergence and tension with other elements must be mappable, with an explicit rule per tension | oath, Interplay |
| Each demand yields a paired commitment: "I must X, and I will Y" | oath, Identity-Mode |
| Every line is a numbered, checkable rule at its strongest literal reading. Every example, table row, and aside counts as a demand, never as illustration | maximalist-reviewer |
| Its tagline alone re-binds on every prompt | drift-reminder hook |
| Its shape sets the shape of compliance: "a terse constitution demands a terse binding" | oath, Articulate |

### 3c. Inherited stance (`ETHOS.md`)

Five core points survive any rewrite as the spine. Commands, not suggestions; one emphatic marker per directive. Self-containment: content not in the body is not followed. The skill-writing stance audit of 2026-09-15 records `manifesto-writing` as the one skill conforming to the core-point spine.

---

## 4. Practice — the twelve shipped files

| File | Words | Opens on enemy | Ends on choice | Boundary section | Attribution | Register | Species |
|---|---|---|---|---|---|---|---|
| zen-of-python | 134 | no | no | no | description only | aphorism | canon, verbatim |
| intervention | 759 | yes | "Choose." | no | none | parable, neutral | transformed |
| first-principles | 861 | yes | "The Choice" | no | After Aristotle… | urgent, neutral | transformed |
| self-documenting-code | 1161 | yes | "Choose Path 2" | Four Exceptions | none | neutral | transformed |
| stop-yapping | 1214 | yes (quoted sentence) | "Pick." | removed deliberately | After Brussee | abusive, model-addressed | transformed |
| correct-by-construction | 1366 | yes | "The Choice" | What You Give Up | After Oaten | neutral | transformed |
| dry | 1399 | yes | "The Choice" | When Duplication is Acceptable | After Thomas… | neutral | transformed |
| yagni | 1498 | yes | "The Choice" | When To Build For Tomorrow | After Beck… | neutral | transformed |
| simple-made-easy | 1559 | "The Problem" | "Choose." | no | After Hickey | neutral | transformed |
| kiss | 1937 | yes | "Your Choice" | When Complexity is Justified | After Hickey… | neutral, evidence-heavy | transformed |
| cargo-cult-science | 3854 | no | no (a wish) | no | by Feynman | lecture, hedged (19 hedges) | canon, verbatim |
| postgres | 5267 | yes (quoted sentence) | "PICK" | removed deliberately | none | abusive, model-addressed | transformed |

Second-person density per 1000 words: first-principles 29, kiss 34, postgres 73, stop-yapping 77. The register shift of May 2026 doubled direct address.

**Common skeleton of the transformed species.** ALL-CAPS title → "After X" → The Enemy → the core distinction, usually a two-column table → cost or evidence → Commands under imperative headings → a boundary section → The Choice as A/B → closing aphorism that echoes the tagline.

---

## 5. Convergence — the shared spine

1. **Behavioral, not informational.** Curator: "behavioral constitution." Writer: "command rather than explain." Binder: constructs an operating identity. All three define the artifact by what it makes the reader do.
2. **One enemy, named first, named precisely.** Skill rule, decision-log rule, and ten of twelve files.
3. **Compression to binaries.** Core distinction, two-column table, aphorism under 15 words. The binding analysis found binary distinctions among the patterns that actually bind.
4. **Declaration over persuasion.** The sentence "crystallization and transmission, not discovery or persuasion" appears in both projects. Evidence is declared as fact, never cited.
5. **Ends in a stark choice.** Skill rule; every transformed file.
6. **Rare, timeless, high bar.** Curator's five-year test; skill's "requires conviction"; version only on thesis change.
7. **The file is the unit.** Primary text, self-contained, loadable alone; a name is never a source.
8. **Bindability is the test.** Lines are demands checkable at a literal reading; target 70%+ bindable; the text passes its own rules.
9. **Tagline is the atom.** It must re-bind alone, on every prompt, and sit distinct from its neighbors.

---

## 6. Tensions and gaps

| # | Tension | Side A | Side B | State |
|---|---|---|---|---|
| T1 | Two species | Skill defines by form (enemy, commands, choice) | Curator admits by content; zen-of-python and cargo-cult-science ship verbatim, violating every form rule | Unstated; collection holds both |
| T2 | Length | Skill: 1500–2500 words, "shorter is better"; writer brief: under 200 lines | postgres ships at 5267 words / 269 lines by explicit spec ("constitution length") | No length rule survives practice |
| T3 | Register | Skill: "moral urgency", neutral declarative; conventions name the skill's defaults as the cause of three failed drafts | Practice since May: abusive, contemptuous, profanity at peaks; identity attacks | Skill never updated; register is unspecified doctrine, specified only in session logs |
| T4 | Reader | Skill: "assumes sympathetic readers" | Decision log: the model is the reader and is treated as resistant, addicted, "wired to yap" | Direct contradiction in the prerequisites |
| T5 | Boundary vs escape | Candidacy criterion: "the principle knows its own exceptions"; six files carry a boundary section | "No escape hatch" ruling; stop-yapping and postgres strip it | The line between a boundary (where the principle stops) and an escape (when it may be ignored) is undrawn |
| T6 | Evidence | Curator: "distilled wisdom with evidence"; "unproven theories need evidence first" | Skill: "declarations, not arguments"; declare, do not cite | Resolved in practice: accuracy is mandatory (29 fixes), argumentation is forbidden, numbers appear as flat declarations. Not written down |
| T7 | Rationale | ETHOS for skills: "policy without rationale" | Skill preserves "the moral core — why this matters"; every file carries a stakes or cost section | Different artifact classes; must be stated so ETHOS is not imported wholesale |
| T8 | Attribution | Skill: mandatory "After [Author]" | Four files carry none (intervention, self-documenting-code, postgres, zen) | Inconsistent; no rule for user-authored substrate |
| T9 | Self-reference | Writer brief: the manifesto passes its own rules | Only stop-yapping was checked this way | One-off, not a gate |
| T10 | Ownership of the definition | claude-skills holds the "quality standard" every failure log says must be supplied to writers | LLM_MANIFESTOS holds the learned standard (register, reader, escape hatch, anti-Claude list, reviewer protocol) in logs | The skill is the declared source of truth and is the stale one |
| T11 | Theme | Must differentiate within the collection | Three defined themes hold zero files; one theme holds seven | Taxonomy carries little signal |

---

## 7. Working definition (as the two projects jointly hold it today)

A manifesto is a behavioral constitution: one self-contained primary text that, once loaded, constructs the reader's operating identity. It names one enemy first and precisely. It reduces its subject to a few binary distinctions and a set of irreducible demands, each checkable at a literal reading. It states positions as facts, commands in the imperative, and declares its evidence without citing. It addresses the reader as "you" — the model, when bound — and holds the diagnosis and the prescription in one voice. It marks where the principle stops and offers no clause for ignoring it. It passes its own rules. It ends with a stark choice. It compresses to a tagline that re-binds alone. It is timeless enough to version only when its thesis changes.

**Checks already present somewhere in the corpus, collected:**

| Check | Form | Source |
|---|---|---|
| Enemy named in the first section | structural | skill |
| Ends with a choice | structural | skill, practice |
| Sentences under 20 words; sections under 150 | measurable | skill |
| Aphorisms under 15 words | measurable | skill |
| No hedges ("I think", "perhaps", "it seems") | grep | skill, stop-yapping kill list |
| No anti-Claude tells (delve, three-part lists, summary paragraphs, uniform sentence weight, zero fragments) | checklist | 2026-05-11 recon |
| Bindable lines ≥ 70% | ratio | writer brief |
| Every table row and example reads as a demand | review | maximalist-reviewer |
| Passes its own rules | self-review | writer brief |
| Five frontmatter fields; semver major | schema | generate.py |
| Tagline distinct from all existing taglines | collection | curator |
| Theme shared by ≥ 2 files | collection | curator |
| Attribution "After [Author]" | structural | skill |
| Factual claims verified by reviewers who did not write the text | process | conventions |

---

## 8. Questions the design discussion must settle

1. **One species or two.** Is a verbatim canonical text (Zen, Feynman) a manifesto, or a different artifact class the collection also keeps? If both, what does the schema or theme say about it?
2. **Who reads.** Human sympathetic reader (skill) or resistant model (practice)? Is register a per-manifesto choice recorded in frontmatter, or a collection rule?
3. **Length.** A ceiling, a bindable-ratio floor instead of a ceiling, or nothing?
4. **Boundary vs escape.** Draw the line: a boundary section defines the enemy's edge; an escape clause permits non-compliance by context. Keep the first, forbid the second?
5. **Evidence.** State the resolved rule: accuracy mandatory, citation forbidden, numbers declared flat.
6. **Where the definition lives.** The skill (claude-skills) or the guide (LLM_MANIFESTOS)? Whichever is chosen must absorb the session-log lessons; the other must point to it, not duplicate it.
7. **Acceptance test.** Adopt the maximalist-reviewer rule extraction plus the bindable-ratio as the gate for entry, replacing the curator's four questions or sitting beside them?
8. **Tagline as a stated requirement.** Form rule: one line, under eight words, re-binds alone, distinct in the collection.
9. **Attribution for user-authored substrate.** Mandatory line, or omit when no external author exists?
10. **Theme taxonomy.** Retire the three empty themes, or populate them before the next manifesto ships?
