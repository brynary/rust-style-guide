# Terrain Map: Topics for a Rust Style-Guide "Skill" for AI Coding Agents

## TL;DR
- This report proposes a **38-topic, 11-category** map for the Rust style-guide skill, sized to the ~40-topic / one-page-per-topic budget, covering everything from the user's seven seed topics (error handling, logging, async, panics, clippy, enums-vs-traits, newtype) to type design, ownership, API design, and tooling.
- The single most consequential authoring decision is the **functional-vs-object-oriented style axis** (the user leans OO "unless unnatural"); it is flagged as the top-level decision point because it cascades into ~10 other topics (iterators-vs-loops, trait design, encapsulation, builder usage).
- I identify **17 explicit decision points** where reputable sources genuinely disagree (e.g., thiserror vs anyhow vs hand-rolled error structs, tracing vs log, unwrap/expect policy, clone-liberally vs borrow-aggressively, pedantic-clippy vs cherry-pick) and lay out the competing options and tradeoffs so they can be resolved up front during drafting.

## Key Findings

1. **The seed topics are well-chosen but unevenly scoped.** "Error handling" and "async" each really need 2–3 pages of distinct sub-topics (philosophy, error types, the `?` operator; runtime choice, async patterns, blocking/cancellation), while "newtype" is a tight one-pager. The map splits the large ones and merges small adjacent ones to fit ~40.

2. **Authoritative sources frequently disagree, and that disagreement is the most useful planning signal.** The official Rust API Guidelines, the Rust Book, and clippy docs are largely descriptive/permissive ("these are guidelines, some firmer than others"). Opinionated sources diverge sharply: Microsoft's Pragmatic Rust Guidelines tell libraries to hand-roll canonical error *structs* (with a `Backtrace`, `is_xxx()` accessors, and a `pub(crate)` `ErrorKind`) and never mention thiserror, whereas most community blogs treat thiserror-for-libraries / anyhow-for-apps as the default. A house style must *choose*.

3. **A clear library-vs-application split runs through many topics** (errors, panics, dependency choice, logging facade vs subscriber, MSRV). The skill should make agents first establish "am I writing a library or a binary?" because the idiomatic answer flips for several topics. Microsoft makes this split explicit: M-ERRORS-CANONICAL-STRUCTS (libraries, marked stable v1.0) vs M-APP-ERROR ("Applications... may use anyhow, eyre or similar," marked draft v0.1).

4. **Some ecosystem facts are now settled and should be encoded as defaults, not decision points.** async-std has been officially discontinued by maintainer Josh Triplett — RustSec advisory RUSTSEC-2025-0052 (dated 2025-08-24) states "The async-std has been discontinued. Alternatives: smol," with final release v1.13.2; corrode.dev dates the discontinuation to March 1, 2025. So the runtime decision is effectively tokio (default) vs smol (minimal/embedded) vs specialized (glommio/monoio). tracing has become the de-facto standard for new instrumentation. rustfmt defaults are near-universal: per rustfmt's official Configurations.md, `max_width` "Default value: 100" (Stable: Yes) and `tab_spaces` "Default value: 4" (Stable: Yes).

5. **A skill is itself an AI-consumption artifact, and Microsoft's M-DESIGN-FOR-AI guideline is directly relevant.** The Pragmatic Rust Guidelines' AI section states: "Use Strong Types. Avoid primitive obsession by using strong types with strict well-documented semantics. Follow C-NEWTYPE," and "The more your APIs... look and feel like the majority of Rust code in the world, the better it is for AI." The style guide should bias toward strong types (newtypes, enums, typestate) precisely because the compiler can then backstop an agent's lack of understanding.

---

## Details: The Categorized Topic Map

Each topic below is scoped to ~one page. Topics are tagged **[SEED]** (user-specified), **[ESSENTIAL]**, or **[OPTIONAL]** for prioritization, and **⚖️ DECISION POINT** where a convention must be chosen.

### Category A — Foundations & Philosophy (3 topics)

