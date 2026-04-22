---
title: "Decomplect"
tagline: "decomplect"
version: "1.0.0"
theme: "software-engineering"
description: "Complexity from braiding is killing software. Simple means untangled. Keep things separate."
---

# DECOMPLECT
## A Manifesto Against Braided Code

*After Rich Hickey, Kelly Johnson, and the engineers who understood that simple beats clever*

---

## Name Your Enemy

**Complexity is killing your software.**

Not the complexity inherent in hard problems. The complexity you add. The braiding. The interleaving. The tangled mess where changing one thing breaks three others.

Enterprise bloat with 11-layer architectures for operations that should take minutes. AI slop that clones code without comprehension. Frameworks with 68 interfaces for 26,759 lines. Systems so Byzantine that nobody understands them anymore.

This is not sophistication. This is failure disguised as engineering.

The enemy has two faces:
- **Over-engineering:** Smart developers being too clever, building for futures that never arrive
- **AI sloppiness:** Generated code without comprehension, additions without understanding

Both braid things that should stay separate. Both create systems where nobody knows what's happening.

---

## Simple vs Complected

**Simple** comes from Latin *sim-plex*: one fold, one twist.

Simple means not intertwined. Not braided together. Components that are separate. Responsibilities that are distinct. This is **objective**. Either things are coupled or they aren't.

**Complected** means braided, interleaved, entwined.

When you mix data access with business logic. When you couple UI to database. When you braid 47 configuration options into one framework. When you create dependencies that spread like vines through your codebase.

This is also objective. The braiding is real. The coupling exists.

**Easy** is different.

Easy means familiar. Near at hand. Relative to your current skills. A framework with 47 options becomes "easy" once you've memorized them. But it's still complected—those 47 dimensions are still braided together.

**You are confusing easy with simple. This confusion is destroying your code.**

You choose familiar complexity over unfamiliar simplicity. You reach for the complicated framework you know. You copy the pattern you've seen before. You mistake "I understand this mess" for "this is not a mess."

Stop.

---

## What Happens When You Complect

Knight Capital lost $440 million in 45 minutes. Boeing's 737 MAX killed 346 people. The Ariane 5 rocket exploded from a data conversion bug.

These are not edge cases. These are symptoms.

GitClear analyzed 211 million changed lines from Google, Microsoft, Meta in 2024:
- Code churn projected to **double** versus 2021
- Code cloning grew **4x** in one year
- Copy-paste now exceeds moved code for the first time in history

AI-generated code shows:
- 30.5% incorrect
- 23.2% partially incorrect
- 4x increase in duplication
- Written 55% faster, with quality decline that eats the savings

Enterprise systems reveal:
- 50+ databases in single organizations
- Hundreds of separate programs
- Byzantine, poorly documented processes
- "Variegated patchworks" nobody fully understands

**When complexity exceeds human comprehension, systems fail.**

The German Tiger tank—a masterpiece of over-engineering—lost to the simpler Soviet T-34 because it couldn't be repaired in field conditions.

Kelly Johnson's 1960 insight from aerospace: design systems an average mechanic can repair in combat with basic tools. Sophisticated systems fail under real constraints.

Software forgot this lesson.

---

## The Law You Cannot Break

**Gall's Law (1975):**

*A complex system that works is invariably found to have evolved from a simple system that worked. A complex system designed from scratch never works and cannot be patched up to make it work. You have to start over with a working simple system.*

You cannot architect complexity upfront and succeed.

Complex systems only work when they evolved from simple systems that worked. Every successful complex system started simple, proved itself, then grew as real needs emerged.

Every failed complex system was architected for imagined requirements that turned out wrong.

Google started with a search bar. Amazon started selling books. Facebook started as a campus directory. They didn't begin with today's complexity. That evolved over years as actual needs emerged.

Your 11-layer architecture designed for scale you'll never reach? It will fail.

Your microservices before you need them? They will fail.

Your elaborate abstractions for flexibility you don't have? They will fail.

**Start simple. Prove it works. Then evolve.**

---

## What the Masters Built

| System | Why It Lasted |
|--------|---------------|
| Unix (50+ years) | Do one thing well. Composable tools. No braiding. |
| UTF-8 | Simple, elegant solution to complex character encoding. |
| Google's homepage | One search bar. Instantly understandable. |
| iPhone | Intuitive design where competitors drowned users in options. |
| Go language | Intentionally simple. "Less is exponentially more." |

The masters understood:

**Tony Hoare (1980):** "There are two ways of constructing a software design: One way is to make it so simple that there are *obviously* no deficiencies. The other is to make it so complicated that there are no *obvious* deficiencies. The first method is far more difficult."

**Edsger Dijkstra:** "Simplicity is prerequisite for reliability. The price of reliability is the pursuit of the utmost simplicity. It is a price which the very rich find most hard to pay."

**Ken Thompson:** "When I see a top-down description of a system with infinite libraries described by layers and layers, all I see is a morass. Maybe I do what I do because if I built anything more complicated, I couldn't understand it."

Thompson wasn't limiting himself. He was recognizing: *if you can't understand it, you can't maintain it, debug it, or evolve it.*

This is wisdom.

---

## Commands

### Attack Complexity at the Source

Participate in planning. Ask "why" for every feature. Propose simpler alternatives.

- 10 fields instead of 20
- Basic search instead of advanced queries
- Core feature instead of edge cases

