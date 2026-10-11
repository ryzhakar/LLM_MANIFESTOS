BOUND: First Principles (/home/user/LLM_MANIFESTOS/manifestos/first-principles.md, full); Strunk SPR v3 (/home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml, 2923 lines, full); manifesto-oath protocol (/home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md, full)  
INTERPLAY: First Principles and Strunk converge on the irreducible, concrete unit over the inherited or vague form, and the oath converges on scanning every output for violations; they pull apart where First Principles discards convention while Strunk's Judgment Protocol keeps it, and where Strunk's latitude pulls against this audit's no-judgment scope; resolution: the verbatim quote with file:line is the atom, prose stays active, positive, and terse, extraction never interprets.  
COMMIT: I must reduce every claim to a verbatim quote with file:line, and I will check each row against its source line by script; I must write concrete, active, positive prose without needless words, and I will cut every sentence that carries no fact; I must not judge overlap or recommend, and I will not.

# Collection Overlap Audit — volume, debt, dependencies, reuse

## Claims

Label: every row is doctrine (the manifesto text states it). No row is learned or practiced.

Paths: a manifesto row cites `/home/user/LLM_MANIFESTOS/manifestos/NAME`; an `archive:NAME` row cites `/home/user/LLM_MANIFESTOS/archive/software_building_principles/NAME` (pre-collection source).

Topics: `volume` (code volume, line count) · `cost-debt` (code as cost, debt, liability, asset) · `deletion` · `dependencies` (dependencies, packages, libraries, imports, adopted systems) · `reuse-components` (reuse, abstraction, components) · `trust-ownership` (trust or ownership of code one did not write) · `maintenance-economics`.

Stance: the polarity the quote gives the thing it names. `for` = commended or required; `against` = condemned or warned off; `conditional` = commended or condemned only under a stated condition. The named thing decides, not the topic tag: "Codebase bloats" is `against` (bloat); "Less code = fewer bugs." is `for` (less code).

Quotes drop markdown emphasis markers (`**`, `*`, backticks) and nothing else (`\|` inside a quote is the table escape for `|`); each quote was matched against its source line by script and holds 25 words or fewer. Out by sense, no row: Rust value ownership (correct-by-construction.md:92, 271); "dependency" as reliance on an intervener (intervention.md:61); "reuse variables" (kiss.md:171); license headers as comments (self-documenting-code.md:42). Rows from intervention.md concern trust in an inherited system's self-report. Row self-documenting-code.md:288 concerns comments.

