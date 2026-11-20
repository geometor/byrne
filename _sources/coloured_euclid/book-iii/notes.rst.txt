:book: III
:type: notes
:title: Book III Notes — Multi-Case Plates & Rational Circle Models
:folio: 0105
:page: 71

.. _byrne-book-iii-notes:
.. _byrne-unit-4-notes:

Book III Notes: Multi-Case Plates & Rational Circle Parameterizations
=====================================================================

.. rubric:: Chiswick Press Case Splits & Exact Rational Points on the Circle

.. folio:: 0105
   :page: 71

Multi-Figure Layouts on Pickering pp. 102, 115 & 121
----------------------------------------------------

In Book III, Euclid frequently distinguishes geometric configurations according to whether the circle's center lies *on*, *within*, or *outside* an inscribed angle (:ref:`III.20 <byrne-iii-20>`, p. 102) or whether a secant passes *through* or *aside from* the center (:ref:`III.36 <byrne-iii-36>`, p. 121). On these pages, Whittingham sets ``FIGURE I`` and ``FIGURE II`` vertically on the same quarto leaf, reusing the color semantics across both cases.

Pythagorean Rational Points on Circles in ``geometor.byrne``
------------------------------------------------------------

Using the rational circle parameterization $(\frac{1-t^2}{1+t^2}, \frac{2t}{1+t^2})$, all three Book III showcase models (:func:`~geometor.byrne.constructions.build_iii20`, :func:`~geometor.byrne.constructions.build_iii31`, :func:`~geometor.byrne.constructions.build_iii36`) place every center, chord endpoint, and tangent contact at **exact rational coordinates** in $\mathbb{Q}$ without introducing square roots.
