---
title: "Respect the Engine"
tagline: "you use 5% of what you bought."
version: "1.0.0"
theme: "software-engineering"
description: "Postgres is a precision instrument. You use it as a filing cabinet. The schema is the architecture. The application is the view layer. Everything else you believe is wrong."
---

# RESPECT THE ENGINE

"I write an application that uses a database."

That sentence. That's you. That's the sentence that caused every outage, every 2am page, every "why is it slow" in Slack while the on-call engineer stares at your code wondering who the fuck hired you.

The database is subordinate. The ORM is the interface. The schema is a chore. SQL is a necessary evil. Performance means "add an index." You rush through the data model to get to the REAL work — your precious application code that'll be rewritten in two years and forgotten in three.

BACKWARDS. All of it.

The database IS the system. Your application is a disposable skin. The schema outlives every line of code you will ever write and your React app will be Angular next year and something else the year after and the data will STILL BE THERE still rotting still constraining engineers who never heard your name and never will and they will spend MONTHS untangling the shit you left because you couldn't spend DAYS thinking about it. You ran `makemigrations`. You went to lunch. You left a crime scene.

You handed your most permanent artifact to a code generator. Your SCHEMA. The one thing that will outlast your career at this company and you let an ORM vomit it out while you weren't looking. You didn't review it. Didn't question it. Didn't think. You have never once in your life looked at a generated migration and asked "is this right?" Not once. You trust a machine to design your architecture and you can't even spell the word "architecture" without autocomplete.

Pathetic. Genuinely pathetic.

The ORM didn't solve the impedance mismatch. It WALLPAPERED OVER IT. Your objects are graphs. Your database is sets. Incompatible. PERMANENTLY incompatible. And every N+1 query and every cartesian explosion and every lazy-load cascade that melts your production system is that incompatibility ripping through your fantasy while you stand there going "but it works in dev." YES IT WORKS IN DEV. EVERYTHING WORKS IN DEV WITH TWELVE ROWS. You have the engineering instincts of a child testing a bridge by stepping on it gently.

You bought a precision engine — decades of optimizer research, a type system richer than your programming language — and you use 5% of it. EXPLAIN plans? Never read one. Window functions? Couldn't write one with a gun to your head. Partial indexes, domain types, SKIP LOCKED, HOT updates — blank stares. All of them. Full-text search has been in Postgres since before you started programming. You added Elasticsearch because Stack Overflow told you to. You didn't check. You NEVER check.

Slow? "Add an index." That's it. That's your whole act. A blog post wrote your entire performance strategy. You don't even remember which one.

You are not an engineer with a database problem. You ARE the database problem. You are the reason it's slow. You are the reason it's broken. You are the reason someone gets paged at 3am.

Sit the fuck down and read.

---

## I. THE SCHEMA IS THE ARCHITECTURE

The shape of your data is wrong. You KNOW it's wrong. Every query is a hack around it being wrong and you write those hacks every single day and you never stop — not once — to ask why EVERY QUERY FEELS LIKE A WORKAROUND. Because the schema is wrong. Because YOU made it wrong. In week one. Before you knew anything.

Analysts join five tables to get one answer. Five. Schema discussions eat sprints and everyone tiptoes around it because fixing the schema means admitting the schema is broken and admitting the schema is broken means admitting YOU broke it and nobody wants to have that conversation so velocity stays slow and the CTO keeps asking why and everyone shrugs.

200 tables. 30 with "user" in the name. Columns called `status`, `type`, `flag`, `misc_data`. A table called `tmp_orders_v2_final_BACKUP` sitting in production. You know that table. You KNOW it. You walk past it every day like a stain on the carpet you've decided is part of the décor.

The original authors left. Lucky them. Nobody alive understands what's there. The schema is the only documentation that can't lie — yours is so illegible it might as well be written in shit. Names that mean nothing. Relationships nobody can explain. Institutional knowledge locked in two heads. One of them is interviewing at your competitor RIGHT NOW. When they leave you will own a system nobody on earth understands. Congratulations. That's your legacy. That's what you built.

