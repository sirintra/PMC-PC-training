import os
import sys

# Add project root to Python path
sys.path.insert(0, os.path.abspath(".."))

project = "PMC-PC Training"
author = "Sirintra Nakjang"
release = "0.1"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
]

autosummary_generate = True

templates_path = ["_templates"]
exclude_patterns = ["_build"]

#html_theme = "furo"

# If your package imports heavy deps, mock them:
autodoc_mock_imports = ["numpy", "pandas", "scipy", "sklearn"]

# Required metadata for EPUB builds
copyright = "2026, Sirintra Nakjang"
version = "1.0"
epub_version = "3"

