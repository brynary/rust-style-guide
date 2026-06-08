# Rust Style Guide Skill

This repository is preparing a Rust style guide that can be packaged as a skill for AI coding agents. The goal is to give agents concrete, opinionated defaults for writing idiomatic Rust in the project owner's preferred style.

This is not the finished style guide yet. The current repository maps the terrain, identifies decisions to resolve, and defines the drafting format.

## Start Here

- [OUTLINE.md](OUTLINE.md): the 40-topic map for the planned guide.
- [DECISIONS.md](DECISIONS.md): style decisions to resolve before drafting final topic pages.
- [DRAFTING.md](DRAFTING.md): drafting order, page rules, and scope rules.
- [TEMPLATE.md](TEMPLATE.md): the required format for each topic page.
- [samples/](samples): sample topic pages in the intended format.
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

1. Resolve the decision register in [DECISIONS.md](DECISIONS.md).
2. Draft topic pages using [TEMPLATE.md](TEMPLATE.md).
3. Follow the drafting order in [DRAFTING.md](DRAFTING.md).
4. Use the sample pages as format references.
5. Package the final topic pages as an AI-agent skill.
