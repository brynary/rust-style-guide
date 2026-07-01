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
6. For performance investigation, load [workflows/performance-investigation.md](workflows/performance-investigation.md).
7. For code review or refactor work, load [workflows/code-review-refactor.md](workflows/code-review-refactor.md).
8. Apply the loaded rules directly. If required project context is missing, ask one focused question before broad changes.

[root.md](root.md) carries the routing examples and core behavior rules; follow it rather than duplicating its guidance here.
