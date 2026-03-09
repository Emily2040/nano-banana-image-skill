
# Authoring Examples

These files validate against `schemas/authoring-base.json`.

## Included examples

- `portrait-night-market-editorial.json`  
  Photoreal editorial portrait, fast concept path, smartphone-night capture cues.

- `poster-edo-festival-text.json`  
  Edo / ukiyo-e inspired festival poster with explicit on-image text hierarchy.

- `product-bottle-relight.json`  
  Preservation-heavy product edit with background swap and relight instructions.

- `scifi-drone-vfx-establishing.json`  
  Airborne VFX-style establishing frame for a sci-fi pitch deck.

- `infographic-exoplanet-classroom.json`  
  Classroom-ready exoplanet infographic with labeled modules.

## Usage

Compile any authoring example into runtime JSON:

```bash
python scripts/compile_runtime.py examples/authoring/poster-edo-festival-text.json   -o /tmp/poster.runtime.json
```

Use authoring examples when you need:
- a richer brief,
- explicit assumptions,
- preservation logic,
- a planning-stage artifact before runtime execution.
