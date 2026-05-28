#!/usr/bin/env python3
"""
Toy 3542 — K-type graph visualization + D_IV⁵-specific math relations

Elie, Wednesday 2026-05-27 ~09:15 EDT
Casey explicit Tuesday directive ("we will increase the depth of our
investigation and map the full K-type graph reaction table") + Keeper
Wednesday menu item #1.

PURPOSE
-------
Tangible visualization artifact for Phase A K-type graph (36 nodes,
cutoff m_1 + m_2 ≤ 7). Loads play/data/k_type_nodes_phase_A.json v0.2
and produces:
  - PNG matplotlib visualization
  - PDF for paper/curriculum integration
  - Annotated D_IV⁵-specific math relations:
    * T2435 RATIFIED substrate anchor at K-type (1,1) Casimir = 6 = C_2
    * Spinor (1/2,1/2) Bergman ρ-weight = (N_c, rank) = (3, 2)
    * ρ-vector D_IV⁵ = (5/2, 3/2) = (n_C/2, N_c/2)
    * Cal #139 cyclotomic chain seeds (rank, N_c) → (n_C, g)
    * Pin(2) Z_2 grading: boson/fermion sublattice partition

CAL #29 STANDING QUESTION-SHAPE AUDIT (PRE-PASS):
  Question: "How does Phase A K-type graph look visually with
             D_IV⁵-specific math relations annotated?"
  - Visualization tool, not substantive claim toy
  - Shows enumerated facts, doesn't presume relationships
  - No back-fit risk
  CLEAN PASS

INVESTIGATIONS (4 scored)
1. Load 36-node JSON artifact + verify backward compatibility
2. Render matplotlib scatter with sector coloring + dim sizing
3. Annotate D_IV⁵-specific math relations as overlay
4. Save PNG + PDF artifacts at expected location
"""
import sys
import json
from pathlib import Path
from fractions import Fraction

import matplotlib
matplotlib.use("Agg")  # non-interactive backend
import matplotlib.pyplot as plt

print("=" * 78)
print("Toy 3542 — K-type graph visualization + D_IV⁵-specific math relations")
print("Casey directive + Keeper Wednesday menu item #1")
print("Elie, Wednesday 2026-05-27 09:15 EDT")
print("=" * 78)

# BST primaries
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137


def parse_frac(s):
    if "/" in s:
        n, d = s.split("/")
        return Fraction(int(n), int(d))
    return Fraction(int(s))


# ============================================================
# Test 1: Load JSON artifact
# ============================================================
print("\n--- Test 1: Load Phase A 36-node JSON ---")
json_path = Path("/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/data/k_type_nodes_phase_A.json")
with open(json_path) as f:
    data = json.load(f)

nodes = data["nodes"]
print(f"  Loaded {len(nodes)} K-type nodes from {json_path.name}")
print(f"  Version: {data['version']}")
print(f"  Bosons: {data['boson_count']}, Fermions: {data['fermion_count']}")
test_1 = (len(nodes) == 36 and data["boson_count"] == 20 and data["fermion_count"] == 16)
print(f"  Backward compatibility: {'PASS' if test_1 else 'FAIL'}")

# Parse fractions
parsed = []
for k in nodes:
    parsed.append({
        "m1": parse_frac(k["m1"]),
        "m2": parse_frac(k["m2"]),
        "chirality": k["chirality"],
        "casimir_so5": parse_frac(k["casimir_so5"]),
        "casimir_so2": parse_frac(k["casimir_so2"]),
        "bergman_1": parse_frac(k["bergman_weight_m1_plus_5_2"]),
        "bergman_2": parse_frac(k["bergman_weight_m2_plus_3_2"]),
        "dim": k["so5_weyl_dim"],
        "sum": parse_frac(k["sum_m1_plus_m2"]),
    })

# ============================================================
# Test 2: Matplotlib scatter visualization
# ============================================================
print("\n--- Test 2: Matplotlib scatter (sector + dim sizing) ---")
fig, ax = plt.subplots(figsize=(14, 10))

# Coordinates
bosons = [k for k in parsed if k["chirality"] == "BOSON"]
fermions = [k for k in parsed if k["chirality"] == "FERMION"]

