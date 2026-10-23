# Verification of the digest modes, minified files, and doctor

Date 2026-10-23. Worktree `<worktree>`, branch `verify/digests`. Claude Code 2.1.309, model haiku (resolved to `claude-haiku-5-5`). Every command used a copy of the config, `.manifestos.d3.yaml`, that differs from `.manifestos.yaml` in `manifesto_dir` alone, which points at the worktree's `plugin` folder. The copy is deleted at the end. Captures sit in the git-ignored `<recon>/captures-3.6/d3b/`; this report carries no identifier from them.

Words are whitespace-separated tokens, counted with `wc -w`.

## Two premises of the brief did not hold

| Premise | Observed |
|---|---|
| The stack holds `raise-the-bar`. | Neither `.manifestos.yaml` nor the copy lists it. The stack holds eight elements: three skills (`write-well`, `manifesto-writing`, `decide-while-away`) and five manifestos (`first-principles`, `cargo-cult-science`, `dry`, `simple-made-easy`, `lines-spent`). |
| Digest modes refuse until a local `raise-the-bar` digest exists. | Before step 0 every mode compiled with exit 0, because all five manifestos have a shipped single digest and skills enter in full. Nothing in the stack refuses. |

I ran steps 1 and 2 before step 0 and again after it. Every output was byte-identical across the two runs (steps 1 and 2), which fits `raise-the-bar` lying outside the stack. I wrote the local digest anyway, as the brief orders. Refusal texts were exercised in a temp copy (step 4).

## Step 0: local digest for `raise-the-bar`

