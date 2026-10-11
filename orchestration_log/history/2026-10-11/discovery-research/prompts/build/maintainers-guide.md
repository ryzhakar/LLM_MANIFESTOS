CONSTITUTION BINDING — do this before the task body. Load each element completely from source, run the binding protocol in element 3 (deconstruct, map convergence and tension, activate), write the binding as the first lines of your report, then proceed. You rebind from source on this dispatch.
1. First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md
2. Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml
3. Binding protocol — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md
4. Stop Yapping — /home/user/LLM_MANIFESTOS/manifestos/stop-yapping.md

ROLE: You are rewriting the collection's maintainer guide and its conventions record so they state the entry gate and the species the owner decided, as commands and facts, with nothing argued.

CONTEXT: Repository /home/user/LLM_MANIFESTOS, branch claude/manifesto-design-discussion-liuuvf (pull nothing; another agent may write under drafts/, do not touch it). Schema already shipped (commit 628881c and earlier): fields kind (manifesto|canon), register, reader; tagline ≤8 words except canon; themes trimmed to two. The plugin's writing standard now lives at /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md (read it whole; the guide points to it by name and repeats nothing from it).

OWNER DECISIONS (binding):
- Two species. `kind: manifesto` obeys the writing standard. `kind: canon` is a verbatim text kept for extraction, exempt from form rules, never counted against the entry bar, carries author and year in its attribution line.
- Entry gate, in order: substrate (2–11 primary texts, saved verbatim under resources/<date>-<slug>/ with an index) → discovery tree (ground-truth audits of the collection, surveys by focus not by source, verification of every axiom against the texts, a candidates report) → one verified axiom stated by ≥2 authors, one precise enemy, and ground the collection does not hold or can re-cut by named rows → spec → writer bound to the writing standard and a register reference → five unbiased reviewers plus a register reviewer and a maximalist self-pass → ship. The gate's artifacts for 2026-10-11 live under orchestration_log/history/2026-10-11/discovery-research/ and resources/2026-10-11-code-liability-and-dependencies/; cite them as the worked example.
- Drafts live under drafts/<slug>/ (SPEC.md, v1.md, v2.md, reviews/); generate.py scans only manifestos/, so a draft enters the collection only by moving to manifestos/.
- Re-cuts of existing manifestos are permitted when the resulting stack is sharper; a re-cut names the rows that move (file:line) and the held ground after; a re-cut that removes an enemy-section row bumps the major version, one that moves other rows does not.
- Versioning: major only; patch forbidden; the guide's own example text that shows `1.0.1` style edits is corrected.
- Attribution mandatory: "After [authors]" for transformed texts; "by [author], [year]" for canon.
- Register and reader are frontmatter facts; the guide names the enum values and says the writing standard chooses them.
- Theme rule unchanged (≥2 files per theme; differentiate within the collection).
- Policy without rationale: strip every sentence in the guide that argues for a rule or narrates what goes wrong.

INPUT FILES: /home/user/LLM_MANIFESTOS/MAINTAINERS_GUIDE.md, README.template.md, generate.py, themes.yaml, orchestration_log/reference/conventions.md, orchestration_log/reference/codebase_state.md, orchestration_log/reference/deferred_items.md, /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/collection-schema-report.md, /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/build-log.md, and the writing standard named above.

TASK:
1. Rewrite MAINTAINERS_GUIDE.md: keep its section order (Philosophy, Architecture, Roles, Workflows, Troubleshooting, Reference); replace Workflows' "Adding a New Manifesto" with the entry gate; add "Species" under Philosophy; add "Re-cutting an existing manifesto" under Workflows; correct the frontmatter schema in Reference to the shipped generate.py (read it); fix the file-naming examples to kebab-case (the conventions record says the `Manifesto, X.md` examples are wrong); strip rationale sentences. Keep under 320 lines.
2. Update conventions.md: the Manifesto Writing Process section points to the writing standard by name and keeps only the dispatch lessons that are not in the standard; add the schema facts; keep Forbidden Patterns, updated (PostCompact no longer exists in the plugin; drafts/ exists; patch versions forbidden, debt cleared).
3. Update codebase_state.md inventory (12 files with kind/register/reader; two themes; first-principles 1.0.0) and deferred_items.md (OQ-001 and OQ-002 resolved with the commit hashes from the schema report; add one open item per thing still deferred in build-log.md).
4. Commits, atomic, single-line, no attribution: `doc: maintainers guide — entry gate, species, re-cuts, schema`; `doc: conventions — writing standard by reference, schema facts`; `doc: reference — inventory and deferred items after schema change`. Push with retries (2s, 4s, 8s, 16s). If the push is rejected because the branch moved, `git pull --rebase origin claude/manifesto-design-discussion-liuuvf` and push again; never force.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/maintainers-guide-report.md

REPORT FORMAT:
(binding lines)
# Maintainers Guide rewrite
## Line counts — before, after, per file
## Rationale sentences removed — count, three examples
## Commits — hash | message
## Open

SCOPE: The four documents named. No manifesto body, no schema code, no drafts/.

TOOLS: Read; Edit; Write; Bash; Grep.

End with a 3-sentence summary for a notification: line counts, commits, push result.