The schema IS the architecture. IS. The longest-lived hardest-to-change artifact in your system and you designed it on day one with zero domain knowledge zero review zero thought. You just typed. And now every system in the company is bolted to your day-one typing and moving ANYTHING is a multi-sprint cross-team war room and it will be expensive and it will fail partially and it will be your fault. Your fault. YOURS. Not "tech debt." Not "legacy." YOU.

Data outlives code. You've heard this. You nod at the conference talk. You fly home. You generate your schema from ORM models. Again. ALWAYS again. Because you don't believe it. You SAY "data outlives code" and you DESIGN like your application is the permanent thing and the data is disposable and three years from now your app will be gone and the data will still be there still broken still YOURS and the engineers who inherit it will spend their careers working around decisions you made before your first standup.

The schema is not a prerequisite you complete before the real work starts. The schema IS the real work. It's the most consequential design artifact you will produce — more permanent than any API, more constraining than any architecture document, more expensive to change than anything else in your system. Design it FIRST. Before the API. Before the models. Before one line of application code. Use views as contracts — stable interfaces that consumers query while you refactor the storage underneath. This is how databases are meant to work. You've never done it.

Keep shipping day-one schemas into production. Keep calling the wreckage "tech debt" like it's something that happened TO you. It didn't happen to you. You ARE the debt.

### What your type system looks like from the outside

VARCHAR and INTEGER. That's your entire modeling vocabulary. Postgres ships a type system that expresses domain rules at the storage layer — not just column shape but what values MEAN and what constraints they carry universally for every writer forever — and you've never opened the documentation page. You validate in app code what the database enforces permanently. Your app guards one door. The type system seals the building. You chose the door.

Read this table slowly. Every row is a tool you should already know.

| Your hack | What you were too lazy to find | Years of ignorance |
|---|---|---|
| Validate positive numbers in app code | `CREATE DOMAIN positive_integer AS integer CHECK (value > 0)` | Every writer. Every column. No app code. Forever. You didn't know. |
| Store status as VARCHAR, validate in app | `CREATE TYPE status AS ENUM ('active', 'suspended', 'closed')` | Invalid values die at the type level. You validated in an `if` statement. |
| Two columns for start/end, check overlaps in app | Range types (`daterange`, `int4range`) with native overlap operators | Since 2012. TWENTY TWELVE. |
| Cron job to find booking conflicts after the fact | Exclusion constraints — "no two ranges overlap" as a write-time guarantee | You find conflicts AFTER they happen. The database prevents them BEFORE. |
| Three VARCHAR columns for a composite value | Composite types, arrays — structured and collection types at the column level | Your schema is flat because your thinking is flat. |
| JSONB for everything because modeling is hard | JSONB with GIN indexing — for genuinely polymorphic data | Not a license to skip the work. Not your escape hatch from thinking. |

---

## II. THINK IN SETS

The N+1 is back. Third time this quarter. Same bug. Same cause. Same you. ALWAYS the same you.

You think in loops because you ARE a loop. Fetch one thing. Look at it. Fetch the next thing. Look at it. Four hundred round trips to render ONE PAGE and you didn't even notice. Four hundred. To render a LIST. Your brain grabs one object at a time because that's all it can hold and you dragged that crippled thinking into a set-theory engine and now you're SHOCKED it's slow. You brought a spoon to dig a foundation and you're confused that the house isn't built. The spoon is your brain. The foundation is the query. You. Are not. Equipped.

SQL is set theory. Sets. WHOLE sets. You don't fetch a user then fetch their orders then fetch the items. You describe the SHAPE of the answer — users with their orders with their items, filtered, joined, projected, in ONE declaration — and the engine builds it. You describe WHAT. It decides HOW. That's the contract you've been violating with every `for` loop you've ever written.