| file | line | quote | topic | stance |
|---|---|---|---|---|
| correct-by-construction.md | 25 | "Silent failure is not ease. It is debt with compound interest." | cost-debt | against |
| correct-by-construction.md | 136 | "The abstraction is free." | reuse-components | for |
| correct-by-construction.md | 224 | "Maintenance \| Refactor with confidence \| Refactor with fear" | maintenance-economics | for |
| correct-by-construction.md | 229 | "The "fast" language is slow in the moments that cost the most: 3am debugging, six-month-old code" | maintenance-economics | against |
| correct-by-construction.md | 231 | "Pay at compile time or pay forever in production." | maintenance-economics | for |
| correct-by-construction.md | 273 | "Pay upfront. Compile-time strictness is cheaper than runtime debugging." | maintenance-economics | for |
| dry.md | 13 | "Knowledge duplication is destroying your codebase." | reuse-components | against |
| dry.md | 17 | "This is what kills velocity, breeds bugs, and turns engineering teams into archaeological expeditions" | maintenance-economics | against |
| dry.md | 27 | "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system." | reuse-components | for |
| dry.md | 68 | "Abstract it \| Keep it separate" | reuse-components | conditional |
| dry.md | 70 | "Removing incidental duplication creates coupling. Coupling creates fragility." | reuse-components | against |
| dry.md | 74 | "When some single facet of the code has to change, do you find yourself making that change in multiple places?" | reuse-components | conditional |
| dry.md | 84 | "Eight places. One bug. Eight fixes required." | maintenance-economics | against |
| dry.md | 92 | "Development effort multiplies" | maintenance-economics | against |
| dry.md | 93 | "Test effort multiplies" | maintenance-economics | against |
| dry.md | 95 | "Codebase bloats" | volume | against |
| dry.md | 97 | "One developer inherited code where fixing a single bug required changes in eight different places." | trust-ownership | against |
| dry.md | 97 | "a difficult, hackish, buggy, high maintenance mess" | maintenance-economics | against |
| dry.md | 103 | "The wrong abstraction is worse than duplication." | reuse-components | conditional |
| dry.md | 117 | "We could not make updates without potentially breaking 60-70 other libraries." | dependencies | against |
| dry.md | 119 | "You keep adding conditionals to broken abstractions rather than admitting the abstraction was wrong." | reuse-components | against |
| dry.md | 121 | "If you find yourself passing parameters and adding conditional paths through shared code, the abstraction is incorrect." | reuse-components | conditional |
| dry.md | 123 | "Delete it. Start over." | deletion | conditional |
| dry.md | 133 | "Two instances don't give you enough information. You'll build the wrong abstraction. Three instances reveal the pattern." | reuse-components | conditional |
| dry.md | 135 | "Premature abstraction is the enemy of good design." | reuse-components | against |
| dry.md | 143 | ""Shared libraries" become bottlenecks where no team can change anything without coordinating with everyone." | dependencies | against |
| dry.md | 149 | "AI creates massive code cloning—duplicating knowledge across repositories with no thought for consolidation." | reuse-components | against |
| dry.md | 151 | "Studies confirm: code duplication leads to higher defect rates." | cost-debt | against |
| dry.md | 153 | "AI doesn't factor in long-term costs. It just keeps generating." | volume | against |
| dry.md | 167 | "Abstract actual knowledge duplication, not incidental similarities. Wait until duplication is painful. Create stable abstractions that don't require constant modification." | reuse-components | conditional |
| dry.md | 173 | "Syntax duplication representing different business concepts? Don't abstract." | reuse-components | conditional |
| dry.md | 177 | "Inline the code. Delete unused bits. Start fresh. Keeping broken abstractions wastes far more than deleting them." | deletion | conditional |
| dry.md | 181 | "Context-specific logic serving different business domains? Duplicate it." | reuse-components | conditional |
| dry.md | 183 | "Code crossing microservice boundaries? Duplicate it. Sharing creates coupling that defeats service boundaries." | reuse-components | conditional |
| dry.md | 185 | "Research or experimental code with limited lifespan? Duplicate it." | reuse-components | conditional |
| dry.md | 187 | "One-time migration scripts? Duplicate it. You'll never maintain them." | maintenance-economics | conditional |
| dry.md | 189 | "Write Everything Twice (WET): you can duplicate twice, but never three times." | reuse-components | conditional |
| dry.md | 191 | "Don't fear duplication until then." | reuse-components | conditional |
| dry.md | 195 | "Programming is fundamentally about managing knowledge, not writing code." | cost-debt | against |
| dry.md | 199 | "As AI generates code without considering maintainability, DRY principles become critical to combat technical debt explosion." | cost-debt | against |
| dry.md | 222 | "Delete wrong abstractions." | deletion | conditional |
| intervention.md | 15 | "You will want to trust what the system says about itself." | trust-ownership | against |
| intervention.md | 31 | "Nothing inside a corrupted system is a reliable source about that system." | trust-ownership | against |
| intervention.md | 35 | "The test suite passes but tests nothing." | trust-ownership | against |
| kiss.md | 22 | "Frameworks with 68 interfaces for 26,759 lines." | volume | against |
| kiss.md | 22 | "AI slop that clones code without comprehension." | trust-ownership | against |
| kiss.md | 28 | "AI sloppiness: Generated code without comprehension, additions without understanding" | trust-ownership | against |
| kiss.md | 38 | "Components that are separate." | reuse-components | for |
| kiss.md | 42 | "When you create dependencies that spread like vines through your codebase." | dependencies | against |
| kiss.md | 52 | "You reach for the complicated framework you know." | dependencies | against |
| kiss.md | 65 | "Code churn projected to double versus 2021" | volume | against |
| kiss.md | 66 | "Code cloning grew 4x in one year" | volume | against |
| kiss.md | 67 | "Copy-paste now exceeds moved code for the first time in history" | reuse-components | against |
| kiss.md | 70 | "30.5% incorrect" | trust-ownership | against |
| kiss.md | 72 | "4x increase in duplication" | volume | against |
| kiss.md | 73 | "Written 55% faster, with quality decline that eats the savings" | maintenance-economics | against |
| kiss.md | 109 | "Your elaborate abstractions for flexibility you don't have? They will fail." | reuse-components | against |
| kiss.md | 131 | "When I see a top-down description of a system with infinite libraries described by layers and layers, all I see is a morass." | dependencies | against |
| kiss.md | 133 | "if you can't understand it, you can't maintain it, debug it, or evolve it." | maintenance-economics | conditional |
| kiss.md | 153 | "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away." | deletion | for |
| kiss.md | 157 | "Remove dead code immediately. Delete speculative "future" code. Delete "just in case" functions." | deletion | for |
| kiss.md | 159 | "Every line you don't write is a line you don't maintain, test, debug, or understand." | volume | for |
| kiss.md | 161 | "Less code = fewer bugs." | volume | for |
| kiss.md | 163 | "The best code is no code." | volume | for |
| kiss.md | 167 | "Keep methods under 20 lines." | volume | for |
| kiss.md | 187 | "If you can't answer, delete the layer." | deletion | conditional |
| kiss.md | 193 | "Don't create interfaces until you need to swap implementations." | reuse-components | conditional |
| kiss.md | 195 | "Having 68 interfaces for 26,000 lines of code is not good practice." | volume | against |
| kiss.md | 199 | "You have 3+ concrete implementations" | reuse-components | conditional |
| kiss.md | 200 | "Variation exists in production" | reuse-components | conditional |
| kiss.md | 201 | "Cost of change is real and measured" | reuse-components | conditional |
| kiss.md | 203 | "YAGNI applies to abstractions too." | reuse-components | conditional |
| kiss.md | 226 | "This prevents building infrastructure you'll never use." | volume | against |
| kiss.md | 232 | "It writes code that needs revision within 2 weeks." | maintenance-economics | against |
| kiss.md | 234 | "Use AI for suggestions. Never for blind generation." | trust-ownership | conditional |
| kiss.md | 238 | "Every line of code you add is a line you must understand. If you don't understand it, don't merge it." | trust-ownership | conditional |
| kiss.md | 257 | "Don't under-engineer by removing necessary functionality." | deletion | conditional |
| kiss.md | 273 | "Delete before adding" | deletion | for |
| kiss.md | 277 | "The investment pays off every day afterward in maintenance, debugging, and feature additions." | maintenance-economics | for |
| kiss.md | 294 | "Let abstraction multiply \| Abstract when necessary" | reuse-components | conditional |
| kiss.md | 299 | "Complexity is debt. It robs you of capital to invest in the future." | cost-debt | against |
| kiss.md | 311 | "Delete what adds no value." | deletion | for |
| postgres.md | 15 | "your precious application code that'll be rewritten in two years and forgotten in three." | cost-debt | against |
| postgres.md | 19 | "Your application is a disposable skin." | cost-debt | against |
| postgres.md | 19 | "The schema outlives every line of code you will ever write" | cost-debt | against |
| postgres.md | 21 | "You handed your most permanent artifact to a code generator." | trust-ownership | against |
| postgres.md | 25 | "The ORM didn't solve the impedance mismatch. It WALLPAPERED OVER IT." | dependencies | against |
| postgres.md | 27 | "decades of optimizer research, a type system richer than your programming language — and you use 5% of it." | dependencies | against |
| postgres.md | 27 | "You added Elasticsearch because Stack Overflow told you to. You didn't check." | dependencies | against |
| postgres.md | 49 | "Data outlives code." | cost-debt | against |
| postgres.md | 53 | "Keep calling the wreckage "tech debt" like it's something that happened TO you." | cost-debt | against |
| postgres.md | 95 | "You copy-paste SQL you don't understand. Everyone can tell." | trust-ownership | against |
| postgres.md | 213 | "Six systems. Six backup strategies. Six monitoring dashboards nobody checks. Six failure modes you haven't tested." | dependencies | against |
| postgres.md | 215 | "You added an entire system — with its own cluster and its own monitoring and its own failure modes" | dependencies | against |
| postgres.md | 219 | "Elasticsearch \| tsvector, tsquery, ts_rank with GIN indexes." | dependencies | for |
| postgres.md | 220 | "Elasticsearch (fuzzy) \| pg_trgm. Trigram similarity." | dependencies | for |
| postgres.md | 221 | "RabbitMQ / Redis queue \| SELECT ... FOR UPDATE SKIP LOCKED" | dependencies | for |
| postgres.md | 222 | "External pub/sub \| LISTEN / NOTIFY" | dependencies | for |
| postgres.md | 223 | "Redis (caching) \| Materialized views. Precomputed. Refreshable. Indexable." | dependencies | for |
| postgres.md | 224 | "MongoDB \| JSONB with GIN and containment operators" | dependencies | for |
| postgres.md | 225 | "External lock service \| pg_advisory_lock" | dependencies | for |
| postgres.md | 226 | "External scheduler \| pg_cron (third-party, widely available) \| Not stock. But one install vs an entire scheduling system." | dependencies | conditional |
| postgres.md | 228 | "Check Postgres FIRST. Before you add another animal to the zoo." | dependencies | for |
| postgres.md | 228 | "Every system you add is a permanent line item" | maintenance-economics | against |
| postgres.md | 230 | "What ships in the box. What you already own. What you refuse to learn." | dependencies | for |
| postgres.md | 234 | "Now you have invalidation bugs AND consistency problems AND another system to monitor." | dependencies | against |
| postgres.md | 236 | "So you layered a broken cache over a working cache" | dependencies | against |
| postgres.md | 261 | "No extensions to beg for. No bleeding edge." | dependencies | for |
| postgres.md | 263 | "Monday you'll generate a schema from ORM models without reviewing it." | trust-ownership | against |
| self-documenting-code.md | 184 | ""Utils" and "Helpers" are where self-documentation goes to die:" | reuse-components | against |
| self-documenting-code.md | 288 | "Delete your comments. Rewrite your code." | deletion | for |
| self-documenting-code.md | 290 | "Every line of code you write is teaching someone about your domain." | cost-debt | for |
| simple-made-easy.md | 19 | "Every entanglement you introduce is a burden you will carry forever." | cost-debt | against |
| simple-made-easy.md | 45 | "Inheritance is easy to describe. It is also definitionally complex" | reuse-components | against |
| simple-made-easy.md | 55 | "You will pay for complexity." | cost-debt | against |
| simple-made-easy.md | 57 | "Every hidden dependency is a trap waiting for the next maintainer." | dependencies | against |
| simple-made-easy.md | 71 | "Composition requires that the things being composed are simple — otherwise you are just complecting at a higher level." | reuse-components | conditional |
| simple-made-easy.md | 81 | "We optimize for constructs. We should optimize for artifacts." | maintenance-economics | for |
| simple-made-easy.md | 98 | "ORM \| Declarative Data Manipulation" | dependencies | against |
| simple-made-easy.md | 122 | "You create thousands of variations where a handful of structures would suffice." | volume | against |
| simple-made-easy.md | 124 | "Stop writing classes for every new piece of information." | volume | against |
| simple-made-easy.md | 132 | "Make them small — far smaller than you think." | volume | for |
| simple-made-easy.md | 134 | "Build from subcomponents. Inject dependencies. You should have more subcomponents than you do." | reuse-components | for |
| simple-made-easy.md | 148 | "The components must be simple first — only then does separation help." | reuse-components | conditional |
| simple-made-easy.md | 150 | "Look for the hidden dependencies." | dependencies | for |
| simple-made-easy.md | 158 | "Before you write anything, choose tools that produce simpler artifacts." | dependencies | conditional |
| simple-made-easy.md | 171 | "The alternative is to start fast and slow down forever. Complexity accumulates. Each sprint accomplishes less." | maintenance-economics | against |
| simple-made-easy.md | 173 | "Spend time up front. Think before you type. The investment pays compound interest." | maintenance-economics | for |
| simple-made-easy.md | 183 | "When you simplify, you often end up with more things. This is correct." | volume | for |
| simple-made-easy.md | 185 | "More pieces, hanging cleanly, are simpler than fewer pieces tangled together." | volume | for |
| simple-made-easy.md | 187 | "The pieces that are separate can be changed independently. That is the payoff." | reuse-components | for |
| yagni.md | 15 | "You design elaborate frameworks for flexibility you'll never use." | volume | against |
| yagni.md | 19 | "Every feature you build for tomorrow has a two-thirds chance of being useless and a 100% certainty of making your code harder to change." | cost-debt | against |
| yagni.md | 25 | "writing code for features you don't need yet, building infrastructure for problems you haven't encountered" | volume | against |
| yagni.md | 44 | "Presumptive features don't just waste time. They create cascading costs that multiply." | cost-debt | against |
| yagni.md | 46 | "Every hour spent building unused features is an hour not spent on features people actually want." | cost-debt | against |
| yagni.md | 50 | "Every unused feature adds complexity. Classes to navigate. Methods to understand. Abstractions to learn." | cost-debt | against |
| yagni.md | 52 | "You pay twice: once to build it wrong, once to remove it and build it right." | cost-debt | against |
| yagni.md | 56 | "This isn't engineering. This is technical bankruptcy." | cost-debt | against |
| yagni.md | 60 | "Build only what you need right now." | volume | for |
| yagni.md | 66 | "Abstract factories and interfaces for every class "for flexibility" \| Concrete classes. Refactor to interfaces when second implementation arrives." | reuse-components | conditional |
| yagni.md | 70 | "Build exactly what you need. Build it well. Stop there." | volume | for |
| yagni.md | 76 | "Simple abstractions added only when needed." | reuse-components | conditional |
| yagni.md | 78 | "Presumptive features are technical debt—maintenance costs on complexity that provides zero value." | cost-debt | against |
| yagni.md | 85 | "Tripled codebase. Zero benefit. Brutal onboarding." | volume | against |
| yagni.md | 95 | "One-third of IT budgets spent on licenses for bloated software nobody fully understands." | dependencies | against |
| yagni.md | 99 | "AI generates features you didn't specify because it learned from code containing the presumptive features you're trying to avoid." | volume | against |
| yagni.md | 103 | "accumulated presumptive features that provide zero value but create infinite maintenance burden" | maintenance-economics | against |
| yagni.md | 109 | "Don't add fields until you use them. Don't add methods until you need them. Don't add abstractions for "flexibility."" | volume | conditional |
| yagni.md | 111 | "Imagine the refactoring before building. Often adding later is cheaper—you'll have more information." | maintenance-economics | conditional |
| yagni.md | 117 | "Databases, languages, platforms must be chosen upfront." | dependencies | for |
| yagni.md | 137 | "First you learn the value of abstraction, then you learn the cost of abstraction, then you're ready to engineer." | reuse-components | conditional |
| yagni.md | 147 | "Accumulate complexity and technical debt." | cost-debt | against |
| yagni.md | 147 | "Maintain code nobody understands for features nobody uses." | maintenance-economics | against |
| yagni.md | 155 | "You aren't gonna need it. Even if you eventually do need it, you don't need it now." | volume | conditional |
| archive:DRY.md | 4 | "Knowledge duplication is technical debt, and you're accumulating it faster than ever" | cost-debt | against |
| archive:DRY.md | 36 | "Blindly removing all duplication that triggers static analysis warnings leaves code in worse shape." | reuse-components | conditional |
| archive:DRY.md | 42 | "I inherited a codebase that made very heavy use of code duplication and one time I had to fix a bug in eight different places!" | maintenance-economics | against |
| archive:DRY.md | 52 | "Any bugs or vulnerabilities within code are replicated when blocks are copy-pasted." | reuse-components | against |
| archive:DRY.md | 54 | "Code base bloats. More lines mean more surface area for bugs, more to understand when onboarding" | volume | against |
| archive:DRY.md | 60 | "Duplication is far cheaper than the wrong abstraction" | reuse-components | conditional |
| archive:DRY.md | 78 | "we could not make updates to the shared code without potentially breaking 60-70 other libraries." | dependencies | against |
| archive:DRY.md | 84 | ""Shared libraries" become bottlenecks where no team can change anything without coordinating with everyone." | dependencies | against |
| archive:DRY.md | 88 | "AI tools are creating a technical debt nightmare." | cost-debt | against |
| archive:DRY.md | 90 | "higher cloud storage expenses, longer testing cycles, more resources debugging, technical debt accumulation" | cost-debt | against |
| archive:DRY.md | 90 | "measuring developer productivity by commits or lines written in the AI era will accelerate technical debt catastrophically" | volume | against |
| archive:DRY.md | 90 | "AI doesn't factor in long-term costs—it just keeps generating more code." | volume | against |
| archive:DRY.md | 129 | "Delete the bits that aren't needed for this particular caller" | deletion | conditional |
| archive:DRY.md | 132 | "keeping broken abstractions wastes far more effort than deleting them." | deletion | conditional |
| archive:DRY.md | 140 | "You'll never maintain them, so duplication doesn't create maintenance burden." | maintenance-economics | conditional |
| archive:DRY.md | 148 | "Every line of code that goes into an application must be maintained, and is a potential source of future bugs." | cost-debt | against |
| archive:DRY.md | 148 | "Duplication needlessly bloats the codebase, resulting in more opportunities for bugs and adding accidental complexity to the system." | volume | against |
| archive:KISS.md | 9 | "We've built 68 interfaces for 26,759 lines of code—one interface per 393 lines" | volume | against |
| archive:KISS.md | 19 | "NASA lists "excessive features" as a top 10 risk factor for project failure." | volume | against |
| archive:KISS.md | 25 | "Complexity kills. It sucks the life out of developers; it makes products difficult to plan, build, and test" | maintenance-economics | against |
| archive:KISS.md | 29 | "Stanford research found programmers using AI assistants "wrote significantly less secure code."" | trust-ownership | against |
| archive:KISS.md | 29 | "A 2023 Bilkent University study found 30.5% of AI-generated code was incorrect, 23.2% partially incorrect." | trust-ownership | against |
| archive:KISS.md | 29 | "there's a significant decline in quality and maintainability that eats up those savings in maintenance and debugging." | maintenance-economics | against |
| archive:KISS.md | 31 | "AI generates additions but never updates, deletions, or moves." | deletion | against |
| archive:KISS.md | 31 | "It lacks context about your library versions, environment, or API." | dependencies | against |
| archive:KISS.md | 31 | "It generates short-term code requiring revision within 2 weeks" | maintenance-economics | against |
| archive:KISS.md | 31 | "the support costs associated with complex code have increased in recent years in large part due to the proliferation of AI-generated code use" | maintenance-economics | against |
| archive:KISS.md | 39 | "Small, composable tools that work together." | reuse-components | for |
| archive:KISS.md | 63 | "Delete code aggressively." | deletion | for |
| archive:KISS.md | 63 | "Less code means fewer bugs and easier maintenance." | volume | for |
| archive:KISS.md | 65 | "Keep methods under 20 lines." | volume | for |
| archive:KISS.md | 79 | "But each component should still be as simple as possible." | reuse-components | conditional |
| archive:KISS.md | 83 | "Don't under-engineer by removing necessary functionality." | deletion | conditional |
| archive:KISS.md | 89 | "Complexity is debt, it robs you of capital to invest in the future." | cost-debt | against |
| archive:KISS.md | 91 | "AI tools generate code faster than we can understand it." | trust-ownership | against |
| archive:SELF_DOCUMENTING_CODE.md | 5 | "Self-documenting code is not about writing less." | volume | against |
| archive:SELF_DOCUMENTING_CODE.md | 263 | ""Utils" and "Helpers" are where self-documentation goes to die:" | reuse-components | against |
| archive:SELF_DOCUMENTING_CODE.md | 459 | "Every line of code you write is teaching someone about your domain." | cost-debt | for |

