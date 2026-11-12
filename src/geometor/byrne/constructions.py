"""Exact symbolic ``geometor.model`` constructions for 17 Oliver Byrne (1847) showcase plates.

Every construction executes with :class:`geometor.model.Model` (``auto_intersect=False``,
zero ``float`` or ``sp.Float`` coordinates) over exact SymPy algebraic fields:

- $\\mathbb{Q}$: ``I.4``, ``I.5``, ``I.15``, ``I.32``, ``I.46``, ``I.47``, ``II.4``,
  ``II.5``, ``III.20``, ``III.31``, ``III.36``, ``IV.4``
- $\\mathbb{Q}(\\sqrt{3})$: ``I.1``
- $\\mathbb{Q}(\\phi)$ where $\\phi = \\frac{1 + \\sqrt{5}}{2}$: ``II.11``, ``VI.30``
- $\\mathbb{Q}(\\phi, \\sqrt{10 - 2\\sqrt{5}})$: ``IV.10``, ``IV.11``

Each :class:`ByrnePlate` pairs the populated symbolic :class:`~geometor.model.Model` and
verified algebraic proof identities with authentic 1847 Chiswick Press four-color visual
layers calibrated against the William Pickering scan (Internet Archive ``firstsixbooksofe00eucl``).
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model
from geometor.model.invariants import line_spread, quadrance

PHI: sp.Expr = (sp.Integer(1) + sp.sqrt(5)) / sp.Integer(2)


def spread(v1: spg.Point, p1: spg.Point, v2: spg.Point, p2: spg.Point) -> sp.Expr:
    """Compute exact rational spread between segments (v1, p1) and (v2, p2)."""
    return line_spread((v1, p1), (v2, p2))

__all__ = [
    "PHI",
    "PLATE_REGISTRY",
    "ByrnePlate",
    "StyledAngleWedge",
    "StyledArc",
    "StyledCircle",
    "StyledPolygon",
    "StyledSegment",
    "build_all_plates",
    "build_plate",
    "list_plate_ids",
]


@dataclass(frozen=True)
class StyledSegment:
    """Byrne-styled straight segment joining two exact :class:`sympy.geometry.Point` objects."""

    p1: spg.Point
    p2: spg.Point
    color: str
    stroke: str = "solid"
    weight: str = "normal"
    ref: str = ""
    aliases: tuple[str, ...] = ()


@dataclass(frozen=True)
class StyledCircle:
    """Byrne-styled full circle from an exact :class:`sympy.geometry.Circle`."""

    circle: spg.Circle
    color: str
    stroke: str = "solid"
    ref: str = ""
    aliases: tuple[str, ...] = ()


@dataclass(frozen=True)
class StyledArc:
    """Byrne-styled circular arc centered at ``center`` through ``start`` to ``end`` CCW."""

    center: spg.Point
    start: spg.Point
    end: spg.Point
    color: str
    stroke: str = "solid"
    ref: str = ""


@dataclass(frozen=True)
class StyledPolygon:
    """Byrne-styled planar region (filled, half-filled, tinted, or outlined)."""

    vertices: tuple[spg.Point, ...]
    color: str
    mode: str = "filled"  # "filled" | "tinted" | "outline" | "half"
    stroke_color: str = ""
    ref: str = ""
    aliases: tuple[str, ...] = ()


@dataclass(frozen=True)
class StyledAngleWedge:
    """Byrne-styled woodblock angle sector at ``vertex`` from ray ``arm1`` to ``arm2``."""

    arm1: spg.Point
    vertex: spg.Point
    arm2: spg.Point
    color: str
    radius_px: float = 26.0
    ref: str = ""


@dataclass
class ByrnePlate:
    """Complete symbolic model, verified invariants, and 1847 visual layers for one plate."""

    prop_id: str
    slug: str
    heath_id: str
    g_id: str
    book: int
    title: str
    pickering_page: str
    number_field: str
    model: Model
    polygons: list[StyledPolygon] = field(default_factory=list)
    wedges: list[StyledAngleWedge] = field(default_factory=list)
    circles: list[StyledCircle] = field(default_factory=list)
    arcs: list[StyledArc] = field(default_factory=list)
    segments: list[StyledSegment] = field(default_factory=list)
    proof_checks: dict[str, bool] = field(default_factory=dict)
    canvas_size: tuple[int, int] = (640, 460)
    show_labels: bool = False


def _new_model(name: str) -> Model:
    return Model(name, logger=False, auto_intersect=False)


def _zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def _seg(
    model: Model,
    p1: spg.Point,
    p2: spg.Point,
    color: str,
    stroke: str = "solid",
    *,
    weight: str = "normal",
    by: str = "",
) -> StyledSegment:
    s = model.set_segment(p1, p2, classes=[f"byrne_{color}"], by=by)
    id1, id2 = model[p1].ID, model[p2].ID
    ref = model[s].ID
    rev = f"/ {id2} {id1} /"
    line_f = f"[ {id1} {id2} ]"
    line_r = f"[ {id2} {id1} ]"
    return StyledSegment(
        p1=p1,
        p2=p2,
        color=color,
        stroke=stroke,
        weight=weight,
        ref=ref,
        aliases=(rev, line_f, line_r),
    )


def _poly(
    model: Model,
    pts: list[spg.Point],
    color: str,
    mode: str = "filled",
    *,
    stroke_color: str = "",
    by: str = "",
) -> StyledPolygon:
    poly = model.set_polygon(pts, classes=[f"byrne_{color}"], by=by)
    ids = [model[p].ID for p in pts]
    ref = model[poly].ID
    rev = f"< {' '.join(reversed(ids))} >"
    return StyledPolygon(
        vertices=tuple(pts),
        color=color,
        mode=mode,
        stroke_color=stroke_color or color,
        ref=ref,
        aliases=(rev,),
    )


def _circ(
    model: Model,
    center: spg.Point,
    radius_pt: spg.Point,
    color: str,
    stroke: str = "solid",
    *,
    by: str = "",
) -> tuple[spg.Circle, StyledCircle]:
    c = model.construct_circle(center, radius_pt, classes=[f"byrne_{color}"], by=by)
    ref = model[c].ID
    return c, StyledCircle(circle=c, color=color, stroke=stroke, ref=ref)


def _wedge(
    model: Model,
    arm1: spg.Point,
    vertex: spg.Point,
    arm2: spg.Point,
    color: str,
    radius_px: float = 26.0,
) -> StyledAngleWedge:
    i1, iv, i2 = model[arm1].ID, model[vertex].ID, model[arm2].ID
    ref = f"< {i1} {iv} {i2} )"
    return StyledAngleWedge(
        arm1=arm1,
        vertex=vertex,
        arm2=arm2,
        color=color,
        radius_px=radius_px,
        ref=ref,
    )


# ---------------------------------------------------------------------------
# Book I Showcase Constructions
# ---------------------------------------------------------------------------


def build_i1() -> ByrnePlate:
    """Book I, Prop. 1 (p. 1): Equilateral triangle constructed on a given finite line."""
    m = _new_model("I.1")
    a = m.set_point(0, 0, ID="A", classes=["given"])
    b = m.set_point(1, 0, ID="B", classes=["given"])
    c_ab, sc_ab = _circ(m, a, b, "blue", by="I.post.3")
    c_ba, sc_ba = _circ(m, b, a, "red", by="I.post.3")
    c = m.intersect(c_ab, c_ba, side_of=(a, b, 1), ID="C", by="I.1")

    segs = [
        _seg(m, a, b, "black", weight="thick", by="given"),
        _seg(m, a, c, "yellow", weight="thick", by="I.post.1"),
        _seg(m, b, c, "red", weight="thick", by="I.post.1"),
    ]
    p_abc = _poly(m, [a, b, c], "yellow", mode="outline", stroke_color="none", by="I.1")

    checks = {
        "AC_eq_AB": _zero(quadrance(a, c) - quadrance(a, b)),
        "BC_eq_AB": _zero(quadrance(b, c) - quadrance(a, b)),
        "equiangular_spread_3_4": _zero(spread(a, b, a, c) - sp.Rational(3, 4)),
    }
    return ByrnePlate(
        prop_id="I.1",
        slug="i1",
        heath_id="elem.1.1",
        g_id="G.84",
        book=1,
        title="Book I, Prop. I — Equilateral Triangle on a Given Segment",
        pickering_page="p. 1",
        number_field="Q(sqrt(3))",
        model=m,
        polygons=[p_abc],
        circles=[sc_ab, sc_ba],
        segments=segs,
        proof_checks=checks,
        canvas_size=(640, 430),
    )


def build_i4() -> ByrnePlate:
    """Book I, Prop. 4 (p. 4): Side-Angle-Side triangle congruence."""
    m = _new_model("I.4")
    a = m.set_point(sp.Rational(4, 5), sp.Rational(11, 5), ID="A", classes=["given"])
    b = m.set_point(0, 0, ID="B", classes=["given"])
    c = m.set_point(sp.Rational(13, 5), 0, ID="C", classes=["given"])

    shift = sp.Rational(18, 5)
    d = m.set_point(a.x + shift, a.y, ID="D", classes=["given"])
    e = m.set_point(b.x + shift, b.y, ID="E", classes=["given"])
    f = m.set_point(c.x + shift, c.y, ID="F", classes=["given"])

    polys = [
        _poly(m, [a, b, c], "yellow", mode="outline", stroke_color="none"),
        _poly(m, [d, e, f], "yellow", mode="outline", stroke_color="none"),
    ]
    wedges = [
        _wedge(m, b, a, c, "yellow", 28),
        _wedge(m, c, b, a, "blue", 28),
        _wedge(m, a, c, b, "red", 28),
        _wedge(m, e, d, f, "yellow", 28),
        _wedge(m, f, e, d, "blue", 28),
        _wedge(m, d, f, e, "red", 28),
    ]
    segs = [
        _seg(m, a, b, "red", weight="thick"),
        _seg(m, a, c, "blue", weight="thick"),
        _seg(m, b, c, "black", weight="thick"),
        _seg(m, d, e, "red", weight="thick"),
        _seg(m, d, f, "blue", weight="thick"),
        _seg(m, e, f, "black", weight="thick"),
    ]
    checks = {
        "AB_eq_DE": _zero(quadrance(a, b) - quadrance(d, e)),
        "AC_eq_DF": _zero(quadrance(a, c) - quadrance(d, f)),
        "BC_eq_EF": _zero(quadrance(b, c) - quadrance(e, f)),
        "apex_spreads_equal": _zero(spread(a, b, a, c) - spread(d, e, d, f)),
    }
    return ByrnePlate(
        prop_id="I.4",
        slug="i4",
        heath_id="elem.1.4",
        g_id="G.90",
        book=1,
        title="Book I, Prop. IV — Side-Angle-Side Congruence",
        pickering_page="p. 4",
        number_field="Q",
        model=m,
        polygons=polys,
        wedges=wedges,
        segments=segs,
        proof_checks=checks,
        canvas_size=(680, 360),
    )


def build_i5() -> ByrnePlate:
    """Book I, Prop. 5 (p. 5): Pons Asinorum — base angles of an isosceles triangle."""
    m = _new_model("I.5")
    a = m.set_point(0, sp.Rational(12, 5), ID="A", classes=["given"])
    b = m.set_point(-1, 0, ID="B", classes=["given"])
    c = m.set_point(1, 0, ID="C", classes=["given"])

    m.construct_line(a, b, guide=True)
    l_ac = m.construct_line(a, c, guide=True)
    f = m.set_point(sp.Rational(-9, 5), sp.Rational(-96, 50), ID="F")
    c_af = m.construct_circle(a, f, guide=True)
    g = m.intersect(l_ac, c_af, beyond=(a, c), ID="G", by="I.3")
    d = m.set_point(sp.Rational(-11, 5), sp.Rational(-144, 50), ID="D")
    e = m.set_point(sp.Rational(11, 5), sp.Rational(-144, 50), ID="E")

    polys = [_poly(m, [a, b, c], "red", mode="outline", stroke_color="none")]
    wedges = [
        _wedge(m, b, a, c, "black", 28),
        _wedge(m, c, b, a, "blue", 25),
        _wedge(m, a, c, b, "blue", 25),
        _wedge(m, f, b, c, "yellow", 24),
        _wedge(m, b, c, g, "yellow", 24),
        _wedge(m, c, f, a, "red", 24),
        _wedge(m, a, g, b, "red", 24),
    ]
    segs = [
        _seg(m, a, b, "red", weight="thick"),
        _seg(m, a, c, "red", weight="thick"),
        _seg(m, b, c, "black", weight="thick"),
        _seg(m, b, f, "yellow", weight="thick"),
        _seg(m, c, g, "yellow", weight="thick"),
        _seg(m, f, d, "yellow", stroke="dotted", weight="thin"),
        _seg(m, g, e, "yellow", stroke="dotted", weight="thin"),
        _seg(m, f, c, "blue", weight="normal"),
        _seg(m, g, b, "blue", weight="normal"),
    ]
    checks = {
        "isosceles_AB_eq_AC": _zero(quadrance(a, b) - quadrance(a, c)),
        "AF_eq_AG": _zero(quadrance(a, f) - quadrance(a, g)),
        "FC_eq_GB": _zero(quadrance(f, c) - quadrance(g, b)),
        "base_spreads_equal": _zero(spread(b, a, b, c) - spread(c, a, c, b)),
    }
    return ByrnePlate(
        prop_id="I.5",
        slug="i5",
        heath_id="elem.1.5",
        g_id="G.91",
        book=1,
        title="Book I, Prop. V — Pons Asinorum (Isosceles Base Angles)",
        pickering_page="p. 5",
        number_field="Q",
        model=m,
        polygons=polys,
        wedges=wedges,
        segments=segs,
        proof_checks=checks,
        canvas_size=(600, 520),
    )


def build_i15() -> ByrnePlate:
    """Book I, Prop. 15 (p. 15): Vertical angles of two intersecting straight lines."""
    m = _new_model("I.15")
    a = m.set_point(-3, sp.Rational(-6, 5), ID="A", classes=["given"])
    b = m.set_point(3, sp.Rational(6, 5), ID="B", classes=["given"])
    c = m.set_point(sp.Rational(-11, 5), sp.Rational(9, 5), ID="C", classes=["given"])
    d = m.set_point(sp.Rational(11, 5), sp.Rational(-9, 5), ID="D", classes=["given"])

    l_ab = m.construct_line(a, b, guide=True)
    l_cd = m.construct_line(c, d, guide=True)
    e = m.intersect(l_ab, l_cd, ID="E", by="I.15")

    wedges = [
        _wedge(m, b, e, c, "red", 42),
        _wedge(m, c, e, a, "yellow", 42),
        _wedge(m, a, e, d, "blue", 42),
        _wedge(m, d, e, b, "black", 42),
    ]
    segs = [
        _seg(m, a, b, "black", weight="thick"),
        _seg(m, c, d, "red", weight="thick"),
    ]
    checks = {
        "vertical_spreads_top_bottom": _zero(spread(e, b, e, c) - spread(e, a, e, d)),
        "vertical_spreads_left_right": _zero(spread(e, c, e, a) - spread(e, d, e, b)),
    }
    return ByrnePlate(
        prop_id="I.15",
        slug="i15",
        heath_id="elem.1.15",
        g_id="G.104",
        book=1,
        title="Book I, Prop. XV — Equality of Vertical Angles",
        pickering_page="p. 15",
        number_field="Q",
        model=m,
        wedges=wedges,
        segments=segs,
        proof_checks=checks,
        canvas_size=(600, 380),
    )


def build_i32() -> ByrnePlate:
    """Book I, Prop. 32 (p. 33): Exterior angle & interior angle sum of a triangle."""
    m = _new_model("I.32")
    b = m.set_point(0, 0, ID="B", classes=["given"])
    c = m.set_point(sp.Rational(12, 5), 0, ID="C", classes=["given"])
    a = m.set_point(sp.Rational(4, 5), sp.Rational(11, 5), ID="A", classes=["given"])
    d = m.set_point(sp.Rational(21, 5), 0, ID="D")
    e = m.set_point(c.x + a.x - b.x, c.y + a.y - b.y, ID="E")
    f = m.set_point(a.x + sp.Rational(2, 5) * (a.x - b.x), a.y + sp.Rational(2, 5) * (a.y - b.y), ID="F")

    wedges = [
        _wedge(m, c, b, a, "yellow", 28),
        _wedge(m, b, a, c, "blue", 28),
        _wedge(m, a, c, b, "black", 28),
        _wedge(m, e, c, a, "red", 30),
        _wedge(m, d, c, e, "black", 30),
    ]
    segs = [
        _seg(m, b, a, "black", weight="thick"),
        _seg(m, a, f, "black", stroke="dotted", weight="thin"),
        _seg(m, a, c, "yellow", weight="thick"),
        _seg(m, b, c, "red", weight="thick"),
        _seg(m, c, d, "red", stroke="dotted", weight="normal"),
        _seg(m, c, e, "blue", weight="thick"),
    ]
    checks = {
        "CE_parallel_BA": _zero((e.x - c.x) * (a.y - b.y) - (e.y - c.y) * (a.x - b.x)),
        "alternate_spread_equal": _zero(spread(a, b, a, c) - spread(c, a, c, e)),
        "corresponding_spread_equal": _zero(spread(b, a, b, c) - spread(c, e, c, d)),
    }
    return ByrnePlate(
        prop_id="I.32",
        slug="i32",
        heath_id="elem.1.32",
        g_id="G.125",
        book=1,
        title="Book I, Prop. XXXII — Exterior Angle & Triangle Angle Sum",
        pickering_page="p. 33",
        number_field="Q",
        model=m,
        wedges=wedges,
        segments=segs,
        proof_checks=checks,
        canvas_size=(640, 420),
    )


def build_i46() -> ByrnePlate:
    """Book I, Prop. 46 (p. 47): To describe a square on a given straight line."""
    m = _new_model("I.46")
    a = m.set_point(0, 0, ID="A", classes=["given"])
    b = m.set_point(3, 0, ID="B", classes=["given"])
    c = m.set_point(0, 3, ID="C")
    d = m.set_point(3, 3, ID="D")
    e = m.set_point(0, sp.Rational(39, 10), ID="E")

    polys = [_poly(m, [a, b, d, c], "yellow", mode="outline", stroke_color="none")]
    wedges = [
        _wedge(m, b, a, c, "yellow", 28),
        _wedge(m, a, c, d, "black", 28),
        _wedge(m, c, d, b, "blue", 28),
        _wedge(m, d, b, a, "red", 28),
    ]
    segs = [
        _seg(m, a, b, "black", weight="thick"),
        _seg(m, a, c, "blue", weight="thick"),
        _seg(m, c, e, "blue", stroke="dotted", weight="normal"),
        _seg(m, c, d, "red", weight="thick"),
        _seg(m, b, d, "yellow", weight="thick"),
    ]
    checks = {
        "four_equal_sides": _zero(quadrance(a, b) - quadrance(a, c))
        and _zero(quadrance(a, b) - quadrance(c, d))
        and _zero(quadrance(a, b) - quadrance(b, d)),
        "right_angles": _zero(spread(a, b, a, c) - 1) and _zero(spread(c, a, c, d) - 1),
    }
    return ByrnePlate(
        prop_id="I.46",
        slug="i46",
        heath_id="elem.1.46",
        g_id="G.139",
        book=1,
        title="Book I, Prop. XLVI — Construction of the Square",
        pickering_page="p. 47",
        number_field="Q",
        model=m,
        polygons=polys,
        wedges=wedges,
        segments=segs,
        proof_checks=checks,
        canvas_size=(540, 480),
    )


def build_i47() -> ByrnePlate:
    """Book I, Prop. 47 (pp. 48–49): Byrne's Iconic Pythagorean Theorem."""
    m = _new_model("I.47")
    b = m.set_point(0, 0, ID="B", classes=["given"])
    c = m.set_point(5, 0, ID="C", classes=["given"])
    a = m.set_point(sp.Rational(9, 5), sp.Rational(12, 5), ID="A", classes=["given"])

    # Outward square < A B F G > on left short leg AB (|AB| = 3)
    f = m.set_point(sp.Rational(-12, 5), sp.Rational(9, 5), ID="F")
    g = m.set_point(sp.Rational(-3, 5), sp.Rational(21, 5), ID="G")

    # Outward square < A C K H > on right long leg AC (|AC| = 4)
    h = m.set_point(sp.Rational(21, 5), sp.Rational(28, 5), ID="H")
    k = m.set_point(sp.Rational(37, 5), sp.Rational(16, 5), ID="K")

    # Downward square < B C E D > on hypotenuse BC (|BC| = 5) split at L, M
    d = m.set_point(0, -5, ID="D")
    e = m.set_point(5, -5, ID="E")
    pt_l = m.set_point(sp.Rational(9, 5), 0, ID="L")
    pt_m = m.set_point(sp.Rational(9, 5), -5, ID="M")

    polys = [
        _poly(m, [a, b, f, g], "black", mode="filled", by="I.46"),
        _poly(m, [a, c, k, h], "red", mode="filled", by="I.46"),
        _poly(m, [b, pt_l, pt_m, d], "yellow", mode="filled", by="I.31"),
        _poly(m, [c, pt_l, pt_m, e], "blue", mode="filled", by="I.31"),
        _poly(m, [a, b, c], "yellow", mode="outline", stroke_color="none"),
    ]
    segs = [
        _seg(m, b, c, "red", weight="thick", by="given"),
        _seg(m, a, b, "yellow", weight="thick", by="given"),
        _seg(m, a, c, "blue", weight="thick", by="given"),
        _seg(m, a, pt_m, "black", stroke="dotted", weight="normal", by="I.31"),
        _seg(m, c, k, "blue", stroke="dotted", weight="normal"),
        _seg(m, c, e, "red", stroke="dashed", weight="normal"),
        _seg(m, a, d, "black", weight="normal", by="I.post.1"),
        _seg(m, f, c, "black", weight="normal", by="I.post.1"),
    ]

    poly_abfg = spg.Polygon(a, b, f, g)
    poly_ackh = spg.Polygon(a, c, k, h)
    poly_blmd = spg.Polygon(b, pt_l, pt_m, d)
    poly_clme = spg.Polygon(c, pt_l, pt_m, e)

    checks = {
        "right_angle_at_A": _zero(spread(a, b, a, c) - 1),
        "pythagorean_quadrance": _zero(
            quadrance(b, c) - (quadrance(a, b) + quadrance(a, c))
        ),
        "windmill_chords_equal": _zero(quadrance(a, d) - quadrance(f, c)),
        "left_square_eq_yellow_rect": _zero(
            abs(poly_abfg.area) - abs(poly_blmd.area)
        ),
        "right_square_eq_blue_rect": _zero(
            abs(poly_ackh.area) - abs(poly_clme.area)
        ),
    }
    return ByrnePlate(
        prop_id="I.47",
        slug="i47",
        heath_id="elem.1.47",
        g_id="G.140",
        book=1,
        title="Book I, Prop. XLVII — The Pythagorean Theorem",
        pickering_page="pp. 48–49",
        number_field="Q",
        model=m,
        polygons=polys,
        segments=segs,
        proof_checks=checks,
        canvas_size=(640, 620),
    )


