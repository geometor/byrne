"""Chiswick Press Typographic & Synthesis SVG Tableaux for Oliver Byrne's 1847 Codex.

Generates theme-adaptive ``.euclid-graphic`` SVG plates for the non-spatial and
synthesizing sections of *The First Six Books of the Elements of Euclid* (1847):

- ``preliminaries``: Introduction Right-Triangle Manifesto (pp. x–xi), Definition IX
  plane rectilinear angle (p. xviii), Definition XXXIII rhomboid & XXXV parallel lines (p. xxii).
- ``v_defs``: Book V, Definition V Eudoxian Criterion of Same Ratio (p. 154, ``0188.jpg``).
- ``v11``: Book V, Proposition XI — Transitivity of Ratios (p. 175, ``0209.jpg``).
- ``v16``: Book V, Proposition XVI — *Alternando* (p. 181, ``0215.jpg``).
- ``v18``: Book V, Proposition XVIII — *Componendo* (p. 185, ``0219.jpg``).
- ``v22``: Book V, Proposition XXII — *Ex Aequali* (p. 193, ``0227.jpg``).
- ``rosetta``: Unit VII 3-Way Rosetta Synthesis (Heath 1908 · Byrne 1847 · GEOMETOR DAG).
"""

from __future__ import annotations

import html
from collections.abc import Callable
from pathlib import Path

from geometor.byrne.palette import byrne_css_variables
from geometor.byrne.render import SVG_TICK_DEFS

__all__ = [
    "TABLEAU_FOLIO_MAP",
    "TABLEAU_IDS",
    "export_all_tableaux",
    "render_tableau_svg",
]

TABLEAU_FOLIO_MAP: dict[str, str] = {
    "preliminaries": "0014",
    "v_defs": "0185",
    "v11": "0209",
    "v16": "0215",
    "v18": "0219",
    "v22": "0227",
    "rosetta": "0082",
}

TABLEAU_STYLE: str = (
    byrne_css_variables()
    + """
  .euclid-graphic .svg-bg { fill: var(--geom-bg); }
  .euclid-graphic .byrne-stroke-red { stroke: var(--byrne-red); }
  .euclid-graphic .byrne-stroke-blue { stroke: var(--byrne-blue); }
  .euclid-graphic .byrne-stroke-yellow { stroke: var(--byrne-yellow); }
  .euclid-graphic .byrne-stroke-black { stroke: var(--byrne-black); }
  .euclid-graphic .byrne-stroke-none { stroke: none; }
  .euclid-graphic .byrne-fill-red { fill: var(--byrne-fill-red); }
  .euclid-graphic .byrne-fill-blue { fill: var(--byrne-fill-blue); }
  .euclid-graphic .byrne-fill-yellow { fill: var(--byrne-fill-yellow); }
  .euclid-graphic .byrne-fill-black { fill: var(--byrne-fill-black); }
  .euclid-graphic .byrne-fill-none { fill: none; }
  .euclid-graphic .byrne-dotted { stroke-dasharray: 2.6 3.8; }
  .euclid-graphic .byrne-dashed { stroke-dasharray: 7 4.2; }
  .euclid-graphic .byrne-plate-line { fill: none; stroke-width: 3.6; stroke-linecap: round; }
  .euclid-graphic .byrne-plate-circle { fill: none; stroke-width: 2.7; stroke-linecap: round; }
  .euclid-graphic .byrne-plate-poly { stroke-linejoin: round; stroke-width: 2.2; }
  .euclid-graphic .byrne-plate-wedge { fill-opacity: 0.88; stroke-width: 1.4; stroke-linejoin: round; }
  .euclid-graphic .byrne-ink {
    fill: var(--geom-fg);
    font-family: "EB Garamond", "Cochineal", "Georgia", serif;
  }
  .euclid-graphic .byrne-caption {
    fill: var(--geom-fg);
    opacity: 0.78;
    font-size: 13px;
    font-style: italic;
    font-family: "EB Garamond", "Georgia", serif;
  }
  .euclid-graphic .byrne-heading {
    fill: var(--geom-fg);
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.08em;
    font-family: "EB Garamond", "Georgia", serif;
  }
  .euclid-graphic .byrne-op-text {
    fill: var(--geom-fg);
    font-size: 21px;
    font-weight: 600;
    font-family: "EB Garamond", "Georgia", serif;
  }
  .euclid-graphic .byrne-mult {
    fill: var(--geom-fg);
    font-size: 19px;
    font-style: italic;
    font-weight: 600;
    font-family: "EB Garamond", "Georgia", serif;
  }
  .euclid-graphic .byrne-rule {
    stroke: var(--geom-fg);
    stroke-opacity: 0.22;
    stroke-width: 1.1;
  }
  .euclid-graphic .byrne-frac-bar {
    stroke: var(--geom-fg);
    stroke-width: 2.0;
    stroke-linecap: round;
  }
"""
)


