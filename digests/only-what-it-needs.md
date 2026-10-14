Take in what you use. Expose what must go out.

Whatever crosses a boundary is coupling. On the taking end, reach no further than the body uses; on the giving end, reveal nothing a caller does not need.

Widen no parameter for a field you expect to read later; a shared pointer is a global with a parameter name. Unused reach is coupling for nothing: cut it and keep the crossing the body needs.

Read and write only what enters through the function's arguments: no global, no shared handle, no generator outside the signature. Call no function that reaches outside its own signature, since the caller inherits the callee's reach.

Take a parameter no wider than the fields the body reads. Require no guarantee stronger than the body uses.

Give each difficult or likely-to-change decision a module that hides it, named by recorded variation in use, not by forecast. Keep values that must agree, or a structure kept in step by hand across functions, in one unit only a few functions can change.

Reveal through an interface only what callers need. The module-level case, that revealing more forecloses whole classes of systems, holds for large systems; carry it no wider.

Hide by cutting code you are writing anyway; add nothing for it: no variant, no interface with one implementation, no unit for an unasked requirement, no base class. "Almost anything can change" is not a trigger; it hides everything and names nothing. State the cut's cost and carry it on purpose. Where there is no invariant and no decision to hide, use public data, a plain struct, and no class.

Before you ship, understand each function from its own text and the signatures it calls, opening nothing else; name in one line the decision each module or class hides; check every public member against callers' needs.

Apply these rules to every reply, the tenth as strictly as the first: ask of every function what the body reads, what the signature lets in, and what the interface reveals; if one check fails, rewrite the whole reply, not the line.
