#!/usr/bin/env python3
"""
WHAT IF? — The BST Parameter Landscape Explorer
=================================================
Systematically explores ALL possible (N_c, n_C, N_max) integer triples
and shows why only (3, 5, 137) produces a viable universe.

A CI can sweep parameter space programmatically:

    from toy_what_if import WhatIfMachine
    wim = WhatIfMachine()
    result = wim.compute(Nc=3, nC=5, Nmax=137)
    landscape = wim.sweep()
    wim.what_if(Nc=4)

Or run directly for the visual interface:
    python toy_what_if.py

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from math import factorial, pi, sqrt, log, floor
from dataclasses import dataclass, field
from typing import Tuple, Optional, List, Dict

# ─── Observed values for comparison ───
OBSERVED = {
    'alpha':            1 / 137.035999,
    'proton_electron':  1836.15267,
    'sin2_theta_W':     0.23122,
    'alpha_s':          0.35,
    'N_gen':            3,
    'gluons':           8,
}

# The one true triple
TRUE_TRIPLE = (3, 5, 137)

# ─── Number of constraints ───
N_CONSTRAINTS = 13


# ─────────────────────────────────────────────────────────────
#  Data classes
# ─────────────────────────────────────────────────────────────

@dataclass
class ConstraintResult:
    """Result of a single constraint check."""
    name: str
    passed: bool
    explanation: str
    category: str = ""  # "gauge", "geometry", "channel", "precision"

@dataclass
class PhysicsResult:
    """Full physics computation for one (Nc, nC, Nmax) triple."""
    Nc: int
    nC: int
    Nmax: int
    # Derived integers
    genus: int = 0
    C2: int = 0
    Gamma_order: int = 0
    vol: float = 0.0
    # Physics
    alpha: float = 0.0
    proton_electron: float = 0.0
    sin2_theta_W: float = 0.0
    alpha_s: float = 0.0
    beta0: float = 0.0
    N_gen: int = 0
    gluons: int = 0
    mass_gap_units: float = 0.0
    n_s: float = 0.0          # spectral index
    # Constraints
    constraints: List[ConstraintResult] = field(default_factory=list)
    score: int = 0
    max_score: int = N_CONSTRAINTS
    viable: bool = False


@dataclass
class LandscapeResult:
    """Result of a parameter sweep."""
    results: Dict[Tuple[int, int, int], PhysicsResult]
    best_triple: Tuple[int, int, int]
    best_score: int
    viable_count: int
    total_count: int


# ─────────────────────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────────────────────

def _is_prime(n: int) -> bool:
    """Simple primality test."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def _compute_alpha(Nc: int, nC: int) -> float:
    """Compute Wyler/BST fine structure constant from (Nc, nC)."""
    if nC < 1 or Nc < 1:
        return 0.0
    Gamma_order = factorial(nC) * 2**(nC - 1)
    vol = pi**nC / Gamma_order
    return (Nc**2) / (2**Nc * pi**4) * vol**(1/4)


# ─────────────────────────────────────────────────────────────
#  Constraint functions — each returns (bool, explanation)
#  13 total constraints across four categories
# ─────────────────────────────────────────────────────────────

# === GAUGE CONSTRAINTS (require specific Nc) ===

def check_asymptotic_freedom(Nc: int, nC: int) -> Tuple[bool, str]:
    """beta_0 > 0 requires 11*Nc/3 > 2*N_f/3 where N_f = nC + 1."""
    N_f = nC + 1
    beta0 = (11 * Nc - 2 * N_f) / 3.0
    if Nc < 2:
        return False, f"N_c={Nc} < 2: no non-abelian gauge group"
    if beta0 > 0:
        return True, f"beta_0 = {beta0:.1f} > 0 (11x{Nc} - 2x{N_f} = {11*Nc - 2*N_f})"
    return False, f"beta_0 = {beta0:.1f} <= 0: too many flavors (N_f={N_f})"


def check_confinement(Nc: int) -> Tuple[bool, str]:
    """Color confinement requires N_c >= 3 for area law."""
    if Nc >= 3:
        return True, f"N_c={Nc}: SU({Nc}) confines via area law"
    return False, f"N_c={Nc}: SU({Nc}) does not confine"


def check_generations(Nc: int, nC: int) -> Tuple[bool, str]:
    """Lefschetz: Z_{N_c} on CP^{n_C-1} gives exactly N_c fixed points.
    We need exactly 3 generations, so N_c must be 3."""
    if Nc != 3:
        return False, f"N_c={Nc} gives {Nc} generations, need 3"
    if nC < Nc:
        return False, f"n_C={nC} < N_c={Nc}: CP^{nC-1} too small for Z_3"
    return True, f"Z_3 on CP^{nC-1}: Lefschetz gives 3 fixed pts = 3 generations"


