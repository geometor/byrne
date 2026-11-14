"""Digital Scriptorium Codex, Visual Pseudocode Engine, and Symbolic Proofs for Oliver Byrne's 1847 Euclid.

Unites Oliver Byrne's *The First Six Books of the Elements of Euclid in Which Coloured
Diagrams and Symbols Are Used Instead of Letters for the Greater Ease of Learners*
(London: William Pickering / Chiswick Press, 1847) with:

1. **Inline Byrne Visual Glyph Roles** (:mod:`geometor.byrne.sphinx_ext`) rendering
   authentic four-color vector micro-glyphs inside Sphinx/HTML/EPUB proof equations
   with bidirectional ``.euclid-graphic`` hover/click highlighting;
2. **Formal Pointer-Free Visual Pseudocode Grammar** (:mod:`geometor.byrne.pseudocode`)
   modeling Byrne's 1847 notation as a typed geometric value-token DSL alongside
   Heath's classical alphabetic Euclid and ``geometor/elements`` formal pseudocode; and
3. **100% Exact Symbolic Constructions & Renderer** (:mod:`geometor.byrne.constructions`,
   :mod:`geometor.byrne.render`) built on :class:`geometor.model.Model` over exact
   SymPy number fields ($\\mathbb{Q}$, $\\mathbb{Q}(\\sqrt{3})$, $\\mathbb{Q}(\\phi)$,
   and cyclotomic pentagonal extensions).
"""

from __future__ import annotations

from geometor.byrne.constructions import (
    PHI,
    PLATE_REGISTRY,
    ByrnePlate,
    build_all_plates,
    build_plate,
    list_plate_ids,
)
from geometor.byrne.palette import (
    BYRNE_COLORS,
    BYRNE_STROKE_STYLES,
    ByrneColorSpec,
    get_color_spec,
)
from geometor.byrne.pseudocode import (
    ROSETTA_PROGRAMS,
    ByrneProgram,
    ByrneStatement,
    RosettaMetrics,
    VisualToken,
    compute_rosetta_metrics,
    get_rosetta_program,
)
from geometor.byrne.render import export_all_plates, export_plate_svg, render_plate_svg

__version__ = "0.1.2"

__all__ = [
    "BYRNE_COLORS",
    "BYRNE_STROKE_STYLES",
    "PHI",
    "PLATE_REGISTRY",
    "ROSETTA_PROGRAMS",
    "ByrneColorSpec",
    "ByrnePlate",
    "ByrneProgram",
    "ByrneStatement",
    "RosettaMetrics",
    "VisualToken",
    "__version__",
    "build_all_plates",
    "build_plate",
    "compute_rosetta_metrics",
    "export_all_plates",
    "export_plate_svg",
    "get_color_spec",
    "get_rosetta_program",
    "list_plate_ids",
    "render_plate_svg",
]
