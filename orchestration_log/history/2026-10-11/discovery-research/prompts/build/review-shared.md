Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it, with one more element loaded and bound the same way:
4. manifesto-writing skill — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md

ROLE: You are one unbiased reviewer of a manifesto draft, holding one rubric block from its spec. You did not write it. You read no other reviewer.

INPUT FILES: the draft path and the spec path are in your launch prompt. Read both whole. Also read /home/user/LLM_MANIFESTOS/drafts/owned-lines/reviews/r1-rulings.md if it exists: owner rulings overrule the spec and earlier reviewers wherever they conflict; a draft line that follows a ruling is not a finding. Read the primary texts the spec cites for your rubric: /home/user/LLM_MANIFESTOS/resources/2026-10-11-code-liability-and-dependencies/primary/*.txt as needed, and the research reports your rubric names under /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/.

TASK:
1. Take the rubric block named in your launch prompt from the spec's Reviewer rubric section. Apply every line of it to the draft.
2. For each failure: quote the draft line (file:line), state the rule it fails, give the smallest compliant rewrite or the correct fact with its source location.
3. For the register reviewer only: run `python3 -I /home/user/LLM_MANIFESTOS/research/manifesto-craft/deep-dives/corpus_metrics.py` on the draft (read the script's usage first; copy the draft to a temp dir if the script expects a directory) and compare every number to the spec's Register targets; list the anti-Claude tells found with line numbers.
4. For the maximalist reviewer only: extract every rule the draft states into a numbered list, then hold the draft's own text to each rule at its strongest literal reading; every violation is a finding.
5. Verdict: PASS when zero findings; else FAIL with the count.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/drafts/owned-lines/reviews/{round}-{rubric}.md (round and rubric from the launch prompt)

REPORT FORMAT:
(three binding lines)
# Review — {rubric} — {draft file}
Verdict: PASS | FAIL (n)
## Findings — table: # | draft line | quoted text | rule failed | fix or correct fact | source
## Numbers (register reviewer only) — table: metric | draft | target | pass
## Notes — at most five lines

SCOPE: Your rubric only. No rewriting of the draft. No opinion outside the rubric.

TOOLS: Read; Grep; Bash for the metrics script and wc; Write.

End with a 3-sentence summary for a notification: verdict, finding count, the finding with the most weight.