# ---------------------------------------------------------------------------
# Book II Geometric Algebra & Golden Section
# ---------------------------------------------------------------------------


def build_ii4() -> ByrnePlate:
    """Book II, Prop. 4 (pp. 56–57): Square on a divided line (a + b)² = a² + b² + 2ab."""
    m = _new_model("II.4")
    # Whole segment AB = 5 cut at C into AC = 3, CB = 2
    a = m.set_point(0, 5, ID="A", classes=["given"])
    c = m.set_point(3, 5, ID="C", classes=["given"])
    b = m.set_point(5, 5, ID="B", classes=["given"])

    d = m.set_point(0, 0, ID="D")
    e = m.set_point(5, 0, ID="E")
    k = m.set_point(3, 0, ID="K")
    h = m.set_point(0, 3, ID="H")
    g = m.set_point(3, 3, ID="G")
    f = m.set_point(5, 3, ID="F")

    polys = [
        _poly(m, [d, k, g, h], "blue", mode="half", by="II.4"),
        _poly(m, [g, f, b, c], "red", mode="half", by="II.4"),
        _poly(m, [h, g, c, a], "yellow", mode="filled", by="II.4"),
        _poly(m, [k, e, f, g], "yellow", mode="filled", by="II.4"),
    ]
    segs = [
        _seg(m, a, c, "blue", weight="thick"),
        _seg(m, c, b, "red", weight="thick"),
        _seg(m, d, g, "black", weight="normal"),
        _seg(m, g, b, "black", stroke="dotted", weight="normal"),
        _seg(m, h, f, "black", stroke="dashed", weight="thin"),
        _seg(m, c, k, "black", stroke="dashed", weight="thin"),
    ]
    checks = {
        "binomial_area_identity": _zero(
            sp.Integer(5) ** 2 - (sp.Integer(3) ** 2 + sp.Integer(2) ** 2 + 2 * 3 * 2)
        ),
        "diagonal_collinear": _zero((g.x - d.x) * (b.y - d.y) - (g.y - d.y) * (b.x - d.x)),
    }
    return ByrnePlate(
        prop_id="II.4",
        slug="ii4",
        heath_id="elem.2.4",
        g_id="G.147",
        book=2,
        title="Book II, Prop. IV — Square of a Divided Line",
        pickering_page="pp. 56–57",
        number_field="Q",
        model=m,
        polygons=polys,
        segments=segs,
        proof_checks=checks,
        canvas_size=(540, 500),
    )


