"""Interactive ``.euclid-graphic`` SVG renderer for Oliver Byrne (1847) symbolic plates.

Exports crisp pixel-space SVGs directly from :class:`~geometor.byrne.constructions.ByrnePlate`
models while satisfying both:

1. **Standalone SVG fidelity** (embedded ``<style>`` sheet using ``--byrne-*`` Chiswick
   Press colors for light and dark themes), and
2. **PHOTON Publish interactive codex contract** (``svg.euclid-graphic``, ``<defs>``
   ``#geom-tick-1..3``, ``#elements`` / ``#graphics`` / ``#highlights`` / ``#points`` /
   ``#labels``, 3-vertex midpoint ``<path>`` segments, ``.geom-ang-arc`` overlays,
   ``data-ref``, ``data-aliases``, and ``data-byrne-color``).
"""

from __future__ import annotations

import html
import math
from pathlib import Path

from geometor.byrne.constructions import ByrnePlate, build_all_plates
from geometor.byrne.palette import byrne_css_variables, stroke_dasharray

__all__ = [
    "EMBEDDED_SVG_STYLE",
    "PLATE_FOLIO_MAP",
    "SVG_TICK_DEFS",
    "export_all_plates",
    "export_plate_svg",
    "render_plate_svg",
]

PLATE_FOLIO_MAP: dict[str, str] = {
    "i1": "0035",
    "i4": "0038",
    "i5": "0039",
    "i15": "0049",
    "i32": "0067",
    "i46": "0081",
    "i47": "0082",
    "ii4": "0090",
    "ii5": "0092",
    "ii11": "0100",
    "iii20": "0136",
    "iii31": "0149",
    "iii36": "0155",
    "iv4": "0163",
    "iv10": "0169",
    "iv11": "0171",
    "vi30": "0292",
}

