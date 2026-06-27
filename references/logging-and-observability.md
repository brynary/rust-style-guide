# Logging and Observability

## Rule

Use `tracing` for structured operation traces: spans for operations, fields for IDs and state, events for meaningful milestones and failures, and fixed message strings instead of prose-only logs.

## Why

Structured traces make logs searchable, aggregatable, and useful after the fact. Fixed messages identify event kinds, while fields carry the data that changes per run.

## Do

- Use `tracing` everywhere; applications configure subscribers and libraries only emit spans and events.
- Add spans around meaningful operations such as requests, jobs, commands, tasks, external calls, and workflow steps.
- Attach structured fields for IDs, names, states, attempts, counts, durations, and safe error summaries.
- Use fixed message strings; put variable data in fields.
- Keep INFO low-volume and high-signal: startup, shutdown, operation start/end, and key outcomes.
- Use DEBUG for investigation detail: branches taken, retries, resolved config, request metadata, and intermediate state.
- Use WARN for degraded behavior or retryable unexpected conditions.
- Use ERROR when the current operation failed and cannot continue.
- Log errors in an `error` field and render or collect full cause chains deliberately at boundaries that need them.
- Use snake_case field names consistently across the codebase.
- Prefer counts, byte lengths, hashes, redacted displays, or booleans over raw sensitive values.

## Avoid

- Do not interpolate variable values into the message string.
- Do not log prose-only messages when fields would make the event queryable.
- Do not duplicate events already emitted by a parent operation or domain event.
- Do not log hot loops, per-token streams, or high-cardinality chatter at INFO.
- Do not configure a subscriber inside reusable libraries.
- Do not use tracing events as user-facing CLI or API output.
- Do not log secrets, API keys, bearer tokens, cookies, raw credentials, unredacted URLs, raw command output, or request bodies.
- Do not rely on logs for behavior that should be represented as durable events, metrics, or user-visible output.

## Library vs Application

Libraries may depend on `tracing` and emit events, but they should not initialize global subscribers or choose output formats. Applications own subscriber setup, filtering, formatting, destinations, and propagation to worker processes.

## Example

```rust
use tracing::{debug, error, info, warn, Instrument};

pub async fn sync_account(account_id: AccountId, client: &BillingClient) -> Result<(), SyncError> {
    let span = tracing::info_span!("sync_account", account_id = %account_id);

    async move {
        info!("Starting account sync");

        let invoices = client
            .list_invoices(account_id)
            .await
            .map_err(SyncError::ListInvoices)?;

        debug!(invoice_count = invoices.len(), "Listed invoices");

        for invoice in invoices {
            if invoice.is_stale() {
                warn!(invoice_id = %invoice.id(), "Skipping stale invoice");
                continue;
            }

            client
                .sync_invoice(&invoice)
                .await
                .map_err(SyncError::SyncInvoice)?;
        }

        info!("Account sync complete");
        Ok(())
    }
    .instrument(span)
    .await
}

pub fn log_sync_failure(account_id: AccountId, error: &SyncError) {
    error!(account_id = %account_id, error = %error, "Account sync failed");
}
```

Prefer this shape over interpolated messages:

```rust
info!(account_id = %account_id, invoice_count = count, "Account sync complete");
```

Avoid:

```rust
info!("Account {account_id} sync complete with {count} invoices");
```

## Exceptions

- Use plain `println!` or `eprintln!` for intentional user-facing CLI output, not developer logs.
- Add more DEBUG detail temporarily while investigating a hard problem, then keep only the durable signal.
- Use metrics or durable domain events instead of logs when data must drive alerts, billing, audit, or product behavior.
