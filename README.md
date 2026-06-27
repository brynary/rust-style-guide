# Rust Style Guide Skill

This repository contains a Rust style guide that can be packaged as a skill for AI coding agents. The goal is to give agents concrete, opinionated defaults for writing idiomatic Rust in the project owner's preferred style.

The current packaged skill shape is `SKILL.md`, `agents/openai.yaml`, and focused topic pages under `references/`. Planning files remain in the repo as source material, but ordinary skill use should load only the router and relevant references.

## Start Here

- [SKILL.md](SKILL.md): root skill router for progressive disclosure.
- [agents/openai.yaml](agents/openai.yaml): UI metadata for the packaged skill.
- [references/topics.md](references/topics.md): topic index for the packaged skill.
- [references/](references): focused Rust style policy pages.
- [OUTLINE.md](OUTLINE.md): the 40-topic map used to draft the guide.
- [DECISIONS.md](DECISIONS.md): resolved style decision register.
- [DRAFTING.md](DRAFTING.md): drafting order, page rules, and scope rules.
- [TEMPLATE.md](TEMPLATE.md): the required format for each topic page.
- [AGENTS.md](AGENTS.md): repository instructions for AI coding agents.

## Research

The source research reports live in [.ai/research/](.ai/research). They were used to synthesize the outline and decision register. Treat them as background material, not as final policy.

## Intended Style

The guide should be Rust-idiomatic with an OO-leaning default:

- Prefer structs with methods and clear encapsulation when natural.
- Do not force inheritance-shaped designs into Rust.
- Prefer enums for closed sets and traits for open extension points.
- Prefer explicit, compiler-backed types over primitive-heavy APIs.
- Keep public library guidance stricter than internal application guidance.

## Workflow

1. Update [DECISIONS.md](DECISIONS.md) when policy changes.
2. Update the relevant page under [references/](references).
3. Keep [references/topics.md](references/topics.md) linked to every packaged reference page.
4. Keep [SKILL.md](SKILL.md) small and route through progressive disclosure.
5. Use [DRAFTING.md](DRAFTING.md) and [TEMPLATE.md](TEMPLATE.md) only when adding or reshaping pages.

## Packaging Model

The skill uses progressive disclosure:

- `SKILL.md` stays small and routes tasks to relevant references.
- `agents/openai.yaml` provides user-facing skill metadata.
- `references/topics.md` indexes the available topic pages.
- Focused topic pages live under `references/`.
- Planning files like `README.md`, `OUTLINE.md`, `DRAFTING.md`, `DECISIONS.md`, and `.ai/research/` stay outside the packaged skill unless explicitly needed.
