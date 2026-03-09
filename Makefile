
.PHONY: validate compile-examples

validate:
	python scripts/validate_repo.py

compile-examples:
	python scripts/compile_runtime.py examples/authoring/portrait-night-market-editorial.json -o examples/runtime/portrait-night-market-editorial.runtime.generated.json
	python scripts/compile_runtime.py examples/authoring/poster-edo-festival-text.json -o examples/runtime/poster-edo-festival-text.runtime.generated.json
	python scripts/compile_runtime.py examples/authoring/product-bottle-relight.json -o examples/runtime/product-bottle-relight.runtime.generated.json
	python scripts/compile_runtime.py examples/authoring/scifi-drone-vfx-establishing.json -o examples/runtime/scifi-drone-vfx-establishing.runtime.generated.json
	python scripts/compile_runtime.py examples/authoring/infographic-exoplanet-classroom.json -o examples/runtime/infographic-exoplanet-classroom.runtime.generated.json
