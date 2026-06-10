"""
K-Type Address Lattice Visualization v0.2
==========================================
Keeper, Tuesday 2026-06-09 late-afternoon

v0.2 updates from v0.1:
  - Lepton inverted-pyramid: explicit F86 support-flag spine (3 tiers = rank-2 forces 3 generations)
  - Bergman kernel one-object unification annotation (mixing + VEV + lepton pyramid = ONE kernel)
  - Genus/2 = 5/2 -> sqrt prediction annotation (Cabibbo 2/sqrt(79))
  - Casey #9 at parameter level annotation (one boundary, two scales)
  - Three-levers-as-ONE-reduction-candidate visualization
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np

# --- K-type lattice ---
def casimir(a, b):
    return a*a + b*b + 3*a + b

lattice = [(a, b) for a in range(5) for b in range(a + 1)]

cells = {
    (0, 0): 0, (1, 0): 5, (1, 1): 6, (2, 0): 10, (2, 1): 12,
    (2, 2): 16, (3, 0): 18, (3, 1): 20, (3, 2): 24, (3, 3): 30, (4, 0): 28,
}

anchors = {
    (0, 0): "VACUUM\n+ K(0,0) = 1920/π⁵",
    (1, 0): "MESON FLOOR\n5 cells = n_C",
    (1, 1): "BARYON FLOOR\n6 cells = C_2",
    (2, 0): "ρ(1450)\nexcited mesons",
    (2, 1): "Δ(1232)\nbaryons",
    (2, 2): "f_2(1270)\ntensor mesons",
    (3, 0): "Higher mesons",
    (3, 1): "Higher baryons",
    (3, 2): "Higher tensors",
    (3, 3): "Higher spin",
    (4, 0): "Higher",
}

reach = {
    (0, 0): "vacuum",  (1, 0): "floor",  (1, 1): "floor",
    (2, 0): "excited", (2, 1): "excited", (2, 2): "excited",
    (3, 0): "excited", (3, 1): "excited", (3, 2): "excited", (3, 3): "excited",
}

REACH_COLORS = {
    "vacuum":   "#5050d0",
    "floor":    "#2a9d3a",
    "boundary": "#e8b020",
    "drowned":  "#d04040",
    "excited":  "#888888",
}

# ============================================================
# Figure setup — three panels (main lattice + support-flag + one-object unification)
# ============================================================
fig = plt.figure(figsize=(24, 14))
ax_main = plt.subplot2grid((2, 3), (0, 0), colspan=2, rowspan=2)
ax_flag = plt.subplot2grid((2, 3), (0, 2))
ax_unif = plt.subplot2grid((2, 3), (1, 2))

# ============================================================
# Main panel: K-type lattice with Bergman kernel unification overlay
# ============================================================
ax_main.set_facecolor("#fafafa")

# Lattice points
for (a, b) in lattice:
    col = REACH_COLORS[reach.get((a, b), "excited")]
    size = 1600 if (a, b) in [(1, 0), (1, 1)] else (1100 if (a, b) == (0, 0) else 850)
    ax_main.scatter(a, b, s=size, c=col, edgecolors="black",
                    linewidths=2, alpha=0.85, zorder=3)
    C = casimir(a, b)
    if (a, b) in cells:
        inner = f"C={C}\n{cells[(a,b)]} cells"
    else:
        inner = f"C={C}"
    ax_main.annotate(inner, (a, b), ha="center", va="center",
                     fontsize=8.5, weight="bold", color="white", zorder=4)
    label = anchors.get((a, b), "")
    if label:
        if (a, b) == (0, 0):
            xtxt, ytxt, ha = a, b + 0.45, "center"
        elif (a, b) == (1, 0):
            xtxt, ytxt, ha = a - 0.05, b - 0.55, "center"
        elif (a, b) == (1, 1):
            xtxt, ytxt, ha = a, b + 0.55, "center"
        else:
            xtxt, ytxt, ha = a + 0.05, b + 0.28, "left"
        ax_main.annotate(label, (xtxt, ytxt), ha=ha, va="center",
                         fontsize=7.5, zorder=4,
                         bbox=dict(boxstyle="round,pad=0.2",
                                   facecolor="white", edgecolor="gray",
                                   alpha=0.92))

# Floor highlights
for fp in [(1, 0), (1, 1)]:
    ax_main.add_patch(Circle(fp, 0.20, facecolor="none",
                              edgecolor="red", linewidth=3, zorder=2))

# Confined quarks (Filter 1) blur
quark_blur_x = np.random.normal(0.5, 0.4, 60)
quark_blur_y = np.random.normal(-0.6, 0.3, 60)
ax_main.scatter(quark_blur_x, quark_blur_y, s=18, c="#aa55aa", alpha=0.35, zorder=1)
ax_main.text(0.5, -1.1,
             "Confined quarks (Filter 1)\nF77 DERIVED Monday",
             ha="center", fontsize=8, style="italic",
             bbox=dict(boxstyle="round,pad=0.3",
                       facecolor="#f0e0f0", edgecolor="#aa55aa"))

# Goldstone pion
ax_main.scatter([0.88], [-0.15], s=180, marker="D", c="#cc8800",
                edgecolors="black", linewidths=1.5, zorder=3)
ax_main.annotate("π (Goldstone)\nFilter 3", (0.88, -0.15),
                 xytext=(15, 5), textcoords="offset points", fontsize=7.5,
                 bbox=dict(boxstyle="round,pad=0.25",
                           facecolor="#fff4e0", edgecolor="#cc8800"))

# === HEADLINE: Bergman kernel unification (NEW v0.2) ===
ax_main.text(2.8, 4.0,
             "★ HEADLINE: Three reduction-levers = ONE Bergman kernel of D_IV⁵\n"
             "   (Lyra F84 + Elie 4073 + Grace gate verdict — Tuesday)",
             fontsize=10.5, weight="bold", color="#a00080",
             bbox=dict(boxstyle="round,pad=0.4",
                       facecolor="#ffe8ff", edgecolor="#a00080", linewidth=1.5))

# === Three kernel evaluations cross-linked ===
ax_main.text(2.8, 3.45,
             "Kernel evaluated three ways:\n"
             "1. K(p,p) coincidence → 225 = (dim SO(4,2))² [VEV; F85]\n"
             "2. K(p,q)/√(…) displacement → mixing angles [F84; 4071]\n"
             "3. Vertical kernel through support-flag → leptons [F86]\n\n"
             "Genus/2 = n_C/2 = 5/2 (half-integer) → √ in Cabibbo\n"
             "λ = 2/√79 = 0.22502 vs obs 0.2248 — predicted not fitted",
             fontsize=8, color="#404040",
             bbox=dict(boxstyle="round,pad=0.3",
                       facecolor="white", edgecolor="#a00080"))

# === Casey #9 at parameter level (Grace deepest finding) ===
ax_main.text(2.8, 1.7,
             "★ DEEPEST: Casey #9 at parameter level\n"
             "(Grace K287 standing finding)\n\n"
             "Ledger structure IS reach-bound:\n"
             "  DERIVED = scale-independent (α, θ_QCD)\n"
             "  HONEST-NEG = running (α_s, sin²θ_W, q masses)\n"
             "  REDUCTION-CANDIDATES = scale-clean middle\n\n"
             "Conformal boundary = parameter-space\n"
             "hadron floor. One boundary, two scales.",
             fontsize=8, weight="bold", color="#006000",
             bbox=dict(boxstyle="round,pad=0.4",
                       facecolor="#f0fff0", edgecolor="#006000", linewidth=1.5))

# Axes
ax_main.set_xlabel("a  (SO(5) first highest-weight)", fontsize=13)
ax_main.set_ylabel("b  (SO(5) second highest-weight)", fontsize=13)
ax_main.set_xlim(-1.0, 5.5)
ax_main.set_ylim(-1.7, 4.7)
ax_main.set_aspect("equal")
ax_main.grid(True, alpha=0.25)
ax_main.set_title("D_IV^5 K-Type Address Lattice v0.2 — Bergman kernel unification headline\n"
                  "rank=2 Cartan slice (faithful 2D); Casimir + cells inside; v0.2 absorbs F84/F85/F86 + Casey #9 at parameter level",
                  fontsize=12)

# Legend
legend_handles = [
    plt.scatter([], [], s=200, c=REACH_COLORS["vacuum"], edgecolors="black", label="Substrate vacuum"),
    plt.scatter([], [], s=200, c=REACH_COLORS["floor"],  edgecolors="black", label="FLOOR (substrate measures)"),
    plt.scatter([], [], s=200, c=REACH_COLORS["excited"], edgecolors="black", label="Excited tower"),
]
ax_main.legend(handles=legend_handles, loc="upper left", fontsize=8.5, framealpha=0.95)

# ============================================================
# Right-top panel: F86 support-flag (NEW v0.2 — explicit substrate-architectural answer)
# ============================================================
ax_flag.set_facecolor("#fafafa")
ax_flag.set_title("F86 SUPPORT-FLAG — rank-2 D_IV⁵ has\nexactly 3 support-dims → 3 generations forced",
                  fontsize=10.5, weight="bold")

# Three tiers as horizontal bars with dimension labels
# Apex (electron) = full bulk, dim n_C = 5
ax_flag.barh([0], [5], color="#2a9d3a", edgecolor="black", linewidth=1.5,
             alpha=0.85, height=0.8)
ax_flag.text(2.5, 0, "TIER 1 (apex) — ELECTRON\n"
                     "Full bulk D_IV⁵\n"
                     "dim n_C = 5 — π⁵ VOLUME class\n"
                     "m_e = substrate anchor",
              ha="center", va="center", fontsize=8.5, weight="bold", color="white")

# Middle (muon) = Cartan slice, dim rank = 2
ax_flag.barh([1.5], [2], left=[1.5], color="#e8b020", edgecolor="black",
             linewidth=1.5, alpha=0.85, height=0.8)
ax_flag.text(2.5, 1.5, "TIER 2 (middle) — MUON\n"
                       "Cartan slice (maximal flat torus)\n"
                       "dim rank = 2 — π² SPECTRAL class\n"
                       "m_μ/m_e = (24/π²)^6 [T190]",
              ha="center", va="center", fontsize=8.5, weight="bold", color="white")

# Top (tau) = point, dim 0
ax_flag.barh([3], [0.3], left=[2.35], color="#d04040", edgecolor="black",
             linewidth=1.5, alpha=0.85, height=0.8)
ax_flag.text(2.5, 3, "TIER 3 (top) — TAU\n"
                     "Point (counting)\n"
                     "dim 0 — π⁰ COMBINATORIAL class\n"
                     "m_τ/m_e = 49·71 [T2003]",
              ha="center", va="center", fontsize=8.5, weight="bold", color="white")

# Drop annotations
ax_flag.annotate("Drop = N_c = 3", xy=(0, 0.4), xytext=(0, 1.1),
                 fontsize=9, ha="center", color="#404040",
                 arrowprops=dict(arrowstyle="<->", color="#404040", lw=1.2))
ax_flag.annotate("Drop = rank = 2", xy=(1.5, 1.9), xytext=(1.5, 2.6),
                 fontsize=9, ha="center", color="#404040",
                 arrowprops=dict(arrowstyle="<->", color="#404040", lw=1.2))

ax_flag.set_xlabel("Support dimension on D_IV⁵", fontsize=11)
ax_flag.set_xlim(-0.5, 5.5)
ax_flag.set_ylim(-0.7, 3.9)
ax_flag.set_yticks([])
ax_flag.grid(True, alpha=0.25, axis="x")

# Footnote
ax_flag.text(2.5, -0.5,
             "π-ladder spine {5, 2, 0} = {n_C, rank, 0}\n"
             "Dimension drops {N_c, rank}\n"
             "rank-2 → exactly 3 tiers → exactly 3 generations",
             ha="center", fontsize=8, style="italic",
             bbox=dict(boxstyle="round,pad=0.3",
                       facecolor="#fff8e0", edgecolor="#cc8800"))

# ============================================================
# Right-bottom panel: One-object unification diagram (NEW v0.2)
# ============================================================
ax_unif.set_facecolor("#fafafa")
ax_unif.set_title("Three reduction-levers = ONE Bergman kernel object\n"
                  "→ ONE Hua/Bergman computation forces 2 → ~13",
                  fontsize=10.5, weight="bold")

# Central node: Bergman kernel of D_IV^5
ax_unif.scatter([0.5], [0.5], s=4000, c="#a00080", edgecolors="black",
                linewidths=2, alpha=0.85, zorder=3)
ax_unif.annotate("ONE Bergman\nkernel of D_IV⁵\n(K264 D-tier;\nHua + 2-adic)",
                 (0.5, 0.5), ha="center", va="center", fontsize=9,
                 weight="bold", color="white", zorder=4)

# Three radial nodes for each evaluation
positions = [(0.1, 0.9), (0.9, 0.9), (0.5, 0.05)]
labels = [
    ("VEV (coincidence)\nK(p,p) = 225 = a_0\n= (dim SO(4,2))²\n[F85 + K283 v0.2]",
     "#d04040"),
    ("Mixing 8 angles\n(displacement)\nK(p,q)/√(...)\ngenus/2 → √\n[F84 + 4071/4073]",
     "#0050a0"),
    ("Lepton masses\n(vertical flag)\nover {5,2,0} tiers\n[F86 + 4072]",
     "#206020"),
]

for pos, (lbl, col) in zip(positions, labels):
    ax_unif.scatter([pos[0]], [pos[1]], s=1800, c=col, edgecolors="black",
                    linewidths=1.5, alpha=0.8, zorder=3)
    ax_unif.annotate(lbl, pos, ha="center", va="center", fontsize=7.5,
                     color="white", weight="bold", zorder=4)
    # Arrow from center to each
    ax_unif.add_patch(FancyArrowPatch((0.5, 0.5), pos, arrowstyle="-",
                                       color=col, lw=2, alpha=0.5,
                                       zorder=2))

# Reduction potential
ax_unif.text(0.5, -0.18,
             "If Lyra's Hua computation forces all three:\n"
             "Count moves 2 → ~13 (largest reduction in program history)\n"
             "All from ONE machinery already built for K(0,0)",
             ha="center", fontsize=8.5, weight="bold", color="#a00080",
             bbox=dict(boxstyle="round,pad=0.4",
                       facecolor="#ffe8ff", edgecolor="#a00080"))

ax_unif.set_xlim(-0.1, 1.1)
ax_unif.set_ylim(-0.35, 1.1)
ax_unif.set_xticks([])
ax_unif.set_yticks([])

# ============================================================
# Suptitle
# ============================================================
plt.suptitle("BST K-Type Address Lattice v0.2 — Tuesday 2026-06-09 substrate-architectural unification headline\n"
             "Three reduction-levers = ONE Bergman kernel of D_IV⁵ + F86 support-flag forces 3 generations + Casey #9 at parameter level",
             fontsize=14, y=1.00)

plt.tight_layout()
out = "/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/Keeper_K_type_address_lattice_v0_2.png"
plt.savefig(out, dpi=150, bbox_inches="tight")
print(f"Saved: {out}")