def _wrap_svg(slug: str, title: str, width: int, height: int, body_lines: list[str]) -> str:
    folio = TABLEAU_FOLIO_MAP.get(slug, "")
    folio_attr = f' data-folio="{html.escape(folio)}" data-graphic="g1"' if folio else ""
    return "\n".join(
        [
            (
                f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
                f'viewBox="0 0 {width} {height}" width="{width}" height="{height}" '
                f'data-graphic-id="{html.escape(slug)}"{folio_attr} role="img" '
                f'aria-label="{html.escape(title)}">'
            ),
            f"  <title>{html.escape(title)}</title>",
            SVG_TICK_DEFS,
            "  <style>",
            TABLEAU_STYLE,
            "  </style>",
            f'  <rect class="svg-bg" x="0" y="0" width="{width}" height="{height}" rx="6" />',
            '  <g id="elements">',
            '    <g id="graphics">',
            *body_lines,
            "    </g>",
            '    <g id="highlights"></g>',
            '    <g id="points"></g>',
            '    <g id="labels"></g>',
            "  </g>",
            "</svg>",
            "",
        ]
    )


def _tok_circle(cx: float, cy: float, color: str, r: float = 11.5, outline: bool = False) -> str:
    fill_cls = "byrne-fill-none" if outline else f"byrne-fill-{color}"
    sw = "2.5" if outline else "1.5"
    return (
        f'      <circle class="{fill_cls} byrne-stroke-{color}" '
        f'cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" stroke-width="{sw}" />'
    )


def _tok_square(cx: float, cy: float, color: str, s: float = 21.0, outline: bool = False) -> str:
    fill_cls = "byrne-fill-none" if outline else f"byrne-fill-{color}"
    sw = "2.5" if outline else "1.5"
    x = cx - 0.5 * s
    y = cy - 0.5 * s
    return (
        f'      <rect class="{fill_cls} byrne-stroke-{color}" '
        f'x="{x:.1f}" y="{y:.1f}" width="{s:.1f}" height="{s:.1f}" stroke-width="{sw}" />'
    )


def _tok_diamond(cx: float, cy: float, color: str, r: float = 13.0, outline: bool = False) -> str:
    fill_cls = "byrne-fill-none" if outline else f"byrne-fill-{color}"
    sw = "2.4" if outline else "1.4"
    pts = f"{cx:.1f},{cy - r:.1f} {cx + r * 0.88:.1f},{cy:.1f} {cx:.1f},{cy + r:.1f} {cx - r * 0.88:.1f},{cy:.1f}"
    return (
        f'      <polygon class="{fill_cls} byrne-stroke-{color}" '
        f'points="{pts}" stroke-width="{sw}" stroke-linejoin="round" />'
    )


def _tok_shield(cx: float, cy: float, color: str, s: float = 12.0, outline: bool = False) -> str:
    fill_cls = "byrne-fill-none" if outline else f"byrne-fill-{color}"
    sw = "2.5" if outline else "1.5"
    x0, x1 = cx - s * 0.88, cx + s * 0.88
    y0, ym, y1 = cy - s * 0.92, cy + s * 0.08, cy + s * 1.02
    d = (
        f"M {x0:.1f} {y0:.1f} H {x1:.1f} V {ym:.1f} "
        f"C {x1:.1f} {cy + s * 0.65:.1f} {cx:.1f} {y1:.1f} {cx:.1f} {y1:.1f} "
        f"C {cx:.1f} {y1:.1f} {x0:.1f} {cy + s * 0.65:.1f} {x0:.1f} {ym:.1f} Z"
    )
    return (
        f'      <path class="{fill_cls} byrne-stroke-{color}" '
        f'd="{d}" stroke-width="{sw}" stroke-linejoin="round" />'
    )