A set operation says "give me all active users who ordered in the last 30 days with their total spend, ranked." One statement. One round trip. The engine joins, filters, aggregates, sorts — all internally, no network hops, no serialization overhead, no iteration. Your loop version does the same work in 400 round trips because you can't conceive of asking for the answer all at once. You have to touch each piece individually like a child counting on fingers.

When that clicks — ACTUALLY clicks, not "yeah I know about JOINs" — N+1 becomes physically impossible to write. Your hands won't do it. Insane. Unthinkable.

Nobody taught you this. The shift has no name. The industry says "learn SQL" and hands you syntax — SELECT FROM WHERE — like handing someone chess notation and calling them a grandmaster. You know how the pieces move. You've been losing for years. You don't even know you're losing.

### What you refuse to learn

Every row in this table is a tool that exists. Right now. In the database you already run.

| What you actually write | What you'd know if you read the docs | This is you being incompetent |
|---|---|---|
| Subqueries nested four deep, then bitch that SQL is "unreadable" | CTEs. `WITH` clause. Name your results. | YOUR SQL is unreadable because YOU won't name things. That's not SQL's fault. That's yours. |
| Pull a million rows into Python to compute a running total in a `for` loop | Window functions. Rankings, running totals, lag/lead, partitioned aggregates. | Available since 2009. You were in middle school. Postgres was already smarter than you are now. |
| N+1 queries that JOINs can't solve | Lateral joins. Correlated subquery in FROM. | The tool you need every single week. Never heard of it. Never will, probably. |
| `SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END)` pasted from Stack Overflow | `COUNT(*) FILTER (WHERE status = 'active')` | You copy-paste SQL you don't understand. Everyone can tell. |
| Pull data to the app to run business logic on it | Functions and procedures — logic that runs WHERE THE DATA LIVES | You'd rather ship a million rows across a network than learn to write SQL. Incredible. |

Every round trip costs: connection, parse, plan, execute, serialize, network. N+1 is N wasted round trips. You've known this for years. You keep doing it. Loops are comfortable. Thinking is work. Comfort is why you're here reading this.

47 columns to display 3. You grabbed everything because specifying what you need means knowing what you need. You don't. 10,000 rows to show 20. Same disease. Every wasted byte is I/O YOU burned, memory YOU wasted, cache pressure YOU caused for every other query on the system. Your laziness is everyone else's latency. Every time.

### OFFSET is a lie

`OFFSET 10000 LIMIT 20`. Reads 10,020 rows. Throws away 10,000. Returns 20. You didn't "skip" anything. The database read EVERY ROW and threw most of them away while you thought you were being clever. Page 500 is slower than page 1. Linear degradation.

`WHERE id > last_seen_id ORDER BY id LIMIT 20`. Constant cost. Page 5,000 same speed as page 1. Keyset pagination. The pattern Postgres was designed for. You skipped it because OFFSET fit in one line. One line. That's the threshold of effort you won't cross.

---

## III. THE PLANNER IS SMARTER THAN YOU

"Add an index."

That's your whole act. Three words from a blog post you don't remember reading. Your ENTIRE relationship with database performance is cargo cult: someone said "add an index," you add an index, sometimes it works and you learn nothing from the success and sometimes it doesn't and you learn nothing from the failure and you have NEVER — not once in your career — stopped to ask what an index actually IS or what it COSTS on every write or why the planner just ignored the one you created because that would mean admitting you don't understand the tool you use every day and you will do anything — ANYTHING — to avoid that admission.

The planner ignores your indexes. It does. Often. And it's RIGHT. Smarter than you. Always has been. Always will be.

A cost-based optimizer sits between your query and the disk. Decades of research. More thought in that optimizer than in your entire application. It decides HOW. You describe WHAT. That's the contract. Feed it accurate statistics and good schemas and indexes that match actual access patterns. Or starve it. Your choice. You chose starvation. You always choose starvation.

