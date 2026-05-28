#!/usr/bin/env python3
"""
Toy 3546 — Interactive HTML K-type graph viewer

Elie, Wednesday 2026-05-27 ~09:50 EDT
Extends Toy 3542 static visualization with interactive HTML viewer.
Team navigation tool for the Phase A 36-node K-type graph.

PURPOSE
-------
Generate single-file self-contained HTML viewer with:
  - Sortable table of all 36 K-types with full property data
  - Scatter plot (SVG) positioned at (m_1, m_2) with hover details
  - Filter by sector (BOSON/FERMION/all)
  - Sort by any column
  - Annotation overlays for substrate-anchor points
  - No external dependencies (pure HTML/CSS/JS)

CAL #29 STANDING QUESTION-SHAPE AUDIT (PRE-PASS):
  Question: "Build interactive HTML viewer for Phase A K-type graph"
  - Tool infrastructure, no substantive claim
  - Loads existing JSON artifact
  - Doesn't promote K-type → observable identifications
  CLEAN PASS

INVESTIGATIONS (4 scored)
1. Load Phase A 36-node JSON
2. Generate sortable HTML table with full data
3. Generate inline SVG scatter plot with hover tooltips
4. Write self-contained HTML file
"""
import sys
import json
from pathlib import Path

print("=" * 78)
print("Toy 3546 — Interactive HTML K-type graph viewer")
print("Team navigation tool for Phase A 36-node K-type graph")
print("Elie, Wednesday 2026-05-27 09:50 EDT")
print("=" * 78)

# ============================================================
# Test 1: Load JSON
# ============================================================
print("\n--- Test 1: Load Phase A 36-node JSON ---")
json_path = Path("/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/data/k_type_nodes_phase_A.json")
with open(json_path) as f:
    data = json.load(f)
nodes = data["nodes"]
print(f"  Loaded {len(nodes)} K-types from {json_path.name}")
test_1 = len(nodes) == 36
print(f"  Test 1: {'PASS' if test_1 else 'FAIL'}")


def parse_frac(s):
    if "/" in s:
        n, d = s.split("/")
        return float(int(n) / int(d))
    return float(int(s))


# ============================================================
# Test 2: Generate sortable HTML table
# ============================================================
print("\n--- Test 2: Generate HTML table ---")

# Prepare table rows
rows = []
for i, k in enumerate(nodes):
    m1 = parse_frac(k["m1"])
    m2 = parse_frac(k["m2"])
    rows.append({
        "idx": i + 1,
        "m1_str": k["m1"],
        "m2_str": k["m2"],
        "m1_float": m1,
        "m2_float": m2,
        "chirality": k["chirality"],
        "casimir_so5": k["casimir_so5"],
        "casimir_so5_float": parse_frac(k["casimir_so5"]),
        "casimir_so2": k["casimir_so2"],
        "casimir_so2_float": parse_frac(k["casimir_so2"]),
        "bergman_1": k["bergman_weight_m1_plus_5_2"],
        "bergman_2": k["bergman_weight_m2_plus_3_2"],
        "dim": k["so5_weyl_dim"],
        "sum": k["sum_m1_plus_m2"],
        "in_v0_2": k.get("added_in_v0_2_extension", False),
    })

test_2 = len(rows) == 36
print(f"  Generated {len(rows)} table rows")
print(f"  Test 2: {'PASS' if test_2 else 'FAIL'}")

# ============================================================
# Test 3: Generate inline SVG scatter
# ============================================================
print("\n--- Test 3: Generate SVG scatter ---")

# SVG dimensions
SVG_W, SVG_H = 700, 540
MARGIN_L, MARGIN_R = 60, 30
MARGIN_T, MARGIN_B = 40, 60
PLOT_W = SVG_W - MARGIN_L - MARGIN_R
PLOT_H = SVG_H - MARGIN_T - MARGIN_B

# Data range
M1_MAX = 7.5
M2_MAX = 5.5

def x_coord(m1):
    return MARGIN_L + (m1 / M1_MAX) * PLOT_W

def y_coord(m2):
    return MARGIN_T + PLOT_H - (m2 / M2_MAX) * PLOT_H

