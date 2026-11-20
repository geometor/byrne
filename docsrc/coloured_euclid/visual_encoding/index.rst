:layout: book
:type: book
:order: 7
:title: Pointer-Free Visual Pseudocode — 3-Way Rosetta Analysis
:folio: 0014
:page: x

.. _byrne-rosetta:
.. _byrne-visual-encoding:
.. _byrne-visual-encoding-en:
.. _byrne-unit-7-en:

Pointer-Free Visual Pseudocode — 3-Way Rosetta Analysis
=======================================================

.. rubric:: Side-by-Side Formalism Alignment: Heath (1908) · Byrne (1847) · GEOMETOR DAG

.. folio:: 0014
   :page: x

Side-by-side compiler and visual-register comparison across :person:`Heath's <heath>` classical alphabetic Euclid (*pass-by-reference* vertex pointers), :person:`Oliver Byrne's <byrne>` 1847 colored glyph equations (*pass-by-value* visual literals with zero pointer dereferences), and exact ``geometor.model`` SymPy algebraic constructions.

.. picture:: /_static/figures/rosetta.svg
   :alt: Three-column Rosetta comparison between Heath alphabetic pointers, Byrne pass-by-value color tokens, and GEOMETOR exact symbolic DAG.
   :caption: **3-Way Rosetta Architecture.** Eliminating alphabetic pointer indirection reduces verbal token load by 80–92% while mapping bijectively onto exact ``geometor.model`` Rational Trigonometry invariants.

1. Formal Grammar of Byrne's 1847 Visual Pseudocode
---------------------------------------------------

In :mod:`geometor.byrne.pseudocode`, every proposition in :person:`Oliver Byrne's <byrne>` 1847 treatise is modeled as an abstract syntax tree (:class:`~geometor.byrne.pseudocode.ByrneProgram`) over typed **pass-by-value geometric literals**:

.. code-block:: text

   Program     ::= PhaseBlock+
   PhaseBlock  ::= ("GIVEN" | "SOUGHT" | "CONSTRUCTION" | "DEMONSTRATION" | "QED") Statement+
   Statement   ::= (VisualToken | Operator | Connector)+ ("[" Justification+ "]")?
   VisualToken ::= Sort "(" ColorExpr ("," StrokeMode)? ("," FillMode)? ")" ("²")?
   Sort        ::= line | angle | tri | sq | rect | arc | circle | mag
   ColorExpr   ::= red | blue | yellow | black | Color "+" Color | Color "/" Color "/" Color
   StrokeMode  ::= solid | dashed | dotted | solid-dotted
   Operator    ::= "=" | "+" | "-" | "⊏" | "⊐" | "∥" | "⊥" | "∷" | "×" | "∟" | "2∟" | "∴" | "∵"

2. Rosetta Case I: ``I.1`` (*Equilateral Triangle*, ``G.84``)
-------------------------------------------------------------

* **Heath / Classical Alphabetic Prose (179 words, 31 vertex-pointer lookups):**
  *"With centre A and distance AB let the circle BCD be described; again, with centre B and distance BA let the circle ACE be described; and from the point C, in which the circles cut one another, to the points A, B let the straight lines CA, CB be joined..."*
* **Byrne 1847 Visual Pseudocode (22 words, 0 pointers, 6 registers):**
  Describe :byrne-circle:`blue <i1:( A B )>` and :byrne-circle:`red <i1:( B A )>`; draw :byrne-line:`yellow solid <i1:/ A C />` and :byrne-line:`red solid <i1:/ B C />` (:just:`I.post.3`, :just:`I.post.1`). Then :byrne-line:`yellow solid <i1:/ A C />` = :byrne-line:`black solid <i1:/ A B />` (:just:`I.def.15`) and :byrne-line:`red solid <i1:/ B C />` = :byrne-line:`black solid <i1:/ A B />` (:just:`I.def.15`), :byrne-op:`therefore` :byrne-line:`yellow solid <i1:/ A C />` = :byrne-line:`red solid <i1:/ B C />` = :byrne-line:`black solid <i1:/ A B />` (:just:`C.N.1`).
