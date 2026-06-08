# AGENTS.md

## Project Purpose

This repository is preparing a Rust style guide that can be packaged as a skill for AI coding agents. The guide should help agents write idiomatic Rust using the project owner's conventions.

Keep the work simple, explicit, and useful for agents. Do not turn the guide into a Rust textbook.

## Key Files

- [OUTLINE.md](OUTLINE.md): topic map for the full style guide.
- [DECISIONS.md](DECISIONS.md): unresolved style decisions and suggested defaults.
- [DRAFTING.md](DRAFTING.md): drafting order, scope rules, and page-writing guidance.
- [TEMPLATE.md](TEMPLATE.md): required topic page format.
- [samples/](samples): sample topic pages showing the desired format.
- [.ai/research/](.ai/research): source research reports used to create the outline.

## Working Rules

- Read [DECISIONS.md](DECISIONS.md) before drafting or changing policy pages.
- Use [TEMPLATE.md](TEMPLATE.md) for every topic page.
- Follow [DRAFTING.md](DRAFTING.md) for drafting order and scope.
- Keep topic pages short, concrete, and mechanical enough for an agent to follow.
- Put unresolved choices in `Decision Points` instead of hiding them in prose.
- Treat the sample pages as format examples, not final policy unless the user says otherwise.
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
- Avoid adding new topic files unless the user asks to start drafting pages.
- When adding or changing decisions, update [DECISIONS.md](DECISIONS.md) and keep topic references in [OUTLINE.md](OUTLINE.md) consistent.
