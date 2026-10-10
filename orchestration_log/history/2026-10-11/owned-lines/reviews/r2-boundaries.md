BOUND: First Principles — /home/user/LLM_MANIFESTOS/manifestos/first-principles.md — full; Strunk SPR v3 — /home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml — full (2,923 lines); manifesto-oath — /home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md — full; manifesto-writing — /home/user/claude-skills/manifesto/skills/manifesto-writing/SKILL.md — full; inputs read whole: SPEC.md, v2.md, reviews/r1-rulings.md, discovery/verify-axioms.md, primary L1-03, L1-04-full, L1-05, L1-06, L2-05 (cited lines), L2-02:36
INTERPLAY: All four demand the located quote over the paraphrase and the command over the hedge; First Principles' refusal to inherit pulls against Strunk's judgment latitude and the r1 rulings; resolved: every verdict rests on a v2.md line and a source line, a draft line that follows a ruling is no finding, and no rewriting appears here.
COMMIT: I must test every B-clause against "what the enemy is not" and every sentence against "when the reader may stop", and I will quote the line for each verdict; I must not rewrite the draft or judge outside the boundaries rubric, and I will not report an opinion as a finding.

# Review — boundaries — v2.md
Verdict: PASS

## Findings
| # | draft line | quoted text | rule failed | fix or correct fact | source |
|---|---|---|---|---|---|
| — | — | none | — | — | — |

Clause check (practiced; evidence for the pass, not findings):

| clause | draft line | quoted text | what the enemy is not | source |
|---|---|---|---|---|
| B1 | v2.md:33 | "Code that gets better over time is the frontier; counting output never gets you there." | code that gets better over time | L1-04-full.txt:34, :36 |
| B2 | v2.md:29 | "First-time code is DEBT. A little buys speed if you consolidate it promptly; unpaid, it's interest your "Done" books as income." | debt taken and repaid; carries "a little" and "promptly" (ruling 2); two sentences; no heading | L1-03.txt:16 |
| B3 | v2.md:47 | "Done code is not the enemy; upkeep falls on most, not all. You call ALL yours done." | code that is done; names the reader's error (ruling 4); the only "not the enemy" in the file (ruling 6) | L2-05.txt:91; L1-04-full.txt:26 |
| B4 | v2.md:33 | "Name the more MAINTAINABLE one: easier to read and change. Ship it, even when it runs LONGER." | more lines that read easier; A2 carries maintainability | L1-06.txt:30 |
| B5 | v2.md:51 | "Vetted reuse is engineering; unvetted, you're a stranger's COURIER." | vetted reuse | L2-05.txt:177, :195 |
| B6 | v2.md:55 | "You want a score? Lines REMOVED, behaviour intact. Report lines you removed as progress only beside the passing run of the tests that cover them." | lines removed, behaviour intact, reported as progress | L1-06.txt:28 |

## Notes
- Escape scan: no hit in the body for hobby, deadline, prototype, small, quick, throwaway, user, request, unless, except; the conditionals present are spec gates, none names a circumstance of the reader: v2.md:29 "if you consolidate it promptly" (ruling 2), :49 "Untrusted input? State its vulnerability history." (demand 14), :57 "None? Say so." (demand 6).
- A3 carries "most, not all" at v2.md:47; A2 carries maintainability at v2.md:33.
- Not counted, outside the boundaries rubric: v2.md:47 head "Charge EVERY line you ship, the day it ships, for understanding, debugging, maintaining, and adapting it." and its limit "upkeep falls on most, not all." stand side by side; "Maintaining? Adapting to change." glosses the head; the source example of done code is "may never need to be modified again" (L2-05.txt:91). The maximalist and precision lenses own it.
- Not counted: "done" has no definition inside v2.md:47; ruling 4 fixes the clause's content and v2 follows it.
