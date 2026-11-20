<a href="https://geometor.github.io/byrne/"><img src="docsrc/_static/logo.png" alt="GEOMETOR • byrne Medallion" align="right" width="150"></a>

# GEOMETOR • byrne

**Visit the Online Archive:** https://geometor.github.io/byrne/

<p align="center">
  <a href="https://geometor.github.io/byrne/"><img src="docsrc/_static/figures/i47.svg" alt="GEOMETOR • byrne featured geometric construction"></a>
</p>

**Oliver Byrne • The First Six Books of the Elements of Euclid (Coloured Diagrams) • semantic digital archive**

## Mission

`geometor/byrne` is part of the interconnected [GEOMETOR](https://geometor.com) semantic digital archive. It provides a multi-track Book Codex, pointer-free visual pseudocode grammar, and exact symbolic color-token proof engine for Oliver Byrne's celebrated 1847 edition of Euclid's *Elements*. The archive liberates Byrne's revolutionary four-color visual pedagogy from static print bounds into addressable semantic units, calibrated theme-adaptive vector diagrams, primary-source Chiswick Press provenance, and exact symbolic geometry across the GEOMETOR corpus.

## Books in This Archive

- [The First Six Books of the Elements of Euclid](https://geometor.github.io/byrne/coloured_euclid/) — Oliver Byrne's landmark 1847 Chiswick Press masterpiece, replacing alphabetical point labels with colored diagrams and symbols across Books I–VI.

## Repository Contents

- `docsrc/` — Multi-track Book Codex, visual pseudocode documentation, and Sphinx site compiled by [PHOTON publish](https://github.com/photon-platform/publish).
- `resources/` — 1847 primary scan provenance, color palette definitions, and apparatus datasets.
- `src/geometor/byrne/` — Python modules for exact SymPy geometric constructions, inline Byrne glyph roles, and pseudocode DSL analysis.

## Local Build & Verification

```bash
publish build
uv run --no-sync pytest
```
## Part of the GEOMETOR Knowledge Archive

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
