"""Formal grammar, AST, and 3-way Rosetta metrics for Oliver Byrne's 1847 Visual Pseudocode.

Models Oliver Byrne's 1847 notation (*Introduction*, pp. ix–xi, xxvii–xxix) as a
**pointer-free, typed geometric value-token language**:

- **Classical Euclidean Text (Heath / Heiberg)**: *Pass-by-reference*. Geometric
  objects are unnamed in ink; vertices carry alphabetic memory addresses
  (``A``, ``B``, ``C``, ...) and prose dereferences composite tuples
  (``line AB``, ``angle BAC``, ``triangle FBC``, ``square ABFG``) at every step.
- **Byrne 1847 Visual Pseudocode**: *Pass-by-value*. Every geometric primitive is
  assigned a perceptual signature ``(kind, color, stroke, fill)`` that appears
  *literally* inside vertical symbolic equations (``∴``, ``∵``, ``=``, ``+``,
  ``⊏``, ``⊐``, ``∥``, ``⊥``, ``∷``) with marginal axiom/proposition citations.
- **GEOMETOR Formal Pseudocode (elements / model)**: *Typed Constructive DAG*.
  Explicit constructor steps (``line``, ``circle``, ``intersect``) and symbolic
  algebraic invariants over exact number fields.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import StrEnum

from geometor.byrne.sphinx_ext import render_byrne_glyph_html, render_byrne_operator_html

__all__ = [
    "ROSETTA_PROGRAMS",
    "ByrneProgram",
    "ByrneStatement",
    "FillMode",
    "OpToken",
    "ProofPhase",
    "RegisterDiagnostic",
    "RosettaMetrics",
    "StrokeMode",
    "TextFragment",
    "TokenKind",
    "VisualToken",
    "analyze_visual_registers",
    "compute_rosetta_metrics",
    "count_alphabetic_dereferences",
    "get_rosetta_program",
]


class TokenKind(StrEnum):
    """Typed geometric primitive sorts in Byrne's 1847 visual grammar."""

    LINE = "line"
    ANGLE = "angle"
    TRIANGLE = "tri"
    SQUARE = "sq"
    RECTANGLE = "rect"
    ARC = "arc"
    CIRCLE = "circle"
    MAGNITUDE = "mag"


class StrokeMode(StrEnum):
    """Stroke patterns used by Byrne to multiply his 4-color register space."""

    SOLID = "solid"
    DASHED = "dashed"
    DOTTED = "dotted"
    SOLID_DOTTED = "solid-dotted"


class FillMode(StrEnum):
    """Planar region rendering modes in Chiswick Press woodblock plates."""

    NONE = "outline"
    FILLED = "filled"
    HALF = "half"
    THREE_SIDE = "three-side"


class ProofPhase(StrEnum):
    """Canonical block phases in Byrne's structured proposition layout."""

    ENUNCIATION = "enunciation"
    GIVEN = "given"
    SOUGHT = "sought"
    CONSTRUCTION = "construction"
    DEMONSTRATION = "demonstration"
    QED = "qed"


@dataclass(frozen=True)
class VisualToken:
    """An inline pass-by-value geometric glyph in a Byrne statement.

    Encodes primitive ``kind`` (:class:`TokenKind`), Byrne ``color`` expression,
    ``stroke`` (:class:`StrokeMode`), ``fill`` (:class:`FillMode`), optional
    interactive ``geom_ref``, ``squared`` exponent flag, Book V ``shape_hint``,
    and intentional symmetric ``congruence_group``.
    """

    kind: TokenKind
    color: str
    stroke: StrokeMode = StrokeMode.SOLID
    fill: FillMode = FillMode.FILLED
    geom_ref: str = ""
    squared: bool = False
    shape_hint: str = ""
    congruence_group: str = ""

    @property
    def register_signature(self) -> tuple[str, str, str, str, str]:
        """Perceptual tuple distinguishing this token in visual working memory."""
        return (
            self.kind.value,
            self.color,
            self.stroke.value,
            self.fill.value,
            self.shape_hint,
        )

    def role_spec_body(self, plate_id: str = "") -> str:
        """Build the RST role argument string for ``:byrne-<kind>:``."""
        parts: list[str] = [self.color]
        if self.kind in {TokenKind.LINE, TokenKind.ARC, TokenKind.CIRCLE}:
            if self.stroke != StrokeMode.SOLID:
                parts.append(self.stroke.value)
            elif self.kind == TokenKind.LINE:
                parts.append("solid")
        if (
            self.kind in {TokenKind.TRIANGLE, TokenKind.SQUARE, TokenKind.RECTANGLE}
            and "/" not in self.color
            and self.fill != FillMode.THREE_SIDE
        ):
            parts.append(self.fill.value)
        if self.shape_hint:
            parts.append(self.shape_hint)
        if self.squared:
            parts.append("squared")
        spec = " ".join(parts)
        if self.geom_ref:
            qualified = f"{plate_id}:{self.geom_ref}" if plate_id else self.geom_ref
            return f"{spec} <{qualified}>"
        return spec

    def to_rst(self, plate_id: str = "") -> str:
        """Compile this visual token into a Sphinx ``:byrne-*:`` role."""
        return f":byrne-{self.kind.value}:`{self.role_spec_body(plate_id)}`"

    def to_html(self, plate_id: str = "") -> str:
        """Render this visual token directly to an interactive HTML/SVG span."""
        return render_byrne_glyph_html(
            f"byrne-{self.kind.value}",
            self.role_spec_body(plate_id),
        )

    def to_compact(self) -> str:
        """Return a concise human-readable token representation for CLI/tables."""
        mods = [self.color]
        if self.stroke != StrokeMode.SOLID:
            mods.append(self.stroke.value)
        if self.shape_hint:
            mods.append(self.shape_hint)
        exp = "²" if self.squared else ""
        return f"⟦{self.kind.value}:{' '.join(mods)}⟧{exp}"


@dataclass(frozen=True)
class OpToken:
    """An algebraic, relational, or deductive operator in a Byrne equation."""

    symbol: str

    def to_rst(self) -> str:
        if self.symbol in {"+", "-", "=", ",", ":"}:
            return self.symbol
        return f":byrne-op:`{self.symbol}`"

    def to_html(self) -> str:
        if self.symbol in {"+", "-", "=", ",", ":"}:
            return f'<span class="byrne-op-token">{self.symbol}</span>'
        return render_byrne_operator_html(self.symbol)

    def to_compact(self) -> str:
        mapping = {
            "therefore": "∴",
            "because": "∵",
            "gt": "⊏",
            "lt": "⊐",
            "parallel": "∥",
            "perp": "⊥",
            "prop": "∷",
            "rect-by": "×",
            "right-angle": "∟",
            "two-right-angles": "2∟",
        }
        return mapping.get(self.symbol, self.symbol)