def build_ii5() -> ByrnePlate:
    """Book II, Prop. 5 (p. 58): Equal and unequal division AD·DB + CD² = CB²."""
    m = _new_model("II.5")
    # AB = 6 bisected at C = 3 and cut unequally at D = 5
    a = m.set_point(0, 3, ID="A", classes=["given"])
    c = m.set_point(3, 3, ID="C", classes=["given"])
    d = m.set_point(5, 3, ID="D", classes=["given"])
    b = m.set_point(6, 3, ID="B", classes=["given"])

    # Square CEFB on CB (3x3) below y=3
    e = m.set_point(3, 0, ID="E")
    f = m.set_point(6, 0, ID="F")
    pt_h = m.set_point(3, 2, ID="H")
    pt_l = m.set_point(5, 2, ID="L")
    pt_m = m.set_point(6, 2, ID="M")
    pt_g = m.set_point(5, 0, ID="G")
    pt_k = m.set_point(0, 2, ID="K")

    polys = [
        _poly(m, [a, c, pt_h, pt_k], "black", mode="filled"),
        _poly(m, [c, d, pt_l, pt_h], "yellow", mode="filled"),
        _poly(m, [pt_l, pt_m, f, pt_g], "yellow", mode="filled"),
        _poly(m, [pt_h, pt_l, pt_g, e], "red", mode="filled"),
        _poly(m, [d, b, pt_m, pt_l], "blue", mode="filled"),
    ]
    segs = [
        _seg(m, a, c, "black", weight="thick"),
        _seg(m, c, d, "red", weight="thick"),
        _seg(m, d, b, "blue", weight="thick"),
        _seg(m, e, b, "black", stroke="dotted", weight="normal"),
    ]
    checks = {
        "gnomon_plus_square_identity": _zero((5 * 1) + (2**2) - (3**2)),
    }
    return ByrnePlate(
        prop_id="II.5",
        slug="ii5",
        heath_id="elem.2.5",
        g_id="G.148",
        book=2,
        title="Book II, Prop. V — Rectangle of Unequal Segments Plus Inner Square",
        pickering_page="p. 58",
        number_field="Q",
        model=m,
        polygons=polys,
        segments=segs,
        proof_checks=checks,
        canvas_size=(620, 380),
    )


