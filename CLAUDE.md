
# Nano Banana Image Skill

This repository is a project skill pack for image prompt authoring.

## Start here

1. Read `SKILL.md`.
2. Use `skills/core/` for modular behavior.
3. Use `schemas/` and `examples/` when generating structured output.

## Repo intent

The repo teaches agents how to:
- interview image requests efficiently,
- ground scenes and edits,
- route style and output profiles,
- preserve identity across edits,
- compile clean prompts for Nano Banana Pro and Nano Banana 2,
- emit structured JSON.

## Editing rules

- Keep `SKILL.md` focused; move detail outward.
- Preserve cross-agent compatibility files:
  - `AGENTS.md`
  - `CLAUDE.md`
  - `GEMINI.md`
- Keep examples validating against the schemas.
- Keep the `docs/` front-end polished and functional.

## Preferred answer shape

For prompt tasks:
- model target
- assumptions
- production prompt
- preserve / avoid block
- runtime JSON

For repo changes:
- edit the relevant file(s)
- install dev dependencies before full validation
- run validation if possible
- update examples when behavior shifts
