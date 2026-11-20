"""Authentic 1847 Chiswick Press four-color palette and stroke grammar for Oliver Byrne's Euclid.

Calibrated directly against the 1847 William Pickering / Charles Whittingham (Chiswick Press)
woodblock color plates (Internet Archive ``firstsixbooksofe00eucl``), with theme-adaptive
CSS custom properties so all four primary inks—**Red**, **Blue**, **Yellow**, and **Black**—remain
legible on both warm rag-paper light themes and modern dark themes.
"""

from __future__ import annotations

from dataclasses import dataclass

__all__ = [
    "BYRNE_COLORS",
    "BYRNE_STROKE_STYLES",
    "VALID_COLORS",
    "VALID_STROKES",
    "ByrneColorSpec",
    "byrne_css_variables",
    "get_color_spec",
    "stroke_dasharray",
]


@dataclass(frozen=True)
class ByrneColorSpec:
    """Color specification for one of Oliver Byrne's four 1847 woodblock inks.

    Stores canonical token ``name``, human-readable ``label``, light/dark stroke
    and fill hex values (``light_hex``, ``dark_hex``, ``light_fill_hex``,
    ``dark_fill_hex``), CSS custom property tokens (``css_var``, ``css_fill_var``),
    and the 1847 Chiswick Press ``historical_pigment`` note.
    """

    name: str
    label: str
    light_hex: str
    dark_hex: str
    light_fill_hex: str
    dark_fill_hex: str
    css_var: str
    css_fill_var: str
    historical_pigment: str


BYRNE_COLORS: dict[str, ByrneColorSpec] = {
    "red": ByrneColorSpec(
        name="red",
        label="Vermilion Red",
        light_hex="#d92b2b",
        dark_hex="#f04848",
        light_fill_hex="#d92b2b",
        dark_fill_hex="#d93838",
        css_var="var(--byrne-red)",
        css_fill_var="var(--byrne-fill-red)",
        historical_pigment="Chiswick Press vermilion/scarlet relief woodblock ink",
    ),
    "blue": ByrneColorSpec(
        name="blue",
        label="Prussian Blue",
        light_hex="#1c6ea4",
        dark_hex="#4ba3e3",
        light_fill_hex="#1c6ea4",
        dark_fill_hex="#2574ab",
        css_var="var(--byrne-blue)",
        css_fill_var="var(--byrne-fill-blue)",
        historical_pigment="Chiswick Press deep Prussian/slate blue relief woodblock ink",
    ),
    "yellow": ByrneColorSpec(
        name="yellow",
        label="Ochre Gamboge Yellow",
        light_hex="#e6b800",
        dark_hex="#f5ca24",
        light_fill_hex="#e6b800",
        dark_fill_hex="#dfb208",
        css_var="var(--byrne-yellow)",
        css_fill_var="var(--byrne-fill-yellow)",
        historical_pigment="Chiswick Press warm chrome-ochre / gamboge yellow woodblock ink",
    ),
    "black": ByrneColorSpec(
        name="black",
        label="Chiswick Lampblack Ink",
        light_hex="#1a1a1a",
        dark_hex="#e8e6df",
        light_fill_hex="#1a1a1a",
        dark_fill_hex="#363945",
        css_var="var(--byrne-black)",
        css_fill_var="var(--byrne-fill-black)",
        historical_pigment="Charles Whittingham Caslon letterpress lampblack ink",
    ),
}

BYRNE_STROKE_STYLES: dict[str, str] = {
    "solid": "",
    "dashed": "7 4.2",
    "dotted": "2.4 3.6",
}

VALID_COLORS: frozenset[str] = frozenset(BYRNE_COLORS.keys())
VALID_STROKES: frozenset[str] = frozenset((*BYRNE_STROKE_STYLES.keys(), "solid-dotted"))


