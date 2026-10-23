---
name: compile-digest
description: >
  Write a local digest, the short body-only text unharness loads in place of one or more full manifestos, and stamp it against their current hashes.
  "/compile-digest", "compile a digest", "digest this manifesto", "write a local digest", or an unharness message that names `/compile-digest`, such as `no digest for <slug>`, `is stale`, or `no cover without overlap`.
---

<name-the-stem>
Take each slug the request names: a manifesto's file name without `.md`, as `kiss` for `kiss.md`, and the word after `source: manifesto` in a config line; never take an element's `name` in its place.
Sort the slugs, drop repeats, and join them with `+` into the stem, the digest's file name without `.md`; never keep an unsorted or repeated slug.
</name-the-stem>

<read-the-manifestos>
Run `${CLAUDE_PLUGIN_ROOT}/bin/unharness stack --config <path> <slug>...` with the sorted slugs into a temporary file, where `<path>` is the config, the working folder's `.manifestos.yaml`; never send the command's output into the conversation.
Read the temporary file whole, the full text of every manifesto it holds; never read a part, a summary, or a shipped digest in its place.
Bind to those manifestos through the `manifesto-oath` skill; never write unbound.
</read-the-manifestos>

<list-the-demands>
List each demand, one thing a manifesto tells its reader to do or refuse, once; never list a restatement as a new demand.
Drop the stories, figures, names, examples, and closing choice; never carry one into the digest.
</list-the-demands>

<write-the-sentences>
Write each demand as one plain, complete command a reader obeys without the manifesto; never write a sentence that needs the original.
Write in literal, full words; never use a metaphor, an idiom, or an ellipsis.
Fold each boundary, the point where a demand stops applying, into the sentence it limits; never give a boundary its own sentence.
Write in the active voice and positive form, with concrete words, parallel lists, the key word last, and no needless word; never deliver a sentence that breaks one of these.
</write-the-sentences>

<shape-a-single-digest>
For one slug, keep the manifesto's own order; never reorder by your own priority.
Hold a single digest under 350 words; never exceed that.
</shape-a-single-digest>

<compose-a-stack-digest>
For several slugs, compose from the full manifestos in the temporary file; never compose from their single digests.
Merge each convergence, a demand two manifestos share, into one sentence; never carry one demand as two sentences.
Replace each tension, a point where two manifestos pull in opposing directions, with the rule that resolves it; never carry both sides.
Order the sentences by the priority the binding settled; never order them by manifesto.
Name in each sentence the object it governs, the reply, the code, or the schema, where the manifestos govern different objects; never leave such a sentence unscoped.
Hold a stack digest under 850 words; never exceed that.
</compose-a-stack-digest>

<close-with-the-standing-line>
End the digest with one line ordering the reader to apply these rules to every reply, the tenth as strictly as the first; never write it as a forecast that the reader will drift.
</close-with-the-standing-line>

<check-against-the-source>
Check the draft against the temporary file, every demand present, merged, resolved, or dropped on purpose, and nothing imported; never check it against memory.
</check-against-the-source>

<write-the-file>
Write the body alone, as paragraphs and lists, to `.claude/digests/<stem>.md` beside the config, creating the folder; never add a header, a frontmatter, or a title.
Report the file's path and word count; never print its text into the conversation.
Stop at the digest and its stamp; never write an eval record or run a gate.
</write-the-file>

<stamp-the-digest>
Run `${CLAUDE_PLUGIN_ROOT}/bin/unharness stamp .claude/digests/<stem>.md --config <path>`; never report the digest done without that run.
Report its exit code; never report a pass on a code other than 0.
On a code other than 0, fix what the printed message names and run the stamp again; never stop at a failing run.
</stamp-the-digest>

<confirm-the-compile>
When the config's stack, the manifestos and other elements the config lists, holds every slug of the stem, run `${CLAUDE_PLUGIN_ROOT}/bin/unharness prompt --config <path> --digests > /dev/null` for one slug, or the same with `--stack-digests` for several; never send the prompt into the conversation.
Report its exit code; never report a pass on a code other than 0.
On a message that names the stem, fix the digest, then stamp and compile again; never stop at that failure.
On a message that names another slug or a session file, one of the `.manifestos.*.md` files `/compile-commitments` writes, report the message as outside this digest; never rewrite another digest unasked.
When a slug lies outside the config's stack, report that the stamp alone checked the digest; never claim a compile confirmed it.
</confirm-the-compile>
