# Logging and Observability

## Rule

Use structured diagnostics: `tracing` for applications and services, and the `log` facade for broadly reusable libraries unless the project decides otherwise.

## Why

Applications need spans, structured fields, and async-aware context. Libraries should avoid forcing a subscriber or runtime choice on callers.

## Do

- Record values as fields instead of formatting them into the message.
- Use spans for request, job, command, or task lifecycles.
- Keep library instrumentation lightweight and caller-controlled.
- Use levels consistently: `trace` for very noisy details, `debug` for developer diagnostics, `info` for important lifecycle events, `warn` for degraded behavior, and `error` for failures requiring attention.
- Redact secrets and personal data.

## Avoid

- Do not log secrets, tokens, passwords, raw authorization headers, or full PII payloads.
- Do not use `println!` for diagnostics in application code.
- Do not concatenate structured values into strings when fields would work.
- Do not log and return the same error at every layer.

## Example

```rust
use tracing::{info, instrument, warn};

#[instrument(skip(store), fields(user_id = %user_id))]
pub async fn refresh_user(store: &UserStore, user_id: UserId) -> Result<(), RefreshError> {
    let user = store.load(user_id).await?;

    if user.is_suspended() {
        warn!(reason = "suspended", "skipping user refresh");
        return Ok(());
    }

    store.refresh(user).await?;
    info!("user refresh completed");

    Ok(())
}
```

## Library Notes

Reusable libraries should usually emit diagnostics through `log` or carefully chosen `tracing` instrumentation without installing a global subscriber.

## Decision Points

- Project default: `tracing`, `log`, or mixed.
- Whether libraries may depend on `tracing`.
- Standard field names for request IDs, user IDs, job IDs, and error IDs.