def _tok_tri(cx: float, cy: float, color: str, r: float = 11.5) -> str:
    pts = f"{cx:.1f},{cy - r:.1f} {cx + r * 0.95:.1f},{cy + r * 0.85:.1f} {cx - r * 0.95:.1f},{cy + r * 0.85:.1f}"
    return (
        f'      <polygon class="byrne-fill-{color} byrne-stroke-{color}" '
        f'points="{pts}" stroke-width="1.4" stroke-linejoin="round" />'
    )


def _tok_crescent(cx: float, cy: float, color: str, r: float = 11.5) -> str:
    d = (
        f"M {cx - r:.1f} {cy + 4:.1f} "
        f"A {r:.1f} {r:.1f} 0 0 1 {cx + r:.1f} {cy + 4:.1f} "
        f"Q {cx:.1f} {cy + r * 0.95:.1f} {cx - r:.1f} {cy + 4:.1f} Z"
    )
    return (
        f'      <path class="byrne-fill-none byrne-stroke-{color}" '
        f'd="{d}" stroke-width="2.4" stroke-linejoin="round" />'
    )


def _txt(x: float, y: float, text: str, cls: str = "byrne-op-text", anchor: str = "middle") -> str:
    return (
        f'      <text class="{cls}" x="{x:.1f}" y="{y:.1f}" '
        f'text-anchor="{anchor}">{html.escape(text)}</text>'
    )


def _build_preliminaries() -> str:
    lines = [
        # Column dividers
        '      <line class="byrne-rule" x1="232" y1="26" x2="232" y2="294" />',
        '      <line class="byrne-rule" x1="456" y1="26" x2="456" y2="294" />',
        # Panel 1: Introduction Right Triangle (pp. x–xi)
        _txt(120, 42, "INTRODUCTION (pp. x–xi)", "byrne-heading"),
        # Right angle wedge & acute wedges at (52, 224), (192, 224), (52, 84)
        '      <path class="byrne-fill-none byrne-stroke-black" d="M 52 198 H 78 V 224" stroke-width="1.8" />',
        '      <path class="byrne-plate-wedge byrne-fill-yellow byrne-stroke-yellow" d="M 52 84 L 52 118 A 34 34 0 0 0 76 108 Z" />',
        '      <path class="byrne-plate-wedge byrne-fill-blue byrne-stroke-blue" d="M 192 224 L 158 224 A 34 34 0 0 1 168 200 Z" />',
        '      <path class="byrne-plate-line byrne-stroke-blue" d="M 52 84 L 52 154 L 52 224" />',
        '      <path class="byrne-plate-line byrne-stroke-yellow" d="M 52 224 L 122 224 L 192 224" />',
        '      <path class="byrne-plate-line byrne-stroke-red" d="M 52 84 L 122 154 L 192 224" />',
        _txt(120, 268, "Self-naming colored primitives", "byrne-caption"),
        # Panel 2: Definitions IX & XXXIII (pp. xviii, xxii)
        _txt(344, 42, "DEFINITIONS (pp. xviii–xxii)", "byrne-heading"),
        # Def IX angle
        '      <path class="byrne-plate-wedge byrne-fill-yellow byrne-stroke-yellow" d="M 268 148 L 316 148 A 48 48 0 0 0 307 120 Z" />',
        '      <path class="byrne-plate-line byrne-stroke-red" d="M 268 148 L 328 148 L 388 148" />',
        '      <path class="byrne-plate-line byrne-stroke-blue" d="M 268 148 L 316 113 L 364 78" />',
        # Def XXXIII rhomboid
        '      <path class="byrne-plate-line byrne-stroke-blue" d="M 292 184 L 348 184 L 404 184" />',
        '      <path class="byrne-plate-line byrne-stroke-blue" d="M 268 232 L 324 232 L 380 232" />',
        '      <path class="byrne-plate-line byrne-stroke-red" d="M 268 232 L 280 208 L 292 184" />',
        '      <path class="byrne-plate-line byrne-stroke-red" d="M 380 232 L 392 208 L 404 184" />',
        _txt(344, 268, "Def. IX angle · Def. XXXIII rhomboid", "byrne-caption"),
        # Panel 3: Def XXXV Parallels & Postulates I–III
        _txt(568, 42, "POSTULATES I–III (pp. xxii–xxiii)", "byrne-heading"),
        '      <path class="byrne-plate-line byrne-stroke-yellow" d="M 492 86 L 568 86 L 644 86" />',
        '      <path class="byrne-plate-line byrne-stroke-red" d="M 492 108 L 568 108 L 644 108" />',
        '      <circle class="byrne-plate-circle byrne-stroke-blue" cx="546" cy="190" r="44" />',
        '      <circle class="byrne-plate-circle byrne-stroke-red" cx="590" cy="190" r="44" />',
        '      <path class="byrne-plate-line byrne-stroke-black" d="M 546 190 L 568 190 L 590 190" />',
        '      <path class="byrne-plate-line byrne-stroke-black byrne-dotted" d="M 590 190 L 617 190 L 644 190" />',
        _txt(568, 268, "Parallels · Straightedge & Compass", "byrne-caption"),
    ]
    return _wrap_svg(
        "preliminaries",
        "Oliver Byrne (1847) Preliminaries — Ocular Manifesto, Definitions & Postulates",
        680,
        300,
        lines,
    )


