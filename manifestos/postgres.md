---
title: "Respect the Engine"
tagline: "you use 5% of what you bought."
version: "1.0.0"
theme: "software-engineering"
description: "Postgres is a precision instrument. You use it as a filing cabinet. The schema is the architecture. The application is the view layer. Everything else you believe is wrong."
---

# RESPECT THE ENGINE

"I write an application that uses a database."

That sentence. Right there. The root of every bad query you've written, every outage you've caused, every "why is it slow" you've posted in Slack at 2am while the on-call engineer who actually understands the system stares at your code and wonders how you got hired.

The database is subordinate. The application is the system. The ORM is the natural interface. The schema is a chore. SQL is a necessary evil. Performance means "add an index" or "add Redis." You rush through the data model to get to the REAL work — your precious application code that'll be rewritten in two years and forgotten in three.

Backwards. All of it.

The database is the system. The application is a disposable view layer. The schema outlives every line of code you will ever write. Your React app will be Angular next year and something else the year after. The data will still be there. Still shaping every query, every report, every integration, every decision made by systems you can't imagine yet. The most permanent artifact in your stack and you designed it in sprint one. With zero domain knowledge. Generated it from ORM models. Never came back.

You delegated your architecture to a code generator. Pathetic.

You bought a precision engine — decades of research, thousands of person-years of optimizer work, a type system richer than most programming languages — and you use 5% of it. EXPLAIN plans? Never read one on purpose. Window functions? Never written one. Partial indexes, domain types, SKIP LOCKED, HOT updates — blank stares, all of them. Full-text search has been sitting in Postgres THIS WHOLE TIME and you added Elasticsearch because you couldn't be bothered to check.

Slow? "Add an index." That's it. The full extent of your diagnostic capability. Three words from a blog post written by someone who actually understood the engine. You recite them like a parrot. Zero comprehension. When it doesn't work you blame Postgres. Never yourself. NEVER yourself.

Here's the religion. Try to keep up.

---

## I. THE SCHEMA IS THE ARCHITECTURE

The shape of the data is wrong. You know it.

Every query is a workaround. Analysts join five tables for one answer. Schema discussions eat sprints. Velocity is slow and nobody can explain why. YOU can explain why. The schema doesn't match the domain. It never did. You slapped it together in week one, and the domain evolved while the schema rotted. Now you have 200 tables, 30 with "user" in the name. Columns called `status`, `type`, `flag`, `misc_data`. A table called `tmp_orders_v2_final_BACKUP` sitting in production like a tombstone for decisions nobody remembers making.

Nobody understands what's there anymore. The original authors left. The schema is the only documentation that can't lie, and yours is illegible. Names that mean nothing. Relationships that make no sense. Institutional knowledge locked in two heads, one of which is already interviewing elsewhere. Design for legibility or accept that your schema is a write-only artifact — documentation nobody can read, about a system nobody can change.

The schema IS the architecture. Not "supports." Not "reflects." IS. The data model is the longest-lived, hardest-to-change artifact in your system. Data accumulates dependencies like gravity accumulates mass — other systems attach, downstream consumers multiply, and moving anything becomes the hardest operation in software. You designed a public API in your first week on the project. No design review. No migration strategy. No thought.

Data outlives code. Not as a platitude — as a physical fact. Your application will be rewritten. The data will not be migrated. It will be inherited, by engineers who never met you, who will be constrained by every decision you made in week one. Everyone says "data outlives code." Nobody designs like it's true. You nod at the conference talk, fly home, and generate your schema from ORM models. Again.

Design the schema FIRST. Before the API. Before the application models. As the primary architectural act. Use views as stable contracts — the API surface within the database itself. Consumers query views; you refactor the tables underneath without breaking them. Or keep wondering why every schema change is a cross-team incident.

### Your type system is a crayon drawing

VARCHAR and INTEGER. That's your whole palette. Postgres ships a type system that makes your application-layer validation look like a child's homework.

