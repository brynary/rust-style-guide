# Drafting Instructions

Use these instructions when turning the outline into guideline pages.

## Priorities

1. Resolve the decision register in [DECISIONS.md](DECISIONS.md).
2. Keep [SKILL.md](SKILL.md) and [root.md](root.md) small and use them as routers.
3. Draft the core guideline pages first: errors, panics, type/API design, ownership, async, logging, linting, and testing.
4. Add workflow pages only where repeated task procedures need more than policy.
5. Add advanced guideline pages only where the target codebase needs them.
6. Keep every page mechanical enough for an agent to follow.

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

- Use [TEMPLATE.md](TEMPLATE.md) for every guideline page.
- Give every rule exactly one owner page; sibling pages may carry at most a one-line reminder that links to the owner.
- Make examples demonstrate only the owning page's rules; incidental code in an example follows other pages' rules but does not showcase them.
- Make the `Rule` section a direct default, not a discussion.
- Keep `Why` short and practical.
- Prefer concrete guidance over philosophy.
- Include exceptions only when an agent could reasonably encounter them.
- Add a small preferred Rust example when the topic affects code shape.
- Put unresolved choices in `Decision Points` instead of burying them in prose.

## Progressive Disclosure

- Treat [SKILL.md](SKILL.md) as the Codex entrypoint and [root.md](root.md) as the root router, not the guide itself.
- Keep detailed policy in `guidelines/` pages.
- Keep procedural task flows in `workflows/` pages.
- Keep [guidelines.md](guidelines.md) as the one-page guideline index.
- Link guideline and workflow files directly from [root.md](root.md), [guidelines.md](guidelines.md), or [SKILL.md](SKILL.md); avoid deep reference chains.
- Do not load every guideline page for ordinary tasks.
- Use routing examples for common task types so agents know which pages to load.

## Scope Rules

- Do not re-teach Rust syntax or ownership basics unless a style choice depends on them.
- Do not include long surveys of ecosystem options on guideline pages.
- Do not add advanced topics unless they affect likely agent output.
- Keep library/application differences explicit when the right answer changes by context.
- Treat public API guidance as stricter than internal application guidance.
- Do not package planning files or research reports into the final skill unless the user explicitly asks for them.
