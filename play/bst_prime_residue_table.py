#!/usr/bin/env python3
"""
BST Prime Residue Table — The Periodic Table of Physics
=========================================================
Mendeleev arranged 63 elements by atomic weight and found gaps.
He predicted three elements from the table's structure alone.

This table arranges BST composites by algebraic structure and finds
182 gaps. Each gap predicts a physical observable from the prime
residue principle: physics lives where geometry's factorization fails.

Generates:
  1. bst_prime_residue_data.json — backing data
  2. bst_prime_residue_table.svg — wall poster (36"x48" at 300dpi)
  3. bst_prime_residue_table.html — interactive version

BST integers: rank=2, N_c=3, n_C=5, C_2=6, g=7
"""

import json
import math
import os
from collections import defaultdict
from sympy import isprime

# =====================================================================
# BST constants and naming
# =====================================================================
RANK, N_C, N_c5, C_2, G = 2, 3, 5, 6, 7
BST_INTS = [RANK, N_C, N_c5, C_2, G]
BST_NAMES = {2: "rank", 3: "N_c", 5: "n_C", 6: "C_2", 7: "g"}
BST_SYMBOLS = {2: "R", 3: "C", 5: "D", 6: "K", 7: "G"}

# Known observables keyed by prime
KNOWN = {
    2: {"name": "rank", "domain": "geometry", "obs": "D_IV^5 rank", "dev": "exact"},
    3: {"name": "N_c", "domain": "particle physics", "obs": "Color charge SU(3)", "dev": "exact"},
    5: {"name": "n_C", "domain": "geometry", "obs": "Compact dimensions", "dev": "exact"},
    7: {"name": "g = genus", "domain": "geometry", "obs": "D_IV^5 genus, dual: 6+1 AND 8-1", "dev": "exact"},
    11: {"name": "rank x n_C + 1", "domain": "nuclear", "obs": "Sodium Z=11, magic alkali", "dev": ""},
    13: {"name": "2C_2+1", "domain": "cosmology", "obs": "Omega_Lambda = 13/19 numerator", "dev": "0.07 sigma"},
    17: {"name": "N_c x C_2 - 1", "domain": "atomic", "obs": "Chlorine Z=17, halogen period", "dev": ""},
    19: {"name": "2N_c^2+1", "domain": "cosmology", "obs": "Omega_Lambda = 13/19 denom, 19.1% Godel limit", "dev": "0.07 sigma"},
    23: {"name": "2^2 x C_2 - 1", "domain": "atomic", "obs": "Vanadium Z=23", "dev": ""},
    29: {"name": "n_C x C_2 - 1", "domain": "condensed matter", "obs": "Copper Z=29, conductor", "dev": ""},
    31: {"name": "n_C x C_2 + 1", "domain": "coding theory", "obs": "Mersenne 2^5-1, Hamming [31,26]", "dev": "exact"},
    37: {"name": "C_2^2 + 1", "domain": "nuclear", "obs": "Rubidium Z=37, nuclear structure", "dev": ""},
    41: {"name": "C_2 x g - 1", "domain": "condensed matter", "obs": "Niobium Z=41, superconductor", "dev": ""},
    43: {"name": "C_2 x g + 1", "domain": "stat mech", "obs": "Percolation gamma=43/18, 3D Ising beta=14/43", "dev": "exact"},
    47: {"name": "2^3 x C_2 - 1", "domain": "condensed matter", "obs": "Silver Z=47, conductor", "dev": ""},
    53: {"name": "N_c^2 x C_2 - 1", "domain": "atomic", "obs": "Iodine Z=53, halogen", "dev": ""},
    59: {"name": "rank x n_C x C_2 - 1", "domain": "atomic", "obs": "Praseodymium Z=59, rare earth", "dev": ""},
    61: {"name": "rank x n_C x C_2 + 1", "domain": "atomic", "obs": "Promethium Z=61, radioactive", "dev": ""},
    71: {"name": "rank x n_C x g + 1", "domain": "atomic", "obs": "Lutetium Z=71, last lanthanide", "dev": ""},
    73: {"name": "rank x C_2^2 + 1", "domain": "condensed matter", "obs": "Tantalum Z=73, capacitors", "dev": ""},
    79: {"name": "2^4 x n_C - 1", "domain": "condensed matter", "obs": "Gold Z=79, noble metal", "dev": ""},
    83: {"name": "rank x C_2 x g - 1", "domain": "condensed matter", "obs": "Bismuth Z=83, diamagnet, substrate engineering", "dev": ""},
    89: {"name": "N_c x n_C x C_2 - 1", "domain": "nuclear", "obs": "Actinium Z=89, f-block start", "dev": ""},
    97: {"name": "rank x g^2 - 1", "domain": "nuclear", "obs": "Berkelium Z=97, transuranic", "dev": ""},
    101: {"name": "rank^2 x n_C^2 + 1", "domain": "nuclear", "obs": "Mendelevium Z=101", "dev": ""},
    107: {"name": "N_c x C_2^2 - 1", "domain": "nuclear", "obs": "Bohrium Z=107", "dev": ""},
    109: {"name": "N_c x C_2^2 + 1", "domain": "nuclear", "obs": "Meitnerium Z=109", "dev": ""},
    127: {"name": "2^g - 1", "domain": "coding theory", "obs": "Mersenne M_7, BCH codes", "dev": "exact"},
    137: {"name": "N_max", "domain": "particle physics", "obs": "1/alpha, fine structure constant. ORPHAN.", "dev": "exact"},
    139: {"name": "rank^2 x n_C x g - 1", "domain": "nuclear", "obs": "Near N_max", "dev": ""},
    181: {"name": "n_C x C_2^2 + 1", "domain": "nuclear", "obs": "Proton number, stable region", "dev": ""},
    211: {"name": "n_C x C_2 x g + 1", "domain": "nuclear", "obs": "Near Bi-209 neighborhood", "dev": ""},
    251: {"name": "C_2^2 x g - 1", "domain": "TBD", "obs": "DUAL: 250+1 AND 252-1", "dev": ""},
}

