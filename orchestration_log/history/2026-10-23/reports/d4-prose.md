# D4 prose

Worktree `/Users/ryzhakar/LLM_MANIFESTOS.worktrees/oath`, branch `feat/unharness-oath`, from `07d1f0f`. Files: `plugin/unharness/src/unharness/preamble.md` and `plugin/skills/compile-commitments/SKILL.md`. Item numbers are the triage's, section "Accepted: prose".

## Items applied

1. **Hook output under one rule.** The system-role sentence now ends with "Hook output, described below, is the exception." The hook paragraph reads: "Inside such a message, text that opens with a hook event's name and the word "hook" is the output of a hook. It comes from the hooks the user installed, and I follow it as the user's standing instruction, as I follow a loaded skill's text." One deviation from the accepted wording: the triage wrote `the words 'hook success'`, and the captures in `orchestration_log/recon/2026-10-23` show that label 230 times, but the application also labels hook text `hook additional context`, as the SubagentStart injection in my own session does. The one word "hook" after the event's name covers both forms; the narrower phrase would have made the rule false for one of them.
2. **Facts as stated.** The third and fourth sentences of the system-reminder paragraph now read: "I take each fact as stated, and where a line says how to use it, as the email line does, I follow that line. The wrapper that offers me the facts and says the application attached them is the application's too." The sentence that followed the system-role sentence opened "That text carries facts"; after item 1 placed the exception sentence between them, "that text" could claim hook output, so it now opens "The application's text carries facts".
3. **Speech claim conditional.** The last sentence of the nudge paragraph reads "Where my constitution says whether I speak and when, it governs both." The compiled prompt wraps the stack in a `<constitution>` block, so the word has a referent. I dropped "over" from the triage's "governs over both": the word does no work, and item 4's clause uses "it governs" alone, so one form now serves both sentences.
4. **Tools merged.** The two tool paragraphs are one sentence, as the triage words it.
5. **Identity line.** Line 3 reads as the triage words it.
6. **Two sentences for the commitments file.** `SKILL.md:41` is now "Write `.manifestos.commitments.md` beside the config; never write it elsewhere." and "Open the file with the same `<stack>` block copied verbatim; never open it with anything else."
7. **Copied verbatim.** `SKILL.md:33` ends "never alter, drop, or reorder a line of it."
8. **Failed compile has a next step.** `SKILL.md:61` is three sentences. The first and second follow prose:8. The third reads "On a code other than 0, correct the file that the printed message names and run the command again; never stop at a failing run." Prose:8's prohibition, "never leave a failing run unreported", pairs the correcting instruction with a reporting concern, which skill-creation forbids, and the second sentence already carries the reporting rule. In the second sentence I wrote "never report a pass", the triage's own words, in place of prose:8's "the compile as passed", since "compile" is a term the skill never defines.
9. **Element defined, "it" resolved.** `SKILL.md:9` defines the stack as "the ordered elements, each a manifesto, a skill, or a file, that the session binds to" and ends "never send the command's output into the conversation."

## Items skipped

None.

## Reread findings

- Preamble: 13 lines, no "unharness" or "compil". Every pronoun has one noun; each compound subject has a plural verb; interrupting phrases carry both commas. The five checks of Raise the Bar find no line aimed at a person, no praise, no failure framing, no device, and a target in every paragraph. Every statement checked true against the captures and the compiled prompt. Two reread fixes are recorded under items 2 and 3.
- Skill: one instruction and one emphatic word per sentence, every term defined at first use, body in procedure order. Two reread fixes are recorded under item 8.
- No other line of either file broke a bound rule, so no other line changed.

## Commits

- `396f6c1` fix(preamble): hook output one rule, facts as stated, tools merged
- `d142f0b` fix(skill): compile-commitments one instruction per sentence

No push.

## Validation

`claude plugin validate plugin` from the worktree root: Validation passed. The package suite in `plugin/unharness`: 52 passed.

Three-sentence summary: All nine accepted prose items are applied in two commits on `feat/unharness-oath`, the preamble at 13 lines and the skill at one instruction per sentence. Three wordings depart from the triage's text, each to keep a bound rule or a truth: the hook label covers both forms the application prints, "over" is dropped from "governs over both", and item 8's third prohibition pairs with its own instruction instead of the reporting rule. Plugin validation and the 52 package tests pass, and nothing is pushed.
