:title: GEOMETOR • byrne

GEOMETOR • byrne
================

.. rubric:: Oliver Byrne's *Coloured Elements of Euclid* (1847) — Digital Scriptorium Codex & Pointer-Free Visual Pseudocode Engine

Digital critical edition, dedicated per-proposition **Book Codex**, formal **Pointer-Free Visual Pseudocode** grammar, and **100% exact symbolic SymPy constructions** for :person:`Oliver Byrne's <byrne>` landmark treatise:

   *The First Six Books of the Elements of Euclid in Which Coloured Diagrams and Symbols Are Used Instead of Letters for the Greater Ease of Learners* (London: :person:`William Pickering <pickering>`, printed by :person:`Charles Whittingham <whittingham>` at the Chiswick Press, 1847).

.. picture:: /_static/figures/i47.svg
   :alt: Oliver Byrne's iconic four-color Pythagorean Theorem plate (Book I, Proposition 47) rendered from exact rational coordinates in geometor.model.
   :caption: **Book I, Proposition XLVII (pp. 48–49).** :byrne-rect:`yellow filled <i47:< B L M D >>` + :byrne-rect:`blue filled <i47:< C L M E >>` = :byrne-sq:`black filled <i47:< A B F G >>` + :byrne-sq:`red filled <i47:< A C K H >>` — hover or click any inline colored glyph or diagram region to pulse its exact counterpart (:ref:`open Proposition I.47 <byrne-i-47>`).

----

Book Codex & Analytical Treatises
---------------------------------

:doc:`The First Six Books of the Elements of Euclid (Pickering / Chiswick Press, 1847) <coloured_euclid/index>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dedicated per-proposition Digital Scriptorium **Book Codex** (*Proposition · Commentary* and *Book Overview · Summary · Notes*) spanning all six planar and proportional books of :person:`Euclid <euclid>`:

* **Foundations & Book I**: :ref:`1847 Introduction, Simson Definitions, Postulates, Axioms & Operators <byrne-unit-1-en>` · :ref:`Book I <byrne-book-i>` (:ref:`I.1 <byrne-i-1>`, :ref:`I.4 <byrne-i-4>`, :ref:`I.5 <byrne-i-5>`, :ref:`I.15 <byrne-i-15>`, :ref:`I.32 <byrne-i-32>`, :ref:`I.46 <byrne-i-46>`, :ref:`I.47 <byrne-i-47>`).
* **Geometric Algebra, Circles & Regular Polygons**: :ref:`Book II <byrne-book-ii>` (:ref:`II.4 <byrne-ii-4>`, :ref:`II.5 <byrne-ii-5>`, :ref:`II.11 <byrne-ii-11>`) · :ref:`Book III <byrne-book-iii>` (:ref:`III.20 <byrne-iii-20>`, :ref:`III.31 <byrne-iii-31>`, :ref:`III.36 <byrne-iii-36>`) · :ref:`Book IV <byrne-book-iv>` (:ref:`IV.4 <byrne-iv-4>`, :ref:`IV.10 <byrne-iv-10>`, :ref:`IV.11 <byrne-iv-11>`).
* **Eudoxian Proportions, Similarity & Rosetta Grammar**: :ref:`Book V <byrne-book-v>` (:ref:`V.11 <byrne-v-11>`, :ref:`V.16 <byrne-v-16>`, :ref:`V.18 <byrne-v-18>`, :ref:`V.22 <byrne-v-22>`) · :ref:`Book VI <byrne-book-vi>` (:ref:`VI.30 <byrne-vi-30>`) · :ref:`3-Way Rosetta Analysis (Heath · Byrne · GEOMETOR) <byrne-unit-7-en>`.
* **Scholarly Apparatus**: :doc:`People </coloured_euclid/persons>` · :doc:`Bibliography </coloured_euclid/bibliography>` · :ref:`Concordance <concordance>` · :ref:`Glossary <glossary>`.

:doc:`Pointer-Free Visual Pseudocode: Language Specification & Compiler Metrics <pseudocode/index>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Formal computer-science analysis of Oliver Byrne's 1847 visual notation as a **typed, pass-by-value geometric DSL** that eliminates alphabetic vertex-pointer dereferencing (``AB``, ``∠BAC``, ``□ABFG``), achieving an **80–92% reduction in verbal prose** while encoding congruence symmetries directly in perceptual registers.

----

Context & Architecture
----------------------

* :doc:`About This Edition <about/index>`
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
   about/index
   usage/index
   pseudocode/index
   log/index
   modules/index
