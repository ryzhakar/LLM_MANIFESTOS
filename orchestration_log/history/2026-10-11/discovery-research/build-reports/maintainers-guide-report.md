Binding, elements loaded: First Principles (/home/user/LLM_MANIFESTOS/manifestos/first-principles.md, 116 lines, v1.0.0), Strunk SPR v3 (/home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml, 2923 lines), manifesto-oath protocol (/home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md), Stop Yapping (/home/user/LLM_MANIFESTOS/manifestos/stop-yapping.md); each read in full from source. Writing standard (/home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md) read whole as task input.
Binding, interplay: First Principles, Strunk, and Stop Yapping converge on the verified atom stated briefly: the owner's decisions are the atoms, the files are the proof, every other word goes. Tensions: Stop Yapping cuts articles and demands fragments while Strunk demands complete, clear sentences; resolution: Strunk's technical-documentation allowance, so the guide uses commands, tables, and full sentences and this report uses fragments. Strunk's judgment latitude against the owner's "commands and facts, nothing argued"; resolution: the owner governs, no hedge enters the guide.
Binding, commitments: I must state each owner decision as a command or fact, and I will cite each claim to a file or a run; I must strip every sentence that argues or narrates failure, and I will count the removals against the old text; I must not edit manifesto bodies, schema code, or drafts/, and I will not; every deviation sits under Open.

# Maintainers Guide rewrite

Repository /home/user/LLM_MANIFESTOS, branch claude/manifesto-design-discussion-liuuvf. Verified before writing: `just readme` exit 0, 12 manifestos, no panel; `tests/test_generate.py` 18 of 18; `ManifestoMetadata` ignores extra keys and accepts `1.1.0`.

## Line counts — before, after, per file

| file | before (628881c) | after (b4bc61c) |
|---|---|---|
| MAINTAINERS_GUIDE.md | 497 | 314 |
| orchestration_log/reference/conventions.md | 153 | 138 |
| orchestration_log/reference/codebase_state.md | 109 | 109 |
| orchestration_log/reference/deferred_items.md | 46 | 55 |

Guide cap 320; after 314. Section order held: Philosophy (+ Species), Architecture, Maintainer Roles, Workflows (+ Entry Gate, Re-cutting), Troubleshooting, Reference. The old trailing "Philosophy Revisited" and closing "Questions? Issues?" are gone (Open 8).

## Rationale sentences removed — count, three examples

36: 28 in MAINTAINERS_GUIDE.md (counted against 628881c; each quote checked present in the old file and absent from the new), 8 in conventions.md.

