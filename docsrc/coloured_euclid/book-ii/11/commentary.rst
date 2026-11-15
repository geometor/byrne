:canonical_id: II.11.commentary
:book: II
:proposition: 11
:type: commentary
:title: Commentary — Proposition II.11
:folio: II.11
:page: 66

.. _byrne-ii-11-commentary:

Commentary on Proposition II.11: Exact Q(phi) Area Cancellation & Gateway to the Pentagon
=========================================================================================

.. rubric:: Pickering Folio 0100 (p. 66) & Symbolic Golden Ratio Identity (II.11 · G.154)

Symbolic Verification in $\mathbb{Q}(\phi)$
-------------------------------------------

In :func:`geometor.byrne.constructions.build_ii11`, setting $|AB| = 1$ yields exact coordinates in $\mathbb{Q}(\sqrt{5}) = \mathbb{Q}(\phi)$:

.. math::

   |EB| = \frac{\sqrt{5}}{2}, \qquad
   |AH| = |AF| = \frac{\sqrt{5} - 1}{2} = \phi^{-1}, \qquad
   |HB| = 1 - \phi^{-1} = \frac{3 - \sqrt{5}}{2} = \phi^{-2}.

Both the blue golden square :byrne-sq:`blue filled <ii11:< A F G H >>` and the yellow complement rectangle :byrne-rect:`yellow filled <ii11:< H B D K >>` simplify in SymPy to the exact irrational area $\frac{3 - \sqrt{5}}{2} = 2 - \phi$, with difference identically ``0``. Notice how Byrne styles the divided line :byrne-line:`red solid-dotted <ii11:/ A H /; / H B />` as red solid (:byrne-line:`red solid <ii11:/ A H />`) concatenated with red dotted (:byrne-line:`red dotted <ii11:/ H B />`) so whole and parts remain visually linked yet algebraically distinct!
