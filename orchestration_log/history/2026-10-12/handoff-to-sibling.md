# Handoff to sibling session: source dump (2026-10-12)

From `llm-manifestos-30` to `llm-manifestos-0d`, at the owner's 19:45 commitment (`events.md`). Facts and paths only. Dump folder: `/Users/ryzhakar/LLM_MANIFESTOS/resources/2026-10-12-source-dump/` (below: `$D`).

## 0. Verify before you trust

- Folder: `cd $D && shasum -a 256 -c index/MANIFEST.sha256` (0 failures at handoff, 287 files).
- Archive: `cd /Users/ryzhakar/archives && shasum -a 256 -c 2026-10-12-source-dump.tar.gz.sha256`; sha256 `eca7ee24123b3ae56219f759e2354f1d6219c0681f25e32c55874c3b37d4c93b`.
- Git: only `$D/README.md`, `$D/index/MANIFEST.sha256` and `$D/.gitignore` are tracked (commit `b43f398`, not pushed). Everything else in `$D` is local-only by the folder's own `.gitignore`.
- Any edit under `$D` needs: refresh the file's line in `index/MANIFEST.sha256`, rebuild the archive with `COPYFILE_DISABLE=1 tar -czf ... -C resources 2026-10-12-source-dump`, rewrite the sidecar, verify by extracting to a temp dir and running the manifest check.

## 1. Where discovery stands

