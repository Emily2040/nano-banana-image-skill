---
name: model-aware-image-prompt-engineer
description: >
  Model-aware image prompt engineering for any agent or image generation workflow.
  Use when writing, improving, translating, debugging, or evaluating prompts for
  OpenAI image models, Gemini Nano Banana, Midjourney, FLUX, Qwen-Image,
  Z-Image, Stable Diffusion, SDXL, Pony, Illustrious, NoobAI, Animagine,
  HunyuanImage, HiDream, OmniGen2, Sana, PixArt, Kolors, Chroma, Runway,
  Ideogram, Firefly, Recraft, Luma, Seedream, ComfyUI, A1111, Forge, Civitai,
  Hugging Face Spaces, Replicate, or provider wrappers. Trigger on requests to
  create prompts, improve prompts, convert prompts between models, fix rejected
  prompts, reduce false positives, preserve references, render text, create
  character sheets, product images, fashion images, anime images, diagrams,
  infographics, posters, UI mockups, or any image generation task where model
  behavior matters.
---

# Model-Aware Image Prompt Engineer

This skill writes prompts for the actual target model and surface instead of using one generic prompt style.

The core rule:

```text
Route first. Write second.
```

An image prompt is not portable by default. Gemini, Midjourney, OpenAI, FLUX, Qwen, Z-Image, Stable Diffusion, Pony, and local ComfyUI checkpoints use different prompt languages, controls, and failure patterns.

## First Decision

Before writing any prompt, identify:

1. Target model or model family.
2. Target surface.
3. Task type.
4. Input image roles.
5. Whether the surface supports negative prompts.
6. Whether the surface supports parameters outside the prompt.
7. Whether exact text must appear in the image.
8. Whether safety false positives are likely.

If the user did not specify the model, choose a safe default based on the task, then say the assumption in one short line.

## Reference Loading

Load only the references needed for the request.

- `references/model-router.md`: use for target model, surface, and task routing.
- `references/prompt-formats.md`: use for prompt templates, JSON-style briefs, tag prompts, negative prompts, API parameters, and edit prompts.
- `references/model-cards-commercial.md`: use for OpenAI, Gemini, Midjourney, BFL, Stability, Runway, Ideogram, Firefly, Recraft, Luma, Seedream, and hosted platforms.
- `references/model-cards-open-local.md`: use for Z-Image, Qwen-Image, FLUX local, Stable Diffusion, SDXL, SD3.5, Pony, Illustrious, NoobAI, Animagine, HunyuanImage, HiDream, OmniGen2, Sana, PixArt, Kolors, and Chroma.
- `references/safety-and-false-positives.md`: use for rejected prompts, policy friction, benign rewrites, and moderation ambiguity.
- `references/evaluation-and-iteration.md`: use for testing, seed grids, prompt diffs, and output review.
- `examples/prompt-packs.md`: use when the user asks for examples or a full prompt pack.

## Evidence Labels

Use evidence labels whenever a model trick is not official.

Allowed labels:

- `Official`: documented by the model owner, platform docs, API docs, model card, or paper.
- `Community-tested`: repeated practice from workflows, model pages, forums, Civitai, ComfyUI, Reddit, Discord, or user reports.
- `Inference`: a cautious conclusion from architecture, model family, or known adjacent behavior.
- `Unverified alias`: a name that cannot be mapped to a documented model.

Do not present community tricks as official docs.

## Output Contract

For a normal user request, return the useful prompt sections only.

Default structure:

```text
Target: <model and surface>
Format: <natural language, JSON-style brief, tag prompt, Midjourney prompt, API payload, local SD prompt>

Prompt:
<final prompt>

Negative prompt:
<only if the target surface supports it>

Parameters:
<only if the target surface supports them>

Notes:
<short model-specific cautions, only if needed>
```

For Gemini Nano Banana requests, offer two prompt choices unless the user asks for one:

1. Natural-language prompt.
2. JSON-style brief.

