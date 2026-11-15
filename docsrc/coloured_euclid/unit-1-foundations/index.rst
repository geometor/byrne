:layout: book
:type: book
:order: 0
:title: Preliminaries — Introduction, Definitions, Postulates, Axioms & Symbols
:folio: Introduction
:page: vii

.. _byrne-preliminaries:
.. _byrne-unit-1-en:

Preliminaries — Introduction, Definitions, Postulates, Axioms & Symbols
=======================================================================

.. rubric:: Oliver Byrne — *Pickering Edition* (pp. vii–xxix, Leaves 11–33)

:person:`Oliver Byrne's <byrne>` 1847 *Introduction* establishes the manifesto of **pointer-free visual deduction**: geometric primitives are colored in Chiswick Press vermilion, ultramarine, gamboge, and lampblack so they *name themselves* directly inside the proof equations without alphabetic vertex labels, followed by :person:`Robert Simson's <simson>` 35 Definitions, 3 Postulates, 12 Axioms, and Byrne's operator key.

.. picture:: /_static/figures/preliminaries.svg
   :alt: Oliver Byrne 1847 Preliminaries plate showing the self-naming colored right triangle (pp. x–xi), Definition IX angle, Definition XXXIII rhomboid, parallel lines, and Postulates I–III circles.
   :caption: **Preliminaries Overview (pp. x–xxiii).** Left: Byrne's *Introduction* right-angled triangle replacing 30 lines of alphabetic prose with self-naming colored sides and wedges. Center & Right: Simson's *Definitions* and *Postulates I–III* in four-color Chiswick Press register.

.. folio:: Introduction
   :page: vii

Introduction: The Ocular Manifesto (pp. vii–xvi)
------------------------------------------------

The arts and sciences have become so extensive, that to facilitate their acquirement is of as much importance as to extend their boundaries. Illustration, if it does not shorten the time of study, will at least make it more agreeable. This Work has a greater aim than mere illustration; we do not introduce colours for the purpose of entertainment, or to amuse by certain combinations of tint and form, but **to assist the mind in its researches after truth**, to increase the facilities of instruction, and to diffuse permanent knowledge.

In accordance with :person:`Horace's <horace>` maxim (:cite:`*Ars Poetica* 180–182 <horace:ars>`) and the intuitive pedagogy of :person:`Pestalozzi <pestalozzi>`, :person:`Oliver Byrne <byrne>` states on page ``ix`` the foundational principle of :term:`pointer-free visual notation <pointer-free-notation>`:

.. epigraph::

   “In the demonstrations of Euclid, **the letters annexed to points, lines, or other parts of a diagram are in fact but arbitrary names**, and represent them in the demonstration; instead of these, **the parts being differently coloured, are made to name themselves**, for their forms in corresponding colours represent them in the demonstration.”

   — :person:`Oliver Byrne <byrne>`, :cite:`*Introduction*, p. ix <byrne:1847>`

On pages ``x–xi``, Byrne contrasts six elementary relations of a right-angled triangle (legs :byrne-line:`yellow solid`, :byrne-line:`blue solid`, hypotenuse :byrne-line:`red solid`) expressed first in thirty lines of alphabetic prose (`AB`, `BC`, `AC`, `angle BAC`) and then in six immediate colored equations:

.. container:: byrne-eq-block

   :byrne-angle:`yellow` + :byrne-angle:`blue` + :byrne-op:`right-angle` = :byrne-op:`two-right-angles`

   :byrne-line:`red solid` :byrne-op:`gt` :byrne-line:`blue solid` and :byrne-line:`red solid` :byrne-op:`gt` :byrne-line:`yellow solid`

   :byrne-line:`yellow solid` + :byrne-line:`blue solid` :byrne-op:`gt` :byrne-line:`red solid`

   :byrne-line:`red solid squared` = :byrne-line:`yellow solid squared` + :byrne-line:`blue solid squared`

.. folio:: Definitions
   :page: xvii

Book I. Definitions (I–XXXV, Simson Numbering, pp. xvii–xxii)
-------------------------------------------------------------

