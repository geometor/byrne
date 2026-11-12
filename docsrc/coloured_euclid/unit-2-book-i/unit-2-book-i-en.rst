:layout: book

.. _byrne-unit-2-en:

Unit II: Book I — Congruence, Parallels & The Pythagorean Theorem
=================================================================

.. rubric:: Showcase Propositions of Book I (Pickering pp. 1–50, Leaves 35–84)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. folio:: I.1
   :page: 1

Proposition I. Problem (*Equilateral Triangle*, p. 1 · ``G.84``)
----------------------------------------------------------------

*On a given finite straight line* (:byrne-line:`black solid <i1:/ A B />`) *to describe an equilateral triangle.*

.. picture:: /_static/figures/i1.svg
   :alt: Book I Proposition 1 — Equilateral triangle constructed by blue and red circles on black base.
   :caption: **Book I, Prop. I (p. 1).** Exact $\mathbb{Q}(\sqrt{3})$ construction via ``Model.intersect``.

.. container:: byrne-eq-block

   **Construction.** From the extremities of :byrne-line:`black solid <i1:/ A B />` describe :byrne-circle:`blue <i1:( A B )>` and :byrne-circle:`red <i1:( B A )>` (:just:`I.post.3`); from their intersection draw :byrne-line:`yellow solid <i1:/ A C />` and :byrne-line:`red solid <i1:/ B C />` (:just:`I.post.1`).

   **Demonstration.**

   :byrne-line:`yellow solid <i1:/ A C />` = :byrne-line:`black solid <i1:/ A B />` (:just:`I.def.15`, radii of :byrne-circle:`blue <i1:( A B )>`),

   :byrne-line:`red solid <i1:/ B C />` = :byrne-line:`black solid <i1:/ A B />` (:just:`I.def.15`, radii of :byrne-circle:`red <i1:( B A )>`),

   :byrne-op:`therefore` :byrne-line:`yellow solid <i1:/ A C />` = :byrne-line:`red solid <i1:/ B C />` = :byrne-line:`black solid <i1:/ A B />` (:just:`C.N.1`).

   :byrne-op:`therefore` :byrne-tri:`yellow/red/black <i1:< A B C >>` is equilateral (:just:`I.def.20`). **Q.E.F.**

.. folio:: I.4
   :page: 4

Proposition IV. Theorem (*Side-Angle-Side Congruence*, p. 4 · ``G.90``)
-----------------------------------------------------------------------

*If two triangles have two sides of the one equal to two sides of the other, each to each, and have likewise the angles contained by those sides equal to one another, they shall have their bases equal, and the two triangles shall be equal, and their other angles shall be equal, each to each.*

.. picture:: /_static/figures/i4.svg
   :alt: Book I Proposition 4 — Two congruent triangles with matching red, blue, and black sides and yellow, blue, and red angle wedges.
   :caption: **Book I, Prop. IV (p. 4).** Identical color registers encode corresponding sides and subtended angles across both triangles.

.. container:: byrne-eq-block

   **Given.** Two triangles having :byrne-line:`red solid <i4:/ A B /; / D E />` equal, :byrne-line:`blue solid <i4:/ A C /; / D F />` equal, and contained apex angles :byrne-angle:`yellow <i4:< B A C ); < E D F )>` equal.

   **Demonstration.** Superposing the first triangle upon the second so that equal :byrne-line:`red solid <i4:/ A B /; / D E />` and :byrne-angle:`yellow <i4:< B A C ); < E D F )>` coincide (:just:`C.N.4`), :byrne-line:`blue solid <i4:/ A C /; / D F />` coincides, whence bases :byrne-line:`black solid <i4:/ B C /; / E F />` coincide (Axiom X),

   :byrne-op:`therefore` :byrne-angle:`blue <i4:< C B A ); < F E D )>` are equal and :byrne-angle:`red <i4:< A C B ); < D F E )>` are equal. **Q.E.D.**

