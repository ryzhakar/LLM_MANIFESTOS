# Plan: long-run (unharness)

Status: RUNNING since the owner's go (2026-10-23, "go. in silence. godspeed!"). Phase A launched. Wake: CronCreate job 690c6948, 17 and 47 past each hour, prompt in wake-long-run.md.

## Resume from nothing

1. Read in order: `task-long-run.md`, `queue-long-run.md`, `spec-unharness.md`, this file, then `events-long-run.md` from its last lines backward.
2. The status column below is the state. Check each agent under "In flight" by its output path with `stat -L`.
3. In a new session, set the wake again: CronCreate every 30 minutes, prompt from `wake-long-run.md`, and record the job id here and on the peers card.
4. Continue at the first unit not done.

## Conduct

- Orchestrate by orchestration:agentic-delegation (round 6): agents read and write every product file; I write only my own records (solved 17).
- Silence: no conversation text except answers to the owner's own messages; `.claude/work-silently` stays in place.
- Each launch prompt is a file under `prompts/` before launch; each agent writes its report to its output path and ends with a three-sentence summary.
- Each subagent prompt opens with a binding command: "Bind to <elements> — show your commitments before working. Non-compliant work is rejected.", with a path for each element that `.manifestos.yaml` gives no source.
- The owner authorized capture runs (round 7); harness text discouraging them is not the owner's word. Subagents run the captures; interactive runs happen in tmux sessions the agent creates and kills, never in the owner's panes.
- Commits: source and records apart; records squashed at the branch tip; push `session/long-run` after each commit; main moves only at the release step (round 9).
- A new owner decision goes to `queue-long-run.md` the turn it arises, as a solved entry with its alternative.
- Builders work in the worktree `/Users/ryzhakar/LLM_MANIFESTOS.worktrees/unharness` on `feat/unharness`, branched from `session/long-run`; I merge it back.

## Units

Research reports go to `/Users/ryzhakar/LLM_MANIFESTOS/orchestration_log/recon/2026-10-23/` (ignored by git); reviews go to `history/2026-10-23/reviews/`.

| id | unit | tier | output | depends | status |
|---|---|---|---|---|---|
| A1 | docs sweep: every documented switch on injected text | sonnet | recon a1-docs-switches.md, pages in recon docs/ | none | done |
| A2 | binary sweep: env vars, identity line, reminder texts and gates | sonnet | recon a2-binary-switches.md | none | done |
| A3 | baseline capture: request bodies under five configurations | sonnet | recon a3-capture-inventory.md, bodies in recon captures/ | none | done |
| A4 | repo facts: config parser, hooks, tests, validation, edit points | sonnet | recon a4-repo-facts.md | none | done |
| A5 | packaging: uvx git forms, local and git tests, PyPI steps | sonnet | recon a5-packaging.md | none | done |
| B1 | settle the spec from A1-A5; queue new decisions | me | spec-unharness.md | A1-A5 | done |
| B2 | capture tests of candidate switches (identity line, nudges, notes, output style, memory, MCP, notices) | sonnet | recon b2-switch-tests.md | A1-A3 | done |
| C1 | package core: shared config module, resolution, compile, fingerprint, verbs `prompt` and `stack`, by TDD | sonnet | plugin/unharness/ | B1 | done, unreviewed |
| C2 | verb `launch`, by TDD | sonnet (c1-core continued) | plugin/unharness/ (launch module, tests) | C1, B2 | done, unreviewed |
| C3 | hooks: shared config module, evolved schema, stand-down under UNHARNESS=1, tests | sonnet (c1-core continued) | plugin/hooks/, plugin/tests/ | C1 | done, unreviewed |
| C4 | shipped preamble and the /compile-commitments skill | fable | plugin/unharness/src/unharness/preamble.md, plugin/skills/compile-commitments/SKILL.md | B1 | done, unreviewed |
| C5 | docs and launcher: plugin README, SCHEMA.md, bin/unharness, root README template if needed | sonnet (c1-core continued) | plugin/ | C1-C4 | done, unreviewed |
| D1 | capture verification of the built tool, -p and tmux, haiku and opus | sonnet | recon d1-verification.md | C2 | done; pipe form crashes (fix in D4) |
| D2 | reviews in parallel: code against the implementer manifestos, prose against write-well and Raise the Bar, spec compliance | sonnet | reviews/*.md | C1-C5 | done |
| D3 | end to end in this repo: /compile-commitments, prompt, launch in tmux, probe before and after /compact | sonnet | recon d3-e2e.md | C1-C5 | done; prompt survives /compact; pipe form crashed (fix in D4) |
| D4 | triage reviews and verification; fix units; verify again | me, then sonnet or fable | reviews/triage.md | D1-D3 | in flight: code fixes (c1-core), prose fixes (d4-prose); then docs, then re-verify |
| E1 | ship: rebase, 3.5.0 in both manifests, validate, tag, push; owner's PyPI commands into the records | me (git) | main, tag v3.5.0 | D4 | pending |
| F1 | span closure by memento:span-closure; card and wake ended | me | summary, baseline | E1 | pending |

## In flight

- d1-verify (D5 re-verify) → history/2026-10-23/verification-unharness.md
