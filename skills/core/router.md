
# Router

## Purpose

Choose the correct **task mode**, **model target**, and **module stack** before writing the prompt.

## Primary modes

### `generate`
Create a new image from text and optional references.

### `edit`
Preserve an existing image while changing one or more specific elements.

### `composite`
Combine multiple references or subjects into one new composition.

### `relight`
Change lighting conditions while preserving scene geometry and subject identity.

### `outpaint`
Extend canvas beyond current edges.

### `variation`
Generate alternate versions with controlled continuity.

## Model selection

### Prefer Nano Banana Pro when
- the image contains meaningful text,
- layout precision matters,
- the instruction chain is long or multi-part,
- the output is client-facing and premium,
- the edit requires aggressive preservation.

### Prefer Nano Banana 2 when
- you need fast exploration,
- you want multiple variants quickly,
- the image is concept-first and text-light,
- the edit is straightforward,
- the user clearly values speed.

### Prefer Nano Banana when
- you need a light legacy fast path,
- the task is simple,
- the environment is constrained.

## Routing matrix

| Request pattern | Mode | Typical model | Extra modules |
|---|---|---|---|
| "make a poster" | generate | Pro | poster-layout, text-layout, text-in-image |
| "change only the background" | edit | Pro | preservation, edit-delta, background-swap |
| "same character in three moods" | variation | Pro or 2 | continuity, reference-binding |
| "extend the image upward for a banner" | outpaint | Pro or 2 | outpaint, composition-camera |
| "turn this into a drone shot" | edit or variation | 2 | drone, vfx-shot |
| "clean infographic with readable labels" | generate | Pro | infographic, text-layout |

## Example 1 — product page image

**User:**  
> White background ecommerce shot of a ceramic bottle with readable label.

Route to:
- mode: `generate`
- model: `nano-banana-pro`
- profile: `product`
- overlay: maybe none
- likely extras: `text-layout` if label legibility matters

## Example 2 — mood-only change

**User:**  
> Keep the same scene but make it feel like storm twilight.

Route to:
- mode: `relight` or `edit`
- model: `nano-banana-pro` if preservation is strict, otherwise `nano-banana-2`
- extras: `preservation`, `lighting-materials`, `edit-delta`

## Example 3 — multiple refs

**User:**  
> Use this face, this jacket, and this stage photo to build one poster.

Route to:
- mode: `composite`
- model: `nano-banana-pro`
- extras: `reference-binding`, `preservation`, `poster-layout`, `text-layout`

## Escalation rules

Escalate to **Pro** if any of these appear:
- exact text,
- infographic,
- dense poster layout,
- brand-sensitive product labels,
- "keep it exactly the same except...",
- series continuity with tight locks.

## Common routing mistakes

- treating `relight` as a full scene rewrite,
- choosing a fast model for typography-heavy work,
- forgetting that posters are layout problems, not just pretty pictures,
- using `generate` when the user clearly wants preservation from a source image.
