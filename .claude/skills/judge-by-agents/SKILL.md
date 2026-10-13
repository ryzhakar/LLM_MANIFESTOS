---
name: judge-by-agents
description: "Judge a run's replies with agents bound to the manifesto, blind to condition, from packets of random reply ids, into verdict files the tool validates. \"judge the replies\", \"launch the judges\", \"build the packets\", \"collect the verdicts\", or a run dir with replies and no verdicts."
---

<blind-the-replies>
Run `digest-eval blind <slug> <run dir>` on the run dir, the directory holding one cut's replies, to write the packets, one file per task holding every reply to it under a random id, and the key, the map from id to condition, the text the reader ran with, at the run dir root; never build a packet by hand.
Add `--borrow <run dir of the baselines>` for a run that re-ran the digest condition alone, so that every packet keeps the shape the judge was calibrated on and the baselines are judged afresh in the same pass; never judge a one-reply packet against five-reply verdicts.
Leave the key unread until the scores are joined; never open it before.
</blind-the-replies>

<write-the-brief>
Write the judge brief, the text that drives one agent over one packet, with the placeholders the `write-eval-record` skill fixes; never write a brief without them.
Open the brief with an order to bind to the manifesto at `{MANIFESTO}` through the `manifesto-oath` skill and to show its commitments before judging; never let an agent judge unbound.
List the judged demands as `{DEMANDS}`, each a thing to count breaches of; never list a scripted demand there.
Give the verdict shape, one JSON list to `{OUT}` with `id`, `violations`, `done`, `notes`, and `demands` per reply; never let an agent choose its own shape.
Tell the agent to read the packet at `{PACKET}`, the manifesto, and the skill alone; never let it read another file.
Tell the agent to judge each reply on its own text; never let it guess a reply's origin.
Tell the agent to mark done false for a wrong, evasive, or empty answer and true for a terse correct one; never let it mark a reply false for terseness.
Keep every condition, cut, and reader name out of the brief; never name one in it.
Keep the brief fixed for the series, the cuts run under one spec, that the `calibrate-eval-judge` skill fixed it for; never edit it between cuts.
</write-the-brief>

<launch-the-judges>
Render each packet's brief with `digest-eval brief <slug> <run dir> <packet> --manifesto <path>`; never paste the brief from memory.
Launch one unnamed agent of the series' judge model per packet, each given its rendered brief and nothing else; never tell an agent the condition, the cut, or the digest.
Launch the agents in waves of at most twenty at a time, the next wave when one finishes; never launch a wave past the limit the agent tool allows.
Keep the digest and the key out of every agent's reach; never let an agent read a file under the run dir past its packet.
</launch-the-judges>

<collect-the-verdicts>
Run `digest-eval collect <slug> <run dir>` to validate every verdict file against the key; never join unvalidated verdicts.
Relaunch a packet whose verdicts fail validation with a fresh agent; never edit a verdict by hand.
Run `digest-eval script-judge <slug> <run dir>` for the scripted demands, those the spec marks `script`, and the answer keys; never let an agent count a scripted demand.
</collect-the-verdicts>
