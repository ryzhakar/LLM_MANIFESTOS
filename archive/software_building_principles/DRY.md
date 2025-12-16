
# MANIFESTO: Don't Repeat Yourself (DRY)

## Knowledge duplication is technical debt, and you're accumulating it faster than ever

**Every software system is a repository of knowledge**—business rules, domain logic, system behavior, validation rules, transformation logic, API contracts. When that knowledge exists in multiple places, those representations inevitably fall out of sync. Someone fixes a bug in one location but misses another. Requirements change and only half the copies get updated. **The result:** a codebase where you can't trust anything because truth has no single source. This isn't a minor problem—it's the maintenance nightmare that brings entire engineering organizations to a standstill. The solution is DRY: **Don't Repeat Yourself.** But almost everyone misunderstands what it actually means.

**Dave Thomas and Andy Hunt coined DRY** in their 1999 book "The Pragmatic Programmer: From Journeyman to Master." The principle's actual definition: **"Every piece of knowledge must have a single, unambiguous, authoritative representation within a system."** Read that carefully. It says **knowledge,** not code. It says **within a system,** which includes databases, tests, documentation, build systems, and configurations—not just source code. Most developers reduce DRY to "don't copy-paste code," missing the entire point. Thomas himself later said: "Don't Repeat Yourself (or DRY) is probably one of the most misunderstood parts of the book."

The principle emerged from Thomas and Hunt's observation that programmers are "constantly in maintenance mode" from day one. Hunt states: "It's only the first 10 minutes that the code's original, when you type it in the first time. That's it." After those 10 minutes, you're maintaining—fixing bugs, adding features, adapting to changes. When knowledge is duplicated, every change requires updating multiple locations. Miss one, and your system has inconsistent behavior. **This is the Whack-a-Mole problem:** fix one issue, two more pop up elsewhere. You constantly push them back, and you never finish.

## The distinction that changes everything: knowledge duplication versus incidental duplication

**Here's what most developers get wrong:** Not all code duplication is DRY violation. **DRY is about knowledge duplication, not syntax duplication.** Two pieces of code can look identical but represent completely different knowledge in your system. Merging them would be a mistake—you'd create coupling between unrelated concerns that should evolve independently.

Consider this example from Thomas Benard:

```
// Validation for user description  
public bool isLongEnough() {
  String words[] = description.split(' ');
  return words.length > 10;
}

// Validation for API response
public bool containsEnoughElements() {
  String elements[] = description.split(' ');  
  return elements.length > 10;
}
```

**These look identical.** Static analysis tools flag them as duplication. But they represent **different knowledge**—one is a user input validation rule (a business constraint on what users can submit), the other is an API response viability check (a technical constraint on external data). They happen to have the same implementation today, but they could diverge tomorrow for completely unrelated reasons. User descriptions might require 20 words while API responses need only 5. **Merging them creates inappropriate coupling.**

**Anthony Sciamanna calls this "incidental duplication"**—code that looks the same but represents different behaviors in the system. It's duplication of syntax that doesn't duplicate behavior, knowledge, or system concepts. **Removing incidental duplication creates the opposite of the desired effect:** it makes code harder to understand and harder to change in the future. You've coupled things that should remain independent, forcing future changes to one concern to consider impacts on an unrelated concern.

Static analysis tools can only detect syntax duplication, not knowledge duplication. Blindly removing all duplication that triggers static analysis warnings leaves code in worse shape. **The acid test from The Pragmatic Programmer:** "When some single facet of the code has to change, do you find yourself making that change in multiple places, and in multiple different formats?" If yes, you have a DRY violation. If no—if the code might change for different reasons at different times—you don't.

## The catastrophic cost of violating DRY: real maintenance nightmares

When knowledge is duplicated, the costs compound viciously:

**Kent C. Dodds' experience:** "Once, I inherited a codebase that made very heavy use of code duplication and one time I had to fix a bug in **eight different places!** 😱 Talk about irritating! Abstracting that code into a function that could be called anywhere it was needed would've helped out a LOT."

