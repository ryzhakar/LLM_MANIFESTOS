# MANIFESTO: Knowledge Has One Home

## The Enemy is Clear

**Knowledge duplication** is destroying your codebase.

Not code duplication. **Knowledge duplication.**

Every business rule in two places. Every validation in three files. Every transformation scattered across five modules. This is the enemy. This is what kills velocity, breeds bugs, and turns engineering teams into archaeological expeditions hunting for "the other place this needs to change."

Name it clearly: **when the same piece of knowledge exists in multiple locations, your system is lying to itself.**

Someone will update one location and miss the others. Requirements will change and half the copies will stay frozen. Your codebase becomes a minefield where you can't trust anything because truth has no single source.

You are playing Whack-a-Mole. Fix one bug, two more pop up. Push them back, they never disappear. You will never finish.

## The Principle

**Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.**

Not every line of code. **Knowledge.**

Not just in source files. **Within a system**: databases, tests, documentation, build configs, API contracts.

One truth. One location. One update propagates everywhere.

This is DRY. Most of you have misunderstood it since 1999.

## The Distinction That Changes Everything

Two pieces of code can look identical and represent **completely different knowledge.**

Static analysis flags them as duplication. Your linter screams. You rush to extract a shared function.

**You just created a disaster.**

```
// User input validation - business rule
public bool isLongEnough() {
  String words[] = description.split(' ');
  return words.length > 10;
}

// API response check - technical constraint
public bool containsEnoughElements() {
  String elements[] = description.split(' ');
  return elements.length > 10;
}
```

These represent different knowledge. User descriptions might require 20 words tomorrow. API responses might need only 5. **They will diverge.** Merging them couples unrelated concerns.

This is **incidental duplication**—syntax that happens to match but doesn't represent the same knowledge.

| Knowledge Duplication | Incidental Duplication |
|----------------------|------------------------|
| Same business rule in multiple places | Same syntax, different meanings |
| Changes together when requirements shift | Changes independently for different reasons |
| **DRY violation** | **Not a DRY violation** |
| Abstract it | Keep it separate |

Removing incidental duplication creates coupling. Coupling creates fragility. Fragility creates the maintenance nightmare you're trying to avoid.

## The Test

**When some single facet of the code has to change, do you find yourself making that change in multiple places?**

Yes? Knowledge duplication. Fix it.

No? Different knowledge. Leave it alone.

Static analysis cannot tell the difference. Linters cannot tell the difference. **You must think.**

## The Cost of Violation

Eight places. One bug. Eight fixes required.

Eight opportunities to miss one. Eight testing cycles. Eight times the development effort.

You ship the fix. Users report the bug still happens. You hunt through the codebase finding the copies you missed. **You are the Whack-a-Mole player.**

Knowledge duplication compounds:

- Development effort **multiplies**
- Test effort **multiplies**
- Quality risk **escalates**
- Codebase **bloats**

One developer inherited code where fixing a single bug required changes in eight different places. Another described "elegant code" rotting into "a difficult, hackish, buggy, high maintenance mess" as duplicates diverged into unmaintainable variants.

This is entropy. Copies drift. No one knows which version is correct. Your system has multiple truths. **Truth cannot be multiple.**

## The Opposite Disaster

The wrong abstraction is worse than duplication.

You see duplication. You extract it. You name it. You feel clever.

Time passes.

New requirement arrives. Almost fits the abstraction. You add a parameter. Add a conditional.

Another requirement. Another parameter. Another conditional.

Loop until the abstraction becomes incomprehensible.

Programmer A sees duplication, creates abstraction, feels satisfied. Time passes. Programmer B adds parameter. Programmer C adds another. Programmer D adds conditional logic. **The abstraction is now more complex than duplication would have been.**

"We had 'Base'→'BaseThing'→'BaseAPIThing'→'HABaseThing'→'The Actual Thing.' We could not make updates without potentially breaking 60-70 other libraries."

Sunk cost fallacy makes it worse. You keep adding conditionals to broken abstractions rather than admitting the abstraction was wrong.

If you find yourself passing parameters and adding conditional paths through shared code, **the abstraction is incorrect.**

Delete it. Start over.

## The Rule of Three

