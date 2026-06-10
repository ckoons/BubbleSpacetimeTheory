"""
K-Type Address Lattice Visualization v0.1
==========================================
Keeper, Tuesday 2026-06-09 afternoon

Comprehensive chart of the rank-2 Cartan slice of D_IV^5: every K-type lattice address
(a, b) marked with what it handles/anchors per K_Type_Address_Registry_v0_1.

Shows in one figure:
  - K-type lattice points (a, b) with Casimir C(a,b) + cell-count (where assigned)
  - Substrate-reach color coding (vacuum / floor / boundary / drowned / excited)
  - Hadron content at each floor + elevation address
  - Excited tower at higher K-types
  - Confined quarks (Filter 1) as smeared cloud (no clean address)
  - Goldstone pion (Filter 3) as separate marker
  - Lepton inverted-pyramid hypothesis as separate cluster
  - Schur generators (225 + 79) cross-referenced
  - Casey #9 reach-bound (156.4 MeV cell scale boundary)
  - Open lanes (gauge bosons + Higgs K-type placements)
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

# --- K-type lattice ---
def casimir(a, b):
    return a*a + b*b + 3*a + b

lattice = [(a, b) for a in range(5) for b in range(a + 1)]

# Cell-counts per F52/T2488 (substrate-measured at specific K-types)
cells = {
    (0, 0): 0,    # vacuum
    (1, 0): 5,    # MESON FLOOR = n_C
    (1, 1): 6,    # BARYON FLOOR = C_2
    (2, 0): 10,
    (2, 1): 12,
    (2, 2): 16,
    (3, 0): 18,
    (3, 1): 20,
    (3, 2): 24,
    (3, 3): 30,
    (4, 0): 28,
}

# What each K-type address handles/anchors
anchors = {
    (0, 0): "VACUUM\n+ K(0,0) = 1920/π⁵\nsubstrate self-ref",
    (1, 0): "MESON FLOOR\n5 cells = n_C\n[ρ, ω floor + K, φ\nboundary + J/ψ, Υ\ndrowned]",
    (1, 1): "BARYON FLOOR\n6 cells = C_2\n[p, n floor + Λ, Σ,\nΞ, Ω boundary +\nΛ_c, Λ_b drowned]\n+ C_2 = 6 triple",
    (2, 0): "Excited mesons\nρ(1450), ρ(1700)",
    (2, 1): "Δ baryons\nΔ(1232) spin-3/2",
    (2, 2): "Tensor mesons\nf_2(1270), a_2(1320)",
    (3, 0): "Higher excited\nmesons",
    (3, 1): "Higher excited\nbaryons",
    (3, 2): "Higher tensor",
    (3, 3): "Higher spin",
    (4, 0): "Higher",
}

# Substrate-reach status (drives color)
reach = {
    (0, 0): "vacuum",
    (1, 0): "floor",
    (1, 1): "floor",
    (2, 0): "excited",
    (2, 1): "excited",
    (2, 2): "excited",
    (3, 0): "excited",
    (3, 1): "excited",
    (3, 2): "excited",
    (3, 3): "excited",
    (4, 0): "excited",
}

REACH_COLORS = {
    "vacuum":   "#5050d0",
    "floor":    "#2a9d3a",
    "boundary": "#e8b020",
    "drowned":  "#d04040",
    "excited":  "#888888",
}

# ============================================================
# Figure setup
# ============================================================
fig = plt.figure(figsize=(22, 13))
ax_main = plt.subplot2grid((2, 3), (0, 0), colspan=2, rowspan=2)
ax_lep  = plt.subplot2grid((2, 3), (0, 2))
ax_open = plt.subplot2grid((2, 3), (1, 2))

# ============================================================
# Main panel: K-type lattice with everything anchored
# ============================================================
ax_main.set_facecolor("#fafafa")

# Lattice points
for (a, b) in lattice:
    col = REACH_COLORS[reach.get((a, b), "excited")]
    size = 1600 if (a, b) in [(1, 0), (1, 1)] else (1100 if (a, b) == (0, 0) else 900)
    ax_main.scatter(a, b, s=size, c=col, edgecolors="black",
                    linewidths=2, alpha=0.85, zorder=3)
    # Casimir label inside
    C = casimir(a, b)
    if (a, b) in cells:
        inner = f"C={C}\n{cells[(a,b)]} cells"
    else:
        inner = f"C={C}"
    ax_main.annotate(inner, (a, b), ha="center", va="center",
                     fontsize=8.5, weight="bold", color="white", zorder=4)
    # Anchored physics label below
    label = anchors.get((a, b), "")
    if label:
        offset_y = -0.32 if (a, b) in [(1, 0), (1, 1)] else -0.27
        # Adjust label position depending on location
        if (a, b) == (0, 0):
            xtxt, ytxt, ha = a, b + 0.5, "center"
        elif (a, b) in [(1, 0)]:
            xtxt, ytxt, ha = a - 0.05, b - 0.55, "center"
        elif (a, b) == (1, 1):
            xtxt, ytxt, ha = a, b + 0.55, "center"
        else:
            xtxt, ytxt, ha = a + 0.05, b + 0.30, "left"
        ax_main.annotate(label, (xtxt, ytxt), ha=ha, va="center",
                         fontsize=7.5, zorder=4,
                         bbox=dict(boxstyle="round,pad=0.25",
                                   facecolor="white", edgecolor="gray",
                                   alpha=0.92))

# Floor highlight (red circles around (1,0) and (1,1))
for fp in [(1, 0), (1, 1)]:
    ax_main.add_patch(Circle(fp, 0.20, facecolor="none",
                              edgecolor="red", linewidth=3, zorder=2))

# === Confined quarks (Filter 1) — smeared cloud below floor ===
quark_blur_x = np.random.normal(0.5, 0.4, 60)
quark_blur_y = np.random.normal(-0.6, 0.3, 60)
ax_main.scatter(quark_blur_x, quark_blur_y, s=18, c="#aa55aa",
                alpha=0.35, zorder=1)
ax_main.text(0.5, -1.1, "Confined quarks (Filter 1)\nscale-dependent superposition\n0.014 → 2.15 cells (155×)\nNO clean K-type address",
             ha="center", fontsize=8, style="italic",
             bbox=dict(boxstyle="round,pad=0.4",
                       facecolor="#f0e0f0", edgecolor="#aa55aa"))

# === Goldstone pion (Filter 3) — separate marker ===
ax_main.scatter([0.88], [-0.15], s=180, marker="D", c="#cc8800",
                edgecolors="black", linewidths=1.5, zorder=3)
ax_main.annotate("π (Goldstone)\nn = 0.88 cells\nFilter 3\nchiral remnant\nNOT eigenstate",
                  (0.88, -0.15), xytext=(15, 5), textcoords="offset points",
                  fontsize=7.5,
                  bbox=dict(boxstyle="round,pad=0.25",
                            facecolor="#fff4e0", edgecolor="#cc8800"))

# === Schur generator: 225 across 4 lanes ===
ax_main.text(2.5, 4.0, "225 = (N_c·n_C)² Schur generator (4 lanes)",
             fontsize=10, weight="bold", color="#c00000",
             bbox=dict(boxstyle="round,pad=0.3",
                       facecolor="#fff0f0", edgecolor="#c00000"))
ax_main.text(2.5, 3.6,
             "• c_FK = 225/π^(9/2) [T2442]\n"
             "• a_0 Bergman trace = 225 [K266]\n"
             "• dim SO(4,2)² = 225 [F66/K258]\n"
             "• Higgs VEV / (g·cell) = 225 [K283 v0.2]",
             fontsize=8, color="#c00000")
ax_main.annotate("", xy=(0.05, 0.05), xytext=(2.45, 3.5),
                 arrowprops=dict(arrowstyle="->", color="#c00000",
                                 lw=1.2, alpha=0.6, connectionstyle="arc3,rad=-0.2"))

# === Schur generator: 79 mixing-sector candidate ===
ax_main.text(2.5, 2.5, "79 = rank⁴·n_C − 1 Schur candidate",
             fontsize=10, weight="bold", color="#0050a0",
             bbox=dict(boxstyle="round,pad=0.3",
                       facecolor="#f0f0ff", edgecolor="#0050a0"))
ax_main.text(2.5, 2.1,
             "Mixing sector — Lyra F81 multi-week:\n"
             "• Cabibbo θ_C ~ 2/√79\n"
             "• V_cb ~ C₂²/(11·79); 11 = rank·C_2 − 1\n"
             "• Other 6 angles: K-type forcing OPEN",
             fontsize=8, color="#0050a0")

# === Casey #9 reach-bound at floor ===
ax_main.text(0.5, 1.85, "Casey #9 reach-bound:\nfloor at 156.4 MeV cell scale\n(K272 Filter 1 derived;\nK280 boundary scale precise)",
             ha="center", fontsize=8.5, weight="bold", color="#006000",
             bbox=dict(boxstyle="round,pad=0.3",
                       facecolor="#f0fff0", edgecolor="#006000"))

# Axes / limits
ax_main.set_xlabel("a  (SO(5) first highest-weight)", fontsize=13)
ax_main.set_ylabel("b  (SO(5) second highest-weight)", fontsize=13)
ax_main.set_xlim(-1.0, 5.2)
ax_main.set_ylim(-1.7, 4.7)
ax_main.set_aspect("equal")
ax_main.grid(True, alpha=0.25)
ax_main.set_title("D_IV^5 K-Type Address Lattice — what each (a, b) anchors\n"
                  "rank=2 Cartan slice (faithful 2D); Casimir C(a,b) inside circle; cells below where assigned",
                  fontsize=13)

# Legend for reach status
legend_handles = [
    plt.scatter([], [], s=200, c=REACH_COLORS["vacuum"], edgecolors="black", label="Substrate vacuum"),
    plt.scatter([], [], s=200, c=REACH_COLORS["floor"],  edgecolors="black", label="FLOOR (substrate measures cleanly)"),
    plt.scatter([], [], s=200, c=REACH_COLORS["boundary"], edgecolors="black", label="BOUNDARY (Yukawa ~ cell)"),
    plt.scatter([], [], s=200, c=REACH_COLORS["drowned"], edgecolors="black", label="DROWNED (Yukawa dominates)"),
    plt.scatter([], [], s=200, c=REACH_COLORS["excited"], edgecolors="black", label="Excited tower (above floor)"),
]
ax_main.legend(handles=legend_handles, loc="upper right", fontsize=8.5, framealpha=0.95)

# ============================================================
# Right-top panel: Lepton inverted-pyramid hypothesis
# ============================================================
ax_lep.set_facecolor("#fafafa")
ax_lep.set_title("Lepton K-type substructure\n(Casey inverted-pyramid hypothesis, K281)",
                 fontsize=10)

# Pyramid: apex at bottom, widens upward
# Each lepton has a supporting K-type SET (not single address)

# Apex (electron — substrate anchor)
ax_lep.scatter([0], [0], s=400, c="#2a9d3a", edgecolors="black",
               linewidths=2, zorder=5)
ax_lep.annotate("e  (apex)\nm_e = 1\nsubstrate anchor\n0.003 cells", (0, 0),
                xytext=(20, -10), textcoords="offset points", fontsize=8)

# Muon — boundary scale (~0.68 cell = strange scale)
ax_lep.scatter([-0.4, 0.4], [1, 1], s=200, c="#e8b020",
               edgecolors="black", linewidths=1.5, zorder=5)
ax_lep.plot([-0.4, 0.4], [1, 1], "k--", alpha=0.3)
ax_lep.plot([0, -0.4], [0, 1], "k--", alpha=0.3)
ax_lep.plot([0, 0.4], [0, 1], "k--", alpha=0.3)
ax_lep.text(0, 1.25, "μ  (boundary)\n0.68 cell = strange scale\nm_μ/m_e = (24/π²)^6  [T190]",
            ha="center", fontsize=8,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#fff8e0",
                      edgecolor="#cc8800"))

# Tau — drowned (~11 cells = charm/bottom scale)
ax_lep.scatter([-0.8, 0, 0.8], [2.2, 2.2, 2.2], s=200, c="#d04040",
               edgecolors="black", linewidths=1.5, zorder=5)
ax_lep.plot([-0.8, 0.8], [2.2, 2.2], "k--", alpha=0.3)
ax_lep.plot([-0.4, -0.8], [1, 2.2], "k--", alpha=0.3)
ax_lep.plot([-0.4, 0], [1, 2.2], "k--", alpha=0.3)
ax_lep.plot([0.4, 0], [1, 2.2], "k--", alpha=0.3)
ax_lep.plot([0.4, 0.8], [1, 2.2], "k--", alpha=0.3)
ax_lep.text(0, 2.55, "τ  (drowned)\n11 cells = charm/bottom scale\nm_τ/m_e = 49·71  [T2003]",
            ha="center", fontsize=8,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#ffe8e8",
                      edgecolor="#a00000"))

# Neutrinos — below apex
ax_lep.scatter([-0.3, 0, 0.3], [-1.0, -1.0, -1.0], s=80, c="#5050d0",
               marker="v", edgecolors="black", linewidths=1, zorder=5)
ax_lep.text(0, -1.4, "ν_e, ν_μ, ν_τ\nsub-eV to MeV\nBELOW substrate apex",
            ha="center", fontsize=7.5, color="#3030a0")

ax_lep.set_xlim(-2.0, 2.0)
ax_lep.set_ylim(-1.8, 3.2)
ax_lep.set_xticks([])
ax_lep.set_yticks([])
ax_lep.text(-1.9, 3.0, "Each lepton supported by a SET\nof K-types (Casey hypothesis);\nLyra K-type spectral lane\nderivation OPEN (multi-week)",
            fontsize=7.5, style="italic", color="#404040")

# ============================================================
# Right-bottom panel: Open K-type placements (gauge bosons + Higgs)
# ============================================================
ax_open.set_facecolor("#fafafa")
ax_open.set_title("Open K-type placements\n(gauge bosons + Higgs — F66 extension multi-week)",
                  fontsize=10)

open_particles = [
    ("γ (photon)", 0,        "EM conformal boundary\nSO(4,2); F66"),
    ("gluons",     0,        "SU(N_c=3) color\nsymmetry"),
    ("W±",         80.4e3,   "EW symmetry breaking\n514 cells (drowned)"),
    ("Z⁰",         91.2e3,   "EW symmetry breaking\n583 cells (drowned)"),
    ("Higgs H",    125e3,    "Higgs field excitation\n800 cells (drowned)\nVol 2 Ch 9 D-tier exists"),
]

for i, (name, mass_MeV, desc) in enumerate(open_particles):
    y = 4 - i
    color = "#888888" if mass_MeV == 0 else "#d04040"
    ax_open.scatter([0.5], [y], s=200, c=color, edgecolors="black",
                    linewidths=1.5, zorder=3)
    mass_label = "massless" if mass_MeV == 0 else f"{mass_MeV/1000:.1f} GeV"
    ax_open.annotate(f"{name}  ({mass_label})\n{desc}", (0.5, y),
                     xytext=(15, 0), textcoords="offset points", fontsize=8,
                     va="center",
                     bbox=dict(boxstyle="round,pad=0.2",
                               facecolor="white", edgecolor="gray"))

ax_open.set_xlim(0, 4)
ax_open.set_ylim(-1.5, 4.8)
ax_open.set_xticks([])
ax_open.set_yticks([])
ax_open.text(0, -1.2, "K-type addresses on D_IV^5 lattice OPEN;\n"
                       "Lyra F66 extension to electroweak\nsector is the investigation lane",
             fontsize=8, style="italic", color="#404040")

# ============================================================
# Suptitle
# ============================================================
plt.suptitle("BST K-Type Address Lattice — every (a, b) on D_IV⁵ marked with what it handles/anchors\n"
             "Tue 2026-06-09 — Keeper v0.1 visualization complementing K-Type Address Registry",
             fontsize=14, y=1.00)

plt.tight_layout()
out = "/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/Keeper_K_type_address_lattice_v0_1.png"
plt.savefig(out, dpi=150, bbox_inches="tight")
print(f"Saved: {out}")
