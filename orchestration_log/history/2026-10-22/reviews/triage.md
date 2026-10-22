# Triage: Raise the Bar, two reviews into one list

Sources: `reviews/fidelity.md` (15 findings, F1–F15) and `reviews/self.md` (91 violations, S1–S91), both read in full against `plugin/manifestos/raise-the-bar.md` at 4edb556. Line numbers below refer to that commit.

## Apply, in this order

Apply every item exactly as written; each gives the line and the replacement.

1. **Line 36, the merged non-negotiable rule** (F1, F2, F4). Replace the whole bullet with `- State each non-negotiable plainly, with its reason.` Then move the positive-target rule back to "Readers who are models", as item 9 below does.
2. **Line 6, the description** (F3). Replace the value with `"This manifesto tells a writer how to state a demand, a belief, and the stakes, with pressure from stakes and resources rather than from contempt or threat."`
3. **Line 19, "The standard"** (F3, F12, S6, S7). Replace the paragraph with: `This manifesto is for you, the writer of any text that asks a reader to meet a standard, whether a person or a model writes the text or reads it. It sets the stance your text takes toward that reader: how the text states the demand, the stakes, and belief in the reader; how it treats failure, praise, and blame; and how it sets force and register and frames the enemy. You can set that stance from this page alone: the four principles give the reasons, the worked example shows one group of rules per line, and the checks test a draft for the five faults.`
4. **Line 13, the enemy contrast** (S5). Replace the last two sentences with: `The text that uses it raises its voice, aims at the person, presses through consequences, and leaves the grounds, the belief, and the means unstated. The text that raises the bar holds a high standard, states belief in the reader, stays precise about the work, and puts all three on the page.`
5. **Line 24, principle 2** (F15). Replace `Feedback weakens as it draws attention from the work onto the person.` with `One large meta-analysis finds that feedback weakens as it draws attention from the work onto the person.`
6. **Line 25, principle 3** (F6). Replace `Expectations held in the writer's head change little, and expectations stated to the reader raise performance.` with `Workshops that train managers to hold high expectations change little, and expectations stated to the reader raise performance.`
7. **Line 26, principle 4** (F14, S25). Replace the first sentence with `Contrary experience easily undoes a belief that words built, and an undone belief lowers the reader's trust in the next text.`
8. **Lines 48 and 84, the tested wording** (S1, S75). The quoted note states belief with no ground, so it models the intent rule, not the belief rule. Line 48 becomes `- State belief outright, beside the standard and its grounds, as the worked example's belief line does.` Line 84 becomes `- State the intent as the reason for the feedback, the high standard and the belief that the reader can meet it, as in the tested line "I'm giving you these comments because I have very high expectations and I know that you can reach them," and never as an effort to persuade.`
9. **Line 96 and the model rules** (S4, S22, S77, F5, F1). Replace lines 96 to 100 with:
   ```
   No rule here is tested on models in its stated form; the four rules below rest on vendor guidance and on single studies. Apply the other rules to model-read text for one voice across texts, not for a tested gain.

   - Give a model the target, the success criteria, and the reason behind each instruction.
   - Prefer a positive target. Where a prohibition is the clearest form of a constraint, state it plainly, once, with its reason; in tests on models, naming a forbidden word cut its use and left only a small trace of its meaning.
   - Reserve emphasis for rules that never bend, keep it calm, and write judgment calls as decision rules; in one study, emphasis raised compliance with the line it marked, and a vendor warns that aggressive wording can make its models overtrigger.
   - When people and models read one text, let this section's rules govern the action steps and the rest of the page govern the framing around those steps.
   ```
10. **Line 50** (S32). Delete `- Write only belief that is true.`; principle 4 and the first closing check carry it. Report it as a merge.
11. **Line 56** (F13). Replace `criticism motivates more when it tells the reader how to improve` with `criticism raises intrinsic motivation more when it tells the reader how to improve`.
12. **Line 60** (F9). Replace `naming the thing to avoid draws errors toward it` with `in penalty kicks, naming the thing to avoid drew errors toward it, even when the instruction said to pass it`.
13. **Line 65** (F8). Replace `a general offer changes nothing` with `in one study, a general offer of support changed nothing`.
14. **Line 66, the threats reason** (F7, F10). Replace the second sentence with `In a person, controlling language raises anger and resistance. In a model, threats, rudeness, and flattery give no reliable gain and cost accuracy on small models, and flattery raises compliance with objectionable requests.`
15. **Line 70** (S24). Replace `needless complexity lowers the reader's estimate of the writer's intelligence` with `needless complexity costs the text its credibility with the reader`.
16. **Line 86** (S76). Replace `reflection of the group's sentiment` with `echoes of what the group feels`.
17. **Line 90** (F11). Replace `the early wins, not the wording, set the ceiling` with `the early wins, not the words, set the ceiling`.
18. **Line 113, the worked example's failure line** (S9). Replace `The outage traced to one untested path.` with `Each outage traced to one untested path.`

After the edits, run `just readme`, confirm that each rule of the rulebook still appears once, and commit as `fix(manifestos): raise the bar, review triage applied`.

## Rejected, with the reason

- **S3, S13, the tagline and the last line:** the owner chose "raise the bar, not the voice"; it is the manifesto's one aphorism and sets old behavior against new, as the enemy rule allows.
- **S8:** item 1 drops "once" from the non-negotiable rule, so the force line may restate the demand.
- **S2, S10–S12, S14–S21, S23, S26–S31, S33, S34:** they apply the content rules to the manifesto as if it were a single instruction. The five checks and the two closing checks are the manifesto's self-test, and the extra lines would load the writer with what the writer does not need.
- **S35–S47:** the manifesto's own rule permits a plain prohibition where it is the clearest form; these rules define the stance by contrast, and their contrasts are content, not action steps of a target text.
- **S48–S74:** the four principles give the reasons; a purpose clause on every rule would restate them in 27 places.
- **S78–S91:** bold labels and the italic attribution mark structure, not emphasis.
- **Fidelity, "reasons dropped whole" and "outside the manifesto":** the brief allows those drops, and the two d = .19 figures belong to two outcomes the source reports separately.
