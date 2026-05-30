# Commercial And Hosted Model Cards

Use these cards for model-specific prompting. Check current docs when exact model names, pricing, policy, or API fields matter.

## OpenAI Image Models

Evidence level: Official.

Use for:

- General generation.
- Image editing.
- Product images.
- diagrams and UI mockups.
- Character sheets with references.
- Text integrated into the image.

Prompt dialect:

- Plain task instruction.
- Exact text in quotes.
- Preserve and change statements for edits.
- Avoid dumping unsupported sampler or CFG controls into prose.

Prompt pattern:

```text
Create a [asset type] showing [subject]. Composition: [framing]. Setting: [place]. Materials: [details]. Lighting: [source]. Camera or render: [style]. Exact text: "[text]" at [placement]. Preserve [details].
```

Failure modes:

- Too much prose can dilute the instruction.
- Complex exact typography may still need iteration.
- Reference image role confusion can occur if inputs are not labeled.

Skill rule:

- Keep prompts direct.
- Separate edit target from preserved details.
- Do not include Midjourney parameters or Stable Diffusion settings.

## Gemini Nano Banana Family

Evidence level: Official for model names and image capabilities. Community-tested for JSON-style image prompt briefs.

Names:

- Nano Banana: Gemini 2.5 Flash Image.
- Nano Banana Pro: Gemini 3 Pro Image.
- Nano Banana 2: Gemini 3.1 Flash Image.

Use for:

- Image generation.
- Image editing.
- Multi-image reference tasks.
- Text and layout prompts.
- Fast prompt iteration.

Prompt dialect:

- Natural language works.
- JSON-style briefs often work well because Gemini follows structured labels.
- Use both when the user wants choice or precision.

Natural-language template:

```text
Create a [format] image of [subject]. Frame it as [composition] in [setting]. Use [style], [camera], and [lighting]. Render the exact text "[text]" at [placement] in [font style]. Use Image A for [role] and preserve [details].
```

JSON-style template:

```json
{
  "task": "generate_image",
  "subject": "",
  "composition": "",
  "setting": "",
  "style": "",
  "camera": "",
  "lighting": "",
  "text_to_render": [
    {
      "exact_text": "",
      "placement": "",
      "font_style": "",
      "color": ""
    }
  ],
  "reference_roles": [
    {
      "image": "Image A",
      "use_for": ""
    }
  ],
  "must_preserve": [],
  "must_avoid": []
}
```

Failure modes:

- Text rendering can still fail.
- Edits can drift if the prompt does not separate change from preserve.
- False positives can happen on ambiguous prompts, real people, identity edits, public figures, and sensitive contexts.

Skill rule:

- For Gemini and Nano Banana, offer natural language plus JSON-style prompt when useful.
- Label community JSON-style prompting as community-tested.
- Do not frame structured prompts as filter bypass.

## Midjourney

Evidence level: Official for parameter syntax and platform behavior.

Use for:

- Editorial images.
- concept art.
- Style exploration.
- High visual variation.
- Character and style reference workflows.

Prompt dialect:

- Natural-language scene description plus Midjourney parameters.
- Use image references, style references, character references, and Omni Reference when available.

Template:

```text
[Subject], [relationship], [setting], [composition], [lighting], [medium], [style constraints] --ar [ratio] --v [version] --stylize [value]
```

Failure modes:

- Prompt bloat can reduce control.
- Parameters copied from older versions can behave differently.
- Negative concepts need Midjourney `--no`, not SD negative prompt blocks.

Skill rule:

- Keep parameters at the end.
- Do not include SD sampler or CFG settings.
- Use `--no` only for clear visual exclusions.

## Black Forest Labs FLUX Hosted Surfaces

Evidence level: Official for BFL docs.

Use for:

- Photographic and design generation.
- Readable text tasks on FLUX.2 surfaces.
- Reference-guided workflows where supported.

Prompt dialect:

- Clear natural language.
- Positive visual statements.
- Exact text, placement, style, size, and color.
- Hex colors when brand precision matters.

Important surface rule:

- FLUX.2 hosted docs state no negative prompt support on that surface.

Template:

```text
A [asset type] of [subject] in [setting]. Composition: [framing]. Materials and colors: [details, hex colors]. Lighting: [source]. Text: "[exact text]" placed [location], [typography].
```

Failure modes:

- Prompt upsampling can change intent.
- Local wrappers may expose controls that hosted BFL does not.

