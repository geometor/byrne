"""Self-contained Sphinx extension for Oliver Byrne's 1847 inline visual glyph roles.

Registers nine inline RST roles without modifying ``photon-platform/publish``:

- ``:byrne-line:`` — Colored/styled straight line segment (supports ``solid``,
  ``dashed``, ``dotted``, ``solid-dotted``, orientations, and ``squared`` / ``^2``).
- ``:byrne-angle:`` — Colored wedge sector (single color or split composite such
  as ``yellow+black`` or ``blue+yellow``).
- ``:byrne-tri:`` — Colored triangle (filled ``red filled`` or 3-side colored
  ``red/blue/black``).
- ``:byrne-sq:`` — Colored square (``filled``, ``outline``, or ``half`` diagonal).
- ``:byrne-rect:`` — Colored rectangle (``filled`` or ``outline``).
- ``:byrne-arc:`` — Colored circular arc.
- ``:byrne-circle:`` — Colored full circle.
- ``:byrne-mag:`` — Book V Eudoxian abstract magnitude symbols (``red circle``,
  ``yellow square``, ``blue diamond``, ``black shield``, ``red pentagon``).
- ``:byrne-op:`` — Byrne's 1847 formal typographic and geometric operators
  (``right-angle``, ``two-right-angles``, ``gt`` / ``⊏``, ``lt`` / ``⊐``,
  ``therefore`` / ``∴``, ``because`` / ``∵``, ``parallel`` / ``∥``,
  ``perp`` / ``⊥``, ``prop`` / ``::``, ``rect-by`` / ``×``).

Every geometric role accepts an optional ``<plate_id:geom_expr>`` target in angle
brackets (for example ``:byrne-sq:`black filled <i47:< A B F G >>```), emitting a
``<span class="byrne-token geom-ref" data-ref="...">`` wrapper around an inline
``<svg class="byrne-glyph">`` micro-glyph so both ``geometor_interactive.js`` and
``byrne_interactive.js`` highlight bidirectionally on hover and click.
"""

from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path
from typing import Any

try:
    from docutils import nodes, utils
except ImportError:  # pragma: no cover
    nodes = None  # type: ignore[assignment]
    utils = None  # type: ignore[assignment]

from geometor.byrne.palette import VALID_COLORS, get_color_spec, stroke_dasharray

__all__ = [
    "BYRNE_ROLE_NAMES",
    "parse_byrne_role_spec",
    "render_byrne_glyph_html",
    "render_byrne_operator_html",
    "setup",
]

BYRNE_ROLE_NAMES: tuple[str, ...] = (
    "byrne-line",
    "byrne-angle",
    "byrne-tri",
    "byrne-sq",
    "byrne-rect",
    "byrne-arc",
    "byrne-circle",
    "byrne-mag",
    "byrne-op",
)

_STATIC_DIR = Path(__file__).resolve().parent / "static"


