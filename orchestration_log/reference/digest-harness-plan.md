# Digest test harness plan

As built, 2026-10-12. The plan this file held said "Not started" and listed six items in dependency order; this record replaces it. Each item gives the plan's wording in one line, what was built, and the difference. The process is described by ten skills and the tool is `tools/digest-eval/` (both in `codebase_state.md`). Facts are read from the repo, `pi --help` and the 2026-10-12 files under `orchestration_log/history/`; an item marked unverified was not checked. Updated in place in the turn a fact changes. Corrected 2026-10-13 after two independent checks (`orchestration_log/recon/2026-10-12/reference-verify.md` and `reference-verify-2.md`, gitignored). A fact that changes with a commit carries the time it was measured (2026-10-13, 10:05 to 10:07 UTC, `HEAD` `e21d6b1`).

## 1. Access point

**Plan.** One command, `ask <system-file> <user-file>`, prints one reply; a session form takes a transcript file; every run records model id, quantisation and sampling settings.

**Built.** `tools/digest-eval/digest_eval/readers.py`: a `Reader` interface and one adapter, `PiReader`. It calls `pi -p` with tools, context files, skills, extensions, MCP, prompt templates and themes switched off, `--model <model>` (the Petro series uses `long`, the 9B tier), the condition text appended through `--append-system-prompt` (pi's standard system prompt stays, by owner ruling), `--no-session` for a single reply or `--session-dir` and `--session-id` for a session turn, stdin from `/dev/null`, a 900 s timeout and two attempts, and a leaked `</think>` draft cut off. The spec's `reader` field names the adapter and model.

**Difference.** No `ask` command exists; the tool's entry is `digest-eval run` over a whole cut (item 4). A session is a script of turns held under one session id, not a transcript file. A reply record's `reader` field holds the adapter and model only, `{"adapter": "pi", "model": "long"}`: no quantisation, no sampling settings. The quantisation sits in the model file name (`Qwen3.5-9B-UD-Q4_K_XL.gguf`, `events.md`), in no record. `pi --help` lists no seed or temperature flag, so sampling is unseeded and cannot be fixed or recorded.

## 2. Judge access

**Plan.** A big model behind an API the script can call; a second one for the final gate. Owner picks.

**Built.** `digest_eval/judges.py` and `digest_eval/script_judge.py`, three judges:

- `AgentJudge`: Claude agents dispatched by an orchestrating session (skill `judge-by-agents`). `digest-eval blind` writes packets and a key, `digest-eval brief` renders one brief per packet, one agent per packet writes `judge/<packet>.verdict.json`, `digest-eval collect` validates the files against the key. The series' configuration is named in `spec.json` (Petro: `sonnet-agents` with `judge_brief.md`).
- The script judge: `digest-eval script-judge` counts the scripted demands (regex, sentence length) and checks answer keys.
- `SystemOneJudge`: a stub for a decision-only model served at `POST /v1/systemone`; it raises `NotImplementedError`, and its test checks the interface only.

**Difference.** No API the script calls: the tool calls no judge model, and an orchestrating session launches the agents. One judge configuration per series, no second judge for the gate (the gate is arithmetic over the scores, item 6), no headless API judge. System-One has no model integration. A judge-path test against a local `llama-server` on port 4150 was ordered 2026-10-12 at 20:16 UTC; no result file existed at the 2026-10-12 check, and its notes now sit at `orchestration_log/recon/2026-10-12/llama-server-judge-path.md` (gitignored; listed 2026-10-13 09:51 UTC). Its findings are the peer's claims in `events.md` (2026-10-13 about 09:40 UTC; `events.md` corrects its own 09:55 estimate, and the note file's mtime is 09:39:19 UTC, `stat` at 10:06 UTC): `/v1/systemone` on the generative 9B answers HTTP 501 "This model is not a decision model", first-token probabilities are usable, a real decision model is untested; I did not re-run them. The pilot mixed judge models (six opus agents, one sonnet), the flaw behind the one-configuration rule.

