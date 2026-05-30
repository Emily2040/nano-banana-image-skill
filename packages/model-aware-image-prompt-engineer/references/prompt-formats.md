# Prompt Formats

Use the prompt format that the target surface can actually read.

## Natural-Language Prompt

Use for:

- OpenAI image prompts.
- Gemini chat surfaces.
- Midjourney base prompt.
- FLUX hosted surfaces.
- Z-Image.
- Qwen when not using tag checkpoints.
- Sana.
- PixArt.
- Kolors.
- HiDream.

Template:

```text
Create a [asset type] of [subject]. Frame it as [composition] in [setting]. Use [materials, color, surface]. Lighting: [source and quality]. Camera or render: [view, lens, medium]. Exact text: "[text]" placed [location], [font category], [color]. Preserve [details]. Do not add [only if the target has no separate negative field and the constraint is essential].
```

Rules:

- Put the subject first.
- Put relationships before style.
- Put exact text in quotes.
- Use one visual register.
- Keep constraints visible and concrete.

## JSON-Style Brief

Use for:

- Gemini Nano Banana family.
- Multimodal reference routing.
- Complex edit instructions.
- Prompt translation between models.
- Product, typography, and layout tasks.

Evidence level:

- Community-tested for Gemini image workflows.
- Also useful as a general agent planning format.
- Not an official hidden image mode unless the platform documents JSON for that endpoint.

Template:

```json
{
  "task": "generate_image",
  "target_surface": "",
  "asset_type": "",
  "subject": "",
  "composition": "",
  "setting": "",
  "style": "",
  "camera": "",
  "lighting": "",
  "materials": [],
  "text_to_render": [
    {
      "exact_text": "",
      "placement": "",
      "case": "",
      "font_style": "",
      "color": ""
    }
  ],
  "reference_images": [
    {
      "label": "Image A",
      "role": "",
      "must_preserve": []
    }
  ],
  "changes": [],
  "must_preserve": [],
  "must_avoid": []
}
```

Rules:

- Use short strings.
- Use lists for preservation constraints.
- Keep `must_avoid` compliant and concrete.
- Do not use JSON-style briefs to evade platform policy.

## API Payload Format

Use for:

- API examples.
- Developer implementation.
- Exact reproducibility.

Template:

```json
{
  "model": "",
  "prompt": "",
  "size": "",
  "seed": null,
  "negative_prompt": "",
  "input_images": [
    {
      "label": "Image 1",
      "role": ""
    }
  ]
}
```

Rules:

- Match the real API schema before giving code.
- Omit unsupported fields.
- Keep prompt and parameters separate.

## Midjourney Prompt

Use for:

- Midjourney web and Discord.

Template:

```text
[Subject], [composition], [setting], [materials], [lighting], [camera or medium], [style anchors] --ar [ratio] --v [version] --stylize [value]
```

Rules:

- Use Midjourney parameters only.
- Use `--no` only for supported negative concepts.
- Put image reference URLs before prompt text when needed.
- Do not include Stable Diffusion negative prompt blocks.

## Stable Diffusion Local Format

Use for:

- ComfyUI.
- A1111.
- Forge.
- Civitai generator.
- Local APIs.

Template:

```text
Checkpoint:
[checkpoint name]

Positive:
[trigger words], [subject], [pose], [clothing or object construction], [setting], [lighting], [camera or style]

Negative:
[specific artifacts and unwanted elements for this model]

Settings:
size: [width x height]
sampler: [sampler]
scheduler: [scheduler]
steps: [range]
CFG or guidance: [range]
seed: fixed for iteration, random for exploration
LoRA: [name, weight, trigger words]
VAE: [if needed]
clip skip: [if needed]
```

Rules:

- Use trigger words exactly when the LoRA or checkpoint requires them.
- Keep negative prompt targeted.
- Do not paste old universal negative prompts unless the user requests a legacy workflow.
- Keep settings out of the positive prompt.

## Tag Prompt Format

Use for:

- Animagine.
- Pony-based models.
- Some Illustrious and NoobAI workflows.
- Other booru-trained checkpoints.

Template:

```text
[model-required opening tags], [subject count], [character], [series or source if allowed], [rating or safety tag if required], [pose], [clothing], [setting], [composition], [style tokens required by model]
```

Rules:

- Use the checkpoint's own tag order.
- Do not mix Pony score tags into non-Pony prompts.
- Do not use natural prose when the model card says tag prompts work better.
- Avoid underscores if the checkpoint guide warns against them.

## Edit Prompt Format

Use for:

- Image editing.
- Try-on.
- Product mockups.
- Background replacement.
- Multi-image fusion.

Template:

```text
Image A: [role].
Image B: [role].
Change only [target region or object] to [new state].
Preserve [identity, pose, lighting, camera, background, garment, typography, material].
Do not change [critical invariants].
```

Rules:

- Use labels, not pronouns.
- State "change only" and "preserve" separately.
- If the user asks to edit a real person, check platform policy and safety context.
- For text edits, preserve font, size, color, layout, and spacing if requested.

## Reference Image Role Map

Use exact roles:

```text
Image A: identity only.
Image B: outfit only.
Image C: pose only.
Image D: background only.
Image E: color palette only.
Image F: typography only.
Image G: product shape only.
```

Rules:

- One role per image is cleaner than one image doing everything.
- If one reference has multiple roles, list them in priority order.
- Tell the model what not to borrow from each image when needed.

## Exact Text Rendering

Template:

```text
Render the exact text "[TEXT]" at [location]. Use [case], [font category], [weight], [color]. Do not add any other readable text.
```

Rules:

- Keep text short.
- Quote the text.
- Avoid multiple font systems unless the design requires them.
- If there are multiple text blocks, number them.

## Prompt Translation Format

When converting a prompt between models:

```text
Source model:
<model>

Target model:
<model and surface>

Keep:
<subject, composition, style, text, references>

Remove:
<unsupported syntax, wrong parameters, irrelevant negative prompt>

Converted prompt:
<target dialect>
```

Do not do literal translation. Translate behavior and controls.