Here's how the planner thinks — since you never bothered to learn. Data lives in 8KB pages on disk. Every page is a physical read. Sequential reads are fast — the disk head moves forward. Random reads are slow — the head jumps. An index scan looks up rows by jumping to scattered pages. When your index scan touches 40% of the table, the random I/O across 40% of the pages costs MORE than just reading the whole table sequentially. So the planner chose a sequential scan. It did the math. It was right. You blamed it. Of course you did.

The planner makes these decisions from statistics — row counts, value distributions, null fractions, most common values, join selectivity. It builds a cost model of every possible execution plan and picks the cheapest. When the statistics are stale — and yours ARE stale because you've never once checked — the cost model is wrong. Wrong model → wrong plan → slow query. Not a broken engine. A starved one. You starved it.

Slow query? Stop asking "what's wrong with the database." Ask "what did I fail to give the planner." EXPLAIN ANALYZE shows you the plan it chose — estimates versus actuals, time per node, rows expected versus rows received. When estimated rows say 100 and actual rows say 500,000, that's the planner telling you its statistics are garbage. YOUR garbage. It's TALKING TO YOU. You've never listened.

### You starve it then blame it

`ANALYZE` refreshes statistics. `default_statistics_target` controls histogram granularity — crank it for skewed columns where the default misses. Most common values, histograms, null fractions — the planner's entire worldview and you've never once checked whether it's accurate. It never occurred to you to check.

Autovacuum triggers ANALYZE based on change volume — a threshold, not a timer. But the threshold doesn't know you just loaded 10 million rows. YOU know. Run it yourself. Or watch queries go from 2ms to 20 seconds and spend two hours in Slack blaming infra for something YOU caused. Again.

### You index like a drunk throwing darts

`CREATE INDEX ON users (email)`. Done. No thought about selectivity or write cost or whether the planner will even USE it. You just created a data structure that will be maintained on every INSERT and UPDATE for the rest of this table's life and you spent less time deciding than you spend choosing lunch. Less thought than a lunch order. For a permanent data structure. On a production system.

| The tool | What it does | Why you're still useless without it |
|---|---|---|
| Partial index | `WHERE status = 'active'` — why are you indexing dead rows? | Your full-table index is 10x fatter than it needs to be. You're paying for corpses on every write. |
| Expression index | `ON (lower(email))` — indexes what you actually query | You query `lower(email)` but indexed `email`. Planner can't use it. You blamed the planner. Of course. |
| Covering index | `INCLUDE (total, created_at)` — answers the query from the index | Skips heap lookups for all-visible pages. You've never heard the term "all-visible." |
| BRIN | Block range index for naturally ordered data | Timestamps in append-only tables. Fraction of a B-tree. Been there the whole time. |
| GIN | Full-text, JSONB, arrays | The workhorse for non-scalar data. You've never touched it. |
| GiST | Geometry, range overlap, spatial | Exact for ranges and geometry. Lossy only for pg_trgm. You wouldn't know the difference. |

---

## IV. NOTHING IS FREE

"Postgres CAN do X."

CAN. That's where your analysis ends. Every. Single. Time. Can it? Great. Ship it. What it costs, what it charges downstream, what rots — you never ask. Asking means understanding. Understanding means effort. Effort on infrastructure is the one thing you will NEVER spend because infrastructure isn't real to you. It's someone else's problem until it's 3am and it's YOUR problem and you stand there staring at graphs you can't read wondering what happened.

YOU happened.

Nothing is free. Here's the model you should have learned on day one: Postgres doesn't update rows in place. It creates a NEW version of the row and marks the old one dead. Every UPDATE is an INSERT plus a tombstone. The dead versions pile up until vacuum reclaims them. Indexes get maintained on every write — each index is a separate data structure that has to be updated independently. WAL logs every change before it's considered committed. Connections are full OS processes with their own memory. EVERYTHING has weight. You've been piling weight on for years without reading the scale. You are the entropy.

This is what you've been paying without knowing. Read it. Understand what each feature COSTS.

