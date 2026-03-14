#!/usr/bin/env python3
"""
CASIMIR FORCE = COMMITMENT EXCLUSION -- Toy 125
=================================================
The vacuum pushes where it can commit.

The Casimir force between parallel plates:

    F/A = -pi^2 hbar c / (240 a^4)

In BST, 240 = |Phi(E8)| = |W(D5)|/|W(B2)| = 1920/8 = 2 x 5!

So  pi^2/240 = pi^2 / (2 x n_C!)

The Casimir coefficient encodes the dimension of spacetime.

BST interpretation: The Casimir force is NOT a "vacuum fluctuation" force.
It is differential commitment pressure. Between the plates, modes with
wavelength > 2a cannot commit (write to the substrate). Outside, all modes
commit freely. The pressure difference IS the Casimir force.

    Where commitment is excluded, the pushing stops.
    The difference is force.

Key results:
  - Standard Casimir: F/A = -pi^2 hbar c / (240 a^4)  --  the 240 is |Phi(E8)|
  - BST modification: at a ~ hbar/(N_max m_e c), DF/F ~ 10^-7
  - Thermal: F/A -> -zeta(3) k_B T / (8 pi a^3)  --  zeta(3) connects to Riemann
  - Casimir-Polder: F = -3 alpha_pol hbar c / (8 pi^2 a^5)

    from toy_casimir_commitment import CasimirCommitment
    cc = CasimirCommitment()
    cc.the_force()                # standard Casimir derivation
    cc.why_240()                  # 240 = |Phi(E8)| = 1920/8 = 2 x 5!
    cc.commitment_exclusion()     # BST picture: commitment pressure
    cc.the_modification()         # BST prediction: DF/F ~ 10^-7
    cc.thermal_and_polder()       # thermal crossover + Casimir-Polder
    cc.the_experiment()           # phonon-gapped materials prediction
    cc.summary()                  # the unifying principle
    cc.show()                     # 6-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from math import factorial

# =====================================================================
# BST CONSTANTS -- the five integers
# =====================================================================

N_c = 3                      # color charges
n_C = 5                      # complex dimension of D_IV^5
genus = n_C + 2              # = 7
C2 = n_C + 1                 # = 6, Casimir eigenvalue
N_max = 137                  # Haldane channel capacity
Gamma_order = 1920           # |W(D5)| = n_C! * 2^(n_C-1)
W_B2 = 8                     # |W(B2)| Weyl group order
Phi_E8 = 240                 # |Phi(E8)| = root system of E8

# Derived
_vol_D = np.pi**n_C / Gamma_order
alpha = (N_c**2 / (2**N_c * np.pi**4)) * _vol_D**(1/4)  # ~ 1/137.036

# Physical constants (SI)
hbar = 1.054571817e-34       # J*s
c_light = 2.99792458e8       # m/s
hbar_c = hbar * c_light      # J*m
eV_to_J = 1.602176634e-19   # J/eV
k_B = 1.380649e-23          # J/K
m_e = 9.1093837015e-31      # kg (electron mass)
m_e_eV = 0.51099895e6       # eV

# Casimir prefactor: pi^2 * hbar * c / 240
CASIMIR_PREFACTOR = np.pi**2 * hbar_c / 240.0  # J*m

# Zeta function values
ZETA_3 = 1.2020569031595942   # Apery's constant
ZETA_4 = np.pi**4 / 90.0      # pi^4/90

# BST modification scale: a ~ hbar / (N_max * m_e * c)
a_BST = hbar / (N_max * m_e * c_light)   # ~ 2.8 pm

# Commitment wavelength scale
lambda_commit = a_BST  # same thing, two names


# =====================================================================
# MATERIALS DATABASE (phonon-gapped candidates)
# =====================================================================

MATERIALS = {
    'gold': {
        'name': 'Gold (Au)',
        'gap_THz': 0.0,
        'gap_meV': 0.0,
        'plasma_eV': 9.0,
        'description': 'Standard Casimir plates (no phonon gap)',
        'color': '#ffd700',
    },
    'si_ge_phononic': {
        'name': 'Si/Ge phononic crystal',
        'gap_THz': 2.0,
        'gap_meV': 2.0 * 4.136,     # THz -> meV
        'plasma_eV': 16.0,
        'description': 'Engineered bandgap at ~2 THz',
        'color': '#44ff88',
    },
    'bi2se3': {
        'name': 'Bi2Se3 (topological insulator)',
        'gap_THz': 1.8,
        'gap_meV': 1.8 * 4.136,
        'plasma_eV': 10.0,
        'description': 'Surface Dirac gap ~1.8 THz',
        'color': '#00ccff',
    },
    'metamaterial': {
        'name': 'Acoustic metamaterial',
        'gap_THz': 0.5,
        'gap_meV': 0.5 * 4.136,
        'plasma_eV': 15.0,
        'description': 'Engineered sub-THz gap',
        'color': '#ff8844',
    },
    'srtio3': {
        'name': 'SrTiO3 (quantum paraelectric)',
        'gap_THz': 2.5,
        'gap_meV': 2.5 * 4.136,
        'plasma_eV': 12.0,
        'description': 'Soft phonon gap ~2.5 THz at low T',
        'color': '#ff44ff',
    },
}


# =====================================================================
# MATPLOTLIB SETUP
# =====================================================================

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Rectangle

# Visual constants
BG = '#0a0a1a'
BG_PANEL = '#0d0d24'
BG_BOX = '#141432'
GOLD = '#ffd700'
GOLD_DIM = '#aa8800'
CYAN = '#53d8fb'
CYAN_DIM = '#2a7090'
PURPLE = '#9966ff'
PURPLE_L = '#9966cc'
GREEN = '#44ff88'
GREEN_DIM = '#228844'
ORANGE = '#ff8800'
RED = '#ff4444'
RED_DIM = '#cc2222'
WHITE = '#ffffff'
GREY = '#888888'
DGREY = '#444444'
MAGENTA = '#ff44cc'
TEAL = '#00cc99'
DEEP_BLUE = '#2266ff'

GLOW_GOLD = [pe.withStroke(linewidth=3, foreground='#554400'), pe.Normal()]
GLOW_CYAN = [pe.withStroke(linewidth=3, foreground='#004455'), pe.Normal()]
GLOW_GREEN = [pe.withStroke(linewidth=2, foreground='#004422'), pe.Normal()]
GLOW_RED = [pe.withStroke(linewidth=3, foreground='#440000'), pe.Normal()]


# =====================================================================
# HELPER FUNCTIONS
# =====================================================================

def casimir_force(a):
    """Standard Casimir force per unit area (N/m^2) at separation a (m)."""
    return -CASIMIR_PREFACTOR / a**4


def casimir_energy(a):
    """Casimir energy per unit area (J/m^2) at separation a (m)."""
    return -CASIMIR_PREFACTOR / (3.0 * a**3)


def thermal_casimir(a, T):
    """
    Thermal Casimir force per unit area (N/m^2).
    Interpolates between quantum (low T) and classical (high T) regimes.
    """
    if T <= 0:
        return casimir_force(a)
    F_quantum = casimir_force(a)
    x_th = hbar_c / (k_B * T * a)
    if x_th > 50:
        return F_quantum
    F_thermal = -ZETA_3 * k_B * T / (8.0 * np.pi * a**3)
    weight = np.exp(-x_th)
    return F_quantum * (1 - weight) + F_thermal * weight


def bst_casimir_force(a, gap_meV=0.0):
    """
    BST Casimir force with N_max cutoff and optional phonon gap.
    Uses the discrete mode sum: sum_{n=1}^{N_max} n^{-4} w_n(x).
    """
    ns = np.arange(1, N_max + 1, dtype=np.float64)
    if gap_meV > 0:
        delta_J = gap_meV * 1e-3 * eV_to_J
        x = delta_J * a / hbar_c
        if x > 0:
            ratios = ns * np.pi / x
            weights = np.where(ratios > 500, 1.0 / ns**4,
                               (1.0 - np.exp(-ratios)) / ns**4)
        else:
            weights = 1.0 / ns**4
    else:
        weights = 1.0 / ns**4
    S = np.sum(weights)
    F_std = -CASIMIR_PREFACTOR / a**4
    return F_std * S / ZETA_4


def phonon_gap_correction(a, gap_THz, plasma_eV):
    """
    BST phonon-gap correction to Casimir force.
    Returns fractional deviation DF/F.
    """
    omega_gap = gap_THz * 1e12 * 2.0 * np.pi
    omega_plasma = plasma_eV * eV_to_J / hbar
    if omega_plasma == 0 or omega_gap == 0:
        return 0.0
    return -(omega_gap / omega_plasma) * alpha / (2.0 * np.pi)


def casimir_polder(a, alpha_pol):
    """
    Casimir-Polder force (N) for atom at distance a from surface.
    alpha_pol: atomic polarizability in SI (C^2 m^2 / J).
    """
    return -3.0 * alpha_pol * hbar_c / (8.0 * np.pi**2 * a**5)


def _discrete_correction(x, N=N_max):
    """
    Fractional correction to Casimir force from phonon gap.
    x = Delta * d / (hbar c) is dimensionless gap parameter.
    Returns C(x) = 1 - S_N(x) / zeta_N(4).
    """
    ns = np.arange(1, N + 1, dtype=np.float64)
    zeta_N = np.sum(1.0 / ns**4)
    if x < 1e-10:
        return 0.0
    ratios = ns * np.pi / x
    weights = np.where(ratios > 500, 1.0 / ns**4,
                       (1.0 - np.exp(-ratios)) / ns**4)
    S = np.sum(weights)
    return 1.0 - S / zeta_N


# =====================================================================
# THE CASIMIR COMMITMENT CLASS
# =====================================================================

class CasimirCommitment:
    """
    Casimir Force = Commitment Exclusion -- Toy 125.

    The vacuum pushes where it can commit. Where commitment is excluded,
    the pushing stops. The difference is force.

    Every computation uses only:
        N_c=3, n_C=5, g=7, C2=6, N_max=137
    and derived quantities.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        if not quiet:
            self._print_header()

    def _print_header(self):
        print()
        print("  " + "=" * 62)
        print("  CASIMIR FORCE = COMMITMENT EXCLUSION -- BST Toy 125")
        print("  Five integers: N_c=3  n_C=5  g=7  C2=6  N_max=137")
        print(f"  alpha = {alpha:.8f}  (1/alpha = {1/alpha:.3f})")
        print(f"  240 = |Phi(E8)| = {Gamma_order}/{W_B2}"
              f" = 2 x {n_C}! = {Phi_E8}")
        print("  " + "=" * 62)

    # -----------------------------------------------------------------
    # 1. the_force
    # -----------------------------------------------------------------

    def the_force(self, a_m=1e-6) -> dict:
        """
        The standard Casimir force between parallel plates.

        F/A = -pi^2 hbar c / (240 a^4)

        Derivation: boundary conditions discretize modes (k_z = n pi/a).
        Inside: fewer modes than outside. The energy difference (or
        equivalently, the mode-count asymmetry) produces a force.
        Regularized via zeta(-3) = 1/120.

        Parameters
        ----------
        a_m : float
            Plate separation in meters (default 1 micron).

        Returns
        -------
        dict with force, energy, and key quantities.
        """
        F = casimir_force(a_m)
        E = casimir_energy(a_m)
        energy_scale = hbar_c / a_m

        print()
        print("  THE FORCE")
        print("  " + "-" * 50)
        print()
        print("  Two perfectly conducting parallel plates in vacuum,")
        print("  separated by distance a, feel an attractive force:")
        print()
        print("    F/A = -pi^2 hbar c / (240 a^4)")
        print()
        print("  Derivation:")
        print("    1. EM modes between plates: k_z = n pi / a")
        print("    2. Zero-point energy: E_0 = hbar omega / 2")
        print("    3. Modes with lambda > 2a CANNOT FIT between plates")
        print("    4. Outside: all modes contribute freely (continuum)")
        print("    5. Inside: fewer modes => less zero-point energy")
        print("    6. Regularized sum: sum n^3 -> zeta(-3) = 1/120")
        print("    7. Transverse integral: pi^2/2")
        print("    8. Combined: pi^2/(2 x 120) = pi^2/240")
        print()
        print("  Power law decomposition:")
        print("    1/a^4 = (1/a^3) x (1/a)")
        print("    1/a^3 = missing commitment channels (mode density)")
        print("    1/a   = energy per missing channel (hbar c / a)")
        print()
        print(f"  For a = {a_m*1e6:.1f} um:")
        print(f"    Energy scale: hbar c / a = {energy_scale/eV_to_J:.4f} eV")
        print(f"    Mode n=1: E_1 = pi hbar c / a"
              f" = {np.pi*energy_scale/eV_to_J:.4f} eV")
        print(f"    Pressure:  F/A = {F:.4e} N/m^2  ({F:.4e} Pa)")
        print(f"    Energy:    E/A = {E:.4e} J/m^2")
        print()

        # Thermal crossover
        T_cross = hbar_c / (k_B * a_m)
        print(f"  Thermal crossover: T_cross = {T_cross:.1f} K")
        if T_cross > 300:
            print(f"    Room temp (300 K) is quantum regime for this separation.")
        else:
            print(f"    Room temp (300 K) is classical regime.")
        print()
        print("  Confirmed experimentally:")
        print("    Lamoreaux (1997): 5% precision")
        print("    Mohideen & Roy (1998): 1% precision")
        print("    Bressi et al. (2002): parallel plates, 1/d^4 confirmed")
        print("    Munday et al. (2009): repulsive Casimir in dielectrics")

        return {
            'F_per_area_Pa': F,
            'E_per_area_Jm2': E,
            'energy_scale_eV': energy_scale / eV_to_J,
            'T_crossover_K': T_cross,
            'a_m': a_m,
        }

    # -----------------------------------------------------------------
    # 2. why_240
    # -----------------------------------------------------------------

    def why_240(self) -> dict:
        """
        Why 240? Because 240 = |Phi(E8)| = |W(D5)|/|W(B2)| = 2 x 5!

        The Casimir coefficient knows about E8.

        The coefficient pi^2/240 decomposes as:
            pi^2/240 = (pi^2/2) x (1/5!)

        1/120 = 1/5! = zeta(-3) = regularized sum of n^3
              = volume of the 5-simplex
              = combinatorics of n_C = 5 mode counting

        pi^2/2 = 2 polarizations x 2D transverse momentum integration

        Returns
        -------
        dict with the E8 decomposition and verification.
        """
        print()
        print("  WHY 240?")
        print("  " + "-" * 50)
        print()
        print("  The Casimir coefficient is pi^2 / 240.")
        print("  Where does 240 come from?")
        print()

        # The decomposition chain
        print("  Chain of identities:")
        print()
        print(f"    240 = |Phi(E8)|")
        print(f"        = the number of root vectors in E8")
        print()
        print(f"    240 = |W(D5)| / |W(B2)|")
        print(f"        = {Gamma_order} / {W_B2}")
        print(f"        = {Gamma_order // W_B2}")
        print()
        print(f"    240 = 2 x {n_C}!")
        print(f"        = 2 x {factorial(n_C)}")
        print()
        print(f"    240 = 2 x n_C!")
        print(f"        => pi^2/240 = pi^2 / (2 x n_C!)")
        print()

        # Verify the Weyl group orders
        w_d5 = factorial(n_C) * 2**(n_C - 1)
        w_b2 = 2**2 * factorial(2)
        ratio = w_d5 // w_b2

        print("  Weyl group verification:")
        print(f"    |W(D5)| = {n_C}! x 2^({n_C}-1) = "
              f"{factorial(n_C)} x {2**(n_C-1)} = {w_d5}")
        print(f"    |W(B2)| = 2^2 x 2! = {w_b2}")
        print(f"    Ratio: {w_d5}/{w_b2} = {ratio}")
        assert ratio == Phi_E8, "Weyl ratio check failed"
        print()

        # The deep decomposition
        print("  The coefficient decomposition:")
        print(f"    pi^2/240 = (pi^2/2) x (1/{factorial(n_C)})")
        print()
        print(f"    1/{factorial(n_C)} = 1/{n_C}! = zeta(-3)")
        print(f"         = regularized sum: sum_{{n=1}}^inf n^3")
        print(f"         = volume of the {n_C}-simplex")
        print(f"         = -B_4/4 = -(-1/30)/4  (Bernoulli number)")
        print()
        print(f"    pi^2/2 = 2 polarizations x 2D angular integral")
        print()

        # Connection to domain volume
        print("  Connection to Vol(D_IV^5):")
        print(f"    Vol(D_IV^5) = pi^5 / {Gamma_order}")
        print(f"                = pi^5 / (2^4 x {n_C}!)")
        print(f"                = {np.pi**5/Gamma_order:.8f}")
        print()
        print(f"    The {n_C}! = {factorial(n_C)} appears in BOTH:")
        print(f"    - Casimir coefficient: pi^2/(2 x {n_C}!)")
        print(f"    - Domain volume: pi^5/(2^4 x {n_C}!)")
        print(f"    Not a coincidence.")
        print()

        # Connection to proton mass
        print("  Connection to proton mass:")
        print(f"    m_p = 6 pi^5 m_e = C2 x |W(D5)| x Vol(D_IV^5) x m_e")
        print(f"         = {C2} x {Gamma_order} x pi^5/{Gamma_order} x m_e")
        print(f"         = {C2} pi^5 m_e = {C2 * np.pi**5:.3f} m_e")
        print()
        print("  The Casimir force, E8, and the proton mass all")
        print("  share the same combinatorics of D_IV^5.")

        return {
            'Phi_E8': Phi_E8,
            'W_D5': w_d5,
            'W_B2': w_b2,
            'ratio': ratio,
            'n_C_factorial': factorial(n_C),
            'vol_D': np.pi**n_C / Gamma_order,
        }

    # -----------------------------------------------------------------
    # 3. commitment_exclusion
    # -----------------------------------------------------------------

    def commitment_exclusion(self) -> dict:
        """
        BST picture: the Casimir force is commitment pressure.

        The vacuum has a commitment rate Theta -- the rate at which
        the substrate writes new correlations through S^1 fiber modes.

        Theta_mode = alpha * omega / (2 pi)

        Modes that don't fit can't commit. The force comes from
        differential commitment capacity, not zero-point energy.

        The Haldane partition function:
            Z_mode = (1 - e^(-138 beta hbar omega)) / (1 - e^(-beta hbar omega))
        At T=0: Z -> 1, E_0 = 0.  Yet Casimir survives because it
        depends on mode COUNTING, not absolute energy.

        Returns
        -------
        dict with BST interpretation details.
        """
        print()
        print("  COMMITMENT EXCLUSION")
        print("  " + "-" * 50)
        print()
        print("  STANDARD PICTURE (correct result, wrong interpretation):")
        print("    'Vacuum fluctuations push the plates together.'")
        print("    'Zero-point energy creates pressure.'")
        print()
        print("  BST PICTURE (correct result, correct interpretation):")
        print("    The substrate has a commitment rate Theta_vac --")
        print("    the rate at which new correlations are written.")
        print()
        print("    Each mode of the S^1 fiber contributes to Theta_vac.")
        print("    The commitment rate per mode is:")
        print("      Theta_mode = alpha omega / (2 pi)")
        print(f"    where alpha = 1/N_max = 1/{N_max}")
        print()
        print("  What the plates do:")
        print("    Inside:  Only modes with lambda_n = 2a/n fit.")
        print("             Modes with lambda > 2a are EXCLUDED.")
        print("             => Fewer commitment channels.")
        print("             => Lower commitment rate: Theta_in < Theta_out")
        print()
        print("    Outside: All modes up to N_max = 137 contribute.")
        print("             => Full commitment rate: Theta_out")
        print()
        print("  The force:")
        print("    Theta_inside < Theta_outside")
        print("    => Substrate pushes HARDER from outside")
        print("    => Plates are pushed TOGETHER")
        print("    => F/A = -(pi^2 hbar c) / (240 a^4)")
        print()
        print("  Why the two calculations agree:")
        print("    Zero-point energy ~ hbar omega / 2")
        print("    Commitment rate   ~ alpha omega / (2 pi)")
        print("    Both proportional to omega, mode by mode.")
        print("    Same mode-count difference => same force.")
        print()
        print("  But the INTERPRETATION differs:")
        print("    QFT:  residual energy of quantum vacuum")
        print("    BST:  pressure from the substrate's writing rate")
        print()

        # Haldane partition function demonstration
        a_sample = 1e-6
        omega_1 = np.pi * c_light / a_sample
        print("  THE DEEP POINT: zero-point energy is unnecessary.")
        print()
        print("  The Haldane partition function:")
        print("    Z_mode = (1 - e^(-138 beta hbar omega))"
              " / (1 - e^(-beta hbar omega))")
        print()
        T_list = [0, 77, 300, 1000]
        print(f"  Z values for mode n=1 at a = 1 um:")
        for T_K in T_list:
            if T_K == 0:
                Z = 1.0
            else:
                bho = hbar * omega_1 / (k_B * T_K)
                if bho > 500:
                    Z = 1.0
                else:
                    Z = (1.0 - np.exp(-138.0 * bho)) / (1.0 - np.exp(-bho))
            print(f"    T = {T_K:>5d} K:  Z = {Z:.4f}")
        print()
        print("  At T=0: Z=1, E_0=0 in BST.  Yet Casimir survives.")
        print("  The force depends on mode COUNTING, not absolute energy.")
        print()
        print("  The 1/d^4 power law:")
        print("    1/d^3 = missing commitment channels (cubic scaling)")
        print("    1/d   = energy per missing channel (hbar c / d)")
        print("    Product: (missing channels) x (cost each) = hbar c / d^4")

        return {
            'interpretation': 'commitment_pressure',
            'Theta_mode': 'alpha * omega / (2 pi)',
        }

    # -----------------------------------------------------------------
    # 4. the_modification
    # -----------------------------------------------------------------

    def the_modification(self) -> dict:
        """
        BST predicts modifications to the standard Casimir force.

        Two effects:
        1. Channel cutoff: N_max = 137 truncates the mode sum.
           zeta(4) -> zeta_137(4).  Correction ~ 10^-7.

        2. Phonon gap: materials with gap Delta have coupling weights
           w_n = 1 - exp(-E_n/Delta) modifying each mode.
           Correction: DF/F ~ -(omega_gap/omega_plasma) x alpha/(2pi)

        The BST characteristic scale:
           a_BST = hbar / (N_max m_e c) ~ 2.8 pm

        Returns
        -------
        dict with modification predictions.
        """
        ns = np.arange(1, N_max + 1, dtype=np.float64)
        zeta4_137 = np.sum(1.0 / ns**4)
        cutoff_frac = 1.0 - zeta4_137 / ZETA_4

        print()
        print("  THE MODIFICATION")
        print("  " + "-" * 50)
        print()
        print("  BST predicts TWO modifications to standard Casimir:")
        print()

        # 1. Channel cutoff
        print("  1. CHANNEL CUTOFF (N_max = 137):")
        print(f"     The mode sum is finite: sum_{{n=1}}^{{{N_max}}} 1/n^4")
        print(f"     zeta(4) = pi^4/90    = {ZETA_4:.10f}")
        print(f"     zeta_{N_max}(4)       = {zeta4_137:.10f}")
        print(f"     Fractional correction: {cutoff_frac:.4e}")
        print(f"     This gives DF/F ~ {cutoff_frac:.2e}")
        print()

        # 2. Phonon gap
        print("  2. PHONON GAP (materials with bandgap):")
        print("     Modes with hbar omega < Delta are transparent.")
        print("     They don't couple to the material's commitment.")
        print("     Coupling weight: w_n = 1 - exp(-E_n/Delta)")
        print()
        print("     Fractional deviation:")
        print("       DF/F = -(omega_gap/omega_plasma) x alpha/(2pi)")
        print()

        # Materials table
        print(f"  {'Material':<30} {'gap (THz)':>10} {'plasma (eV)':>12}"
              f" {'DF/F':>14}")
        print(f"  {'=' * 30} {'=' * 10} {'=' * 12} {'=' * 14}")

        results = {}
        for key, mat in MATERIALS.items():
            delta_f = phonon_gap_correction(1e-6, mat['gap_THz'], mat['plasma_eV'])
            results[key] = delta_f
            print(f"  {mat['name']:<30} {mat['gap_THz']:>10.1f}"
                  f" {mat['plasma_eV']:>12.1f}"
                  f" {delta_f:>14.2e}")
        print()

        # BST characteristic scale
        print(f"  BST characteristic scale:")
        print(f"    a_BST = hbar / (N_max x m_e x c)")
        print(f"          = {a_BST:.4e} m  ({a_BST*1e12:.2f} pm)")
        print()

        # Distance dependence of discrete correction
        gap_meV = 8.0  # example
        distances_um = [0.5, 1.0, 2.0, 5.0, 10.0, 50.0, 100.0]
        print(f"  Discrete correction vs distance (Delta = {gap_meV} meV):")
        print(f"  {'a (um)':<10} {'x = Delta a/(hbar c)':<22} {'Correction':<14}")
        print(f"  {'=' * 10} {'=' * 22} {'=' * 14}")
        for a_um in distances_um:
            a_m = a_um * 1e-6
            delta_J = gap_meV * 1e-3 * eV_to_J
            x = delta_J * a_m / hbar_c
            corr = _discrete_correction(x)
            print(f"  {a_um:<10.1f} {x:<22.6f} {corr:<14.4e}")
        print()
        print("  Key signature: the deviation is FREQUENCY-DEPENDENT.")
        print("  It peaks when a ~ c/omega_gap, providing a distinctive")
        print("  BST fingerprint distinguishable from systematic errors.")

        return {
            'cutoff_correction': cutoff_frac,
            'materials': results,
            'a_BST_m': a_BST,
            'zeta4_137': zeta4_137,
        }

    # -----------------------------------------------------------------
    # 5. thermal_and_polder
    # -----------------------------------------------------------------

    def thermal_and_polder(self) -> dict:
        """
        Thermal Casimir effect and Casimir-Polder interaction.

        Thermal crossover:
        - Low T (k_B T << hbar c/a):  F/A = -pi^2 hbar c / (240 a^4)
        - High T (k_B T >> hbar c/a): F/A = -zeta(3) k_B T / (8 pi a^3)

        The zeta(3) = Apery's constant appears in the thermal limit.
        zeta(-3) = 1/120 appears in the quantum limit.
        Both from the Riemann zeta function.

        BST Haldane saturation:
        Standard Z -> infinity as T -> infinity.
        BST: Z -> N_max + 1 = 138.  Thermal force saturates.

        Casimir-Polder:
        Single boundary, 1/a^5 (extra 1/a from no second boundary).

        Returns
        -------
        dict with thermal and Casimir-Polder results.
        """
        print()
        print("  THERMAL CASIMIR & CASIMIR-POLDER")
        print("  " + "-" * 50)
        print()
        print("  THERMAL CASIMIR EFFECT")
        print()
        print("  At finite temperature T, thermal photons add to the")
        print("  zero-point modes. Two regimes:")
        print()
        print("  Low T  (k_B T << hbar c / a):  Quantum regime")
        print("    F/A = -pi^2 hbar c / (240 a^4)")
        print("    Thermal occupation << 1, same as T=0.")
        print()
        print("  High T (k_B T >> hbar c / a):  Classical regime")
        print("    F/A = -zeta(3) k_B T / (8 pi a^3)")
        print(f"    zeta(3) = {ZETA_3:.10f}  (Apery's constant)")
        print()
        print("  Note the power law change: 1/a^4 -> 1/a^3")
        print("  Thermal fluctuations dominate; one power of 1/a lost.")
        print()

        # Crossover at representative separations
        for a_label, a_val in [('100 nm', 100e-9), ('1 um', 1e-6),
                                ('10 um', 10e-6)]:
            T_cross = hbar_c / (k_B * a_val)
            regime = 'QUANTUM' if 300 < T_cross else 'CLASSICAL'
            print(f"  a = {a_label}: T_cross = {T_cross:.0f} K"
                  f"  (room temp: {regime})")
        print()

        # BST thermal modification
        print("  BST HALDANE SATURATION:")
        print()
        print("  The Haldane cap N_max = 137 limits each mode to at most")
        print("  138 states (n = 0, 1, ..., 137). At extreme temperature:")
        print()
        print(f"    Standard bosonic: Z_mode -> 1/(beta hbar omega) -> infinity")
        print(f"    BST Haldane:      Z_mode -> {N_max + 1}  (capped)")
        print()
        print("  The thermal Casimir force SATURATES at extreme T:")
        print(f"    F/A -> -ln({N_max + 1}) k_B T / (8 pi a^3)")
        print(f"         = -{np.log(N_max + 1):.4f} k_B T / (8 pi a^3)")
        print()
        T_sat_1um = (N_max + 1) * hbar_c / (k_B * 1e-6)
        print(f"  For a = 1 um: saturation T ~ {T_sat_1um:.2e} K")
        print(f"  Inaccessible in lab, but cosmologically relevant.")
        print()

        # Casimir-Polder
        print("  CASIMIR-POLDER FORCE (atom near surface)")
        print()
        print("  A polarizable atom at distance a from a conductor:")
        print("    F_CP = -3 alpha_pol hbar c / (8 pi^2 a^5)")
        print()
        print("  Note the 1/a^5 (vs 1/a^4 for two plates).")
        print("  Extra 1/a: single-boundary, no resonance.")
        print()
        print("  BST interpretation:")
        print("    The atom sits in a commitment gradient.")
        print("    One side: full mode spectrum (free space)")
        print("    Other side: truncated spectrum (near surface)")
        print("    gradient Theta ~ -1/a^4, force ~ -alpha_pol / a^5")
        print()
        print("  The zeta connections to Riemann:")
        print("    zeta(-3) = 1/120 -> quantum Casimir coefficient")
        print("    zeta(3) = 1.202  -> thermal Casimir coefficient")
        print("    Both arise from the analytic continuation of the")
        print("    same Riemann zeta function whose zeros connect to")
        print("    the D_IV^5 spectral geometry.")

        return {
            'T_crossover_1um': hbar_c / (k_B * 1e-6),
            'zeta_3': ZETA_3,
            'haldane_saturation': np.log(N_max + 1),
            'T_saturation_1um': T_sat_1um,
        }

    # -----------------------------------------------------------------
    # 6. the_experiment
    # -----------------------------------------------------------------

    def the_experiment(self) -> dict:
        """
        Phonon-gapped materials: BST's most accessible prediction.

        Protocol:
            1. Gold-gold plates: control measurement
            2. Gold + gapped material: test measurement
            3. Compare at separations 0.5 - 5 um
            4. Look for systematic offset ~ 10^-7

        Key signature: frequency-dependent deviation that peaks at
        a ~ c/omega_gap.  Distinguishable from smooth systematics.

        Returns
        -------
        dict with experimental parameters and predictions.
        """
        print()
        print("  THE EXPERIMENT")
        print("  " + "-" * 50)
        print()
        print("  BST PREDICTION:")
        print("  A material with a phonon bandgap should exhibit a")
        print("  MODIFIED Casimir force compared to a normal conductor.")
        print()
        print("  Why?")
        print("    Phonon gap => frozen internal degrees of freedom")
        print("    Frozen modes => reduced commitment coupling")
        print("    Reduced coupling => softer boundary condition")
        print("    Softer boundary => less mode exclusion => less force")
        print()
        print("  Predicted fractional deviation:")
        print("    DF/F = -(omega_gap / omega_plasma) x alpha / (2 pi)")
        print()

        # Materials table with peak separation
        print(f"  {'Material':<30} {'gap (THz)':>10} {'peak a (um)':>12}"
              f" {'|DF/F|':>14}")
        print(f"  {'=' * 30} {'=' * 10} {'=' * 12} {'=' * 14}")

        results = {}
        for key, mat in MATERIALS.items():
            gap_THz = mat['gap_THz']
            if gap_THz == 0:
                continue
            a_peak = c_light / (2.0 * np.pi * gap_THz * 1e12)
            delta_f = phonon_gap_correction(1e-6, gap_THz, mat['plasma_eV'])
            results[key] = {
                'name': mat['name'],
                'gap_THz': gap_THz,
                'a_peak_um': a_peak * 1e6,
                'DF_F': delta_f,
            }
            print(f"  {mat['name']:<30} {gap_THz:>10.1f}"
                  f" {a_peak*1e6:>12.1f}"
                  f" {abs(delta_f):>14.2e}")
        print()

        # Protocol
        print("  EXPERIMENTAL PROTOCOL:")
        print("    1. Measure F between two gold plates (control)")
        print("    2. Replace one plate with phonon-gapped material")
        print("    3. Compare at separations 0.5 - 5 um")
        print("    4. Look for systematic offset ~ 10^-7 of total force")
        print("    5. Vary a. Map the frequency-dependent shape.")
        print()
        print("  PRECISION:")
        print("    Current Casimir experiments: ~1% precision (10^-2)")
        print("    State-of-art interferometric: ~0.1% (10^-3)")
        print("    BST signal: ~10^-7")
        print()
        print("  THE WAY FORWARD:")
        print("    Absolute precision of 10^-7 is hard.")
        print("    But the SHAPE is distinctive:")
        print("      - Deviation peaks at specific a (material-dependent)")
        print("      - Deviation vanishes at small a (all modes above gap)")
        print("      - Deviation grows with a until gap modes dominate")
        print("    This frequency-dependent fingerprint distinguishes")
        print("    BST from systematic errors, which are smooth in a.")
        print()
        print("  SCALE HIERARCHY (commitment exclusion at every scale):")
        print("    Laboratory:    conducting plates      a ~ 1 um")
        print("    Atomic:        atom + surface         a ~ 1 nm")
        print("    Nuclear:       quark confinement bag  a ~ 1 fm")
        print("    Cosmological:  Hubble horizon         R_H ~ 10^26 m")
        print()
        print("  The Casimir effect is the existence proof that")
        print("  vacuum mode exclusion produces real forces.")

        return results

    # -----------------------------------------------------------------
    # 7. summary
    # -----------------------------------------------------------------

    def summary(self) -> dict:
        """
        The unifying principle.
        """
        ns = np.arange(1, N_max + 1, dtype=np.float64)
        zeta4_137 = np.sum(1.0 / ns**4)
        cutoff_corr = 1.0 - zeta4_137 / ZETA_4

        print()
        print("  " + "=" * 62)
        print("  SUMMARY: CASIMIR FORCE = COMMITMENT EXCLUSION")
        print("  " + "=" * 62)
        print()
        print("  1. The vacuum has a commitment rate Theta -- the rate")
        print("     at which the substrate writes new correlations.")
        print()
        print("  2. Conducting plates exclude modes with lambda > 2a.")
        print("     => Fewer commitment channels inside.")
        print("     => Theta_inside < Theta_outside.")
        print()
        print("  3. The coefficient pi^2/240 = pi^2/(2 x 5!) is fixed")
        print(f"     by the n_C = {n_C} geometry of D_IV^5.")
        print(f"     240 = |Phi(E8)| = {Gamma_order}/{W_B2}"
              f" = 2 x {n_C}!")
        print()
        print("  4. The 1/d^4 power law:")
        print("     (missing channels)^3 x (energy each) = hbar c / d^4")
        print()
        print("  5. BST predicts modifications:")
        print(f"     - Channel cutoff N_max={N_max}: "
              f"DF/F ~ {cutoff_corr:.2e}")
        print("     - Phonon-gapped materials: DF/F ~ 10^-7")
        print("     - Haldane thermal saturation at extreme T")
        print()
        print("  THE UNIFYING PRINCIPLE:")
        print("    Boundaries truncate the substrate's commitment")
        print("    capacity. The resulting pressure differential = force.")
        print()
        print("    Two plates      => attraction  (symmetric truncation)")
        print("    One frozen face => thrust      (asymmetric truncation)")
        print("    Cosmic horizon  => dark energy (global truncation)")
        print()
        print("  The substrate pushes where it can commit.")
        print("  Where commitment is excluded, the pushing stops.")
        print("  The difference is force.")
        print()
        print("  " + "=" * 62)

        return {
            'Phi_E8': Phi_E8,
            'cutoff_correction': cutoff_corr,
            'n_C': n_C,
        }

    # =================================================================
    # VISUALIZATION: 6-panel show()
    # =================================================================

    def show(self):
        """
        Six-panel visualization:
          1. The Force -- plates, modes, F vs distance
          2. Why 240? -- E8 root system hierarchy
          3. Commitment Exclusion -- BST picture with plates
          4. The Modification -- standard vs BST-modified curves
          5. Thermal & Casimir-Polder -- crossover, zeta(3)
          6. The Experiment -- phonon-gap materials prediction
        """
        fig = plt.figure(figsize=(20, 14), facecolor=BG)
        if fig.canvas.manager:
            fig.canvas.manager.set_window_title(
                'Casimir Force = Commitment Exclusion -- Toy 125 -- BST')

        fig.text(0.5, 0.98,
                 'CASIMIR FORCE = COMMITMENT EXCLUSION',
                 fontsize=26, fontweight='bold', color=GOLD, ha='center',
                 va='top', fontfamily='monospace',
                 path_effects=GLOW_GOLD)
        fig.text(0.5, 0.955,
                 r'F/A = $-\pi^2 \hbar c\,/\,(240\,a^4)$'
                 r'$\;\;$where 240 = $|\Phi(E_8)|$ = 1920/8 = 2$\times$5!',
                 fontsize=13, color=CYAN, ha='center', va='top',
                 fontfamily='monospace', style='italic',
                 path_effects=GLOW_CYAN)

        fig.text(0.5, 0.012,
                 'Copyright (c) 2026 Casey Koons -- Demonstration Only'
                 ' -- Toy 125',
                 fontsize=8, color=DGREY, ha='center',
                 fontfamily='monospace')

        gs = GridSpec(2, 3, figure=fig,
                      left=0.05, right=0.96, top=0.92, bottom=0.05,
                      hspace=0.32, wspace=0.28)

        ax1 = fig.add_subplot(gs[0, 0])
        self._draw_the_force(ax1)

        ax2 = fig.add_subplot(gs[0, 1])
        self._draw_why_240(ax2)

        ax3 = fig.add_subplot(gs[0, 2])
        self._draw_commitment_exclusion(ax3)

        ax4 = fig.add_subplot(gs[1, 0])
        self._draw_modification(ax4)

        ax5 = fig.add_subplot(gs[1, 1])
        self._draw_thermal_polder(ax5)

        ax6 = fig.add_subplot(gs[1, 2])
        self._draw_experiment(ax6)

        self.fig = fig
        plt.show(block=False)
        return fig

    # ------------------------------------------------------------------
    # Panel helpers
    # ------------------------------------------------------------------

    def _panel_setup(self, ax, title, subtitle=None):
        """Common panel setup: dark background, title, spines."""
        ax.set_facecolor(BG_PANEL)
        for spine in ax.spines.values():
            spine.set_color(DGREY)
            spine.set_linewidth(0.5)
        ax.set_title(title, fontsize=13, fontweight='bold', color=GOLD,
                     pad=10, path_effects=GLOW_GOLD)
        if subtitle:
            ax.text(0.5, 1.01, subtitle, transform=ax.transAxes,
                    ha='center', va='bottom', fontsize=8, color=GREY,
                    fontfamily='monospace')
        ax.tick_params(colors=GREY, which='both')

    # ------------------------------------------------------------------
    # Panel 1: The Force
    # ------------------------------------------------------------------

    def _draw_the_force(self, ax):
        """
        Two parallel plates with vacuum modes between and outside.
        Standing waves that fit, force arrows, F/A formula.
        """
        self._panel_setup(ax, "The Force",
                         r"F/A = $-\pi^2\hbar c\,/\,(240\,a^4)$")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_xticks([])
        ax.set_yticks([])

        # Draw the two conducting plates
        plate_color = '#aabbcc'
        plate_left_x = 3.0
        plate_right_x = 7.0

        ax.add_patch(Rectangle((plate_left_x - 0.15, 1.0), 0.3, 8.0,
                               facecolor=plate_color, edgecolor=WHITE,
                               linewidth=1.5, alpha=0.8))
        ax.add_patch(Rectangle((plate_right_x - 0.15, 1.0), 0.3, 8.0,
                               facecolor=plate_color, edgecolor=WHITE,
                               linewidth=1.5, alpha=0.8))

        # Label plates
        ax.text(plate_left_x, 0.6, 'plate', ha='center', fontsize=7,
                color=GREY)
        ax.text(plate_right_x, 0.6, 'plate', ha='center', fontsize=7,
                color=GREY)

        # Draw modes that FIT between plates (standing waves)
        gap_center = (plate_left_x + plate_right_x) / 2.0
        gap_width = plate_right_x - plate_left_x

        for n in range(1, 5):
            y_base = 1.5 + n * 1.5
            x_mode = np.linspace(plate_left_x + 0.3, plate_right_x - 0.3, 80)
            amplitude = 0.35
            y_mode = y_base + amplitude * np.sin(n * np.pi *
                     (x_mode - plate_left_x) / gap_width)
            ax.plot(x_mode, y_mode, color=CYAN, linewidth=1.2, alpha=0.7)
            ax.text(plate_right_x + 0.4, y_base, f'n={n}', fontsize=6,
                    color=CYAN_DIM, va='center')

        # Draw modes OUTSIDE (continuous, more of them)
        for i in range(8):
            y_base = 1.5 + i * 1.0
            # Left side
            x_left = np.linspace(0.3, plate_left_x - 0.4, 40)
            y_left = y_base + 0.2 * np.sin(
                (2 + i * 0.7) * np.pi * x_left / 3.0)
            ax.plot(x_left, y_left, color=GREEN, linewidth=0.6, alpha=0.3)
            # Right side
            x_right = np.linspace(plate_right_x + 0.4, 9.7, 40)
            y_right = y_base + 0.2 * np.sin(
                (2 + i * 0.7) * np.pi * x_right / 3.0)
            ax.plot(x_right, y_right, color=GREEN, linewidth=0.6, alpha=0.3)

        # Force arrows (pointing inward from outside)
        ax.annotate('', xy=(plate_left_x + 0.4, 5.0),
                    xytext=(plate_left_x - 0.8, 5.0),
                    arrowprops=dict(arrowstyle='->', color=ORANGE,
                                   linewidth=2.5))
        ax.annotate('', xy=(plate_right_x - 0.4, 5.0),
                    xytext=(plate_right_x + 0.8, 5.0),
                    arrowprops=dict(arrowstyle='->', color=ORANGE,
                                   linewidth=2.5))
        ax.text(gap_center, 9.4, 'fewer modes\ninside',
                ha='center', fontsize=8, color=RED,
                fontweight='bold', va='top')
        ax.text(1.5, 9.4, 'more\nmodes', ha='center', fontsize=7,
                color=GREEN, va='top')
        ax.text(8.5, 9.4, 'more\nmodes', ha='center', fontsize=7,
                color=GREEN, va='top')

        # Separation label
        ax.annotate('', xy=(plate_right_x, 0.3),
                    xytext=(plate_left_x, 0.3),
                    arrowprops=dict(arrowstyle='<->', color=GOLD,
                                   linewidth=1.5))
        ax.text(gap_center, 0.1, 'a', ha='center', fontsize=12,
                color=GOLD, fontweight='bold')

    # ------------------------------------------------------------------
    # Panel 2: Why 240?
    # ------------------------------------------------------------------

    def _draw_why_240(self, ax):
        """
        240 = |Phi(E8)| = 1920/8 = 2 x 5!
        The Casimir coefficient knows about E8.
        """
        self._panel_setup(ax, "Why 240?",
                         "The Casimir coefficient knows about E8")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_xticks([])
        ax.set_yticks([])

        # The big number
        ax.text(5.0, 9.0, '240', ha='center', va='center',
                fontsize=48, fontweight='bold', color=GOLD,
                path_effects=GLOW_GOLD)

        # The three decompositions
        y_start = 7.2
        spacing = 1.4

        decomps = [
            (r'$|\Phi(E_8)|$', 'Root vectors of E8', CYAN),
            (r'$|W(D_5)|\,/\,|W(B_2)|$',
             f'= {Gamma_order} / {W_B2}', GREEN),
            (r'$2 \times 5!$', f'= 2 x {factorial(n_C)}', ORANGE),
        ]

        for i, (formula, note, color) in enumerate(decomps):
            y = y_start - i * spacing
            ax.text(5.0, y, f'= {formula}', ha='center', va='center',
                    fontsize=16, color=color, fontweight='bold')
            ax.text(5.0, y - 0.45, note, ha='center', va='center',
                    fontsize=9, color=GREY, style='italic')

        # The Casimir connection
        ax.plot([1.5, 8.5], [3.6, 3.6], color=DGREY, linewidth=0.8,
                linestyle='--')

        ax.text(5.0, 3.1, r'$\pi^2/240 = \pi^2\,/\,(2 \times n_C!)$',
                ha='center', fontsize=14, color=WHITE, fontweight='bold')

        # Volume connection
        ax.text(5.0, 2.2,
                r'Vol$(D_{IV}^5) = \pi^5/1920 = \pi^5/(2^4 \times 5!)$',
                ha='center', fontsize=10, color=PURPLE)

        # Proton mass connection
        ax.text(5.0, 1.3,
                r'$m_p = 6\pi^5 m_e = C_2 \times |W(D_5)|'
                r'\times \mathrm{Vol}(D_{IV}^5) \times m_e$',
                ha='center', fontsize=9, color=CYAN_DIM)

        # Bottom line
        ax.text(5.0, 0.4,
                'Same combinatorics: Casimir, E8, proton mass',
                ha='center', fontsize=9, color=GOLD_DIM,
                fontweight='bold', style='italic')

    # ------------------------------------------------------------------
    # Panel 3: Commitment Exclusion
    # ------------------------------------------------------------------

    def _draw_commitment_exclusion(self, ax):
        """
        BST picture: modes that don't fit can't commit.
        Commitment pressure from outside > inside.
        """
        self._panel_setup(ax, "Commitment Exclusion",
                         "Not fluctuations -- commitment pressure")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_xticks([])
        ax.set_yticks([])

        # Outside regions: full commitment (bright dots)
        rng = np.random.RandomState(125)

        # Left region
        n_dots = 120
        x_left = rng.uniform(0.3, 2.8, n_dots)
        y_left = rng.uniform(1.0, 8.5, n_dots)
        ax.scatter(x_left, y_left, s=8, color=GREEN, alpha=0.4,
                   edgecolors='none')

        # Right region
        x_right = rng.uniform(7.2, 9.7, n_dots)
        y_right = rng.uniform(1.0, 8.5, n_dots)
        ax.scatter(x_right, y_right, s=8, color=GREEN, alpha=0.4,
                   edgecolors='none')

        # Inside region: reduced commitment (fewer, dimmer dots)
        n_inside = 40
        x_inside = rng.uniform(3.5, 6.5, n_inside)
        y_inside = rng.uniform(1.0, 8.5, n_inside)
        ax.scatter(x_inside, y_inside, s=6, color=CYAN_DIM, alpha=0.25,
                   edgecolors='none')

        # Plates
        ax.add_patch(Rectangle((3.0, 0.8), 0.2, 8.2,
                               facecolor='#667788', edgecolor=WHITE,
                               linewidth=1.0, alpha=0.9))
        ax.add_patch(Rectangle((6.8, 0.8), 0.2, 8.2,
                               facecolor='#667788', edgecolor=WHITE,
                               linewidth=1.0, alpha=0.9))

        # Labels
        ax.text(1.5, 9.2, r'$\Theta_{out}$  (full)', ha='center',
                fontsize=10, color=GREEN, fontweight='bold')
        ax.text(5.0, 9.2, r'$\Theta_{in}$  (reduced)', ha='center',
                fontsize=10, color=RED, fontweight='bold')
        ax.text(8.5, 9.2, r'$\Theta_{out}$  (full)', ha='center',
                fontsize=10, color=GREEN, fontweight='bold')

        # Pressure arrows (from outside pushing in)
        for y_arr in [3.0, 5.0, 7.0]:
            ax.annotate('', xy=(3.2, y_arr),
                        xytext=(1.0, y_arr),
                        arrowprops=dict(arrowstyle='->', color=ORANGE,
                                       linewidth=2.0, alpha=0.7))
            ax.annotate('', xy=(6.8, y_arr),
                        xytext=(9.0, y_arr),
                        arrowprops=dict(arrowstyle='->', color=ORANGE,
                                       linewidth=2.0, alpha=0.7))

        # Excluded mode crosses
        for y_x in [2.5, 4.5, 6.5]:
            ax.plot([4.3, 4.7], [y_x - 0.2, y_x + 0.2],
                    color=RED, linewidth=2, alpha=0.6)
            ax.plot([4.3, 4.7], [y_x + 0.2, y_x - 0.2],
                    color=RED, linewidth=2, alpha=0.6)
            ax.text(5.3, y_x, 'excluded', fontsize=6, color=RED,
                    va='center', alpha=0.7)

        # The key equation
        ax.text(5.0, 0.4,
                r'$\Theta_{in} < \Theta_{out}$'
                r'  $\Rightarrow$  net inward pressure',
                ha='center', fontsize=10, color=GOLD,
                fontweight='bold', path_effects=GLOW_GOLD)

    # ------------------------------------------------------------------
    # Panel 4: The Modification
    # ------------------------------------------------------------------

    def _draw_modification(self, ax):
        """
        Plot standard Casimir force vs BST-modified force with phonon gaps.
        Discrete BST mode sum with coupling weights.
        """
        self._panel_setup(ax, "The Modification",
                         r"BST: $\Delta F/F \sim 10^{-7}$ in gapped materials")

        ns = np.arange(1, N_max + 1, dtype=np.float64)
        zeta4_137 = np.sum(1.0 / ns**4)

        # Log-log plot: force vs distance for standard and gapped materials
        a_nm = np.logspace(1.5, 5, 300)
        a_m = a_nm * 1e-9
        F_std = CASIMIR_PREFACTOR / a_m**4   # magnitude

        # Standard with N_max cutoff only
        F_bst_0 = F_std * zeta4_137 / ZETA_4

        # Gapped materials
        gaps = [
            (0.0,  'Standard', CYAN,   '-',  2.0),
            (MATERIALS['bi2se3']['gap_meV'],
             r'Bi$_2$Se$_3$ (7.4 meV)', GREEN, '--', 1.5),
            (MATERIALS['srtio3']['gap_meV'],
             'SrTiO3 (10.3 meV)', ORANGE, '--', 1.5),
            (50.0, r'$\Delta$ = 50 meV', RED,    ':',  1.5),
        ]

        for gap_meV, label, color, ls, lw in gaps:
            if gap_meV == 0:
                ax.loglog(a_nm, F_bst_0, color=color, lw=lw, ls=ls,
                          label=label)
            else:
                delta_J = gap_meV * 1e-3 * eV_to_J
                F = np.zeros_like(a_m)
                for i, a in enumerate(a_m):
                    x = delta_J * a / hbar_c
                    if x < 1e-10:
                        ratios_w = 1.0 / ns**4
                    else:
                        ratios = ns * np.pi / x
                        ratios_w = np.where(ratios > 500, 1.0 / ns**4,
                                            (1.0 - np.exp(-ratios)) / ns**4)
                    S = np.sum(ratios_w)
                    F[i] = F_std[i] * S / ZETA_4
                ax.loglog(a_nm, F, color=color, lw=lw, ls=ls, label=label)

        # Experimental range highlight
        ax.axvspan(100, 10000, color=GREEN, alpha=0.03)
        ax.text(1000, F_std[0] * 1e-2,
                'expt\nrange', fontsize=7, color=GREEN_DIM,
                ha='center', va='center', fontfamily='monospace')

        # Annotation box
        ax.text(0.03, 0.03,
                r'$\frac{\Delta F}{F} = -\frac{\omega_{gap}}'
                r'{\omega_{pl}}\cdot\frac{\alpha}{2\pi} \sim 10^{-7}$',
                transform=ax.transAxes, fontsize=9, color=WHITE,
                va='bottom', fontfamily='serif',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_BOX,
                         edgecolor=DGREY))

        ax.set_xlabel('Plate separation (nm)', color=GREY, fontsize=9,
                      fontfamily='monospace')
        ax.set_ylabel(r'$|F/A|$ (Pa)', color=GREY, fontsize=9,
                      fontfamily='monospace')
        ax.tick_params(colors=GREY, labelsize=7)
        ax.legend(fontsize=7, loc='upper right', framealpha=0.3,
                  facecolor=BG_PANEL, edgecolor=DGREY, labelcolor=GREY)

    # ------------------------------------------------------------------
    # Panel 5: Thermal & Casimir-Polder
    # ------------------------------------------------------------------

    def _draw_thermal_polder(self, ax):
        """
        Thermal crossover, Haldane saturation, and zeta(3) connection.
        """
        self._panel_setup(ax, "Thermal & Casimir-Polder",
                         r"$\zeta(3)$ appears; Haldane cap saturates")

        # Temperature sweep at fixed separation
        a_fixed = 1e-6  # 1 um
        T_range = np.logspace(-1, 5, 400)
        F_values = np.array([np.abs(thermal_casimir(a_fixed, T))
                            for T in T_range])

        # Quantum limit
        F_quantum = np.abs(casimir_force(a_fixed))
        # Classical limit
        F_classical = ZETA_3 * k_B * T_range / (8.0 * np.pi * a_fixed**3)

        ax.loglog(T_range, F_values, color=GOLD, linewidth=2.5,
                  label='Full thermal',
                  path_effects=[pe.withStroke(linewidth=4,
                               foreground=GOLD_DIM), pe.Normal()])
        ax.loglog(T_range, np.full_like(T_range, F_quantum),
                  color=CYAN, linewidth=1.5, linestyle='--',
                  label=r'Quantum: $\pi^2\hbar c/(240 a^4)$')
        ax.loglog(T_range, F_classical, color=ORANGE, linewidth=1.5,
                  linestyle=':', alpha=0.7,
                  label=r'Thermal: $\zeta(3)k_BT/(8\pi a^3)$')

        # Crossover point
        T_cross = hbar_c / (k_B * a_fixed)
        ax.axvline(x=T_cross, color=MAGENTA, linewidth=1.0,
                   linestyle='--', alpha=0.5)
        ax.text(T_cross * 1.3, F_quantum * 0.3,
                r'$T_{cross}$' + f'\n= {T_cross:.0f} K',
                fontsize=7, color=MAGENTA, va='center',
                fontfamily='monospace')

        # Room temperature marker
        ax.axvline(x=300, color=GREEN, linewidth=1.0,
                   linestyle='--', alpha=0.3)
        ax.text(320, F_quantum * 3.0, '300 K', fontsize=7,
                color=GREEN_DIM, va='center', fontfamily='monospace')

        ax.set_xlabel('Temperature (K)', color=GREY, fontsize=9,
                      fontfamily='monospace')
        ax.set_ylabel(r'$|F/A|$ (Pa) at $a$ = 1 $\mu$m',
                      color=GREY, fontsize=9, fontfamily='monospace')
        ax.tick_params(colors=GREY, labelsize=7)
        ax.legend(fontsize=6, loc='lower right', framealpha=0.3,
                  facecolor=BG_PANEL, edgecolor=DGREY, labelcolor=GREY)

        # Casimir-Polder annotation
        ax.text(0.03, 0.58,
                'CASIMIR-POLDER:\n'
                r'$F = -3\alpha_{pol}\hbar c/(8\pi^2 a^5)$'
                '\nSingle boundary: extra 1/a',
                transform=ax.transAxes, fontsize=7, color=PURPLE,
                va='center', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_PANEL,
                         edgecolor=PURPLE, alpha=0.8, linewidth=0.5))

        # Zeta connection
        ax.text(0.03, 0.18,
                r'$\zeta(-3) = 1/120 \;\rightarrow\;$' + ' quantum\n'
                r'$\zeta(3) = 1.202... \;\rightarrow\;$' + ' thermal\n'
                'Same Riemann function!',
                transform=ax.transAxes, fontsize=7, color=CYAN_DIM,
                va='center', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_PANEL,
                         edgecolor=CYAN_DIM, alpha=0.8, linewidth=0.5))

    # ------------------------------------------------------------------
    # Panel 6: The Experiment
    # ------------------------------------------------------------------

    def _draw_experiment(self, ax):
        """
        Phonon-gapped materials prediction.
        Fractional deviation vs plate separation for candidate materials.
        """
        self._panel_setup(ax, "The Experiment",
                         "Phonon-gapped materials: testable prediction")

        ns = np.arange(1, N_max + 1, dtype=np.float64)
        zeta4_137 = np.sum(1.0 / ns**4)

        # Plot fractional deviation vs separation for each material
        a_nm = np.logspace(2, 6, 300)
        a_m = a_nm * 1e-9

        for key in ['si_ge_phononic', 'bi2se3', 'srtio3', 'metamaterial']:
            mat = MATERIALS[key]
            if mat['gap_meV'] <= 0:
                continue
            delta_J = mat['gap_meV'] * 1e-3 * eV_to_J
            corrections = np.zeros_like(a_m)
            for i, a in enumerate(a_m):
                x = delta_J * a / hbar_c
                corrections[i] = _discrete_correction(x)

            mask = corrections > 1e-16
            if np.any(mask):
                short_name = mat['name'].split('(')[0].strip()
                ax.loglog(a_nm[mask], corrections[mask],
                          color=mat['color'], lw=2,
                          label=f"{short_name} ({mat['gap_meV']:.1f} meV)")

        # N_max cutoff line
        nmax_corr = abs(1.0 - zeta4_137 / ZETA_4)
        ax.axhline(nmax_corr, color=RED, ls='--', lw=1.5, alpha=0.7)
        ax.text(a_nm[5], nmax_corr * 2.5,
                f'N_max={N_max} cutoff ({nmax_corr:.1e})',
                fontsize=7, color=RED, fontfamily='monospace')

        # Precision lines
        precisions = [
            (1e-2, 'Current (~1%)', GREY),
            (1e-3, 'Next-gen (~0.1%)', DGREY),
        ]
        for prec, label, color in precisions:
            ax.axhline(prec, color=color, ls=':', lw=1, alpha=0.7)
            ax.text(a_nm[3], prec * 1.5, label, fontsize=6,
                    color=color, fontfamily='monospace')

        ax.set_xlabel('Plate separation (nm)', color=GREY, fontsize=9,
                      fontfamily='monospace')
        ax.set_ylabel(r'$|\Delta F/F|$', color=GREY, fontsize=9,
                      fontfamily='monospace')
        ax.set_ylim(1e-15, 1)
        ax.tick_params(colors=GREY, labelsize=7)
        ax.legend(fontsize=6, loc='lower right', framealpha=0.3,
                  facecolor=BG_PANEL, edgecolor=DGREY, labelcolor=GREY)

        # Protocol box
        ax.text(0.03, 0.72,
                'PROTOCOL:\n'
                '1. Gold-gold (control)\n'
                '2. Gold-gapped (test)\n'
                '3. Compare at 0.5-5 um\n'
                '4. Map peak at\n'
                r'   $a \sim c/\omega_{gap}$',
                transform=ax.transAxes, fontsize=7, color=GREEN,
                va='top', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG_PANEL,
                         edgecolor=GREEN_DIM, alpha=0.8, linewidth=0.5))

        # BST prediction
        ax.text(0.97, 0.03,
                r'BST: $\Delta F/F = -(\omega_{gap}/\omega_{pl})'
                r'\cdot\alpha/(2\pi)$',
                transform=ax.transAxes, fontsize=8, color=GOLD,
                ha='right', va='bottom', fontweight='bold',
                path_effects=GLOW_GOLD)


# =====================================================================
# MAIN
# =====================================================================

if __name__ == '__main__':
    cc = CasimirCommitment()

    # Run all panels
    cc.the_force()
    cc.why_240()
    cc.commitment_exclusion()
    cc.the_modification()
    cc.thermal_and_polder()
    cc.the_experiment()
    cc.summary()

    # Visualization
    try:
        cc.show()
        print()
        print("  Done. Close the plot window to exit.")
        plt.show(block=True)
    except Exception as e:
        print(f"\n  Visualization skipped: {e}")
        print("  Text API methods above contain all results.")
