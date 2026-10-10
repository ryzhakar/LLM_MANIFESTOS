BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines through `</instruction_matrix>`); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full
INTERPLAY: All four demand the verified text over the remembered name and the flat claim over the hedge; Strunk's judgment latitude and manifesto-writing's fury register pull against a reviewer's literal check, resolved: the check runs on the located source line, the register earns no allowance on a fact, and the owner rulings overrule the spec.
COMMIT: I must test every figure and boundary against a quoted source line, and I will rate each VERIFIED, QUALIFIED, UNVERIFIED, or CONTRADICTED with file:line; I must not rewrite the draft or judge outside accuracy, and I will give only the smallest compliant fix; I must treat a sentence that outruns its source as a finding, and I will not excuse it for register.

# Review — accuracy — v2.md
Verdict: FAIL (2)

## Findings

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| 1 | v2.md:29 | "First-time code is DEBT. A little buys speed if you consolidate it promptly; unpaid, it's interest your "Done" books as income." | Boundary B2 and axiom A1 limit: the source says shipping first-time code is LIKE going into debt (an analogy, scoped to shipping); the draft states identity and drops "shipping". Second clause: the source keeps debt and interest apart (unrepaid debt is the danger; each minute spent on not-quite-right code counts as interest); the draft calls the unpaid debt itself interest. Identity "code is debt" also nears the §8 CONTRADICTED "liability" claim. | "Shipping first-time code is like going into DEBT. A little buys speed if you consolidate it promptly. Unpaid, every minute on it is interest your "Done" books as income." (each sentence under 20 words; "a little" and "promptly" kept per ruling 2) | L1-03.txt:16 "Shipping first time code is like going into debt." and "Every minute spent on not-quite-right code counts as interest on that debt."; verify-axioms.md:153-154 (frame labelled analogy); SPEC.md:135 (B2 "first-time code shipped") |
| 2 | v2.md:33 | "Code that gets better over time is the frontier; counting output never gets you there." | UNVERIFIED: the clause after the semicolon is a universal causal claim ("never") with no source line; B1 carries only the two source sentences. Owner ruling 3 bars a behavior assertion with no VERIFIED §7 figure behind it. | Cut the clause: "Code that gets better over time is the frontier." | L1-04-full.txt:34 "Code that gets better over time." and :36 "This is the frontier."; SPEC.md:134 (B1); r1-rulings.md:3 |

### Figure ratings (rubric step 1)

| fig | draft line | draft wording | §7 wording match | rating | source checked |
|---|---|---|---|---|---|
| V1 | v2.md:49 | "Models invent package names: on average at least 5.2 percent for commercial models, 21.7 for open ones." | exact | VERIFIED | spracklen-abs.txt:35 "the average percentage of hallucinated packages is at least 5.2% for commercial models and 21.7% for open-source models"; subject "models" held |
| V2 | v2.md:49 | "Where models pin versions, 36.70 to 55.70 percent of tasks carry a known CVE." | exact; the allowed second sentence omitted | VERIFIED | wang-vulndeps-abs.txt:33 "Among the specified versions, 36.70%-55.70% of tasks contain at least one known CVE" |
| V3 | v2.md:16 | "Repositories that took on an AI coding agent added 281.3 percent more lines in month one." | exact | VERIFIED | he-cursor-v3.txt:2395 "a 281.3% increase in lines added in the first month" |
| V4 | v2.md:16 | "Static-analysis warnings rose 30.3 percent. Complexity rose 41.6 percent. Both stayed up." | exact | VERIFIED | he-cursor-v3.txt:2404 "static analysis warnings increase significantly by 30.3%, and code complexity increases by 41.6%"; :2408 "persists beyond the initial adoption period" |
| V6 | v2.md:51 | "On 22 March 2016 one author unpublished 273 packages. One was left-pad." | exact | VERIFIED | npm-kik-leftpad.txt:71-76 "kik package and 272 other packages. One of those was left-pad."; evidence.md:361, :376, :406 |
| V7 | v2.md:51 | "left-pad was a single eight-line function body." | exact; "function body" kept | VERIFIED (non-blank count) | L2-05.txt:113 "a single 8-line function body"; evidence.md:377 |

Quotes: v2.md:14 and :76 repeat candidate 1 verbatim (SPEC.md:27). The body quotes no other source. Attribution (v2.md:84) matches SPEC.md:244 character for character.

## Notes
- §8 scan of the whole draft (liability, asset, rot, wear, fewer bugs, Equifax, Chrome, Struts, CVE-before-cutoff, hobby clause, vetting-is-safe): zero hits. Axioms A1-A4 carry their §5 limits.
- v2.md:16 "Your count, at SCALE." and v2.md:49 "You're ONE." apply V3, V1, V2 to the reader in the sentence after the figure, as SPEC.md:84 and ruling 3 allow; limits stand: V3 underlying models unfixed (breadth.md:142), V1 covers 16 models of 2024 (breadth.md:138).
- v2.md:47 "upkeep falls on most, not all" follows the A3 writer rule and ruling 4; the source limit is "most of the interesting parts" (L1-04-full.txt:26). Spec wording, no finding.
- Read the draft, spec, r1-rulings, and primary and breadth sources only; no other reviewer.
