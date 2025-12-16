# MANIFESTO: Keep It Simple, Stupid (KISS)

## Complexity is killing your software, and simplicity is the only cure

**Software development faces a crisis.** Complexity has exploded beyond control—GitClear's 2024 study analyzing 211 million changed lines from Google, Microsoft, and Meta found that code churn is projected to **double in 2024** versus 2021, with a **4x growth in code cloning** between 2023-2024 alone. Meanwhile, enterprise systems bloat with 11-layer architectures where simple operations require navigating through APIs, wrappers, factories, pools, controllers, validators, shared code layers, and interfaces—turning 2-hour tasks into 2-day nightmares. This isn't progress. This is complexity killing productivity, sucking the life out of developers, and making software impossible to maintain. The solution isn't newer frameworks, more sophisticated patterns, or AI-generated code. The solution is a return to first principles: **Keep It Simple, Stupid.**

The KISS principle emerged from aerospace engineering, not software. **Kelly Johnson** of Lockheed Skunk Works coined it in 1960 while designing the U-2 and SR-71 Blackbird spy planes. His challenge to engineers was brutal: design jet aircraft that an average mechanic could repair in combat conditions with only a handful of basic tools. The "stupid" didn't insult engineers—it acknowledged that sophisticated systems fail under real-world constraints. When your F-16 takes damage over enemy territory, you need repairs that work with what's available, not solutions that require specialized equipment back at base. This principle created some of aviation's greatest achievements precisely because it eliminated unnecessary complexity while maintaining sophistication where it mattered.

Software forgot this lesson. We've created systems so complex that changing one thing breaks three others in a never-ending game of Whack-a-Mole. We've built 68 interfaces for 26,759 lines of code—one interface per 393 lines—in systems with 11 architectural layers for operations that should take minutes. We've normalized architecture where "simple" user operations traverse APIs, wrappers, server factories, controller pools, validation layers, anemic model layers, persistent layer interfaces, ID-fetching layers, and finally CRUD layers. This isn't engineering. This is madness disguised as sophistication.

## Simplicity is objective, not subjective—and we can measure our failure

**Rich Hickey's 2011 Strange Loop talk "Simple Made Easy"** remains the definitive modern articulation of KISS. Hickey distinguishes **simple** from **easy** with surgical precision. Simple comes from Latin "sim-plex"—literally "one fold" or "one twist." **Simple means things are not intertwined, not braided together.** It's an objective property: components are either coupled or they aren't, responsibilities are either mixed or they aren't. Complexity occurs when we "complect"—interleave, entwine, braid—things that should remain separate.

**Easy** is different—it means near at hand, familiar to our current understanding or skill set. Easy is relative and subjective. Something complex can be easy if you're used to it. A framework with 47 configuration options is "easy" once you've memorized them, but it's not simple—those options represent 47 different dimensions braided together. **This confusion between simple and easy is destroying software quality.** We choose familiar complexity over unfamiliar simplicity because it feels productive in the moment. We reach for the complicated framework we know rather than the simple solution we'd need to think through.

The evidence of our failure is overwhelming. Knight Capital's complex trading algorithm deployed incorrectly in 2012 lost **$440 million in 45 minutes.** Boeing's 737 MAX crashes killed 346 people partly due to over-complex automated flight systems without proper safeguards. The Ariane 5 rocket exploded in 1996 from a data conversion issue—64-bit to 16-bit—that revealed lack of understanding of architectural simplicity. These aren't edge cases. They're symptoms of complexity exceeding human comprehension.

NASA lists "excessive features" as a top 10 risk factor for project failure. Studies of enterprise back-office systems reveal 50+ databases and hundreds of separate programs creating "variegated patchworks" with "Byzantine and poorly documented customized processes." **The German Tiger and Panther tanks of WWII—masterpieces of over-engineering with expensive materials and labor-intensive production—proved inferior to the simpler Soviet T-34 because they couldn't be repaired in field conditions.** Kelly Johnson's original insight keeps proving itself: systems that can't be maintained under real conditions are systems that fail.

## The dual threats: enterprise complexity and AI sloppiness both add complexity without understanding

Today's software suffers from two distinct but equally destructive forces, and KISS stands in opposition to both.

**First, over-engineered enterprise software** driven by smart developers trying to be too clever. **Ray Ozzie warned in 2005:** "Complexity kills. It sucks the life out of developers; it makes products difficult to plan, build, and test; it introduces security challenges; and it causes user and administrator frustration." InfoWorld noted in 2021 that if Ozzie thought things were complicated in 2005, he'd be horrified by cloud-native era complexity. Enterprise architects build for hypothetical futures that never materialize. Teams adopt microservices before they're needed, creating distributed system complexity. Developers pursue "design pattern bingo," adding factories, decorators, observers, and command patterns to CRUD applications that need none of them. **Max Kanat-Alexander defined over-engineering perfectly in 2008:** "When your design actually makes things more complex instead of simplifying things, you're over-engineering."

