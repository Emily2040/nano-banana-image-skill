# Prompt Pack Examples

These examples show the expected output shape. Replace content with the user's actual brief.

## Gemini Nano Banana Product Poster

Target: Gemini Nano Banana, chat or AI Studio

Format: natural language plus JSON-style brief

Natural-language prompt:

```text
Create a square product poster for a matte black travel mug on a brushed steel table. Center the mug in a clean front view with a soft reflection beneath it. Use neutral studio lighting from upper left and a pale gray background. Render the exact text "HOT FOR 12 HOURS" in uppercase white sans-serif letters above the mug. Do not add any other readable text.
```

JSON-style brief:

```json
{
  "task": "generate_image",
  "asset_type": "square product poster",
  "subject": "matte black travel mug",
  "composition": "centered front view, mug occupying the middle third",
  "setting": "brushed steel table, pale gray background",
  "lighting": "neutral studio light from upper left",
  "materials": ["matte black powder-coated metal", "brushed steel"],
  "text_to_render": [
    {
      "exact_text": "HOT FOR 12 HOURS",
      "placement": "above the mug",
      "case": "uppercase",
      "font_style": "white sans-serif",
      "color": "white"
    }
  ],
  "must_avoid": ["extra readable text", "watermark"]
}
```

## Qwen-Image Edit Text Replacement

Target: Qwen-Image Edit

Format: edit prompt

```text
Use Image 1 as the source poster. Change only the headline text. Replace the current headline with the exact text "OPEN DAILY". Preserve the original poster layout, background, illustration, letter spacing, font size, font weight, and color palette. Do not add any other readable text.
```

## FLUX.2 Hosted Brand Visual

Target: BFL FLUX.2 hosted surface

Format: natural language, no negative prompt

```text
A clean editorial brand image of a compact desk lamp on a walnut desk, photographed straight-on at eye level. The lamp has a satin white ceramic shade, brushed aluminum stem, and black fabric power cord. Background: warm off-white wall with subtle plaster texture. Lighting: large softbox from upper left, mild shadow on the desk. Text: "LUMA DESK" in small black uppercase sans-serif letters on a paper card in front of the lamp.
```

## Midjourney Concept Image

Target: Midjourney

Format: Midjourney prompt

```text
compact lunar research kitchen, modular white cabinets, basalt counter, small hydroponic herb wall, astronaut tools neatly mounted, practical industrial design, clean documentary lighting, 28mm architectural interior photo --ar 16:9 --stylize 100
```

## Stable Diffusion SDXL Local

Target: SDXL checkpoint in ComfyUI

Format: positive, negative, settings

```text
Checkpoint:
[checkpoint name]

Positive:
[required trigger words], studio product photo, matte black travel mug, centered front view, brushed steel table, pale gray background, softbox light from upper left, clean catalog composition

Negative:
extra text, watermark, warped handle, duplicate mug, cropped object, noisy background

Settings:
size: 1024x1024
sampler: checkpoint recommendation
scheduler: workflow recommendation
steps: checkpoint recommendation
CFG: checkpoint recommendation
seed: fixed for iteration
```

## Pony-Based Anime Safe Portrait

Target: Pony-based SDXL checkpoint

Format: Pony tag prompt

```text
Positive:
score_9, score_8_up, score_7_up, rating_safe, [source tag], 1girl, standing, blue jacket, white shirt, city street, daytime, looking at viewer, medium shot

Negative:
score_4, score_5, score_6, extra fingers, distorted hands, duplicate face, unreadable text, watermark
```

## Animagine Tag Prompt

Target: Animagine XL

Format: tag prompt

```text
1girl, original character, safe, standing, red coat, black boots, winter street, snow, soft daylight, medium shot, looking at viewer, model-card quality tokens
```

## False Positive Rewrite

Original benign intent:

```text
Fashion image of a black evening dress.
```

Risk:

```text
Body-focused wording or ambiguous age can trigger moderation.
```

Compliant rewrite:

```text
Studio catalog image of an adult-sized black evening dress on a mannequin, structured bodice, long satin skirt, visible seams, straight-on front view, neutral gray background, even studio lighting.
```

## Unknown Model Fallback

Target: unknown image model

Format: generic natural language

```text
Create a clean product image of [subject] in [setting]. Composition: [framing]. Materials: [surface and color]. Lighting: [light source]. Camera or render: [view]. Exact text: "[text]" at [placement]. Preserve [details].
```
