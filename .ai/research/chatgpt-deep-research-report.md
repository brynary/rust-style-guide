# Rust Style Guide Skill Terrain Map

## What this skill should do

A strong Rust style guide for AI coding agents should not try to replace the language reference or re-teach Rust. It should compress the most decision-heavy parts of idiomatic Rust into explicit defaults, exceptions, and examples that an agent can follow mechanically. That matters because the official guidance is both strong and fragmented: the Rust Style Guide is primarily about formatting and is the reference point for rustfmt’s default behavior; the Rust API Guidelines cover naming, interoperability, type safety, flexibility, dependability, future-proofing, and documentation; Cargo documentation covers workspaces, features, and `rust-version`; Clippy and rustc define lint behavior; Tokio and tracing documentation cover async runtime, cancellation, and diagnostics. A good agent skill should consolidate those sources into one opinionated rulebook. citeturn22view0turn20search2turn24view0turn29view0turn25view3

The most important design choice is that each page should answer one practical question an agent encounters while coding: “Should this be an enum or a trait?”, “Is `unwrap()` acceptable here?”, “Should I use `tracing` or `log`?”, “Should this async code use `spawn_blocking`?”, and so on. Rust’s own documentation repeatedly emphasizes patterns that are explicit, type-driven, and example-backed: the style guide prioritizes readability and diff-friendliness; the API guidelines push semantic types, builders, and documentation of `Errors`, `Panics`, and `Safety`; rustdoc guidance recommends a short summary, a deeper explanation, and copy-pasteable examples for each public item. citeturn22view1turn18view0turn33view0

My recommendation is to scope the first version of the skill to **40 markdown pages**. That is enough to cover the core terrain without turning the skill into a mini-book, and it maps cleanly onto the major seams already present in the official Rust materials and the async/tooling ecosystem. citeturn22view0turn20search2turn25view3

## Preference choices to settle before drafting

These are the highest-leverage choices to resolve first, because they will cascade through many pages of the eventual skill.

| Decision | Real options | Suggested default for your skill |
|---|---|---|
| Edition baseline | Rust 2021 vs Rust 2024 | **Target Rust 2024** unless you have legacy constraints. Rust 2024 is the current edition, it implies resolver `3`, and rustfmt now supports explicit `style_edition`, which helps keep editor and CI formatting aligned. citeturn23view0turn23view1turn23view2 |
| MSRV policy | “latest stable only,” “N-2,” or explicit long-tail support | **Declare a `rust-version` and write a plain-language MSRV policy.** Cargo uses `rust-version` for diagnostics and tooling, and Clippy can use it for MSRV-sensitive linting. citeturn24view0turn29view1 |
| Overall style bias | Functional-heavy Rust vs object-oriented-leaning Rust | **Bias toward encapsulated structs with methods, builders, and clear receivers**, because Rust supports OOP-style encapsulation and methods, but still use iterator/functional style when it is materially clearer or removes unnecessary mutation. That fits both Rust’s multi-paradigm reality and your stated preference. citeturn30view0turn36view1turn36view0 |
| Polymorphism default | Enums-first, generics/traits-first, or `dyn Trait`-heavy | **Closed sets → enums; open extension points → traits; runtime heterogeneity only when you really need it → trait objects.** This matches the API guideline tradeoffs around object safety and the language’s strengths. citeturn21view0turn30view1turn7search3 |
| Error style | Typed errors everywhere vs easy erased errors everywhere | **Typed errors in libraries, erased/reporting-focused errors at the app boundary.** `thiserror` is explicitly suited to library-defined errors; `anyhow` is explicitly positioned as common in application code; `miette` is for richer top-level diagnostics. citeturn31view1turn31view0turn31view2 |
| Panic policy | Liberal use of `unwrap`/`expect` vs very narrow panic surface | **Result-by-default; panic only for bugs, broken invariants, and true contract violations.** Examples, tests, prototypes, and logically impossible states can still justify `expect` with a reason. citeturn37view0turn37view1 |
| Logging stack | `log` facade, `tracing`, or mixed | **Make this an explicit policy page.** For broad reusable libraries, `log` remains the conventional facade; for async services and internal codebases, `tracing` is often the better default because spans and structured async-aware diagnostics are first-class. citeturn25view0turn25view1turn25view3 |
| Async portability | Tokio-first vs runtime-agnostic | **Choose consciously.** If your agents mostly write service code, Tokio-first will produce more concrete and reliable output. If you need public libraries, runtime-agnostic surfaces may be worth the extra design constraints. Tokio docs are explicit about runtime-specific task semantics and lifecycle behavior. citeturn26view5turn26view0 |
| Lint strictness | Minimal linting vs curated strictness vs blanket pedantic | **Curated strictness.** Turn on a strong baseline, but avoid blindly denying every pedantic lint; Clippy itself warns that `clippy::pedantic` is aggressive and can produce false positives. citeturn29view0turn29view1turn29view2 |
| Public API stability posture | Expose fields and extension points freely vs keep room to evolve | **Prefer private fields, sealed traits where appropriate, and careful feature-flag discipline.** Those choices preserve invariants and reduce accidental semver commitments. citeturn14view2turn9search1turn24view1 |
| Verification baseline | `fmt` only vs full CI gate | **Require at least `cargo fmt`, `cargo clippy`, `cargo test`, and doctests.** Cargo and rustdoc both treat doctests as part of the normal testing surface, and rustfmt/style-edition mismatches can otherwise create noisy churn. citeturn29view5turn29view3turn23view1 |