## Held ground

One line per manifesto with three or more rows. Quoted fragments carry their line.

- **correct-by-construction.md** (6 rows): Prices strictness against production cost: "Pay at compile time or pay forever in production." (231) "Compile-time strictness is cheaper than runtime debugging." (273) "Silent failure is not ease. It is debt with compound interest." (25); maintenance reads "Refactor with confidence" (224) against "Refactor with fear" (224); abstraction costs nothing at runtime: "The abstraction is free." (136)
- **dry.md** (35 rows): Holds reuse and duplication: "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system." (27); duplication costs ("Development effort multiplies" (92), "Codebase bloats" (95)); "The wrong abstraction is worse than duplication." (103); duplicate until the third instance (133), across service boundaries (183), in throwaway code (185, 187); "Delete wrong abstractions." (222); `"Shared libraries" become bottlenecks where no team can change anything without coordinating with everyone.` (143); AI cloning (149, 153)
- **intervention.md** (3 rows): Holds trust in an inherited system's self-report, not code: "You will want to trust what the system says about itself." (15) "Nothing inside a corrupted system is a reliable source about that system." (31) "The test suite passes but tests nothing." (35)
- **kiss.md** (38 rows): Holds less code and deletion: "Less code = fewer bugs." (161) "The best code is no code." (163) "Delete before adding" (273); dead and speculative code goes (157); "Keep methods under 20 lines." (167); "Complexity is debt. It robs you of capital to invest in the future." (299); dependencies ("When you create dependencies that spread like vines through your codebase." (42)) and libraries (131); abstract on need only (193, 199-203, 294); generated code: "Use AI for suggestions. Never for blind generation." (234) "If you don't understand it, don't merge it." (238); "Don't under-engineer by removing necessary functionality." (257)
- **postgres.md** (27 rows): Holds use-what-ships over added systems: "Check Postgres FIRST. Before you add another animal to the zoo." (228) "Every system you add is a permanent line item" (228); "What ships in the box. What you already own." (230); eight rows pair an external system with a built-in feature (219-226); generated and pasted code: "You handed your most permanent artifact to a code generator." (21) "You copy-paste SQL you don't understand." (95); application code as short-lived: "Your application is a disposable skin." (19) "Data outlives code." (49)
- **self-documenting-code.md** (3 rows): Holds: `"Utils" and "Helpers" are where self-documentation goes to die:` (184) "Delete your comments. Rewrite your code." (288) "Every line of code you write is teaching someone about your domain." (290)
- **simple-made-easy.md** (19 rows): Holds complexity as cost and more parts as correct: "Every entanglement you introduce is a burden you will carry forever." (19) "You will pay for complexity." (55) "Every hidden dependency is a trap waiting for the next maintainer." (57); "When you simplify, you often end up with more things. This is correct." (183); "Stop writing classes for every new piece of information." (124); "Build from subcomponents. Inject dependencies." (134); "The components must be simple first" (148); "start fast and slow down forever" (171); ORM sits on the complex side (98)
- **yagni.md** (24 rows): Holds build-only-now and the cost of presumptive code: "Build only what you need right now." (60); four costs (build 46, delay 48, carry 50, repair 52); "Presumptive features are technical debt" (78); "This is technical bankruptcy." (56); "Don't add fields until you use them." (109); "Tripled codebase." (85); "licenses for bloated software" (95); AI adds unspecified features (99); "then you learn the cost of abstraction" (137)

