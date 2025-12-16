# The Complete No Boilerplate Rust Guide

A comprehensive guide to Rust programming, compiled from the No Boilerplate video series by Tris Oaten. This document progresses from foundational concepts through advanced techniques, covering the language, its philosophy, and practical application.

---

# Part I: Foundation & Motivation

## Chapter 1: Rust Makes You Feel Like a Genius

Rust has a mass appeal problem. The mass appeal of Java, JavaScript, and Python is that if you write code wrong, nothing bad seems to happen. You run it, press F12 in the browser, or check the cloudwatch logs. No errors. No warnings. The code is fine.

Except it wasn't. Not then. Maybe not for years. Silent failures cascade through your system. Type coercion buries mistakes. Nulls propagate invisibly. The worst case: no errors at all. Your code fails silently.

Rust fixes this at compile time. The compiler catches entire categories of bugs before code executes:

- Null pointer dereferences
- Memory safety violations
- Data races in concurrent code
- Type mismatches
- Resource leaks

The borrow checker guarantees memory safety without garbage collection. Lifetimes prove data validity at compile time. The type system encodes business logic that other languages leave to runtime checks.

When Rust code compiles, you know something. Not everything—but far more than in languages that defer all checks to runtime. The compiler is strict because it respects your time. Finding bugs at 3am in production costs more than finding them at compile time.

This isn't about suffering through complexity. It's about leverage. The compiler does work so you don't have to. Every error message is a bug you didn't ship.

---

## Chapter 2: Your Code Can Be Perfect

The memory safety problem isn't theoretical. It's the root cause of 70% of serious security vulnerabilities in major software projects. Microsoft, Google, and Apple have published the data.

C and C++ provide no memory safety guarantees. JavaScript and Python avoid the problem through garbage collection—trading determinism and performance for safety. Rust achieves safety without that tradeoff.

### The Problem Space

Memory bugs cause:
- Buffer overflows enabling arbitrary code execution
- Use-after-free vulnerabilities
- Double-free crashes
- Data races corrupting shared state
- Resource leaks degrading performance

Traditional solutions:
- Manual memory management (C): maximum control, maximum risk
- Garbage collection (Java, Python, Go): safety at runtime cost
- Reference counting (Swift, Python): deterministic but slower

Rust's solution: ownership and borrowing, enforced at compile time with zero runtime cost.

### Ownership Rules

1. Each value has exactly one owner
2. When the owner goes out of scope, the value is dropped
3. Values can be borrowed (referenced) or moved

These rules eliminate use-after-free by construction. The compiler tracks ownership through the program, rejecting code that would create dangling references.

### Practical Impact

Discord rewrote their Read States service from Go to Rust. Go's garbage collector caused latency spikes every few minutes. Rust's compile-time memory management eliminated those spikes entirely.

Cloudflare uses Rust for their edge computing platform. Memory safety at scale matters when you're handling a significant portion of internet traffic.

The Linux kernel now accepts Rust code for new drivers. After 30 years, the kernel maintainers found a language they trust for system-level work alongside C.

---

## Chapter 3: Rust Is Easy

Rust has a reputation for difficulty. This reputation is backwards. Rust is easy—if you work with the compiler instead of against it.

### The Compiler as Teacher

Rust's compiler errors are documentation:

```
error[E0382]: borrow of moved value: `s`
 --> src/main.rs:5:20
  |
3 |     let s = String::from("hello");
  |         - move occurs because `s` has type `String`
4 |     let s2 = s;
  |              - value moved here
5 |     println!("{}", s);
  |                    ^ value borrowed here after move
  |
help: consider cloning the value
  |
4 |     let s2 = s.clone();
  |               ++++++++
```

The error explains:
- What went wrong (borrow of moved value)
- Where it happened (line 5)
- Why it happened (value moved on line 4)
- How to fix it (clone the value)

Read compiler errors carefully. The information is complete. Read twice, read three times if needed. The compiler knows more about your code than you do.

### Unlearning Bad Habits

Dynamic languages teach you to guess and check. Write code, run it, see what breaks, fix it, repeat. This works for small scripts but fails at scale.

Rust teaches you to think first. Model your data. Express constraints in types. Let the compiler verify your reasoning. This feels slower initially—then dramatically faster as projects grow.

### The Rustlings Path

