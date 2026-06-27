---
name: rust-style-guide
description: Apply this Rust style guide when writing, reviewing, refactoring, or configuring Rust code for this project. Covers Rust 2024/MSRV, library vs application conventions, public API design, errors, panics, ownership and cloning, async/Tokio/concurrency, tracing, rustfmt/Clippy, testing with nextest, and unsafe/macro policy.
---

# Rust Style Guide

Use this skill to apply the project's Rust style conventions while writing or reviewing Rust code.

## First Steps

1. Load [root.md](root.md).
2. Identify whether the request is ordinary Rust work or a workflow.
3. For ordinary Rust work, load [guidelines.md](guidelines.md), then only the relevant guideline pages.
4. For new project setup, load [workflows/new-rust-project.md](workflows/new-rust-project.md).
5. For reusable library release verification, load [workflows/reusable-library-release.md](workflows/reusable-library-release.md).
6. Apply the loaded rules directly. If required project context is missing, ask one focused question before broad changes.

## Routing Examples

| Task | Load |
| --- | --- |
| Create a new Rust project | [root.md](root.md), [new project workflow](workflows/new-rust-project.md) |
| Verify a reusable library release | [root.md](root.md), [reusable library release workflow](workflows/reusable-library-release.md) |
| Define a public library error type | [guidelines.md](guidelines.md), [library/application errors](guidelines/library-errors-vs-application-errors.md), [error propagation](guidelines/error-propagation-context-and-messages.md), [public API evolution](guidelines/public-api-evolution.md) |
| Handle top-level CLI/application errors | [guidelines.md](guidelines.md), [library/application errors](guidelines/library-errors-vs-application-errors.md), [error propagation](guidelines/error-propagation-context-and-messages.md), [panics](guidelines/panics-unwrap-expect-and-assertions.md) |
| Choose enum vs trait vs trait object | [guidelines.md](guidelines.md), [enums vs traits](guidelines/enums-vs-traits-vs-generics-vs-trait-objects.md), [trait design](guidelines/trait-design.md), [public API evolution](guidelines/public-api-evolution.md) |
| Add a domain ID or validated value | [guidelines.md](guidelines.md), [newtypes](guidelines/newtype-pattern-and-semantic-wrappers.md), [constructors](guidelines/constructors-and-builders.md), [validation](guidelines/validation-and-invariants.md) |
| Write async service code | [guidelines.md](guidelines.md), [async runtime](guidelines/async-runtime-and-when-to-use-async.md), [task lifecycle](guidelines/async-api-design-and-task-lifecycle.md), [shutdown](guidelines/cancellation-shutdown-and-blocking-work.md), [logging](guidelines/logging-and-observability.md) |
| Add instrumentation | [guidelines.md](guidelines.md), [logging and observability](guidelines/logging-and-observability.md), [error messages](guidelines/error-propagation-context-and-messages.md) |
| Configure formatting, lints, or tests | [guidelines.md](guidelines.md), [rustfmt](guidelines/rustfmt-and-formatting.md), [Clippy](guidelines/rustc-and-clippy-lints.md), [Cargo](guidelines/cargo-workspaces-features-and-dependencies.md), [CI](guidelines/property-tests-snapshots-benchmarks-and-ci.md) |
| Review unsafe code or macros | [guidelines.md](guidelines.md), [unsafe and macros](guidelines/unsafe-code-and-macros.md), [public API evolution](guidelines/public-api-evolution.md) |

## Core Behavior

- Keep the root skill small; use guidelines and workflows for detailed rules.
- Prefer concrete Rust guidance over language tutorials.
- Keep library/application differences explicit.
- Use the project's OO-leaning Rust default without forcing inheritance-shaped designs.
- Prefer strong, compiler-backed types over primitive-heavy APIs.
- Treat guideline pages as policy and workflow pages as procedures; do not load planning files for ordinary Rust work.
- Ask one focused question only when the relevant reference page requires project-specific context that is missing.
