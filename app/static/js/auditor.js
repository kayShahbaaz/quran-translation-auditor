// app/static/js/auditor.js
// Quranic Cross-Lingual Translation Auditor — 5-Translation Panel Engine

(function () {
  "use strict";

  var activeRow = null;

  function escHtml(str) {
    if (!str) return "";
    return String(str)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function safeParseJSON(str) {
    try { return JSON.parse(str); } catch (e) { return {}; }
  }

  function buildScoreSummary(score, band, bandLabel) {
    var pairs = band === "high" ? "10" : "10";
    return '<div class="panel-score-bar">' +
      '<span class="score-badge badge-' + band + '">' + score + '</span>' +
      '<span class="panel-score-desc"><strong>Divergence Friction Score</strong> &mdash; ' +
      escHtml(bandLabel) + ' &nbsp;|&nbsp; Pairwise Macro-Averaged Jaccard across ' + pairs + ' translation pairs (5 translators)</span>' +
      '</div>';
  }

  function buildWordSets(wordSets, translations) {
    var keys   = ["sahih", "haleem", "khattab", "soliman", "kanzuliman"];
    var labels = {
      sahih:      "Sahih International",
      haleem:     "Abdel Haleem",
      khattab:    "Mustafa Khattab",
      soliman:    "Fadel Soliman / Bridges",
      kanzuliman: "Kanzul Iman — Aqib Farid Qadri",
    };
    var html = '<div class="wordset-grid">';
    keys.forEach(function (k) {
      var words = wordSets[k] || [];
      var chips = words.length
        ? words.map(function (w) { return '<span class="chip">' + escHtml(w) + "</span>"; }).join("")
        : '<span class="empty-chip">No content words</span>';
      var trans = translations[k] || "";
      html += '<div class="wordset-card">' +
        '<h4>' + escHtml(labels[k]) + '</h4>' +
        '<div class="trans-preview">' + escHtml(trans) + '</div>' +
        '<div class="word-chips">' + chips + '</div>' +
        '</div>';
    });
    html += '</div>';
    return html;
  }

  function buildPairsLog(pairsLog) {
    var html = '<div class="pairs-title">Pairwise Jaccard Similarity Log &mdash; All 10 Pairs</div><div class="pairs-grid">';
    pairsLog.forEach(function (p) {
      var shared = p.shared.length   ? p.shared.join(", ")        : "&mdash;";
      var excl1  = p.exclusive_t1.length ? p.exclusive_t1.join(", ") : "&mdash;";
      var excl2  = p.exclusive_t2.length ? p.exclusive_t2.join(", ") : "&mdash;";
      var parts  = p.pair.split(" vs ");
      html += '<div class="pair-row">' +
        '<div class="pair-label">' + escHtml(p.label || p.pair) + '</div>' +
        '<div class="pair-sim">Jaccard similarity: <strong>' + p.sim + '</strong></div>' +
        '<div class="pair-shared">&#x2713; Shared: ' + shared + '</div>' +
        '<div class="pair-exclusive">&#x2715; ' + escHtml(parts[0] || "") + ' exclusive: ' + excl1 + '</div>' +
        '<div class="pair-exclusive">&#x2715; ' + escHtml(parts[1] || "") + ' exclusive: ' + excl2 + '</div>' +
        '</div>';
    });
    html += '</div>';
    return html;
  }

  function buildRoots(roots) {
    var html = '<div class="roots-section"><h4>Arabic Root Mappings</h4><div class="root-chips">';
    Object.keys(roots).forEach(function (word) {
      html += '<span class="root-chip"><span class="root-latin">' + escHtml(roots[word]) + '</span>' + escHtml(word) + '</span>';
    });
    html += '</div></div>';
    return html;
  }

  function openPanel(row) {
    var panel      = document.getElementById("detail-panel");
    var panelTitle = document.getElementById("panel-title");
    var panelAr    = document.getElementById("panel-arabic");
    var panelBody  = document.getElementById("panel-body");

    var translations = {
      sahih:      row.dataset.sahih,
      haleem:     row.dataset.haleem,
      khattab:    row.dataset.khattab,
      soliman:    row.dataset.soliman,
      kanzuliman: row.dataset.kanzuliman || "",
    };

    panelTitle.textContent = "Ayah " + row.dataset.ayah + " — Semantic Audit Report";
    panelAr.textContent    = row.dataset.arabic;

    panelBody.innerHTML =
      buildScoreSummary(row.dataset.score, row.dataset.band, row.dataset.bandLabel) +
      buildWordSets(safeParseJSON(row.dataset.wordsets), translations) +
      buildPairsLog(safeParseJSON(row.dataset.pairslog)) +
      buildRoots(safeParseJSON(row.dataset.roots));

    panel.classList.add("visible");
    panel.scrollIntoView({ behavior: "smooth", block: "start" });

    if (activeRow) activeRow.style.outline = "";
    activeRow = row;
    row.style.outline = "2px solid var(--border-focus)";
  }

  function closePanel() {
    var panel = document.getElementById("detail-panel");
    panel.classList.remove("visible");
    if (activeRow) { activeRow.style.outline = ""; activeRow = null; }
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-ayah]").forEach(function (row) {
      row.addEventListener("click", function () { openPanel(row); });
    });
    var btn = document.getElementById("panel-close-btn");
    if (btn) btn.addEventListener("click", closePanel);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closePanel();
      if (e.key === "Enter" && document.activeElement.dataset.ayah) openPanel(document.activeElement);
    });
  });
})();
