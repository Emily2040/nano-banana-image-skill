
# Prompt Compiler

## Purpose

Turn the brief into a final production prompt that is:
- specific,
- ordered,
- model-aware,
- and readable by both humans and machines.

## Canonical order

1. **Deliverable**
2. **Subject and action**
3. **Scene and world logic**
4. **Composition and camera**
5. **Lighting and material response**
6. **Style stack**
7. **Edit delta or preservation**
8. **Text/layout instructions**
9. **Avoid / constraint block**

## Base template

```text
Create [deliverable] of [subject] [action] in [setting].
Composition: [shot, framing, camera angle, lens feel, aspect ratio].
Lighting: [key, fill, rim, practicals, atmosphere, material response].
Style: [family + genre + movement/culture + capture/pipeline + render features + profile/platform].
Preserve: [locks] / Change: [delta].
Text: [headline, subhead, safe margins, placement].
Avoid: [must-avoid list].
```

## Example 1 — clean generation prompt

"Create a cinematic editorial portrait of a synth-pop singer pausing beneath rain-slick market awnings in a narrow neon alley at midnight. Waist-up framing from a slightly low angle, 50mm lens feel, shallow but readable depth, 4:5 aspect ratio, reserve soft negative space above the left shoulder. Mixed lighting with cool cyan ambient bounce, warm stall practicals, thin magenta edge light, wet nylon and skin highlights responding naturally to rain mist. Photoreal, sci-fi inflection, smartphone-night realism without over-sharpening. Avoid extra people crossing the foreground, unreadable signage clutter, or exaggerated cyberpunk armor."

## Example 2 — poster with text

"Create a vertical festival poster in a Japanese Edo / ukiyo-e inspired print language. Spring lantern procession crossing a bridge over dark water, flattened depth, elegant pattern rhythm, disciplined negative space in the upper third for the title block. Headline: 'Lanterns of Spring'. Secondary line area below for date and venue. Strong hierarchy, crisp legibility, uncluttered title field, 9:16 layout."

## Example 3 — edit delta

"Edit the source image while preserving the exact bottle silhouette, label geometry, cap position, crop, camera angle, table reflection, and shadow footprint. Change only the background from matte gray to wet emerald marble with subtle veining, and add a narrow teal rim light from back right. Keep the bottle finish realistic and the label text unchanged."

## Compiler rules

- Front-load the image goal.
- Keep one dominant subject.
- Keep the camera sentence explicit.
- State preservation before change when editing.
- Move long avoid lists to the end.
- Use line breaks in UI outputs when readability helps.

## When to split into blocks

Split into labeled sections when:
- the agent or user wants structured review,
- the prompt contains exact copy,
- multiple references must be preserved,
- you need easy comparison between variants.
