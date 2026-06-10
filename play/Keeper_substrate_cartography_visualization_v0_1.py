"""
Substrate Cartography Visualization v0.1
========================================
Keeper, Monday 2026-06-08 post-EOD

Faithful 2D visualization of D_IV^5's K-type lattice + hadron anchoring + substrate cells.

Why 2D is honest: D_IV^5 has rank 2. The Cartan subspace IS 2-dimensional.
K-types are indexed by SO(5) highest weights (a, b) with a >= b >= 0 — a faithful
discrete lattice covering the manifold's algebraic structure.

What this shows:
  Panel 1: K-type lattice with Casimir eigenvalues + cell-count substrate measure
  Panel 2: Hadron anchoring — floor states (light u/d) + elevations (heavier flavor at same K-type)

What this does NOT show:
  - The full 10-real-dimensional bulk (would need projection)
  - Confined quarks as superpositions (they SPREAD across (a,b) — the 155x volume slide)
  - SO(2) charge structure (would add a third axis)

Per Elie Toy 4053: substrate measures VOLUME (cells per F52), not Casimir.
Cells and Casimir agree at (1,1) baryon = 6 by accident; disagree at (1,0) meson (cells 5 vs C=4).
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ============================================================
# K-type lattice for SO(5): (a, b) integer-valued, a >= b >= 0
# ============================================================

def casimir(a, b):
    """SO(5) quadratic Casimir at highest weight (a, b)."""
    return a*a + b*b + 3*a + b

lattice = [(a, b) for a in range(5) for b in range(a + 1)]

# Cell-count substrate measure per F52 / T2488
# (the substrate MEASURES this; not Casimir — per Elie Toy 4053 cells-vs-Casimir resolution)
cells = {
    (0, 0): 0,
    (1, 0): 5,   # n_C (meson floor)
    (1, 1): 6,   # C_2 (baryon floor)
    (2, 0): 10,
    (2, 1): 12,
    (2, 2): 16,
    (3, 0): 18,
    (3, 1): 20,
    (3, 2): 24,
    (3, 3): 30,
    (4, 0): 28,
}

# Hadron anchoring at K-types:
# same K-type address, different flavor content = "elevation" above floor
hadron_anchors = {
    (1, 0): [  # meson K-type (5 cells = n_C)
        ("rho",   770,  "u/d light",         "floor"),
        ("omega", 782,  "u/d light",         "floor"),
        ("K*",    892,  "strange (us, ds)",  "elevation"),
        ("phi",  1020,  "ss-bar",            "elevation"),
        ("J/psi",3097,  "cc-bar (charm)",    "elevation"),
        ("Upsilon", 9460, "bb-bar (bottom)", "elevation"),
    ],
    (1, 1): [  # baryon K-type (6 cells = C_2)
        ("p, n",   938,  "u/d light",          "floor"),
        ("Lambda",1116, "1x strange",         "elevation"),
        ("Sigma", 1189, "1x strange",         "elevation"),
        ("Xi",    1318, "2x strange",         "elevation"),
        ("Omega-",1672, "3x strange",         "elevation"),
        ("Lambda_c", 2286, "charm",           "elevation"),
        ("Lambda_b", 5620, "bottom",          "elevation"),
    ],
}

# ============================================================
# Plot
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9))

# ---------- Panel 1: K-type lattice ----------
ax1.set_facecolor("#fafafa")

xs, ys, cs = zip(*[(a, b, casimir(a, b)) for (a, b) in lattice])
sc = ax1.scatter(xs, ys, c=cs, s=900, cmap="viridis",
                 edgecolors="black", linewidths=1.5, alpha=0.95,
                 vmin=0, vmax=max(cs))

# Annotate each K-type with Casimir + cells (where assigned)
for (a, b) in lattice:
    label = f"C={casimir(a,b)}"
    if (a, b) in cells:
        label += f"\ncells={cells[(a,b)]}"
    ax1.annotate(label, (a, b),
                 ha="center", va="center", fontsize=8,
                 weight="bold", color="white")

# Highlight SUBSTRATE FLOOR
floor_pts = [(1, 0), (1, 1)]
fxs, fys = zip(*floor_pts)
ax1.scatter(fxs, fys, s=2400, facecolor="none",
            edgecolors="red", linewidth=3,
            label="SUBSTRATE FLOOR (Casey #9)\n(1,0) meson + (1,1) baryon\nminimal cells for light u/d")

ax1.set_xlabel("a  (SO(5) first highest-weight component)", fontsize=12)
ax1.set_ylabel("b  (SO(5) second highest-weight component)", fontsize=12)
ax1.set_title("K-type lattice on D_IV^5 — rank=2 Cartan slice (faithful 2D)\n"
              "Casimir C(a,b) [color/algebraic eigenvalue]  +  cells [substrate measure, F52]",
              fontsize=11)
ax1.set_xlim(-0.5, 4.5)
ax1.set_ylim(-0.5, 4.5)
ax1.set_aspect("equal")
ax1.grid(True, alpha=0.25)
ax1.legend(loc="upper left", fontsize=9, framealpha=0.95)
plt.colorbar(sc, ax=ax1, label="Casimir eigenvalue C(a,b)", shrink=0.8)

# ---------- Panel 2: Hadron anchoring ----------
ax2.set_facecolor("#fafafa")

k_x = {(1, 0): 1.0, (1, 1): 3.0}

# Floor labels + cell-count
for (a, b), x in k_x.items():
    ax2.axvline(x=x, color="gray", linestyle=":", alpha=0.4)
    ax2.text(x, 50, f"K-type ({a},{b})\ncells={cells[(a,b)]}",
             ha="center", va="bottom", fontsize=11, weight="bold",
             bbox=dict(boxstyle="round,pad=0.4",
                       facecolor="lightyellow", edgecolor="black"))

# Hadrons at each K-type
for (a, b), states in hadron_anchors.items():
    x = k_x[(a, b)]
    n = len(states)
    for i, (name, mass, content, cls) in enumerate(states):
        color = "#2a9d3a" if cls == "floor" else "#e08020"
        size = 320 if cls == "floor" else 200
        x_offset = 0.18 * (i - (n - 1) / 2.0)
        ax2.scatter(x + x_offset, mass, s=size, c=color,
                    edgecolors="black", linewidths=1.2, alpha=0.9, zorder=3)
        ax2.annotate(f"{name}\n{mass} MeV\n{content}",
                     (x + x_offset, mass),
                     xytext=(0, 14), textcoords="offset points",
                     ha="center", fontsize=7.5, zorder=4)

# Casey #9 reach-bound visual
ax2.axhspan(700, 1700, alpha=0.08, color="red")
ax2.text(2.0, 950, "Casey #9 substrate-reach\n(only ground states\nwith mass = pure substrate volume)",
         ha="center", fontsize=9, alpha=0.7, style="italic", color="darkred")

ax2.set_xlabel("K-type address", fontsize=12)
ax2.set_ylabel("Hadron mass (MeV, log scale)", fontsize=12)
ax2.set_title("Hadron anchoring at K-type addresses\n"
              "FLOOR (green) = light u/d at minimal cells — mass = volume in cells x pi^n_C\n"
              "ELEVATIONS (orange) = same K-type, heavier substrate-content (s, c, b)",
              fontsize=11)
ax2.set_yscale("log")
ax2.set_xticks([1.0, 3.0])
ax2.set_xticklabels(["(1, 0)\nMESON address",
                     "(1, 1)\nBARYON address"], fontsize=10)
ax2.set_xlim(0.3, 3.7)
ax2.grid(True, alpha=0.25, which="both")

# Legend
floor_patch = mpatches.Patch(color="#2a9d3a", label="FLOOR (light u/d ground states)")
elev_patch  = mpatches.Patch(color="#e08020", label="ELEVATION (heavier flavor, same K-type)")
ax2.legend(handles=[floor_patch, elev_patch], loc="upper left", fontsize=9)

# ---------- Suptitle ----------
plt.suptitle(
    "D_IV^5 Substrate Cartography v0.1 — Keeper (Mon 2026-06-08 post-EOD)\n"
    "rank=2 makes faithful 2D possible (the lattice IS the algebraic geometry, not a projection).\n"
    "Per Elie Toy 4053: the substrate measures VOLUME (cells per F52), not Casimir. Cells=Casimir at (1,1) is accident; meson (1,0) decides it (cells=5, C=4).",
    fontsize=11, y=1.02
)

plt.tight_layout()
out_path = "/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/Keeper_substrate_cartography_v0_1.png"
plt.savefig(out_path, dpi=150, bbox_inches="tight")
print(f"Saved: {out_path}")