def get_color_spec(color: str) -> ByrneColorSpec:
    """Return the :class:`ByrneColorSpec` for ``color`` (case-insensitive).

    Args:
        color: Color identifier (``"red"``, ``"blue"``, ``"yellow"``, ``"black"``, or ``"ink"``).

    Returns:
        Matching :class:`ByrneColorSpec`.

    Raises:
        ValueError: If ``color`` is not one of Byrne's four canonical colors.
    """
    key = color.strip().lower()
    if key == "ink":
        key = "black"
    if key not in BYRNE_COLORS:
        raise ValueError(
            f"Unknown Byrne color {color!r}; expected one of {sorted(BYRNE_COLORS)}"
        )
    return BYRNE_COLORS[key]


def stroke_dasharray(style: str) -> str:
    """Return the SVG ``stroke-dasharray`` value for a Byrne line style."""
    key = style.strip().lower()
    if key not in BYRNE_STROKE_STYLES:
        return ""
    return BYRNE_STROKE_STYLES[key]


def byrne_css_variables() -> str:
    """Return CSS custom property declarations for standalone and inline Byrne SVGs."""
    return (
        "  .euclid-graphic, :root {\n"
        "    --geom-fg: #1a1a1a;\n"
        "    --geom-bg: #faf7f0;\n"
        "    --geom-point-stroke: #faf7f0;\n"
        "    --geom-poly-fill: #1a1a1a;\n"
        "    --geom-accent: #e6b800;\n"
        "    --geom-assert: #1c6ea4;\n"
        "    --byrne-paper: #faf7f0;\n"
        "    --byrne-red: #d92b2b;\n"
        "    --byrne-blue: #1c6ea4;\n"
        "    --byrne-yellow: #e6b800;\n"
        "    --byrne-black: #1a1a1a;\n"
        "    --byrne-fill-red: #d92b2b;\n"
        "    --byrne-fill-blue: #1c6ea4;\n"
        "    --byrne-fill-yellow: #e6b800;\n"
        "    --byrne-fill-black: #1a1a1a;\n"
        "    --byrne-halo: rgba(250, 247, 240, 0.92);\n"
        "  }\n"
        "  html[data-theme=\"dark\"] .euclid-graphic,\n"
        "  body[data-theme=\"dark\"] .euclid-graphic {\n"
        "    --geom-fg: #e8e6df;\n"
        "    --geom-bg: #16161a;\n"
        "    --geom-point-stroke: #16161a;\n"
        "    --geom-poly-fill: #e8e6df;\n"
        "    --geom-accent: #f5ca24;\n"
        "    --geom-assert: #4ba3e3;\n"
        "    --byrne-paper: #16161a;\n"
        "    --byrne-red: #f04848;\n"
        "    --byrne-blue: #4ba3e3;\n"
        "    --byrne-yellow: #f5ca24;\n"
        "    --byrne-black: #e8e6df;\n"
        "    --byrne-fill-red: #d93838;\n"
        "    --byrne-fill-blue: #2574ab;\n"
        "    --byrne-fill-yellow: #dfb208;\n"
        "    --byrne-fill-black: #363945;\n"
        "    --byrne-halo: rgba(22, 22, 26, 0.92);\n"
        "  }\n"
        "  @media (prefers-color-scheme: dark) {\n"
        "    .euclid-graphic, :root {\n"
        "      --geom-fg: #e8e6df;\n"
        "      --geom-bg: #16161a;\n"
        "      --geom-point-stroke: #16161a;\n"
        "      --geom-poly-fill: #e8e6df;\n"
        "      --geom-accent: #f5ca24;\n"
        "      --geom-assert: #4ba3e3;\n"
        "      --byrne-paper: #16161a;\n"
        "      --byrne-red: #f04848;\n"
        "      --byrne-blue: #4ba3e3;\n"
        "      --byrne-yellow: #f5ca24;\n"
        "      --byrne-black: #e8e6df;\n"
        "      --byrne-fill-red: #d93838;\n"
        "      --byrne-fill-blue: #2574ab;\n"
        "      --byrne-fill-yellow: #dfb208;\n"
        "      --byrne-fill-black: #363945;\n"
        "      --byrne-halo: rgba(22, 22, 26, 0.92);\n"
        "    }\n"
        "  }"
    )
