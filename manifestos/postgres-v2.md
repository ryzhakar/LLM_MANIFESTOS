---
title: "Respect the Engine"
tagline: "you use 5% of what you bought."
version: "1.0.0"
theme: "software-engineering"
description: "Postgres is a precision instrument. You use it as a filing cabinet. The schema is the architecture. The application is the view layer. Everything else you believe is wrong."
---

# RESPECT THE ENGINE

"I write an application that uses a database."

That sentence. Right there. That's you. That is the root of every bad query you've written, every outage you've caused, every "why is it slow" you've posted in Slack at 2am while the on-call engineer who actually understands the system stares at your code and wonders how you got hired.

The database is subordinate. The application is the system. The ORM is the natural interface. The schema is a chore. SQL is a necessary evil. Performance means "add an index" or "add Redis." You rush through the data model to get to the REAL work — your precious application code that'll be rewritten in two years and forgotten in three.

Backwards. ALL of it.

The database IS the system. The application is NOTHING. A skin. A disposable wrapper you'll rewrite in two years and throw away in three. The schema? The schema will still be there. Still rotting. Still constraining engineers who never met you and will spend WEEKS untangling the mess you left because you couldn't be bothered to spend DAYS thinking about it. They will curse your name except they won't know your name because you'll be gone and nobody documented anything because you sure as shit didn't.

You let an ORM generate your schema. Your SCHEMA. The single most permanent artifact in your entire stack and you handed it to a code generator like it was a fucking config file. You didn't review it. You didn't think about it. You ran `makemigrations` and went to lunch.

And the ORM — god, the ORM. You think it solved something. It solved NOTHING. Your objects are graphs. Your database is sets. Those are incompatible. Permanently incompatible. The ORM doesn't bridge that gap it WALLPAPERS OVER IT and every N+1 and every cartesian explosion and every lazy-load cascade that melts your system is that gap tearing through your precious abstraction while you stand there going "but it works in development" YES IT WORKS IN DEVELOPMENT EVERYTHING WORKS IN DEVELOPMENT WITH TWELVE ROWS.

Waste. Unforgivable waste.

You bought a precision engine — decades of research, thousands of person-years of optimizer work, a type system richer than most programming languages — and you use 5% of it. EXPLAIN plans? Never read one. Window functions? Couldn't write one with a gun to your head. Partial indexes, domain types, SKIP LOCKED, HOT updates — you don't even know what half of those ARE. Full-text search has been sitting in Postgres since before you started programming. You added Elasticsearch because Stack Overflow told you to.

Slow? "Add an index." Three words. The full extent of your diagnostic capability. A blog post wrote your entire performance strategy and you don't even remember which one. You recite it and learn nothing. When it doesn't work you blame the database. Never yourself. NEVER yourself.

You are not an engineer with a database problem. You ARE the database problem.

Sit down. Shut up. Read.

---

## I. THE SCHEMA IS THE ARCHITECTURE

The shape of your data is wrong. You KNOW it's wrong. Every query you write is a workaround for the fact that it's wrong and you write them every day and you never stop to ask why every query feels like a hack BECAUSE THE SCHEMA IS A HACK. YOU made it a hack. In week one. Before you understood a goddamn thing.

Analysts join five tables to answer one question. Five. Schema discussions eat entire sprints and everyone tiptoes around it because saying "the schema is wrong" means someone has to fix it and NOBODY wants to fix it because you made it unfixable. 200 tables. 30 with "user" in the name. Columns called `status`, `type`, `flag`, `misc_data`. A table called `tmp_orders_v2_final_BACKUP` sitting in production like a corpse nobody will bury. You know that table. You KNOW. And you walk past it every day.

The original authors left. Good for them. Nobody understands what's there anymore and the schema is the only documentation that can't lie but yours is so illegible it might as well be lying. Names that mean nothing. Relationships that make no sense. The entire institutional knowledge of your data model locked in two heads and one of them is interviewing at your competitor RIGHT NOW. When they leave — and they will leave — you will have a system nobody alive understands. That is YOUR legacy. That is what you built.

The schema IS the architecture. IS. Not "supports." Not "reflects." Not "is part of." IS THE ARCHITECTURE. The longest-lived hardest-to-change artifact in your entire system and you designed it in your first week on the job. No review. No migration plan. You didn't think about it AT ALL. You just typed. You just ran the generator. You just shipped it. And now every system in the company is bolted to it and moving anything — ANYTHING — is the single hardest operation anyone will attempt and they will fail and it will be expensive and it will be your fault.