Skill rule:

- Omit negative prompt on BFL FLUX.2 hosted prompts.
- If local ComfyUI FLUX exposes negative conditioning, treat that as a workflow detail, not base model behavior.

## Stability AI And Stable Image

Evidence level: Official for API surfaces, model families, and multi-prompting where documented.

Use for:

- Hosted image generation.
- Stable Diffusion model families.
- Weighted prompts where the surface supports them.

Prompt dialect:

- Prompt plus exposed parameters.
- Negative prompt only where supported.
- Weighted prompt syntax only where supported.

Failure modes:

- Parameter availability differs across Stability endpoints.
- Users often mix local SD settings into hosted endpoints where they do not apply.

Skill rule:

- Match the exact endpoint.
- Separate prompt, negative prompt, and parameters.

## Runway Gen Image Surfaces

Evidence level: Official.

Use for:

- Image generation for video workflows.
- Reference-heavy creative direction.
- Product or scene frames that later animate.

Prompt dialect:

- Natural language.
- Reference roles.
- Describe what should appear, not a long list of negatives.

Failure modes:

- Negative prompt habits from SD can produce worse prompts.
- Vague style language can lead to generic outputs.

Skill rule:

- Write clear positive prompts.
- Describe camera, scene, subject, and action as visible content.

## Ideogram

Evidence level: Official.

Use for:

- Text and typography.
- Posters.
- Logos and signs.
- Layout-heavy generation.

Prompt dialect:

- Natural language with exact text.
- Use Magic Prompt only when prompt expansion is acceptable.
- Negative prompt and style controls where exposed.

Template:

```text
Poster design with the exact headline "[text]" at [location]. Typography: [font style]. Layout: [grid]. Color palette: [colors]. Main visual: [subject].
```

Failure modes:

- Prompt expansion can change exact branding.
- Too many text blocks increase errors.

Skill rule:

- Disable or avoid prompt expansion for exact brand or UI text tasks.

## Adobe Firefly

Evidence level: Official.

Use for:

- Commercial Adobe workflows.
- Generative Fill.
- Prompt to Edit.
- Custom models.
- Design and marketing assets.

Prompt dialect:

- Plain language.
- Style and reference controls when available.
- Clear edit intent.

Failure modes:

- Partner model behavior inside Firefly can differ by selected model.
- Commercial safety controls can constrain output.

Skill rule:

- Identify which Firefly model or partner model is selected.
- Keep prompts clean and commercially safe.

## Recraft

Evidence level: Official.

Use for:

- Vector-like design.
- Logos.
- icons.
- typography.
- brand systems.
- layout-heavy images.

Prompt dialect:

- Design brief language.
- Text and layout constraints.
- Style controls and prompt enhancement where useful.

Failure modes:

- Prompt enhancement can override exact brand rules.
- Raster and vector outputs need different expectations.

Skill rule:

- Use Recraft for design artifacts where editability matters.
- Avoid enhancement when exact text or brand compliance matters.

## Luma

Evidence level: Official.

Use for:

- Image generation and modification linked to video workflows.
- Reference role workflows.

Prompt dialect:

- Natural language.
- Create versus modify should be explicit.
- Label reference roles.

Failure modes:

- Negative prompt support may not exist on a given surface.
- Reference role ambiguity can cause drift.

Skill rule:

- Tell the model what each reference contributes.

## Seedream

Evidence level: Official for ByteDance published model information.

Use for:

- High alignment image generation.
- Style image creation.
- Reference understanding where supported.

Prompt dialect:

- Plain instructions.
- Strong reference labeling.
- Preserve and change clauses for edits.

Failure modes:

- Platform wrappers can differ from base model.
- Public availability varies by region and product surface.

Skill rule:

- Identify the exact Seedream version and surface when precision matters.

## Qwen Hosted Surfaces

Evidence level: Official for Qwen Cloud docs and model cards.

Use for:

- Text rendering.
- Image editing.
- Bilingual text.
- Posters.
- Multi-image workflows.

Prompt dialect:

- Labeled images.
- Exact text.
- Preserve original font, size, and style when editing text.
- `prompt_extend` can help exploration but can hurt exact design.

Failure modes:

- Prompt extension may alter exact intent.
- Multi-input prompts drift when labels are vague.

Skill rule:

- Disable or avoid prompt extension for exact brand, typography, product, legal, medical, or UI work.