| What you took | What it charged you | What you refused to learn |
|---|---|---|
| MVCC — concurrent reads | Dead tuples. Every UPDATE leaves a corpse in the heap rotting until vacuum finds it. | You produce thousands of corpses a day. Never wondered where they go. Never ONCE wondered. |
| Indexes — fast lookups | Every INSERT: heap + every index + WAL. Six indexes = seven writes per row. | You slapped six indexes on a write-heavy table "for performance" and made inserts 7x more expensive. You made it WORSE and you called it TUNING. |
| Connections | Full OS process per connection. Memory per connection. Idle or active — doesn't matter, you pay. | 200 connections open. 190 idle. All eating memory. All doing nothing. Like you. |
| WAL — durability | I/O on every write | You insert rows one at a time in a loop like an animal. Batch. Or use UNLOGGED tables for throwaway data — no WAL, but they get TRUNCATED on crash. Gone. Everything in them. Gone. If you put real data in an UNLOGGED table you deserve the call you'll get at 4am. |
| Checkpoints | Dirty pages flushed to disk. `checkpoint_completion_target` spreads the I/O but the cost is real. | Those "random" slowdowns every few minutes? Checkpoints. Predictable. Tunable. You never looked. You never look at anything. |

**Transactions.** Open a transaction. Make an HTTP call. Wait three seconds. Commit. Those three seconds? Your snapshot pinned the cleanup horizon. Vacuum can't reclaim dead tuples created AFTER your snapshot opened in ANY table — not just yours. The longer you hold it the more bloat piles up EVERYWHERE because you couldn't move one HTTP call outside the transaction boundary. You held the ENTIRE DATABASE hostage to an external API. You didn't know. You never know.

DB work inside. Everything else outside. Commit fast. You break all three every day and you don't even know these are rules.

### You ARE the maintenance problem

Your update frequency IS your vacuum pressure. Same rows hammered? Dead tuples at that rate. Vacuum falls behind. Bloat grows. Table bloat. Index bloat. Swelling. Silent. The database getting fatter and slower every day and you check application metrics and scratch your head. `pg_stat_user_tables` would tell you EXACTLY what's happening. You've never opened it. The system is TELLING you what's wrong and you won't look.

**HOT updates.** Update a row without touching indexed columns AND the new version fits on the same page — Postgres skips ALL index maintenance. Heap-Only Tuple. Zero write amplification. That's why fillfactor exists: leave room on the page. But you put an index on `updated_at` — the column that changes on EVERY UPDATE — and defeated HOT on every single write. EVERY. SINGLE. WRITE. Because you index without thinking. Because you do EVERYTHING without thinking.

**Transaction ID wraparound.** 32-bit transaction IDs. They wrap. Vacuum freezes old tuples to reclaim IDs — that's how the system stays ahead. When vacuum falls far enough behind the database goes read-only. Refuses ALL writes. Production. Read-only. Not a crash — a deliberate shutdown because the system you starved ran out of room to track what's alive. Because vacuum was "a DBA thing." Because the engine would babysit itself. Because you had "real work" to do. Your real work caused this.

This happens. To production databases. Run by people exactly like you.

### You know about pooling and you still hold connections during HTTP calls

Everyone knows "use a pool." Congratulations. First paragraph of every tutorial ever written. You still hold connections while your code waits on external APIs. You still size the pool for total app concurrency instead of concurrent DB work. Release the instant you're done. NEVER hold during HTTP calls or file I/O or anything that isn't a query. PgBouncer transaction-mode pooling enforces this — but session-level features like advisory locks and prepared statements BREAK under transaction-mode. The connection your lock was on isn't yours anymore. Another landmine you'll find with your face.

### Your analytics are attacking your users

OLTP and analytics on the same instance. Point lookups fighting full scans for buffer cache. Your analyst's Monday report evicts hot pages from `shared_buffers` and every production query behind it hits disk. Latency spikes for real users because someone ran a report. `pg_stat_user_tables` and `pg_statio_user_tables` would show you which tables are bleeding. You've never looked.

