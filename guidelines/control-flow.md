# Control Flow

## Rule

Use clarity-first branching: prefer `?`, `let else`, `if let`, `while let`, and `match` when they make branches and exits explicit; use combinators only for simple local transformations.

## Why

Control flow carries invariants, error paths, and state transitions. Explicit branches are easier for agents to modify safely than clever expression chains that hide exits or side effects.

## Do

- Use `?` when the local code only needs to propagate a fallible result.
- Use early returns for invalid inputs, missing prerequisites, and permission checks.
- Use `let else` when a required pattern must be present and the fallback exits the current scope.
- Use `if let` when only one pattern needs special handling.
- Use `while let` for loops that repeatedly consume optional or result-like values.
- Use `match` when multiple variants matter, exhaustiveness matters, or each branch has distinct behavior.
- Keep `match` arms small; extract a helper when a branch grows past the local decision.
- Prefer naming meaningful enum variants over `_` when future variants should force a revisit.
- Use match guards only when the guard is short and directly tied to the arm.
- Keep the main path linear after validation and setup.
- Treat Clippy as authoritative for local control-flow idioms; refactor to satisfy it when it recommends a simpler branch or combinator.

## Avoid

- Do not write long chains of `map`, `and_then`, `or_else`, and `inspect` when the code is really branching.
- Do not add local `#[allow]` or `#[expect]` attributes for Clippy control-flow idiom lints just to keep a preferred style.
- Do not hide side effects inside combinator closures.
- Do not use `match` on `bool`; use `if` with a named condition.
- Do not use `_` to ignore meaningful domain states.
- Do not deeply nest `if` or `match` blocks when guard clauses would make exits clearer.
- Do not use `let else` when the fallback contains substantial recovery logic; use `match`.
- Do not replace explicit error handling with `unwrap` or `expect`.

## Example

Prefer visible exits and exhaustive domain handling:

```rust
pub fn plan_action(request: Request) -> Result<Action, Error> {
    let Some(user_id) = request.user_id() else {
        return Err(Error::MissingUserId);
    };

    let command = Command::parse(request.command())?;

    if !request.permissions().can_run(&user_id, &command) {
        return Err(Error::Forbidden { user_id });
    }

    let action = match command {
        Command::Start { target } => {
            let target = Target::try_new(target)?;
            Action::Start { target }
        }
        Command::Stop { target } => Action::Stop { target },
        Command::Status => Action::Status,
    };

    Ok(action)
}
```

Use combinators for simple local transformations:

```rust
impl User {
    pub fn display_name(&self) -> String {
        self.nickname()
            .filter(|name| !name.is_empty())
            .unwrap_or_else(|| self.username())
            .to_owned()
    }
}
```

## Exceptions

- Use combinators when the transformation is short, linear, and side-effect free.
- Use `_` for intentionally ignored variants in tests, logging, metrics, or external `#[non_exhaustive]` enums.
- Use a `match` even for two cases when it documents a domain state machine or prepares for likely new variants.