| You do this | Postgres already has this |
|---|---|
| Validate positive numbers in app code | `CREATE DOMAIN positive_integer AS integer CHECK (value > 0)` — enforced on every column, every writer, no app code |
| Store status as VARCHAR, validate in app | `CREATE TYPE status AS ENUM ('active', 'suspended', 'closed')` — invalid values rejected at the type level |
| Two columns `start_date`/`end_date`, check overlaps in app | Range types (`daterange`, `int4range`) — native containment, overlap detection. Since 9.2. Since 2012. |
| Cron job to find booking overlaps after the fact | Exclusion constraints — "no two ranges overlap" as a write-time guarantee. Universal. Forever. |
| JSONB column for everything because schema is hard | JSONB with GIN indexing — for genuinely polymorphic data. Not an excuse to skip schema design. |

---

## II. THINK IN SETS

Your queries take forever. The N+1 is back. Third time this quarter. Same bug. Same root cause. Same you.

Not a query problem. A brain problem.

You think in loops. Fetch a user. Fetch their orders. For each order, fetch the items. For each item, fetch the product. 400 database round trips to render one page. You didn't even flinch. 400 round trips to render a LIST. Because your brain processes data one object at a time, one row at a time, one iteration at a time, and you brought that `for` loop brain to a set-theory engine and now you're SHOCKED it's slow.

SQL is set theory. The relational model operates on sets. Whole sets. Not objects. Not rows. The shift: stop asking "for each row, do X" and start asking "describe the shape of the result." One question. One answer. One round trip.

When this clicks — actually clicks, not "I've heard this before" — N+1 becomes unthinkable. Not inadvisable. Unthinkable. Like adding two numbers with a `for` loop. The procedural approach stops being suboptimal and starts being obviously insane.

Nobody teaches this shift. It's unnamed in the industry — they say "learn SQL" and teach syntax without ever articulating the paradigm shift underneath. Chess notation without strategy. You know how the pieces move. No idea how to play. And you've been losing for years.

### Tools you refuse to learn

| You do this | Postgres does this |
|---|---|
| Nested subqueries four levels deep, then complain SQL is "hard to read" | CTEs. `WITH` clause. Name your intermediate results. YOUR SQL is hard to read because you won't name things. |
| Pull a million rows into Python to compute a running total in a `for` loop | Window functions. Rankings, running totals, lag/lead, partition aggregates — without collapsing the result set. Since 8.4. Since 2009. |
| N+1 queries that JOINs can't solve | Lateral joins. Correlated subquery in the FROM clause. The tool you need every week and have never heard of. |
| `SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END)` pasted from Stack Overflow | `COUNT(*) FILTER (WHERE status = 'active')`. Conditional aggregation without CASE nesting. |

Every round trip costs: connection, parse, plan, execute, serialize, network. N+1 is N unnecessary round trips. You know this. You've known this for years. You keep doing it because `for` loops are comfortable and thinking in sets is hard. Comfort is what got you here.

Set-thinking means requesting the exact shape at the exact cardinality. 47 columns to display 3 is loop-thinking — grab everything, sort it out later. 10,000 rows to show 20 is loop-thinking. Every byte transferred is I/O, memory, cache pressure. Specifying what you need requires knowing what you need. That's the cost of thinking in sets.

### OFFSET is a lie

`OFFSET 10000 LIMIT 20`. Reads 10,020 rows. Discards 10,000. Returns 20. You didn't "skip" anything. The database read every row and threw most of them away. Page 500 costs more than page 1. Linear degradation. Loop-thinking applied to pagination.

`WHERE id > last_seen_id ORDER BY id LIMIT 20`. Constant cost with an index on the keyset column. Page 1 and page 5,000 take the same time. Set-thinking applied to pagination. The pattern Postgres was designed for. The one you've never used because OFFSET was shorter to type.

---

## III. THE PLANNER IS A COLLABORATOR

"Add an index."

Your answer to everything. Query slow? Add an index. Still slow? Another index. Still slow? Blame the database. Salt over your shoulder. It works sometimes — you learn nothing from the success. It fails sometimes — you learn nothing from the failure either. What an index IS, what it COSTS, why the planner ignored the one you just created — you've never asked any of these questions.

That last part. The planner can ignore your indexes. It does. Often. And it's usually right.

A cost-based optimizer — decades of research, more thought than your entire application — sits between your query and the disk. It decides HOW. You describe WHAT. That's the contract. Feed it accurate statistics, well-structured schemas, indexes that match real access patterns. Or starve it and watch it guess.