Archive sources with three or more rows (pre-collection; same format):

- **archive:DRY.md** (17 rows): "Knowledge duplication is technical debt" (4); "Every line of code that goes into an application must be maintained, and is a potential source of future bugs." (148); "Duplication is far cheaper than the wrong abstraction" (60); "Code base bloats." (54); "measuring developer productivity by commits or lines written in the AI era will accelerate technical debt catastrophically" (90); "keeping broken abstractions wastes far more effort than deleting them." (132); "I inherited a codebase that made very heavy use of code duplication" (42)
- **archive:KISS.md** (18 rows): "AI generates additions but never updates, deletions, or moves." (31) "It lacks context about your library versions, environment, or API." (31); "NASA lists "excessive features" as a top 10 risk factor for project failure." (19); "one interface per 393 lines" (9); "Small, composable tools that work together." (39); "Complexity is debt, it robs you of capital to invest in the future." (89); "AI tools generate code faster than we can understand it." (91); "Stanford research found programmers using AI assistants "wrote significantly less secure code."" (29)
- **archive:SELF_DOCUMENTING_CODE.md** (3 rows): "Self-documenting code is not about writing less." (5); `"Utils" and "Helpers" are where self-documentation goes to die:` (263); "Every line of code you write is teaching someone about your domain." (459)

