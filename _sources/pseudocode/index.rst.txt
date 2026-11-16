:navigation: header
:order: 25
:nav_title: Pseudocode

==============================
Pointer-Free Visual Pseudocode
==============================

.. rubric:: Oliver Byrne (1847) as a Pointer-Free Visual Programming Language

Long before structured programming, dataflow visual languages, or modern IDE token highlighting, :person:`Oliver Byrne <byrne>` (:cite:`1847, pp. ix–xi, xxvii–xxix <byrne:1847>`) diagnosed the fundamental cognitive bottleneck of classical Euclidean deduction: **alphabetic pointer dereferencing**.

.. picture:: /_static/figures/rosetta.svg
   :alt: Three-column Rosetta comparison between Heath alphabetic pointers, Byrne pass-by-value color tokens, and GEOMETOR exact symbolic DAG.
   :caption: **3-Way Rosetta Architecture.** Heath (1908) alphabetic pointers vs. Byrne (1847) pass-by-value colored literals vs. GEOMETOR exact SymPy algebraic DAG.

Pass-by-Reference vs. Pass-by-Value in Geometry
-----------------------------------------------

In :person:`Euclid's <euclid>` Greek *Stoicheia* and :person:`Heath's <heath>` English edition (``geometor/euclid``), geometric primitives on the page are nameless black ink strokes. To refer to a segment, angle, or square, prose assigns **memory addresses** ($A, B, C, D, \dots$) to point vertices and forms composite tuple expressions (`AB`, `angle FBC`, `parallelogram BLMD`). Reading a single sentence of `I.5` or `I.47` requires dozens of indirect table lookups:

.. math::

   \text{String Token } (\text{``}\triangle FBC\text{''})
   \;\xrightarrow{\text{scan}}\; \{F, B, C\}
   \;\xrightarrow{\text{trace}}\; \text{mental hull}
   \;\xrightarrow{\text{compare}}\; \text{String Token } (\text{``}\triangle ABD\text{''}).

Byrne's 1847 Chiswick Press grammar replaces *pass-by-reference* with **pass-by-value**:

1. **Typed Inline Value-Tokens**: Every primitive sort—segment (:byrne-line:`red solid`), angle (:byrne-angle:`blue`), triangle (:byrne-tri:`yellow filled`), square (:byrne-sq:`black filled`), rectangle (:byrne-rect:`yellow filled`), arc (:byrne-arc:`blue`), circle (:byrne-circle:`red`), and Book V magnitude (:byrne-mag:`red circle`, :byrne-mag:`yellow square`, :byrne-mag:`blue diamond`, :byrne-mag:`black shield`)—appears directly inside the algebraic line as a miniature colored geometric literal.
2. **Formal Operators (pp. xxvii–xxviii)**: Natural-language verbs collapse into symbolic operators: ``=`` (equality of length, angle, or area), ``+`` / ``-`` (composition and subtraction), :byrne-op:`gt` (*greater than*), :byrne-op:`lt` (*less than*), :byrne-op:`parallel` (*parallel*), :byrne-op:`perp` (*perpendicular*), :byrne-op:`right-angle` (*one right angle*), :byrne-op:`two-right-angles` (*two right angles*), :byrne-op:`prop` (*proportion*), :byrne-op:`because` (*because*), and :byrne-op:`therefore` (*therefore*).
3. **Structured Proclean Control Flow**: Every proposition is formatted into explicit visual blocks matching :person:`Proclus's <proclus>` six divisions (:term:`ekthesis`, *diorismos*, *kataskeue*, :term:`apodeixis`, *symperasma*), with each deductive equation placed on its own line accompanied by marginal ``:just:`` citations.

Quantitative Rosetta Compiler Metrics
-------------------------------------

The module :mod:`geometor.byrne.pseudocode` parses seven flagship propositions across Books I–V and measures verbal token load, alphabetic pointer dereferences, and **visual register pressure**:

.. list-table:: **Heath (1908) vs. Byrne (1847) vs. GEOMETOR DAG Metrics**
   :header-rows: 1
   :widths: 10 14 14 14 14 16 18

   * - Prop
     - G-Index
     - Heath Words
     - Heath Pointers
     - Byrne Words
     - Verbal Load
     - Visual Registers
   * - ``I.1``
     - ``G.84``
     - 179
     - 31
     - 22
     - **12.3%**
     - 6 (unique)
   * - ``I.5``
     - ``G.91``
     - 329
     - 62
     - 32
     - **9.7%**
     - 8 (+4 congruence twins)
   * - ``I.47``
     - ``G.140``
     - 314
     - 64
     - 25
     - **8.0%**
     - 9 (stroke-modulated)
   * - ``II.11``
     - ``G.154``
     - 269
     - 56
     - 50
     - **18.6%**
     - 5 (solid-dotted cut)
   * - ``IV.10``
     - ``G.223``
     - 389
     - 78
     - 38
     - **9.8%**
     - 9 (composite + dotted)
   * - ``IV.11``
     - ``G.224``
     - 210
     - 41
     - 42
     - **20.0%**
     - 10 (5-side register overflow)
   * - ``V.16``
     - ``G.276``
     - 253
     - 20
     - 18
     - **7.1%**
     - 4 (pure Eudoxian algebra)

Three Structural Laws Discovered by Register Analysis
-----------------------------------------------------

1. **The Four-Color Working-Memory Ceiling (:term:`Register Pressure <register-pressure>`)**:
   Human visual working memory holds $4 \pm 1$ chromatic chunks effortlessly. Whenever a proposition introduces five or more primitives of the same sort—such as the five sides of the regular pentagon in ``IV.11`` (:byrne-line:`red solid`, :byrne-line:`red dotted`, :byrne-line:`black solid`, :byrne-line:`yellow solid`, :byrne-line:`blue solid`) or shared square/rectangle boundaries in ``I.47``—Byrne multiplies his four ink channels by **stroke modulation** (``solid``, ``dashed``, ``dotted``, ``solid-dotted``).
2. **Intentional :term:`Congruence-Twin Coloring <congruence-twin>`**:
   In ``I.5`` (*Pons Asinorum*), Byrne deliberately binds *both* equal legs to :byrne-line:`red solid`, *both* produced extensions to :byrne-line:`yellow solid`, and *both* auxiliary cross-diagonals to :byrne-line:`blue solid`. What a naive type-checker would flag as a register collision is in fact a **symmetric congruence invariant** encoded directly into the visual type!
3. **Why GEOMETOR Pairs Visual Tokens with Symbolic DAGs**:
   Pure visual tokens excel at human proof comprehension (`apodeixis`), whereas machine constructibility requires explicit incidence/orientation selectors (`side_of`, `beyond`) when circles intersect in two points. Together, ``geometor/euclid`` (textual heritage), ``geometor/byrne`` (pointer-free visual cognition), and ``geometor/elements`` + ``geometor/codes`` (computable symbolic DAGs) form a complete three-pillar Rosetta Stone.

See :ref:`Visual Encoding in the Book Codex <byrne-visual-encoding-en>` for full side-by-side 3-way derivations of each proposition.