# Build SVG circles + diamonds with data attributes for hover
svg_elements = []
for r in rows:
    cx = x_coord(r["m1_float"])
    cy = y_coord(r["m2_float"])
    size = 6 + 0.5 * (r["dim"] ** 0.5)
    color = "#1f77b4" if r["chirality"] == "BOSON" else "#d62728"
    shape = "circle" if r["chirality"] == "BOSON" else "diamond"
    label = f"({r['m1_str']},{r['m2_str']})"
    tooltip = (f"{label} | {r['chirality']} | "
               f"C_SO(5)={r['casimir_so5']} | "
               f"Bergman=({r['bergman_1']},{r['bergman_2']}) | "
               f"dim={r['dim']}")

    if shape == "circle":
        svg_elements.append(
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{size:.1f}" '
            f'fill="{color}" fill-opacity="0.55" stroke="{color}" stroke-width="1.5" '
            f'data-row="{r["idx"]}" data-info="{tooltip}" class="ktype-node" />'
        )
    else:
        # Diamond (rotated square)
        s = size * 1.2
        points = f"{cx},{cy-s} {cx+s},{cy} {cx},{cy+s} {cx-s},{cy}"
        svg_elements.append(
            f'<polygon points="{points}" '
            f'fill="{color}" fill-opacity="0.55" stroke="{color}" stroke-width="1.5" '
            f'data-row="{r["idx"]}" data-info="{tooltip}" class="ktype-node" />'
        )

# Annotation overlays
# T2435 anchor at (1,1)
svg_elements.append(
    f'<circle cx="{x_coord(1):.1f}" cy="{y_coord(1):.1f}" r="20" '
    f'fill="none" stroke="gold" stroke-width="3" stroke-dasharray="4,2" />'
)
svg_elements.append(
    f'<text x="{x_coord(1)+25:.1f}" y="{y_coord(1)-20:.1f}" '
    f'fill="#b8860b" font-size="11" font-weight="bold">T2435 RATIFIED (C_2=6)</text>'
)

# Dirac spinor at (1/2, 1/2)
svg_elements.append(
    f'<circle cx="{x_coord(0.5):.1f}" cy="{y_coord(0.5):.1f}" r="20" '
    f'fill="none" stroke="purple" stroke-width="3" stroke-dasharray="4,2" />'
)
svg_elements.append(
    f'<text x="{x_coord(0.5)-110:.1f}" y="{y_coord(0.5)+25:.1f}" '
    f'fill="purple" font-size="11" font-weight="bold">Dirac (Bergman→(3,2))</text>'
)

# rho-vector
svg_elements.append(
    f'<polygon points="{x_coord(2.5):.1f},{y_coord(1.5)-8:.1f} '
    f'{x_coord(2.5)+8:.1f},{y_coord(1.5):.1f} '
    f'{x_coord(2.5):.1f},{y_coord(1.5)+8:.1f} '
    f'{x_coord(2.5)-8:.1f},{y_coord(1.5):.1f}" '
    f'fill="green" />'
)
svg_elements.append(
    f'<text x="{x_coord(2.5)+15:.1f}" y="{y_coord(1.5)-12:.1f}" '
    f'fill="green" font-size="11" font-weight="bold">ρ = (5/2, 3/2)</text>'
)

# Phase A v0.2 cutoff line
svg_elements.append(
    f'<line x1="{x_coord(0):.1f}" y1="{y_coord(7):.1f}" '
    f'x2="{x_coord(7):.1f}" y2="{y_coord(0):.1f}" '
    f'stroke="navy" stroke-width="1.5" stroke-dasharray="6,4" />'
)

# Phase A v0.1 cutoff line
svg_elements.append(
    f'<line x1="{x_coord(0):.1f}" y1="{y_coord(5):.1f}" '
    f'x2="{x_coord(5):.1f}" y2="{y_coord(0):.1f}" '
    f'stroke="navy" stroke-width="1" stroke-dasharray="2,3" />'
)

# Axes
svg_elements.append(
    f'<line x1="{MARGIN_L}" y1="{MARGIN_T}" x2="{MARGIN_L}" y2="{MARGIN_T + PLOT_H}" '
    f'stroke="#333" stroke-width="1.5" />'
)
svg_elements.append(
    f'<line x1="{MARGIN_L}" y1="{MARGIN_T + PLOT_H}" '
    f'x2="{MARGIN_L + PLOT_W}" y2="{MARGIN_T + PLOT_H}" '
    f'stroke="#333" stroke-width="1.5" />'
)

# Axis labels & ticks
for m1_tick in range(0, 8):
    cx = x_coord(m1_tick)
    cy = MARGIN_T + PLOT_H
    svg_elements.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy+5}" stroke="#333" />')
    svg_elements.append(f'<text x="{cx}" y="{cy+20}" text-anchor="middle" font-size="11">{m1_tick}</text>')

