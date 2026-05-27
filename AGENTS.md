
# Nano Banana Image Skill — AGENTS instructions

This repository is a portable image-prompting skill pack.

## Canonical entrypoint

Read `SKILL.md` first.  
Treat `SKILL.md` as the authoritative workflow for prompt authoring, editing, routing, preservation, and JSON emission.

## Secondary files

Use these on demand:

- `README.md` for installation, examples, and repo intent
- `schemas/authoring-base.json` for rich creative briefs
- `schemas/runtime-compact.json` for final runtime payloads
- `registry/` for aliases, style axes, token budgets, and slop scrubbing
- `skills/core/` for modular prompting logic
- `examples/` for ground-truth samples
- `scripts/compile_runtime.py` to compile authoring JSON into runtime JSON
- `scripts/validate_repo.py` to validate the pack

## Working agreements

- Preserve the exact folder layout unless explicitly asked to restructure it.
- Keep `SKILL.md` concise and move deep details into modular files.
- Prefer editing the most specific file rather than stuffing every rule into the root.
- When adding new style modules, update:
  - `registry/style-axes.md`
  - `registry/aliases.json`
  - example files if behavior changes materially
- When changing schemas, validate the examples immediately after.
- Do not remove the `docs/` site; it is part of the package front-end.
- Before full validation, install dev dependencies with `python -m pip install -r requirements-dev.txt`.

## Expected outputs

For user-facing prompt work, return:
1. chosen model target,
2. assumptions,
3. production prompt,
4. preserve / avoid notes when relevant,
5. runtime JSON when useful.

For repository work, update files directly and keep examples consistent.

## Aesthetic bar

The pack should feel precise, elegant, and operational — not like a blender full of adjectives.