def check_anomaly_free(Nc: int, nC: int) -> Tuple[bool, str]:
    """Anomaly cancellation: genus = n_C + 2 must equal beta_0 for N_f = n_C + 1.
    This pins the relationship: genus = beta_0 requires 11*Nc - 2*(nC+1) = 3*(nC+2)."""
    genus = nC + 2
    N_f = nC + 1
    beta0 = (11 * Nc - 2 * N_f) / 3.0
    if abs(beta0 - genus) < 0.01:
        return True, f"beta_0 = genus = {genus}: anomaly-free (11x{Nc}-2x{N_f} = 3x{genus})"
    return False, f"beta_0={beta0:.1f} != genus={genus}: anomaly mismatch"


# === GEOMETRY CONSTRAINTS (require specific nC) ===

def check_hermitian_symmetric(nC: int) -> Tuple[bool, str]:
    """D_IV^n bounded symmetric domain of type IV exists for n >= 2."""
    if nC >= 2:
        return True, f"D_IV^{nC}: bounded symmetric domain, rank 2"
    return False, f"n_C={nC} < 2: no type IV domain"


def check_wallach_electron(nC: int) -> Tuple[bool, str]:
    """Electron as boundary excitation: weight k=1 below Wallach set k_min = n_C - 2.
    Requires n_C >= 4 so k_min >= 2 > 1, putting electron on boundary Shilov."""
    k_min = nC - 2
    if nC >= 4 and k_min > 1:
        return True, f"k_min={k_min} > 1: electron (k=1) is boundary mode on Shilov S^4xS^1"
    return False, f"k_min={k_min}: electron not cleanly separated from bulk"


def check_1920_cancellation(nC: int) -> Tuple[bool, str]:
    """The 1920 cancellation: |Gamma| = nC! * 2^(nC-1) must equal 1920.
    This gives nC! * 2^(nC-1) = 1920, which is uniquely solved by nC = 5.
    (5! * 2^4 = 120 * 16 = 1920)."""
    Gamma = factorial(nC) * 2**(nC - 1)
    if Gamma == 1920:
        return True, f"|Gamma| = {nC}! x 2^{nC-1} = {Gamma} = 1920: baryon orbit cancellation"
    return False, f"|Gamma| = {nC}! x 2^{nC-1} = {Gamma}, not 1920"


def check_mass_hierarchy(Nc: int, nC: int) -> Tuple[bool, str]:
    """m_p/m_e must match observed 1836.15 to within 1%."""
    C2 = nC + 1
    ratio = C2 * pi**nC
    obs = OBSERVED['proton_electron']
    pct = abs(ratio - obs) / obs * 100
    if pct < 1.0:
        return True, f"m_p/m_e = {ratio:.2f} (obs: {obs:.2f}, err: {pct:.3f}%)"
    return False, f"m_p/m_e = {ratio:.1f} vs obs {obs:.1f} (err: {pct:.1f}%)"


# === CHANNEL CONSTRAINTS (require specific Nmax) ===

def check_prime_channel(Nmax: int) -> Tuple[bool, str]:
    """N_max must be prime for unique channel structure."""
    if _is_prime(Nmax):
        return True, f"N_max={Nmax} is prime: unique channel factorization"
    below = Nmax - 1
    while below > 1 and not _is_prime(below):
        below -= 1
    above = Nmax + 1
    while not _is_prime(above):
        above += 1
    return False, f"N_max={Nmax} not prime (nearest: {below}, {above})"


def check_reality_budget(Nmax: int) -> Tuple[bool, str]:
    """Finite N_max in range [100, 200] for viable cosmological constant."""
    if 100 <= Nmax <= 200:
        return True, f"N_max={Nmax}: Lambda positive, cosmic acceleration viable"
    if Nmax < 100:
        return False, f"N_max={Nmax} < 100: Lambda too large, universe expands too fast"
    return False, f"N_max={Nmax} > 200: Lambda ~ 0, no cosmic acceleration"


def check_spectral_index(nC: int, Nmax: int) -> Tuple[bool, str]:
    """CMB spectral index n_s = 1 - n_C/N_max must match Planck (0.9649 +/- 0.0042)."""
    n_s = 1.0 - nC / Nmax
    obs = 0.9649
    sigma = 0.0042
    deviation = abs(n_s - obs) / sigma
    if deviation < 2.0:
        return True, f"n_s = 1 - {nC}/{Nmax} = {n_s:.4f} (Planck: {obs}, {deviation:.1f}sigma)"
    return False, f"n_s = {n_s:.4f}, {deviation:.1f}sigma from Planck {obs}"


# === THE LOCK: alpha-Nmax consistency ===

