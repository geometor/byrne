"""Comprehensive test suite for ``geometor.byrne``."""

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import sympy as sp

from geometor.byrne import (
    BYRNE_COLORS,
    PHI,
    PLATE_REGISTRY,
    ROSETTA_PROGRAMS,
    TABLEAU_IDS,
    __version__,
    build_all_plates,
    build_plate,
    compute_rosetta_metrics,
    get_color_spec,
    get_rosetta_program,
    list_plate_ids,
    render_plate_svg,
    render_tableau_svg,
)
from geometor.byrne.__main__ import main as cli_main
from geometor.byrne.palette import byrne_css_variables, stroke_dasharray
from geometor.byrne.pseudocode import analyze_visual_registers, count_alphabetic_dereferences
from geometor.byrne.sphinx_ext import (
    BYRNE_ROLE_NAMES,
    parse_byrne_role_spec,
    render_byrne_glyph_html,
    render_byrne_operator_html,
)

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_version_and_palette() -> None:
    assert __version__ == "0.2.1"
    assert set(BYRNE_COLORS.keys()) == {"red", "blue", "yellow", "black"}
    assert get_color_spec("RED").name == "red"
    assert get_color_spec("ink").name == "black"
    with pytest.raises(ValueError, match="Unknown Byrne color"):
        get_color_spec("magenta")
    assert stroke_dasharray("solid") == ""
    assert stroke_dasharray("dashed") != ""
    assert stroke_dasharray("dotted") != ""
    assert "--byrne-red" in byrne_css_variables()


def test_parse_byrne_role_spec_nested_brackets() -> None:
    spec, target = parse_byrne_role_spec("black filled <i47:< A B F G >>")
    assert spec == "black filled"
    assert target == "i47:< A B F G >"

    spec2, target2 = parse_byrne_role_spec("blue <i5:< C B A )>")
    assert spec2 == "blue"
    assert target2 == "i5:< C B A )"

    spec3, target3 = parse_byrne_role_spec("red solid-dotted")
    assert spec3 == "red solid-dotted"
    assert target3 == ""


@pytest.mark.parametrize(
    ("role_name", "body", "expected_substr"),
    [
        ("byrne-line", "red solid <i47:/ B C />", 'data-byrne-kind="line"'),
        ("byrne-line", "red solid-dotted squared", "byrne-token-sup"),
        ("byrne-angle", "yellow+black <iii31:< B A C )>", 'data-byrne-color="yellow+black"'),
        ("byrne-tri", "red/blue/black <i4:< A B C >>", 'data-byrne-color="red/blue/black"'),
        ("byrne-tri", "yellow filled <iv11:< A C D >>", "byrne-glyph-tri"),
        ("byrne-sq", "black filled <i47:< A B F G >>", "byrne-glyph-sq"),
        ("byrne-sq", "blue half <ii4:< D K G H >>", "half-filled square"),
        ("byrne-rect", "yellow filled <i47:< B L M D >>", "byrne-glyph-rect"),
        ("byrne-arc", "blue dotted", "byrne-glyph-arc"),
        ("byrne-circle", "blue <i1:( A B )>", "byrne-glyph-circle"),
        ("byrne-mag", "red circle", "Book V Vermilion Red circle magnitude"),
        ("byrne-mag", "black shield", "shield"),
        ("byrne-op", "two-right-angles", "two right angles"),
        ("byrne-op", "right-angle", "one right angle"),
        ("byrne-op", "gt", "⊏"),
        ("byrne-op", "lt", "⊐"),
    ],
)
def test_inline_byrne_glyph_rendering(
    role_name: str, body: str, expected_substr: str
) -> None:
    assert role_name in BYRNE_ROLE_NAMES
    rendered = render_byrne_glyph_html(role_name, body)
    assert expected_substr in rendered
    if role_name != "byrne-op":
        assert "<svg" in rendered
        assert 'class="byrne-token geom-ref"' in rendered


def test_operator_aliases() -> None:
    assert "∴" in render_byrne_operator_html("therefore")
    assert "∵" in render_byrne_operator_html("because")
    assert "∥" in render_byrne_operator_html("parallel")
    assert "⊥" in render_byrne_operator_html("perp")
    assert "∷" in render_byrne_operator_html("prop")