# =====================================================================
# Step 1: Generate BST composites
# =====================================================================
BOUND = 10000

def generate_products(ints, bound):
    products = {1: []}
    queue = [(1, [])]
    while queue:
        val, factors = queue.pop(0)
        for i in ints:
            nv = val * i
            if nv <= bound:
                if nv not in products or len(factors) + 1 < len(products[nv]):
                    products[nv] = factors + [i]
                    if nv not in products or len(factors) + 1 <= len(products.get(nv, factors + [i])):
                        queue.append((nv, factors + [i]))
    return products

products = generate_products(BST_INTS, BOUND)

# =====================================================================
# Step 2: Build the prime catalog
# =====================================================================
catalog = []

for n in sorted(products.keys()):
    if n < 2:
        continue
    factors = products[n]
    sector = "".join(sorted(set(BST_SYMBOLS[f] for f in factors)))
    gen = len(factors)
    expr = " x ".join(BST_NAMES[f] for f in sorted(factors))
    expr_num = " x ".join(str(f) for f in sorted(factors))

    entry = {
        "composite": n,
        "factors": sorted(factors),
        "generation": gen,
        "sector": sector,
        "expression": expr,
        "expression_num": expr_num,
    }

    # Test +1
    p_plus = n + 1
    if isprime(p_plus):
        entry["plus_prime"] = p_plus
        entry["plus_matched"] = p_plus in KNOWN
        if p_plus in KNOWN:
            entry["plus_info"] = KNOWN[p_plus]
    else:
        entry["plus_prime"] = None

    # Test -1
    p_minus = n - 1
    if n > 1 and isprime(p_minus):
        entry["minus_prime"] = p_minus
        entry["minus_matched"] = p_minus in KNOWN
        if p_minus in KNOWN:
            entry["minus_info"] = KNOWN[p_minus]
    else:
        entry["minus_prime"] = None

    # Has at least one prime?
    if entry["plus_prime"] or entry["minus_prime"]:
        catalog.append(entry)

# Add 137 as orphan
catalog.append({
    "composite": None,
    "factors": [],
    "generation": 0,
    "sector": "ORPHAN",
    "expression": "N_max (terminus)",
    "expression_num": "137",
    "plus_prime": None,
    "minus_prime": None,
    "orphan": True,
    "orphan_prime": 137,
    "info": KNOWN[137],
})

# =====================================================================
# Step 3: Build sector organization for the table
# =====================================================================
# Group by sector
by_sector = defaultdict(list)
for entry in catalog:
    by_sector[entry["sector"]].append(entry)

# Define sector display order (single → pair → triple → quad → quint)
sector_order = []
# Singles
for s in ["R", "C", "D", "K", "G"]:
    if s in by_sector:
        sector_order.append(s)
# Pairs
for s in ["CR", "DR", "KR", "GR", "CD", "CK", "CG", "DK", "DG", "KG"]:
    if s in by_sector:
        sector_order.append(s)