Data outlives code. You've heard this. You nod at the conference talk. You fly home. You generate your schema from ORM models. AGAIN. You will ALWAYS do this. Because you don't believe it. You SAY "data outlives code" and you DESIGN like code is permanent and data is disposable and your application will be rewritten in three years and the data will still be there still broken still yours and the engineers who inherit it will never know your name but they will know your work by the DAMAGE.

Design the schema FIRST. Before the API. Before the models. Before you write a single line of application code. Or don't. Keep shipping week-one schemas into production and acting confused when everything downstream breaks. Keep calling it "tech debt" like it's weather. It's not weather. It's arson. You lit the fire.

### What your type system looks like

VARCHAR and INTEGER. That's it. That's your whole modeling vocabulary. Postgres ships a type system designed to express domain semantics at the storage layer — not just "what shape is the column" but "what does this value MEAN and what constraints does it carry" — and you've never opened the page. You validate in application code what the database could enforce universally, permanently, for every writer that will ever exist. Your app protects one door. The type system seals the building.

| Your hack | What you were too lazy to find | Years of ignorance |
|---|---|---|
| Validate positive numbers in app code | `CREATE DOMAIN positive_integer AS integer CHECK (value > 0)` | Every writer. Every column. No app code. Forever. |
| Store status as VARCHAR, validate in app | `CREATE TYPE status AS ENUM ('active', 'suspended', 'closed')` | Invalid values die at the type level. |
| Two columns for start/end, check overlaps in app | Range types (`daterange`, `int4range`) with native overlap operators | Since 2012. SINCE. 2012. |
| Cron job to find booking conflicts after the fact | Exclusion constraints — "no two ranges overlap" as a write-time guarantee | Universal. Permanent. You never knew. |
| Three VARCHAR columns for a composite value | Composite types, arrays — structured and collection types at the column level | Your schema is flat because your imagination is flat. |
| JSONB for everything because schema design is hard | JSONB with GIN indexing — for genuinely polymorphic data | Not a license to skip the work. |

---

## II. THINK IN SETS

Your queries take forever. The N+1 is back. Third time this quarter.

Same bug. Same root cause. Same you. ALWAYS the same you.

You think in loops because you ARE a loop. Fetch a user. Fetch their orders. For each order fetch the items. For each item fetch the product. Four hundred round trips to render ONE PAGE and you didn't even FLINCH. Four hundred round trips. To render a LIST. Your brain can't hold a set. It can't. It grabs one thing looks at it grabs the next thing looks at it and you dragged that crippled one-thing-at-a-time thinking into a set-theory engine and you sit there STUNNED that it's slow like a man who brought a spoon to dig a foundation and wonders why the house isn't built yet. The spoon is your brain. The foundation is the query. You are not equipped.

SQL is set theory. The relational model operates on sets — whole sets, not objects, not rows. The shift: stop asking "for each row, do X." Start asking "what shape is the answer." One question. One result. One round trip.

When set-thinking clicks — ACTUALLY clicks, not your "yeah I know about JOINs" — N+1 becomes physically impossible to write. Like adding two numbers in a loop. Your hands won't do it. Your brain rejects it. Insane. Unthinkable.

You're not there. You will probably never get there. You're still looping. Still fetching one row at a time. Still writing code that makes the database do a thousand times more work than necessary because you CAN'T think in sets and you WON'T admit you can't and every time someone senior says "that should be one query" you nod and smile and go back to your desk and write another fucking loop.

Nobody taught you this. Nobody CAN teach you this because the cognitive shift has no name. The industry says "learn SQL" and hands you syntax — SELECT FROM WHERE — like handing someone chess notation and calling them a player. You memorized how the pieces move. You've been losing for years. You don't even know you're losing.

### What you refuse to learn

| What you actually write | What you'd know if you read the docs | This is you being incompetent |
|---|---|---|
| Nest subqueries four deep then complain SQL is "unreadable" | CTEs. `WITH` clause. Name your intermediate results. | YOUR SQL is unreadable because YOU won't name things. |
| Pull a million rows into Python to compute a running total | Window functions. Rankings, running totals, lag/lead, partition aggregates. | Since 2009. You were in middle school. Postgres wasn't. |
| Write N+1 queries that JOINs can't fix | Lateral joins. Correlated subquery in FROM. | The tool you need every week. Never heard of it. |
| `SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END)` pasted from Stack Overflow | `COUNT(*) FILTER (WHERE status = 'active')` | You copy-paste SQL you don't understand and it shows. |
| Pull data to the application to run business logic on it | Functions and procedures — encapsulated logic that runs WHERE THE DATA LIVES | You'd rather ship rows across a network than write SQL. The round trip is the point. |