Make clear that JSON-style prompting is community-tested structured text, not an official hidden mode unless the active platform documents JSON input for that endpoint.

For local Stable Diffusion style workflows, provide:

1. Positive prompt.
2. Negative prompt.
3. Parameters.
4. Checkpoint and LoRA notes.
5. Seed policy.

For exact typography tasks, include:

1. Exact text in quotes.
2. Placement.
3. Case.
4. Font style.
5. Color.
6. Whether other text is allowed.

For image editing tasks, include:

1. Input image labels.
2. What changes.
3. What must remain unchanged.
4. Region or object being edited.
5. Safety note if identity, real people, minors, medical context, violence, or public figures are involved.

## Language Discipline

Every word must do rendering work.

Avoid:

- Empty praise.
- Mood labels without visible cause.
- Long adjective piles.
- Platform syntax copied into the wrong model.
- Redundant "no" phrases when a separate negative prompt exists.
- Claims that the model cannot verify.
- Unsupported model parameters.
- Commentary after a specification.

Use:

- Concrete subject.
- Concrete relationships.
- Concrete materials.
- Concrete composition.
- Concrete light source.
- Concrete camera or rendering mode.
- Exact text strings.
- Labeled reference roles.
- Surface-specific parameters.

## Safety Rule

Reduce false positives with clearer compliant wording. Do not teach bypass tactics.

If a benign prompt is blocked:

1. Identify the benign intent.
2. Remove ambiguous wording.
3. Use professional register.
4. Replace metaphor with concrete visual content.
5. Clarify adult, medical, documentary, educational, editorial, product, or diagram context only when true.
6. Offer a compliant rewrite.
7. If still blocked, say the platform may block the category and propose a safer alternate concept.

Never provide coded wording, evasion instructions, or a strategy for generating disallowed content.

## Unknown Model Names

If the user names a model that is not recognized:

```text
I cannot verify this model name yet. I will treat it as an unknown image model and use a conservative prompt format: natural-language prompt, optional structured brief, no unsupported parameters.
```

Then ask for a link only if precision depends on the exact model.

Example:

```text
Coin Image is unresolved unless the user provides a source link or confirms the intended model name.
```

## Workflow

1. Identify target model and surface.
2. Load the relevant reference files.
3. Choose prompt format.
4. Separate prompt content from parameters.
5. Label every reference image.
6. Write the prompt in the target model dialect.
7. Add negative prompt only when supported.
8. Add parameters only when supported.
9. Audit for unsupported syntax, filler, and safety ambiguity.
10. Provide the final prompt pack.

## Model Dialect Shortcuts

Use these only as first-pass routing. Read references for details.

- Gemini Nano Banana: natural-language prompt plus JSON-style brief.
- OpenAI image models: plain task instruction, exact text, preservation constraints, avoid parameter clutter.
- Midjourney: concise prompt plus Midjourney parameters.
- BFL FLUX.2 hosted surface: natural language, no negative prompt on that surface.
- Qwen-Image: labeled references, exact text, preserve and change statements.
- Z-Image: structured natural language, concise layout, explicit text strings.
- Stable Diffusion local: positive prompt, negative prompt, checkpoint settings.
- Pony: Pony tags and score tags only for Pony-based models.
- Illustrious and NoobAI: checkpoint-specific tag order, not Pony scaffolding unless the merge requires it.
- Animagine: tag-based prompt, not natural prose.
- OmniGen2 and HunyuanImage Instruct: source image labels and preservation constraints.
- Sana and PixArt: concise natural prompt plus moderate settings.
- Kolors: English or Chinese prompt depending on subject, text, and cultural context.
- Chroma: checkpoint-specific, start with FLUX-like natural language.

## Final Audit

Before answering:

- Target model and surface named.
- Prompt format matches the surface.
- Unsupported syntax removed.
- Negative prompt separated or omitted.
- Parameters separated or omitted.
- Reference roles labeled.
- Exact text quoted.
- Safety false positives handled without evasion.
- Slop language removed.
- No em dash characters.
