# Rust Style Guide Skill Outline

This outline is for a Rust style guide packaged as an AI-agent skill. The skill should not teach all of Rust. It should give agents clear defaults, exceptions, and small examples for the decisions they face while writing code.

Target size: about 40 topic pages. Each topic should fit on one focused markdown page.

## Drafting Instructions

Use [DRAFTING.md](DRAFTING.md) for drafting order, scope, and page-writing guidance.

## Page Template

Use [TEMPLATE.md](TEMPLATE.md) for every topic page.

## Packaged Skill Shape

The final skill should follow the progressive-disclosure pattern in [SKILL.md](SKILL.md) and [references/topics.md](references/topics.md): a small root router plus focused reference pages. Planning files and research reports should not be part of the packaged skill by default.

## Decision Register

Use [DECISIONS.md](DECISIONS.md) to resolve style decisions before drafting final policy pages.

## Topic Map

### Foundations

1. **House Style and Rust Philosophy**
   - Set the OO-leaning default without forcing inheritance-shaped designs.
   - Decision points: D1, D8, D22.

2. **Library vs Application Conventions**
   - Teach agents to identify whether they are writing public library code, internal application code, CLI code, or tests.
   - Decision points: D2, D4, D5, D16, D19.

3. **Rust Edition and MSRV**
   - Define edition, `rust-version`, MSRV update policy, and stable-vs-nightly expectations.
   - Decision points: D3.

### Tooling and Project Shape

4. **rustfmt and Formatting**
   - Prefer rustfmt defaults, define formatting exceptions, and keep CI/editor behavior aligned.
   - Decision points: custom format settings vs defaults.

5. **rustc and Clippy Lints**
   - Define lint baseline, deny/warn policy, local overrides, and generated-code expectations.
   - Decision points: D20, D21.

6. **Cargo, Workspaces, Features, and Dependencies**
   - Cover workspace layout, additive feature flags, dependency hygiene, public dependency leakage, profiles, and metadata.
   - Decision points: dependency conservatism, feature defaults, MSRV impact.

7. **Modules, Visibility, and Re-exports**
   - Cover `mod`, file layout, `pub`, `pub(crate)`, `pub(super)`, facades, and public API shape.
   - Decision points: D14, D15.

8. **Naming, Imports, and Prelude Policy**
   - Cover casing, acronym style, import style, getter names, and when a prelude is justified.
   - Decision points: D15.

9. **Documentation and Rustdoc Examples**
   - Cover summary lines, `//!`, `///`, `Errors`, `Panics`, `Safety`, examples, and doctest style.
   - Decision points: doc every public item vs only non-obvious items; unwrap in examples.

### Type and API Design

10. **Struct Design and Encapsulation**
    - Cover private fields, method receivers, plain data structs, invariants, and module-based privacy.
    - Decision points: D1, D14.

11. **Constructors and Builders**
    - Cover `new`, `try_new`, `with_*`, `from_*`, `Default`, consuming builders, non-consuming builders, and typestate builders.
    - Decision points: D13.

12. **Newtype Pattern and Semantic Wrappers**
    - Cover IDs, units, validated strings, orphan-rule workarounds, `Deref` restraint, and value objects.
    - Decision points: D12.

13. **Enums vs Traits vs Generics vs Trait Objects**
    - Cover closed worlds, open extension points, static dispatch, dynamic dispatch, object safety, and heterogeneous collections.
    - Decision points: D7.

14. **Trait Design**
    - Cover small traits, associated types, bounds, blanket impls, sealed traits, object safety, and trait contracts.
    - Decision points: D7, trait granularity, sealed traits.

15. **Deriving and Common Trait Implementations**
    - Cover `Debug`, `Clone`, `Copy`, `PartialEq`, `Eq`, `Hash`, `Ord`, `Default`, `Display`, and manual impls.
    - Decision points: D9.

16. **Conversions, Getters, and Method Naming**
    - Cover `From`, `TryFrom`, `AsRef`, `Borrow`, `Deref`, `as_`, `to_`, `into_`, and getter naming.
    - Decision points: D11, whether to expose getters for every field.

17. **Typestate and State Machines**
    - Cover data-bearing enums, `PhantomData`, compile-time state, and when typestate is too much.
    - Decision points: D13, type-level vs runtime validation.

18. **Public API Evolution**
    - Cover semver, `#[non_exhaustive]`, `#[must_use]`, sealed traits, public fields, and public dependencies.
    - Decision points: D14, D15, public API strictness.

### Ownership and Data Flow

19. **Ownership, Borrowing, and Clone Policy**
    - Cover `self`, `&self`, `&mut self`, owned returns, internal clones, and `Rc::clone`/`Arc::clone` style.
    - Decision points: D10.

20. **Strings, Slices, and Flexible Parameters**
    - Cover `String`, `&str`, `Path`, `&Path`, slices, `IntoIterator`, `AsRef`, `Into`, and `Cow`.
    - Decision points: D11.