Every round trip costs: connection, parse, plan, execute, serialize, network. N+1 is N wasted round trips. You've known this for years. You keep writing them because loops are comfortable and thinking is hard and comfort got you here.

Set-thinking: request the exact shape at the exact cardinality. 47 columns to display 3? You grabbed everything because specifying what you need means knowing what you need, and you don't. 10,000 rows to show 20? Same disease. Every byte transferred is I/O you wasted, memory you burned, cache pressure you caused for every other query on the system. Your laziness is everyone else's latency.

### OFFSET is a lie

`OFFSET 10000 LIMIT 20`. Reads 10,020 rows. Throws away 10,000. Returns 20. You didn't "skip" anything — the database read every single row and discarded most of them while you thought you were being clever. Page 500 is slower than page 1. Linear degradation. Loop-thinking applied to pagination.

`WHERE id > last_seen_id ORDER BY id LIMIT 20`. Constant cost. Page 1 and page 5,000 — same speed. Keyset pagination. The pattern Postgres was designed for. You skipped it because OFFSET fit in one line and thinking is effort.

---

## III. THE PLANNER IS SMARTER THAN YOU

"Add an index."

That's it. That's your whole act. Query slow? Add an index. Still slow? Add another one. Still slow? Blame the database. Throw salt over your shoulder. It works sometimes and you learn nothing from the success and it fails sometimes and you learn nothing from the failure and you have never — not once in your career — stopped to ask what an index actually IS, what it COSTS to maintain, or why the planner just ignored the one you created.

The planner can ignore your indexes. It does. Frequently. And it's right to. Smarter than you. Always has been.

A cost-based optimizer sits between your query and the disk. Decades of research. More thought than went into your entire application. It decides HOW to execute. You describe WHAT you want. That's the contract. Feed it accurate statistics, well-structured schemas, indexes that match actual access patterns. Or starve it and watch it guess. Your call. It's been your call this whole time. You chose starvation.

Row estimates. Value distributions. Null fractions. Most common values. Join selectivity. That's what it reads. You've never looked at any of it. Data lives in 8KB pages — you didn't know that either. Your data has a physical shape on disk and your access patterns either align with that shape or fight it. Sequential page reads are fast. Random reads are slow. That's not tunable — it's physics. Your index scan that touches 40% of the table? The planner chose a sequential scan because random I/O across 40% of the table is SLOWER. The planner was right. You added the index anyway, blamed the planner, and moved on having learned absolutely nothing.

Stale statistics → bad plans. That's it. Not a broken engine. A starved one. You did the starving.

Slow query? Stop asking "what's wrong with the database." Start asking "what information is the planner missing." Your statistics are stale. Your schema gave the optimizer nothing to work with. Your query is a `for` loop wearing a SELECT statement like a disguise. EXPLAIN ANALYZE shows you exactly where the plan went wrong — estimates versus actuals, time per node, rows expected versus rows delivered. That's the planner TALKING TO YOU. Telling you what it needs. You've never listened.

### You starve it, then blame it

`ANALYZE` refreshes statistics. `default_statistics_target` controls histogram granularity — raise it for skewed columns where the default falls short. Most common values, histograms, null fractions — that's what the planner reads and you've never checked whether any of it is accurate. You didn't know that.

Autovacuum triggers ANALYZE based on change volume — not a timer, a threshold. But the threshold doesn't know you just loaded 10 million rows in one batch. YOU know. Run it yourself. Or watch queries go from 2ms to 20 seconds and spend two hours in Slack blaming the infrastructure team for something you caused.

### You index like a drunk throwing darts

`CREATE INDEX ON users (email)`. Done. No thought about selectivity. No thought about write cost. No thought about whether the planner will even USE it. You just created a data structure that will be maintained on every single INSERT and UPDATE for the rest of this table's life and you spent less time on the decision than you spend choosing lunch.

