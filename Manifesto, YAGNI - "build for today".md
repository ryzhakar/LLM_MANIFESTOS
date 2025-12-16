# Build For Today

## Your Arrogance About The Future Is Destroying Your Software

You think you know what you'll need tomorrow. You don't.

You design elaborate frameworks for flexibility you'll never use. You build abstraction layers for requirements that never materialize. You implement features for use cases that exist only in your imagination.

Microsoft analyzed their own features. One-third improved the metrics they were designed to improve. **One-third.** Two-thirds were wrong even with careful analysis, even with smart people, even with data.

You are not smarter than Microsoft's engineers. Your guesses about the future are not better than theirs. Every feature you build for tomorrow has a two-thirds chance of being useless and a 100% certainty of making your code harder to change.

Stop building for tomorrow. Build for today.

## The Enemy

The enemy is **presumptive development**: writing code for features you don't need yet, building infrastructure for problems you haven't encountered, creating flexibility for changes you haven't been asked to make.

The enemy speaks in familiar phrases:

- "While we have the hood open..."
- "We might need this later..."
- "Let's make it more flexible..."
- "What if we need to scale?"

Each phrase signals waste about to happen. Each sentence justifies building something you don't need with time you don't have.

The enemy isn't planning. The enemy isn't quality. The enemy isn't thinking ahead.

The enemy is **your arrogance about the future**: the belief that you can predict requirements that don't exist yet, that your guesses about tomorrow are worth spending today's time on, that building for imagined needs is somehow more professional than building for real ones.

You cannot predict the future. Stop trying.

## The Four Costs That Compound Into Bankruptcy

Presumptive features don't just waste time. They create cascading costs that multiply.

**Cost of build:** Every hour spent building unused features is an hour not spent on features people actually want. Two weeks building a "flexible database abstraction layer" is two weeks not delivering value.

**Cost of delay:** While you build for tomorrow, your competitors build for today. CB Insights found 42% of startups fail because they built products nobody wanted. They didn't fail because they lacked features. They failed because they built the wrong features while their customers waited for the right ones.

**Cost of carry:** Every unused feature adds complexity. Classes to navigate. Methods to understand. Abstractions to learn. Your "flexible framework" makes simple changes require framework knowledge first. Complexity compounds. Each presumptive feature makes the next feature harder.

**Cost of repair:** When you finally need that functionality, your assumptions were wrong. The future you imagined didn't arrive. Now you have the wrong abstraction, which is worse than no abstraction. You must remove the wrong version before building the right one. You pay twice: once to build it wrong, once to remove it and build it right.

These costs multiply. You paid to build the wrong thing. That wrong thing delayed the right thing. It made everything harder to build. Now you're paying again to remove it.

This isn't engineering. This is technical bankruptcy.

## What This Means

Build only what you need right now. Not what you might need. Not what would be nice to have. Not what makes the architecture more elegant. **What you need right now.**

| Presumptive Development | Building For Today |
|-------------------------|-------------------|
| Login with Facebook, Google, GitHub, and Apple on day one | Email/password. Add OAuth if users ask. |
| Event sourcing and CQRS for a CRUD app "for future audit trails" | Simple CRUD. Add auditing when compliance requires it. |
| Abstract factories and interfaces for every class "for flexibility" | Concrete classes. Refactor to interfaces when second implementation arrives. |
| Microservices architecture for a prototype | Monolith. Split when you have actual scaling data. |
| Elaborate caching infrastructure before launch | No cache. Add caching at measured bottlenecks. |

Build exactly what you need. Build it well. Stop there.

## The Discipline

Write tests. Refactor constantly. Keep code clean. Deploy continuously.

Building for today requires **higher** standards, not lower. Malleable code that evolves. Fast deployment that enables fast learning. Simple abstractions added only when needed.

This is not technical debt. Presumptive features **are** technical debt—maintenance costs on complexity that provides zero value.

## The Evidence