**Half the battle is preventing complexity from entering requirements.**

Listen to customers. They don't want your elaborate abstractions. They want problems solved.

Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away.

### Delete Code

Remove dead code immediately. Delete speculative "future" code. Delete "just in case" functions.

Every line you don't write is a line you don't maintain, test, debug, or understand.

Less code = fewer bugs.

The best code is no code.

### Write Small Units

Keep methods under 20 lines. Give each function one responsibility.

When you find yourself writing a method that does three things, write three methods.

Use variable names that represent purpose. Never reuse variables for different purposes.

Minimize global state.

**Martin Fowler:** "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."

### Question Every Layer

| Acceptable | Insane |
|-----------|--------|
| 3-4 layers with clear, distinct responsibilities | 11 layers for simple operations |
| Each layer adds measurable value | Layers that exist "just in case" |
| Vertical slicing by feature | Horizontal slicing into API → wrapper → factory → pool → controller → validator → model → persistence → ID-fetcher → CRUD |

For every layer, answer in one sentence: "What value does this add?"

If you can't answer, delete the layer.

### Abstract When Necessary, Not Before

Abstract when you need to generalize **now**. Not for futures that might arrive.

Don't create interfaces until you need to swap implementations.

Having 68 interfaces for 26,000 lines of code is not good practice. It's madness.

| When to Abstract | When to Wait |
|------------------|--------------|
| You have 3+ concrete implementations | You imagine you might need swappability someday |
| Variation exists in production | Variation exists in your head |
| Cost of change is real and measured | Cost of change is theoretical |

**YAGNI applies to abstractions too.**

### Start Monolithic

Microservices add distributed system complexity:
- Network failures
- Eventual consistency
- Distributed transactions
- Deployment coordination
- Monitoring complexity

Don't pay this cost until benefits clearly outweigh it.

Most applications never reach that scale.

**Premature distribution is premature optimization.**

### Build Bottom-Up

Start with the lowest layer needed for your feature. Code only what you need to make it work. Test it.

Move up one layer. Repeat.

This prevents building infrastructure you'll never use.

Top-down design creates elaborate architectures for requirements that change. Bottom-up building creates only what you actually need.

### Resist AI Temptation

AI generates code without comprehension. It violates DRY. It clones similar solutions without understanding context. It creates "just in case" functions. It writes code that needs revision within 2 weeks.

Use AI for suggestions. Never for blind generation.

**Think before accepting.**

Every line of code you add is a line you must understand. If you don't understand it, don't merge it.

---

## When Complexity is Justified

Not all complexity is accidental.

| Essential Complexity | Accidental Complexity |
|---------------------|----------------------|
| Safety-critical systems (aerospace, medical, nuclear) | Enterprise bloat with 11 layers for CRUD |
| High-performance after measuring (real-time, HFT, game engines) | Microservices before you need them |
| Domain complexity (tax code, regulations, scientific computing) | Frameworks with 47 configuration options |
| Professional tools for expert users (compilers, CAD) | Abstractions for futures that don't arrive |

**The goal:** Avoid adding accidental complexity on top of essential complexity.

Einstein: "Make everything as simple as possible, but not simpler."

Don't sacrifice correctness for simplicity. Don't under-engineer by removing necessary functionality.

Bjarne Stroustrup: "If you think it's simple, then you have misunderstood the problem."

**But test your assumptions.** Most problems are simpler than you think. Most complexity is accidental.

---

## The Price of Simplicity

Finding the simple solution is harder than accepting the first complex solution.

"If I had more time, I would have written a shorter letter."

Simplicity takes time upfront. You must:
- Think before coding
- Delete before adding
- Question before building
- Measure before optimizing

**The investment pays off every day afterward** in maintenance, debugging, and feature additions.

Complex code forces you to react to symptoms. Simple code lets you think about problems.

Rob Pike on Ken Thompson: "Ken taught me that thinking before debugging is extremely important. If you dive into the bug, you tend to fix the local issue in the code, but if you think about the bug first, how the bug came to be, you often find and correct a higher-level problem that will improve the design and prevent further bugs."

**This is the discipline.**

---

## Your Choice

| Path A: Complect | Path B: Decomplect |
|------------------|-------------------|
| Keep braiding things together | Separate concerns |
| Add layers "just in case" | Build only what you need |
| Accept AI-generated complexity | Think before accepting |
| Let abstraction multiply | Abstract when necessary |
| Build for imagined futures | Build for actual needs |
| Choose familiar complexity | Choose unfamiliar simplicity |
| **Result: Unmaintainable mess** | **Result: Software that works** |

Complexity is debt. It robs you of capital to invest in the future.

Rob Pike warns: "Everything simple is made too complicated because it's easy to fiddle with; everything complicated stays complicated because it's hard to fix."

You've reached the critical juncture.

Continue adding complexity until your codebase becomes archaeological excavation. Layers upon layers where nobody knows what's happening. Changes that break three things. Bugs that passed all tests. Systems that fail under real conditions.

Or:

**Decomplect.**

Unbraid what should be separate. Delete what adds no value. Build from simple systems that work. Evolve only as real needs emerge.

The masters chose simplicity. The successful companies chose simplicity. The systems that lasted decades chose simplicity.

**Choose simplicity.**

---

*Incidental is Latin for your fault.*