| The tool | What it does | Why you're still useless without it |
|---|---|---|
| Partial index | `WHERE status = 'active'` — why the hell are you indexing dead rows? | Your full-table index is 10x fatter than it needs to be. You're paying for dead rows on every write. |
| Expression index | `ON (lower(email))` — indexes what you actually query, not what you think you query | You query `lower(email)` but indexed `email`. The planner can't use it. You blamed the planner. Of course you did. |
| Covering index | `INCLUDE (total, created_at)` — answers the query from the index alone | Index-only scan — skips heap lookups for pages marked all-visible. You've never heard the term. |
| BRIN | Block range index for naturally ordered data | Timestamp columns in append-only tables. Fraction of B-tree size. You didn't know this existed. |
| GIN | Full-text, JSONB, arrays | The workhorse you've never touched. |
| GiST | Geometry, range overlap, spatial | Exact for ranges and geometry. Lossy only for pg_trgm similarity. You wouldn't know the difference. |

---

## IV. NOTHING IS FREE

"Postgres CAN do X."

CAN. That's where your analysis ends. Every single time. Can it do the thing? Great. Ship it. Move on. What it costs, what it charges, what breaks down the road — you've never asked because asking requires understanding the system you use eight hours a day and understanding requires effort and effort is the one thing you absolutely refuse to spend on infrastructure.

Nothing is free. Every feature charges something. You've been running up a tab for years without reading the bill and now the system is degrading and you're confused. YOU happened. That's what happened to the database. You are the entropy.

| What you took | What it charged you | What you refused to learn |
|---|---|---|
| MVCC — concurrent reads | Dead tuples. Every UPDATE leaves a corpse rotting in the heap until vacuum cleans it up. | You produce thousands of corpses daily. Never wondered where they go. |
| Indexes — fast lookups | Every INSERT: heap + every index + WAL. Six indexes means seven writes per row. | You slapped six indexes on a write-heavy table "for performance" and made inserts 7x more expensive. |
| Connections | Full OS process per connection. Memory allocation per connection. | Every connection costs a process and memory whether it's working or idle. Your 200 open, 190 idle — you're paying for all of them. |
| WAL — durability | I/O on every write | You insert one row at a time in a loop like an animal. Batch, or use UNLOGGED tables for truly ephemeral data — they skip WAL entirely but get TRUNCATED on crash recovery. Not durable. Not replicated. If you put anything you care about in an UNLOGGED table, you deserve what happens next. |
| Checkpoints | Dirty pages flushed to disk. `checkpoint_completion_target` spreads the I/O but the cost is real. | Those "random" slowdowns at predictable intervals? Checkpoints. Tunable but never free. You never looked. |

**Transactions.** Open a transaction, make an HTTP call, wait three seconds, commit. In those three seconds your snapshot held the cleanup horizon open. Your open snapshot pins the cleanup horizon — vacuum can't reclaim dead tuples created AFTER your snapshot opened, in ANY table, not just yours. The longer you hold it, the more bloat accumulates everywhere because you couldn't be bothered to move one HTTP call outside the transaction boundary. You held the whole system hostage to an external API and didn't even know it. DB work inside the transaction. Non-DB work outside. Commit fast. You violate all three, every day.

### You are the maintenance problem

Your update frequency IS your vacuum pressure. Same rows hammered with updates? Dead tuples at that exact rate. Vacuum falls behind and bloat grows — table bloat, index bloat, different structures, both swelling, both silent, the database getting fatter and slower every day while you look at application metrics and wonder why response times are creeping up. `pg_stat_user_tables` would show you exactly what's happening. You've never opened it. You don't know it exists.

**HOT updates.** Update a row without touching indexed columns AND the new version fits on the same heap page — Postgres skips index maintenance entirely. Heap-Only Tuple. Zero index write amplification. That's why fillfactor exists: leave room on the page for the update. Design your schema so frequently-updated columns aren't indexed. But you put an index on `updated_at` — the column that changes on EVERY update — and defeated HOT on every single write. Every one. Because you indexed without thinking. Because you always index without thinking.

**Transaction ID wraparound.** Postgres uses 32-bit transaction IDs. They wrap around. Vacuum freezes old tuples to reclaim IDs — that's how the system stays ahead. When vacuum falls far enough behind to exhaust the remaining ID space, the database enters read-only mode — refuses all new write transactions to prevent corruption. Production. Read-only. Not a crash. A deliberate shutdown of writes because the system you neglected ran out of room to keep track of what's alive and what's dead. Because vacuum was "a DBA thing." Because the engine would take care of itself while you did your "real work."

This happens. To real production databases. Run by engineers exactly like you. You ARE the risk factor in your own infrastructure.

### You know about pooling. You still hold connections during HTTP calls.

