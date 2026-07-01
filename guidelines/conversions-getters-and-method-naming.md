# Conversions, Getters, and Method Naming

## Rule

Prefer concrete borrowed parameters, borrowed field-like accessors, and owned return values for conversions, snapshots, and builders. Use generic conversion bounds only when they clearly help callers.

## Why

Concrete refs make APIs easy to read and call. Owned returns and internal clones avoid unnecessary lifetime coupling when a method builds independent data. Rust method names carry ownership and allocation expectations, so field-like accessors should borrow, while `as_`, `to_`, and `into_` should be used consistently.

## Do

- Accept `&str`, `&[T]`, `&Path`, and concrete refs for read-only inputs by default.
- Clone internally when a constructor stores a normalized or derived value from borrowed input, or when returning an explicitly owned result keeps the API simpler.
- Return borrowed values from cheap field-like accessors where the lifetime is obvious.
- Return owned values from queries, snapshots, and builders when returning references would expose unnecessary lifetimes.
- Use `impl AsRef<Path>` or similar bounds only when the API is clearly path-like and caller flexibility helps.
- Take owned values or `impl Into<T>` in constructors and setters that store the value unchanged.
- Use `From` for infallible, obvious conversions.
- Use `TryFrom` or `FromStr` for validation and fallible parsing.
- Use `From` for lossless numeric widening and `TryFrom` or `TryInto` for narrowing or signedness changes.
- Choose explicit integer overflow behavior with `checked_*`, `saturating_*`, `wrapping_*`, or `overflowing_*` when overflow is possible and meaningful.
- Use `as_*` for cheap borrowed or scalar views.
- Use `to_*` for cloning, allocation, or conversion without consuming `self`.
- Use `into_*` for consuming conversions.
- Use Rust-style accessors such as `id()`, `name()`, and `status()` instead of `get_id()`.
- Use boolean names such as `is_active()`, `has_children()`, and `can_retry()`.

## Avoid

- Do not add generic `AsRef`, `Into`, or `Borrow` bounds to every parameter by habit.
- Do not accept owned `String`, `Vec<T>`, or `PathBuf` unless the API consumes ownership or the owned type is the natural input.
- Do not expose named lifetimes just to avoid cheap clones.
- Do not use bare-noun accessors for owned snapshots, such as `labels() -> Vec<_>`.
- Do not use `From` for conversions that can fail, validate, allocate surprisingly, or lose important meaning.
- Do not use `as` for narrowing numeric casts or float-to-integer conversion unless range, sign, and NaN behavior are checked locally.
- Do not use `as_*` for methods that allocate or clone.
- Do not use `==` for approximate float equality; use a named tolerance, and use `total_cmp` when sorting floats that may include NaN.
- Do not use `get_*` for simple field-like accessors.
- Do not implement `Deref` just to forward methods from an inner value.
- Do not use `Borrow` as a general-purpose parameter-flexibility tool; reserve it for lookup/key equivalence patterns.

## Public API Notes

For public APIs, prefer the simplest signature that communicates the contract. A concrete `&Path` or `&str` is usually clearer than a generic bound. Generic bounds are useful when they remove real caller friction without spreading type parameters through the API.

Trait impls such as `From`, `TryFrom`, `AsRef`, and `Deref` become part of the public API. Add them only when the conversion semantics are stable.

## Example

```rust
use std::fmt;
use std::path::{Path, PathBuf};
use std::str::FromStr;

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct ProjectName(String);

impl ProjectName {
    pub fn try_new(value: &str) -> Result<Self, ProjectNameError> {
        let value = value.trim();

        if value.is_empty() {
            return Err(ProjectNameError::Empty);
        }

        Ok(Self(value.to_owned()))
    }

    pub fn as_str(&self) -> &str {
        &self.0
    }

    pub fn to_slug(&self) -> String {
        self.0.to_ascii_lowercase().replace(' ', "-")
    }

    pub fn into_string(self) -> String {
        self.0
    }
}

impl fmt::Display for ProjectName {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        formatter.write_str(self.as_str())
    }
}

impl FromStr for ProjectName {
    type Err = ProjectNameError;

    fn from_str(value: &str) -> Result<Self, Self::Err> {
        Self::try_new(value)
    }
}

impl From<ProjectName> for String {
    fn from(name: ProjectName) -> Self {
        name.into_string()
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum ProjectNameError {
    Empty,
}

#[derive(Clone, Debug)]
pub struct ProjectConfig {
    root: PathBuf,
    name: ProjectName,
}

impl ProjectConfig {
    pub fn new(root: PathBuf, name: ProjectName) -> Self {
        Self { root, name }
    }

    pub fn root(&self) -> &Path {
        &self.root
    }

    pub fn name(&self) -> &ProjectName {
        &self.name
    }

    pub fn snapshot(&self) -> ProjectConfigSnapshot {
        ProjectConfigSnapshot {
            root: self.root.clone(),
            name: self.name.clone(),
        }
    }
}

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct ProjectConfigSnapshot {
    pub root: PathBuf,
    pub name: ProjectName,
}
```

## Exceptions

- Accept owned values when the function consumes them, stores them without cloning, or mirrors a standard library convention.
- Use generic bounds in low-level utilities where caller flexibility is the main point of the function.
- Return owned snapshots from methods whose names signal ownership, such as `snapshot`, `to_*`, or `*_snapshot`.
- Use `get_*` for keyed lookups, cache retrieval, or fallible/computed access where the method is not simple field-like observation.
