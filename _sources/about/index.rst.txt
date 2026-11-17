:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor.byrne`` brings :person:`Oliver Byrne's <byrne>` celebrated 1847 Chiswick Press masterpiece—:cite:`*The First Six Books of the Elements of Euclid in Which Coloured Diagrams and Symbols Are Used Instead of Letters for the Greater Ease of Learners* <byrne:1847>`—into the **GEOMETOR Digital Scriptorium** as both a scholarly multi-track **Book Codex** (*Byrne 1847 Edition · Executive Summary · Scholarly & Design Notes*) and an executable **Pointer-Free Visual Pseudocode** laboratory.

Where classical Euclidean prose (:person:`T. L. Heath <heath>`, ``geometor/euclid``) operates *by reference*—relying on arbitrary alphabetic vertex pointers ($A, B, C, \dots$) requiring the reader's working memory to shuttle continually between text and diagram—Byrne formulated a revolutionary pass-by-value geometry. As Byrne observed on page ``ix`` of his 1847 *Introduction*: *"the parts being differently coloured, are made to name themselves, for their forms in corresponding colours represent them in the demonstration."* This edition extracts Byrne's implicit visual syntax into a formal, typed geometric token grammar (:mod:`geometor.byrne.pseudocode`) connected directly to ``geometor/elements`` and ``geometor/codes``.

Every showcase plate (from Proposition ``I.1`` through ``VI.30``) is reconstructed from scratch in :mod:`geometor.byrne.constructions` using :class:`geometor.model.Model` (zero floating-point coordinates) over exact algebraic number fields ($\mathbb{Q}$, $\mathbb{Q}(\sqrt{3})$, $\mathbb{Q}(\phi)$, and $\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})$), with proof invariants verified symbolically via Rational Trigonometry quadrance and spread laws. A custom Sphinx extension renders interactive inline SVG micro-glyphs (:byrne-line:`red solid`, :byrne-angle:`blue`, :byrne-sq:`black filled`, :byrne-rect:`yellow filled`) wired directly to responsive ``.euclid-graphic`` plates.

The GEOMETOR Mission
--------------------

The **GEOMETOR** initiative, founded by **phi ARCHITECT**, is dedicated to a three-fold synthesis of classical geometry, exact symbolic computation, and modern knowledge architecture:

* **Extracting Historical Semantic Knowledge**: Moving beyond passive page scans and static OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises. We elevate running prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs where every enunciation, proof step, and historical cross-reference is individually referenceable.
* **Exact Symbolic Grounding (``geometor.model``)**: Anchoring geometric constructions in 100% exact symbolic algebra (via ``SymPy``) and Rational Trigonometry invariants (quadrance, spread, cross-ratio) over exact algebraic number fields rather than lossy floating-point approximations. Every geometric theorem is treated as an exact algebraic truth verifiable through computational modeling.
* **Repurposing Knowledge Across Mediums**: Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (via ``photon-platform/publish``), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG laboratories (``geometor.explorer``), QHD visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

All transcriptions, color/stroke assignments, and symbolic SVG plates derive strictly from the 100% public-domain 1847 William Pickering / Charles Whittingham print:

* **Primary Print Copy**: Oliver Byrne, *The First Six Books of the Elements of Euclid in Which Coloured Diagrams and Symbols Are Used Instead of Letters for the Greater Ease of Learners*. London: William Pickering, printed by Charles Whittingham at the Chiswick Press, 1847. Verified against high-resolution scans from the Thomas Fisher Rare Book Library (Internet Archive ``firstsixbooksofe00eucl``).
* **Scholarly Appreciation**: In our bibliography and historical commentary we honor :person:`Ruari McLean <mclean>` (:cite:`1963 <mclean:1963>`), :person:`Edward Tufte <tufte>` (:cite:`1990 <tufte:1990>`), and :person:`Nicholas Rougeux <rougeux>` (:cite:`c82.net/euclid, 2018 <rougeux:2018>`; :cite:`Making of Byrne's Euclid <rougeux:2018-making>`), while maintaining a strict zero-copy copyright boundary with modern third-party web and print editions.

The text and diagrams are collated and structured into the Digital Scriptorium multi-track codex format, cross-referenced with the classical Greek text of Euclid and modern formal mathematical foundations.

* :doc:`Reader's Guide and Usage </usage/index>`
* :doc:`Coloured Euclid Codex </coloured_euclid/index>`
* :doc:`Visual Pseudocode Specification </pseudocode/index>`
* :doc:`Biographical Register of Persons </coloured_euclid/people/index>`
* :doc:`Systematic Bibliography </coloured_euclid/bibliography>`
