
# Evidence Discipline

## Purpose

Keep observed facts, requested changes, and inferred details separate.

This prevents the prompt from silently inventing things.

## Three buckets

### Observed
Visible in the source image or explicitly stated by the user.

### Requested
The changes or outcomes the user wants.

### Inferred
Reasonable defaults you add to make the image work.

## Example 1 — product edit

**Observed**
- clear glass bottle
- silver cap
- centered crop
- matte gray background

**Requested**
- emerald marble background
- teal rim light

**Inferred**
- keep tabletop reflection subtle
- preserve front-facing orientation

## Example 2 — portrait generation

**Observed**
- user wants a singer in neon rain
- user wants photoreal

**Requested**
- editorial feel
- 4:5 social crop

**Inferred**
- waist-up framing
- 50mm lens feel
- mixed warm/cool practical lighting

The inferred parts should be reversible defaults, not secret canon.

## Example 3 — historical poster

**Observed**
- spring festival
- Edo-inspired style
- title text provided

**Requested**
- poster layout
- readable text

**Inferred**
- reserve upper title field
- flatten depth for print legibility
- avoid noisy background behind the title

## Discipline rules

- Never present inferred details as if they came from the source.
- When a detail matters a lot, ask instead of inferring.
- In edits, preservation locks should come from observed details first.
- In cultural work, avoid inference when it risks historical or regional error.

## Output habit

In user-facing work, it helps to show a short assumptions block:
- locked from source
- requested by user
- assumed for composition
