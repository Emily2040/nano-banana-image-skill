#!/usr/bin/env python3
"""Compile a rich authoring brief into a compact runtime payload.

This script intentionally uses only the Python standard library so it is easy
to run in constrained agent environments.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDERS = {"", "n/a", "na", "none", "null", "not applicable", "not-applicable"}


def _clean_text(value: Optional[str]) -> str:
    if not isinstance(value, str):
        return ""
    stripped = value.strip()
    if stripped.lower().strip(". ") in PLACEHOLDERS:
        return ""
    return stripped


def _nonempty(items: List[Optional[str]]) -> List[str]:
    return [cleaned for item in items if (cleaned := _clean_text(item))]


def _join_phrases(items: List[str], sep: str = ", ") -> str:
    items = _nonempty(items)
    if not items:
        return ""
    return sep.join(items)


def _dedupe(items: List[str]) -> List[str]:
    seen = set()
    output = []
    for item in _nonempty(items):
        key = item.casefold()
        if key not in seen:
            seen.add(key)
            output.append(item)
    return output


def _style_stack(authoring: Dict[str, Any]) -> List[str]:
    style = authoring.get("style", {})
    output = authoring.get("output", {})
    stack: List[str] = []

    for key in ("family", "genre", "movement", "culture", "capture", "pipeline"):
        value = style.get(key)
        if cleaned := _clean_text(value):
            stack.append(cleaned)

    for feature in style.get("render_features", []) or []:
        if cleaned := _clean_text(feature):
            stack.append(cleaned)

    profile = output.get("profile")
    if cleaned := _clean_text(profile):
        stack.append(cleaned)

    platform = output.get("platform")
    if cleaned := _clean_text(platform):
        stack.append(cleaned)

    text_overlay = authoring.get("text_overlay", {})
    if text_overlay.get("enabled"):
        stack.append("text-in-image")

    task = authoring.get("task")
    if task == "relight":
        stack.append("relight")

    return _dedupe(stack)


def _avoid_items(authoring: Dict[str, Any]) -> List[str]:
    constraints = authoring.get("constraints", {})
    compiler = authoring.get("compiler", {})
    avoid = []
    avoid.extend(constraints.get("must_avoid", []) or [])
    avoid.extend(constraints.get("banned_terms", []) or [])
    if avoid_prompt := _clean_text(compiler.get("avoid_prompt")):
        avoid.append(avoid_prompt)
    return _dedupe(avoid)


def _generation_config(authoring: Dict[str, Any]) -> Dict[str, Any]:
    model = authoring["model_target"]["api_model"]
    output = authoring["output"]
    composition = authoring["composition"]
    config: Dict[str, Any] = {
        "response_modalities": ["TEXT", "IMAGE"],
        "response_format": {
            "image": {
                "aspect_ratio": composition["aspect_ratio"],
                "image_size": output["size_tier"],
            }
        },
    }
    if model in {"gemini-3-pro-image-preview", "gemini-3.1-flash-image-preview"}:
        config["thinking_config"] = {
            "enabled": True,
            "note": "Use chat/session history for multi-turn edits so thought signatures are preserved by the SDK.",
        }
    return config


def _compile_prompt(authoring: Dict[str, Any]) -> str:
    task = authoring["task"]
    intent = authoring["intent"]
    subject = authoring["subject"]
    scene = authoring["scene"]
    composition = authoring["composition"]
    lighting = authoring["lighting"]
    style = authoring["style"]
    output = authoring["output"]
    constraints = authoring["constraints"]
    edit = authoring.get("edit", {})
    text_overlay = authoring.get("text_overlay", {})

    deliverable = output["profile"].replace("-", " ")
    image_goal = _clean_text(intent["goal"])

    subject_bits = _nonempty([
        subject.get("primary"),
        _join_phrases(subject.get("descriptors", []) or []),
        subject.get("action"),
        subject.get("wardrobe"),
        subject.get("pose"),
        subject.get("expression"),
    ])
    subject_sentence = f"{subject_bits[0]}"
    if len(subject_bits) > 1:
        subject_sentence = f"{subject_bits[0]} — " + "; ".join(subject_bits[1:])

    scene_bits = _nonempty([
        scene.get("setting"),
        scene.get("era"),
        scene.get("geography"),
        scene.get("weather"),
        scene.get("time_of_day"),
        scene.get("background"),
    ])
    scene_logic = _join_phrases(scene.get("environment_logic", []) or [])

    comp_bits = _nonempty([
        composition.get("shot_type"),
        composition.get("framing"),
        composition.get("camera_angle"),
        f'{composition.get("lens_equivalent_mm")}mm lens feel' if composition.get("lens_equivalent_mm") else None,
        composition.get("depth_behavior"),
        composition.get("motion"),
        f'negative space: {composition.get("negative_space")}' if composition.get("negative_space") else None,
        f'aspect ratio {composition.get("aspect_ratio")}' if composition.get("aspect_ratio") else None,
    ])

    light_bits = _nonempty([
        f'key light: {lighting.get("key")}' if lighting.get("key") else None,
        f'fill: {lighting.get("fill")}' if lighting.get("fill") else None,
        f'rim: {lighting.get("rim")}' if lighting.get("rim") else None,
        f'practicals: {_join_phrases(lighting.get("practicals", []) or [])}' if lighting.get("practicals") else None,
        lighting.get("atmosphere"),
        f'material response: {_join_phrases(lighting.get("material_response", []) or [])}' if lighting.get("material_response") else None,
        lighting.get("color_temperature"),
    ])

    style_stack = _style_stack(authoring)
    style_bits = style_stack.copy()
    if style.get("texture"):
        style_bits.append(style["texture"])
    if style.get("mood"):
        style_bits.append(style["mood"])
    if style.get("palette"):
        style_bits.append("palette: " + _join_phrases(style["palette"]))
    if style.get("influences"):
        for influence in style["influences"]:
            source = influence.get("source")
            traits = _join_phrases(influence.get("traits", []) or [])
            if source and traits:
                style_bits.append(f"{source} traits: {traits}")

    sentences: List[str] = []
    explicit_prompt = _clean_text(authoring.get("compiler", {}).get("compiled_prompt"))
    if explicit_prompt:
        return explicit_prompt

    normalized_goal = image_goal.rstrip(".")
    lower_goal = normalized_goal.lower()
    starts_with_creation_verb = lower_goal.startswith(("create ", "generate ", "make "))
    if lower_goal.startswith("create "):
        normalized_goal = normalized_goal[7:].strip()
    elif lower_goal.startswith("generate "):
        normalized_goal = normalized_goal[9:].strip()
    elif lower_goal.startswith("make "):
        normalized_goal = normalized_goal[5:].strip()

    goal_fragment = normalized_goal or image_goal or "the requested image goal"
    opener = image_goal
    if not starts_with_creation_verb:
        opener = f"Create a {deliverable} for {goal_fragment}."
    if opener and opener[-1] not in ".!?":
        opener += "."
    if task in {"edit", "relight", "composite", "outpaint", "variation"}:
        goal_text = image_goal or "the requested image goal"
        opener = f"{task.capitalize()} the source image(s) to achieve this goal: {goal_text}."
    sentences.append(opener)

    sentences.append(f"Subject: {subject_sentence}.")
    if scene_bits:
        sentences.append(f"Scene: {_join_phrases(scene_bits)}.")
    if scene_logic:
        sentences.append(f"World logic: {scene_logic}.")
    if comp_bits:
        sentences.append(f"Composition: {_join_phrases(comp_bits)}.")
    if light_bits:
        sentences.append(f"Lighting: {_join_phrases(light_bits)}.")
    if style_bits:
        sentences.append(f"Style stack: {_join_phrases(style_bits)}.")

    if edit:
        preserve = _join_phrases(edit.get("preserve", []) or [])
        change = _join_phrases(edit.get("change", []) or [])
        if preserve:
            sentences.append(f"Preserve exactly: {preserve}.")
        if change:
            sentences.append(f"Change only: {change}.")
        if edit.get("mask_hint"):
            sentences.append(f"Mask hint: {edit['mask_hint']}.")
        if edit.get("delta_priority"):
            sentences.append(f"Delta priority: {edit['delta_priority']}.")

    continuity = authoring.get("continuity", {})
    if continuity:
        locks = _join_phrases(continuity.get("locked_traits", []) or [])
        vary_only = _join_phrases(continuity.get("vary_only", []) or [])
        if locks:
            sentences.append(f"Continuity locks: {locks}.")
        if vary_only:
            sentences.append(f"Allowed variation only in: {vary_only}.")

    if text_overlay.get("enabled"):
        text_parts = []
        for block in text_overlay.get("copy", []) or []:
            role = block.get("role", "text")
            text = block.get("text", "")
            if text:
                text_parts.append(f"{role}: {text}")
        if text_parts:
            sentences.append(f"On-image text: {'; '.join(text_parts)}.")
        placement_bits = _nonempty([
            text_overlay.get("placement"),
            text_overlay.get("safe_margins"),
            text_overlay.get("language"),
        ])
        if placement_bits:
            sentences.append(f"Text layout: {_join_phrases(placement_bits)}.")

    include = _join_phrases(constraints.get("must_include", []) or [])
    avoid = _join_phrases(_avoid_items(authoring))
    accessibility = _join_phrases(constraints.get("accessibility", []) or [])
    if include:
        sentences.append(f"Must include: {include}.")
    if avoid:
        sentences.append(f"Avoid: {avoid}.")
    if accessibility:
        sentences.append(f"Accessibility: {accessibility}.")

    return " ".join(sentences)


def compile_runtime(authoring: Dict[str, Any]) -> Dict[str, Any]:
    prompt = _compile_prompt(authoring)
    runtime: Dict[str, Any] = {
        "schema_version": "1.0.0",
        "mode": authoring["task"],
        "model": authoring["model_target"]["api_model"],
        "prompt": prompt,
        "avoid": _avoid_items(authoring),
        "aspect_ratio": authoring["composition"]["aspect_ratio"],
        "image_size": authoring["output"]["size_tier"],
        "profile": authoring["output"]["profile"],
        "generation_config": _generation_config(authoring),
        "metadata": {
            "family": authoring["style"]["family"],
            "platform": authoring["output"].get("platform", "none"),
            "style_stack": _style_stack(authoring),
            "prompt_word_count": len(prompt.split()),
            "provenance": "Gemini-generated or Gemini-edited output; SynthID watermark expected for generated images.",
            "notes": [
                authoring["model_target"]["reason"],
                authoring["intent"]["use_case"],
            ],
        },
    }

    text_overlay = authoring.get("text_overlay", {})
    if text_overlay:
        runtime["text_overlay"] = {
            "enabled": bool(text_overlay.get("enabled")),
            "blocks": text_overlay.get("copy", []),
            "safe_margins": text_overlay.get("safe_margins", ""),
        }

    edit = authoring.get("edit", {})
    if edit.get("source_images"):
        runtime["references"] = edit["source_images"]
    if edit.get("preserve"):
        runtime["preserve"] = edit["preserve"]
    if edit.get("change"):
        runtime["change"] = edit["change"]

    return runtime


def main() -> None:
    parser = argparse.ArgumentParser(description="Compile an authoring brief into runtime JSON.")
    parser.add_argument("input", type=Path, help="Path to authoring JSON file.")
    parser.add_argument("-o", "--output", type=Path, help="Output path for runtime JSON.")
    args = parser.parse_args()

    authoring = json.loads(args.input.read_text(encoding="utf-8"))
    runtime = compile_runtime(authoring)
    data = json.dumps(runtime, indent=2, ensure_ascii=False)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data + "\n", encoding="utf-8")
    else:
        print(data)


if __name__ == "__main__":
    main()