Start with [Rustlings](https://github.com/rust-lang/rustlings)—small exercises that teach Rust incrementally. Each exercise has a compiler error. Fix the error, learn the concept, move on.

The exercises build understanding through practice:
- Variables and mutability
- Functions and control flow
- Ownership and borrowing
- Structs and enums
- Error handling
- Generics and traits

Complete Rustlings and you'll understand Rust's core model. Everything else is library knowledge.

---

# Part II: Language Basics

## Chapter 4: How to Speak Basic Rust

Rust syntax differs from C-family languages in important ways. Understanding the conventions helps you read code and compiler messages fluently.

### Type Annotations

```rust
let x: i32 = 42;
let name: &str = "Rust";
let numbers: Vec<i32> = vec![1, 2, 3];
```

Types follow the variable name after a colon. The compiler usually infers types, but explicit annotations help readability and catch mistakes.

### Function Signatures

```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

Parameters have explicit types. Return type follows `->`. The last expression without a semicolon is the return value.

### The Special Emoji: `?`

```rust
fn read_file(path: &str) -> Result<String, std::io::Error> {
    let content = std::fs::read_to_string(path)?;
    Ok(content)
}
```

The question mark operator propagates errors. If `read_to_string` fails, the function returns early with that error. No explicit error checking at every step.

### Pattern Matching

```rust
match value {
    0 => println!("zero"),
    1..=9 => println!("single digit"),
    _ => println!("larger"),
}
```

`match` must be exhaustive—every case handled. The compiler enforces this. `_` is the wildcard pattern.

### Structs and Enums

```rust
struct Point {
    x: f64,
    y: f64,
}

enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
}
```

Structs hold data. Enums represent variants. Together they model complex domains.

---

## Chapter 5: Learn Rust in 10 Minutes

A rapid tour of Rust syntax for programmers familiar with other languages.

### Variables

```rust
let x = 5;          // immutable by default
let mut y = 10;     // mutable with `mut`
y += 1;             // modification allowed
```

Immutability by default prevents accidental state changes.

### Types

```rust
let integer: i32 = 42;
let float: f64 = 3.14;
let boolean: bool = true;
let character: char = 'R';
let tuple: (i32, f64) = (1, 2.0);
let array: [i32; 3] = [1, 2, 3];
```

Primitive types are lowercase. Generic types use angle brackets.

### Control Flow

```rust
if condition {
    // branch
} else if other {
    // branch
} else {
    // branch
}

for item in collection {
    // iteration
}

while condition {
    // loop
}

loop {
    // infinite until break
}
```

### Options and Results

```rust
let maybe: Option<i32> = Some(42);
let nothing: Option<i32> = None;

let ok: Result<i32, String> = Ok(42);
let err: Result<i32, String> = Err("failed".to_string());
```

Rust has no null. `Option` represents optional values. `Result` represents operations that can fail.

### Ownership

```rust
let s1 = String::from("hello");
let s2 = s1;  // s1 is moved, no longer valid
// println!("{}", s1);  // error: value borrowed after move
```

Assignment moves ownership for heap-allocated types. Use `.clone()` for explicit copies.

### References

```rust
let s = String::from("hello");
let r1 = &s;      // immutable borrow
let r2 = &s;      // multiple immutable borrows OK
let r3 = &mut s;  // error: cannot borrow as mutable while immutably borrowed
```

References borrow without taking ownership. One mutable reference OR many immutable references—never both.

### Iterators

```rust
let sum: i32 = (1..=10)
    .filter(|x| x % 2 == 0)
    .map(|x| x * x)
    .sum();
```

Iterators are lazy and composable. Zero-cost abstractions compile to efficient loops.

---

# Part III: Philosophy & Context

## Chapter 6: Rust Is Not a Faster Horse

When asked what customers wanted, Henry Ford supposedly said they'd ask for a faster horse. Rust isn't a faster C++. It's a different approach to the same problems.

### The Design Space

Languages occupy a spectrum:
- **High-level** (Python, Ruby): Productivity over performance
- **Low-level** (C, Assembly): Control over safety
- **Middle ground** (Java, Go): Balance with tradeoffs

Rust occupies a new position: high-level ergonomics with low-level control, plus safety guarantees neither extreme provides.

### What Makes Rust Different

**Zero-cost abstractions**: High-level code compiles to optimal machine code. Iterators, closures, and pattern matching have no runtime overhead.

**Fearless concurrency**: The type system prevents data races at compile time. Sharing mutable state between threads requires explicit synchronization.

**No garbage collector**: Memory is freed deterministically when ownership ends. Predictable performance without GC pauses.

**Algebraic data types**: Enums with data enable precise modeling. Invalid states become unrepresentable.

### Positioned for the Future

Rust is designed for problems that don't fully exist yet:
- Correct concurrent code as core counts increase
- Safe systems programming as attack surfaces grow
- Efficient computation as energy costs rise

The language will evolve, but its foundations address fundamental challenges.

---

## Chapter 7: Rust Is Boring

"Boring" is the highest compliment for infrastructure technology. Boring means predictable, reliable, and well-understood. Boring means you can focus on your problem instead of fighting your tools.

### Production-Ready

Rust is mature:
- Stable since 2015
- Three-year backward compatibility guarantee
- Used in production by Amazon, Microsoft, Google, Discord, Cloudflare, Mozilla
- Packages on crates.io exceed 100,000

The "new language" period is over. Rust is established infrastructure.

### Conservative Design

Rust moves slowly and deliberately:
- Features require RFCs with community review
- Breaking changes are extremely rare
- Deprecation is gradual with long runways

This conservatism is intentional. Stability matters more than novelty.

### The Standard Library

The standard library is intentionally small. Core functionality only:
- Collections (Vec, HashMap, String)
- I/O abstractions
- Concurrency primitives
- Error handling types

Everything else lives in the ecosystem. This keeps the core stable while allowing rapid ecosystem evolution.

### Boring is Good

You want boring for:
- Database drivers
- Serialization libraries
- HTTP clients
- Cryptography implementations

Rust's entire value proposition is being boring where it matters—and exciting only in what it enables you to build.

---

# Part IV: Core Language Features

## Chapter 8: Error Handling with Results

Rust has no exceptions. Error handling is explicit through the type system.

### The Result Type

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

Functions that can fail return `Result`. The caller must handle both cases.

### Handling Errors

```rust
let file = File::open("data.txt");