* **GEOMETOR Formal Pseudocode (``elements`` / ``model``):**

  .. code-block:: python

     c_ab = model.construct_circle(A, B, by="I.post.3")
     c_ba = model.construct_circle(B, A, by="I.post.3")
     C = model.intersect(c_ab, c_ba, side_of=(A, B, +1), ID="C")
     assert quadrance(A, C) == quadrance(A, B) == quadrance(B, C)

3. Rosetta Case II: ``I.5`` (*Pons Asinorum*, ``G.91``)
-------------------------------------------------------

* **Heath (329 words, 62 vertex-pointer lookups):** Requires tracking overlapping triangles ``AFC``, ``AGB``, ``BFC``, ``CGB`` and three-letter angles ``ABG``, ``ACF``, ``CBG``, ``BCF``, ``ABC``, ``ACB``.
* **Byrne 1847 (32 words, 0 pointers, 4 :term:`congruence-twin <congruence-twin>` pairs):**
  :byrne-line:`red solid` + :byrne-line:`yellow solid` = :byrne-line:`red solid` + :byrne-line:`yellow solid` around common :byrne-angle:`black` (:just:`C.N.2`) $\implies$ :byrne-line:`blue solid` = :byrne-line:`blue solid` and :byrne-angle:`yellow` = :byrne-angle:`yellow` (:just:`I.4`) $\implies$ remaining base angles :byrne-angle:`blue` = :byrne-angle:`blue` (:just:`C.N.3`).
* **GEOMETOR Formal Pseudocode:**

  .. code-block:: python

     G = model.intersect(line_AC, circle(A, F), beyond=(A, C), ID="G")
     assert spread(B, A, B, C) == spread(C, A, C, B)

4. Rosetta Case III: ``I.47`` (*Pythagorean Theorem*, ``G.140``)
----------------------------------------------------------------

* **Heath (314 words, 64 vertex-pointer lookups):** Refers repeatedly to four-letter squares ``BDEC``, ``ABFG``, ``ACKH`` and parallelograms ``BLMD``, ``CLME``.
* **Byrne 1847 (25 words, 0 pointers, 8.0% verbal load):**
  :byrne-sq:`black filled` = 2 × windmill triangle = :byrne-rect:`yellow filled` (:just:`I.4`, :just:`I.41`), and :byrne-sq:`red filled` = 2 × symmetric windmill triangle = :byrne-rect:`blue filled`, :byrne-op:`therefore` :byrne-rect:`yellow filled` + :byrne-rect:`blue filled` = :byrne-sq:`black filled` + :byrne-sq:`red filled` (:just:`C.N.2`).
* **GEOMETOR Formal Pseudocode:**

  .. code-block:: python

     assert spread(A, B, A, C) == 1
     assert quadrance(B, C) == quadrance(A, B) + quadrance(A, C)

5. Rosetta Cases IV–VI: ``II.11``, ``IV.10``–``IV.11`` & Book V ``V.16``
------------------------------------------------------------------------

* **Golden Section & Pentagon (``II.11`` → ``IV.10`` → ``IV.11``):**
  Byrne links colored area subtraction (:byrne-sq:`blue filled` = :byrne-rect:`yellow filled` in ``II.11``) to tangent-secant power (:byrne-line:`blue solid squared` in ``IV.10``) and five-chord cyclotomic symmetry (:byrne-line:`red solid`, :byrne-line:`red dotted`, :byrne-line:`black solid`, :byrne-line:`yellow solid`, :byrne-line:`blue solid` in ``IV.11``), mirrored in SymPy by the algebraic tower $\mathbb{Q} \subset \mathbb{Q}(\phi) \subset \mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})$.
* **Book V Colored Ratio Calculus (``V.16`` *Alternando*, ``G.276``):**
  :byrne-mag:`red circle` : :byrne-mag:`yellow square` :byrne-op:`prop` :byrne-mag:`blue diamond` : :byrne-mag:`black shield` $\implies$ :byrne-mag:`red circle` : :byrne-mag:`blue diamond` :byrne-op:`prop` :byrne-mag:`yellow square` : :byrne-mag:`black shield` (**7.1% verbal load**, connecting directly to ``geometor/codes``).

.. toctree::
   :hidden:

   summary
   notes
