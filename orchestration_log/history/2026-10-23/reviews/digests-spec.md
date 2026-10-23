# Spec review of unharness 3.6.0 (branch feat/digests, head f38fb14)

Spec: `spec-unharness.md` part "3.6.0", lines 125-267. Owner answers: `queue-long-run.md` entries 27-41. Product files read only.

Checks run:

- `uv run --project plugin/unharness pytest -q plugin/unharness`: 166 passed.
- `claude plugin validate plugin`: passed.
- `--help` of every verb: `prompt` and `doctor` take the four mode flags; `stack` takes slugs and `--config`; `stamp` takes DIGEST and `--config`; `launch` takes no mode flag.
- Hand runs against the branch's plugin folder with this repo's config. `--digests`, `--stack-digests`, `--stack-digests --overlap`, `--minified`, and `--stack-digests --overlap --minified` exit 0; `--overlap` alone exits 1 with its message.
- Re-stamped every shipped digest into a copy of `plugin/digests`; the copy's `index.json` equals the shipped one, and every digest file has an entry.
- A scratch project whose element name differs from its slug (`my-dry` for `dry`): stamp, `stack dry kiss`, cover selection, rendered tags, and doctor all key by slug.
- Both repo `.min.md` files hold the same `<stack>` block as their full files. Interplay body: 437 words against a limit of 617. Commitments body: 135 words against a limit of 138, with one line for each of the 8 elements.

## Blocking

None found.

## Should fix

1. `plugin/unharness/tests/test_digests.py:56-60` and `plugin/unharness/tests/test_cli.py:140-177`: the spec test item "session files compiled against the full stack load under `--stack-digests --overlap --minified`" (spec line 250) has no test. The digest tests write only the full pair, and the minified tests never pass a digest flag. The behavior works (hand run, exit 0), but nothing guards the claim of spec line 196 that a flag combination never changes a signature. Fix: add one test in `test_digests.py` that writes both pairs from the full stack and runs `prompt --stack-digests --overlap --minified`.

2. `plugin/unharness/tests/test_digests.py` (whole file) and `test_doctor.py`: no test uses an element whose name differs from its slug, such as `name: my-dry` with `source: manifesto dry`. Decision 1 (spec line 257) and the term at spec line 132 rest on `manifesto_slug` and `manifesto_elements` in `resolve.py:31-38`, and on `digests.py:73`, `digests.py:235-236`, and `digests.py:262`, where hashes and stems key by slug and tags by element name. A regression to keying by name would pass the suite. Fix: add a test with a renamed element that checks the stamp key, the single digest lookup, and the stack tag `my-dry+kiss`.

3. `plugin/skills/compile-digest/SKILL.md:65-71` (`confirm-the-compile`): the skill runs `unharness prompt --digests` or `--stack-digests` after stamping. The spec's six steps (lines 228-233) end at the stamp, and the skill's own `write-the-file` section says "Stop at the digest and its stamp" (line 56). The extra step contradicts that line and is behavior the spec lacks. Fix: delete the section, or add the compile as a seventh spec step and reword line 56.

4. `plugin/unharness/src/unharness/doctor.py:91,97,102`: when any element fails to resolve, the digest, cover, session-file, and prompt-size checks vanish with no line. Spec line 200 promises "one line per check", and the table (lines 202-214) names no such omission. `test_doctor.py:463` asserts the omission, so it is deliberate. Fix: add one sentence to spec line 204's row stating that an unresolved element leaves out the four checks that need the stack, or print a WARN line for each skipped check.

5. `plugin/.claude-plugin/plugin.json:3`, `.claude-plugin/marketplace.json:11`, and `plugin/unharness/pyproject.toml:3` still read 3.5.0. The spec part is titled 3.6.0, and queue 34 ships and tags 3.6.0. Fix: bump the three files in the release step, and confirm `doctor`'s 3.5.0 floor (`doctor.py:40`) stays correct. This is not a code defect if the release step owns the bump.

## Nits

1. `plugin/unharness/src/unharness/doctor.py:226`: with `uvx` on PATH and `uv` absent, the OK detail reads `None /path/uvx`. Spec line 212 says the detail holds the paths of `uv` and `uvx`. Fix: join only the paths that exist.

2. `plugin/unharness/src/unharness/doctor.py:214-215`: a `claude` that prints no version gives a WARN. Spec line 211 lists two WARN causes, not on PATH and a differing version. Fix: add the third cause to the spec row.

