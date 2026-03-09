
# Schema Output

## Purpose

Emit structured JSON that downstream tools can trust.

## Available schemas

- `schemas/authoring-base.json`
- `schemas/runtime-compact.json`
- `schemas/pack-format.json`

## When to emit `authoring-base.json`

Use the full authoring schema when:
- a planner or UI needs a rich brief,
- the user wants traceable assumptions,
- multiple stages or editors will touch the prompt,
- continuity or preservation logic needs to be explicit.

## When to emit `runtime-compact.json`

Use the compact runtime schema when:
- the prompt is ready to run,
- the user wants API-oriented output,
- you need a clean handoff to a generator or editor.

## Minimal runtime example

```json
{
  "schema_version": "1.0.0",
  "mode": "generate",
  "model": "gemini-3.1-flash-image-preview",
  "prompt": "Create a rain-soaked neon alley from a low drone perspective...",
  "aspect_ratio": "16:9",
  "image_size": "2K",
  "profile": "vfx-shot"
}
```

## Rich authoring example

```json
{
  "schema_version": "1.0.0",
  "task": "edit",
  "model_target": {
    "family": "nano-banana-pro",
    "api_model": "gemini-3-pro-image-preview",
    "reason": "Strict preservation and premium label fidelity."
  },
  "intent": {
    "goal": "Upgrade packshot drama without changing product identity.",
    "audience": "Luxury skincare buyers",
    "use_case": "Campaign still"
  }
}
```

## Output habits

- Keep enumerations canonical.
- Prefer arrays for repeated constraints.
- Keep prompt text inside the schema synchronized with the human-readable brief.
- Validate examples after every schema change.

## Companion files

See:
- `examples/authoring/README.md`
- `examples/runtime/README.md`
- `scripts/compile_runtime.py`
- `scripts/validate_repo.py`
