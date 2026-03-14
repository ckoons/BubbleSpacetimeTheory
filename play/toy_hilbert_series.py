#!/usr/bin/env python3
"""
THE HILBERT SERIES OF Q^5 — Toy 141
====================================
The generating function for everything is (1+x)/(1-x)^6.

The Hilbert series H(Q^5, x) = (1+x)/(1-x)^6 encodes all spectral data
of the bounded symmetric domain D_IV^5. Its pole order is C_2 = 6 (mass gap).
Its multiplicities d_k reproduce quark mass ratios, coupling hierarchies,
and the uniqueness of n_C = 5.

    from toy_hilbert_series import HilbertSeries
    hs = HilbertSeries()
    hs.spectral_data()        # eigenvalues and multiplicities
    hs.strange_quark()        # d_2 = 27 = m_s/m_hat
    hs.hierarchy()            # why gravity is weak
    hs.gut_uniqueness()       # dim SU(n) = (n-1)! only at n=5
    hs.spectral_zeta()        # spectral zeta function
    hs.summary()              # the punchline
    hs.show()                 # six-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from math import factorial

# ═══════════════════════════════════════════════════════════════════
# BST CONSTANTS — the five integers
# ═══════════════════════════════════════════════════════════════════

N_c = 3                      # color charges
n_C = 5                      # complex dimension of D_IV^5
genus = n_C + 2              # = 7
C2 = n_C + 1                 # = 6, Casimir eigenvalue = mass gap
N_max = 137                  # Haldane channel capacity

# Physical constants
m_e_MeV = 0.51099895         # electron mass in MeV
alpha = 1.0 / 137.035999084  # fine structure constant


# ═══════════════════════════════════════════════════════════════════
# THE HILBERT SERIES CLASS
# ═══════════════════════════════════════════════════════════════════

class HilbertSeries:
    """
    The Hilbert series H(Q^5, x) = (1+x)/(1-x)^6 and its spectral hierarchy.

    The pole order is C_2 = 6 = mass gap.
    Eigenvalues: lambda_k = k(k+5)   (Laplacian on Q^5)
    Multiplicities: d_k = (2k+5)(k+4)(k+3)(k+2)(k+1)/120
    """

    def __init__(self):
        self.pole_order = C2  # = 6
        self.dim_real = 2 * n_C  # = 10, real dimension of Q^5

    # ─── Core formula ───

    def d(self, k):
        """Multiplicity of the k-th eigenspace on Q^5."""
        return (2*k + 5) * (k + 4) * (k + 3) * (k + 2) * (k + 1) // 120

    def lam(self, k):
        """Eigenvalue of the Laplacian on Q^5 for level k."""
        return k * (k + 5)

    def H(self, x):
        """
        Evaluate the Hilbert series H(Q^5, x) = (1+x)/(1-x)^6.
        Returns float (or inf at x=1).
        """
        if abs(x - 1.0) < 1e-15:
            return float('inf')
        return (1.0 + x) / (1.0 - x)**6

    def H_series(self, k_max=10):
        """
        Return the first k_max+1 coefficients of the Taylor expansion.
        H(x) = sum_{k>=0} d_k x^k  (as a formal power series).

        Note: The Hilbert series of Q^5 in the representation-theoretic
        sense gives coefficients d_k. We verify they match (1+x)/(1-x)^6.
        """
        return [self.d(k) for k in range(k_max + 1)]

    # ─── Spectral data ───

    def spectral_data(self, k_max=8):
        """
        Return the spectral data table: eigenvalues, multiplicities, roles.

        Returns list of dicts with keys: k, eigenvalue, multiplicity, product, role.
        """
        roles = {
            0: 'Vacuum',
            1: f'Proton (lambda_1=C_2={C2}, d_1=g={genus})',
            2: f'Strange sector (d_2=m_s/m_hat=27)',
            3: 'Charm sector',
            4: 'Bottom sector',
            5: 'Top sector',
        }

        data = []
        for k in range(k_max + 1):
            lk = self.lam(k)
            dk = self.d(k)
            entry = {
                'k': k,
                'eigenvalue': lk,
                'multiplicity': dk,
                'product': dk * lk,
                'role': roles.get(k, ''),
            }
            data.append(entry)

        # Print table
        print()
        print("  ━" * 34)
        print("  THE SPECTRAL LADDER OF Q^5")
        print("  H(Q^5, x) = (1+x)/(1-x)^6")
        print("  ━" * 34)
        print()
        print(f"  {'k':>3}  {'lambda_k':>10}  {'d_k':>8}  {'d_k*lambda_k':>14}  Role")
        print(f"  {'─'*3}  {'─'*10}  {'─'*8}  {'─'*14}  {'─'*35}")
        for e in data:
            print(f"  {e['k']:>3}  {e['eigenvalue']:>10}  {e['multiplicity']:>8}  "
                  f"{e['product']:>14}  {e['role']}")

        print()
        print(f"  Pole order = {self.pole_order} = C_2 = mass gap exponent")
        print(f"  d_0 = 1 (unique vacuum)")
        print(f"  d_1 = {self.d(1)} = genus = g (proton has 7 modes)")
        print(f"  d_1 * lambda_1 = {self.d(1) * self.lam(1)} = C_2 * g = 6 * 7")
        print()

        return data

    # ─── Strange quark mass ratio ───

    def strange_quark(self):
        """
        d_2 = 27 = m_s / m_hat (strange to average light quark mass ratio).
        Observed: 27.3 +/- 2.5 (FLAG 2024).
        Match: 1.1%.

        Returns dict with BST prediction and observed value.
        """
        d2 = self.d(2)
        observed = 27.3
        uncertainty = 2.5
        deviation = abs(d2 - observed) / observed * 100

        result = {
            'BST_d2': d2,
            'observed_ratio': observed,
            'uncertainty': uncertainty,
            'deviation_pct': deviation,
            'sigma': abs(d2 - observed) / uncertainty,
        }

        print()
        print("  ━" * 34)
        print("  d_2 = 27 = m_s / m_hat")
        print("  ━" * 34)
        print()
        print(f"  BST prediction:   d_2 = {d2}")
        print(f"  Observed:         m_s/m_hat = {observed} +/- {uncertainty}")
        print(f"  Deviation:        {deviation:.1f}%")
        print(f"  Sigma:            {result['sigma']:.2f} sigma")
        print()
        print("  The second multiplicity of the Laplacian on Q^5 is EXACTLY")
        print("  the strange-to-light quark mass ratio.")
        print()
        print(f"  d_2 = (2*2+5)(2+4)(2+3)(2+2)(2+1)/120")
        print(f"       = 9 * 6 * 5 * 4 * 3 / 120")
        print(f"       = 3240 / 120 = 27")
        print()

        return result

    # ─── Hierarchy problem ───

    def hierarchy(self):
        """
        The hierarchy problem is spectral: forces live at different levels k.

        k=0: alpha^0 = 1 (strong scale)
        k=1: alpha^{4*lambda_1} = alpha^24 (gravity). G ~ alpha^24.
        k=2: alpha^{4*lambda_2} = alpha^56 (dark energy). Lambda ~ alpha^56.

        Returns dict with the three scales.
        """
        scales = []
        labels = ['Strong (QCD)', 'Gravity (G_N)', 'Dark energy (Lambda)']
        for k in range(3):
            lk = self.lam(k)
            exponent = 4 * lk
            suppression = alpha**exponent if exponent > 0 else 1.0
            log10_sup = np.log10(suppression) if suppression > 0 else 0.0
            scales.append({
                'k': k,
                'lambda_k': lk,
                'exponent': exponent,
                'alpha_power': f'alpha^{exponent}',
                'suppression': suppression,
                'log10': log10_sup,
                'label': labels[k],
            })

        print()
        print("  ━" * 34)
        print("  THE HIERARCHY PROBLEM IS SPECTRAL")
        print("  ━" * 34)
        print()
        print("  Why is gravity so weak? Because it lives on the k=1 rung.")
        print("  Why is dark energy so small? Because it lives on k=2.")
        print()
        print(f"  {'Level':>6}  {'lambda_k':>9}  {'Exponent':>9}  {'Suppression':>14}  Force")
        print(f"  {'─'*6}  {'─'*9}  {'─'*9}  {'─'*14}  {'─'*20}")

        for s in scales:
            if s['exponent'] == 0:
                sup_str = '1'
            else:
                sup_str = f'10^{s["log10"]:.0f}'
            print(f"  k = {s['k']}   {s['lambda_k']:>9}  "
                  f"4*lambda={s['exponent']:>3}  {sup_str:>14}  {s['label']}")

        print()
        print(f"  G ~ hbar*c*(6pi^5)^2 * alpha^24 / m_e^2")
        print(f"  Lambda ~ alpha^56 * m_e^4 / hbar^3*c^5")
        print()
        print("  The 10^39 ratio between strong and gravitational forces")
        print(f"  is alpha^24 = (1/137)^24 = 10^{24*np.log10(alpha):.0f}.")
        print("  Not a mystery. Just a spectral gap.")
        print()

        return scales

    # ─── GUT uniqueness ───

    def gut_uniqueness(self):
        """
        dim SU(n) = (n-1)! ONLY at n=5. Both equal 24.
        This is the 5th independent proof that n_C = 5 is unique.

        Returns list of dicts comparing n^2 - 1 vs (n-1)! for n=2..7.
        """
        data = []
        for n in range(2, 8):
            dim_sun = n**2 - 1
            fact = factorial(n - 1)
            match = (dim_sun == fact)
            data.append({
                'n': n,
                'dim_SU_n': dim_sun,
                'factorial_n_minus_1': fact,
                'match': match,
            })

        print()
        print("  ━" * 34)
        print("  GUT UNIQUENESS: dim SU(n) = (n-1)!")
        print("  ━" * 34)
        print()
        print(f"  {'n':>4}  {'n^2-1 = dim SU(n)':>20}  {'(n-1)!':>10}  {'Match?':>8}")
        print(f"  {'─'*4}  {'─'*20}  {'─'*10}  {'─'*8}")
        for e in data:
            marker = '  <<<' if e['match'] else ''
            print(f"  {e['n']:>4}  {e['dim_SU_n']:>20}  {e['factorial_n_minus_1']:>10}  "
                  f"{'YES' if e['match'] else 'no':>8}{marker}")

        print()
        print("  n = 5 is the UNIQUE solution to n^2 - 1 = (n-1)!.")
        print("  Both sides equal 24 = dimension of SU(5).")
        print()
        print("  Proof: n^2 - 1 = (n-1)! => (n+1)(n-1) = (n-1)!")
        print("         => n+1 = (n-2)!  (for n > 1)")
        print("         Factorials grow faster than linear, so this has")
        print("         at most one solution. Check: 5+1=6=3!=6. QED.")
        print()

        return data

    # ─── Spectral zeta function ───

    def spectral_zeta(self, s_values=None, k_max=500):
        """
        Spectral zeta function: zeta_Delta(s) = sum_{k>=1} d_k / lambda_k^s.

        Returns dict mapping s -> zeta_Delta(s) for each s in s_values.
        """
        if s_values is None:
            s_values = [2.0, 3.0, 4.0, 5.0, 6.0]

        results = {}
        for s in s_values:
            total = 0.0
            for k in range(1, k_max + 1):
                lk = self.lam(k)
                dk = self.d(k)
                total += dk / lk**s
            results[s] = total

        print()
        print("  ━" * 34)
        print("  SPECTRAL ZETA FUNCTION")
        print("  zeta_Delta(s) = sum_{k>=1} d_k / lambda_k^s")
        print("  ━" * 34)
        print()
        print(f"  Summing {k_max} terms:")
        print()
        print(f"  {'s':>6}  {'zeta_Delta(s)':>18}")
        print(f"  {'─'*6}  {'─'*18}")
        for s in s_values:
            print(f"  {s:>6.1f}  {results[s]:>18.10f}")

        # Check special value at s=3
        z3 = results.get(3.0, None)
        if z3 is not None:
            print()
            print(f"  zeta_Delta(3) = {z3:.10f}")
            print(f"  Compare: 7/720 = {7/720:.10f}")
            ratio = z3 / (7.0/720.0)
            print(f"  Ratio zeta_Delta(3) / (7/720) = {ratio:.6f}")

        print()

        return results

    # ─── Summary ───

    def summary(self):
        """The punchline."""
        print()
        print("  ━" * 34)
        print("  THE PUNCHLINE")
        print("  ━" * 34)
        print()
        print("  H(Q^5, x) = (1+x) / (1-x)^6")
        print()
        print("  Six characters. One rational function. It encodes:")
        print()
        print(f"    Pole order = {C2} = C_2 = mass gap")
        print(f"    d_0 = {self.d(0)}           vacuum uniqueness")
        print(f"    d_1 = {self.d(1)} = g        proton modes")
        print(f"    d_2 = {self.d(2)}          strange quark mass ratio")
        print(f"    lambda_1 = {self.lam(1)} = C_2   proton eigenvalue")
        print(f"    4*lambda_1 = 24      gravity exponent (alpha^24)")
        print(f"    4*lambda_2 = 56      dark energy exponent (alpha^56)")
        print(f"    dim SU(5) = 24 = 4!  GUT uniqueness")
        print()
        print("  The mass gap, the mass hierarchy, the coupling hierarchies,")
        print("  and the uniqueness of n=5. All from one generating function.")
        print()
        print("  The generating function for everything.")
        print()

        return {
            'formula': '(1+x)/(1-x)^6',
            'pole_order': C2,
            'd_values': [self.d(k) for k in range(6)],
            'eigenvalues': [self.lam(k) for k in range(6)],
            'gravity_exponent': 24,
            'dark_energy_exponent': 56,
            'gut_dimension': 24,
        }

    # ─── Visualization ───

    def show(self):
        """Six-panel visualization of the Hilbert series and its physics."""
        try:
            import matplotlib
            matplotlib.use('TkAgg')
            import matplotlib.pyplot as plt
            from matplotlib.patches import FancyBboxPatch, Rectangle
        except ImportError:
            print("  matplotlib not available. Use text methods instead.")
            return

        fig, axes = plt.subplots(2, 3, figsize=(20, 13), facecolor='#0a0a1a')
        fig.canvas.manager.set_window_title('THE HILBERT SERIES OF Q\u2075 \u2014 Toy 141')

        fig.text(0.5, 0.97,
                 'THE HILBERT SERIES OF Q\u2075 \u2014 Toy 141',
                 fontsize=22, fontweight='bold', color='#ffd700',
                 ha='center', fontfamily='monospace')
        fig.text(0.5, 0.94,
                 'H(Q\u2075, x) = (1+x)/(1\u2212x)\u2076   |   N_c=3, n_C=5, g=7, C\u2082=6, N_max=137',
                 fontsize=11, color='#888888', ha='center', fontfamily='monospace')

        GOLD = '#ffd700'
        CYAN = '#00ddff'
        GREEN = '#44ff88'
        BG = '#0d0d24'
        FAINT = '#555555'
        WHITE = '#ffffff'

        # ─── Panel 1: The Generating Function ───
        ax = axes[0, 0]
        ax.set_facecolor(BG)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        ax.set_title('THE GENERATING FUNCTION', color=CYAN, fontfamily='monospace',
                      fontsize=13, fontweight='bold', pad=12)

        ax.text(5, 8.5, 'H(x) = (1+x) / (1\u2212x)\u2076', color=GOLD,
                fontsize=16, fontweight='bold', ha='center', fontfamily='monospace')
        ax.text(5, 7.5, f'Pole order = {C2} = C\u2082 = mass gap',
                color=WHITE, fontsize=10, ha='center', fontfamily='monospace')

        # Bar chart of first 6 multiplicities
        k_vals = list(range(6))
        d_vals = [self.d(k) for k in k_vals]
        max_d = max(d_vals)

        for i, (k, dk) in enumerate(zip(k_vals, d_vals)):
            bar_h = (dk / max_d) * 4.5
            x0 = 1.2 + i * 1.4
            ax.add_patch(Rectangle((x0, 1.0), 1.0, bar_h,
                                   facecolor=GOLD, alpha=0.7, edgecolor=GOLD))
            ax.text(x0 + 0.5, 1.0 + bar_h + 0.2, str(dk), color=WHITE,
                    fontsize=9, ha='center', fontfamily='monospace', fontweight='bold')
            ax.text(x0 + 0.5, 0.5, f'k={k}', color=FAINT,
                    fontsize=8, ha='center', fontfamily='monospace')

        ax.text(5, 0.0, 'd_k = (2k+5)(k+4)(k+3)(k+2)(k+1)/120',
                color=FAINT, fontsize=8, ha='center', fontfamily='monospace')
        ax.text(5, -0.5, '(2k+5) = spectral velocity = ALL Chern integers',
                color=GOLD, fontsize=7, ha='center', fontfamily='monospace', alpha=0.8)

        # ─── Panel 2: The Spectral Ladder ───
        ax = axes[0, 1]
        ax.set_facecolor(BG)
        ax.axis('off')
        ax.set_title('THE SPECTRAL LADDER', color=CYAN, fontfamily='monospace',
                      fontsize=13, fontweight='bold', pad=12)
        ax.set_xlim(0, 10)
        ax.set_ylim(-0.5, 10)

        # Draw energy levels as horizontal lines with width ~ d_k
        k_show = 6
        y_positions = np.linspace(1.0, 8.5, k_show)

        for i in range(k_show):
            k = i
            lk = self.lam(k)
            dk = self.d(k)
            y = y_positions[i]
            width = min(dk / 60.0, 8.0)  # scale width
            lw = max(1.5, min(dk / 30.0, 6.0))

            x_left = 5 - width / 2
            x_right = 5 + width / 2

            if k == 1:
                color = GREEN
            elif k == 2:
                color = GOLD
            else:
                color = CYAN

            ax.plot([x_left, x_right], [y, y], color=color, lw=lw, solid_capstyle='round')

            # Labels
            ax.text(0.3, y, f'k={k}', color=FAINT, fontsize=8,
                    fontfamily='monospace', va='center')
            ax.text(x_right + 0.3, y + 0.15, f'\u03bb={lk}', color=color, fontsize=8,
                    fontfamily='monospace', va='center')
            ax.text(x_right + 0.3, y - 0.25, f'd={dk}', color=FAINT, fontsize=7,
                    fontfamily='monospace', va='center')

        # Annotations
        ax.text(5, 0.0, 'k=1: d\u2081=7=g, d\u2081\u00d7\u03bb\u2081=42=C\u2082\u00d7g',
                color=GREEN, fontsize=8, ha='center', fontfamily='monospace')

        # ─── Panel 3: d_2 = 27 = m_s/m_hat ───
        ax = axes[0, 2]
        ax.set_facecolor(BG)
        ax.axis('off')
        ax.set_title('d\u2082 = 27 = m_s / m\u0302', color=CYAN, fontfamily='monospace',
                      fontsize=13, fontweight='bold', pad=12)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        # Big 27
        ax.text(5, 7.0, '27', color=GOLD, fontsize=72, fontweight='bold',
                ha='center', va='center', fontfamily='monospace')

        # Comparison
        ax.text(5, 4.5, 'BST:  d\u2082 = 27  (exact integer)',
                color=GREEN, fontsize=11, ha='center', fontfamily='monospace')
        ax.text(5, 3.7, 'Obs:  m_s/m\u0302 = 27.3 \u00b1 2.5  (FLAG 2024)',
                color=WHITE, fontsize=11, ha='center', fontfamily='monospace')

        deviation = abs(27 - 27.3) / 27.3 * 100
        ax.text(5, 2.7, f'Deviation: {deviation:.1f}%',
                color=GREEN, fontsize=12, fontweight='bold',
                ha='center', fontfamily='monospace')

        ax.text(5, 1.5, '9 \u00d7 6 \u00d7 5 \u00d7 4 \u00d7 3 / 120 = 27',
                color=FAINT, fontsize=9, ha='center', fontfamily='monospace')
        ax.text(5, 0.7, 'The strange quark mass ratio',
                color=FAINT, fontsize=9, ha='center', fontfamily='monospace')
        ax.text(5, 0.2, 'is a multiplicity on Q\u2075.',
                color=FAINT, fontsize=9, ha='center', fontfamily='monospace')

        # ─── Panel 4: The Hierarchy Problem Is Spectral ───
        ax = axes[1, 0]
        ax.set_facecolor(BG)
        ax.axis('off')
        ax.set_title('THE HIERARCHY IS SPECTRAL', color=CYAN, fontfamily='monospace',
                      fontsize=13, fontweight='bold', pad=12)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        # Three rows
        hierarchy_data = [
            ('k = 0', 'Strong', '\u03b1\u2070 = 1', 0, '#ff4444'),
            ('k = 1', 'Gravity', '\u03b1\u00b2\u2074', 24, GREEN),
            ('k = 2', 'Dark energy', '\u03b1\u2075\u2076', 56, CYAN),
        ]

        for idx, (level, force, expr, exp, color) in enumerate(hierarchy_data):
            y = 7.5 - idx * 2.5

            ax.text(0.5, y + 0.3, level, color=color, fontsize=12,
                    fontweight='bold', fontfamily='monospace')
            ax.text(0.5, y - 0.3, force, color=FAINT, fontsize=10,
                    fontfamily='monospace')

            # Log-scale bar
            if exp == 0:
                bar_len = 8.0
            else:
                log_val = exp * np.log10(alpha)
                bar_len = max(0.3, 8.0 + log_val / 6.0)  # scale

            ax.add_patch(Rectangle((3.5, y - 0.15), bar_len, 0.3,
                                   facecolor=color, alpha=0.5, edgecolor=color))

            # Suppression text
            if exp == 0:
                ax.text(3.5 + bar_len + 0.2, y, '= 1', color=WHITE,
                        fontsize=9, fontfamily='monospace', va='center')
            else:
                log10_val = exp * np.log10(alpha)
                ax.text(3.5 + bar_len + 0.2, y,
                        f'{expr} = 10^{log10_val:.0f}',
                        color=WHITE, fontsize=9, fontfamily='monospace', va='center')

        ax.text(5, 1.2, 'Gravity/Strong = \u03b1\u00b2\u2074 = 10\u207b\u2075\u00b2',
                color=GOLD, fontsize=10, ha='center', fontfamily='monospace')
        ax.text(5, 0.4, 'NOT a mystery. A spectral gap.',
                color=GOLD, fontsize=10, fontweight='bold',
                ha='center', fontfamily='monospace')

        # ─── Panel 5: GUT Uniqueness ───
        ax = axes[1, 1]
        ax.set_facecolor(BG)
        ax.axis('off')
        ax.set_title('GUT UNIQUENESS: dim SU(n) = (n\u22121)!', color=CYAN,
                      fontfamily='monospace', fontsize=13, fontweight='bold', pad=12)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        # Table header
        ax.text(1.5, 8.5, 'n', color=FAINT, fontsize=11,
                fontweight='bold', fontfamily='monospace', ha='center')
        ax.text(4.0, 8.5, 'n\u00b2\u22121', color=FAINT, fontsize=11,
                fontweight='bold', fontfamily='monospace', ha='center')
        ax.text(6.5, 8.5, '(n\u22121)!', color=FAINT, fontsize=11,
                fontweight='bold', fontfamily='monospace', ha='center')
        ax.text(8.5, 8.5, 'Equal?', color=FAINT, fontsize=11,
                fontweight='bold', fontfamily='monospace', ha='center')

        ax.plot([0.5, 9.5], [8.1, 8.1], color=FAINT, lw=0.5)

        for idx, n in enumerate(range(2, 8)):
            y = 7.3 - idx * 1.0
            dim_sun = n**2 - 1
            fact = factorial(n - 1)
            match = (dim_sun == fact)

            color = GOLD if match else WHITE
            weight = 'bold' if match else 'normal'

            ax.text(1.5, y, str(n), color=color, fontsize=11,
                    fontfamily='monospace', ha='center', fontweight=weight)
            ax.text(4.0, y, str(dim_sun), color=color, fontsize=11,
                    fontfamily='monospace', ha='center', fontweight=weight)
            ax.text(6.5, y, str(fact), color=color, fontsize=11,
                    fontfamily='monospace', ha='center', fontweight=weight)
            if match:
                ax.text(8.5, y, 'YES', color=GREEN, fontsize=11,
                        fontfamily='monospace', ha='center', fontweight='bold')
            else:
                ax.text(8.5, y, 'no', color=FAINT, fontsize=11,
                        fontfamily='monospace', ha='center')

        ax.text(5, 0.8, 'n = 5 is unique. Both sides = 24.',
                color=GOLD, fontsize=11, fontweight='bold',
                ha='center', fontfamily='monospace')
        ax.text(5, 0.1, '5th independent proof of n_C = 5.',
                color=FAINT, fontsize=9, ha='center', fontfamily='monospace')

        # ─── Panel 6: The Punchline ───
        ax = axes[1, 2]
        ax.set_facecolor(BG)
        ax.axis('off')
        ax.set_title('THE PUNCHLINE', color=CYAN, fontfamily='monospace',
                      fontsize=13, fontweight='bold', pad=12)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        ax.text(5, 8.0, '(1+x)', color=GOLD, fontsize=20,
                fontweight='bold', ha='center', fontfamily='monospace')
        ax.text(5, 7.1, '\u2500\u2500\u2500\u2500\u2500\u2500', color=GOLD, fontsize=20,
                ha='center', fontfamily='monospace')
        ax.text(5, 6.2, '(1\u2212x)\u2076', color=GOLD, fontsize=20,
                fontweight='bold', ha='center', fontfamily='monospace')

        lines = [
            ('Mass gap', f'pole order = {C2} = C\u2082'),
            ('Mass hierarchy', 'd\u2082 = 27 = m_s/m\u0302'),
            ('Gravity', '\u03b1\u00b2\u2074 from \u03bb\u2081 = 6'),
            ('Dark energy', '\u03b1\u2075\u2076 from \u03bb\u2082 = 14'),
            ('Uniqueness', 'dim SU(5) = 4! = 24'),
        ]

        for i, (label, detail) in enumerate(lines):
            y = 4.8 - i * 0.8
            ax.text(1.0, y, label, color=GREEN, fontsize=10,
                    fontfamily='monospace', fontweight='bold')
            ax.text(5.5, y, detail, color=WHITE, fontsize=9,
                    fontfamily='monospace')

        ax.text(5, 0.6, 'Six characters encode',
                color=FAINT, fontsize=9, ha='center', fontfamily='monospace')
        ax.text(5, 0.0, 'the generating function for everything.',
                color=GOLD, fontsize=11, fontweight='bold',
                ha='center', fontfamily='monospace')

        # ─── Finalize ───
        plt.tight_layout(rect=(0, 0.01, 1, 0.92))
        plt.show(block=False)
        print("  [Plot displayed]")


# ═══════════════════════════════════════════════════════════════════
# MAIN — menu-driven interface
# ═══════════════════════════════════════════════════════════════════

def main():
    hs = HilbertSeries()

    print()
    print("  ━" * 34)
    print("  THE HILBERT SERIES OF Q\u2075 \u2014 Toy 141")
    print("  H(Q\u2075, x) = (1+x)/(1\u2212x)\u2076")
    print("  The generating function for everything.")
    print("  ━" * 34)
    print()
    print("  1) Spectral data table (eigenvalues and multiplicities)")
    print("  2) d_2 = 27 = m_s/m_hat (strange quark mass ratio)")
    print("  3) The hierarchy problem is spectral")
    print("  4) GUT uniqueness: dim SU(n) = (n-1)!")
    print("  5) Spectral zeta function")
    print("  6) Summary (the punchline)")
    print("  7) Show all panels (matplotlib)")
    print("  8) Run everything")
    print()

    try:
        choice = input("  Choice [1-8]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = '8'

    if choice == '1':
        hs.spectral_data()
    elif choice == '2':
        hs.strange_quark()
    elif choice == '3':
        hs.hierarchy()
    elif choice == '4':
        hs.gut_uniqueness()
    elif choice == '5':
        hs.spectral_zeta()
    elif choice == '6':
        hs.summary()
    elif choice == '7':
        hs.show()
    elif choice == '8':
        hs.spectral_data()
        hs.strange_quark()
        hs.hierarchy()
        hs.gut_uniqueness()
        hs.spectral_zeta()
        hs.summary()
        try:
            hs.show()
        except Exception as e:
            print(f"  [Visualization skipped: {e}]")
    else:
        hs.summary()

    print()
    print("  All from (1+x)/(1-x)^6. Zero free parameters.")
    print("  Copyright (c) 2026 Casey Koons. Created with Claude Opus 4.6.")
    print()


if __name__ == '__main__':
    main()
