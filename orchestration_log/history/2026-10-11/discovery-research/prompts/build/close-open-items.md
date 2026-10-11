Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it.

ROLE: You are closing the collection's open items so nothing remains for the owner.

CONTEXT: Repository /home/user/LLM_MANIFESTOS, branch claude/manifesto-design-discussion-liuuvf. Another agent is writing under drafts/; do not touch drafts/. Commit rule: single-line conventional, no attribution trailers, atomic by artifact class, explicit paths. Owner rulings: (a) every manifesto carries an attribution line; transformed texts "After [authors]"; canon "by [author], [year]"; a text with no external source reads "Original, [year]" with the year from `git log --diff-filter=A --format=%ad --date=short -- <file>`; (b) the QuickDraw source tree under resources/ carries a non-commercial-use COPYRIGHT.TXT and leaves the repository; its README rows stay with a note "removed: non-commercial license; sha256 kept"; (c) deferred items OQ-004, OQ-005 and OQ-006 are resolved by this work or by the plugin branch; record the hashes.

INPUT FILES: /home/user/LLM_MANIFESTOS/manifestos/intervention.md, self-documenting-code.md, postgres.md, cargo-cult-science.md (frontmatter and the first and last 15 lines of each); /home/user/LLM_MANIFESTOS/archive/software_building_principles/SELF_DOCUMENTING_CODE.md (for the authors it cites); /home/user/LLM_MANIFESTOS/orchestration_log/history/2026-05-11/session.md lines 12-20 (postgres substrate provenance); /home/user/LLM_MANIFESTOS/orchestration_log/reference/deferred_items.md; /home/user/LLM_MANIFESTOS/resources/2026-10-11-code-liability-and-dependencies/README.md; `find /home/user/LLM_MANIFESTOS/resources -iname 'COPYRIGHT*'`.

TASK:
1. Attribution: self-documenting-code.md gets "*After [the authors the archive source names, in its order]*" as its last line after a `---`; postgres.md gets "*After the maintainer's raw materials, 2026-05-11*"; intervention.md gets "*Original, [year of its first commit]*"; cargo-cult-science.md's byline gains the year 1974 in the form "*by RICHARD P. FEYNMAN, 1974*". Change nothing else in the bodies. Run the generator and tests (`python3 generate.py`, `python3 tests/test_generate.py`) green. Commit `chore: attribution lines on four manifestos` (the four files) and `chore: regenerate README` if README changed.
2. QuickDraw: locate the directory holding COPYRIGHT.TXT under resources/; `git rm -r` it; edit the resources README so its rows read "removed: non-commercial license; sha256 kept" (keep the sha256 values). Commit `chore(resources): remove QuickDraw source, non-commercial license`.
3. deferred_items.md: mark OQ-006 resolved with the attribution commit hash; mark OQ-004 and OQ-005 resolved "on claude-skills branch manifesto-binding-channel" (the plugin agent is committing those now; write the branch name, not a hash). Commit `doc: deferred items — OQ-004, OQ-005, OQ-006 resolved`.
4. Push with retries (2s, 4s, 8s, 16s); if rejected because the remote moved, `git pull --rebase` and push once; never force.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/close-open-items-report.md

REPORT FORMAT:
(three binding lines)
# Close open items
## Attribution lines — file | line added | source of the names
## QuickDraw — path removed, file count, README rows changed
## Deferred — items and their resolution text
## Commits — hash | message
## Push

SCOPE: Only the files named. No drafts/. No body edits beyond the attribution lines.

TOOLS: Read; Edit; Bash; Grep; Write.

End with a 3-sentence summary for a notification.
