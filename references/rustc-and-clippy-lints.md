# rustc and Clippy Lints

## Rule

Use curated workspace lints: start from the Fabro lint shape, tailor project-specific denies, and require justified local exceptions with `#[expect(..., reason = "...")]`.

## Why

A curated lint set catches real mistakes without making agents satisfy every stylistic Clippy preference. Central policy keeps the baseline consistent, while local `expect` attributes make intentional exceptions auditable.

## Do

- Put shared lint policy in the workspace `Cargo.toml`.
- Run Clippy in CI with `cargo +nightly-2026-04-14 clippy --workspace --all-targets -- -D warnings`.
- Enable `clippy::pedantic` at `warn`, then allow noisy lints the project has rejected.
- Deny lints that catch correctness or project-boundary violations.
- Use `#[expect(lint_name, reason = "...")]` for narrow local exceptions.
- Review Fabro's `disallowed_methods` and `disallowed_types` before copying them; these should reflect the target project's architecture.
- Put architecture-specific Clippy settings in `clippy.toml`.

## Avoid

- Do not enable all restriction lints.
- Do not deny all pedantic lints by default.
- Do not add unexplained `#[allow(...)]` attributes.
- Do not hide one-off exceptions in workspace-wide lint config.
- Do not copy project-specific disallowed methods, types, or environment rules without checking that they match the new codebase.
- Do not use local lint bypasses for combinator-vs-control-flow idioms; refactor to Clippy's preferred shape or change the workspace lint policy deliberately.

## Example

Use this as the starting workspace policy, then tailor the project-specific entries:

```toml
[workspace.lints.rust]
unsafe_code = "deny"
unreachable_pub = "warn"

[workspace.lints.clippy]
pedantic = { level = "warn", priority = -2 }
allow_attributes_without_reason = "warn"

# Allowed pedantic lints
implicit_hasher = "allow"
missing_errors_doc = "allow"
missing_panics_doc = "allow"
module_name_repetitions = "allow"
must_use_candidate = "allow"
similar_names = "allow"
struct_excessive_bools = "allow"
too_many_arguments = "allow"
too_many_lines = "allow"
cast_precision_loss = "allow"
doc_markdown = "allow"

# Disallowed restriction lints
print_stdout = "warn"
print_stderr = "warn"
dbg_macro = "warn"
empty_drop = "warn"
empty_structs_with_brackets = "warn"
disallowed_methods = "deny"
exit = "warn"
get_unwrap = "warn"
unwrap_used = "deny"
rc_buffer = "warn"
rc_mutex = "warn"
rest_pat_in_fully_bound_structs = "warn"
use_self = "warn"

# Project-specific lints; review before copying.
wildcard_imports = "warn"
absolute_paths = "warn"
```

Justify local exceptions near the code:

```rust
#[expect(
    clippy::too_many_arguments,
    reason = "Constructor mirrors the wire contract fields one-to-one"
)]
pub fn new(
    id: RunId,
    parent_id: Option<RunId>,
    status: RunStatus,
    started_at: Timestamp,
    finished_at: Option<Timestamp>,
    labels: Labels,
    metadata: Metadata,
) -> Self {
    Self {
        id,
        parent_id,
        status,
        started_at,
        finished_at,
        labels,
        metadata,
    }
}
```

Use `clippy.toml` for project-specific architectural guardrails:

```toml
allow-unwrap-in-tests = true
allow-unwrap-types = ["std::sync::LockResult"]

disallowed-methods = [
  { path = "std::thread::sleep", reason = "Prefer tokio::time::sleep on Tokio paths; document intentional blocking sleeps with #[expect(clippy::disallowed_methods, reason = \"...\")]", replacement = "tokio::time::sleep" },
  { path = "std::thread::spawn", reason = "Prefer Tokio task APIs on async paths; document intentional dedicated OS threads with #[expect(clippy::disallowed_methods, reason = \"...\")]" },
  { path = "std::process::Command::new", reason = "Prefer tokio::process::Command on Tokio paths; document intentional synchronous subprocesses with #[expect(clippy::disallowed_methods, reason = \"...\")]" },
]

disallowed-types = [
  { path = "std::io::Read", reason = "Blocking trait; prefer tokio::io::AsyncReadExt on Tokio paths. Document intentional sync I/O with #[expect(clippy::disallowed_types, reason = \"...\")]" },
  { path = "std::net::TcpStream", reason = "Blocking socket; prefer tokio::net::TcpStream on Tokio paths. Document intentional sync networking with #[expect(clippy::disallowed_types, reason = \"...\")]" },
]
```

## Exceptions

- Use `#[allow]` only when `#[expect]` is unavailable or the lint is intentionally disabled for generated code.
- Move a lint to workspace config when the project has rejected it as policy, not because one function is inconvenient.
- Lower or remove `unsafe_code = "deny"` only for crates whose purpose requires unsafe code, then document the local unsafe policy.
