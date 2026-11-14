=========
Changelog
=========

0.1.2 (2026-11-14)
------------------

- **changed**: Standardized Book Title Page, top-level Header Navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author/Translator profiles in ``People``, and English structural terminology.

0.1.1 (2026-11-13)
------------------

- Resolve 100% of marginal ``.. folio::`` scan links (18 directives) to Chiswick Press facsimile page scans via ``publish folio-links``.

0.1.0 (2026-11-12)
------------------

- Initialized ``geometor-byrne`` namespace package (``src/geometor/byrne/``), CLI (``geometor-byrne``), and PEP 621 ``pyproject.toml`` targeting Python ``>=3.13``.
- Implemented self-contained Sphinx extension ``geometor.byrne.sphinx_ext`` registering ``:byrne-line:``, ``:byrne-angle:``, ``:byrne-tri:``, ``:byrne-sq:``, ``:byrne-rect:``, ``:byrne-arc:``, ``:byrne-circle:``, ``:byrne-mag:``, and ``:byrne-op:`` with theme-adaptive Chiswick Press CSS variables and bidirectional SVG highlighting (``byrne.css``, ``byrne_interactive.js``).
- Implemented ``geometor.byrne.pseudocode`` modeling Oliver Byrne's 1847 notation as a pointer-free pass-by-value geometric token grammar with 3-way Rosetta comparisons (Heath · Byrne 1847 · GEOMETOR) and static visual-register diagnostics across ``I.1``, ``I.5``, ``I.47``, ``II.11``, ``IV.10``, ``IV.11``, and ``V.16``.
- Constructed and verified 17 exact ``geometor.model.Model`` showcase plates (``I.1``, ``I.4``, ``I.5``, ``I.15``, ``I.32``, ``I.46``, ``I.47``, ``II.4``, ``II.5``, ``II.11``, ``III.20``, ``III.31``, ``III.36``, ``IV.4``, ``IV.10``, ``IV.11``, ``VI.30``) with zero ``sp.Float`` atoms and interactive ``.euclid-graphic`` SVG export.
- Authored synchronized 3-track Book Codex (``docsrc/coloured_euclid/``) with Simson–Heath–G-Index concordance, prosopography, bibliography, and glossary calibrated directly against the 1847 William Pickering / Chiswick Press scan (``firstsixbooksofe00eucl``).