* **I.** A *point* is that which has no parts.
* **II.** A *line* (:byrne-line:`black solid`) is length without breadth.
* **III.** The extremities of a line are points.
* **IV.** A *straight* or *right line* (:byrne-line:`red solid`) is that which lies evenly between its extreme points.
* **V–VII.** A *superficies* (surface) has length and breadth only; its extremities are lines; a *plane superficies* is that in which any two points being taken, the straight line between them lies wholly in that plane.
* **VIII–IX.** A *plane angle* (:byrne-angle:`blue`) is the inclination of two lines to one another in a plane, which meet together, but are not in the same direction; a *plane rectilineal angle* is contained by two straight lines.
* **X.** When a straight line standing on another straight line makes the adjacent angles equal to one another (:byrne-angle:`yellow` = :byrne-angle:`red`), each of the angles is called a *right angle* (:byrne-op:`right-angle`); and the straight line which stands on the other is called a *perpendicular* (:byrne-op:`perp`) to it.
* **XI–XII.** An *obtuse angle* is greater (:byrne-op:`gt`) than a right angle; an *acute angle* is less (:byrne-op:`lt`) than a right angle.
* **XV–XVIII.** A *circle* (:byrne-circle:`blue`) is a plane figure contained by one line, called the *circumference*, such that all straight lines drawn from a certain point within the figure (the *centre*) to the circumference are equal to one another; a *diameter* passes through the centre and bisects the circle into two *semicircles*.
* **XIX–XXIII.** Rectilineal figures: *trilateral* (:byrne-tri:`yellow filled`), *quadrilateral* (:byrne-sq:`red filled`), and *multilateral* polygons.
* **XXIV–XXVI.** Among trilateral figures: an *equilateral triangle* has three equal sides; an *isosceles triangle* has two equal sides; a *scalene triangle* has three unequal sides; further divided into *right-angled*, *obtuse-angled*, and *acute-angled* triangles.
* **XXVII–XXXIV.** Among four-sided figures (:person:`Simson's <simson>` expanded classification): **XXVII.** a *square* (:byrne-sq:`black filled`) has all its sides equal and all its angles right angles; **XXVIII.** an *oblong* (:byrne-rect:`yellow filled`) is right-angled but not equilateral; **XXIX.** a *rhombus* is equilateral but not right-angled; **XXX.** a *rhomboid* has opposite sides equal without being equilateral or right-angled; **XXXI–XXXIV.** *trapezia* and *parallelograms*.
* **XXXV.** *Parallel straight lines* (:byrne-op:`parallel`) are such as are in the same plane, and which being produced ever so far both ways do not meet.

.. folio:: Postulates & Axioms
   :page: xxiii

Postulates (I–III) & Axioms (I–XII, pp. xxiii–xxiv)
---------------------------------------------------

**Postulates**

* **Postulate I** (:just:`I.post.1` / ``G.24``): Let it be granted that a straight line (:byrne-line:`red solid`) may be drawn from any one point to any other point.
* **Postulate II** (:just:`I.post.2` / ``G.25``): That a terminated straight line may be produced to any length in a straight line (:byrne-line:`red solid-dotted`).
* **Postulate III** (:just:`I.post.3` / ``G.26``): And that a circle (:byrne-circle:`blue`) may be described from any centre, at any distance from that centre.

**Axioms (Simson Numbering)**

* **Axiom I** (:just:`C.N.1`): Things which are equal to the same thing are equal to one another.
* **Axiom II** (:just:`C.N.2`): If equals be added to equals, the wholes are equal.
* **Axiom III** (:just:`C.N.3`): If equals be taken from equals, the remainders are equal.
* **Axioms IV–V**: If equals be added to or taken from unequals, the wholes or remainders are unequal (:byrne-op:`gt` / :byrne-op:`lt`).
* **Axioms VI–VII**: Things which are double of the same, or halves of the same, are equal to one another.
* **Axiom VIII** (:just:`C.N.4`): Magnitudes which coincide with one another, that is, which exactly fill the same space, are equal to one another.
* **Axiom IX** (:just:`C.N.5`): The whole is greater (:byrne-op:`gt`) than its part.
* **Axiom X**: Two straight lines cannot enclose a space.
* **Axiom XI** (:just:`I.post.4` / ``G.27``): All right angles (:byrne-op:`right-angle`) are equal to one another.
* **Axiom XII** (:just:`I.post.5` / ``G.28``): If a straight line meet two straight lines, so as to make the two interior angles on the same side of it taken together less (:byrne-op:`lt`) than two right angles (:byrne-op:`two-right-angles`), these straight lines, being continually produced, shall at length meet on that side on which are the angles which are less than two right angles.

.. folio:: Symbols
   :page: xxvii

Symbols and Abbreviations (pp. xxvii–xxix)
------------------------------------------

.. list-table:: **Oliver Byrne's 1847 Formal Operator Table**
   :header-rows: 1
   :widths: 20 30 50

   * - Glyph
     - RST Role
     - Meaning in Byrne (1847)
   * - ``∴`` / ``∵``
     - ``:byrne-op:`therefore``` / ``:byrne-op:`because```
     - Deductive inference (*therefore*) and premise (*because*).
   * - ``=`` / ``+`` / ``-``
     - Standard operators
     - Equality, geometric composition (sum), and remainder (difference).
   * - :byrne-op:`gt` / :byrne-op:`lt`
     - ``:byrne-op:`gt``` / ``:byrne-op:`lt```
     - *Greater than* (``⊏``) and *less than* (``⊐``) in Byrne's square-bracket notation.
   * - :byrne-op:`parallel` / :byrne-op:`perp`
     - ``:byrne-op:`parallel``` / ``:byrne-op:`perp```
     - Parallel straight lines and perpendicularity.
   * - :byrne-op:`right-angle`
     - ``:byrne-op:`right-angle```
     - One right angle (quadrant arc between perpendicular arms).
   * - :byrne-op:`two-right-angles`
     - ``:byrne-op:`two-right-angles```
     - Two right angles (bisected semicircle standing on a straight line).
   * - :byrne-line:`red solid squared`
     - ``:byrne-line:`red solid squared```
     - Square described upon the colored straight line.
   * - :byrne-op:`prop`
     - ``:byrne-op:`prop```
     - Equality of ratios (``: ∷ :``) across Book V and Book VI proportions.

.. toctree::
   :hidden:

   summary
   notes
