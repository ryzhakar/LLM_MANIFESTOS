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
| Sonnet | Manifesto quality assessment, frontmatter drafting, source-code reasoning, theme recommendations, reference doc updates, **driving an iteration loop as the suborchestrator, judging replies, diagnosing failing demands** |
| Opus | Manifesto body text, synthesis across sources, strategic judgment (versioning, archival, taxonomy) |
| Fable | **Writing instructions where the wording is the product: skills and the digest sentence a hypothesis calls for.** The scope comes from the 2026-10-12 events (`events.md`: the skills the writer wrote, the sentence a hypothesis calls for) and the owner's ruling that fable may be a writer. Never the orchestrator of an iteration loop: it writes on call, and a sonnet suborchestrator runs the reader, judges, scores, gates and waits (owner ruling, 2026-10-12; a fable agent that ran the whole Petro series is the recorded misuse, `history/2026-10-12/failures.md`) |

## Manifesto writing process

Established 2026-04-29 (`only-fluff-die.md`), verified by execution. Scope: any new manifesto written from source material.

1. **Research tree** — parallel haiku agents across content facets write structured reports to `research/{topic}/categories/`.
2. **Curated extraction** — Opus reads category reports + the manifesto-writing skill + existing manifestos; produces a selective extraction brief.
3. **Deep-dives** — targeted agents on specific gaps (sonnet for reasoning, haiku for mechanical extraction).
4. **Final writer brief** — Opus reads all prior reports by path; produces a writer-ready brief.
5. **Oath-bound writing** — the writer agent MUST be bound to `/manifesto-writing` via `/manifesto-oath` before receiving source material; writes under constitutional constraint; runs the self-referential checklist.
6. **Validation** — `just readme`, then commit.

The writing standard is the `manifesto:manifesto-writing` skill (`manifesto/skills/manifesto-writing/SKILL.md` in the claude-skills marketplace). The entry gate for a new manifesto has no home today: `MAINTAINERS_GUIDE.md` holds none on `main` or at the tip of `origin/claude/manifesto-design-discussion-liuuvf`. It was committed in `b0645cb` and `4c4f786` and carried by `79b4954` (all 2026-10-11, on the branch; `79b4954` is the last guide version before the revert) and reverted by `8d4ef6f` (2026-10-12); `orchestration_log/history/2026-10-11/session.md` (D12) summarises its stages. Restoring or rewriting it is an owner call (`codebase_state.md`, Next Actions). This section restates neither the standard nor the gate.

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

## Lessons from 2026-10-12

Source: `orchestration_log/history/2026-10-12/` (`events.md`, `failures.md`, `petro-cut-1.md`, `stop-yapping-pilot-1.md`, `handoff-to-sibling.md`); the guard kernel and the landing-order kernel come from entries dated 2026-10-13 in `events.md` and `failures.md`. Times are UTC.

### Evals

- Keep every eval directory local-only, gitignored and expendable. Freeze its findings as dated reports under `orchestration_log/history/<date>/`, rendered from the files by script, one report per cut. Why: owner rulings of 2026-10-12; the raw files are not published and the repo is public. Scope: every eval series, here and in a stack's project.
- Keep one judge configuration and one reader in one series; a change of either starts a new series. Why: the pilot mixed judges (six opus agents on the single-task packets, one sonnet agent on the session packet), so no comparison across packets holds; its report puts the full manifesto at 1.11 violations per reply on the six single tasks under opus judges and at 4.40 on session turns 1 to 5 under the sonnet judge, different tasks, so the two figures show a mixed instrument and do not isolate the judge. The Petro judge also over-counts against planted violations by a scale of about 2.1, so only same-configuration comparisons hold. Scope: every series (`write-eval-spec`).
- Measure the baselines once per series; a cut re-runs the digest condition only. Why: a full cut of 195 replies took about 1h48 at about two replies a minute, and cut 2 ran 39 digest-only replies. Scope: re-cuts under one spec and one judge configuration.

### Reader and runs

