:canonical_id: IV.4.commentary
:book: IV
:proposition: 4
:type: commentary
:title: Commentary — Proposition IV.4
:folio: IV.4
:page: 129

.. _byrne-iv-4-commentary:

Commentary on Proposition IV.4: Color-Matched Dotted Inradii & Heronian 13-14-15 Integer Coordinates
====================================================================================================

.. rubric:: Pickering Folio 0163 (p. 129) & Kimberling X(1) Incenter over Q (IV.4 · G.217)

Color-Matched Solid Sides & Dotted Perpendiculars
-------------------------------------------------

On Pickering **p. 129 (Leaf 163)**, Byrne pairs each solid triangle side with a **dotted inradius of the exact same color**:

* :byrne-line:`black dotted <iv4:/ I E />` :byrne-op:`perp` :byrne-line:`black solid <iv4:/ B C />`,
* :byrne-line:`yellow dotted <iv4:/ I F />` :byrne-op:`perp` :byrne-line:`yellow solid <iv4:/ A B />`, and
* :byrne-line:`red dotted <iv4:/ I G />` :byrne-op:`perp` :byrne-line:`red solid <iv4:/ A C />`,

reserving **blue** (:byrne-line:`blue dotted <iv4:/ B I />` and :byrne-line:`blue solid <iv4:/ C I />`) exclusively for the two angle bisectors! Every geometric role is decoded instantly by ``(color, stroke)`` without a single letter.

Heronian ``13-14-15`` Integer Incircle in ``geometor.byrne``
------------------------------------------------------------

In :func:`geometor.byrne.constructions.build_iv4`, placing $B = (0, 0)$, $C = (14, 0)$, $A = (5, 12)$ yields exact integer side lengths $(13, 14, 15)$, area $84$, semiperimeter $s = 21$, integer incenter $I = X(1) = (6, 4)$ (cross-referenced to ``geometor/etc``), integer inradius $r = 4$ ($Q(I,E)=Q(I,F)=Q(I,G)=16$), and exact rational touchpoints $E=(6,0)$, $F=(\frac{30}{13}, \frac{72}{13})$, $G=(\frac{46}{5}, \frac{32}{5})$.
