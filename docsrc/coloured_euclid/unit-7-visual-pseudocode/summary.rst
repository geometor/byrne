.. _byrne-unit-7-summary:

Unit VII Summary: Complementarity of the Three Euclidean Formalisms
===================================================================

.. rubric:: Synthesis of Textual, Chromatic & Symbolic Representations

.. list-table:: **Architectural Comparison Across the GEOMETOR Triad**
   :header-rows: 1
   :widths: 22 26 26 26

   * - Dimension
     - Heath / ``geometor/euclid``
     - Byrne 1847 / ``geometor/byrne``
     - ``geometor/elements`` & ``model``
   * - **Binding Model**
     - Pass-by-reference (`A, B, C`)
     - Pass-by-value (:byrne-line:`red solid`, :byrne-sq:`black filled`)
     - Typed Symbolic DAG (`Point`, `Circle`, `Polygon`)
   * - **Cognitive Strength**
     - Unbounded variable namespace
     - Zero eye-lookup latency; instant symmetry
     - Deterministic machine constructibility
   * - **Scaling Limit**
     - High working-memory indirection
     - 4-color :term:`register pressure <register-pressure>`
     - Requires explicit orientation selectors (`side_of`)
   * - **Proof Verification**
     - Natural-language syllogism
     - Visual equational inspection
     - Exact SymPy polynomial/radical simplification
