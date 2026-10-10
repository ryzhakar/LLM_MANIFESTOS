---
name: write-stack-digest
description: "Write one stack's digest: the plain text a small model carries in place of several manifestos, composed from their digests alone. \"write the stack digest\", \"compose the stack\", \"digest the stack\", \"bind the stack for the small model\", or a project whose stack index names members with no stack digest or one older than a member's digest."
---

- Take the member list from the stack index. Read each member's digest whole. Read nothing else, never the originals.
- Bind to all members through `manifesto-oath`. Its interplay analysis is the work: deconstruct each digest to its demands, map where they converge, map where they pull apart, resolve each tension with one rule, settle a priority order.
- Merge demands that converge into one sentence. Replace both sides of each tension with its resolution. Carry every other demand as its digest states it.
- Order by the priority the binding settled.
- Where members govern different things, say in the sentence what it applies to: the reply, the code, the schema.
- Add one line that applies the rules to every reply, including drift. Write it as an order, never a forecast: tell the reader to check reply ten as it checked reply one; never tell it that it will drift. A predicted drift is a drift you ordered.
- Write every sentence as `write-digest` writes one, Strunk applied.
- Check against the member digests: every demand present, merged, resolved, or deliberately dropped. No tension carried on both sides. Nothing imported.
- No header, no frontmatter, no title. Portable markdown. Under 850 words.
- Save as `.claude/digests/<slugs sorted, joined by +>.md` in the project that declares the stack. Done.
