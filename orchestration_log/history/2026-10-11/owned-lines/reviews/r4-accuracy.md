BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full
INTERPLAY: First Principles and the oath demand the located primary over the claim, while Strunk's judgment latitude pulls against First Principles' refusal to inherit; resolved: every verdict rests on a quoted source line, and the owner rulings overrule the spec wherever they conflict.
COMMIT: I must test each figure and quote against its source line, and I will rate or fail it by location; I must not rewrite the draft or opine outside the accuracy rubric, and I will give only the smallest compliant fix.

# Review — accuracy — v4.md
Verdict: FAIL (3)

## Findings

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| 1 | v4.md:38 | "Who pulls a stranger's EIGHT LINES into my build unopened? YOU. An owner who never looked." | r1-rulings #3: no sentence asserts a model behavior as fact unless a VERIFIED SPEC §7 figure backs it. V6 and V7 state what npm packages and one function body were, never what the reader pulls. The scene (v4.md:16) and the prediction (v4.md:64) are the two sanctioned behavior claims (ruling 16); this is a third. | Make it conditional: "Pulled unopened, a stranger's EIGHT LINES are yours. An owner who never looked." | r1-rulings.md:5 (#3), :18 (#16); SPEC.md:93-94 (V6, V7); L2-05.txt:113 (the "never looked" fact is about "many developers") |
| 2 | v4.md:42 | "Both stayed up. That agent is you." | SPEC §7 V3 limit: "VERIFIED, MODEL; underlying models unfixed". The study's agent is Cursor's LLM agent with models unfixed; the sentence identifies the reader with that agent. Class membership is the verified reach. | "You are an AI coding agent." | SPEC.md:90 (V3); breadth.md:142 (breadth-F78); he-cursor-v3.txt:2395 |
| 3 | v4.md:20 | `"I added." "I pulled."` | SPEC §15 accuracy: every quote matches its source verbatim. The quoted reflex has one source, the enemy line (v4.md:14 = SPEC §3 candidate 1): "I added a helper for the parsing and pulled in a library for the dates." "I pulled." occurs nowhere in it. | `"I added." "Pulled in."` (both fragments verbatim substrings of the enemy line, case aside) | SPEC.md:27 (candidate 1); v4.md:14 |

## Notes
- Ratings: V1, V2, V3, V4, V6, V7 each VERIFIED, wording equal to SPEC §7 (V1 "In 2024 tests" carries the §7 limit "16 models of 2024": models fixed on the 20 Jan 2024 leaderboard, spracklen-v3.txt:500; 5.2/21.7 at spracklen-abs.txt:35; 36.70-55.70 at wang-vulndeps-abs.txt:33; 281.3 at he-cursor-v3.txt:2395; 30.3/41.6 at :2404, "persists" at :2408; 273 and 22 March 2016 at breadth/npm-kik-leftpad.txt:73-78; eight-line at L2-05.txt:113, E141 non-blank count). No UNVERIFIED or CONTRADICTED figure; V8-V15 absent.
- No SPEC §8 claim in any wording (grepped: Equifax, Chrome, rot/rust/wear, fewer bugs, hobby, n^2, SQLite, GitClear, liability/asset, 750,000, upgrade-at-once: none).
- Axiom limits carried: A1 "a little" + "promptly" (L1-03.txt:16; ruling 2); A2 "Ship the one I change faster. Even LONGER." (L1-06.txt:30, L2-02.txt:36); A3 "most of it" follows ruling 4 (widens Skrenta's "most of the interesting parts", L1-04-full.txt:26, by owner ruling); A4 wording "lines of code written" meets VERIFIED (verify-axioms.md:99).
- Sanctioned, not scored: scene v4.md:16 and prediction v4.md:64 (ruling 16); "You call ALL of yours done" v4.md:38 (ruling 4); enemy line v4.md:14 and v4.md:66 verbatim to SPEC.md:27; attribution v4.md:74 verbatim to SPEC.md:244.
- The body quotes no source text; its only quoted strings are the enemy line and reflex fragments.