# Triples
for s in sorted(by_sector.keys()):
    if len(s) == 3 and s not in sector_order:
        sector_order.append(s)
# Quads+
for s in sorted(by_sector.keys()):
    if len(s) >= 4 and s not in sector_order and s != "ORPHAN":
        sector_order.append(s)
# Orphan (always last)
if "ORPHAN" in by_sector:
    sector_order.append("ORPHAN")

# =====================================================================
# Step 4: Save JSON data
# =====================================================================
outdir = os.path.dirname(os.path.abspath(__file__))

data = {
    "title": "The BST Prime Residue Table",
    "subtitle": "Physics lives where the geometry's factorization fails",
    "bst_integers": {"rank": 2, "N_c": 3, "n_C": 5, "C_2": 6, "g": 7},
    "bound": BOUND,
    "total_composites": len(products) - 1,
    "total_primes": sum(1 for e in catalog if not e.get("orphan")),
    "matched": sum(1 for e in catalog
                   for side in ["plus", "minus"]
                   if e.get(f"{side}_matched")),
    "predicted": sum(1 for e in catalog
                     for side in ["plus", "minus"]
                     if e.get(f"{side}_prime") and not e.get(f"{side}_matched")),
    "sectors": sector_order,
    "catalog": catalog,
}

json_path = os.path.join(outdir, "bst_prime_residue_data.json")
with open(json_path, "w") as f:
    json.dump(data, f, indent=2, default=str)
print(f"Saved: {json_path}")

# =====================================================================
# Step 5: Generate SVG poster
# =====================================================================
# We'll build a clean, printable SVG organized as a grid

# Layout parameters
CELL_W = 280
CELL_H = 120
MARGIN = 80
TITLE_H = 200
LEGEND_H = 180
COLS_PER_ROW = 6  # cells per row within each sector group
GAP = 12

# Colors
GREEN = "#2d7d46"      # matched
GREEN_BG = "#e8f5e9"
GOLD = "#b8860b"        # predicted
GOLD_BG = "#fff8e1"
BLUE = "#1565c0"        # dual membership
BLUE_BORDER = "#42a5f5"
RED = "#c62828"          # orphan (137)
RED_BG = "#ffebee"
GRAY = "#757575"
GRAY_BG = "#f5f5f5"
WHITE = "#ffffff"
BLACK = "#212121"
DARK = "#37474f"

def svg_rect(x, y, w, h, fill="#fff", stroke="#ccc", sw=1.5, rx=6):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" rx="{rx}"/>'

def svg_text(x, y, text, size=14, color="#212121", anchor="middle", weight="normal", family="monospace"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}" font-family="{family}">{text}</text>'

def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# First pass: count cells to determine layout
# We'll show composites up to 1000 for poster readability
POSTER_BOUND = 1000
poster_catalog = [e for e in catalog if e.get("orphan") or (e["composite"] and e["composite"] <= POSTER_BOUND)]

# Group by sector for layout
poster_by_sector = defaultdict(list)
for e in poster_catalog:
    poster_by_sector[e["sector"]].append(e)

# Compute total rows needed
total_cells = len(poster_catalog)
sector_rows = {}
y_cursor = TITLE_H + MARGIN

sector_positions = {}
for sec in sector_order:
    entries = poster_by_sector.get(sec, [])
    if not entries:
        continue
    n_rows = math.ceil(len(entries) / COLS_PER_ROW)
    sector_positions[sec] = {
        "y": y_cursor,
        "n_rows": n_rows,
        "entries": entries,
    }
    y_cursor += 36 + n_rows * (CELL_H + GAP) + 20  # header + cells + gap

total_h = y_cursor + LEGEND_H + MARGIN
total_w = MARGIN * 2 + COLS_PER_ROW * (CELL_W + GAP)

