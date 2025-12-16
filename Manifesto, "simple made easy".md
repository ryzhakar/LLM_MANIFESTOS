# The Simplicity Manifesto

*After Rich Hickey*

---

## The Problem

We have a culture of complexity. We build systems we cannot understand, then blame our tools when they fail us. We confuse *easy* with *simple*, and this confusion is killing our software.

Simplicity is a prerequisite for reliability. You cannot make reliable what you cannot understand. You cannot change what you cannot reason about. Every entanglement you introduce is a burden you will carry forever.

This is not about taste. This is about whether your software works.

---

## The Distinction

**Simple** and **easy** are not the same thing. Learn the difference. Use the words precisely.

**Simple** comes from *sim-plex*: one fold, one braid. Simple means *not interleaved*. It is objective. You can look at a thing and see whether it is tangled with other things.

**Easy** comes from the root of *adjacent*: to lie near. Easy means *close to hand*, *familiar*, *within our capabilities*. It is relative. What is easy for you may be hard for me. What is familiar is not necessarily simple.

We are infatuated with easy. We want tools we can install in five seconds. We want syntax that looks like what we already know. We mistake familiarity for quality.

This infatuation is destroying us.

---

## The Trap

Some things that are easy are also complex. This is the trap.

Object-oriented programming is easy. It is familiar. It is everywhere. It is also complex — it complects state, identity, and value into an inseparable knot.

Inheritance is easy to describe. It is also definitionally complex — it says "these two types are braided together."

Variables are easy. They are in every language. They complect value and time in ways you cannot undo.

Easy and complex can coexist. When they do, easy wins in the short term and complex wins forever after.

---

## The Cost

You will pay for complexity. Not today. Not this sprint. But you will pay.

Every intertwining limits your ability to reason. Every complection adds combinatorial burden. Every hidden dependency is a trap waiting for the next maintainer.

The tests will not save you. Every bug found in the field passed the type checker. Every bug found in the field passed all the tests. When the guardrails fail — and they will fail — you will need to *think*. And you cannot think about what is tangled beyond comprehension.

Guardrails do not guide you anywhere. They just keep you from falling off cliffs you should not be near.

---

## The Terms

Learn this vocabulary. Use it.

**Complect**: to interleave, to braid together, to entangle. This is what you do to your software when you make it worse. It is an old word. Start using it again.

**Compose**: to place together. This is what you should do instead. Composition requires that the things being composed are simple — otherwise you are just complecting at a higher level.

**Incidental complexity**: complexity that was not in the problem. You introduced it. You chose the tool. You made the decision. *Incidental* is Latin for *your fault*.

**Inherent complexity**: complexity that is actually in the problem. This is not your fault. But it is also rarer than you think.

**Construct**: the code you write, the syntax you type, the experience of authoring.

**Artifact**: the running program, the thing the user experiences, the system you must maintain for years.

We optimize for constructs. We should optimize for artifacts. The user does not care how pleasant your typing experience was.

---

## The Toolkit

Complexity has simpler replacements. Choose them.

| Complex | Simple |
|---------|--------|
| State, Objects | Values |
| Methods | Functions, Namespaces |
| Variables | Managed References |
| Inheritance, Switch, Pattern Matching | Polymorphism à la carte |
| Syntax | Data |
| Imperative Loops, Fold | Set Functions |
| Actors | Queues |
| ORM | Declarative Data Manipulation |
| Conditionals scattered through code | Rules, gathered |
| Inconsistency | Transactions, Values |

This is not a ranking of bad to good. It is a map from tangled to untangled. The right column is not pure — it is *simpler*. That is enough.

---

## The Principles

### On State

State complects value and time. When you have state, you cannot get a value independent of when you ask. When you have state, you cannot reproduce what happened at the client. When you have state, you have poison — it leaks through every abstraction you wrap around it.

The only cure is a functional interface: same input, same output. If the wrapper is still stateful — if you can ask the same question twice and get different answers — the complexity has escaped.