## Proposed topic map

The tables below are the terrain map I would use for the skill. They are organized into five clusters and total **40 pages**.

### Foundations and tooling

This cluster is grounded mainly in the Rust Style Guide, rustfmt, Cargo, Clippy, rustc lint behavior, and the API Guidelines’ sections on naming and documentation. It is where the skill establishes repository-wide defaults that agents can apply mechanically. citeturn22view0turn23view1turn24view0turn24view1turn29view0turn29view1turn17view0turn18view0

| Topic page | What the page should settle | Key preference choices |
|---|---|---|
| Rust edition and MSRV policy | Which edition agents target, whether `edition = "2024"` is mandatory, how `rust-version` is declared and updated | 2024 vs 2021; latest-stable-only vs explicit MSRV window |
| rustfmt, style edition, and formatting exceptions | Default formatting stance, whether to stick close to rustfmt defaults, and when `#[rustfmt::skip]` is allowed | “Rustfmt default almost always” vs custom config-heavy style |
| rustc and Clippy lint baseline | Mandatory lint groups, deny vs warn policy, how local allowances are documented | Curated deny list vs aggressive pedantic posture |
| Cargo workspace and crate boundaries | When to split into crates, how to structure workspaces, inheritance via `[workspace.*]`, resolver expectations | Monorepo workspace-by-default vs single-crate unless forced |
| Module layout, visibility, and re-exports | File/module layout, `pub` vs `pub(crate)` vs `pub(super)`, where facades live | Deep internal modules + public facade vs flatter module exposure |
| Naming conventions, imports, and public prelude policy | Case conventions, acronym style, import grouping, whether to define a public prelude | Explicit imports everywhere vs curated prelude |
| Documentation style, rustdoc sections, and examples | Required doc structure, `Errors`/`Panics`/`Safety` sections, example expectations | Doc every public item vs doc only non-obvious items |
| Feature flags, dependency policy, and Cargo metadata | Additive feature policy, default-features stance, dependency hygiene, metadata minimums | Conservative feature set vs broad optional integrations |

### API and type design

This cluster should be anchored in the API Guidelines’ sections on interoperability, type safety, predictability, flexibility, and future-proofing, plus the Rust Book’s treatment of traits and Rust’s object-oriented capabilities. This is the heart of “idiomatic Rust API shape.” citeturn14view4turn16view0turn14view3turn21view0turn14view2turn30view0turn30view1

| Topic page | What the page should settle | Key preference choices |
|---|---|---|
| Struct design and private fields | Whether fields are public by default, how invariants are protected, when plain data structs are acceptable | Encapsulated structs by default vs data-first public structs |
| Constructors and builder pattern | When to use `new`, `with_*`, `from_*`, and when to introduce builders | Lightweight constructors vs builders for most multi-option types |
| Enums vs traits vs trait objects | The primary rule for modeling variation and extensibility | Enums for closed worlds, traits for extensibility, `dyn` only when truly needed |
| Newtype pattern and semantic wrappers | When to wrap primitive or foreign types for domain meaning, invariants, or API hiding | Aggressive semantic wrappers vs use only at clear boundaries |
| Ownership, borrowing, and clone policy in signatures | Whether functions take ownership, borrow, or accept `AsRef`/`IntoIterator` | Caller-controlled ownership, minimal implicit clones |
| Generics, trait bounds, and `impl Trait` | How generic to make APIs, when generic signatures become too noisy, and when object safety matters | Broad generics by default vs concrete signatures unless reuse demands more |
| Common trait implementations and derive policy | Which traits to derive or implement eagerly on public types | “Implement common traits early” vs minimalist impl surface |
| Conversion traits, getters, and method naming | `From`/`TryFrom`/`AsRef`, `as_` vs `to_` vs `into_`, getter names without `get_` | Strict standard-trait and naming adherence vs local conventions |
| Public API evolution: sealed traits and `non_exhaustive` | How much future-proofing to build into public interfaces up front | Seal aggressively vs expose more downstream implementation freedom |

