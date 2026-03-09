
# Reference Binding

## Purpose

Bind uploaded or cited references to explicit roles so the model knows what each reference controls.

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
