# Open And Local Model Cards

Open and local models need model cards because local workflows expose controls that hosted chat tools hide. Do not assume all "open models" behave the same.

## Z-Image And Z-Image-Turbo

Evidence level: Official for model family and Diffusers support. Community-tested for prompting style.

Use for:

- Open-weight text-to-image.
- Image-to-image.
- Inpainting.
- Bilingual English and Chinese text tasks.
- Local fast iteration with Z-Image-Turbo.

Prompt dialect:

- Structured natural language.
- Concise subject, layout, style, material, light, and text.
- Not old SD tag soup.

Template:

```text
[Subject] in [setting], [composition]. [Action or relationship]. [Material, color, surface]. [Lighting]. [Camera or render style]. Exact text: "[text]" at [location]. Preserve [details].
```

Community tricks:

- Keep prompts balanced.
- Put layout before style.
- Quote text.
- Avoid overlong quality phrases.
- Use prompt enhancers only when exact intent is not critical.

Failure modes:

- Literal prompt following can expose grammar mistakes.
- Local performance depends on quantization, workflow, and sampler.

## Qwen-Image And Qwen-Image Edit

Evidence level: Official for model card, paper, and Qwen Cloud behavior. Community-tested for ComfyUI workflows.

Use for:

- Exact text rendering.
- Bilingual text.
- Posters.
- UI mockups.
- Image editing.
- Multi-image reference tasks.

Prompt dialect:

- Natural language or structured edit brief.
- Labeled image roles.
- Exact text in quotes.
- Explicit preserve and change statements.

Template:

```text
Use Image 1 for the person, Image 2 for the clothing, and Image 3 for the pose. Change only [target]. Keep [identity, face, lighting, background, typography] unchanged. Render the exact text "[text]" in [language], [font style], at [placement].
```

Community tricks:

- Use "Person A" and "Person B" instead of pronouns.
- For text, state language, case, placement, and whether other text is allowed.
- Disable prompt extension for exact design tasks.
- In ComfyUI, verify text encoder, VAE, LoRA, and workflow before blaming the prompt.

Failure modes:

- Long text can still degrade.
- Prompt extension can alter exact brand or layout requirements.
- Bad local workflows create false prompt failures.

## FLUX Local Workflows

Evidence level: Official for BFL model family. Community-tested for ComfyUI behavior.

Use for:

- Natural-language image generation.
- Prompt adherence.
- Local workflows with FLUX checkpoints.
- Reference workflows when using Kontext or supported wrappers.

Prompt dialect:

- Natural language.
- Clear subject and scene.
- Use tags only if the checkpoint examples use them.

Template:

```text
A [asset type] of [subject] doing [action] in [setting]. Composition: [framing]. Lighting: [lighting]. Materials and colors: [details]. Text: "[exact text]" placed [location], [typography].
```

Community tricks:

- Avoid SD 1.5 tag soup on base FLUX.
- Keep the first sentence unambiguous.
- Prompt upsampling can help generic prompts but can change exact intent.
- Some local workflows expose negative conditioning, but hosted FLUX.2 may not.

Failure modes:

- Workflow differences are large.
- LoRAs can require trigger words and change base prompt behavior.

## Stable Diffusion 1.5

Evidence level: Official and community ecosystem.

Use for:

- Lightweight local generation.
- Large LoRA ecosystem.
- Style-specific checkpoints.
- ControlNet and inpainting workflows.

Prompt dialect:

- Tags, weighted tokens, trigger words, negative prompt, settings.

Template:

```text
Positive:
[LoRA triggers], [subject], [pose], [clothing or object], [setting], [lighting], [style tags]

Negative:
[model-relevant artifacts], [unwanted elements]

Settings:
size: 512x512 or checkpoint-native size
steps: workflow range
CFG: workflow range
sampler: workflow sampler
seed: fixed for iteration
```

Community tricks:

- Trigger words matter.
- Clip skip may matter for anime checkpoints.
- VAE can change color and detail.
- Excessive token weights create artifacts.

Failure modes:

- Small native resolution can hurt composition.
- Universal negative prompts can over-constrain.

## SDXL And SD3.5

Evidence level: Official and community ecosystem.