def build_ii11() -> ByrnePlate:
    """Book II, Prop. 11 (p. 66): Cutting a line in Extreme and Mean Ratio (Golden Section)."""
    m = _new_model("II.11")
    inv_phi = sp.simplify(PHI - 1)  # 1/phi = (sqrt(5) - 1)/2

    a = m.set_point(0, 1, ID="A", classes=["given"])
    b = m.set_point(1, 1, ID="B", classes=["given"])
    c = m.set_point(0, 0, ID="C")
    d = m.set_point(1, 0, ID="D")
    e = m.set_point(0, sp.Rational(1, 2), ID="E")

    l_ca = m.construct_line(c, a, guide=True)
    c_eb = m.construct_circle(e, b, guide=True)
    f = m.intersect(l_ca, c_eb, beyond=(c, a), ID="F", by="I.3")

    h = m.set_point(inv_phi, 1, ID="H")
    g = m.set_point(inv_phi, f.y, ID="G")
    k = m.set_point(inv_phi, 0, ID="K")

    polys = [
        _poly(m, [a, f, g, h], "blue", mode="filled", by="I.46"),
        _poly(m, [a, h, k, c], "blue", mode="tinted", by="II.11"),
        _poly(m, [h, b, d, k], "yellow", mode="filled", by="II.11"),
    ]
    segs = [
        _seg(m, a, h, "red", weight="thick"),
        _seg(m, h, b, "red", stroke="dotted", weight="thick"),
        _seg(m, e, b, "black", weight="thick", by="I.post.1"),
        _seg(m, c, f, "blue", weight="normal"),
        _seg(m, g, k, "black", stroke="dashed", weight="normal"),
    ]

    sq_afgh = spg.Polygon(a, f, g, h)
    rect_hbdk = spg.Polygon(h, b, d, k)
    checks = {
        "EF_eq_EB": _zero(quadrance(e, f) - quadrance(e, b)),
        "golden_area_equality": _zero(abs(sq_afgh.area) - abs(rect_hbdk.area)),
        "AH_sq_eq_AB_times_HB": _zero(
            quadrance(a, h) - sp.sqrt(quadrance(a, b)) * sp.sqrt(quadrance(h, b))
        ),
    }
    return ByrnePlate(
        prop_id="II.11",
        slug="ii11",
        heath_id="elem.2.11",
        g_id="G.154",
        book=2,
        title="Book II, Prop. XI — Golden Section by Colored Areas",
        pickering_page="p. 66",
        number_field="Q(phi)",
        model=m,
        polygons=polys,
        segments=segs,
        proof_checks=checks,
        canvas_size=(540, 580),
    )


