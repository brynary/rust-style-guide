# Ownership, Borrowing, and Clone Policy

## Rule

Prefer borrowed parameters, owned values at boundaries, and borrowed plain accessors. Clone freely to keep APIs simple, and write `.clone()` consistently for ordinary values, `Rc`, and `Arc`.

## Why

Borrowed inputs keep call sites flexible. Owned values avoid tying callers to internal lifetimes at storage and snapshot boundaries. Plain accessors should not hide ownership or allocation costs; optimize clone costs only when they are known to matter.

## Do

- Use `&self` for observation, `&mut self` for in-place mutation, and `self` for consuming transitions.
- Accept borrowed inputs such as `&str`, `&[T]`, `&Path`, and `&Thing` by default.
- Clone internally when storing a borrowed input keeps the constructor or setter simple.
- Return borrowed values from plain accessors when the lifetime is obvious.
- Return owned snapshots, IDs, handles, or collections when returning references would expose unnecessary lifetimes, and name owned snapshots explicitly.
- Use `.clone()` for ordinary values, `Rc`, and `Arc`.
- Prefer explicit owned snapshot types when callers need stable data after mutation.
- Revisit clone costs only when profiling or domain knowledge shows they matter.

## Avoid

- Do not add lifetime parameters only to avoid cheap clones.
- Do not accept owned values when the function only reads them.
- Do not hide clones in bare-noun accessors such as `labels() -> Vec<_>` or `settings() -> Arc<_>`.
- Do not return references from computed queries or snapshots when an owned value would make the API simpler.
- Do not use `Cow` by habit; reserve it for APIs that genuinely benefit from borrowed-or-owned behavior.
- Do not mix `Arc::clone(&value)` and `value.clone()` styles in the same codebase.
- Do not hide expensive deep clones in hot paths once cost is known to matter.

## Public API Notes

For internal application code, favor the simplest API and clone at boundaries. For plain accessors, borrowing is usually the simplest API. For published libraries, document ownership behavior when clones may be large or surprising.

## Example

```rust
use std::{
    path::{Path, PathBuf},
    sync::Arc,
};

#[derive(Clone, Debug)]
pub struct Settings {
    service_name: String,
    root:         PathBuf,
}

impl Settings {
    pub fn new(service_name: &str, root: &Path) -> Self {
        Self {
            service_name: service_name.to_owned(),
            root:         root.to_path_buf(),
        }
    }

    pub fn service_name(&self) -> &str {
        &self.service_name
    }

    pub fn root(&self) -> &Path {
        &self.root
    }
}

#[derive(Clone, Debug)]
pub struct Client {
    settings: Arc<Settings>,
    labels:   Vec<String>,
}

impl Client {
    pub fn new(settings: Arc<Settings>, labels: &[String]) -> Self {
        Self {
            settings,
            labels:   labels.to_vec(),
        }
    }

    pub fn settings(&self) -> &Settings {
        self.settings.as_ref()
    }

    pub fn labels(&self) -> &[String] {
        &self.labels
    }

    pub fn labels_snapshot(&self) -> Vec<String> {
        self.labels.clone()
    }

    pub fn add_label(&mut self, label: &str) {
        self.labels.push(label.to_owned());
    }

    pub fn into_labels(self) -> Vec<String> {
        self.labels
    }
}
```

Bad: hide an owned clone behind a plain accessor.

```rust
pub fn labels(&self) -> Vec<String> {
    self.labels.clone()
}
```

Good: borrow by default and name owned snapshots explicitly.

```rust
pub fn labels(&self) -> &[String] {
    &self.labels
}

pub fn labels_snapshot(&self) -> Vec<String> {
    self.labels.clone()
}
```

## Exceptions

- Accept owned values when the function consumes, stores, or forwards ownership without cloning.
- Return owned handles from methods whose names make shared ownership explicit.
- Avoid clones in measured hot paths, large data movement, or resource-heavy types.
- Use specialized clone spelling only when matching an existing local convention in code you are modifying.