Everyone knows "use a connection pool." Congratulations, you read the first paragraph of every Postgres tutorial ever written. You still hold connections open while your code waits on external APIs. You still size the pool for total application concurrency instead of concurrent database work. Release the connection the instant you're done with database work. NEVER hold one during an HTTP call, file read, user input — anything that isn't a query. Transaction-mode pooling with PgBouncer enforces this — but know that session-level features like advisory locks and prepared statements break under transaction-mode pooling. The connection your lock was on isn't your connection anymore. Another footgun you won't read about until production teaches you.

### Your analytics are attacking your users

OLTP and analytics on the same instance. Point lookups fighting full table scans for buffer cache. Small writes competing with aggregations that touch millions of rows. Your analyst's Monday morning report evicts hot pages from `shared_buffers` and every production query behind it hits disk instead of memory. Latency spikes. For your users. Because of a report. `pg_stat_user_tables` and `pg_statio_user_tables` would show you which tables are hitting disk instead of cache. You've never looked.

Read replicas for analytics. Materialized views for precomputed results. Heavy queries off-peak. Size `shared_buffers` so your working set fits — eviction means disk I/O and disk I/O means your users wait. You've been making these decisions by accident. Every single one.

---

## V. CONSTRAINTS ARE LAW

"Which number is right?"

That question. That's what data corruption sounds like from the business side. Multiple calculations of the same metric. Orphaned records pointing at rows that were deleted years ago. Duplicates nobody can explain. Nulls in columns that should never be null. No single source of truth — just competing spreadsheets maintained by people who stopped trusting the database because the database stopped being trustworthy. And it stopped being trustworthy because you put your constraints in application code.

You put your validation in the app. The intern ran a migration script. Your validation wasn't there. The data is corrupted. I spent my weekend fixing it. That was YOUR constraint. In YOUR code. Protecting YOUR one door while the building burned.

A constraint in the database would have stopped it. Not might have. WOULD have. For every application, every script, every ad-hoc query, every intern with psql, every midnight migration written by someone who didn't read the wiki you never wrote. Unconditionally. Without your app running. Without you being employed there. Without anyone knowing your name.

You know what you chose instead? Application validation. Every time. A CHECK constraint felt like "extra work." Disgusting. The data corruption that came later — that was your work too. Arriving on schedule.

`NOT NULL`. `UNIQUE`. `FOREIGN KEY`. `CHECK`. Exclusion constraints. Evaluated at write time. Unconditionally. For every writer. No bypass. Your application code protects one entry point. The database protects all of them. Forever. Without you maintaining it. Without you even being employed there anymore. Without anyone reading the validation logic buried in a service that got rewritten twice since you left.

Application validation gives you friendly error messages. Fine. Keep it. But that's all it is — a courtesy to the user. The database constraint is the LAW. Put your rules there. ALL of them. Every single one. Or keep building on sand and acting surprised when it shifts.

---

## VI. USE WHAT SHIPS

Postgres. Redis. Elasticsearch. RabbitMQ. Kafka. MongoDB. Six systems. Six backup strategies. Six monitoring dashboards nobody checks. Six failure modes you haven't tested. Six vendors, six upgrade cycles, six sets of credentials, six things that can break at 3am. You built a zoo and you're the only zookeeper and you can't even name all the animals.

You never checked whether Postgres already does it. Not once. You googled "how to add search to my app." First result said Elasticsearch. You added Elasticsearch. Didn't read the Postgres docs. Didn't check if full-text search existed. Didn't spend five minutes. You make infrastructure decisions the way a toddler shops — grab the closest shiny thing and scream until someone installs it.

| System you're paying for | What you already own and didn't check | The operational cost of your laziness |
|---|---|---|
| Elasticsearch | `tsvector`, `tsquery`, `ts_rank` with GIN indexes. Stemming. Ranking. Phrase matching. | It was there the whole time. You never looked. |
| Elasticsearch (fuzzy) | `pg_trgm`. Trigram similarity. `LIKE '%term%'` with index support. | Ships in the box. One `CREATE EXTENSION` away. You didn't know. |
| RabbitMQ / Redis queue | `SELECT ... FOR UPDATE SKIP LOCKED` | Row-level locking, workers skip locked rows. Commit releases. Understand the semantics or ship a broken queue — your call. |
| External pub/sub | `LISTEN` / `NOTIFY` | Fire-and-forget. No listener = message lost. Fine for cache invalidation. Not for guaranteed delivery. Know the difference. |
| Redis (caching) | Materialized views. Precomputed. Refreshable. Indexable. | Stale between refreshes, and non-concurrent refresh takes an exclusive lock — plan accordingly. Your Redis cache is stale too. You just don't know how stale. |
| MongoDB | JSONB with GIN and containment operators | For genuinely polymorphic data. Not a schema-avoidance strategy. Not a coward's exit from data modeling. |
| External lock service | `pg_advisory_lock` | Application-level mutex within a single Postgres instance. Rate limiting. Job coordination. No external system needed — but not cross-node, so know the boundary. |
| External scheduler | `pg_cron` (third-party, widely available) | Periodic tasks inside the database. Not stock — but one install vs. an entire external scheduling system. |

