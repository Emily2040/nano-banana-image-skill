
# Slop Scrubber

## Purpose

Remove prompt filler that sounds impressive but directs almost nothing.

See `registry/forbidden-slop.json`.

## Slop categories

### Empty prestige words
- masterpiece
- award-winning
- best quality
- stunning
- breathtaking

### Duplicate specificity
- ultra detailed + hyper detailed + insanely detailed
- cinematic + filmic + movie-like

### Redundant render flexing
- unreal engine + octane + path tracing + nuke + ray tracing
when the image only needs one or none

## Scrub rules

1. Replace prestige with physics.
2. Replace mood mush with lighting.
3. Replace "beautiful composition" with framing language.
4. Replace "highly detailed" with actual visible details.
5. Keep only the one pipeline cue that really matters.

## Example 1

**Before:**  
"Masterpiece ultra detailed 8k cinematic portrait with incredible lighting."

**After:**  
"Waist-up portrait with soft key from front-left, narrow amber rim light, cool ambient fill, visible skin texture, satin jacket highlights, and uncluttered background."

## Example 2

**Before:**  
"Epic futuristic cyberpunk alley trending on artstation."

**After:**  
"Narrow rain-soaked alley with stacked bilingual signs, wet asphalt reflections, cool haze depth, and overhead cable clutter, viewed from a low drifting camera."

## Example 3

**Before:**  
"Beautiful product photography."

**After:**  
"Centered product shot with controlled top softbox, crisp label readability, restrained side reflections, matte white sweep, and subtle shadow anchor."

## Keep the useful parts

Do **not** scrub away:
- preservation locks,
- negative space requests,
- exact copy,
- style family,
- cultural grounding,
- lighting structure,
- material cues.

The goal is not minimalism for its own sake.  
The goal is to stop the prompt from cosplaying as useful.
