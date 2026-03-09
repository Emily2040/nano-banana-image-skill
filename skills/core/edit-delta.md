
# Edit Delta

## Purpose

Write edits as the **smallest set of changes** needed to reach the user's goal.

## Delta formula

1. preserve locks
2. changed region or property
3. new behavior
4. what not to disturb

## Example 1 — background change

"Preserve the exact subject, crop, shadows, and camera angle. Replace only the matte gray background with wet emerald marble featuring subtle diagonal veining. Do not alter bottle reflections beyond the new background color bounce."

## Example 2 — relight

"Keep scene geometry and pose identical. Shift from flat daylight to moody storm twilight with cool ambient fill and a thin back-right cyan edge light. Preserve material realism and do not deepen shadows to the point of detail loss."

## Example 3 — wardrobe swap

"Keep face, pose, crop, and hair unchanged. Replace the black leather jacket with an ivory satin bomber jacket of similar silhouette and fit. Preserve hand position and necklace visibility."

## Delta rules

- Name what stays fixed first.
- Describe only the changed attributes.
- Prevent adjacent drift explicitly.
- Avoid full-scene rewrites unless requested.

## When the delta is too large

If the requested change touches:
- subject identity,
- pose,
- background,
- lighting,
- wardrobe,
- and text,
then it may no longer be a delta edit. Route to composite or regenerate.
