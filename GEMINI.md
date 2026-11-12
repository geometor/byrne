# GEOMETOR • byrne

Digital Scriptorium Book Codex, Pointer-Free Visual Pseudocode Grammar, and Exact Symbolic Color-Token Proof Engine for **Oliver Byrne's** *The First Six Books of the Elements of Euclid in Which Coloured Diagrams and Symbols Are Used Instead of Letters for the Greater Ease of Learners* (London: William Pickering / Chiswick Press, 1847).

## Architecture & Modules (`src/geometor/byrne/`)

- **`palette.py`**: Calibrated 1847 Chiswick Press four-color ink specs (`red`, `blue`, `yellow`, `black`), stroke dash arrays (`solid`, `dashed`, `dotted`, `solid-dotted`), and light/dark CSS custom property generators.
- **`sphinx_ext.py` + `static/{byrne.css,byrne_interactive.js}`**: Self-contained Sphinx extension registering `:byrne-line:`, `:byrne-angle:`, `:byrne-tri:`, `:byrne-sq:`, `:byrne-rect:`, `:byrne-arc:`, `:byrne-circle:`, `:byrne-mag:`, and `:byrne-op:` without modifying `photon-platform/publish`. Note: `photon_platform.publish.images` strips `<style>` blocks when inlining `.euclid-graphic` SVGs, so all plate CSS rules live both in `render.EMBEDDED_SVG_STYLE` and `static/byrne.css`.
- **`pseudocode.py`**: Formal Pointer-Free Visual Pseudocode AST (`VisualToken`, `ByrneStatement`, `ByrneProgram`), alphabetic pointer-dereference counter, static register-collision & congruence-twin analyzer, and 7-proposition 3-way Rosetta corpus (`I.1`, `I.5`, `I.47`, `II.11`, `IV.10`, `IV.11`, `V.16`).
- **`constructions.py` & `render.py`**: 17 exact `geometor.model.Model(..., auto_intersect=False)` constructions (zero `float` / `sp.Float`) over $\mathbb{Q}$, $\mathbb{Q}(\sqrt{3})$, $\mathbb{Q}(\phi)$, and pentagonal radical extensions, exporting `.euclid-graphic` SVGs with 3-vertex midpoint `<path>` geometry, `#geom-tick-1..3` markers, `data-ref`, `data-aliases`, and `data-byrne-color`.

## Archival Provenance & Copyright Boundary

- **Primary Witness**: 1847 Pickering / Whittingham scan (`Internet Archive: firstsixbooksofe00eucl`, Thomas Fisher Rare Book Library; gitignored local PDF `resources/pickering_1847/pdfs/byrne_1847_pickering.pdf`). Pagination formula: `Printed Page = Leaf - 34` starting at `Leaf 35 = p. 1`.
- **Strict Boundary**: Zero HTML, CSS, JavaScript, SVG paths, or traced woodcut assets may ever be copied from `c82.net/euclid` (Nicholas Rougeux, 2018, CC BY-NC-SA) or commercial facsimiles. All calibrations come directly from multimodal inspection of the 1847 public-domain scan and exact `geometor.model` algebra.

## Verification Gates

```bash
pytest
ruff check src demos tests
publish build
```
