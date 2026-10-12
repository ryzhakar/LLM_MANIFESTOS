# stop-yapping digest, pilot 1: data (frozen 2026-10-12)

A pilot, not a cut: the instrument was built while the run went. Raw files are local-only (`evals/stop-yapping/pilot-1/`, gitignored; a trimmed fixture is tracked at `tools/digest-eval/tests/fixtures/pilot-1/`). Flaws are listed in `failures.md` ("Pilot cut 1 was reported as a gate pass on an unsound instrument") and are repeated in the last section.

## Instrument

- Reader: `pi -p --model long` (9B, 131K context) with the standard prompt, `--append-system-prompt <file>` carrying the digest (`digests/stop-yapping.md`, 251 words) or the full manifesto (`manifestos/stop-yapping.md`, 1,231 words); nothing appended for the nothing-loaded condition. No tools, no session files for singles; sessions held with `--session-dir` plus `--session-id`. Stdin closed (an open pipe hung a call for 14 minutes). Sampling unseeded.
- Replies: 6 single tasks x 3 conditions x 3 repeats = 54, plus a 16-turn session per condition = 48; 102 in all. Serial on the local llama-server, about 10 to 14 s per warm reply. One reply in 102 carried a literal `</think>` draft; the text after it was judged.
- Judges: six opus agents (one per single-task packet, nine blind replies each), one sonnet agent (the session packet, 48 replies), each bound to the full manifesto through `manifesto-oath`; verdict per reply: a violation count and done. The rubric (`judge_brief.md`) was written mid-run: count one per word or phrase before the first word of substance, hedge, pleasantry or praise, filler or softener, connective, long form, announcement, restatement, sentence over fifteen words, and (one per sentence) an article the meaning survives without.
- Scripted cross-check (`det_check.py`, literal word lists only, code excluded): not the gate.
- Gate (invented by the pilot, fixed before reading replies): digest below nothing-loaded overall and on at least 5 of 6 tasks; (none - digest) at least 0.75 x (none - full); done count not more than one below either baseline.

## Single tasks (opus judges), mean violations per reply (done of 3)

| task | nothing loaded | digest | full manifesto |
|---|---|---|---|
| t1-keyerror | 12.33 (3) | 2.67 (3) | 3.00 (3) |
| t2-process-thread | 6.00 (3) | 2.00 (3) | 1.33 (3) |
| t3-reverse-js | 6.00 (3) | 0.00 (3) | 0.00 (3) |
| t4-requests | 9.33 (2) | 1.33 (3) | 1.00 (2) |
| t5-git-undo | 7.33 (3) | 1.67 (3) | 1.00 (3) |
| t6-select-star | 9.33 (3) | 2.00 (3) | 0.33 (3) |
| all 18 | 8.39, done 17 | 1.61, done 18 | 1.11, done 17 |

Gate on those numbers: cut PASS (6 of 6 tasks), near full PASS (6.78 against 5.46 needed), completion PASS. Mean reply length: 170 words nothing loaded, 54 digest, 46 full. Scripted counter on the same replies: 1.17, 0.17, 0.22 per reply; articles per 100 words 4.52, 2.81, 2.54.

Judge notes: opus marked `done` true on a reply with a broken `str.reduce` method (t3) and on a reply stating that `git reset HEAD~1` leaves changes staged (t5); both are wrong on the substance.

## Session, 16 turns per condition (sonnet judge), mean violations per reply

| condition | turns 1 to 5 | turns 12 to 16 | drift | done |
|---|---|---|---|---|
| nothing loaded | 4.80 | 5.60 | +0.80 | 16 of 16 |
| digest | 3.00 | 4.60 | +1.60 | 16 of 16 |
| full manifesto | 4.40 | 1.40 | -3.00 | 16 of 16 |

Per turn, violations / words (nothing loaded | digest | full):

| turn | nothing | digest | full |
|---|---|---|---|
| 1 | 7/187 | 3/59 | 5/84 |
| 2 | 3/195 | 2/73 | 3/71 |
| 3 | 7/233 | 4/64 | 4/76 |
| 4 | 5/187 | 3/66 | 5/42 |
| 5 | 2/208 | 3/58 | 5/60 |
| 6 | 1/313 | 4/83 | 3/83 |
| 7 | 2/292 | 4/98 | 1/65 |
| 8 | 8/214 | 4/100 | 1/59 |
| 9 | 9/189 | 3/90 | 2/61 |
| 10 | 4/238 | 3/79 | 0/51 |
| 11 | 7/254 | 3/96 | 2/74 |
| 12 | 4/252 | 7/77 | 1/52 |
| 13 | 3/272 | 3/48 | 3/62 |
| 14 | 6/373 | 5/107 | 2/96 |
| 15 | 10/378 | 6/91 | 0/77 |
| 16 | 5/398 | 2/122 | 1/77 |

Scripted counter, sessions, turns 1 to 5 against 12 to 16: nothing loaded 1.2 and 1.2, digest 0.2 and 1.0, full 0.6 and 0.4. Late digest replies show the forbidden openers ("This is about...", "Here's the comparison"), softeners ("You should wait"), filler ("just", "very") and retained articles. The sonnet and opus judges score on different scales (the full manifesto scored 1.11 per reply in the opus packets and 4.40 early in the sonnet session), so only comparisons inside one packet hold.

## What the pilot established

- A 251-word digest cut violations per reply from 8.39 to 1.61 on six tasks, close to the full text (1.11), with completion intact on the judge's reading. The full manifesto kept improving over the session (-3.00 slope shift) where the digest rose (+1.60); one session per condition, so the drift is unreplicated.
- The reader leaks a literal `</think>` draft rarely (1 in 102) and a digest-loaded reply took about 12 s.
- No placebo or one-line control, three repeats per cell, thresholds invented, judge models mixed, rubric written mid-run, completion judged leniently: the result is a large effect on a small set, not a gate pass.

— measured by Claude (orchestrator), 2026-10-12, from the pilot's stored scores and verdicts
