# Codebase State

_Last verified: 2026-10-12 (first pass; `date -u` read 20:30 UTC), corrected 2026-10-13 after two independent checks (`orchestration_log/recon/2026-10-12/reference-verify.md`: 132 rows, 112 consistent, 9 contradicted, 11 uncheckable; `reference-verify-2.md`: 73 rows, 67 consistent, 2 contradicted, 4 uncheckable; both gitignored). A fact that changes with a commit carries the time it was measured. Measured by command on 2026-10-13 between 10:05 and 10:07 UTC at `HEAD` `e21d6b1`: `python3 -I tools/digest-eval/tests/test_digest_eval.py`, 13 tests, OK (10:05:45 UTC), on a working tree whose only uncommitted tool change was the `runner.py` `DONE` line and its regression assertion in `test_digest_eval.py` (13 test functions at that time), both since committed in `e7defef` (2026-10-13 13:09:02 +0300; `git diff HEAD --stat -- tools .claude` is empty at 15:03 UTC); read-only git (log, reflog, show, ls-files, ls-tree, check-ignore, status, diff, rev-list); `stat`, `shasum -a 256`, `tar -t`. The source-dump facts in Resources, the ahead count and `HEAD` were re-measured on 2026-10-13 between 15:00 and 15:01 UTC at `HEAD` `998256a` (`shasum -a 256`, `shasum -a 256 -c`, `stat`, `tar -t`, `git ls-files`, `git rev-list`). On 2026-10-12: `pi --help`. Read, not run: `generate.py`, `README.template.md`, `themes.yaml`, `config.yaml`, every manifesto's frontmatter, the justfile, `.gitignore`, the ten skills, the tool sources. Not run: `just readme`, `tests/check_skills.py`, any reader or judge. An item marked unverified was not checked._

---

## Manifesto Inventory

| File | Title | Tagline | Theme | Version |
|------|-------|---------|-------|---------|
| `cargo-cult-science.md` | Cargo Cult Science | "the first principle is that you must not fool yourself" | cognitive-science | 1.0.0 |
| `correct-by-construction.md` | Correct By Construction | "invalid states cannot compile" | software-engineering | 1.0.0 |
| `dry.md` | Knowledge Has One Home | "knowledge has one home" | software-engineering | 1.0.0 |
| `first-principles.md` | The First Principles | "atoms, not analogies" | cognitive-science | 1.0.1 |
| `intervention.md` | Trust Nothing, Restore Everything | "roots, not canopy" | cognitive-science | 1.0.0 |
| `kiss.md` | Decomplect | "incidental is Latin for your fault" | software-engineering | 2.0.0 |
| `lines-spent.md` | Lines Spent | "spent, not produced. yours, not theirs." | software-engineering | 1.0.0 |
| `postgres.md` | Respect the Engine | "you use 5% of what you bought." | software-engineering | 1.0.0 |
| `self-documenting-code.md` | Code Speaks | "comments are lies" | software-engineering | 1.0.0 |
| `simple-made-easy.md` | The Simplicity Manifesto | "the confusion is killing you" | cognitive-science | 2.0.0 |
| `stop-yapping.md` | Stop Yapping | "answer. shut up." | cognitive-science | 1.0.0 |
| `yagni.md` | Build For Today | "build for today" | software-engineering | 1.0.0 |
| `zen-of-python.md` | The Zen of Python | "refuse to guess" | software-engineering | 1.0.0 |

**Total:** 13 files. 8 software-engineering, 5 cognitive-science.

Frontmatter holds five fields: `title`, `tagline`, `version`, `theme`, `description`. The 2026-10-11 baseline listed `kind`, `register` and `reader` columns, a tagline word cap and `tests/test_generate.py`; none exists on `main` (no file carries the fields, `generate.py` has no such validator, `tests/` is absent). That work was committed on `origin/claude/manifesto-design-discussion-liuuvf` (`1fa3f28`, `4fdf61b`, tests `613f75f`, `531e955`) and reverted there by `3ae2a7e` (2026-10-12 03:52 UTC). `git log -- generate.py` on `main` lists `7d118d2` and `67542f2` only.

---

## Digests