.. folio:: I.5
   :page: 5

Proposition V. Theorem (*Pons Asinorum*, p. 5 · ``G.91``)
---------------------------------------------------------

*The angles at the base of an isosceles triangle are equal to one another; and if the equal sides be produced, the angles upon the other side of the base shall be equal.*

.. picture:: /_static/figures/i5.svg
   :alt: Book I Proposition 5 — Pons Asinorum with red isosceles legs, yellow extensions, blue cross-diagonals, and symmetric colored angle sectors.
   :caption: **Book I, Prop. V (p. 5).** :term:`Congruence-twin coloring <congruence-twin>` turns mirror-symmetric triangles into immediate visual equations.

.. container:: byrne-eq-block

   **Construction.** Produce equal legs :byrne-line:`red solid <i5:/ A B /; / A C />` by equal extensions :byrne-line:`yellow solid <i5:/ B F /; / C G />` (:just:`I.post.2`, :just:`I.3`), and join cross-lines :byrne-line:`blue solid <i5:/ F C /; / G B />` (:just:`I.post.1`).

   **Demonstration.**

   :byrne-line:`red solid <i5:/ A B />` + :byrne-line:`yellow solid <i5:/ B F />` = :byrne-line:`red solid <i5:/ A C />` + :byrne-line:`yellow solid <i5:/ C G />` (:just:`C.N.2`), with common apex :byrne-angle:`black <i5:< B A C )>`.

   :byrne-op:`therefore` :byrne-line:`blue solid <i5:/ F C />` = :byrne-line:`blue solid <i5:/ G B />` and lower angles :byrne-angle:`red <i5:< C F A ); < A G B )>` are equal (:just:`I.4`).

   In the lower triangles on common base :byrne-line:`black solid <i5:/ B C />`, :byrne-angle:`yellow <i5:< F B C )>` = :byrne-angle:`yellow <i5:< B C G )>` (:just:`I.4`).

   Subtracting equal parts from equal whole angles (:just:`C.N.3`),

   :byrne-op:`therefore` interior base angles :byrne-angle:`blue <i5:< C B A )>` = :byrne-angle:`blue <i5:< A C B )>`. **Q.E.D.**

.. folio:: I.15 & I.32
   :page: 15

Propositions XV & XXXII (*Vertical Angles & Angle Sum of a Triangle*, pp. 15, 33)
---------------------------------------------------------------------------------

.. picture:: /_static/figures/i15.svg
   :alt: Book I Proposition 15 — Intersecting black and red straight lines forming red, yellow, blue, and black vertical angle sectors.
   :caption: **Book I, Prop. XV (p. 15 · G.104).** Adjacent supplementary pairs cancel common sectors to prove vertical angle equality.

.. container:: byrne-eq-block

   **Prop. XV Demonstration (:just:`I.13`, :just:`C.N.3`).**

   :byrne-angle:`red <i15:< B E C )>` + :byrne-angle:`yellow <i15:< C E A )>` = :byrne-op:`two-right-angles` = :byrne-angle:`yellow <i15:< C E A )>` + :byrne-angle:`blue <i15:< A E D )>`

   :byrne-op:`therefore` :byrne-angle:`red <i15:< B E C )>` = :byrne-angle:`blue <i15:< A E D )>`, and similarly :byrne-angle:`yellow <i15:< C E A )>` = :byrne-angle:`black <i15:< D E B )>`. **Q.E.D.**

.. picture:: /_static/figures/i32.svg
   :alt: Book I Proposition 32 — Triangle with parallel blue auxiliary line splitting the exterior angle into alternate and corresponding components.
   :caption: **Book I, Prop. XXXII (p. 33 · G.125).** Parallel line :byrne-line:`blue solid <i32:/ C E />` transports both remote interior angles into the exterior angle.

