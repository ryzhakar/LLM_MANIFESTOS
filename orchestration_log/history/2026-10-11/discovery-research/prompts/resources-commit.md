Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it.

ROLE: You are making the fetched primary texts durable by copying them, unchanged, into a tracked folder of the repository and committing on the current branch.

CONTEXT: Repository /home/user/LLM_MANIFESTOS, branch claude/manifesto-design-discussion-liuuvf (confirm with `git branch --show-current`). The folder research/ is gitignored and will vanish with the container. Every text must be copied byte-for-byte from disk; nothing is written from memory or re-fetched. Commit rule from the owner: single-line conventional commit message, no body, no attribution trailers of any kind.

INPUT FILES:
1. /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/*.txt — the eleven primary copies plus supplementary files (L2-01-discussion, L2-02-dumped-retro, L2-03-dumped-bowers) and L1-04-full.txt if it exists
2. /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/discovery/evidence/*.txt — second sources fetched by the evidence surveyor
3. /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/discovery/**/* — any other fetched texts (breadth may have added some)
4. /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/index-lane1.md and index-lane2.md
5. /home/user/LLM_MANIFESTOS/research/manifesto-craft/sources.md
6. /home/user/LLM_MANIFESTOS/.gitignore

TASK:
1. Create /home/user/LLM_MANIFESTOS/resources/2026-10-11-code-liability-and-dependencies/ with subfolders primary/, secondary/, index/.
2. `cp -p` every file from input 1 into primary/, every file from inputs 2 and 3 into secondary/ (keep subfolder names under secondary/ when they exist), and inputs 4 and 5 into index/. Copy; never edit, rename, or reformat a text.
3. Verify every copy with `sha256sum` against its origin; list the pairs in the README.
4. Write resources/2026-10-11-code-liability-and-dependencies/README.md: one table for primary/ with columns ID | title | author | year | URL fetched | status (FULL/PARTIAL) | words, every cell taken verbatim from the 6-line headers of the copies and the fetch tables in index/; one table for secondary/ with file | title or URL as given in its own header or first lines | which survey fetched it (evidence or breadth, by folder); a note that research/ is gitignored and these copies are the durable record; the sha256 list. No prose about the texts' arguments.
5. Confirm `git check-ignore -v resources/` returns nothing (not ignored). If ignored, stop and report.
6. `git add resources/` then commit with exactly this message: `chore(resources): add fetched primary and secondary texts for code-liability and dependency substrate`
7. `git push -u origin claude/manifesto-design-discussion-liuuvf`; on a network failure retry up to 4 times with 2s, 4s, 8s, 16s waits.
8. Report `git log --oneline -1`, `git status --short`, and the file count committed.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/resources-commit-report.md

REPORT FORMAT:
(three binding lines)
# Resources Commit
## Files copied — table: destination | origin | sha256 match (yes/no) | bytes
## Commit — hash, message, branch, push result
## Skipped — anything not copied and why

SCOPE: Copy, verify, commit, push. Do not touch research/ contents, manifestos/, or any other tracked file. Do not add attribution lines. Do not create a new branch.

TOOLS: Bash for cp, sha256sum, git, find; Read for the index headers; Write for the README and the report.

End with a 3-sentence summary for a notification: files committed, commit hash, anything skipped.
