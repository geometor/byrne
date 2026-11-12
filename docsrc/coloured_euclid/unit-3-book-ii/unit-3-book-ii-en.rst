:layout: book

.. _byrne-unit-3-en:

Unit III: Book II — Geometric Algebra & The Golden Section
==========================================================

.. rubric:: Coloured Rectangles, Gnomons & Extreme and Mean Ratio (Pickering pp. 51–71, Leaves 85–105)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

Book II Definitions: Contained Rectangles & The Gnomon (p. 51)
--------------------------------------------------------------

* **Definition I.** Every right-angled parallelogram is said to be *contained* (:byrne-op:`rect-by`) by any two of the straight lines which contain one of the right angles.
* **Definition II.** In every parallelogram, any of the parallelograms about a diameter, together with the two complements, is called a :term:`gnomon <gnomon>`.

.. folio:: II.4
   :page: 56

Proposition IV. Theorem (*Binomial Square*, pp. 56–57 · ``G.147``)
------------------------------------------------------------------

*If a straight line be divided into any two parts* (:byrne-line:`blue solid <ii4:/ A C />` + :byrne-line:`red solid <ii4:/ C B />`), *the square on the whole line is equal to the squares on the two parts, together with twice the rectangle contained by the parts.*

.. picture:: /_static/figures/ii4.svg
   :alt: Book II Proposition 4 — Binomial square partitioned into diagonal half-filled blue and red squares and two solid yellow rectangles.
   :caption: **Book II, Prop. IV (pp. 56–57).** $(a + b)^2 = a^2 + b^2 + 2ab$ made immediately legible by half-filled diagonal squares and solid yellow complements.

.. container:: byrne-eq-block

   **Demonstration (:just:`I.46`, :just:`I.31`, :just:`I.29`, :just:`I.6`, :just:`I.43`).**

   Along diagonal :byrne-line:`black solid <ii4:/ D G />` + :byrne-line:`black dotted <ii4:/ G B />`, the two parallelograms about the diameter are equilateral right-angled squares (:byrne-sq:`blue half <ii4:< D K G H >>` = :byrne-line:`blue solid squared <ii4:/ A C />` and :byrne-sq:`red half <ii4:< G F B C >>` = :byrne-line:`red solid squared <ii4:/ C B />`), while the two complements :byrne-rect:`yellow filled <ii4:< H G C A >>` and :byrne-rect:`yellow filled <ii4:< K E F G >>` are equal (:just:`I.43`) and each equals :byrne-line:`blue solid <ii4:/ A C />` :byrne-op:`rect-by` :byrne-line:`red solid <ii4:/ C B />`.

   :byrne-op:`therefore` whole square = :byrne-sq:`blue half <ii4:< D K G H >>` + :byrne-sq:`red half <ii4:< G F B C >>` + 2 × :byrne-rect:`yellow filled <ii4:< H G C A >>`. **Q.E.D.**

.. folio:: II.5
   :page: 58

Proposition V. Theorem (*Equal & Unequal Division*, p. 58 · ``G.148``)
----------------------------------------------------------------------

*If a straight line be divided into two equal parts and also into two unequal parts, the rectangle contained by the unequal parts, together with the square on the line between the points of section, is equal to the square on the half.*

.. picture:: /_static/figures/ii5.svg
   :alt: Book II Proposition 5 — Half-square decomposed into red inner square plus L-shaped gnomon equal to the rectangle of unequal segments.
   :caption: **Book II, Prop. V (p. 58).** $AD \cdot DB + CD^2 = CB^2$ via :term:`gnomon <gnomon>` equivalence.

.. container:: byrne-eq-block

   **Demonstration (:just:`I.43`, :just:`C.N.2`).**

   Left wing :byrne-rect:`black filled <ii5:< A C H K >>` equals vertical complement :byrne-rect:`yellow filled <ii5:< L M F G >>`. Adding :byrne-rect:`yellow filled <ii5:< C D L H >>` to each transforms the rectangle of unequal parts into the L-shaped :term:`gnomon <gnomon>`; adding inner :byrne-sq:`red filled <ii5:< H L G E >>` completes the square on the half-line! **Q.E.D.**

.. folio:: II.11
   :page: 66

Proposition XI. Problem (*The Golden Section by Colored Areas*, p. 66 · ``G.154``)
----------------------------------------------------------------------------------

*To divide a given straight line* (:byrne-line:`red solid-dotted <ii11:/ A H /; / H B />`) *into two parts, so that the rectangle contained by the whole and one of the parts may be equal to the square on the other part.*

.. picture:: /_static/figures/ii11.svg
   :alt: Book II Proposition 11 — Golden section construction showing blue golden square equal in area to yellow complement rectangle.
   :caption: **Book II, Prop. XI (p. 66).** Pure $\mathbb{Q}(\phi)$ area proof of the :term:`Golden Section <extreme-and-mean-ratio>` prior to Book V proportion theory.

.. container:: byrne-eq-block

   **Construction.** Describe the unit square on the given line, bisect the left vertical side at $E$ (:just:`I.10`), join oblique secant :byrne-line:`black solid <ii11:/ E B />` (:just:`I.post.1`), step off $EF = EB$ upward (:just:`I.3`), and describe the golden square :byrne-sq:`blue filled <ii11:< A F G H >>` (:just:`I.46`), partitioning the main square into shared strip :byrne-rect:`blue outline <ii11:< A H K C >>` and right rectangle :byrne-rect:`yellow filled <ii11:< H B D K >>`.

   **Demonstration.**

   By ``II.6`` applied to the bisected vertical side and :just:`I.47` on the right triangle containing :byrne-line:`black solid <ii11:/ E B />`:

   (:byrne-sq:`blue filled <ii11:< A F G H >>` + :byrne-rect:`blue outline <ii11:< A H K C >>`) = (:byrne-rect:`blue outline <ii11:< A H K C >>` + :byrne-rect:`yellow filled <ii11:< H B D K >>`).

   Subtracting the common strip :byrne-rect:`blue outline <ii11:< A H K C >>` from both (:just:`C.N.3`),

   :byrne-op:`therefore` :byrne-sq:`blue filled <ii11:< A F G H >>` = :byrne-rect:`yellow filled <ii11:< H B D K >>`, i.e. :byrne-line:`red solid squared <ii11:/ A H />` = whole line :byrne-op:`rect-by` :byrne-line:`red dotted <ii11:/ H B />`. **Q.E.F.**