`digests/` holds 13 files, one per manifesto, under the manifesto's own file name (`diff <(ls digests) <(ls manifestos)` is empty). All tracked. Each file is the body alone with no header (the `write-digest` skill's shape rule), 120 to 349 words, 3,382 in all: `zen-of-python` 120, `dry` 196, `first-principles` 216, `yagni` 243, `correct-by-construction` 248, `intervention` 251, `stop-yapping` 251, `self-documenting-code` 271, `cargo-cult-science` 275, `lines-spent` 301, `kiss` 317, `simple-made-easy` 344, `postgres` 349. Whether each digest still matches its manifesto's text is unchecked.

A stack digest, one text for several manifestos, is never saved here: it lives at `.claude/digests/<member slugs sorted, joined by +>.md` in the project that declares the stack. The only one is the Petro stack's (11 members) under `/Users/ryzhakar/petro/`: 849 words on 2026-10-13 at 10:05 UTC (848 at the 2026-10-12 check, 841 at cut 1).

---

## Skills

Ten skills in `.claude/skills/<name>/SKILL.md`, all tracked, each a set of tagged blocks of `rule; never ...` lines; first committed in `5e957ff`. At 2026-10-13 10:05 UTC no skill file differs from `HEAD` (`git status`). The edits after the pilot are committed: `test-digest/SKILL.md` in `1577a81` (a cut after the first runs with `--only digest`; the run is awaited by a background loop on `progress.log`; a series stops at the fifth cut; the conditions line takes `--manifesto <paths>`) and `judge-by-agents/SKILL.md` in `e21d6b1` (`blind --borrow`; unnamed agents launched in waves of at most twenty).

| Skill | Does |
|-------|------|
| `write-digest` | First cut of one manifesto's digest: every demand as one plain sentence, boundaries folded in, one standing line, body only, under 350 words, saved as `digests/<slug>.md`. |
| `write-stack-digest` | One stack's digest composed from its members' digests alone: converging demands merged, each tension replaced by one rule, under 850 words. |
| `test-digest` | One cut through the loop (ledger check, series prep, conditions, reader, judges, score, gate, ledger) and the decision to stop or diagnose and re-cut. |
| `recut-digest` | Applies one diagnosed change, one sentence or demand, to a digest and records the cut. |
| `write-eval-spec` | Turns the demand list into the frozen spec: per-demand script or judge check, conditions, reader, judge, gate thresholds. |
| `write-eval-tasks` | Writes the task set: families that tempt a demand, answer keys, sessions for drift, a dev/test split by family, repeats sized by `digest-eval reps`. |
| `calibrate-eval-judge` | Measures a judge configuration against reference raters on a blind sample and fixes it for a series. |
| `judge-by-agents` | Blinds the replies, renders one brief per packet, launches one unnamed agent per packet in waves of at most twenty, collects and validates the verdicts, runs the script judge. |
| `diagnose-eval-failures` | Reads the `dev` failures, names the one failing demand, writes the one-change hypothesis before the next cut runs. |
| `write-eval-record` | The fixed shape and place of every record under `evals/<slug>/`. |

---

## Digest-eval tool

`tools/digest-eval/`, standard-library Python (`TOOL_VERSION` 0.1.0), tracked since `63f3908`. It runs the mechanical stages of the eval loop. It calls no model except through the reader adapter; agents judge.

