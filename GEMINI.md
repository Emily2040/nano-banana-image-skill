
# Nano Banana Image Skill

This repository contains a portable image-prompting skill pack.

@./SKILL.md

## Additional context

- `README.md` explains installation and cross-agent usage.
- `schemas/authoring-base.json` defines the rich authoring contract.
- `schemas/runtime-compact.json` defines the compact runtime payload.
- `skills/core/` contains modular prompting logic.
- `examples/` provides valid sample inputs and outputs.

## Guidance

- Keep responses concrete and model-aware.
- Prefer explicit composition, lighting, and layout instructions over generic quality filler.
- For edits, preserve unchanged elements explicitly before describing changes.
- When modifying the repo, keep `docs/` intact and update examples with schema changes.

## Gemini API/runtime notes

- Current public Gemini image generation docs use `generateContent` and can return text parts plus inline image data.
- Documented image model IDs include `gemini-3-pro-image-preview` for Nano Banana Pro, `gemini-3.1-flash-image-preview` for Nano Banana 2 / V2, and `gemini-2.5-flash-image` for the legacy Nano Banana fast path.
- Runtime payloads should keep prompt text, image config, source references, and provenance notes separate.