match file {
    Ok(f) => process(f),
    Err(e) => eprintln!("Error: {}", e),
}
```

Or with the question mark operator:

```rust
fn read_data() -> Result<String, std::io::Error> {
    let content = std::fs::read_to_string("data.txt")?;
    Ok(content)
}
```

The `?` operator propagates errors up the call stack. Functions compose cleanly.

### Why No Exceptions?

Exceptions have hidden control flow. Any function might throw, and callers can't know without reading documentation or source code.

Result types make failure explicit:
- Function signatures declare possible errors
- Callers must handle errors
- Control flow is visible

This explicitness catches mistakes at compile time rather than production.

### Composing Fallible Operations

```rust
fn process() -> Result<Data, Error> {
    let config = read_config()?;
    let connection = connect(&config)?;
    let data = fetch(&connection)?;
    Ok(data)
}
```

Each `?` handles errors uniformly. Successful values unwrap and continue. Errors return early. The happy path reads linearly.

---

## Chapter 9: Data Modelling

Rust's type system enables precise domain modeling. The goal: make invalid states unrepresentable.

### Product Types (Structs)

```rust
struct User {
    id: UserId,
    email: Email,
    created: DateTime<Utc>,
}
```

A struct contains all its fields simultaneously. The possible values equal the product of each field's possibilities.

### Sum Types (Enums)

```rust
enum PaymentMethod {
    CreditCard { number: String, expiry: Date },
    BankTransfer { account: String, routing: String },
    Crypto { address: String },
}
```

An enum is exactly one of its variants. The possible values equal the sum of each variant's possibilities.

### Making Invalid States Unrepresentable

Bad design—boolean flags:
```rust
struct Order {
    shipped: bool,
    delivered: bool,
    cancelled: bool,
    // What if shipped && cancelled?
}
```

Good design—enum states:
```rust
enum OrderStatus {
    Pending,
    Shipped { tracking: String },
    Delivered { date: DateTime },
    Cancelled { reason: String },
}
```

The enum cannot represent invalid combinations. The type system enforces business rules.

### Pattern Matching is Exhaustive

```rust
fn process_payment(method: PaymentMethod) {
    match method {
        PaymentMethod::CreditCard { number, expiry } => charge_card(number, expiry),
        PaymentMethod::BankTransfer { account, routing } => transfer(account, routing),
        PaymentMethod::Crypto { address } => send_crypto(address),
    }
}
```

Add a new variant and the compiler shows every place that needs updating. Impossible to forget.

---

## Chapter 10: Turtles All The Way Down

Rust has two features that no other popular language possesses: macros and the unsafe system. These superpowers make Rust simultaneously as low-level as C and as high-level as Lisp, whereas most languages are stuck in the middle.

### The Abstraction Floor

Most languages have an abstraction floor you cannot go below without abandoning the language itself.

JavaScript and Python functions are written in C. To modify them, you must write C code yourself.

High-level languages typically hide their implementation. Even Go, often compared to Rust, is partly written in C++ and assembly.

High-level ergonomics and low-level hardware control have been considered mutually exclusive. Until now.

### Unsafe Rust

```rust
fn push_front_node(&mut self, mut node: Box<Node<T>>) {
    unsafe {
        node.next = self.head;
        node.prev = None;
        let node = Some(Box::leak(node).into());
        match self.head {
            None => self.tail = node,
            Some(head) => (*head.as_ptr()).prev = node,
        }
        self.head = node;
        self.len += 1;
    }
}
```

Unsafe operations:
- Dereferencing a raw pointer
- Reading or writing a mutable or external static variable
- Accessing a field of a union
- Calling an unsafe function (including C functions)
- Implementing an unsafe trait

These operations can violate memory-safety guarantees and cannot be used in safe Rust.

Unsafe code is for framework authors, not application developers. You will not write unsafe code in normal work.

However, frameworks you use—crates and third-party Rust libraries—will be faster, more powerful, and pure Rust with no C dependencies because of the unsafe system.

### Macros

Macros are Rust code with two critical properties:
1. They run at compile time
2. They modify source code

These properties enable capabilities impossible in nearly all other languages. Lisps are the exception.

```rust
let countries = sqlx::query!(
    "SELECT country, COUNT(*) as count
     FROM users
     WHERE organization = ?",
     organization
)
```

The `sqlx::query!` macro runs your SQL query on your local dev database at compile time in a rolled-back transaction. Errors use the same rich diagnostics as normal Rust code, visible in IDEs and Cargo.

### No Rust 2.0

There's no need for Rust 2.0. You can write new language features today without waiting for a new version that may never arrive.

Examples already in use:
- async!
- serde
- contracts
- proof systems
- literals (list!, map!, etc)

The combination of low-level hardware access and high-level macros creates a language perfect not just for today but for the next 40 years.

---

## Chapter 11: Rust's Magic Macros

Macros are the most powerful feature in Rust, and in any language.

Most articles about macros focus narrowly on their DRY capabilities—syntax rewriting and code templates. They miss the real power: compile-time code execution.

### What Made Lisp Different

Paul Graham listed nine innovations that made Lisp different. The ninth: the whole language available at compile time.

This defines Rust macros: the entire language available at compile time and runtime. A macro is a function that executes at compile time with full access to the compiler's internals and can rewrite your code.

### Declarative Macros

```rust
macro_rules! say_hello {
    () => {
        println!("Hello!")
    };
}

