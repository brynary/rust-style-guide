# Rust Style Guide

Use this skill to apply the project's Rust style conventions while writing, reviewing, refactoring, or configuring Rust code.

## Supporting Files

- [guidelines.md](guidelines.md) - index of Rust style policy pages. Load this for ordinary Rust work, then load only the guideline pages relevant to the task.
- [workflows/new-rust-project.md](workflows/new-rust-project.md) - workflow for creating or configuring a new Rust crate, workspace, CLI, library, service, or application.
- [workflows/reusable-library-release.md](workflows/reusable-library-release.md) - workflow for verifying reusable library releases, feature combinations, dependency checks, and out-of-box builds.
- [workflows/performance-investigation.md](workflows/performance-investigation.md) - workflow for measuring, profiling, and changing performance-sensitive Rust code.
- [workflows/existing-code-review-refactor.md](workflows/existing-code-review-refactor.md) - workflow for reviewing, refactoring, or changing existing Rust code.

## Routing Examples

| Task | Load |
| --- | --- |
| Create a new Rust project | [workflows/new-rust-project.md](workflows/new-rust-project.md), [guidelines.md](guidelines.md) |
| Verify a reusable library release | [workflows/reusable-library-release.md](workflows/reusable-library-release.md), [guidelines.md](guidelines.md) |
| Investigate performance | [workflows/performance-investigation.md](workflows/performance-investigation.md), [guidelines.md](guidelines.md) |
| Review or refactor existing code | [workflows/existing-code-review-refactor.md](workflows/existing-code-review-refactor.md), [guidelines.md](guidelines.md) |
| Define a public library error type | [guidelines.md](guidelines.md), library/application errors, error propagation, public API evolution |
| Handle top-level CLI/application errors | [guidelines.md](guidelines.md), library/application errors, error propagation, panics |
| Choose enum vs trait vs trait object | [guidelines.md](guidelines.md), enums vs traits, trait design, public API evolution |
| Add a domain ID or validated value | [guidelines.md](guidelines.md), newtypes, constructors, validation |
| Write async service code | [guidelines.md](guidelines.md), async runtime, task lifecycle, shutdown, logging |
| Add instrumentation | [guidelines.md](guidelines.md), logging and observability, error messages |
| Configure formatting, lints, or tests | [guidelines.md](guidelines.md), rustfmt, Clippy, Cargo, CI |
| Review unsafe code or macros | [guidelines.md](guidelines.md), unsafe and macros, public API evolution |

## Core Behavior

- Keep the root router small; use guidelines and workflows for details.
- Prefer concrete Rust guidance over language tutorials.
- Keep library/application differences explicit.
- Use the project's OO-leaning Rust default without forcing inheritance-shaped designs.
- Prefer strong, compiler-backed types over primitive-heavy APIs.
- Treat guideline pages as policy; treat workflow pages as procedures.
- Ask one focused question only when required project context is missing.