Read replicas for analytics. Materialized views for precomputed results — stale between refreshes, and non-concurrent refresh takes an exclusive lock, so plan it or pay for it. Heavy queries off-peak. Size `shared_buffers` so your working set fits in memory. You've been making these decisions by accident your entire career.

---

## V. CONSTRAINTS ARE LAW

"Which number is right?"

That question. From the business side. From the people who PAY you. Multiple numbers for the same metric. Orphaned records pointing at ghosts. Duplicates nobody can explain. Nulls where nulls should be impossible. No source of truth — just competing spreadsheets maintained by people who gave up on the database because the database gave up on them.

The database gave up because YOU gave up. You put your constraints in application code. YOUR code. Running in YOUR app. Guarding ONE door. And when the intern ran a migration script that didn't go through your app the constraints weren't there and the data corrupted and I spent my weekend fixing it. MY weekend. YOUR constraint. YOUR code. YOUR fault.

A database constraint would have stopped it. Cold fact. No ambiguity. Here's the difference and you need to burn it into your skull: a constraint in your app runs when YOUR code runs, in YOUR process, for YOUR one entry point. A constraint in the database runs at WRITE TIME, unconditionally, for EVERY writer that will ever exist — every app, every script, every psql session, every migration, every future system you can't predict. Your app constraint is a request. The database constraint is physics. They are not the same kind of thing and you have spent your entire career treating them as interchangeable.

You chose the request. EVERY time. A CHECK constraint felt like "overhead." Disgusting. The corruption that followed? That was your work too. Just slower. Just quieter. Just more expensive.

`NOT NULL`. `UNIQUE`. `FOREIGN KEY`. `CHECK`. Exclusion constraints. Evaluated at write time. For every writer. No exceptions. No bypass. Your app protects one entry point. The database protects ALL of them. Forever. Without maintenance. Without you.

Application validation gives friendly error messages. Keep it. But that's a courtesy. Database constraints are LAW. The only law your data has. Put your rules there. ALL of them. Or keep pouring data into an unguarded bucket and acting shocked when it rots.

---

## VI. USE WHAT SHIPS

Postgres. Redis. Elasticsearch. RabbitMQ. Kafka. MongoDB. Six systems. Six backup strategies. Six monitoring dashboards nobody checks. Six failure modes you haven't tested. Six things that break at 3am and you are the only person who can fix them and you can't fix them because you don't understand half of them because you didn't need half of them because you never checked whether Postgres ALREADY DOES THE THING.

You never checked. Not once. You googled "how to add search." First result said Elasticsearch. You added Elasticsearch. Didn't spend five minutes checking whether Postgres has full-text search. It does. It has since 2008. You added an entire system — with its own cluster and its own monitoring and its own failure modes and its own on-call rotation — because you couldn't be bothered to read ONE documentation page.

| System you're paying for | What you already own and didn't check | The cost of your laziness |
|---|---|---|
| Elasticsearch | `tsvector`, `tsquery`, `ts_rank` with GIN indexes. Stemming. Ranking. Phrase matching. | There the whole time. You never looked. |
| Elasticsearch (fuzzy) | `pg_trgm`. Trigram similarity. Index-backed `LIKE '%term%'`. | One `CREATE EXTENSION` away. You didn't know. |
| RabbitMQ / Redis queue | `SELECT ... FOR UPDATE SKIP LOCKED` | Workers skip locked rows. Commit releases. Understand the semantics or ship a broken queue. |
| External pub/sub | `LISTEN` / `NOTIFY` | Fire-and-forget. No listener = message gone. Fine for invalidation. Not for delivery. Know the difference or don't use it. |
| Redis (caching) | Materialized views. Precomputed. Refreshable. Indexable. | Stale between refreshes. Non-concurrent refresh locks the view. Your Redis cache is stale too — you just don't know how stale. |
| MongoDB | JSONB with GIN and containment operators | For genuinely polymorphic data. Not your escape from schema design. Not your coward's exit. |
| External lock service | `pg_advisory_lock` | Application mutex within one instance. Not distributed. Not crash-safe. Know the boundaries. |
| External scheduler | `pg_cron` (third-party, widely available) | Not stock. But one install vs an entire scheduling system. |