| File | Does |
|------|------|
| `digest-eval` | Shell launcher; follows symlinks to its real path, then `exec python3 -I cli.py "$@"`. |
| `cli.py` | The command line. `evals/<slug>/` resolves from the current directory. |
| `digest_eval/spec.py` | Validates `spec.json`; `JsonTaskSource` reads `tasks.json`. |
| `digest_eval/conditions.py` | Writes `conditions/<cond>.txt`: `digest`, `full` (members concatenated, frontmatter stripped), `terse`, `placebo` (a named source cycled to the digest's word count), optional ablations (the digest minus one sentence). `none` has no file. |
| `digest_eval/readers.py` | `Reader` interface; `PiReader`, the only adapter; strips a leaked `</think>` draft; 900 s timeout, two attempts, stdin `/dev/null`. |
| `digest_eval/runner.py` | Serial, resumable runner; appends `progress.log`, which ends with `DONE` on both paths: the `sessions=False` path writes it before its early return (`runner.py:33-35`, re-read 2026-10-13 10:05 UTC in the working tree, when `git status` listed `M runner.py` and `HEAD`'s early return had no `DONE`; committed since in `e7defef` (2026-10-13 13:09:02 +0300) and re-read at 15:03 UTC: lines 33-35 are `if not sessions:`, `log(run_dir, "DONE")`, `return`). The independent verification of 2026-10-13 found that a no-sessions run never wrote `DONE`, so an `until grep -q DONE progress.log` wait would hang; `digest-eval run` also prints `DONE <run dir>` to stdout. |
| `digest_eval/blinder.py` | Packets under random reply ids; `key.json` at the run dir root. |
| `digest_eval/judges.py` | `Judge` interface; `AgentJudge` (renders the brief, validates verdict files); `SystemOneJudge`, a stub that raises `NotImplementedError`. |
| `digest_eval/script_judge.py` | Counts the scripted demands (regex, sentence length) outside code blocks; checks answer keys for `done`. |
| `digest_eval/score.py` | Joins rows; means per condition and per demand; paired differences with bootstrap intervals (2,000 resamples, seed 20261012); drift slope; `reps_needed`. |
| `digest_eval/gate.py` | Applies the spec's thresholds; up to six checks. The completion check compares the digest's done rate with the better of the `none` and `full` done rates less the margin (`gate.py:35`, committed in `63f3908`; no diff against `HEAD` at 2026-10-13 10:05 UTC). |
| `digest_eval/ledger.py` | Builds ledger entries; the `stale` check. |
| `digest_eval/records.py` | Record shapes and paths, verdict validation, JSON helpers; `canonical_demands` maps a judge's shortened demand keys (`d07`) onto the spec's ids (`d07-exact`) (committed in `1577a81`; used by `validate_verdicts` and `score.join`; the 13th test covers it). |

### Command

`digest-eval <subcommand> <slug> [<run-dir>] [options]`; the subcommands, as `cli.py` defines them in the working tree:

| Subcommand | Does |
|------------|------|
| `conditions <slug> <run> --digest P --manifesto P...` | Writes the condition texts. |
| `run <slug> <run> [--reps N] [--split S] [--reader-model M] [--only C...] [--no-sessions]` | Serial reader run; resumes by skipping existing replies; prints `DONE <run dir>`. |
| `blind <slug> <run> [--seed N] [--borrow RUN]` | Writes packets and the key. `--borrow` fills the packets from an earlier run's other conditions (committed in `1577a81`). |
| `brief <slug> <run> <packet> --manifesto P` | Renders the judge brief for one packet. |
| `collect <slug> <run>` | Validates every verdict file against the key; exits 1 on any problem. |
| `script-judge <slug> <run>` | Writes `script.json`. |
| `score <slug> <run> [--previous RUN] [--baselines RUN]` | Writes `scores.json`. |
| `gate <slug> <run>` | Writes `gate.json`. |
| `ledger <slug> <run> --digest P --manifesto P... [--cut N] [--kind cut\|transfer\|pilot] [--member P...] [--reader-model M] [--hypothesis T] [--change T]` | Appends one line to `ledger.jsonl`. |
| `stale <slug> --digest P` | Compares the latest cut's ledger entry with the digest, the manifesto versions and the member digests on disk. |
| `reps <slug> <run>` | Repeats needed, from the spread of digest-minus-none differences; falls back to the script judge's counts when no judged pairs exist. |

`justfile` recipes (read 2026-10-12): `readme`; `install-digest-eval` (symlinks the launcher to `~/.local/bin/digest-eval`); `test-digest-eval` (`python3 -I tools/digest-eval/tests/test_digest_eval.py < /dev/null`). The launcher was not installed at the 2026-10-12 check and was still absent at 2026-10-13 10:06 UTC (`ls ~/.local/bin/digest-eval` fails; `command -v digest-eval` prints nothing).

### Tests

- `tests/test_digest_eval.py`: 13 offline tests (no agent, no model call): pilot reproduction, conditions, the `pi` command line, a fake-reader cut through runner, blinder, script judge, score, gate, ledger and `stale`, gate failure, spec validation, the System-One stub, repeats sizing, demand-key canonicalisation (`1577a81`), the symlinked launcher. The regression assertion on the `DONE` line of a no-sessions run in `Loop.test_cli_on_pilot_layout` (two added lines) is committed in `e7defef`; it was uncommitted at 2026-10-13 10:05 UTC.
- `tests/check_skills.py`: checks the skills against the mechanical rules of skill-creation (frontmatter, tag structure, one emphatic word and one command per sentence). Not run by me.
- `tests/fixtures/pilot-1/`: tracked, 110 files (`key.json`, `judge/`, `runs/`), a trimmed copy of the stop-yapping pilot's replies, key and verdicts. The test scores it and expects 8.39, 1.61 and 1.11 violations per reply for none, digest and full, and 17, 18 and 17 done.

---

## Evals

`evals/` is gitignored and local-only by owner ruling (2026-10-12): evals are expendable; their findings are frozen as dated reports under `orchestration_log/history/<date>/`. Here it holds `evals/stop-yapping/pilot-1/` only (the pilot). Layout of one series, `evals/<slug>/`, per the `write-eval-record` skill and `records.py`: `spec.json`, `tasks.json`, `judge_brief.md`, `demands.md`, `resolutions.md` (stacks), `calibration.json`, `ledger.jsonl`, one run dir per cut `cut-<n>/` (`conditions/`, `runs/`, `key.json`, `judge/`, `script.json`, `scores.json`, `gate.json`, `hypothesis.md`, `cut.json`) and `cut-<n>-<model>/` for a transfer run.

A stack's evals live in the project that holds the stack digest, not in this repo. The first series, the Petro stack, is at `/Users/ryzhakar/petro/evals/<slug>/` (the slug is the member names joined by `+`). Listed on 2026-10-13 at 10:05 UTC: `spec.json` (39 demands, reader `pi` on `long`, judge `sonnet-agents`, 1 repeat), `tasks.json` (23 singles in 9 families, each family in both `dev` and `test`; 2 sessions of 8 turns, one per split), `judge_brief.md`, `calibration.json`, `calibration/` (`acceptance.json`, `agreement.json`, `key.json`, `reference.json`, `reference2.json`, `judge/`), `demands.md`, `resolutions.md`, `placebo.md`, `HANDOFF.md` (8,982 bytes; none existed when the series driver started at about 09:40 UTC; `instruction-writer` wrote it after the session limit lifted, file time 2026-10-13 09:55:55 UTC), `ledger.jsonl` (3 lines; 1 at the 2026-10-12 check), and the run dirs `cut-1`, `cut-1-aborted`, `cut-2`, `cut-3`. Each run dir also holds `progress.log`, `run.stdout`, `cwd/` and `sessions/` (`cut-1-aborted` has no `sessions/`). That folder has no `.git`.

Outcome of the Petro series, read from the ledger on 2026-10-13 at 10:05 UTC: no `cut-4` exists; the series stopped after cut 3, on the `test-digest` stop rule (two cuts in a row with `changed_vs_previous` false: the ledger holds false for cuts 2 and 3; `events.md` names the rule). Failed gate checks on the test split: cut 1 "beats terse"; cut 2 "beats terse", "beats placebo" and "drift"; cut 3 those three and "completion". Digest words per cut: 841, 848, 849.

Frozen reports under `orchestration_log/history/2026-10-12/`: `stop-yapping-pilot-1.md` and `petro-cut-1.md` (first committed in `2dcd1d4`), `petro-cut-2.md` and `petro-cut-3.md` (first committed in `787eb4a`, 2026-10-13). The raw eval data is archived outside git: `/Users/ryzhakar/archives/petro-evals-2026-10-12.tar.gz`, 1,497,598 bytes, written 2026-10-13 12:54 local (09:54 UTC), 832 files under `petro/` and `LLM_MANIFESTOS/evals/` (`tar -t`, 2026-10-13 10:07 UTC), with a `.sha256` sidecar; `shasum -a 256` of the archive at 10:05 UTC equals the sidecar, `5ced9e4078a91113823ccdda252b7d0c1e24dcd9b665d5612e3c1ff7cece0c2e`.

---

## Resources

`resources/` is tracked and not scanned by `generate.py`. Two folders:

- `2026-10-11-code-liability-and-dependencies/`: 190 tracked files, verbatim sources and indexes.
- `2026-10-12-source-dump/`: tracked as 15 files at 2026-10-13 15:00 UTC (`git ls-files -- resources/2026-10-12-source-dump`): `README.md`, `index/MANIFEST.sha256`, a folder `.gitignore` and 12 build scripts under `scripts/build/`, added by commit `998256a` ("keep the source-pull build scripts in the dump"); the process document `orchestration_log/history/2026-10-13/source-pull-process.md` carries their detail. The folder `.gitignore` ignores everything else (`/*`, then `!/.gitignore`, `!/README.md`, `!/index/`, `/index/*`, `!/index/MANIFEST.sha256`, `!/scripts/`, `/scripts/*`, `!/scripts/build/`). Of 299 files on disk, 284 are local-only; the manifest has 298 lines and all 298 pass `shasum -a 256 -c` (15:01 UTC). The content lives in a hashed archive outside git, `/Users/ryzhakar/archives/2026-10-12-source-dump.tar.gz` (299 files): 53,841,729 bytes, mtime 2026-10-13T14:56:57Z, sha256 `7ec7fde8a7201ecc4da7d58d8b7e078241a85c900a82cff1b2e191d7b667190c`, equal to its `.sha256` sidecar (`shasum -a 256 -c`: OK, 15:00 UTC). Two superseded archives sit beside it, each with its own sidecar: `.prev2` (sha256 `98dbe94bfa2284410b7663ea9853e01a89b5810a2a2bfffda60d3d050f4c6386`, 53,829,839 bytes, mtime 2026-10-12T20:04:09Z) and `.prev` (sha256 `eca7ee24123b3ae56219f759e2354f1d6219c0681f25e32c55874c3b37d4c93b`, 53,829,689 bytes, mtime 2026-10-12T17:33:26Z). The folder name carries no topic, by owner ruling. Per `handoff-to-sibling.md` (not re-read): one blog post, four talks with transcripts and frame extractions, three discovered texts. The README and manifest were committed in `50ef56d` (2026-10-13 12:35:57 +0300) and again in `998256a` (17:59:38 +0300); a sibling session owns this folder.

---

## Orchestration log

`orchestration_log/{reference,history,recon}`. `reference/` holds eight tracked files: the five-file contract (`ground-truth.md`, `user_deferred_items.md`, `decisions.md`, `capabilities.md`, `conventions.md`) plus `codebase_state.md`, `deferred_items.md` and `digest-harness-plan.md`. `decisions.md` (2026-08-10) records `codebase_state.md` and `deferred_items.md` as folded in and deleted; both files exist and are tracked.

`history/2026-10-12/` (listed 2026-10-13 10:05 UTC):

- `events.md`, `failures.md`: the journal and the failure entries of the orchestrating session `llm-manifestos-30`, with entries dated 2026-10-13. Tracked; `failures.md` is committed (`787eb4a`), `events.md` carries an uncommitted edit (`git status`, 10:05 UTC).
- `session.md`: the 2026-10-12 session record. Tracked since `6f96589` ("2026-10-12 session record and closing journal flush").
- `stop-yapping-pilot-1.md`, `petro-cut-1.md`, `petro-cut-2.md`, `petro-cut-3.md`: frozen data reports of the pilot and of Petro cuts 1 to 3. Tracked.
- `handoff-to-sibling.md`: the brief to the sibling session `llm-manifestos-0d`, with a corrections section. Tracked.
- `events-llm-manifestos-0d.md`: that sibling session's journal. Untracked at the 2026-10-12 check; tracked since `50ef56d`, last touched by `034da1d`.

`history/2026-10-13/` (listed 2026-10-13 15:05 UTC): `source-pull-process.md`. Tracked; first committed in `c7c007a`; its own header names the current revision.

`recon/2026-10-12/` (gitignored): `handoff-verify.md`, `manifesto-guidance-inventory.md`, `ollama-system-one.md`, `readme-fix.md`, `quote_check.py`, `prompts/`, and, added on 2026-10-13, `petro-driver-brief.md`, `llama-server-judge-path.md`, `reference-verify.md` and `reference-verify-2.md`.

`recon/2026-10-13/` (gitignored; listed 2026-10-13 15:05 UTC): `source-pull-verify.md` (32,202 bytes), `source-pull-verify-2.md` (24,376) and `source-pull-verify-3.md` (13,261), from the verifier; `scripts-preserve.md` (21,290), the sibling session's report; `prompts/`.

---

## Themes

Defined in `themes.yaml`. Two themes exist; both are in use. `design-methodology`, `ai-instructions` and `research-protocols` were removed in `8d4e199`.

| Key | Icon | Name | In Use |
|-----|------|------|--------|
| `software-engineering` | 🔧 | Software Engineering Principles | Yes (8 files) |
| `cognitive-science` | 🧠 | Cognitive Science | Yes (5 files) |

---

## Generation Pipeline

Source: `generate.py` (133 lines), read, not run. Command: `just readme`.

### Exact command

```
uv run --with pyyaml --with python-frontmatter --with pydantic --with jinja2 --with rich generate.py
```

Dependencies are injected inline via `uv run --with`; no separate virtualenv or requirements file exists.

### Steps (in order, from `generate.py`)

1. **Load config** — reads `config.yaml` (`title`, `description`) and `themes.yaml` via `yaml.safe_load`
2. **Scan** — globs `manifestos/*.md` with `sorted()`, so files are processed alphabetically by filename; exits 1 if `manifestos/` is missing
3. **Parse** — each file is loaded with `frontmatter.load()` (python-frontmatter library)
4. **Validate** — frontmatter dict is passed to `ManifestoMetadata(**post.metadata)` (Pydantic model)
   - Required fields: `title`, `tagline`, `version`, `theme`, `description` (all `str`); the model has no optional fields and no `model_config`, so extra keys are ignored
   - `version` must match regex `^\d+\.\d+\.\d+$`; enforced by `@field_validator('version')`
   - Invalid files are collected into an `errors` list, shown as panels, and skipped (graceful degradation — pipeline continues)
5. **Warn** — theme panel if frontmatter themes are not in `themes.yaml`
6. **Exit early** — if the `manifestos` list is empty after filtering, exits with code 1
7. **Render** — passes `{'project': config, 'manifestos': manifestos, 'themes': themes}` to `jinja2.Template` loaded from `README.template.md`
8. **Write** — writes rendered output to `README.md`, appending a trailing newline; prints the count and a per-theme table

### Template behavior (`README.template.md`)

- Quick Reference table: all manifestos sorted by `title`, with Theme and Version columns
- Theme sections: themes sorted by their key string; each section lists manifestos sorted by `title`; each entry heading reads `[title](path) version`, then the tagline in italics, then the description
- Only themes that appear in at least one manifesto's frontmatter are rendered; unused themes in `themes.yaml` are silently omitted
- Theme display falls back to `{'icon': '📄', 'name': theme_key, 'description': ''}` if the theme key is missing from `themes.yaml`
- A closing Maintenance section points to `MAINTAINERS_GUIDE.md`

---

## What is tracked vs. ignored

`.gitignore` (six lines, read 2026-10-12; each matched with `git check-ignore -v`):

- `orchestration_log/history/*/cost.md` — gitignored (three files exist: 2026-04-29, 2026-05-01, 2026-05-11)
- `orchestration_log/recon/` — gitignored (`7b3878d`); local recon notes, including `recon/2026-10-12/`
- `/evals/` — gitignored (`9021645`), anchored at the root; local-only by owner ruling
- `/research/` (repo root only) — gitignored, anchored in `8d4e199`; holds `2026-10-12-discovery/` and `caveman/`; `archive/research/` is tracked and not matched
- `*.DS_Store`, `__pycache__/` — gitignored

Tracked: the root files `.gitignore`, `MAINTAINERS_GUIDE.md`, `README.md`, `README.template.md`, `config.yaml`, `generate.py`, `justfile` and `themes.yaml` (`git ls-tree --name-only HEAD`, 2026-10-13 10:06 UTC, `HEAD` `e21d6b1`); and the directories `manifestos/`, `digests/`, `.claude/skills/`, `tools/digest-eval/` (with its 110-file fixture), `resources/` (the source-dump folder as `README.md`, `index/MANIFEST.sha256`, its own `.gitignore` and 12 build scripts under `scripts/build/`: 15 files at 2026-10-13 15:00 UTC), `orchestration_log/{reference,history}`, `archive/`, `instructions/` and `source material/` (3 files). `README.md` is a generated artifact committed after each `just readme` run (unverified: `git log` shows commits beside manifesto changes, not one per run).

Not scanned by `generate.py`: everything outside `manifestos/`. `drafts/` does not exist; `MAINTAINERS_GUIDE.md` on `main` holds no `drafts`, `recut` or `orchestration_log` text, so the 2026-10-11 baseline's draft-ship flow and `recut-<slug>.md` rule are unverified on `main` (`history/2026-10-11/recut-kiss.md` exists).

### Archive directory

`archive/` contains four subdirectories: `design/`, `dieter_rams/`, `research/`, `software_building_principles/`. These are pre-collection source materials, not deprecated manifestos. No `archive/deprecated/` path exists yet (`MAINTAINERS_GUIDE.md` lines 292 and 432 describe it; created on first archival).

---

## Known Limitations

- **The entry gate is absent (measured 2026-10-12; commits re-measured 2026-10-13 09:51 UTC).** `conventions.md` used to say the gate lives in `MAINTAINERS_GUIDE.md`, Workflows. `MAINTAINERS_GUIDE.md` is 497 lines on `main` and at the tip of `origin/claude/manifesto-design-discussion-liuuvf` (`d54bd3f`), and no line of either holds "entry gate" (count 0 for `main`, `d54bd3f` and `8d4ef6f`); the only "gate" lines are the validation gate (`just readme`, lines 29, 58, 105). It survives in three commits on the branch: `b0645cb` (2026-10-11 13:42:58 UTC), `4c4f786` (13:46:49 UTC) and `79b4954` (13:47:45 UTC, "doc: guide and conventions — ship archive paths, re-cut record name"); each holds four "entry gate" lines. `79b4954` is the last guide version before `8d4ef6f` "revert: maintainers guide to main" (2026-10-12 03:52:13 UTC) removed the gate, so a restore from `4c4f786` alone would lose the `79b4954` edits. `history/2026-10-11/session.md` (D12) and `handoff-to-sibling.md` still point at it.
- **`origin/main` already holds the five slice commits (measured 2026-10-12 20:30 UTC; ahead count re-measured 2026-10-13 15:00 UTC).** `9021645`, `63f3908`, `5e957ff`, `6744a10` and `b43f398` (all committed at 22:39:20 +0300) are on `origin/main`; `git reflog show origin/main` records `update by push` at 22:39:47 +0300. The repo's records do not identify the actor: `.git/hooks` holds only `*.sample` files and `.git/config` holds `[core]`, the `origin` remote and `branch.main.*`; it sets no hook or push rule. The reflog shows pushes the same day at 14:40:13, 14:45:29 and 14:47:15 +0300 as well. `2dcd1d4`, `6d55190` and `6f96589` (committed 2026-10-12 20:26:37 UTC) were not pushed: `main` was ahead 3 at 20:30 UTC (from the commit times and the reflog, whose last push is 22:39:47 +0300), and ahead 12 on 2026-10-13 at 15:00 UTC at `HEAD` `998256a` (`git rev-list --left-right --count origin/main...main` reads `0 12`; `origin/main` is `b43f398`, its last reflog entry the 22:39:47 +0300 push; the twelve, newest first: `998256a`, `c7c007a`, `3148d45`, `e7defef`, `e21d6b1`, `034da1d`, `1577a81`, `787eb4a`, `50ef56d`, `6f96589`, `6d55190`, `2dcd1d4`). The ahead count changes at every commit; read it again before relying on it. `events.md` states the repo is public; the independent check (`reference-verify.md`, 2026-10-13 09:42 UTC) found the GitHub page at HTTP 200 and the API reporting `private: false` (not re-run by me), so the three source-dump files pushed in `b43f398` and the history files pushed by 22:39:47 +0300 are public; the later commits, including the 12 build scripts of `998256a`, are not pushed.
- **No charter, no memento configuration (measured 2026-10-12).** `CLAUDE.md` and `.claude/memento.yaml` do not exist. Per `events.md`, memento runs in preservation mode: no project goal stands, and the shipped schema's `docs/` homes are absent, so traces go to `orchestration_log/history/<date>/`.
- **The shell's `grep` skips files a `.gitignore` hides (measured 2026-10-12 20:30 UTC).** `type grep` reports a shell function from a shell snapshot. `grep -rl '/tmp/srp-substrate' resources/2026-10-12-source-dump` found 0 files; `find resources/2026-10-12-source-dump -type f ! -name '*.png' ! -name '*.pdf' -exec grep -l '/tmp/srp-substrate' {} +` found 20 (the verifier re-ran the `find`: 20 on 2026-10-13). Search ignored folders with `find ... -exec grep`.
- **Digest-eval runs do not reproduce end to end (measured 2026-10-12).** Reader records hold the adapter and model only. `pi --help` lists no seed or temperature flag, so the reader is unseeded; agent judges vary (self-difference 0.38 and 0.5 per demand in the Petro calibration); `evals/` is gitignored. `score` is reproduced from stored records on the tracked fixture; `gate` is tested on synthetic scores only. `SystemOneJudge` is a stub.
- **No `archive/deprecated/` path exists.** `MAINTAINERS_GUIDE.md` describes an archival workflow using it; the first archival action will need to create it.
- **`generate.py` accepts any `x.y.z` version.** `ground-truth.md` says patch versions are never used; `first-principles.md` sits at 1.0.1, the only patch version (open owner item, `user_deferred_items.md`). The generator does not enforce the rule.
- **Attribution lines are not uniform (measured 2026-10-13 09:51 UTC).** Two manifestos carry a `*by NAME, YEAR*` line (`cargo-cult-science.md:11`, `zen-of-python.md:28`). Eight carry an `*After ...*` line: `correct-by-construction.md:13`, `dry.md:232`, `first-principles.md:12`, `kiss.md:12`, `lines-spent.md:79`, `simple-made-easy.md:11`, `stop-yapping.md:131`, `yagni.md:161`. `intervention.md`, `postgres.md` and `self-documenting-code.md` carry neither (`grep -n -E '^\*After |^\*by [A-Z]'`). `MAINTAINERS_GUIDE.md` on `main` holds no attribution rule (no line contains "attribution"). The 2026-10-11 baseline's "attribution complete" was the branch's state.
- **No CI/CD gate.** `just readme` is a manual step; there is no `.github/` and no hook. Nothing prevents committing a manifesto without regenerating README, creating drift.
- **`stop-yapping.md` replaced `only-fluff-die.md`** (2026-05-01, `d94e962`). Same function (language compression), a harsher, model-addressed register (`decisions.md`). Theme: cognitive-science.
- **`postgres.md` added (2026-05-11).** Application Postgres manifesto, 269 lines, 5337 words, three full rewrites (`decisions.md`); the 2026-10-11 baseline's counts of reviewers and fixes are unverified. Theme: software-engineering.
- **`kiss.md` and `simple-made-easy.md` are both at version 2.0.0.** Both reached 2.0.0 in `5994364` (2026-04-22, "differentiate simple-made-easy and decomplect"); `kiss.md` was last edited in `8d4e199` (2026-10-12) (`git log -S'version: "2.0.0"'` and `git log` per file, 2026-10-13 09:51 UTC). `7c6467a` added `intervention.md` and touched neither file. Their current thesis boundaries may still be settling.

---

## Next Actions

These are observations, not commitments. An orchestrator or maintainer should evaluate each.

- Add a CI step (e.g., a pre-commit hook or GitHub Action) that runs `just readme` and fails if `README.md` has uncommitted changes.
- Decide where the entry gate lives: restore it from `79b4954` (the last guide version that carries it; `b0645cb` and `4c4f786` hold earlier forms), or retire every pointer to it. Owner call.
- Decide who may push `main` of the public repo; the reflog shows four pushes on 2026-10-12 and no hook.
- Run `just install-digest-eval` where the eval loop will run; the `test-digest` skill stops on a missing command.