Row estimates, value distributions, null fractions, most common values, join selectivity — that's what it reads. Data lives in 8KB pages. Sequential reads are fast. Random reads are slow. Your index scan touches 40% of the table's pages at random? Sequential scan wins. The planner knows this. You added the index anyway, blamed the planner for ignoring it. Smarter than you. Usually is.

Stale statistics → bad plans. Not a broken engine. A starved one. You did the starving.

Slow query? "What information is the planner missing?" The database is fine. Your statistics are stale. Your schema gave the planner nothing. Your query reads like a `for` loop in a trench coat. EXPLAIN ANALYZE shows you exactly where — estimates versus actuals, time spent, information missing. That's not debugging. That's the planner telling you what it needs. Write, explain, understand, adjust, repeat.

### Feed the planner

`ANALYZE` refreshes statistics. `default_statistics_target` controls granularity — raise it for skewed columns where the default histogram isn't enough. Most common values, histograms, null fractions: this is what the planner reads. Managing statistics quality IS managing plan quality. They are the same activity.

Autovacuum runs ANALYZE periodically, but autovacuum doesn't know you just loaded 10 million rows. YOU know. Run it yourself. Or keep watching queries go from 2ms to 20 seconds after a data load and blaming the database.

### Stop throwing darts

You create indexes drunk and blindfolded. `CREATE INDEX ON users (email)`. Done. Never thought about what, why, or what it costs on every write.

| Index type | What it does | Why you're still not using it |
|---|---|---|
| Partial | `... WHERE status = 'active'` — index only rows you query | Your full-table index is 10x bigger than it needs to be |
| Expression | `... ON (lower(email))` — index computed values | You query `lower(email)` but index `email`. Planner can't use it. You blame the planner. |
| Covering | `... INCLUDE (total, created_at)` — columns in the index | Index-only scan. No heap lookup. No second I/O. |
| BRIN | Naturally ordered data (timestamps, sequential IDs) | Only works when physical row order matches logical order. Tiny when it does. |
| GIN | Full-text search, JSONB containment, array membership | The workhorse for non-scalar data. You've never used it. |
| GiST | Geometric data, range overlap | Lossy for tsvector — requires heap rechecks. For full-text, use GIN. |

---

## IV. EVERYTHING HAS A PHYSICAL COST

"Postgres CAN do X."

CAN. That's your entire analysis. Can it? Great. Ship it. You never ask the next question. What does it COST? Cost requires understanding. Understanding requires effort. Effort is the one thing you will not spend.

Every feature has a physical cost. There is no free lunch. There is no magic. You've been adding capabilities without budgeting their consequences for years and you stand there baffled watching the system degrade.

You happened. That's what happened.

| Feature | What you get | What it costs | The part you ignored |
|---|---|---|---|
| MVCC | Concurrent reads | Dead tuples. Every UPDATE/DELETE leaves a corpse. They rot in place until vacuum cleans up. | You generate thousands of dead tuples daily and never wondered where they go. |
| Indexes | Fast lookups | Every INSERT: heap + every index + WAL. Six indexes = seven writes per insert. | You added six indexes on a write-heavy table "for performance." Inserts got 7x more expensive. UPDATEs can avoid this via HOT — INSERTs cannot. |
| Connections | Database access | Full OS process per connection. Memory per connection. | Postgres is built for tens to low hundreds of active connections. Your 200 open, 190 idle — you're paying for all of them. |
| WAL | Durability | I/O on every write, journaled separately | You insert rows one at a time in a loop. Batch. Or use `UNLOGGED` tables for ephemeral data — no WAL, no replication, no recovery. |
| Checkpoints | Dirty pages flushed to disk | I/O spikes. Latency spikes. | Your "random" slowdowns at regular intervals? Checkpoints. Predictable. You never looked. |

**Transactions.** Everything they touch, for their entire duration. Locks. Snapshots. Vacuum prevention. Open a transaction, make an HTTP call, wait 3 seconds, commit. Those 3 seconds? Your snapshot held the cleanup horizon open. Bloat pressure across the ENTIRE database — every table, not just yours — because you couldn't move one HTTP call outside the transaction boundary.

