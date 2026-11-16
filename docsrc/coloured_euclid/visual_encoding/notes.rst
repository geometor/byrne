.. _byrne-visual-encoding-notes:
.. _byrne-unit-7-notes:

Visual Encoding Notes: Compiler Diagnostics & Interactive Synthesis
===================================================================

.. rubric:: Static Register Checking & Future Extensions

Automated Register Auditing (:func:`~geometor.byrne.pseudocode.analyze_visual_registers`)
-----------------------------------------------------------------------------------------

When our static analyzer audits all seven propositions in :data:`~geometor.byrne.pseudocode.ROSETTA_PROGRAMS`, it verifies ``is_unambiguous == True`` across every proposition while automatically classifying Byrne's two register-extension mechanisms:

* **Symmetric Congruence Twins** (`I.5`, `I.47`, `IV.11`): Multiple `geom_ref` paths deliberately share a visual token because their equality is an invariant of the configuration.
* **Stroke Modulation** (`I.47`, `II.11`, `IV.10`, `IV.11`): Dashed, dotted, and solid-dotted strokes expand 4 colors into 16 distinct 1D line registers without requiring additional printing inks.

Interactive Synergy in the Browser
----------------------------------

In print (1847), a reader still locates a :byrne-rect:`yellow filled` token on the diagram by color perception alone. In ``geometor/byrne``, ``byrne_interactive.js`` and ``geometor_interactive.js`` unite Byrne's pass-by-value color tokens with GEOMETOR's exact ``data-ref`` graph—so hovering or locking any inline glyph dims unrelated ink and pulses the exact SymPy-constructed geometric entity!
