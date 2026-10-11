BOUND: First Principles (/home/user/LLM_MANIFESTOS/manifestos/first-principles.md, full); Strunk SPR v3 (/home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml, 2,923 lines, full); manifesto-oath (/home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md, full); manifesto-writing (/home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md, full).
INTERPLAY: All four demand the located source over the paraphrase and the definite claim over the hedge; Strunk's judgment latitude pulls against First Principles' refusal to inherit, and the review rules outrank the draft's register; resolved: a claim stands only with a source line, and no rating is granted on inheritance.
COMMIT: I must test each figure, quote, and claim against its source line, and I will quote the draft with file:line; I must not rewrite the draft or add opinion, and I will give the smallest fix and its source; I must rate every figure VERIFIED, QUALIFIED, UNVERIFIED, or CONTRADICTED, and I will leave none unrated.

# Review — accuracy — /home/user/LLM_MANIFESTOS/drafts/owned-lines/v1.md

Verdict: FAIL (4)

## Findings

SPEC = /home/user/LLM_MANIFESTOS/drafts/owned-lines/SPEC.md. Primary texts = /home/user/LLM_MANIFESTOS/resources/2026-10-11-code-liability-and-dependencies/primary/. Labels: doctrine = a text states it; learned = a record shows it; practiced = the shipped file does it.

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| 1 | v1.md:61 | "Pulled lines skip the writing. NEVER the debugging." | SPEC §4 D2 hinge: installing outsources the work, "never the outage". The draft says "never the debugging". Cox lists debugging among the work a dependency outsources, so the line contradicts its source at the literal reading (doctrine). Fix: "Pulled lines skip the writing. NEVER the outage." | L2-05.txt:39 "outsources the work of developing that code—designing, writing, testing, debugging, and maintaining"; L2-05.txt:61 "In the middle of a production outage, you’ll be the one debugging it."; SPEC.md:40 | L2-05.txt:39, :61; SPEC.md:40 |
| 2 | v1.md:30 | "Debt taken and repaid is not the enemy: first-time code shipped and then consolidated." | SPEC §5 A1 limit, §9 B2: the limit is "A little debt" repaid "promptly". The draft drops both and bounds the enemy at any repaid debt at any time (doctrine). Fix: "A little debt, repaid promptly, is not the enemy: first-time code shipped, then consolidated." B2 stays at two sentences. | L1-03.txt:16 "A little debt speeds development so long as it is paid back promptly with a rewrite." and "The danger occurs when the debt is not repaid." | L1-03.txt:16; SPEC.md:52, :135 |
| 3 | v1.md:28 | "You love the parallel path." | SPEC §7 and §8: a flat claim about model behavior with no §7 row; rated UNVERIFIED. SPEC §8 lists "models duplicate more" as VERIFIED counters: the duplicate-line-density effect is insignificant. Fix: cut the sentence; keep "A new helper beside the old one: both alive, both YOURS." as a noun phrase, then the command. | he-cursor-v3.txt:2405 "The effect on duplicate line density is insignificant."; the practice itself is human: L1-06.txt:30 "simply piling your new stuff on top of the old stuff" | he-cursor-v3.txt:2405; breadth.md:144 (F80); SPEC.md:120 |
| 4 | v1.md:36 | "No code is option ONE. You skip it." | SPEC §7 V5 and §8 "Claude overengineers, as fact": the only source is a publisher assertion with no measurement; declaring it flat turns assertion into fact. Rated UNVERIFIED. Fix: "No code is option ONE." and keep the next sentence as the command. | breadth-F85 "have a tendency to overengineer" cites no measurement; the demand stands on L1-05.txt:42 "because you completely exhausted all your other options" | breadth.md:149, :234 (F85, R14); SPEC.md:92, :124; L1-05.txt:42 |

## Notes

- Ratings: V1 (v1.md:55) VERIFIED; V2 (:57) VERIFIED; V3 (:18) VERIFIED; V4 (:18, "Both stayed up" = "persists beyond the initial adoption period", he-cursor-v3.txt:2406-2408) VERIFIED; V6 (:59) VERIFIED; V7 (:59) VERIFIED under a non-blank count (8 of 13 lines, left-pad 0.0.3). Six of six wordings match SPEC §7 verbatim (grep -F); V8-V15 absent; candidate 1 and the attribution match SPEC verbatim; no §8 term found (liability, asset, rot, Equifax, Chrome, n^2, fewer bugs).
- Spec conflict: SPEC.md:40 and :148 disagree (§4 "never the outage"; §10 "never the debugging"); finding 1 follows §4 because L2-05.txt:39 lists debugging as outsourced.
- Inside spec wording, outside source limits, not flagged: v1.md:55 "You're one." sets 2024-model rates (16 models) beside the reader, and no current-model rate exists (breadth.md:231); v1.md:34 "Maintainability wins EVERY tie" is narrower than L1-06.txt:30 "you should always favor maintainability".
- Not flagged: enemy-premise claims at v1.md:16 and :65 (owner-fixed, SPEC.md:12).
- Read no other reviewer; reviews/r1-completeness.md exists and stayed unread.