The pattern is always the same: assume the system will need extensive flexibility, build elaborate abstractions to support it, then watch as actual requirements never match the abstraction. The "lasagna architecture" emerges—layer upon layer of indirection where each layer exists not because it solves a problem but because it might enable a solution to a problem that might exist someday. Meanwhile, implementing actual features becomes exponentially harder as you navigate the maze of abstractions.

**Second, sloppy AI-era coding** that generates code without comprehension. GitClear's 2024 study is devastating: AI-generated code shows a **4x increase in code cloning,** with copy-paste exceeding moved code for the first time in history. The code "resembles an itinerant contributor, prone to violate DRY-ness." Stanford research found programmers using AI assistants "wrote significantly less secure code." A 2023 Bilkent University study found **30.5% of AI-generated code was incorrect, 23.2% partially incorrect.** GitHub's data shows developers write code "55% faster" with Copilot—but there's a significant decline in quality and maintainability that eats up those savings in maintenance and debugging.

**The core problem:** AI generates additions but never updates, deletions, or moves. It lacks context about your library versions, environment, or API. It creates code "just in case" without understanding whether you actually need it. It replicates similar solutions without considering appropriateness. It generates short-term code requiring revision within 2 weeks—a telltale sign of not thinking through the problem. As Lee Atchison, former Amazon architect, observes: "Code complexity and the support costs associated with complex code have increased in recent years in large part due to the proliferation of AI-generated code use."

**Both over-engineering and AI sloppiness share the same fundamental flaw:** they add complexity without adding understanding. One comes from smart people being too clever; the other from tools generating code without comprehension. Both produce systems where nobody fully understands what's happening, where changes have unpredictable effects, where debugging becomes archaeological excavation rather than systematic problem-solving.

## Simple beats clever every time—the evidence from masters who built systems that lasted decades

The greatest software systems and companies were built on simplicity, not sophistication.

**Unix** lasted 50+ years because of its philosophy: "Do one thing and do it well." Small, composable tools that work together. Rob Pike and Ken Thompson's work on UTF-8 provided a simple, elegant solution to the complex character encoding problem that's still standard today. **Google's homepage**—a single search bar and minimal text—became the world's most-used search engine through interface simplicity despite algorithm complexity underneath. No onboarding needed, instantly understandable. **The iPhone** won through intuitive design and straightforward navigation where feature-laden competitors drowned users in options.

**Golang** succeeded specifically because Rob Pike, Ken Thompson, and Robert Griesemer designed it with intentional simplicity to solve Google's problems. Pike wrote: "Go was not designed by committee" and "Less is exponentially more." The language's success is directly attributable to its simplicity focus. **Minimum Viable Products** succeeded for Airbnb, Dropbox, and Spotify because they focused on one core problem with simple solutions, then iterated based on real user feedback rather than building everything they imagined they'd need.

The masters of computing understood this deeply. **Tony Hoare** in his 1980 Turing Award lecture: "There are two ways of constructing a software design: One way is to make it so simple that there are obviously no deficiencies and the other way is to make it so complicated that there are no obvious deficiencies. **The first method is far more difficult.**" **Edsger Dijkstra:** "Simplicity is prerequisite for reliability. The price of reliability is the pursuit of the utmost simplicity. It is a price which the very rich find most hard to pay."

**Ken Thompson's** approach reveals the philosophy: "When I see a top-down description of a system or language that has infinite libraries described by layers and layers, all I just see is a morass. I can't get a feel for it. Maybe I do what I do because if I built anything more complicated, I couldn't understand it." Thompson wasn't limiting himself through lack of ability—he was recognizing that if he couldn't understand it, he couldn't maintain it, debug it, or evolve it. **This is wisdom, not limitation.**

**Rob Pike** observed about Thompson: "Ken taught me that thinking before debugging is extremely important. If you dive into the bug, you tend to fix the local issue in the code, but if you think about the bug first, how the bug came to be, you often find and correct a higher-level problem in the code that will improve the design and prevent further bugs." Simple code lets you think about problems. Complex code forces you to just react to symptoms.

## John Gall's Law proves you cannot start complex and succeed

**John Gall's 1975 book "Systemantics"** introduced Gall's Law, fundamental to understanding why KISS matters: **"A complex system that works is invariably found to have evolved from a simple system that worked. A complex system designed from scratch never works and cannot be patched up to make it work. You have to start over with a working simple system."**

This isn't opinion—it's observation from decades of systems across domains. You cannot architect complexity upfront and expect success. **Complex systems only work when they evolved from simple systems that worked.** Every successful complex system has a history: it started simple, proved itself, then grew organically as real needs emerged. Every failed complex system was architected for imagined requirements that turned out wrong.