First time: just write it.

Second time: wince at duplication. Duplicate anyway.

Third time: **now** refactor.

Why wait? Two instances don't give you enough information. You'll build the wrong abstraction. Three instances reveal the pattern.

**Premature abstraction** is the enemy of good design.

## The Modern Threats

### Enterprise Wrong Abstractions

Enterprise architects see duplication as failure. They rush to abstract before understanding whether similarity is knowledge or incidence.

Result: parameter-laden, conditional-riddled shared code that couples unrelated concerns. "Shared libraries" become bottlenecks where no team can change anything without coordinating with everyone.

Changes to one feature require considering impacts on dozens of others through forced coupling.

### AI Code Cloning

AI tools generate code at speed without considering maintainability. Research shows AI creates **massive code cloning**—duplicating knowledge across repositories with no thought for consolidation.

When bugs appear, engineers track down and patch "the same issue across multiple locations." Studies confirm: code duplication leads to higher defect rates.

AI doesn't factor in long-term costs. It just keeps generating. **AI-generated code violates DRY-ness across every repository it touches.**

Both forces—enterprise wrong abstractions and AI code cloning—violate DRY from opposite directions. One abstracts too early. The other duplicates too freely.

**Both create unmaintainable codebases.**

## Success

| System | Before | After |
|--------|--------|-------|
| Web app formatting | Numbers formatted in dozens of places | One change. All numbers updated. |
| E-commerce filtering | Product filters scattered across search, recommendations, related products | Single function. One update propagates everywhere. |
| Analytics MRR | Multiple MRR calculations, constant "which is correct?" debates | One authoritative definition. One source of truth. |

Abstract actual knowledge duplication, not incidental similarities. Wait until duplication is painful. Create stable abstractions that don't require constant modification.

## Commands

Before abstracting, ask: "When this knowledge changes, must I update multiple places?" If yes, knowledge duplication—abstract it. If no, incidental duplication—keep it separate.

Syntax duplication representing different business concepts? Don't abstract.

Code changing independently for different reasons? Don't abstract.

**When you find wrong abstractions:** The fastest way forward is back. Inline the code. Delete unused bits. Start fresh. Keeping broken abstractions wastes far more than deleting them.

## When Duplication is Acceptable

Context-specific logic serving different business domains? **Duplicate it.**

Code crossing microservice boundaries? **Duplicate it.** Sharing creates coupling that defeats service boundaries.

Research or experimental code with limited lifespan? **Duplicate it.**

One-time migration scripts? **Duplicate it.** You'll never maintain them.

Write Everything Twice (WET): you can duplicate twice, but never three times. This aligns with Rule of Three.

**Avoid Hasty Abstractions (AHA):** optimize for change first. You don't know the future. Don't be dogmatic about abstractions. Write them when they feel right. Don't fear duplication until then.

## The Stakes

**Programming is fundamentally about managing knowledge**, not writing code.

Software systems crystallize business logic and domain understanding. When that knowledge scatters across multiple locations, it becomes fragile, inconsistent, unmaintainable.

As AI generates code without considering maintainability, DRY principles become **critical** to combat technical debt explosion.

## The Choice

| The Path of Knowledge Duplication | The Path of Single Truth |
|-----------------------------------|--------------------------|
| Fix bugs in eight places | Fix bugs once |
| Hunt for "the other location" | Know where everything lives |
| Inconsistent behavior across system | Consistent behavior everywhere |
| "Which version is correct?" | One authoritative source |
| Maintenance nightmare | Maintainable evolution |
| Whack-a-Mole forever | Progress that sticks |

**You cannot have both.**

Apply DRY to knowledge duplication. Tolerate incidental duplication. Delete wrong abstractions. Build software that evolves.

## The Declaration

**Apply DRY to knowledge duplication.**

**Tolerate incidental duplication.**

**Delete wrong abstractions.**

**Build software that can actually evolve.**

When the abstraction is wrong, the fastest way forward is back. This is not retreat. This is advance in a better direction.

Knowledge has one home. Find it. Protect it. Everything else is negotiable.

---

*After Dave Thomas, Andy Hunt, Sandi Metz, Kent C. Dodds, Martin Fowler*
