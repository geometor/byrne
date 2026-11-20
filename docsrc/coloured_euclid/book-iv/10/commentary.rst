:canonical_id: IV.10.commentary
:book: IV
:proposition: 10
:order: 10
:type: commentary
:title: Commentary — Proposition IV.10
:folio: 0169
:page: 135

.. _byrne-iv-10-commentary:


.. folio:: 0169
   :page: 135

Commentary on Proposition IV.10: Golden Ratio Meets Tangent-Chord Geometry in Q(phi, sqrt(10 - 2*sqrt(5)))
==========================================================================================================

.. rubric:: Pickering Folios 0169–0170 (pp. 135–136) & Cyclotomic Field Verification (IV.10 · G.223)

Architectural Keystone of Books I–IV
------------------------------------

Pickering **pp. 135–136 (Leaves 169–170)** unite four books of the *Elements* in a single two-circle plate (:byrne-circle:`red <iv10:( A B )>` and :byrne-circle:`blue <iv10:( P A )>`):

1. Golden area division (:ref:`II.11 <byrne-ii-11>`) supplies $|AB| \cdot |CB| = |AC|^2$;
2. Setting $|BD| = |AC|$ converts that area equality into tangent-secant power $|AB| \cdot |CB| = |BD|^2$, proving $BD$ tangent to circumcircle $(ACD)$ (``III.37``);
3. Tangent-chord equality (``III.32``) transfers the $36^\circ$ apex angle into $\triangle BCD$, revealing three equal $\phi^{-1}$ segments ($AC = CD = BD$) and base angles $72^\circ = 2 \times 36^\circ$.

Exact Symbolic Field in ``geometor.byrne``
------------------------------------------

In :func:`geometor.byrne.constructions.build_iv10`, unit legs $|AB| = |AD| = 1$ and base $|BD| = \phi^{-1} = \frac{\sqrt{5}-1}{2}$ lie in $\mathbb{Q}(\phi, \sqrt{10 - 2\sqrt{5}})$, with apex spread $s_{36^\circ} = \frac{5 - \sqrt{5}}{8}$ and base spread $s_{72^\circ} = \frac{5 + \sqrt{5}}{8} = 4 s_{36^\circ}(1 - s_{36^\circ})$.