## 3. Tasks

**Plan.** `tests/<slug>.yaml`, prompts per manifesto, an iterate set and a gate set no cut is tuned against, written from the full texts, owner reviews.

**Built.** `evals/<slug>/tasks.json`, read by `JsonTaskSource`: `singles` (`id`, `family`, `split` `dev` or `test`, `message`, `answer` regex or null) and `sessions` (`id`, `split`, `turns`). Written from the demand list `evals/<slug>/demands.md` through the skills `write-eval-tasks` and `write-eval-record`: a family per demand a task can tempt, answer keys on substance, sessions for drift, a split by family with every family in both splits. `dev` is read between cuts and `test` only by the gate. The Petro series: 23 singles in 9 families (11 dev, 12 test), each family in both splits, and 2 sessions of 8 turns, one per split (read from its `tasks.json`).

**Difference.** JSON, not YAML; under `evals/<slug>/` (gitignored), not `tests/`; one set per series, a manifesto or a stack, not per manifesto; written from the demand list, not from the full text directly. The owner ruled the task source a don't-care (`events.md`); no owner review is recorded (unverified).

## 4. Runner

**Plan.** For a slug and a cut: every condition, task and sample through the access point; replies under `tests/runs/<slug>/cut-<n>/` with a manifest; plus the ten-turn session.

**Built.** `digest-eval run <slug> <run-dir>` (`runner.py`), after `digest-eval conditions`. Serial, one reader per invocation; resumable (a reply whose file exists is skipped); the condition order rotates per repeat. Replies are `runs/<cond>/<task>/r<rep>.json` and `runs/<cond>/<session>/t<NN>.json` under `evals/<slug>/cut-<n>/`; `progress.log` records each reply and ends with `DONE` on both paths: the `sessions=False` path writes it before its early return (`runner.py:33-35`, working tree, re-read 2026-10-13 10:05 UTC; `git status` then listed `M runner.py`, so the fix stays uncommitted until the next commit, together with its regression assertion in `test_digest_eval.py`), and the command also prints `DONE <run dir>` (`cli.py:53`). The independent verification of 2026-10-13 found that a no-sessions run never wrote `DONE`, so an `until grep -q DONE progress.log` wait would hang. Conditions: `none`, `digest`, `full`, `terse`, `placebo`, optional ablations.

**Difference.** The path is `evals/<slug>/cut-<n>/`, not `tests/runs/`. The manifest is `progress.log` plus the `runs/` tree (and `key.json` once blinded); no manifest file exists. Session length comes from `tasks.json`: 8 turns in the Petro series, 16 in the pilot, not ten. Petro cut 1 (195 replies) took about 1h48 from its resized restart (17:35 UTC) to `DONE` at 19:23:07.

## 5. Judge prompt and scorer

**Plan.** Judge bound to the full manifesto; replies shuffled with the condition hidden; two fields per reply, violations and task done; scores saved beside the replies; calibrate on ten owner-labelled replies before trusting it.

**Built.**