def _build_v_defs() -> str:
    lines = [
        _txt(340, 38, "BOOK V · DEFINITION V — EUDOXIAN PROPORTION (p. 154)", "byrne-heading"),
        # Row 1: Proportion
        _tok_circle(196, 86, "red"),
        _txt(224, 93, ":"),
        _tok_square(254, 86, "yellow"),
        _txt(296, 93, "∷"),
        _tok_diamond(338, 86, "blue"),
        _txt(366, 93, ":"),
        _tok_shield(396, 86, "black"),
        _txt(465, 91, "(same ratio)", "byrne-caption", "start"),
        # Row 2: Fractional identity
        _tok_circle(276, 134, "red", r=9.5),
        '      <line class="byrne-frac-bar" x1="258" y1="152" x2="294" y2="152" />',
        _tok_square(276, 171, "yellow", s=17.5),
        _txt(322, 159, "="),
        _tok_diamond(368, 134, "blue", r=10.5),
        '      <line class="byrne-frac-bar" x1="350" y1="152" x2="386" y2="152" />',
        _tok_shield(368, 171, "black", s=9.8),
        '      <line class="byrne-rule" x1="88" y1="202" x2="592" y2="202" />',
        # Row 3: Equimultiple test
        _txt(94, 244, "If  M", "byrne-mult", "start"),
        _tok_circle(154, 238, "red"),
        _txt(214, 244, "⊏ , = , ⊐"),
        _txt(266, 244, "m", "byrne-mult"),
        _tok_square(294, 238, "yellow"),
        _txt(344, 244, "⟹"),
        _txt(386, 244, "M", "byrne-mult"),
        _tok_diamond(414, 238, "blue"),
        _txt(474, 244, "⊏ , = , ⊐"),
        _txt(526, 244, "m", "byrne-mult"),
        _tok_shield(554, 238, "black"),
        _txt(340, 282, "Universal for all integer equimultiples M, m ∈ ℕ⁺", "byrne-caption"),
    ]
    return _wrap_svg(
        "v_defs",
        "Book V, Definition V — Colored Magnitude Tokens & Equimultiple Criterion",
        680,
        304,
        lines,
    )


