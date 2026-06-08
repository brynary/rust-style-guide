# Decision Register

These choices should be resolved before drafting final policy pages. Suggested defaults are included to speed up discussion, not to silently settle the guide.

| ID | Decision | Options | Suggested default |
| --- | --- | --- | --- |
| D1 | Overall style bias | OO-leaning, functional-heavy, or neutral | OO-leaning Rust: structs with methods and encapsulation by default, functional style when it is clearer |
| D2 | Library vs application split | One policy for all code, or separate policies | Separate policies. Libraries are stricter; applications can be more pragmatic |
| D3 | Edition and MSRV | Rust 2021, Rust 2024, latest stable only, explicit MSRV | Rust 2024 unless constrained; always declare `rust-version` for crates |
| D4 | Error strategy for libraries | `thiserror` enums, hand-written structs, `snafu`, erased errors | Typed public errors, usually `thiserror`; revisit canonical struct style for public libraries |
| D5 | Error strategy for applications | `anyhow`, `eyre`, `miette`, domain errors everywhere | `anyhow` for internal apps/CLIs; consider `miette` for rich user-facing diagnostics |
| D6 | Panic and unwrap policy | Ban broadly, allow as assertion, allow in tests only | `Result` by default; `expect` allowed only with invariant-focused messages |
| D7 | Polymorphism default | Enum-first, trait-first, `dyn Trait`-heavy | Closed sets use enums; open extension points use traits; `dyn Trait` for runtime heterogeneity |
| D8 | OO composition style | Method forwarding manually, delegation crates, avoid forwarding | Prefer direct composition and small traits; use delegation only when it removes real boilerplate |
| D9 | Derive policy | Derive common traits eagerly, or keep impl surface minimal | Derive standard traits when semantics are obvious; hand-write `Display` |
| D10 | Clone policy | Clone liberally, borrow aggressively, context-dependent | Borrow at API boundaries; clone internally when it simplifies code and cost is small |
| D11 | Parameter flexibility | Concrete refs only, generic `AsRef`/`Into`, or mixed | Prefer `&str`, `&[T]`, and concrete refs; use generics when caller flexibility is valuable |
| D12 | Newtype aggressiveness | Wrap most primitives, only wrap domain boundaries | Use newtypes for IDs, units, validated values, and public API meaning |
| D13 | Builder style | Non-consuming builders, consuming builders, typestate builders | Use simple constructors first; use builders for many optional fields; typestate only for important invariants |
| D14 | Visibility style | Private by default, `pub(crate)` common, public fields common | Private by default; `pub(crate)` for internal seams; public fields only for plain data |
| D15 | Re-export/prelude policy | Public facade, explicit deep modules, public prelude | Use focused public facades; prelude only for broad library ecosystems |
| D16 | Async runtime | Tokio-first, runtime-agnostic, smol/minimal | Tokio-first for apps/services; runtime-agnostic surfaces for reusable libraries |
| D17 | Async task style | Free spawning, structured lifecycle, mixed | Prefer owned task lifecycle and explicit shutdown paths |
| D18 | Shared state style | Channels first, `Arc<Mutex<T>>` first, mixed | Choose the simpler model; channels for ownership transfer, locks for shared state |
| D19 | Logging stack | `tracing`, `log`, mixed | `tracing` for apps/services; `log` facade for reusable libraries |
| D20 | Clippy strictness | Minimal, curated strictness, blanket pedantic | Curated strictness; do not deny all pedantic lints by default |
| D21 | Lint overrides | `allow`, `expect`, source-local only, Cargo lints | Prefer `#[expect]` with a reason; keep project-wide lints in Cargo when practical |
| D22 | Iterator vs loop style | Iterator chains by default, loops by default, mixed | Use the clearer form; avoid clever chains when a loop communicates intent better |
| D23 | Testing posture | Unit-heavy, integration-heavy, balanced | Balanced: unit tests near logic, integration tests for public behavior, doctests for examples |
| D24 | Test tooling | Plain `cargo test`, `nextest`, `proptest`, `insta`, `criterion` | Start with `cargo test`; add tools when the code benefits from them |
| D25 | Unsafe and macros | Ban, allow with review, broad tolerance | Avoid by default; require narrow scope and written invariants when used |
