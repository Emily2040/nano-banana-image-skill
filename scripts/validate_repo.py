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
GEMINI_3_RATIOS = {
    "1:1",
    "1:4",
    "1:8",
    "2:3",
    "3:2",
    "3:4",
    "4:1",
    "4:3",
    "4:5",
    "5:4",
    "8:1",
    "9:16",
    "16:9",
    "21:9",
}
LEGACY_RATIOS = {"1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"}
MODEL_SIZE_OPTIONS = {
    "gemini-3.1-flash-image-preview": {"512", "1K", "2K", "4K"},
    "gemini-3-pro-image-preview": {"1K", "2K", "4K"},
    "gemini-2.5-flash-image": {"1K"},
}
MODEL_RATIO_OPTIONS = {
    "gemini-3.1-flash-image-preview": GEMINI_3_RATIOS,
    "gemini-3-pro-image-preview": GEMINI_3_RATIOS,
    "gemini-2.5-flash-image": LEGACY_RATIOS,
}
STYLE_MODULE_DIRS = {
    "genre": "genres",
    "movement": "movements",
    "culture": "cultures",
    "capture": "capture",
    "pipeline": "pipelines",
}
RENDER_FEATURE_DIR = "render-features"


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_schema(name: str) -> Dict[str, Any]:
    return load_json(ROOT / "schemas" / name)


def status(message: str) -> None:
    print(message)


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