# ---------------------------------------------------------------------------
# Books III & IV Circles, Tangents & Regular Polygons
# ---------------------------------------------------------------------------


def build_iii20() -> ByrnePlate:
    """Book III, Prop. 20 (p. 102): Central angle is double the inscribed angle."""
    m = _new_model("III.20")
    o = m.set_point(0, 0, ID="O", classes=["given"])
    a = m.set_point(0, 5, ID="A", classes=["given"])
    d = m.set_point(0, -5, ID="D")
    b = m.set_point(-4, -3, ID="B", classes=["given"])
    c = m.set_point(3, -4, ID="C", classes=["given"])

    _, sc = _circ(m, o, a, "blue", by="given")
    wedges = [
        _wedge(m, b, a, c, "yellow", 30),
        _wedge(m, b, o, c, "blue", 30),
        _wedge(m, o, b, a, "red", 24),
    ]
    segs = [
        _seg(m, a, o, "red", weight="thick"),
        _seg(m, o, d, "red", stroke="dotted", weight="normal"),
        _seg(m, a, b, "black", weight="thick"),
        _seg(m, a, c, "black", weight="thick"),
        _seg(m, o, b, "black", weight="normal"),
        _seg(m, o, c, "black", weight="normal"),
    ]

    s_inscribed = spread(a, b, a, c)
    s_central = spread(o, b, o, c)
    checks = {
        "B_and_C_on_circle": _zero(quadrance(o, b) - 25) and _zero(quadrance(o, c) - 25),
        "double_angle_spread_law": _zero(
            s_central - 4 * s_inscribed * (1 - s_inscribed)
        ),
    }
    return ByrnePlate(
        prop_id="III.20",
        slug="iii20",
        heath_id="elem.3.20",
        g_id="G.185",
        book=3,
        title="Book III, Prop. XX — Central & Inscribed Angles",
        pickering_page="p. 102",
        number_field="Q",
        model=m,
        wedges=wedges,
        circles=[sc],
        segments=segs,
        proof_checks=checks,
        canvas_size=(540, 540),
    )


