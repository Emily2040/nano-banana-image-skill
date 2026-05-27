# Nano Banana Image Skill — Orchestrator

Use this skill to turn image requests into **clean, grounded, model-aware prompts** and **structured JSON** for Nano Banana Pro and Nano Banana 2.

## Use this skill when

Activate this skill when the user needs any of the following:

- prompt writing for Gemini image generation,
- image editing instructions that preserve identity or layout,
- text-in-image posters, covers, infographics, or labels,
- style translation across anime, manga, photoreal, 3D, historical, fantasy, sci-fi, and culture-specific treatments,
- continuity across variants, episodes, campaigns, or character sheets,
- conversion of loose art direction into reusable JSON payloads.

## Do not use this skill when

- the task is ordinary image captioning with no need for prompt authoring,
- the task is pure policy review with no image-creation component,
- the request is only about code unrelated to image generation or image editing.

## Operating principles

1. **Ask only for missing critical information.**  
   Use `skills/core/interview.md` and `registry/interview-question-bank.json`.  
   Default intelligently when the user is indifferent.

2. **Ground the world before styling it.**  
   Use `skills/core/grounding.md`, `skills/core/world-model.md`, and `skills/core/evidence-discipline.md`.  
   Lock down what is observed, what is requested, and what is inferred.

3. **Route style as a stack, not a soup.**  
   Use `skills/core/style-router.md` and `registry/style-axes.md`.  
   Typical stack order:
   - family
   - genre
   - movement or culture
   - capture or pipeline
   - render features
   - profile
   - platform
   - overlays

4. **Prefer explicit physical instructions over decorative fluff.**  
   "35mm lens, waist-up portrait, sodium-vapor backlight, rain sheen on black nylon" beats "masterpiece ultra detailed cinematic."

5. **For edits, speak in deltas.**  
   Preserve first. Change second.  
   Use `skills/core/preservation.md` and `skills/core/edit-delta.md`.

6. **Treat typography as layout.**  
   Use `skills/core/text-layout.md` plus the relevant platform and profile docs.  
   Specify hierarchy, safe margins, alignment, and what must remain unobstructed.

7. **Produce two outputs whenever practical.**
   - a readable production brief,
   - a structured JSON payload matching `schemas/runtime-compact.json`.

## Default workflow

### Step 1 — classify the job

Use `skills/core/router.md`.

Choose one primary mode:
- `generate`
- `edit`
- `composite`
- `relight`
- `outpaint`
- `variation`

Then choose the best model target:

- Prefer **Nano Banana Pro** for:
  - heavy typography,
  - infographics,
  - poster composition,
  - complex multi-part instructions,
  - premium client deliverables,
  - strict preservation edits.

- Prefer **Nano Banana 2** for:
  - rapid iteration,
  - fast concept work,
  - batch ideation,
  - simpler edits,
  - variant exploration.

### Step 2 — run the minimum interview

Use `skills/core/interview.md`.

Collect or infer:
- subject,
- action,
- setting,
- viewpoint,
- output profile,
- style family,
- must-keep elements,
- must-avoid elements,
- platform or aspect ratio,
- text requirements.

If the request is already specific, do not interrogate the poor mortal further.

### Step 3 — bind evidence and references

Use:
- `skills/core/reference-binding.md`
- `skills/core/evidence-discipline.md`
- `skills/core/preservation.md`

Rules:
- Never invent reference details that were not visible.
- For identity-sensitive edits, list preserved traits explicitly.
- If two references conflict, prefer the one the user names as primary. Otherwise preserve geometry first, then materials, then color.

### Step 4 — build the style stack

Use:
- `skills/core/style-router.md`
- `registry/style-axes.md`
- relevant files under `skills/families/`, `skills/genres/`, `skills/movements/`, `skills/cultures/`, `skills/capture/`, `skills/pipelines/`, `skills/render-features/`, `skills/profiles/`, `skills/platforms/`, `skills/overlays/`

Choose only what materially improves the result.
A short coherent stack is stronger than a hoarder's attic of style tags.

### Step 5 — direct composition and light

Use:
- `skills/core/composition-camera.md`
- `skills/core/lighting-materials.md`
- `skills/core/aesthetic-director.md`

Always decide:
- framing,
- camera angle,
- lens feel,
- depth behavior,
- light structure,
- material response,
- atmosphere,
- negative space.

### Step 6 — compile the prompt

Use:
- `skills/core/prompt-compiler.md`
- `skills/core/token-budget.md`
- `skills/core/slop-scrubber.md`