def test_static_css_and_js_assets_exist() -> None:
    static_dir = REPO_ROOT / "src" / "geometor" / "byrne" / "static"
    css_text = (static_dir / "byrne.css").read_text(encoding="utf-8")
    js_text = (static_dir / "byrne_interactive.js").read_text(encoding="utf-8")
    assert "svg.euclid-graphic" in css_text
    assert ".byrne-token" in css_text
    assert "initByrneInteractive" in js_text


def test_rosetta_programs_and_register_diagnostics() -> None:
    expected_props = {"I.1", "I.5", "I.47", "II.11", "IV.10", "IV.11", "V.16"}
    assert set(ROSETTA_PROGRAMS.keys()) == expected_props

    for prop_id in expected_props:
        prog = get_rosetta_program(prop_id)
        metrics = compute_rosetta_metrics(prog)
        diag = analyze_visual_registers(prog)

        assert metrics.heath_words > 150
        assert metrics.heath_pointer_dereferences >= 15
        assert metrics.byrne_pointer_dereferences == 0
        assert metrics.word_compression_ratio < 0.25
        assert metrics.byrne_visual_tokens >= 10
        assert diag.is_unambiguous, f"Unexpected collision in {prop_id}: {diag.ambiguous_collisions}"

        for st in prog.statements:
            rst_line = st.to_rst(prog.plate_id)
            compact_line = st.to_compact()
            assert rst_line
            assert compact_line

    # Verify intentional congruence-twin detection on Pons Asinorum (I.5)
    i5_diag = analyze_visual_registers(get_rosetta_program("I.5"))
    assert len(i5_diag.intentional_congruence_twins) >= 3

    # Verify stroke-modulation detection on I.47 and IV.11
    assert analyze_visual_registers(get_rosetta_program("I.47")).uses_stroke_modulation
    assert analyze_visual_registers(get_rosetta_program("IV.11")).uses_stroke_modulation
    assert count_alphabetic_dereferences("Let AB equal AC in triangle ABC at point A.") >= 4


def test_all_17_symbolic_constructions_exact_and_svg_valid() -> None:
    assert len(PLATE_REGISTRY) == 17
    assert sp.simplify(PHI**2 - PHI - 1) == 0

    plates = build_all_plates()
    assert len(plates) == 17

    for plate in plates:
        # 1. Zero sp.Float atoms anywhere in Model points
        for pt in plate.model.points:
            assert not pt.x.atoms(sp.Float), f"Float found in {plate.prop_id} {pt}.x"
            assert not pt.y.atoms(sp.Float), f"Float found in {plate.prop_id} {pt}.y"

        # 2. All symbolic Rational Trigonometry / area proof checks hold identically
        assert plate.proof_checks, f"Missing proof_checks in {plate.prop_id}"
        for check_name, passed in plate.proof_checks.items():
            assert passed, f"Failed {check_name} in {plate.prop_id}"

        # 3. Rendered SVG conforms to .euclid-graphic XML & midpoint-path contract
        svg_str = render_plate_svg(plate)
        assert 'class="euclid-graphic"' in svg_str
        assert f'data-graphic-id="{plate.slug}"' in svg_str
        assert 'id="geom-tick-1"' in svg_str

        root = ET.fromstring(svg_str)
        ns = {"svg": "http://www.w3.org/2000/svg"}
        groups = {g.attrib.get("id") for g in root.findall(".//svg:g", ns) if "id" in g.attrib}
        assert {"elements", "graphics", "highlights", "points", "labels"}.issubset(groups)

        for seg_path in root.findall(".//svg:path[@data-byrne-kind='line']", ns):
            d_attr = seg_path.attrib["d"]
            # Must be a 3-vertex path: M x1 y1 L mx my L x2 y2
            assert d_attr.count(" L ") == 2, f"Non-3-vertex path in {plate.prop_id}: {d_attr}"
            assert seg_path.attrib.get("data-byrne-color") in BYRNE_COLORS
            assert seg_path.attrib.get("data-ref", "").startswith("/")


def test_tableaux_svgs_valid() -> None:
    assert len(TABLEAU_IDS) == 7
    for tid in TABLEAU_IDS:
        svg_str = render_tableau_svg(tid)
        assert 'class="euclid-graphic"' in svg_str
        assert f'data-graphic-id="{tid}"' in svg_str
        ET.fromstring(svg_str)


