# CORRECT BY CONSTRUCTION

## The Rust Correctness Manifesto

*After Tris Oaten's No Boilerplate series*

---

## The Enemy

The industry worships quick starts.

Install in five seconds. Hello world in three lines. Deploy by Friday. Move fast and break things.

This is a lie sold to you by languages that defer all consequences to 3am. Languages where nothing bad *seems* to happen—until production burns and you're reading CloudWatch logs in the dark, hunting a null that propagated silently for eighteen months.

Silent failure is not ease. It is debt with compound interest.

Every dynamic language whispers: *trust yourself, you're smart enough*.

You are not. Neither am I. Neither is anyone. The human brain cannot hold a distributed system in working memory. It cannot trace every possible state through concurrent code. It cannot remember which functions throw and which return errors.

We need help.

---

## The Compiler Works For You

The Rust compiler is not your adversary. It is the most rigorous pair programmer you will ever have. It works 24 hours a day. It never gets tired. It never misses edge cases. It never says "that's probably fine."

When the compiler rejects your code, it is doing work you would otherwise do in production, at 3am, with incomplete logs and angry customers.

**Every compiler error is a bug you did not ship.**

This is not a cost. This is a gift.

---

## The Core Principles

### 1. Make Invalid States Unrepresentable

Bad:
```rust
struct Order {
    shipped: bool,
    delivered: bool,
    cancelled: bool,
}
```
What if `shipped && cancelled`? The type permits it. Your code must check. Your code will forget.

Good:
```rust
enum OrderStatus {
    Pending,
    Shipped { tracking: String },
    Delivered { date: DateTime },
    Cancelled { reason: String },
}
```
The invalid combination cannot exist. Not "should not." *Cannot.*

Design your types so wrong programs do not compile.

---

### 2. Explicit Over Implicit

Rust has no exceptions. Functions that can fail return `Result`. The caller must handle both cases. Control flow is visible in the code.

```rust
let data = fetch_data()?;  // ? propagates errors explicitly
```

No hidden throws. No surprise unwinding. No "maybe this crashes somewhere deep in the stack."

Exceptions are hidden control flow. Results are honest contracts.

---

### 3. Ownership Is Proof

Every value has exactly one owner. When the owner dies, the value dies. This is not a convention. This is enforced.

```rust
let s1 = String::from("hello");
let s2 = s1;  // s1 is gone. Moved. Invalid.
// println!("{}", s1);  // Compiler error: use of moved value
```

Use-after-free is impossible by construction. Double-free is impossible by construction. The entire category of memory bugs—70% of serious security vulnerabilities in major software—*erased*.

Not detected. Not caught. *Erased.*

---

### 4. Concurrency Without Fear

Sharing mutable state between threads requires explicit synchronization. The type system enforces this.

```rust
// This compiles:
let data = Arc::new(Mutex::new(vec![]));

// This does not:
let data = vec![];
thread::spawn(|| data.push(1));  // Error: cannot move out of captured variable
```

Data races are not detected at runtime. They do not compile.

"Fearless concurrency" is not marketing. It is a type-system guarantee.

---

### 5. Zero-Cost Abstractions

High-level code compiles to optimal machine code. Iterators, closures, pattern matching—no runtime overhead.

```rust
let sum: i32 = (1..=1000)
    .filter(|x| x % 2 == 0)
    .map(|x| x * x)
    .sum();
```

This compiles to the same assembly as a hand-written loop. The abstraction is free.

You do not choose between readable and fast. You get both.

---

## The Workflow

### Compiler-Driven Development

1. **Model your domain in types.** Structs for data. Enums for states. Make invalid states unrepresentable.

2. **Write the function signature.** Decide what goes in and what comes out. The types are the contract.

3. **Let the compiler guide you.** Write code. Get errors. The errors tell you exactly what is wrong and often how to fix it.

4. **Iterate until it compiles.** When it compiles, significant categories of bugs are already impossible.

