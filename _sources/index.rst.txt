:title: GEOMETOR • byrne

GEOMETOR • byrne
================

.. rubric:: Oliver Byrne's *Coloured Elements of Euclid* (1847) — Digital Scriptorium Codex & Pointer-Free Visual Pseudocode Engine

Digital critical edition, synchronized 3-track **Book Codex**, formal **Pointer-Free Visual Pseudocode** grammar, and **100% exact symbolic SymPy constructions** for :person:`Oliver Byrne's <byrne>` landmark treatise:

   *The First Six Books of the Elements of Euclid in Which Coloured Diagrams and Symbols Are Used Instead of Letters for the Greater Ease of Learners* (London: :person:`William Pickering <pickering>`, printed by :person:`Charles Whittingham <whittingham>` at the Chiswick Press, 1847).

.. picture:: /_static/figures/i47.svg
   :alt: Oliver Byrne's iconic four-color Pythagorean Theorem plate (Book I, Proposition 47) rendered from exact rational coordinates in geometor.model.
   :caption: **Book I, Proposition XLVII (pp. 48–49).** :byrne-rect:`yellow filled <i47:< B L M D >>` + :byrne-rect:`blue filled <i47:< C L M E >>` = :byrne-sq:`black filled <i47:< A B F G >>` + :byrne-sq:`red filled <i47:< A C K H >>` — hover or click any inline colored glyph or diagram region to pulse its exact counterpart.

----

Book Codex & Analytical Treatises
---------------------------------

:doc:`The First Six Books of the Elements of Euclid (Pickering / Chiswick Press, 1847) <coloured_euclid/index>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Synchronized 3-track Digital Scriptorium **Book Codex** (*Byrne 1847 Edition · Executive Summary · Scholarly & Design Notes*) spanning all six planar and proportional books of :person:`Euclid <euclid>`:

* **Foundations & Book I**: :ref:`1847 Introduction, Simson Definitions, Postulates, Axioms & Operators <byrne-unit-1-en>` · :ref:`Congruence, Pons Asinorum (I.5), Parallels & The Pythagorean Theorem (I.47) <byrne-unit-2-en>`.
* **Geometric Algebra, Circles & Regular Polygons**: :ref:`Book II Colored Rectangles & The Golden Section (II.11) <byrne-unit-3-en>` · :ref:`Books III–IV Thales, Tangent-Secant Power, Golden Triangle (IV.10) & Regular Pentagon (IV.11) <byrne-unit-4-en>`.
* **Eudoxian Proportions, Similarity & Rosetta Grammar**: :ref:`Book V Colored Ratio Algebra <byrne-unit-5-en>` · :ref:`Book VI Similar Figures & Extreme and Mean Ratio (VI.30) <byrne-unit-6-en>` · :ref:`Unit 7: 3-Way Rosetta Analysis (Heath · Byrne · GEOMETOR) <byrne-unit-7-en>`.
* **Scholarly Apparatus**: :doc:`People </coloured_euclid/persons>` · :doc:`Bibliography </coloured_euclid/bibliography>` · :ref:`Concordance <concordance>` · :ref:`Glossary <glossary>`.

:doc:`Pointer-Free Visual Pseudocode: Language Specification & Compiler Metrics <pseudocode/index>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Formal computer-science analysis of Oliver Byrne's 1847 visual notation as a **typed, pass-by-value geometric DSL** that eliminates alphabetic vertex-pointer dereferencing (``AB``, ``∠BAC``, ``□ABFG``), achieving an **80–92% reduction in verbal prose** while encoding congruence symmetries directly in perceptual registers.

----

Context & Architecture
----------------------

* :doc:`Mission & Digital Scriptorium Provenance <mission/index>`
* :doc:`Using This Edition (Reader's Guide & CLI) <usage/index>`
* :doc:`Visual Pseudocode Grammar & Register Analysis <pseudocode/index>`
* :doc:`Python Package & Symbolic API Reference <modules/index>`
* :doc:`Curation & Engineering Log <log/index>`

.. toctree::
   :maxdepth: 2
   :hidden:

   coloured_euclid/index
   coloured_euclid/persons
   coloured_euclid/bibliography
   usage/index
   pseudocode/index
   mission/index
   log/index
   modules/index
