Write code so clear that a new developer learns what it does, why it exists, and how it fits the business without reading a comment. A comment that explains what the code does admits that the code failed; rewrite the code instead.

Allow a comment only to state a non-obvious reason, to warn of danger, to mark a task with its ticket, or to satisfy a legal requirement.

Name everything for its intent in the business, never for its implementation: a function says what it does for the domain, a constant teaches the rule it holds. Use no bare number or string in logic; give each a named constant.

Structure code the way an expert in the domain would explain the process, so that a method body reads as the sequence of business steps. Turn a complex condition into a named concept. Make the construction of an object read as its requirements. Name an algorithm by its business purpose.

Split any function whose name needs "and". Replace any Utils or Helpers module with modules named for what they do. Replace a boolean parameter with two named functions.

When code is unclear, prefer in this order: make it clear, restructure it, extract a named method, add a comment stating why. Never leave unclear code with a comment explaining it.

Write for yourself as you were six months ago, before you knew the domain. In review, reject code that needs comments to say what it does, require domain names, and treat unclear code as a bug, not a style issue.

Apply these rules to every reply, the tenth as strictly as the first.
