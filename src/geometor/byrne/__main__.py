"""CLI entry point for ``geometor-byrne``: render plates and inspect Rosetta metrics."""

from __future__ import annotations

import argparse
from pathlib import Path

from geometor.byrne.constructions import build_all_plates, build_plate, list_plate_ids
from geometor.byrne.pseudocode import ROSETTA_PROGRAMS, compute_rosetta_metrics
from geometor.byrne.render import export_all_plates, export_plate_svg
from geometor.byrne.tableaux import export_all_tableaux


def _cmd_list(_args: argparse.Namespace) -> int:
    print(f"{'Prop':<8} {'Slug':<8} {'G-ID':<8} {'Field':<28} {'Page':<12} Title")
    print("-" * 96)
    for plate in build_all_plates():
        ok = all(plate.proof_checks.values())
        badge = "OK" if ok else "FAIL"
        print(
            f"{plate.prop_id:<8} {plate.slug:<8} {plate.g_id:<8} "
            f"{plate.number_field:<28} {plate.pickering_page:<12} [{badge}] {plate.title}"
        )
    return 0


def _cmd_render(args: argparse.Namespace) -> int:
    out_dir = Path(args.output)
    if args.prop:
        plate = build_plate(args.prop)
        out = export_plate_svg(plate, out_dir / f"{plate.slug}.svg", show_labels=args.labels)
        print(f"Exported {plate.prop_id} -> {out}")
    else:
        written = export_all_plates(out_dir)
        tableaux = export_all_tableaux(out_dir)
        print(
            f"Exported {len(written)} symbolic plates + {len(tableaux)} tableaux -> {out_dir.resolve()}"
        )
    return 0


def _cmd_rosetta(_args: argparse.Namespace) -> int:
    print(
        f"{'Prop':<7} {'Heath Words':>11} {'Heath Ptrs':>10} "
        f"{'Byrne Words':>11} {'Byrne Glyphs':>12} {'Registers':>9} {'Unambig':>8}"
    )
    print("-" * 76)
    for prog in ROSETTA_PROGRAMS.values():
        m = compute_rosetta_metrics(prog)
        print(
            f"{m.prop_id:<7} {m.heath_words:>11} {m.heath_pointer_dereferences:>10} "
            f"{m.byrne_words:>11} {m.byrne_visual_tokens:>12} "
            f"{m.byrne_distinct_registers:>9} {m.register_diagnostic.is_unambiguous!s:>8}"
        )
    return 0


def main(argv: list[str] | None = None) -> int:
    """Execute the ``geometor-byrne`` command-line interface."""
    parser = argparse.ArgumentParser(
        prog="geometor-byrne",
        description="Symbolic constructions, SVG plate renderer, and Rosetta analyzer for Byrne (1847).",
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("list", help="List and verify all 17 symbolic Byrne plates.")

    p_render = sub.add_parser("render", help="Render showcase .euclid-graphic SVG plates.")
    p_render.add_argument(
        "-o",
        "--output",
        default="docsrc/_static/figures",
        help="Destination directory for SVG plates.",
    )
    p_render.add_argument(
        "-p",
        "--prop",
        choices=list_plate_ids(),
        help="Optional single proposition ID to render.",
    )
    p_render.add_argument(
        "--labels",
        action="store_true",
        help="Include editorial vertex labels in rendered SVG.",
    )

    sub.add_parser("rosetta", help="Print 3-way Heath / Byrne / GEOMETOR Rosetta metrics.")

    args = parser.parse_args(argv)
    if args.command == "render":
        return _cmd_render(args)
    if args.command == "rosetta":
        return _cmd_rosetta(args)
    return _cmd_list(args)


if __name__ == "__main__":
    raise SystemExit(main())