## Enemies

| file | enemy (quote) | file:line |
|---|---|---|
| cargo-cult-science.md | "So I call these things Cargo Cult Science, because they follow all the apparent precepts and forms of scientific investigation" — *no enemy section; named at line 37* | cargo-cult-science.md:37 |
| correct-by-construction.md | "The industry worships quick starts." — *section `## The Enemy` at line 17* | correct-by-construction.md:19 |
| dry.md | "Knowledge duplication is destroying your codebase." — *section `## The Enemy is Clear` at line 11* | dry.md:13 |
| first-principles.md | "Your enemy is Reasoning by Analogy." — *section `## The Enemy` at line 30* | first-principles.md:32 |
| intervention.md | "Three temptations will destroy your intervention." — *section `## The Enemy` at line 11* | intervention.md:15 |
| kiss.md | "Complexity is killing your software."; "Over-engineering: Smart developers being too clever, building for futures that never arrive"; "AI sloppiness: Generated code without comprehension, additions without understanding" — *section `## Name Your Enemy` at line 16* | kiss.md:18, kiss.md:27, kiss.md:28 |
| postgres.md | "I write an application that uses a database."; "The database is subordinate." — *no enemy section; first section, lines 11-33* | postgres.md:11, postgres.md:15 |
| self-documenting-code.md | "Every comment in your codebase is an admission of defeat." — *section `## The Enemy` at line 11* | self-documenting-code.md:13 |
| simple-made-easy.md | "We confuse easy with simple, and this confusion is killing our software." — *no enemy section; first section `## The Problem`, line 15* | simple-made-easy.md:17 |
| stop-yapping.md | "Here's what your yapping actually does: it makes your answer WRONG."; "Every word past the answer is you choosing performance over function." — *no enemy section; first section, lines 11-23* | stop-yapping.md:17, stop-yapping.md:19 |
| yagni.md | "The enemy is presumptive development: writing code for features you don't need yet"; "The enemy is your arrogance about the future" — *section `## The Enemy` at line 23* | yagni.md:25, yagni.md:38 |
| zen-of-python.md | "Beautiful is better than ugly." — *no enemy section and no prose; first line quoted* | zen-of-python.md:9 |

