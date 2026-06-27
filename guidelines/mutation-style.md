# Mutation Style

## Rule

Use controlled mutation where it makes ownership and state changes clear: prefer `let mut` locals, `&mut self` methods on the owning type, and loops for multi-step updates; use immutable transforms for simple pure mapping.

## Why

Mutation is normal Rust. The risk is not mutation itself, but mutation with unclear ownership, wide scope, partial updates after errors, or hidden side effects.

## Do

- Use `let mut` for local accumulators, builders, counters, and staged values.
- Use `&mut self` when a method changes the state owned by the type.
- Validate fallible inputs before mutating long-lived object state.
- Keep each public mutating method responsible for preserving the type's invariants.
- Keep mutable scopes small; move back to immutable locals once setup is complete.
- Use loops for mutation, branching, early exits, or multiple accumulators.
- Use iterator chains for simple pure transforms when Clippy accepts the shape.
- Prefer computing a new value locally, then assigning it once, when that avoids partial updates.
- Use `.clone()` freely when it keeps mutation boundaries simple.
- Use `std::mem::take` or `std::mem::replace` when moving a field out while leaving the struct valid.
- Refactor to satisfy Clippy's local mutation, iterator, and control-flow guidance instead of adding line-level lint bypasses.

## Avoid

- Do not force a functional style when a small mutable local is clearer.
- Do not mutate object state before fallible validation unless the partial state is intentional and documented.
- Do not hide mutation inside iterator closures such as `map`, `filter`, or `for_each`.
- Do not expose setters for every field by habit.
- Do not mutate fields from outside the owning type unless the type is plain public data.
- Do not return references into internal mutable state when an owned snapshot would keep callers simpler.
- Do not use interior mutability just to avoid taking `&mut self`.
- Do not add local `#[allow]` or `#[expect]` attributes for Clippy mutability or iterator-vs-loop idiom lints.

## Example

Validate first, then mutate the owned state in a small block:

```rust
pub struct UserAccount {
    email:  EmailAddress,
    labels: Vec<String>,
    active: bool,
}

impl UserAccount {
    pub fn update(&mut self, update: UserUpdate) -> Result<(), Error> {
        let email = match update.email() {
            Some(value) => Some(EmailAddress::parse(value)?),
            None => None,
        };

        let mut labels = Vec::new();
        for label in update.labels() {
            labels.push(Label::parse(label)?.into_string());
        }

        if let Some(email) = email {
            self.email = email;
        }

        self.labels = labels;

        if update.deactivate() {
            self.active = false;
        }

        Ok(())
    }
}
```

Use an immutable transform when there is no stateful behavior:

```rust
pub fn normalized_labels(labels: &[String]) -> Vec<String> {
    labels
        .iter()
        .map(|label| label.trim().to_ascii_lowercase())
        .filter(|label| !label.is_empty())
        .collect()
}
```

## Exceptions

- Mutate as you go when each step is independently valid and there is no meaningful rollback requirement.
- Use interior mutability for narrow caches, shared test fixtures, adapter state, or APIs where runtime borrow checking is genuinely simpler.
- Use public mutable fields only for plain data where field mutation is the intended API.