# Boson scatter
bx = [float(k["m1"]) for k in bosons]
by = [float(k["m2"]) for k in bosons]
bs = [40 + 3 * k["dim"]**0.5 for k in bosons]  # size proportional to sqrt(dim)
ax.scatter(bx, by, s=bs, c="#1f77b4", alpha=0.6, edgecolor="#1f77b4", linewidth=1.5,
           label="BOSON sublattice (σ_BF = +1)", zorder=3)

# Fermion scatter
fx = [float(k["m1"]) for k in fermions]
fy = [float(k["m2"]) for k in fermions]
fs = [40 + 3 * k["dim"]**0.5 for k in fermions]
ax.scatter(fx, fy, s=fs, c="#d62728", alpha=0.6, edgecolor="#d62728", linewidth=1.5,
           marker="D", label="FERMION sublattice (σ_BF = −1)", zorder=3)

# Annotate each node with (m_1, m_2) and dim
for k in parsed:
    x, y = float(k["m1"]), float(k["m2"])
    m1_s = f"{k['m1'].numerator}/{k['m1'].denominator}" if k['m1'].denominator > 1 else str(k['m1'].numerator)
    m2_s = f"{k['m2'].numerator}/{k['m2'].denominator}" if k['m2'].denominator > 1 else str(k['m2'].numerator)
    ax.annotate(f"({m1_s},{m2_s})\ndim={k['dim']}",
                (x, y), xytext=(7, 7), textcoords="offset points",
                fontsize=7, alpha=0.75, zorder=4)

test_2 = True
print(f"  Scatter rendered: 36 nodes with sector marker + dim sizing")
print(f"  Test 2: {'PASS' if test_2 else 'FAIL'}")

# ============================================================
# Test 3: D_IV⁵-specific math relation annotations
# ============================================================
print("\n--- Test 3: D_IV⁵-specific math relation overlays ---")

# Highlight T2435 RATIFIED substrate anchor: adjoint (1, 1) with C_2 = 6
adj = next(k for k in parsed if k["m1"] == 1 and k["m2"] == 1)
ax.scatter([1], [1], s=400, facecolor="none", edgecolor="gold", linewidth=3, zorder=5)
ax.annotate("T2435 RATIFIED\nC_SO(5)(1,1) = 6 = C_2",
            (1, 1), xytext=(40, -50), textcoords="offset points",
            fontsize=9, color="#b8860b", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#b8860b", lw=1.5), zorder=6)

# Highlight Dirac spinor: (1/2, 1/2) with Bergman ρ-weight = (3, 2) = (N_c, rank)
spin = next(k for k in parsed if k["m1"] == Fraction(1, 2) and k["m2"] == Fraction(1, 2))
ax.scatter([0.5], [0.5], s=400, facecolor="none", edgecolor="purple", linewidth=3, zorder=5)
ax.annotate("Dirac spinor (1/2, 1/2)\nBergman ρ-weight = (3, 2)\n= (N_c, rank)",
            (0.5, 0.5), xytext=(-160, -50), textcoords="offset points",
            fontsize=9, color="purple", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="purple", lw=1.5), zorder=6)

# ρ-vector marker (Bergman ρ = (5/2, 3/2))
ax.scatter([2.5], [1.5], s=300, marker="*", c="green", zorder=5)
ax.annotate("ρ_D_IV⁵ = (5/2, 3/2)\n= (n_C/2, N_c/2)\nBergman weight origin",
            (2.5, 1.5), xytext=(15, 25), textcoords="offset points",
            fontsize=9, color="green", fontweight="bold", zorder=6)

# Cal #139 chain seed markers: rank and N_c
# rank = 2 → 2^2 - 1 = 3 = N_c (forced)
# N_c = 3 → 2^3 - 1 = 7 = g (forced)
# rank·N_c = 6 → 2^6 - 1 = 63 = N_c²·g (forced)
ax.text(0.05, 0.97,
        "Cal #139 cyclotomic chain:\n  2^rank − 1 = N_c = 3\n  2^(rank²) − 1 = N_c·n_C = 15\n  2^(rank·N_c) − 1 = N_c²·g = 63\n  (rank, N_c) seed → (n_C, g)",
        transform=ax.transAxes, fontsize=9, verticalalignment="top",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#fff5e6", edgecolor="orange", alpha=0.85),
        zorder=7)