def _escape_data_ref(value: str) -> str:
    """Escape a ``data-ref`` attribute while encoding ``<`` and ``>`` cleanly."""
    return (
        value.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def parse_byrne_role_spec(raw_text: str) -> tuple[str, str]:
    """Split role body ``spec <target>`` into ``(spec, target)``.

    Correctly handles nested geometric angle brackets inside ``<target>``, such as
    ``black filled <i47:< A B F G >>`` or ``blue <i5:< A B C )>``.

    Args:
        raw_text: Unescaped RST role content string.

    Returns:
        Tuple ``(spec_tokens_str, ref_target)``.
    """
    text = (raw_text or "").strip()
    if not text:
        return "", ""
    match = re.match(r"^([^<>]+?)\s+<(.+)>$", text)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return text, ""


def _parse_color_and_modifiers(
    spec: str,
    *,
    default_color: str = "red",
) -> tuple[str, list[str]]:
    """Extract the primary color expression and remaining modifier tokens."""
    tokens = [tok.strip().lower() for tok in spec.split() if tok.strip()]
    if not tokens:
        return default_color, []

    first = tokens[0]
    if first == "ink":
        first = "black"
    if (
        first in VALID_COLORS
        or "+" in first
        or "/" in first
    ):
        return first, tokens[1:]
    return default_color, tokens


def _svg_line_glyph(color_expr: str, modifiers: list[str]) -> tuple[str, str, str]:
    """Build inline SVG for ``:byrne-line:``."""
    primary_color = color_expr.split("+")[0].split("/")[0]
    spec = get_color_spec(primary_color)

    stroke_style = "solid"
    for candidate in ("solid-dotted", "dashed", "dotted", "solid"):
        if candidate in modifiers:
            stroke_style = candidate
            break

    squared = any(m in {"squared", "sq", "^2", "2"} for m in modifiers)
    if "vertical" in modifiers:
        coords = (7.0, 15.0, 7.0, 1.0)
        width, height = 14, 16
    elif "sloped" in modifiers or "sloped-up" in modifiers:
        coords = (2.0, 14.0, 24.0, 2.0)
        width, height = 26, 16
    elif "sloped-down" in modifiers:
        coords = (2.0, 2.0, 24.0, 14.0)
        width, height = 26, 16
    else:
        coords = (1.5, 8.0, 28.5, 8.0)
        width, height = 30, 16

    x1, y1, x2, y2 = coords
    if stroke_style == "solid-dotted":
        mx, my = 0.55 * (x1 + x2), 0.55 * (y1 + y2)
        inner = (
            f'<line class="byrne-stroke-{spec.name}" x1="{x1}" y1="{y1}" '
            f'x2="{mx:.1f}" y2="{my:.1f}" stroke-width="3.2" stroke-linecap="round" />'
            f'<line class="byrne-stroke-{spec.name} byrne-dotted" x1="{mx:.1f}" y1="{my:.1f}" '
            f'x2="{x2}" y2="{y2}" stroke-width="3.2" stroke-linecap="round" />'
        )
    else:
        dash_cls = f" byrne-{stroke_style}" if stroke_style in {"dashed", "dotted"} else ""
        dash_attr = stroke_dasharray(stroke_style)
        extra_dash = f' stroke-dasharray="{dash_attr}"' if dash_attr else ""
        inner = (
            f'<line class="byrne-stroke-{spec.name}{dash_cls}" '
            f'x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke-width="3.2" stroke-linecap="round"{extra_dash} />'
        )

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" class="byrne-glyph byrne-glyph-line" '
        f'width="{width}" height="{height}" viewBox="0 0 {width} {height}" aria-hidden="true">'
        f"{inner}</svg>"
    )
    if squared:
        svg += '<sup class="byrne-token-sup">2</sup>'
    label = f"{spec.label} {stroke_style} line" + (" squared" if squared else "")
    return svg, spec.name, label


def _svg_angle_glyph(color_expr: str, modifiers: list[str]) -> tuple[str, str, str]:
    """Build inline SVG for ``:byrne-angle:`` (single or split wedge)."""
    outline_only = "outline" in modifiers
    if "+" in color_expr:
        parts = [get_color_spec(c) for c in color_expr.split("+")[:2]]
        c1, c2 = parts[0], parts[1]
        inner = (
            f'<path class="byrne-fill-{c1.name}" d="M 2 14 L 19 3 A 18 18 0 0 1 20.5 8.5 Z" />'
            f'<path class="byrne-fill-{c2.name}" d="M 2 14 L 20.5 8.5 A 18 18 0 0 1 21 14 Z" />'
            '<path class="byrne-stroke-black byrne-fill-none" d="M 21 14 L 2 14 L 19 3" '
            'stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round" />'
        )
        color_attr = f"{c1.name}+{c2.name}"
        label = f"Composite {c1.label} + {c2.label} angle"
    else:
        spec = get_color_spec(color_expr)
        fill_cls = "byrne-fill-none" if outline_only else f"byrne-fill-{spec.name}"
        inner = (
            f'<path class="{fill_cls} byrne-stroke-{spec.name}" '
            'd="M 2.5 14.5 L 18.5 3 A 17 17 0 0 1 21 14.5 Z" '
            'stroke-width="1.4" stroke-linejoin="round" />'
        )
        color_attr = spec.name
        label = f"{spec.label} angle"

    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" class="byrne-glyph byrne-glyph-angle" '
        'width="23" height="16" viewBox="0 0 23 16" aria-hidden="true">'
        f"{inner}</svg>"
    )
    return svg, color_attr, label


