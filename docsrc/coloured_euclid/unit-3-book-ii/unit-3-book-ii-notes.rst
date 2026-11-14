.. _byrne-unit-3-notes:

Unit III Notes: Exact $\mathbb{Q}(\phi)$ Coordinates & Half-Filled Woodblocks
=============================================================================

.. rubric:: Typographic & Symbolic Commentary on Book II

Why Byrne Invented Half-Filled Squares in ``II.4``
--------------------------------------------------

Inspection of Pickering **pp. 56–57** (Leaves 90–91) shows a striking Chiswick Press graphic device: instead of printing the two diagonal sub-squares in solid ink, :person:`Byrne <byrne>` fills only the upper-left triangle of each square while outlining the boundary (:byrne-sq:`blue half`, :byrne-sq:`red half`). Why? Because in ``II.4`` Euclid first proves that the two sub-triangles cut by the diagonal are isosceles (:just:`I.6`) before concluding that the four-sided figures are squares! Half-filling makes both the constituent triangle *and* the enclosing square simultaneously visible in a single woodblock impression.

Symbolic Verification in $\mathbb{Q}(\phi)$
-------------------------------------------

In :func:`geometor.byrne.constructions.build_ii11`, setting $|AB| = 1$ yields exact coordinates in $\mathbb{Q}(\sqrt{5})$:

.. math::

   |EB| = \frac{\sqrt{5}}{2}, \qquad
   |AH| = |AF| = \frac{\sqrt{5} - 1}{2} = \phi^{-1}, \qquad
   |HB| = 1 - \phi^{-1} = \frac{3 - \sqrt{5}}{2} = \phi^{-2}.

Both the blue golden square ``< A F G H >`` and the yellow complement rectangle ``< H B D K >`` simplify in SymPy to the exact irrational area $\frac{3 - \sqrt{5}}{2} = 2 - \phi$, with difference identically ``0``.
