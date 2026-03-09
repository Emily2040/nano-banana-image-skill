
# Style Axes Registry

This registry defines how style components stack inside the skill.

## Canonical stacking order

1. **Family**  
   Base visual language.  
   Examples: `anime`, `manga`, `photoreal`, `stylized-3d`, `realistic-3d`

2. **Genre**  
   Story-world framing.  
   Examples: `fantasy`, `historical`, `sci-fi`

3. **Movement**  
   Formal art movement cues.  
   Examples: `surrealism`, `ukiyo-e`

4. **Culture**  
   Specific historical or regional aesthetics that affect ornament, costume, architecture, symbolism, or composition.  
   Examples: `japanese-edo`, `mughal-miniature`

5. **Capture**  
   Device or capture-language cues.  
   Examples: `iphone-night-mode`, `google-pixel-night-sight`, `samsung-galaxy-nightography`, `drone`

6. **Pipeline**  
   Rendering or post-production pipeline cues.  
   Examples: `unreal-engine-5`, `octane-render`, `nuke-composite`

7. **Render features**  
   Light transport or rendering effects.  
   Examples: `ray-tracing`, `path-tracing`, `volumetric-lighting`

8. **Profile**  
   Deliverable shape.  
   Examples: `portrait`, `product`, `architecture`, `character-sheet`, `infographic`, `poster-layout`, `game-key-art`, `vfx-shot`

9. **Platform**  
   Publishing surface.  
   Examples: `instagram-post`, `tiktok-vertical`, `youtube-vlog`, `podcast-cover`

10. **Overlay**  
    Edit or layout operation layered on top.  
    Examples: `text-in-image`, `background-swap`, `outpaint`, `relight`

---

## Precedence rules

### Family beats everything below it
If the family is `manga`, do not accidentally drift into glossy photoreal lighting language unless the user explicitly wants a hybrid treatment.

### Culture and movement are not decoration
Use them when they change structure, not only color.
For example:
- `ukiyo-e` affects line rhythm, flattening, cropping, and pattern logic.
- `mughal-miniature` affects ornament density, profile poses, architecture, textiles, and jewel handling.

### Capture and pipeline are optional
Do not force a rendering pipeline if the user simply wants a believable photo.
Add these only when they materially improve the result.

### Platform can override composition defaults
For example:
- `tiktok-vertical` may force a taller framing and larger face area.
- `podcast-cover` may require centered subject and uncluttered title space.

### Overlays modify, not replace
`relight` is not a style family.  
`text-in-image` is not a genre.  
Treat overlays as operational layers.

---

## Style stack recipes

### Recipe A — cinematic concept frame
- family: `photoreal`
- genre: `sci-fi`
- capture: `drone`
- render feature: `volumetric-lighting`
- profile: `vfx-shot`

Use when the request sounds like a film still or keyframe.

### Recipe B — poster with disciplined typography
- family: `manga` or `photoreal`
- movement: optional
- culture: optional
- profile: `poster-layout`
- platform: `instagram-post` or `none`
- overlay: `text-in-image`

Use when on-image text must actually survive.

### Recipe C — elegant cultural illustration
- family: `stylized-3d` or `manga`
- genre: `historical`
- culture: `japanese-edo` or `mughal-miniature`
- movement: optional `ukiyo-e`
- profile: `portrait` or `poster-layout`

Use when the cultural frame is central, not ornamental wallpaper.

---

## Anti-patterns

### Bad stack
`photoreal + manga + stylized-3d + realistic-3d + surrealism + iphone-night-mode + octane-render + nuke-composite + path-tracing + ray-tracing`

This is not a style stack. It is a small panic attack.

### Better
`photoreal + sci-fi + drone + volumetric-lighting + vfx-shot`

---

## Example translations

### User says
> Make it feel like a premium anime movie poster.

Translate into:
- family: `anime`
- profile: `poster-layout`
- overlay: `text-in-image` only if text is needed
- direct traits: crisp silhouette hierarchy, disciplined character staging, atmospheric backlight, title-safe negative space

### User says
> Shoot it like a flagship phone in low light.

Translate into:
- family: usually `photoreal`
- capture: one of the smartphone night modules
- direct traits: computational dynamic range, localized sharpening, night color bias, controlled shadow lift

### User says
> I want the ad to look rendered, not photographed.

Translate into:
- family: `realistic-3d` or `stylized-3d`
- pipeline: `octane-render` or `unreal-engine-5`
- render feature: choose only if it adds visible behavior
