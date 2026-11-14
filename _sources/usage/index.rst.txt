:navigation: header
:order: 20
:nav_title: Usage

==================
Using This Edition
==================

.. rubric:: Interactive Features & Reader's Guide to Oliver Byrne's Coloured Elements

Welcome to the **GEOMETOR Digital Scriptorium** edition of :person:`Oliver Byrne's <byrne>` 1847 masterpiece, *The First Six Books of the Elements of Euclid in Which Coloured Diagrams and Symbols Are Used Instead of Letters*. This edition combines the typographic and chromatic brilliance of the 1847 Chiswick Press original with modern interactive web technologies and exact symbolic geometry.

Interactive Reader Features
---------------------------

1. Synchronized Reading Tracks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every unit in the :doc:`Book Codex </coloured_euclid/index>` is organized into synchronized reading tracks accessible via the track switcher bar at the top of each page:

* **Byrne (1847) Edition**: Complete primary text transcribed leaf-by-leaf from the 1847 edition, preserving Byrne's color-coded syntax, archaic spellings, and original layout.
* **Summary**: Executive summaries condensing the deductive trajectory, primary theorems, and pedagogical innovations of each book.
* **Notes**: Scholarly commentary on Chiswick Press printing techniques, typographic registration, mathematical analysis, and cross-references to Heath's critical edition (``geometor/euclid``).

2. Primary-Source Folio Milestones
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Marginal citations such as ``[p. 48]`` or ``[p. 49]`` mark the exact page boundaries of the 1847 William Pickering printing. Clicking these marginal folio links or the header **Folio** badge opens the high-resolution archival scan from the Thomas Fisher Rare Book Library, allowing instant comparison between the digital transcription and the historical witness.

3. Interactive Diagrams & Deductive Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Oliver Byrne's signature innovation was replacing alphabetic vertex references (such as $AB$ or $\angle BAC$) with color-coded tokens that match the accompanying diagrams:

* **Bidirectional Glyphs**: Hovering or clicking any inline color glyph—such as a colored line segment (:byrne-line:`red solid`), angle (:byrne-angle:`blue`), square (:byrne-sq:`black filled`), or rectangle (:byrne-rect:`yellow filled`)—highlights or pulses its exact counterpart in the SVG illustration.
* **Formal Operators**: Symbolic operators such as :byrne-op:`right-angle` (*right angle*), :byrne-op:`two-right-angles` (*two right angles*), :byrne-op:`parallel` (*parallel*), and :byrne-op:`perp` (*perpendicular*) provide a concise visual shorthand.
* **Exact Geometric Construction**: Every figure is generated dynamically via ``geometor.model`` over exact algebraic number fields ($\mathbb{Q}$, $\mathbb{Q}(\sqrt{3})$, $\mathbb{Q}(\phi)$), ensuring mathematical fidelity without floating-point distortion.

4. Full-Text Search with In-Page Highlighting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The search box in the left sidebar provides instantaneous full-text indexing across the entire codex. Search query results append ``?highlight=`` parameters to document URLs, automatically highlighting matched words directly in proposition proofs, definitions, and commentary notes.

5. Categories, Tags, Document Types & Collection Views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The left sidebar displays dynamic taxonomy facets:

* **Categories & Tags**: Navigate topics by mathematical theme (*foundations*, *pythagorean-theorem*, *golden-ratio*, *proportions*, *similarity*).
* **Document Types**: Filter pages by content type (*treatise*, *unit*, *log*, *biography*, *reference*).
* **Collection Views**: Collection index pages offer view toggles between **Cards**, **Banners**, and **List** modes.

6. People, Bibliography & Glossary Tooltips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Biographical Hover Cards**: Links formatted with ``:person:`` (e.g., :person:`Oliver Byrne <byrne>`, :person:`Euclid <euclid>`, :person:`William Pickering <pickering>`) provide instant biographical summaries and direct links to the :doc:`People </coloured_euclid/persons>` register.
* **Citation Tooltips**: Bibliographic references formatted with ``:cite:`` link directly to the :doc:`Bibliography </coloured_euclid/bibliography>`.
* **Glossary Definitions**: Technical terms linked with ``:term:`` (e.g., :term:`Pass-by-Value Geometry <pointer-free-notation>`) provide instant definitions.
* **Theme Switcher**: Seamlessly toggle between Light, Dark, or System visual themes using the sun/moon control in the top-right navigation bar.

----

Command-Line & Python API
-------------------------

Command-Line Interface (CLI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``geometor-byrne`` CLI enables inspection, rendering, and analysis from the shell:

.. code-block:: bash

   # List all 1847 Oliver Byrne plates and their verification status
   python3 -m geometor.byrne list

   # Render all plates to SVG files in an output directory
   python3 -m geometor.byrne render -o build/svg/

   # Render a specific proposition plate (e.g., Book I, Proposition 47)
   python3 -m geometor.byrne render --prop I.47 -o build/svg/

   # Display Rosetta comparative metrics (Heath alphabetic vs. Byrne visual)
   python3 -m geometor.byrne rosetta

Python API
~~~~~~~~~~

Programmatically construct plates and compute cognitive metrics:

.. code-block:: python

   from geometor.byrne.constructions import build_plate, list_plate_ids
   from geometor.byrne.pseudocode import ROSETTA_PROGRAMS, compute_rosetta_metrics
   from geometor.byrne.render import export_plate_svg

   # Inspect available plates
   plate_ids = list_plate_ids()
   print("Available plates:", plate_ids)

   # Construct and export Proposition I.47 (Pythagorean Theorem)
   plate = build_plate("I.47")
   print(f"Proposition: {plate.prop_id} - {plate.title}")
   print(f"Proof checks passed: {all(plate.proof_checks.values())}")

   # Compute Rosetta metrics for cognitive verbosity comparison
   prog = ROSETTA_PROGRAMS["I.47"]
   metrics = compute_rosetta_metrics(prog)
   print(f"Heath prose words: {metrics.heath_words}")
   print(f"Byrne visual words: {metrics.byrne_words}")
   print(f"Reduction in verbal prose: {metrics.prose_reduction_pct:.1f}%")
