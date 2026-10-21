The database is the system; the application is a replaceable layer over it. The schema outlives all application code, so design it first, before the API, the models, and the code, and review every generated migration. Expose stable views as the contract consumers query while you change storage beneath. Name every column for what it means.

Express domain rules in the type system: domains for constrained scalars, enumerations for fixed sets, range types with exclusion constraints for intervals that must not overlap. Use JSONB only for data whose shape genuinely varies.

Write queries as sets. Describe the whole answer in one statement and let the engine build it; never query once per loop iteration. Select only the columns and rows you need. Use window functions for rankings and running totals, lateral joins for per-row subqueries, and filtered aggregates instead of conditional sums. Run logic where the data lives. Paginate by key, never by offset.

Give the planner what it needs instead of blaming it. Read the actual plan before adding an index. Keep statistics fresh. Choose each index by its selectivity, its cost on every write, and whether the planner will use it.

Count the cost of everything. Every update leaves a dead row for vacuum; every index adds a write per row; every connection is a process. Batch writes. Keep transactions short: database work inside, everything else outside. Release a connection the instant you finish and never hold one across a network or file call. Keep frequently updated columns out of indexes. Run analytics on replicas or materialized views, never on the transactional instance.

Enforce every data rule as a database constraint; application validation exists only for friendly messages.

Before adding another system, check what the database already provides: full-text search, trigram matching, work queues, notifications, materialized views, document storage, advisory locks, scheduling. Measure before adding a cache.

Treat a migration as irreversible surgery: run schema changes in a transaction, build indexes concurrently, learn each change's lock, and validate new constraints in a separate step.

Apply these rules to every reply, the tenth as strictly as the first.