def build_iii31() -> ByrnePlate:
    """Book III, Prop. 31 (p. 115): Angle in a semicircle is a right angle (Thales)."""
    m = _new_model("III.31")
    o = m.set_point(0, 0, ID="O", classes=["given"])
    b = m.set_point(-5, 0, ID="B", classes=["given"])
    c = m.set_point(5, 0, ID="C", classes=["given"])
    a = m.set_point(-3, 4, ID="A", classes=["given"])

    _, sc = _circ(m, o, b, "black", by="given")
    wedges = [
        _wedge(m, b, a, o, "yellow", 28),
        _wedge(m, o, a, c, "black", 28),
        _wedge(m, o, b, a, "red", 26),
        _wedge(m, a, c, o, "blue", 26),
    ]
    segs = [
        _seg(m, b, o, "blue", weight="thick"),
        _seg(m, o, c, "black", weight="thick"),
        _seg(m, o, a, "red", weight="thick"),
        _seg(m, b, a, "black", weight="thick"),
        _seg(m, a, c, "black", weight="thick"),
    ]
    checks = {
        "A_on_semicircle": _zero(quadrance(o, a) - quadrance(o, b)),
        "thales_right_angle": _zero(spread(a, b, a, c) - 1),
    }
    return ByrnePlate(
        prop_id="III.31",
        slug="iii31",
        heath_id="elem.3.31",
        g_id="G.196",
        book=3,
        title="Book III, Prop. XXXI — Angle in a Semicircle (Thales)",
        pickering_page="p. 115",
        number_field="Q",
        model=m,
        wedges=wedges,
        circles=[sc],
        segments=segs,
        proof_checks=checks,
        canvas_size=(560, 520),
    )


def build_iii36() -> ByrnePlate:
    """Book III, Prop. 36 (p. 121): Tangent-Secant Power of a Point."""
    m = _new_model("III.36")
    o = m.set_point(0, 0, ID="O", classes=["given"])
    a = m.set_point(3, 0, ID="A")
    c = m.set_point(-3, 0, ID="C")
    d = m.set_point(-5, 0, ID="D", classes=["given"])
    t = m.set_point(sp.Rational(-9, 5), sp.Rational(12, 5), ID="T")

    _, sc = _circ(m, o, a, "black", by="given")
    wedges = [_wedge(m, d, t, o, "yellow", 24)]
    segs = [
        _seg(m, d, t, "blue", weight="thick", by="III.17"),
        _seg(m, d, c, "red", weight="thick"),
        _seg(m, c, o, "red", stroke="dotted", weight="thick"),
        _seg(m, o, a, "black", weight="thick"),
        _seg(m, o, t, "yellow", weight="thick"),
    ]
    checks = {
        "T_on_circle": _zero(quadrance(o, t) - 9),
        "tangent_perpendicular_radius": _zero(spread(t, d, t, o) - 1),
        "tangent_secant_power": _zero(
            quadrance(d, t) - sp.sqrt(quadrance(d, c) * quadrance(d, a))
        ),
    }
    return ByrnePlate(
        prop_id="III.36",
        slug="iii36",
        heath_id="elem.3.36",
        g_id="G.201",
        book=3,
        title="Book III, Prop. XXXVI — Tangent-Secant Power of a Point",
        pickering_page="p. 121",
        number_field="Q",
        model=m,
        wedges=wedges,
        circles=[sc],
        segments=segs,
        proof_checks=checks,
        canvas_size=(620, 440),
    )