DB work inside the transaction. Everything else outside. Commit promptly. Three rules. You break all three.

### Your write patterns are the maintenance schedule

Your update frequency IS your vacuum pressure. Same rows updated constantly? Dead tuples at the same rate. Vacuum falls behind, bloat grows. Table bloat. Index bloat. Different things, both growing, both silent. Fatter and slower every day. `pg_stat_user_tables` would show you. You've never opened it.

**HOT updates.** Update a row without touching any indexed column and Postgres skips index maintenance entirely. Heap-Only Tuple update. No write amplification from indexes. Design your schema for this — arrange it so the columns you update frequently are not the columns you index. Your `updated_at` with an index on it defeats HOT on every write. Every single one. This is a schema design decision, not a tuning parameter.

**Transaction ID wraparound.** Postgres uses 32-bit transaction IDs. They wrap around. When vacuum falls behind and can't freeze old tuples, the database enters read-only mode — refuses new write transactions to prevent data corruption before wraparound occurs. Production goes read-only. Not a crash. A deliberate shutdown of writes. Because you thought vacuum was "a DBA thing." Because you thought the engine would babysit itself while you did your "real work."

This happens. To production databases. Run by engineers exactly like you.

### Budget your connections

Pool them. Size the pool for concurrent database work, not total application concurrency. Release immediately after database work. NEVER hold a connection during HTTP calls, file I/O, user input. Transaction-mode pooling with PgBouncer enforces this architecturally.

### Separate competing workloads

OLTP and analytics on the same instance. Point lookups fighting full table scans. Small writes competing with large aggregations. They collide over buffer cache, I/O, CPU. Your analyst's report evicts hot pages from `shared_buffers`, causing latency spikes for production users. `pg_stat_bgwriter` would tell you this is happening. You've never looked at it.

Read replicas for analytics. Materialized views for precomputed results. Heavy queries during off-peak. Size `shared_buffers` so your working set fits in memory — eviction means disk I/O, and disk I/O means your users wait. These are physical cost decisions. Budget them.

---

## V. CONSTRAINTS ARE LAW

"Which number is right?"

Multiple calculations of the same metric. Orphaned records. Duplicates. Nulls where they shouldn't be. No single source of truth. Trust gone. And once trust is gone — really gone — everyone builds a shadow system. Their own spreadsheet. Their own "source of truth." You don't have a database anymore. You have a suggestion box nobody checks.

This happened because you put your constraints in application code.

Application constraint: protects against bugs in THAT application. Database constraint: enforced for every writer. Every application, script, ad-hoc query, intern with a SQL client, midnight migration that will ever touch this data. No bypass under normal operation.

Not "both good practice." Categorically different things. One is a courtesy. The other is physics.

You chose the courtesy. Every time. Writing a CHECK constraint felt like "extra work." The data corruption that followed? That was your work too. Arriving late.

`NOT NULL`. `UNIQUE`. `FOREIGN KEY`. `CHECK`. Exclusion constraints. Evaluated at write time. Unconditionally. For all writers. Your application code protects against one writer. The database protects against all of them. Forever. Without maintenance. Without hoping the new hire reads the wiki page about "data rules" that nobody updated since 2019.

Application validation is necessary — error messages, client feedback. But application validation is a courtesy. Database constraints are the rules of your domain expressed in the only place that enforces them universally. Put them there. ALL of them.

---

## VI. USE WHAT SHIPS

Postgres plus Redis plus Elasticsearch plus RabbitMQ plus Kafka plus MongoDB. Six systems. Six sets of backups. Six failure modes. Six monitoring dashboards nobody checks. Six specialists you can't hire. You built a zoo. You are the zookeeper. And you never — not once — opened the Postgres documentation to ask whether it already does the thing you're adding a new animal for.

You checked nothing. Googled "how to add search to my app," first result said Elasticsearch, so you added Elasticsearch. Like a child grabbing the first toy on the shelf.

