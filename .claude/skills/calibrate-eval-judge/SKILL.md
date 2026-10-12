---
name: calibrate-eval-judge
description: "Measure a judge configuration, an agent model with a brief, against reference raters on a blind sample, record the agreement, and fix the configuration for an eval series. \"calibrate the judge\", \"does sonnet agree\", \"check the judge\", \"fix the judge for the series\", or a spec about to name a judge no calibration record covers."
---

<set-the-acceptance>
Write the acceptance level, the least agreement per demand and for done that admits a judge, the model that counts breaches of the manifesto in a reply, before any rating; never set it after seeing the numbers.
Write the sample size; never rate a sample smaller than it.
</set-the-acceptance>

<build-the-sample>
Take replies from a pilot run or a `dev` run across every condition, a text loaded beside the reader's prompt, blinded through the `judge-by-agents` skill into one packet, a file of replies under random ids with no condition named; never calibrate on `test` replies.
Keep the key, the map from reply id to origin, outside every rater's reach; never show a rater the condition.
</build-the-sample>

<rate-by-reference>
Let the reference raters, the owner, or two agents of a stronger model bound to the manifesto through the `manifesto-oath` skill, each rate the sample alone in the verdict shape the `write-eval-record` skill fixes; never let one rater see another's verdicts.
Take the median of the reference counts per reply and demand as the reference; never take one rater's count.
</rate-by-reference>

<run-the-candidate>
Have the candidate judge rate the same packet twice through the `judge-by-agents` skill, each run alone; never run it once.
</run-the-candidate>

<measure-the-agreement>
Compute per demand the mean absolute difference between the candidate's count and the reference, the candidate's self-difference between its two runs, and the share of replies where candidate and reference agree on done; never report one number for every demand.
Report the candidate's scale against the reference, its mean count divided by the reference's; never compare a cut's numbers with a pilot's under another judge.
</measure-the-agreement>

<fix-the-configuration>
Accept the candidate when every demand and done reach the acceptance level; never accept one that misses a demand.
Rewrite the brief for a missed demand; never patch the brief inside a series, the cuts run under one spec.
Calibrate a rewritten brief again from a fresh sample; never reuse the sample it missed on.
Save the calibration record through the `write-eval-record` skill; never run a series on a judge the ledger cannot name.
Name the accepted judge and the brief's hash in the spec; never name one the calibration record does not cover.
</fix-the-configuration>