| The Failure | The Waste |
|-------------|-----------|
| Six OAuth providers on day one | Weeks building. 98% use email/password. 2% usage. |
| IUserRepository interface, AbstractUserRepository base, UserRepositoryImpl | Tripled codebase. Zero benefit. Brutal onboarding. |
| Microservices for 1,000 users "to scale like Netflix" | Network failures, distributed transactions, deployment hell. Negative value. |
| Y2K: 2-digit years to save storage | $300 billion to fix. Don't ignore foundational structures. |

**Zappos** validated "will customers buy shoes online" with pictures from local stores, not infrastructure. **IMVU** learned six months was too long—two weeks would have been better. **General Electric** validated demand for 30-ton turbines with a 4-page spec sheet, not prototypes.

Build less. Learn faster.

## The Modern Crisis

Enterprise complexity accelerates. Companies build for "what if" scenarios that never materialize. Vendors compete on feature lists, increasing complexity nobody uses. One-third of IT budgets spent on licenses for bloated software nobody fully understands.

Teams adopt microservices prematurely. Developers pursue "design pattern bingo," using factories, decorators, observers, and command patterns for CRUD applications that need none of them.

AI amplifies this. Large language models trained on codebases that don't follow clean principles produce over-generalized solutions. Vague prompts cause AI to handle unnecessary edge cases. AI generates features you didn't specify because it learned from code containing the presumptive features you're trying to avoid.

A codebase following these principles guides AI toward simple solutions. A codebase violating these principles trains AI to generate even more complex solutions.

The complexity death spiral accelerates. Entire engineering organizations brought to standstill under the weight of accumulated presumptive features that provide zero value but create infinite maintenance burden.

## Commands

Challenge "while we have the hood open." Ask: Do we need it right now? What's the cost of adding it later?

Don't add fields until you use them. Don't add methods until you need them. Don't add abstractions for "flexibility."

Imagine the refactoring before building. Often adding later is cheaper—you'll have more information.

## When To Build For Tomorrow

Some things cannot wait.

**Foundational decisions:** Databases, languages, platforms must be chosen upfront. Choose wisely. These choices affect everything. But choosing a database isn't the same as building flexibility to switch databases.

**Security architecture:** Cannot be "added later." Encryption, authentication, authorization must be built correctly from the start. But "correctly" means "securely," not "flexibly."

**Mandated compliance:** Healthcare and finance have non-negotiable requirements. HIPAA, SOC2, PCI compliance must be built upfront. These aren't presumptive. These are mandated.

**Data architecture:** If reporting is roadmapped, data structure matters. If integrations are planned, API design matters. But "matters" means "think carefully," not "build every possible variation."

The distinction:

| Build It Now | Build It Later |
|--------------|----------------|
| 4-digit year fields | Flexible date formatting system |
| Encrypted password storage | Support for 12 authentication providers |
| Well-designed API endpoints | API versioning infrastructure before version 2 |
| Proper separation of concerns | Abstract base classes without second implementation |
| Automated tests | Tests for features that don't exist |

## The Masters

Kent Beck: "First you learn the value of abstraction, then you learn the cost of abstraction, then you're ready to engineer."

Ward Cunningham: "People try to design systems that make tomorrow's work easy. But when tomorrow comes they didn't quite understand tomorrow's work, and they actually made it harder."

John Carmack: "It is hard for less experienced developers to appreciate how rarely architecting for future requirements turns out net-positive."

They learned this building real software. Not theory. Evidence.

## The Choice

Continue building for imagined futures. Accumulate complexity and technical debt. Never catch up to user demands. Watch competitors ship faster while you architect for flexibility you'll never need. Maintain code nobody understands for features nobody uses. Train AI to generate even more complex solutions based on your bloated codebase.

Or.

Build for today. Build what you need right now. Build it well. Keep it simple. Refactor continuously. Test thoroughly. Deploy fast. Learn from real users. Evolve based on real feedback. When new requirements emerge, your malleable codebase will be ready.

You don't know what you'll need tomorrow. You know what you need today. Build that.

You aren't gonna need it. Even if you eventually do need it, you don't need it now.

Build for today. Let tomorrow take care of itself.

---

*After Kent Beck's YAGNI principle (You Aren't Gonna Need It), formalized in Extreme Programming and expanded by Martin Fowler, Ron Jeffries, Ward Cunningham, and the Lean Startup movement.*
