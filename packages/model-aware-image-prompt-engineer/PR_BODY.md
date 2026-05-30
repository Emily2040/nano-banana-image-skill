# [codex] Add model-aware image prompt engineer skill

## Summary

Adds a new `model-aware-image-prompt-engineer` skill package for model-specific image prompt generation across commercial, hosted, open-weight, and local image models.

The skill routes prompts by target model, platform surface, task type, supported controls, input image roles, and safety context before writing the final prompt.

## What Changed

- Added `SKILL.md` with routing workflow, evidence labels, prompt output contract, safety rules, and model dialect shortcuts.
- Added model-router reference for target model, surface, task, and control selection.
- Added prompt format reference for natural language, JSON-style briefs, Midjourney prompts, Stable Diffusion local prompts, tag prompts, API payloads, edit prompts, and exact text rendering.
- Added commercial model cards for OpenAI, Gemini Nano Banana, Midjourney, BFL FLUX, Stability, Runway, Ideogram, Firefly, Recraft, Luma, Seedream, and Qwen hosted surfaces.
- Added open and local model cards for Z-Image, Qwen-Image, FLUX local, Stable Diffusion, SDXL, SD3.5, Pony, Illustrious, NoobAI, Animagine, HunyuanImage, HiDream, OmniGen2, Sana, PixArt, Kolors, Chroma, and unknown open models.
- Added safety and false-positive rewrite guidance focused on compliant benign rewrites, not safety evasion.
- Added evaluation and iteration reference for prompt failure diagnosis, seed grids, negative prompt grids, guidance grids, exact text debugging, multi-character debugging, and reference drift.
- Added prompt pack examples.
- Added README with package overview, usage guidance, model coverage, source links, and validation checklist.
- Added hero and infographic assets.

## Why

Generic image prompt guides are now outdated. Current image models use different prompt formats, different controls, different safety behavior, and different community practices.

This skill makes the first step target model routing instead of generic prompt writing.

## Validation

- Reviewed package structure against skill creation guidance.
- Included official, primary, and community source links.
- Marked community tricks separately from official behavior.
- Kept `Coin Image` as an unresolved alias instead of inventing a model card.
- Generated hero image asset.
- Created deterministic infographic image with readable labels.
- Audited generated Markdown for em dash, en dash, ellipsis, and targeted filler terms.

## Notes

The package is added as a companion skill so it does not replace the existing Nano Banana workflow.
