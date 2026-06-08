# Drafting Instructions

Use these instructions when turning the outline into topic pages.

## Priorities

1. Resolve the decision register in [DECISIONS.md](DECISIONS.md).
2. Draft the core pages first: errors, panics, type/API design, ownership, async, logging, linting, and testing.
3. Add advanced pages only where the target codebase needs them.
4. Keep every page mechanical enough for an agent to follow.

## Drafting Order

1. Foundations
2. Errors, safety, and diagnostics
3. Type and API design
4. Ownership and data flow
5. Async and concurrency
6. Tooling and project shape
7. Everyday implementation
8. Testing and release

## Page Rules

- Use [TEMPLATE.md](TEMPLATE.md) for every topic page.
- Make the `Rule` section a direct default, not a discussion.
- Keep `Why` short and practical.
- Prefer concrete guidance over philosophy.
- Include exceptions only when an agent could reasonably encounter them.
- Add a small preferred Rust example when the topic affects code shape.
- Put unresolved choices in `Decision Points` instead of burying them in prose.

## Scope Rules

- Do not re-teach Rust syntax or ownership basics unless a style choice depends on them.
- Do not include long surveys of ecosystem options on topic pages.
- Do not add advanced topics unless they affect likely agent output.
- Keep library/application differences explicit when the right answer changes by context.
- Treat public API guidance as stricter than internal application guidance.