5. **Add tests for logic.** The compiler handles types, memory, concurrency. Tests handle business rules.

| TDD Cycle | CDD Cycle |
|-----------|-----------|
| Red: write failing test | Red: write code that doesn't compile |
| Green: make it pass | Green: make it compile |
| Refactor: improve code | Refactor: improve the model |
| "Tests passing? Improve tests" | "Compiles? Improve the model" |

The compiler is your first test suite. It runs on every keystroke.

---

### The Typestate Pattern

Encode state machines in the type system.

```rust
struct Light<State> { state: State }
struct On;
struct Off;

impl Light<Off> {
    fn turn_on(self) -> Light<On> { Light { state: On } }
}

impl Light<On> {
    fn turn_off(self) -> Light<Off> { Light { state: Off } }
}
```

Invalid transitions do not exist:
```rust
Light::new().turn_on().turn_on();  // Error: no method `turn_on` on Light<On>
```

The compiler enforces your state machine. Not tests. Not documentation. *The compiler.*

---

### Macros: Compile-Time Execution

Rust macros run at compile time and generate code.

```rust
let account = sqlx::query!("SELECT name, id FROM users WHERE id = $1", user_id)
    .fetch_one(&pool)
    .await?;
```

The `query!` macro:
- Connects to your database at compile time
- Validates SQL syntax
- Checks column names against your schema
- Generates type-safe Rust code

SQL errors become compiler errors. Wrong column names become compiler errors. Type mismatches become compiler errors.

**All before your code runs once.**

---

## The Economics

| Activity | Rust | Dynamic Languages |
|----------|------|-------------------|
| Writing | Slower initially | Faster initially |
| Reading | Types are documentation | Guess and grep |
| Testing | Compiler proves categories | Test everything manually |
| Debugging | Rare—bugs are shallow | Common—bugs hide deep |
| Maintenance | Refactor with confidence | Refactor with fear |
| Runtime | 80x faster than Python | Acceptable until it isn't |

The "slow" language is slow in the moment you feel most impatient: writing new code.

The "fast" language is slow in the moments that cost the most: 3am debugging, six-month-old code, the production incident that erases a week of feature work.

**Pay at compile time or pay forever in production.**

---

## What You Give Up

- Quick hello-worlds
- Instant gratification
- The illusion that your first draft works
- Runtime flexibility you probably shouldn't have

## What You Gain

- Memory safety without garbage collection
- Thread safety without runtime overhead
- Refactoring without regression
- Sleep

---

## The Choice

You can keep writing code that *seems* to work. Code where nothing bad happens until it does. Code that passes tests and crashes in production. Code that makes you scared of your own repository.

Or.

You can write code where the compiler does the work. Where invalid states cannot be represented. Where memory bugs are erased by construction. Where concurrency is fearless because the type system has your back.

The compiler is not the enemy.

The compiler is the ally you did not know you had.

**Make it work for you.**

---

## The Principles, Compressed

1. **Make invalid states unrepresentable.** If the type permits it, someone will do it.

2. **Explicit over implicit.** Results over exceptions. Ownership over garbage collection. Visible control flow over hidden magic.

3. **Pay upfront.** Compile-time strictness is cheaper than runtime debugging.

4. **Trust the type system.** If it compiles, whole categories of bugs are gone.

5. **Compiler-driven development.** Model in types. Let errors guide you. Compile means confidence.

6. **Zero-cost abstractions.** Readable and fast are not tradeoffs.

7. **Done is the engine of more.** When the compiler accepts your code, ship it. The strictness has already done its work.

---

## The Final Word

> *Rust is as pure as possible, but no purerer.*

Correctness is not achieved by testing harder. Correctness is achieved by constructing code where incorrectness cannot compile.

This is not a burden.

This is a superpower.

---

*Encode your invariants. Trust the compiler. Ship with confidence.*