Eight places means eight times the development effort, eight times the testing effort, **eight opportunities to miss one location and create inconsistency.** Every developer who's maintained legacy systems knows this horror: you fix a bug, push to production, then discover the same bug exists in three other modules you didn't know about. Users report the "fixed" bug still happening. You hunt through the codebase finding duplicates. **You become the Whack-a-Mole player Dave Thomas described.**

The costs break down into four categories:

**Development effort multiplies.** Every change requires finding all duplicates. Miss one, create a bug. Teams spend more time searching for duplicates than implementing features.

**Test effort multiplies.** Re-test each clone location. Each clone could break independently. Test matrices explode.

**Quality risk escalates.** Human error in overlooking clones is inevitable. The more duplicates, the higher the probability of missing one. **Any bugs or vulnerabilities within code are replicated when blocks are copy-pasted.**

**Code base bloats.** More lines mean more surface area for bugs, more to understand when onboarding, more to search through when debugging. Bloated codebases slow everything down.

One developer described their "elegant code" turning into "a very difficult, hackish, buggy, and high maintenance mess" after duplicating logic that kept requiring special case modifications. Each client change required updating all copies with slight variations until the duplicates diverged into unmaintainable variants. **This is the natural entropy of duplication**—copies diverge, becoming maintenance nightmares where you can't tell which version is "correct."

## The wrong abstraction is worse than duplication: the lesson everyone learns too late

The flip side of DRY is over-applying it, creating what **Sandi Metz** immortalized in her 2016 blog post as **"the wrong abstraction."** Her principle: **"Duplication is far cheaper than the wrong abstraction"** and **"prefer duplication over the wrong abstraction."**

The wrong abstraction pattern emerges predictably:

1. Programmer A sees duplication
2. Programmer A extracts it and gives it a name (creates abstraction)  
3. Programmer A replaces duplication with the abstraction
4. Time passes
5. New requirement appears that's *almost* perfect for the abstraction
6. Programmer B adds a parameter and conditional logic
7. What was once universal now behaves differently for different cases
8. Another requirement arrives → another parameter → another conditional
9. **Loop until code becomes incomprehensible**

**The result:** "The code no longer represents a single, common abstraction, but has instead become a condition-laden procedure which interleaves a number of vaguely associated ideas. It is hard to understand and easy to break." **The abstraction has become the complexity.** What started as eliminating duplication ended with code more complex than the original duplicates would have been.

**The sunk cost fallacy** makes it worse. Metz observes: "The more complicated and incomprehensible the code, i.e. the deeper the investment in creating it, the more we feel pressure to retain it. It's as if our unconscious tells us 'Goodness, that's so confusing, it must have taken ages to get right. Surely it's really, really important.'" Developers keep adding conditionals to broken abstractions rather than admitting the abstraction was wrong and starting over.

A real example from a LinkedIn discussion: "We had a pile of up to 5 abstraction classes in Python... 'Base'→'BaseThing'→'BaseAPIThing'→'HABaseThing'→'The Actual Thing under development'. In exchange for not duplicating code, we could not make updates to the shared code without potentially breaking 60-70 other libraries." **This is enterprise over-engineering at its worst**—DRY misapplied creates fragile coupling across the entire codebase.

## The dual threats: enterprise wrong abstractions and AI code cloning

Modern development faces DRY violations from two sources:

**Over-engineered enterprise software** creates wrong abstractions at scale. Enterprise architects see any duplication as failure, rushing to abstract before understanding whether the similarity is knowledge duplication or incidental duplication. **The result:** parameter-laden, conditional-riddled shared code that couples unrelated concerns. Changes to one feature require considering impacts on dozens of others through shared abstractions. "Shared libraries" become bottlenecks where no team can change anything without coordinating with everyone.

