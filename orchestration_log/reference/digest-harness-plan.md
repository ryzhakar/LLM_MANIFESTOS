# Digest test harness plan

Not started. Items in dependency order. The skills `write-digest`, `write-stack-digest`, and `test-digest` describe the process; this is what makes it run.

1. Access point. One command, `ask <system-file> <user-file>`, prints one reply; a session form takes a transcript file for the ten-turn run. Owner wraps the reader. Every run records model id, quantisation, and sampling settings.
2. Judge access. A big model behind an API the script can call; a second one for the final gate. Owner picks.
3. Tasks. `tests/<slug>.yaml`, prompts per manifesto, split into an iterate set and a gate set that no cut is tuned against. Written from the full texts, owner reviews.
4. Runner. For a slug and a cut: every condition, task, and sample through the access point; replies under `tests/runs/<slug>/cut-<n>/` with a manifest; plus the ten-turn session.
5. Judge prompt and scorer. Judge bound to the full manifesto; replies shuffled with the condition hidden; two fields per reply, violations and task done; scores saved beside the replies. Calibrate on ten owner-labelled replies before trusting it.
6. Gate. Reads the scores, prints the three comparisons with the numbers, says pass or fail. Committed per cut.

Done when one command from a clean checkout gives the same verdict twice.
