#!/usr/bin/env python3
"""Validate the Nano Banana Image Skill repository."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Dict, Any, List

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - optional dependency in constrained envs
    yaml = None

try:
    from jsonschema import Draft202012Validator  # type: ignore
except Exception:  # pragma: no cover - optional dependency in constrained envs
    Draft202012Validator = None


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_schema(name: str) -> Dict[str, Any]:
    return load_json(ROOT / "schemas" / name)


def parse_frontmatter(path: Path) -> Dict[str, Any]:
    if yaml is None:
        raise RuntimeError(
            "PyYAML is required to parse SKILL.md frontmatter. Install with: "
            "python -m pip install -r requirements-dev.txt or run --lite"
        )
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        raise ValueError(f"{path} is missing YAML frontmatter.")
    return yaml.safe_load(match.group(1))


def load_compiler():
    compiler_path = ROOT / "scripts" / "compile_runtime.py"
    spec = importlib.util.spec_from_file_location("compile_runtime", compiler_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load compile_runtime.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_json_files(schema: Dict[str, Any], paths: List[Path]) -> None:
    if Draft202012Validator is None:
        raise RuntimeError(
            "jsonschema is required for schema validation. Install with: "
            "python -m pip install -r requirements-dev.txt or run --lite"
        )
    validator = Draft202012Validator(schema)
    for path in paths:
        instance = load_json(path)
        errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
        if errors:
            joined = "\n".join(f"  - {path}: {'/'.join(map(str, err.path)) or '<root>'}: {err.message}" for err in errors)
            raise ValueError(f"Schema validation failed:\n{joined}")


def _validate_lite() -> None:
    """Run a dependency-free validation pass."""
    required_paths = [
        ROOT / "README.md",
        ROOT / "SKILL.md",
        ROOT / "AGENTS.md",
        ROOT / "CLAUDE.md",
        ROOT / "GEMINI.md",
        ROOT / "docs" / "index.html",
        ROOT / "schemas" / "authoring-base.json",
        ROOT / "schemas" / "runtime-compact.json",
        ROOT / "schemas" / "pack-format.json",
        ROOT / "scripts" / "compile_runtime.py",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required_paths if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing required files:\n- " + "\n- ".join(missing))

    compiler = load_compiler()
    authoring_examples = sorted((ROOT / "examples" / "authoring").glob("*.json"))
    if not authoring_examples:
        raise ValueError("No authoring examples found.")

    required_runtime_keys = {
        "schema_version",
        "mode",
        "model",
        "prompt",
        "avoid",
        "aspect_ratio",
        "image_size",
        "profile",
        "metadata",
    }

    for authoring_path in authoring_examples:
        authoring = load_json(authoring_path)
        compiled = compiler.compile_runtime(authoring)
        missing_keys = sorted(required_runtime_keys - set(compiled.keys()))
        if missing_keys:
            raise ValueError(
                f"Lite validation failed for {authoring_path.name}; missing runtime keys: {', '.join(missing_keys)}"
            )

    print("✅ Lite validation passed (dependency-free).")
    print(f"   Authoring examples compiled: {len(authoring_examples)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the Nano Banana Image Skill repository.")
    parser.add_argument(
        "--lite",
        action="store_true",
        help="Run dependency-free checks only (skips YAML and JSON Schema validation).",
    )
    args = parser.parse_args()

    if args.lite:
        _validate_lite()
        return

    required_paths = [
        ROOT / "README.md",
        ROOT / "SKILL.md",
        ROOT / "AGENTS.md",
        ROOT / "CLAUDE.md",
        ROOT / "GEMINI.md",
        ROOT / "docs" / "index.html",
        ROOT / "docs" / ".nojekyll",
        ROOT / "schemas" / "authoring-base.json",
        ROOT / "schemas" / "runtime-compact.json",
        ROOT / "schemas" / "pack-format.json",
        ROOT / "scripts" / "compile_runtime.py",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required_paths if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing required files:\n- " + "\n- ".join(missing))

    if yaml is None or Draft202012Validator is None:
        missing_deps = []
        if yaml is None:
            missing_deps.append("PyYAML")
        if Draft202012Validator is None:
            missing_deps.append("jsonschema")
        joined = ", ".join(missing_deps)
        raise RuntimeError(
            f"Missing required dev dependency/dependencies: {joined}. "
            "Install with: python -m pip install -r requirements-dev.txt, or run: "
            "python scripts/validate_repo.py --lite"
        )

    frontmatter = parse_frontmatter(ROOT / "SKILL.md")
    for key in ("name", "description"):
        if key not in frontmatter or not str(frontmatter[key]).strip():
            raise ValueError(f"SKILL.md frontmatter missing required field: {key}")

    if frontmatter["name"] != ROOT.name:
        raise ValueError(
            f"SKILL.md name '{frontmatter['name']}' does not match repo directory '{ROOT.name}'."
        )

    authoring_schema = load_schema("authoring-base.json")
    runtime_schema = load_schema("runtime-compact.json")
    pack_schema = load_schema("pack-format.json")

    authoring_examples = sorted((ROOT / "examples" / "authoring").glob("*.json"))
    runtime_examples = sorted((ROOT / "examples" / "runtime").glob("*.json"))
    if not authoring_examples:
        raise ValueError("No authoring examples found.")
    if not runtime_examples:
        raise ValueError("No runtime examples found.")

    validate_json_files(authoring_schema, authoring_examples)
    validate_json_files(runtime_schema, runtime_examples)
    validate_json_files(pack_schema, [ROOT / "examples" / "pack.sample.json"])

    compiler = load_compiler()
    runtime_validator = Draft202012Validator(runtime_schema)
    for authoring_path in authoring_examples:
        authoring = load_json(authoring_path)
        compiled = compiler.compile_runtime(authoring)
        errors = sorted(runtime_validator.iter_errors(compiled), key=lambda e: list(e.path))
        if errors:
            joined = "\n".join(f"  - {authoring_path.name}: {'/'.join(map(str, err.path)) or '<root>'}: {err.message}" for err in errors)
            raise ValueError(f"Compiled runtime failed validation:\n{joined}")

    print("✅ Repository validation passed.")
    print(f"   Authoring examples: {len(authoring_examples)}")
    print(f"   Runtime examples:   {len(runtime_examples)}")
    print("   Front-end:          docs/index.html")
    print("   Canonical skill:    SKILL.md")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"❌ Validation failed: {exc}", file=sys.stderr)
        sys.exit(1)