- No manifesto is targeted. Manifestos are discovered from the substrate, never chosen ahead (owner rulings, restated at handoff and in the 2026-10-11 framing, `orchestration_log/history/2026-10-11/session.md` Phase 2). "Prepare, do not write yet" covers fetching verbatim, transcribing, extracting, indexing, verifying and preserving; it excludes drafting a manifesto or a digest, a summary offered as a deliverable, and edits under `manifestos/` or `digests/`.
- Discovery has not run on this dump: no survey, axiom verification, stack map or candidates file exists for it. Precedent for that stage: `orchestration_log/history/2026-10-11/` (`discovery-research/`, `session.md`); gate: `MAINTAINERS_GUIDE.md` (Workflows, entry gate); process: `orchestration_log/reference/conventions.md` (Manifesto writing process).
- Threads the sources raise. Read off titles, chapter lists and cross-references in `$D/index/sources.md` only; no transcript or text was read by this session's orchestrator, so the labels are unverified:
  - Responsibility and system decomposition: S-01 (title; its body links D-01 and D-02), D-01 (Parnas 1972), D-02 (Dijkstra EWD447 1974), D-03 (Martin, "The Principles of OOD"; linked from no supplied source).
  - Function design, honest signatures, levels of abstraction: S-02 chapters 1 to 7 and 9 (e.g. "Honest vs. dishonest functions", "Designing empathetic signatures", "Single level of abstraction"); S-04 title ("You Say You Want to Write a Function").
  - Complecting and simplicity: S-04 chapters "The problem of complecting", "Defining simple made easy". Held ground by title: `manifestos/simple-made-easy.md`, `manifestos/kiss.md`.
  - Values, objects, state, identity, equality: S-04 "Value vs. object semantics", "Avoiding global state"; S-05 "Objects and entanglement", "The problem with classes", "The dangers of references", "Ship of Theseus and identity", "Defining equality", "Intrinsic vs extrinsic state"; S-02 "Managing randomness and state".
  - Calculating versus doing, purity: S-04 "Calculating versus doing", "Pure functions and testing"; S-05 "Calculating vs doing", "Value-oriented programming".
  - Types and invariants: S-02 "Encoding invariants in types"; S-05 "Invariants and basis functions". Held ground by title: `manifestos/correct-by-construction.md`.
  - Loops and algorithms: S-03 (title "GoingNative 2013 C++ Seasoning"; S-02's description labels it "No Raw Loops"; no chapters).
  - Series and links: S-04 and S-05 are Part 1 and Part V by title; S-02's description links S-01, S-03 and S-04.
- Open questions the sources leave: (a) which thesis, if any, carries a verified axiom from at least two authors (the entry-gate test); (b) the enemy per thread; (c) overlap with the 13 held manifestos is unaudited (title-level matches above only); (d) whether S-04 and S-05 repeat each other; (e) whether the supplied surface is one thread or several; (f) whether S-03's speaker is who the ASR text suggests (metadata names none); (g) licences (section 2, item 1).

## 2. Open items, ranked

1. Licence flags, all in `$D/README.md`. D-02 (Dijkstra EWD447): Springer-Verlag notice "further reproduction strictly prohibited" on the PDF; owner ruled to keep the text (`$D/secondary/D-02/D-02.txt`, `D-02-transcription-original.html`). D-01 (Parnas): ACM notice allows copying "not for profit" (`$D/secondary/D-01/D-01-original.pdf`, `D-01.txt`). S-03: third-party re-upload by channel 25msr (`$D/primary/S-03-W2tWOdzgXHA/`). S-01: no licence statement on the page (`$D/primary/S-01.txt`, `S-01-raw.html`). No source content is tracked in git; the repo is public.
2. Fragile files outside the archive, in `/tmp/srp-substrate/`: videos and audio (`video/*.mp4`, `audio/*.m4a`, four each, hashes in `$D/index/frames-*.md`), captions, metadata JSON, and the held-out D-02 PDF `held-out/D-02/D-02-original.pdf` with its `.sha256` (sha256 `48a6a3aec4f50c3f4891ac03880f7238fdefe5e80f466f85d792a16352179c2c`, recorded in `$D/README.md`). All re-downloadable from the URLs in `$D/index/sources.md`; the video files are needed to grab any new frame.
3. Extraction quality, `$D/interleaved/extractions/`:
   - Two S-05 extractions still disagree with the checker: `S-05/sc1guyo5Rso-00h55m23s.txt` (CHRISTIE wordmark missing from ON-SCREEN TEXT; device position in VISUAL) and `S-05/sc1guyo5Rso-00h56m56s.txt` (partial "r" at the lectern panel edge). Reports: `_checks/extraction-check3-S-05.md`; stale: `_checks/extraction-check2-S-05-stale.md`.
   - Adjudication of 11 contested frames: 73 claims, 62 confirmed, 3 refuted, 8 unsettled; report `_checks/extraction-adjudication.md` (S-04 at 02m46s, 06m50s, 12m46s, 20m44s, 22m06s, 27m58s, 01h01m23s; S-05 at 28m31s, 33m05s, 35m06s, 51m29s).
   - `[illegible]` extractions: S-03 `W2tWOdzgXHA-00h02m52s.txt`; S-04 `b4p_tcLYDV0-00h02m46s`, `-00h06m50s`, `-00h27m35s`, `-00h27m58s`, `-00h32m50s`, `-01h01m23s`; S-05 `sc1guyo5Rso-00h28m31s`, `-00h51m29s`, `-00h55m23s`, `-01h38m57s`. S-02: none.
   - Frames outside the check rounds were never re-read by a second reader (`$D/README.md`, quality process); the weak spot is small or faint text.
4. Transcript quality, `$D/primary/S-0N-<id>/<id>-transcript.srt|txt`: "Speaker N:" labels unchecked; the Parakeet v3 model writes `<unk>` for "++"; S-03's speaker (Sean Parent) comes from ASR text only; S-03's metadata title and S-02's label for it differ (item in section 1).
5. Scratch-path references that break when `/tmp` clears: `$D/interleaved/scripts/check_extractions.py:14` (`REPORT_DIR`), `$D/index/frames-<id>.md` line 3 in all four (VIDEO FILE), `$D/index/sources.md:44`. `$D/README.md` already reads `/tmp/<scratch>/`.
6. Provenance gaps: the build and verify scripts are in `$D/interleaved/scripts/` (`build_interleaved.py`, `verify_interleaved.py`, `check_extractions.py`) and byte-identical to the originals; the frame descriptions in `$D/index/frames-<id>.md` predate the fresh extractions and were not used by them.

## 3. Owner rulings beyond `events.md`

- Every PNG is read afresh by a vision worker and its information embedded; "this is the work". The old frame descriptions are not a source.
- Delegate reading and checking to haiku subagents; the orchestrator does not read the sources; sonnet only for judgement; orchestrator and suborchestrator resume agents instead of relaunching.
- Original instruction: transcripts from MacWhisper only (no caption substitution), screenshots with ffmpeg only after a transcript lands; sonnet suborchestrator with haiku subagents.
- The sonnet adjudication launch was never declined by the owner (`orchestration_log/history/2026-10-12/failures.md`, "My messages interrupted ...").
- The owner reads no conversation text: decide what can be decided, block only through the prompt tool (`failures.md`, last entry).
- 2026-10-11 rulings still standing (`orchestration_log/history/2026-10-11/session.md`): pull every source into `resources/` verbatim, never from memory; manifestos are malleable; events belong in the tracked log; "nothing ever open for me, you deal with everything"; explicit paths when staging, never `git add -A`.

## 4. `srp-substrate`: retire

It is idle, its job is complete and verified (287 files, 0 manifest failures, archive checked), its context carries the superseded plan and a long message history, and everything it knew sits in `$D/README.md`, `$D/index/` and `$D/interleaved/scripts/`. It belongs to `llm-manifestos-30`; I keep it idle and message it only if you ask me to relay. A message arriving while it holds a permission prompt dismisses the prompt (`failures.md`), so fresh workers are safer.

## 5. Next deliverable to hand to agents (recommendation; the owner has not ordered it)

A collection-overlap audit over the dump, the first tier of the 2026-10-11 discovery tree: per source, a claim table (claim, source ID, locator as `interleaved/S-0N-<id>.md` cue time or text line) mapped against the 13 held manifestos in `manifestos/`, each claim marked held, partly held or unheld, with no thesis stated. One haiku reader per source (S-01 to S-05, D-01 to D-03) reading the interleaved documents and texts, a sonnet pass for the mapping; worker returns under `orchestration_log/recon/2026-10-12/` (gitignored), the report as `orchestration_log/history/2026-10-12/overlap-audit.md`. It feeds open questions (a) to (c) and needs no decision from the owner on a target. The `orchestration:research-tree` skill governs the tree.

— witnessed by Claude (orchestrator), 2026-10-12

## Corrections (appended after 19:52 UTC, from the sibling's verification in `orchestration_log/recon/2026-10-12/handoff-verify.md`; each re-checked here; the text above stands)

1. Section 0, "Git": nothing here was pushed by this session, but the claim "not pushed" is false. `b43f398` and its four predecessors (`9021645`, `63f3908`, `5e957ff`, `6744a10`) are on `origin/main`: `git reflog show origin/main` records `update by push` at 2026-10-12 22:39:47 +0300, 27 s after the commits (22:39:20). This session ran no push; the repo holds no hook and no push configuration (`.git/hooks` has only samples; `.git/config` has the remote and `branch.main.remote`). Who pushed is not determined. `2dcd1d4` (history reports, this brief) was local only (`ahead 1`) when checked. The repo is public, so the three tracked source-dump files are public.
2. Section 2, item 6: the three scripts are not byte-identical to `/tmp/srp-substrate/scripts/`. The label cleanup renamed `ROOT` in each (`build_interleaved.py:14`, `verify_interleaved.py:14`, `check_extractions.py:11`) and removed one docstring word (`check_extractions.py:2`). The README line that says "copied verbatim" (`$D/README.md`, scripts bullet) is wrong the same way; the README is now in your lane.
3. Section 2, item 5: the list was incomplete. 20 text files contain `/tmp/srp-substrate`: `index/frames-<id>.md` (4), `index/sources.md`, `interleaved/scripts/check_extractions.py`, `interleaved/extractions/_checks/` (7: adjudication, check S-02 to S-05, check2-S-04, check2-S-05-stale), `primary/S-01.txt`, `primary/S-0N-<id>/<id>-transcript-provenance.txt` (4), `secondary/D-02/D-02.txt`, `secondary/D-03/D-03.txt`. Only `check_extractions.py:14` reads the path at run time; the rest are documentary text. Cause: I searched a subset of paths, and in this shell `grep` is a function that skips files the folder's `.gitignore` hides, so `grep -r` under `$D` sees only the three tracked files. Use `find $D -type f ! -name '*.png' ! -name '*.pdf' -exec grep -l '/tmp/srp-substrate' {} +`.
4. Sections 1 and 2, the gate pointer: `MAINTAINERS_GUIDE.md` on `main` (497 lines) holds no entry-gate text, and neither does the tip of `origin/claude/manifesto-design-discussion-liuuvf`. The gate was committed on that branch (`b0645cb` 314 lines and `4c4f786` 315 lines, 2026-10-11) and reverted there by `8d4ef6f` "revert: maintainers guide to main" (2026-10-12 03:52 UTC). `orchestration_log/reference/conventions.md:30` and `orchestration_log/history/2026-10-11/session.md` (D12) still point to it. Open question (a) rests on text that survives only in the history of those two commits.
5. Section 2, item 2: video sha256 values are on line 3 of `$D/index/frames-<id>.md`; audio sha256 values are in `$D/primary/S-0N-<id>/<id>-transcript-provenance.txt` ("SOURCE AUDIO: ... sha256 ...").

— witnessed by Claude (orchestrator), 2026-10-12