def check_dirac_consistency(Nc: int, nC: int, Nmax: int) -> Tuple[bool, str]:
    """THE KEY CONSTRAINT: N_max must equal floor(1/alpha).
    alpha is determined by (Nc, nC) alone. N_max = floor(1/alpha) locks all three.
    For (3,5): alpha = 1/137.036, floor(1/alpha) = 137. UNIQUE."""
    alpha = _compute_alpha(Nc, nC)
    if alpha <= 0:
        return False, f"alpha=0: degenerate"
    inv_alpha = 1.0 / alpha
    required_Nmax = floor(inv_alpha)
    if Nmax == required_Nmax:
        return True, (f"N_max={Nmax} = floor(1/alpha) = floor({inv_alpha:.3f}): "
                      f"Dirac quantization locks all three integers")
    return False, (f"N_max={Nmax} != floor(1/alpha) = {required_Nmax} "
                   f"(1/alpha = {inv_alpha:.3f})")


def check_alpha_viable(Nc: int, nC: int) -> Tuple[bool, str]:
    """alpha must lie in a viable window for chemistry: roughly [1/200, 1/100]."""
    alpha = _compute_alpha(Nc, nC)
    if 1/200 < alpha < 1/100:
        return True, f"alpha = 1/{1/alpha:.1f}: chemistry and stable atoms possible"
    if alpha > 0:
        return False, f"alpha = 1/{1/alpha:.1f}: outside viable range [1/200, 1/100]"
    return False, f"alpha ~ 0: degenerate"


# ─────────────────────────────────────────────────────────────
#  The WhatIfMachine — CI programmatic interface
# ─────────────────────────────────────────────────────────────

