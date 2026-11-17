GEOMETOR • byrne
================

**Visit the Online Archive:** https://geometor.github.io/byrne/

.. image:: docsrc/_static/figures/i47.svg
   :alt: GEOMETOR • byrne featured geometric construction
   :target: https://geometor.github.io/byrne/
   :align: center

**Oliver Byrne • The First Six Books of the Elements of Euclid (Coloured Diagrams) • semantic digital archive**

Mission
-------

``geometor/byrne`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It provides a multi-track Book Codex, pointer-free visual pseudocode grammar, and exact symbolic color-token proof engine for Oliver Byrne's celebrated 1847 edition of Euclid's *Elements*. The archive liberates Byrne's revolutionary four-color visual pedagogy from static print bounds into addressable semantic units, calibrated theme-adaptive vector diagrams, primary-source Chiswick Press provenance, and exact symbolic geometry across the GEOMETOR corpus.

Books in This Archive
---------------------

- `The First Six Books of the Elements of Euclid <https://geometor.github.io/byrne/coloured_euclid/>`_ — Oliver Byrne's landmark 1847 Chiswick Press masterpiece, replacing alphabetical point labels with colored diagrams and symbols across Books I–VI.

Python Package & Modules
------------------------

The ``geometor-byrne`` Python package (``import geometor.byrne``) provides the executable symbolic geometry, construction, and compilation modules powering this archive:

- ``constructions.py`` — Exact symbolic ``geometor.model`` constructions for 17 Oliver Byrne (1847) showcase plates.
- ``palette.py`` — Authentic 1847 Chiswick Press four-color palette and stroke grammar for Oliver Byrne's Euclid.
- ``pseudocode.py`` — Formal grammar, AST, and 3-way Rosetta metrics for Oliver Byrne's 1847 Visual Pseudocode.
- ``render.py`` — Interactive ``.euclid-graphic`` SVG renderer for Oliver Byrne (1847) symbolic plates.
- ``tableaux.py`` — Chiswick Press Typographic & Synthesis SVG Tableaux for Oliver Byrne's 1847 Codex.
- ``sphinx_ext.py`` — Self-contained Sphinx extension for Oliver Byrne's 1847 inline visual glyph roles.

See the `API Reference <https://geometor.github.io/byrne/modules/>`_ for full module documentation.

Repository Contents
-------------------

- ``docsrc/`` — Multi-track Book Codex, visual pseudocode documentation, and Sphinx site compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``resources/`` — 1847 primary scan provenance, color palette definitions, and apparatus datasets.
- ``src/geometor/byrne/`` — Python modules for exact SymPy geometric constructions, inline Byrne glyph roles, and pseudocode DSL analysis.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