- `evals/<slug>/judge_brief.md`: placeholders `{PACKET}`, `{OUT}`, `{MANIFESTO}`, `{DEMANDS}`; opens with an order to bind to the manifesto through `manifesto-oath`; names no condition.
- `digest-eval blind`: one packet per task under random five-character reply ids; `key.json` at the run dir root, never under `judge/`. `digest-eval collect` validates the verdicts.
- `digest-eval score` (`score.py`): rows per reply, means per condition and per demand, paired differences with bootstrap intervals, drift slope; `scores.json` beside the replies.
- Calibration through the skill `calibrate-eval-judge`, recorded as `evals/<slug>/calibration.json` (Petro, read 2026-10-13 09:51 UTC). The sample is 12 replies in two packets, violations planted by fable: `calib` (8 replies, 14 planted demands) and `calib2` (4 replies for `d35-names`, after that demand's text was amended to count distinct literals); two sonnet runs per packet; the acceptance level (mean absolute difference at most 0.5 per demand, self-difference at most 0.5, done agreement at least 0.875) set before rating. `calib` missed `d35-names` (mean absolute difference 0.75 in run A against the 0.5 bound); `calib2` met the level (0.5 in both runs, self-difference 0.5); accepted.

**Difference.** A verdict carries `id`, `violations`, `done`, `notes` and a per-demand `demands` map, not two fields; the scripted demands and answer keys are counted by script, not by the judge. The calibration reference is planted violations (owner ruling, `events.md`), not ten owner-labelled replies; 12 replies, not 10; no human rater. Recorded limits: the judge over-counts unplanted breaches (scale about 2.1 against the planted totals), and planted violations cannot measure false positives. The record's own deviation from `calibrate-eval-judge`: `calib2` is a fresh sample for the missed demand only, not a full fresh sample, and its `brief_sha256` field reads "see ledger entry; the brief is unchanged since calibration" rather than a hash. The `calibrate-eval-judge` skill still names the owner or two stronger-model agents as the reference raters, so skill and practice differ.

## 6. Gate

**Plan.** Reads the scores, prints the three comparisons with the numbers, says pass or fail. Committed per cut.

**Built.** `digest-eval gate <slug> <run-dir>` (`gate.py`): reads `scores.json` and the spec's thresholds (`split`, `ci`, `min_cut_vs_none`, `margin_vs_full`, `completion_margin`, `drift_margin`) and writes `gate.json` with `pass`, one entry per check and `changed_vs_previous`. Up to six checks, each present when its baseline exists: cut vs none (mean difference at or below the threshold, interval excludes zero), near full, beats terse and beats placebo (interval below zero), completion (the digest's done rate at or above the better of the `none` and `full` done rates less the margin, `gate.py:35`, committed and unchanged at 2026-10-13 09:51 UTC), drift (slope against the full text). The gate reads the `test` split. `digest-eval ledger` appends one line per run dir to `evals/<slug>/ledger.jsonl`; `digest-eval stale` and `digest-eval reps` support the loop.

**Difference.** Six checks with confidence intervals, not three comparisons. The completion floor takes `none` and `full` only: `terse` and `placebo` done rates never enter it, while `write-eval-spec` says "the best baseline, a condition other than the digest", so skill and code differ. Records are no longer committed per cut: the owner ruled evals local-only (`events.md`), so the gate, scores and ledger stay in gitignored `evals/`, and each cut's findings are frozen as a dated report under `orchestration_log/history/<date>/` (`petro-cut-1.md`: five of six checks passed, "beats terse" failed). Read from the Petro ledger on 2026-10-13 at 10:05 UTC: cut 2 failed "beats terse", "beats placebo" and "drift", cut 3 those three and "completion", and the series stopped after cut 3 because cuts 2 and 3 both show `changed_vs_previous` false (reports `petro-cut-2.md` and `petro-cut-3.md`, first committed in `787eb4a`).

## Done when

**Plan.** "Done when one command from a clean checkout gives the same verdict twice."

**Found.** Scoring reproduces from stored records. `PilotReproduction` in `tools/digest-eval/tests/test_digest_eval.py` scores the tracked fixture `tests/fixtures/pilot-1/` and gets the pilot's stored numbers (8.39, 1.61 and 1.11 violations per reply; done 17, 18 and 17). The bootstrap is seeded (20261012), and `gate` is a pure function of `scores.json` and the spec, tested on synthetic scores, not on the fixture. The full pipeline does not reproduce: the reader is unseeded (`pi` has no seed or temperature flag), agent judges vary (self-difference 0.38 and 0.5 per demand in the Petro calibration), and `evals/` is gitignored, so a clean checkout holds the fixture and no other record. One command from a clean checkout cannot give the same verdict twice.

**Intended replacement.** Test-retest: run one cut twice end to end (same digest, spec, tasks, reader and judge configuration; fresh replies and fresh verdicts) and require the same gate verdict. Not yet run. The agreement bound on the numbers is fixed in no file (unverified).