say_hello!(); // expands to println!("Hello!");
```

`macro_rules!` defines a pattern-matching macro. Like a match statement executed at compile time, it lets you pattern-match on token streams and generate code in response.

### Procedural Macros

Procedural macros execute arbitrary code at compile time and generate new code based on the results. They unlock truly impossible things.

**Derive macros** add code to structs and enums:
```rust
#[derive(Debug, Clone, Serialize)]
struct User { name: String }
```

**Attribute macros** define custom attributes:
```rust
#[get("/")]
fn index() {}
```

**Function-like macros** operate on token streams:
```rust
html! { <div id="app"></div> }
```

### Embedded Languages

```rust
lisp!(defun factorial ((n i32)) i32
  (if (<= n 1)
    1
    (* n (factorial (- n 1)))));

let graydons_way = factorial(5 + 5);
let mccarthys_way = lisp!(factorial (+ 5 5));
assert!(graydons_way == mccarthys_way);
```

Macros can embed entirely new languages. This macro_lisp example defines a Lisp function that compiles to normal Rust.

### Compile-time SQL Validation

```rust
let account = sqlx::query!(
    "SELECT name, id FROM account")
    .fetch_one(&mut conn)
    .await?;

println!("{}: {}", account.id, account.name);
```

At compile time, the macro:
1. Parses your SQL query string
2. Generates parameterized test data matching your table schema
3. Executes the query on your local dev database inside a transaction
4. Rolls back the transaction (no side effects)
5. Extracts column names and types for the generated Rust code

If the query fails, you see the database error in your compiler output at the exact line number.

---

# Part V: Advanced Concepts

## Chapter 12: Functional Rust

Rust is far more functional than it appears. The language's ML roots shine through: the first Rust compiler was written in OCaml. Rust is Haskell's functional paradigm expressed through C's practical syntax.

### Functional Features

Common in many languages:
1. First-class functions
2. Anonymous functions (closures)
3. Iterators
4. `map()`, `filter()`, et al.

Distinctive to Rust:
1. Configurable closures (move or borrow)
2. Sum types (Enums)
3. Lazy evaluation (iterators and macros)
4. Tail recursion (via `tailcall` crate)
5. Pure functions (with caveats)

### Pure Functions

```rust
fn f(x: i32) -> i32 { x + 1 }
```

Pure functions are deterministic: output depends only on inputs. No side-effects like memory mutations or I/O.

Language support for pure functions enables:
- **Referential transparency**: Same inputs always yield identical results
- **Parallelization**: Pure functions run safely on separate threads
- **Dead code elimination**: Unused pure functions can be safely removed

### Const Functions

```rust
const fn addone(x: i32) -> i32 { x + 1 }
```

Const functions execute at compile time and runtime, limited to provably pure operations.

Supported in const functions:
- Arithmetic operators
- Tuples, arrays, and indexing
- Struct creation
- Closures without capturing
- Shared borrows (no interior mutability)
- Control flow: `loop`, `while`, `if`, `match`

Not supported:
- Mutable references
- Interior mutability
- Iteration (use the `konst` crate)
- File system access
- Debug printing

### Practical Purity: Rayon

```rust
use rayon::prelude::*;

