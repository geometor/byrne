:layout: book

.. _byrne-unit-4-notes:

Unit IV Notes: Five-Color Overflow in ``IV.11`` & Heronian Integer Incircle
===========================================================================

.. rubric:: Chromatic Register Analysis & Exact Cyclotomic Algebra

Solving the Five-Edge Pentagon Paradox on a Four-Ink Press
----------------------------------------------------------

Book IV, Proposition 11 (Pickering **p. 137**, Leaf 171) poses a crisp combinatorial test for :person:`Oliver Byrne <byrne>`: a regular pentagon has **five** distinct perimeter chords, yet the Chiswick Press palette has only **four** inks (red, blue, yellow, black), and the inscribed Golden Triangle already occupies solid **yellow** (:byrne-tri:`yellow filled`)!

Byrne solves this :term:`register pressure <register-pressure>` cleanly:

* Four sides receive solid inks (:byrne-line:`red solid`, :byrne-line:`black solid`, :byrne-line:`yellow solid`, :byrne-line:`blue solid`), and
* The fifth side is printed as **red dotted** (:byrne-line:`red dotted`), keeping all five chords individually addressable in the ``Q.E.F.`` conclusion without adding a fifth press run.

Exact Symbolic Coordinates in ``geometor.byrne``
------------------------------------------------

* **Heronian ``13-14-15`` Triangle in ``IV.4``**: :func:`geometor.byrne.constructions.build_iv4` places $B = (0, 0)$, $C = (14, 0)$, $A = (5, 12)$, yielding exact **integer** side lengths $(13, 14, 15)$, area $84$, semiperimeter $21$, integer incenter $I = (6, 4)$, and integer inradius $r = 4$ over $\mathbb{Q}$.
* **Pentagonal Radical Tower in ``IV.10`` & ``IV.11``**: :func:`geometor.byrne.constructions.build_iv11` constructs all five vertices on the unit circle using exact nested radicals $\cos 72^\circ = \frac{\sqrt{5}-1}{4}$ and $\sin 72^\circ = \frac{\sqrt{10 + 2\sqrt{5}}}{4}$, verifying symbolically that all five side quadrances equal $\frac{5 - \sqrt{5}}{2}$ and diagonal-to-side quadrance equals $\phi^2 = \frac{3 + \sqrt{5}}{2}$.
