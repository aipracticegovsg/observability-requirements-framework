// Interactive "what's mandatory for my system" checklist.
// Reads the same docs/assets/requirements.json the requirements table uses,
// and derives the action for each item from the selected risk level (the JSON
// already carries the high/medium/low action per item).

function __orfReady(fn) {
  if (document.readyState !== "loading") fn();
  else document.addEventListener("DOMContentLoaded", fn);
}

__orfReady(function () {
  var root = document.getElementById("orf-checklist");
  if (!root) return;

  var self = document.querySelector('script[src$="javascripts/checklist.js"]');
  var siteRoot = self
    ? self.src.replace(/javascripts\/.*$/, "")
    : "/";
  var dataUrl = siteRoot + "assets/requirements.json";

  var RISK_LABELS = { high: "High-Risk", medium: "Medium-Risk", low: "Low-Risk" };
  var ACTION_CLASS = function (a) {
    a = (a || "").toLowerCase();
    if (a === "mandatory") return "mand";
    if (a.indexOf("waivable") !== -1) return "waiv";
    return "gth";
  };

  // ---- Controls UI ------------------------------------------------------
  root.innerHTML =
    '<div class="orf-cl-controls">' +
    '  <label>Risk level: ' +
    '    <select id="orf-cl-risk">' +
    '      <option value="high">High-Risk</option>' +
    '      <option value="medium">Medium-Risk</option>' +
    '      <option value="low">Low-Risk</option>' +
    "    </select>" +
    "  </label>" +
    '  <label><input type="checkbox" id="orf-cl-gth"> Include Good-to-Have</label>' +
    '  <button id="orf-cl-print" type="button">Print / Save as PDF</button>' +
    "</div>" +
    '<div id="orf-cl-summary" class="orf-cl-summary"></div>' +
    '<div id="orf-cl-body"></div>';

  var riskSel = document.getElementById("orf-cl-risk");
  var gthChk = document.getElementById("orf-cl-gth");
  var summaryEl = document.getElementById("orf-cl-summary");
  var bodyEl = document.getElementById("orf-cl-body");
  document.getElementById("orf-cl-print").addEventListener("click", function () {
    window.print();
  });

  var DATA = [];

  function render() {
    var risk = riskSel.value;
    var showGth = gthChk.checked;
    var counts = { mand: 0, waiv: 0, gth: 0 };
    var groups = {};
    var order = [];

    DATA.forEach(function (item) {
      var action = item[risk];
      var cls = ACTION_CLASS(action);
      counts[cls]++;
      if (cls === "gth" && !showGth) return;
      if (!groups[item.category_name]) {
        groups[item.category_name] = [];
        order.push(item.category_name);
      }
      groups[item.category_name].push({ item: item, action: action, cls: cls });
    });

    summaryEl.innerHTML =
      "<strong>" + RISK_LABELS[risk] + " system</strong> &mdash; " +
      '<span class="orf-action orf-action-mand">' + counts.mand + " Mandatory</span> " +
      '<span class="orf-action orf-action-waiv">' + counts.waiv + " Mandatory but Waivable</span> " +
      '<span class="orf-action orf-action-gth">' + counts.gth + " Good-to-Have</span>" +
      (showGth ? "" : '<div class="orf-cl-hint">Good-to-Have items hidden &mdash; tick the box to show them.</div>');

    var html = "";
    order.forEach(function (cat) {
      html += '<h3 class="orf-cl-cat">' + cat + "</h3>";
      html += '<table class="orf-cl-table"><thead><tr>' +
        "<th>Action</th><th>Tier</th><th>Type</th><th>ID</th><th>Telemetry Item</th>" +
        "</tr></thead><tbody>";
      groups[cat].forEach(function (row) {
        html +=
          "<tr>" +
          '<td><span class="orf-action orf-action-' + row.cls + '">' + row.action + "</span></td>" +
          '<td><span class="orf-tier orf-tier-' + row.item.tier + '">Tier ' + row.item.tier + "</span></td>" +
          "<td>" + row.item.type + "</td>" +
          "<td><code>" + row.item.id + "</code></td>" +
          '<td>' + row.item.name +
          '<div class="orf-cl-def">' + row.item.definition + "</div></td>" +
          "</tr>";
      });
      html += "</tbody></table>";
    });
    bodyEl.innerHTML = html;
  }

  riskSel.addEventListener("change", render);
  gthChk.addEventListener("change", render);

  fetch(dataUrl)
    .then(function (r) { return r.json(); })
    .then(function (rows) { DATA = rows; render(); })
    .catch(function (e) {
      bodyEl.innerHTML =
        '<p style="color:#c62828">Could not load requirements data (' + e +
        "). Run <code>python scripts/build_json.py</code> and rebuild.</p>";
    });
});