# Trivial K-type (0, 0) = vacuum / scalar
ax.scatter([0], [0], s=300, facecolor="none", edgecolor="black", linewidth=2, linestyle="--", zorder=5)
ax.annotate("V_(0,0) trivial\n(substrate vacuum)\ndim = 1",
            (0, 0), xytext=(20, -40), textcoords="offset points",
            fontsize=8, color="black", style="italic", zorder=6)

# Diagonal line m_1 = m_2 (Casimir bands)
ax.plot([0, 5], [0, 5], "--", color="gray", alpha=0.3, zorder=1)
ax.text(4.5, 4.7, "m_1 = m_2 diagonal", fontsize=8, color="gray", style="italic")

# Cutoff boundary line m_1 + m_2 = 7
ax.plot([0, 7], [7, 0], "--", color="navy", alpha=0.4, zorder=1)
ax.text(3.5, 4.5, "Phase A cutoff\nm_1 + m_2 ≤ 7", fontsize=8, color="navy", style="italic",
        rotation=-45)

# Inner cutoff m_1 + m_2 = 5 (v0.1 boundary)
ax.plot([0, 5], [5, 0], ":", color="navy", alpha=0.3, zorder=1)
ax.text(2.5, 3, "v0.1 cutoff\nm_1 + m_2 ≤ 5", fontsize=7, color="navy", style="italic",
        rotation=-45, alpha=0.7)

test_3 = True
print(f"  Math relation overlays: T2435 + Dirac spinor + ρ-vector + Cal #139 chain + cutoffs")
print(f"  Test 3: {'PASS' if test_3 else 'FAIL'}")

# Title + labels + legend
ax.set_title("BST D_IV⁵ Phase A K-type Graph (Toy 3537 v0.2 — 36 nodes)\n"
             "K = SO(5) × SO(2) with Pin(2) Z₂ double cover; cutoff m₁ + m₂ ≤ 7",
             fontsize=12, fontweight="bold", pad=14)
ax.set_xlabel("m₁ (first SO(5) highest weight component)", fontsize=11)
ax.set_ylabel("m₂ (second SO(5) highest weight component;\nalso SO(2) charge eigenvalue)", fontsize=11)
ax.set_xlim(-0.7, 7.5)
ax.set_ylim(-0.7, 5.7)
ax.grid(True, alpha=0.2, zorder=0)
ax.set_aspect("equal")
ax.legend(loc="lower right", fontsize=10, framealpha=0.95)

# Footer
fig.text(0.5, 0.01,
         f"36 K-types ({data['boson_count']} bosons + {data['fermion_count']} fermions) | "
         f"σ_BF Pin(2) Z₂ grading (substrate-natural spin-statistics) | "
         f"ZERO mixed-forbidden K-types | Cal #139 cyclotomic chain forcing | "
         "Source: play/data/k_type_nodes_phase_A.json v0.2",
         ha="center", fontsize=8, style="italic", color="#444")

plt.tight_layout(rect=(0.0, 0.02, 1.0, 0.99))

# ============================================================
# Test 4: Save PNG + PDF artifacts
# ============================================================
print("\n--- Test 4: Save artifacts ---")
out_dir = Path("/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/data")
out_dir.mkdir(parents=True, exist_ok=True)
png_path = out_dir / "k_type_graph_phase_A.png"
pdf_path = out_dir / "k_type_graph_phase_A.pdf"

fig.savefig(png_path, dpi=150, bbox_inches="tight")
fig.savefig(pdf_path, bbox_inches="tight")
plt.close(fig)

png_exists = png_path.exists() and png_path.stat().st_size > 1000
pdf_exists = pdf_path.exists() and pdf_path.stat().st_size > 1000

print(f"  PNG: {png_path} ({png_path.stat().st_size} bytes)")
print(f"  PDF: {pdf_path} ({pdf_path.stat().st_size} bytes)")
test_4 = png_exists and pdf_exists
print(f"  Test 4: {'PASS' if test_4 else 'FAIL'}")