Use for:

- Higher-resolution local generation.
- General images.
- Anime and design checkpoints.
- LoRA workflows.

Prompt dialect:

- Natural language or tags depending on checkpoint.
- Positive prompt, negative prompt, settings.

Community tricks:

- Use checkpoint-native resolution.
- Keep LoRA triggers intact.
- Avoid old SD 1.5 defaults unless the checkpoint guide says so.
- Test CFG and sampler in small grids.

Failure modes:

- Some checkpoints expect tag order.
- Some checkpoints respond better to prose.
- Local wrappers can apply hidden prompt processing.

## Pony Diffusion XL And Pony-Based Models

Evidence level: Community model ecosystem.

Use for:

- Pony-trained anime and illustration models.
- Pony LoRAs.
- Tag-driven image generation.

Prompt dialect:

- Pony score tags.
- Source tags.
- Safety rating tags.
- Danbooru-style tags.

Template:

```text
Positive:
score_9, score_8_up, score_7_up, rating_safe, [source tag], [subject count], [character or object tags], [pose], [clothing], [setting], [style]

Negative:
[lower score tags if desired], [artifact tags], [unwanted source tags]
```

Community tricks:

- Put Pony score tags first.
- Use safe rating tags when the target output should be safe.
- Use source tags to control broad style.
- Do not move Pony scaffolding into non-Pony models.

Failure modes:

- Pony merges differ from base Pony.
- Some hosted platforms alter safety-related tags.
- Results can vary heavily by seed.

## Illustrious XL

Evidence level: Model card plus community workflows.

Use for:

- SDXL-derived anime and illustration workflows.
- Natural-language plus tag hybrid prompts.

Prompt dialect:

- Comma-separated tags often work.
- Newer versions may support more natural language.
- Tag order still matters.

Template:

```text
[subject], [identity], [attributes], [clothing], [pose], [environment], [lighting], [camera angle], [style or era], [checkpoint-required quality tokens]
```

Community tricks:

- Put subject and identity early.
- Use tags before general style notes.
- Do not assume Pony score tags transfer.

Failure modes:

- Merges can behave differently.
- Artist or style tokens may dominate subject if placed too early.

## NoobAI XL

Evidence level: Community docs and platform guides.

Use for:

- SDXL-derived anime workflows.
- Illustrious-related local models.

Prompt dialect:

- Comma-separated tag phrases.
- Character, source, style, period, and safety tags.

Template:

```text
[model-required opening tokens], [subject count], [character], [series], [style if allowed], [pose], [clothing], [setting], [period tag], [safety tag]
```

Community tricks:

- Follow the active guide for the exact checkpoint.
- Avoid underscores if the guide warns against them.
- Keep opening tokens model-specific.

Failure modes:

- Guide advice differs by version.
- Some platforms hide the underlying checkpoint changes.

## Animagine XL

Evidence level: Official model card.

Use for:

- Anime tag prompts.
- Character and series prompts where tags are available.

Prompt dialect:

- Tag-based.
- Natural language may be less effective.

Template:

```text
[subject count], [character], [series], safe, [pose], [clothing], [setting], [lighting], [composition], [model-card quality tokens]
```

Community tricks:

- Follow model-card tag order.
- Keep characters and series near the front.
- Use safety tags when required.

Failure modes:

- Anatomy can fail.
- Text rendering is weak.
- Recent characters can be weak.
- Multi-character scenes can drift.

## HunyuanImage 3.0 And Instruct

Evidence level: Official model cards and paper.

Use for:

- Large open-weight image generation.
- Image-to-image.
- Edit and fusion tasks with Instruct.

Prompt dialect:

- Plain instructions.
- Task labels.
- Source image roles.

Template:

```text
Task: [generate/edit/fuse].
Use Image 1 for [role], Image 2 for [role].
Create [subject] in [setting] with [composition].
Preserve [details].
Change [target] to [new state].
```

Community tricks:

- Label the task before the content.
- Use fewer steps for distilled checkpoints when docs recommend it.
- Expect heavy local requirements.

Failure modes:

- VRAM, quantization, and workflow strongly affect output.
- Instruct behavior differs from base generation.

