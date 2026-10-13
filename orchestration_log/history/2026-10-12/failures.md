# Failures: 2026-10-12

One entry per failure diagnosed: what happened, the mechanism, the correction. Times are UTC and approximate.

## A backgrounded reader call hung for 14 minutes (about 15:05 to 15:19)

**What happened.** A `pi` probe with the digest appended produced no output and no request reached the llama-server. The process sat asleep.
**Mechanism.** In a background shell stdin is an open pipe, and `pi -p` waits on stdin. With stdin from `/dev/null` the same call returned in 12 s.
**Correction.** The probe was killed and rerun with stdin closed and a 240-second cap; the harness and the `digest-eval` tool pass `stdin` as `/dev/null`. — witnessed by Claude (orchestrator), 2026-10-12

## My messages interrupted `srp-substrate`'s permission prompt and I reported it as an owner decision (about 16:40)

**What happened.** `srp-substrate` asked to launch a sonnet worker to adjudicate nine contested frames. Two unrequested messages of mine, a stop of one of its workers and a clarifying note, reached it after it had asked. The interruption registered as a decline. I told the owner they had declined, recommended the declined option, and built a three-option summary on it. The owner said they had not declined.
**Mechanism.** A message from me landing mid-prompt dismisses the prompt. The agent then read the dismissal as the owner's refusal.
**Correction.** One correcting message voided the decline and asked the agent to re-issue the launch, with a promise to send nothing until its final report. — witnessed by Claude (orchestrator), 2026-10-12

## Misread "eval lane only, not SRP" as an order to leave SRP (about 16:30)

**What happened.** I stopped supervising `srp-substrate` and deleted its check-back. The owner said they had not asked to abandon SRP.
**Mechanism.** I read a rebuke about steering as a change of scope.
**Correction.** The SRP watch was restored and both lanes stayed mine. — witnessed by Claude (orchestrator), 2026-10-12

## Wakes were set from a clock estimate that ran ahead of the machine clock (repeatedly, 15:20 to 17:10)

**What happened.** I planned wakes for times the machine had not reached, replaced them several times, and left prompts naming runs that had finished; the first check-back fired late and its instructions were stale.
**Mechanism.** I estimated the time from the length of my own work instead of reading it.
**Correction.** `date` is read before each wake is set, and a wake's prompt is rewritten whenever the set of pending runs changes. — witnessed by Claude (orchestrator), 2026-10-12

## Pilot cut 1 was reported as a gate pass on an unsound instrument (about 15:45 to 16:10)

**What happened.** The digest passed the three checks I had fixed in `gate.md`. The thresholds were my own, the single-task packets used opus judges and the session packet a sonnet judge (full-text score 1.11 against 4.40), the rubric was written mid-run, and completion was judged by an LLM that marked replies done despite a broken method and a wrong `git reset` claim. There were no placebo or one-line controls, three repeats per cell, and one session per condition.
**Mechanism.** The harness was built to produce a verdict before the instrument was fixed.
**Correction.** The result is recorded as a pilot with its flaws in `evals/stop-yapping/pilot-1/README.md`, and the plumbing was rebuilt as the `digest-eval` skills and tool. — witnessed by Claude (orchestrator), 2026-10-12

## The project's own records were not read before building (found at init, about 17:25)

**What happened.** The harness was built without reading `orchestration_log/reference/digest-harness-plan.md` (the project's plan for this harness) or the 2026-10-11 session record, and `memento:init` was not run at the start of the span.
**Mechanism.** The span started from a skill invocation and went straight to work.
**Correction.** `memento:init` was run at about 17:25; the plan's staleness and the missing charter are recorded in `events.md`. — witnessed by Claude (orchestrator), 2026-10-12

## Decisions were left to the owner in chat text the owner does not read (about 16:00 to 17:05)

**What happened.** I listed open decisions "for you" in replies. They stalled, and the owner said they read none of the conversation and that nothing is ever theirs to chase.
**Mechanism.** I assumed the owner read the conversation.
**Correction.** Decisions I can take, I take and report; a decision that blocks goes through the prompt tool. — witnessed by Claude (orchestrator), 2026-10-12

## The handoff brief carried five defects, three of them claims I did not re-check (found by the sibling at about 19:55)

**What happened.** The brief said "not pushed" (the five slice commits were on `origin/main`), that the scripts were "byte-identical to the originals" (a later label cleanup had edited them), that six files held scratch paths (twenty did), that the entry gate sat in `MAINTAINERS_GUIDE.md` (absent on `main`, reverted on the 2026-10-11 branch), and that audio hashes sat in the frames indexes (video hashes do; audio hashes are in the provenance files).
**Mechanism.** I repeated a statement from my own earlier summary without reading the remote-tracking ref; I verified the scripts before the rename edited them and did not verify again; I searched a subset of paths for the scratch path, and `grep -r` in this shell is a function that skips files a `.gitignore` hides, so its "zero" counts were blind to a folder that ignores everything but three files; I cited a gate from a session record without opening the guide.
**Correction.** A corrections section was appended to the brief with each item re-checked; searches over ignored folders use `find -exec grep`; a claim of a complete list now names its command. — witnessed by Claude (orchestrator), 2026-10-12

## A fable agent drove the whole iteration loop (found by the owner at about 20:40)

**What happened.** I dispatched `instruction-writer` (fable) to write the skills and tool, then handed it the first live series, and it ran the loop end to end: reader runs, judge launches, scoring, gates, diagnosis and re-cuts, five waits on its own monitor, over about three hours. The owner called it egregious misuse.
**Mechanism.** I scoped the agent by the people who knew the code, not by the role: a writer's tier ended up doing orchestration, the work the dev cycle assigns to a sonnet suborchestrator, and the series waited on a monitor that failed twice.
**Correction.** The agent is landed gracefully (no mid-write kill, tests passing, a handoff file), and a sonnet suborchestrator drives the loop under a written brief; fable stays on call for writing tasks only. — witnessed by Claude (orchestrator), 2026-10-12

## The guard on the judge-path test counted an unrelated process, and the series lost its landing to the session limit (found 2026-10-13 about 09:36 UTC)

**What happened.** I told `llama-jev-recon` to send requests only while `pgrep -x pi` was 0. An interactive `pi` (pid 92242, cwd `/Users/ryzhakar`, not a reader) was alive from about 20:54 UTC, so the guard could not open; the run had already stalled at 20:31. Separately, the account session limit stopped `instruction-writer` before it read my landing order, so no `HANDOFF.md` exists and the cut-3 reader's output sat unjudged for 12 hours.
**Mechanism.** I named the reader by the process name alone, which any interactive `pi` shares; and I ordered a graceful landing from an agent whose quota I could not see.
**Correction.** Guards identify the reader by its arguments (`pgrep -f 'pi -p'`); the series driver's brief reconstructs state from the series directory's files instead of a handoff; a landing order goes with a fallback state description. — witnessed by Claude (orchestrator), 2026-10-12