**Martin Fowler and Kent Beck** identified "duplicated code" as "number one in the stink parade" in their book "Refactoring," but they meant knowledge duplication. Enterprise developers misread this as "all duplication is bad," leading to premature abstraction. **The rule they should have remembered:** Don Roberts' "Rule of Three"—the first time you do something, you just do it. The second time, you wince at duplication but duplicate anyway. **The third time you do something similar, you refactor.** Three instances give you enough information to identify the right abstraction. Two instances don't.

**AI-era coding sloppiness** creates the opposite problem: massive knowledge duplication through code cloning. AI tools are creating a **technical debt nightmare.** GitClear's research shows AI generates code at speed without considering best practices, leading to **code cloning** where code is duplicated across different parts instead of consolidated into reusable modules. When a bug needs fixing in duplicated code, engineers must "track down and patch the same issue across multiple locations." A 2023 study from Central China Normal University found **code duplication leads to higher defect rates.**

**The cost impact** of AI-driven duplication: higher cloud storage expenses, longer testing cycles, more resources debugging, technical debt accumulation. As GitClear CEO Bill Harding warns, measuring developer productivity by commits or lines written in the AI era will accelerate technical debt catastrophically. AI doesn't factor in long-term costs—it just keeps generating more code. **AI-generated code "resembles an itinerant contributor, prone to violate DRY-ness" across every repository it touches.**

Both forces—enterprise wrong abstractions and AI code cloning—violate DRY, just from opposite directions. One abstracts too early, the other duplicates too freely. **Both create unmaintainable codebases.**

## Real success: when DRY actually improves systems

**Dave Thomas' number formatting story** shows DRY done right. He worked on a large web application for online membership registration. When numbers grew from hundreds to tens of thousands, the client wanted commas in all numbers for readability. **Result:** "Luckily, I only had one change to make, and every number the system outputted then had commas in it." One change propagated throughout the entire system automatically—this is successful DRY implementation.

**An e-commerce platform** had similar code for product filtering across multiple pages: search results, recommendations, and related products. After refactoring to a single reusable function:
- **Efficiency boost:** Only one code segment needs updates for new product attributes
- **Reduced bugs:** Issues in filtering corrected once, improving user experience across the platform  
- **Collaborative ease:** All developers reference the same function, reducing misunderstandings and onboarding time

**dbt Labs' analytics example:** For subscription-based companies, Monthly Recurring Revenue (MRR) and Customer Lifetime Value (CLV) are essential metrics calculated throughout systems. **DRY solution:** "By writing DRY definitions for key business logic and metrics that are referenced throughout a dbt project and/or BI tool, data teams can create those single, unambiguous, and authoritative representations for their essential transformations." **The benefit:** consistent definitions and values across all reporting and analysis. No more "which MRR number is correct?" debates.

These success stories share characteristics: **they abstracted actual knowledge duplication,** not incidental similarities. They waited until the duplication was painful before abstracting. They created abstractions that remained stable—they didn't require constant parameter additions and conditional modifications.

## How to apply DRY correctly: practical wisdom for identifying true duplication

**The Rule of Three** prevents premature abstraction. Martin Fowler in "Refactoring" attributed this to Don Roberts: **"The first time you do something, you just do it. The second time you do something similar, you wince at the duplication, but you do the duplicate thing anyway. The third time you do something similar, you refactor."** Or: "Three strikes, then you refactor."

Why wait until three? **Prevents premature abstraction**—waiting provides more context about what the right abstraction should be. With only two instances, you might select an abstraction that doesn't fit future needs. After three instances, commonalities and differences become clearer.

**Ask these questions before abstracting:**

1. **"Are we looking at syntax duplication or knowledge duplication?"** If it's the same code but representing different business concepts, don't abstract.

2. **"Will this code change together or independently?"** If independently, it's incidental duplication—keep it separate.

3. **"Does this represent the same business rule/domain concept?"** If not, don't abstract even if code looks identical.

4. **"When some single facet of the code has to change, do you find yourself making that change in multiple places?"** This is the acid test—if yes, you have real knowledge duplication.

