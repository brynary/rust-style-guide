# AGENTS.md

## Project Purpose

This repository is preparing a Rust style guide that can be packaged as a skill for AI coding agents. The guide should help agents write idiomatic Rust using the project owner's conventions.

Keep the work simple, explicit, and useful for agents. Do not turn the guide into a Rust textbook.

## Key Files

- [OUTLINE.md](OUTLINE.md): guideline map for the full style guide.
- [DECISIONS.md](DECISIONS.md): unresolved style decisions and suggested defaults.
- [DRAFTING.md](DRAFTING.md): drafting order, scope rules, and page-writing guidance.
- [TEMPLATE.md](TEMPLATE.md): required guideline page format.
- [SKILL.md](SKILL.md): Codex-required skill entrypoint.
- [root.md](root.md): root router for the packaged skill.
- [guidelines.md](guidelines.md): guideline index for progressive disclosure.
- [guidelines/](guidelines): focused Rust style policy pages.
- [workflows/](workflows): procedural workflows for larger tasks.
- [.ai/research/](.ai/research): source research reports used to create the outline.

## Working Rules

- Read [DECISIONS.md](DECISIONS.md) before drafting or changing policy pages.
- Use [TEMPLATE.md](TEMPLATE.md) for every guideline page.
- Follow [DRAFTING.md](DRAFTING.md) for drafting order and scope.
- Keep guideline pages short, concrete, and mechanical enough for an agent to follow.
- Put unresolved choices in `Decision Points` instead of hiding them in prose.
- Keep [SKILL.md](SKILL.md) and [root.md](root.md) small. Put detailed policy in `guidelines/` and procedures in `workflows/`.
- Link guideline and workflow files directly from [root.md](root.md), [guidelines.md](guidelines.md), or [SKILL.md](SKILL.md); avoid deep reference chains.
- Do not edit files in [.ai/research/](.ai/research) unless explicitly asked.

## Style Guide Bias

The intended guide is Rust-idiomatic with an OO-leaning default:

- Prefer structs with methods and clear encapsulation when that feels natural.
- Do not force inheritance-shaped designs into Rust.
- Prefer enums for closed sets and traits for open extension points.
- Prefer explicit, compiler-backed types over primitive obsession.
- Keep library guidance stricter than application guidance.

## Editing Expectations

- Preserve ASCII-only markdown unless a file already uses non-ASCII intentionally.
- Keep changes narrowly scoped to the requested document.
- Avoid adding new guideline or workflow files unless the user asks to start drafting pages.
- When adding or changing decisions, update [DECISIONS.md](DECISIONS.md) and keep topic references in [OUTLINE.md](OUTLINE.md) consistent.
- Do not include planning docs or research reports in the final packaged skill unless explicitly requested.
