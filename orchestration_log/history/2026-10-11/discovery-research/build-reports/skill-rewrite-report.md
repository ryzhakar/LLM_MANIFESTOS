Loaded, full, from source: First Principles (manifestos/first-principles.md); Strunk SPR v3 (instructions/strunk_spr_v3_complete.xml, 2923 lines); oath protocol (claude-skills/manifesto/skills/manifesto-oath/SKILL.md); Stop Yapping (manifestos/stop-yapping.md); ETHOS (claude-skills/ETHOS.md); skill-writing standard (claude-skills/memento/skills/skill-creation/SKILL.md).
Converge: commands not suggestions; cut to verified atoms; no rationale; concrete, short, checkable.
Tensions → rules: standard's "prose and inline backticks only" vs owner "keep the table" → rows kept as one backticked command, examples as `Turn X into Y` commands. Stop Yapping fragments vs Strunk/standard full sentences → skill in full command sentences, report in fragments. ETHOS no-rationale vs manifesto stakes → skill carries none; manifestos keep stakes as declarations. "Full rewrite, never edit" vs "orchestrator edits register" → register mismatch = rewrite at fresh path; match = direct edit. "Bind to register reference before substrate" vs "choose register after enemy" → bind to requested register or `contemptuous`; rebind on mismatch.
I must state each owner decision as a command, and I will carry none as rationale. I must verify each spine hypothesis against the logs, and I will not inherit an unverified one. I must not exceed 2600 tokens, and I will not.

# manifesto-writing rewrite

## Tokens — before, after
1243 → 2363 (cl100k, `just tokens` recipe run by hand; `just` absent). Ceiling 2600. 163 lines, 68 command sentences. Each has exactly one `never`.

## Five core points — the spine you kept most prominent, each with its tag
1. Reader = model. Enemy = its own trained reflex, in its mouth, first line under the title. `<name-the-enemy-and-the-reader>`
2. Register by enemy type: `reflex`→contemptuous, `framework`→declarative, `environment`→parable. The test is where the reflex lives. `<choose-the-register>`
3. Bindable floor: at least 70% bindable lines (opens the tag), at most 5 one-sentence axioms, each tested VERIFIED/QUALIFIED/CONTRADICTED. Boundary stays, escape dies. `<build-the-structure>`, `<extract-from-the-substrate>`
4. Self-check: anti-Claude lexical/structural/tonal tells, counts measured rather than estimated, the draft passes its own rules, `Before you ship` section. `<run-the-self-check>`
5. Declare, never cite. A non-author rates every figure. UNVERIFIED or CONTRADICTED figures get struck. `<write-the-draft>`, `<review-the-draft>`

## Prompt-eval score — if run
Rubric: prompt-engineering/agents/prompt-eval.md (an agent, not a skill). Applied by hand.
Base: 39/48 = 81% (Good). MUST/MUST_NOT violations: 0. SHOULD met: 22. The formula's +1 per SHOULD overflows to 103, so the nominal score is 100 (capped).
Misses: STR-1 no role line, STR-5 procedure order instead of canonical, CLR-5 no numbers, CON-3, CON-4 (ETHOS forbids rationale), SAF-1, OUT-2 no full template, AGT-3, AGT-4 no allowed-tools.
N/A: TOOLS, DATA_SEPARATION, AGT-5, AGT-10.
Fixed during eval: CLR-3 (tense rule vs kept example; imperative scoped to commands), CON-1 (canon scope line), SAF-4 (substrate-as-data line).

## Commits — hash | message
e7ace90 | feat(manifesto-writing): practiced standard — model reader, register by enemy, bindable floor, self-check
879bc24 | doc(readme): regenerate for manifesto-writing
Branch `manifesto-writing-standard` pushed. The first push was 8ec924d. I amended it to fix CLR-3 and force-pushed with lease to my own branch. Remote = 879bc24.

## Open
- Transform table and the 3 examples are kept in content, as backticked command sentences rather than a Markdown table (the standard forbids non-prose inside tags). Owner: confirm or demand a literal table.
- The cut row "qualifications/caveats unless the point" is folded into the boundary/escape test.
- Dropped: Prerequisites ("sympathetic readers" contradicts the model reader), 1500–2500 length, present-tense rule (example 2 uses future). "Future promises" became "promises".
- Contemptuous floor 70/50/50 per 1000 words (`you`, ALL-CAPS, fragments) is my derivation from corpus-audit (stop-yapping 81.6/60.5/134.2; postgres 70.5/59.6/56.2), not an owner figure. Postgres clears `you` by 0.5.
- Added beyond the owner list, all from logs: identity attacks, profanity cap 3, close quoting the opening enemy line, reflex defeats its own goal (helpfulness paradox), requester escalation, theme must be shared, version 1.0.0 / major on thesis change (MAINTAINERS_GUIDE). Also added, not from logs: injection line, canon scope line.
- `Before you ship` is a literal heading. stop-yapping's "Before You Send" fails it.
- Spine check: the definition says "ten of twelve open on enemy"; corpus-audit counts 9. "Ends in choice in every transformed file" is false (dry and correct-by-construction add sections after the choice). The 70% target traces to a writer brief, not the logs. It stands on the owner decision.
- The skill assumes dispatch. Subagents lack the Agent tool, so it runs from the main session.
- plugin.json not bumped (scope). A minor bump 3.2.0→3.3.0 is likely due.
- Worktree /home/user/claude-skills-skill left in place. /home/user/claude-skills untouched.

Tokens 1243→2363 (ceiling 2600). Prompt-eval 81% base (39/48, 0 MUST violations; nominal 100 after SHOULD bonus). Branch manifesto-writing-standard pushed at 879bc24 (force-with-lease after an amend).

## Integration
Owner rulings applied: (1) Transform mapping back as the literal Markdown table inside `<extract-from-the-substrate>`. Examples unchanged. (2) Self-check heading now begins `Before you`, any capitalization. stop-yapping's "Before You Send" passes. (3) Contemptuous floor 70/50/50 kept. (4) Tokens 2363 → 2407 (under 2600).
1f314d1 | fix(manifesto-writing): mapping table and self-check heading rule | pushed to manifesto-writing-standard
c84a59b | merge: manifesto-writing standard into binding-channel | --no-ff onto b4e4bde, README merge clean
Regeneration after merge: no diff, so no `doc(readme): regenerate after merge` commit. plugin.json stays 3.3.0.
manifesto-binding-channel pushed b4e4bde..c84a59b, no force. Worktree /home/user/claude-skills-skill removed.