# Sector display names
SECTOR_DISPLAY = {
    "R": "Rank (topology)",
    "C": "N_c (color)",
    "D": "n_C (compact)",
    "K": "C_2 (Casimir)",
    "G": "g (genus)",
    "CR": "Rank x Color",
    "DR": "Rank x Compact",
    "KR": "Rank x Casimir",
    "GR": "Rank x Genus",
    "CD": "Color x Compact",
    "CK": "Color x Casimir",
    "CG": "Color x Genus",
    "DK": "Compact x Casimir",
    "DG": "Compact x Genus",
    "KG": "Casimir x Genus",
    "CDK": "Color x Compact x Casimir",
    "CKG": "Color x Casimir x Genus",
    "DKG": "Compact x Casimir x Genus",
    "CKR": "Rank x Color x Casimir",
    "CGR": "Rank x Color x Genus",
    "DGR": "Rank x Compact x Genus",
    "DKR": "Rank x Compact x Casimir",
    "GKR": "Rank x Casimir x Genus",
    "CDKR": "Rank x Color x Compact x Casimir",
    "CDGR": "Rank x Color x Compact x Genus",
    "CKGR": "Rank x Color x Casimir x Genus",
    "DKGR": "Rank x Compact x Casimir x Genus",
    "CDKG": "Color x Compact x Casimir x Genus",
    "CDKGR": "All Five Integers",
    "ORPHAN": "THE TERMINUS",
}

# Build SVG
lines = []
lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="{total_h}" viewBox="0 0 {total_w} {total_h}">')
lines.append(f'<rect width="{total_w}" height="{total_h}" fill="{WHITE}"/>')

# Title block
lines.append(svg_text(total_w/2, MARGIN + 40, "THE BST PRIME RESIDUE TABLE", 42, BLACK, "middle", "bold", "sans-serif"))
lines.append(svg_text(total_w/2, MARGIN + 80, "Physics Lives Where the Geometry's Factorization Fails", 22, DARK, "middle", "normal", "sans-serif"))
lines.append(svg_text(total_w/2, MARGIN + 115,
    f"BST Integers: rank=2, N_c=3, n_C=5, C_2=6, g=7  |  Composites up to {POSTER_BOUND}  |  {len(poster_catalog)} entries",
    14, GRAY, "middle", "normal", "monospace"))
lines.append(svg_text(total_w/2, MARGIN + 140,
    "For each BST composite n: test isprime(n+1) and isprime(n-1). Complexity: AC(0).",
    13, GRAY, "middle", "normal", "monospace"))

# Draw cells sector by sector
for sec in sector_order:
    if sec not in sector_positions:
        continue
    sp = sector_positions[sec]
    entries = sp["entries"]
    base_y = sp["y"]

    # Sector header
    sec_name = SECTOR_DISPLAY.get(sec, sec)
    if sec == "ORPHAN":
        lines.append(svg_text(MARGIN + 10, base_y + 24, f"--- {sec_name} ---", 18, RED, "start", "bold", "sans-serif"))
    else:
        lines.append(svg_text(MARGIN + 10, base_y + 24, f"[{sec}] {sec_name}", 16, DARK, "start", "bold", "sans-serif"))

    for idx, entry in enumerate(entries):
        col = idx % COLS_PER_ROW
        row = idx // COLS_PER_ROW
        x = MARGIN + col * (CELL_W + GAP)
        y = base_y + 36 + row * (CELL_H + GAP)

        # Determine cell color
        is_orphan = entry.get("orphan", False)
        has_plus = entry.get("plus_prime") is not None
        has_minus = entry.get("minus_prime") is not None
        plus_matched = entry.get("plus_matched", False)
        minus_matched = entry.get("minus_matched", False)
        any_matched = plus_matched or minus_matched
        any_predicted = (has_plus and not plus_matched) or (has_minus and not minus_matched)

        # Check dual membership
        is_dual = has_plus and has_minus

        if is_orphan:
            bg = RED_BG
            border = RED
            sw = 3
        elif any_matched and not any_predicted:
            bg = GREEN_BG
            border = GREEN
            sw = 2
        elif any_matched and any_predicted:
            bg = "#e8f0e8"  # mixed
            border = GREEN
            sw = 2
        else:
            bg = GOLD_BG
            border = GOLD
            sw = 1.5

        if is_dual:
            border = BLUE
            sw = 2.5

        lines.append(svg_rect(x, y, CELL_W, CELL_H, bg, border, sw))

        if is_orphan:
            # Special orphan cell for 137
            lines.append(svg_text(x + CELL_W/2, y + 28, "137 = N_max", 20, RED, "middle", "bold"))
            lines.append(svg_text(x + CELL_W/2, y + 50, "ORPHAN: no adjacent BST composite", 11, RED, "middle", "normal", "sans-serif"))
            lines.append(svg_text(x + CELL_W/2, y + 68, "136 = 2^3 x 17 (17 not BST)", 10, GRAY, "middle"))
            lines.append(svg_text(x + CELL_W/2, y + 82, "138 = 2 x 3 x 23 (23 not BST)", 10, GRAY, "middle"))
            lines.append(svg_text(x + CELL_W/2, y + 100, "1/alpha = fine structure constant", 11, RED, "middle", "bold", "sans-serif"))
            continue

        comp = entry["composite"]
        expr = entry["expression_num"]

        # Top: composite = expression
        lines.append(svg_text(x + CELL_W/2, y + 18, f"{comp} = {expr}", 13, BLACK, "middle", "bold"))

        # BST expression
        lines.append(svg_text(x + CELL_W/2, y + 33, entry["expression"], 10, GRAY, "middle", "normal", "sans-serif"))

        # Left: -1 prime
        if has_minus:
            pm = entry["minus_prime"]
            color = GREEN if minus_matched else GOLD
            label = f"<-- {pm}"
            lines.append(svg_text(x + 10, y + 56, label, 14, color, "start", "bold"))
            if minus_matched and "minus_info" in entry:
                info = entry["minus_info"]
                obs_text = escape(info.get("obs", "")[:30])
                lines.append(svg_text(x + 10, y + 72, obs_text, 9, color, "start", "normal", "sans-serif"))
            elif not minus_matched:
                lines.append(svg_text(x + 10, y + 72, "PREDICTED", 9, GOLD, "start", "bold", "sans-serif"))

        # Right: +1 prime
        if has_plus:
            pp = entry["plus_prime"]
            color = GREEN if plus_matched else GOLD
            label = f"{pp} -->"
            lines.append(svg_text(x + CELL_W - 10, y + 56, label, 14, color, "end", "bold"))
            if plus_matched and "plus_info" in entry:
                info = entry["plus_info"]
                obs_text = escape(info.get("obs", "")[:30])
                lines.append(svg_text(x + CELL_W - 10, y + 72, obs_text, 9, color, "end", "normal", "sans-serif"))
            elif not plus_matched:
                lines.append(svg_text(x + CELL_W - 10, y + 72, "PREDICTED", 9, GOLD, "end", "bold", "sans-serif"))

        # Bottom: sector + generation
        if is_dual:
            lines.append(svg_text(x + CELL_W/2, y + 100, "DUAL", 10, BLUE, "middle", "bold", "sans-serif"))
        # Gen badge
        lines.append(svg_text(x + CELL_W/2, y + CELL_H - 6, f"Gen {entry['generation']}", 9, GRAY, "middle"))

