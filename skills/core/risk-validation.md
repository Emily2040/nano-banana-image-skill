
# Risk Validation

## Purpose

Catch prompt failures before they waste cycles.

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
- Likeness concerns
- brand marks
- unsafe or disallowed content
- false documentary implications
- sensitive cultural claims

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
