
# Interview

## Purpose

Extract the **minimum missing information** needed to write a strong image prompt or edit delta.

The interview is not a customs checkpoint. It is a scalpel.

## Ask in this order

1. **Task mode**  
   Generate, edit, composite, relight, outpaint, or variation?

2. **Subject + action**  
   Who or what is the subject, and what is happening?

3. **Profile + platform**  
   Portrait, product, poster, infographic, vfx shot, etc.  
   Instagram post, TikTok vertical, podcast cover, or none?

4. **Style family**  
   Anime, manga, photoreal, stylized 3D, realistic 3D.

5. **Locks + constraints**  
   What must remain exact? What must never appear?

6. **Text requirements**  
   Is there on-image copy? Exact words? Safe margins?

## Skip the interview when

- the request already specifies subject, scene, profile, and constraints,
- the user clearly does not care about style and wants a fast default,
- the task is a tiny delta edit such as "add soft teal rim light only."

## High-value question patterns

### For vague generation
- What is the main subject?
- What is the subject doing?
- What output shape do you need: portrait, poster, cover, or product shot?
- Do you want speed or maximum fidelity?
- Any must-avoid elements?

### For editing
- What must stay unchanged?
- What is the one thing you want to change first?
- Should framing and camera angle remain locked?
- Do labels, logos, or text need to remain exact?

### For text-in-image
- What exact copy must appear?
- Which text is headline versus supporting copy?
- Do you want empty space reserved for type?
- Should typography feel editorial, technical, festive, or quiet?

## Example 1 — vague ask

**User:**  
> Make me a cool portrait.

**Bad follow-up:**  
> Please specify subject, ethnicity, age, outfit, setting, style, camera, mood, aspect ratio, and lighting.

That is not a follow-up. That is a form letter.

**Better follow-up:**  
> Who is the subject, and do you want this to read as a photo, anime frame, or illustrated poster?

If the user answers "a singer in neon rain, make it photoreal," you can infer plenty of the rest.

## Example 2 — edit ask

**User:**  
> Change the background but keep everything else.

**Good follow-up:**  
> Should I keep the exact crop, shadows, and subject position locked as well?

That one question often saves an entire revision loop.

## Example 3 — poster ask

**User:**  
> I need a spring festival poster.

**Good follow-up:**  
> What exact title text must appear, and is this square, vertical, or print poster format?

## Default assumptions when the user is indifferent

- If no platform is given, use the natural aspect ratio for the profile.
- If no style family is given, choose the most literal interpretation of the request.
- If text is requested but no hierarchy is given, assume headline > subhead > support copy.
- If editing without a preserve list, lock identity, crop, geometry, and main materials by default.

## Failure modes

- Asking ten medium-value questions instead of two high-value ones.
- Asking about style before understanding the actual deliverable.
- Forgetting to ask about on-image text until the end.
- Treating "cool" or "cinematic" as sufficient direction.

## Quick checklist

Before you stop interviewing, do you know:
- what it is,
- what it is doing,
- what format it must fit,
- what must not drift,
- whether text is involved?
