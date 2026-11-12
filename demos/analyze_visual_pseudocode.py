"""Print the 3-way Rosetta analysis (Heath · Byrne 1847 · GEOMETOR) across 7 propositions."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
for _extra in (_REPO_ROOT / "src", _REPO_ROOT.parent / "model" / "src"):
    if str(_extra) not in sys.path:
        sys.path.insert(0, str(_extra))

from geometor.byrne.pseudocode import ROSETTA_PROGRAMS, compute_rosetta_metrics


def main() -> None:
    """Display token compression, pointer elimination, and register diagnostics."""
    print("=== OLIVER BYRNE (1847) POINTER-FREE VISUAL PSEUDOCODE ROSETTA REPORT ===\n")
    for prop_id, prog in ROSETTA_PROGRAMS.items():
        m = compute_rosetta_metrics(prog)
        diag = m.register_diagnostic
        print(f"[{prop_id}] {prog.title} ({prog.pickering_page}, G-Index {prog.g_id})")
        print(
            f"  Heath 1908   : {m.heath_words} words, "
            f"{m.heath_pointer_dereferences} alphabetic pointer dereferences"
        )
        print(
            f"  Byrne 1847   : {m.byrne_words} words ({m.word_compression_ratio:.1%} verbal load), "
            f"{m.byrne_pointer_dereferences} pointers, {m.byrne_visual_tokens} inline glyphs "
            f"across {m.byrne_distinct_registers} distinct visual registers"
        )
        print(
            f"  Register QA  : stroke_mod={diag.uses_stroke_modulation}, "
            f"composite={diag.uses_composite_tokens}, "
            f"congruence_twins={len(diag.intentional_congruence_twins)}, "
            f"unambiguous={diag.is_unambiguous}"
        )
        for st in prog.statements:
            print(f"    {st.phase.value.upper():<14} {st.to_compact()}")
        print()


if __name__ == "__main__":
    main()