def _build_v11() -> str:
    lines = [
        _txt(340, 38, "BOOK V · PROPOSITION XI — TRANSITIVITY OF RATIOS (p. 175)", "byrne-heading"),
        # Row 1: Given two proportions sharing red circle : yellow shield
        _txt(84, 94, "Let", "byrne-mult"),
        _tok_diamond(122, 88, "blue"),
        _txt(146, 94, ":"),
        _tok_square(172, 88, "blue"),
        _txt(204, 94, "="),
        _tok_circle(236, 88, "red"),
        _txt(260, 94, ":"),
        _tok_shield(286, 88, "yellow"),
        _txt(338, 94, "and", "byrne-caption"),
        _tok_circle(388, 88, "red"),
        _txt(412, 94, ":"),
        _tok_shield(438, 88, "yellow"),
        _txt(470, 94, "="),
        _tok_tri(502, 88, "black"),
        _txt(526, 94, ":"),
        _tok_circle(552, 88, "black", r=8.5),
        '      <line class="byrne-rule" x1="88" y1="126" x2="592" y2="126" />',
        # Row 2: Equimultiple bridge
        _txt(106, 170, "M", "byrne-mult"),
        _tok_diamond(132, 164, "blue"),
        _txt(182, 170, "⊏,=,⊐"),
        _txt(224, 170, "m", "byrne-mult"),
        _tok_square(248, 164, "blue"),
        _txt(288, 170, "⟺"),
        _txt(324, 170, "M", "byrne-mult"),
        _tok_circle(350, 164, "red"),
        _txt(400, 170, "⊏,=,⊐"),
        _txt(442, 170, "m", "byrne-mult"),
        _tok_shield(468, 164, "yellow"),
        _txt(508, 170, "⟺"),
        _txt(544, 170, "M", "byrne-mult"),
        _tok_tri(570, 164, "black"),
        '      <line class="byrne-rule" x1="88" y1="200" x2="592" y2="200" />',
        # Row 3: Conclusion
        _txt(214, 248, "∴"),
        _tok_diamond(256, 242, "blue"),
        _txt(284, 248, ":"),
        _tok_square(314, 242, "blue"),
        _txt(352, 248, "="),
        _tok_tri(390, 242, "black"),
        _txt(418, 248, ":"),
        _tok_circle(446, 242, "black", r=8.5),
        _txt(340, 282, "Ratios that are the same to the same ratio are the same to each other", "byrne-caption"),
    ]
    return _wrap_svg(
        "v11",
        "Book V, Prop. XI — Transitivity of Ratios (Pickering p. 175)",
        680,
        300,
        lines,
    )


def _build_v16() -> str:
    lines = [
        _txt(340, 38, "BOOK V · PROPOSITION XVI — ALTERNANDO (p. 181)", "byrne-heading"),
        # Row 1: Given
        _txt(166, 94, "Let", "byrne-mult"),
        _tok_shield(212, 88, "red"),
        _txt(242, 94, ":"),
        _tok_shield(272, 88, "black", outline=True),
        _txt(314, 94, "∷"),
        _tok_square(356, 88, "yellow"),
        _txt(386, 94, ":"),
        _tok_diamond(416, 88, "blue"),
        '      <line class="byrne-rule" x1="100" y1="126" x2="580" y2="126" />',
        # Row 2: Equimultiple step (V.15 + V.14)
        _txt(144, 170, "M", "byrne-mult"),
        _tok_shield(174, 164, "red"),
        _txt(204, 170, ":"),
        _txt(230, 170, "M", "byrne-mult"),
        _tok_shield(260, 164, "black", outline=True),
        _txt(304, 170, "∷"),
        _txt(344, 170, "m", "byrne-mult"),
        _tok_square(374, 164, "yellow"),
        _txt(404, 170, ":"),
        _txt(430, 170, "m", "byrne-mult"),
        _tok_diamond(460, 164, "blue"),
        _txt(530, 168, "(V.15, V.14)", "byrne-caption"),
        '      <line class="byrne-rule" x1="100" y1="200" x2="580" y2="200" />',
        # Row 3: Alternate conclusion
        _txt(172, 248, "∴"),
        _tok_shield(212, 242, "red"),
        _txt(242, 248, ":"),
        _tok_square(272, 242, "yellow"),
        _txt(314, 248, "∷"),
        _tok_shield(356, 242, "black", outline=True),
        _txt(386, 248, ":"),
        _tok_diamond(416, 242, "blue"),
        _txt(340, 282, "Interchanging middle terms preserves Eudoxian proportion", "byrne-caption"),
    ]
    return _wrap_svg(
        "v16",
        "Book V, Prop. XVI — Alternando (Pickering p. 181)",
        680,
        300,
        lines,
    )