def _svg_tri_glyph(color_expr: str, modifiers: list[str]) -> tuple[str, str, str]:
    """Build inline SVG for ``:byrne-tri:`` (filled or 3-side colored outline)."""
    if "/" in color_expr:
        sides = [get_color_spec(c) for c in color_expr.split("/")[:3]]
        while len(sides) < 3:
            sides.append(sides[-1])
        s_left, s_right, s_base = sides[0], sides[1], sides[2]
        inner = (
            f'<line class="byrne-stroke-{s_left.name}" x1="10" y1="2" x2="2" y2="15" '
            'stroke-width="2.4" stroke-linecap="round" />'
            f'<line class="byrne-stroke-{s_right.name}" x1="10" y1="2" x2="18" y2="15" '
            'stroke-width="2.4" stroke-linecap="round" />'
            f'<line class="byrne-stroke-{s_base.name}" x1="2" y1="15" x2="18" y2="15" '
            'stroke-width="2.4" stroke-linecap="round" />'
        )
        color_attr = f"{s_left.name}/{s_right.name}/{s_base.name}"
        label = f"Triangle ({s_left.name}/{s_right.name}/{s_base.name} sides)"
    else:
        spec = get_color_spec(color_expr)
        is_outline = "outline" in modifiers and "filled" not in modifiers
        fill_cls = "byrne-fill-none" if is_outline else f"byrne-fill-{spec.name}"
        inner = (
            f'<polygon class="{fill_cls} byrne-stroke-{spec.name}" '
            'points="10,2 18,15 2,15" stroke-width="1.8" stroke-linejoin="round" />'
        )
        color_attr = spec.name
        label = f"{spec.label} triangle"

    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" class="byrne-glyph byrne-glyph-tri" '
        'width="20" height="17" viewBox="0 0 20 17" aria-hidden="true">'
        f"{inner}</svg>"
    )
    return svg, color_attr, label


def _svg_sq_glyph(color_expr: str, modifiers: list[str]) -> tuple[str, str, str]:
    """Build inline SVG for ``:byrne-sq:`` (filled, outline, or diagonal half-filled)."""
    spec = get_color_spec(color_expr)
    if "half" in modifiers:
        inner = (
            f'<polygon class="byrne-fill-{spec.name}" points="2,2 15,2 2,15" />'
            f'<rect class="byrne-fill-none byrne-stroke-{spec.name}" '
            'x="2" y="2" width="13" height="13" stroke-width="1.8" />'
        )
        mode = "half-filled"
    elif "outline" in modifiers and "filled" not in modifiers:
        inner = (
            f'<rect class="byrne-fill-none byrne-stroke-{spec.name}" '
            'x="2" y="2" width="13" height="13" stroke-width="2.1" />'
        )
        mode = "outlined"
    else:
        inner = (
            f'<rect class="byrne-fill-{spec.name} byrne-stroke-{spec.name}" '
            'x="2" y="2" width="13" height="13" stroke-width="1.5" />'
        )
        mode = "filled"

    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" class="byrne-glyph byrne-glyph-sq" '
        'width="17" height="17" viewBox="0 0 17 17" aria-hidden="true">'
        f"{inner}</svg>"
    )
    return svg, spec.name, f"{spec.label} {mode} square"


def _svg_rect_glyph(color_expr: str, modifiers: list[str]) -> tuple[str, str, str]:
    """Build inline SVG for ``:byrne-rect:``."""
    spec = get_color_spec(color_expr)
    is_outline = "outline" in modifiers and "filled" not in modifiers
    fill_cls = "byrne-fill-none" if is_outline else f"byrne-fill-{spec.name}"
    stroke_w = "2.0" if is_outline else "1.5"
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" class="byrne-glyph byrne-glyph-rect" '
        'width="24" height="16" viewBox="0 0 24 16" aria-hidden="true">'
        f'<rect class="{fill_cls} byrne-stroke-{spec.name}" '
        f'x="2" y="2.5" width="20" height="11" stroke-width="{stroke_w}" /></svg>'
    )
    mode = "outlined" if is_outline else "filled"
    return svg, spec.name, f"{spec.label} {mode} rectangle"


