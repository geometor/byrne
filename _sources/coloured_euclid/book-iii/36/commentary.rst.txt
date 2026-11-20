:canonical_id: III.36.commentary
:book: III
:proposition: 36
:order: 36
:type: commentary
:title: Commentary — Proposition III.36
:folio: 0155
:page: 121

.. _byrne-iii-36-commentary:


.. folio:: 0155
   :page: 121

Commentary on Proposition III.36: Three-Part Secant Encoding & Tangent Power Invariant
======================================================================================

.. rubric:: Pickering Folio 0155 (p. 121) & Exact Rational Secant-Tangent Power (III.36 · G.201)

Tripartite Line Token on Pickering p. 121
-----------------------------------------

Pickering **p. 121 (Leaf 155)** showcases one of Byrne's cleverest compound line tokens: the diameter-secant $AD$ is printed inline as a single horizontal bar made of **black solid** ($AO$) + **red dotted** ($OC$) + **red solid** ($CD$). This single compound token lets the reader see simultaneously:

1. The bisected diameter ($AO = OC$, invoking ``II.6``),
2. The right-triangle hypotenuse $OD = OC + CD$ (invoking :ref:`I.47 <byrne-i-47>`), and
3. The whole cutting line $AD = AO + OC + CD$ multiplied (:byrne-op:`rect-by`) by external part $CD$.

Exact Symbolic Verification over $\mathbb{Q}$
---------------------------------------------

In :func:`geometor.byrne.constructions.build_iii36`, circle radius $r = 3$, external point $D$ at distance $|OD| = 5$, external segment $|DC| = 2$, whole secant $|DA| = 8$, and rational contact point $T = (\frac{9}{5}, \frac{12}{5})$ satisfy $|DT|^2 = Q(D, T) = 16 = 8 \times 2 = |DA| \cdot |DC|$ identically over $\mathbb{Q}$.
