:canonical_id: I.46.commentary
:book: I
:proposition: 46
:order: 46
:type: commentary
:title: Commentary — Proposition I.46
:folio: 0081
:page: 47

.. _byrne-i-46-commentary:


.. folio:: 0081
   :page: 47

Commentary on Proposition I.46: Constructing the Orthogonal Unit Before the Pythagorean Climax
==============================================================================================

.. rubric:: Pickering Folio 0081 Verification & Parallel Metric Foundations (I.46 · G.139)

Pickering p. 47: Four Sides, Four Quadrants, Four Inks
------------------------------------------------------

On Pickering **p. 47 (Leaf 81)**, Byrne assigns each side of the constructed square a distinct ink (:byrne-line:`black solid <i46:/ A B />`, :byrne-line:`blue solid <i46:/ A C />`, :byrne-line:`red solid <i46:/ C D />`, :byrne-line:`yellow solid <i46:/ B D />`) and prints four quarter-disk right-angle sectors in permuted colors (:byrne-angle:`yellow <i46:< B A C )>`, :byrne-angle:`black <i46:< A C D )>`, :byrne-angle:`blue <i46:< C D B )>`, :byrne-angle:`red <i46:< D B A )>`) so every edge and every vertex angle remains uniquely addressable without a single letter. Notice that Byrne cites Simson's **Definition XXVII** (where Simson defines a square purely by four equal sides and four right angles, avoiding Euclid's redundant rhombic/rectangular clauses).

Exact Symbolic Model in ``geometor.byrne``
------------------------------------------

In :func:`geometor.byrne.constructions.build_i46`, $A=(0,0), B=(3,0), C=(0,3), D=(3,3)$ over $\mathbb{Q}$ verify equal side quadrances $Q = 9$ and unit orthogonal spreads $s(AB, AC) = s(CA, CD) = 1$, serving immediately as the subroutine invoked three times in :ref:`Proposition I.47 <byrne-i-47>`.