def _svg_arc_glyph(color_expr: str, modifiers: list[str]) -> tuple[str, str, str]:
    """Build inline SVG for ``:byrne-arc:``."""
    spec = get_color_spec(color_expr)
    dash_cls = " byrne-dotted" if "dotted" in modifiers else (" byrne-dashed" if "dashed" in modifiers else "")
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" class="byrne-glyph byrne-glyph-arc" '
        'width="24" height="15" viewBox="0 0 24 15" aria-hidden="true">'
        f'<path class="byrne-fill-none byrne-stroke-{spec.name}{dash_cls}" '
        'd="M 2 12.5 A 13 13 0 0 1 22 12.5" stroke-width="2.6" stroke-linecap="round" /></svg>'
    )
    return svg, spec.name, f"{spec.label} circular arc"


def _svg_circle_glyph(color_expr: str, modifiers: list[str]) -> tuple[str, str, str]:
    """Build inline SVG for ``:byrne-circle:``."""
    spec = get_color_spec(color_expr)
    is_filled = "filled" in modifiers
    fill_cls = f"byrne-fill-{spec.name}" if is_filled else "byrne-fill-none"
    dash_cls = " byrne-dotted" if "dotted" in modifiers else (" byrne-dashed" if "dashed" in modifiers else "")
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" class="byrne-glyph byrne-glyph-circle" '
        'width="18" height="18" viewBox="0 0 18 18" aria-hidden="true">'
        f'<circle class="{fill_cls} byrne-stroke-{spec.name}{dash_cls}" '
        'cx="9" cy="9" r="6.6" stroke-width="2.3" /></svg>'
    )
    return svg, spec.name, f"{spec.label} circle"


def _svg_mag_glyph(color_expr: str, modifiers: list[str]) -> tuple[str, str, str]:
    """Build inline SVG for Book V Eudoxian abstract magnitude tokens (``:byrne-mag:``)."""
    spec = get_color_spec(color_expr)
    shape = modifiers[0] if modifiers else {
        "red": "circle",
        "yellow": "square",
        "blue": "diamond",
        "black": "shield",
    }.get(spec.name, "circle")

    if shape in {"square", "sq"}:
        inner = f'<rect class="byrne-fill-{spec.name}" x="2.5" y="2.5" width="11" height="11" />'
        shape_label = "square"
    elif shape in {"diamond", "lozenge"}:
        inner = f'<polygon class="byrne-fill-{spec.name}" points="8,1.2 14.8,8 8,14.8 1.2,8" />'
        shape_label = "diamond"
    elif shape in {"shield", "crest", "wedge"}:
        inner = (
            f'<path class="byrne-fill-{spec.name}" '
            'd="M 2.5 2 H 13.5 V 8.5 C 13.5 12 8 15 8 15 C 8 15 2.5 12 2.5 8.5 Z" />'
        )
        shape_label = "shield"
    elif shape in {"pentagon", "pent"}:
        inner = (
            f'<polygon class="byrne-fill-{spec.name}" '
            'points="8,1.4 14.5,6.1 12.1,14.2 3.9,14.2 1.5,6.1" />'
        )
        shape_label = "pentagon"
    else:
        inner = f'<circle class="byrne-fill-{spec.name}" cx="8" cy="8" r="6.2" />'
        shape_label = "circle"

    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" class="byrne-glyph byrne-glyph-mag" '
        'width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">'
        f"{inner}</svg>"
    )
    return svg, spec.name, f"Book V {spec.label} {shape_label} magnitude"