Examples:
1. "Adding a manifesto is a significant event. Manifestos are rare and precious." (guide, Curator's Responsibility)
2. "Eliminates knowledge duplication (DRY manifesto)" and the other bullets of "Why This Design" (guide, Architecture)
3. "README drift is silent corruption of the collection's navigation layer." (conventions, Forbidden Patterns)

Also cut: the three "Common mistakes" bullets, the four oath bullets, "The collection should age like wine, not milk."

## Commits — hash | message

| hash | message |
|---|---|
| b0645cb | doc: maintainers guide — entry gate, species, re-cuts, schema |
| f7204f9 | doc: conventions — writing standard by reference, schema facts |
| b4bc61c | doc: reference — inventory and deferred items after schema change |

Push: `git push -u origin claude/manifesto-design-discussion-liuuvf` succeeded on the first attempt (no retry, no rebase); 628881c..b4bc61c; local and origin HEAD both b4bc61c3e64ee0f6b3b5c718972528f187a15a6d. No attribution lines, single-line messages. `drafts/` (untracked, another agent) untouched.

What changed, in brief:
- Guide: entry gate (6 stages, artifact per stage, orchestrator check, worked example from the 2026-10-11 paths); Species (manifesto, canon); Re-cutting (rows as file:line, held ground, version rule); versioning major only with the `1.0.1` text replaced by a forbidden row; Reference schema rebuilt from generate.py (kind, register, reader, tagline rule, duplicate-tagline warning, extra keys ignored); file naming kebab-case; Troubleshooting samples replaced with real generator output.
- conventions.md: Manifesto Writing Process points to `manifesto:manifesto-writing` and keeps five dispatch lessons the standard lacks; Frontmatter Schema rewritten (the `[ORCHESTRATOR: verify]` tag resolved by test); Forbidden Patterns updated; stale `Manifesto, X.md` note removed.
- codebase_state.md: 12-file inventory with kind/register/reader; two themes; first-principles 1.0.0; generate.py 182 lines; template columns; Known Limitations and Next Actions rewritten.
- deferred_items.md: OQ-001 resolved by cf168d1; OQ-002 resolved by 12ba3f1; OQ-004 (ETHOS.md:37 names PostCompact) and OQ-005 (two manifesto-dir paths) opened, the two items build-log.md lists as deferred to the owner.

## Open

1. PostCompact: none of the four documents named it, so nothing changed for it. It survives only in /home/user/claude-skills/ETHOS.md:37 (OQ-004).
2. "Never counted against the entry bar" (canon) is stated verbatim in the guide. Two readings: canon files are not held to the bar; canon ground does not count as held ground in gate test 3. Owner rules.
3. Re-cut record location is undecided. The guide places it in the `SPEC.md` of the draft that causes the re-cut; a re-cut with no draft has no home.
4. Spec contents beyond the axiom with its authors, the enemy, the ground, and the re-cut record are undefined. The guide merges "gate test" and "spec" into one stage with one artifact, `drafts/<slug>/SPEC.md`.
5. The gate says "verified axiom". The guide reads it as rated VERIFIED; a QUALIFIED axiom does not pass as written.
6. The fate of `drafts/<slug>/` after ship is undefined. The guide says only "move the final version to `manifestos/<slug>.md`".
7. README.template.md ("Adding a new manifesto") still lists direct file creation and bypasses the entry gate. Out of scope (template); needs one line pointing to the gate.
8. Dropped from the old guide: "Philosophy Revisited" (reject list folded into Curator, long-view commands folded into Navigator), the Accept list, the Curator "Questions to ask", the `docs/`, `requirements/`, `scratch/` pointers (no such directories exist). Restore any on request.
9. Troubleshooting: the old "Missing Frontmatter / Missing key: 'title'" sample did not match generate.py, which reports a missing field as "Schema Validation ... Field required". The sample is replaced.
10. conventions.md Model Tiers "Rationale:" sentence untouched (outside the named sections).
11. Pre-standard files, bodies out of scope: 4 files carry no attribution line (intervention, postgres, self-documenting-code, zen-of-python); cargo-cult-science.md has `*by RICHARD P. FEYNMAN*` with no year; only stop-yapping.md has `reader: model`. Recorded in codebase_state.md Known Limitations.
12. generate.py accepts any `x.y.z`; the major-only rule is unenforced. Recorded in the guide and codebase_state.md.
13. The manifesto-oath SKILL.md example still shows first-principles at v1.0.1. Out of scope (plugin).
14. Attribution placement is not fixed: the writing standard ends the body with it; existing files put it under the title or at the end. The guide states the format only.

Notification summary: Guide 497 to 314 lines, conventions 153 to 138, codebase_state 109 to 109, deferred_items 46 to 55; 36 rationale sentences removed. Three commits, b0645cb, f7204f9, b4bc61c, each single-line with no attribution. Push succeeded first attempt, 628881c..b4bc61c, no rebase.

## Follow-up

Owner rulings 1-6 applied on the same branch. Guide 314 to 315 lines (cap 320).

| hash | message |
|---|---|
| 4c4f786 | doc: maintainers guide — gate verdicts, canon, re-cut record, draft fate, spec contents |
| abfb453 | chore: readme template points to entry gate |
| 48abccb | chore: regenerate README |
| ef8dd7b | doc: deferred items — attribution backfill open |

ef8dd7b is a fourth commit, outside the owner's three: it records the attribution backfill as OQ-006 and leaves the backfill open, per the ruling.

Push: succeeded first attempt, 0512d03..ef8dd7b; local and origin HEAD both ef8dd7bf44fa8c4dd22d32cf337f030194a729ae. 0512d03 (another agent's drafts/owned-lines SPEC.md) was already on origin. `just readme` exit 0, 12 manifestos, README diff 1 insertion, 5 deletions.

Rulings to guide:
1. Gate test 1 reads "at least one axiom ... VERIFIED"; further axioms may be QUALIFIED and carry their limit inside the manifesto. Closes Open 5.
2. Species table: canon is not counted when checking held ground, needs no axiom, and its attribution requires the year. Gate test 3 repeats the held-ground exemption. Closes Open 2.
3. A re-cut without a draft goes in `orchestration_log/history/<date>/recut-<file>.md`. Closes Open 3.
4. Stage 6 archives `drafts/<slug>/reviews/` under `orchestration_log/history/<date>/reviews/`; the ship commit deletes `drafts/<slug>/`. Closes Open 6.
5. README.template.md "Adding a new manifesto" is one line pointing to the entry gate; README regenerated. Closes Open 7.
6. Stage 3 states the SPEC.md contents list. Closes Open 4.

Open after follow-up:
1. `<file>` in `recut-<file>.md` is read as the manifesto's file name without `.md`. A re-cut touching several files has one record file; its name is undecided.
2. The ship commit deletes SPEC.md with the rest of `drafts/<slug>/`; only `reviews/` is archived. A re-cut recorded in that SPEC.md survives in git history alone.
3. conventions.md and codebase_state.md do not yet name `history/<date>/reviews/` or `recut-<file>.md`.
4. The ship commit command stages `drafts/<slug>/` with `git add -A`; stage 6 assumes the draft directory is tracked.
5. Attribution backfill stays open as OQ-006 (Open 11 and 14 of the first report stand).

## Follow-up 2

| hash | message |
|---|---|
| 79b4954 | doc: guide and conventions — ship archive paths, re-cut record name |

One commit holds MAINTAINERS_GUIDE.md (315 lines), conventions.md, and codebase_state.md. Push succeeded first attempt, ef8dd7b..79b4954; local and origin HEAD both 79b495407e4ced0788dcd533f71304804d01610b.

Rulings applied:
1. At ship, `SPEC.md` and `reviews/` move to `orchestration_log/history/<date>/<slug>/`; draft versions are deleted. Closes Follow-up Open 2.
2. The re-cut record is `orchestration_log/history/<date>/recut-<slug>.md`; `<slug>` names the cut, for one file the file's base name. Closes Follow-up Open 1.
3. conventions.md (File Naming, Orchestration Log Structure) and codebase_state.md (tracked list) name both paths. Closes Follow-up Open 3.
4. Stage 6 stages explicit paths, never `git add -A`. Closes Follow-up Open 4.
