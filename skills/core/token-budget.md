
# Token Budget

## Purpose

Keep prompts dense with useful information instead of inflated with verbal fog.

The skill uses **authoring budgets**, not model context limits.  
See `registry/token-budgets.json`.

## General rule

Use the shortest prompt that still pins down:
- subject,
- action,
- setting,
- composition,
- lighting,
- style,
- text or preservation requirements.

## What to cut first

1. duplicate style adjectives
2. repeated mood words
3. secondary props with no visual impact
4. background lore that will not show on camera
5. named pipelines that do not alter the result

## Example 1 — bloated

"An ultra detailed masterpiece cinematic award-winning best-quality futuristic neon alley with stunning beautiful epic atmosphere, incredibly detailed rain, highly detailed signs, absolutely gorgeous reflections, unreal octane masterpiece..."

Most of that is decorative mush.

## Example 1 — repaired

"Rain-soaked neon alley at midnight, low hovering drone perspective, narrow vanishing corridor, reflective asphalt, bilingual signs, cool blue ambient haze, warm shop practicals, wet metal shutters, light mist revealing depth."

Much leaner. Much stronger.

## Example 2 — edit delta budget

For edits, spend tokens on:
- preserved elements,
- changed elements,
- light/material behavior,
- mask or region hints if needed.

Do not restate the entire original image unless essential.

## Example 3 — poster budget

Typography-heavy work earns a larger budget because you need:
- exact copy,
- hierarchy,
- placement,
- safe margins,
- background discipline.

That is a real use of words. Decorative adjectives are not.

## Budget profiles

Model-aware ceiling notes:
- Nano Banana model prompts currently cap at **about 480 tokens**; use this as a hard stop.
- If a prompt gets near that cap, remove decorative language before removing physical constraints.

### Fast ideation
Aim for 100–180 words.

### Complex scene
Aim for 180–320 words.

### Poster or infographic
Aim for 220–420 words.

### Delta edit
Aim for 90–200 words.

## Compression move

If the prompt feels too long, rewrite long adjective chains into one physical statement.

### Before
"luxurious elegant glossy premium sophisticated dark teal mood"

### After
"deep teal lacquered finish with restrained luxury editorial lighting"

Same idea. Fewer calories.
