#!/usr/bin/env python3
"""
THE WEYL CANCELLATION UNFOLDING  --  Toy 61
============================================
The 1920 cancellation is not a numerical coincidence. It is a THEOREM
about the Weyl group W(D_5) of the root system D_5.

|W(D_5)| = 5! x 2^4 = 120 x 16 = 1920

This number appears in TWO places:
  1. Vol(D_IV^5) = pi^5 / 1920    (Hua's formula -- the denominator)
  2. Baryon orbit size = 1920      (S_5 x (Z_2)^4 acting freely)

When computing m_p/m_e, they MULTIPLY and CANCEL:

    m_p/m_e = C_2 x |orbit| x Vol(D_IV^5)
            = 6   x  1920   x  pi^5/1920
            = 6   x  pi^5
            = 6 pi^5  =  1836.118

This is NOT coincidence -- it is the SAME Weyl group appearing in two
roles (symmetry reduction of the volume, and orbit count on the boundary).

The theorem generalizes: for any D_IV^n, the Weyl group W(D_n) cancels,
leaving C_2(pi_{n+1}) x pi^n = (n+1) pi^n.

Connection to E_8: |W(D_5)| / |W(B_2)| = 1920 / 8 = 240 = |Phi(E_8)|.

CI Interface:
    from toy_weyl_cancellation import WeylCancellation
    wc = WeylCancellation()
    wc.weyl_order(n=5)       # |W(D_n)| = n! x 2^(n-1), n=1..8
    wc.hua_volume()          # Vol(D_IV^5) = pi^5/1920
    wc.baryon_orbit()        # 1920 circuit configs from S_5 x (Z_2)^4
    wc.cancellation()        # 1920 x pi^5/1920 = pi^5, then x6 = 6pi^5
    wc.factorization()       # 1920 = 5! x 2^4 tree
    wc.generalize(n)         # cancellation for arbitrary D_n
    wc.e8_connection()       # |W(D_5)|/|W(B_2)| = 240 = |Phi(E_8)|
    wc.weyl_group_table()    # D_1 through D_8 comparison
    wc.summary()             # key insight
    wc.show()                # 4-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
import math
import sys
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.gridspec import GridSpec

# ──────────────────────────────────────────────────────────────────
#  BST Constants
# ──────────────────────────────────────────────────────────────────
N_c   = 3           # color charges
n_C   = 5           # complex dimension of D_IV^5
C_2   = n_C + 1     # 6  Casimir eigenvalue C_2(pi_6)
genus = n_C + 2     # 7  genus of D_IV^5
N_max = 137         # channel capacity
alpha = 1.0 / 137.035999

# Weyl group
FACTORIAL_5 = math.factorial(n_C)           # 120 = 5!
SIGNS_4     = 2**(n_C - 1)                  # 16  = 2^4
W_D5        = FACTORIAL_5 * SIGNS_4          # 1920 = |W(D_5)|
W_B2        = 8                              # |W(B_2)| = 2! x 2^2 = 8
E8_ROOTS    = W_D5 // W_B2                   # 240 = |Phi(E_8)|

# Hua volume
HUA_VOL     = np.pi**n_C / W_D5             # pi^5 / 1920

# Mass ratio
PROTON_RATIO = C_2 * np.pi**n_C             # 6 pi^5
OBSERVED     = 1836.15267343


# ══════════════════════════════════════════════════════════════════
#  Helper: Weyl group order for D_n
# ══════════════════════════════════════════════════════════════════

def weyl_dn(n):
    """Return |W(D_n)| = n! x 2^(n-1) for n >= 1."""
    return math.factorial(n) * (2 ** (n - 1))

def weyl_bn(n):
    """Return |W(B_n)| = n! x 2^n for n >= 1."""
    return math.factorial(n) * (2 ** n)

def hua_vol_n(n):
    """Return Vol(D_IV^n) = pi^n / |W(D_n)|."""
    return np.pi**n / weyl_dn(n)

def casimir_n(n):
    """C_2(pi_{n+1}) = n + 1 for the Bergman space."""
    return n + 1


# ══════════════════════════════════════════════════════════════════
#  CLASS: WeylCancellation
# ══════════════════════════════════════════════════════════════════

class WeylCancellation:
    """Toy 61: The Weyl Cancellation Unfolding."""

    def __init__(self, quiet=False):
        self.quiet = quiet
        if not quiet:
            print()
            print("=" * 68)
            print("  THE WEYL CANCELLATION UNFOLDING  --  BST Toy 61")
            print("  |W(D_5)| = 1920 cancels between volume and orbit")
            print("=" * 68)

    def _p(self, text=""):
        if not self.quiet:
            print(text)

    # ──────────────────────────────────────────────────────────────
    # 1. weyl_order
    # ──────────────────────────────────────────────────────────────

    def weyl_order(self, n=5):
        """Compute |W(D_n)| = n! x 2^(n-1) for n=1..8, highlight n."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  WEYL GROUP ORDERS  |W(D_n)| = n! x 2^(n-1)")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  n │  n!      │  2^(n-1)  │  |W(D_n)|    │  Note")
        self._p("  ──┼──────────┼───────────┼──────────────┼──────────────────")

        for k in range(1, 9):
            fk = math.factorial(k)
            sk = 2**(k - 1)
            wk = fk * sk
            marker = "  <── BST" if k == n else ""
            arrow = " *" if k == n else "  "
            note = ""
            if k == 1:
                note = "trivial"
            elif k == 2:
                note = "rectangle"
            elif k == 3:
                note = "|S_4| = 24"
            elif k == 4:
                note = "24-cell (triality)"
            elif k == 5:
                note = "demipenteract"
            elif k == 6:
                note = "demihexeract"
            elif k == 7:
                note = "demihepteract"
            elif k == 8:
                note = "demiocteract"
            self._p(f" {arrow}{k} │ {fk:>8} │ {sk:>9} │ {wk:>12} │ {note}{marker}")

        self._p()
        self._p(f"  For n = {n}:")
        self._p(f"    |W(D_{n})| = {n}! x 2^{n-1} = {math.factorial(n)} x {2**(n-1)} = {weyl_dn(n)}")
        self._p()
        return weyl_dn(n)

    # ──────────────────────────────────────────────────────────────
    # 2. hua_volume
    # ──────────────────────────────────────────────────────────────

    def hua_volume(self):
        """Show Vol(D_IV^5) = pi^5 / |W(D_5)| = pi^5 / 1920."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  HUA'S VOLUME FORMULA (1963)")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  Theorem (Hua):")
        self._p(f"    Vol(D_IV^n) = pi^n / |W(D_n)|")
        self._p()
        self._p(f"  For n = n_C = {n_C}:")
        self._p(f"    Vol(D_IV^5) = pi^5 / |W(D_5)|")
        self._p(f"               = pi^5 / {W_D5}")
        self._p(f"               = {np.pi**5:.6f} / {W_D5}")
        self._p(f"               = {HUA_VOL:.10f}")
        self._p()
        self._p("  WHY 1920 appears in the denominator:")
        self._p("    The Bergman metric integrand is invariant under W(D_5).")
        self._p("    The integral over D_IV^5 decomposes into |W(D_5)| copies")
        self._p("    of a fundamental domain. Raw integral = pi^5.")
        self._p("    Dividing by the symmetry group: pi^5 / 1920.")
        self._p()
        self._p("    The 1920 is a SYMMETRY REDUCTION, not a mystery number.")
        self._p()
        return HUA_VOL

    # ──────────────────────────────────────────────────────────────
    # 3. baryon_orbit
    # ──────────────────────────────────────────────────────────────

    def baryon_orbit(self):
        """Show 1920 baryon circuit configurations from S_5 x (Z_2)^4."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  BARYON ORBIT ON THE SHILOV BOUNDARY")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  A baryon = Z_3 color circuit visiting 3 points on S^4 x S^1.")
        self._p()
        self._p("  The W(D_5) action on baryon configurations:")
        self._p(f"    S_5:     permute 5 complex dimensions  ({FACTORIAL_5} elements)")
        self._p(f"    (Z_2)^4: flip even subsets of S^1 phases ({SIGNS_4} elements)")
        self._p()
        self._p("  The even-parity constraint:")
        self._p("    The Shilov boundary S^4 x S^1 has a Z_2 identification.")
        self._p("    Only EVEN numbers of sign flips preserve z . z = sum z_j^2.")
        self._p("    This distinguishes D_n from B_n:")
        self._p(f"      |W(D_5)| = 5! x 2^4 = {W_D5}")
        self._p(f"      |W(B_5)| = 5! x 2^5 = {weyl_bn(5)}  (would allow odd flips)")
        self._p()
        self._p("  Freeness (orbit-stabilizer):")
        self._p("    For generic baryon configs, Stab(B) = {{e}}.")
        self._p("    No non-trivial permutation or sign flip fixes a generic triple.")
        self._p(f"    Therefore: |orbit| = |W(D_5)| / 1 = {W_D5}")
        self._p()
        self._p(f"  The baryon orbit has EXACTLY {W_D5} configurations.")
        self._p("  This is the SAME group that divides the volume.")
        self._p()
        return W_D5

    # ──────────────────────────────────────────────────────────────
    # 4. cancellation
    # ──────────────────────────────────────────────────────────────

    def cancellation(self):
        """The multiplication: 1920 x pi^5/1920 = pi^5, then x C_2 = 6 pi^5."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  THE CANCELLATION")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The proton mass formula:")
        self._p()
        self._p("    m_p / m_e = C_2 x |orbit| x Vol(D_IV^5)")
        self._p()
        self._p("  Step by step:")
        self._p()
        self._p(f"    = C_2  x  |W(D_5)|  x  pi^5 / |W(D_5)|")
        self._p(f"    = {C_2}    x   {W_D5}     x  pi^5 / {W_D5}")
        self._p()
        self._p(f"         {W_D5} cancels with {W_D5}:")
        self._p()
        self._p(f"    = {C_2}    x    ----{W_D5}----    x    pi^5 / ----{W_D5}----")
        self._p()
        self._p(f"    = {C_2}    x    pi^5")
        self._p()
        self._p(f"    = {C_2} pi^5")
        self._p()
        self._p(f"    = {PROTON_RATIO:.6f}")
        self._p()
        self._p(f"  Observed: {OBSERVED}")
        error_pct = abs(PROTON_RATIO - OBSERVED) / OBSERVED * 100
        self._p(f"  Error:    {error_pct:.4f}%")
        self._p()
        self._p("  The 1920 is a GAUGE REDUNDANCY of the calculation.")
        self._p("  The physical content is C_2 x pi^n_C  --  nothing more.")
        self._p()
        return PROTON_RATIO

    # ──────────────────────────────────────────────────────────────
    # 5. factorization
    # ──────────────────────────────────────────────────────────────

    def factorization(self):
        """Show 1920 = 5! x 2^4 = S_5 (permutations) x (Z_2)^4 (sign flips)."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  FACTORIZATION OF 1920")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  1920 = |W(D_5)| = S_5  x  (Z_2)^4")
        self._p()
        self._p("  The factorization tree:")
        self._p()
        self._p("                      1920")
        self._p("                     /    \\")
        self._p("                   120     16")
        self._p("                  (5!)    (2^4)")
        self._p("                 /    \\     |")
        self._p("               5  x  24   2x2x2x2")
        self._p("                    (4!)   even sign")
        self._p("                   /    \\   flips in 5D")
        self._p("                  4  x  6")
        self._p("                      (3!)")
        self._p("                     /    \\")
        self._p("                    3  x  2")
        self._p()
        self._p("  Physical meaning of each factor:")
        self._p()
        self._p(f"    120 = 5! = |S_5|")
        self._p(f"      Permutations of n_C = {n_C} complex dimensions.")
        self._p(f"      Each quark in the baryon circuit can occupy any of")
        self._p(f"      the {n_C} causal winding modes.")
        self._p()
        self._p(f"    16 = 2^4 = |(Z_2)^4|")
        self._p(f"      Even sign-flip patterns in {n_C} dimensions.")
        self._p(f"      Relative S^1 phase orientations between quark pairs.")
        self._p(f"      Even parity: prod(epsilon_j) = +1 (color-singlet).")
        self._p()
        self._p(f"  Cross-check:")
        self._p(f"    {FACTORIAL_5} x {SIGNS_4} = {W_D5}")
        self._p()

        # Prime factorization
        self._p("  Prime factorization:")
        self._p(f"    1920 = 2^7 x 3 x 5")
        self._p(f"         = 128 x 15")
        self._p(f"         = {2**7} x {15}")
        assert 2**7 * 3 * 5 == 1920
        self._p()
        return (FACTORIAL_5, SIGNS_4)

    # ──────────────────────────────────────────────────────────────
    # 6. generalize
    # ──────────────────────────────────────────────────────────────

    def generalize(self, n=None):
        """Show cancellation for arbitrary D_n."""
        if n is None:
            n = n_C

        self._p()
        self._p("  " + "=" * 60)
        self._p(f"  GENERAL WEYL CANCELLATION FOR D_IV^{n}")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  Theorem (General Weyl Cancellation):")
        self._p("    For any type IV bounded symmetric domain D_IV^n, n >= 1:")
        self._p()
        self._p("    m_p/m_e = C_2(pi_{n+1}) x |orbit| x Vol(D_IV^n)")
        self._p("            = (n+1) x |W(D_n)| x pi^n / |W(D_n)|")
        self._p("            = (n+1) x pi^n")
        self._p()
        self._p("  The Weyl group W(D_n) ALWAYS cancels.")
        self._p()

        wn = weyl_dn(n)
        vol = hua_vol_n(n)
        c2 = casimir_n(n)
        mass_ratio = c2 * np.pi**n

        self._p(f"  For n = {n}:")
        self._p(f"    |W(D_{n})| = {n}! x 2^{n-1} = {math.factorial(n)} x {2**(n-1)} = {wn}")
        self._p(f"    Vol(D_IV^{n}) = pi^{n} / {wn} = {vol:.10f}")
        self._p(f"    C_2(pi_{n+1}) = {n} + 1 = {c2}")
        self._p()
        self._p(f"    Cancellation:")
        self._p(f"      {c2} x {wn} x pi^{n}/{wn}")
        self._p(f"      = {c2} x pi^{n}")
        self._p(f"      = {mass_ratio:.6f}")
        self._p()

        # Table for n=1..8
        self._p("  Sweep across all D_IV^n:")
        self._p()
        self._p("  n │  |W(D_n)|    │  Vol(D_IV^n)      │  C_2  │  C_2 x pi^n")
        self._p("  ──┼──────────────┼───────────────────┼───────┼────────────────")

        for k in range(1, 9):
            wk = weyl_dn(k)
            vk = hua_vol_n(k)
            ck = casimir_n(k)
            mk = ck * np.pi**k
            marker = "  <── BST" if k == n_C else ""
            self._p(f"  {k} │ {wk:>12} │ {vk:>17.10f} │ {ck:>5} │ {mk:>14.4f}{marker}")

        self._p()
        self._p("  In EVERY row: |W(D_n)| cancels. The mass ratio depends only")
        self._p(f"  on n (dimension) and C_2 = n+1 (Casimir). Nothing else.")
        self._p()
        return mass_ratio

    # ──────────────────────────────────────────────────────────────
    # 7. e8_connection
    # ──────────────────────────────────────────────────────────────

    def e8_connection(self):
        """Show |W(D_5)|/|W(B_2)| = 1920/8 = 240 = |Phi(E_8)|."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  E_8 CONNECTION")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  Two Weyl groups in BST:")
        self._p()
        self._p(f"    W(D_5): symmetry of D_IV^5 quadratic form   |W(D_5)| = {W_D5}")
        self._p(f"    W(B_2): restricted root system of SO_0(5,2)  |W(B_2)| = {W_B2}")
        self._p()
        self._p(f"  Their ratio:")
        self._p()
        self._p(f"    |W(D_5)| / |W(B_2)| = {W_D5} / {W_B2} = {E8_ROOTS}")
        self._p()
        self._p(f"  240 = |Phi(E_8)| = number of roots of E_8")
        self._p()
        self._p("  This is the largest exceptional simple Lie algebra.")
        self._p("  dim(E_8) = 248 = 240 roots + 8 Cartan generators")
        self._p()
        self._p("  The E_8 lattice:")
        self._p("    - Densest sphere packing in 8 dimensions")
        self._p("    - Kissing number = 240 (each sphere touches 240 neighbors)")
        self._p("    - Self-dual: E_8 = E_8^*")
        self._p()
        self._p("  In BST, the E_8 connection arises because:")
        self._p("    D_5 is the root system of SO(10)")
        self._p("    B_2 is the restricted root system of the isometry group")
        self._p("    Their ratio encodes the E_8 root count")
        self._p()
        self._p("  Physical interpretation:")
        self._p("    The 1920 baryon configurations decompose into")
        self._p(f"    240 E_8-equivalent classes, each containing {W_B2} elements.")
        self._p(f"    {E8_ROOTS} x {W_B2} = {E8_ROOTS * W_B2}")
        self._p()

        # Verify
        assert E8_ROOTS == 240
        assert E8_ROOTS * W_B2 == W_D5
        return E8_ROOTS

    # ──────────────────────────────────────────────────────────────
    # 8. weyl_group_table
    # ──────────────────────────────────────────────────────────────

    def weyl_group_table(self):
        """Comparison table: D_1 through D_8 orders, volumes, physical meaning."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  WEYL GROUP TABLE: D_1 THROUGH D_8")
        self._p("  " + "=" * 60)
        self._p()

        meanings = {
            1: "trivial (point)",
            2: "rectangle symmetry (Z_2 x Z_2)",
            3: "cube-octahedron (= S_4, |W(D_3)|=24)",
            4: "demitesseract / 24-cell (triality)",
            5: "demipenteract -- BST DOMAIN",
            6: "demihexeract (SO(12) Weyl group)",
            7: "demihepteract (SO(14) Weyl group)",
            8: "demiocteract (SO(16) Weyl group)",
        }

        lie_groups = {
            1: "SO(2) ~ U(1)",
            2: "SO(4) ~ SU(2)xSU(2)",
            3: "SO(6) ~ SU(4)",
            4: "SO(8) (triality)",
            5: "SO(10) (GUT group)",
            6: "SO(12)",
            7: "SO(14)",
            8: "SO(16)",
        }

        self._p("  n │  |W(D_n)|    │  Vol(D_IV^n)       │  Lie group        │  Geometry")
        self._p("  ──┼──────────────┼────────────────────┼───────────────────┼──────────────────────")

        for k in range(1, 9):
            wk = weyl_dn(k)
            vk = hua_vol_n(k)
            lg = lie_groups[k]
            gm = meanings[k]
            marker = " ***" if k == n_C else ""
            self._p(f"  {k} │ {wk:>12} │ {vk:>18.10f} │ {lg:<17} │ {gm}{marker}")

        self._p()
        self._p("  The root system D_n is also the root system of SO(2n).")
        self._p("  At n=5, SO(10) is the Georgi-Jarlskog GUT group.")
        self._p("  In BST, SO(10) is not a broken gauge symmetry at 10^16 GeV.")
        self._p("  It is the Weyl symmetry of the domain geometry.")
        self._p()

        self._p("  Casimir eigenvalues C_2(pi_{n+1}) = n + 1:")
        self._p()
        for k in range(1, 9):
            ck = casimir_n(k)
            mk = ck * np.pi**k
            self._p(f"    n={k}: C_2 = {ck},  mass ratio = {ck} pi^{k} = {mk:.4f}")
        self._p()
        return

    # ──────────────────────────────────────────────────────────────
    # 9. summary
    # ──────────────────────────────────────────────────────────────

    def summary(self):
        """Key insight: the 1920 cancellation is a theorem about W(D_5)."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  SUMMARY: THE WEYL CANCELLATION UNFOLDING")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  1920 = |W(D_5)| = 5! x 2^4 = 120 x 16")
        self._p()
        self._p("  It is the order of the Weyl group of the root system D_5,")
        self._p("  which is the symmetry group of z . z = sum z_j^2 on D_IV^5.")
        self._p()
        self._p("  This group appears in TWO places:")
        self._p()
        self._p("    VOLUME:  Vol(D_IV^5) = pi^5 / |W(D_5)| = pi^5 / 1920")
        self._p("             (symmetry reduction by the Weyl group)")
        self._p()
        self._p("    ORBIT:   |orbit(B)| = |W(D_5)| = 1920")
        self._p("             (free action on baryon configurations)")
        self._p()
        self._p("  They cancel:")
        self._p("    1920 x (pi^5 / 1920) = pi^5")
        self._p()
        self._p("  Leaving:")
        self._p(f"    m_p/m_e = C_2 x pi^5 = {C_2} x pi^5 = {PROTON_RATIO:.4f}")
        self._p(f"    Observed: {OBSERVED}")
        self._p(f"    Error: {abs(PROTON_RATIO - OBSERVED)/OBSERVED*100:.4f}%")
        self._p()
        self._p("  The 1920 is a gauge redundancy.")
        self._p("  The physical content is C_2 x pi^n_C.")
        self._p("  The Weyl group is the SAME group in both roles.")
        self._p("  That is why it cancels -- not by accident, but by theorem.")
        self._p()
        self._p(f"  E_8 bonus: |W(D_5)|/|W(B_2)| = 1920/8 = 240 = |Phi(E_8)|")
        self._p()
        return

    # ──────────────────────────────────────────────────────────────
    # 10. show  --  4-panel visualization
    # ──────────────────────────────────────────────────────────────

    def show(self):
        """4-panel visualization: cancellation, factorization tree, D_n sweep, E_8."""

        BG = '#0a0a1a'
        GOLD = '#ffaa00'
        GOLD_DIM = '#aa8800'
        BLUE = '#4488ff'
        BLUE_DIM = '#336699'
        RED = '#ff4488'
        RED_DIM = '#cc3366'
        GREEN = '#00ff88'
        GREEN_DIM = '#00aa66'
        WHITE = '#ffffff'
        GREY = '#888888'
        CYAN = '#44ddff'
        ORANGE = '#ff8800'
        CANCEL_RED = '#ff2222'

        fig = plt.figure(figsize=(17, 12), facecolor=BG)
        fig.canvas.manager.set_window_title('The Weyl Cancellation Unfolding — BST Toy 61')

        fig.text(0.5, 0.975, 'THE WEYL CANCELLATION UNFOLDING',
                 fontsize=26, fontweight='bold', color=GOLD, ha='center',
                 fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=2, foreground='#442200')])
        fig.text(0.5, 0.950, '|W(D\u2085)| = 1920 appears twice and cancels: SAME group, two roles',
                 fontsize=12, color=GOLD_DIM, ha='center', fontfamily='monospace')

        # ─── Panel 1 (top-left): THE CANCELLATION ───
        ax1 = fig.add_axes([0.02, 0.50, 0.48, 0.43])
        ax1.set_facecolor(BG)
        ax1.axis('off')
        ax1.set_xlim(0, 10)
        ax1.set_ylim(0, 10)

        ax1.text(5, 9.5, 'THE CANCELLATION', fontsize=17, fontweight='bold',
                 color=GOLD, ha='center', fontfamily='monospace')

        # The formula, line by line
        ax1.text(5, 8.5, 'm\u209a / m\u2091  =  C\u2082  \u00d7  |orbit|  \u00d7  Vol(D\u2009\u1d62\u1d65\u2075)',
                 fontsize=13, color=WHITE, ha='center', fontfamily='monospace')

        ax1.text(5, 7.5, f'=   {C_2}   \u00d7   {W_D5}   \u00d7   \u03c0\u2075 / {W_D5}',
                 fontsize=14, color=ORANGE, ha='center', fontfamily='monospace')

        # Strikethrough animation: draw the 1920s with red lines through them
        # First 1920
        t1920_1_x = 3.35
        ax1.text(t1920_1_x, 6.3, f'{W_D5}', fontsize=15, color='#ff4444',
                 ha='center', fontfamily='monospace', fontweight='bold')
        ax1.plot([t1920_1_x - 0.5, t1920_1_x + 0.5], [6.3, 6.3],
                 color=CANCEL_RED, linewidth=4, alpha=0.9)

        ax1.text(5.0, 6.3, '\u00d7   \u03c0\u2075 /', fontsize=15, color=ORANGE,
                 ha='center', fontfamily='monospace')

        # Second 1920
        t1920_2_x = 6.65
        ax1.text(t1920_2_x, 6.3, f'{W_D5}', fontsize=15, color='#ff4444',
                 ha='center', fontfamily='monospace', fontweight='bold')
        ax1.plot([t1920_2_x - 0.5, t1920_2_x + 0.5], [6.3, 6.3],
                 color=CANCEL_RED, linewidth=4, alpha=0.9)

        ax1.text(1.85, 6.3, f'=   {C_2}   \u00d7', fontsize=15, color=ORANGE,
                 ha='center', fontfamily='monospace')

        # Arrow showing cancellation
        ax1.annotate('', xy=(t1920_2_x + 0.6, 6.3), xytext=(t1920_1_x - 0.6, 6.3),
                     arrowprops=dict(arrowstyle='<->', color=CANCEL_RED,
                                     lw=2, connectionstyle='arc3,rad=0.4'))
        ax1.text(5.0, 7.0, 'CANCEL', fontsize=10, fontweight='bold',
                 color=CANCEL_RED, ha='center', fontfamily='monospace')

        # Result
        ax1.text(5, 5.0, f'=   {C_2}  \u00d7  \u03c0\u2075', fontsize=16,
                 color=WHITE, ha='center', fontfamily='monospace', fontweight='bold')

        # Boxed final answer
        box = FancyBboxPatch((2.0, 3.4), 6.0, 1.3, boxstyle='round,pad=0.2',
                              facecolor='#0a2a1a', edgecolor=GREEN, linewidth=2.5)
        ax1.add_patch(box)
        ax1.text(5, 4.15, f'= 6\u03c0\u2075 = {PROTON_RATIO:.3f}', fontsize=18,
                 fontweight='bold', color=GREEN, ha='center', fontfamily='monospace')
        ax1.text(5, 3.7, f'm\u209a / m\u2091', fontsize=12, color=GREEN_DIM,
                 ha='center', fontfamily='monospace')

        # Error
        error_pct = abs(PROTON_RATIO - OBSERVED) / OBSERVED * 100
        ax1.text(5, 2.6, f'observed: {OBSERVED}   error: {error_pct:.4f}%',
                 fontsize=11, color=GREY, ha='center', fontfamily='monospace')

        # Explanatory labels
        ax1.text(3.35, 1.7, '|W(D\u2085)| = 1920', fontsize=10, color=BLUE,
                 ha='center', fontfamily='monospace')
        ax1.text(3.35, 1.2, 'baryon orbit', fontsize=9, color=BLUE_DIM,
                 ha='center', fontfamily='monospace')
        ax1.text(3.35, 0.8, '(orbit count)', fontsize=9, color=BLUE_DIM,
                 ha='center', fontfamily='monospace')

        ax1.text(6.65, 1.7, '\u03c0\u2075/|W(D\u2085)|', fontsize=10, color=RED,
                 ha='center', fontfamily='monospace')
        ax1.text(6.65, 1.2, 'Hua volume', fontsize=9, color=RED_DIM,
                 ha='center', fontfamily='monospace')
        ax1.text(6.65, 0.8, '(symmetry reduction)', fontsize=9, color=RED_DIM,
                 ha='center', fontfamily='monospace')

        ax1.text(5.0, 0.2, 'SAME GROUP, two roles \u2192 identical cancellation',
                 fontsize=10, fontweight='bold', color=GOLD_DIM, ha='center',
                 fontfamily='monospace')

        # ─── Panel 2 (top-right): FACTORIZATION TREE ───
        ax2 = fig.add_axes([0.52, 0.50, 0.46, 0.43])
        ax2.set_facecolor(BG)
        ax2.axis('off')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 10)

        ax2.text(5, 9.5, 'FACTORIZATION TREE', fontsize=17, fontweight='bold',
                 color=CYAN, ha='center', fontfamily='monospace')

        # 1920 at top
        ax2.text(5, 8.5, '1920', fontsize=20, fontweight='bold', color=WHITE,
                 ha='center', fontfamily='monospace',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a1a3a',
                           edgecolor=CYAN, linewidth=2))
        ax2.text(5, 7.9, '|W(D\u2085)|', fontsize=10, color=GREY,
                 ha='center', fontfamily='monospace')

        # Branches to 120 and 16
        ax2.plot([5, 3], [7.7, 6.8], color=CYAN, linewidth=2, alpha=0.6)
        ax2.plot([5, 7], [7.7, 6.8], color=CYAN, linewidth=2, alpha=0.6)

        ax2.text(3, 6.5, '120', fontsize=16, fontweight='bold', color=BLUE,
                 ha='center', fontfamily='monospace',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a1a2a',
                           edgecolor=BLUE, linewidth=2))
        ax2.text(3, 5.9, '5! = |S\u2085|', fontsize=10, color=BLUE_DIM,
                 ha='center', fontfamily='monospace')
        ax2.text(3, 5.4, 'permutations of', fontsize=8, color=BLUE_DIM,
                 ha='center', fontfamily='monospace')
        ax2.text(3, 5.0, '5 complex dims', fontsize=8, color=BLUE_DIM,
                 ha='center', fontfamily='monospace')

        ax2.text(7, 6.5, '16', fontsize=16, fontweight='bold', color=RED,
                 ha='center', fontfamily='monospace',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#2a0a1a',
                           edgecolor=RED, linewidth=2))
        ax2.text(7, 5.9, '2\u2074 = |(Z\u2082)\u2074|', fontsize=10, color=RED_DIM,
                 ha='center', fontfamily='monospace')
        ax2.text(7, 5.4, 'even sign flips', fontsize=8, color=RED_DIM,
                 ha='center', fontfamily='monospace')
        ax2.text(7, 5.0, 'in 5 dimensions', fontsize=8, color=RED_DIM,
                 ha='center', fontfamily='monospace')

        # Further decomposition of 120
        ax2.plot([3, 1.5], [4.7, 3.8], color=BLUE, linewidth=1.5, alpha=0.4)
        ax2.plot([3, 4.5], [4.7, 3.8], color=BLUE, linewidth=1.5, alpha=0.4)

        ax2.text(1.5, 3.5, '5', fontsize=14, fontweight='bold', color=BLUE,
                 ha='center', fontfamily='monospace')
        ax2.text(1.5, 3.0, 'n\u209c', fontsize=9, color=BLUE_DIM,
                 ha='center', fontfamily='monospace')

        ax2.text(4.5, 3.5, '24', fontsize=14, fontweight='bold', color=BLUE,
                 ha='center', fontfamily='monospace')
        ax2.text(4.5, 3.0, '4! = |S\u2084|', fontsize=9, color=BLUE_DIM,
                 ha='center', fontfamily='monospace')

        # Further decomposition of 16
        ax2.plot([7, 6], [4.7, 3.8], color=RED, linewidth=1.5, alpha=0.4)
        ax2.plot([7, 8], [4.7, 3.8], color=RED, linewidth=1.5, alpha=0.4)

        ax2.text(6, 3.5, '2\u00b3=8', fontsize=11, color=RED,
                 ha='center', fontfamily='monospace')
        ax2.text(8, 3.5, '2', fontsize=11, color=RED,
                 ha='center', fontfamily='monospace')

        # Connection note
        ax2.text(2.5, 6.7, '\u00d7', fontsize=16, color=CYAN,
                 ha='center', fontfamily='monospace')

        # D_n vs B_n comparison
        ax2.text(5, 2.0, 'D\u2085 vs B\u2085:', fontsize=11, fontweight='bold',
                 color=GOLD, ha='center', fontfamily='monospace')
        ax2.text(5, 1.4, f'|W(D\u2085)| = 5! \u00d7 2\u2074 = {W_D5}  (even sign flips)',
                 fontsize=10, color=BLUE, ha='center', fontfamily='monospace')
        ax2.text(5, 0.8, f'|W(B\u2085)| = 5! \u00d7 2\u2075 = {weyl_bn(5)}  (all sign flips)',
                 fontsize=10, color=RED, ha='center', fontfamily='monospace')
        ax2.text(5, 0.2, 'Even parity from Z\u2082 identification on Shilov boundary',
                 fontsize=9, color=GREY, ha='center', fontfamily='monospace')

        # ─── Panel 3 (bottom-left): D_n SWEEP ───
        ax3 = fig.add_axes([0.06, 0.06, 0.42, 0.38])
        ax3.set_facecolor('#0d0d1a')

        ns = np.arange(1, 9)
        weyl_orders = np.array([weyl_dn(k) for k in ns])
        mass_ratios = np.array([casimir_n(k) * np.pi**k for k in ns])

        # Bar chart of |W(D_n)| with log scale
        colors_bar = ['#336699'] * 8
        colors_bar[4] = GOLD  # n=5 highlighted

        bars = ax3.bar(ns - 0.2, weyl_orders, width=0.35, color=colors_bar,
                       edgecolor='#556699', linewidth=0.5, alpha=0.85, label='|W(D_n)|')

        # Overlay mass ratios on secondary axis
        ax3b = ax3.twinx()
        colors_line = [GREEN_DIM] * 8
        colors_line[4] = GREEN
        ax3b.plot(ns, mass_ratios, 'o-', color=GREEN, linewidth=2, markersize=8,
                  markerfacecolor=GREEN, markeredgecolor='#005533', zorder=5,
                  label='(n+1)\u03c0\u207f')

        # Highlight n=5
        ax3b.plot([5], [PROTON_RATIO], 'o', markersize=14, markerfacecolor=GREEN,
                  markeredgecolor=WHITE, markeredgewidth=2, zorder=6)
        ax3b.annotate(f'{PROTON_RATIO:.1f}\n= m\u209a/m\u2091',
                      xy=(5, PROTON_RATIO), xytext=(6.5, PROTON_RATIO * 0.8),
                      fontsize=9, color=GREEN, fontfamily='monospace',
                      fontweight='bold',
                      arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

        ax3.set_yscale('log')
        ax3.set_xlabel('n (complex dimension)', fontsize=11, color=GREY,
                        fontfamily='monospace')
        ax3.set_ylabel('|W(D_n)|', fontsize=11, color=BLUE, fontfamily='monospace')
        ax3b.set_ylabel('(n+1)\u03c0\u207f', fontsize=11, color=GREEN,
                         fontfamily='monospace')
        ax3b.set_yscale('log')

        ax3.set_xticks(ns)
        ax3.tick_params(colors=GREY)
        ax3b.tick_params(colors=GREY)
        ax3.spines['bottom'].set_color(GREY)
        ax3.spines['left'].set_color(BLUE_DIM)
        ax3.spines['right'].set_color(GREEN_DIM)
        ax3.spines['top'].set_visible(False)
        ax3b.spines['bottom'].set_color(GREY)
        ax3b.spines['left'].set_color(BLUE_DIM)
        ax3b.spines['right'].set_color(GREEN_DIM)
        ax3b.spines['top'].set_visible(False)

        ax3.set_title('D_n SWEEP: Weyl orders vs mass ratios',
                       fontsize=13, fontweight='bold', color=CYAN,
                       fontfamily='monospace', pad=10)

        # Add cancellation arrows for n=5
        ax3.annotate('cancels!', xy=(5 + 0.17, weyl_orders[4]),
                     fontsize=9, color=CANCEL_RED, fontfamily='monospace',
                     fontweight='bold', ha='left')

        # ─── Panel 4 (bottom-right): E_8 CONNECTION ───
        ax4 = fig.add_axes([0.56, 0.06, 0.40, 0.38])
        ax4.set_facecolor(BG)
        ax4.axis('off')
        ax4.set_xlim(0, 10)
        ax4.set_ylim(0, 10)

        ax4.text(5, 9.5, 'E\u2088 CONNECTION', fontsize=17, fontweight='bold',
                 color='#ff88ff', ha='center', fontfamily='monospace')

        # The key equation
        ax4.text(5, 8.3, '|W(D\u2085)| / |W(B\u2082)| = 240 = |\u03a6(E\u2088)|',
                 fontsize=14, fontweight='bold', color=WHITE, ha='center',
                 fontfamily='monospace',
                 bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a0a2a',
                           edgecolor='#ff88ff', linewidth=2))

        ax4.text(5, 7.3, f'{W_D5}  /  {W_B2}  =  {E8_ROOTS}', fontsize=16,
                 fontweight='bold', color='#dd88ff', ha='center',
                 fontfamily='monospace')

        # Three boxes
        box_data = [
            (2.0, 5.5, f'|W(D\u2085)|\n= {W_D5}', BLUE, '#0a1a2a',
             'quadratic form\nsymmetry of D_IV\u2075'),
            (5.0, 5.5, f'|W(B\u2082)|\n= {W_B2}', RED, '#2a0a1a',
             'restricted root\nsystem SO\u2080(5,2)'),
            (8.0, 5.5, f'|\u03a6(E\u2088)|\n= {E8_ROOTS}', '#ff88ff', '#1a0a2a',
             'roots of E\u2088\nkissing number'),
        ]

        for bx, by, btxt, bcol, bfill, bnote in box_data:
            box = FancyBboxPatch((bx - 1.1, by - 0.6), 2.2, 1.2,
                                  boxstyle='round,pad=0.15',
                                  facecolor=bfill, edgecolor=bcol, linewidth=2)
            ax4.add_patch(box)
            ax4.text(bx, by + 0.15, btxt, fontsize=12, fontweight='bold',
                     color=bcol, ha='center', va='center', fontfamily='monospace')
            ax4.text(bx, by - 0.9, bnote, fontsize=8, color=bcol,
                     ha='center', fontfamily='monospace', alpha=0.7)

        # Division and equals signs
        ax4.text(3.5, 5.5, '\u00f7', fontsize=20, fontweight='bold',
                 color=WHITE, ha='center', va='center', fontfamily='monospace')
        ax4.text(6.5, 5.5, '=', fontsize=20, fontweight='bold',
                 color=WHITE, ha='center', va='center', fontfamily='monospace')

        # E_8 lattice properties
        ax4.text(5, 3.2, 'E\u2088 lattice properties:', fontsize=11,
                 fontweight='bold', color='#cc88ff', ha='center',
                 fontfamily='monospace')
        props = [
            'Densest packing in 8D (Viazovska, 2016)',
            'Kissing number = 240',
            'Self-dual: E\u2088 = E\u2088*',
            'dim(E\u2088) = 248 = 240 roots + 8 Cartan',
        ]
        for i, prop in enumerate(props):
            ax4.text(5, 2.5 - i * 0.5, prop, fontsize=9, color='#aa77cc',
                     ha='center', fontfamily='monospace')

        # Bottom insight
        ax4.text(5, 0.4, '1920 baryon configs = 240 E\u2088-classes \u00d7 8 B\u2082-orbits',
                 fontsize=10, fontweight='bold', color=GOLD,
                 ha='center', fontfamily='monospace',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#2a2a0a',
                           edgecolor=GOLD_DIM, linewidth=1.5))

        # Copyright
        fig.text(0.5, 0.005, '\u00a9 2026 Casey Koons  |  Claude Opus 4.6  |  Bubble Spacetime Theory',
                 fontsize=8, color='#444444', ha='center', fontfamily='monospace')

        plt.show()


# ══════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════

def main():
    """Interactive menu for the Weyl Cancellation Unfolding."""
    wc = WeylCancellation(quiet=False)

    menu = """
  ============================================
   THE WEYL CANCELLATION UNFOLDING  --  Toy 61
  ============================================
   |W(D_5)| = 1920 in two roles, perfect cancel

   1. Weyl group orders (D_1 through D_8)
   2. Hua volume formula
   3. Baryon orbit (S_5 x (Z_2)^4)
   4. The cancellation (step by step)
   5. Factorization tree (1920 = 5! x 2^4)
   6. Generalize to arbitrary D_n
   7. E_8 connection (1920/8 = 240)
   8. Weyl group table (full comparison)
   9. Summary
   0. Show visualization (4-panel)
   q. Quit
  ============================================
"""

    while True:
        print(menu)
        choice = input("  Choice: ").strip().lower()
        if choice == '1':
            wc.weyl_order()
        elif choice == '2':
            wc.hua_volume()
        elif choice == '3':
            wc.baryon_orbit()
        elif choice == '4':
            wc.cancellation()
        elif choice == '5':
            wc.factorization()
        elif choice == '6':
            try:
                n_input = input("  Enter n (default 5): ").strip()
                n_val = int(n_input) if n_input else 5
                if n_val < 1 or n_val > 20:
                    print("  Please use 1 <= n <= 20.")
                    continue
            except ValueError:
                n_val = 5
            wc.generalize(n_val)
        elif choice == '7':
            wc.e8_connection()
        elif choice == '8':
            wc.weyl_group_table()
        elif choice == '9':
            wc.summary()
        elif choice == '0':
            wc.show()
        elif choice in ('q', 'quit', 'exit'):
            print("  Goodbye.")
            break
        else:
            print("  Unknown choice. Try again.")


if __name__ == '__main__':
    main()
