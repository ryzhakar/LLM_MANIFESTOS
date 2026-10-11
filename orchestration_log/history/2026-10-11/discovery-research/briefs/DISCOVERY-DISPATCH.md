<!-- AUTHOR BINDING, the brief-writer's own. BOUND in full: first-principles.md; strunk_spr_v3_complete.xml; manifesto-oath SKILL.md; manifesto-writing SKILL.md; claude-skills CLAUDE.md "Agent dispatch".
INTERPLAY: all five demand command over suggestion and primary text over name; the dispatch rule and the oath converge on rebinding from source, which DISCOVERY-BRIEF.md §a carries into every launch.
COMMIT: I must match each model to its work type, and I will put every reading agent on sonnet; I must open every agent's instructions with a source-path binding, and I will route every launch through DISCOVERY-BRIEF.md §a. -->
# Discovery Dispatch — latent manifestos

R = /home/user/LLM_MANIFESTOS/research/manifesto-craft. Expand R to the absolute path in every launch prompt. Every agent reads R/DISCOVERY-BRIEF.md; its §a binding preamble opens each agent's instructions. Launch every agent of a tier in one message, in the background. Tier 0 and the two lane fetches (Tier 1) precede this roster.

| Tier | Agent | Model | Inputs | Output path | Blocked by |
|---|---|---|---|---|---|
| 2 | survey: enemies | sonnet | R/DISCOVERY-BRIEF.md; R/recon/index-lane1.md; R/recon/index-lane2.md; R/recon/sources/*.txt (11) | R/discovery/enemies.md | both lane indexes |
| 2 | survey: distinctions-vocabulary | sonnet | as enemies | R/discovery/distinctions-vocabulary.md | both lane indexes |
| 2 | survey: evidence | sonnet | as enemies; WebSearch and curl for second sources | R/discovery/evidence.md | both lane indexes |
| 2 | survey: demands | sonnet | as enemies | R/discovery/demands.md | both lane indexes |
| 2 | survey: tensions | sonnet | as enemies | R/discovery/tensions.md | both lane indexes |
| 2 | survey: collection-fit | sonnet | as enemies; R/deep-dives/{corpus,doctrine,runtime,collection-overlap}-audit.md | R/discovery/collection-fit.md | both lane indexes; R/deep-dives/collection-overlap-audit.md |
| 2 | survey: breadth | sonnet | as enemies; WebSearch and curl for adjacent primary texts | R/discovery/breadth.md | both lane indexes |
| 3 | verify-{id} — template; one row per trigger | sonnet | R/DISCOVERY-BRIEF.md; the report holding {id}; every location that row cites | R/discovery/verify-{id}.md | the Tier 2 report holding {id} |
| 4 | resolve-{topic} — template; one row per contradiction | sonnet | R/DISCOVERY-BRIEF.md; report A; report B; the locations both cite | R/discovery/{topic}-resolution.md | reports A and B; every Tier 3 verifier on the same id |
| 5 | synthesizer | opus | R/DISCOVERY-BRIEF.md; every R/discovery/ report; both lane indexes; the four Tier 0 audits | R/discovery/candidates.md | every Tier 2–4 report |

Model basis: every surveyor, verifier, and resolver reads meaning, so sonnet; the synthesizer decides which manifestos exist and ranks them, so opus.

## Launch prompt — exactly three lines per agent

```
Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/DISCOVERY-BRIEF.md for instructions.
Your category/target: {X}.
Write to {output path}.
```

| Agent | {X} |
|---|---|
| survey | one slug: enemies · distinctions-vocabulary · evidence · demands · tensions · collection-fit · breadth |
| verifier | verify {id} in {absolute report path} |
| resolver | resolve {topic}: {absolute path A} {id A} vs {absolute path B} {id B} |
| synthesizer | synthesizer |

Write each filled launch prompt to R/prompts/discovery-launch-{agent}.md before launching it.

## Tier 3 triggers — one verifier each
- Every candidate statement a survey rates AXIOM.
- Every enemy cluster, distinction, or axiom cluster that crosses lanes on a single quote per lane.
- Every evidence claim marked VERIFIED in-text but UNVERIFIED or CONTRADICTED in corroboration.
- Every breadth find cited as contradicting a substrate claim.
- Every finding two reports cite with different status.
- Every extraordinary claim in a completion summary.

## Tier 4 triggers — one resolver each
- One quote, claim, or cluster given different status, rating, or reading by two reports.
- A collection-fit focus point that another survey's clusters contradict.

## Gates — confirm before launching the next tier
- Lines 1–3 of every output begin `BOUND:`, `INTERPLAY:`, `COMMIT:`.
- Tier 2: every §c question appears as a Q heading or under Open questions; the slug's category table exists; every finding row carries quote, location, origin, reader, status, lens.
- Tiers 3–4: status and rating, or verdict, present.
- Tier 5: two to four candidates; every field cited; no title, no prose draft; every AXIOM names a verification report.