3. `plugin/unharness/src/unharness/digests.py:108`: a local stack file with an unsorted stem, such as `kiss+dry.md`, never becomes a candidate and raises nothing, while `stamp` refuses the same name (line 258). Spec lines 138 and 151 define sorted stems but say what `prompt` does with a hand-named file nowhere. Fix: state in the spec that such files are ignored, or have doctor WARN on them.

4. `plugin/unharness/src/unharness/digests.py:256,258-259`: the stamp refusals "no digest at ..." and "... is not named by sorted, distinct slugs joined by +" are not in the spec, which gives verbatim text only for the four prompt refusals. The check for an empty slug (`"" in slugs`) is also unspecified. Fix: add the two messages and the empty-slug case to spec line 151.

5. `.manifestos.commitments.min.md:16` begins "I must not fool myself". Spec line 191 asks for one `I must ..., and I will ...` line per element. The full file uses the same opening, so the choice follows its source. Fix: either accept it, or word the line "I must report every doubt, and I will not fool myself".

6. `plugin/skills/compile-commitments/SKILL.md` (`write-the-minified-pair`, last paragraph): the `sed ... | wc -w` count applies to the min file only; the skill does not say to count the full body and divide by three. Spec line 190 sets the limit as one third of the full body. Fix: add "against one third of the same count on the full file".

7. `plugin/skills/compile-digest/SKILL.md` lines 25-28 restate Strunk's rules in a short list, where spec step 4 says "Strunk applied". The skill never names write-well or Strunk. Fix: add one line naming Strunk's rules, if the owner wants the source named.

## Spec statements against code

Every statement in lines 125-267 was traced to code or a test. Mismatches are listed in full above; none was found in the code itself. Implemented behavior the spec lacks:

| Code | Behavior | Spec |
|---|---|---|
| `doctor.py:91,97,102` | checks drop when an element fails | silent (Should fix 4) |
| `doctor.py:214` | WARN when `claude` prints no version | silent (Nit 2) |
| `digests.py:108` | unsorted local stems are ignored | silent (Nit 3) |
| `digests.py:256,258-259` | text of two stamp refusals, empty-slug refusal | silent (Nit 4) |
| `compile-digest/SKILL.md:65-71` | compile run after the stamp | silent (Should fix 3) |
| `plugin/digests/index.json` | shipped index of the 14 single digests and the one stack digest | spec line 148 describes the plugin index; no line says the release ships it. Contents verified current. |

Test items of spec lines 245-253 without a test: the combined `--stack-digests --overlap --minified` load (Should fix 1), and the end-to-end run of `/compile-digest`, which needs a live session and has no pytest form. The `launch` verb rejecting mode flags (line 239) is also untested; `argparse` enforces it.

## The 11 decisions

| # | Decision | Code honors it | Test |
|---|---|---|---|
| 1 | Plugin folder holds `manifestos/` and `digests/`; digests key by slug | Yes: `resolve.py:31-45`, `digests.py:73` | Folder yes; name against slug no (Should fix 2) |
| 2 | Own message when each manifesto is covered but no disjoint choice exists | Yes: `digests.py:136,220-222` | Yes: `test_digests.py:352` |
| 3 | Every considered digest must be usable | Yes: `digests.py:173-186` | Yes: lines 132, 179, 415 |
| 4 | Local wins per stem, even when stale | Yes: `digests.py:95-98,105-109` | Yes: lines 121, 132 |
| 5 | Stale names `/compile-digest`; only a missing entry names `stamp` | Yes: `digests.py:119,122` | Yes: lines 154, 179 |
| 6 | Stack block at first member; tag by `+` of element names; `governs` by `; `, config order | Yes: `digests.py:230-250` | Yes: lines 217, 365, 380 |
| 7 | `stack` takes slugs and no mode flag | Yes: `cli.py:33-36,92-93` | Yes: lines 110, 529 |
| 8 | `/compile-digest` composes from full manifestos, writes no eval record | Yes: skill lines 20-22, 38, 53-56 | Skill text only |
| 9 | Min body at most one third of the full body; min commitments one line per element | Yes in the skill and in this repo's pair; no code enforces it, and the spec asks for none | n/a |
| 10 | Doctor FAILs on what the flags load, WARNs on the rest; missing `claude` WARN; cover falls back to `--stack-digests --overlap` | Yes: `doctor.py:156-169,208-212,256-281,297-301` | Yes: `test_doctor.py:233-248,328-428` |
| 11 | Stamp writes sorted, two-space JSON, prints one line | Yes: `digests.py:262-264`, `cli.py:80-82` | Yes: `test_digests.py:429` |

## Counts

Blocking 0. Should fix 5. Nits 7.