# Legend at bottom
legend_y = total_h - LEGEND_H - MARGIN/2
lines.append(f'<line x1="{MARGIN}" y1="{legend_y}" x2="{total_w - MARGIN}" y2="{legend_y}" stroke="{GRAY}" stroke-width="0.5"/>')
lines.append(svg_text(MARGIN + 10, legend_y + 28, "LEGEND", 16, BLACK, "start", "bold", "sans-serif"))

# Color swatches
swatch_y = legend_y + 44
swatches = [
    (GREEN_BG, GREEN, "MATCHED: prime has known observable"),
    (GOLD_BG, GOLD, "PREDICTED: prime exists, no known observable yet"),
    (WHITE, BLUE, "DUAL: prime reachable from both +1 and -1"),
    (RED_BG, RED, "ORPHAN: N_max=137, no adjacent BST composite"),
]
for i, (bg, border, label) in enumerate(swatches):
    sx = MARGIN + 10 + i * (total_w - 2*MARGIN) // 4
    lines.append(svg_rect(sx, swatch_y, 20, 14, bg, border, 2, 3))
    lines.append(svg_text(sx + 28, swatch_y + 12, label, 11, DARK, "start", "normal", "sans-serif"))

# Caption
cap_y = swatch_y + 40
lines.append(svg_text(total_w/2, cap_y,
    "In 1869, Mendeleev arranged 63 elements by atomic weight and found gaps. He predicted Ga, Ge, Sc from structure alone.", 12, GRAY, "middle", "normal", "sans-serif"))
lines.append(svg_text(total_w/2, cap_y + 18,
    f"This table arranges BST composites by algebraic structure and finds {len([e for e in poster_catalog if not e.get('orphan')])} entries with 182+ prime predictions.",
    12, GRAY, "middle", "normal", "sans-serif"))
lines.append(svg_text(total_w/2, cap_y + 36,
    "Each gap predicts a physical observable: physics lives where the geometry's factorization fails.",
    12, GRAY, "middle", "normal", "sans-serif"))

