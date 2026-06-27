# Strings, Slices, and Flexible Parameters

## Rule

Accept concrete borrowed string, slice, and path parameters by default; store owned values; use flexible generic bounds only when they clearly improve caller ergonomics.

## Why

`&str`, `&[T]`, and `&Path` make APIs easy to read and accept the common owned and borrowed caller types. Storing `String`, `Vec<T>`, and `PathBuf` keeps lifetimes out of structs and return values. Generic bounds are useful, but overusing them makes signatures harder for agents and humans to reason about.

## Do

- Accept `&str` instead of `&String` for read-only text.
- Accept `&[T]` instead of `&Vec<T>` for read-only sequences.
- Accept `&Path` instead of `&PathBuf` for read-only paths.
- Store owned `String`, `Vec<T>`, and `PathBuf` inside structs.
- Clone, `to_owned`, `to_vec`, or `to_path_buf` at the boundary when storing borrowed inputs.
- Return owned snapshots when callers need stable data independent of the owner.
- Use `IntoIterator` for APIs whose purpose is to consume or extend from a sequence of items.
- Use `AsRef<str>` or `AsRef<Path>` only when caller flexibility clearly helps and the bound stays local.
- Use `impl Into<String>` mostly for constructors or setters that immediately store the owned value.
- Accept `impl Read` or `impl Write` when a reusable library should test I/O behavior without touching the filesystem.
- Use `Cow` only when the API genuinely often borrows but sometimes allocates, and the lifetime stays local.

## Avoid

- Do not accept `&String`, `&Vec<T>`, or `&PathBuf` by habit.
- Do not store borrowed references in structs just to avoid allocation.
- Do not return borrowed data when an owned value would avoid awkward lifetimes.
- Do not add `AsRef`, `Into`, `Borrow`, or generic type parameters to every function by default.
- Do not use `Cow` as a general-purpose way to avoid deciding between borrowed and owned data.
- Do not accept owned `String`, `Vec<T>`, or `PathBuf` for functions that only read the input.
- Do not use `Borrow` for ordinary parameter flexibility; reserve it for key-equivalence and lookup patterns.

## Public API Notes

For public APIs, concrete borrowed refs are usually clearer than generic bounds. Add flexible bounds when they materially reduce caller friction and do not leak type parameters through the API.

For application internals, prefer the simplest signature and clone at the boundary.

## Example

```rust
use std::{
    borrow::Cow,
    path::{Path, PathBuf},
};

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct FileMatcher {
    root:       PathBuf,
    extensions: Vec<String>,
}

impl FileMatcher {
    pub fn new(root: &Path, extensions: &[String]) -> Self {
        Self {
            root:       root.to_path_buf(),
            extensions: extensions.to_vec(),
        }
    }

    pub fn from_extensions<I, S>(root: &Path, extensions: I) -> Self
    where
        I: IntoIterator<Item = S>,
        S: AsRef<str>,
    {
        let extensions = extensions
            .into_iter()
            .map(|extension| normalize_extension(extension.as_ref()).into_owned())
            .collect();

        Self {
            root: root.to_path_buf(),
            extensions,
        }
    }

    pub fn add_extension(&mut self, extension: &str) {
        self.extensions
            .push(normalize_extension(extension).into_owned());
    }

    pub fn matches_extension(&self, extension: &str) -> bool {
        let extension = normalize_extension(extension);

        self.extensions
            .iter()
            .any(|candidate| candidate.as_str() == extension.as_ref())
    }

    pub fn root(&self) -> &Path {
        &self.root
    }

    pub fn path_for(&self, relative: &Path) -> PathBuf {
        self.root.join(relative)
    }

    pub fn extensions(&self) -> &[String] {
        &self.extensions
    }

    pub fn extension_names(&self) -> Vec<String> {
        self.extensions.clone()
    }
}

pub fn normalize_extension(extension: &str) -> Cow<'_, str> {
    let trimmed = extension.trim();
    let normalized = trimmed.strip_prefix('.').unwrap_or(trimmed);

    if normalized.len() == extension.len() {
        Cow::Borrowed(extension)
    } else {
        Cow::Owned(normalized.to_owned())
    }
}
```

## Exceptions

- Accept owned values when the function consumes ownership, stores without cloning, or mirrors a standard library convention.
- Use `impl AsRef<Path>` for top-level file-opening helpers when accepting many path-like caller types is the main ergonomic benefit.
- Use `impl Read` or `impl Write` for lower-level helpers whose purpose is data processing, not path handling.
- Use `Cow` in parsing, normalization, and formatting helpers that can usually return a borrowed value.
- Use slices of references, such as `&[&str]`, when the call sites naturally already have borrowed items.
