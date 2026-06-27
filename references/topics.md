# Topic Index

Load this file first, then load only the topic pages needed for the task.

Topic pages should use short, directive rules. Do not load every topic page by default.

## Foundations

- [House style and Rust philosophy](house-style-and-rust-philosophy.md)
- [Library vs application conventions](library-vs-application-conventions.md)
- [Rust edition and MSRV](rust-edition-and-msrv.md)

## Tooling and Project Shape

- [rustfmt and formatting](rustfmt-and-formatting.md)
- [rustc and Clippy lints](rustc-and-clippy-lints.md)
- [Cargo, workspaces, features, and dependencies](cargo-workspaces-features-and-dependencies.md)
- [Modules, visibility, and re-exports](modules-visibility-and-re-exports.md)
- [Naming, imports, and prelude policy](naming-imports-and-prelude-policy.md)
- [Documentation and rustdoc examples](documentation-and-rustdoc-examples.md)

## Type and API Design

- [Struct design and encapsulation](struct-design-and-encapsulation.md)
- [Constructors and builders](constructors-and-builders.md)
- [Newtype pattern and semantic wrappers](newtype-pattern-and-semantic-wrappers.md)
- [Enums vs traits vs generics vs trait objects](enums-vs-traits-vs-generics-vs-trait-objects.md)
- [Trait design](trait-design.md)
- [Deriving and common trait implementations](deriving-and-common-trait-implementations.md)
- [Conversions, getters, and method naming](conversions-getters-and-method-naming.md)
- [Typestate and state machines](typestate-and-state-machines.md)
- [Public API evolution](public-api-evolution.md)

## Ownership and Data Flow

- [Ownership, borrowing, and clone policy](ownership-borrowing-and-clone-policy.md)
- [Strings, slices, and flexible parameters](strings-slices-and-flexible-parameters.md)
- [Lifetimes](lifetimes.md)
- [Smart pointers and interior mutability](smart-pointers-and-interior-mutability.md)
- [Collections and data structures](collections-and-data-structures.md)

## Errors, Safety, and Diagnostics

- [Error taxonomy and layer boundaries](error-taxonomy-and-layer-boundaries.md)
- [Library errors vs application errors](library-errors-vs-application-errors.md)
- [Error propagation, context, and messages](error-propagation-context-and-messages.md)
- [Panics, unwrap, expect, and assertions](panics-unwrap-expect-and-assertions.md)
- [Validation and invariants](validation-and-invariants.md)
- [Logging and observability](logging-and-observability.md)

## Async and Concurrency

- [Async runtime and when to use async](async-runtime-and-when-to-use-async.md)
- [Async API design and task lifecycle](async-api-design-and-task-lifecycle.md)
- [Cancellation, shutdown, and blocking work](cancellation-shutdown-and-blocking-work.md)
- [Concurrency primitives](concurrency-primitives.md)

## Everyday Implementation

- [Control flow](control-flow.md)
- [Option and Result idioms](option-and-result-idioms.md)
- [Iterators, closures, and loops](iterators-closures-and-loops.md)
- [Mutation style](mutation-style.md)

## Testing and Release

- [Testing and doctests](testing-and-doctests.md)
- [Property tests, snapshots, benchmarks, and CI](property-tests-snapshots-benchmarks-and-ci.md)
- [Unsafe code and macros](unsafe-code-and-macros.md)

## Routing Notes

- For public API work, always include public API evolution.
- For async service work, include logging and observability.
- For error-handling work, distinguish library errors from application errors before choosing crates.
- For advanced topics like typestate, unsafe, macros, or specialized collections, load the page only when the task directly needs it.
