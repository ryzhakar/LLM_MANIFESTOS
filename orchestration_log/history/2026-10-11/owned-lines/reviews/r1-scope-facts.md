BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines through `</instruction_matrix>`); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full
INTERPLAY: All four demand the located source over the name and the checkable line over the judgment call; Strunk's judgment latitude and the skill's absolutes pull against First Principles' refusal to inherit; resolved: SPEC §4-§10 and the primary texts are the only authority, every finding quotes the draft line and a source line, no allowance for convention.
COMMIT: I must trace every draft claim to a located SPEC or primary line, and I will report no finding without a quote and a source; I must not rewrite the draft or judge outside the scope-facts rubric, and I will give only the smallest compliant fix; I must report facts, not conclusions, and I will label each source doctrine, learned, or practiced.

# Review — scope-facts — v1.md

Verdict: FAIL (2)

## Findings

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| 1 | 40 | `No "future" code. No "just in case" functions.` | SPEC §10: "Carry content, not wording." The two fragments lift the tokens `"future"` and `"just in case"` from the kiss row `Delete speculative "future" code. Delete "just in case" functions.` Content already stands in L40's first sentence (demand 4) and L42 (demand 5); §10 maps the row to demands 4, 5 only. | Delete both fragments. | SPEC.md:143, :147 (doctrine); kiss.md:159 (practiced) |
| 2 | 69 | `Prove it works or claim NOTHING.` | Every claim traces to §4-§10; §6 closes the demand set at sixteen. "Prove it works" matches no demand: demand 7 asks for proof "that behaviour survived", demand 6 for tests protecting a deletion. The phrase also stands in kiss.md:113 (`Prove it works.`), outside the four kiss rows. | `Prove behaviour survived or claim NOTHING.` | SPEC.md:59, :69, :257 (doctrine); L1-06.txt:28 "while preserving all existing functionality"; kiss.md:113 (practiced) |

## Notes

- Passed: frontmatter by script (`python3 -I`): key order matches §14, tagline 6 words, normalized tagline and title unique across the 12 manifestos, theme in themes.yaml, semver, kind/register/reader values.
- Passed: V1, V2, V3, V4, V6, V7 match §7 wording character for character; no V8-V15 figure, no §8 claim, no HUMAN-only demand, no escape clause; attribution matches §14 exactly; a 3-gram scan against the 12 other manifestos found no other restated ground (yagni "presumptive", postgres "permanent line item" and "what ships in the box", dry duplication, kiss enemy: absent).
- Spec tension, not counted: §4 D2 hinge says installing never outsources "the outage" (L2-05.txt:61); §10 row says "never the debugging"; L2-05.txt:39 lists debugging among outsourced work; draft L61 `NEVER the debugging` follows §10.
- Not counted: axiom heads differ from §5 wording by one word each (L24 "a line" to "every line"; L65 "Do not" to "Never"); same scope.
- Not counted: L84 `Fail ONE? Rewrite the WHOLE response. Not the line.` echoes stop-yapping.md:107; §11 row 6 and §1 prescribe it.
