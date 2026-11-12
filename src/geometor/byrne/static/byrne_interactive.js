/**
 * GEOMETOR • byrne — Bidirectional Visual Value-Token Highlighter
 *
 * Complements photon-platform/publish `geometor_interactive.js` by linking
 * inline `:byrne-*:` micro-glyph tokens (`.byrne-token`) with `.euclid-graphic`
 * plate elements via both exact `data-ref` / `data-aliases` targets AND
 * scoped `data-byrne-color` + `data-byrne-kind` visual token matching.
 */
(function () {
  "use strict";

  function normRef(raw) {
    return (raw || "").replace(/\s+/g, " ").trim();
  }

  function splitQualifiedRef(raw) {
    var trimmed = normRef(raw);
    if (!trimmed) return { gid: "", expr: "" };
    var idx = trimmed.indexOf(":");
    if (idx === -1) return { gid: "", expr: trimmed };
    return {
      gid: trimmed.slice(0, idx).trim(),
      expr: normRef(trimmed.slice(idx + 1)),
    };
  }

  function elementMatchesExpr(svgEl, expr) {
    if (!expr) return false;
    var primary = normRef(svgEl.getAttribute("data-ref"));
    if (primary && primary === expr) return true;
    var aliases = (svgEl.getAttribute("data-aliases") || "").split("|");
    for (var i = 0; i < aliases.length; i++) {
      if (normRef(aliases[i]) === expr) return true;
    }
    return false;
  }

  function findTargetSvgs(gid, sourceEl) {
    var allSvgs = Array.prototype.slice.call(
      document.querySelectorAll("svg.euclid-graphic")
    );
    if (!allSvgs.length) return [];
    if (gid) {
      var exact = allSvgs.filter(function (svg) {
        var idAttr = svg.getAttribute("data-graphic-id") || "";
        return idAttr === gid || idAttr.endsWith("." + gid);
      });
      if (exact.length) return exact;
    }
    // Nearest preceding .euclid-graphic in reading order as fallback
    if (sourceEl && sourceEl.compareDocumentPosition) {
      var preceding = allSvgs.filter(function (svg) {
        return Boolean(
          svg.compareDocumentPosition(sourceEl) &
            Node.DOCUMENT_POSITION_FOLLOWING
        );
      });
      if (preceding.length) return [preceding[preceding.length - 1]];
    }
    return [allSvgs[0]];
  }

  function clearAllHighlights(keepLocked) {
    document
      .querySelectorAll("svg.euclid-graphic.byrne-has-focus")
      .forEach(function (svg) {
        if (keepLocked && svg.hasAttribute("data-byrne-locked")) return;
        svg.classList.remove("byrne-has-focus");
      });
    document
      .querySelectorAll("svg.euclid-graphic .byrne-highlight")
      .forEach(function (el) {
        var parentSvg = el.closest("svg.euclid-graphic");
        if (keepLocked && parentSvg && parentSvg.hasAttribute("data-byrne-locked")) {
          return;
        }
        el.classList.remove("byrne-highlight");
      });
    document.querySelectorAll(".byrne-token.byrne-active").forEach(function (tok) {
      if (keepLocked && tok.classList.contains("byrne-locked")) return;
      tok.classList.remove("byrne-active");
    });
  }

  function highlightFromToken(tokenEl) {
    var rawRef = tokenEl.getAttribute("data-ref") || "";
    var color = tokenEl.getAttribute("data-byrne-color") || "";
    var kind = tokenEl.getAttribute("data-byrne-kind") || "";
    var refParts = splitQualifiedRef(rawRef);
    var svgs = findTargetSvgs(refParts.gid, tokenEl);

    tokenEl.classList.add("byrne-active");

    // Highlight sibling tokens sharing the exact same non-empty data-ref
    if (rawRef) {
      document.querySelectorAll(".byrne-token").forEach(function (peer) {
        if ((peer.getAttribute("data-ref") || "") === rawRef) {
          peer.classList.add("byrne-active");
        }
      });
    }

    svgs.forEach(function (svg) {
      var matched = [];
      var candidates = svg.querySelectorAll("[data-ref], [data-byrne-color]");

      if (refParts.expr) {
        // Handle multi-part ";" targets as well as single targets
        var subExprs = refParts.expr.split(";").map(normRef).filter(Boolean);
        candidates.forEach(function (el) {
          for (var i = 0; i < subExprs.length; i++) {
            if (elementMatchesExpr(el, subExprs[i])) {
              matched.push(el);
              break;
            }
          }
        });
      }

      // Fallback to color + kind matching within the target plate when no explicit ref matched
      if (!matched.length && color && color.indexOf("+") === -1 && color.indexOf("/") === -1) {
        candidates.forEach(function (el) {
          var elColor = el.getAttribute("data-byrne-color") || "";
          var elKind = el.getAttribute("data-byrne-kind") || "";
          if (elColor === color && (!kind || !elKind || elKind === kind)) {
            matched.push(el);
          }
        });
      }

      if (matched.length) {
        svg.classList.add("byrne-has-focus");
        matched.forEach(function (el) {
          el.classList.add("byrne-highlight");
        });
      }
    });
  }

  function highlightFromSvgElement(svgEl) {
    var svg = svgEl.closest("svg.euclid-graphic");
    if (!svg) return;
    var gid = svg.getAttribute("data-graphic-id") || "";
    var expr = normRef(svgEl.getAttribute("data-ref"));
    var color = svgEl.getAttribute("data-byrne-color") || "";

    svg.classList.add("byrne-has-focus");
    svgEl.classList.add("byrne-highlight");

    document.querySelectorAll(".byrne-token").forEach(function (tok) {
      var tokParts = splitQualifiedRef(tok.getAttribute("data-ref") || "");
      if (tokParts.gid && gid && tokParts.gid !== gid && !gid.endsWith("." + tokParts.gid)) {
        return;
      }
      if (expr && tokParts.expr) {
        var subExprs = tokParts.expr.split(";").map(normRef).filter(Boolean);
        if (subExprs.indexOf(expr) !== -1 || elementMatchesExpr(svgEl, tokParts.expr)) {
          tok.classList.add("byrne-active");
          return;
        }
      }
      if (!tokParts.expr && color && tok.getAttribute("data-byrne-color") === color) {
        var nearest = findTargetSvgs("", tok);
        if (nearest.indexOf(svg) !== -1) {
          tok.classList.add("byrne-active");
        }
      }
    });
  }

  function initByrneInteractive() {
    document.querySelectorAll(".byrne-token").forEach(function (tok) {
      if (tok.hasAttribute("data-byrne-bound")) return;
      tok.setAttribute("data-byrne-bound", "1");

      tok.addEventListener("mouseenter", function () {
        clearAllHighlights(true);
        highlightFromToken(tok);
      });

      tok.addEventListener("mouseleave", function () {
        clearAllHighlights(true);
      });

      tok.addEventListener("click", function (ev) {
        ev.stopPropagation();
        var wasLocked = tok.classList.contains("byrne-locked");
        document.querySelectorAll(".byrne-token.byrne-locked").forEach(function (el) {
          el.classList.remove("byrne-locked");
        });
        document
          .querySelectorAll("svg.euclid-graphic[data-byrne-locked]")
          .forEach(function (s) {
            s.removeAttribute("data-byrne-locked");
          });
        clearAllHighlights(false);
        if (!wasLocked) {
          tok.classList.add("byrne-locked");
          highlightFromToken(tok);
          document
            .querySelectorAll("svg.euclid-graphic.byrne-has-focus")
            .forEach(function (s) {
              s.setAttribute("data-byrne-locked", "1");
            });
        }
      });
    });

    document
      .querySelectorAll(
        "svg.euclid-graphic [data-byrne-color], svg.euclid-graphic [data-ref]"
      )
      .forEach(function (svgEl) {
        if (svgEl.hasAttribute("data-byrne-svg-bound")) return;
        svgEl.setAttribute("data-byrne-svg-bound", "1");

        svgEl.addEventListener("mouseenter", function () {
          clearAllHighlights(true);
          highlightFromSvgElement(svgEl);
        });

        svgEl.addEventListener("mouseleave", function () {
          clearAllHighlights(true);
        });
      });

    document.addEventListener("click", function () {
      document.querySelectorAll(".byrne-token.byrne-locked").forEach(function (el) {
        el.classList.remove("byrne-locked");
      });
      document
        .querySelectorAll("svg.euclid-graphic[data-byrne-locked]")
        .forEach(function (s) {
          s.removeAttribute("data-byrne-locked");
        });
      clearAllHighlights(false);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initByrneInteractive);
  } else {
    initByrneInteractive();
  }
})();
