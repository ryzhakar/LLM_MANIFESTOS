BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full; manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full
INTERPLAY: First Principles and manifesto-writing both demand the verified atom over the inherited claim and converge on striking every figure that fails its source; Strunk's judgment latitude pulls against the spec's literal figure wording, resolved: spec wording and owner rulings decide, the primary text decides what the spec leaves open.
COMMIT: I must trace every figure, quote, and limit to a file:line, and I will list a mismatch only with the quoted draft line and the source; I must not rewrite the draft or judge outside accuracy, and I will give the smallest compliant fix; I must not let a spec or ruling stand in for a source check, and I will rate every figure VERIFIED, QUALIFIED, UNVERIFIED, or CONTRADICTED.

# Review — accuracy — v3.md
Verdict: FAIL (2)

Paths. Draft = /home/user/LLM_MANIFESTOS/drafts/owned-lines/v3.md. Spec = .../SPEC.md (§5 axioms, §7 figures, §8 forbidden, §9 boundaries). `bz` = /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/discovery/breadth/ (spracklen-*, wang-vulndeps-*, he-cursor-v3, npm-kik-leftpad, L1 files named bare); `breadth.md` and `evidence.md` and `verify-axioms.md` = .../manifesto-craft/discovery/; `L2-05:n` = /home/user/LLM_MANIFESTOS/resources/2026-10-11-code-liability-and-dependencies/primary/L2-05.txt line n. Labels: doctrine = the spec or a primary text states it.

## Findings

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| 1 | v3.md:38 | "Good software is out there, and reusing it is your job, until you pull a package unopened." | B5 states what the enemy is not (vetted reuse); the draft turns it into a duty. No source says reuse is the reader's job. Cox's own limits point the other way: a tiny dependency may be copied, an unisolatable one avoided. SPEC §16 sets no threshold between copying and depending. Doctrine. | "Good software is out there. Open it, then reuse it." Carries B5 without a duty. | L2-05:195 "There’s a lot of good software out there. Let’s work together to find out how to reuse it safely."; L2-05:177; L2-05:137 "the best answer may be to avoid it entirely"; L2-05:141 "A little copying is better than a little dependency."; SPEC §9 B5; SPEC §16 |
| 2 | v3.md:64 | "Models invent package names: on average at least 5.2 percent for commercial models, 21.7 for open ones. Where models pin versions, 36.70 to 55.70 percent of tasks carry a known CVE. You're a model. YOUR NUMBERS." | V1 limit not carried, then the sentence attributes the figures to the reader. V1 is 16 models of 2024; its commercial set is GPT-3.5, GPT-4, GPT-4 Turbo, no Claude; no current-model rate exists. V2 is ten models, one preprint, May 2026, no replication; the reader is none of them. "YOUR NUMBERS" claims the reader's own rate equals the study's. SPEC §7 limits the figure's subject to the study's subject. Doctrine. | Add the limit and name the class: "In 2024 tests, models invented package names: on average at least 5.2 percent for commercial models, 21.7 for open ones." and "You're a model. YOUR CLASS." (V2 sentence unchanged.) | SPEC §7 V1 verdict cell "16 models of 2024"; spracklen-v3.txt:509 (GPT series as the commercial models); breadth.md:231 R11 "Measured on 2024 models; no current-model rate found."; breadth.md:232 R12 "One preprint, May 2026; no replication found."; wang-vulndeps.txt:1483; SPEC §7 intro |

### Figure and quote ratings (rubric: rate every figure)

| draft line | item | rating | check against source |
|---|---|---|---|
| v3.md:64 | V1 5.2 / 21.7 percent | VERIFIED (wording exact; limit missing, finding 2) | spracklen-abs.txt:35 "at least 5.2% for commercial models and 21.7% for open-source models" |
| v3.md:64 | V2 36.70 to 55.70 percent | VERIFIED (wording exact) | wang-vulndeps-abs.txt:33 "Among the specified versions, 36.70%-55.70% of tasks contain at least one known CVE" |
| v3.md:64 | V3 281.3 percent, month one | VERIFIED (wording exact) | he-cursor-v3.txt:2395 "a 281.3% increase in lines added in the first month" |
| v3.md:64 | V4 30.3 / 41.6 percent, "Both stayed up" | VERIFIED (wording exact) | he-cursor-v3.txt:2404 and :2408 "persists beyond the initial adoption period" |
| v3.md:38 | V6 22 March 2016, 273 packages, left-pad | VERIFIED (wording exact) | bz/npm-kik-leftpad.txt:71-79 "Azer unpublished his kik package and 272 other packages. One of those was left-pad." failures from 2:30 PM, Tuesday, March 22 |
| v3.md:38 | V7 single eight-line function body | VERIFIED (wording exact; non-blank count; "function body" kept) | L2-05:113 "a single 8-line function body"; evidence.md:377 E141 |
| v3.md:14, :68 | enemy line, quoted twice | VERIFIED verbatim to SPEC §3 candidate 1 | SPEC §3 |
| v3.md:76 | attribution line | VERIFIED verbatim to SPEC §14 | SPEC §14 |
| v3.md:34 | debt boundary, both limits "a little" and "promptly" | QUALIFIED within limit (consolidate = rewrite) | L1-03.txt:16, :12; ruling 2 |
| v3.md:34 | "Code that gets better over time is the frontier." | VERIFIED (B1) | L1-04-full.txt:34, :36 |
| v3.md:38 | "designing, writing, testing, debugging, and maintaining" | VERIFIED verbatim | L2-05:16, :39 |
| v3.md:38 | "NEVER THE OUTAGE" | VERIFIED per ruling 1 | L2-05:61; ruling 1 |
| v3.md:42 | A4 head "lines of code written" | VERIFIED wording; QUALIFIED axiom, limit carried (lines removed, behaviour intact) | verify-axioms.md S3; L1-06.txt:28 |
| v3.md:22-30 | table rows 2, 3, 4, 6, 7 | VERIFIED against Cox (:141, :111/:167, :125, :151); row 5 "SPENT TWICE" is a derived count, see Notes | L2-05 |

No §8 claim appears in any wording: no "liability, not asset", no Equifax, Chrome, SQLite, pcregrep, n^2, 750,000, 30 percent, "fewer bugs", "ten small changes", rot or wear, hobby code, or overengineering assertion (grep on v3.md: zero hits).

## Notes
1. Applied without a finding: ruling 1 (outage), ruling 2 (debt limits), ruling 4 ("most of your code" follows the owner's "most code, not all"; the source reads "most of the interesting parts", L1-04-full.txt:26).
2. "Response four", "response ten", "response eleven" (v3.md:64) are the ruling-16 prediction form (stop-yapping.md:113 "Three responses in... Ten in"), not figures; no source rates them.
3. "SPENT TWICE" (v3.md:28) and "ZERO" (v3.md:42) are derived counts, not §7 figures: two implementations remain; lines written never count (SPEC §5 A4 writer rule).
4. A2 "Least means least work for ME" (v3.md:34) widens the spec's "least a reader must read" (L1-05.txt:35) to maintainer effort; L1-06.txt:30 and L2-02 (quoted in verify-axioms.md S4) support it. Within limit; the boundaries reviewer judges the wording.
5. The V6 unpublish date rests on npm's failure timeline (2:30 PM, 22 March), not on a stamped unpublish time; SPEC rates it VERIFIED.
