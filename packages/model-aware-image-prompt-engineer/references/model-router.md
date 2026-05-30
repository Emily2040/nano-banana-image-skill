# Model Router

Use this file before writing a prompt.

## Routing Questions

Ask these internally. Do not ask the user unless the answer changes the output and cannot be inferred.

1. Which model or platform will run the prompt?
2. Is the user using chat, API, ComfyUI, A1111, Forge, Civitai, Replicate, Hugging Face, Midjourney, or a provider wrapper?
3. Is the task generation, editing, inpainting, style transfer, product visualization, typography, character consistency, reference fusion, diagram, or infographic?
4. Does the model support image inputs?
5. Does the surface expose negative prompts?
6. Does the surface expose seed, size, CFG, sampler, scheduler, guidance, style reference, character reference, or prompt extension?
7. Is exact text required?
8. Is a real person, public figure, minor, medical situation, injury, political context, or identity edit involved?

## Surface Classes

### Plain Chat Box

Examples:

- ChatGPT image prompt box.
- Gemini app.
- Consumer web wrappers.
- Mobile prompt box.

Return:

- One natural-language prompt.
- Optional short alternate prompt.
- No raw API parameters unless the user can paste them.

Avoid:

- Sampler names.
- CFG.
- Raw JSON payloads unless the user requested a structured brief.
- Negative prompt blocks unless the UI has one.

### API Surface

Examples:

- OpenAI Images API.
- Gemini API.
- Qwen Cloud.
- Stability API.
- Replicate endpoint.

Return:

- Prompt field.
- Parameter block.
- Image role map.
- Separate negative prompt only if the API supports it.

Avoid:

- Hiding controllable parameters inside prose.
- Mixing multiple endpoints in one payload.

### Midjourney Surface

Examples:

- Midjourney web.
- Midjourney Discord.

Return:

- One prompt line.
- Midjourney parameters only.
- Version, aspect ratio, stylize, seed, quality, weird, character reference, style reference, and negative concepts only when useful.

Avoid:

- Stable Diffusion negative prompt blocks.
- CFG and sampler settings.
- JSON payloads.

### Local Stable Diffusion Surface

Examples:

- ComfyUI.
- A1111.
- Forge.
- Civitai generator.
- Local wrapper.

Return:

- Positive prompt.
- Negative prompt.
- Model or checkpoint.
- LoRA trigger words and weights if known.
- Settings.
- Seed policy.

Avoid:

- One universal negative prompt.
- Midjourney parameters.
- OpenAI or Gemini prose if the checkpoint is tag-trained.

### Multimodal Edit Surface

Examples:

- Gemini image editing.
- Qwen-Image Edit.
- FLUX Kontext.
- OmniGen2.
- HunyuanImage Instruct.
- OpenAI image edit.

Return:

- Image labels.
- Role for each image.
- What changes.
- What remains unchanged.
- Region, object, or layer being edited.
- Exact text if any.

Avoid:

- Pronouns across multiple images.
- Unlabeled references.
- Vague "make it better" instructions.

## Task Routing

### Exact Typography

Prefer:

- Qwen-Image.
- Gemini Nano Banana family.
- Ideogram.
- Recraft.
- FLUX.2 if the surface supports text well.
- OpenAI image models for integrated design tasks.

Prompt requirements:

- Quote exact text.
- State placement.
- State case.
- State font category.
- State color.
- State whether other text is allowed.

### Character Consistency

Prefer:

- Gemini Nano Banana family.
- OpenAI image models with reference images.
- FLUX Kontext.
- Qwen-Image Edit.
- OmniGen2.
- HunyuanImage Instruct.
- Midjourney character reference.

Prompt requirements:

- Label each reference image.
- Name identity anchors.
- State body, clothing, pose, and scene separately.
- Preserve face only when allowed by platform policy.

### Anime And Tag Checkpoints

Prefer:

- Animagine for tag-based anime prompts.
- Pony for Pony-based models.
- Illustrious and NoobAI for SDXL anime local workflows.

Prompt requirements:

- Use model-specific tag order.
- Use source, rating, or score tags only when the model expects them.
- Do not transfer Pony syntax to non-Pony models.

### Product, Fashion, And Commercial Images

Prefer:

- OpenAI image models.
- Gemini Nano Banana family.
- Midjourney.
- FLUX.
- Qwen for text-heavy packaging.
- Recraft for design systems and vector-like outputs.
- Firefly where commercial safety and Adobe workflows matter.

Prompt requirements:

- Product form.
- Materials.
- Surface finish.
- Camera angle.
- Lighting setup.
- Background.
- Exact label text if any.

### Infographics And Diagrams

Prefer:

- Deterministic SVG, HTML, or design tools when exact text matters.
- Recraft, Ideogram, Qwen, Gemini, or OpenAI when the user wants generated visual style.

Prompt requirements:

- Keep text short.
- Use labeled blocks.
- Limit the number of words in the image.
- Provide a separate text spec for accurate recreation.

### Exploration Versus Production

Exploration:

- More creative variation.
- Random seed.
- Prompt extension can be useful.
- Shorter constraints.

Production:

- Fixed seed for iteration where supported.
- Exact prompt record.
- Prompt extension disabled when accuracy matters.
- Fewer assumptions.
- Reference images labeled.
- Output checklist.

## Default Model Choice When Unknown

Use a conservative format:

```text
Target: Unknown image model or generic chat surface
Format: Natural-language prompt with optional structured brief
```

Do not include model-specific parameters.

Do not claim behavior for an unknown model.

## Unverified Alias Policy

If a model name cannot be verified:

1. Mark it `Unverified alias`.
2. Do not invent syntax.
3. Offer a generic prompt.
4. Ask for a link only if exact support matters.

Current unresolved example:

```text
Coin Image: unresolved alias. Possible speech or platform naming issue. Do not publish a model card without a source.
```