The evidence surrounds us. Successful startups begin with MVPs—laughably simple versions that prove the concept—then evolve. Failed startups spend years building sophisticated platforms for markets that don't exist. Successful open-source projects start solving one problem well, then expand. Failed projects try to be everything to everyone from day one. **Google, Amazon, Facebook—all started with simple solutions to focused problems.** Their current complexity evolved over years as actual needs emerged, not from initial grand designs.

## How to apply KISS in practice: concrete techniques for writing simple code

Applying KISS requires discipline and specific practices:

**Attack business complexity directly.** Participate in planning meetings. Ask "why" questions about features. Propose simpler alternatives—10 fields instead of 20, basic search instead of advanced queries. Listen to customers to discard unnecessary features. **Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away.** Half the battle is preventing complexity from entering requirements.

**Delete code aggressively.** Remove dead code immediately. Delete speculative "future" code. Every line of code you don't write is a line you don't have to maintain, test, debug, or understand. Less code means fewer bugs and easier maintenance. **Rob Pike's five rules of programming** start with: "You can't tell where a program will spend its time" and "Measure. Don't tune for speed until you've measured." Most optimization is waste—measure first, then optimize only what matters.

**Keep methods under 20 lines.** Give each class and function one responsibility. Use variable names that accurately represent purpose—never reuse variables for different purposes. Minimize global state. When you find yourself writing a method that does three things, write three methods. **Martin Fowler:** "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."

**Question every layer.** Maximum 3-4 layers for most applications. Each layer should have clear, distinct responsibility. Ask for every layer: "Is this adding value or just indirection?" If you can't articulate what value a layer provides in one sentence, you don't need it. Vertical slicing by feature beats horizontal slicing by layer.

**Use abstractions carefully.** Abstract when you need to generalize NOW, not in the future. Ensure abstractions are cohesive—things that belong together. Don't create interfaces until you need to swap implementations. Having 68 interfaces for 26,000 lines is **insanity dressed as good practice.**

**Start with monoliths, split when necessary.** Microservices add distributed system complexity: network failures, eventual consistency, distributed transactions, deployment coordination, monitoring complexity. Don't pay that cost until the benefits clearly outweigh it. Most applications never reach that scale.

**Practice bottom-to-top development.** Start with the lowest layer needed for your feature. Code only what you need to make it work. Test it. Refactor if necessary. Move up one layer. Repeat. This prevents building infrastructure you'll never use.

## When KISS doesn't apply: the critical exceptions

KISS has limits, and understanding them prevents misapplication:

**Safety-critical systems** justify complexity when lives are at stake—aerospace, medical devices, nuclear systems need redundancy and verification. But each component should still be as simple as possible. **High-performance systems** for real-time applications, high-frequency trading, or game engines may need complex algorithms after measuring performance and confirming simpler solutions won't work.

**Domain inherent complexity** exists in tax code, regulatory compliance, scientific computing. Some problem domains are inherently complex. The goal isn't to make them simple—that's impossible—but to avoid adding accidental complexity on top of essential complexity. **Specialized professional tools** for experts (compilers, CAD software, professional video editing) appropriately serve users who can handle complexity.

**Einstein's warning applies:** "Make everything as simple as possible, but not simpler." Don't sacrifice correctness for simplicity. Don't under-engineer by removing necessary functionality. **Bjarne Stroustrup:** "If you think it's simple, then you have misunderstood the problem." Deep understanding often reveals why problems need careful solutions.

**Simplicity takes time upfront.** As the saying goes: "If I had more time, I would have written a shorter letter." Finding the simple solution is often harder than accepting the first complex solution that comes to mind. But the investment pays off every day afterward in maintenance, debugging, and feature additions.

## The path forward: simplicity as competitive advantage

**Dave Cheney captures it:** "Complexity is debt, it robs you of capital to invest in the future. Good programmers write simple programs." **Rob Pike warns:** "Such is modern computing: everything simple is made too complicated because it's easy to fiddle with; everything complicated stays complicated because it's hard to fix."

We've reached a critical juncture. Complexity continues accelerating. Enterprise systems grow more Byzantine. AI tools generate code faster than we can understand it. **The only way forward is back to fundamentals.** KISS isn't a limitation—it's liberation. Simple code is code you can understand, modify, debug, and trust. Simple systems are systems you can reason about, predict, and control.

Your choice is clear: continue adding complexity until your codebase becomes unmaintainable, or embrace simplicity and ship software that actually works. The masters chose simplicity. The successful companies chose simplicity. The systems that lasted decades chose simplicity. **Choose simplicity. Keep It Simple, Stupid.**