def test_apparatus_json_and_rst_anchor_integrity() -> None:
    res_dir = REPO_ROOT / "resources" / "pickering_1847"
    for fname in (
        "sources_manifest.json",
        "concordance.json",
        "persons.json",
        "citations.json",
        "glossary.json",
        "structure_map.json",
    ):
        fpath = res_dir / fname
        assert fpath.is_file(), f"Missing {fname}"
        data = json.loads(fpath.read_text(encoding="utf-8"))
        assert data

    persons = json.loads((res_dir / "persons.json").read_text(encoding="utf-8"))
    citations = json.loads((res_dir / "citations.json").read_text(encoding="utf-8"))
    glossary = json.loads((res_dir / "glossary.json").read_text(encoding="utf-8"))

    assert "rougeux" in persons
    assert "tufte" in persons
    assert "rougeux:2018" in citations
    assert "rougeux:2018-making" in citations

    codex_dir = REPO_ROOT / "docsrc" / "coloured_euclid"
    persons_rst = "\n".join(p.read_text(encoding="utf-8") for p in sorted((codex_dir / "people").glob("*.rst")))
    bib_rst = (codex_dir / "bibliography.rst").read_text(encoding="utf-8")
    gloss_rst = (codex_dir / "glossary.rst").read_text(encoding="utf-8")

    def _slug(key: str) -> str:
        return re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")

    for p_key in persons:
        assert f".. _person-{_slug(p_key)}:" in persons_rst
    for c_key in citations:
        assert f".. _cite-{_slug(c_key)}:" in bib_rst
    for t_key in glossary:
        assert f".. _term-{_slug(t_key)}:" in gloss_rst


def test_cli_commands(tmp_path: Path) -> None:
    assert list_plate_ids()[0] == "I.1"
    assert build_plate("I.47").slug == "i47"
    assert cli_main(["list"]) == 0
    assert cli_main(["rosetta"]) == 0
    assert cli_main(["render", "-p", "I.47", "-o", str(tmp_path), "--labels"]) == 0
    assert (tmp_path / "i47.svg").is_file()


def test_separate_book_and_proposition_pages() -> None:
    res_dir = REPO_ROOT / "resources" / "pickering_1847"
    codex_dir = REPO_ROOT / "docsrc" / "coloured_euclid"
    structure = json.loads((res_dir / "structure_map.json").read_text(encoding="utf-8"))
    folio_map = json.loads((res_dir / "folio_map.json").read_text(encoding="utf-8"))

    assert ".. collection::" in (codex_dir / "index.rst").read_text(encoding="utf-8")

    # Legacy multi-proposition unit folders must not exist
    for legacy_slug in (
        "unit-1-foundations",
        "unit-2-book-i",
        "unit-3-book-ii",
        "unit-4-books-iii-iv",
        "unit-5-book-v",
        "unit-6-book-vi",
        "unit-7-visual-pseudocode",
    ):
        assert not (codex_dir / legacy_slug).exists()

    prop_count = 0
    assert len(structure["units"]) == 8
    for unit in structure["units"]:
        sec_dir = codex_dir / unit["id"]
        assert (sec_dir / "index.rst").is_file()
        assert (sec_dir / "summary.rst").is_file()
        assert (sec_dir / "notes.rst").is_file()
        sec_rst = (sec_dir / "index.rst").read_text(encoding="utf-8")
        assert ".. picture:: /_static/figures/" in sec_rst

        if unit["id"].startswith("book-"):
            assert ".. collection::" in sec_rst

        for prop_id in unit["propositions"]:
            prop_num = int(prop_id.split(".")[1])
            prop_dir = sec_dir / f"{prop_num:02d}"
            assert (prop_dir / "index.rst").is_file(), f"Missing {prop_dir}/index.rst"
            assert (prop_dir / "commentary.rst").is_file(), f"Missing {prop_dir}/commentary.rst"
            prop_rst = (prop_dir / "index.rst").read_text(encoding="utf-8")
            assert ".. picture:: /_static/figures/" in prop_rst, f"Missing plate in {prop_dir}"
            assert prop_id in folio_map["folios"], f"Missing folio mapping for {prop_id}"
            scan_file = REPO_ROOT / folio_map["folios"][prop_id]["default"]
            assert scan_file.is_file(), f"Missing scan image {scan_file} for {prop_id}"
            prop_count += 1

    assert prop_count == 21