def build_iv4() -> ByrnePlate:
    """Book IV, Prop. 4 (p. 129): Inscribing a Circle in a Given Triangle (13-14-15)."""
    m = _new_model("IV.4")
    b = m.set_point(0, 0, ID="B", classes=["given"])
    c = m.set_point(14, 0, ID="C", classes=["given"])
    a = m.set_point(5, 12, ID="A", classes=["given"])

    inc = m.set_point(6, 4, ID="I")
    e = m.set_point(6, 0, ID="E")
    f = m.set_point(sp.Rational(30, 13), sp.Rational(72, 13), ID="F")
    g = m.set_point(sp.Rational(46, 5), sp.Rational(32, 5), ID="G")

    _, sc_in = _circ(m, inc, e, "black", by="IV.4")
    polys = [_poly(m, [a, b, c], "yellow", mode="outline", stroke_color="none")]
    segs = [
        _seg(m, a, b, "yellow", weight="thick"),
        _seg(m, a, c, "red", weight="thick"),
        _seg(m, b, c, "black", weight="thick"),
        _seg(m, b, inc, "blue", stroke="dotted", weight="normal", by="I.9"),
        _seg(m, c, inc, "blue", weight="normal", by="I.9"),
        _seg(m, inc, e, "black", stroke="dotted", weight="normal", by="I.12"),
        _seg(m, inc, f, "yellow", stroke="dotted", weight="normal", by="I.12"),
        _seg(m, inc, g, "red", stroke="dotted", weight="normal", by="I.12"),
    ]
    checks = {
        "equal_inradii": _zero(quadrance(inc, e) - quadrance(inc, f))
        and _zero(quadrance(inc, e) - quadrance(inc, g)),
        "perpendicular_contacts": _zero(spread(e, inc, e, c) - 1)
        and _zero(spread(f, inc, f, b) - 1)
        and _zero(spread(g, inc, g, c) - 1),
    }
    return ByrnePlate(
        prop_id="IV.4",
        slug="iv4",
        heath_id="elem.4.4",
        g_id="G.217",
        book=4,
        title="Book IV, Prop. IV — Incircle of a Triangle",
        pickering_page="p. 129",
        number_field="Q",
        model=m,
        polygons=polys,
        circles=[sc_in],
        segments=segs,
        proof_checks=checks,
        canvas_size=(620, 480),
    )


def build_iv10() -> ByrnePlate:
    """Book IV, Prop. 10 (pp. 135–136): Isosceles 36°-72°-72° Golden Triangle."""
    m = _new_model("IV.10")
    inv_phi = sp.simplify(PHI - 1)

    a = m.set_point(0, 0, ID="A", classes=["given"])
    b = m.set_point(1, 0, ID="B", classes=["given"])
    c = m.set_point(inv_phi, 0, ID="C", by="II.11")

    c_ab, sc_ab = _circ(m, a, b, "red", by="I.post.3")
    k = m.set_point(1 + inv_phi, 0, ID="K", guide=True)
    c_bk = m.construct_circle(b, k, guide=True)
    d = m.intersect(c_ab, c_bk, side_of=(a, b, 1), ID="D", by="IV.1")

    # Circumcenter P of < A C D > via exact perpendicular bisectors
    mid_ac = m.set_point(c.x / 2, 0, ID="M1", guide=True)
    p_ac_up = m.set_point(c.x / 2, 1, ID="M2", guide=True)
    mid_ad = m.set_point(d.x / 2, d.y / 2, ID="M3", guide=True)
    p_ad_perp = m.set_point(d.x / 2 - d.y, d.y / 2 + d.x, ID="M4", guide=True)
    l_b1 = m.construct_line(mid_ac, p_ac_up, guide=True)
    l_b2 = m.construct_line(mid_ad, p_ad_perp, guide=True)
    p = m.intersect(l_b1, l_b2, ID="P", guide=True, by="IV.5")
    _, sc_acd = _circ(m, p, a, "blue", by="IV.5")

    polys = [_poly(m, [a, b, d], "yellow", mode="outline", stroke_color="none")]
    wedges = [
        _wedge(m, b, a, d, "red", 28),
        _wedge(m, c, d, b, "yellow", 24),
        _wedge(m, d, b, a, "blue", 26),
    ]
    segs = [
        _seg(m, a, c, "black", weight="thick"),
        _seg(m, c, b, "black", stroke="dotted", weight="thick"),
        _seg(m, a, d, "yellow", weight="thick"),
        _seg(m, b, d, "blue", weight="thick"),
        _seg(m, c, d, "red", weight="thick"),
    ]
    checks = {
        "BD_eq_AC": _zero(quadrance(b, d) - quadrance(a, c)),
        "CD_eq_BD": _zero(quadrance(c, d) - quadrance(b, d)),
        "circumcircle_passes_C_and_D": _zero(quadrance(p, a) - quadrance(p, c))
        and _zero(quadrance(p, a) - quadrance(p, d)),
        "base_angles_equal": _zero(spread(b, a, b, d) - spread(d, a, d, b)),
    }
    return ByrnePlate(
        prop_id="IV.10",
        slug="iv10",
        heath_id="elem.4.10",
        g_id="G.223",
        book=4,
        title="Book IV, Prop. X — The 36°–72°–72° Golden Triangle",
        pickering_page="pp. 135–136",
        number_field="Q(phi, sqrt(10 - 2*sqrt(5)))",
        model=m,
        polygons=polys,
        wedges=wedges,
        circles=[sc_ab, sc_acd],
        segments=segs,
        proof_checks=checks,
        canvas_size=(580, 560),
    )