| Command | Exit | Observed | Expected | Verdict |
|---|---|---|---|---|
| `plugin/bin/unharness stack --config .manifestos.d3.yaml raise-the-bar` (the skill's own launcher path, no `UNHARNESS_FROM`) | 0 | A `<stack>` block with one line, then the full text of the manifesto. The launcher ran the bundled package. | The skill's read step works as written. | PASS |
| Write `.claude/digests/raise-the-bar.md` | n/a | 346 words, body only, ends with the standing line. | Under 350 words, body only. | PASS |
| `unharness stamp .claude/digests/raise-the-bar.md --config .manifestos.d3.yaml` | 0 | Printed `stamped raise-the-bar in .claude/digests/index.json`. The entry's hash equals the manifesto's hash in the `<stack>` block (`b6131386...`). | Index created beside the digest with the stem's hash. | PASS |
| `unharness prompt --digests` after the stamp | 0 | Exit 0, output unchanged from before. | The skill says a slug outside the stack gets no compile confirmation, so this run proves only that nothing broke. | PASS |
| Commit | n/a | `f7e7b20 doc(repo): local digest for raise-the-bar`, holding the digest and the index. | As specified. | PASS |

### How the skill read in use

- **Clear.** The name-the-stem, read-the-manifestos, write-the-file, and stamp steps ran as written. The launcher path in the skill works now; the 3.5.0 record needed `UNHARNESS_FROM`.
- **The 350-word cap forces dropped demands, and the skill does not say which.** The first faithful draft ran 503 words. Three more passes reached 346. The skill's check step allows a demand to be "dropped on purpose" but gives no rule for choosing. I dropped, in this order: the second statement of belief with its grounds, the reason for each non-negotiable, the scope of trust, the tutorial boundary, the model-reader emphasis rules, the "we" rule, the plain-words rule, and five of the seven closing checks. A reader of the skill cannot tell whether such drops are expected for a long manifesto or whether the cap should yield.
- **No counting rule.** The skill names a word cap but not how to count. The spec defines words as whitespace-separated tokens; the skill does not repeat it.
- **Binding step is ambiguous for a subagent.** The skill orders binding through `manifesto-oath`, but a subagent already receives the binding from its start hook. The skill does not say whether to bind a second time to the manifesto it digests.
- **Idioms in the manifesto.** "Raise the bar", "lift", and "fanfare" are figures. The skill bans idioms in the digest, so each had to be rewritten as a literal demand. This worked, but the skill names no check for it.

## Step 1: `unharness doctor`

Both runs printed 27 lines, identical to each other and unchanged by step 0. Both exited 1.

| Command | Exit | Observed (lines, in order) | Expected | Verdict |
|---|---|---|---|---|
| `doctor --config .manifestos.d3.yaml` | 1 | `OK config`; eight `OK element` lines (five manifestos resolve into the worktree, the three skills into the logins' caches); three `OK skill` lines (1.10.0, 3.4.0, 1.10.0); five `OK digest <slug>: plugin, current`; `OK cover: first-principles, cargo-cult-science, dry, simple-made-easy, lines-spent; 1332 words`; four `OK` session-file lines, all current; `OK preamble: shipped`; `OK claude` (2.1.309); `OK uv` (both paths); `FAIL manifesto plugin: 3.4.0 is below 3.5.0, whose hooks do not stand down`; `OK prompt size: full 14886 words; shortest 5580 words`. | The order and detail of the spec's table; exit 1 on any FAIL. | PASS |
| `doctor --config .manifestos.d3.yaml --stack-digests --overlap --minified` | 1 | The same 27 lines. | The same, since nothing in this stack refuses under any flag. | PASS |
| The `cover` line against the digests | n/a | 1332 words equals 275 + 196 + 216 + 344 + 301, the five shipped single digests. | Total words of the chosen texts. | PASS |
| The `digest` lines against candidate stack digests | n/a | No stack-digest line. The one shipped stack digest names eleven slugs, six of them outside this stack, so it is no candidate. | One line per candidate stack digest, none here. | PASS |

Environment finding, not a product fault: the `meta` login holds `manifesto` plugin 3.4.0, so doctor's FAIL is correct and the exit code of 1 follows from it. The worktree's own `plugin.json`, `pyproject.toml`, and `marketplace.json` still read 3.5.0.

Unexplained: the `prompt size` line counts 14886 and 5580 words; `wc -w` on the compiled prompts gives 14888 and 5582. The two-word gap is the same in both modes. I did not trace it.

## Step 2: `unharness prompt` in six modes

All commands carried `--config .manifestos.d3.yaml`, stdout to a file, stderr empty in every row.

| Mode | Exit | Words | Digest files used (found by matching their text in the output) | Expected | Verdict |
|---|---|---|---|---|---|
| none | 0 | 14888 | none, all eight elements in full | Full texts, 3.5.0 behavior | PASS |
| `--digests` | 0 | 7278 | five plugin singles: `first-principles`, `cargo-cult-science`, `dry`, `simple-made-easy`, `lines-spent` | Singles for manifestos, skills in full | PASS |
| `--stack-digests` | 0 | 7278 | the same five; output identical to `--digests` | Identical when no stack digest has all its slugs in the stack | PASS |
| `--stack-digests --overlap` | 0 | 7278 | the same five; output identical to `--digests` | The same | PASS |
| `--minified` | 0 | 13192 | none; the min interplay and min commitments replace the full pair | Min pair read, texts in full | PASS |
| `--stack-digests --overlap --minified` | 0 | 5582 | the five singles plus the min pair | The shortest mode | PASS |

The constitution blocks, in order, are the eight element tags in config order in every mode. The constitution holds 12318 words in full and 4708 words as digests. The min interplay body holds 436 words against 1852 in the full one, and the min commitments hold 134 against 414; both ratios are under one third.

| Command | Exit | Observed | Expected | Verdict |
|---|---|---|---|---|
| `unharness stack --config .manifestos.d3.yaml` | 0 | One `<stack>` block and the full constitution. It names no digest file. | `stack` takes no mode flag, so it cannot report digest files per mode. | PASS |
| `unharness stack ... --digests` | 2 | `unrecognized arguments: --digests` | Rejection of mode flags. | PASS |
| `unharness prompt ... --overlap` | 1 | `unharness: --overlap requires --stack-digests` | The spec's text. | PASS |
| Refusal text, no mode refuses in this repo | n/a | Not observed with the repo's stack; see step 4 for the missing-digest message in a temp copy. | n/a | n/a |

Observation, outside the spec: piping `unharness stack` into `head` printed a `BrokenPipeError` traceback.

## Step 3: launch and capture in the shortest mode

Mode: `--stack-digests --overlap --minified` (5582 words, 34459 bytes). Command, typed in tmux session `unharness-d3b` (200 by 50, started in the worktree), run through a script outside the repo:

```
env -i HOME USER LOGNAME PATH SHELL TERM TMPDIR LANG CLAUDE_CONFIG_DIR=<meta login> \
  CLAUDE_CODE_ENABLE_TELEMETRY=1 OTEL_LOG_RAW_API_BODIES=file:<captures>/ \
  bash -c 'plugin/bin/unharness prompt --config .manifestos.d3.yaml --stack-digests --overlap --minified \
    | plugin/bin/unharness launch -- claude --model haiku --plugin-dir <worktree>/plugin'
```

The session got two questions and a `/compact`: the question about governing elements, then `/compact`, then a request to quote the first line of the commitments, then `/exit`. I killed `unharness-d3b` afterward; `tmux ls` then listed only the owner's four sessions, which I never touched. I used the plain `claude` binary under the `meta` login, as the 3.5.0 record did, and not a `claude@meta` shell function.

The index holds four requests.

| # | query_source | Messages | System block 1, characters | Byte-equal to the compiled prompt |
|---|---|---|---|---|
| 0 | generate_session_title | 1 | 3059, a title instruction | no, a different prompt |
| 1 | repl_main_thread, first question | 2 | 34413 | yes |
| 2 | compact | 4 | 34413 | yes |
| 3 | repl_main_thread, after the compaction | 2 | 34413 | yes |

| Check | Observed | Expected | Verdict |
|---|---|---|---|
| The documented pipe `prompt \| launch -- claude` starts a session | It started with no crash. The 3.5.0 record crashed twice on this Mac with a `kqueue` error. | A session. | PASS |
| System block before compaction (#1) equals the compiled prompt | Byte-equal; 34413 characters, 34459 bytes, SHA-256 starting `c06f2b87d0ecd54d`. | Byte-equal. | PASS |
| System block in the compaction request (#2) and after compaction (#3) | Both byte-equal to the same prompt. | Byte-equal. | PASS |
| The cache file the launcher wrote | Its file name is the SHA-256 of the compiled prompt, `c06f2b87...`. | Name equals the prompt's hash. | PASS |
| Each request has two system blocks | The identity line (57 characters) and the prompt; nothing else. | No default Claude Code prompt. | PASS |
| No CLAUDE.md text | The compiled prompt holds none. In the whole body the string appears once, inside the Agent tool's own parameter description ("instructions such as CLAUDE.md or a skill"), and never in the messages. No memory-file wrapper appears. This repo has no CLAUDE.md, so the check shows the string's absence, not a strip. | None. | PASS |
| No git instructions | No `gitStatus` and no git-safety text in any message or system block. The word "commit" occurs in the messages only inside skill descriptions and one hook paragraph about work in a shared folder. | None. | PASS |
| No billing or attribution text | No `x-anthropic-billing`, no `cc_version`, no `Co-Authored`, in any request. | None. | PASS |
| The reply after compaction quotes the first commitment | It matches the first `I must` line of the min commitments file exactly, not the full file's line. | The min file's first line. | PASS |

Excerpt of the reply after compaction:

```
I must apply Strunk's rules to every sentence, and I will reread
each draft, excusing no rule.
```

Observations the captures show, none scored:

- **The first reply listed ten names.** It gave the eight element names, then `interplay` and `commitments`, which are section tags of the prompt and not elements. The 3.5.0 record shows the same pattern after compaction.
- **The binding hook line survives.** Requests #1 to #3 each carry one `Active bindings` line in the messages, so the per-turn hook ran. The doctor FAIL above, the meta login at 3.4.0, is a candidate cause. The captures do not settle it, because no run with the login's plugin removed was made. The element names are therefore also available outside the system prompt; only the quoted commitment, which the hook line does not carry, is evidence that the model read the compiled prompt.
- **Other harness text remains outside the system block**: the user-reminder, a SessionStart hook paragraph, the deferred tool and skill lists, and 15 tools.
- **Sample.** One session, one model, one compaction.

## Step 4: stamp, then edit the manifesto, in a temp copy

A temp folder held a copy of the repo's `plugin/manifestos` and `plugin/digests`, a config pointing at that copy, and the four session files. A throwaway local `dry` digest of three sentences sat beside it. No product file was edited.

| Command | Exit | Observed | Expected | Verdict |
|---|---|---|---|---|
| `prompt --digests` before the stamp | 1 | `unharness: <digest path> has no entry in <index path>; run unharness stamp <digest path>` | The spec's second refusal, naming `unharness stamp`. | PASS |
| `unharness stamp <digest path> --config <copy>` | 0 | `stamped dry in <index path>` | One-line report. | PASS |
| The new index | n/a | `{"dry": {"dry": "5dd350b8..."}}`, two-space indent. The hash equals the `dry` line of the `<stack>` block. | One entry, the stack block's hash. | PASS |
| `prompt --digests` after the stamp | 0 | The local three-sentence text is present once; the plugin's `dry` digest is absent. | Local wins. | PASS |
| Append one line to the copy of `manifestos/dry.md`, then `prompt --digests` | 1 | `unharness: <digest path> is stale (changed: dry); run /compile-digest dry` | The spec's stale message, naming `/compile-digest` and not `stamp`. | PASS |
| Plain `prompt` in the same state | 1 | `unharness: .manifestos.interplay.md is stale (changed: dry); run /compile-commitments` | A stale session file, since the stack block records `dry`. | PASS |
| In a second temp copy, add `raise-the-bar` to the stack, no local digest; `prompt --digests` and `prompt --stack-digests --overlap` | 1 and 1 | `unharness: no digest for raise-the-bar: tried <local path> and <plugin path>; run /compile-digest raise-the-bar` | The spec's first refusal, verbatim. | PASS |
| The same copy, plain `prompt` | 1 | `.manifestos.interplay.md is stale (changed: raise-the-bar); run /compile-commitments` | A stale session file. | PASS |

In both temp copies the digest refusal came before the session-file refusal whenever a digest mode was on, and the session-file refusal came alone in the full mode.

## Counts

| Step | Scored rows | PASS | FAIL |
|---|---|---|---|
| 0 | 5 | 5 | 0 |
| 1 | 4 | 4 | 0 |
| 2 | 9 | 9 | 0 |
| 3 | 9 | 9 | 0 |
| 4 | 8 | 8 | 0 |
| Total | 35 | 35 | 0 |

The premise table, the reading notes, the observations, and the one step-2 row marked n/a are not scored.

## Findings that need an owner

- **Task premise.** The stack lacks `raise-the-bar`, so no digest mode refuses here. The brief's expectation of refusals did not apply.
- **Meta login plugin.** The `meta` login's `manifesto` plugin is 3.4.0. Doctor fails on it, and the binding hook line still fires in the captured session.
- **Version strings.** `plugin.json`, `pyproject.toml`, and `marketplace.json` read 3.5.0 in the verify worktree.
- **Skill gap.** `/compile-digest` states a word cap and no rule for choosing which demands to drop when the cap binds.
- **Doctor word count.** Its totals trail the compiled prompt's by two words; the cause is untraced.

## Summary

Every scored check passed: the six prompt modes compile with the expected sizes, doctor prints the specified lines, and the stamp, stale, and missing-digest refusals match the spec's text. In the captured session the system block was byte-equal to the compiled shortest-mode prompt before and after `/compact`, with no CLAUDE.md, git-instruction, or billing text, and the documented pipe no longer crashes. Two premises of the brief were false in this repo, and the meta login's older plugin makes doctor fail and lets the binding hook line through.