## HiDream-I1 And HiDream-E1

Evidence level: Official model cards and Diffusers docs.

Use for:

- Open-source generation.
- Editing model family tasks.
- Local experiments with multiple text encoders.

Prompt dialect:

- Natural language.
- Minimal negative prompt.

Template:

```text
[Subject] in [setting], [composition], [action], [materials], [lighting], [camera], [style].
Negative: [only concrete artifacts to suppress]
```

Community tricks:

- Use the correct workflow for Full, Dev, Fast, or Edit.
- Keep prompt content aligned across text encoders unless the workflow has a reason to split prompts.

Failure modes:

- Multiple encoders make wrapper behavior variable.
- Large models need careful local setup.

## OmniGen2

Evidence level: Official model card and paper.

Use for:

- Text-to-image.
- Image editing.
- In-context generation.
- Multi-image reference composition.

Prompt dialect:

- English prompts are recommended by the model card.
- Label sources.
- Use text guidance and image guidance controls where exposed.

Template:

```text
Use Image 1 for [subject], Image 2 for [background], and Image 3 for [style]. Place [subject] into [background]. Preserve [source details]. Change [target]. Use [lighting and camera].
```

Community tricks:

- Clear input images matter.
- Higher image guidance preserves reference structure more but can reduce text instruction influence.

Failure modes:

- Reference dominance can override prompt changes.
- Poor input image quality harms output.

## Sana

Evidence level: Official docs and Diffusers docs.

Use for:

- Efficient open-source image synthesis.
- Fast iteration.
- High-resolution workflows.

Prompt dialect:

- Concise natural language.
- Negative prompt and guidance where exposed.

Template:

```text
[Subject], [setting], [composition], [material or style], [lighting], [camera].
Negative: [specific artifacts only]
```

Community tricks:

- Keep guidance moderate.
- Use it for iteration before final refinement if needed.

Failure modes:

- Overpacked prompts can weaken layout.

## PixArt-Sigma

Evidence level: Official Diffusers docs.

Use for:

- Prompt adherence tests.
- High-resolution DiT generation.
- Layout exploration.

Prompt dialect:

- Ordered natural language.
- Negative prompt and guidance where exposed.

Template:

```text
[Subject], [relationship], [setting], [composition], [style], [lighting], [camera].
```

Community tricks:

- Keep the prompt ordered and specific.
- Use another model for final render if visual finish is not enough.

Failure modes:

- Visual finish can trail newer large models.

## Kolors

Evidence level: Official and Diffusers docs.

Use for:

- English and Chinese prompt understanding.
- Chinese cultural subjects.
- Chinese text or signage tasks.
- IP-Adapter workflows.

Prompt dialect:

- English or Chinese depending on target content.
- Natural language.
- Negative prompt where exposed.

Template:

```text
[Subject] in [setting], [composition], [materials], [lighting], [camera]. Chinese text: "[text]" placed [location].
```

Community tricks:

- Use Chinese prompt variants for Chinese typography, packaging, signage, or cultural context.
- Label IP-Adapter reference role.

Failure modes:

- Hosted wrappers may differ from local Kolors.
- Text tasks still need iteration.

## Chroma

Evidence level: Community ecosystem.

Use for:

- FLUX-derived local workflows.
- Experiments where the exact checkpoint examples show the expected prompt style.

Prompt dialect:

- Checkpoint-specific.
- Start with FLUX-like natural language.
- Add tags only if examples use them.

Template:

```text
[Subject] in [setting], [composition], [action], [lighting], [camera], [style].
```

Community tricks:

- Ask for exact checkpoint if the user needs precision.
- Follow the example prompts shipped with the checkpoint.

Failure modes:

- Model name alone is not enough.
- Merges and quantized versions can behave differently.

## Unknown Open Model

Use this fallback:

```text
Target: unknown open image model
Format: natural-language prompt plus optional local settings if the UI exposes them

Prompt:
[Subject] in [setting], [composition], [materials], [lighting], [camera or render style]. Exact text: "[text]" at [placement]. Preserve [details].
```

Do not invent:

- Negative prompt support.
- CFG ranges.
- Trigger tags.
- Safety behavior.
- Reference image syntax.
