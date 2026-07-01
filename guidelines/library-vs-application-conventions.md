# Library vs Application Conventions

## Rule

Identify the code context first: write reusable libraries with stable, caller-controlled APIs, and write applications, services, CLIs, and tests with more concrete operational choices.

## Why

Library choices become another crate's constraints. Application choices optimize for delivery, observability, deployment, and local clarity.

## Do

- Treat public library APIs as long-lived contracts.
- Use typed public library errors, usually with `thiserror`.
- Use `anyhow` for internal application and CLI top-level error plumbing.
- Use `miette` when a CLI needs rich user-facing diagnostics.
- Document each project's sync vs async posture explicitly; use Tokio when the project chooses async.
- Use `tracing` for instrumentation across libraries and applications.
- Let applications install `tracing` subscribers, configure filters, spawn tasks, and own shutdown.
- Keep typed domain errors inside applications when code needs to branch on failures.

## Avoid

- Do not expose `anyhow::Error` from reusable public library APIs.
- Do not make a library install a global tracing subscriber.
- Do not hide Tokio task ownership, cancellation, or shutdown inside a library API.
- Do not force library-level abstraction into application code when one concrete type is enough.
- Do not over-model one-off CLI failure paths with large public error enums.

## Library vs Application

Library code should protect caller choice where it affects API stability: typed errors, careful dependency exposure, documented runtime assumptions, and no global process setup.

Application and CLI code may choose concrete dependencies directly: `anyhow` at boundaries, documented Tokio runtime setup when async is chosen, `tracing_subscriber` initialization, and pragmatic startup validation.

## Example

Library API:

```rust
use thiserror::Error;
use tracing::instrument;

#[derive(Debug, Error)]
pub enum ClientError {
    #[error("request failed")]
    Request(#[from] reqwest::Error),

    #[error("user {user_id} was not found")]
    NotFound { user_id: UserId },
}

#[instrument(skip(client), fields(user_id = %user_id))]
pub async fn fetch_user(client: &reqwest::Client, user_id: UserId) -> Result<User, ClientError> {
    let response = client.get(user_url(user_id)).send().await?;

    if response.status() == reqwest::StatusCode::NOT_FOUND {
        return Err(ClientError::NotFound { user_id });
    }

    let response = response.error_for_status()?;

    Ok(response.json().await?)
}
```

Application boundary:

```rust
use anyhow::{Context, Result};

#[tokio::main]
async fn main() -> Result<()> {
    tracing_subscriber::fmt()
        .with_env_filter("info")
        .init();

    let config = Config::load("app.toml").context("failed to load application config")?;
    let client = reqwest::Client::new();

    run_service(config, client).await.context("service failed")
}
```

## Exceptions

- Keep application internals typed when the caller must recover differently from different failures.
- Use a library-specific dependency when it is part of the crate's purpose and documented API.
- Use lighter examples or test helpers in tests when production error and logging structure would obscure the behavior under test.