| You added | Postgres already ships | What you need to know |
|---|---|---|
| Elasticsearch | Full-text search: `tsvector`, `tsquery`, `ts_rank`, GIN indexes. Stemming, ranking, phrase matching. | It was there the whole time. |
| Elasticsearch (fuzzy) | `pg_trgm`. Trigram similarity. `LIKE '%term%'` with index support. | Ships stock. |
| RabbitMQ / Redis queue | `SELECT ... FOR UPDATE SKIP LOCKED`. Row locked for transaction duration, other workers skip it. | Commit to release. Understand the transaction semantics or you'll ship a broken queue. |
| External message broker | `LISTEN` / `NOTIFY`. Lightweight event signaling. | Fire-and-forget. No listener connected = message lost. Fine for invalidation, not for guaranteed delivery. |
| Redis (caching) | Materialized views. Precomputed, refreshable, indexable. | Stale between refreshes — but the staleness is bounded and explicit. Your Redis cache is stale too, except you don't know how stale. |
| MongoDB | JSONB. Indexable document storage with GIN and containment operators. | For genuinely polymorphic data. Not a schema-avoidance strategy. |
| External lock service | `pg_advisory_lock`. Distributed mutex, rate limiting, leader election. | Inside the database you're already running. |
| External scheduler | `pg_cron`. Recurring tasks inside the database. | No external scheduler for simple periodic work. |

Not "always use Postgres." But CHECK POSTGRES FIRST. Before adding another system you'll have to monitor, back up, keep consistent, and debug at 3am. Every new system is operational cost you're committing to forever.

This manifesto covers stock Postgres 13+ for application databases. Not OLAP. Not cloud-provider proprietary features. Not DBA runbooks. Not "Postgres vs MySQL." What ships in the box. What you already have. What you refuse to learn.

### The database already has a cache

`shared_buffers`. LRU eviction. Transparent, automatically correct, no invalidation bugs, no consistency problems. You added Redis on top of it. Now you have invalidation bugs and consistency problems.

Did you measure where the bottleneck was first? Check whether `shared_buffers` was sized right? Whether your working set fit in memory?

No. "Everyone uses Redis." So you layered a second cache over a first cache you never configured, never measured, never understood. You replaced something that works with something that breaks and called it an improvement.

### Migrations don't have to be disasters

**Transactional DDL.** Schema changes in transactions. They roll back atomically — step 3 of 5 fails, steps 1 and 2 undo themselves. Your migration framework supports this. You've never used it deliberately.

**`CREATE INDEX CONCURRENTLY`.** Doesn't lock the table. Takes longer. Worth it. You've been locking production tables because you typed `CREATE INDEX` without the one word that prevents the outage.

**Lock level awareness.** `ALTER TABLE ADD COLUMN` with a nullable column or with a non-volatile default is near-instant on PG13+ — no table rewrite. But `ALTER TABLE ADD COLUMN ... NOT NULL` without a default just fails on tables with existing rows. The real rewrite triggers are less obvious: changing column types, adding constraints that require validation. Know your DDL lock levels or keep causing incidents.

### Instruments you're not reading

| Instrument | What it shows you | Your current diagnostic process |
|---|---|---|
| `pg_stat_statements` | Top queries by time, calls, rows — the single most diagnostic tool in Postgres | You've never installed it. Not "haven't checked." Haven't INSTALLED. |
| `pg_stat_user_tables` | Seq scans, dead tuples, last vacuum, last analyze | Nothing. Per-table health data you've never checked. |
| `pg_stat_activity` | Active queries, wait events, connection state — right now | Check it during incidents. Never before. |
| `auto_explain` | Automatic plan logging for queries above a threshold | Manually run EXPLAIN on queries users complain about. |

---

## PICK

Everything in this manifesto ships with stock Postgres 13+. No extensions you need to beg your cloud provider for. No bleeding edge. This is what you already have. What you've always had.

Next Monday you will generate a schema from your ORM models and deploy it without review. Write a `for` loop that makes 200 round trips to render a page. Add an index without checking EXPLAIN. Hold a transaction open during an HTTP call. Add Redis without measuring. All of it, because it's what you've always done.

**A:** Do all of that. Keep going. Comfortable. Familiar. Ignorant. Yours.

**B:** Open the documentation. Read one EXPLAIN plan. Write one CHECK constraint. Run one ANALYZE. Design one schema before writing one line of application code.

Pick.
