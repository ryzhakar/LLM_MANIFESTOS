Read /home/user/LLM_MANIFESTOS/research/manifesto-craft/prompts/_binding.md first and obey it.

ROLE: You are adversarially verifying every statement the Tier 2 surveys rated AXIOM, against the primary texts, hunting for the counter-quote that would demote it.

CONTEXT: Five survey reports each rated statements AXIOM, CANDIDATE, or REJECT. AXIOM must mean the eleven texts support stating it as a rule. Your job is to try to break each AXIOM. A statement keeps AXIOM only if no text in the substrate contradicts it and at least two texts, from different authors, state or entail it.

INPUT FILES:
1. Rated-statement sections only of: /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/enemies.md, tensions.md, distinctions-vocabulary.md, demands.md, collection-fit.md (grep for "AXIOM" to locate; do not read the rest of these reports)
2. All eleven primary copies: /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/sources/L1-01.txt … L1-06.txt, L2-01.txt … L2-05.txt, read whole
3. /home/user/LLM_MANIFESTOS/research/manifesto-craft/recon/discovery/evidence/skrenta-wayback.txt (the fuller Skrenta text) if present

TASK:
1. Collect every AXIOM-rated statement across the five reports. Merge statements that say the same thing; keep the wording of each report that rated it, with its ID (report:R-id).
2. For each distinct statement: search all eleven texts (and the Skrenta copy) for (a) every passage that states or entails it, (b) every passage that contradicts, qualifies, or limits it. Quote each at most 25 words with {ID}.txt:line.
3. Rule: VERIFIED when supported by two or more authors and contradicted by none; QUALIFIED when supported but limited by a text (state the limit as the texts state it); CONTRADICTED when a text denies it. Record which lanes the supporting authors come from.
4. For each statement, write the strictest literal reading a maximalist reviewer would hold (one checkable sentence) and whether any of the eleven texts would itself violate that reading.
5. Write the report.

OUTPUT PATH: /home/user/LLM_MANIFESTOS/research/manifesto-craft/discovery/verify-axioms.md

REPORT FORMAT:
(three binding lines)
# Axiom Verification
## Statements — table: # | merged statement | rated AXIOM by (report:R-id list)
## Per statement — supporting quotes; contradicting or limiting quotes; lanes; verdict VERIFIED / QUALIFIED / CONTRADICTED; strictest literal reading; texts that would violate it
## Summary table — # | verdict | supporting authors | limiting text

SCOPE: Verify only. No new candidates, no recommendations, no drafting.

TOOLS: Read; Grep; Write.

End with a 3-sentence summary for a notification: distinct statements, verdict counts, the one contradiction with the most weight.
