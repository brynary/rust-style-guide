# Guideline Page Template

Use this format for Rust style guide guideline pages.

```markdown
# Guideline Name

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

## Example

Small preferred example.

## Exceptions

Narrow cases where the default can be broken.
```

Optional sections:

- `Activation`
- `Library vs Application`
- `Async Notes`
- `Public API Notes`
- `Safety Notes`
- `Decision Points`

Use `Activation` for conditional or advanced guideline pages such as async, typestate, unsafe code, macros, and specialized tooling. It should say when to load the page and when not to.
