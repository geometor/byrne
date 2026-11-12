:navigation: header
:order: 10

=======
mission
=======

``geometor.byrne`` brings :person:`Oliver Byrne's <byrne>` celebrated 1847 Chiswick Press masterpiece—:cite:`*The First Six Books of the Elements of Euclid in Which Coloured Diagrams and Symbols Are Used Instead of Letters for the Greater Ease of Learners* <byrne:1847>`—into the **GEOMETOR Digital Scriptorium** as both a scholarly multi-track **Book Codex** and an executable **Visual Pseudocode** laboratory.

Core Architectural Pillars
--------------------------

1. **Pointer-Free Visual Pseudocode (:term:`Pass-by-Value Geometry <pointer-free-notation>`)**:
   Classical Euclidean prose (:person:`T. L. Heath <heath>`, ``geometor/euclid``) operates *by reference*: vertices receive arbitrary alphabetic pointers ($A, B, C, \dots$) and every step forces the reader's eye to shuttle between text and diagram to assemble segments, angles, and polygons in working memory. On page ``ix`` of his 1847 *Introduction*, Byrne formulated a radical alternative: *"the parts being differently coloured, are made to name themselves, for their forms in corresponding colours represent them in the demonstration."* ``geometor.byrne`` formalizes this 1847 insight as a typed geometric token grammar (:mod:`geometor.byrne.pseudocode`) bridged directly to ``geometor/elements`` and ``geometor/codes``.
2. **100% Exact Symbolic Precision (``geometor.model``)**:
   Every showcase plate (``I.1`` through ``VI.30``) is constructed from scratch in :mod:`geometor.byrne.constructions` using :class:`geometor.model.Model` (``auto_intersect=False``, zero floating-point coordinates) over exact SymPy number fields ($\mathbb{Q}$, $\mathbb{Q}(\sqrt{3})$, $\mathbb{Q}(\phi)$, and $\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})$), with algebraic proof invariants verified symbolically via Rational Trigonometry quadrance and spread laws.
3. **Self-Contained Bidirectional Interactive Typography**:
   Our custom Sphinx extension (:mod:`geometor.byrne.sphinx_ext`) renders authentic inline SVG micro-glyphs (:byrne-line:`red solid`, :byrne-angle:`blue`, :byrne-sq:`black filled`, :byrne-rect:`yellow filled`, :byrne-mag:`red circle`, :byrne-op:`two-right-angles`) wired directly to ``.euclid-graphic`` plates without modifying ``photon-platform/publish``.
4. **100% Public-Domain Archival Provenance & Scholarly Appreciation**:
   All transcriptions, color/stroke assignments, and symbolic SVG plates derive strictly from the 100% public-domain 1847 William Pickering / Charles Whittingham print (Internet Archive ``firstsixbooksofe00eucl``, Thomas Fisher Rare Book Library scan). In our bibliography and commentary we honor :person:`Ruari McLean <mclean>` (:cite:`1963 <mclean:1963>`), :person:`Edward Tufte <tufte>` (:cite:`1990 <tufte:1990>`), and :person:`Nicholas Rougeux <rougeux>` (:cite:`c82.net/euclid, 2018 <rougeux:2018>`; :cite:`Making of Byrne's Euclid <rougeux:2018-making>`), while maintaining a strict zero-copy copyright boundary with modern third-party web and print editions.
