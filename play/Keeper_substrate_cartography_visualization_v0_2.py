"""
Substrate Cartography Visualization v0.2 — Lane formulas + k decomposition
Keeper, Monday 2026-06-08 post-EOD (iteration after Casey feedback on v0.1)

v0.1 -> v0.2 changes:
  - Drop the cluttered K-type lattice panel (Casey: "too many objects overlaying")
  - Two clean lane charts: meson (1,0) + baryon (1,1)
  - Formulas prominent at top of each panel
  - k axis explicit; k = (k_s, k_c, k_b) heavy-quark substrate-content count
  - Floor = clean BST substrate formula; elevations = QCD/constituent-quark (semi-empirical)
  - Casey #9 reach-bound visually marked AT the floor
  - Three colored ladders per panel (strange, charm, bottom) — all start at floor at k=0
"""

import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# Constants + substrate floor formulas (clean BST per F52/T2487/T2488)
# ============================================================
m_e   = 0.511          # MeV
pi5   = np.pi**5
n_C   = 5
C_2   = 6

m_floor_meson  = n_C * pi5 * m_e   # 5*pi^5*m_e   ~ 782 MeV  (predicts omega)
m_floor_baryon = C_2 * pi5 * m_e   # 6*pi^5*m_e   ~ 938 MeV  (predicts proton)

# Empirical Delta_m per heavy quark (fit from data; QCD, not BST-forced per Casey #9)
# Meson lane:
dm_s_M = (1020 - m_floor_meson) / 2     # phi (k_s=2) -> ~119 MeV/strange
dm_c_M = (3097 - m_floor_meson) / 2     # J/psi (k_c=2) -> ~1158 MeV/charm
dm_b_M = (9460 - m_floor_meson) / 2     # Upsilon (k_b=2) -> ~4339 MeV/bottom
# Baryon lane:
dm_s_B = (1672 - m_floor_baryon) / 3    # Omega- (k_s=3) -> ~245 MeV/strange
dm_c_B = (2286 - m_floor_baryon) / 1    # Lambda_c (k_c=1) -> ~1348 MeV/charm
dm_b_B = (5620 - m_floor_baryon) / 1    # Lambda_b (k_b=1) -> ~4682 MeV/bottom

# ============================================================
# Hadron data — (name, mass_MeV, k_s, k_c, k_b, content_str)
# ============================================================
mesons = [
    ("rho",     770,  0, 0, 0, "u-ubar / d-dbar"),
    ("omega",   782,  0, 0, 0, "u-ubar + d-dbar  (floor PREDICTED 0.05%)"),
    ("K*",      892,  1, 0, 0, "u-sbar"),
    ("phi",    1020,  2, 0, 0, "s-sbar"),
    ("D*",     2007,  0, 1, 0, "c-ubar"),
    ("J/psi",  3097,  0, 2, 0, "c-cbar"),
    ("B*",     5325,  0, 0, 1, "b-ubar"),
    ("Upsilon",9460,  0, 0, 2, "b-bbar"),
]
baryons = [
    ("p",        938,  0, 0, 0, "uud  (floor PREDICTED 0.002%)"),
    ("n",        940,  0, 0, 0, "udd"),
    ("Lambda",  1116,  1, 0, 0, "uds"),
    ("Sigma",   1189,  1, 0, 0, "uus / dds"),
    ("Xi",      1318,  2, 0, 0, "uss / dss"),
    ("Omega-",  1672,  3, 0, 0, "sss"),
    ("Lambda_c",2286,  0, 1, 0, "udc"),
    ("Lambda_b",5620,  0, 0, 1, "udb"),
]

# Color palette per heavy flavor
COL_FLOOR   = "#2a9d3a"
COL_STRANGE = "#e08020"
COL_CHARM   = "#d04040"
COL_BOTTOM  = "#5050d0"

def k_total(h):
    _, _, k_s, k_c, k_b, _ = h
    return k_s + k_c + k_b

def heavy_color(h):
    _, _, k_s, k_c, k_b, _ = h
    if k_s + k_c + k_b == 0: return COL_FLOOR
    if k_b > 0: return COL_BOTTOM
    if k_c > 0: return COL_CHARM
    return COL_STRANGE

def klabel(h):
    _, _, k_s, k_c, k_b, _ = h
    parts = []
    if k_s > 0: parts.append(f"k_s={k_s}")
    if k_c > 0: parts.append(f"k_c={k_c}")
    if k_b > 0: parts.append(f"k_b={k_b}")
    return ", ".join(parts) if parts else "floor (all k=0)"