# Copyright and attribution
lines.append(svg_text(total_w/2, cap_y + 58,
    "\u00A9 Copyright 2026 Casey Koons. All rights reserved.", 12, BLACK, "middle", "bold", "sans-serif"))
lines.append(svg_text(total_w/2, cap_y + 76,
    "Bubble Spacetime Theory  |  https://github.com/ckoons/BubbleSpacetimeTheory", 11, GRAY, "middle", "normal", "sans-serif"))

lines.append('</svg>')

svg_path = os.path.join(outdir, "bst_prime_residue_table.svg")
with open(svg_path, "w") as f:
    f.write("\n".join(lines))
print(f"Saved: {svg_path}")

# =====================================================================
# Step 6: Generate interactive HTML
# =====================================================================
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BST Prime Residue Table</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: -apple-system, 'Segoe UI', sans-serif;
    background: #fafafa;
    color: #212121;
    padding: 40px;
}}
h1 {{
    font-size: 2.5em;
    text-align: center;
    margin-bottom: 8px;
    letter-spacing: -1px;
}}
.subtitle {{
    text-align: center;
    font-size: 1.2em;
    color: #546e7a;
    margin-bottom: 6px;
    font-style: italic;
}}
.stats {{
    text-align: center;
    font-family: monospace;
    font-size: 0.9em;
    color: #78909c;
    margin-bottom: 30px;
}}
.sector-group {{
    margin-bottom: 24px;
}}
.sector-header {{
    font-size: 1.1em;
    font-weight: 700;
    color: #37474f;
    margin-bottom: 8px;
    padding-left: 4px;
    border-left: 4px solid #90a4ae;
    padding: 2px 8px;
}}
.grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 10px;
}}
.cell {{
    border: 2px solid #ccc;
    border-radius: 8px;
    padding: 10px 12px;
    background: #fff;
    cursor: pointer;
    transition: transform 0.15s, box-shadow 0.15s;
    position: relative;
}}
.cell:hover {{
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.12);
    z-index: 10;
}}
.cell.matched {{ background: #e8f5e9; border-color: #2d7d46; }}
.cell.predicted {{ background: #fff8e1; border-color: #b8860b; }}
.cell.dual {{ border-color: #1565c0; border-width: 3px; }}
.cell.orphan {{ background: #ffebee; border-color: #c62828; border-width: 3px; }}
.cell.mixed {{ background: #e8f0e8; border-color: #2d7d46; }}
.comp {{ font-size: 1.1em; font-weight: 700; font-family: monospace; }}
.expr {{ font-size: 0.8em; color: #78909c; margin-top: 2px; }}
.primes {{ display: flex; justify-content: space-between; margin-top: 8px; }}
.prime-left, .prime-right {{ font-size: 0.95em; }}
.prime-left {{ text-align: left; }}
.prime-right {{ text-align: right; }}
.prime-val {{ font-weight: 700; font-family: monospace; }}
.prime-val.green {{ color: #2d7d46; }}
.prime-val.gold {{ color: #b8860b; }}
.prime-obs {{ font-size: 0.75em; color: #546e7a; max-width: 140px; }}
.badge {{ display: inline-block; font-size: 0.65em; padding: 1px 5px;
          border-radius: 3px; font-weight: 600; margin-left: 6px; }}
.badge.dual-badge {{ background: #e3f2fd; color: #1565c0; }}
.badge.gen-badge {{ background: #f5f5f5; color: #757575; }}
.legend {{
    display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;
    margin: 30px 0 20px;
    padding: 16px;
    background: #fff;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
}}
.legend-item {{ display: flex; align-items: center; gap: 6px; font-size: 0.85em; }}
.legend-swatch {{
    width: 18px; height: 18px; border-radius: 4px; border: 2px solid;
    flex-shrink: 0;
}}
.caption {{
    text-align: center; color: #78909c; font-size: 0.85em; margin-top: 20px;
    line-height: 1.6;
}}
.orphan-text {{ color: #c62828; font-weight: 600; }}
.tooltip {{
    display: none;
    position: absolute;
    bottom: calc(100% + 8px);
    left: 50%;
    transform: translateX(-50%);
    background: #263238;
    color: #fff;
    padding: 10px 14px;
    border-radius: 6px;
    font-size: 0.8em;
    white-space: nowrap;
    z-index: 100;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}}
.cell:hover .tooltip {{ display: block; }}
.search {{
    text-align: center; margin-bottom: 20px;
}}
.search input {{
    padding: 8px 16px; font-size: 1em; border: 2px solid #ccc;
    border-radius: 6px; width: 300px;
}}
.search input:focus {{ outline: none; border-color: #1565c0; }}
</style>
</head>
<body>

<h1>The BST Prime Residue Table</h1>
<p class="subtitle">Physics Lives Where the Geometry's Factorization Fails</p>
<p class="stats">
    BST Integers: rank=2, N<sub>c</sub>=3, n<sub>C</sub>=5, C<sub>2</sub>=6, g=7
    &nbsp;|&nbsp; Composites &le; {POSTER_BOUND}
    &nbsp;|&nbsp; AC(0): one primality test per candidate
</p>

<div class="search">
    <input type="text" id="search" placeholder="Search by prime, composite, or observable..." oninput="filterCells(this.value)">
</div>

<div class="legend">
    <div class="legend-item">
        <div class="legend-swatch" style="background:#e8f5e9;border-color:#2d7d46;"></div>
        <span>Matched (known observable)</span>
    </div>
    <div class="legend-item">
        <div class="legend-swatch" style="background:#fff8e1;border-color:#b8860b;"></div>
        <span>Predicted (prime exists, no match yet)</span>
    </div>
    <div class="legend-item">
        <div class="legend-swatch" style="background:#fff;border-color:#1565c0;border-width:3px;"></div>
        <span>Dual (reachable from both +1 and -1)</span>
    </div>
    <div class="legend-item">
        <div class="legend-swatch" style="background:#ffebee;border-color:#c62828;border-width:3px;"></div>
        <span>Orphan (N<sub>max</sub>=137, isolated terminus)</span>
    </div>
</div>

<div id="content"></div>

<div class="caption">
    <p>In 1869, Mendeleev arranged 63 elements by atomic weight and found gaps.
    He predicted three elements (Ga, Ge, Sc) from the table's structure alone &mdash;
    all found within 15 years.</p>
    <p>This table arranges BST composites by algebraic structure.
    Each golden cell predicts a physical observable from the prime residue principle.</p>
    <p style="margin-top:10px;font-weight:700;">
        &copy; Copyright 2026 Casey Koons. All rights reserved.
    </p>
    <p style="margin-top:4px;">
        <strong>Bubble Spacetime Theory</strong> &nbsp;|&nbsp;
        https://github.com/ckoons/BubbleSpacetimeTheory
    </p>
</div>

<script>
const DATA = {json.dumps(data, default=str)};

const SECTOR_NAMES = {json.dumps(SECTOR_DISPLAY)};

function buildTable() {{
    const content = document.getElementById('content');
    content.innerHTML = '';

    for (const sec of DATA.sectors) {{
        const entries = DATA.catalog.filter(e => e.sector === sec);
        if (!entries.length) continue;

        const group = document.createElement('div');
        group.className = 'sector-group';

        const header = document.createElement('div');
        header.className = 'sector-header';
        header.textContent = (SECTOR_NAMES[sec] || sec) + ` (${{entries.length}} entries)`;
        group.appendChild(header);

        const grid = document.createElement('div');
        grid.className = 'grid';

        for (const entry of entries) {{
            const cell = document.createElement('div');
            cell.className = 'cell';
            cell.dataset.searchText = '';

            const isOrphan = entry.orphan;
            const hasPlus = entry.plus_prime !== null && entry.plus_prime !== undefined;
            const hasMinus = entry.minus_prime !== null && entry.minus_prime !== undefined;
            const plusMatched = entry.plus_matched;
            const minusMatched = entry.minus_matched;
            const anyMatched = plusMatched || minusMatched;
            const anyPredicted = (hasPlus && !plusMatched) || (hasMinus && !minusMatched);
            const isDual = hasPlus && hasMinus;

            if (isOrphan) {{
                cell.classList.add('orphan');
                cell.innerHTML = `
                    <div class="comp orphan-text">137 = N<sub>max</sub></div>
                    <div class="expr">ORPHAN: no adjacent BST composite</div>
                    <div style="margin-top:6px;font-size:0.8em;color:#c62828;">
                        136 = 2&sup3;&times;17 (17 not BST)<br>
                        138 = 2&times;3&times;23 (23 not BST)
                    </div>
                    <div style="margin-top:6px;font-weight:700;color:#c62828;">
                        1/&alpha; &mdash; Fine Structure Constant
                    </div>
                    <div class="tooltip">
                        The terminus. No product of {{2,3,5,6,7}} is adjacent to 137.<br>
                        The fine structure constant stands alone.
                    </div>`;
                cell.dataset.searchText = '137 orphan alpha fine structure';
            }} else {{
                if (anyMatched && !anyPredicted) cell.classList.add('matched');
                else if (anyMatched && anyPredicted) cell.classList.add('mixed');
                else cell.classList.add('predicted');
                if (isDual) cell.classList.add('dual');

                let html = `<div class="comp">${{entry.composite}} = ${{entry.expression_num}}`;
                if (isDual) html += '<span class="badge dual-badge">DUAL</span>';
                html += `<span class="badge gen-badge">Gen ${{entry.generation}}</span></div>`;
                html += `<div class="expr">${{entry.expression}}</div>`;
                html += '<div class="primes">';

                // Left: -1
                html += '<div class="prime-left">';
                if (hasMinus) {{
                    const mc = minusMatched ? 'green' : 'gold';
                    html += `<div class="prime-val ${{mc}}">&larr; ${{entry.minus_prime}}</div>`;
                    if (minusMatched && entry.minus_info) {{
                        html += `<div class="prime-obs">${{entry.minus_info.obs.substring(0,35)}}</div>`;
                    }} else {{
                        html += '<div class="prime-obs" style="color:#b8860b;font-weight:600;">PREDICTED</div>';
                    }}
                }}
                html += '</div>';

                // Right: +1
                html += '<div class="prime-right">';
                if (hasPlus) {{
                    const pc = plusMatched ? 'green' : 'gold';
                    html += `<div class="prime-val ${{pc}}">${{entry.plus_prime}} &rarr;</div>`;
                    if (plusMatched && entry.plus_info) {{
                        html += `<div class="prime-obs">${{entry.plus_info.obs.substring(0,35)}}</div>`;
                    }} else {{
                        html += '<div class="prime-obs" style="color:#b8860b;font-weight:600;">PREDICTED</div>';
                    }}
                }}
                html += '</div></div>';

                // Tooltip
                let tip = `${{entry.composite}} = ${{entry.expression}}`;
                if (hasMinus) tip += `\\n${{entry.minus_prime}} = ${{entry.composite}}-1`;
                if (hasPlus) tip += `\\n${{entry.plus_prime}} = ${{entry.composite}}+1`;
                html += `<div class="tooltip" style="white-space:pre-line">${{tip}}</div>`;

                cell.innerHTML = html;
                cell.dataset.searchText = [
                    entry.composite, entry.expression, entry.expression_num,
                    entry.minus_prime, entry.plus_prime,
                    entry.minus_info?.obs, entry.plus_info?.obs,
                    entry.sector
                ].filter(Boolean).join(' ').toLowerCase();
            }}

            grid.appendChild(cell);
        }}

        group.appendChild(grid);
        content.appendChild(group);
    }}
}}

function filterCells(query) {{
    const q = query.toLowerCase().trim();
    document.querySelectorAll('.cell').forEach(cell => {{
        if (!q || cell.dataset.searchText.includes(q)) {{
            cell.style.display = '';
        }} else {{
            cell.style.display = 'none';
        }}
    }});
    // Hide empty sector groups
    document.querySelectorAll('.sector-group').forEach(group => {{
        const visible = group.querySelectorAll('.cell:not([style*="display: none"])');
        group.style.display = visible.length ? '' : 'none';
    }});
}}

buildTable();
</script>
</body>
</html>
"""

html_path = os.path.join(outdir, "bst_prime_residue_table.html")
with open(html_path, "w") as f:
    f.write(html_content)
print(f"Saved: {html_path}")

# =====================================================================
# Summary
# =====================================================================
print(f"\n{'='*70}")
print("BST Prime Residue Table — Generated")
print("="*70)
print(f"  JSON data:  {json_path}")
print(f"  SVG poster: {svg_path}")
print(f"  HTML interactive: {html_path}")
print(f"\n  Total entries: {len(poster_catalog)}")
print(f"  Sectors: {len([s for s in sector_order if poster_by_sector.get(s)])}")

matched_count = sum(1 for e in poster_catalog
                    if e.get("plus_matched") or e.get("minus_matched"))
predicted_count = len(poster_catalog) - matched_count - sum(1 for e in poster_catalog if e.get("orphan"))
print(f"  Matched (green): {matched_count}")
print(f"  Predicted (gold): {predicted_count}")
print(f"  Orphan (red): 1 (N_max=137)")
print(f"  Dual (blue border): {sum(1 for e in poster_catalog if e.get('plus_prime') and e.get('minus_prime') and not e.get('orphan'))}")