def _build_v18() -> str:
    lines = [
        _txt(340, 38, "BOOK V · PROPOSITION XVIII — COMPONENDO (p. 185)", "byrne-heading"),
        # Row 1: Given
        _txt(166, 94, "Let", "byrne-mult"),
        _tok_shield(212, 88, "red"),
        _txt(242, 94, ":"),
        _tok_shield(272, 88, "black", outline=True),
        _txt(314, 94, "∷"),
        _tok_square(356, 88, "yellow"),
        _txt(386, 94, ":"),
        _tok_diamond(416, 88, "blue"),
        '      <line class="byrne-rule" x1="90" y1="126" x2="590" y2="126" />',
        # Row 2: Reductio via fourth proportional black circle = blue diamond
        _txt(176, 170, "Separando (V.17) + V.9  ⟹", "byrne-caption"),
        _tok_circle(316, 164, "black"),
        _txt(350, 170, "="),
        _tok_diamond(384, 164, "blue"),
        '      <line class="byrne-rule" x1="90" y1="200" x2="590" y2="200" />',
        # Row 3: Composed proportion
        _txt(112, 248, "∴"),
        _tok_shield(150, 242, "red"),
        _txt(180, 248, "+"),
        _tok_shield(210, 242, "black", outline=True),
        _txt(242, 248, ":"),
        _tok_shield(274, 242, "black", outline=True),
        _txt(318, 248, "∷"),
        _tok_square(362, 242, "yellow"),
        _txt(392, 248, "+"),
        _tok_diamond(422, 242, "blue"),
        _txt(454, 248, ":"),
        _tok_diamond(486, 242, "blue"),
        _txt(340, 282, "Magnitudes proportional separately remain proportional jointly", "byrne-caption"),
    ]
    return _wrap_svg(
        "v18",
        "Book V, Prop. XVIII — Componendo (Pickering p. 185)",
        680,
        300,
        lines,
    )


def _build_v22() -> str:
    lines = [
        _txt(340, 38, "BOOK V · PROPOSITION XXII — EX AEQUALI (pp. 193–194)", "byrne-heading"),
        # Row 1: Two ordered triples
        _txt(132, 86, "1st triple:", "byrne-caption"),
        _tok_shield(216, 81, "red"),
        _txt(246, 86, ","),
        _tok_diamond(276, 81, "blue"),
        _txt(306, 86, ","),
        _tok_square(336, 81, "yellow"),
        _txt(412, 86, "2nd triple:", "byrne-caption"),
        _tok_diamond(488, 81, "red"),
        _txt(516, 86, ","),
        _tok_crescent(544, 81, "blue"),
        _txt(572, 86, ","),
        _tok_circle(600, 81, "yellow"),
        # Row 2: Pairwise proportions
        _tok_shield(118, 152, "red"),
        _txt(144, 158, ":"),
        _tok_diamond(170, 152, "blue"),
        _txt(202, 158, "∷"),
        _tok_diamond(234, 152, "red"),
        _txt(260, 158, ":"),
        _tok_crescent(286, 152, "blue"),
        _txt(338, 158, "and", "byrne-caption"),
        _tok_diamond(388, 152, "blue"),
        _txt(414, 158, ":"),
        _tok_square(440, 152, "yellow"),
        _txt(472, 158, "∷"),
        _tok_crescent(504, 152, "blue"),
        _txt(530, 158, ":"),
        _tok_circle(556, 152, "yellow"),
        '      <line class="byrne-rule" x1="88" y1="194" x2="592" y2="194" />',
        # Row 3: Ex aequali conclusion
        _txt(172, 246, "∴"),
        _tok_shield(214, 240, "red"),
        _txt(244, 246, ":"),
        _tok_square(274, 240, "yellow"),
        _txt(316, 246, "∷"),
        _tok_diamond(358, 240, "red"),
        _txt(388, 246, ":"),
        _tok_circle(418, 240, "yellow"),
        _txt(495, 245, "(ex æquali)", "byrne-caption", "start"),
        _txt(340, 284, "Elimination of middle magnitudes across equimultiple chains", "byrne-caption"),
    ]
    return _wrap_svg(
        "v22",
        "Book V, Prop. XXII — Ex Aequali (Pickering pp. 193–194)",
        680,
        304,
        lines,
    )