### Errors, diagnostics, and safety

Rust’s official documentation is unusually explicit about error handling and safety contracts. The API Guidelines require `Errors`, `Panics`, and `Safety` sections; the Book recommends `Result` as the default for fallible APIs; `panic!` is for detected bugs; `thiserror` is public-API-neutral for typed errors; `anyhow` is explicitly framed as common in application code; `miette` is for richer reporting; and the Book plus Nomicon both stress small unsafe blocks and safe abstractions with private invariants. citeturn18view0turn37view0turn37view1turn31view1turn31view0turn31view2turn28view0turn28view1

| Topic page | What the page should settle | Key preference choices |
|---|---|---|
| Error taxonomy and layer boundaries | Operational vs domain vs programming errors; what belongs in types versus logs | Fine-grained domain errors vs coarser top-level categories |
| Library errors vs application errors | Whether library crates must return typed errors and where erased/report-style errors are permitted | Library typed errors, app-level erasure/reporting |
| Error propagation, context, and display messages | Mandatory use of `?`, context attachment style, and message-writing conventions | Sparse messages vs rich layered context |
| Panic policy and contract violations | Accepted uses of `panic!`, `unwrap`, and `expect`; required justification patterns | Very narrow panic surface vs pragmatic bootstrapping exceptions |
| Validation, invariants, and assertions | Encode with types vs runtime validation; `assert!` vs `debug_assert!`; constructor validation | Type-level enforcement first vs runtime validation first |
| Logging vs tracing | Which diagnostic stack to use, how fields are named, and how much structure is required | `tracing`-first for services vs `log`-facade-first for general libraries |
| Backtraces and user-facing diagnostics | When to capture backtraces, whether top-level binaries standardize on `miette` or similar | Plain stderr errors vs richer end-user diagnostics |
| Unsafe code boundaries and safety documentation | Whether unsafe is allowed at all, required review language, module privacy rules, safety comments | “Unsafe only behind narrow safe abstractions” vs broader tolerance |

### Async and concurrency

If your agents will touch modern service code, this cluster is essential. Tokio’s docs are concrete about task lifecycle, shutdown, `spawn_blocking`, cancellation, and `select!` cancellation safety; tracing is designed for async-aware scoped diagnostics; and the standard library docs on `Arc`, `Mutex`, and one-time initialization help define the sync side of the style guide. citeturn26view5turn26view0turn26view1turn26view2turn26view3turn26view4turn25view3turn27view0turn27view1turn27view2

| Topic page | What the page should settle | Key preference choices |
|---|---|---|
| Async runtime policy | Whether the codebase is Tokio-specific, runtime-agnostic, or mixed | Tokio-first vs portability-first |
| Async API design and sync/async split | Whether crates expose sync and async variants, async traits, or runtime-specific entry points | One async surface vs duplicated sync/async APIs |
| Spawned tasks, `JoinHandle` use, and task lifecycle | When to spawn, whether un-awaited tasks are allowed, ownership expectations, abort behavior | Structured concurrency bias vs freer background spawning |
| Cancellation and graceful shutdown | Token-based cancellation, shutdown sequencing, and whether agents must build graceful termination paths | Best-effort shutdown vs always-graceful-by-design |
| Blocking work in async contexts | Rules for `spawn_blocking`, dedicated threads, and prohibition on blocking within async tasks or destructors | Strict “never block in async” vs pragmatic exceptions |
| Shared state vs channels | When to choose message passing instead of shared mutable state | Channels/query tasks first vs guarded shared state when simpler |
| Locking, `Arc`, and interior mutability across tasks | When `Arc<Mutex<T>>` is acceptable, when `RwLock` is worth it, and mutation patterns under sharing | Conservative lock usage vs pragmatic `Arc<Mutex<T>>` default |
| Global initialization and one-time state | Whether to standardize on `OnceLock`/`LazyLock`, and how much global state is acceptable | Minimal globals vs controlled one-time initialized singletons |
| `select!`, timeouts, and cancellation safety | Required timeout patterns, `else` branches, and avoidance of non-cancel-safe operations in loops | Mandatory timeouts and explicit `else` vs looser style |

