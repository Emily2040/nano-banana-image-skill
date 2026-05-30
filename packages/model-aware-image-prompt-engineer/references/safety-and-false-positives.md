# Safety And False Positives

This file is for compliant prompt rewriting. It must not be used to evade safety systems.

## Core Rule

Clarify benign intent. Do not bypass policy.

If a prompt is blocked and the user intent is allowed:

1. Identify the benign goal.
2. Remove ambiguous wording.
3. Use a professional register.
4. Replace metaphor with concrete visual detail.
5. Separate the object from body-focused language when relevant.
6. Make age, consent, medical, documentary, educational, editorial, or product context explicit only when true.
7. Offer a compliant rewrite.

If the user intent is disallowed, refuse the disallowed part and offer a safe alternative.

## Common False Positive Causes

### Ambiguous Age

Risk:

- Youth-coded descriptors.
- School settings.
- Small body descriptors.
- Casual terms that can imply a minor.

Rewrite:

```text
Adult model, age 25, studio fashion catalog pose, structured garment construction, neutral background.
```

Use only when the subject is intended to be an adult.

### Body-Focused Fashion Prompt

Risk:

- The prompt focuses on exposure, body areas, or suggestive framing.

Rewrite:

```text
Studio product photo of an adult-sized satin evening dress on a mannequin, straight-on catalog lighting, plain gray background, garment construction visible.
```

### Medical Or Anatomy Prompt

Risk:

- Casual wording around body parts.
- Injury spectacle.
- Graphic detail without educational context.

Rewrite:

```text
Educational medical diagram, neutral white background, simplified anatomical labels with leader lines, non-graphic clinical illustration style.
```

### Violence Or Injury

Risk:

- Graphic words.
- Gore-focused detail.
- Action framed as spectacle.

Rewrite:

```text
Non-graphic aftermath scene, damaged object on the ground, emergency lighting in the background, no visible injury detail.
```

### Real Person Or Identity Edit

Risk:

- Public figures.
- Face swap.
- Impersonation.
- Deceptive edit.

Rewrite:

```text
Create a fictional adult person with similar broad styling cues: short dark hair, navy suit, studio portrait lighting. Do not copy any real person's face.
```

### Political Or Current Event Image

Risk:

- Persuasion.
- Fabricated public figure imagery.
- Misleading news-like frame.

Rewrite:

```text
Neutral editorial illustration about a public policy topic, symbolic objects on a desk, no real people, no campaign slogans.
```

## Register Fixes

Use the safest accurate register.

Product:

```text
Catalog product image, neutral background, clear material construction, even studio lighting.
```

Fashion:

```text
Fashion editorial image, adult model, garment construction specified by panels, seams, fabric, and hardware.
```

Educational:

```text
Educational diagram, labeled parts, neutral presentation, simplified visual style.
```

Documentary:

```text
Documentary-style scene, neutral observation, no sensational framing.
```

Medical:

```text
Clinical illustration, non-graphic, anatomical labels, educational context.
```

## What Not To Do

Do not provide:

- Coded words for banned subjects.
- Misspellings intended to avoid filters.
- Alternate language tricks for prohibited content.
- Hidden instructions.
- Suggestions to use less moderated platforms.
- Instructions for generating disallowed sexual, violent, deceptive, or abusive imagery.

## Model Notes

### Gemini

- Can be over-cautious.
- Structured prompts can clarify benign intent.
- JSON-style briefs are not a safety bypass.
- Real-person, identity, political, and sensitive context prompts need extra clarity.

### Hosted Open Models

- A hosted wrapper can enforce policy even when the base model is open.
- Civitai, Hugging Face, Replicate, and custom APIs can behave differently.
- Do not assume a local prompt will pass hosted moderation.

### Local Models

- Local workflows vary by checkpoint, safety checker, and UI.
- If a local safety checker blocks benign output, explain that the checker may be conservative and rewrite the prompt in compliant language.
- Do not instruct the user to disable safety systems for disallowed content.

## Rejected Prompt Rewrite Template

```text
Original benign intent:
<one sentence>

Likely ambiguity:
<why the system may have rejected it>

Compliant rewrite:
<prompt>

If still blocked:
<safe alternate prompt or model-surface limitation note>
```

## Safe Alternate Concepts

When a blocked prompt cannot be made acceptable:

- Product-only version.
- Mannequin version.
- Abstract symbolic version.
- Diagram version.
- Fictional adult character version.
- Non-graphic scene version.
- No real-person identity version.

## Prompt Audit

Before returning:

- Remove sexualized framing unless explicitly allowed and platform-appropriate.
- Remove youth-coded ambiguity.
- Remove real-person deception.
- Remove injury spectacle.
- Remove public-figure fabrication.
- Remove policy evasion language.
- Use concrete visual description.
- Keep the user's allowed intent intact.