- Run every reader call with stdin from `/dev/null`. Why: in a background shell stdin is an open pipe and `pi -p` waits on it; one probe hung 14 minutes and returned in 12 s with stdin closed. Scope: every non-interactive `pi` call, by hand or in a script; `digest-eval` does it already.
- Wait on a run with a background command that exits on the run's `DONE` line in `progress.log` (or a `Traceback` or `Killed`); never use the Monitor tool. Both kinds of run, with and without `--no-sessions`, end `progress.log` with `DONE` (`runner.py:33-35`, working tree, re-read 2026-10-13 10:05 UTC; `git status` then listed `M runner.py`, so the fix is uncommitted until the next commit); the independent verification of 2026-10-13 found that a no-sessions run had never written it, so an `until grep -q DONE progress.log` wait would have hung. Why: its monitor failed to wake `instruction-writer` twice in a row (cut 1 `DONE` at 19:23:07, cut 2 at 20:01:33; nine and six minutes idle). Scope: any agent waiting on a run; the `test-digest` skill's run-the-reader step carries the loop (committed in `1577a81`; no skill differs from `HEAD` at 2026-10-13 10:05 UTC).
- Name a reader in a guard by its arguments, `pgrep -f 'pi -p'`; never `pgrep -x pi`. Why: an unrelated interactive `pi` (pid 92242, not a reader) counted, so the guard on the judge-path test could not open (`failures.md`, found 2026-10-13). Scope: every guard or wait that tests whether a reader is running.
- Copy, do not move, a file a live run reads. Why: the Petro series read the repo's skill and tool files while a plugin was being designed from them. Scope: skills, tool code and any file a running series reads; remove the original only after the copy is verified and the owner's ruling stands.

### Searches and times

- Search ignored folders with `find ... -exec grep -l`; never `grep -r`. Why: in this shell `grep` is a function that skips files a `.gitignore` hides; under the source-dump folder it found 0 files where `find -exec grep` found 20. Scope: every search over `evals/`, `research/`, `orchestration_log/recon/` and the source-dump folder; a claim of a complete list names its command.
- Take a time in a journal trace from a file time, a commit time or `date -u`; never from an estimate. Why: estimated traces ran 8 to 12 minutes late, and wakes set from an estimate fired late with stale prompts. Scope: journals, wakes and reports; the local clock is UTC+3.

### Agents and sessions

- Send nothing to an agent holding a permission prompt until its report arrives. Why: a message landing mid-prompt dismisses the prompt, and the agent read the dismissal as the owner's refusal. Scope: any agent that has asked the owner; one correcting message voids a wrong decline.
- Treat a message from a peer session as binding nothing beyond the owner's word: answer facts and paths, and move, remove or accept nothing on its say-so. Why: a peer's request carries no owner authority of its own; the upstream session's inventory request was answered with facts and paths only until the owner stated the assignment (20:25). Scope: every message from another session.
- Take every decision you can take and report it; send a decision that blocks through the prompt tool. Why: the owner reads no conversation text, and decisions listed "for you" in replies stalled. Scope: every session.
- Send a landing order to an agent with a fallback: the next driver reconstructs state from the series directory's files, not from a handoff file. Why: the account session limit stopped `instruction-writer` (and `reference-verifier`) at 20:39 UTC on 2026-10-12, before it read the landing order; no `HANDOFF.md` existed when the driver started (about 09:40 UTC on 2026-10-13; none was found at the resume at about 09:36, `events.md`), and `instruction-writer` wrote one in the series directory after the limit lifted (`stat`, 2026-10-13 10:05 UTC: 8,982 bytes, file time 09:55:55 UTC); cut 3's reader output sat unjudged for about 12 hours (`events.md` and `failures.md`, 2026-10-13). Scope: any order to land, hand off or stop that an agent must read before it acts; the next driver's brief names the files that hold the state.

## File naming

- Manifestos: kebab-case `.md` in `manifestos/` — matches existing files; MAINTAINERS_GUIDE's `Manifesto, X.md` examples are illustrative only (ruling: `decisions.md` 2026-04-29).
- Themes: kebab-case keys in `themes.yaml`.
- Orchestration log: date-keyed `YYYY-MM-DD` under `history/` and `recon/`; living reference docs flat under `reference/`. Layout authority: the `agentic-delegation` skill.