1. **House Style Overview & the OO-vs-Functional Axis** — [ESSENTIAL] ⚖️ **DECISION POINT (the big one).** Frames the whole guide: when to prefer struct-centric/method-based code with encapsulation vs iterator/combinator/immutable pipelines. Establishes the default posture (user leans OO unless unnatural) and the "functional core, imperative/OO shell" compromise that corrode.dev and others describe. Cross-references every topic this touches.
2. **Library vs Application vs Binary Conventions** — [ESSENTIAL]. A decision tree agents run first: error strategy, panic tolerance, dependency latitude, and API discipline all differ. Library = strict; application = pragmatic.
3. **Designing Rust for AI Agents & Compiler-Backstopped Code** — [OPTIONAL]. Encodes Microsoft's M-DESIGN-FOR-AI: strong types, thorough docs, testable APIs so the compiler catches agent mistakes. Could be merged into #1 if space is tight.

### Category B — Error Handling (5 topics)

4. **Error-Handling Philosophy: Result vs Panic** — [SEED][ESSENTIAL]. When failure is "expected/recoverable" (return `Result`) vs a "broken invariant/contract" (panic), per the Rust Book's "To panic! or Not to panic!" framing.
5. **Error Types & Libraries** — [SEED][ESSENTIAL] ⚖️ **DECISION POINT.** thiserror vs anyhow/eyre vs snafu vs hand-rolled structs. Lay out: thiserror (library structured enums, low boilerplate), anyhow/eyre (application type-erased), snafu (context selectors, module-level errors), and Microsoft's contrarian M-ERRORS-CANONICAL-STRUCTS position (verbatim: "Errors should be a situation-specific `struct` that contain a `Backtrace`, a possible upstream error cause, and helper methods") which exposes `is_xxx()` accessors over a `pub(crate)` `ErrorKind` rather than a public enum, and does not mention thiserror at all. Must pick the house default for each of library/app.
6. **The `?` Operator, Error Conversion & Context** — [SEED][ESSENTIAL]. `?` with `From`/`Into` conversions, `#[from]`, adding context (anyhow's `.context()`, snafu selectors), the `Box<dyn Error>` escape hatch and when it's acceptable.
7. **Custom Error Design: enums vs structs, `#[non_exhaustive]`, naming** — [ESSENTIAL]. Single `Error` vs domain-specific (`ParseError`, `ConfigError`), avoiding a god-enum, `#[non_exhaustive]` for forward-compat, Display/Error trait impls, "Errors" doc sections.
8. **Fallible Constructors & Validation at the Boundary** — [OPTIONAL]. `new()` vs `try_new()`, validating into newtypes (`TryFrom<String> for Password`), parse-don't-validate. Could merge with #25 (constructors).

### Category C — Panics, Assertions & Invariants (2 topics)

9. **unwrap/expect Policy & When Panicking Is Acceptable** — [SEED][ESSENTIAL] ⚖️ **DECISION POINT.** The spectrum from "ban unwrap, lint with `clippy::unwrap_used`" (thecodedmessage) to "unwrap is a deliberate assertion tool" (Cloudflare-outage discourse). House rule needed: prefer `expect` with invariant-describing messages; where unwrap is tolerated (tests, provably-non-empty, regex constants, mutex lock).
10. **Assertions, Invariants & `unreachable!`/`todo!`/`debug_assert!`** — [ESSENTIAL]. When to use `assert!`/`debug_assert!`/`unreachable!`, contract enforcement, fail-fast at startup for missing config.

### Category D — Type & API Design (6 topics)

11. **Enums vs Trait Objects vs Generics (Polymorphism)** — [SEED][ESSENTIAL] ⚖️ **DECISION POINT.** Closed set you own → enum + match (static dispatch, no vtable); open/extensible set defined by callers → `dyn Trait`; generics/`impl Trait` for static dispatch with monomorphization. The decisive question: "who defines the concrete types?" The performance gap can be large: per the enum_dispatch docs.rs benchmark (homogeneous Vec of 1024 trait objects), `boxdyn` ran 5,900,191 ns/iter vs `enumdispatch` 479,630 ns/iter — "a result that is 10 times faster than the closest alternative, and almost 12 times faster than the best technique."
12. **The Newtype Pattern** — [SEED][ESSENTIAL]. Single-field tuple structs for type safety (UserId vs AccountId), units, orphan-rule workarounds, restricting API surface; when to impl `Deref` (smart pointers yes; invariant-bearing newtypes no, per C-DEREF).
13. **Typestate & Phantom Types** — [OPTIONAL]. Compile-time state machines, `PhantomData`, typestate builders that make invalid states unrepresentable. Advanced; mark optional.
14. **Builder Pattern & Constructors** — [ESSENTIAL]. When to use builders (many optional params), `new()` conventions, typestate builders enforcing required fields, `Default`.
15. **Trait Design: bounds, associated types, sealed traits, blanket impls** — [ESSENTIAL]. `where` clauses, `impl Trait` in arg/return position, associated types vs generic params, sealed-trait pattern, object safety constraints.
16. **Deriving vs Hand-Implementing Traits** — [ESSENTIAL] ⚖️ **DECISION POINT.** Derive-heavy vs explicit. Which of Debug/Clone/Copy/PartialEq/Eq/Hash/Ord/Default to derive routinely; when manual impls are warranted (custom Display always manual; Hash/Eq must agree).

### Category E — Ownership, Borrowing & Conversions (4 topics)

17. **Clone vs Borrow & Function-Signature Conventions** — [ESSENTIAL] ⚖️ **DECISION POINT.** "Clone liberally for clarity" vs "borrow aggressively for performance." Accept `&str`/`&[T]` in params, return owned; `&self` vs `self`; when `.clone()` is acceptable.
18. **`&str` vs `String` vs `impl AsRef<str>` vs `Cow`** — [ESSENTIAL]. The classic param-type decision: `&str` for simplicity, generics (`AsRef`/`Into`) for flexibility, `Cow` for sometimes-allocate, `Borrow` for map keys. Tradeoffs of signature complexity.
19. **Conversions: From/Into/TryFrom/TryInto, AsRef, Deref** — [ESSENTIAL]. Implement `From` (not `Into`), `TryFrom` for fallible, `AsRef`/`AsMut` for cheap ref conversion, Deref-coercion pitfalls (don't simulate inheritance). Also the home for numeric conversions (`as` truncates; `From` for lossless widening; `TryFrom` for fallible narrowing) if numeric overflow isn't promoted to its own topic.
20. **Lifetimes & Elision Conventions** — [OPTIONAL]. When to name lifetimes, rely on elision, avoid gratuitous explicit lifetimes; lifetime-in-struct guidance.

### Category F — Idiomatic Constructs (4 topics)

21. **Iterators, Combinators & Closures** — [ESSENTIAL] ⚖️ **DECISION POINT** (links to #1). Iterator chains vs explicit loops, `collect` patterns, custom iterators, lazy evaluation, closure capture (`move`), when a `for` loop is clearer than `fold`.
22. **Pattern Matching: match vs if-let vs let-else** — [ESSENTIAL]. Exhaustiveness, `let-else` for early return, match guards, `@` bindings, when `if let` beats `match`.
23. **Option Handling** — [ESSENTIAL]. Option combinators (`map`/`and_then`/`unwrap_or_else`), `?` on Option, `Option` vs `Result`, `ok_or`, avoiding null-object antipatterns.
24. **Collections & Data-Structure Choice** — [OPTIONAL]. Vec vs VecDeque, HashMap vs BTreeMap (ordering/determinism), capacity hints, when SmallVec/arrayvec earn their dependency.

### Category G — Concurrency & Async (4 topics)

25. **Async Runtime Choice & When to Use Async** — [SEED][ESSENTIAL] ⚖️ **DECISION POINT.** tokio (default, dominant ecosystem) vs smol (minimal) vs specialized; async-std is discontinued (RUSTSEC-2025-0052), so it is not a candidate for new code. When sync threads are simpler than async. Libraries should avoid hard-coding a runtime.
26. **Async Patterns: async traits, Send bounds, cancellation, blocking** — [SEED][ESSENTIAL]. `async fn` in traits and Send-bound issues, `spawn_blocking` for blocking calls, cancellation safety in `select!`, yield points for long CPU work (Microsoft M-YIELD-POINTS).
27. **Concurrency Primitives: threads, channels, Arc/Mutex/RwLock (+ rayon)** — [ESSENTIAL]. `Arc<Mutex<T>>` as the default shared-state pattern, RwLock for read-heavy, channels for message-passing, std vs tokio sync types, deadlock/lock-ordering discipline, and `rayon::par_iter` for CPU-bound data parallelism. (rayon merged in here to free a slot for Logging — see #28.)
28. **Logging & Observability** — [SEED][ESSENTIAL] ⚖️ **DECISION POINT.** tracing vs log: tracing for structured spans, async-aware instrumentation, `#[instrument]`, OpenTelemetry integration; `log` facade for ubiquity and lightweight libraries. Structured fields (never concatenate values into messages), log levels (TRACE/DEBUG dev, INFO+ prod), and never logging secrets/PII. Recommended default: tracing for apps/services, `log` facade for libraries.

### Category H — Tooling & Linting (3 topics)

29. **Clippy Configuration & Lint Policy** — [SEED][ESSENTIAL] ⚖️ **DECISION POINT.** Enable pedantic group wholesale vs cherry-pick; correctness=deny; `unwrap_used`/`expect_used`/`dbg_macro`/`todo` policy; configure via `[lints]` in Cargo.toml vs source attributes; prefer `#[expect]` over `#[allow]` for lint overrides (Microsoft M-LINT-OVERRIDE-EXPECT: "Use #[expect] instead of #[allow] for lint overrides").
30. **rustfmt & CI Enforcement** — [ESSENTIAL]. Use defaults (`max_width` 100, `tab_spaces` 4 — both stable) unless strong reason; `group_imports`/`imports_granularity` choices (unstable); `cargo fmt --check` and `cargo clippy -- -D warnings` in CI.
31. **Cargo.toml, Features, Profiles & Workspaces** — [ESSENTIAL]. Additive feature flags, workspace lints/deps, profile tuning (debug symbols for bench), workspace structure.

### Category I — Documentation & Testing (3 topics)

32. **Documentation Conventions** — [ESSENTIAL]. `///` and `//!`, canonical sections (Examples/Errors/Panics/Safety), runnable examples, crate/module-level docs, `#[doc(inline)]` for re-exports. Summary sentence one line ≈15 words (Microsoft M-FIRST-DOC-SENTENCE: "First Sentence is One Line; Approx. 15 Words").
33. **Testing Conventions** — [ESSENTIAL] ⚖️ **DECISION POINT.** Unit (in-module `#[cfg(test)]`) vs integration (`tests/`), naming, when to add proptest/quickcheck, insta snapshots, mockall; cargo-nextest vs cargo test.
34. **Doctests & Examples** — [OPTIONAL]. Doctest conventions, hidden `#` lines, `?`-in-doctests, `examples/` directory. Could merge into #32.

### Category J — Project Structure & Public Interface (3 topics)

35. **Module Organization & Visibility** — [ESSENTIAL] ⚖️ **DECISION POINT.** `pub` vs `pub(crate)` vs private; module-level (not type-level) encapsulation; whether to allow complex `pub(in path)` (PingCAP discourages); file layout (`mod.rs` vs `foo.rs`).
36. **Re-exports, Prelude & Public API Surface** — [ESSENTIAL]. `pub use` to flatten API, when a `prelude` module is justified, avoiding glob re-exports, keeping a minimal coherent public surface.
37. **API Stability: semver, `#[non_exhaustive]`, `#[must_use]`** — [ESSENTIAL]. What counts as breaking (per the Cargo semver reference), `#[non_exhaustive]` on enums/structs, `#[must_use]` on Result-like returns, sealed traits, cargo-semver-checks in CI.

### Category K — Naming & Cross-Cutting Conventions (1 topic)

38. **Naming Conventions** — [ESSENTIAL]. Types/traits `UpperCamelCase`, fns/vars `snake_case`, consts `SCREAMING_SNAKE_CASE`, getters without `get_` prefix (C-GETTER), conversion-method naming (`as_`/`to_`/`into_`), iterator-method naming.

### Topics Folded In or Deferred (to stay ≤40)
- **Unsafe code** — folded into a note under #15/#37; full treatment is optional. *If the codebase uses unsafe, promote to a dedicated topic* (Microsoft M-UNSAFE: valid reasons are novel abstractions, performance-after-benchmarking, FFI; document safety invariants; pass Miri). This is the most defensible *addition* if you go to 39–40 topics.
- **Macros (declarative vs procedural)** — strong candidate for topic #39: when a function/generic suffices over a macro, prefer derive over proc-macro for per-field code (per Effective Rust Item 28), hygiene, `$crate`.
- **Numeric types & overflow** (checked/wrapping/saturating, `as` vs `TryFrom`) — folded into #19 (conversions); promote to #40 if arithmetic-heavy.
- **String handling beyond params** (byte strings, formatting, building) — folded into #18.
- **Interior mutability (Cell/RefCell)** — folded into #27.
- **RAII/Drop/scope guards** — folded into #14 or #27.
- **const/static/const-generics** — optional; fold into #31 or drop.
- **Serialization (serde)** — fold into #31/dependency guidance unless serde-heavy.
- **Config/secrets/env** — application-only; fold into #2.
- **Comments/TODO conventions** — fold into #32.

---

## Consolidated Decision Points (resolve these before drafting)

These are the choices where reasonable Rust engineers disagree and the house style must take a position. Ordered roughly by blast radius.

1. **Functional vs Object-Oriented default style** (Topic 1). OO/struct-centric (user's lean) vs functional/iterator-pipeline. *Tradeoff:* OO gives encapsulation, familiar mental model, easier incremental mutation; functional gives composability, fewer intermediate-state bugs, idiomatic iterator ergonomics. *Recommended framing:* "functional core, OO/imperative shell" with OO as the tie-breaker.
2. **Library error strategy** (Topic 5). thiserror enum vs hand-rolled canonical struct (Microsoft M-ERRORS-CANONICAL-STRUCTS) vs snafu. *Tradeoff:* thiserror = least boilerplate, ecosystem-standard; canonical struct = better forward-compat & hidden internals but more code; snafu = best context/scaling but verbose.
3. **Application error strategy** (Topic 5). anyhow vs eyre vs the same library types (Microsoft M-APP-ERROR permits anyhow/eyre for apps but mandates canonical structs for libraries). *Tradeoff:* type-erasure convenience vs typed handling.
4. **unwrap/expect policy** (Topic 9). Ban-and-lint vs allow-as-assertion. *Tradeoff:* safety/explicitness vs ergonomics.
5. **Polymorphism default** (Topic 11). Enum-first vs trait-object-first. *Tradeoff:* performance (up to ~10–12x in the enum_dispatch benchmark) & closed-set clarity vs extensibility.
6. **Derive-heavy vs explicit trait impls** (Topic 16).
7. **Clone-liberally vs borrow-aggressively** (Topic 17). Readability/velocity vs allocation cost.
8. **Param-type convention** (Topic 18). Always `&str`/concrete vs generic `impl AsRef`/`Into`. *Tradeoff:* signature simplicity vs caller flexibility.
9. **Iterators vs explicit loops** (Topic 21) — sub-axis of #1.
10. **Async runtime** (Topic 25). tokio default vs smol vs runtime-agnostic libraries.
11. **Logging/observability stack** (Topic 28). tracing vs log. *Tradeoff:* tracing = structured spans, async-aware, OpenTelemetry; log = lightweight facade, ubiquitous. *Recommended default:* tracing for applications/services, `log` facade for libraries.
12. **Clippy strictness** (Topic 29). Pedantic-wholesale vs cherry-pick; which restriction lints to deny.
13. **Lint configuration location** (Topic 29/31). `[lints]` table in Cargo.toml vs source attributes (and `#[expect]` over `#[allow]`).
14. **Test framework additions** (Topic 33). Plain `#[test]` only vs proptest/insta/mockall/nextest adoption thresholds.
15. **Visibility granularity** (Topic 35). Allow `pub(in path)` vs restrict to `pub`/`pub(crate)`/private.
16. **MSRV policy & dependency latitude** (Topics 2/31). How conservative; minimal-versions; vetting new deps.
17. **`Rc::clone(&x)` explicit form vs `x.clone()`** (Topic 17 sub-point) — small but worth a house ruling.

---

## Recommendations (staged, with thresholds)

**Stage 1 — Lock the philosophy (do first).** Resolve Decision Points 1, 2, 3, 4 (style axis + error strategy + panic policy). These four cascade into the most topics; writing any other page before they're settled risks rework. *Threshold to proceed:* a one-paragraph ruling on each, with the library/application split made explicit.

**Stage 2 — Draft the ESSENTIAL core (~26 topics).** Write Categories B, C, D, E, H, I, J first; they're the highest-value and least speculative. Encode settled facts as defaults (tokio, tracing, rustfmt defaults at 100/4, correctness=deny). *Threshold:* every ESSENTIAL topic has a page with at least one ✅/❌ code example and an explicit house ruling on any embedded decision point.

**Stage 3 — Add OPTIONAL/advanced topics to taste (typestate, lifetimes, collections, doctests, macros).** Add only those matching the target codebase's actual patterns. *Threshold to include unsafe/macros as full topics:* the codebase contains hand-written `unsafe` or non-trivial `macro_rules!`/proc-macros.

**Stage 4 — Validate the cap.** The map above sits at **38 topics** with Logging promoted (#28) and rayon merged into concurrency (#27). If you go to 39–40, promote in this order: **Macros**, then **Unsafe**, then **Numeric/Overflow**. If you must cut below 38, apply the "Folded In" merges in priority order (numeric→conversions, strings→params, interior-mutability→concurrency, RAII→builders).

**Benchmarks that would change the plan:**
- If the target is primarily **libraries**, promote API-stability (#37), error-struct discipline (#5/#7), and docs (#32) to the front and tighten unwrap policy to "deny."
- If primarily **services/apps**, promote async (Cat G), logging/observability (#28), and config/secrets, and relax error types to anyhow/eyre.
- If the codebase is **performance-critical**, promote allocation/perf, enum-dispatch over trait objects, and `Cow`/borrow-aggressive conventions.

---

## Caveats

- **Source quality varies.** The most-cited "vs" comparisons (thiserror/anyhow/snafu, tokio/smol, tracing/log) come heavily from blog posts and aggregators; I cross-checked against primary sources (clippy docs, rustfmt Configurations.md, the Cargo semver reference, Microsoft's Pragmatic Rust Guidelines, the Rust Book) where possible. Treat blog consensus as signal, not gospel.
- **Microsoft's Pragmatic Rust Guidelines are opinionated and not universal.** Their canonical-error-struct stance (M-ERRORS-CANONICAL-STRUCTS, v1.0) and complete absence of any thiserror recommendation diverge from mainstream community practice; I present it as one pole of a decision point, not the answer. Note also that M-APP-ERROR is still early-draft (v0.1).
- **Ecosystem drift.** async-std's discontinuation is confirmed (RUSTSEC-2025-0052, 2025-08-24; final release v1.13.2); runtime/observability recommendations can shift. The skill should note its "as-of" date and the volatile topics (async, observability, lint groups).
- **The ~40 cap forces real cuts.** Several legitimate topics (numeric overflow, interior mutability, RAII, const generics, serde) are folded into neighbors rather than given their own page; if any is central to the target codebase, it deserves promotion.
- **This is a terrain map, not the guide.** No actual style rules are authored here beyond the minimum needed to characterize each decision point; the rulings in "Decision Points" are recommended starting positions, not finished policy.