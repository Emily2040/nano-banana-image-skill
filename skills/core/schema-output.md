
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
- Do not add ad-hoc top-level fields; use the schema's existing notes fields.

## Preflight and provenance notes

Encode risk/provenance guidance without changing the schema:

- In `authoring-base.json`, use `safety.person_likeness`, `safety.brand_marks`, `safety.copyright`, `safety.minors`, and `safety.policy_notes`.
- In `authoring-base.json`, use `edit.source_images[].notes` for source rights, consent boundaries, role limits, and prior generated-turn IDs.
- In `runtime-compact.json`, use `references[].notes` and `metadata.notes` for source-image rights, SynthID/provenance, documentary disclaimers, and session continuity.
- Put unsupported output limitations in notes, not fake fields.

### Transparent-background output

- Set `output.transparent_background` to `true` only when the intended pipeline can verify a real alpha channel.
- If the model request is only "transparent background", note the limitation and prompt for a cutout-ready solid matte instead.
- Runtime compact has no transparent-background field; put the requirement in `prompt` and the verification caveat in `metadata.notes`.

### Multi-turn output

- Carry stable source IDs and prior output IDs in `edit.source_images[].notes` or runtime `references[].notes`.
- Repeat preservation locks and allowed deltas in every runtime prompt after a session reset.
- Add a `metadata.notes` item when the result is generated, edited, composited, source-derived, or intended only as illustrative/simulated output.

## Companion files

See:
- `examples/authoring/README.md`
- `examples/runtime/README.md`
- `scripts/compile_runtime.py`
- `scripts/validate_repo.py`
- `references/gemini-runtime-preflight.md`