21. **Lifetimes**
    - Cover lifetime elision, naming lifetimes, lifetime-bearing structs, and avoiding gratuitous annotations.
    - Decision points: how much API complexity to accept for avoiding allocation.

22. **Smart Pointers and Interior Mutability**
    - Cover `Box`, `Rc`, `Arc`, `Cell`, `RefCell`, `Mutex`, `RwLock`, `OnceLock`, and `LazyLock`.
    - Decision points: D18, when interior mutability is acceptable.

23. **Collections and Data Structures**
    - Cover `Vec`, `VecDeque`, maps, sets, deterministic ordering, capacity hints, and small collection crates.
    - Decision points: dependency threshold for specialized collections.

### Errors, Safety, and Diagnostics

24. **Error Taxonomy and Layer Boundaries**
    - Cover domain errors, infrastructure errors, programming errors, conversion between layers, and avoiding error leakage.
    - Decision points: granularity of error enums and context boundaries.

25. **Library Errors vs Application Errors**
    - Cover `thiserror`, `anyhow`, `eyre`, `miette`, hand-written errors, and public error stability.
    - Decision points: D4, D5.

26. **Error Propagation, Context, and Messages**
    - Cover `?`, `From`, `#[from]`, `.context()`, `Display`, source chains, and message style.
    - Decision points: sparse vs rich context.

27. **Panics, `unwrap`, `expect`, and Assertions**
    - Cover `panic!`, `unwrap`, `expect`, `assert!`, `debug_assert!`, `unreachable!`, `todo!`, and tests.
    - Decision points: D6.

28. **Validation and Invariants**
    - Cover fallible constructors, boundary validation, parse-don't-validate, newtypes, and fail-fast startup checks.
    - Decision points: type-level vs runtime validation.

29. **Logging and Observability**
    - Cover `tracing`, `log`, spans, fields, levels, backtraces, PII/secrets, and OpenTelemetry hooks.
    - Decision points: D19.

### Async and Concurrency

30. **Async Runtime and When to Use Async**
    - Cover Tokio-first vs runtime-agnostic design, sync alternatives, and library/runtime boundaries.
    - Decision points: D16.

31. **Async API Design and Task Lifecycle**
    - Cover async traits, `Send` bounds, `JoinHandle`, spawning, ownership, task naming, and task cleanup.
    - Decision points: D17.

32. **Cancellation, Shutdown, and Blocking Work**
    - Cover cancellation safety, graceful shutdown, `select!`, timeouts, `spawn_blocking`, and CPU-bound work.
    - Decision points: D17.

33. **Concurrency Primitives**
    - Cover threads, channels, `Arc<Mutex<T>>`, `RwLock`, lock ordering, tokio vs std sync types, and `rayon`.
    - Decision points: D18.

### Everyday Implementation

34. **Control Flow**
    - Cover `match`, `if let`, `while let`, `let else`, early returns, match guards, and exhaustiveness.
    - Decision points: exhaustive clarity vs concise happy-path code.

35. **Option and Result Idioms**
    - Cover `Option`, `Result`, `ok_or`, `map`, `and_then`, `unwrap_or_else`, and using `?` on both types.
    - Decision points: combinators vs explicit control flow.

36. **Iterators, Closures, and Loops**
    - Cover iterator chains, `collect`, `fold`, `try_fold`, closure capture, and when loops are clearer.
    - Decision points: D22.

37. **Mutation Style**
    - Cover controlled mutable locals, in-place updates, immutable transforms, builders, and functional-core/OO-shell framing.
    - Decision points: D1, D10, D22.

### Testing and Release

38. **Testing and Doctests**
    - Cover unit tests, integration tests, module-private tests, doctests, test naming, and fallible test helpers.
    - Decision points: D23.

39. **Property Tests, Snapshots, Benchmarks, and CI**
    - Cover `proptest`, `quickcheck`, `insta`, `criterion`, `cargo test`, `cargo clippy`, `cargo fmt`, and `nextest`.
    - Decision points: D24.

40. **Unsafe Code and Macros**
    - Cover when `unsafe` is allowed, `SAFETY:` comments, safe abstraction boundaries, `macro_rules!`, proc macros, and macro restraint.
    - Decision points: D25.

## Sample Topic Pages

Three sample pages use the proposed format:

- [Error Handling Strategy](samples/error-handling-strategy.md)
- [Enums vs Traits](samples/enums-vs-traits.md)
- [Logging and Observability](samples/logging-and-observability.md)

## Topics Folded In

These are important, but probably do not need standalone pages in v1 unless the target codebase depends on them heavily:

- FFI: fold into unsafe and dependency policy.
- Numeric overflow and casts: fold into conversions.
- Serde: fold into features, dependencies, and type design.
- no_std and embedded: add dedicated pages only if this guide targets embedded code.
- Proc-macro crate architecture: add a dedicated page only if agents will write proc macros.
- Database/application configuration/secrets: add app-specific pages only if the guide becomes service-focused.
