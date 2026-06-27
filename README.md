# Rust Style Guide Skill

This repository contains a Rust style guide that can be packaged as a skill for AI coding agents. The goal is to give agents concrete, opinionated defaults for writing idiomatic Rust in the project owner's preferred style.

The current packaged skill shape is `SKILL.md`, `root.md`, `agents/openai.yaml`, focused policy pages under `guidelines/`, and procedure pages under `workflows/`. Planning files remain in the repo as source material, but ordinary skill use should load only the router and relevant guidelines or workflows.

## Start Here

- [SKILL.md](SKILL.md): root skill router for progressive disclosure.
- [root.md](root.md): human-readable router for guidelines and workflows.
- [agents/openai.yaml](agents/openai.yaml): UI metadata for the packaged skill.
- [guidelines.md](guidelines.md): guideline index for the packaged skill.
- [guidelines/](guidelines): focused Rust style policy pages.
- [workflows/](workflows): procedural workflows for larger tasks.
- [OUTLINE.md](OUTLINE.md): the guideline map used to draft the guide.
- [DECISIONS.md](DECISIONS.md): resolved style decision register.
- [DRAFTING.md](DRAFTING.md): drafting order, page rules, and scope rules.
- [TEMPLATE.md](TEMPLATE.md): the required format for each guideline page.
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
2. Update the relevant page under [guidelines/](guidelines) or [workflows/](workflows).
3. Keep [guidelines.md](guidelines.md) linked to every packaged guideline page.
4. Keep [SKILL.md](SKILL.md) small and route through progressive disclosure.
5. Run `bash checks/check.sh` before committing skill changes.
6. Use [DRAFTING.md](DRAFTING.md) and [TEMPLATE.md](TEMPLATE.md) only when adding or reshaping pages.

## Packaging Model

The skill uses progressive disclosure:

- `SKILL.md` stays small and routes tasks to relevant guidelines and workflows.
- `root.md` describes the guideline/workflow routing model.
- `agents/openai.yaml` provides user-facing skill metadata.
- `guidelines.md` indexes the available guideline pages.
- Focused policy pages live under `guidelines/`.
- Procedural pages live under `workflows/`.
- Planning files like `README.md`, `OUTLINE.md`, `DRAFTING.md`, `DECISIONS.md`, and `.ai/research/` stay outside the packaged skill unless explicitly needed.
