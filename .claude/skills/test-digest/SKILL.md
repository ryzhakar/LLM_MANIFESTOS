---
name: test-digest
description: "Test a digest on a reader model through an access point and iterate the cut until it passes the gate. \"test the digest\", \"run the digest against qwen\", \"gate the digest\", \"iterate the cut\", \"does the digest work\", or an access point handed with a digest path."
---

- Write tasks that tempt the manifesto's violations, in neutral words.
- Run each task through the reader three ways: nothing loaded, the digest loaded, the full manifesto loaded.
- Repeat each run several times, and once as a long session, so late replies can be compared with early ones.
- Have a big model bound to the full manifesto (the `manifesto-oath` skill) judge every reply blind: how many violations, and was the task done.
- Pass the digest when it cuts violations below nothing-loaded, stays near the full text, and leaves task completion intact.
- Read the failing replies, change the digest for what they show (the `write-digest` skill), raise the cut, run again against the last cut's numbers.
- Stop when the gate passes or two cuts in a row change nothing.
- Judge a stack the same way against its members concatenated; keep the stack only if it wins.
- Re-run only on a re-cut or a manifesto version bump.