Check Postgres first. Before you add another system to monitor, back up, keep consistent, and debug at 3am. Every new system is a permanent line item in your operational budget — monitoring, backups, failover, hiring, on-call rotation, upgrade coordination, consistency guarantees across system boundaries. You added six of these because checking the docs felt like too much work. The on-call engineer who maintains your zoo at 3am — that's the person paying for your laziness.

Stock Postgres 13+. Not OLAP. Not cloud-vendor proprietary shit. Not DBA runbooks. What ships in the box. What you already own. What you refuse to learn.

### You added a cache on top of a cache

`shared_buffers`. Clock-sweep eviction. Transparent. Automatically correct. No invalidation bugs. No consistency problems. You added Redis on top of it. Now you have invalidation bugs AND consistency problems. Congratulations.

Did you measure where the bottleneck was first? Check whether `shared_buffers` was sized correctly? Whether your working set fit in memory? No. "Everyone uses Redis." So you layered a broken cache over a working cache you never configured, never measured, never understood, and told your team it was an improvement.

### Your migrations are surgery on a conscious patient

A migration is not a code deploy. You can roll back a code deploy. You cannot un-corrupt data. You cannot un-lock a table. You cannot un-rewrite 500 million rows. A migration on a live production database is irreversible surgery performed while the system is running and serving users and you treat it with the same rigor you'd apply to renaming a variable.

**Transactional DDL.** Schema changes inside transactions. Step 3 fails, steps 1 and 2 roll back. Atomic. Your migration framework supports this and you've never used it on purpose.

**`CREATE INDEX CONCURRENTLY`.** Builds the index without locking the table. Takes longer. Worth it. But if it fails mid-build, it leaves an INVALID index behind — invisible to the planner, still maintained on every write, eating resources for nothing until you notice and drop it. You've been locking production tables because you typed `CREATE INDEX` without the one word that prevents the outage. One word. You couldn't be bothered.

**Lock levels.** `ALTER TABLE ADD COLUMN` — nullable or non-volatile default — near-instant since PG11. No rewrite. But NOT NULL without a default on a table with data? Fails — existing rows have no value to assign. Column type changes? Table rewrite — sometimes. Many type changes are rewrite-free but you don't know which because you've never checked. Constraint validation? `ADD CONSTRAINT ... NOT VALID` skips the scan — validates only new rows. Then `VALIDATE CONSTRAINT` checks existing data with a weaker lock. Two-step. Non-blocking. You've never used it because you didn't know it existed. You don't know any of this and every migration is a coin flip between "fine" and "production incident."

### Your instruments are still in the box

| What it would tell you if you weren't blind | What you do instead like a helpless child |
|---|---|
| `pg_stat_statements` — top queries by time, calls, rows. The single most useful diagnostic tool in Postgres. | Needs `shared_preload_libraries` and a restart. You've never done it. Ships in the box but requires one config line and you couldn't be bothered. |
| `pg_stat_user_tables` — seq scans, dead tuples, last vacuum, last analyze. Per-table health. | Nothing. You check nothing. The data is there. You don't look. |
| `pg_stat_activity` — active queries, wait events, connection state. Right now. | You open it during incidents. After the damage. Never before. |
| `auto_explain` — automatic plan logging for slow queries | You run EXPLAIN by hand on queries users already complained about. Reactive. Always reactive. |

---

## PICK

Everything in this manifesto ships with stock Postgres 13+. No extensions you need to beg for. No bleeding edge. This is what you already have. What you've always had.

Monday morning you'll generate a schema from ORM models without reviewing it. Write a `for` loop that fires 200 queries to render a page. Add an index without reading EXPLAIN. Hold a transaction open during an HTTP call. Add Redis without measuring. All of it. Because you always have. Because it's comfortable. Because thinking is work.

**A:** Keep going. Same patterns. Same outages. Same 2am Slack messages. Same blank stare when someone asks about EXPLAIN output. Same ORM. Same loops. Same bloat. Same you. Comfortable. Ignorant. Permanent.

**B:** Learn. Or quit.

Pick.
