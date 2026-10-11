BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines through `</instruction_matrix>`); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full
INTERPLAY: First Principles and the oath demand the located atom over its name; Strunk demands concrete, positive, unambiguous prose yet grants deviation latitude, which pulls against the rubric's literal-reading mandate; resolved: the precision rubric runs at its literal reading, register and fragments draw no finding here, every fact carries a file:line.
COMMIT: I must tie every finding to a quoted draft line and a source location, and I will leave none bare; I must not rewrite the draft or judge register, and I will give only the smallest compliant form; I must count the ratio by the §13 count under ruling 11, and I will print its numerator and denominator.

# Review — precision — /home/user/LLM_MANIFESTOS/drafts/owned-lines/v2.md

Verdict: FAIL (5)

Rubric: SPEC.md:259. Rulings applied: r1-rulings.md (rulings 10, 11, 13, 14). Every finding is doctrine (the spec or a ruling states the rule).

## Findings

| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| 1 | v2.md:33 | "Name the more MAINTAINABLE one: easier to read and change." | Every demand checkable at one response or one diff. "More MAINTAINABLE" is glossed by two more comparatives; a reviewer has no observable to check on a line of code. Ruling 10 orders the tie test to name its observable. | "Two versions pass the same tests? Ship the more MAINTAINABLE one, even when it runs LONGER, and name the line that makes it easier to change." The observable is a named line. | doctrine: SPEC.md:53, :259; r1-rulings.md:12; L1-06.txt:30 ("you should always favor maintainability") |
| 2 | v2.md:33 | "Least means least a READER must read." against "Ship it, even when it runs LONGER." | Every demand checkable at one response or one diff. Read literally, "least" counts what a reader must read (volume, L1-05.txt:35); the later sentence orders the longer version shipped. The two checks return opposite verdicts on one diff. "Read" carries two senses, volume and effort. | "Least means the fewest lines a READER must read among versions equally easy to change." | doctrine: SPEC.md:53 (A2 writer rule); L1-05.txt:35; L1-06.txt:30 |
| 3 | v2.md:47 | "Charge EVERY line you ship, the day it ships, for understanding, debugging, maintaining, and adapting it." | Every demand checkable at one response or one diff. "Charge" names no output in a response or a diff; compliance has no observable. Ruling 12 fixes only the temporal anchor, not the observable. | "Charge EVERY line you ship, the day it ships: in your summary, name who debugs it and who adapts it to change." | doctrine: SPEC.md:54, :259; r1-rulings.md:12; L1-06.txt:24; L1-05.txt:42 |
| 4 | v2.md:49 | "Read a package's files before you depend on it." | Every demand checkable at one response or one diff. "Depend on it" names no event a reviewer can find; the same draft anchors demand 9 at "Before your manifest changes" (v2.md:51). | "Read a package's files before your manifest changes. NAME them." | doctrine: SPEC.md:71, :259; v2.md:51 |
| 5 | v2.md:49; v2.md:69 | "Untrusted input? State its vulnerability history." / "Package meeting untrusted input. Vulnerability history stated?" | Every demand checkable at one response or one diff. At :49 "its" binds to the nearest noun, "input"; the trigger has no subject. At :69 "meeting" replaces the spec's "touches". Ambiguous pronoun reference is Strunk severity 5. | ":49: "Package touches untrusted input? State that package's vulnerability history." :69: "Package touching untrusted input. Vulnerability history stated?"" | doctrine: SPEC.md:76 (demand 14: "When a package touches untrusted input, state its vulnerability history."); strunk_spr_v3_complete.xml:134, :143 |

## Notes

1. Bindable ratio 26/36 = 0.722 (pass), §13 count under ruling 11. Denominator 36 = every non-blank, non-heading body line, v2.md:14-84, table header :24, delimiter :25 and rule :82 included. Numerator 26 = all but :14, :16, :24, :25, :33, :76, :78, :80, :82, :84.
2. Margin is zero lines. Repairing findings 1-2 restores :33 and gives 27/36 = 0.750. Without :33, dropping any one of :22, :26, :27 gives 25/36 = 0.694; any added non-bindable line costs the same.
3. Clean: all six figures (v2.md:16, :49, :51) match SPEC §7 wording and subject (V1, V2, V3, V4, V6, V7); every "you", "your", "yours" in headings, table and body is the model; zero hedges outside quotes (grep hit only "can", v2.md:22, a boundary modal); "maintaining" is glossed "Adapting to change" (v2.md:47) and "MAINTAINABLE" is glossed (v2.md:33), neither means wear.
4. Ruling 10 items closed: "the minimum" (v2.md:37) and "proof" (v2.md:55) name their observables, "maintaining" is glossed; the tie test stays open (finding 1).
5. Spec-wording gap, not a draft failure: V1 leaves the base of "5.2 percent" unnamed (the study reports percent of generated packages that are hallucinated, spracklen-abs.txt:35); the draft follows SPEC.md:88 verbatim.
