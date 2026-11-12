================
GEOMETOR • byrne
================

Digital Scriptorium **Book Codex**, **Pointer-Free Visual Pseudocode Grammar**, and **Exact Symbolic Color-Token Proof Engine** for **Oliver Byrne's** *The First Six Books of the Elements of Euclid in Which Coloured Diagrams and Symbols Are Used Instead of Letters for the Greater Ease of Learners* (London: William Pickering / Charles Whittingham at the Chiswick Press, 1847).

.. image:: docsrc/_static/figures/i47.svg
   :alt: Oliver Byrne Book I Proposition 47 Pythagorean Theorem rendered from exact SymPy coordinates
   :align: center

Highlights
----------

- **Self-Contained Inline Byrne Glyph Roles (``geometor.byrne.sphinx_ext``)**:
  Renders authentic four-color inline SVG micro-glyphs (``:byrne-line:``, ``:byrne-angle:``, ``:byrne-tri:``, ``:byrne-sq:``, ``:byrne-rect:``, ``:byrne-arc:``, ``:byrne-circle:``, ``:byrne-mag:``, ``:byrne-op:``) with bidirectional ``.euclid-graphic`` hover and click-lock highlighting—without modifying ``photon-platform/publish``.
- **Pointer-Free Visual Pseudocode & 3-Way Rosetta Analysis (``geometor.byrne.pseudocode``)**:
  Formalizes Byrne's 1847 notation (*"the parts being differently coloured, are made to name themselves"*, p. ix) as a **pass-by-value geometric token DSL**, comparing verbal load, pointer dereferencing, stroke modulation, and congruence-twin registers across Heath (``geometor/euclid``), Byrne (1847), and ``geometor/elements`` / ``geometor/codes``.
- **17 Exact Symbolic ``geometor.model`` Plates (``geometor.byrne.constructions`` & ``render``)**:
  Every plate (``I.1``, ``I.4``, ``I.5``, ``I.15``, ``I.32``, ``I.46``, ``I.47``, ``II.4``, ``II.5``, ``II.11``, ``III.20``, ``III.31``, ``III.36``, ``IV.4``, ``IV.10``, ``IV.11``, ``VI.30``) is constructed with ``Model(..., auto_intersect=False)`` over exact SymPy number fields ($\mathbb{Q}$, $\mathbb{Q}(\sqrt{3})$, $\mathbb{Q}(\phi)$, and $\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})$) with zero floating-point coordinates.
- **3-Track Digital Scriptorium Book Codex (``docsrc/coloured_euclid/``)**:
  Synchronized *Byrne (1847) · Summary · Notes* tracks across Books I–VI plus full prosopography, bibliography (honoring Ruari McLean, Edward Tufte, and Nicholas Rougeux's 2018 ``c82.net/euclid`` while maintaining a 100% public-domain provenance boundary), glossary, and Simson–Heath–G-Index concordance.

Quick Start
-----------

.. code-block:: bash

   # Run the symbolic verification & Rosetta test suite
   pytest

   # Render all 17 exact .euclid-graphic SVG plates
   geometor-byrne render -o docsrc/_static/figures

   # Print the 3-way Heath / Byrne / GEOMETOR Rosetta metrics table
   geometor-byrne rosetta

   # Build the multi-track HTML Book Codex into docs/
   publish build

License & Provenance
--------------------

Source code and symbolic SVG constructions are licensed under the **MIT License**. Primary Euclidean text and 1847 color/symbol calibrations derive exclusively from the **100% Public Domain** 1847 William Pickering / Chiswick Press print (Internet Archive ``firstsixbooksofe00eucl``).
