# Summary: unharness 3.6.0 — digests, minified session files, signatures, doctor

Shipped 2026-10-23: origin/main fb7e3ae, tag v3.6.0, plugin 3.6.0. Linear history, no merges, no trailers.

## What it does
- `unharness prompt --digests | --stack-digests [--overlap] | --minified`: manifestos render from digests (single or stack), the shortest exact cover wins; skills and files always ship in full; the condensed interplay/commitments pair loads under `--minified`. Full prompt here: 14 888 words; shortest mode: 5 653.
- Digest sources: `.claude/digests/` (local, wins) then `<registry>/digests/` and `digests/stacks/`; the `index.json` sidecar records each digest's manifesto hashes; `unharness stamp <digest>` writes it. A missing or stale digest refuses with the fix named (`/compile-digest`, `unharness stamp`).
- Signatures: every compiled artifact (interplay, commitments, their `.min` pair, digest index entries) is checked against canonical source hashes; mode never changes a signature, so commitments written against full manifestos load in digest mode.
- `unharness doctor [mode flags]`: config, element reachability, skill versions, digest coverage and cover, session-file signatures, preamble, claude/uv presence, installed plugin floor (3.6.0), prompt sizes. `OK|WARN|FAIL` lines, exit 1 on FAIL.
- `/compile-digest <names…>`: a session writes a local single or stack digest and stamps it. `/compile-commitments` now writes the full pair and the condensed pair.
- Every plugin hook stands down under `UNHARNESS=1` (drift-reminder and subagent-start were leaking the "Active bindings" line; found by the captures). Preamble now names the harness nudges and the empty turn as their complete answer.

## Evidence
- 190 tests, 25 hook tests, `claude plugin validate` passes.
- Reviews: code 0 blocking, spec 0, prose 2 (docs); 47 findings applied, 14 rejected, 9 deferred (reviews/digests-triage.md).
- E2E (verification-digests.md): 35 PASS, 0 FAIL; system block byte-equal to the compiled prompt before, during, and after /compact in the shortest mode; no CLAUDE.md/git/billing text.
- Git install line verified against the tag.

## For the owner
1. Update the installed plugin to 3.6.0 (`/plugin marketplace update`, `/reload-plugins`): doctor FAILs on 3.4.0 and its hooks still inject.
2. Queue 44 (unsolved): the rule for which demands a digest drops at its word cap.
3. Queue 45 (solved): under unharness, subagents get no binding from the plugin; alternative recorded.
4. Deferred: Block/Document merge; BrokenPipeError on `stack | head`; PyPI publish as before.
5. Conduct: three silence breaches and a run of padding calls this span, logged; the preamble paragraph (P1) is the shipped antidote.
