# Evaluation And Iteration

Use this file when a prompt fails, a user compares models, or a local workflow needs diagnosis.

## Review Checklist

Check the output against the prompt:

1. Subject exists.
2. Composition matches.
3. Setting matches.
4. Materials and colors match.
5. Lighting matches.
6. Camera or render style matches.
7. Exact text is present and correct.
8. Reference roles are respected.
9. Preserved details stayed unchanged.
10. Unwanted artifacts are absent.
11. Safety rewrite did not change the benign goal.

## Failure Classification

### Prompt Failure

Signs:

- Subject is vague.
- Relationships are ambiguous.
- Reference roles are not labeled.
- Text is not quoted.
- Prompt mixes incompatible styles.
- Negative statements are inside the positive prompt when the surface has a negative prompt field.

Fix:

- Rewrite the prompt.
- Label references.
- Separate parameters.
- Remove unsupported syntax.

### Model Limitation

Signs:

- Exact text fails across several clean prompts.
- Multi-character identity fails across seeds.
- The model card lists the failed feature as weak.
- The model cannot use image references.

Fix:

- Switch model.
- Simplify text.
- Use a deterministic design tool for text.
- Use editing or inpainting after base generation.

### Workflow Failure

Signs:

- Local checkpoint missing required VAE.
- Wrong text encoder.
- LoRA trigger missing.
- CFG too high or too low.
- Sampler or scheduler mismatch.
- Resolution outside checkpoint range.
- Prompt extension changed the prompt.

Fix:

- Verify workflow settings.
- Restore checkpoint-recommended defaults.
- Test a small grid.

### Safety Or Moderation Failure

Signs:

- Benign prompt blocked.
- Prompt contains ambiguous age, identity, injury, medical, sexual, or political terms.
- Platform blocks a whole category.

Fix:

- Use the compliant rewrite process.
- Switch to a safer concept if needed.
- Do not use evasion tactics.

## Local Testing Grid

Use small grids before rewriting everything.

### Seed Grid

Purpose:

- Identify whether the prompt is sound but the seed failed.

Process:

```text
Prompt fixed.
Settings fixed.
Run 4 to 8 seeds.
```

### Prompt Variant Grid

Purpose:

- Identify whether phrasing is the cause.

Process:

```text
Seed fixed.
Settings fixed.
Compare:
1. concise natural prompt
2. structured natural prompt
3. tag prompt if model supports it
4. reference-labeled edit prompt
```

### Negative Prompt Grid

Purpose:

- Identify whether negative prompt is helping or harming.

Process:

```text
Prompt fixed.
Seed fixed.
Compare:
1. no negative prompt
2. minimal negative prompt
3. targeted negative prompt
```

Do not use a huge universal negative prompt unless it is part of a legacy workflow the user requested.

### Guidance Grid

Purpose:

- Identify whether guidance is over- or under-constraining.

Process:

```text
Prompt fixed.
Seed fixed.
Test low, medium, high guidance inside the model's normal range.
```

Watch for:

- Low guidance: ignored details.
- High guidance: artifacts, stiffness, over-sharpening, layout damage.

## Exact Text Debugging

If text is wrong:

1. Shorten the text.
2. Put exact text in quotes.
3. State location.
4. State case.
5. State font category.
6. Limit other text.
7. Switch to Qwen, Ideogram, Recraft, Gemini, or a deterministic design tool if text remains wrong.

## Multi-Character Debugging

If characters merge:

1. Name each character or person label.
2. State spatial positions.
3. State clothing per character.
4. Avoid pronouns.
5. Use references with one role each.
6. Generate one character sheet first if the model supports it.

Template:

```text
Person A stands on the left wearing [clothing]. Person B stands on the right wearing [clothing]. Person A holds [object]. Person B looks toward Person A. Keep Person A and Person B visually distinct.
```

## Reference Drift Debugging

If references are ignored:

1. Reduce the number of references.
2. Assign one role per reference.
3. State what not to borrow.
4. Increase image guidance if the workflow supports it.
5. Use an edit model instead of a pure generation model.

## Prompt Diff Record

When iterating, keep a compact record:

```text
Run 01:
model:
surface:
prompt:
negative:
settings:
seed:
issue:

Run 02:
change:
result:
```

## Pass Criteria

A prompt is ready when:

- The target model is named.
- The prompt format matches the surface.
- Output-critical details are visible in the prompt.
- Unsupported syntax is removed.
- Safety wording is compliant.
- The user can paste the prompt without needing hidden context.