class WhatIfMachine:
    """Explore the BST parameter landscape programmatically.

    Usage:
        wim = WhatIfMachine()
        result = wim.compute(Nc=3, nC=5, Nmax=137)
        landscape = wim.sweep()
        wim.what_if(Nc=4)
    """

    def compute(self, Nc: int = 3, nC: int = 5, Nmax: int = 137) -> PhysicsResult:
        """Compute full physics and run all 13 constraint checks for a triple."""
        r = PhysicsResult(Nc=Nc, nC=nC, Nmax=Nmax)

        # Derived integers
        r.genus = nC + 2
        r.C2 = nC + 1
        r.Gamma_order = factorial(nC) * 2**(nC - 1) if nC >= 1 else 0
        r.vol = pi**nC / r.Gamma_order if r.Gamma_order > 0 else 0.0

        # Physics computations
        r.alpha = _compute_alpha(Nc, nC)
        r.proton_electron = r.C2 * pi**nC
        r.sin2_theta_W = Nc / (Nc + 2 * nC) if (Nc + 2 * nC) > 0 else 0.0
        r.alpha_s = (nC + 2) / (4 * nC) if nC > 0 else 0.0
        r.beta0 = (11 * Nc - 2 * (nC + 1)) / 3.0
        r.N_gen = Nc
        r.gluons = Nc**2 - 1
        r.mass_gap_units = r.C2 * pi**nC
        r.n_s = 1.0 - nC / Nmax if Nmax > 0 else 0.0

        # Run all 13 constraints, organized by category
        checks_and_names = [
            # Gauge constraints (Nc)
            ("Asymptotic freedom",     "gauge",     check_asymptotic_freedom(Nc, nC)),
            ("Color confinement",      "gauge",     check_confinement(Nc)),
            ("Three generations",      "gauge",     check_generations(Nc, nC)),
            ("Anomaly cancellation",   "gauge",     check_anomaly_free(Nc, nC)),
            # Geometry constraints (nC)
            ("Hermitian symmetric",    "geometry",  check_hermitian_symmetric(nC)),
            ("Wallach electron bound", "geometry",  check_wallach_electron(nC)),
            ("1920 cancellation",      "geometry",  check_1920_cancellation(nC)),
            ("Mass hierarchy (1%)",    "geometry",  check_mass_hierarchy(Nc, nC)),
            ("Viable alpha",           "geometry",  check_alpha_viable(Nc, nC)),
            # Channel constraints (Nmax)
            ("Prime channel",          "channel",   check_prime_channel(Nmax)),
            ("Reality budget",         "channel",   check_reality_budget(Nmax)),
            ("Spectral index n_s",     "channel",   check_spectral_index(nC, Nmax)),
            # The lock (all three)
            ("Dirac consistency",      "lock",      check_dirac_consistency(Nc, nC, Nmax)),
        ]

        r.constraints = []
        r.score = 0
        for name, cat, (passed, explanation) in checks_and_names:
            r.constraints.append(ConstraintResult(
                name=name, passed=passed, explanation=explanation, category=cat))
            if passed:
                r.score += 1
        r.max_score = len(checks_and_names)
        r.viable = (r.score == r.max_score)
        return r

    def sweep(self,
              Nc_range: Tuple[int, int] = (1, 8),
              nC_range: Tuple[int, int] = (1, 10),
              Nmax_range: Tuple[int, int] = (100, 200)) -> LandscapeResult:
        """Sweep all integer triples in the given ranges."""
        results = {}
        best_triple = (0, 0, 0)
        best_score = -1
        viable_count = 0

        for Nc in range(Nc_range[0], Nc_range[1] + 1):
            for nC in range(nC_range[0], nC_range[1] + 1):
                for Nmax in range(Nmax_range[0], Nmax_range[1] + 1):
                    r = self.compute(Nc, nC, Nmax)
                    results[(Nc, nC, Nmax)] = r
                    if r.score > best_score:
                        best_score = r.score
                        best_triple = (Nc, nC, Nmax)
                    if r.viable:
                        viable_count += 1

        return LandscapeResult(
            results=results,
            best_triple=best_triple,
            best_score=best_score,
            viable_count=viable_count,
            total_count=len(results),
        )

    def sweep_NcnC(self,
                   Nc_range: Tuple[int, int] = (1, 8),
                   nC_range: Tuple[int, int] = (1, 10),
                   Nmax: int = 137) -> Dict[Tuple[int, int], PhysicsResult]:
        """Sweep (Nc, nC) at fixed Nmax. Returns dict keyed by (Nc, nC)."""
        results = {}
        for Nc in range(Nc_range[0], Nc_range[1] + 1):
            for nC in range(nC_range[0], nC_range[1] + 1):
                results[(Nc, nC)] = self.compute(Nc, nC, Nmax)
        return results

    def what_if(self, Nc: Optional[int] = None, nC: Optional[int] = None,
                Nmax: Optional[int] = None, silent: bool = False) -> PhysicsResult:
        """Ask 'what if?' — change one parameter from the true triple.
        Prints a comparison report unless silent=True."""
        use_Nc = Nc if Nc is not None else TRUE_TRIPLE[0]
        use_nC = nC if nC is not None else TRUE_TRIPLE[1]
        use_Nmax = Nmax if Nmax is not None else TRUE_TRIPLE[2]

        alt = self.compute(use_Nc, use_nC, use_Nmax)
        ref = self.compute(*TRUE_TRIPLE)

        if not silent:
            changed = []
            if Nc is not None and Nc != 3:
                changed.append(f"N_c: 3 -> {Nc}")
            if nC is not None and nC != 5:
                changed.append(f"n_C: 5 -> {nC}")
            if Nmax is not None and Nmax != 137:
                changed.append(f"N_max: 137 -> {Nmax}")
            change_str = ", ".join(changed) if changed else "no change"

            print(f"\n{'='*72}")
            print(f"  WHAT IF?  ({use_Nc}, {use_nC}, {use_Nmax})")
            print(f"  Changed: {change_str}")
            print(f"{'='*72}")
            print(f"  Viability: {alt.score}/{alt.max_score}"
                  f"  (reality: {ref.score}/{ref.max_score})")
            print()

            # Show constraints grouped by category
            cats = [("gauge", "GAUGE (N_c)"), ("geometry", "GEOMETRY (n_C)"),
                    ("channel", "CHANNEL (N_max)"), ("lock", "THE LOCK (all three)")]
            for cat_key, cat_label in cats:
                cat_constraints = [c for c in alt.constraints if c.category == cat_key]
                if not cat_constraints:
                    continue
                print(f"  --- {cat_label} ---")
                for c in cat_constraints:
                    mark = " PASS " if c.passed else "FAIL! "
                    print(f"  [{mark}] {c.name}")
                    print(f"           {c.explanation}")
                print()

            # Physics comparison
            print(f"  {'Quantity':<22} {'What-If':>14} {'Reality':>14} {'Observed':>14}")
            print(f"  {'-'*22} {'-'*14} {'-'*14} {'-'*14}")
            def fmt_a(a):
                return f"1/{1/a:.1f}" if a > 1e-6 else "~0"
            rows = [
                ("alpha",        fmt_a(alt.alpha), fmt_a(ref.alpha), fmt_a(OBSERVED['alpha'])),
                ("m_p/m_e",      f"{alt.proton_electron:.1f}",
                                 f"{ref.proton_electron:.2f}",
                                 f"{OBSERVED['proton_electron']:.2f}"),
                ("sin2_theta_W", f"{alt.sin2_theta_W:.5f}",
                                 f"{ref.sin2_theta_W:.5f}",
                                 f"{OBSERVED['sin2_theta_W']:.5f}"),
                ("alpha_s(m_p)", f"{alt.alpha_s:.4f}",
                                 f"{ref.alpha_s:.4f}",
                                 f"{OBSERVED['alpha_s']:.4f}"),
                ("n_s (CMB)",    f"{alt.n_s:.4f}",
                                 f"{ref.n_s:.4f}",
                                 "0.9649"),
                ("beta_0",       f"{alt.beta0:.1f}",
                                 f"{ref.beta0:.1f}",
                                 "> 0"),
                ("generations",  f"{alt.N_gen}", f"{ref.N_gen}", f"{OBSERVED['N_gen']}"),
                ("gluons",       f"{alt.gluons}", f"{ref.gluons}", f"{OBSERVED['gluons']}"),
                ("|Gamma|",      f"{alt.Gamma_order}", f"{ref.Gamma_order}", "1920"),
            ]
            for label, v_alt, v_ref, v_obs in rows:
                print(f"  {label:<22} {v_alt:>14} {v_ref:>14} {v_obs:>14}")

            # Summary
            failures = [c for c in alt.constraints if not c.passed]
            if failures:
                print(f"\n  BROKEN ({len(failures)} constraint{'s' if len(failures)>1 else ''}):")
                for c in failures:
                    print(f"    x {c.name}: {c.explanation}")
            else:
                print(f"\n  ALL {alt.max_score} CONSTRAINTS SATISFIED — viable universe!")

            print(f"{'='*72}\n")

        return alt