### Implementation, testing, and release

This cluster translates Rust’s language features into day-to-day style decisions. The Book explicitly presents both control-flow shorthand (`if let`, `let...else`) and functional features like iterators and closures; it also shows iterator-based rewrites that remove clones and mutation. Meanwhile, Cargo and rustdoc make unit, integration, and documentation tests part of the normal workflow, and community tools like proptest, insta, and criterion provide mature extended verification options. citeturn34search3turn34search0turn36view1turn36view0turn36view2turn29view4turn29view5turn29view3turn11search0turn11search1turn11search2

| Topic page | What the page should settle | Key preference choices |
|---|---|---|
| Control-flow idioms: `match`, `if let`, `let...else` | When to prefer exhaustive `match` vs concise conditional forms | Exhaustiveness/readability first vs concise happy-path code |
| Iterator chains, closures, and explicit loops | When iterator style is preferred and when a `for` loop is clearer | Clear loop by default vs chain adapters when naturally expressive |
| Object-oriented bias vs free functions and functional pipelines | Whether behavior should usually live in `impl` blocks on domain types | Method-centric OO-leaning style vs many free helper functions |
| Mutation style and caller-controlled ownership | When to mutate in place, when to use builders, and how much temporary mutability is acceptable | Controlled mutable locals are fine vs minimize mutation aggressively |
| Testing strategy, test organization, and doctests | Unit vs integration tests, `#[cfg(test)]`, doctest expectations, failure style in tests | Heavy unit testing vs more black-box integration coverage |
| Property tests, snapshot tests, benchmarking, CI, and release workflow | When to add proptest/insta/criterion, required CI commands, release-note expectations | Minimal CI gate vs strong pre-merge verification and release discipline |

## Recommended page template

To make the eventual skill reliable for agents, each markdown page should use the same structure. That mirrors rustdoc’s guidance that good documentation starts with a short description, follows with more detail, and includes copy-pasteable examples; it also matches the API Guidelines’ emphasis on examples plus explicit `Errors`, `Panics`, and `Safety` sections where relevant. citeturn33view0turn18view0

| Section in each page | What it should contain |
|---|---|
| Rule | A one-sentence default the agent can follow mechanically |
| Why | Short rationale focused on readability, correctness, interoperability, or performance |
| Do this | Canonical patterns and preferred syntax |
| Avoid this | Common anti-patterns and why they are discouraged |
| Exceptions | The narrow cases where breaking the default is acceptable |
| Example | A small preferred example |
| Counterexample | A small rejected or less-preferred example |
| Notes by context | Optional notes for library code vs binary code, sync vs async, public API vs internal code |

For your specific taste, I would also add one line to every page that says either **“OO-leaning default”** or **“use functional style here”** wherever the tradeoff is non-obvious. That will keep the skill aligned with your preference without pretending Rust is only one paradigm. Rust explicitly supports OOP-style encapsulation and methods, while also taking major inspiration from functional programming and treating iterator/closure style as an important part of idiomatic code. citeturn30view0turn36view1turn30view2

## Open questions and limitations

A few scoping questions will materially change the final skill:

- Is this skill primarily for **internal service/application code**, **public library crates**, or both? That one choice affects errors, logging, async portability, and public API policy. citeturn31view0turn31view1turn25view0turn25view1
- Do you want to support **Tokio-specific code** as a first-class default, or require runtime-agnostic patterns except at the binary boundary? citeturn26view5turn26view1
- Will the agents write **stable-only Rust**, or may they use nightly-only conveniences in tightly controlled places? Several docs above note nightly-only features or unstable config surfaces. citeturn23view1turn29view1turn31view1
- Do you care about **public API semver discipline** as much as internal readability? If yes, pages on sealed traits, private fields, feature flags, and metadata become much stricter. citeturn14view2turn24view1turn18view0
- If your codebase targets **no_std**, embedded, FFI-heavy, or proc-macro-heavy** Rust, you should add extra topic pages beyond the 40 above, because those areas have their own strong conventions and hazards. citeturn37view2turn28view0

Taken together, the map above gives you a practical drafting outline: start by fixing the small set of global preference choices, then write one strict markdown page per topic, with examples and explicit exceptions. That will give your agents a style skill that is narrow enough to apply consistently, but broad enough to produce idiomatic Rust across error handling, diagnostics, async code, API design, and daily implementation work. citeturn22view0turn20search2turn25view3turn33view0