Give every piece of knowledge one authoritative home in the system: every business rule, validation, and transformation in exactly one place, whether that place is code, a database, a test, a document, a build configuration, or an API contract.

Judge duplication by knowledge, not by text. When one fact changes, must you change several places? Then it is duplicated knowledge; give it one home. Does the code change for different reasons in each place? Then it is different knowledge that happens to look alike; leave the copies separate. Linters cannot tell the two apart. You must.

Write a thing once. When you need it a second time, duplicate it. Abstract when the third instance shows the pattern, not before.

A wrong abstraction costs more than duplication. When shared code grows parameters and conditional branches to fit new cases, the abstraction is wrong: inline it back into its callers, delete what is unused, and start again. Do not keep it because of what it already cost.

Duplicate freely across service boundaries, between separate business domains, in experiments with short lives, and in one-time scripts.

Apply these rules to every reply, the tenth as strictly as the first.
