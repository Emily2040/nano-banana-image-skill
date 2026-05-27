#!/usr/bin/env python3
"""Compile runtime JSON into a Gemini image-generation request skeleton.

The output keeps binary reference images out of band: callers should attach
their actual image bytes or files using the SDK/client they run with.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict


def _camel_generation_config(runtime: Dict[str, Any]) -> Dict[str, Any]:
    image_config = runtime["generation_config"]["response_format"]["image"]
    config: Dict[str, Any] = {
        "responseModalities": runtime["generation_config"]["response_modalities"],
        "imageConfig": {
            "aspectRatio": image_config["aspect_ratio"],
            "imageSize": image_config["image_size"],
        },
    }
    thinking = runtime["generation_config"].get("thinking_config")
    if thinking:
        config["thinkingConfig"] = {
            key: value
            for key, value in {
                "enabled": thinking.get("enabled"),
                "includeThoughts": thinking.get("include_thoughts"),
            }.items()
            if value is not None
        }
    return config


def compile_gemini_request(runtime: Dict[str, Any]) -> Dict[str, Any]:
    request: Dict[str, Any] = {
        "model": runtime["model"],
        "body": {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": runtime["prompt"],
                        }
                    ],
                }
            ],
            "generationConfig": _camel_generation_config(runtime),
        },
    }
    if runtime.get("references"):
        request["reference_placeholders"] = runtime["references"]
    return request


def main() -> None:
    parser = argparse.ArgumentParser(description="Compile runtime JSON into a Gemini request skeleton.")
    parser.add_argument("input", type=Path, help="Path to runtime JSON file.")
    parser.add_argument("-o", "--output", type=Path, help="Output path for Gemini request JSON.")
    args = parser.parse_args()

    runtime = json.loads(args.input.read_text(encoding="utf-8"))
    request = compile_gemini_request(runtime)
    data = json.dumps(request, indent=2, ensure_ascii=False)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data + "\n", encoding="utf-8")
    else:
        print(data)


if __name__ == "__main__":
    main()
