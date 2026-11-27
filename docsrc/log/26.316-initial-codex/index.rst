:date: 2026-11-12
:type: log
:summary: Inaugural 0.1.0 release of geometor/byrne — 3-track Digital Scriptorium Book Codex for Oliver Byrne's 1847 Coloured Euclid, self-contained inline SVG glyph roles, Pointer-Free Visual Pseudocode Rosetta analyzer, and 17 exact SymPy .euclid-graphic plates.

Inaugural Digital Scriptorium Codex & Visual Pseudocode Engine (v0.1.0)
=======================================================================

Launched ``geometor/byrne`` (``v0.1.0``), uniting :person:`Oliver Byrne's <byrne>` 1847 Chiswick Press *First Six Books of the Elements of Euclid* with GEOMETOR's exact symbolic geometry engine:

- **Archival Multimodal Calibration**: Inspected 26 high-resolution pages directly from the 1847 William Pickering / Charles Whittingham print (Internet Archive ``firstsixbooksofe00eucl``, Thomas Fisher Rare Book Library scan) to verify Byrne's Simson axiom numbering, custom operators (``⊏``, ``⊐``, bisected semicircle for two right angles), Book V magnitude icons, and authentic 4-color plate assignments—including documenting the famous 1847 Title Page ``I.47`` color-plate transposition relative to pp. 48–49.
- **Self-Contained Inline Glyph Roles (``geometor.byrne.sphinx_ext``)**: Implemented ``:byrne-line:``, ``:byrne-angle:``, ``:byrne-tri:``, ``:byrne-sq:``, ``:byrne-rect:``, ``:byrne-arc:``, ``:byrne-circle:``, ``:byrne-mag:``, and ``:byrne-op:`` with theme-adaptive Chiswick Press CSS variables and bidirectional SVG hover/click highlighting without modifying ``photon-platform/publish``.
- **Pointer-Free Visual Pseudocode Grammar (``geometor.byrne.pseudocode``)**: Modeled Byrne's notation as a pass-by-value geometric token DSL across ``I.1``, ``I.5``, ``I.47``, ``II.11``, ``IV.10``, ``IV.11``, and ``V.16``, quantifying 80–92.9% verbal compression, zero alphabetic pointer dereferencing, stroke-modulation register expansion, and congruence-twin symmetry.
- **17 Exact Symbolic ``.euclid-graphic`` Plates (``geometor.byrne.constructions`` & ``render``)**: Built 100% exact :class:`geometor.model.Model` constructions (zero ``sp.Float``) over :math:`\mathbb{Q}`, :math:`\mathbb{Q}(\sqrt{3})`, :math:`\mathbb{Q}(\phi)`, and pentagonal radical towers with verified Rational Trigonometry proof checks.
