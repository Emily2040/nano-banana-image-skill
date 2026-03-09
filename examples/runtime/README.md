
# Runtime Examples

These files validate against `schemas/runtime-compact.json`.

## Included examples

- `portrait-night-market-editorial.json`
- `poster-edo-festival-text.json`
- `product-bottle-relight.json`
- `scifi-drone-vfx-establishing.json`
- `infographic-exoplanet-classroom.json`

Each runtime example includes:
- selected model,
- compiled production prompt,
- aspect ratio,
- image size,
- compact metadata,
- text, reference, preserve, and change blocks when relevant.

## Notes

The runtime payloads are compact on purpose:
- human-readable enough for review,
- structured enough for downstream tooling,
- small enough to stay practical inside agent workflows.