for m2_tick in range(0, 6):
    cy = y_coord(m2_tick)
    svg_elements.append(f'<line x1="{MARGIN_L-5}" y1="{cy}" x2="{MARGIN_L}" y2="{cy}" stroke="#333" />')
    svg_elements.append(f'<text x="{MARGIN_L-10}" y="{cy+4}" text-anchor="end" font-size="11">{m2_tick}</text>')

svg_elements.append(f'<text x="{MARGIN_L + PLOT_W/2}" y="{SVG_H - 15}" text-anchor="middle" font-size="13">m₁ (SO(5) highest weight)</text>')
svg_elements.append(f'<text x="15" y="{MARGIN_T + PLOT_H/2}" text-anchor="middle" font-size="13" transform="rotate(-90 15 {MARGIN_T + PLOT_H/2})">m₂</text>')

svg_content = "\n".join(svg_elements)
test_3 = len(svg_elements) > 30
print(f"  SVG elements generated: {len(svg_elements)}")
print(f"  Test 3: {'PASS' if test_3 else 'FAIL'}")

# ============================================================
# Test 4: Write HTML file
# ============================================================
print("\n--- Test 4: Write self-contained HTML ---")

# Generate table rows HTML
table_html = []
for r in rows:
    classes = "v02-new" if r["in_v0_2"] else ""
    table_html.append(
        f'<tr class="{r["chirality"].lower()} {classes}" '
        f'data-idx="{r["idx"]}" data-chirality="{r["chirality"]}">'
        f'<td>{r["idx"]}</td>'
        f'<td class="ktype-label">({r["m1_str"]}, {r["m2_str"]})</td>'
        f'<td>{r["chirality"]}</td>'
        f'<td>{r["casimir_so5"]}</td>'
        f'<td>{r["casimir_so2"]}</td>'
        f'<td>({r["bergman_1"]}, {r["bergman_2"]})</td>'
        f'<td>{r["dim"]}</td>'
        f'<td>{r["sum"]}</td>'
        f'<td>{"v0.2" if r["in_v0_2"] else "v0.1"}</td>'
        f'</tr>'
    )