def render_byrne_operator_html(op_spec: str) -> str:
    """Render one of Oliver Byrne's 1847 geometric/algebraic operators (``:byrne-op:``).

    Args:
        op_spec: Operator token such as ``"right-angle"``, ``"two-right-angles"``,
            ``"gt"``, ``"lt"``, ``"therefore"``, ``"because"``, ``"parallel"``,
            ``"perp"``, ``"prop"``, or ``"rect-by"``.

    Returns:
        Inline HTML span containing an authentic SVG or typographic symbol.
    """
    key = (op_spec or "").strip().lower()
    if key in {"right-angle", "right", "quadrant", "∟"}:
        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" class="byrne-glyph byrne-glyph-op" '
            'width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">'
            '<path class="byrne-fill-none byrne-stroke-black" '
            'd="M 3 2 V 13.5 H 14.5 M 3 4.5 A 9 9 0 0 1 12 13.5" '
            'stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" /></svg>'
        )
        return (
            '<span class="byrne-op-token" title="One right angle (Byrne 1847 quadrant)" '
            f'aria-label="one right angle">{svg}</span>'
        )
    if key in {"two-right-angles", "2-right-angles", "semicircle"}:
        svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" class="byrne-glyph byrne-glyph-op" '
            'width="24" height="15" viewBox="0 0 24 15" aria-hidden="true">'
            '<path class="byrne-fill-none byrne-stroke-black" '
            'd="M 1.5 13 H 22.5 M 3.5 13 A 8.5 8.5 0 0 1 20.5 13 M 12 13 V 2" '
            'stroke-width="1.65" stroke-linecap="round" /></svg>'
        )
        return (
            '<span class="byrne-op-token" title="Two right angles (Byrne 1847 bisected semicircle)" '
            f'aria-label="two right angles">{svg}</span>'
        )

    symbol_map: dict[str, tuple[str, str]] = {
        "gt": ("⊏", "Greater than (Byrne 1847 ⊏)"),
        "⊏": ("⊏", "Greater than (Byrne 1847 ⊏)"),
        "lt": ("⊐", "Less than (Byrne 1847 ⊐)"),
        "⊐": ("⊐", "Less than (Byrne 1847 ⊐)"),
        "therefore": ("∴", "Therefore (∴)"),
        "∴": ("∴", "Therefore (∴)"),
        "because": ("∵", "Because (∵)"),
        "∵": ("∵", "Because (∵)"),
        "parallel": ("∥", "Parallel to (∥)"),
        "∥": ("∥", "Parallel to (∥)"),
        "||": ("∥", "Parallel to (∥)"),
        "perp": ("⊥", "Perpendicular to (⊥)"),
        "⊥": ("⊥", "Perpendicular to (⊥)"),
        "prop": ("∷", "As / proportional to (∷)"),
        "::": ("∷", "As / proportional to (∷)"),
        "∷": ("∷", "As / proportional to (∷)"),
        "rect-by": ("×", "Rectangle contained by (×)"),
        "×": ("×", "Rectangle contained by (×)"),
    }
    sym, tip = symbol_map.get(key, (op_spec.strip(), f"Byrne operator {op_spec.strip()}"))
    esc_sym = html.escape(sym)
    esc_tip = html.escape(tip, quote=True)
    return f'<span class="byrne-op-token" title="{esc_tip}">{esc_sym}</span>'


def render_byrne_glyph_html(role_name: str, raw_content: str) -> str:
    """Render any ``:byrne-*:`` role specification into an interactive HTML span.

    Args:
        role_name: Canonical role name (e.g. ``"byrne-line"``, ``"byrne-sq"``).
        raw_content: Unescaped role body string, optionally ending with ``<target>``.

    Returns:
        Complete HTML ``<span>`` element containing the inline SVG glyph and metadata.
    """
    short_kind = role_name.removeprefix("byrne-")
    if short_kind == "op":
        spec_only, _ = parse_byrne_role_spec(raw_content)
        return render_byrne_operator_html(spec_only or raw_content)

    spec_text, ref_target = parse_byrne_role_spec(raw_content)
    color_expr, modifiers = _parse_color_and_modifiers(spec_text)

    dispatch = {
        "line": _svg_line_glyph,
        "angle": _svg_angle_glyph,
        "tri": _svg_tri_glyph,
        "sq": _svg_sq_glyph,
        "rect": _svg_rect_glyph,
        "arc": _svg_arc_glyph,
        "circle": _svg_circle_glyph,
        "mag": _svg_mag_glyph,
    }
    builder_fn = dispatch.get(short_kind, _svg_line_glyph)
    svg_html, color_attr, human_label = builder_fn(color_expr, modifiers)

    ref_attr = f' data-ref="{_escape_data_ref(ref_target)}"' if ref_target else ""
    ref_suffix = f" ({ref_target.split(':', 1)[-1].strip()})" if ref_target else ""
    tooltip = html.escape(f"{human_label}{ref_suffix}", quote=True)
    aria = html.escape(human_label, quote=True)
    esc_color = html.escape(color_attr, quote=True)
    esc_kind = html.escape(short_kind, quote=True)

    return (
        f'<span class="byrne-token geom-ref" data-byrne-kind="{esc_kind}" '
        f'data-byrne-color="{esc_color}"{ref_attr} title="{tooltip}" '
        f'role="img" aria-label="{aria}">{svg_html}</span>'
    )


