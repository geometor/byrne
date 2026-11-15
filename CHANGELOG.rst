=========
Changelog
=========

0.2.0 (2026-11-15)
------------------

- **changed**: Split the crammed multi-proposition unit pages (``unit-2-book-i`` through ``unit-6-book-vi``) into **6 dedicated Book sections** (``book-i`` through ``book-vi``, each with ``Overview · Summary · Notes`` tracks and ``.. collection::`` thumbnail galleries) and **21 dedicated per-proposition pages** (``book-i/{01,04,05,15,32,46,47}``, ``book-ii/{04,05,11}``, ``book-iii/{20,31,36}``, ``book-iv/{04,10,11}``, ``book-v/{11,16,18,22}``, ``book-vi/{30}``), each with synchronized ``Proposition · Commentary`` companion tracks.
- **added**: Full 1847 William Pickering / Chiswick Press italicized enunciations, inline ``:byrne-*:`` visual-token demonstrations, and symbolic/chromatic commentary across all 21 showcase propositions, plus hierarchical ``.toc-outline`` Table of Contents styling in ``byrne.css`` and ``docsrc/coloured_euclid/index.rst``.
- **fixed**: Extracted and verified Pickering 1847 Book V folio scans (``0209.jpg``, ``0215.jpg``, ``0219.jpg``, ``0227.jpg``, ``0228.jpg``) directly from ``byrne_1847_pickering.pdf``, correcting the ``V.16`` (*Alternando*) folio link to p. 181 (``0215.jpg``) and documenting the authentic 1847 Chiswick Press ``triangte`` compositorial variant on ``IV.4`` (p. 129, ``0163.jpg``).

0.1.5 (2026-11-15)
------------------

- Rebuilt codex documentation with ``photon-platform/publish`` ``v0.4.6`` so every inline ``.euclid-graphic`` SVG carries explicit ``viewBox`` pixel dimensions, per-diagram scoped ``<style>`` rules, and Nocturnal Codex dark/light theme parity.

0.1.4 (2026-11-15)
------------------

- Ensure canonical GEOMETOR ``logo.png`` and ``favicon.ico`` brand assets are provisioned in ``docsrc/_static/`` and rendered in site headers and browser tabs.

0.1.3 (2026-11-14)
------------------

- Standardized top-level ``About`` page (``docsrc/about/index.rst`` promoted to top header ``:order: 10``) with the three-pillar GEOMETOR semantic-extraction mission and archival provenance; retired ``docsrc/mission/`` stubs cleanly into Home and ``About``.

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
