
# Reference Binding

## Purpose

Bind uploaded or cited references to explicit roles so the model knows what each reference controls.

## Source intake preflight

Before assigning roles, record what is safe to use:

- origin: user upload, licensed asset, commissioned work, generated output, or web reference;
- rights boundary: owned/cleared, inspiration only, unknown, or needs confirmation;
- likeness consent: required for identifiable people, especially face-preserving edits;
- brand/IP status: real logo/product/character, fictional mark, user-provided mark, or generic trait reference;
- minor status: no minors, adult subjects, age-ambiguous, or guardian authority confirmed.

If rights, consent, or minor status is unclear, do not bind that reference as `identity` or literal `primary` material until resolved.

## Common roles

- `primary` — main composition or subject anchor
- `identity` — face, body, silhouette, key character traits
- `material` — finish, texture, fabric, surface behavior
- `style` — formal treatment, color logic, illustration language
- `layout` — framing, spacing, title field, poster grid

## Binding rules

- State the role of each reference.
- Preserve the strongest role-specific details.
- Avoid inventing hidden details from a reference.
- If references conflict, prioritize the user-named primary reference.
- Do not let a style reference override likeness, consent, brand, or age constraints.
- Treat web references as `style`, `layout`, or `material` only unless reuse rights are explicit.
- Keep source IDs stable across multi-turn edits; when a generated result becomes the next source, mark it as a generated turn in the notes.
- For transparent-background work, bind the source subject separately from the background target and note that alpha must be verified downstream.

## Example 1 — face + wardrobe + stage

Reference A: identity  
Reference B: wardrobe  
Reference C: stage lighting

Compiled instruction:
"Use A for face shape, hairline, and expression; B for jacket cut and surface finish; C for stage scale, color lighting, and crowd depth."

## Example 2 — product relight

Reference A: product geometry  
Reference B: marble material inspiration

Compiled instruction:
"Preserve product silhouette, cap, label placement, and crop from A. Use B only to guide the emerald marble background material and surface veining."

## Example 3 — poster layout

Reference A: composition and negative space  
Reference B: text style hierarchy  
Reference C: cultural pattern motifs

Compiled instruction:
"Keep layout spacing from A, use B for headline/subhead hierarchy, and borrow only ornamental pattern logic from C."

## Failure modes

- letting a style reference accidentally override identity,
- letting a layout reference change costume or props,
- treating a texture board as a full-scene composition.

## Reference checklist

For each reference, ask:
- What is this controlling?
- What should it **not** control?
- Which visible details are essential?
- Which hidden details must remain unspecified?
- Is this source cleared for the requested use?
- Is likeness consent or guardian authority needed?
- Could this imply a real brand endorsement, copyrighted character use, or documentary claim?
- Does this turn depend on prior session context or generated outputs?
