#!/usr/bin/env python3
"""
BST Commitment Density Transition Profile — Solar System
=========================================================

Computes and plots the transition from gravitational commitment density
(near the Sun) to cosmological channel noise (far from the Sun) across
four interpolation models:

  A  Simple addition (no MOND — control)
  B  Shannon / Wiener filter (BST-Shannon)
  C  Simple MOND interpolation  mu(x) = x/(1+x)
  D  Standard MOND interpolation mu(x) = x/sqrt(1+x^2)

Four panels (2x2):
  1  Commitment density  rho(r)/rho_137  vs r
  2  Acceleration a(r)   vs r
  3  Clock rate N(r)/N_0 vs r
  4  G/C ratio           vs r

Casey Koons — Bubble Spacetime Theory, March 2026
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, NullFormatter

# ── Physical constants ──────────────────────────────────────────────
GM_sun = 1.327e20        # m^3 s^-2
a0     = 1.2e-10         # m s^-2   (MOND critical acceleration)
c      = 3.0e8           # m s^-1
AU     = 1.496e11        # m

# Transition radius
r_t = np.sqrt(GM_sun / a0)                     # metres
r_t_AU = r_t / AU                              # ~ 7100 AU

# Channel-noise background commitment density (normalised to rho_137 = 1)
rho_inf = a0 * r_t / c**2                      # dimensionless rho_inf / rho_137

# ── Radial grid (log-spaced, 0.1 AU to 100 000 AU) ─────────────────
r_AU  = np.logspace(np.log10(0.1), np.log10(1e5), 4000)
r     = r_AU * AU                               # metres

# ── Newtonian quantities ────────────────────────────────────────────
phi_N  = GM_sun / (r * c**2)                    # dimensionless potential / c^2
a_N    = GM_sun / r**2                           # m s^-2

# Gravitational commitment density: rho_grav / rho_137
rho_grav = phi_N                                # proportional to GM/(rc^2)

# ── Model A — Simple addition (no MOND) ────────────────────────────
rho_A = rho_grav + rho_inf
a_A   = a_N.copy()                              # accelerometer sees only grad(rho_grav)

# ── Model B — Shannon / Wiener filter (BST-Shannon) ────────────────
#   a_eff = a_N^2/(a_N + a0) + sqrt(a_N * a0) * a0/(a_N + a0)
#   Limits: a_N >> a0 -> a_N ;  a_N << a0 -> sqrt(a_N * a0)
x_B   = a_N / a0
a_B   = (a_N**2 / (a_N + a0)) + (np.sqrt(a_N * a0) * a0 / (a_N + a0))
# Effective potential from integrating a_B outward (for density plot)
# rho_B = integral of a_B dr / c^2, computed via effective enhancement
rho_B = rho_grav * (a_B / a_N) + rho_inf

# ── Model C — Simple MOND: mu(x)=x/(1+x) ──────────────────────────
#   mu(a/a0) * a = a_N  =>  [a/(a0+a)] * a = a_N
#   a^2 = a_N*(a + a0)  =>  a^2 - a_N*a - a_N*a0 = 0
#   a = [a_N + sqrt(a_N^2 + 4*a_N*a0)] / 2
a_C   = 0.5 * (a_N + np.sqrt(a_N**2 + 4.0 * a_N * a0))
rho_C = rho_grav * (a_C / a_N) + rho_inf

# ── Model D — Standard MOND: mu(x) = x/sqrt(1+x^2) ────────────────
#   mu(a/a0)*a = a_N  =>  a^2/sqrt(a0^2+a^2) = a_N
#   a^4 = a_N^2*(a0^2 + a^2)  =>  a^4 - a_N^2*a^2 - a_N^2*a0^2 = 0
#   Let u = a^2:  u = [a_N^2 + sqrt(a_N^4 + 4*a_N^2*a0^2)] / 2
u_D   = 0.5 * (a_N**2 + np.sqrt(a_N**4 + 4.0 * a_N**2 * a0**2))
a_D   = np.sqrt(u_D)
rho_D = rho_grav * (a_D / a_N) + rho_inf

# ── Clock rate: N(r)/N0 = sqrt(1 - rho/rho_137) ≈ 1 - rho/(2*rho_137)
# With rho_137 = 1 in our normalisation:
clock_A = np.sqrt(1.0 - np.clip(rho_A, 0, 0.999))
clock_B = np.sqrt(1.0 - np.clip(rho_B, 0, 0.999))
clock_C = np.sqrt(1.0 - np.clip(rho_C, 0, 0.999))
clock_D = np.sqrt(1.0 - np.clip(rho_D, 0, 0.999))

# ── G/C ratio (gravitational field / commitment rate) ───────────────
# Defined as a(r) / [c * (1 - N/N0)]  ~  a(r) / [c * rho/(2*rho_137)]
# This ratio is constant in pure Newton and deviates in MOND-like regimes.
eps = 1e-30
gc_A = a_A / (c * np.clip(1.0 - clock_A, eps, None))
gc_B = a_B / (c * np.clip(1.0 - clock_B, eps, None))
gc_C = a_C / (c * np.clip(1.0 - clock_C, eps, None))
gc_D = a_D / (c * np.clip(1.0 - clock_D, eps, None))

# Normalise G/C to the value at 1 AU for clearer comparison
idx_1AU = np.argmin(np.abs(r_AU - 1.0))
gc_A /= gc_A[idx_1AU]
gc_B /= gc_B[idx_1AU]
gc_C /= gc_C[idx_1AU]
gc_D /= gc_D[idx_1AU]

# ── Solar-system landmarks ──────────────────────────────────────────
landmarks = {
    "Mercury":       0.387,
    "Venus":         0.723,
    "Earth":         1.0,
    "Mars":          1.524,
    "Jupiter":       5.203,
    "Saturn":        9.537,
    "Uranus":       19.19,
    "Neptune":      30.07,
    "Pluto":        39.48,
    "New Horizons":  58.0,
    "Voyager 1":   160.0,
}

# ── Plotting ────────────────────────────────────────────────────────
model_styles = {
    "A  Newton (control)":   {"color": "#888888", "ls": "--", "lw": 1.5},
    "B  BST-Shannon":        {"color": "#2271B2", "ls": "-",  "lw": 2.2},
    "C  MOND x/(1+x)":      {"color": "#D55E00", "ls": "-.", "lw": 1.8},
    "D  MOND x/sqrt(1+x^2)":{"color": "#009E73", "ls": ":",  "lw": 1.8},
}

fig, axes = plt.subplots(2, 2, figsize=(14, 10), dpi=180)
fig.subplots_adjust(hspace=0.32, wspace=0.30, left=0.08, right=0.96,
                    top=0.92, bottom=0.08)
fig.suptitle("BST Commitment Density Transition Profile — Solar System",
             fontsize=15, fontweight="bold", y=0.97)

# Clock slowdown: 1 - N/N0 = 1 - sqrt(1-rho) ≈ rho/2  (more informative than N/N0)
slow_A = 1.0 - clock_A
slow_B = 1.0 - clock_B
slow_C = 1.0 - clock_C
slow_D = 1.0 - clock_D

data_map = {
    0: {"ylabel": r"Commitment density  $\rho\,/\,\rho_{137}$",
        "data": [rho_A, rho_B, rho_C, rho_D]},
    1: {"ylabel": r"Acceleration  $a(r)$  [m s$^{-2}$]",
        "data": [a_A, a_B, a_C, a_D]},
    2: {"ylabel": r"Clock slowdown  $1 - N(r)/N_0$",
        "data": [slow_A, slow_B, slow_C, slow_D]},
    3: {"ylabel": r"$G/C$ ratio  (normalised to 1 AU)",
        "data": [gc_A, gc_B, gc_C, gc_D]},
}

panel_letters = ["(a)", "(b)", "(c)", "(d)"]

for idx, ax in enumerate(axes.flat):
    info  = data_map[idx]
    yvals = info["data"]

    for (label, sty), y in zip(model_styles.items(), yvals):
        ax.loglog(r_AU, y, label=label, **sty)

    # Transition radius
    ax.axvline(r_t_AU, color="red", ls="--", lw=1.0, alpha=0.7)
    # Label it once (top-right panel)
    if idx == 1:
        ax.text(r_t_AU * 1.15, ax.get_ylim()[0] if ax.get_ylim()[0] > 0 else 1e-16,
                r"$r_t \approx 7100$ AU", color="red", fontsize=8,
                va="bottom", rotation=90)

    # a0 reference line on acceleration panel
    if idx == 1:
        ax.axhline(a0, color="red", ls=":", lw=0.8, alpha=0.6)
        ax.text(0.12, a0 * 1.5, r"$a_0 = 1.2\times10^{-10}$ m s$^{-2}$",
                color="red", fontsize=7, transform=ax.get_yaxis_transform())

    # Planet / spacecraft markers
    for name, pos_AU in landmarks.items():
        ax.axvline(pos_AU, color="#CCCCCC", lw=0.4, zorder=0)

    # Labels for selected landmarks (only on bottom panels to avoid clutter)
    if idx >= 2:
        for name, pos_AU in landmarks.items():
            if name in ("Earth", "Jupiter", "Neptune", "Voyager 1", "New Horizons"):
                ylims = ax.get_ylim()
                ax.text(pos_AU, 0.97, name, fontsize=5.5, rotation=90,
                        ha="right", va="top", color="#666666",
                        transform=ax.get_xaxis_transform())

    ax.set_xlabel("Distance from Sun  [AU]", fontsize=9)
    ax.set_ylabel(info["ylabel"], fontsize=9)
    ax.set_xlim(0.1, 1e5)
    ax.tick_params(labelsize=8)
    ax.text(0.02, 0.95, panel_letters[idx], transform=ax.transAxes,
            fontsize=11, fontweight="bold", va="top")

    if idx == 0:
        ax.legend(fontsize=7, loc="upper right", framealpha=0.9)

# ── Divergence annotation on acceleration panel (idx=1) ─────────────
ax1 = axes.flat[1]
# Find where Model B deviates from Model A by >5%
ratio_BA = a_B / a_A
diverge_mask = ratio_BA > 1.05
if np.any(diverge_mask):
    r_div = r_AU[diverge_mask][0]
    ax1.annotate(f"Models diverge\n(>{5}% at {r_div:.0f} AU)",
                 xy=(r_div, a_N[diverge_mask][0]),
                 xytext=(r_div * 0.05, a_N[diverge_mask][0] * 20),
                 fontsize=7, color="#2271B2",
                 arrowprops=dict(arrowstyle="->", color="#2271B2", lw=1.0))

# ── Testable prediction zone shading on acceleration panel ──────────
ax1.axvspan(50, 1e5, color="#FFE0B2", alpha=0.15, zorder=0)
ax1.text(300, ax1.get_ylim()[1] * 0.3 if ax1.get_ylim()[1] > 0 else 1e-10,
         "Testable prediction zone",
         fontsize=7, color="#E65100", fontstyle="italic",
         bbox=dict(boxstyle="round,pad=0.3", fc="#FFF3E0", ec="#E65100",
                   alpha=0.8))

# ── Add transition radius label to panel (a) ───────────────────────
ax0 = axes.flat[0]
ax0.text(r_t_AU * 1.3, rho_inf * 3,
         r"$r_t = \sqrt{GM_\odot / a_0}$" + f"\n{r_t_AU:.0f} AU",
         fontsize=7, color="red",
         bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="red", alpha=0.8))

# ── Save ────────────────────────────────────────────────────────────
outpath = "/Users/cskoons/projects/github/BubbleSpacetimeTheory/notes/BST_TransitionProfile.png"
fig.savefig(outpath, bbox_inches="tight")
print(f"Saved: {outpath}")
print(f"\nTransition radius r_t = {r_t_AU:.1f} AU  ({r_t/1e3:.2e} km)")
print(f"rho_inf / rho_137    = {rho_inf:.4e}")
print(f"\nDivergence summary (acceleration, ratio to Newton):")
for label_tag, a_model in [("B (BST-Shannon)", a_B), ("C (MOND simple)", a_C),
                            ("D (MOND std)", a_D)]:
    ratio = a_model / a_A
    # Find where ratio exceeds 1.01 (1% deviation)
    mask_01 = ratio > 1.01
    mask_05 = ratio > 1.05
    mask_10 = ratio > 1.10
    r01 = r_AU[mask_01][0] if np.any(mask_01) else float("inf")
    r05 = r_AU[mask_05][0] if np.any(mask_05) else float("inf")
    r10 = r_AU[mask_10][0] if np.any(mask_10) else float("inf")
    print(f"  {label_tag:25s}  >1%: {r01:8.0f} AU   >5%: {r05:8.0f} AU   >10%: {r10:8.0f} AU")
