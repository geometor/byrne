:canonical_id: III.31.commentary
:book: III
:proposition: 31
:type: commentary
:title: Commentary — Proposition III.31
:folio: III.31
:page: 115

.. _byrne-iii-31-commentary:

Commentary on Proposition III.31: Split Semicircular Angle Wedge & Unit Spread Orthogonality
============================================================================================

.. rubric:: Pickering Folio 0149 (p. 115) & Exact Rational Semicircle (III.31 · G.196)

Bicolor Decomposition of the Inscribed Right Angle
--------------------------------------------------

On Pickering **p. 115 (Leaf 149)**, Byrne renders the inscribed angle at $A$ as a single split bicolor glyph :byrne-angle:`yellow+black <iii31:< B A O ); < O A C )>` partitioned by median radius :byrne-line:`red solid <iii31:/ O A />`. Because :byrne-angle:`yellow <iii31:< B A O )>` = :byrne-angle:`red <iii31:< O B A )>` in the left isosceles triangle and :byrne-angle:`black <iii31:< O A C )>` = :byrne-angle:`blue <iii31:< A C O )>` in the right isosceles triangle, the composite apex angle visibly equals the sum of the two remaining triangle angles—hence exactly half of :byrne-op:`two-right-angles`!

Exact Rational Model in ``geometor.byrne``
------------------------------------------

In :func:`geometor.byrne.constructions.build_iii31`, diameter $B=(-5,0), C=(5,0)$ and apex $A=(-3,4)$ on circle $x^2+y^2=25$ give equal radius quadrances $Q(O,B)=Q(O,A)=Q(O,C)=25$ and exact perpendicular spread $s(AB, AC) = 1$.