This has nothing to do with concurrency. Single-threaded programs full of variables are just as incomprehensible.

### On Information

Information is simple. The only thing you can do to information is ruin it.

Objects were made to encapsulate I/O devices — screens you cannot touch, mice you cannot reach. They were never meant for information. Applying them to data is a category error.

When you wrap data in objects, you destroy your ability to build generic operations. You tie your logic to representation. You create thousands of variations where a handful of structures would suffice.

Data has few essential forms: maps, sets, sequences. That is nearly all. Represent data as data. Use maps. Use sets. Stop writing classes for every new piece of information.

### On Abstraction

To abstract is to draw away — specifically, to draw away from the physical nature of something. Abstraction is not hiding. Hiding changes nothing about complexity. Abstraction means engaging only with what matters.

Design by asking: who, what, when, where, why, how. Then *keep them separate*.

**What**: the operations, the specifications. Make them small — far smaller than you think. Use only values and other abstractions in their definitions. Never let "what" dictate "how."

**Who**: the entities, the data. Build from subcomponents. Inject dependencies. You should have more subcomponents than you do.

**How**: the implementation. Connect via polymorphism. Keep implementations as islands. The more declarative, the better.

**When and Where**: decouple ruthlessly. If A calls B directly, you have complected when and where. Put a queue between them. Queues solve this problem. Use queues extensively.

**Why**: the policy, the rules. Gather them. Do not scatter conditionals throughout your code. Find a declarative system. Make the rules visible.

### On Modularity

Modularity is necessary but not sufficient.

You can write modular software that is completely complected. Separate classes that assume everything about each other. Clean APIs that secretly depend on timing. Layers that look independent but share hidden state.

Partitioning does not imply simplicity. Simplicity enables partitioning. The components must be simple *first* — only then does separation help.

Do not be fooled by code organization. Look for the hidden dependencies. Look for what one part must know about another. That is where the complexity lives.

---

## The Practice

### Choose Simpler Constructs

Start here. Before you write anything, choose tools that produce simpler artifacts.

- **Values**: Use `final`, `val`, `const`. Find persistent collections for your language.
- **Functions**: Stateless methods. Most languages have them.
- **Data**: Maps, sets, sequences. Not classes for every noun.
- **Queues**: For decoupling when and where.
- **Declarative data manipulation**: SQL, LINQ, Datalog.
- **Polymorphism à la carte**: Protocols, type classes — if your language has them. If not, find approximations.

### Simplify Before You Start

You cannot go as fast as possible from the beginning if you care about simplicity. There is ramp-up. Accept it.

The alternative is to start fast and slow down forever. Complexity accumulates. Each sprint accomplishes less. Eventually you are rewriting what you already wrote. The net forward motion approaches zero.

Spend time up front. Think before you type. The investment pays compound interest.

### Develop Entanglement Radar

Train yourself to see complecting. Look at software and ask: what is interleaved here that could be independent? What does this component know about that component that it should not need to know?

This is where the leverage is. Not in names, not in formatting, not in syntactic preferences. In the interconnections that did not need to exist.

### Accept More Parts

When you simplify, you often end up with more things. This is correct.

Simplicity is not about counting. Four straight lines are simpler than two knotted ones. More pieces, hanging cleanly, are simpler than fewer pieces tangled together.

The pieces that are separate can be changed independently. That is the payoff.

> Simplicity is the ultimate sophistication.
_- Leonardo da Vinci_
---

## The Choice

Simplicity is a choice. It requires vigilance. It requires discipline. It requires refusing the easy path when the easy path is complex.

Your sensibilities are wrong. You have been trained to equate simple with easy. They are different things.

The guardrails will not save you. Tests, types, refactoring tools — these are safety nets, not solutions. They do not touch the core problem.

You can build the same systems you build now with dramatically simpler tools. You do not need the complexity. You never did.

The complexity is your fault. The simplicity can be too.

Choose.