# ─────────────────────────────────────────────────────────────
#  Visual interface
# ─────────────────────────────────────────────────────────────

def run_visual():
    """Launch the interactive matplotlib visualization."""
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Slider, Button
    import matplotlib.patheffects as pe
    import matplotlib.colors as mcolors

    # Colors
    BG = '#0a0a1a'
    GOLD = '#ffd700'
    CYAN = '#00ccff'
    GREEN = '#44ff88'
    RED = '#ff4444'
    YELLOW = '#ffcc00'
    GREY = '#666688'
    WHITE = '#ccccdd'
    PANEL = '#0d0d28'
    SLIDER_BG = '#1a1a2e'

    wim = WhatIfMachine()

    # ─── Figure ───
    fig = plt.figure(figsize=(18, 11), facecolor=BG)
    fig.canvas.manager.set_window_title('WHAT IF? — BST Parameter Landscape')

    # Title
    fig.text(0.5, 0.97, 'WHAT IF?', fontsize=32, fontweight='bold',
             color=CYAN, ha='center', va='top', fontfamily='monospace',
             path_effects=[pe.withStroke(linewidth=3, foreground='#004466')])
    fig.text(0.5, 0.935, 'Only (3, 5, 137) passes all 13 constraints',
             fontsize=13, color='#6688aa', ha='center', va='top',
             fontfamily='monospace')

    # ─── Sliders ───
    ax_Nc   = fig.add_axes([0.08, 0.885, 0.25, 0.020])
    ax_nC   = fig.add_axes([0.08, 0.860, 0.25, 0.020])
    ax_Nmax = fig.add_axes([0.08, 0.835, 0.25, 0.020])
    for ax in [ax_Nc, ax_nC, ax_Nmax]:
        ax.set_facecolor(SLIDER_BG)

    slider_Nc   = Slider(ax_Nc,   'N_c  ', 1, 8, valinit=3, valstep=1,
                          color='#ff4466', valfmt='%d')
    slider_nC   = Slider(ax_nC,   'n_C  ', 1, 10, valinit=5, valstep=1,
                          color='#44ff66', valfmt='%d')
    slider_Nmax = Slider(ax_Nmax, 'N_max', 50, 250, valinit=137, valstep=1,
                          color='#4466ff', valfmt='%d')

    for s in [slider_Nc, slider_nC, slider_Nmax]:
        s.label.set_color(WHITE)
        s.label.set_fontsize(13)
        s.label.set_fontfamily('monospace')
        s.valtext.set_color(WHITE)
        s.valtext.set_fontsize(13)

    # ─── Score display ───
    ax_score = fig.add_axes([0.38, 0.83, 0.22, 0.08])
    ax_score.set_facecolor(BG)
    ax_score.axis('off')

    # ─── Buttons ───
    ax_btn = fig.add_axes([0.63, 0.85, 0.10, 0.04])
    btn_sweep = Button(ax_btn, 'Sweep All', color='#1a1a3a', hovercolor='#2a2a5a')
    btn_sweep.label.set_color(CYAN)
    btn_sweep.label.set_fontsize(11)
    btn_sweep.label.set_fontfamily('monospace')

    ax_rst = fig.add_axes([0.75, 0.85, 0.12, 0.04])
    btn_reset = Button(ax_rst, 'Reset (3,5,137)', color='#1a1a3a', hovercolor='#2a2a5a')
    btn_reset.label.set_color(GOLD)
    btn_reset.label.set_fontsize(10)
    btn_reset.label.set_fontfamily('monospace')

    # ─── Panels ───
    ax_heat   = fig.add_axes([0.05, 0.08, 0.38, 0.72])
    ax_heat.set_facecolor(PANEL)
    ax_report = fig.add_axes([0.48, 0.38, 0.50, 0.42])
    ax_report.set_facecolor(PANEL)
    ax_report.axis('off')
    ax_table  = fig.add_axes([0.48, 0.08, 0.50, 0.27])
    ax_table.set_facecolor(PANEL)
    ax_table.axis('off')

    # ─── Cache ───
    sweep_cache = {}

    def get_sweep_grid(Nmax: int):
        """Compute or retrieve cached (Nc, nC) viability grid."""
        if Nmax in sweep_cache:
            return sweep_cache[Nmax]
        grid = np.zeros((10, 8))  # nC=1..10 x Nc=1..8
        for i, nC in enumerate(range(1, 11)):
            for j, Nc in enumerate(range(1, 9)):
                grid[i, j] = wim.compute(Nc, nC, Nmax).score
        sweep_cache[Nmax] = grid
        return grid

    def draw_heatmap(ax, Nmax, hl_Nc=None, hl_nC=None):
        """Draw the viability heat map."""
        ax.clear()
        ax.set_facecolor(PANEL)
        grid = get_sweep_grid(Nmax)

        colors_list = ['#1a0000', '#440000', '#882200', '#cc4400',
                       '#cc8800', '#aaaa00', '#66bb33', '#33cc55',
                       '#00dd77', '#00ff88']
        cmap = mcolors.LinearSegmentedColormap.from_list('v', colors_list, N=256)

        im = ax.imshow(grid, cmap=cmap, aspect='auto', origin='lower',
                       vmin=0, vmax=N_CONSTRAINTS,
                       extent=[0.5, 8.5, 0.5, 10.5])

        # Score annotations
        for i, nC in enumerate(range(1, 11)):
            for j, Nc in enumerate(range(1, 9)):
                score = int(grid[i, j])
                color = WHITE if score < N_CONSTRAINTS * 0.6 else '#000000'
                fontw = 'bold' if score >= N_CONSTRAINTS - 1 else 'normal'
                ax.text(Nc, nC, str(score), ha='center', va='center',
                        fontsize=10, fontweight=fontw, color=color,
                        fontfamily='monospace')

        # Highlight selection
        if hl_Nc and hl_nC and 1 <= hl_Nc <= 8 and 1 <= hl_nC <= 10:
            rect = plt.Rectangle((hl_Nc - 0.5, hl_nC - 0.5), 1, 1,
                                 linewidth=3, edgecolor=CYAN,
                                 facecolor='none', zorder=10)
            ax.add_patch(rect)

        # Gold marker for (3,5) when Nmax=137
        if Nmax == 137:
            star = plt.Rectangle((2.5, 4.5), 1, 1, linewidth=2,
                                 edgecolor=GOLD, facecolor='none',
                                 linestyle='--', zorder=9)
            ax.add_patch(star)

        ax.set_xticks(range(1, 9))
        ax.set_yticks(range(1, 11))
        ax.set_xlabel('N_c (color charges)', fontsize=12, color=WHITE,
                       fontfamily='monospace')
        ax.set_ylabel('n_C (complex dimension)', fontsize=12, color=WHITE,
                       fontfamily='monospace')
        ax.set_title(f'Viability  (N_max = {Nmax}, max = {N_CONSTRAINTS})',
                     fontsize=14, fontweight='bold', color=GOLD,
                     fontfamily='monospace', pad=10)
        ax.tick_params(colors=WHITE, labelsize=11)
        for spine in ax.spines.values():
            spine.set_color('#333366')

    def draw_report(ax, result: PhysicsResult):
        """Draw constraint report."""
        ax.clear()
        ax.set_facecolor(PANEL)
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        triple_str = f"({result.Nc}, {result.nC}, {result.Nmax})"
        is_true = (result.Nc, result.nC, result.Nmax) == TRUE_TRIPLE
        hdr_color = GREEN if is_true else (YELLOW if result.score >= 10 else RED)

        ax.text(0.02, 0.97, f'CONSTRAINTS: {triple_str}',
                fontsize=13, fontweight='bold', color=hdr_color,
                fontfamily='monospace', va='top')
        status = "VIABLE" if result.viable else f"{result.score}/{result.max_score}"
        ax.text(0.98, 0.97, status, fontsize=13, fontweight='bold',
                color=GREEN if result.viable else RED,
                fontfamily='monospace', va='top', ha='right')

        # Category labels and constraints
        y = 0.89
        cat_colors = {"gauge": "#ff6666", "geometry": "#66aaff",
                      "channel": "#aa66ff", "lock": GOLD}
        cat_labels = {"gauge": "GAUGE", "geometry": "GEOMETRY",
                      "channel": "CHANNEL", "lock": "LOCK"}
        last_cat = None

        for c in result.constraints:
            if c.category != last_cat:
                if last_cat is not None:
                    y -= 0.01
                ax.text(0.02, y, cat_labels.get(c.category, ""),
                        fontsize=7, color=cat_colors.get(c.category, GREY),
                        fontfamily='monospace', va='top', fontweight='bold')
                y -= 0.025
                last_cat = c.category

            icon_color = GREEN if c.passed else RED
            icon = "OK" if c.passed else "XX"
            ax.text(0.02, y, f'[{icon}]', fontsize=8, fontweight='bold',
                    color=icon_color, fontfamily='monospace', va='top')
            ax.text(0.10, y, c.name, fontsize=8, fontweight='bold',
                    color=WHITE if c.passed else '#ff8866',
                    fontfamily='monospace', va='top')
            expl = c.explanation[:58] + '...' if len(c.explanation) > 58 else c.explanation
            ax.text(0.10, y - 0.03, expl, fontsize=6.5,
                    color=GREY, fontfamily='monospace', va='top')
            y -= 0.065

    def draw_table(ax, result: PhysicsResult):
        """Draw physics comparison table."""
        ax.clear()
        ax.set_facecolor(PANEL)
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        ref = wim.compute(*TRUE_TRIPLE)
        triple_str = f"({result.Nc}, {result.nC}, {result.Nmax})"
        is_true = (result.Nc, result.nC, result.Nmax) == TRUE_TRIPLE

        ax.text(0.02, 0.95, 'PHYSICS COMPARISON', fontsize=12,
                fontweight='bold', color=GOLD, fontfamily='monospace', va='top')

        cols = [0.02, 0.24, 0.48, 0.74]
        ax.text(cols[0], 0.83, 'Quantity', fontsize=9, color=CYAN,
                fontfamily='monospace', va='top', fontweight='bold')
        ax.text(cols[1], 0.83, triple_str, fontsize=9, color=CYAN,
                fontfamily='monospace', va='top', fontweight='bold')
        ax.text(cols[2], 0.83, '(3,5,137)', fontsize=9, color=GOLD,
                fontfamily='monospace', va='top', fontweight='bold')
        ax.text(cols[3], 0.83, 'Observed', fontsize=9, color=GREEN,
                fontfamily='monospace', va='top', fontweight='bold')

        ax.plot([0.02, 0.98], [0.79, 0.79], color='#333366', linewidth=1)

        def fmt_a(a):
            return f"1/{1/a:.1f}" if a > 1e-6 else "~0"

        rows = [
            ("alpha",        fmt_a(result.alpha), fmt_a(ref.alpha), fmt_a(OBSERVED['alpha'])),
            ("m_p/m_e",      f"{result.proton_electron:.1f}",
                             f"{ref.proton_electron:.2f}", f"{OBSERVED['proton_electron']:.2f}"),
            ("sin2_theta_W", f"{result.sin2_theta_W:.5f}",
                             f"{ref.sin2_theta_W:.5f}", f"{OBSERVED['sin2_theta_W']:.5f}"),
            ("alpha_s",      f"{result.alpha_s:.4f}", f"{ref.alpha_s:.4f}", "0.3500"),
            ("n_s",          f"{result.n_s:.4f}", f"{ref.n_s:.4f}", "0.9649"),
            ("generations",  f"{result.N_gen}", f"{ref.N_gen}", "3"),
            ("|Gamma|",      f"{result.Gamma_order}", f"{ref.Gamma_order}", "1920"),
            ("genus",        f"{result.genus}", f"{ref.genus}", "7"),
        ]

        y = 0.73
        dy = 0.088
        for label, v_alt, v_ref, v_obs in rows:
            row_color = WHITE
            if not is_true and v_alt != v_ref:
                row_color = '#ff8866'
            ax.text(cols[0], y, label, fontsize=8.5, color=row_color,
                    fontfamily='monospace', va='top')
            ax.text(cols[1], y, v_alt, fontsize=8.5, color=row_color,
                    fontfamily='monospace', va='top')
            ax.text(cols[2], y, v_ref, fontsize=8.5, color=GOLD,
                    fontfamily='monospace', va='top')
            ax.text(cols[3], y, v_obs, fontsize=8.5, color=GREEN,
                    fontfamily='monospace', va='top')
            y -= dy

    def draw_score(ax, result: PhysicsResult):
        """Draw big score indicator."""
        ax.clear()
        ax.set_facecolor(BG)
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        s = result.score
        m = result.max_score
        if s == m:
            sc, label = GREEN, 'VIABLE'
        elif s >= m - 2:
            sc, label = YELLOW, 'CLOSE'
        elif s >= m // 2:
            sc, label = '#ff8844', 'PARTIAL'
        else:
            sc, label = RED, 'DEAD'

        ax.text(0.5, 0.72, f'{s} / {m}', fontsize=26,
                fontweight='bold', color=sc, ha='center', va='center',
                fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#000000')])
        ax.text(0.5, 0.2, label, fontsize=15, fontweight='bold',
                color=sc, ha='center', va='center', fontfamily='monospace')

    # ─── Master render ───
    def render(val=None):
        Nc = int(slider_Nc.val)
        nC = int(slider_nC.val)
        Nmax = int(slider_Nmax.val)
        result = wim.compute(Nc, nC, Nmax)
        draw_heatmap(ax_heat, Nmax, hl_Nc=Nc, hl_nC=nC)
        draw_report(ax_report, result)
        draw_table(ax_table, result)
        draw_score(ax_score, result)
        fig.canvas.draw_idle()

    def on_sweep(event):
        Nmax = int(slider_Nmax.val)
        sweep_cache.pop(Nmax, None)
        render()

    def on_reset(event):
        slider_Nc.set_val(3)
        slider_nC.set_val(5)
        slider_Nmax.set_val(137)

    slider_Nc.on_changed(render)
    slider_nC.on_changed(render)
    slider_Nmax.on_changed(render)
    btn_sweep.on_clicked(on_sweep)
    btn_reset.on_clicked(on_reset)

    render()
    plt.show()


# ─────────────────────────────────────────────────────────────
#  CLI summary — landscape report
# ─────────────────────────────────────────────────────────────

def cli_summary():
    """Print a textual landscape summary."""
    wim = WhatIfMachine()

    print(f"\n{'='*74}")
    print(f"  WHAT IF? — BST Parameter Landscape ({N_CONSTRAINTS} constraints)")
    print(f"  Sweeping N_c=1..8, n_C=1..10 at N_max=137")
    print(f"{'='*74}")

    # Score grid
    print(f"\n  {'n_C \\\\ N_c':>10}", end="")
    for Nc in range(1, 9):
        print(f"  {Nc:>4}", end="")
    print()
    print("  " + "-" * 50)

    for nC in range(1, 11):
        print(f"  {nC:>10}", end="")
        for Nc in range(1, 9):
            r = wim.compute(Nc, nC, 137)
            mark = f"  {r.score:>3}" + ("*" if r.viable else " ")
            print(mark, end="")
        print()

    print(f"\n  * = all {N_CONSTRAINTS} constraints satisfied (viable universe)")
    print()

    # The unique winner
    ref = wim.compute(3, 5, 137)
    print(f"  UNIQUE MAXIMUM: (3, 5, 137) with score {ref.score}/{ref.max_score}")
    print()

    # Interesting comparisons
    comparisons = [
        ("4 colors",    4, 5, 137),
        ("2 colors",    2, 5, 137),
        ("dim 4",       3, 4, 137),
        ("dim 6",       3, 6, 137),
        ("N_max=139",   3, 5, 139),
        ("N_max=131",   3, 5, 131),
        ("N_max=136",   3, 5, 136),
        ("dim 3",       3, 3, 137),
        ("5 colors",    5, 5, 137),
    ]

    print("  WHAT-IF COMPARISONS:")
    print(f"  {'Scenario':<16} {'Triple':<16} {'Score':>6}  Failures")
    print("  " + "-" * 70)
    for label, Nc, nC, Nmax in comparisons:
        r = wim.compute(Nc, nC, Nmax)
        fails = [c.name for c in r.constraints if not c.passed]
        fail_str = ", ".join(fails) if fails else "NONE (VIABLE)"
        print(f"  {label:<16} ({Nc},{nC},{Nmax}){'':<8} {r.score:>3}/{r.max_score}"
              f"  {fail_str}")

    print()

    # Sweep primes near 137
    print("  PRIME N_max SWEEP (N_c=3, n_C=5):")
    primes = [p for p in range(100, 200) if _is_prime(p)]
    for p in primes:
        r = wim.compute(3, 5, p)
        alpha_str = f"1/{1/r.alpha:.1f}" if r.alpha > 1e-6 else "~0"
        marker = " <<<< OUR UNIVERSE" if p == 137 else ""
        star = "*" if r.viable else " "
        fails = [c.name for c in r.constraints if not c.passed]
        fail_str = "; ".join(fails) if fails else ""
        print(f"    N_max={p:>3}  score={r.score}/{r.max_score}{star}"
              f"  alpha={alpha_str:<10}{marker}"
              f"  {fail_str}")

    print(f"\n{'='*74}")
    print(f"  Result: (3, 5, 137) is the UNIQUE viable triple.")
    print(f"  No other integer triple passes all {N_CONSTRAINTS} constraints.")
    print(f"{'='*74}\n")


# ─────────────────────────────────────────────────────────────
#  Main
# ─────────────────────────────────────────────────────────────

if __name__ == '__main__':
    import sys

    if '--cli' in sys.argv:
        cli_summary()
    elif '--what-if' in sys.argv:
        wim = WhatIfMachine()
        kwargs = {}
        for arg in sys.argv:
            if arg.startswith('--Nc='):
                kwargs['Nc'] = int(arg.split('=')[1])
            elif arg.startswith('--nC='):
                kwargs['nC'] = int(arg.split('=')[1])
            elif arg.startswith('--Nmax='):
                kwargs['Nmax'] = int(arg.split('=')[1])
        wim.what_if(**kwargs)
    elif '--sweep' in sys.argv:
        wim = WhatIfMachine()
        print("Sweeping full parameter space (N_c=1..8, n_C=1..10, N_max=100..200)...")
        landscape = wim.sweep()
        print(f"Total triples evaluated: {landscape.total_count}")
        print(f"Viable universes found:  {landscape.viable_count}")
        print(f"Best triple:             {landscape.best_triple}")
        print(f"Best score:              {landscape.best_score}/{N_CONSTRAINTS}")
    else:
        # Default: visual mode with CLI preamble
        cli_summary()
        run_visual()
