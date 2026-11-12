"""Render all 17 exact symbolic Oliver Byrne (1847) plates into docsrc/_static/figures/."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
for _extra in (_REPO_ROOT / "src", _REPO_ROOT.parent / "model" / "src"):
    if str(_extra) not in sys.path:
        sys.path.insert(0, str(_extra))

from geometor.byrne.constructions import build_all_plates
from geometor.byrne.render import export_plate_svg


def main() -> None:
    """Build, algebraically verify, and export all 17 showcase SVG plates."""
    figures_dir = _REPO_ROOT / "docsrc" / "_static" / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    plates = build_all_plates()
    for plate in plates:
        failed = [k for k, ok in plate.proof_checks.items() if not ok]
        if failed:
            raise AssertionError(f"Proof invariant failed in {plate.prop_id}: {failed}")
        out_path = export_plate_svg(plate, figures_dir / f"{plate.slug}.svg")
        print(f"[OK] {plate.prop_id:<6} -> {out_path.relative_to(_REPO_ROOT)} ({plate.number_field})")

    print(f"\nSuccessfully verified and exported {len(plates)} plates.")


if __name__ == "__main__":
    main()