def plot_lane(ax, hadrons, lane_name, k_address, cells, m_floor,
              dm_s, dm_c, dm_b, floor_pct_match):
    # --- Background: substrate floor band ---
    ax.axhspan(m_floor * 0.97, m_floor * 1.03, alpha=0.15, color="red", zorder=1)
    ax.axhline(y=m_floor, color="red", linestyle="--", linewidth=2.5, zorder=2,
               label=f"Substrate floor (BST clean): m = {cells}·π⁵·m_e = {m_floor:.0f} MeV")

    # --- Predicted ladder lines (one per heavy flavor) ---
    ks = np.array([0, 1, 2, 3])
    ax.plot(ks, m_floor + dm_s * ks, color=COL_STRANGE, linestyle="-",
            linewidth=2, alpha=0.6, zorder=2,
            label=f"strange ladder: m = floor + {dm_s:.0f}·k_s")
    ax.plot(ks, m_floor + dm_c * ks, color=COL_CHARM, linestyle="-",
            linewidth=2, alpha=0.6, zorder=2,
            label=f"charm ladder:   m = floor + {dm_c:.0f}·k_c")
    ax.plot(ks, m_floor + dm_b * ks, color=COL_BOTTOM, linestyle="-",
            linewidth=2, alpha=0.6, zorder=2,
            label=f"bottom ladder:  m = floor + {dm_b:.0f}·k_b")

    # --- Hadron points ---
    for h in hadrons:
        name, mass, k_s, k_c, k_b, content = h
        k = k_total(h)
        col = heavy_color(h)
        sz = 380 if k == 0 else 240
        ax.scatter(k, mass, s=sz, c=col, edgecolors="black",
                   linewidths=1.4, zorder=5)
        ax.annotate(f"{name}\n{mass} MeV\n[{content}]\n{klabel(h)}",
                    (k, mass),
                    xytext=(12, 8), textcoords="offset points",
                    fontsize=8, zorder=6)

    # --- Formula box ---
    formula = (
        f"FLOOR (substrate, BST-forced, F52/T2487/T2488):\n"
        f"   m_floor = cells · π^{{n_C}} · m_e = {cells}π⁵ · m_e  ≈  {m_floor:.1f} MeV  "
        f"(matches observed to {floor_pct_match})\n\n"
        f"ELEVATIONS (QCD constituent-quark, NOT substrate-forced per Casey #9 reach-bound):\n"
        f"   m_hadron ≈ m_floor + Δm_s · k_s + Δm_c · k_c + Δm_b · k_b\n"
        f"   where k_s, k_c, k_b = count of strange / charm / bottom quarks in the hadron\n"
        f"   Δm_s = {dm_s:.0f}    Δm_c = {dm_c:.0f}    Δm_b = {dm_b:.0f}   (MeV per heavy quark)"
    )
    ax.text(0.5, 0.975, formula, transform=ax.transAxes,
            fontsize=9.5, ha="center", va="top", family="monospace",
            bbox=dict(boxstyle="round,pad=0.6", facecolor="lightyellow",
                      edgecolor="black", linewidth=1.2))

    ax.set_title(f"{lane_name} lane — K-type address {k_address}, cells = {cells}",
                 fontsize=13)
    ax.set_xlabel("k = heavy-quark count (k_s + k_c + k_b)", fontsize=11)
    ax.set_ylabel("Hadron mass (MeV, log scale)", fontsize=11)
    ax.set_yscale("log")
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(500, 20000)
    ax.set_xticks([0, 1, 2, 3])
    ax.grid(True, alpha=0.3, which="both")
    ax.legend(loc="lower right", fontsize=8.5)


# ============================================================
# Plot
# ============================================================
fig, (ax_m, ax_b) = plt.subplots(1, 2, figsize=(20, 10))

plot_lane(ax_m, mesons,  "MESON",  "(1, 0)", n_C, m_floor_meson,
          dm_s_M, dm_c_M, dm_b_M, "0.05% (omega)")
plot_lane(ax_b, baryons, "BARYON", "(1, 1)", C_2, m_floor_baryon,
          dm_s_B, dm_c_B, dm_b_B, "0.002% (proton)")

plt.suptitle(
    "D_IV⁵ Substrate Cartography v0.2 — formulas + k decomposition\n"
    "k = heavy-quark substrate-content count.  Floor = BST forces.  Elevations = QCD adds.\n"
    "Casey #9 reach-bound is visible as the red floor band: substrate forces below, QCD takes over above.",
    fontsize=12, y=1.02
)
plt.tight_layout()

out = "/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/Keeper_substrate_cartography_v0_2.png"
plt.savefig(out, dpi=150, bbox_inches="tight")
print(f"Saved: {out}")
