# Topic Page Template

Use this format for Rust style guide topic pages.

```markdown
# Topic Name

## Rule

One sentence the agent can follow by default.

## Why

Short rationale.

## Do

- Preferred patterns.
- Naming or API conventions.

## Avoid

- Common anti-patterns.
- Cases where agents usually overreach.

## Exceptions

Narrow cases where the default can be broken.

## Example

Small preferred example.
```

Optional sections:

- `Activation`
- `Library vs Application`
- `Async Notes`
- `Public API Notes`
- `Safety Notes`
- `Decision Points`

Use `Activation` for conditional or advanced pages such as async, typestate, unsafe code, macros, and specialized tooling. It should say when to load the page and when not to.
