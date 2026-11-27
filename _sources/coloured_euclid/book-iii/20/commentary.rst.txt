:canonical_id: III.20.commentary
:book: III
:proposition: 20
:order: 20
:type: commentary
:title: Commentary — Proposition III.20
:folio: 0136
:page: 102

.. _byrne-iii-20-commentary:


.. folio:: 0136
   :page: 102

Commentary on Proposition III.20: Double-Angle Spread Law & Isosceles Radius Triangles
======================================================================================

.. rubric:: Pickering Folio 0136 (p. 102) & Rational Spread Verification (III.20 · G.185)

Visual Clarity of Pickering p. 102
----------------------------------

On Pickering **p. 102 (Leaf 136)**, Byrne draws the diameter through the inscribed vertex as :byrne-line:`red solid-dotted <iii20:/ A O /; / O D />`—solid red along radius :math:`AO` so it pairs visually with equal radius :math:`OB`, and dotted red along continuation :math:`OD` so it frames the exterior central sector :byrne-angle:`blue <iii20:< B O C )>`.

Double-Angle Spread Identity over :math:`\mathbb{Q}`
----------------------------------------------------

In :func:`geometor.byrne.constructions.build_iii20`, points :math:`O=(0,0)` and rational circle points :math:`A, B, C \in \mathbb{Q}^2` satisfy Rational Trigonometry's **double-spread polynomial** identically:

.. math::

   s_{\text{central}} = 4 s_{\text{inscribed}} (1 - s_{\text{inscribed}}),

where :math:`s_{\text{inscribed}} = s(AB, AC)` and :math:`s_{\text{central}} = s(OB, OC)`.