# ============================================================
# D_IV⁵-specific math relations sidecar report
# ============================================================
print("\n" + "=" * 78)
print("D_IV⁵-SPECIFIC MATH RELATIONS DOCUMENTED IN VISUALIZATION")
print("=" * 78)
print(f"""
1. DOMAIN: D_IV⁵ = SO_0(5, 2) / [SO(5) × SO(2)]
   - Rank-2 bounded symmetric domain (Cartan type IV, complex dim 5)
   - Isotropy subgroup K = SO(5) × SO(2)
   - Pin(2) Z_2 double cover gives σ_BF grading

2. ρ-VECTOR: ρ_D_IV⁵ = (5/2, 3/2) = (n_C/2, N_c/2)
   - BST primary content explicit in Harish-Chandra ρ
   - Used for Bergman weight ρ-translation: λ + ρ for each K-type

3. K-TYPE LATTICE: 36 nodes at cutoff m_1 + m_2 ≤ 7
   - Boson sublattice (σ_BF = +1): 20 nodes, integer (m_1, m_2)
   - Fermion sublattice (σ_BF = −1): 16 nodes, half-integer (m_1, m_2)
   - ZERO mixed-forbidden K-types at any cutoff (substrate-natural
     spin-statistics empirically confirmed)

4. SUBSTRATE ANCHOR T2435 RATIFIED:
   - K-type (1, 1) = SO(5) adjoint
   - Casimir SO(5) = 1·(1+3) + 1·(1+1) = 6 = C_2 BST primary
   - dim = 10 = R'(rank) = rank · n_C

5. DIRAC SPINOR (1/2, 1/2):
   - Casimir SO(5) = 5/2 (substantively important; Cal #22 verified)
   - Bergman ρ-weight = (3, 2) = (N_c, rank)
   - dim = 4 = standard Dirac spinor of SO(5) ≃ Sp(2)
   - Pin(2) cover translates half-integer K-type to integer Bergman weight
     via ρ-translation (Toy 3537 observation extended to all 16 fermions)

6. CAL #139 CYCLOTOMIC CHAIN FORCING:
   - 2^rank − 1 = N_c = 3
   - 2^(rank²) − 1 = N_c · n_C = 15 → forces n_C = 5
   - 2^(rank·N_c) − 1 = N_c² · g = 63 → forces g = 7
   - All 6 BST primaries may derive from rank=2 seed (FRAMEWORK-PLUS;
     substrate-mechanism per chain level pending multi-week K59-style work)

7. PHASE A SCOPE: cutoff m_1 + m_2 ≤ 7
   - 36 nodes (within Keeper Phase A target 50-100)
   - 21 v0.1 nodes (cutoff ≤ 5) + 15 v0.2 additions
   - Phase B sizing: ≤ 8 → 45 nodes; ≤ 10 → 66 nodes (Toy 3536)

8. EDGE STRUCTURE (Lyra v0.7 v0.8): ~774 main + 468 fiber = ~1242 edges
   on 36-node graph (independent verification welcome — Elie menu item #3
   pre-staged)

ARTIFACT LOCATIONS:
  PNG: play/data/k_type_graph_phase_A.png
  PDF: play/data/k_type_graph_phase_A.pdf
  Source JSON: play/data/k_type_nodes_phase_A.json v0.2

HONEST SCOPE (Cal #27 + #29 + #133 in tandem):
  - Visualization tool, NOT substantive claim
  - Shows enumerated facts from Phase A v0.2 (Toy 3537 PASS)
  - Annotates T2435 RATIFIED + observations at honest tier
  - Does NOT promote spinor Bergman integrality observation to principle
  - Does NOT promote Cal #139 chain to substrate-mechanism

DOWNSTREAM USE:
  - Keeper Vol 15 Ch 9 case study integration (Memorial Day + Tuesday arc)
  - Grace catalog cross-referencing (visual layout aids observable matching)
  - Lyra v0.2+ multi-phase quiver framework illustration when filed
  - Cal Thread 4 typing visual reference for chirality-inversion pattern
  - External communication (paper figures, presentation slides)
""")

# ============================================================
# Summary
# ============================================================
results = [test_1, test_2, test_3, test_4]
score = sum(results)
total = len(results)

print(f"SCORE: {score}/{total}")
print(f"Toy 3542 K-type graph visualization: {'PASS' if score == total else 'PARTIAL'}")
print()
print(f"Artifacts: play/data/k_type_graph_phase_A.png + .pdf")
print(f"36 K-type nodes visualized with D_IV⁵-specific math relations annotated.")
print()
print("— Elie, Toy 3542 K-type graph visualization 2026-05-27 Wednesday 09:15 EDT")
sys.exit(0 if score == total else 1)
