:folio: 0011
:page: vii
:type: notes
:title: Foundations Notes

.. _byrne-foundations-notes:
.. _byrne-unit-1-notes:

Foundations Notes: Chiswick Press Printing, Simson Numbering & Reception
========================================================================

.. folio:: 0011
   :page: vii

.. rubric:: Historical, Typographic & Epistemological Commentary

Chiswick Press Four-Run Relief Registration
-------------------------------------------

Printed in 1847 by :person:`Charles Whittingham the Younger <whittingham>` for publisher :person:`William Pickering <pickering>`, Byrne's *Euclid* predated commercial chromolithography in mathematical publishing. Every page required **four separate letterpress/woodblock press runs**:

1. **Caslon Lampblack** (text, operators, black lines, and Renaissance woodcut initials),
2. **Vermilion Red**,
3. **Prussian Blue**, and
4. **Ochre-Gamboge Yellow**.

As :person:`Ruari McLean <mclean>` documented in :cite:`*Victorian Book Design and Colour Printing* (1963) <mclean:1963>`, aligning tiny inline woodblock rules and angle wedges inside Caslon text lines to sub-millimeter tolerances was an extraordinary feat of hand-press craftsmanship—explaining its steep 25-shilling price and commercial scarcity prior to the 1851 Great Exhibition.

Simson's Axioms XI & XII vs. Heiberg / Heath
--------------------------------------------

Readers cross-referencing ``geometor/euclid`` (:cite:`Heath 1908 <heath:1908>`) and ``geometor/hilbert`` should note two pivotal numbering shifts inherited from :person:`Robert Simson <simson>`:

* **Right-Angle Equality**: Listed by Byrne as **Axiom XI**, whereas Heiberg/Heath restore it to **Postulate 4** (:just:`I.post.4`, ``G.27``).
* **The Parallel Postulate**: Listed by Byrne as **Axiom XII**, whereas Heiberg/Heath restore it to **Postulate 5** (:just:`I.post.5`, ``G.28``).

From De Morgan's Skepticism to Tufte & Rougeux
----------------------------------------------

While :person:`Augustus De Morgan <demorgan>` (:cite:`1872 <demorgan:1872>`) dismissed Byrne's colours as a pedagogical "trick," twentieth- and twenty-first-century scholarship vindicated Byrne's architecture:

* :person:`P. H. J. Hoenen <hoenen>` (:cite:`*De Noetica Geometriae*, 1954 <hoenen:1954>`, ``geometor/hoenen``) showed philosophically that geometric judgment reads universal necessity directly inside the spatial *phantasma*.
* :person:`Edward Tufte <tufte>` (:cite:`*Envisioning Information*, 1990 <tufte:1990>`) demonstrated how inline colored nouns eliminate eye-movement indirection between legend and diagram.
* In December 2018, :person:`Nicholas Rougeux <rougeux>` (:cite:`c82.net/euclid <rougeux:2018>`; :cite:`Making of Byrne's Euclid <rougeux:2018-making>`) created a celebrated interactive web edition bringing clickable diagram highlighting to every proposition. ``geometor/byrne`` honors Rougeux's design milestone while coupling inline vector glyphs to **100% exact symbolic SymPy constructions** (:mod:`geometor.byrne.constructions`) derived strictly from the public-domain 1847 Pickering witness.
