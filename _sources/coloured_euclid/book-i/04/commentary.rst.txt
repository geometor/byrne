:canonical_id: I.4.commentary
:book: I
:proposition: 4
:order: 4
:type: commentary
:title: Commentary — Proposition I.4
:folio: 0038
:page: 4

.. _byrne-i-4-commentary:


.. folio:: 0038
   :page: 4

Commentary on Proposition I.4: Congruence-Twin Coloring & Superposition (*Epharmozein*)
=======================================================================================

.. rubric:: Chromatic Equivalence Classes & Rational Coordinates (I.4 · G.90)

Intentional Congruence-Twin Registers
-------------------------------------

Proposition I.4 (Pickering **p. 4, Leaf 38**) introduces Byrne's signature device for congruence theorems: **intentional register sharing** (:term:`congruence-twin <congruence-twin>`). Rather than assigning six distinct colors to the six sides of two triangles, Byrne colors corresponding parts with the *same* ink—making equality of hypothesis and conclusion visually isomorphic:

* Equal left legs share :byrne-line:`red solid <i4:/ A B /; / D E />`, equal right legs share :byrne-line:`blue solid <i4:/ A C /; / D F />`, and equal bases share :byrne-line:`black solid <i4:/ B C /; / E F />`.
* Opposite each colored side, Byrne assigns a complementary angle color (:byrne-angle:`red <i4:< A C B ); < D F E )>` opposite red leg, :byrne-angle:`blue <i4:< C B A ); < F E D )>` opposite blue leg, :byrne-angle:`yellow <i4:< B A C ); < E D F )>` opposite black base) so "angles subtended by equal sides" becomes an immediate chromatic pairing.

Symbolic Verification over $\mathbb{Q}$
---------------------------------------

In :func:`geometor.byrne.constructions.build_i4`, both triangles are modeled over $\mathbb{Q}$ via exact rational translation, confirming identical side quadrances $Q(A,B)=Q(D,E)$, $Q(A,C)=Q(D,F)$, $Q(B,C)=Q(E,F)$ and identical vertex spreads. Compare ``geometor/hilbert`` (*Axiom III.5*), where Hilbert elevates ``I.4`` from a superposition argument (*epharmozein*, :just:`C.N.4`) to an explicit congruence axiom.
