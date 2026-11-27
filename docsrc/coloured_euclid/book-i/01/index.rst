:canonical_id: I.1
:book: I
:proposition: 1
:order: 1
:type: proposition
:title: Proposition I.1 — Equilateral Triangle
:folio: 0035
:page: 1
:featured_image: /_static/figures/i1.svg

.. _byrne-i-1:

.. folio:: 0035
   :page: 1

Proposition I.1 — Equilateral Triangle
======================================

.. rubric:: Book I, Proposition I. Problem (*Pickering p. 1* · ``G.84``)

*On a given finite straight line* (:byrne-line:`black solid <i1:/ A B />`) *to describe an equilateral triangle.*

.. picture:: /_static/figures/i1.svg
   :alt: Book I Proposition 1 — Equilateral triangle constructed by blue and red circles on black base.
   :caption: **Book I, Prop. I (p. 1).** Exact :math:`\mathbb{Q}(\sqrt{3})` construction via ``Model.intersect``.

.. picture:: 0035.g1.png
   :alt: Oliver Byrne 1847 Pickering archival full-RGB plate for Proposition I.1 (Leaf 35).
   :caption: **1847 Chiswick Press Archival Plate (Leaf 35, p. 1).** Full-RGB reproduction of Byrne's four-color woodblock print.

.. container:: byrne-eq-block

   **Construction.** From the extremities of :byrne-line:`black solid <i1:/ A B />` describe :byrne-circle:`blue <i1:( A B )>` and :byrne-circle:`red <i1:( B A )>` (:just:`I.post.3`); from their intersection draw :byrne-line:`yellow solid <i1:/ A C />` and :byrne-line:`red solid <i1:/ B C />` (:just:`I.post.1`).

   **Demonstration.**

   :byrne-line:`yellow solid <i1:/ A C />` = :byrne-line:`black solid <i1:/ A B />` (:just:`I.def.15`, radii of :byrne-circle:`blue <i1:( A B )>`),

   :byrne-line:`red solid <i1:/ B C />` = :byrne-line:`black solid <i1:/ A B />` (:just:`I.def.15`, radii of :byrne-circle:`red <i1:( B A )>`),

   :byrne-op:`therefore` :byrne-line:`yellow solid <i1:/ A C />` = :byrne-line:`red solid <i1:/ B C />` = :byrne-line:`black solid <i1:/ A B />` (:just:`C.N.1`).

   :byrne-op:`therefore` :byrne-tri:`yellow/red/black <i1:< A B C >>` is equilateral (:just:`I.def.20`). **Q.E.F.**

----

See :ref:`Commentary on Proposition I.1 <byrne-i-1-commentary>`.

.. toctree::
   :hidden:

   commentary