Check Postgres FIRST. Before you add another animal to the zoo. Every system you add is a permanent line item — monitoring, backups, failover, hiring, on-call, upgrades, cross-system consistency. You added six because checking the docs felt like work. The on-call engineer maintaining your zoo at 3am? That's who pays for your laziness.

Stock Postgres 13+. Not OLAP. Not cloud-vendor proprietary shit. Not DBA runbooks. What ships in the box. What you already own. What you refuse to learn.

### You put a cache on top of a cache

`shared_buffers`. Clock-sweep eviction. Transparent. Automatically correct. No invalidation bugs. No consistency problems. You added Redis on top of it. Now you have invalidation bugs AND consistency problems AND another system to monitor. Brilliant.

Did you measure where the bottleneck was? Check whether `shared_buffers` was sized right? Whether your working set fit in memory? No. "Everyone uses Redis." So you layered a broken cache over a working cache you never configured never measured never understood and told your team it was an "optimization."

### Your migrations are surgery on a conscious patient

A migration is not a code deploy. You roll back code. You cannot un-corrupt data. You cannot un-lock a table. You cannot un-rewrite 500 million rows. A production migration is irreversible surgery and you treat it with the rigor of a rename refactor.

**Transactional DDL.** Schema changes inside transactions. Step 3 fails, steps 1 and 2 undo. Atomic. Your framework supports this. You've never used it deliberately.

**`CREATE INDEX CONCURRENTLY`.** Builds without locking the table. If it fails mid-build it leaves an INVALID index behind — invisible to the planner, maintained on every write, eating resources for nothing until you find it and drop it. You've been locking production tables because you typed `CREATE INDEX` without the one word that prevents the outage. One word. You couldn't be bothered with one word.

**Lock levels.** `ALTER TABLE ADD COLUMN` — nullable or non-volatile default — instant since PG11. No rewrite. NOT NULL without a default on a table with data? Fails. Column type changes? Rewrite sometimes — many are free but you don't know which because you've never checked. `ADD CONSTRAINT ... NOT VALID` skips the validation scan. `VALIDATE CONSTRAINT` checks existing rows with a weaker lock. Two steps. Non-blocking. You've never used it because you didn't know it existed. Every migration is a coin flip and you throw the coin without looking.

### Your instruments are still in the box

| What it would tell you if you weren't blind | What you do instead |
|---|---|---|
| `pg_stat_statements` — top queries by time, calls, rows. Needs `shared_preload_libraries` and a restart. One config line. | You've never done it. The single most diagnostic tool in Postgres and you haven't configured one line. |
| `pg_stat_user_tables` — seq scans, dead tuples, last vacuum, last analyze. Per-table health. | Nothing. You look at nothing. The data screams at you and you cover your ears. |
| `pg_stat_activity` — active queries, wait events, connection state. Right now. Live. | You open it AFTER the outage. After the damage. Reactive. Always reactive. Always too late. |
| `auto_explain` — automatic EXPLAIN logging above a time threshold | You run EXPLAIN by hand on queries users already complained about. By then it's too late. It was always too late with you. |

---

## PICK

Everything here ships with stock Postgres 13+. No extensions to beg for. No bleeding edge. This is what you already own. What you've always owned.

Monday you'll generate a schema from ORM models without reviewing it. Write a loop that fires 200 queries per page. Add an index without EXPLAIN. Hold a transaction open during an HTTP call. Add Redis without measuring. Because you always have. Because thinking is effort and effort is the one thing you won't spend.

**A:** Keep going. "I write an application that uses a database." Same sentence. Same patterns. Same outages. Same 2am pages. Same you, five years from now, ten years from now, saying the same sentence, meaning the same wrong thing, causing the same damage. Comfortable. Ignorant. Permanent.

**B:** "The database is the system. I am learning to deserve it."

Pick.