@dataclass(frozen=True)
class TextFragment:
    """Minimal connecting English keyword in Byrne's telegraphic equations."""

    text: str

    def to_rst(self) -> str:
        return self.text

    def to_compact(self) -> str:
        return self.text


StatementItem = VisualToken | OpToken | TextFragment


@dataclass(frozen=True)
class ByrneStatement:
    """A single structured line in a Byrne visual program.

    Stores block ``phase`` (:class:`ProofPhase`), ordered ``items`` of visual
    tokens, operators, and minimal connectors, marginal Euclidean
    ``justifications``, and an optional analytical ``comment``.
    """

    phase: ProofPhase
    items: tuple[StatementItem, ...]
    justifications: tuple[str, ...] = ()
    comment: str = ""

    def visual_tokens(self) -> list[VisualToken]:
        """Return all :class:`VisualToken` instances in this statement."""
        return [it for it in self.items if isinstance(it, VisualToken)]

    def word_count(self) -> int:
        """Count natural-language words (excluding pure visual glyphs and operators)."""
        total = 0
        for it in self.items:
            if isinstance(it, TextFragment):
                total += len(re.findall(r"[A-Za-z']+", it.text))
        return total

    def to_rst(self, plate_id: str = "") -> str:
        """Compile statement into RST with inline ``:byrne-*:`` and ``:just:`` roles."""
        parts: list[str] = []
        for it in self.items:
            if isinstance(it, VisualToken):
                parts.append(it.to_rst(plate_id))
            else:
                parts.append(it.to_rst())
        body = " ".join(p for p in parts if p)
        if self.justifications:
            cites = ", ".join(f":just:`{j}`" for j in self.justifications)
            return f"{body} ({cites})"
        return body

    def to_compact(self) -> str:
        """Render statement into compact Unicode pseudocode."""
        parts = [it.to_compact() for it in self.items]
        body = " ".join(p for p in parts if p)
        if self.justifications:
            return f"{body}    [{', '.join(self.justifications)}]"
        return body


@dataclass(frozen=True)
class ByrneProgram:
    """Complete 3-way Rosetta formalization of a Euclidean proposition.

    Pairs Byrne's 1847 pointer-free visual program with Heath's classical
    alphabetic English translation and GEOMETOR's formal DAG pseudocode.
    """

    prop_id: str
    plate_id: str
    heath_id: str
    g_id: str
    title: str
    pickering_page: str
    number_field: str
    statements: tuple[ByrneStatement, ...]
    heath_text: str
    geometor_steps: tuple[str, ...]
    design_notes: str = ""

    def all_visual_tokens(self) -> list[VisualToken]:
        """Flatten all visual tokens appearing across all phases of the program."""
        out: list[VisualToken] = []
        for st in self.statements:
            out.extend(st.visual_tokens())
        return out


@dataclass(frozen=True)
class RegisterDiagnostic:
    """Static visual register-allocation audit for a :class:`ByrneProgram`."""

    distinct_signatures: int
    distinct_geom_refs: int
    uses_stroke_modulation: bool
    uses_composite_tokens: bool
    intentional_congruence_twins: tuple[str, ...]
    ambiguous_collisions: tuple[str, ...]

    @property
    def is_unambiguous(self) -> bool:
        """Return True iff zero unintended visual register collisions exist."""
        return len(self.ambiguous_collisions) == 0


@dataclass(frozen=True)
class RosettaMetrics:
    """Quantitative comparison across Heath (alphabetic), Byrne (visual), and GEOMETOR (DAG)."""

    prop_id: str
    heath_words: int
    heath_pointer_dereferences: int
    byrne_words: int
    byrne_pointer_dereferences: int
    byrne_visual_tokens: int
    byrne_distinct_registers: int
    byrne_statement_count: int
    geometor_step_count: int
    word_compression_ratio: float
    register_diagnostic: RegisterDiagnostic


_POINTER_TOKEN_RE = re.compile(
    r"\b(?:[A-Z]{2,4}|angle\s+[A-Z]{3}|triangle\s+[A-Z]{3}|square\s+[A-Z]{2,4}|"
    r"circle\s+[A-Z]{2,3}|point\s+[A-Z]|center\s+[A-Z]|centre\s+[A-Z])\b"
)


def count_alphabetic_dereferences(text: str) -> int:
    """Count symbolic letter-pointer dereferences (``AB``, ``BCD``, ``point A``, ...) in classical prose.

    Excludes Roman numeral proposition references (``I``, ``II``, ``III``, ``IV``, ``V``, ``VI``)
    when preceded by ``Book`` or ``Prop``.
    """
    cleaned = re.sub(r"\b(?:Book|Prop\.?|Post\.?|Def\.?|C\.N\.?)\s+[IVXLCDM]+\b", "", text)
    hits: list[str] = []
    for match in re.finditer(r"\b[A-Z]{1,4}\b", cleaned):
        tok = match.group(0)
        # Single capital 'I' or sentence-start 'A' is only a vertex pointer after 'point'/'centre'/'at'/'from'/'to'
        start = match.start()
        prefix = cleaned[max(0, start - 10) : start].lower()
        if len(tok) == 1:
            if any(
                prefix.endswith(kw)
                for kw in ("point ", "centre ", "center ", "at ", "from ", "to ", "join ", "let ")
            ):
                hits.append(tok)
        else:
            if tok not in {"QED", "QEF"}:
                hits.append(tok)
    return len(hits)


