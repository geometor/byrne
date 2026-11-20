:canonical_id: I.47.commentary
:book: I
:proposition: 47
:order: 47
:type: commentary
:title: Commentary — Proposition I.47
:folio: 0082
:page: 48

.. _byrne-i-47-commentary:


.. folio:: 0082
   :page: 48

Commentary on Proposition I.47: Euclid's Windmill, Boundary Stroke Modulation & Rational Coordinates
====================================================================================================

.. rubric:: Pickering Folios 0082–0083 (pp. 48–49) & Exact Q Invariants (I.47 · G.140)

Boundary Stroke Modulation Under Register Pressure
--------------------------------------------------

In ``I.47`` (Pickering **pp. 48–49, Leaves 82–83**), the solid red square :byrne-sq:`red filled <i47:< A C K H >>` and solid blue rectangle :byrne-rect:`blue filled <i47:< C L M E >>` must also have their outer edges cited as 1D segments in the SAS congruence step (:just:`I.4`). Because a red solid line would vanish into a red solid square, Byrne prints the outer edge of the red square as :byrne-line:`blue dotted <i47:/ C K />` and the right edge of the blue rectangle as :byrne-line:`red dashed <i47:/ C E />`—a textbook resolution of :term:`chromatic register pressure <register-pressure>`, reducing Heath's **314 words** and **64 vertex pointers** to **25 words** and **zero pointers**.

Exact Rational Trigonometry Model in ``geometor.byrne``
-------------------------------------------------------

In :func:`geometor.byrne.constructions.build_i47`, ``I.47`` is modeled over pure rational coordinates $\mathbb{Q}$ ($B = (0, 0)$, $C = (5, 0)$, $A = (\frac{9}{5}, \frac{12}{5})$), yielding exact integer leg and hypotenuse quadrances:

.. math::

   Q(A, B) = 9, \qquad Q(A, C) = 16, \qquad Q(B, C) = 25 = 9 + 16,

perpendicular spread $s(AB, AC) = 1$, altitude foot $L = (\frac{9}{5}, 0)$ partitioning the hypotenuse square into area $5 \times \frac{9}{5} = 9$ (:byrne-rect:`yellow filled <i47:< B L M D >>`) and area $5 \times \frac{16}{5} = 16$ (:byrne-rect:`blue filled <i47:< C L M E >>`), and equal windmill-chord quadrances $Q(A, D) = Q(F, C) = 58$.