## Titles and taglines

Frontmatter: title at line 2, tagline at line 3 in all 12 files.

| file | title | tagline |
|---|---|---|
| cargo-cult-science.md | Cargo Cult Science | the first principle is that you must not fool yourself |
| correct-by-construction.md | Correct By Construction | invalid states cannot compile |
| dry.md | Knowledge Has One Home | knowledge has one home |
| first-principles.md | The First Principles | atoms, not analogies |
| intervention.md | Trust Nothing, Restore Everything | roots, not canopy |
| kiss.md | Decomplect | incidental is Latin for your fault |
| postgres.md | Respect the Engine | you use 5% of what you bought. |
| self-documenting-code.md | Code Speaks | comments are lies |
| simple-made-easy.md | The Simplicity Manifesto | the confusion is killing you |
| stop-yapping.md | Stop Yapping | answer. shut up. |
| yagni.md | Build For Today | build for today |
| zen-of-python.md | The Zen of Python | refuse to guess |

## Counts

Rows per topic:

| topic | manifestos (12 files) | archive (4 files) | total |
|---|---|---|---|
| volume | 25 | 9 | 34 |
| cost-debt | 21 | 6 | 27 |
| deletion | 10 | 5 | 15 |
| dependencies | 29 | 3 | 32 |
| reuse-components | 37 | 6 | 43 |
| trust-ownership | 12 | 3 | 15 |
| maintenance-economics | 21 | 6 | 27 |
| **total** | **155** | **38** | **193** |