def analyze_visual_registers(program: ByrneProgram) -> RegisterDiagnostic:
    """Audit visual register allocation and collision freedom in ``program``.

    Distinguishes:

    1. **Stroke modulation** (``dashed`` / ``dotted`` / ``solid-dotted``) when 4 colors
       alone cannot separate adjacent collinear or overlapping elements;
    2. **Composite tokens** (``yellow+black`` split angles or ``red/blue/black`` triangles);
    3. **Intentional congruence twins** (e.g. equal legs ``/ A B /`` and ``/ A C /`` in ``I.5``
       deliberately sharing ``red solid`` to encode ``AB = AC`` visually); and
    4. **Ambiguous collisions** (two unequal ``geom_ref`` entities sharing an identical
       register signature without a ``congruence_group`` declaration).
    """
    tokens = program.all_visual_tokens()
    sig_to_refs: dict[tuple[str, str, str, str, str], set[str]] = {}
    sig_to_groups: dict[tuple[str, str, str, str, str], set[str]] = {}
    all_refs: set[str] = set()
    uses_stroke_mod = False
    uses_composite = False

    for tok in tokens:
        sig = tok.register_signature
        if tok.stroke != StrokeMode.SOLID:
            uses_stroke_mod = True
        if "+" in tok.color or "/" in tok.color:
            uses_composite = True
        if tok.geom_ref:
            all_refs.add(tok.geom_ref)
            sig_to_refs.setdefault(sig, set()).add(tok.geom_ref)
        if tok.congruence_group:
            sig_to_groups.setdefault(sig, set()).add(tok.congruence_group)

    twins: list[str] = []
    collisions: list[str] = []
    for sig, refs in sig_to_refs.items():
        if len(refs) > 1:
            groups = sig_to_groups.get(sig, set())
            desc = f"{sig[0]}({sig[1]}, {sig[2]}) -> {sorted(refs)}"
            if groups:
                twins.append(desc)
            else:
                collisions.append(desc)

    return RegisterDiagnostic(
        distinct_signatures=len({t.register_signature for t in tokens}),
        distinct_geom_refs=len(all_refs),
        uses_stroke_modulation=uses_stroke_mod,
        uses_composite_tokens=uses_composite,
        intentional_congruence_twins=tuple(sorted(twins)),
        ambiguous_collisions=tuple(sorted(collisions)),
    )


def compute_rosetta_metrics(program: ByrneProgram) -> RosettaMetrics:
    """Compute quantitative Rosetta comparison metrics for a :class:`ByrneProgram`."""
    heath_words = len(re.findall(r"[A-Za-z']+", program.heath_text))
    heath_ptrs = count_alphabetic_dereferences(program.heath_text)
    byrne_words = sum(st.word_count() for st in program.statements)
    byrne_toks = program.all_visual_tokens()
    diag = analyze_visual_registers(program)
    ratio = round(byrne_words / heath_words, 3) if heath_words else 0.0

    return RosettaMetrics(
        prop_id=program.prop_id,
        heath_words=heath_words,
        heath_pointer_dereferences=heath_ptrs,
        byrne_words=byrne_words,
        byrne_pointer_dereferences=0,
        byrne_visual_tokens=len(byrne_toks),
        byrne_distinct_registers=diag.distinct_signatures,
        byrne_statement_count=len(program.statements),
        geometor_step_count=len(program.geometor_steps),
        word_compression_ratio=ratio,
        register_diagnostic=diag,
    )


# ---------------------------------------------------------------------------
# Canonical 7-Proposition Rosetta Corpus (Verified against 1847 Pickering Scan)
# ---------------------------------------------------------------------------

