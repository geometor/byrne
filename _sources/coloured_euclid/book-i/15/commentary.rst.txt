:canonical_id: I.15.commentary
:book: I
:proposition: 15
:type: commentary
:title: Commentary — Proposition I.15
:folio: I.15
:page: 15

.. _byrne-i-15-commentary:

Commentary on Proposition I.15: Four-Sector Partition & Algebraic Cancellation of Supplementary Angles
======================================================================================================

.. rubric:: Pickering Folio 0049 Verification & Spread Invariants (I.15 · G.104)

Pickering p. 15: Pure Visual Equations
--------------------------------------

Pickering **p. 15 (Leaf 49)** is one of the purest demonstrations in Byrne's *Elements*. Because four rays meeting at a point partition the full circle into exactly four sectors, Chiswick Press's four inks (:byrne-angle:`yellow <i15:< C E A )>`, :byrne-angle:`red <i15:< B E C )>`, :byrne-angle:`black <i15:< D E B )>`, :byrne-angle:`blue <i15:< A E D )>`) saturate the palette 1-to-1 without a single auxiliary stroke modifier. Subtracting the shared :byrne-angle:`red <i15:< B E C )>` sector from two :byrne-op:`two-right-angles` equations turns ``I.15`` into a three-line visual cancellation.

Symbolic Verification over $\mathbb{Q}$
---------------------------------------

In :func:`geometor.byrne.constructions.build_i15`, intersecting rational lines $AB$ and $CD$ at $E = (0, 0)$ yields exact equality of opposite spreads $s(EB, EC) = s(EA, ED)$ and $s(EC, EA) = s(ED, EB)$ over $\mathbb{Q}$—reflecting the projective fact that in Rational Trigonometry two lines define a single well-defined spread independent of ray orientation.