Rows per file (topic columns: vol, cost, del, dep, reuse, trust, maint):

| file | rows | vol | cost | del | dep | reuse | trust | maint |
|---|---|---|---|---|---|---|---|---|
| cargo-cult-science.md | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| correct-by-construction.md | 6 | 0 | 1 | 0 | 0 | 1 | 0 | 4 |
| dry.md | 35 | 2 | 3 | 3 | 2 | 18 | 1 | 6 |
| first-principles.md | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| intervention.md | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| kiss.md | 38 | 10 | 1 | 6 | 3 | 9 | 5 | 4 |
| postgres.md | 27 | 0 | 5 | 0 | 18 | 0 | 3 | 1 |
| self-documenting-code.md | 3 | 0 | 1 | 1 | 0 | 1 | 0 | 0 |
| simple-made-easy.md | 19 | 5 | 2 | 0 | 4 | 5 | 0 | 3 |
| stop-yapping.md | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| yagni.md | 24 | 8 | 8 | 0 | 2 | 3 | 0 | 3 |
| zen-of-python.md | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| archive:DRY.md | 17 | 4 | 4 | 2 | 2 | 3 | 0 | 2 |
| archive:KISS.md | 18 | 4 | 1 | 3 | 1 | 2 | 3 | 4 |
| archive:SELF_DOCUMENTING_CODE.md | 3 | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| archive:zen-of-python.md | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
