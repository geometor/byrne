.. _byrne-unit-2-notes:

Unit II Notes: Windmill Geometry, Stroke Disambiguation & The 1847 Title-Page Anomaly
=====================================================================================

.. rubric:: Archival & Symbolic Commentary on Book I

Archival Note: The 1847 Title-Page Transposition of ``I.47``
------------------------------------------------------------

Direct multimodal inspection of the 1847 Pickering volume reveals a delightful bibliographic detail between **Leaf 7 (Title Page)** and **Leaves 82–83 (pp. 48–49)**:

* On **pp. 48–49** (the actual proof of ``I.47``), the narrow left hypotenuse rectangle under the short leg is printed in **ochre yellow** (:byrne-rect:`yellow filled`, equal to the **black** leg square :byrne-sq:`black filled`) and the wide right hypotenuse rectangle under the long leg is printed in **Prussian blue** (:byrne-rect:`blue filled`, equal to the **red** leg square :byrne-sq:`red filled`).
* On the **1847 Title Page emblem** (Leaf 7), :person:`Whittingham's <whittingham>` pressman transposed the yellow and blue woodblocks on the bottom square (coloring the narrow left strip blue and the wide right rectangle yellow)! Our symbolic ``i47.svg`` plate faithfully follows the mathematically canonical proof plate on **pp. 48–49**.

Boundary Stroke Modulation in ``I.47``
--------------------------------------

In ``I.47``, the solid red square :byrne-sq:`red filled <i47:< A C K H >>` and solid blue rectangle :byrne-rect:`blue filled <i47:< C L M E >>` must also have their individual outer sides cited as 1D segments in the SAS congruence step (:just:`I.4`). Because a red solid line would vanish into a red solid square, Byrne prints the outer edge of the red square as :byrne-line:`blue dotted <i47:/ C K />` and the right edge of the blue rectangle as :byrne-line:`red dashed <i47:/ C E />`—a textbook resolution of :term:`chromatic register pressure <register-pressure>`.

Rational Trigonometry Invariants in ``geometor.byrne``
------------------------------------------------------

In :func:`geometor.byrne.constructions.build_i47`, ``I.47`` is modeled over pure rational coordinates $\mathbb{Q}$ ($B = (0, 0)$, $C = (5, 0)$, $A = (\frac{9}{5}, \frac{12}{5})$), giving exact integer quadrances $Q(A, B) = 9$, $Q(A, C) = 16$, $Q(B, C) = 25$, perpendicular spread $s(AB, AC) = 1$, and exact windmill-chord quadrance $Q(A, D) = Q(F, C) = \frac{290}{5} = 58$.