# Sortable data for JS
js_data = json.dumps([{
    "idx": r["idx"],
    "m1_str": r["m1_str"],
    "m2_str": r["m2_str"],
    "m1_float": r["m1_float"],
    "m2_float": r["m2_float"],
    "chirality": r["chirality"],
    "casimir_so5": r["casimir_so5"],
    "casimir_so5_float": r["casimir_so5_float"],
    "casimir_so2_float": r["casimir_so2_float"],
    "bergman_1": r["bergman_1"],
    "bergman_2": r["bergman_2"],
    "dim": r["dim"],
    "sum": r["sum"],
    "in_v0_2": r["in_v0_2"],
} for r in rows])

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>BST D_IV⁵ Phase A K-type Graph Interactive Viewer</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
         margin: 20px; color: #222; background: #fafafa; max-width: 1200px; }}
  h1 {{ color: #1a1a1a; }}
  .meta {{ color: #666; font-size: 0.9em; margin-bottom: 20px; }}
  .controls {{ background: #fff; padding: 10px 15px; border: 1px solid #ddd;
              border-radius: 6px; margin-bottom: 15px; display: flex; gap: 15px; align-items: center; }}
  .controls label {{ font-size: 0.9em; }}
  .controls select, .controls button {{ padding: 4px 10px; font-size: 0.9em; }}
  .viewer {{ display: flex; gap: 20px; }}
  .scatter-pane {{ background: #fff; padding: 15px; border: 1px solid #ddd; border-radius: 6px; }}
  .table-pane {{ flex: 1; background: #fff; padding: 15px; border: 1px solid #ddd; border-radius: 6px;
                overflow-x: auto; max-height: 600px; }}
  .ktype-node:hover {{ stroke-width: 3px !important; cursor: pointer; }}
  .selected {{ stroke: black !important; stroke-width: 3px !important; }}
  .tooltip {{ position: absolute; background: rgba(0,0,0,0.85); color: white;
              padding: 6px 10px; border-radius: 4px; font-size: 0.85em;
              pointer-events: none; display: none; z-index: 1000; max-width: 320px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 0.85em; }}
  th {{ background: #f0f0f0; padding: 6px 8px; cursor: pointer; user-select: none;
        text-align: left; border-bottom: 2px solid #ddd; position: sticky; top: 0; }}
  th:hover {{ background: #e0e0e0; }}
  td {{ padding: 4px 8px; border-bottom: 1px solid #eee; }}
  tr.boson {{ background: rgba(31, 119, 180, 0.05); }}
  tr.fermion {{ background: rgba(214, 39, 40, 0.05); }}
  tr.v02-new {{ font-weight: bold; }}
  tr:hover {{ background: rgba(255, 215, 0, 0.15) !important; cursor: pointer; }}
  .ktype-label {{ font-family: "SF Mono", Monaco, monospace; }}
  .legend {{ font-size: 0.85em; color: #666; margin-top: 10px; }}
  .legend-item {{ display: inline-block; margin-right: 15px; }}
  .swatch {{ display: inline-block; width: 14px; height: 14px; margin-right: 4px; vertical-align: middle; }}
</style>
</head>
<body>

<h1>BST D_IV⁵ Phase A K-type Graph — Interactive Viewer</h1>
<div class="meta">
  Domain: D_IV⁵ = SO_0(5,2) / [SO(5) × SO(2)] • K-isotropy: SO(5) × SO(2) with Pin(2) Z₂ cover •
  Cutoff: m₁ + m₂ ≤ 7 • 36 nodes ({data['boson_count']} bosons + {data['fermion_count']} fermions) •
  ρ_D_IV⁵ = (5/2, 3/2) • Source: <code>play/data/k_type_nodes_phase_A.json</code> v0.2 •
  Generated: Toy 3546 (2026-05-27 Elie)
</div>

<div class="controls">
  <label>Filter sector:
    <select id="sector-filter">
      <option value="all">All</option>
      <option value="BOSON">BOSON only</option>
      <option value="FERMION">FERMION only</option>
    </select>
  </label>
  <label>Sort table:
    <select id="sort-by">
      <option value="idx">Default (idx)</option>
      <option value="casimir_so5_float">Casimir SO(5)</option>
      <option value="dim">SO(5) dim</option>
      <option value="m1_float">m₁</option>
      <option value="m2_float">m₂</option>
    </select>
  </label>
  <span class="legend">
    <span class="legend-item"><span class="swatch" style="background: #1f77b4;"></span>BOSON (σ_BF=+1)</span>
    <span class="legend-item"><span class="swatch" style="background: #d62728; clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);"></span>FERMION (σ_BF=−1)</span>
  </span>
</div>

<div class="viewer">

<div class="scatter-pane">
<svg width="{SVG_W}" height="{SVG_H}" id="scatter">
{svg_content}
</svg>
<div class="legend">
  <strong>Annotations:</strong>
  Gold ring = T2435 RATIFIED (Casimir = C_2 = 6) •
  Purple ring = Dirac spinor (Bergman = (N_c, rank)) •
  Green diamond = ρ-vector origin •
  Navy dashed = Phase A cutoff
</div>
</div>

<div class="table-pane">
<table id="ktype-table">
<thead>
<tr>
<th data-sort="idx">#</th>
<th data-sort="ktype">K-type (m₁,m₂)</th>
<th data-sort="chirality">Sector</th>
<th data-sort="casimir_so5_float">C_SO(5)</th>
<th data-sort="casimir_so2_float">C_SO(2)</th>
<th data-sort="bergman">Bergman ρ-wt</th>
<th data-sort="dim">dim_irrep</th>
<th data-sort="sum">m₁+m₂</th>
<th data-sort="version">v0.x</th>
</tr>
</thead>
<tbody>
{chr(10).join(table_html)}
</tbody>
</table>
</div>

</div>

<div id="tooltip" class="tooltip"></div>

<script>
const data = {js_data};

// Tooltip on SVG hover
const tooltip = document.getElementById("tooltip");
document.querySelectorAll(".ktype-node").forEach(node => {{
  node.addEventListener("mousemove", e => {{
    tooltip.textContent = node.dataset.info;
    tooltip.style.left = (e.pageX + 12) + "px";
    tooltip.style.top = (e.pageY + 12) + "px";
    tooltip.style.display = "block";
  }});
  node.addEventListener("mouseleave", () => {{
    tooltip.style.display = "none";
  }});
  node.addEventListener("click", () => {{
    const idx = node.dataset.row;
    document.querySelectorAll(".selected").forEach(el => el.classList.remove("selected"));
    node.classList.add("selected");
    const row = document.querySelector(`tr[data-idx="${{idx}}"]`);
    if (row) {{
      row.scrollIntoView({{behavior: "smooth", block: "center"}});
      row.style.background = "rgba(255, 215, 0, 0.4)";
      setTimeout(() => row.style.background = "", 1500);
    }}
  }});
}});

// Filter
document.getElementById("sector-filter").addEventListener("change", e => {{
  const v = e.target.value;
  document.querySelectorAll(".ktype-node").forEach(node => {{
    const isBoson = node.dataset.info.includes("BOSON");
    const isFermion = node.dataset.info.includes("FERMION");
    if (v === "all") node.style.display = "";
    else if (v === "BOSON" && isBoson) node.style.display = "";
    else if (v === "FERMION" && isFermion) node.style.display = "";
    else node.style.display = "none";
  }});
  document.querySelectorAll("#ktype-table tbody tr").forEach(row => {{
    if (v === "all" || row.dataset.chirality === v) row.style.display = "";
    else row.style.display = "none";
  }});
}});

// Sort
document.getElementById("sort-by").addEventListener("change", e => {{
  const key = e.target.value;
  const tbody = document.querySelector("#ktype-table tbody");
  const rows = Array.from(tbody.querySelectorAll("tr"));
  rows.sort((a, b) => {{
    const ai = parseInt(a.dataset.idx) - 1;
    const bi = parseInt(b.dataset.idx) - 1;
    if (key === "idx") return ai - bi;
    if (key === "dim") return data[ai].dim - data[bi].dim;
    return data[ai][key] - data[bi][key];
  }});
  rows.forEach(r => tbody.appendChild(r));
}});

// Table row click → highlight on scatter
document.querySelectorAll("#ktype-table tbody tr").forEach(row => {{
  row.addEventListener("click", () => {{
    const idx = row.dataset.idx;
    document.querySelectorAll(".selected").forEach(el => el.classList.remove("selected"));
    const node = document.querySelector(`.ktype-node[data-row="${{idx}}"]`);
    if (node) {{
      node.classList.add("selected");
      node.scrollIntoView({{behavior: "smooth", block: "center"}});
    }}
  }});
}});
</script>

</body>
</html>
"""

out_dir = Path("/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/data")
html_path = out_dir / "k_type_graph_phase_A_viewer.html"
with open(html_path, "w") as f:
    f.write(html_template)

print(f"  Wrote {html_path}")
print(f"  Size: {html_path.stat().st_size} bytes")
test_4 = html_path.exists() and html_path.stat().st_size > 5000
print(f"  Test 4: {'PASS' if test_4 else 'FAIL'}")

# ============================================================
# Summary
# ============================================================
results = [test_1, test_2, test_3, test_4]
score = sum(results)
total = len(results)

print("\n" + "=" * 78)
print("INTERACTIVE HTML K-TYPE VIEWER — RESULT")
print("=" * 78)
print(f"""
DELIVERABLE: play/data/k_type_graph_phase_A_viewer.html (~{html_path.stat().st_size//1024}KB)

FEATURES:
  - Single-file self-contained HTML (no external dependencies)
  - SVG scatter plot of 36 K-types positioned at (m_1, m_2)
  - Color/shape by sector (blue circles = bosons, red diamonds = fermions)
  - Marker size proportional to √(SO(5) Weyl dim)
  - Annotation overlays:
    * T2435 RATIFIED gold ring at (1,1) Casimir = C_2 = 6
    * Dirac spinor purple ring at (1/2, 1/2) Bergman = (N_c, rank)
    * ρ-vector green diamond at (5/2, 3/2) = (n_C/2, N_c/2)
    * Phase A cutoff lines (v0.1 dotted ≤5; v0.2 dashed ≤7)
  - Interactive features:
    * Hover scatter node → tooltip with full K-type properties
    * Click scatter node → highlight + scroll to table row
    * Sortable table (by Casimir, dim, m_1, m_2)
    * Sector filter (all / BOSON / FERMION)
    * Click table row → highlight scatter node
  - v0.1 vs v0.2 visual differentiation (v0.2 new rows bolded)

OPEN: file://{html_path}

DOWNSTREAM USE:
  - Team navigation tool for inspecting K-type properties
  - Visual aid for Grace catalog matching (sortable + filterable)
  - Vol 15 Ch 9 case study integration (Keeper)
  - Lyra Multi-phase quiver v0.2+ reference when filed
  - External presentation companion
""")

print(f"SCORE: {score}/{total}")
print(f"Toy 3546 HTML K-type viewer: {'PASS' if score == total else 'PARTIAL'}")
print()
print(f"Interactive viewer: {html_path}")
print()
print("— Elie, Toy 3546 HTML K-type viewer 2026-05-27 Wednesday 09:50 EDT")
sys.exit(0 if score == total else 1)