fn sum_of_squares(input: &[i32]) -> i32 {
    input.par_iter()
         .map(|&i| i * i)
         .sum()
}
```

Rayon parallelizes iterators with a single-line change. Type-system side-effect encoding enables parallelization without explicit purity declarations.

---

## Chapter 13: Compiler-Driven Development

Don't just run your code—model it.

### Tests vs Types

| Tests                               | Types                               |
| ----------------------------------- | ----------------------------------- |
| Improve your code with feedback     | Improve your code with feedback     |
| Not deployed (stripped from bundle) | Not deployed (stripped from binary) |
| Can be enforced in CI               | Enforced by the compiler everywhere |

### The TDD Method

1. **Red**: Write a failing test
2. **Green**: Make it pass with minimal code
3. **Refactor**: Improve the code

Tests failing? Improve the code. Tests passing? Improve the tests.

### Compiler-Driven Development

```rust
enum ID {
    V4(u8, u8, u8, u8),
    V6(u16, u16, u16, u16, u16, u16, u16, u16),
    Mac(u8, u8, u8, u8, u8, u8),
}
```

Add new variants:
```rust
enum ID {
    V4(u8, u8, u8, u8),
    V6(u16, u16, u16, u16, u16, u16, u16, u16),
    Mac(u8, u8, u8, u8, u8, u8),
    FreqHz(u64),
    Coord { lat: f64, lon: f64 },
    Uuid([u8; 16]),
}
```

The compiler tells you every match that needs updating:
```
error[E0004]: non-exhaustive patterns:
|     match node {
|           ^^^^ FreqHz, Coord, Uuid not covered
```

Compile error? Improve the code. Compiled OK? Improve the model.

### Typestate Pattern

```rust
struct Light<State> {
    state: State,
}

struct On;
struct Off;

impl Light<Off> {
    fn new() -> Self { Light { state: Off } }
    fn turn_on(self) -> Light<On> { Light { state: On } }
}

impl Light<On> {
    fn turn_off(self) -> Light<Off> { Light { state: Off } }
}
```

Invalid state transitions are compile errors:
```rust
let light = Light::new().turn_on().turn_on(); // error: no method `turn_on` on Light<On>
```

The type system enforces valid state machines.

---

# Part VI: Testing & Tooling

## Chapter 14: Rust Testing

The compiler proves many things, but not everything. Testing complements the type system.

### Testing Spectrum

| Happy Path   | Comprehensive | Probabilistic |
| ------------ | ------------- | ------------- |
| Assertions   | Black Box     | QuickCheck    |
| Doctests     | White Box     | Proptest      |
| Examples     |               | Fuzzing       |

### Assertions

```rust
fn assertion_test() {
    assert!(0 == 0);
    debug_assert!(0 == 1, "Maths is hard");
}
```

Use `assert!` for tests that always run and `debug_assert!` for compile-time stripped checks.

### Doctests

```rust
/// ```
/// my_adder(1, 2)
/// ```
fn my_adder(x: i32, y: i32) -> i32 {
    x + y
}
```

Doctests combine documentation with testing. Examples in documentation are compiled and run.

### Proptest

```rust
use proptest::prelude::*;

proptest! {
    #[test]
    fn hello_with_strings(a: String) {
        hello(a);
    }
}
```

Proptest generates random inputs and finds minimal failing cases automatically. The type system tells Proptest what to generate—no manual specification needed.

### Fuzzing

```rust
#![no_main]
#[macro_use] extern crate libfuzzer_sys;

fuzz_target!(|data: &[u8]| {
    if let Ok(s) = std::str::from_utf8(data) {
        let _ = url::Url::parse(s);
    }
});
```

Cargo-fuzz uses LLVM's libFuzzer to generate and track pseudorandom data. It persists across sessions, enabling fuzzing of effectively infinite state spaces.

### Integration Testing with SQLx

```rust
struct Country { country: String, count: i64 }

let countries = sqlx::query_as!(
    Country,
    "SELECT country, COUNT(*) as count
    FROM users
    GROUP BY country
    WHERE organization = ?",
    organization
)
    .fetch_all(&pool)
    .await?;
```

SQLx validates queries against your actual database during compilation inside rolled-back transactions. Type-safe SQL with zero runtime overhead.

---

## Chapter 15: Oxidise Your Life

Build your entire toolkit in Rust—from shells to editors. Every tool is a single `cargo install` away.

### Shell and Userland

**Nu Shell**: `cargo install nu`

Most shells remain stuck in the 1980s. Nu treats data as structured objects instead of raw text streams.

**Coreutils**: `cargo install coreutils`

The uutils project reimplements GNU Coreutils in Rust, enabling uniform tools across Linux, macOS, Windows.

**Starship**: `cargo install starship`

Fast prompt toolkit with plugins for version control, package managers, and more.

**exa**: `cargo install exa`

Better `ls` with colors, Git integration, and sensible defaults.

**ripgrep**: `cargo install ripgrep`

The fastest search tool. If you use `grep`, `ag`, or `git grep`, upgrade to ripgrep.

### Development Tools

**bacon**: `cargo install bacon`

Continuously runs `cargo clippy`, `build`, `test`, or `run` with instant feedback.

**gitui**: `cargo install gitui`

Fast, pure-Rust Git UI.

**irust**: `cargo install irust`

Rust REPL for interactive experimentation.

### Applications

**ncspot**: `cargo install ncspot`

ncurses Spotify client with Vim bindings.

**wiki-tui**: `cargo install wiki-tui`

Command-line Wikipedia access.

**rtx-cli**: `cargo install rtx-cli`

Pure-Rust asdf replacement. Switches versions of Python, Node, Ruby with 20-200x faster performance.

---

# Part VII: Deep Internals

## Chapter 16: Rust Is Written in Rust

The Rust compiler is written in Rust. This is called self-hosting.

### Maths and Programming

Maths is based on axioms—fundamental, self-evident rules. Mathematicians discover these rules; they don't invent them.

Programming is applied mathematics. Rust is built on simple, elegant rules: functional programming and the borrow checker. Starting with good rules means you can discover features rather than invent them.

### Self-Hosting

Other self-hosted languages include C, C++, Go, Haskell, Java, Kotlin, OCaml, Python (PyPy), TypeScript, and Zig.

The first version of any language can't be self-hosted—there's no compiler yet. Rust bootstrapped in OCaml.

### High-Level and Low-Level Combined

Rust uniquely combines extreme high-level functional programming with low-level hardware access through the unsafe system. Starting with low-level control in a high-level functional language yields far more than the sum of its parts.

### Algebraic Types

```rust
pub enum Option<T> {
    None,
    Some(T),
}

pub enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

Rust's Option and Result types aren't magic—they're sum types built from enums. You could build your own.

Rust has no null concept. Most languages started with nulls (the "billion-dollar mistake") and retrofitted options. This never works cleanly.

### Move Semantics

```rust
fn destroy_box(b: Box<i32>) {
    println!("Destroying a box that contains {b}");
}

fn move_demo() {
    let a = Box::new(5i32);
    destroy_box(a);
}
```

When the Box falls out of scope, the compiler inserts cleanup code. This happens deterministically at compile time, not runtime like garbage collection.

### The Drop Function

```rust
pub fn drop<T>(_x: T) {}
```

That's the entire function. No body. It takes ownership of its parameter, then does nothing—triggering Rust's normal move semantics to clean up memory as the function returns. No magic.

---

# Part VIII: Performance & Economics

## Chapter 17: Rust Makes Cents

Rust has a feature that doesn't get enough attention: Rust is cheap.

### Energy Efficiency

Research shows that the fastest languages using the least RAM also use less electricity and produce less CO2. Ruby, Python, and Perl use around 70x the energy of Rust.

### AWS Lambda Performance

```
Rust
Init Duration: 33.60 ms
Billed Duration: 393 ms (Max Memory: 31 MB)
Warm Boot: 51 ms

Node.js
Init Duration: 236.67 ms
Billed Duration: 916 ms (Max Memory: 81 MB)
Warm Boot: 268 ms
```

Results:
- Lambda initialization: 7x faster
- Warm boot: 5x faster
- Cold boot: 2x faster
- Memory usage: 2.5x less

### Developer Costs

What developers do:
- Design code
- Write code
- Read code
- Test code
- Maintain code
- Support code

Rust optimizes for the expensive activities: maintenance and support. The compiler catches bugs early, reducing production incidents and debugging time.

### Writing Rust

```rust
async fn hi(req: Request) -> Result<impl IntoResponse> {
    let params = req.query_string_parameters();
    let name = params.first("name").unwrap_or("stranger");
    Ok(format!("hello {}", name))
}
```

Writing Rust is conversing with the compiler. It tells you where you've made mistakes and suggests fixes. Because you've modeled valid states, the compiler knows valid transitions between states.

### Testing Costs

Testing is cheap in Rust. Fewer tests are needed, and they run lightning-fast. Unit tests run 80x faster than Python, 20x faster than Ruby.

Fearless concurrency extends to tests. Run them concurrently without modification.

### Maintenance Costs

Maintenance is expensive—it blocks new development. Rust prioritizes easy finishes and transitions over easy starts.

Constant compiler corrections feel frustrating initially, but it's a superpower. Instant feedback on day one beats finding a null pointer crash at 4am.

### The Whole Stack in One Language

| Layer                 | Framework       |
| --------------------- | --------------- |
| Web frontend (Wasm)   | Yew.rs          |
| Backend API           | Rocket.rs       |
| Embedded hardware     | Embassy.dev     |
| Mobile app            | Tauri           |
| TLS/SSL               | RusTLS          |
| Build tooling         | Rust macros     |

One language for everything. No context switching between Python, JavaScript, C, and shell scripts.

---

# Part IX: Web & WebAssembly

## Chapter 18: Web-Native Rust Apps

In 2017, WebAssembly arrived—a quiet revolution. Rust embraced it instantly and became the best choice for WebAssembly development.

### Why the Web Dominates

The web's advantage isn't technology—it's distribution. Anyone could write HTML, host it for free, and reach the world. For developers, it meant no installation, no patching, no app store gatekeepers.

### Beyond the DOM

WebGL offers GPU-accelerated graphics, freeing you from DOM limitations entirely.

Performance fundamentals:
- **WebAssembly** is faster than JavaScript for computation
- **WebGL** offers GPU acceleration—60fps UI without DOM overhead
- **Local storage** provides low-latency data access

### Building with Bracket

```rust
struct State {}

impl GameState for State {
    fn tick(&mut self, ctx: &mut BTerm) {
        ctx.print(1, 1, "Hello Bracket World");
    }
}

fn main_bracket() -> BError {
    let context = BTermBuilder::simple80x50()
        .with_title("Hello Minimal Bracket World")
        .build()?;
    main_loop(context, State {})
}
```

Bracket provides a virtual ASCII terminal and game loop. Build grid-based games and apps with WebGL-native rendering, 60fps performance, and WebAssembly-ready deployment.

### Building with EGUI

```rust
impl App for MyApp {
    fn update(&mut self, ctx: &Context, _frame: &mut Frame) {
        CentralPanel::default().show(ctx, |ui| {
            ui.heading("My egui Application");
            ui.horizontal(|ui| {
                ui.label("Your name: ");
                ui.text_edit_singleline(&mut self.name);
            });
            ui.add(Slider::new(&mut self.age, 0..=120).text("age"));
        });
    }
}
```

EGUI is a native Rust UI toolkit. Immediate-mode: buttons re-render every frame. This integrates naturally with game engines.

### Bevy Game Engine

```rust
fn bevy(
    mut commands: Commands,
    meshes: ResMut<Assets<Mesh>>,
    materials: ResMut<Assets<ColorMaterial>>,
) {
    commands.spawn_bundle(Camera2dBundle::default());
    commands.spawn_bundle(SpriteBundle {
        sprite: Sprite {
            color: Color::rgb(0.25, 0.25, 0.75),
            custom_size: Some(Vec2::new(50.0, 100.0)),
            ..default()
        },
        ..default()
    });
}
```

Bevy provides:
- Real-time 2D/3D graphics
- Lights, shadows, cameras, meshes, textures, materials
- Audio loading and playback
- Hot-reloading
- WebGL and WebGPU support

---

## Chapter 19: Build Your Rust Lightsaber

Set up a complete Rust development environment.

### Installation

```sh
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Installs the entire toolchain: rustc, Cargo, Clippy, rustfmt, and documentation tools.

### Editor Setup

Choose an editor with first-class LSP support:
- **VSCode**: Full-featured with rust-analyzer extension
- **Neovim**: Lightweight with LSP power
- **AstroNvim**: Out-of-the-box Rust support

### Essential Libraries

**Tokio**: Most popular async runtime
```rust
#[tokio::main]
async fn main() -> Result<()> {
    let mut client = client::connect("127.0.0.1:6379").await?;
    client.set("hello", "world".into()).await?;
    Ok(())
}
```

**Color-Eyre**: Unified error handling with beautiful reports
```rust
fn get_cluster_info() -> Result<String> {
    let config = std::fs::read_to_string("cluster.json")?;
    Ok(config)
}
```

**Rayon**: Data parallelism with guaranteed safety
```rust
fn sum_of_squares(input: &[i32]) -> i32 {
    input.par_iter()
         .map(|&i| i * i)
         .sum()
}
```

**SQLx**: Compile-time checked SQL
```rust
let _stream = sqlx::query_as::<_, User>(
    "SELECT * FROM users WHERE email = ?")
    .bind("test@example.com")
    .fetch_all(&pool);
```

**Clippy**: Enable pedantic lints
```shell
cargo clippy --fix -- \
-W clippy::pedantic \
-W clippy::nursery \
-W clippy::unwrap_used
```

---

# Part X: Philosophy & Closing

## Chapter 20: The Cult of Done

Written by maker Bre Pettis and writer Kio Stark in 2009, released under Creative Commons.

### Three States of Being

```rust
enum Being {
    NotKnowing,
    Action,
    Completion
}
```

1. **Not Knowing**: Initial ignorance, uncertainty, and curiosity
2. **Action**: Learning, exploring, working through effort and mistakes
3. **Completion**: The finished task. Not knowing becomes knowledge through action

These states are cyclical: completion leads to understanding and new ideas.

### Everything Is a Draft

Prototypes become production. Sketches become plans. Notes become published books. Nothing is perfect, even when it's finished.

### Banish Procrastination

Wait more than a week? Abandon it. Don't discard it—try something else. Creativity flows when it flows.

### The Point of Done

Being done means moving to the next project. Each completion makes you better, wiser, closer to your breakthrough.

### Failure Counts as Done

Failure proves you tried and teaches what not to do next. First-time success teaches nothing. Repeated failure teaches everything.

### Done Is the Engine of More

Being done is wonderful, addictive, and the only way to discover what's next.

### The 13 Principles

1. There are three states of being: Not knowing, action, completion.
2. Accept that everything is a draft.
3. There is no editing stage.
4. Pretending you know what you're doing is almost the same as knowing.
5. Banish procrastination. Wait more than a week? Abandon it.
6. The point of being done is not to finish, but to get other things done.
7. Once you're done, throw it away.
8. Laugh at perfection. It's boring.
9. Dirty hands are right.
10. Failure counts as done. So do mistakes.
11. Destruction is a variant of done.
12. Publish ideas on the internet—that counts as done.
13. Done is the engine of more.

---

## Chapter 21: A Good Rust Stack

A curated selection of Rust crates that combine into a production-ready stack.

### The Personal Standard Library

| CRATE        | DESCRIPTION                                           |
| ------------ | ----------------------------------------------------- |
| Color-eyre   | Ergonomic Results and colourful errors                |
| iRust        | Fully-featured REPL, debug, asm inspection            |
| Bacon        | Build, clippy, test, run watcher                      |
| Tracing      | Async-native logging                                  |
| SQLx         | Rust-native correct SQL                               |
| Poem-openapi | Fast, correct, and ergonomic REST builder             |

### Poem-openapi

```rust
#[OpenApi]
impl TodosApi {
    #[oai(path = "/todos", method = "post")]
    async fn create(&self, pool: Data<&PgPool>, body: Json<CreateTodo>)
        -> Result<Json<i64>> {
        let id = sqlx::query!("INSERT INTO todos (title) VALUES ($1) RETURNING id", body.title)
            .fetch_one(pool.0)
            .await?
            .id;
        Ok(Json(id))
    }
}
```

The type system captures the entire API interface and auto-generates documentation. No separate API configuration—structs define everything.

### Frontend with Rstml

```rust
html! {
    <div class="container">
        <h1>{title}</h1>
        <ul>
            {items.iter().map(|item| html! { <li>{item}</li> }).collect::<Vec<_>>()}
        </ul>
    </div>
}
```

RSX-style HTML validated by the Rust compiler via macros, eliminating template syntax mismatches.

---

# Conclusion

Rust represents a fundamental shift in how we think about programming languages. It proves that safety and performance aren't tradeoffs—they're complementary. That catching bugs at compile time saves more time than any productivity feature. That the best code is code that doesn't need to exist because the compiler prevents the bugs it would fix.

The learning curve is real but temporary. The benefits compound over time. Every bug the compiler catches is one less production incident. Every type constraint is documentation that never goes stale. Every ownership rule is a guarantee that makes concurrent code tractable.

The Rust community values correctness above cleverness, stability above novelty, and teaching above gatekeeping. This culture produced a language that makes you better at programming, not just at Rust.

Whether you're building web services, embedded systems, command-line tools, or anything in between, Rust offers the same guarantees: if it compiles, significant categories of bugs simply cannot exist.

That's all folks.

---

*Compiled from the No Boilerplate video series by Tris Oaten*
*Transcripts and source code: [github.com/0atman/noboilerplate](https://github.com/0atman/noboilerplate)*