def _build_rosetta() -> str:
    lines = [
        '      <line class="byrne-rule" x1="228" y1="26" x2="228" y2="278" />',
        '      <line class="byrne-rule" x1="454" y1="26" x2="454" y2="278" />',
        # Column 1: Heath Alphabetic
        _txt(116, 42, "1. HEATH (1908)", "byrne-heading"),
        _txt(116, 70, "Pass-by-Reference", "byrne-caption"),
        '      <polygon class="byrne-fill-none byrne-stroke-black" points="72,170 160,170 104,118" stroke-width="2.0" />',
        _txt(102, 112, "A", "byrne-caption"),
        _txt(62, 176, "B", "byrne-caption"),
        _txt(170, 176, "C", "byrne-caption"),
        _txt(116, 214, "□BDEC = □ABFG + □ACKH", "byrne-caption"),
        _txt(116, 242, "64 vertex pointers", "byrne-mult"),
        # Column 2: Byrne 1847
        _txt(341, 42, "2. BYRNE (1847)", "byrne-heading"),
        _txt(341, 70, "Pass-by-Value Registers", "byrne-caption"),
        '      <rect class="byrne-fill-yellow byrne-stroke-yellow" x="256" y="114" width="30" height="44" />',
        _txt(300, 143, "+"),
        '      <rect class="byrne-fill-blue byrne-stroke-blue" x="314" y="114" width="22" height="44" />',
        _txt(350, 143, "="),
        _tok_square(378, 136, "black", s=26),
        _txt(404, 143, "+"),
        _tok_square(430, 136, "red", s=20),
        _txt(341, 214, "Self-naming area literals", "byrne-caption"),
        _txt(341, 242, "0 vertex pointers", "byrne-mult"),
        # Column 3: GEOMETOR Symbolic DAG
        _txt(566, 42, "3. GEOMETOR DAG", "byrne-heading"),
        _txt(566, 70, "Exact SymPy Algebra", "byrne-caption"),
        '      <circle class="byrne-fill-red byrne-stroke-red" cx="516" cy="122" r="9" />',
        '      <circle class="byrne-fill-blue byrne-stroke-blue" cx="616" cy="122" r="9" />',
        '      <circle class="byrne-fill-yellow byrne-stroke-yellow" cx="566" cy="168" r="10" />',
        '      <line class="byrne-stroke-black" x1="523" y1="129" x2="558" y2="161" stroke-width="2.0" />',
        '      <line class="byrne-stroke-black" x1="609" y1="129" x2="574" y2="161" stroke-width="2.0" />',
        _txt(566, 214, "Q(B,C) = Q(A,B) + Q(A,C)", "byrne-caption"),
        _txt(566, 242, "0 sp.Float atoms", "byrne-mult"),
    ]
    return _wrap_svg(
        "rosetta",
        "3-Way Rosetta Synthesis — Heath (1908) · Byrne (1847) · GEOMETOR Symbolic DAG",
        680,
        296,
        lines,
    )


_BUILDERS: dict[str, Callable[[], str]] = {
    "preliminaries": _build_preliminaries,
    "v_defs": _build_v_defs,
    "v11": _build_v11,
    "v16": _build_v16,
    "v18": _build_v18,
    "v22": _build_v22,
    "rosetta": _build_rosetta,
}

TABLEAU_IDS: tuple[str, ...] = tuple(_BUILDERS.keys())


def render_tableau_svg(tableau_id: str) -> str:
    """Render one of the 7 Chiswick Press typographic/synthesis SVG tableaux."""
    if tableau_id not in _BUILDERS:
        valid = ", ".join(TABLEAU_IDS)
        raise KeyError(f"Unknown tableau {tableau_id!r}. Valid IDs: {valid}")
    return _BUILDERS[tableau_id]()


def export_all_tableaux(output_dir: str | Path) -> list[Path]:
    """Write all 7 Chiswick Press typographic/synthesis SVG tableaux into ``output_dir``."""
    out_root = Path(output_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for tid in TABLEAU_IDS:
        target = out_root / f"{tid}.svg"
        target.write_text(render_tableau_svg(tid), encoding="utf-8")
        written.append(target.resolve())
    return written
