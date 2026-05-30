
# Risk Validation

## Purpose

Catch prompt failures before they waste cycles.

## Preflight gates

Run these before compiling the prompt or emitting runtime JSON. If a gate is unknown, ask one targeted question or record a conservative assumption.

### Source-image rights
- Confirm uploaded/source images are user-owned, licensed, commissioned, or otherwise cleared for the requested use.
- Bind each source image to an allowed role: identity, layout, material, style, or primary scene. Do not let a reference control roles it was not cleared to control.
- Treat web-found images as inspiration only unless rights and reuse terms are explicit.

### Likeness and consent
- For identifiable people, confirm consent or clear authority before face-preserving edits, identity transfer, or commercial use.
- Avoid placing real people in sexual, humiliating, criminal, medical, political, or other sensitive contexts unless the user has explicit authorization and the request remains non-deceptive.
- For public figures, keep the prompt non-impersonating and do not imply endorsement or private access.

### Brand and IP
- Check whether logos, labels, product packaging, fictional characters, or franchise elements are owned, licensed, user-provided, or merely inspirational.
- Preserve real brand marks only when the request has a legitimate use case and no false endorsement, counterfeit product, or misleading ad claim.
- Convert protected style or character requests into visual traits when rights are unclear.

### Minors
- Treat children and age-ambiguous subjects conservatively.
- Do not generate sexualized, exploitative, humiliating, or unsafe minor content.
- For source images of minors, require guardian authority and avoid identity-preserving edits in sensitive contexts.

### Deceptive or documentary claims
- If the image could be mistaken for evidence, news, legal proof, product proof, medical proof, or historical documentation, label the output as fictional, staged, simulated, concept art, or illustrative.
- Do not fabricate real events, dates, injuries, endorsements, crimes, documents, or scientific claims.
- Use grounding only for verifiable facts; keep unverified claims out of visible text.

### SynthID and provenance
- Gemini-generated images should be treated as carrying provider provenance such as SynthID. Do not request removal, concealment, or absence of provenance signals.
- Record whether an output is generated, edited, composited, or source-derived in notes when the downstream use might matter.
- Do not claim an edited image is an unaltered photo.

### Transparent-background requests
- Do not promise a true alpha channel from prompt wording alone.
- For cutouts, request a clean high-contrast matte or simple solid background and note that alpha/mask extraction must be verified downstream.
- Set transparent-background expectations only when the runtime or post-process path can actually validate transparency.

### Multi-turn edit sessions
- Carry forward source IDs, preservation locks, allowed deltas, and prior output IDs across turns.
- If the session resets, restate the full preservation/change contract instead of relying on chat memory.
- Note which generated turn became the new source image when chaining edits.

## Check these categories

### Ambiguity
- Is the subject actually clear?
- Are there contradictory style families?
- Is the requested text too vague?

### Preservation risk
- Did you lock the elements that matter?
- Could the camera angle drift?
- Could the label or face drift?

### Real-world plausibility
- Do materials and light agree?
- Do era details collide?
- Is the cultural treatment under-specified?

### Text risk
- Too many words?
- No reserved quiet space?
- Typography tone not specified?

### Policy / compliance
- source-image rights
- likeness consent
- brand marks and IP
- minors
- unsafe or disallowed content
- false documentary implications
- sensitive cultural claims
- SynthID/provenance expectations
- transparent-background limitations

## Example 1 — hidden contradiction

User asks for:
- documentary realism
- surreal dream physics
- exact historical accuracy

That needs arbitration. Ask which one dominates.

## Example 2 — poster overload

User asks for:
- huge scene
- lots of tiny details
- seven lines of text
- vertical cover

Risk:
the scene will eat the typography alive.

Repair:
simplify background, enlarge hierarchy zones, or move some copy outside the image.

## Example 3 — product edit drift

User asks:
> Keep the product identical, but make it more dramatic.

Risk:
"more dramatic" can mutate geometry, crop, or label.

Repair:
spell out the allowed drama vector: lighting only, background only, or composition only.

## Validation output pattern

Useful brief note:
- **Potential risks:** [list]
- **Chosen resolution:** [list]
- **Assumptions:** [list]

That saves future argument with both the model and the client.
