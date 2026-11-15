:canonical_id: I.32.commentary
:book: I
:proposition: 32
:type: commentary
:title: Commentary — Proposition I.32
:folio: I.32
:page: 33

.. _byrne-i-32-commentary:

Commentary on Proposition I.32: Parallel Transport of Angles & Euclid's Fifth Postulate Horizon
===============================================================================================

.. rubric:: Composite Angle Wedges & Rational Spread Identities (I.32 · G.125)

Composite Bicolor Wedges on Pickering p. 33
-------------------------------------------

On Pickering **p. 33 (Leaf 67)**, Byrne introduces **composite split-color angle wedges**: the exterior angle is printed as a single bicolor sector split by the parallel ray :byrne-line:`blue solid <i32:/ C E />`, and in the final line all three wedges around vertex $C$ are printed fused into one semicircular fan equal to :byrne-op:`two-right-angles`. One glance reveals how parallel transport reassembles the three dispersed interior angles at a single vertex.

Symbolic Verification & The Triple Spread Formula
-------------------------------------------------

In :func:`geometor.byrne.constructions.build_i32`, setting $E = C + (A - B)$ over $\mathbb{Q}$ enforces exact parallelism $(E - C) \times (A - B) = 0$, verifying alternate-angle spread equality $s(AB, AC) = s(CA, CE)$ and corresponding-angle spread equality $s(BA, BC) = s(CE, CD)$. In Rational Trigonometry (``geometor/wildberger``), Euclid's angle-sum law ``I.32`` translates algebraically into the polynomial **Triple Spread Formula** $(s_1 + s_2 + s_3)^2 = 2(s_1^2 + s_2^2 + s_3^2) + 4 s_1 s_2 s_3$.
