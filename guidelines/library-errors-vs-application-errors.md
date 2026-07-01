# Library Errors vs Application Errors

## Rule

Expose typed errors from reusable library boundaries, usually with `thiserror`; use `anyhow` inside applications and CLIs, and use `miette` only when rich user-facing diagnostics are worth the extra structure.

## Why

Library callers need stable types they can inspect and branch on. Applications usually need fast propagation, useful context, and deliberate rendering at the final boundary.

## Do

- Define a crate-local `Error` enum and `Result<T>` alias when a library crate has one cohesive error surface.
- Use `thiserror::Error` for ordinary typed errors.
- Keep public error variants branch-oriented, not a dump of every dependency failure.
- Preserve causes with `#[source]` or `#[from]`.
- Keep useful structured fields on typed errors instead of folding them into `String`.
- Add `#[non_exhaustive]` to public error enums that may grow in a published API.
- Use `anyhow::Result<T>` in binaries, command handlers, workers, tests, and internal application glue.
- Add application context with `.context(...)` or `.with_context(...)` instead of stringifying the source error.
- Use `miette` for CLI diagnostics that benefit from labels, source snippets, help text, or polished reports.
- Convert to `miette` only at the presentation layer: std and `thiserror` errors do not cross `?` into `miette::Report` without `IntoDiagnostic::into_diagnostic()` or `#[derive(Diagnostic)]`, so keep internal errors on `thiserror` or `anyhow`.
- Keep typed domain errors in application code when code branches on the failure.

## Avoid

- Do not expose `anyhow::Error` from reusable library APIs.
- Do not use `miette` as a general internal application error type.
- Do not mix `anyhow` and `eyre` in the same application without a project-level reason.
- Do not make `Box<dyn std::error::Error>` the default public error strategy.
- Do not leak database, HTTP, SDK, or parser error types from a public API unless they are intentionally part of the contract.
- Do not create public variants only to mirror each dependency error.
- Do not convert errors to `String` to cross internal crate boundaries.

## Public API Notes

`thiserror` is usually fine for public libraries because it generates standard trait impls without becoming part of function signatures. Be more careful with the fields on public error variants: exposed source types can make dependencies part of the public contract.

For published crates, prefer stable domain variants and hide implementation details when callers should not depend on them. For internal application crates, optimize for clarity and accept breaking error-shape changes.

## Example

Library crate:

```rust
#[derive(Debug, thiserror::Error)]
#[non_exhaustive]
pub enum ConfigError {
    #[error("configuration file {path} was not found")]
    NotFound {
        path: std::path::PathBuf,

        #[source]
        source: std::io::Error,
    },

    #[error("reading configuration file {path}")]
    Read {
        path: std::path::PathBuf,

        #[source]
        source: std::io::Error,
    },

    #[error("configuration value {key} is invalid")]
    InvalidValue { key: String },
}

pub type Result<T> = std::result::Result<T, ConfigError>;

pub fn load_config(path: &std::path::Path) -> Result<Config> {
    let contents = match std::fs::read_to_string(path) {
        Ok(contents) => contents,
        Err(source) if source.kind() == std::io::ErrorKind::NotFound => {
            return Err(ConfigError::NotFound {
                path: path.to_path_buf(),
                source,
            });
        }
        Err(source) => {
            return Err(ConfigError::Read {
                path: path.to_path_buf(),
                source,
            });
        }
    };

    parse_config(&contents)
}
```

Application boundary:

```rust
use anyhow::{Context, Result};

fn run() -> Result<()> {
    let path = std::path::PathBuf::from("config.toml");
    let config = config_lib::load_config(&path)
        .with_context(|| format!("failed to load {}", path.display()))?;

    start_server(config).context("failed to start server")?;
    Ok(())
}
```

## Exceptions

- Use hand-written error impls when avoiding a dependency or tightly controlling a public API matters.
- Use `anyhow` in internal libraries that are only application implementation details and are not consumed as reusable APIs.
- Use `miette` at the CLI presentation layer when the diagnostic output is part of the product experience.
