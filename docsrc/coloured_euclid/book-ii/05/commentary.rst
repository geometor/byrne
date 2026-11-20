:canonical_id: II.5.commentary
:book: II
:proposition: 5
:order: 5
:type: commentary
:title: Commentary — Proposition II.5
:folio: 0092
:page: 58

.. _byrne-ii-5-commentary:


.. folio:: 0092
   :page: 58

Commentary on Proposition II.5: Gnomon Surgery & Completing the Square
======================================================================

.. rubric:: Pickering Folio 0092 (p. 58) & Quadratic Area Conservation (II.5 · G.148)

Algebraic Identity Behind ``II.5``
----------------------------------

Setting half-length $a = CB$ and offset $x = CD$, the unequal parts are $AD = a + x$ and $DB = a - x$, so Proposition II.5 expresses the universal identity:

.. math::

   (a + x)(a - x) + x^2 = a^2.

In :func:`geometor.byrne.constructions.build_ii5`, $A=(0,0), C=(4,0), D=(6,0), B=(8,0)$ over $\mathbb{Q}$ give $AD \cdot DB = 6 \times 2 = 12$ and $CD^2 = 2^2 = 4$ (:byrne-sq:`red filled <ii5:< H L G E >>`), summing identically to $CB^2 = 4^2 = 16$. Together with its twin ``II.6`` (external division, used in :ref:`II.11 <byrne-ii-11>` and :ref:`III.36 <byrne-iii-36>`), ``II.5`` forms the geometric engine of Renaissance Cossic quadratic solution (see ``geometor/pacioli``, *Summa* 1494).
