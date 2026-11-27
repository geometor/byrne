:canonical_id: IV.11.commentary
:book: IV
:proposition: 11
:order: 11
:type: commentary
:title: Commentary — Proposition IV.11
:folio: 0171
:page: 137

.. _byrne-iv-11-commentary:


.. folio:: 0171
   :page: 137

Commentary on Proposition IV.11: Five Pentagon Sides in Four Inks & Exact Pentagonal Quadrances
===============================================================================================

.. rubric:: Pickering Folio 0171 (p. 137) & Pentagonal Radical Tower (IV.11 · G.224)

Register-Pressure Resolution via ``red dotted``
-----------------------------------------------

Pickering **p. 137 (Leaf 171)** is one of the finest illustrations of :term:`register pressure <register-pressure>` in the 1847 Chiswick Press edition: with solid yellow occupied by the central Golden Triangle :byrne-tri:`yellow filled <iv11:< A C D >>` and four solid inks assigned to four perimeter sides (:byrne-line:`black solid <iv11:/ C D />`, :byrne-line:`red solid <iv11:/ A B />`, :byrne-line:`blue solid <iv11:/ E A />`, :byrne-line:`yellow solid <iv11:/ D E />`), Byrne encodes the fifth chord :math:`BC` as :byrne-line:`red dotted <iv11:/ B C />` so all five sides appear distinctly in the final visual equality.

Exact Symbolic Verification in ``geometor.byrne``
-------------------------------------------------

In :func:`geometor.byrne.constructions.build_iv11`, all five vertices lie exactly on the unit circle over :math:`\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})`:

.. math::

   Q_{\text{side}} = \frac{5 - \sqrt{5}}{2} = 3 - \phi, \qquad
   Q_{\text{diag}} = \frac{5 + \sqrt{5}}{2} = 2 + \phi, \qquad
   \frac{Q_{\text{diag}}}{Q_{\text{side}}} = \phi^2 = \frac{3 + \sqrt{5}}{2},

preparing the direct lift to the regular icosahedron and dodecahedron in Book XIII (and :person:`Pacioli's <byrne>` *De Divina Proportione* in ``geometor/pacioli``).