EMBEDDED_SVG_STYLE: str = (
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
  .euclid-graphic .byrne-dashed { stroke-dasharray: 7 4.2; }
  .euclid-graphic .byrne-dotted { stroke-dasharray: 2.4 3.6; }
  .euclid-graphic .byrne-plate-line { fill: none; stroke-width: 3.4; stroke-linecap: round; }
  .euclid-graphic .byrne-plate-line.byrne-thin { stroke-width: 2.2; }
  .euclid-graphic .byrne-plate-line.byrne-thick { stroke-width: 4.2; }
  .euclid-graphic .byrne-plate-circle,
  .euclid-graphic .byrne-plate-arc { fill: none; stroke-width: 2.75; stroke-linecap: round; }
  .euclid-graphic .byrne-plate-poly { stroke-linejoin: round; stroke-width: 2.2; }
  .euclid-graphic .byrne-plate-poly.byrne-filled { fill-opacity: 0.9; }
  .euclid-graphic .byrne-plate-poly.byrne-tinted { fill-opacity: 0.22; }
  .euclid-graphic .byrne-plate-wedge { fill-opacity: 0.88; stroke-width: 1.35; stroke-linejoin: round; }
  .euclid-graphic .geom-ang-arc { fill: none; stroke-width: 1.6; opacity: 0.85; }
  .euclid-graphic .geom-point { fill: var(--geom-fg); stroke: var(--geom-point-stroke); stroke-width: 1.2; opacity: 0.45; }
  .euclid-graphic .geom-label {
    fill: var(--geom-fg);
    font-size: 12px;
    font-weight: 600;
    font-family: "EB Garamond", "Georgia", serif;
    paint-order: stroke fill;
    stroke: var(--byrne-halo);
    stroke-width: 3.2px;
  }
"""
)

SVG_TICK_DEFS: str = """  <defs>
    <marker id="geom-tick-1" viewBox="-4 -6 8 12" markerWidth="8" markerHeight="12" orient="auto">
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" />
    </marker>
    <marker id="geom-tick-2" viewBox="-6 -6 12 12" markerWidth="12" markerHeight="12" orient="auto">
      <line x1="-2" y1="-4.5" x2="-2" y2="4.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" />
      <line x1="2" y1="-4.5" x2="2" y2="4.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" />
    </marker>
    <marker id="geom-tick-3" viewBox="-8 -6 16 12" markerWidth="16" markerHeight="12" orient="auto">
      <line x1="-3.5" y1="-4.5" x2="-3.5" y2="4.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" />
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" />
      <line x1="3.5" y1="-4.5" x2="3.5" y2="4.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" />
    </marker>
  </defs>"""

_SVG_TICK_DEFS = SVG_TICK_DEFS


def _fmt(val: float) -> str:
    """Format a pixel coordinate compactly to 2 decimal places."""
    if abs(val - round(val)) < 1e-5:
        return str(round(val))
    return f"{val:.2f}".rstrip("0").rstrip(".")


def _esc_ref(val: str) -> str:
    return (
        val.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def render_plate_svg(
    plate: ByrnePlate,
    *,
    margin: float = 42.0,
    show_labels: bool | None = None,
    folio: str | None = None,
    graphic: str | None = "g1",
    graphic_id: str | None = None,
) -> str:
    """Render a :class:`~geometor.byrne.constructions.ByrnePlate` into a ``.euclid-graphic`` SVG."""
    width, height = plate.canvas_size
    draw_labels = plate.show_labels if show_labels is None else show_labels
    model = plate.model

    # Gather bounding box across all visible points and styled circles
    xs: list[float] = []
    ys: list[float] = []
    visible_pts = [pt for pt in model.points if not model[pt].guide]
    for pt in visible_pts:
        xs.append(float(pt.x.evalf()))
        ys.append(float(pt.y.evalf()))
    for sc in plate.circles:
        cx = float(sc.circle.center.x.evalf())
        cy = float(sc.circle.center.y.evalf())
        r = float(sc.circle.radius.evalf())
        xs.extend((cx - r, cx + r))
        ys.extend((cy - r, cy + r))

    xmin, xmax = (min(xs), max(xs)) if xs else (-1.0, 1.0)
    ymin, ymax = (min(ys), max(ys)) if ys else (-1.0, 1.0)
    span_x = max(xmax - xmin, 1e-4)
    span_y = max(ymax - ymin, 1e-4)

    avail_w = max(width - 2.0 * margin, 100.0)
    avail_h = max(height - 2.0 * margin, 100.0)
    scale = min(avail_w / span_x, avail_h / span_y)

    cx_m = 0.5 * (xmin + xmax)
    cy_m = 0.5 * (ymin + ymax)
    cx_s = 0.5 * width
    cy_s = 0.5 * height

    def to_svg(mx: float, my: float) -> tuple[float, float]:
        return (cx_s + (mx - cx_m) * scale, cy_s - (my - cy_m) * scale)

    def pt_svg(pt) -> tuple[float, float]:
        return to_svg(float(pt.x.evalf()), float(pt.y.evalf()))

    graphics_elems: list[str] = []

    # 1. Planar polygons (drawn underneath circles, wedges, and strokes)
    for spoly in plate.polygons:
        coords = [pt_svg(v) for v in spoly.vertices]
        pts_str = " ".join(f"{_fmt(x)},{_fmt(y)}" for x, y in coords)
        ref_attr = f' data-ref="{_esc_ref(spoly.ref)}"' if spoly.ref else ""
        alias_attr = (
            f' data-aliases="{_esc_ref(" | ".join(spoly.aliases))}"'
            if spoly.aliases
            else ""
        )
        stroke_col = spoly.stroke_color or spoly.color
        stroke_cls = (
            "byrne-stroke-none"
            if stroke_col == "none"
            else f"byrne-stroke-{stroke_col}"
        )

        if spoly.mode == "half" and len(coords) == 4:
            # Byrne's II.4 diagonal half-filled square!
            tri_pts = " ".join(f"{_fmt(x)},{_fmt(y)}" for x, y in (coords[3], coords[2], coords[0]))
            graphics_elems.append(
                f'      <g class="geom-polygon byrne-plate-poly" '
                f'data-byrne-kind="sq" data-byrne-color="{spoly.color}"'
                f"{ref_attr}{alias_attr}>"
                f'<polygon class="byrne-fill-{spoly.color} byrne-stroke-none" points="{tri_pts}" />'
                f'<polygon class="byrne-fill-none {stroke_cls}" points="{pts_str}" />'
                f"<title>{html.escape(spoly.ref)}</title></g>"
            )
        else:
            if spoly.mode == "outline":
                fill_cls = "byrne-fill-none"
                mode_cls = "byrne-outline"
            elif spoly.mode == "tinted":
                fill_cls = f"byrne-fill-{spoly.color}"
                mode_cls = "byrne-tinted"
            else:
                fill_cls = f"byrne-fill-{spoly.color}"
                mode_cls = "byrne-filled"

            kind_tag = "sq" if len(coords) == 4 else ("tri" if len(coords) == 3 else "poly")
            graphics_elems.append(
                f'      <polygon class="geom-polygon byrne-plate-poly {mode_cls} '
                f'{fill_cls} {stroke_cls}" points="{pts_str}" '
                f'data-byrne-kind="{kind_tag}" data-byrne-color="{spoly.color}"'
                f"{ref_attr}{alias_attr}>"
                f"<title>{html.escape(spoly.ref)}</title></polygon>"
            )

    # 2. Circles
    for sc in plate.circles:
        ccx, ccy = pt_svg(sc.circle.center)
        r_px = float(sc.circle.radius.evalf()) * scale
        dash_cls = f" byrne-{sc.stroke}" if sc.stroke in {"dashed", "dotted"} else ""
        dash_val = stroke_dasharray(sc.stroke)
        dash_attr = f' stroke-dasharray="{dash_val}"' if dash_val else ""
        ref_attr = f' data-ref="{_esc_ref(sc.ref)}"' if sc.ref else ""
        graphics_elems.append(
            f'      <circle class="geom-circle byrne-plate-circle '
            f'byrne-stroke-{sc.color}{dash_cls}" '
            f'cx="{_fmt(ccx)}" cy="{_fmt(ccy)}" r="{_fmt(r_px)}"'
            f'{dash_attr} data-byrne-kind="circle" data-byrne-color="{sc.color}"'
            f'{ref_attr} fill="none">'
            f"<title>{html.escape(sc.ref)}</title></circle>"
        )

    # 3. Angle wedges + .geom-ang-arc interactive overlays
    for w in plate.wedges:
        vx, vy = pt_svg(w.vertex)
        a1x, a1y = pt_svg(w.arm1)
        a2x, a2y = pt_svg(w.arm2)

        ang1 = math.atan2(a1y - vy, a1x - vx)
        ang2 = math.atan2(a2y - vy, a2x - vx)
        diff = (ang2 - ang1 + math.pi) % (2.0 * math.pi) - math.pi
        sweep_flag = 1 if diff >= 0 else 0

        # Clamp wedge radius so it never exceeds 42% of either arm length
        len1 = math.hypot(a1x - vx, a1y - vy)
        len2 = math.hypot(a2x - vx, a2y - vy)
        r_w = min(w.radius_px, 0.42 * min(len1, len2))

        sx1, sy1 = vx + r_w * math.cos(ang1), vy + r_w * math.sin(ang1)
        sx2, sy2 = vx + r_w * math.cos(ang2), vy + r_w * math.sin(ang2)

        id1 = model[w.arm1].ID
        iv = model[w.vertex].ID
        id2 = model[w.arm2].ID
        rev_ref = f"< {id2} {iv} {id1} )"
        ref_attr = f' data-ref="{_esc_ref(w.ref)}" data-aliases="{_esc_ref(rev_ref)}"'

        wedge_d = (
            f"M {_fmt(vx)} {_fmt(vy)} L {_fmt(sx1)} {_fmt(sy1)} "
            f"A {_fmt(r_w)} {_fmt(r_w)} 0 0 {sweep_flag} {_fmt(sx2)} {_fmt(sy2)} Z"
        )
        arc_d = (
            f"M {_fmt(sx1)} {_fmt(sy1)} "
            f"A {_fmt(r_w)} {_fmt(r_w)} 0 0 {sweep_flag} {_fmt(sx2)} {_fmt(sy2)}"
        )
        graphics_elems.append(
            f'      <g class="geom-angle" data-byrne-kind="angle" '
            f'data-byrne-color="{w.color}"{ref_attr}>'
            f'<path class="byrne-plate-wedge byrne-fill-{w.color} byrne-stroke-{w.color}" '
            f'd="{wedge_d}" />'
            f'<path class="geom-ang-arc byrne-stroke-{w.color}" d="{arc_d}" fill="none" />'
            f"<title>{html.escape(w.ref)}</title></g>"
        )

    # 4. Segments (3-vertex midpoint <path> for tick-marker compatibility)
    for seg in plate.segments:
        x1, y1 = pt_svg(seg.p1)
        x2, y2 = pt_svg(seg.p2)
        mx, my = 0.5 * (x1 + x2), 0.5 * (y1 + y2)

        weight_cls = (
            " byrne-thick"
            if seg.weight == "thick"
            else (" byrne-thin" if seg.weight == "thin" else "")
        )
        dash_cls = f" byrne-{seg.stroke}" if seg.stroke in {"dashed", "dotted"} else ""
        dash_val = stroke_dasharray(seg.stroke)
        dash_attr = f' stroke-dasharray="{dash_val}"' if dash_val else ""
        ref_attr = f' data-ref="{_esc_ref(seg.ref)}"' if seg.ref else ""
        alias_attr = (
            f' data-aliases="{_esc_ref(" | ".join(seg.aliases))}"'
            if seg.aliases
            else ""
        )
        graphics_elems.append(
            f'      <path class="geom-segment byrne-plate-line '
            f'byrne-stroke-{seg.color}{weight_cls}{dash_cls}" '
            f'd="M {_fmt(x1)} {_fmt(y1)} L {_fmt(mx)} {_fmt(my)} L {_fmt(x2)} {_fmt(y2)}"'
            f'{dash_attr} data-byrne-kind="line" data-byrne-color="{seg.color}"'
            f'{ref_attr}{alias_attr} fill="none">'
            f"<title>{html.escape(seg.ref)}</title></path>"
        )

    # 5. Subtle interactive point anchors & optional editorial labels
    point_elems: list[str] = []
    label_elems: list[str] = []
    for pt in visible_pts:
        pid = model[pt].ID
        if not pid:
            continue
        px, py = pt_svg(pt)
        tip = f"{pid} = ({pt.x}, {pt.y})"
        point_elems.append(
            f'      <circle class="geom-point" cx="{_fmt(px)}" cy="{_fmt(py)}" r="2.6" '
            f'data-ref="{html.escape(pid)}"><title>{html.escape(tip)}</title></circle>'
        )
        if draw_labels:
            label_elems.append(
                f'      <text class="geom-label" x="{_fmt(px + 6)}" y="{_fmt(py - 6)}" '
                f'data-ref="{html.escape(pid)}">{html.escape(pid)}</text>'
            )

    resolved_folio = folio if folio is not None else PLATE_FOLIO_MAP.get(plate.slug, "")
    resolved_gid = graphic_id if graphic_id is not None else plate.slug
    folio_attr = f' data-folio="{html.escape(resolved_folio)}"' if resolved_folio else ""
    graphic_attr = f' data-graphic="{html.escape(graphic)}"' if graphic else ""

    parts = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
            f'viewBox="0 0 {width} {height}" data-graphic-id="{html.escape(resolved_gid)}"'
            f'{folio_attr}{graphic_attr} '
            f'role="img" aria-label="{html.escape(plate.title)}">'
        ),
        f"  <title>{html.escape(plate.title)}</title>",
        SVG_TICK_DEFS,
        "  <style>",
        EMBEDDED_SVG_STYLE,
        "  </style>",
        f'  <rect class="svg-bg" x="0" y="0" width="{width}" height="{height}" rx="6" />',
        '  <g id="elements">',
        '    <g id="graphics">',
        *graphics_elems,
        "    </g>",
        '    <g id="highlights"></g>',
        '    <g id="points">',
        *point_elems,
        "    </g>",
        '    <g id="labels">',
        *label_elems,
        "    </g>",
        "  </g>",
        "</svg>",
        "",
    ]
    return "\n".join(parts)


def export_plate_svg(
    plate: ByrnePlate,
    output_path: str | Path,
    *,
    margin: float = 42.0,
    show_labels: bool | None = None,
    folio: str | None = None,
    graphic: str | None = "g1",
    graphic_id: str | None = None,
) -> Path:
    """Write ``plate`` as an interactive ``.euclid-graphic`` SVG file."""
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    svg_text = render_plate_svg(
        plate,
        margin=margin,
        show_labels=show_labels,
        folio=folio,
        graphic=graphic,
        graphic_id=graphic_id,
    )
    target.write_text(svg_text, encoding="utf-8")
    return target.resolve()


def export_all_plates(output_dir: str | Path) -> list[Path]:
    """Construct and export all 17 showcase Byrne plates into ``output_dir``."""
    out_root = Path(output_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for plate in build_all_plates():
        written.append(export_plate_svg(plate, out_root / f"{plate.slug}.svg"))
    return written
