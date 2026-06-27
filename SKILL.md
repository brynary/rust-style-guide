---
name: rust-style-guide
description: Apply this Rust style guide when writing, reviewing, refactoring, or configuring Rust code for this project. Covers Rust 2024/MSRV, library vs application conventions, public API design, errors, panics, ownership and cloning, async/Tokio/concurrency, tracing, rustfmt/Clippy, testing with nextest, and unsafe/macro policy.
---

# Rust Style Guide

Use this skill to apply the project's Rust style conventions while writing or reviewing Rust code.

## First Steps

1. Identify the context: library, application, CLI, test, public API, internal module, sync code, or async code.
2. Load [references/topics.md](references/topics.md).
3. Load only the topic pages relevant to the task.
4. Apply the loaded rules directly. If required project context is missing, ask one focused question before broad changes.

## Routing Examples

| Task | Load |
| --- | --- |
| Define a public library error type | [topics.md](references/topics.md), [library/application errors](references/library-errors-vs-application-errors.md), [error propagation](references/error-propagation-context-and-messages.md), [public API evolution](references/public-api-evolution.md) |
| Handle top-level CLI/application errors | [topics.md](references/topics.md), [library/application errors](references/library-errors-vs-application-errors.md), [error propagation](references/error-propagation-context-and-messages.md), [panics](references/panics-unwrap-expect-and-assertions.md) |
| Choose enum vs trait vs trait object | [topics.md](references/topics.md), [enums vs traits](references/enums-vs-traits-vs-generics-vs-trait-objects.md), [trait design](references/trait-design.md), [public API evolution](references/public-api-evolution.md) |
| Add a domain ID or validated value | [topics.md](references/topics.md), [newtypes](references/newtype-pattern-and-semantic-wrappers.md), [constructors](references/constructors-and-builders.md), [validation](references/validation-and-invariants.md) |
| Write async service code | [topics.md](references/topics.md), [async runtime](references/async-runtime-and-when-to-use-async.md), [task lifecycle](references/async-api-design-and-task-lifecycle.md), [shutdown](references/cancellation-shutdown-and-blocking-work.md), [logging](references/logging-and-observability.md) |
| Add instrumentation | [topics.md](references/topics.md), [logging and observability](references/logging-and-observability.md), [error messages](references/error-propagation-context-and-messages.md) |
| Configure formatting, lints, or tests | [topics.md](references/topics.md), [rustfmt](references/rustfmt-and-formatting.md), [Clippy](references/rustc-and-clippy-lints.md), [Cargo](references/cargo-workspaces-features-and-dependencies.md), [CI](references/property-tests-snapshots-benchmarks-and-ci.md) |
| Review unsafe code or macros | [topics.md](references/topics.md), [unsafe and macros](references/unsafe-code-and-macros.md), [public API evolution](references/public-api-evolution.md) |

## Core Behavior

- Keep the root skill small; use references for detailed rules.
- Prefer concrete Rust guidance over language tutorials.
- Keep library/application differences explicit.
- Use the project's OO-leaning Rust default without forcing inheritance-shaped designs.
- Prefer strong, compiler-backed types over primitive-heavy APIs.
- Treat reference pages as policy; do not load planning files for ordinary Rust work.
- Ask one focused question only when the relevant reference page requires project-specific context that is missing.
