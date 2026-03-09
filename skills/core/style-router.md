
# Style Router

## Purpose

Build a coherent style stack from the user's request without turning the prompt into adjective soup.

## Style stack order

1. Family
2. Genre
3. Movement
4. Culture
5. Capture
6. Pipeline
7. Render features
8. Profile
9. Platform
10. Overlay

See `registry/style-axes.md` for the canonical registry.

## Routing rules

### Start with family
Choose exactly one dominant family:
- anime
- manga
- photoreal
- stylized-3d
- realistic-3d

### Add genre only if it changes the world
- fantasy introduces mythic logic, creature design, relics, and impossible environments.
- historical introduces era fidelity, costume discipline, and grounded architecture.
- sci-fi introduces speculative systems, interfaces, engineered surfaces, and tech grammar.

### Add movement or culture only if it changes formal structure
- `ukiyo-e` changes line rhythm, flattening, crop logic, and pattern behavior.
- `mughal-miniature` changes ornament density, pose logic, and architectural detailing.

### Add capture or pipeline only if visible in the final image
- `drone` changes angle, scale, and parallax.
- `octane-render` changes finish language and clean CG surface behavior.
- `nuke-composite` suggests plate realism, integration, and post composite logic.

## Example 1 — premium anime character poster

Route:
- family: anime
- profile: poster-layout
- overlay: text-in-image if text is required
- optional genre: fantasy or sci-fi
- optional render feature: volumetric-lighting

Do **not** also add `photoreal` and `realistic-3d` unless hybridization is explicitly desired.

## Example 2 — smartphone low-light street portrait

Route:
- family: photoreal
- capture: iphone-night-mode or pixel-night-sight or nightography
- profile: portrait
- maybe platform: instagram-post or tiktok-vertical

## Example 3 — CG product hero

Route:
- family: realistic-3d
- pipeline: octane-render
- render feature: path-tracing
- profile: product

## Hybrid routing

Hybrid prompts can work if one family stays dominant.

### Good hybrid
"Photoreal base with subtle surrealist impossibilities."

### Bad hybrid
"Photoreal anime manga realistic-3D stylized-3D."

That is not hybrid. That is indecision wearing seven hats.

## Tie-breaker

When two style signals conflict, ask:
- Which one changes the silhouette?
- Which one changes the material language?
- Which one changes the layout?

The most structural signal wins.