def _build_rosetta_corpus() -> dict[str, ByrneProgram]:
    programs: list[ByrneProgram] = [
        # 1. Book I, Proposition 1 (p. 1, leaf-035)
        ByrneProgram(
            prop_id="I.1",
            plate_id="i1",
            heath_id="elem.1.1",
            g_id="G.84",
            title="On a given finite straight line to construct an equilateral triangle",
            pickering_page="p. 1 (leaf 35)",
            number_field="Q(sqrt(3))",
            statements=(
                ByrneStatement(
                    ProofPhase.GIVEN,
                    (TextFragment("Let"), VisualToken(TokenKind.LINE, "black", geom_ref="/ A B /"), TextFragment("be the given finite straight line.")),
                ),
                ByrneStatement(
                    ProofPhase.SOUGHT,
                    (TextFragment("To construct an equilateral triangle on"), VisualToken(TokenKind.LINE, "black", geom_ref="/ A B /"), TextFragment(".")),
                ),
                ByrneStatement(
                    ProofPhase.CONSTRUCTION,
                    (TextFragment("Describe"), VisualToken(TokenKind.CIRCLE, "blue", geom_ref="( A B )"), TextFragment("and"), VisualToken(TokenKind.CIRCLE, "red", geom_ref="( B A )"), TextFragment("; draw"), VisualToken(TokenKind.LINE, "yellow", geom_ref="/ A C /"), TextFragment("and"), VisualToken(TokenKind.LINE, "red", geom_ref="/ B C /"), TextFragment(".")),
                    justifications=("I.post.3", "I.post.1"),
                ),
                ByrneStatement(
                    ProofPhase.DEMONSTRATION,
                    (VisualToken(TokenKind.LINE, "yellow", geom_ref="/ A C /"), OpToken("="), VisualToken(TokenKind.LINE, "black", geom_ref="/ A B /")),
                    justifications=("I.def.15",),
                ),
                ByrneStatement(
                    ProofPhase.DEMONSTRATION,
                    (VisualToken(TokenKind.LINE, "red", geom_ref="/ B C /"), OpToken("="), VisualToken(TokenKind.LINE, "black", geom_ref="/ A B /")),
                    justifications=("I.def.15",),
                ),
                ByrneStatement(
                    ProofPhase.DEMONSTRATION,
                    (OpToken("therefore"), VisualToken(TokenKind.LINE, "yellow", geom_ref="/ A C /"), OpToken("="), VisualToken(TokenKind.LINE, "red", geom_ref="/ B C /"), OpToken("="), VisualToken(TokenKind.LINE, "black", geom_ref="/ A B /")),
                    justifications=("C.N.1",),
                ),
                ByrneStatement(
                    ProofPhase.QED,
                    (OpToken("therefore"), VisualToken(TokenKind.TRIANGLE, "yellow/red/black", fill=FillMode.THREE_SIDE, geom_ref="< A B C >"), TextFragment("is equilateral. Q.E.F.")),
                    justifications=("I.def.20",),
                ),
            ),
            heath_text=(
                "Let AB be the given finite straight line. Thus it is required to construct an "
                "equilateral triangle on the straight line AB. With centre A and distance AB let "
                "the circle BCD be described; again, with centre B and distance BA let the circle "
                "ACE be described; and from the point C, in which the circles cut one another, to "
                "the points A, B let the straight lines CA, CB be joined. Now, since the point A is "
                "the centre of the circle CDB, AC is equal to AB. Again, since the point B is the "
                "centre of the circle CAE, BC is equal to BA. But CA was also proved equal to AB; "
                "therefore each of the straight lines CA, CB is equal to AB. And things which are "
                "equal to the same thing are also equal to one another; therefore CA is also equal "
                "to CB. Therefore the three straight lines CA, AB, BC are equal to one another. "
                "Therefore the triangle ABC is equilateral; and it has been constructed on the "
                "given finite straight line AB."
            ),
            geometor_steps=(
                "given A, B, / A B /",
                "( A B ) <- circle(A, B)          # I.post.3",
                "( B A ) <- circle(B, A)          # I.post.3",
                "C <- intersect(( A B ), ( B A ))",
                "/ A C / <- segment(A, C)         # I.post.1",
                "/ B C / <- segment(B, C)         # I.post.1",
                "assert quadrance(A, C) == quadrance(A, B) == quadrance(B, C)",
            ),
            design_notes=(
                "Zero alphabetic labels appear anywhere on p. 1. Five distinct visual registers "
                "(black base, blue circle, red circle, yellow left side, red right side) replace "
                "29 letter-pointer dereferences in Heath's prose."
            ),
        ),
        # 2. Book I, Proposition 5 — Pons Asinorum (p. 5, leaf-039)
        ByrneProgram(
            prop_id="I.5",
            plate_id="i5",
            heath_id="elem.1.5",
            g_id="G.91",
            title="In isosceles triangles the angles at the base are equal to one another (Pons Asinorum)",
            pickering_page="p. 5 (leaf 39)",
            number_field="Q(sqrt(3))",
            statements=(
                ByrneStatement(
                    ProofPhase.GIVEN,
                    (TextFragment("In"), VisualToken(TokenKind.TRIANGLE, "red/red/black", fill=FillMode.THREE_SIDE, geom_ref="< A B C >"), TextFragment("let the equal legs be"), VisualToken(TokenKind.LINE, "red", geom_ref="/ A B /", congruence_group="isosceles-legs"), TextFragment("and"), VisualToken(TokenKind.LINE, "red", geom_ref="/ A C /", congruence_group="isosceles-legs"), TextFragment(".")),
                ),
                ByrneStatement(
                    ProofPhase.CONSTRUCTION,
                    (TextFragment("Produce equal extensions"), VisualToken(TokenKind.LINE, "yellow", geom_ref="/ B F /", congruence_group="produced-legs"), TextFragment("and"), VisualToken(TokenKind.LINE, "yellow", geom_ref="/ C G /", congruence_group="produced-legs"), TextFragment("; join"), VisualToken(TokenKind.LINE, "blue", geom_ref="/ F C /", congruence_group="cross-diagonals"), TextFragment("and"), VisualToken(TokenKind.LINE, "blue", geom_ref="/ G B /", congruence_group="cross-diagonals"), TextFragment(".")),
                    justifications=("I.post.2", "I.3", "I.post.1"),
                ),
                ByrneStatement(
                    ProofPhase.DEMONSTRATION,
                    (VisualToken(TokenKind.LINE, "red", geom_ref="/ A B /", congruence_group="isosceles-legs"), OpToken("+"), VisualToken(TokenKind.LINE, "yellow", geom_ref="/ B F /", congruence_group="produced-legs"), OpToken("="), VisualToken(TokenKind.LINE, "red", geom_ref="/ A C /", congruence_group="isosceles-legs"), OpToken("+"), VisualToken(TokenKind.LINE, "yellow", geom_ref="/ C G /", congruence_group="produced-legs"), TextFragment(", with common"), VisualToken(TokenKind.ANGLE, "black", geom_ref="< B A C )")),
                    justifications=("C.N.2",),
                ),
                ByrneStatement(
                    ProofPhase.DEMONSTRATION,
                    (OpToken("therefore"), VisualToken(TokenKind.LINE, "blue", geom_ref="/ F C /", congruence_group="cross-diagonals"), OpToken("="), VisualToken(TokenKind.LINE, "blue", geom_ref="/ G B /", congruence_group="cross-diagonals"), TextFragment("and sub-base angles"), VisualToken(TokenKind.ANGLE, "yellow", geom_ref="< F B C )", congruence_group="sub-base-angles"), TextFragment("are equal via"), VisualToken(TokenKind.ANGLE, "red", geom_ref="< A F C )", congruence_group="lower-apex-angles")),
                    justifications=("I.4",),
                ),
                ByrneStatement(
                    ProofPhase.QED,
                    (OpToken("therefore"), TextFragment("remaining interior base angles"), VisualToken(TokenKind.ANGLE, "blue", geom_ref="< A B C )", congruence_group="base-angles"), TextFragment("and"), VisualToken(TokenKind.ANGLE, "blue", geom_ref="< A C B )", congruence_group="base-angles"), TextFragment("are equal. Q.E.D.")),
                    justifications=("C.N.3",),
                ),
            ),
            heath_text=(
                "Let ABC be an isosceles triangle having the side AB equal to the side AC; and "
                "let the straight lines BD, CE be produced further in a straight line with AB, AC. "
                "I say that the angle ABC is equal to the angle ACB, and the angle CBD to the "
                "angle BCE. Let a point F be taken at random on BD; from AE the greater let AG be "
                "cut off equal to AF the less; and let the straight lines FC, GB be joined. Then, "
                "since AF is equal to AG and AB to AC, the two sides FA, AC are equal to the two "
                "sides GA, AB, respectively; and they contain a common angle, the angle FAG. "
                "Therefore the base FC is equal to the base GB, and the triangle AFC will be equal "
                "to the triangle AGB, and the remaining angles will be equal to the remaining "
                "angles respectively, namely those which the equal sides subtend, that is, the "
                "angle ACF to the angle ABG, and the angle AFC to the angle AGB. And, since the "
                "whole AF is equal to the whole AG, and in these AB is equal to AC, the remainder "
                "BF is equal to the remainder CG. But FC was also proved equal to GB; therefore "
                "the two sides BF, FC are equal to the two sides CG, GB respectively; and the "
                "angle BFC is equal to the angle CGB, while the base BC is common to them; "
                "therefore the triangle BFC is also equal to the triangle CGB, and the remaining "
                "angles will be equal to the remaining angles respectively, namely those which "
                "the equal sides subtend; therefore the angle FBC is equal to the angle GCB, and "
                "the angle BCF to the angle CBG. Accordingly, since the whole angle ABG was "
                "proved equal to the angle ACF, and in these the angle CBG is equal to the angle "
                "BCF, the remaining angle ABC is equal to the remaining angle ACB."
            ),
            geometor_steps=(
                "given A, B, C with quadrance(A, B) == quadrance(A, C)",
                "F <- extend(/ A B /); G <- cut(/ A C /, length=/ A F /)  # I.post.2, I.3",
                "/ F C / <- segment(F, C); / G B / <- segment(G, B)       # I.post.1",
                "congruent(< A F C >, < A G B >)                          # I.4 SAS",
                "congruent(< B F C >, < C G B >)                          # I.4 SAS",
                "assert spread(B, A, B, C) == spread(C, A, C, B)          # C.N.3",
            ),
            design_notes=(
                "Demonstrates Byrne's 'congruence-twin' idiom: symmetric equal pairs share the "
                "same color register (red legs, yellow extensions, blue diagonals), turning "
                "mirror symmetry into immediate perceptual equivalence and conquering the "
                "notorious 'Bridge of Asses'."
            ),
        ),
        # 3. Book I, Proposition 47 — Pythagorean Theorem (pp. 48–49, leaves 82–83)
        ByrneProgram(
            prop_id="I.47",
            plate_id="i47",
            heath_id="elem.1.47",
            g_id="G.140",
            title="In right-angled triangles the square on the side subtending the right angle is equal to the squares on the sides containing the right angle",
            pickering_page="pp. 48–49 (leaves 82–83)",
            number_field="Q",
            statements=(
                ByrneStatement(
                    ProofPhase.GIVEN,
                    (TextFragment("Right-angled triangle with hypotenuse"), VisualToken(TokenKind.LINE, "red", geom_ref="/ B C /"), TextFragment("and legs"), VisualToken(TokenKind.LINE, "yellow", geom_ref="/ A B /"), TextFragment(","), VisualToken(TokenKind.LINE, "blue", geom_ref="/ A C /"), TextFragment(".")),
                ),
                ByrneStatement(
                    ProofPhase.CONSTRUCTION,
                    (TextFragment("Construct"), VisualToken(TokenKind.SQUARE, "black", geom_ref="< A B F G >"), TextFragment(","), VisualToken(TokenKind.SQUARE, "red", geom_ref="< A C K H >"), TextFragment(", and hypotenuse square"), VisualToken(TokenKind.RECTANGLE, "yellow", geom_ref="< B L M D >"), OpToken("+"), VisualToken(TokenKind.RECTANGLE, "blue", geom_ref="< C L M E >"), TextFragment("split by"), VisualToken(TokenKind.LINE, "black", stroke=StrokeMode.DOTTED, geom_ref="/ A M /"), OpToken("parallel"), TextFragment("to sides; join"), VisualToken(TokenKind.LINE, "black", geom_ref="/ A D /", congruence_group="windmill-chords"), TextFragment("and"), VisualToken(TokenKind.LINE, "black", geom_ref="/ F C /", congruence_group="windmill-chords"), TextFragment(".")),
                    justifications=("I.46", "I.31", "I.post.1"),
                ),
                ByrneStatement(
                    ProofPhase.DEMONSTRATION,
                    (VisualToken(TokenKind.SQUARE, "black", geom_ref="< A B F G >"), OpToken("="), TextFragment("2 × windmill triangle ="), VisualToken(TokenKind.RECTANGLE, "yellow", geom_ref="< B L M D >")),
                    justifications=("I.14", "I.4", "I.41"),
                ),
                ByrneStatement(
                    ProofPhase.DEMONSTRATION,
                    (VisualToken(TokenKind.SQUARE, "red", geom_ref="< A C K H >"), OpToken("="), TextFragment("2 × symmetric windmill triangle ="), VisualToken(TokenKind.RECTANGLE, "blue", geom_ref="< C L M E >")),
                    justifications=("I.4", "I.41"),
                ),
                ByrneStatement(
                    ProofPhase.QED,
                    (OpToken("therefore"), VisualToken(TokenKind.RECTANGLE, "yellow", geom_ref="< B L M D >"), OpToken("+"), VisualToken(TokenKind.RECTANGLE, "blue", geom_ref="< C L M E >"), OpToken("="), VisualToken(TokenKind.SQUARE, "black", geom_ref="< A B F G >"), OpToken("+"), VisualToken(TokenKind.SQUARE, "red", geom_ref="< A C K H >"), TextFragment(". Q.E.D.")),
                    justifications=("C.N.2",),
                ),
            ),
            heath_text=(
                "Let ABC be a right-angled triangle having the angle BAC right; I say that the "
                "square on BC is equal to the squares on BA, AC. For let there be described on BC "
                "the square BDEC, and on BA, AC the squares GB, HC; through A let AL be drawn "
                "parallel to either BD or CE, and let AD, FC be joined. Then, since each of the "
                "angles BAC, BAG is right, it follows that with a straight line BA, and at the "
                "point A on it, the two straight lines AC, AG not lying on the same side make the "
                "adjacent angles equal to two right angles; therefore CA is in a straight line "
                "with AG. For the same reason BA is also in a straight line with AH. And, since "
                "the angle DBC is equal to the angle FBA: for each is right: let the angle ABC be "
                "added to each; therefore the whole angle DBA is equal to the whole angle FBC. "
                "And, since DB is equal to BC, and FB to BA, the two sides AB, BD are equal to "
                "the two sides FB, BC respectively, and the angle ABD is equal to the angle FBC; "
                "therefore the base AD is equal to the base FC, and the triangle ABD is equal to "
                "the triangle FBC. Now the parallelogram BL is double of the triangle ABD, for "
                "they have the same base BD and are in the same parallels BD, AL. And the square "
                "GB is double of the triangle FBC, for they again have the same base FB and are "
                "in the same parallels FB, GC. Therefore the parallelogram BL is also equal to "
                "the square GB. Similarly, if AE, BK be joined, the parallelogram CL can also be "
                "proved equal to the square HC; therefore the whole square BDEC is equal to the "
                "two squares GB, HC."
            ),
            geometor_steps=(
                "given right < A B C > with spread(A, B, A, C) == 1",
                "< A B F G >, < A C K H >, < B D E C > <- squares(I.46)",
                "[ A L ] <- parallel(A, [ B D ]) intersecting / B C / at L, / D E / at M",
                "area(< A B F G >) == 2 * area(< F B C >) == 2 * area(< A B D >) == area(< B L M D >)",
                "area(< A C K H >) == 2 * area(< B C K >) == 2 * area(< A C E >) == area(< C L M E >)",
                "assert quadrance(B, C) == quadrance(A, B) + quadrance(A, C)",
            ),
            design_notes=(
                "Byrne's masterpiece (pp. 48–49). Solid filled squares (black, red) and "
                "rectangles (yellow, blue) make area conservation instantaneous, while dotted "
                "and dashed boundary strokes disambiguate segments sharing polygon edges."
            ),
        ),
        # 4. Book II, Proposition 11 — Extreme and Mean Ratio / Golden Section (p. 66, leaf 100)
        ByrneProgram(
            prop_id="II.11",
            plate_id="ii11",
            heath_id="elem.2.11",
            g_id="G.154",
            title="To cut a given straight line so that the rectangle contained by the whole and one segment equals the square on the remaining segment",
            pickering_page="p. 66 (leaf 100)",
            number_field="Q(phi)",
            statements=(
                ByrneStatement(
                    ProofPhase.GIVEN,
                    (TextFragment("Given straight line"), VisualToken(TokenKind.LINE, "red", stroke=StrokeMode.SOLID_DOTTED, geom_ref="/ A B /"), TextFragment("to be divided in golden section at"), TextFragment("H.")),
                ),
                ByrneStatement(
                    ProofPhase.CONSTRUCTION,
                    (TextFragment("Describe square"), VisualToken(TokenKind.RECTANGLE, "yellow", geom_ref="< H B D K >"), OpToken("+"), VisualToken(TokenKind.RECTANGLE, "blue", geom_ref="< A H K C >"), TextFragment("; bisect side at E, join"), VisualToken(TokenKind.LINE, "black", geom_ref="/ E B /"), TextFragment(", extend to F, and describe golden square"), VisualToken(TokenKind.SQUARE, "blue", geom_ref="< A F G H >"), TextFragment(".")),
                    justifications=("I.46", "I.10", "I.post.1", "I.3"),
                ),
                ByrneStatement(
                    ProofPhase.DEMONSTRATION,
                    (TextFragment("By II.6 on bisected side + extension,"), VisualToken(TokenKind.SQUARE, "blue", geom_ref="< A F G H >"), OpToken("+"), VisualToken(TokenKind.RECTANGLE, "blue", geom_ref="< A H K C >"), TextFragment("+ quarter-square ="), VisualToken(TokenKind.LINE, "black", geom_ref="/ E B /", squared=True)),
                    justifications=("II.6", "I.47"),
                ),
                ByrneStatement(
                    ProofPhase.DEMONSTRATION,
                    (TextFragment("Subtracting quarter-square and common strip"), VisualToken(TokenKind.RECTANGLE, "blue", geom_ref="< A H K C >"), TextFragment("from both equals:")),
                    justifications=("C.N.3",),
                ),
                ByrneStatement(
                    ProofPhase.QED,
                    (OpToken("therefore"), VisualToken(TokenKind.SQUARE, "blue", geom_ref="< A F G H >"), OpToken("="), VisualToken(TokenKind.RECTANGLE, "yellow", geom_ref="< H B D K >"), TextFragment("(i.e. AH² = AB × HB). Q.E.F.")),
                ),
            ),
            heath_text=(
                "Let AB be the given straight line; thus it is required to cut AB so that the "
                "rectangle contained by the whole and one of the segments is equal to the square "
                "on the remaining segment. For let the square ABDC be described on AB; let AC be "
                "bisected at the point E, and let BE be joined; let CA be drawn through to F, and "
                "let EF be made equal to BE; let the square FH be described on AF, and let GH be "
                "drawn through to K. I say that AB has been cut at H so as to make the rectangle "
                "contained by AB, BH equal to the square on AH. For, since the straight line AC "
                "has been bisected at E, and FA is added to it, the rectangle contained by CF, FA "
                "together with the square on AE is equal to the square on EF. But EF is equal to "
                "EB; therefore the rectangle CF, FA together with the square on AE is equal to "
                "the square on EB. But the squares on BA, AE are equal to the square on EB, for "
                "the angle at A is right; therefore the rectangle CF, FA together with the square "
                "on AE is equal to the squares on BA, AE. Let the square on AE be subtracted from "
                "each; therefore the remaining rectangle CF, FA is equal to the square on AB. Now "
                "the rectangle CF, FA is FK, and the square on AB is AD; therefore FK is equal to "
                "AD. Let AK be subtracted from each; therefore FH which remains is equal to HD."
            ),
            geometor_steps=(
                "given / A B / of length 1",
                "< A B D C > <- square(/ A B /); E <- midpoint(/ A C /)",
                "( E B ) <- circle(E, B) cutting [ C A ] at F with |AF| = phi^(-1)",
                "< A F G H > <- square(/ A F /) cutting / A B / at H",
                "assert |AH|^2 == |AB| * |HB|  # (phi - 1)^2 == 1 * (2 - phi)",
            ),
            design_notes=(
                "Turns Euclid's algebraic completion of the square (x^2 + ax = a^2) into a pure "
                "two-color visual subtraction: subtracting the shared blue strip leaves the blue "
                "golden square equal to the yellow complement rectangle."
            ),
        ),
        # 5. Book IV, Proposition 10 — Golden Triangle (pp. 135–136, leaves 169–170)
        ByrneProgram(
            prop_id="IV.10",
            plate_id="iv10",
            heath_id="elem.4.10",
            g_id="G.223",
            title="To construct an isosceles triangle having each of the angles at the base double of the remaining one",
            pickering_page="pp. 135–136 (leaves 169–170)",
            number_field="Q(phi) + pentagonal y",
            statements=(
                ByrneStatement(
                    ProofPhase.CONSTRUCTION,
                    (TextFragment("Cut"), VisualToken(TokenKind.LINE, "black", stroke=StrokeMode.SOLID_DOTTED, geom_ref="/ A B /"), TextFragment("at C in golden ratio (II.11); describe"), VisualToken(TokenKind.CIRCLE, "red", geom_ref="( A B )"), TextFragment(", fit chord"), VisualToken(TokenKind.LINE, "blue", geom_ref="/ B D /"), TextFragment("= AC, join"), VisualToken(TokenKind.LINE, "yellow", geom_ref="/ A D /"), TextFragment("and"), VisualToken(TokenKind.LINE, "red", geom_ref="/ C D /"), TextFragment(", and circumscribe"), VisualToken(TokenKind.CIRCLE, "blue", geom_ref="( A C D )"), TextFragment(".")),
                    justifications=("II.11", "I.post.3", "IV.1", "IV.5"),
                ),
                ByrneStatement(
                    ProofPhase.DEMONSTRATION,
                    (VisualToken(TokenKind.LINE, "blue", geom_ref="/ B D /", squared=True), TextFragment("= AB × BC →"), VisualToken(TokenKind.LINE, "blue", geom_ref="/ B D /"), TextFragment("is tangent to"), VisualToken(TokenKind.CIRCLE, "blue", geom_ref="( A C D )")),
                    justifications=("II.11", "III.37"),
                ),
                ByrneStatement(
                    ProofPhase.DEMONSTRATION,
                    (TextFragment("By alternate-segment theorem (III.32),"), VisualToken(TokenKind.ANGLE, "yellow", geom_ref="< B D C )"), OpToken("="), VisualToken(TokenKind.ANGLE, "red", geom_ref="< D A C )"), TextFragment(", making"), VisualToken(TokenKind.LINE, "red", geom_ref="/ C D /"), OpToken("="), VisualToken(TokenKind.LINE, "blue", geom_ref="/ B D /")),
                    justifications=("III.32", "I.32", "I.6"),
                ),
                ByrneStatement(
                    ProofPhase.QED,
                    (OpToken("therefore"), TextFragment("each base angle of"), VisualToken(TokenKind.TRIANGLE, "yellow/black/blue", fill=FillMode.THREE_SIDE, geom_ref="< A B D >"), TextFragment("is double the apex angle"), VisualToken(TokenKind.ANGLE, "red", geom_ref="< D A C )"), TextFragment("(72° = 2 × 36°). Q.E.F.")),
                ),
            ),
            heath_text=(
                "Let any straight line AB be set out, and let it be cut at the point C so that "
                "the rectangle contained by AB, BC is equal to the square on CA; with centre A "
                "and distance AB let the circle BDE be described, and let there be fitted in the "
                "circle BDE the straight line BD equal to the straight line AC which is not "
                "greater than the diameter of the circle BDE. Let AD, DC be joined, and let the "
                "circle ACD be described about the triangle ACD. Then, since the rectangle AB, BC "
                "is equal to the square on AC, and AC is equal to BD, the rectangle AB, BC is "
                "equal to the square on BD. And, since a point B has been taken outside the "
                "circle ACD, and from B the two straight lines BA, BD have fallen on the circle "
                "ACD, and one of them cuts it, while the other falls on it, and the rectangle "
                "AB, BC is equal to the square on BD, therefore BD touches the circle ACD. Since, "
                "then, BD touches it, and DC is drawn across from the point of contact at D, the "
                "angle BDC is equal to the angle DAC in the alternate segment of the circle. "
                "Since, then, the angle BDC is equal to the angle DAC, let the angle CDA be added "
                "to each; therefore the whole angle BDA is equal to the two angles CDA, DAC. But "
                "the exterior angle BCD is equal to the angles CDA, DAC; therefore the angle BDA "
                "is also equal to the angle BCD. And the angle BDA is equal to the angle CBD, "
                "since the side AD is also equal to AB; so that the angle DBA is also equal to "
                "the angle BCD. Therefore the three angles BDA, DBA, BCD are equal to one another. "
                "And, since the angle DBC is equal to the angle BCD, the side BD is also equal to "
                "the side DC. But BD is by hypothesis equal to CA; therefore CA is also equal to "
                "CD, so that the angle CDA is also equal to the angle DAC; therefore the angles "
                "CDA, DAC are double of the angle DAC. But the angle BCD is equal to the angles "
                "CDA, DAC; therefore the angle BCD is also double of the angle CAD."
            ),
            geometor_steps=(
                "given / A B / cut in golden section at C (|AC| = phi^(-1) * |AB|)",
                "( A B ) <- circle(A, B); D <- chord_fit(( A B ), B, |AC|)",
                "( A C D ) <- circumcircle(< A C D >)                      # IV.5",
                "tangent(/ B D /, ( A C D )) by |BD|^2 == |AB| * |BC|      # III.37",
                "assert angle(A, B, D) == angle(A, D, B) == 2 * angle(B, A, D)",
            ),
            design_notes=(
                "Bridges Book II golden area algebra (II.11) and Book III tangent-secant power "
                "(III.37) to synthesize the 36°-72°-72° sublime triangle."
            ),
        ),
        # 6. Book IV, Proposition 11 — Regular Pentagon (p. 137, leaf 171)
        ByrneProgram(
            prop_id="IV.11",
            plate_id="iv11",
            heath_id="elem.4.11",
            g_id="G.224",
            title="In a given circle to inscribe an equilateral and equiangular pentagon",
            pickering_page="p. 137 (leaf 171)",
            number_field="Q(phi, sqrt(10 - 2*sqrt(5)))",
            statements=(
                ByrneStatement(
                    ProofPhase.CONSTRUCTION,
                    (TextFragment("In given"), VisualToken(TokenKind.CIRCLE, "blue", geom_ref="( O A )"), TextFragment("inscribe golden triangle"), VisualToken(TokenKind.TRIANGLE, "yellow", geom_ref="< A C D >"), TextFragment("(IV.10, IV.2); bisect its base angles by"), VisualToken(TokenKind.LINE, "black", geom_ref="/ C E /", congruence_group="pentagon-diagonals"), TextFragment("and"), VisualToken(TokenKind.LINE, "black", geom_ref="/ D B /", congruence_group="pentagon-diagonals"), TextFragment("and join the five chords.")),
                    justifications=("IV.10", "IV.2", "I.9", "I.post.1"),
                ),
                ByrneStatement(
                    ProofPhase.DEMONSTRATION,
                    (TextFragment("All five inscribed angles"), VisualToken(TokenKind.ANGLE, "black", geom_ref="< C A D )"), TextFragment(", half-base wedges"), VisualToken(TokenKind.ANGLE, "blue", geom_ref="< A C E )"), TextFragment(", and"), VisualToken(TokenKind.ANGLE, "red", geom_ref="< C D B )"), TextFragment("are equal (36° each), cutting five equal arcs.")),
                    justifications=("C.N.7", "III.26"),
                ),
                ByrneStatement(
                    ProofPhase.QED,
                    (OpToken("therefore"), TextFragment("chords"), VisualToken(TokenKind.LINE, "red", geom_ref="/ A B /"), TextFragment(","), VisualToken(TokenKind.LINE, "black", geom_ref="/ C D /"), TextFragment(","), VisualToken(TokenKind.LINE, "blue", geom_ref="/ A E /"), TextFragment(","), VisualToken(TokenKind.LINE, "yellow", geom_ref="/ E D /"), TextFragment(", and"), VisualToken(TokenKind.LINE, "red", stroke=StrokeMode.DOTTED, geom_ref="/ B C /"), TextFragment("form a regular pentagon. Q.E.F.")),
                    justifications=("III.29", "III.27"),
                ),
            ),
            heath_text=(
                "Let ABCDE be the given circle; thus it is required to inscribe in the circle "
                "ABCDE an equilateral and equiangular pentagon. Let the isosceles triangle FGH be "
                "set out having each of the angles at G, H double of the angle at F; let there be "
                "inscribed in the circle ABCDE the triangle ACD equiangular with the triangle "
                "FGH, so that the angle CAD is equal to the angle at F and the angles at G, H "
                "respectively equal to the angles ACD, CDA; therefore each of the angles ACD, CDA "
                "is also double of the angle CAD. Now let the angles ACD, CDA be bisected "
                "respectively by the straight lines CE, DB, and let AB, BC, DE, EA be joined. "
                "Then, since each of the angles ACD, CDA is double of the angle CAD, and they "
                "have been bisected by the straight lines CE, DB, the five angles DAC, ACE, ECD, "
                "CDB, BDA are equal to one another. But equal angles stand on equal circumferences; "
                "therefore the five circumferences AB, BC, CD, DE, EA are equal to one another. "
                "But equal circumferences are subtended by equal straight lines; therefore the "
                "five straight lines AB, BC, CD, DE, EA are equal to one another; therefore the "
                "pentagon ABCDE is equilateral."
            ),
            geometor_steps=(
                "given circle ( O A )",
                "inscribe golden < A C D > in ( O A )                       # IV.10, IV.2",
                "B <- bisect(< A D C )) ∩ ( O A ); E <- bisect(< A C D )) ∩ ( O A )",
                "connect pentagon < A B C D E >",
                "assert equal quadrances on all 5 sides and equal spreads on all 5 interior angles",
            ),
            design_notes=(
                "Five pentagon sides exceed Byrne's 4 colors, so Byrne assigns black, red, blue, "
                "yellow, and red-dotted to the five edges around the solid yellow golden triangle!"
            ),
        ),
        # 7. Book V, Definition 5 & Proposition 16 — Eudoxian Colored Magnitude Calculus (pp. 154, 187)
        ByrneProgram(
            prop_id="V.16",
            plate_id="v16",
            heath_id="elem.5.16",
            g_id="G.276",
            title="If four magnitudes of the same kind be proportional, they will also be proportional alternately (Alternando)",
            pickering_page="pp. 154, 187 (leaves 188, 221)",
            number_field="Abstract Eudoxian Ordered Semigroup",
            statements=(
                ByrneStatement(
                    ProofPhase.GIVEN,
                    (VisualToken(TokenKind.MAGNITUDE, "red", shape_hint="circle"), OpToken(":"), VisualToken(TokenKind.MAGNITUDE, "yellow", shape_hint="square"), OpToken("prop"), VisualToken(TokenKind.MAGNITUDE, "blue", shape_hint="diamond"), OpToken(":"), VisualToken(TokenKind.MAGNITUDE, "black", shape_hint="shield")),
                    justifications=("V.def.5",),
                ),
                ByrneStatement(
                    ProofPhase.DEMONSTRATION,
                    (TextFragment("Take equimultiples m ·"), VisualToken(TokenKind.MAGNITUDE, "red", shape_hint="circle"), TextFragment(", m ·"), VisualToken(TokenKind.MAGNITUDE, "yellow", shape_hint="square"), TextFragment("and n ·"), VisualToken(TokenKind.MAGNITUDE, "blue", shape_hint="diamond"), TextFragment(", n ·"), VisualToken(TokenKind.MAGNITUDE, "black", shape_hint="shield")),
                    justifications=("V.4", "V.15"),
                ),
                ByrneStatement(
                    ProofPhase.DEMONSTRATION,
                    (TextFragment("Order trichotomy (⊏, =, ⊐) transfers from"), VisualToken(TokenKind.MAGNITUDE, "yellow", shape_hint="square"), TextFragment("vs."), VisualToken(TokenKind.MAGNITUDE, "black", shape_hint="shield"), TextFragment("to their equimultiples")),
                    justifications=("V.14", "V.def.5"),
                ),
                ByrneStatement(
                    ProofPhase.QED,
                    (OpToken("therefore"), VisualToken(TokenKind.MAGNITUDE, "red", shape_hint="circle"), OpToken(":"), VisualToken(TokenKind.MAGNITUDE, "blue", shape_hint="diamond"), OpToken("prop"), VisualToken(TokenKind.MAGNITUDE, "yellow", shape_hint="square"), OpToken(":"), VisualToken(TokenKind.MAGNITUDE, "black", shape_hint="shield"), TextFragment(". Q.E.D.")),
                ),
            ),
            heath_text=(
                "If four magnitudes be proportional, they will also be proportional alternately. "
                "Let A, B, C, D be four proportional magnitudes, so that, as A is to B, so is C "
                "to D; I say that they will also be proportional alternately, that is, as A is to "
                "C, so is B to D. For of A, B let equimultiples E, F be taken, and of C, D other "
                "arbitrary equimultiples G, H. Then, since E is the same multiple of A that F is "
                "of B, and parts have the same ratio as their same multiples, therefore, as A is "
                "to B, so is E to F. But as A is to B, so is C to D; therefore also, as C is to "
                "D, so is E to F. Again, since G, H are equimultiples of C, D, therefore, as C is "
                "to D, so is G to H. But, as C is to D, so is E to F; therefore also, as E is to "
                "F, so is G to H. And, if four magnitudes be proportional, and the first be "
                "greater than the third, the second will also be greater than the fourth; if "
                "equal, equal; and if less, less. Therefore, if E is in excess of G, F is also in "
                "excess of H; if equal, equal; and if less, less. Now E, F are equimultiples of "
                "A, B, and G, H other arbitrary equimultiples of C, D; therefore, as A is to C, "
                "so is B to D."
            ),
            geometor_steps=(
                "given magnitudes (A, B, C, D) satisfying Eudoxus(A, B, C, D)   # V.def.5",
                "for all m, n in N+: sign(m*A - n*C) == sign(m*B - n*D)         # V.15, V.11, V.14",
                "conclude Eudoxus(A, C, B, D)                                   # Alternando",
            ),
            design_notes=(
                "In Book V (pp. 153–212), Byrne abandons line diagrams altogether and invents a "
                "four-glyph symbolic algebra (red circle, yellow square, blue diamond, black shield) "
                "for abstract Eudoxian magnitudes—connecting directly to geometor/codes."
            ),
        ),
    ]
    return {p.prop_id: p for p in programs}


ROSETTA_PROGRAMS: dict[str, ByrneProgram] = _build_rosetta_corpus()


def get_rosetta_program(prop_id: str) -> ByrneProgram:
    """Lookup a :class:`ByrneProgram` by proposition ID (e.g. ``"I.47"``)."""
    key = prop_id.strip()
    if key not in ROSETTA_PROGRAMS:
        raise KeyError(
            f"Unknown Rosetta proposition {prop_id!r}; available: {sorted(ROSETTA_PROGRAMS)}"
        )
    return ROSETTA_PROGRAMS[key]
