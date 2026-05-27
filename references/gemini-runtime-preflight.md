# Gemini Runtime Preflight

Use this when converting a finished brief into a Gemini/Nano Banana runtime request.

## Provider facts to respect

- Gemini image models can generate, edit, compose, and iterate over images with text plus source images.
- Generated images include SynthID provenance. Do not ask the model to remove, hide, or avoid it.
- Image editing requires rights to uploaded images and must not deceive, harass, or harm.
- Multi-turn editing depends on carrying the conversation context forward. If the API response includes session or thought-signature data, pass it back exactly as required by the runtime.

## Preflight checklist

Before calling the model, confirm:

- source-image rights: owned, licensed, commissioned, or otherwise cleared;
- likeness consent: identifiable people are authorized for this edit and use case;
- brand/IP: logos, labels, products, characters, and style references are cleared or decomposed into generic traits;
- minors: no sexualized, exploitative, unsafe, or sensitive identity-preserving treatment;
- documentary truth: photoreal outputs are not framed as proof of real events unless fact-grounded and allowed;
- provenance: generated/edited/composited status is preserved in handoff notes;
- transparency: alpha is not promised unless downstream tooling validates it;
- session continuity: source IDs, turn IDs, preservation locks, and allowed deltas are carried forward.

## Prompt and payload notes

- Put rights and provenance notes in authoring `safety.policy_notes` or runtime `metadata.notes`; do not add unsupported schema fields.
- Put reference roles and rights boundaries in `edit.source_images[].notes` or runtime `references[].notes`.
- For transparent-background requests, prefer "isolated on solid white" or "cutout-ready on high-contrast matte" unless the post-process path will verify true alpha.
- For multi-turn edits, name the prior output as the new source, then repeat the exact preserve/change list.
