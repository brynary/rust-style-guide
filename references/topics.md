# Topic Index

Load this file first, then load only the topic pages needed for the task.

Topic pages should use short, directive rules. Do not load every topic page by default.

## Foundations

- House style and Rust philosophy
- Library vs application conventions
- Rust edition and MSRV

## Tooling and Project Shape

- rustfmt and formatting
- rustc and Clippy lints
- Cargo, workspaces, features, and dependencies
- Modules, visibility, and re-exports
- Naming, imports, and prelude policy
- Documentation and rustdoc examples

## Type and API Design

- Struct design and encapsulation
- Constructors and builders
- Newtype pattern and semantic wrappers
- Enums vs traits vs generics vs trait objects
- Trait design
- Deriving and common trait implementations
- Conversions, getters, and method naming
- Typestate and state machines
- Public API evolution

## Ownership and Data Flow

- Ownership, borrowing, and clone policy
- Strings, slices, and flexible parameters
- Lifetimes
- Smart pointers and interior mutability
- Collections and data structures

## Errors, Safety, and Diagnostics

- Error taxonomy and layer boundaries
- Library errors vs application errors
- Error propagation, context, and messages
- Panics, `unwrap`, `expect`, and assertions
- Validation and invariants
- Logging and observability

## Async and Concurrency

- Async runtime and when to use async
- Async API design and task lifecycle
- Cancellation, shutdown, and blocking work
- Concurrency primitives

## Everyday Implementation

- Control flow
- Option and Result idioms
- Iterators, closures, and loops
- Mutation style

## Testing and Release

- Testing and doctests
- Property tests, snapshots, benchmarks, and CI
- Unsafe code and macros

## Routing Notes

- For public API work, always include public API evolution.
- For async service work, include logging and observability.
- For error-handling work, distinguish library errors from application errors before choosing crates.
- For advanced topics like typestate, unsafe, macros, or specialized collections, load the page only when the task directly needs it.
