# Guidelines

Load this file for Rust style policy, then load only the guideline pages needed for the task.

Guideline pages are policy. Do not load every guideline page by default.

## Foundations

- [House style and Rust philosophy](guidelines/house-style-and-rust-philosophy.md)
- [Library vs application conventions](guidelines/library-vs-application-conventions.md)
- [Rust edition and MSRV](guidelines/rust-edition-and-msrv.md)

## Tooling and Project Shape

- [rustfmt and formatting](guidelines/rustfmt-and-formatting.md)
- [rustc and Clippy lints](guidelines/rustc-and-clippy-lints.md)
- [Cargo, workspaces, features, and dependencies](guidelines/cargo-workspaces-features-and-dependencies.md)
- [Modules, visibility, and re-exports](guidelines/modules-visibility-and-re-exports.md)
- [Naming, imports, and prelude policy](guidelines/naming-imports-and-prelude-policy.md)
- [Documentation and rustdoc examples](guidelines/documentation-and-rustdoc-examples.md)

## Type and API Design

- [Struct design and encapsulation](guidelines/struct-design-and-encapsulation.md)
- [Constructors and builders](guidelines/constructors-and-builders.md)
- [Newtype pattern and semantic wrappers](guidelines/newtype-pattern-and-semantic-wrappers.md)
- [Enums vs traits vs generics vs trait objects](guidelines/enums-vs-traits-vs-generics-vs-trait-objects.md)
- [Trait design](guidelines/trait-design.md)
- [Deriving and common trait implementations](guidelines/deriving-and-common-trait-implementations.md)
- [Conversions, getters, and method naming](guidelines/conversions-getters-and-method-naming.md)
- [Typestate and state machines](guidelines/typestate-and-state-machines.md)
- [Public API evolution](guidelines/public-api-evolution.md)

## Ownership and Data Flow

- [Ownership, borrowing, and clone policy](guidelines/ownership-borrowing-and-clone-policy.md)
- [Strings, slices, and flexible parameters](guidelines/strings-slices-and-flexible-parameters.md)
- [Lifetimes](guidelines/lifetimes.md)
- [Smart pointers and interior mutability](guidelines/smart-pointers-and-interior-mutability.md)
- [Collections and data structures](guidelines/collections-and-data-structures.md)

## Errors, Safety, and Diagnostics

- [Error taxonomy and layer boundaries](guidelines/error-taxonomy-and-layer-boundaries.md)
- [Library errors vs application errors](guidelines/library-errors-vs-application-errors.md)
- [Error propagation, context, and messages](guidelines/error-propagation-context-and-messages.md)
- [Panics, unwrap, expect, and assertions](guidelines/panics-unwrap-expect-and-assertions.md)
- [Validation and invariants](guidelines/validation-and-invariants.md)
- [Logging and observability](guidelines/logging-and-observability.md)

## Async and Concurrency

- [Async runtime and when to use async](guidelines/async-runtime-and-when-to-use-async.md)
- [Async API design and task lifecycle](guidelines/async-api-design-and-task-lifecycle.md)
- [Cancellation, shutdown, and blocking work](guidelines/cancellation-shutdown-and-blocking-work.md)
- [Concurrency primitives](guidelines/concurrency-primitives.md)

## Everyday Implementation

- [Control flow](guidelines/control-flow.md)
- [Option and Result idioms](guidelines/option-and-result-idioms.md)
- [Iterators, closures, and loops](guidelines/iterators-closures-and-loops.md)
- [Mutation style](guidelines/mutation-style.md)

## Testing and Release

- [Testing and doctests](guidelines/testing-and-doctests.md)
- [Property tests, snapshots, benchmarks, and CI](guidelines/property-tests-snapshots-benchmarks-and-ci.md)
- [Unsafe code and macros](guidelines/unsafe-code-and-macros.md)

## Routing Notes

- For new Rust project setup, load [workflows/new-rust-project.md](workflows/new-rust-project.md) before individual setup guidelines.
- For reusable library release verification, load [workflows/reusable-library-release.md](workflows/reusable-library-release.md) before individual release guidelines.
- For performance investigation, load [workflows/performance-investigation.md](workflows/performance-investigation.md) before individual performance-related guidelines.
- For public API work, always include public API evolution.
- For async service work, include logging and observability.
- For error-handling work, distinguish library errors from application errors before choosing crates.
- For advanced topics like typestate, unsafe, macros, or specialized collections, load the page only when the task directly needs it.
