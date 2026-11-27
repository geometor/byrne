:canonical_id: I.5.commentary
:book: I
:proposition: 5
:order: 5
:type: commentary
:title: Commentary — Proposition I.5
:folio: 0039
:page: 5

.. _byrne-i-5-commentary:


.. folio:: 0039
   :page: 5

Commentary on Proposition I.5: Untangling the Bridge of Asses via Symmetric Color Twins
=======================================================================================

.. rubric:: Mirror-Symmetric Register Analysis & Rational Quadrances (I.5 · G.91)

Why ``I.5`` Earned the Name *Pons Asinorum*—and How Byrne Tames It
------------------------------------------------------------------

In classical alphabetic editions, Proposition I.5 requires **329 words** and **62 three-letter vertex-pointer dereferences** because four overlapping triangles (``AFC``, ``AGB``, ``BFC``, ``CGB``) share vertices ``A, B, C, F, G``. On Pickering **p. 5 (Leaf 39)**, Byrne assigns bilateral mirror twins (:byrne-line:`red solid <i5:/ A B /; / A C />`, :byrne-line:`yellow solid <i5:/ B F /; / C G />`, :byrne-line:`blue solid <i5:/ F C /; / G B />`, :byrne-angle:`yellow <i5:< F B C ); < B C G )>`, :byrne-angle:`blue <i5:< C B A ); < A C B )>`), compressing the proof to **32 words** (90.3% compression) and **zero pointer lookups**.

Exact Symbolic Model in ``geometor.byrne``
------------------------------------------

In :func:`geometor.byrne.constructions.build_i5`, the isosceles triangle and its auxiliary extensions are constructed over exact rational coordinates :math:`\mathbb{Q}`, verifying :math:`Q(A,B)=Q(A,C)`, :math:`Q(F,C)=Q(G,B)`, and exact equality of base spreads :math:`s(BA, BC) = s(CA, CB)` as well as exterior spreads :math:`s(BF, BC) = s(CG, CB)`. (Compare :person:`Pappus's <pappus>` self-congruence shortcut in :person:`Proclus <proclus>`, ``geometor/proclus``.)