**Mathias Verraes' principle:** "'Don't Repeat Yourself' was never about code. It's about knowledge. It's about cohesion. If two pieces of code represent the exact same knowledge, they will always change together." **This is the test:** if they change together, they're knowledge duplication. If they change independently for different reasons, they're incidental duplication.

**When you find the wrong abstraction,** Metz's prescription is brutal but effective: **the fastest way forward is back.**

1. **Re-introduce duplication** by inlining the abstracted code back into every caller
2. **Within each caller,** use the parameters to determine the subset of inlined code this specific caller executes
3. **Delete the bits** that aren't needed for this particular caller
4. **Start fresh:** re-isolate duplication and re-extract abstractions with better understanding

**"If you find yourself passing parameters and adding conditional paths through shared code, the abstraction is incorrect."** Delete it. Start over. The sunk cost fallacy says this is wasteful—you invested so much in that abstraction! The reality is that keeping broken abstractions wastes far more effort than deleting them.

## When duplication is acceptable: critical exceptions to DRY

DRY has important limits:

**Context-specific logic** serving completely different business domains should be duplicated. Code that crosses microservice or module boundaries may be better duplicated—sharing code between services creates coupling that defeats the purpose of service boundaries. **Bounded contexts** in Domain-Driven Design explicitly allow duplication across context boundaries to maintain independence.

**Research or experimental code** with limited lifespan doesn't need abstraction. **One-time scripts**—migration scripts, temporary utilities—should prioritize clarity over DRY. You'll never maintain them, so duplication doesn't create maintenance burden.

**The "WET" principle**—"Write Everything Twice"—offers a middle ground. Conlin Durbin's definition: "You can ask yourself 'Haven't I written this before?' two times, but never three." This aligns with the Rule of Three—tolerate duplication twice, refactor on the third instance.

**AHA Programming** (Avoid Hasty Abstractions), coined by Cher Scarlett and popularized by Kent C. Dodds, emphasizes: **"Optimize for change first."** Dodds writes: "I think the key is that we don't know what the future of code will be. We could spend weeks optimizing code for performance, or coming up with the best API for our new abstraction, only to find out the next day that we made incorrect assumptions." **Recommendation:** "Don't be dogmatic about when you start writing abstractions but instead write the abstraction when it feels right and don't be afraid to duplicate code until you get there."

## The path forward: knowledge management as core discipline

**Robert C. Martin (Uncle Bob)** from "97 Things Every Programmer Should Know": "Every line of code that goes into an application must be maintained, and is a potential source of future bugs. Duplication needlessly bloats the codebase, resulting in more opportunities for bugs and adding accidental complexity to the system."

DRY remains profoundly relevant because **programming is fundamentally about managing knowledge,** not just writing code. Every software system crystallizes business logic, domain understanding, and system behavior. When that knowledge is scattered across multiple locations, it becomes fragile, inconsistent, unmaintainable, and costly.

**The balanced perspective:**
- Not all code duplication is knowledge duplication  
- Premature abstraction is worse than duplication
- Context matters—duplication across bounded contexts may be preferable
- Wait for patterns to emerge (Rule of Three)

**Against over-engineering:** Wrong abstractions create unmaintainable parameter-laden, conditional-riddled code that's harder to change than duplicated code would have been.

**Against AI sloppiness:** As AI tools generate code at unprecedented speed without considering maintainability, DRY principles become more critical than ever to combat the explosion of technical debt from code cloning.

**The path forward** requires:
1. Understanding the principle's true meaning—it's about knowledge representation
2. Practicing discernment—learning to distinguish incidental from essential duplication  
3. Embracing the Rule of Three—resisting premature abstraction
4. Being willing to delete bad abstractions—sometimes the fastest way forward is back
5. Optimizing for change—making decisions based on how code will evolve, not present state

**Sandi Metz's final wisdom:** "When the abstraction is wrong, the fastest way forward is back. This is not retreat, it's advance in a better direction." **Apply DRY to knowledge duplication. Tolerate incidental duplication. Delete wrong abstractions. Build software that can actually evolve.**