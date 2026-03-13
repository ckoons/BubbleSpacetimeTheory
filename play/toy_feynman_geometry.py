#!/usr/bin/env python3
"""
THE FEYNMAN BRIDGE
==================
Feynman diagrams as substrate topology: loops = S¹ windings.

QED computes the electron's magnetic moment by summing Feynman
diagrams loop by loop. Each loop adds one power of α/π and
improves precision by ~2-3 digits. BST says these loops ARE
literal windings around the S¹ fiber of spacetime.

    from toy_feynman_geometry import FeynmanGeometry
    fg = FeynmanGeometry()
    fg.loop_contribution(1)        # Schwinger's α/(2π)
    fg.cumulative(3)               # through 3 loops
    fg.precision_table()           # all 5 loops
    fg.bst_interpretation(2)       # what loop 2 means geometrically
    fg.proton_moment()             # QCD: one formula, no diagrams
    fg.qed_vs_qcd()                # perturbative vs geometric
    fg.alpha_origin()              # where 1/137 comes from
    fg.summary()                   # the punchline

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np

# ═══════════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════════

ALPHA = 1.0 / 137.035999177       # fine structure constant (2023 CODATA)
ALPHA_OVER_PI = ALPHA / np.pi      # expansion parameter

# BST integers
N_c = 3
n_C = 5
genus = n_C + 2       # = 7
C2 = n_C + 1          # = 6
N_max = 137

# QED coefficients: a_e = Σ A_n × (α/π)^n
# Each tuple: (order, coefficient, formula_str, reference, n_diagrams, exact?)
QED_COEFFS = [
    (1,  0.5,                'α/(2π)',
     'Schwinger 1948',        1,     True),
    (2, -0.328478965579,     '−0.3285 (α/π)²',
     'Petermann 1957',        7,     True),
    (3,  1.181241456587,     '+1.1812 (α/π)³',
     'Laporta & Remiddi 1996', 72,   True),
    (4, -1.912245764,        '−1.9122 (α/π)⁴',
     'Aoyama et al. 2015',   891,   True),
    (5,  6.675,              '+6.675 (α/π)⁵',
     'Aoyama et al. 2019',   12672, False),
]

# Experimental electron anomalous magnetic moment
A_E_EXP = 0.00115965218091   # Fan et al. 2023 (Harvard)

# Proton magnetic moment
MU_P_EXP = 2.79284735        # nuclear magnetons
MU_P_BST = 14.0 / 5.0        # N_gluon × α_s = 8 × 7/20
MU_N_EXP = -1.91304273       # neutron, nuclear magnetons


# ═══════════════════════════════════════════════════════════════════
# THE FEYNMAN BRIDGE CLASS
# ═══════════════════════════════════════════════════════════════════

class FeynmanGeometry:
    """
    The Feynman Bridge: QED diagrams as S¹ fiber topology.

    Each Feynman loop is one winding around the S¹ fiber of the
    spacetime substrate S² × S¹. The expansion parameter α/π is the
    coupling constant divided by the winding circumference. Signs
    alternate because successive windings have opposite phase
    orientation on S¹.

    QED: 12,672 diagrams → 12 digits of precision (perturbative).
    QCD: 1 formula → 3 digits of precision (geometric, exact).
    Same substrate. Different regime.
    """

    def __init__(self, quiet=False):
        self._cumulative = []
        total = 0.0
        for order, coeff, _, _, _, _ in QED_COEFFS:
            total += coeff * ALPHA_OVER_PI**order
            self._cumulative.append(total)
        if not quiet:
            self._print_header()

    def _print_header(self):
        print("=" * 68)
        print("  THE FEYNMAN BRIDGE")
        print("  Feynman diagrams as S¹ fiber windings on D_IV⁵")
        print(f"  α = 1/{1/ALPHA:.6f}   α/π = {ALPHA_OVER_PI:.10f}")
        print("=" * 68)

    def _matching_digits(self, n_loops: int) -> int:
        """Count consecutive matching characters from the start."""
        exp_s = f"{A_E_EXP:.15f}"
        bst_s = f"{self._cumulative[n_loops - 1]:.15f}"
        count = 0
        for e, b in zip(exp_s, bst_s):
            if e == b:
                count += 1
            else:
                break
        return count

    def _sig_figs(self, n_loops: int) -> int:
        """Approximate significant figures of agreement."""
        bst = self._cumulative[n_loops - 1]
        if bst == 0:
            return 0
        rel_err = abs(bst - A_E_EXP) / A_E_EXP
        if rel_err == 0:
            return 15
        return max(0, int(-np.log10(rel_err)))

    # ─── Loop contribution ───

    def loop_contribution(self, n: int) -> dict:
        """
        The nth loop contribution to the electron g-2.
        """
        if n < 1 or n > 5:
            print(f"  Loop order must be 1-5 (got {n})")
            return {}

        order, coeff, formula, ref, n_diag, exact = QED_COEFFS[n - 1]
        aopi_n = ALPHA_OVER_PI**order
        contrib = coeff * aopi_n

        print()
        print(f"  LOOP {n} CONTRIBUTION")
        print(f"  ═══════════════════════════════════")
        print(f"  Coefficient A_{n} = {coeff:+.12f}"
              f"{'  (exact)' if exact else '  (±numerical)'}")
        print(f"  Formula: {formula}")
        print(f"  Reference: {ref}")
        print(f"  (α/π)^{n} = {aopi_n:.6e}")
        print(f"  Contribution: {contrib:+.6e}")
        print(f"  Feynman diagrams at this order: {n_diag:,}")
        print()
        print(f"  BST: this is winding #{n} around the S¹ fiber.")
        if coeff > 0:
            print(f"  Sign is POSITIVE — constructive winding phase.")
        else:
            print(f"  Sign is NEGATIVE — destructive winding phase.")
        print(f"  Signs alternate: +, −, +, −, + (winding orientation).")

        return {
            'order': n,
            'coefficient': coeff,
            'contribution': contrib,
            'n_diagrams': n_diag,
            'exact': exact,
            'reference': ref,
        }

    # ─── Cumulative ───

    def cumulative(self, n: int) -> dict:
        """
        Electron g-2 through n loops.
        Shows running total and matching digits.
        """
        if n < 1 or n > 5:
            print(f"  Loop order must be 1-5 (got {n})")
            return {}

        bst_val = self._cumulative[n - 1]
        n_match = self._matching_digits(n)
        sig = self._sig_figs(n)
        rel_err = abs(bst_val - A_E_EXP) / A_E_EXP

        total_diagrams = sum(d for _, _, _, _, d, _ in QED_COEFFS[:n])

        print()
        print(f"  CUMULATIVE THROUGH {n} LOOP{'S' if n > 1 else ''}")
        print(f"  ═══════════════════════════════════")
        print(f"  Experiment: {A_E_EXP:.15f}")
        print(f"  BST ({n}-loop): {bst_val:.15f}")
        print()

        # Show digit-by-digit comparison
        exp_s = f"{A_E_EXP:.15f}"
        bst_s = f"{bst_val:.15f}"
        match_line = ""
        for i in range(len(exp_s)):
            if i < n_match:
                match_line += "█"
            else:
                match_line += "·"
        print(f"  Match:      {match_line}")
        print()
        print(f"  Matching characters: {n_match}")
        print(f"  Significant figures: ~{sig}")
        print(f"  Relative error: {rel_err:.2e}")
        print(f"  Total diagrams computed: {total_diagrams:,}")

        return {
            'n_loops': n,
            'value': bst_val,
            'experiment': A_E_EXP,
            'matching_chars': n_match,
            'sig_figs': sig,
            'rel_error': rel_err,
            'total_diagrams': total_diagrams,
        }

    # ─── Precision table ───

    def precision_table(self) -> list:
        """All 5 loops: coefficients, cumulative, precision growth."""
        print()
        print("  THE PRECISION LADDER")
        print("  ═══════════════════════════════════════════════════════")
        print()
        print(f"  {'Loop':>4} {'Coefficient':>14} {'Diagrams':>10} "
              f"{'Cumulative':>18} {'Sig figs':>8} {'Rel err':>10}")
        print(f"  {'─'*4} {'─'*14} {'─'*10} "
              f"{'─'*18} {'─'*8} {'─'*10}")

        results = []
        for i, (order, coeff, _, ref, n_diag, _) in enumerate(QED_COEFFS):
            bst_val = self._cumulative[i]
            sig = self._sig_figs(i + 1)
            rel_err = abs(bst_val - A_E_EXP) / A_E_EXP
            print(f"  {order:4d} {coeff:+14.6f} {n_diag:10,} "
                  f"{bst_val:18.15f} {'~' + str(sig):>8} {rel_err:10.2e}")
            results.append({
                'order': order, 'coefficient': coeff,
                'n_diagrams': n_diag, 'cumulative': bst_val,
                'sig_figs': sig, 'rel_error': rel_err,
            })

        print()
        print(f"  Experiment: {A_E_EXP:.15f}")
        print()
        print(f"  Total diagrams: {sum(r['n_diagrams'] for r in results):,}")
        print(f"  Each loop adds ~2-3 significant figures.")
        print(f"  Signs alternate: +, −, +, −, + (S¹ winding phases).")

        return results

    # ─── BST interpretation ───

    def bst_interpretation(self, n: int) -> dict:
        """
        What the nth Feynman loop means in BST geometry.
        """
        if n < 1 or n > 5:
            print(f"  Loop order must be 1-5 (got {n})")
            return {}

        _, coeff, _, _, n_diag, _ = QED_COEFFS[n - 1]
        sign = "positive" if coeff > 0 else "negative"

        print()
        print(f"  BST INTERPRETATION — LOOP {n}")
        print(f"  ═══════════════════════════════════════")
        print()
        print(f"  QED picture:")
        print(f"    {n_diag:,} Feynman diagram{'s' if n_diag > 1 else ''}")
        print(f"    Each is a virtual photon path")
        print(f"    Sum gives coefficient A_{n} = {coeff:+.6f}")
        print()
        print(f"  BST picture:")
        print(f"    Winding #{n} around the S¹ fiber")
        print(f"    Phase orientation: {sign} (alternates with winding)")
        print(f"    The {n_diag:,} diagrams are {n_diag:,} geodesic paths")
        print(f"    through D_IV⁵ that complete {n} S¹ windings")
        print()

        if n == 1:
            print(f"  The Schwinger term: one photon traverses S¹ once.")
            print(f"  α/(2π) = coupling / circumference.")
            print(f"  This IS the statement that the S¹ fiber exists.")
        elif n == 2:
            print(f"  Second winding: opposite phase → negative coefficient.")
            print(f"  The 7 diagrams are 7 distinct geodesic paths")
            print(f"  that complete two S¹ windings. Their amplitudes")
            print(f"  interfere to give A₂ = {coeff:+.6f}.")
        elif n == 3:
            print(f"  Third winding: constructive again → positive.")
            print(f"  72 geodesic paths. The coefficient magnitude grows")
            print(f"  (|A₃| > |A₂|), signaling the asymptotic nature")
            print(f"  of the winding series.")
        elif n == 4:
            print(f"  Fourth winding: destructive → negative.")
            print(f"  891 diagrams. Computed numerically (Kinoshita group,")
            print(f"  decades of work). Confirmed by Volkov (2019).")
        elif n == 5:
            print(f"  Fifth winding: constructive → positive.")
            print(f"  12,672 diagrams. The frontier of perturbative QED.")
            print(f"  |A₅| = 6.675 — growing magnitudes signal the")
            print(f"  series is asymptotic (diverges at high order).")
            print(f"  In BST: higher windings become topologically")
            print(f"  unstable on S¹. The substrate has finite capacity.")

        return {
            'order': n,
            'qed_diagrams': n_diag,
            'bst_windings': n,
            'sign': sign,
            'coefficient': coeff,
        }

    # ─── Proton magnetic moment ───

    def proton_moment(self) -> dict:
        """
        QCD regime: one formula, no diagrams needed.

        BST: μ_p/μ_N = N_gluon × α_s = 8 × 7/20 = 14/5 = 2.800
        Experiment: 2.79285 (0.26%)

        No Feynman series. No 12,672 diagrams. One line of geometry.
        """
        n_gluon = N_c**2 - 1  # = 8
        alpha_s = (n_C + 2) / (4 * n_C)  # = 7/20 = 0.35
        mu_p_bst = n_gluon * alpha_s  # = 56/20 = 14/5 = 2.8
        err_pct = abs(mu_p_bst - MU_P_EXP) / MU_P_EXP * 100

        # Decomposition
        kappa_p = mu_p_bst - 1.0  # anomalous part = 9/5
        kappa_formula = f"N_c²/n_C = {N_c}²/{n_C} = {N_c**2}/{n_C}"

        print()
        print("  PROTON MAGNETIC MOMENT — THE QCD REGIME")
        print("  ═══════════════════════════════════════════════════")
        print()
        print(f"  QED approach: IMPOSSIBLE.")
        print(f"    α_s ≈ 0.35 at proton scale — too large for")
        print(f"    perturbation theory. Feynman series diverges.")
        print(f"    Lattice QCD gives ~1-2% after years of computing.")
        print()
        print(f"  BST approach: ONE FORMULA.")
        print(f"    μ_p/μ_N = N_gluon × α_s(m_p)")
        print(f"            = (N_c²−1) × (n_C+2)/(4n_C)")
        print(f"            = {n_gluon} × {alpha_s}")
        print(f"            = {n_gluon * alpha_s:.1f}")
        print(f"            = 14/5")
        print()
        print(f"  Decomposition:")
        print(f"    Dirac value:     1 μ_N (point particle)")
        print(f"    Anomalous part:  {kappa_formula} = {kappa_p:.1f} μ_N")
        print(f"    Total:           14/5 = {mu_p_bst:.4f} μ_N")
        print(f"    Experiment:      {MU_P_EXP:.8f} μ_N")
        print(f"    Error:           {err_pct:.2f}%")
        print()
        print(f"  The proton's excess moment comes from 8 gluon modes,")
        print(f"  each contributing α_s = 7/20 of a nuclear magneton.")
        print(f"  No diagrams. No series. Geometry gives the answer.")

        return {
            'mu_p_bst': mu_p_bst,
            'mu_p_exp': MU_P_EXP,
            'error_pct': err_pct,
            'n_gluon': n_gluon,
            'alpha_s': alpha_s,
            'anomalous_moment': kappa_p,
        }

    # ─── QED vs QCD comparison ───

    def qed_vs_qcd(self) -> dict:
        """
        Same substrate, different regime.

        QED: α small → series converges → 12 digits from 13,643 diagrams.
        QCD: α_s large → series diverges → BST gives exact geometry.
        """
        total_diag = sum(d for _, _, _, _, d, _ in QED_COEFFS)
        sig_qed = self._sig_figs(5)
        err_qcd = abs(MU_P_BST - MU_P_EXP) / MU_P_EXP * 100
        sig_qcd = max(0, int(-np.log10(err_qcd / 100)))

        print()
        print("  QED vs QCD — SAME SUBSTRATE, DIFFERENT REGIME")
        print("  ═══════════════════════════════════════════════════")
        print()
        print(f"  {'':20} {'QED (electron g-2)':>22} {'QCD (proton μ)':>22}")
        print(f"  {'─'*20} {'─'*22} {'─'*22}")
        print(f"  {'Coupling':20} {'α = 1/137':>22} {'α_s = 7/20':>22}")
        print(f"  {'Regime':20} {'Perturbative':>22} {'Non-perturbative':>22}")
        print(f"  {'Feynman diagrams':20} {total_diag:>21,} {'∞ (diverges)':>22}")
        print(f"  {'BST formula':20} {'Σ A_n(α/π)^n':>22} {'N_gluon × α_s':>22}")
        print(f"  {'Precision':20} {'~' + str(sig_qed) + ' sig figs':>22} "
              f"{'~' + str(sig_qcd) + ' sig figs':>22}")
        print(f"  {'Error':20} {abs(self._cumulative[4] - A_E_EXP)/A_E_EXP:>22.2e} "
              f"{err_qcd/100:>22.2e}")
        print()
        print(f"  WHY THE DIFFERENCE:")
        print(f"  Both live on the same substrate (D_IV⁵ with S¹ fiber).")
        print(f"  When the coupling is small (α = 1/137), the Taylor")
        print(f"  expansion around flat S¹ converges — each loop adds")
        print(f"  precision. When the coupling is large (α_s = 0.35),")
        print(f"  the Taylor expansion diverges — you need the exact")
        print(f"  geometric answer directly.")
        print()
        print(f"  BST has BOTH: the exact geometry (works always) and")
        print(f"  the perturbative expansion (works when α is small).")
        print(f"  They agree because they compute the same thing")
        print(f"  from different directions.")

        return {
            'qed_diagrams': total_diag,
            'qed_sig_figs': sig_qed,
            'qcd_sig_figs': sig_qcd,
            'alpha_em': ALPHA,
            'alpha_s': 7 / 20,
        }

    # ─── Alpha origin ───

    def alpha_origin(self) -> dict:
        """
        Where 1/137 comes from.

        BST: α = (9/8π⁴)(π⁵/1920)^{1/4} — the Bergman volume ratio.
        """
        alpha_bst = (9.0 / (8 * np.pi**4)) * (np.pi**5 / 1920)**0.25
        err = abs(alpha_bst - ALPHA) / ALPHA * 100

        print()
        print("  THE ORIGIN OF α = 1/137")
        print("  ═══════════════════════════════════════")
        print()
        print(f"  BST formula:")
        print(f"    α = (9/8π⁴) × (π⁵/1920)^(1/4)")
        print()
        print(f"  Where:")
        print(f"    9 = N_c² (color degrees of freedom)")
        print(f"    8π⁴ = normalization of S⁴ × S¹ Shilov boundary")
        print(f"    π⁵/1920 = Vol(D_IV⁵) in Bergman metric")
        print(f"    1920 = |Γ| = |S₅ × (Z₂)⁴| (Hua's group)")
        print()
        print(f"  BST:        α = {alpha_bst:.12f}")
        print(f"  Experiment: α = {ALPHA:.12f}")
        print(f"  Agreement: {err:.4f}%")
        print()
        print(f"  α is not a free parameter. It is the ratio of two")
        print(f"  volumes on D_IV⁵ — the electromagnetic coupling")
        print(f"  between the photon and the S¹ geometric fiber.")
        print(f"  Every Feynman loop is powered by this one number.")

        return {
            'alpha_bst': alpha_bst,
            'alpha_exp': ALPHA,
            'error_pct': err,
        }

    # ─── Summary ───

    def summary(self) -> dict:
        """The Feynman Bridge in one box."""
        total_diag = sum(d for _, _, _, _, d, _ in QED_COEFFS)

        print()
        print("  ╔═══════════════════════════════════════════════════════╗")
        print("  ║         THE FEYNMAN BRIDGE — SUMMARY                 ║")
        print("  ╠═══════════════════════════════════════════════════════╣")
        print("  ║                                                       ║")
        print("  ║  Every Feynman loop is one winding around S¹.        ║")
        print("  ║  Every vertex is a commitment event.                  ║")
        print("  ║  Every propagator is a geodesic on D_IV⁵.            ║")
        print("  ║                                                       ║")
        print(f"  ║  QED: {total_diag:,} diagrams → ~{self._sig_figs(5)}"
              f" digits          ║")
        print(f"  ║  QCD: 1 formula (14/5) → 0.26%                      ║")
        print("  ║                                                       ║")
        print("  ║  Signs alternate (+−+−+) because successive          ║")
        print("  ║  S¹ windings have opposite phase orientation.         ║")
        print("  ║                                                       ║")
        print("  ║  The diagrams aren't abstract squiggles.              ║")
        print("  ║  They're counting substrate topology.                 ║")
        print("  ║                                                       ║")
        print("  ╚═══════════════════════════════════════════════════════╝")

        return {
            'total_diagrams': total_diag,
            'qed_precision': self._sig_figs(5),
            'qcd_error': 0.26,
            'key_insight': 'Feynman loops = S¹ windings',
        }

    # ─── Visualization helpers ───

    def _draw_photon_arc(self, ax, x_left, x_right, y_base,
                         height=0.25, n_waves=8, color='#00ccff',
                         lw=2, alpha_val=0.9):
        """Draw a wavy semicircular photon propagator."""
        t = np.linspace(0, np.pi, 300)
        cx = (x_left + x_right) / 2
        rx = (x_right - x_left) / 2

        x_arc = cx + rx * np.cos(np.pi - t)
        y_arc = y_base + height * np.sin(t)

        # Tangent direction
        dx_dt = rx * np.sin(np.pi - t)
        dy_dt = height * np.cos(t)
        ds = np.sqrt(dx_dt**2 + dy_dt**2)
        ds = np.where(ds < 1e-10, 1.0, ds)

        # Normal (perpendicular to tangent, outward)
        nx = -dy_dt / ds
        ny = dx_dt / ds

        amp = min(rx, height) * 0.15
        wave = amp * np.sin(n_waves * t)

        ax.plot(x_arc + wave * nx, y_arc + wave * ny,
                color=color, lw=lw, alpha=alpha_val, zorder=3)

    def _draw_feynman_panel(self, ax, n_loops):
        """Draw accumulated Feynman diagram for n loops."""
        ax.set_facecolor('#0d0d24')
        ax.set_xlim(-0.05, 1.05)
        ax.set_ylim(-0.15, 1.0)
        ax.axis('off')

        y_line = 0.18
        # Electron line
        ax.plot([0.02, 0.98], [y_line, y_line],
                color='#ffcc44', lw=2.5, zorder=2)
        # Arrow
        ax.annotate('', xy=(0.98, y_line), xytext=(0.92, y_line),
                    arrowprops=dict(arrowstyle='->', color='#ffcc44', lw=2))
        ax.text(0.0, y_line - 0.07, 'e⁻', color='#ffcc44', fontsize=11,
                ha='center', fontfamily='monospace')
        ax.text(1.0, y_line - 0.07, 'e⁻', color='#ffcc44', fontsize=11,
                ha='center', fontfamily='monospace')

        # Photon arcs
        colors = ['#00ccff', '#00ff88', '#ffcc44', '#ff8844', '#ff4488']
        margin = 0.08
        span = 0.84
        loop_w = span / max(n_loops, 1)

        for i in range(n_loops):
            x_left = margin + i * loop_w + loop_w * 0.1
            x_right = margin + (i + 1) * loop_w - loop_w * 0.1
            c = colors[i % len(colors)]

            # Vertices
            ax.plot(x_left, y_line, 'o', color='#ff4444',
                    markersize=7, zorder=10)
            ax.plot(x_right, y_line, 'o', color='#ff4444',
                    markersize=7, zorder=10)

            # Photon arc
            h = 0.22 + 0.04 * (i % 2)
            self._draw_photon_arc(ax, x_left, x_right, y_line,
                                  height=h, color=c, n_waves=6)

            # Label
            ax.text((x_left + x_right) / 2, y_line + h + 0.04,
                    f'γ_{i+1}', color=c, fontsize=8, ha='center',
                    fontfamily='monospace')

        # Title and info
        ax.set_title(f'QED: {n_loops}-LOOP ELECTRON g−2',
                     color='#00ccff', fontsize=13, fontweight='bold',
                     fontfamily='monospace', pad=10)

        _, coeff, formula, ref, n_diag, _ = QED_COEFFS[n_loops - 1]
        total_diag = sum(d for _, _, _, _, d, _ in QED_COEFFS[:n_loops])

        ax.text(0.5, 0.88,
                f'Loop {n_loops}: A_{n_loops} = {coeff:+.6f}   ({ref})',
                color='#ffffff', fontsize=10, ha='center',
                fontfamily='monospace', transform=ax.transAxes)
        ax.text(0.5, 0.80,
                f'{n_diag:,} diagrams at order {n_loops}  ·  '
                f'{total_diag:,} total',
                color='#888888', fontsize=9, ha='center',
                fontfamily='monospace', transform=ax.transAxes)

    def _draw_bst_panel(self, ax, n_loops):
        """Draw S¹ fiber with n windings."""
        ax.set_facecolor('#0d0d24')
        ax.set_xlim(-1.8, 1.8)
        ax.set_ylim(-1.8, 1.8)
        ax.set_aspect('equal')
        ax.axis('off')

        # S¹ base circle
        theta = np.linspace(0, 2 * np.pi, 200)
        ax.plot(np.cos(theta), np.sin(theta),
                color='#333366', lw=3, zorder=1)
        ax.text(0, 0, 'S¹', color='#444466', fontsize=28,
                ha='center', va='center', fontfamily='monospace',
                fontweight='bold')

        # Windings
        colors = ['#00ccff', '#00ff88', '#ffcc44', '#ff8844', '#ff4488']
        for i in range(n_loops):
            r = 1.0 + (i + 1) * 0.1
            offset = i * 0.4
            theta_w = np.linspace(offset, offset + 2 * np.pi, 200)
            c = colors[i % len(colors)]

            ax.plot(r * np.cos(theta_w), r * np.sin(theta_w),
                    color=c, lw=2.5, alpha=0.85, zorder=2 + i)

            # Arrowhead at end
            end = offset + 2 * np.pi - 0.15
            ax.annotate('',
                        xy=(r * np.cos(end + 0.15),
                            r * np.sin(end + 0.15)),
                        xytext=(r * np.cos(end),
                                r * np.sin(end)),
                        arrowprops=dict(arrowstyle='->', color=c,
                                        lw=2.5))

            # Label
            lab_angle = offset + np.pi * 0.7
            lr = r + 0.22
            sign = '+' if QED_COEFFS[i][1] > 0 else '−'
            ax.text(lr * np.cos(lab_angle), lr * np.sin(lab_angle),
                    f'n={i+1} ({sign})', color=c, fontsize=9,
                    ha='center', va='center', fontfamily='monospace',
                    fontweight='bold')

        # Title
        ax.set_title(
            f'BST: {n_loops} WINDING{"S" if n_loops > 1 else ""} ON S¹',
            color='#ff4444', fontsize=13, fontweight='bold',
            fontfamily='monospace', pad=10)

        # Annotations
        ax.text(0, -1.6,
                'Each loop = one S¹ winding\n'
                'Vertices = commitment events\n'
                'Propagators = D_IV⁵ geodesics',
                color='#666688', fontsize=8, ha='center',
                fontfamily='monospace')

    def _draw_precision_panel(self, ax, n_loops):
        """Draw digit-by-digit precision comparison."""
        ax.set_facecolor('#0d0d24')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        bst_val = self._cumulative[n_loops - 1]
        exp_s = f"{A_E_EXP:.15f}"
        bst_s = f"{bst_val:.15f}"
        n_match = self._matching_digits(n_loops)
        sig = self._sig_figs(n_loops)

        # Title
        ax.text(0.5, 0.92, 'PRECISION — DIGITS MATCHING EXPERIMENT',
                color='#00ff44', fontsize=11, fontweight='bold',
                ha='center', fontfamily='monospace')

        # Experiment label and value
        ax.text(0.02, 0.70, 'Experiment:', color='#888888',
                fontsize=9, fontfamily='monospace')
        x0 = 0.16
        cw = 0.038
        for i, ch in enumerate(exp_s[:18]):
            ax.text(x0 + i * cw, 0.70, ch, color='#ffffff',
                    fontsize=14, fontfamily='monospace',
                    fontweight='bold', ha='center')

        # BST label and value with color coding
        ax.text(0.02, 0.42, f'BST ({n_loops}-loop):', color='#888888',
                fontsize=9, fontfamily='monospace')
        for i, ch in enumerate(bst_s[:18]):
            if i < n_match:
                color = '#00ff44'
            elif i < len(exp_s):
                color = '#ff4444'
            else:
                color = '#444444'
            ax.text(x0 + i * cw, 0.42, ch, color=color,
                    fontsize=14, fontfamily='monospace',
                    fontweight='bold', ha='center')

        # Stats
        ax.text(0.85, 0.70, f'~{sig} sig figs',
                color='#00ff44', fontsize=12, fontweight='bold',
                ha='center', fontfamily='monospace')

        total_diag = sum(d for _, _, _, _, d, _ in QED_COEFFS[:n_loops])
        ax.text(0.85, 0.50, f'{total_diag:,} diagrams',
                color='#888888', fontsize=10, ha='center',
                fontfamily='monospace')

        # QCD contrast
        ax.text(0.5, 0.12,
                f'QCD contrast: μ_p = 14/5 = {MU_P_BST:.1f}  '
                f'(exp: {MU_P_EXP:.5f})  0.26%  — ONE formula, '
                f'ZERO diagrams',
                color='#ff8844', fontsize=9, ha='center',
                fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3',
                          facecolor='#1a1a0d', edgecolor='#ff8844',
                          alpha=0.8))

    # ─── Main visualization ───

    def show(self):
        """Launch the interactive 3-panel visualization with slider."""
        try:
            import matplotlib
            matplotlib.use('TkAgg')
            import matplotlib.pyplot as plt
            from matplotlib.widgets import Slider
        except ImportError:
            print("matplotlib not available. Use text API.")
            return

        fig = plt.figure(figsize=(18, 11), facecolor='#0a0a1a')
        if fig.canvas.manager:
            fig.canvas.manager.set_window_title(
                'BST Toy 36 — The Feynman Bridge')

        fig.text(0.5, 0.97, 'THE FEYNMAN BRIDGE',
                 fontsize=24, fontweight='bold', color='#00ccff',
                 ha='center', fontfamily='monospace')
        fig.text(0.5, 0.94,
                 'Feynman diagrams as S¹ fiber windings  ·  '
                 'loops = topology',
                 fontsize=10, color='#668899', ha='center',
                 fontfamily='monospace')
        fig.text(0.5, 0.015,
                 'Copyright (c) 2026 Casey Koons — Demonstration Only',
                 fontsize=8, color='#334455', ha='center',
                 fontfamily='monospace')

        # Panels
        ax_feynman = fig.add_axes([0.03, 0.28, 0.45, 0.60])
        ax_bst = fig.add_axes([0.52, 0.28, 0.45, 0.60])
        ax_digits = fig.add_axes([0.03, 0.08, 0.94, 0.16])

        # Slider
        ax_slider = fig.add_axes([0.15, 0.035, 0.70, 0.02])
        slider = Slider(ax_slider, 'Loop Order', 1, 5,
                        valinit=1, valstep=1, color='#00ccff')
        ax_slider.set_facecolor('#0d0d24')

        fg = self  # capture for closure

        def draw_state(n):
            ax_feynman.clear()
            ax_bst.clear()
            ax_digits.clear()
            fg._draw_feynman_panel(ax_feynman, n)
            fg._draw_bst_panel(ax_bst, n)
            fg._draw_precision_panel(ax_digits, n)
            fig.canvas.draw_idle()

        slider.on_changed(lambda val: draw_state(int(val)))
        draw_state(1)

        plt.show(block=False)


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    fg = FeynmanGeometry()

    print()
    print("  What would you like to explore?")
    print("  1) Single loop contribution")
    print("  2) Cumulative through N loops")
    print("  3) Full precision table")
    print("  4) BST interpretation of a loop")
    print("  5) Proton magnetic moment (QCD)")
    print("  6) QED vs QCD comparison")
    print("  7) Origin of α = 1/137")
    print("  8) Full analysis + visualization")
    print()

    try:
        choice = input("  Choice [1-8]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = '8'

    if choice == '1':
        try:
            n = int(input("  Loop order [1-5]: ").strip())
        except (EOFError, KeyboardInterrupt, ValueError):
            n = 1
        fg.loop_contribution(n)
    elif choice == '2':
        try:
            n = int(input("  Through N loops [1-5]: ").strip())
        except (EOFError, KeyboardInterrupt, ValueError):
            n = 3
        fg.cumulative(n)
    elif choice == '3':
        fg.precision_table()
    elif choice == '4':
        try:
            n = int(input("  Loop order [1-5]: ").strip())
        except (EOFError, KeyboardInterrupt, ValueError):
            n = 1
        fg.bst_interpretation(n)
    elif choice == '5':
        fg.proton_moment()
    elif choice == '6':
        fg.qed_vs_qcd()
    elif choice == '7':
        fg.alpha_origin()
    elif choice == '8':
        fg.precision_table()
        fg.proton_moment()
        fg.qed_vs_qcd()
        fg.alpha_origin()
        fg.summary()
        try:
            fg.show()
            input("\n  Press Enter to close...")
        except Exception:
            pass
    else:
        fg.summary()


if __name__ == '__main__':
    main()
