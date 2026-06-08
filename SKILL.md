---
name: rust-style-guide
description: Use when writing, reviewing, or refactoring Rust code and the user wants idiomatic Rust that follows this project's conventions. Covers errors, panics, ownership, API design, async, logging, linting, testing, and related Rust style decisions.
---

# Rust Style Guide

Use this skill to apply the project's Rust style conventions while writing or reviewing Rust code.

## First Steps

1. Identify the context: library, application, CLI, test, public API, internal module, sync code, or async code.
2. Load [references/topics.md](references/topics.md).
3. Load only the topic pages relevant to the task.
4. Apply the rules directly. If a loaded topic page marks a decision as unresolved, ask before choosing a policy.

## Routing Examples

| Task | Load |
| --- | --- |
| Define a public library error type | `topics.md`, library errors, error propagation, public API evolution |
| Handle top-level CLI/application errors | `topics.md`, application errors, error propagation, panics |
| Choose enum vs trait vs trait object | `topics.md`, enums vs traits, trait design, public API evolution |
| Add a domain ID or validated value | `topics.md`, newtypes, constructors, validation |
| Write async service code | `topics.md`, async runtime, task lifecycle, cancellation, logging |
| Add instrumentation | `topics.md`, logging and observability, error messages |
| Set project linting | `topics.md`, clippy, rustfmt, cargo |
| Review unsafe code or macros | `topics.md`, unsafe and macros, public API evolution |

## Core Behavior

- Keep the root skill small; use references for detailed rules.
- Prefer concrete Rust guidance over language tutorials.
- Keep library/application differences explicit.
- Use the project's OO-leaning Rust default without forcing inheritance-shaped designs.
- Prefer strong, compiler-backed types over primitive-heavy APIs.
- Ask one focused question when a loaded topic page has an unresolved decision point.
