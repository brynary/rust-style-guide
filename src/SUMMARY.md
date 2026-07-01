# Summary

[Introduction](README.md)

# Skill

- [Skill Router](root.md)
- [Guidelines Index](guidelines.md)

# Foundations

- [House Style and Rust Philosophy](guidelines/house-style-and-rust-philosophy.md)
- [Library vs Application Conventions](guidelines/library-vs-application-conventions.md)
- [Rust Edition and MSRV](guidelines/rust-edition-and-msrv.md)

# Tooling and Project Shape

- [rustfmt and Formatting](guidelines/rustfmt-and-formatting.md)
- [rustc and Clippy Lints](guidelines/rustc-and-clippy-lints.md)
- [Cargo, Workspaces, Features, and Dependencies](guidelines/cargo-workspaces-features-and-dependencies.md)
- [Modules, Visibility, and Re-exports](guidelines/modules-visibility-and-re-exports.md)
- [Naming, Imports, and Prelude Policy](guidelines/naming-imports-and-prelude-policy.md)
- [Documentation and Rustdoc Examples](guidelines/documentation-and-rustdoc-examples.md)

# Type and API Design

- [Struct Design and Encapsulation](guidelines/struct-design-and-encapsulation.md)
- [Constructors and Builders](guidelines/constructors-and-builders.md)
- [Newtype Pattern and Semantic Wrappers](guidelines/newtype-pattern-and-semantic-wrappers.md)
- [Enums vs Traits vs Generics vs Trait Objects](guidelines/enums-vs-traits-vs-generics-vs-trait-objects.md)
- [Trait Design](guidelines/trait-design.md)
- [Deriving and Common Trait Implementations](guidelines/deriving-and-common-trait-implementations.md)
- [Conversions, Getters, and Method Naming](guidelines/conversions-getters-and-method-naming.md)
- [Typestate and State Machines](guidelines/typestate-and-state-machines.md)
- [Public API Evolution](guidelines/public-api-evolution.md)

# Ownership and Data Flow

- [Ownership, Borrowing, and Clone Policy](guidelines/ownership-borrowing-and-clone-policy.md)
- [Lifetimes](guidelines/lifetimes.md)
- [Smart Pointers and Interior Mutability](guidelines/smart-pointers-and-interior-mutability.md)
- [Collections and Data Structures](guidelines/collections-and-data-structures.md)

# Errors, Safety, and Diagnostics

- [Error Taxonomy and Layer Boundaries](guidelines/error-taxonomy-and-layer-boundaries.md)
- [Library Errors vs Application Errors](guidelines/library-errors-vs-application-errors.md)
- [Error Propagation, Context, and Messages](guidelines/error-propagation-context-and-messages.md)
- [Panics, unwrap, expect, and Assertions](guidelines/panics-unwrap-expect-and-assertions.md)
- [Validation and Invariants](guidelines/validation-and-invariants.md)
- [Logging and Observability](guidelines/logging-and-observability.md)

# Async and Concurrency

- [Async Runtime and When to Use Async](guidelines/async-runtime-and-when-to-use-async.md)
- [Async API Design and Task Lifecycle](guidelines/async-api-design-and-task-lifecycle.md)
- [Cancellation, Shutdown, and Blocking Work](guidelines/cancellation-shutdown-and-blocking-work.md)
- [Concurrency Primitives](guidelines/concurrency-primitives.md)

# Everyday Implementation

- [Control Flow](guidelines/control-flow.md)
- [Option and Result Idioms](guidelines/option-and-result-idioms.md)
- [Iterators, Closures, and Loops](guidelines/iterators-closures-and-loops.md)

# Testing and Release

- [Testing and Doctests](guidelines/testing-and-doctests.md)
- [Property Tests, Snapshots, Benchmarks, and CI](guidelines/property-tests-snapshots-benchmarks-and-ci.md)
- [Unsafe Code and Macros](guidelines/unsafe-code-and-macros.md)

# Workflows

- [New Rust Project](workflows/new-rust-project.md)
- [Reusable Library Release](workflows/reusable-library-release.md)
- [Performance Investigation](workflows/performance-investigation.md)
- [Code Review and Refactor](workflows/code-review-refactor.md)
