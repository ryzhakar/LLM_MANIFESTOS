## Preservation
- Archive: /Users/ryzhakar/archives/2026-10-12-source-dump.tar.gz . Its sha256 is in the sidecar file /Users/ryzhakar/archives/2026-10-12-source-dump.tar.gz.sha256 (the hash is not written here because this README is inside the archive).
- Restore, from the repo root: `tar -xzf /Users/ryzhakar/archives/2026-10-12-source-dump.tar.gz -C resources/` . Then check from the restored folder: `shasum -a 256 -c index/MANIFEST.sha256` (expect 0 failures).
- Git: only README.md and index/MANIFEST.sha256 are tracked (plus the folder's .gitignore); everything else in this folder is local-only and lives in the archive. The folder holds third-party transcripts, frames and texts, so it is not published through git.

# Fetched texts: source dump (2026-10-12)

Fetched, durable, verbatim source texts, transcripts and frames, ready for a later manifesto-writing pass. Nothing here is a manifesto or a digest.

Audio, video and YouTube caption files are NOT stored here. They live only in `/tmp/<scratch>/` (`audio/`, `video/`, `captions/`, `meta/`), which vanishes with the container.

Every copied file was verified with sha256 against its origin. Frames are ffmpeg outputs with no origin copy; see `## Frames`. `index/MANIFEST.sha256` lists the sha256 of every file in this folder.

Index files: `index/frames-<videoID>.md` (one per video, frame-by-frame), `index/sources.md` (source dump with metadata and chapters).

## primary/

Supplied by the stakeholder. Status for videos is the transcript STATUS from each provenance file. Words for S-01 are body words (header and LINKS section excluded). Words for transcripts are `wc -w` of the whole `.txt`.

| file | ID | title | author or speaker | year or upload date | URL fetched | supplied or discovered | added | status | words or duration | transcript | frames |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `S-01.txt`, `S-01-raw.html` | S-01 | The Single Responsibility Principle | Robert C. Martin (Uncle Bob) | 2014 (printed "08 May 2014") | https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html | supplied | 2026-10-12 | FULL | 1261 words | n/a | n/a |
| `S-02-2OMRWPOSw9s/` | S-02 (video 2OMRWPOSw9s) | How to write the perfect function | Logan Smith (channel and uploader) | 2026-08-20 | https://www.youtube.com/watch?v=2OMRWPOSw9s | supplied | 2026-10-12 | FULL | 9639 words; 47:32 (2852 s) | SRT, 776 cues; TXT | 30 PNG |
| `S-03-W2tWOdzgXHA/` | S-03 (video W2tWOdzgXHA) | GoingNative 2013 C++ Seasoning | not recorded in metadata (channel 25msr; transcript names "Sean Parent" at 00:00:33) | 2017-05-25 | https://www.youtube.com/watch?v=W2tWOdzgXHA | supplied | 2026-10-12 | FULL | 11172 words; 1:17:12 (4632 s) | SRT, 1869 cues; TXT | 30 PNG |
| `S-04-b4p_tcLYDV0/` | S-04 (video b4p_tcLYDV0) | Value Oriented Programming Part 1: You Say You Want to Write a Function - Tony Van Eerd  CppNow 2023 | Tony Van Eerd (in title; channel CppNow) | 2023-09-07 | https://www.youtube.com/watch?v=b4p_tcLYDV0 | supplied | 2026-10-12 | FULL | 14407 words; 1:20:48 (4848 s) | SRT, 2626 cues; TXT | 30 PNG |
| `S-05-sc1guyo5Rso/` | S-05 (video sc1guyo5Rso) | Value Oriented Programming Part V - Return of the Values - Tony Van Eerd - C++Now 2024 | Tony Van Eerd (in title; channel CppNow) | 2024-07-27 | https://www.youtube.com/watch?v=sc1guyo5Rso | supplied (not discovered); added later in the session | 2026-10-12, later in the session | FULL | 18368 words; 1:42:03 (6123 s) | SRT, 3248 cues; TXT | 30 PNG |

Files per folder:

- `S-01.txt`: extracted body text with a header block. `S-01-raw.html`: the fetched page, byte copy (35634 bytes).
- `S-02-2OMRWPOSw9s/`: `2OMRWPOSw9s-metadata-trimmed.json`, `2OMRWPOSw9s-transcript-provenance.txt`, `2OMRWPOSw9s-transcript.srt`, `2OMRWPOSw9s-transcript.txt`, `frames/` (30 PNG, named `2OMRWPOSw9s-HHhMMmSSs.png`, listed in `index/frames-2OMRWPOSw9s.md`).
- `S-03-W2tWOdzgXHA/`: `W2tWOdzgXHA-metadata-trimmed.json`, `W2tWOdzgXHA-transcript-provenance.txt`, `W2tWOdzgXHA-transcript.srt`, `W2tWOdzgXHA-transcript.txt`, `frames/` (30 PNG, listed in `index/frames-W2tWOdzgXHA.md`).
- `S-04-b4p_tcLYDV0/`: `b4p_tcLYDV0-metadata-trimmed.json`, `b4p_tcLYDV0-transcript-provenance.txt`, `b4p_tcLYDV0-transcript.srt`, `b4p_tcLYDV0-transcript.txt`, `frames/` (30 PNG, listed in `index/frames-b4p_tcLYDV0.md`).
- `S-05-sc1guyo5Rso/`: `sc1guyo5Rso-metadata-trimmed.json`, `sc1guyo5Rso-transcript-provenance.txt`, `sc1guyo5Rso-transcript.srt`, `sc1guyo5Rso-transcript.txt`, `frames/` (30 PNG, listed in `index/frames-sc1guyo5Rso.md`).

## secondary/

Discovered, not supplied by the stakeholder. D-01 and D-02 are linked from S-01's body. D-03 was found independently.

| file | ID | title | author | year | URL fetched | supplied or discovered | status | words | note |
|---|---|---|---|---|---|---|---|---|---|
| `D-01/D-01-original.pdf`, `D-01/D-01.txt` | D-01 | On the Criteria To Be Used in Decomposing Systems into Modules | D.L. Parnas, Carnegie-Mellon University (as printed) | 1972 (as printed; Comm. ACM 15(12)) | https://wstomv.win.tue.nl/edu/2ip30/references/criteria_for_modularization.pdf (mirror; the URL linked from S-01, cs.umd.edu, returned 403) | discovered (not supplied) | FULL (PDF text layer, `pdftotext -layout`, no OCR) | 4891 | Linked from S-01. Host is a university course folder, not the ACM. See Licensing. |
| `D-02/D-02.txt`, `D-02/D-02-transcription-original.html` | D-02 | On the role of scientific thought (EWD 447) | Edsger W. Dijkstra | 1974 (printed "30th August 1974") | https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html (transcription); PDF at https://www.cs.utexas.edu/~EWD/ewd04xx/EWD447.PDF | discovered (not supplied) | FULL as text (third-party transcription, Richard Walker per the page). PDF pages 2 to 7 are scans with no text layer | 3307 | Linked from S-01 (PDF link). See Licensing. |
| `D-02/D-02-original.pdf` | D-02 | On the role of scientific thought (EWD 447) | Edsger W. Dijkstra | 1974 | https://www.cs.utexas.edu/~EWD/ewd04xx/EWD447.PDF | discovered (not supplied) | held out of the repo (see Licensing) | n/a | Kept at `/tmp/<scratch>/held-out/D-02/D-02-original.pdf`. |
| `D-03/D-03.txt`, `D-03/D-03-original.html` | D-03 | The Principles of OOD | Robert C. Martin (attribution from the brief; not printed on the page) | not recorded (no article date; earliest dated item is a 2005 reader comment) | http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod | discovered (not supplied) | FULL (article only; reader comments excluded) | 732 | Not linked from any supplied source. No licence found. |

Words for D-01, D-02, D-03 are body words (header excluded). `D-01/D-01.txt` and `D-03/D-03.txt` start with a header block (`ID:`, `TITLE:`, `AUTHOR:`, `YEAR:`, `URL FETCHED:`, `EXTRACTION METHOD:`).

## Transcription

- Tool: MacWhisper 15.0.1 (1502), bundled CLI `mw`.
- Model: `parakeet-pro:nvidia_parakeet-v3` (from the provenance files).
- Language: en (passed explicitly).
- The transcripts are the unedited MacWhisper outputs. Nothing was corrected, cleaned or summarised.
- SRT cues carry `Speaker N:` prefixes (diarization was on). The TXT has none. The speaker labels were not checked against the audio. The S-05 report records skew: Speaker 1 holds 2896 of 3248 cues (89%), and labels run up to Speaker 9.
- The ASR writes `<unk>` for "++" and similar. Counts of `<unk>` (identical in SRT and TXT): S-02 = 5, S-03 = 6, S-04 = 0, S-05 = 11.
- The ASR misspells names. Example: the S-02 transcript says "Tony Veneard" (2 occurrences in the TXT) for Tony Van Eerd. Nothing was corrected.
- YouTube auto-captions (VTT files in `/tmp/<scratch>/captions/`) were fetched only as supplementary timing aids. They are not in the repo and are not indexed as transcripts. For S-03 the `en` caption track returned HTTP 429 and only `en-orig` was written.

## Frames

- Selection: a separate step read each transcript and picked timestamps. A later step grabbed each PNG with `ffmpeg -ss <t> -i <video> -frames:v 1` and described it by viewing it. Each video has an index at `index/frames-<videoID>.md`.
- The "expected" content in the plans was written from the transcript alone, and it was often wrong. For S-02 the expectation was "no" in 13 of 30 rows. Read the "what the frame shows" column, not the motivating passage, for what is on screen.
- Tallies are the `matches expectation` column of each index.

| video | PNG count | yes | partly | no | folder size (`du -sk`, `frames/`) |
|---|---|---|---|---|---|
| S-02 2OMRWPOSw9s | 30 | 7 | 10 | 13 | 5552 KB |
| S-03 W2tWOdzgXHA | 30 | 18 | 8 | 4 | 3396 KB |
| S-04 b4p_tcLYDV0 | 30 | 21 | 9 | 0 | 21396 KB |
| S-05 sc1guyo5Rso | 30 | 20 | 7 | 3 | 21788 KB |

Re-grabbed frames (from the anomaly sections of each index). The file kept is named; the planned timestamp is in brackets.

- S-02: `00h11m17s` [planned 00:11:13, which was black]; `00h22m04s` [planned 00:22:02, a ring animation]; `00h31m57s` [planned 00:31:55, caught mid-glitch]. `00h08m14s` was kept at its planned time, although it is a ring animation; its re-grabs were also rings or black and were discarded.
- S-03: `00h00m39s` [planned 00:00:35]; `00h01m40s` [planned 00:01:38]; `00h04m48s` [planned 00:04:44]; `00h06m01s` [planned 00:05:57]; `00h49m10s` [planned 00:49:06, a best-available fallback that does not match the plan].
- S-04: none.
- S-05: `01h09m54s` [planned 01:09:50]; `01h38m57s` [planned 01:38:53]. Neither re-grab shows the expected content.

## Licensing and redistribution flags

- **S-01** (blog post): the page has no licence or copyright statement (`blog-fetch.md`). The author's copyright applies by default. Held as a private research copy.
- **S-02 to S-05** (YouTube videos): the `license` key is absent from each metadata JSON. The reports record it as null or absent. The transcripts and frames are derivatives of the third-party talks and uploads.
- **S-03**: the upload is a re-upload by channel 25msr, dated 2017-05-25. It is not the original GoingNative/Microsoft channel, and not the speaker.
- Audio and video files are deliberately not stored in the repo.
- **D-01**: the ACM permission notice, verbatim from `discovery-D-01.md` (p. 1053):
  > Copyright @ 1972, Association for Computing Machinery, Inc.
  > General permission to republish, but not for profit, all or part of this material is granted, provided that reference is made to this publication, to its date of issue, and to the fact that reprinting privileges were granted by permission of the Association for Computing Machinery.

  The condition is "not for profit", and the reference must be kept. The host (a TU Eindhoven course folder) gives no notice of its own. Flagged.
- **D-02**: the Springer-Verlag notice, verbatim from `discovery.md` (PDF page 1):
  > The following manuscript
  > EWD 4 4 7 : On the role of scientific thought
  > is held in copyright by Springer-Verlag New York.
  > The manuscript was published as pages 60–66 of
  > Edsger W. Dijkstra, Selected Writings on Computing: A Personal Perspective, Springer-Verlag, 1982. ISBN 0–387–90652–5.
  > Reproduced with permission from Springer-Verlag New York.
  > Any further reproduction is strictly prohibited.

  The PDF was removed from the repo and kept at `/tmp/<scratch>/held-out/D-02/D-02-original.pdf` (sha256 `48a6a3aec4f50c3f4891ac03880f7238fdefe5e80f466f85d792a16352179c2c`). `D-02.txt` and `D-02-transcription-original.html` are still present and flagged. The transcription page carries no copyright line. Recommend the owner decide before publishing.
- **D-03**: no licence or copyright statement was found on the page (`discovery.md`).

Nothing here is cleared for redistribution outside the research use; decide before any push.

## interleaved/ (derived files)

Derived files, not sources. The sources are the transcripts and frames under `primary/`.

- `interleaved/S-02-2OMRWPOSw9s.md`, `S-03-W2tWOdzgXHA.md`, `S-04-b4p_tcLYDV0.md`, `S-05-sc1guyo5Rso.md`: one time-ordered document per video. Each SRT cue is a line `[hh:mm:ss] <cue text>` in transcript order. Each of the 30 frames is inserted after the last cue starting at or before the frame's timestamp, as a quoted block with the PNG link and the extraction of that PNG. Built mechanically by script from `primary/S-0N-<id>/<id>-transcript.srt` and `interleaved/extractions/S-0N/`. Cue text and extractions are verbatim. The scripts (`build_interleaved.py`, `verify_interleaved.py`, `check_extractions.py`) are in `interleaved/scripts/`, copied from `/tmp/<scratch>/scripts/` where they were run, with two edits. The `ROOT` constant of each script (`build_interleaved.py` line 14, `verify_interleaved.py` line 14, `check_extractions.py` line 11) was changed from the original scratch folder path to `/Users/ryzhakar/LLM_MANIFESTOS/resources/2026-10-12-source-dump`. In the `check_extractions.py` docstring (line 2) the one word between `sample for` and `frame extractions` was removed. A diff against the originals shows no other difference.
- Verified by `verify_interleaved.py`, PASS for all four files: cue texts equal the SRT in order (776, 1869, 2626 and 3248 cues); frame blocks equal the PNGs, each exactly once (30 of 30 per file, no duplicates); links resolve (30 of 30); each quoted block equals its extraction file byte for byte (30 of 30); each frame sits in its placement gap (30 of 30).
- `interleaved/extractions/`: 120 text files, one per PNG (`S-02/` to `S-05/`, 30 each), with sections ON-SCREEN TEXT, VISUAL and NOTES. Each was written by reading its PNG afresh with a vision model (haiku-class workers). The earlier frame descriptions in `index/frames-*.md` were not used.
- Quality process, from the reports in `interleaved/extractions/_checks/`:
  - Round 1, an independent re-read of 5 random frames per video: S-02 5 OK, 0 PROBLEMS; S-03 5 OK, 0 PROBLEMS; S-04 0 OK, 5 PROBLEMS; S-05 3 OK, 2 PROBLEMS.
  - All 30 S-04 extractions were re-extracted after round 1. Seven S-05 extractions differ from the first version (28m31s, 33m05s, 35m06s, 51m29s, 55m23s, 56m56s, 01h38m57s). The reports do not state why 55m23s, 56m56s and 01h38m57s were rewritten. S-02 and S-03 were not re-extracted.
  - Round 2, a re-read after re-extraction: S-04, 8 frames, 3 OK and 5 PROBLEMS; S-05, 4 frames (28m31s, 51m29s, 33m05s, 35m06s), 0 OK and 4 PROBLEMS, the last two for the missing CHRISTIE wordmark only. The wordmark was then added to those files.
  - Contested frames, 11 in total, were sent to a sonnet adjudicator who re-read the PNG pixels: S-04 at 02m46s, 06m50s, 12m46s, 20m44s, 22m06s, 27m58s and 01h01m23s; S-05 at 28m31s, 33m05s, 35m06s and 51m29s. Of 73 claims: 62 CONFIRMED, 3 REFUTED, 8 UNSETTLED. CONFIRMED means the adjudicator agreed with the claim as the check stated it; REFUTED means the claim was wrong; UNSETTLED means the pixels do not decide it, and the extraction gives a bracketed description. Telling corrections in the report: the chalkboard word is "Marshell", not "Marshall" (S-04 12m46s); the presenter faces the viewer's right, not left (S-04 02m46s, 22m06s, 27m58s); "Tully" is legible and was wrongly marked [illegible] (S-05 28m31s).
  - Round 3, an independent haiku re-read of the seven S-05 extractions rewritten after round 1 (28m31s, 33m05s, 35m06s, 51m29s, 55m23s, 56m56s, 01h38m57s), checked against the final extraction files: 5 OK, 2 PROBLEMS. The round-2 S-05 report is kept as `interleaved/extractions/_checks/extraction-check2-S-05-stale.md`, because it predates the final files. The two remaining disagreements were left as they are. 00h55m23s: the CHRISTIE wordmark at the bottom right is missing from ON-SCREEN TEXT, and the device's position in VISUAL differs from the checker's reading (the checker has it held in his hand beyond the lectern's right edge, not on the podium top to his left). 00h56m56s: a partial "r" at the left edge of the lectern panel is missing from ON-SCREEN TEXT.
  - Frames checked by the rounds: S-02 5 of 30, S-03 5 of 30, S-04 8 of 30, S-05 7 of 30. The other frames were not checked by any round.
- Weak spot: small or faint text. This means chalkboard fragments behind the speaker, graph axis labels and corner logos. The reports record missed axis letters and the missed CHRISTIE wordmark. Some words are partial and are marked `[illegible]` in place. Frames never checked may contain misses.
- Tallies per video from `check_extractions.py` (NOTES `(none)` / files containing `[illegible]` / NOTES containing "uninformative"): S-02 27 / 0 / 0; S-03 16 / 1 / 3; S-04 0 / 6 / 0; S-05 16 / 4 / 2.
- Licensing: the slide text and code in the extractions carry the same licence flags as the frames and transcripts they come from. See `## Licensing and redistribution flags`.

## Not done

- No manifesto. No digest.
- No OCR. The D-02 scanned pages (2 to 7) were not read. The D-01 text layer is used as embedded, uncorrected.
- No sources beyond the five supplied and the three discovered. The D-02 PDF is held out. D-01 is from a mirror. D-03 reader comments are excluded.
