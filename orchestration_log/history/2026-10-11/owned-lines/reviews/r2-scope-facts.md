BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines through `</instruction_matrix>`); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full
INTERPLAY: All four demand the located source over the name and the checkable line over the judgment call; Strunk's judgment latitude and the skill's absolutes pull against First Principles' refusal to inherit; resolved: SPEC §4-§10, the primary texts, and the r1 rulings are the only authority, every finding quotes the draft line and a source line, no allowance for convention.
COMMIT: I must trace every draft claim to a located SPEC, ruling, or primary line, and I will report no finding without a quote and a source; I must not rewrite the draft or judge outside the scope-facts rubric, and I will give only the smallest compliant fix; I must report facts, not conclusions, and I will label each source doctrine, learned, or practiced.

# Review — scope-facts — v2.md

Verdict: FAIL (2)

## Findings

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| 1 | 33 | `Code that gets better over time is the frontier; counting output never gets you there.` | SPEC §15 scope-facts: "Every claim traces to §4–§10." The clause after the semicolon is a universal claim (counting output never reaches code that gets better over time). B1 carries only "Code that gets better over time." and "This is the frontier."; no §4-§10 line, no §7 figure, and no primary line says counting output cannot reach it. The nearest figure, V4, states what happened in repositories that took on an AI coding agent. | Cut the clause: `Code that gets better over time is the frontier.` | SPEC.md:134 (doctrine); L1-04-full.txt:34, :36 (doctrine); SPEC.md:91 (doctrine) |
| 2 | 72 | `Rewrite your WHOLE response, never the line, no patch notes.` | SPEC §6 closes the demand set at sixteen; §11 row 6 prescribes "rewrite the whole response, not the line." "No patch notes" is a seventeenth command matching no demand and no §4-§10 line; ruling 12 fixes the rule as "a failed check means the whole response is rewritten" with no patch-notes clause. The word "patch" comes from stop-yapping.md:107 ("You don't get to patch noise"), a file outside the four kiss rows. | `Rewrite your WHOLE response, never the line.` | SPEC.md:57, :164 (doctrine); r1-rulings.md ruling 12, line 14 (learned); stop-yapping.md:107 (practiced) |

## Notes

- Passed by script (`python3 -I`, generate.py rules): key order matches §14, tagline 6 words, tagline and title unique among the 12 manifestos after normalize_tagline, theme in themes.yaml and carried by 7 others, semver, kind/register/reader values, description one line; the only body `---` is L82. Candidate 1 (L14, L76) and the attribution (L84) match §3 and §14 byte for byte.
- Passed: V1, V2 (first sentence), V3, V4, V6, V7 are substrings of the §7 wording and match; no V8-V15 figure, no §8 claim, no HUMAN-only demand, no escape clause. 2-gram and 3-gram scans against the 12 other manifestos found no restated enemy (kiss's enemy, yagni "presumptive", postgres "what ships in the box" / "permanent line item", dry duplication all absent). The v1 findings (L40 token lift, "Prove it works") are gone.
- Spec tension, not counted: L47 `You debug THAT.` follows the SPEC.md:40 D2 hinge (L2-05.txt:61 "you'll be the one debugging it"), while L76 leaves the bill "for whoever gets paged" per SPEC.md:203; L53's head is a metrics-policy sentence that SPEC.md:55 (A4) mandates and SPEC.md:207 lists as a HUMAN-only category.
- Not counted: L37 `DELETE it.` carries kiss.md:159 row 1 content (speculative code) under demand 3 though SPEC.md:147 maps the row to demands 4, 5; L39 `DEAD` and L41 carry the same row; L29 `First-time code is DEBT` is flat where L1-03.txt:16 says "is like going into debt" (quote fidelity belongs to the accuracy rubric).
- Not counted: L16 `you read it out like your PAYCHECK` and L47 `You call ALL yours done` follow SPEC.md:12 (enemy in the reader's own mouth) and ruling 4; L72 `Fail ONE? ... Rewrite your WHOLE response` follows SPEC.md:164.
