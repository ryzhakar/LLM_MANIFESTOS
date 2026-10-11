<!-- AUTHOR BINDING, the brief-writer's own. BOUND in full: first-principles.md; strunk_spr_v3_complete.xml; manifesto-oath SKILL.md; manifesto-writing SKILL.md; claude-skills CLAUDE.md "Agent dispatch".
INTERPLAY: all five demand command over suggestion and primary text over name; the dispatch rule and the oath converge on rebinding from source, which BRIEF.md §a carries into every launch.
COMMIT: I must match each model to its work type, and I will put haiku on transforms only; I must open every agent's instructions with a source-path binding, and I will route every launch through BRIEF.md §a. -->
# Dispatch Roster — manifesto-craft

R = /home/user/LLM_MANIFESTOS/research/manifesto-craft. Expand R to the absolute path in every launch prompt. Every agent reads R/BRIEF.md; its §a binding preamble opens each agent's instructions. Launch every agent of a tier in one message, in the background.

| Tier | Agent | Model | Inputs | Output path | Blocked by |
|---|---|---|---|---|---|
| 1 | index-parser | haiku | R/BRIEF.md; R/sources.md | R/index.md | R/sources.md present |
| 2 | survey: entry-gate | sonnet | R/BRIEF.md; R/index.md; R/recon/sources/; R/deep-dives/{corpus,doctrine,runtime}-audit.md; BRIEF §f files | R/categories/entry-gate.md | Tier 1; all three Tier 0 audits |
| 2 | survey: binding-function | sonnet | as entry-gate | R/categories/binding-function.md | as entry-gate |
| 2 | survey: reader-register | sonnet | as entry-gate | R/categories/reader-register.md | as entry-gate |
| 2 | survey: form-aesthetics | sonnet | as entry-gate | R/categories/form-aesthetics.md | as entry-gate |
| 2 | survey: boundary-evidence | sonnet | as entry-gate | R/categories/boundary-evidence.md | as entry-gate |
| 2 | survey: failure-modes | sonnet | as entry-gate | R/categories/failure-modes.md | as entry-gate |
| 2 | breadth-expander | sonnet | R/BRIEF.md; R/index.md; R/sources.md | R/deep-dives/unlisted-sources.md | Tier 1 |
| 3 | verify-{id} — template; one row per trigger | sonnet | R/BRIEF.md; the report holding {id}; every location that row cites | R/deep-dives/verify-{id}.md | the Tier 2 report holding {id} |
| 4 | resolve-{topic} — template; one row per contradiction | sonnet | R/BRIEF.md; report A; report B; the locations both cite | R/deep-dives/{topic}-resolution.md | reports A and B; every Tier 3 verifier on the same id |
| 5 | synthesizer | opus | R/BRIEF.md; every Tier 0–4 report; then /home/user/LLM_MANIFESTOS/orchestration_log/history/2026-10-10/manifesto-definition.md, last (BRIEF §e6 step 6) | R/synthesis/synthesis.md | every Tier 0–4 report |

Model basis: haiku for the deterministic parse and fetch; sonnet for every agent that reads meaning; opus for the synthesis, which weighs every report and whose rule tiers guide the design discussion.

## Launch prompt — exactly three lines per agent

```
Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/BRIEF.md for instructions.
Your category/target: {X}.
Write to {output path}.
```

| Agent | {X} |
|---|---|
| index-parser | index parser |
| survey | one slug: entry-gate · binding-function · reader-register · form-aesthetics · boundary-evidence · failure-modes |
| breadth-expander | breadth expander |
| verifier | verify {id} in {absolute report path} |
| resolver | resolve {topic}: {absolute path A} {id A} vs {absolute path B} {id B} |
| synthesizer | synthesizer |

Write each filled launch prompt to R/prompts/launch-{agent}.md before launching it.

## Tier 3 triggers — one verifier each
- Every statement a survey rates RULE.
- Every MODEL finding a rated statement rests on.
- Every SECONDARY or UNVERIFIED finding a RULE or CANDIDATE rests on.
- Every finding two reports cite with different status.
- Every high-signal breadth find no survey cites.
- Every extraordinary claim in a completion summary.

## Tier 4 triggers — one resolver each
- One id, question, or shipped file given different status or rating by two reports.

## Gates — confirm before launching the next tier
- Lines 1–3 of every output begin `BOUND:`, `INTERPLAY:`, `COMMIT:`.
- Tier 1: the Statistics count equals the numbered rows.
- Tier 2: every §c question appears as a Q heading or under Open questions; every finding row carries quote, location, origin, reader, status.
- Tiers 3–4: claim status and rating, or verdict, present.
- Tier 5: every RULE row names a verification report.