.. container:: byrne-eq-block

   **Prop. XXXII Demonstration (:just:`I.31`, :just:`I.29`, :just:`I.13`).**

   Draw :byrne-line:`blue solid <i32:/ C E />` :byrne-op:`parallel` :byrne-line:`black solid <i32:/ B A />` (:just:`I.31`).

   :byrne-angle:`red <i32:< E C A )>` = :byrne-angle:`blue <i32:< B A C )>` (alternate, :just:`I.29`), and :byrne-angle:`black <i32:< D C E )>` = :byrne-angle:`yellow <i32:< C B A )>` (corresponding, :just:`I.29`).

   :byrne-op:`therefore` exterior (:byrne-angle:`red <i32:< E C A )>` + :byrne-angle:`black <i32:< D C E )>`) = :byrne-angle:`blue <i32:< B A C )>` + :byrne-angle:`yellow <i32:< C B A )>`,

   and adding interior :byrne-angle:`black <i32:< A C B )>` to both yields :byrne-angle:`blue <i32:< B A C )>` + :byrne-angle:`yellow <i32:< C B A )>` + :byrne-angle:`black <i32:< A C B )>` = :byrne-op:`two-right-angles`. **Q.E.D.**

.. folio:: I.46 & I.47
   :page: 47

Propositions XLVI & XLVII (*The Square & The Pythagorean Theorem*, pp. 47–49)
-----------------------------------------------------------------------------

.. picture:: /_static/figures/i46.svg
   :alt: Book I Proposition 46 — Construction of a square with black, blue, red, and yellow sides and four colored right-angle quadrants.
   :caption: **Book I, Prop. XLVI (p. 47 · G.139).** Construction of the square on :byrne-line:`black solid <i46:/ A B />`.

.. picture:: /_static/figures/i47.svg
   :alt: Book I Proposition 47 — Oliver Byrne's four-color Pythagorean Theorem plate with black and red squares equal to yellow and blue hypotenuse rectangles.
   :caption: **Book I, Prop. XLVII (pp. 48–49 · G.140).** Byrne's masterpiece: Euclid's windmill proof rendered as coloured area conservation.

.. container:: byrne-eq-block

   **Given.** Right-angled triangle with hypotenuse :byrne-line:`red solid <i47:/ B C />` subtending the right angle between legs :byrne-line:`yellow solid <i47:/ A B />` and :byrne-line:`blue solid <i47:/ A C />`.

   **Construction.** Describe :byrne-sq:`black filled <i47:< A B F G >>` and :byrne-sq:`red filled <i47:< A C K H >>` (:just:`I.46`), and divide the hypotenuse square by :byrne-line:`black dotted <i47:/ A M />` (:just:`I.31`) into :byrne-rect:`yellow filled <i47:< B L M D >>` and :byrne-rect:`blue filled <i47:< C L M E >>`; draw windmill chords :byrne-line:`black solid <i47:/ A D />` and :byrne-line:`black solid <i47:/ F C />` (:just:`I.post.1`).

   **Demonstration.**

   By collinearity of adjacent right angles (:just:`I.14`), SAS congruence of the rotated windmill triangles (:just:`I.4`), and double-area parallelograms between the same parallels (:just:`I.41`):

   :byrne-sq:`black filled <i47:< A B F G >>` = :byrne-rect:`yellow filled <i47:< B L M D >>`,

   and symmetrically on the right leg (:byrne-line:`blue dotted <i47:/ C K />`, :byrne-line:`red dashed <i47:/ C E />`):

   :byrne-sq:`red filled <i47:< A C K H >>` = :byrne-rect:`blue filled <i47:< C L M E >>`.

   :byrne-op:`therefore` :byrne-rect:`yellow filled <i47:< B L M D >>` + :byrne-rect:`blue filled <i47:< C L M E >>` = :byrne-sq:`black filled <i47:< A B F G >>` + :byrne-sq:`red filled <i47:< A C K H >>` (:just:`C.N.2`). **Q.E.D.**