def load_gemini_compiler():
    compiler_path = ROOT / "scripts" / "compile_gemini_request.py"
    spec = importlib.util.spec_from_file_location("compile_gemini_request", compiler_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load compile_gemini_request.py")
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


def _word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def _module_names(folder: str) -> set[str]:
    root = ROOT / "skills" / folder
    if not root.exists():
        return set()
    names = set()
    for path in root.glob("*.md"):
        if path.name != "base.md":
            names.add(path.stem)
    for path in root.glob("*/base.md"):
        names.add(path.parent.name)
    return names


def validate_style_modules(authoring_paths: List[Path]) -> None:
    available = {key: _module_names(folder) for key, folder in STYLE_MODULE_DIRS.items()}
    available["render_features"] = _module_names(RENDER_FEATURE_DIR)
    for path in authoring_paths:
        style = load_json(path).get("style", {})
        for key, names in available.items():
            values = style.get(key)
            if values is None:
                continue
            if isinstance(values, str):
                values = [values]
            for value in values or []:
                if value and value not in names:
                    raise ValueError(
                        f"{path.relative_to(ROOT)} references unknown {key} module '{value}'."
                    )


def validate_runtime_options(runtime: Dict[str, Any], source: str) -> None:
    model = runtime["model"]
    aspect_ratio = runtime["aspect_ratio"]
    image_size = runtime["image_size"]
    if aspect_ratio not in MODEL_RATIO_OPTIONS[model]:
        raise ValueError(f"{source}: aspect ratio {aspect_ratio!r} is not supported for {model}.")
    if image_size not in MODEL_SIZE_OPTIONS[model]:
        raise ValueError(f"{source}: image size {image_size!r} is not supported for {model}.")


def validate_prompt_budget(authoring: Dict[str, Any], runtime: Dict[str, Any], source: str) -> None:
    compiler = authoring.get("compiler", {})
    profile = compiler.get("token_budget_profile")
    if not profile:
        return
    budgets = load_json(ROOT / "registry" / "token-budgets.json")
    family = authoring["model_target"]["family"]
    budget = budgets.get("profiles", {}).get(family, {}).get(profile)
    if not budget:
        raise ValueError(f"{source}: unknown token budget profile {family}/{profile}.")
    words = _word_count(runtime["prompt"])
    if words > budget["max_words"]:
        raise ValueError(
            f"{source}: compiled prompt has {words} words, exceeding {family}/{profile} max {budget['max_words']}."
        )


def validate_compiled_parity(
    authoring_paths: List[Path],
    runtime_schema: Dict[str, Any],
    compiler: Any,
) -> None:
    if Draft202012Validator is None:
        raise RuntimeError("jsonschema is required for runtime parity validation.")
    runtime_validator = Draft202012Validator(runtime_schema)
    for authoring_path in authoring_paths:
        runtime_path = ROOT / "examples" / "runtime" / authoring_path.name
        if not runtime_path.exists():
            raise FileNotFoundError(f"Missing runtime example for {authoring_path.name}.")
        authoring = load_json(authoring_path)
        compiled = compiler.compile_runtime(authoring)
        errors = sorted(runtime_validator.iter_errors(compiled), key=lambda e: list(e.path))
        if errors:
            joined = "\n".join(
                f"  - {authoring_path.name}: {'/'.join(map(str, err.path)) or '<root>'}: {err.message}"
                for err in errors
            )
            raise ValueError(f"Compiled runtime failed validation:\n{joined}")
        validate_runtime_options(compiled, authoring_path.name)
        validate_prompt_budget(authoring, compiled, authoring_path.name)
        checked_in = load_json(runtime_path)
        if compiled != checked_in:
            raise ValueError(
                f"{runtime_path.relative_to(ROOT)} is stale. Regenerate it from {authoring_path.relative_to(ROOT)}."
            )


def validate_gemini_request_compilation(runtime_paths: List[Path]) -> None:
    compiler = load_gemini_compiler()
    for runtime_path in runtime_paths:
        runtime = load_json(runtime_path)
        request = compiler.compile_gemini_request(runtime)
        if request.get("model") != runtime["model"]:
            raise ValueError(f"{runtime_path.relative_to(ROOT)} Gemini request model does not match runtime model.")
        body = request.get("body", {})
        contents = body.get("contents", [])
        if not contents or not contents[0].get("parts"):
            raise ValueError(f"{runtime_path.relative_to(ROOT)} Gemini request missing contents parts.")
        if contents[0]["parts"][0].get("text") != runtime["prompt"]:
            raise ValueError(f"{runtime_path.relative_to(ROOT)} Gemini request prompt does not match runtime prompt.")
        image_config = body.get("generationConfig", {}).get("imageConfig", {})
        if image_config.get("aspectRatio") != runtime["aspect_ratio"]:
            raise ValueError(f"{runtime_path.relative_to(ROOT)} Gemini request aspect ratio mismatch.")
        if image_config.get("imageSize") != runtime["image_size"]:
            raise ValueError(f"{runtime_path.relative_to(ROOT)} Gemini request image size mismatch.")


def validate_documentation_assets() -> None:
    html_path = ROOT / "docs" / "index.html"
    html = html_path.read_text(encoding="utf-8")
    refs = set()
    for match in re.finditer(r'\b(?:src|href|content)=["\'](\.?/?assets/[^"\']+)["\']', html):
        refs.add(Path("docs") / match.group(1).lstrip("./"))

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for match in re.finditer(r'!\[[^\]]*\]\((docs/assets/[^)\s]+)(?:\s+"[^"]*")?\)', readme):
        refs.add(Path(match.group(1)))

    missing = [str(path) for path in sorted(refs) if not (ROOT / path).exists()]
    if missing:
        raise FileNotFoundError("Missing referenced documentation assets:\n- " + "\n- ".join(missing))

    for path in sorted(refs):
        absolute = ROOT / path
        if absolute.suffix.lower() == ".png":
            with absolute.open("rb") as handle:
                if handle.read(8) != b"\x89PNG\r\n\x1a\n":
                    raise ValueError(f"{path} is not a valid PNG file.")


def _validate_lite() -> None:
    """Run a dependency-free validation pass."""
    required_paths = [
        ROOT / "README.md",
        ROOT / "SKILL.md",
        ROOT / "AGENTS.md",
        ROOT / "CLAUDE.md",
        ROOT / "GEMINI.md",
        ROOT / "docs" / "index.html",
        ROOT / "docs" / "assets" / "hero-imagegen.png",
        ROOT / "docs" / "assets" / "infographic-imagegen.png",
        ROOT / "schemas" / "authoring-base.json",
        ROOT / "schemas" / "runtime-compact.json",
        ROOT / "schemas" / "pack-format.json",
        ROOT / "scripts" / "compile_runtime.py",
        ROOT / "scripts" / "compile_gemini_request.py",
        ROOT / "agents" / "openai.yaml",
        ROOT / ".github" / "workflows" / "validate.yml",
        ROOT / "references" / "gemini-runtime-preflight.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required_paths if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing required files:\n- " + "\n- ".join(missing))

    validate_documentation_assets()

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
        "generation_config",
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

    status("OK Lite validation passed (dependency-free).")
    status(f"   Authoring examples compiled: {len(authoring_examples)}")


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
        ROOT / "docs" / "assets" / "hero-imagegen.png",
        ROOT / "docs" / "assets" / "infographic-imagegen.png",
        ROOT / "schemas" / "authoring-base.json",
        ROOT / "schemas" / "runtime-compact.json",
        ROOT / "schemas" / "pack-format.json",
        ROOT / "scripts" / "compile_runtime.py",
        ROOT / "scripts" / "compile_gemini_request.py",
        ROOT / "agents" / "openai.yaml",
        ROOT / ".github" / "workflows" / "validate.yml",
        ROOT / "references" / "gemini-runtime-preflight.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required_paths if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing required files:\n- " + "\n- ".join(missing))

    validate_documentation_assets()

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

    pack = load_json(ROOT / "examples" / "pack.sample.json")
    if frontmatter["name"] != pack["name"]:
        raise ValueError(
            f"SKILL.md name '{frontmatter['name']}' does not match pack name '{pack['name']}'."
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
    validate_style_modules(authoring_examples)

    compiler = load_compiler()
    validate_compiled_parity(authoring_examples, runtime_schema, compiler)
    validate_gemini_request_compilation(runtime_examples)

    status("OK Repository validation passed.")
    status(f"   Authoring examples: {len(authoring_examples)}")
    status(f"   Runtime examples:   {len(runtime_examples)}")
    status("   Front-end:          docs/index.html")
    status("   Canonical skill:    SKILL.md")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR Validation failed: {exc}", file=sys.stderr)
        sys.exit(1)