if nodes is not None:
    class byrne_glyph_node(nodes.Inline, nodes.TextElement):
        """Docutils inline AST node for Oliver Byrne visual value-tokens."""
else:  # pragma: no cover
    class byrne_glyph_node:  # type: ignore[no-redef]
        """Fallback placeholder when docutils is absent."""


def _visit_byrne_glyph_html(self: Any, node: nodes.Element) -> None:
    self.body.append(str(node["rendered_html"]))
    raise nodes.SkipNode


def _depart_byrne_glyph_html(self: Any, node: nodes.Element) -> None:
    pass


def _visit_byrne_glyph_text(self: Any, node: nodes.Element) -> None:
    self.add_text(f"[{node.get('alt_label', node.astext())}]")
    raise nodes.SkipNode


def _make_byrne_role(role_name: str):
    """Create a Sphinx role handler bound to ``role_name``."""

    def _role_fn(
        name: str,
        rawtext: str,
        text: str,
        lineno: int,
        inliner: Any,
        options: dict[str, Any] | None = None,
        content: list[str] | None = None,
    ) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        restored = utils.unescape(text, restore_backslashes=True).strip()
        try:
            rendered = render_byrne_glyph_html(role_name, restored)
        except ValueError as exc:
            msg = inliner.reporter.error(
                f"Invalid {role_name} specification {restored!r}: {exc}",
                line=lineno,
            )
            prb = inliner.problematic(rawtext, rawtext, msg)
            return [prb], [msg]

        spec_only, _ = parse_byrne_role_spec(restored)
        alt_label = f"{role_name}:{spec_only or restored}"
        node = byrne_glyph_node(rawtext, alt_label)
        node["rendered_html"] = rendered
        node["alt_label"] = alt_label
        return [node], []

    return _role_fn


def _seed_apparatus_from_pickering(app: Any) -> None:
    """Preload ``resources/pickering_1847/{citations,persons,glossary}.json`` for ``:cite:``/``:person:``/``:term:``."""
    env = getattr(app, "env", None)
    if env is None:
        return
    srcdir = Path(getattr(app, "srcdir", "."))
    pickering_dir = srcdir.parent / "resources" / "pickering_1847"
    if not pickering_dir.is_dir():
        return

    registries: dict[str, dict[str, Any]] = {"cite": {}, "person": {}, "term": {}}
    file_map = {
        "cite": "citations.json",
        "person": "persons.json",
        "term": "glossary.json",
    }
    for kind, fname in file_map.items():
        fpath = pickering_dir / fname
        if fpath.is_file():
            try:
                registries[kind] = json.loads(fpath.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue

    cache = getattr(env, "_photon_apparatus_cache", None)
    if cache is None:
        cache = {}
        env._photon_apparatus_cache = cache
    for book_key in ("coloured_euclid", "pseudocode", "mission", "default"):
        cache[book_key] = registries


def _copy_byrne_static_assets(app: Any, exception: Exception | None) -> None:
    """Copy ``byrne.css`` and ``byrne_interactive.js`` into the built ``_static`` folder."""
    if exception is not None:
        return
    outdir = Path(getattr(app, "outdir", ""))
    if not outdir.is_dir():
        return
    target_static = outdir / "_static"
    target_static.mkdir(parents=True, exist_ok=True)
    for asset_name in ("byrne.css", "byrne_interactive.js"):
        src = _STATIC_DIR / asset_name
        if src.is_file():
            shutil.copy2(src, target_static / asset_name)


def setup(app: Any) -> dict[str, Any]:
    """Register Oliver Byrne inline roles, static stylesheets, and JS handlers in Sphinx."""
    app.add_node(
        byrne_glyph_node,
        html=(_visit_byrne_glyph_html, _depart_byrne_glyph_html),
        text=(_visit_byrne_glyph_text, _depart_byrne_glyph_html),
    )
    for rname in BYRNE_ROLE_NAMES:
        app.add_role(rname, _make_byrne_role(rname))

    app.add_css_file("byrne.css")
    app.add_js_file("byrne_interactive.js")
    app.connect("builder-inited", _seed_apparatus_from_pickering)
    app.connect("build-finished", _copy_byrne_static_assets)

    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