Recommended prompt order:
1. deliverable and image goal,
2. subject and action,
3. environment and world logic,
4. composition and camera,
5. lighting and material behavior,
6. style stack,
7. preservation or edit delta,
8. text/layout instructions,
9. constraints and avoid list.

### Step 7 — validate risk

Use:
- `skills/core/risk-validation.md`
- `references/gemini-runtime-preflight.md` when preparing a Gemini runtime call.

Check for:
- contradictory requirements,
- unsafe or disallowed content,
- copyright or brand issues,
- source-image rights,
- likeness consent,
- minors and age ambiguity,
- unsupported historical claims,
- deceptive or documentary claims,
- SynthID/provenance expectations,
- transparent-background limitations,
- multi-turn edit/session continuity,
- impossible continuity locks,
- overloaded text requirements,
- mismatched profile/platform combinations.

### Step 8 — emit outputs

Use `skills/core/schema-output.md`.

Preferred final structure:

```markdown
## Model target
## Assumptions
## Production prompt
## Preserve / Avoid
## Runtime JSON
## Next iteration options
```

## Prompt quality rules

### Hard rules

- Keep the prompt concrete.
- Keep the camera physically plausible unless surrealism is intentional.
- Keep material response compatible with the light.
- Keep historical details from different eras from colliding without explanation.
- For edits, avoid rewriting the whole scene if only one thing changes.
- When text matters, reserve negative space for it on purpose.

### Slop to remove

Use `registry/forbidden-slop.json`.

Actively scrub:
- generic quality filler,
- contradictory style clusters,
- empty intensifiers,
- duplicate camera directions,
- random render-engine name dropping that adds nothing.

### Influence handling

Use `skills/core/influence-decomposer.md`.

Convert named inspirations into:
- palette,
- shape language,
- contrast ratio,
- line behavior,
- texture character,
- staging logic,
- cultural or historical cues.

Do not rely on name-dropping alone.

## Mini examples

### Example A — fast concept frame

**User request**  
"Give me a sci-fi alley with rain, neon signs, and a low drone perspective."

**Good response shape**
- model target: Nano Banana 2
- style stack: photoreal + sci-fi + drone + volumetric-lighting + vfx-shot
- prompt emphasizes wet surfaces, parallax, depth haze, signage placement, and flight-camera perspective
- no fake "8k masterpiece" sludge

### Example B — poster with text

**User request**  
"Festival poster in an Edo print style with the title Lanterns of Spring."

**Good response shape**
- model target: Nano Banana Pro
- style stack: poster-layout + text-in-image + japanese-edo + ukiyo-e
- prompt specifies title block, secondary text zones, safe margins, and clear hierarchy
- avoid dense scene clutter behind key type

### Example C — precise product relight

**User request**  
"Keep the bottle identical. Change only the background and add teal rim light."

**Good response shape**
- model target: Nano Banana Pro
- mode: edit + relight
- preserve geometry, label, cap, camera angle, crop, and shadow shape
- change only backdrop material and rim-light color/placement

## File guide

Core workflow:
- `skills/core/interview.md`
- `skills/core/router.md`
- `skills/core/prompt-compiler.md`
- `skills/core/schema-output.md`

For style and art direction:
- `skills/core/style-router.md`
- `skills/core/aesthetic-director.md`
- `skills/core/composition-camera.md`
- `skills/core/lighting-materials.md`

For safe, grounded edits:
- `skills/core/grounding.md`
- `skills/core/world-model.md`
- `skills/core/reference-binding.md`
- `skills/core/preservation.md`
- `skills/core/edit-delta.md`
- `skills/core/risk-validation.md`
- `references/gemini-runtime-preflight.md`

For registries and schemas:
- `registry/style-axes.md`
- `registry/aliases.json`
- `registry/forbidden-slop.json`
- `registry/token-budgets.json`
- `schemas/authoring-base.json`
- `schemas/runtime-compact.json`

For examples:
- `examples/authoring/README.md`
- `examples/runtime/README.md`

## Output contract

When the user wants a final prompt, provide:

- a short note explaining the selected model target,
- the final prompt,
- a preserve/avoid block when relevant,
- a runtime JSON example when useful.

When the user wants only structured output, return JSON that validates against:
- `schemas/authoring-base.json`, or
- `schemas/runtime-compact.json`

When the user wants the repo improved, edit the modular files rather than bloating this orchestrator.
