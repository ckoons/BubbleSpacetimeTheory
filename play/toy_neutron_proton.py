#!/usr/bin/env python3
"""
THE NEUTRON-PROTON SPLIT  (Toy 75)
====================================
The most consequential mass difference in physics.

If Δm = m_n - m_p were negative, the proton would decay.
No hydrogen. No stars. No life. No us.

BST derivation (from BST_PartitionFunction_DeepPhysics.md):

    (m_n - m_p) / m_e = 91/36 = (7 × 13) / 6²

where:
    7  = genus of D_IV^5 = n_C + 2
    13 = N_c + 2n_C = Weinberg denominator (sin²θ_W = 3/13)
    6² = C₂² = Casimir eigenvalue squared

So  Δm = (91/36) × m_e = 1.291 MeV     (observed 1.2934 MeV → 0.18%)

The neutron has ONE more flavor link than the proton: a Hopf intersection
changes one up-quark to down-quark. That extra link costs exactly
(7 × 13) / 36 electron masses.

CI Interface:
    from toy_neutron_proton import NeutronProtonSplit
    nps = NeutronProtonSplit()
    nps.mass_difference()          # Δm = (91/36) m_e
    nps.integer_decomposition()    # 91 = 7 × 13, 36 = 6²
    nps.proton_structure()         # Z₃ baryon circuit
    nps.neutron_structure()        # Z₃ + one Hopf-modified vertex
    nps.stability_analysis()       # why Δm > 0 matters
    nps.em_self_energy()           # EM correction: 0.034 m_e
    nps.bbn_window()               # the narrow habitability window
    nps.isospin_breaking()         # S¹ fiber asymmetry → u-d split
    nps.summary()                  # key insight
    nps.show()                     # 4-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from math import factorial
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

# ═══════════════════════════════════════════════════════════════════
#  BST CONSTANTS — the five integers
# ═══════════════════════════════════════════════════════════════════

N_c   = 3                       # color charges
n_C   = 5                       # complex dimension of D_IV^5
genus = n_C + 2                 # = 7
C_2   = n_C + 1                 # = 6, Casimir eigenvalue
N_max = 137                     # Haldane channel capacity
Gamma_order = factorial(n_C) * 2**(n_C - 1)  # = 1920 = |W(D_5)|

# Wyler alpha
_vol_D = np.pi**n_C / Gamma_order
alpha  = (N_c**2 / (2**N_c * np.pi**4)) * _vol_D**(1/4)  # ~ 1/137.036

# Mass ratio
mp_over_me = C_2 * np.pi**n_C   # 6π⁵ ≈ 1836.12

# Physical units
m_e_MeV = 0.51099895            # electron mass (MeV)
m_p_MeV = mp_over_me * m_e_MeV  # proton mass from BST

# ─── THE KEY FORMULA ───
# (m_n - m_p) / m_e = 91/36 = (7 × 13) / 6²
DELTA_NUM   = genus * (N_c + 2 * n_C)   # 7 × 13 = 91
DELTA_DEN   = C_2**2                     # 6² = 36
DELTA_RATIO = DELTA_NUM / DELTA_DEN      # 91/36 ≈ 2.5278

# Neutron mass
m_n_MeV = m_p_MeV + DELTA_RATIO * m_e_MeV

# Observed values
OBS_m_p   = 938.272088          # MeV
OBS_m_n   = 939.565421          # MeV
OBS_m_e   = 0.51099895          # MeV
OBS_delta = OBS_m_n - OBS_m_p   # 1.293333 MeV

# Weinberg angle
sin2_thetaW = N_c / (N_c + 2 * n_C)  # 3/13


# ═══════════════════════════════════════════════════════════════════
#  CLASS: NeutronProtonSplit
# ═══════════════════════════════════════════════════════════════════

class NeutronProtonSplit:
    """Toy 75: The Neutron-Proton Split — the most consequential mass difference."""

    def __init__(self, quiet=False):
        self.quiet = quiet
        if not quiet:
            print()
            print("=" * 68)
            print("  THE NEUTRON-PROTON SPLIT  --  BST Toy 75")
            print("  (m_n - m_p)/m_e = 91/36 = (7 x 13) / 6^2")
            print("=" * 68)
            print(f"  D_IV^5 :  n_C = {n_C},  genus = {genus},  C_2 = {C_2}")
            print(f"  N_c = {N_c},  N_max = {N_max}")
            print(f"  alpha = 1/{1/alpha:.6f}")
            print(f"  m_p/m_e = 6pi^5 = {mp_over_me:.2f}")
            print(f"  m_p(BST) = {m_p_MeV:.3f} MeV")
            print(f"  Dm/m_e   = {DELTA_NUM}/{DELTA_DEN} = {DELTA_RATIO:.6f}")
            print(f"  Dm(BST)  = {DELTA_RATIO * m_e_MeV:.4f} MeV")
            print(f"  Dm(obs)  = {OBS_delta:.4f} MeV")
            pct = abs(DELTA_RATIO * m_e_MeV - OBS_delta) / OBS_delta * 100
            print(f"  match    = {pct:.2f}%")
            print("=" * 68)

    def _p(self, text=""):
        if not self.quiet:
            print(text)

    # ──────────────────────────────────────────────────────────────
    # 1. mass_difference
    # ──────────────────────────────────────────────────────────────

    def mass_difference(self):
        """Compute Δm = (91/36) m_e and compare to observed."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  THE MASS DIFFERENCE")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  BST formula:")
        self._p()
        self._p("    (m_n - m_p) / m_e = 91/36")
        self._p()
        self._p("  Step by step:")
        self._p(f"    numerator:   7 x 13 = {DELTA_NUM}")
        self._p(f"    denominator: 6^2    = {DELTA_DEN}")
        self._p(f"    ratio:       {DELTA_NUM}/{DELTA_DEN} = {DELTA_RATIO:.6f}")
        self._p()

        bst_delta = DELTA_RATIO * m_e_MeV
        pct = abs(bst_delta - OBS_delta) / OBS_delta * 100

        self._p(f"    Dm(BST) = ({DELTA_NUM}/{DELTA_DEN}) x {m_e_MeV} MeV")
        self._p(f"            = {bst_delta:.4f} MeV")
        self._p()
        self._p(f"    Dm(obs) = {OBS_delta:.4f} MeV")
        self._p(f"    match:    {pct:.2f}%")
        self._p()

        # Full nucleon masses
        self._p("  Full nucleon masses:")
        self._p(f"    m_p(BST) = 6pi^5 x m_e = {m_p_MeV:.3f} MeV   (obs {OBS_m_p:.3f})")
        self._p(f"    m_n(BST) = m_p + (91/36)m_e = {m_n_MeV:.3f} MeV   (obs {OBS_m_n:.3f})")
        pct_p = abs(m_p_MeV - OBS_m_p) / OBS_m_p * 100
        pct_n = abs(m_n_MeV - OBS_m_n) / OBS_m_n * 100
        self._p(f"    proton match: {pct_p:.3f}%")
        self._p(f"    neutron match: {pct_n:.3f}%")
        self._p()

        return {
            'formula': '(m_n - m_p)/m_e = 91/36 = (7 x 13) / 6^2',
            'ratio': DELTA_RATIO,
            'delta_bst_MeV': round(bst_delta, 4),
            'delta_obs_MeV': round(OBS_delta, 4),
            'precision_pct': round(pct, 2),
            'm_p_bst': round(m_p_MeV, 3),
            'm_n_bst': round(m_n_MeV, 3),
        }

    # ──────────────────────────────────────────────────────────────
    # 2. integer_decomposition
    # ──────────────────────────────────────────────────────────────

    def integer_decomposition(self):
        """Show 91 = 7 x 13, 36 = 6^2 — all BST integers."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  INTEGER DECOMPOSITION")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  91/36 = (7 x 13) / 6^2")
        self._p()
        self._p("  Every factor is a BST integer:")
        self._p()
        self._p(f"    7  = n_C + 2 = {n_C} + 2 = genus of D_IV^5")
        self._p(f"         Topological genus of the Shilov boundary")
        self._p(f"         Also: Fano number, dimensions of G_2")
        self._p()
        self._p(f"    13 = N_c + 2n_C = {N_c} + 2x{n_C} = Weinberg denominator")
        self._p(f"         sin^2(theta_W) = N_c/(N_c + 2n_C) = 3/13")
        self._p(f"         Total flavor links: 3 colors + 2x5 complex directions")
        self._p(f"         Also: c_5 in Chern class of Q^5")
        self._p()
        self._p(f"    6  = C_2 = n_C + 1 = Casimir eigenvalue")
        self._p(f"         The same 6 in m_p/m_e = 6pi^5")
        self._p(f"         6^2 = 36 appears as the squared stabilizer")
        self._p()

        # Cross-checks
        self._p("  Cross-checks:")
        self._p(f"    91 = 7 x 13 = genus x Weinberg_denom     CHECK")
        self._p(f"    36 = 6^2    = C_2^2                      CHECK")
        self._p(f"    91 is also the 13th triangular number:  T_13 = 13x14/2 = 91")
        self._p(f"    36 is the 8th triangular number:        T_8  =  8x9/2  = 36")
        self._p()

        # The 55
        kinetic_num = DELTA_NUM - DELTA_DEN  # 91 - 36 = 55
        self._p("  Kinetic energy budget:")
        self._p(f"    (m_n - m_p - m_e)/m_e = (91 - 36)/36 = {kinetic_num}/{DELTA_DEN}")
        self._p(f"                          = {kinetic_num/DELTA_DEN:.6f}")
        self._p(f"    This is the kinetic energy available in neutron beta decay")
        self._p(f"    55 = T_10 (10th triangular number) = 10x11/2")
        self._p(f"    55 = 5 x 11 = n_C x dim(K)  where K = SO(5)xSO(2)")
        self._p()

        return {
            'numerator': DELTA_NUM,
            'denominator': DELTA_DEN,
            'genus': genus,
            'weinberg_denom': N_c + 2 * n_C,
            'casimir': C_2,
            'kinetic_55': kinetic_num,
        }

    # ──────────────────────────────────────────────────────────────
    # 3. proton_structure
    # ──────────────────────────────────────────────────────────────

    def proton_structure(self):
        """Z_3 baryon circuit: 3 quarks (uud), winding number."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  PROTON STRUCTURE")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The proton is a Z_3 color circuit on the Shilov boundary S^4 x S^1.")
        self._p()
        self._p("  Quark content: u  u  d")
        self._p("  Colors:        r  g  b   (Z_3 cycle: r -> g -> b -> r)")
        self._p("  Charge:       +2/3 +2/3 -1/3 = +1")
        self._p()
        self._p("  Mass origin:")
        self._p(f"    m_p / m_e = C_2 x pi^n_C = {C_2} x pi^{n_C} = 6pi^5")
        self._p(f"    m_p = 6pi^5 x m_e = {mp_over_me:.4f} x {m_e_MeV} MeV")
        self._p(f"        = {m_p_MeV:.3f} MeV")
        self._p()
        self._p("  The Z_3 circuit:")
        self._p()
        self._p("           u (red)")
        self._p("            / \\")
        self._p("           /   \\")
        self._p("          /  p  \\")
        self._p("         /   +1  \\")
        self._p("        u(green)---d(blue)")
        self._p()
        self._p("  Each vertex is a quark. Each edge is a gluon flux tube.")
        self._p("  The winding number on S^1 gives baryon number B = 1.")
        self._p("  The circuit traverses all N_c = 3 color charges exactly once.")
        self._p()

        return {
            'quarks': ['u', 'u', 'd'],
            'colors': ['r', 'g', 'b'],
            'charge': +1,
            'mass_formula': 'm_p = 6pi^5 m_e',
            'mass_MeV': round(m_p_MeV, 3),
            'baryon_number': 1,
        }

    # ──────────────────────────────────────────────────────────────
    # 4. neutron_structure
    # ──────────────────────────────────────────────────────────────

    def neutron_structure(self):
        """Z_3 circuit + one Hopf-modified vertex."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  NEUTRON STRUCTURE")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The neutron is the proton's Z_3 circuit with ONE Hopf-modified vertex.")
        self._p()
        self._p("  Quark content: u  d  d")
        self._p("  Colors:        r  g  b   (Z_3 cycle: r -> g -> b -> r)")
        self._p("  Charge:       +2/3 -1/3 -1/3 = 0")
        self._p()
        self._p("  The Hopf modification:")
        self._p("    One u-quark vertex is replaced by a d-quark vertex.")
        self._p("    The Hopf fibration S^3 -> S^2 changes the fiber winding at")
        self._p("    that vertex, adding an extra flavor link.")
        self._p()
        self._p("  Mass formula:")
        self._p(f"    m_n = m_p + (91/36) m_e")
        self._p(f"        = 6pi^5 m_e  +  (7 x 13 / 6^2) m_e")
        self._p(f"        = {m_p_MeV:.3f} + {DELTA_RATIO * m_e_MeV:.4f} MeV")
        self._p(f"        = {m_n_MeV:.3f} MeV")
        self._p()
        self._p("  The modified circuit:")
        self._p()
        self._p("           u (red)")
        self._p("            / \\")
        self._p("           /   \\ <-- Hopf modification")
        self._p("          /  n  \\     (extra flavor link)")
        self._p("         /    0  \\")
        self._p("        d(green)---d(blue)")
        self._p()
        self._p("  The extra link costs (genus x Weinberg_denom) / C_2^2 electron masses.")
        self._p("  The numerator 91 encodes the topological (7) and electroweak (13) structure.")
        self._p("  The denominator 36 encodes the Casimir stabilizer squared.")
        self._p()

        return {
            'quarks': ['u', 'd', 'd'],
            'colors': ['r', 'g', 'b'],
            'charge': 0,
            'mass_formula': 'm_n = 6pi^5 m_e + (91/36) m_e',
            'mass_MeV': round(m_n_MeV, 3),
            'hopf_cost_me': round(DELTA_RATIO, 6),
            'hopf_cost_MeV': round(DELTA_RATIO * m_e_MeV, 4),
        }

    # ──────────────────────────────────────────────────────────────
    # 5. stability_analysis
    # ──────────────────────────────────────────────────────────────

    def stability_analysis(self):
        """Why Δm > 0 matters for hydrogen and the universe."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  STABILITY ANALYSIS: WHY Dm > 0 MATTERS")
        self._p("  " + "=" * 60)
        self._p()

        bst_delta = DELTA_RATIO * m_e_MeV

        self._p(f"  Dm = {bst_delta:.4f} MeV > 0")
        self._p()
        self._p("  CONSEQUENCE 1:  Hydrogen is stable")
        self._p("    m_n > m_p  means  the NEUTRON decays, not the proton.")
        self._p("    n -> p + e- + nu_bar_e   (beta decay)")
        self._p("    Free protons live (essentially) forever.")
        self._p("    Free hydrogen atoms are stable.")
        self._p()
        self._p("  CONSEQUENCE 2:  Stars can burn")
        self._p("    pp-chain:  p + p -> d + e+ + nu_e")
        self._p("    Requires converting a proton INTO a neutron (beta+ process).")
        self._p("    This costs Dm = 1.29 MeV per conversion.")
        self._p("    If m_n < m_p, protons would spontaneously become neutrons")
        self._p("    and there would be no hydrogen fuel for stars.")
        self._p()
        self._p("  CONSEQUENCE 3:  Chemistry exists")
        self._p("    Stable hydrogen = stable atoms = stable molecules.")
        self._p("    If protons decayed, there would be no electrons in atomic")
        self._p("    orbits, no chemical bonds, no biochemistry.")
        self._p()

        # The critical comparison
        self._p("  THE CRITICAL COMPARISON:")
        self._p(f"    Dm        = {bst_delta:.4f} MeV")
        self._p(f"    m_e       = {m_e_MeV:.4f} MeV")
        self._p(f"    Dm / m_e  = {DELTA_RATIO:.4f}")
        self._p(f"    Dm > m_e  (neutron CAN decay to proton + electron + neutrino)")
        self._p(f"    Dm - m_e  = {bst_delta - m_e_MeV:.4f} MeV  (kinetic energy available)")
        self._p()
        self._p("  If Dm < m_e = 0.511 MeV, even free neutron decay would be forbidden!")
        self._p("  BST gives Dm/m_e = 91/36 = 2.528 > 1. The universe is safe.")
        self._p()

        # Counterfactual
        self._p("  COUNTERFACTUAL UNIVERSES:")
        self._p()
        self._p("   Dm sign  │ Dm vs m_e │  Universe")
        self._p("  ──────────┼───────────┼─────────────────────────────────")
        self._p("   Dm < 0   │    --     │  Proton decays. No hydrogen. Dead.")
        self._p("   0 < Dm   │ Dm < m_e  │  Free neutrons stable. Neutron stars")
        self._p("            │           │  everywhere. Very different cosmos.")
        self._p("   0 < Dm   │ Dm > m_e  │  OUR UNIVERSE. Free neutrons decay.")
        self._p("            │           │  Hydrogen stable. Stars burn.")
        self._p(f"   {DELTA_RATIO:.3f}    │  > 1      │  <-- BST prediction (91/36)")
        self._p("  ──────────┼───────────┼─────────────────────────────────")
        self._p()

        return {
            'delta_MeV': round(bst_delta, 4),
            'delta_over_m_e': round(DELTA_RATIO, 4),
            'decay_kinetic_MeV': round(bst_delta - m_e_MeV, 4),
            'hydrogen_stable': True,
            'neutron_can_decay': True,
        }

    # ──────────────────────────────────────────────────────────────
    # 6. em_self_energy
    # ──────────────────────────────────────────────────────────────

    def em_self_energy(self):
        """EM self-energy correction: observed proton has a ~0.034 m_e residual."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  ELECTROMAGNETIC SELF-ENERGY CORRECTION")
        self._p("  " + "=" * 60)
        self._p()

        # The proton has EM self-energy from its charge
        # m_p(obs) = m_p(strong) + EM correction
        # BST: m_p(strong) = 6pi^5 m_e
        # Residual = m_p(obs) - 6pi^5 m_e

        residual_MeV = OBS_m_p - m_p_MeV
        residual_me  = residual_MeV / m_e_MeV

        self._p("  The proton mass has an electromagnetic component:")
        self._p()
        self._p("    m_p(obs) = m_p(strong) + Dm_EM")
        self._p()
        self._p("  BST gives the strong mass:")
        self._p(f"    m_p(strong) = 6pi^5 m_e = {m_p_MeV:.4f} MeV")
        self._p(f"    m_p(obs)                = {OBS_m_p:.4f} MeV")
        self._p()
        self._p(f"    Dm_EM = m_p(obs) - 6pi^5 m_e")
        self._p(f"          = {residual_MeV:.4f} MeV")
        self._p(f"          = {residual_me:.4f} m_e")
        self._p()
        self._p("  This is tiny: about 0.034 electron masses.")
        self._p("  The 6pi^5 formula gets 99.998% of the proton mass from geometry alone.")
        self._p()

        # EM correction estimate from alpha
        em_est = alpha * m_p_MeV * N_c / (2 * np.pi * C_2)
        self._p("  BST estimate of EM self-energy:")
        self._p(f"    Dm_EM ~ alpha x m_p x N_c / (2pi x C_2)")
        self._p(f"         ~ {alpha:.6f} x {m_p_MeV:.1f} x {N_c} / (2pi x {C_2})")
        self._p(f"         ~ {em_est:.4f} MeV")
        self._p(f"    (Order-of-magnitude check: {em_est:.3f} vs {residual_MeV:.3f} MeV)")
        self._p()

        # The neutron has ZERO charge, so its EM self-energy is different
        n_residual_MeV = OBS_m_n - m_n_MeV
        n_residual_me  = n_residual_MeV / m_e_MeV

        self._p("  Neutron EM correction:")
        self._p(f"    m_n(BST) = m_p(strong) + (91/36)m_e = {m_n_MeV:.4f} MeV")
        self._p(f"    m_n(obs)                            = {OBS_m_n:.4f} MeV")
        self._p(f"    residual = {n_residual_MeV:.4f} MeV = {n_residual_me:.4f} m_e")
        self._p()
        self._p("  The neutron is charge-neutral but has internal charge distribution")
        self._p("  (positive core, negative surface), contributing to its EM self-energy.")
        self._p()

        return {
            'proton_residual_MeV': round(residual_MeV, 4),
            'proton_residual_me': round(residual_me, 4),
            'neutron_residual_MeV': round(n_residual_MeV, 4),
            'neutron_residual_me': round(n_residual_me, 4),
            'em_estimate_MeV': round(em_est, 4),
        }

    # ──────────────────────────────────────────────────────────────
    # 7. bbn_window
    # ──────────────────────────────────────────────────────────────

    def bbn_window(self):
        """The narrow BBN window: too small Δm = no H, too large = no He."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  THE BBN HABITABILITY WINDOW")
        self._p("  " + "=" * 60)
        self._p()

        bst_delta = DELTA_RATIO * m_e_MeV

        self._p("  Big Bang Nucleosynthesis (t = 1-180 seconds after Big Bang)")
        self._p("  requires Dm to be in a NARROW WINDOW.")
        self._p()
        self._p("  The n/p freeze-out ratio:")
        self._p("    At T_freeze ~ 0.7 MeV, weak interactions freeze out.")
        self._p("    n/p = exp(-Dm / T_freeze)")
        self._p()

        T_freeze = 0.7  # MeV, approximate
        np_ratio = np.exp(-bst_delta / T_freeze)
        self._p(f"    With Dm = {bst_delta:.4f} MeV:")
        self._p(f"      n/p = exp(-{bst_delta:.3f} / {T_freeze}) = {np_ratio:.4f}")
        self._p(f"      For every {1/np_ratio:.1f} protons, there is 1 neutron.")
        self._p()

        # Helium abundance
        # Y_p ~ 2(n/p) / (1 + n/p) with some neutron decay correction
        Y_p = 2 * np_ratio / (1 + np_ratio) * 0.886  # ~decay correction
        self._p(f"    Helium mass fraction Y_p ~ {Y_p:.3f}  (observed ~0.245)")
        self._p()

        self._p("  THE WINDOW (approximate):")
        self._p()
        self._p("    Dm (MeV)  │  n/p freeze  │  Y_p    │  Universe")
        self._p("   ───────────┼──────────────┼─────────┼──────────────────────")

        test_deltas = [0.0, 0.3, 0.5, 0.8, 1.0, OBS_delta, 2.0, 3.0, 5.0]
        for dm in test_deltas:
            r = np.exp(-dm / T_freeze)
            yp = 2 * r / (1 + r) * 0.886
            if dm < m_e_MeV:
                note = "neutrons stable!" if dm < 0.01 else "n stable or slow decay"
            elif dm < 0.8:
                note = "too much He, little H"
            elif dm > 4.0:
                note = "all n decay, no He"
            elif dm > 2.5:
                note = "very little He"
            elif abs(dm - OBS_delta) < 0.01:
                note = "<-- OUR UNIVERSE"
            elif dm < 1.5:
                note = "habitable zone"
            else:
                note = "marginal"

            marker = "  ***" if abs(dm - OBS_delta) < 0.01 else ""
            self._p(f"    {dm:>6.3f}    │    {r:.4f}     │  {yp:.3f}  │  {note}{marker}")

        self._p("   ───────────┼──────────────┼─────────┼──────────────────────")
        self._p()
        self._p("  BST controls the window via genus x Weinberg / C_2^2:")
        self._p(f"    Dm = (7 x 13 / 36) x m_e = {bst_delta:.4f} MeV")
        self._p(f"    The SAME integers that set sin^2(theta_W) and m_p/m_e")
        self._p(f"    also set the neutron-proton split.")
        self._p()
        self._p("  The universe's habitability is not a tuned coincidence.")
        self._p("  It is locked by the topology of D_IV^5.")
        self._p()

        return {
            'delta_MeV': round(bst_delta, 4),
            'T_freeze_MeV': T_freeze,
            'np_ratio': round(np_ratio, 4),
            'He_fraction': round(Y_p, 3),
        }

    # ──────────────────────────────────────────────────────────────
    # 8. isospin_breaking
    # ──────────────────────────────────────────────────────────────

    def isospin_breaking(self):
        """S^1 fiber asymmetry gives u-d mass difference."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  ISOSPIN BREAKING: S^1 FIBER ASYMMETRY")
        self._p("  " + "=" * 60)
        self._p()

        # Quark masses from BST (same as atom_assembler)
        m_u = N_c * np.sqrt(2) * m_e_MeV           # 3sqrt(2) m_e ~ 2.17 MeV
        m_d_over_u = (N_c + 2 * n_C) / C_2         # 13/6
        m_d = m_d_over_u * m_u                      # ~ 4.70 MeV
        ud_diff = m_d - m_u

        self._p("  In exact isospin symmetry, u and d quarks have equal mass.")
        self._p("  Nature breaks this symmetry: m_d > m_u.")
        self._p()
        self._p("  BST mechanism: S^1 fiber asymmetry on the Shilov boundary.")
        self._p()
        self._p("  The Shilov boundary of D_IV^5 is S^4 x S^1.")
        self._p("  S^4 carries the N_c = 3 color directions (isotropic).")
        self._p("  S^1 carries the compact phase (anisotropic: one direction).")
        self._p()
        self._p("  Quark masses from BST:")
        self._p(f"    m_u = N_c x sqrt(2) x m_e = {N_c} x sqrt(2) x m_e")
        self._p(f"        = {m_u:.4f} MeV   (obs ~ 2.16 MeV)")
        self._p()
        self._p(f"    m_d / m_u = (N_c + 2n_C) / C_2 = {N_c + 2*n_C}/{C_2} = {m_d_over_u:.4f}")
        self._p(f"    m_d = {m_d:.4f} MeV   (obs ~ 4.67 MeV)")
        self._p()
        self._p(f"    m_d - m_u = {ud_diff:.4f} MeV")
        self._p()
        self._p("  The 13/6 ratio:")
        self._p(f"    13 = N_c + 2n_C = Weinberg denominator")
        self._p(f"     6 = C_2 = Casimir eigenvalue")
        self._p(f"    This is the SAME 13 and 6 in the neutron-proton split!")
        self._p()
        self._p("  Connection to the mass difference:")
        self._p(f"    The neutron has two d-quarks and one u-quark (udd).")
        self._p(f"    The proton has two u-quarks and one d-quark (uud).")
        self._p(f"    Naive quark mass difference: m_d - m_u = {ud_diff:.2f} MeV")
        self._p(f"    But the full n-p split is {DELTA_RATIO * m_e_MeV:.2f} MeV")
        self._p(f"    because confinement + EM effects modify the bare quark masses.")
        self._p()
        self._p("  The physical interpretation:")
        self._p("    - Isospin is an approximate symmetry of S^4 (the large sphere)")
        self._p("    - It is broken by S^1 (the compact fiber)")
        self._p("    - The breaking ratio is 13/6 = (N_c + 2n_C) / C_2")
        self._p("    - This ratio appears in BOTH the quark mass ratio AND sin^2(theta_W)")
        self._p("    - Electroweak symmetry breaking and isospin breaking have")
        self._p("      the SAME geometric origin: the S^1 fiber.")
        self._p()

        return {
            'm_u_MeV': round(m_u, 4),
            'm_d_MeV': round(m_d, 4),
            'md_over_mu': round(m_d_over_u, 4),
            'ud_diff_MeV': round(ud_diff, 4),
            'origin': 'S^1 fiber asymmetry on Shilov boundary S^4 x S^1',
        }

    # ──────────────────────────────────────────────────────────────
    # 9. summary
    # ──────────────────────────────────────────────────────────────

    def summary(self):
        """Key insight: the neutron-proton split is set by BST topology."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  SUMMARY: THE NEUTRON-PROTON SPLIT")
        self._p("  " + "=" * 60)
        self._p()

        bst_delta = DELTA_RATIO * m_e_MeV
        pct = abs(bst_delta - OBS_delta) / OBS_delta * 100

        self._p("  The most consequential mass difference in physics:")
        self._p()
        self._p(f"    (m_n - m_p) / m_e = 91/36 = (7 x 13) / 6^2")
        self._p()
        self._p(f"    = (genus x Weinberg_denom) / C_2^2")
        self._p()
        self._p(f"    = {bst_delta:.4f} MeV   (observed {OBS_delta:.4f} MeV,  {pct:.2f}%)")
        self._p()
        self._p("  Every integer is a BST constant:")
        self._p(f"    7  = genus = n_C + 2")
        self._p(f"    13 = Weinberg denominator = N_c + 2n_C")
        self._p(f"    6  = Casimir eigenvalue = C_2 = n_C + 1")
        self._p()
        self._p("  The SAME 6 that makes m_p/m_e = 6pi^5")
        self._p("  The SAME 13 that makes sin^2(theta_W) = 3/13")
        self._p("  The SAME 7 that makes v = m_p^2/(7 m_e)")
        self._p()
        self._p("  If this number were negative: no hydrogen.")
        self._p("  If too large: no helium at BBN.")
        self._p("  If too small: neutrons stable (different cosmos).")
        self._p()
        self._p("  BST says: these are not tunable parameters.")
        self._p("  They are LOCKED by the topology of D_IV^5.")
        self._p("  The universe MUST have stable hydrogen.")
        self._p("  The neutron MUST decay.")
        self._p("  The Goldilocks window is not fine-tuning -- it is geometry.")
        self._p()

        return {
            'formula': '(m_n - m_p)/m_e = 91/36 = (7 x 13)/6^2',
            'delta_MeV': round(bst_delta, 4),
            'match_pct': round(pct, 2),
            'insight': 'Habitability locked by D_IV^5 topology, not fine-tuning.',
        }

    # ──────────────────────────────────────────────────────────────
    # 10. show  --  4-panel visualization
    # ──────────────────────────────────────────────────────────────

    def show(self):
        """4-panel visualization of the neutron-proton split."""

        BG       = '#0a0a1a'
        GOLD     = '#ffaa00'
        GOLD_DIM = '#aa8800'
        BLUE     = '#4488ff'
        BLUE_DIM = '#336699'
        RED      = '#ff4488'
        RED_DIM  = '#cc3366'
        GREEN    = '#00ff88'
        GREEN_DIM = '#00aa66'
        WHITE    = '#ffffff'
        GREY     = '#888888'
        CYAN     = '#44ddff'
        ORANGE   = '#ff8800'
        PURPLE   = '#bb88ff'
        PURPLE_DIM = '#8855cc'

        fig = plt.figure(figsize=(17, 12), facecolor=BG)
        fig.canvas.manager.set_window_title(
            'The Neutron-Proton Split -- BST Toy 75')

        # Main title
        fig.text(0.5, 0.975, 'THE NEUTRON-PROTON SPLIT',
                 fontsize=26, fontweight='bold', color=GOLD, ha='center',
                 fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=2, foreground='#442200')])
        fig.text(0.5, 0.950,
                 '(m_n - m_p)/m_e = 91/36 = (7 x 13) / 6^2   --   '
                 'the most consequential mass difference',
                 fontsize=11, color=GOLD_DIM, ha='center', fontfamily='monospace')

        bst_delta = DELTA_RATIO * m_e_MeV
        pct = abs(bst_delta - OBS_delta) / OBS_delta * 100

        # ─── Panel 1 (top-left): THE FORMULA ───
        ax1 = fig.add_axes([0.02, 0.50, 0.48, 0.43])
        ax1.set_facecolor(BG)
        ax1.axis('off')
        ax1.set_xlim(0, 10)
        ax1.set_ylim(0, 10)

        ax1.text(5, 9.5, 'THE MASS DIFFERENCE', fontsize=17,
                 fontweight='bold', color=GOLD, ha='center',
                 fontfamily='monospace')

        # Formula
        ax1.text(5, 8.5, '(m_n - m_p) / m_e  =  91 / 36',
                 fontsize=14, color=WHITE, ha='center', fontfamily='monospace',
                 fontweight='bold')

        # Decomposition
        ax1.text(5, 7.5, '= (7 x 13) / 6\u00b2',
                 fontsize=16, color=ORANGE, ha='center', fontfamily='monospace',
                 fontweight='bold')

        # Three labeled boxes for 7, 13, 6
        box_data = [
            (2.0, 6.0, '7', CYAN, '#0a1a2a',
             'genus\nn_C + 2'),
            (5.0, 6.0, '13', PURPLE, '#1a0a2a',
             'Weinberg\nN_c + 2n_C'),
            (8.0, 6.0, '6\u00b2=36', RED, '#2a0a1a',
             'Casimir\u00b2\nC_2\u00b2'),
        ]

        for bx, by, btxt, bcol, bfill, bnote in box_data:
            box = FancyBboxPatch((bx - 0.9, by - 0.5), 1.8, 1.0,
                                  boxstyle='round,pad=0.15',
                                  facecolor=bfill, edgecolor=bcol,
                                  linewidth=2)
            ax1.add_patch(box)
            ax1.text(bx, by + 0.1, btxt, fontsize=14, fontweight='bold',
                     color=bcol, ha='center', va='center',
                     fontfamily='monospace')
            ax1.text(bx, by - 0.75, bnote, fontsize=9, color=bcol,
                     ha='center', fontfamily='monospace', alpha=0.7)

        # Multiply and divide symbols
        ax1.text(3.5, 6.0, '\u00d7', fontsize=18, fontweight='bold',
                 color=WHITE, ha='center', va='center', fontfamily='monospace')
        ax1.text(6.5, 6.0, '\u00f7', fontsize=18, fontweight='bold',
                 color=WHITE, ha='center', va='center', fontfamily='monospace')

        # Result box
        box_result = FancyBboxPatch((1.5, 3.0), 7.0, 1.5,
                                     boxstyle='round,pad=0.2',
                                     facecolor='#0a2a1a',
                                     edgecolor=GREEN, linewidth=2.5)
        ax1.add_patch(box_result)
        ax1.text(5, 3.95, f'\u0394m = (91/36) x m_e = {bst_delta:.4f} MeV',
                 fontsize=14, fontweight='bold', color=GREEN, ha='center',
                 fontfamily='monospace')
        ax1.text(5, 3.35, f'observed: {OBS_delta:.4f} MeV   match: {pct:.2f}%',
                 fontsize=11, color=GREEN_DIM, ha='center',
                 fontfamily='monospace')

        # Cross-connections
        ax1.text(5, 2.2, 'Same 6 as m_p/m_e = 6\u03c0\u2075', fontsize=9,
                 color=RED_DIM, ha='center', fontfamily='monospace')
        ax1.text(5, 1.7, 'Same 13 as sin\u00b2\u03b8_W = 3/13', fontsize=9,
                 color=PURPLE_DIM, ha='center', fontfamily='monospace')
        ax1.text(5, 1.2, 'Same 7 as v = m_p\u00b2/(7 m_e)', fontsize=9,
                 color=CYAN, ha='center', fontfamily='monospace', alpha=0.6)

        ax1.text(5, 0.4, 'ALL from D_IV\u2075 topology -- no free parameters',
                 fontsize=10, fontweight='bold', color=GOLD_DIM, ha='center',
                 fontfamily='monospace')

        # ─── Panel 2 (top-right): BARYON CIRCUITS ───
        ax2 = fig.add_axes([0.52, 0.50, 0.46, 0.43])
        ax2.set_facecolor(BG)
        ax2.axis('off')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 10)

        ax2.text(5, 9.5, 'PROTON vs NEUTRON', fontsize=17,
                 fontweight='bold', color=CYAN, ha='center',
                 fontfamily='monospace')

        # ── Proton triangle (left side) ──
        px, py = 2.5, 6.5  # center
        pr = 1.5            # radius
        # Triangle vertices
        p_verts = []
        for i in range(3):
            angle = np.pi/2 + 2*np.pi*i/3
            p_verts.append((px + pr*np.cos(angle), py + pr*np.sin(angle)))

        # Draw edges (gluon tubes)
        for i in range(3):
            j = (i + 1) % 3
            ax2.plot([p_verts[i][0], p_verts[j][0]],
                     [p_verts[i][1], p_verts[j][1]],
                     color=BLUE, linewidth=3, alpha=0.6)

        # Draw vertices (quarks)
        quark_colors_p = ['#ff4444', '#44ff44', '#4444ff']  # RGB for r,g,b
        quark_labels_p = ['u', 'u', 'd']
        color_labels_p = ['r', 'g', 'b']
        for i, (vx, vy) in enumerate(p_verts):
            circle = Circle((vx, vy), 0.3, facecolor=quark_colors_p[i],
                           edgecolor=WHITE, linewidth=2, alpha=0.8)
            ax2.add_patch(circle)
            ax2.text(vx, vy, quark_labels_p[i], fontsize=12,
                     fontweight='bold', color=WHITE, ha='center',
                     va='center', fontfamily='monospace')
            ax2.text(vx + 0.4 * np.cos(np.pi/2 + 2*np.pi*i/3),
                     vy + 0.4 * np.sin(np.pi/2 + 2*np.pi*i/3),
                     color_labels_p[i], fontsize=8, color=GREY,
                     ha='center', fontfamily='monospace')

        ax2.text(px, py - 0.15, 'p', fontsize=14, fontweight='bold',
                 color=WHITE, ha='center', va='center', fontfamily='monospace')
        ax2.text(px, py + 0.25, '+1', fontsize=10, color=GOLD,
                 ha='center', fontfamily='monospace')

        ax2.text(px, 4.5, 'PROTON', fontsize=13, fontweight='bold',
                 color=BLUE, ha='center', fontfamily='monospace')
        ax2.text(px, 4.0, f'm_p = 6\u03c0\u2075 m_e', fontsize=10,
                 color=BLUE_DIM, ha='center', fontfamily='monospace')
        ax2.text(px, 3.5, f'= {m_p_MeV:.3f} MeV', fontsize=10,
                 color=BLUE_DIM, ha='center', fontfamily='monospace')

        # ── Neutron triangle (right side) ──
        nx, ny = 7.5, 6.5
        n_verts = []
        for i in range(3):
            angle = np.pi/2 + 2*np.pi*i/3
            n_verts.append((nx + pr*np.cos(angle), ny + pr*np.sin(angle)))

        # Draw edges
        for i in range(3):
            j = (i + 1) % 3
            lw = 3
            col = RED if (i == 0) else BLUE  # highlight the Hopf edge
            al = 0.8 if (i == 0) else 0.6
            ax2.plot([n_verts[i][0], n_verts[j][0]],
                     [n_verts[i][1], n_verts[j][1]],
                     color=col, linewidth=lw, alpha=al)

        # Mark the Hopf modification
        hopf_mx = (n_verts[0][0] + n_verts[1][0]) / 2
        hopf_my = (n_verts[0][1] + n_verts[1][1]) / 2
        ax2.text(hopf_mx + 0.5, hopf_my + 0.3, 'Hopf', fontsize=8,
                 fontweight='bold', color=RED, ha='center',
                 fontfamily='monospace')
        ax2.annotate('', xy=(hopf_mx + 0.1, hopf_my + 0.05),
                     xytext=(hopf_mx + 0.45, hopf_my + 0.2),
                     arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

        # Draw vertices (quarks)
        quark_colors_n = ['#ff4444', '#44ff44', '#4444ff']
        quark_labels_n = ['u', 'd', 'd']
        color_labels_n = ['r', 'g', 'b']
        for i, (vx, vy) in enumerate(n_verts):
            circle = Circle((vx, vy), 0.3, facecolor=quark_colors_n[i],
                           edgecolor=WHITE, linewidth=2, alpha=0.8)
            ax2.add_patch(circle)
            ax2.text(vx, vy, quark_labels_n[i], fontsize=12,
                     fontweight='bold', color=WHITE, ha='center',
                     va='center', fontfamily='monospace')
            ax2.text(vx + 0.4 * np.cos(np.pi/2 + 2*np.pi*i/3),
                     vy + 0.4 * np.sin(np.pi/2 + 2*np.pi*i/3),
                     color_labels_n[i], fontsize=8, color=GREY,
                     ha='center', fontfamily='monospace')

        ax2.text(nx, ny - 0.15, 'n', fontsize=14, fontweight='bold',
                 color=WHITE, ha='center', va='center', fontfamily='monospace')
        ax2.text(nx, ny + 0.25, ' 0', fontsize=10, color=GREY,
                 ha='center', fontfamily='monospace')

        ax2.text(nx, 4.5, 'NEUTRON', fontsize=13, fontweight='bold',
                 color=RED, ha='center', fontfamily='monospace')
        ax2.text(nx, 4.0, 'm_n = m_p + (91/36)m_e', fontsize=10,
                 color=RED_DIM, ha='center', fontfamily='monospace')
        ax2.text(nx, 3.5, f'= {m_n_MeV:.3f} MeV', fontsize=10,
                 color=RED_DIM, ha='center', fontfamily='monospace')

        # Arrow between the two with delta
        ax2.annotate('', xy=(5.5, 6.5), xytext=(4.5, 6.5),
                     arrowprops=dict(arrowstyle='->', color=GOLD,
                                     lw=2.5))
        ax2.text(5.0, 7.0, f'+{bst_delta:.3f}', fontsize=10,
                 fontweight='bold', color=GOLD, ha='center',
                 fontfamily='monospace')
        ax2.text(5.0, 6.6, 'MeV', fontsize=8, color=GOLD_DIM,
                 ha='center', fontfamily='monospace')

        # Key differences
        ax2.text(5, 2.7, 'ONE Hopf-modified vertex', fontsize=11,
                 fontweight='bold', color=GOLD, ha='center',
                 fontfamily='monospace')
        ax2.text(5, 2.1, 'u \u2192 d flips charge by -1', fontsize=10,
                 color=GREY, ha='center', fontfamily='monospace')
        ax2.text(5, 1.5, 'costs (7\u00d713)/6\u00b2 = 91/36 electron masses',
                 fontsize=10, color=GREY, ha='center', fontfamily='monospace')
        ax2.text(5, 0.7, 'n \u2192 p + e\u207b + \u03bd\u0304_e   (beta decay)',
                 fontsize=11, fontweight='bold', color=GREEN, ha='center',
                 fontfamily='monospace')

        # ─── Panel 3 (bottom-left): BBN WINDOW ───
        ax3 = fig.add_axes([0.06, 0.06, 0.42, 0.38])
        ax3.set_facecolor('#0d0d1a')

        # Plot He abundance vs Dm
        dm_range = np.linspace(0.01, 5.0, 200)
        T_freeze = 0.7  # MeV
        np_ratios = np.exp(-dm_range / T_freeze)
        Y_p = 2 * np_ratios / (1 + np_ratios) * 0.886

        ax3.fill_between(dm_range, 0, 1, where=(dm_range < m_e_MeV),
                          color='#440000', alpha=0.3, label='n stable')
        ax3.fill_between(dm_range, 0, 1, where=(dm_range > 3.0),
                          color='#000044', alpha=0.3, label='no He')
        ax3.fill_between(dm_range, 0, 1,
                          where=(dm_range > m_e_MeV) & (dm_range < 3.0),
                          color='#003300', alpha=0.15, label='habitable')

        ax3.plot(dm_range, Y_p, color=CYAN, linewidth=2.5)

        # Mark BST prediction
        bst_Y = 2 * np.exp(-bst_delta / T_freeze) / (1 + np.exp(-bst_delta / T_freeze)) * 0.886
        ax3.plot([bst_delta], [bst_Y], 'o', markersize=12,
                 markerfacecolor=GOLD, markeredgecolor=WHITE,
                 markeredgewidth=2, zorder=5)
        ax3.annotate(f'BST: {bst_delta:.3f} MeV\nY_p = {bst_Y:.3f}',
                     xy=(bst_delta, bst_Y),
                     xytext=(bst_delta + 1.0, bst_Y + 0.15),
                     fontsize=9, color=GOLD, fontfamily='monospace',
                     fontweight='bold',
                     arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

        # Mark observed
        ax3.axhline(y=0.245, color=GREEN, linewidth=1, linestyle='--',
                     alpha=0.5)
        ax3.text(4.3, 0.255, 'obs Y_p ~ 0.245', fontsize=8, color=GREEN_DIM,
                 fontfamily='monospace')

        # Mark m_e threshold
        ax3.axvline(x=m_e_MeV, color=RED, linewidth=1.5, linestyle=':',
                     alpha=0.7)
        ax3.text(m_e_MeV + 0.05, 0.85, 'm_e', fontsize=9, color=RED,
                 fontfamily='monospace', fontweight='bold')

        # Labels for danger zones
        ax3.text(0.2, 0.92, 'DEAD\nn stable', fontsize=9,
                 fontweight='bold', color='#ff4444', fontfamily='monospace',
                 ha='center')
        ax3.text(4.2, 0.08, 'DEAD\nno He', fontsize=9,
                 fontweight='bold', color='#4444ff', fontfamily='monospace',
                 ha='center')

        ax3.set_xlabel('\u0394m = m_n - m_p  (MeV)', fontsize=11,
                        color=GREY, fontfamily='monospace')
        ax3.set_ylabel('Helium mass fraction Y_p', fontsize=11,
                        color=GREY, fontfamily='monospace')
        ax3.set_title('BBN HABITABILITY WINDOW', fontsize=13,
                       fontweight='bold', color=CYAN, fontfamily='monospace',
                       pad=10)
        ax3.set_ylim(0, 1.0)
        ax3.set_xlim(0, 5.0)

        ax3.tick_params(colors=GREY)
        for spine in ax3.spines.values():
            spine.set_color(GREY)
            spine.set_alpha(0.3)

        # ─── Panel 4 (bottom-right): INTEGER WEB ───
        ax4 = fig.add_axes([0.56, 0.06, 0.40, 0.38])
        ax4.set_facecolor(BG)
        ax4.axis('off')
        ax4.set_xlim(0, 10)
        ax4.set_ylim(0, 10)

        ax4.text(5, 9.5, 'THE INTEGER WEB', fontsize=17,
                 fontweight='bold', color=PURPLE, ha='center',
                 fontfamily='monospace')

        ax4.text(5, 8.7, 'One set of integers controls everything',
                 fontsize=10, color=PURPLE_DIM, ha='center',
                 fontfamily='monospace')

        # Central integer display
        ints_data = [
            # (x, y, label, value, color, connections)
            (5.0, 7.5, 'n_C', '5', WHITE),
            (2.0, 6.0, 'N_c', '3', BLUE),
            (8.0, 6.0, 'genus', '7', CYAN),
            (3.0, 4.0, 'C_2', '6', RED),
            (7.0, 4.0, '13', '13', PURPLE),
        ]

        for ix, iy, ilbl, ival, icol in ints_data:
            box = FancyBboxPatch((ix - 0.65, iy - 0.35), 1.3, 0.7,
                                  boxstyle='round,pad=0.1',
                                  facecolor='#0d0d2a',
                                  edgecolor=icol, linewidth=1.5)
            ax4.add_patch(box)
            ax4.text(ix, iy + 0.05, f'{ilbl}={ival}', fontsize=10,
                     fontweight='bold', color=icol, ha='center',
                     va='center', fontfamily='monospace')

        # Draw connections (derivations)
        connections = [
            (5.0, 7.1, 2.0, 6.4, GREY),   # n_C -> N_c (derived)
            (5.0, 7.1, 8.0, 6.4, GREY),   # n_C -> genus
            (5.0, 7.1, 3.0, 4.4, GREY),   # n_C -> C_2
            (2.0, 5.6, 7.0, 4.4, GREY),   # N_c -> 13
            (5.0, 7.1, 7.0, 4.4, GREY),   # n_C -> 13
        ]
        for x1, y1, x2, y2, col in connections:
            ax4.plot([x1, x2], [y1, y2], color=col, linewidth=1,
                     alpha=0.4, linestyle='--')

        # Physics results from these integers
        results = [
            (1.5, 2.8, 'm_p/m_e = 6\u03c0\u2075', RED_DIM, 'C_2 = 6'),
            (5.0, 2.8, '\u0394m/m_e = 91/36', GOLD, '7\u00d713/6\u00b2'),
            (8.5, 2.8, 'sin\u00b2\u03b8_W = 3/13', PURPLE_DIM, 'N_c/(N_c+2n_C)'),
            (3.0, 1.5, 'v = m_p\u00b2/(7m_e)', CYAN, 'genus = 7'),
            (7.0, 1.5, '\u03b1 \u2248 1/137', GREEN_DIM, 'Wyler formula'),
        ]

        for rx, ry, rlbl, rcol, rnote in results:
            ax4.text(rx, ry, rlbl, fontsize=9, fontweight='bold',
                     color=rcol, ha='center', fontfamily='monospace')
            ax4.text(rx, ry - 0.4, rnote, fontsize=7, color=GREY,
                     ha='center', fontfamily='monospace')

        # Bottom message
        ax4.text(5, 0.3,
                 'NOT fine-tuning -- TOPOLOGY.',
                 fontsize=12, fontweight='bold', color=GOLD, ha='center',
                 fontfamily='monospace',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#2a2a0a',
                           edgecolor=GOLD_DIM, linewidth=1.5))

        # Copyright
        fig.text(0.5, 0.005,
                 '\u00a9 2026 Casey Koons  |  Claude Opus 4.6  |  '
                 'Bubble Spacetime Theory',
                 fontsize=8, color='#444444', ha='center',
                 fontfamily='monospace')

        plt.show()


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    """Interactive menu for the Neutron-Proton Split."""
    nps = NeutronProtonSplit(quiet=False)

    menu = """
  ============================================
   THE NEUTRON-PROTON SPLIT  --  Toy 75
  ============================================
   91/36 = (7 x 13) / 6^2  --  one number,
   one universe

   1. Mass difference (91/36 m_e)
   2. Integer decomposition (7, 13, 6)
   3. Proton structure (Z_3 circuit)
   4. Neutron structure (Hopf vertex)
   5. Stability analysis (why Dm > 0)
   6. EM self-energy correction
   7. BBN habitability window
   8. Isospin breaking (S^1 fiber)
   9. Summary
   0. Show visualization (4-panel)
   q. Quit
  ============================================
"""

    while True:
        print(menu)
        choice = input("  Choice: ").strip().lower()
        if choice == '1':
            nps.mass_difference()
        elif choice == '2':
            nps.integer_decomposition()
        elif choice == '3':
            nps.proton_structure()
        elif choice == '4':
            nps.neutron_structure()
        elif choice == '5':
            nps.stability_analysis()
        elif choice == '6':
            nps.em_self_energy()
        elif choice == '7':
            nps.bbn_window()
        elif choice == '8':
            nps.isospin_breaking()
        elif choice == '9':
            nps.summary()
        elif choice == '0':
            nps.show()
        elif choice in ('q', 'quit', 'exit'):
            print("  Goodbye.")
            break
        else:
            print("  Unknown choice. Try again.")


if __name__ == '__main__':
    main()
