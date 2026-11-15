:canonical_id: I.1.commentary
:book: I
:proposition: 1
:type: commentary
:title: Commentary — Proposition I.1
:folio: I.1
:page: 1

.. _byrne-i-1-commentary:

Commentary on Proposition I.1: Pointer-Free Genesis & Exact Q(sqrt(3)) Construction
===================================================================================

.. rubric:: Chiswick Press Register Design & Symbolic Verification (I.1 · G.84)

Visual Grammar & Pointer Elimination
------------------------------------

Whereas :person:`Heath's <heath>` classical translation (:cite:`1908 <heath:1908>`, ``geometor/euclid``) requires **179 words** and **31 alphabetic vertex-pointer lookups** (``AB``, ``BCD``, ``ACE``, ``CA``, ``CB``), :person:`Oliver Byrne <byrne>` reduces Proposition I.1 on Pickering **p. 1 (Leaf 35)** to **22 connecting words** and **zero pointer lookups** across six distinct visual registers:

* Given base :byrne-line:`black solid <i1:/ A B />`,
* Left circle :byrne-circle:`blue <i1:( A B )>` and right circle :byrne-circle:`red <i1:( B A )>`,
* Constructed legs :byrne-line:`yellow solid <i1:/ A C />` and :byrne-line:`red solid <i1:/ B C />`, and
* Resulting 3-color trilateral glyph :byrne-tri:`yellow/red/black <i1:< A B C >>`.

Exact Symbolic Model in ``geometor.byrne``
------------------------------------------

In :func:`geometor.byrne.constructions.build_i1`, setting $A = (0, 0)$ and $B = (2, 0)$ yields exact apex $C = (1, \sqrt{3})$ in $\mathbb{Q}(\sqrt{3})$ via ``Model.intersect``, with equal Rational Trigonometry quadrances:

.. math::

   Q(A, B) = Q(A, C) = Q(B, C) = 4, \qquad
   s(AB, AC) = s(BA, BC) = s(CA, CB) = \frac{3}{4}.
