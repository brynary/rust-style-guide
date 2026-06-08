# Error Handling Strategy

## Rule

Return typed errors from libraries and use erased, context-rich errors near application boundaries.

## Why

Library callers often need to inspect and recover from specific failures. Applications usually need good diagnostics and clear operator-facing messages more than public error stability.

## Do

- Use `Result<T, E>` for expected or recoverable failure.
- Use a domain-specific error type for public library APIs.
- Use `thiserror` for low-boilerplate typed errors unless the project chooses hand-written error structs.
- Use `anyhow::Result<T>` in binaries, CLIs, tests, and top-level application glue when typed recovery is not needed.
- Add context at boundaries where the caller would otherwise lose meaning.

## Avoid

- Do not expose raw infrastructure errors from domain APIs.
- Do not use `Box<dyn Error>` as the default public API shape.
- Do not panic for ordinary parse, IO, network, or validation failures.
- Do not write vague messages like `"failed"` or `"bad input"`.

## Exceptions

- A small internal helper may return an upstream error directly if it is not part of the public boundary.
- A public library may choose hand-written error structs instead of `thiserror` if forward compatibility is more important than enum ergonomics.
- User-facing CLIs may use `miette` or a similar reporting crate for richer diagnostics.

## Example

```rust
use std::path::Path;

use thiserror::Error;

#[derive(Debug, Error)]
pub enum ConfigError {
    #[error("failed to read config from {path}")]
    Read {
        path: String,
        #[source]
        source: std::io::Error,
    },

    #[error("config is missing required field `{field}`")]
    MissingField { field: &'static str },
}

pub fn load_config(path: &Path) -> Result<Config, ConfigError> {
    let contents = std::fs::read_to_string(path).map_err(|source| ConfigError::Read {
        path: path.display().to_string(),
        source,
    })?;

    Config::parse(&contents)
}
```

## Application Boundary

```rust
use std::path::Path;

use anyhow::{Context, Result};

fn main() -> Result<()> {
    let config = load_config(Path::new("app.toml")).context("could not load application config")?;
    run(config)
}
```

## Decision Points

- Library error shape: `thiserror` enum, hand-written struct, or `snafu`.
- Application error reporting: `anyhow`, `eyre`, or `miette`.
- How much context to attach at each layer.
