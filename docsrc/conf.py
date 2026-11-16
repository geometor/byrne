"""Sphinx configuration for GEOMETOR • byrne."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (_REPO_ROOT / "src", _WORKSPACE_ROOT / "model" / "src"):
    if str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.byrne as module  # noqa: E402

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "byrne"
repo_name = "byrne"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

site_title = "Oliver Byrne"
project = site_title
html_title = f"{site_title} • {org_name}"
author = "Oliver Byrne"
copyright = "1847 William Pickering / Chiswick Press · Digital Codex GEOMETOR"

if "geometor.byrne.sphinx_ext" not in extensions:  # noqa: F405
    extensions.append("geometor.byrne.sphinx_ext")  # noqa: F405

html_static_path = ["_static", str(_REPO_ROOT / "src" / "geometor" / "byrne" / "static")]

# Restrict AutoAPI strictly to `src/geometor` and avoid duplicate root index with modules/index.rst
autoapi_dirs = [str(_REPO_ROOT / "src" / "geometor")]
autoapi_add_toctree_entry = False
suppress_warnings = ["autoapi.python_import_resolution"]
if "modules/api/geometor/byrne/index.rst" not in exclude_patterns:  # noqa: F405
    exclude_patterns.append("modules/api/geometor/byrne/index.rst")  # noqa: F405

# Prune remote-only intersphinx targets so offline sandbox builds emit zero network warnings,
# and bind local inventories across the GEOMETOR workspace canon.
for _remote_key in [k for k, v in list(intersphinx_mapping.items()) if v[1] is None]:  # noqa: F405
    del intersphinx_mapping[_remote_key]  # noqa: F405

# Register offline-first local intersphinx inventories across the GEOMETOR canon
for _sister_repo in ("euclid", "elements", "codes", "proclus", "hoenen", "hilbert", "pappus", "model"):
    _local_inv = (_WORKSPACE_ROOT / _sister_repo / "docs" / "objects.inv").resolve()
    if _local_inv.is_file():
        intersphinx_mapping[_sister_repo] = (  # noqa: F405
            f"https://geometor.github.io/{_sister_repo}",
            (str(_local_inv), None),
        )