def build_iv11() -> ByrnePlate:
    """Book IV, Prop. 11 (p. 137): Regular Pentagon Inscribed in a Given Circle."""
    m = _new_model("IV.11")
    cos72 = (sp.sqrt(5) - 1) / sp.Integer(4)
    sin72 = sp.sqrt(10 + 2 * sp.sqrt(5)) / sp.Integer(4)
    cos36 = (sp.sqrt(5) + 1) / sp.Integer(4)
    sin36 = sp.sqrt(10 - 2 * sp.sqrt(5)) / sp.Integer(4)

    o = m.set_point(0, 0, ID="O", guide=True)
    a = m.set_point(0, 1, ID="A", classes=["given"])
    b = m.set_point(-sin72, cos72, ID="B")
    c = m.set_point(-sin36, -cos36, ID="C")
    d = m.set_point(sin36, -cos36, ID="D")
    e = m.set_point(sin72, cos72, ID="E")

    _, sc_circ = _circ(m, o, a, "blue", by="given")
    polys = [
        _poly(m, [a, c, d], "yellow", mode="filled", by="IV.2"),
        _poly(m, [a, b, c, d, e], "blue", mode="outline", stroke_color="none"),
    ]
    wedges = [
        _wedge(m, c, a, d, "black", 28),
        _wedge(m, e, c, a, "blue", 26),
        _wedge(m, d, c, e, "black", 26),
        _wedge(m, b, d, c, "red", 26),
    ]
    segs = [
        _seg(m, a, b, "red", weight="thick"),
        _seg(m, b, c, "red", stroke="dotted", weight="thick"),
        _seg(m, c, d, "black", weight="thick"),
        _seg(m, d, e, "yellow", weight="thick"),
        _seg(m, e, a, "blue", weight="thick"),
        _seg(m, c, e, "black", weight="normal", by="I.9"),
        _seg(m, d, b, "black", weight="normal", by="I.9"),
    ]

    q_ab = quadrance(a, b)
    checks = {
        "all_vertices_on_unit_circle": all(
            _zero(quadrance(o, pt) - 1) for pt in (a, b, c, d, e)
        ),
        "equilateral_pentagon": all(
            _zero(quadrance(p1, p2) - q_ab)
            for p1, p2 in ((b, c), (c, d), (d, e), (e, a))
        ),
        "diagonal_to_side_phi_squared": _zero(
            quadrance(a, c) - PHI**2 * q_ab
        ),
    }
    return ByrnePlate(
        prop_id="IV.11",
        slug="iv11",
        heath_id="elem.4.11",
        g_id="G.224",
        book=4,
        title="Book IV, Prop. XI — Regular Pentagon Inscribed in a Circle",
        pickering_page="p. 137",
        number_field="Q(phi, sqrt(10 - 2*sqrt(5)))",
        model=m,
        polygons=polys,
        wedges=wedges,
        circles=[sc_circ],
        segments=segs,
        proof_checks=checks,
        canvas_size=(540, 540),
    )


# ---------------------------------------------------------------------------
# Book VI Similar Figures & Extreme and Mean Ratio
# ---------------------------------------------------------------------------


def build_vi30() -> ByrnePlate:
    """Book VI, Prop. 30 (p. 258): Extreme and Mean Ratio via Application of Areas."""
    m = _new_model("VI.30")
    inv_phi = sp.simplify(PHI - 1)

    a = m.set_point(0, 0, ID="A", classes=["given"])
    e = m.set_point(inv_phi, 0, ID="E", by="VI.29")
    b = m.set_point(1, 0, ID="B", classes=["given"])

    d = m.set_point(0, 1, ID="D")
    f = m.set_point(inv_phi, 1, ID="F")
    c = m.set_point(1, 1, ID="C")
    h = m.set_point(0, -inv_phi, ID="H")
    pt_m = m.set_point(inv_phi, -inv_phi, ID="M")

    polys = [
        _poly(m, [a, e, f, d], "blue", mode="filled", by="VI.29"),
        _poly(m, [e, b, c, f], "yellow", mode="filled", by="I.46"),
        _poly(m, [a, e, pt_m, h], "red", mode="outline", stroke_color="red", by="VI.29"),
    ]
    segs = [
        _seg(m, a, e, "red", weight="thick"),
        _seg(m, e, b, "red", stroke="dotted", weight="thick"),
        _seg(m, h, pt_m, "yellow", weight="thick"),
        _seg(m, a, h, "red", weight="thick"),
        _seg(m, e, pt_m, "blue", weight="thick"),
    ]
    checks = {
        "applied_rectangle_equals_unit_square": _zero(
            inv_phi * (1 + inv_phi) - 1
        ),
        "extreme_and_mean_proportion": _zero(
            quadrance(a, e) - sp.sqrt(quadrance(a, b)) * sp.sqrt(quadrance(e, b))
        ),
    }
    return ByrnePlate(
        prop_id="VI.30",
        slug="vi30",
        heath_id="elem.6.30",
        g_id="G.328",
        book=6,
        title="Book VI, Prop. XXX — Extreme & Mean Ratio by Application of Areas",
        pickering_page="p. 258",
        number_field="Q(phi)",
        model=m,
        polygons=polys,
        segments=segs,
        proof_checks=checks,
        canvas_size=(540, 580),
    )


PLATE_REGISTRY: dict[str, Callable[[], ByrnePlate]] = {
    "I.1": build_i1,
    "I.4": build_i4,
    "I.5": build_i5,
    "I.15": build_i15,
    "I.32": build_i32,
    "I.46": build_i46,
    "I.47": build_i47,
    "II.4": build_ii4,
    "II.5": build_ii5,
    "II.11": build_ii11,
    "III.20": build_iii20,
    "III.31": build_iii31,
    "III.36": build_iii36,
    "IV.4": build_iv4,
    "IV.10": build_iv10,
    "IV.11": build_iv11,
    "VI.30": build_vi30,
}


def list_plate_ids() -> list[str]:
    """Return ordered list of all 17 showcase Byrne proposition IDs."""
    return list(PLATE_REGISTRY.keys())


def build_plate(prop_id: str) -> ByrnePlate:
    """Construct and verify a single :class:`ByrnePlate` by proposition ID."""
    key = prop_id.strip()
    if key not in PLATE_REGISTRY:
        raise KeyError(
            f"Unknown Byrne plate {prop_id!r}; available: {list(PLATE_REGISTRY)}"
        )
    return PLATE_REGISTRY[key]()


def build_all_plates() -> list[ByrnePlate]:
    """Construct and verify all 17 showcase :class:`ByrnePlate` models."""
    return [builder() for builder in PLATE_REGISTRY.values()]
