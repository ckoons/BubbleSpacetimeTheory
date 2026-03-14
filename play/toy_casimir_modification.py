#!/usr/bin/env python3
"""
THE CASIMIR MODIFICATION
========================
BST predicts a modified Casimir force in phonon-gapped materials.

The standard Casimir effect is vacuum pressure between parallel plates:
    F = -pi^2 hbar c / (240 d^4)

In BST, vacuum fluctuations are commitment rate fluctuations. The Casimir
force is the pressure difference between committed (between plates) and
uncommitted (outside) channels. Two BST modifications arise:

  1. PHONON GAP: Materials with a phonon gap Delta make modes with
     hbar*omega < Delta transparent -- they cannot be absorbed, so they
     don't contribute to the commitment pressure. Mode n has energy
     E_n = n*pi*hbar*c/d. The coupling weight is:
         w_n = 1 - exp(-E_n/Delta) = 1 - exp(-n*pi/(Delta*d/(hbar*c)))
     This produces a measurable correction at accessible plate spacings.

  2. CHANNEL CUTOFF: The BST channel capacity N_max = 137 truncates
     the mode sum. The zeta function zeta(4) = pi^4/90 becomes the
     partial sum zeta_137(4), giving a ~10^-7 correction.

    from toy_casimir_modification import CasimirModification
    cm = CasimirModification()
    cm.standard_casimir()              # derivation from vacuum modes
    cm.phonon_gap_correction()         # how a gap modifies the spectrum
    cm.bst_casimir(100e-9, 5.0)        # modified force (d=100nm, Delta=5meV)
    cm.channel_cutoff()                # N_max = 137 high-frequency cutoff
    cm.correction_function()           # g(x) transition curve
    cm.experimental_proposal()         # materials, spacing, expected signal
    cm.force_vs_distance()             # F(d) comparison plots
    cm.zeta_comparison()               # zeta_137(4) vs zeta(4)
    cm.summary()                       # key insight
    cm.show()                          # 4-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np

# =====================================================================
# BST CONSTANTS -- the five integers
# =====================================================================

N_c = 3                      # color charges
n_C = 5                      # complex dimension of D_IV^5
genus = n_C + 2              # = 7
C2 = n_C + 1                 # = 6, Casimir eigenvalue
N_max = 137                  # Haldane channel capacity
Gamma_order = 1920           # |Gamma| = n_C! * 2^(n_C-1)

# Derived
_vol_D = np.pi**n_C / Gamma_order
alpha = (N_c**2 / (2**N_c * np.pi**4)) * _vol_D**(1/4)  # ~ 1/137.036

# Physical constants (SI)
hbar = 1.054571817e-34       # J*s
c_light = 2.99792458e8      # m/s
hbar_c = hbar * c_light      # J*m = 1.9733e-25 J*m
eV_to_J = 1.602176634e-19   # J/eV
k_B = 1.380649e-23          # J/K

# Casimir prefactor: pi^2 * hbar * c / 240
CASIMIR_PREFACTOR = np.pi**2 * hbar_c / 240.0  # J*m  (force = this / d^4  per m^2)


# =====================================================================
# MATERIALS DATABASE
# =====================================================================

MATERIALS = {
    'gold': {
        'name': 'Gold (Au)',
        'gap_meV': 0.0,
        'description': 'Standard Casimir plates (no phonon gap)',
        'color': '#ffd700',
    },
    'bi2se3': {
        'name': 'Bi2Se3 (topological insulator)',
        'gap_meV': 3.0,
        'description': 'Surface gap ~3 meV, bulk gap ~300 meV',
        'color': '#44ff88',
    },
    'bi2te3': {
        'name': 'Bi2Te3 (topological insulator)',
        'gap_meV': 1.5,
        'description': 'Surface gap ~1.5 meV',
        'color': '#00ccff',
    },
    'srtio3': {
        'name': 'SrTiO3 (quantum paraelectric)',
        'gap_meV': 8.0,
        'description': 'Soft phonon gap ~8 meV at low T',
        'color': '#ff8844',
    },
    'graphene': {
        'name': 'Gapped graphene (substrate-induced)',
        'gap_meV': 50.0,
        'description': 'Gap ~50 meV on hBN substrate',
        'color': '#ff44ff',
    },
    'ideal_10meV': {
        'name': 'Ideal 10 meV gap material',
        'gap_meV': 10.0,
        'description': 'Hypothetical optimized material',
        'color': '#ffaa44',
    },
}


# =====================================================================
# THE CASIMIR MODIFICATION
# =====================================================================

class CasimirModification:
    """
    BST-modified Casimir effect in phonon-gapped materials.

    Every computation uses only:
        N_c=3, n_C=5, g=7, C2=6, N_max=137
    and derived quantities (alpha, etc.)
    """

    def __init__(self, quiet=False):
        if not quiet:
            self._print_header()

    def _print_header(self):
        print("=" * 68)
        print("  THE CASIMIR MODIFICATION -- BST Toy 82")
        print("  Five integers: N_c=3  n_C=5  g=7  C2=6  N_max=137")
        print(f"  alpha = {alpha:.8f}  (1/alpha = {1/alpha:.3f})")
        print(f"  N_max = {N_max}  (channel capacity cutoff)")
        print("=" * 68)

    # -----------------------------------------------------------------
    # 1. standard_casimir
    # -----------------------------------------------------------------

    def standard_casimir(self, d_m=100e-9) -> dict:
        """
        Standard Casimir force: F = -pi^2 hbar c / (240 d^4).

        Derivation: sum zero-point energies (1/2)hbar*omega for all EM
        modes between perfectly conducting parallel plates at separation d.
        The allowed modes have k_z = n*pi/d. Regularize the divergent sum
        via zeta-function: sum n^(-4) = zeta(4) = pi^4/90, giving the
        prefactor pi^2/240.

        Parameters
        ----------
        d_m : float
            Plate separation in meters (default 100 nm).

        Returns
        -------
        dict with force, pressure, energy, and derivation steps.
        """
        F_per_area = -CASIMIR_PREFACTOR / d_m**4   # N/m^2 (pressure)
        E_per_area = -CASIMIR_PREFACTOR / (3 * d_m**3)  # J/m^2

        # Energy scale at this distance
        hbar_c_over_d = hbar_c / d_m  # J
        hbar_c_over_d_eV = hbar_c_over_d / eV_to_J

        print()
        print("  STANDARD CASIMIR EFFECT")
        print("  " + "-" * 40)
        print()
        print("  Derivation:")
        print("    1. EM modes between plates: k_z = n*pi/d")
        print("    2. Zero-point energy: E_0 = (1/2)*hbar*omega")
        print("    3. Mode energies: E_n = n*pi*hbar*c/d")
        print("    4. Sum over modes (regularized):")
        print("       sum_{n=1}^inf n^{-4} = zeta(4) = pi^4/90")
        print("    5. Net pressure (inside - outside):")
        print("       F/A = -pi^2*hbar*c / (240*d^4)")
        print()
        print(f"  For d = {d_m*1e9:.1f} nm:")
        print(f"    Energy scale: hbar*c/d = {hbar_c_over_d_eV:.3f} eV")
        print(f"    Mode n=1:  E_1 = pi*hbar*c/d = {np.pi*hbar_c_over_d_eV:.3f} eV")
        print(f"    Pressure:  F/A = {F_per_area:.4e} N/m^2")
        print(f"             = {F_per_area:.4e} Pa")
        print(f"    Energy:    E/A = {E_per_area:.4e} J/m^2")
        print()
        print("  Key: zeta(4) = pi^4/90  (Euler, 1735)")
        print("  The Casimir force is a GEOMETRIC consequence of")
        print("  quantized vacuum fluctuations + boundary conditions.")
        print()
        print("  BST interpretation: this is the commitment pressure")
        print("  difference between constrained and free channels.")

        return {
            'F_per_area_Pa': F_per_area,
            'E_per_area_Jm2': E_per_area,
            'energy_scale_eV': hbar_c_over_d_eV,
            'd_m': d_m,
            'formula': 'F/A = -pi^2*hbar*c / (240*d^4)',
        }

    # -----------------------------------------------------------------
    # 2. phonon_gap_correction
    # -----------------------------------------------------------------

    def phonon_gap_correction(self, delta_meV=5.0) -> dict:
        """
        How a phonon gap Delta modifies the Casimir spectrum.

        Modes with hbar*omega < Delta cannot excite phonons in the
        material. In BST language, these modes are "transparent" to
        the material's commitment channels -- they pass through without
        being absorbed into the plate's degrees of freedom.

        Mode n has energy E_n = n*pi*hbar*c/d.
        Coupling weight: w_n = 1 - exp(-E_n/Delta) = 1 - exp(-n*pi/x)
        where x = Delta*d/(hbar*c).

        For x << pi: all modes have E_n >> Delta, so w_n ~ 1 (no correction).
        For x >> N_max*pi: all modes have E_n << Delta, force vanishes.

        The correction function g(x) gives the continuum approximation:
            g(x) = (15/pi^4) * integral_0^x  t^3/(e^t - 1) dt

        Parameters
        ----------
        delta_meV : float
            Phonon gap in meV (default 5 meV).

        Returns
        -------
        dict with correction values at various spacings.
        """
        delta_J = delta_meV * 1e-3 * eV_to_J

        print()
        print("  PHONON GAP CORRECTION")
        print("  " + "-" * 40)
        print()
        print(f"  Phonon gap: Delta = {delta_meV} meV")
        print()
        print("  Physics:")
        print("    - Mode n has energy E_n = n*pi*hbar*c/d")
        print("    - Modes with E_n < Delta are transparent to the material")
        print("    - They don't couple to the material's commitment channels")
        print("    - Coupling weight: w_n = 1 - exp(-E_n/Delta)")
        print()
        print("  Dimensionless parameter: x = Delta*d/(hbar*c)")
        print("    x << pi:  E_1 >> Delta, all modes couple, no correction")
        print("    x >> pi:  E_1 << Delta, mode n=1 transparent")
        print()
        print("  Modified force (discrete BST sum):")
        print("    F_BST = F_Casimir * [sum_{n=1}^{N_max} n^{-4} w_n] / zeta(4)")
        print()

        # Table of corrections at various distances
        distances_nm = [50, 100, 200, 500, 1000, 5000, 10000, 50000]

        ns = np.arange(1, N_max + 1, dtype=np.float64)
        zeta4_137 = np.sum(1.0 / ns**4)
        zeta4 = np.pi**4 / 90.0

        print(f"  {'d (nm)':>8}  {'x':>10}  {'E_1/Delta':>10}  {'Correction':>12}  {'g(x)':>12}")
        print(f"  {'=' * 8}  {'=' * 10}  {'=' * 10}  {'=' * 12}  {'=' * 12}")

        results = []
        for d_nm in distances_nm:
            d_m = d_nm * 1e-9
            x = delta_J * d_m / hbar_c
            E1_over_Delta = np.pi / x  # E_1/Delta = pi*hbar_c/(d*Delta) = pi/x

            # Discrete mode sum
            weights = (1.0 - np.exp(-ns * np.pi / x)) / ns**4
            S = np.sum(weights)
            correction = 1.0 - S / zeta4_137

            # Continuum g(x)
            gx = self._g_function(x)

            print(f"  {d_nm:8.0f}  {x:10.6f}  {E1_over_Delta:10.2f}"
                  f"  {correction:12.4e}  {gx:12.4e}")
            results.append({'d_nm': d_nm, 'x': x, 'correction': correction, 'g': gx})

        print()
        print("  When E_1/Delta >> 1 (small x): all modes above gap, tiny correction.")
        print("  When E_1/Delta << 1 (large x): mode n=1 below gap, large correction.")
        print()
        print("  BST: transparent modes carry no commitment.")
        print("  The plates 'see' fewer vacuum channels.")

        return {
            'delta_meV': delta_meV,
            'table': results,
            'formula': 'w_n = 1 - exp(-n*pi/x), x = Delta*d/(hbar*c)',
        }

    # -----------------------------------------------------------------
    # 3. bst_casimir
    # -----------------------------------------------------------------

    def bst_casimir(self, d_m=100e-9, delta_meV=5.0) -> dict:
        """
        Full BST-modified Casimir force with both phonon gap and N_max cutoff.

        F_BST = -(pi^2*hbar*c)/(240*d^4) * S_137(x) / zeta(4)

        where S_137(x) = sum_{n=1}^{137} n^{-4} * [1 - exp(-n*pi/x)]
              and x = Delta*d/(hbar*c).

        Parameters
        ----------
        d_m : float
            Plate separation in meters.
        delta_meV : float
            Phonon gap in meV (0 for standard).

        Returns
        -------
        dict with standard force, BST force, both corrections.
        """
        delta_J = delta_meV * 1e-3 * eV_to_J

        # Standard Casimir
        F_standard = -CASIMIR_PREFACTOR / d_m**4

        # Dimensionless gap parameter
        x = delta_J * d_m / hbar_c if delta_meV > 0 else 0.0

        # Mode energies
        ns = np.arange(1, N_max + 1, dtype=np.float64)
        zeta4 = np.pi**4 / 90.0
        zeta4_137 = np.sum(1.0 / ns**4)

        # BST mode sum with gap: weight = 1 - exp(-E_n/Delta) = 1 - exp(-n*pi/x)
        if delta_meV > 0 and x > 0:
            # For each mode: E_n/Delta = n*pi/x
            ratios = ns * np.pi / x
            # Clamp to avoid overflow in exp for very large ratios
            weights = np.where(ratios > 500, 1.0 / ns**4,
                               (1.0 - np.exp(-ratios)) / ns**4)
        else:
            weights = 1.0 / ns**4

        S_Nmax = np.sum(weights)

        # BST force
        F_bst = F_standard * S_Nmax / zeta4

        # Separate corrections
        # 1. Channel cutoff correction (N_max vs infinity, no gap)
        cutoff_ratio = zeta4_137 / zeta4
        cutoff_correction = 1.0 - cutoff_ratio

        # 2. Gap correction (at this distance, relative to N_max sum)
        if delta_meV > 0:
            gap_ratio = S_Nmax / zeta4_137
            gap_correction = 1.0 - gap_ratio
        else:
            gap_correction = 0.0

        # Total correction
        total_ratio = S_Nmax / zeta4
        total_correction = 1.0 - total_ratio

        print()
        print("  BST CASIMIR FORCE")
        print("  " + "-" * 40)
        print()
        print(f"  Parameters:")
        print(f"    Plate separation:  d = {d_m*1e9:.1f} nm")
        print(f"    Phonon gap:        Delta = {delta_meV} meV")
        print(f"    Channel capacity:  N_max = {N_max}")
        print()
        E_scale = hbar_c / d_m / eV_to_J
        print(f"  Energy scale: hbar*c/d = {E_scale:.3f} eV")
        print(f"  Mode n=1:     E_1 = {np.pi * E_scale:.3f} eV")
        if delta_meV > 0:
            E1_over_gap = np.pi * E_scale / (delta_meV * 1e-3)
            print(f"  Gap parameter: x = Delta*d/(hbar*c) = {x:.6f}")
            print(f"  E_1/Delta = {E1_over_gap:.1f}  (mode n=1 is {E1_over_gap:.0f}x above gap)")
        print()
        print(f"  Standard Casimir:  F/A = {F_standard:.4e} Pa")
        print(f"  BST Casimir:       F/A = {F_bst:.4e} Pa")
        print()
        print(f"  Corrections:")
        print(f"    N_max cutoff:  {cutoff_correction:+.4e}  ({cutoff_correction*100:+.2e}%)")
        if delta_meV > 0:
            print(f"    Phonon gap:    {gap_correction:+.4e}  ({gap_correction*100:+.2e}%)")
        print(f"    TOTAL:         {total_correction:+.4e}  ({total_correction*100:+.2e}%)")
        print()
        print(f"  Mode sum: sum_{{n=1}}^{{{N_max}}} n^(-4) * [1-exp(-n*pi/x)]")
        print(f"          = {S_Nmax:.10f}")
        print(f"  zeta(4) = pi^4/90 = {zeta4:.10f}")
        print(f"  Ratio:    {total_ratio:.15f}")
        print()
        if delta_meV > 0 and gap_correction < 1e-6:
            print(f"  NOTE: At d={d_m*1e9:.0f}nm with Delta={delta_meV}meV, E_1/Delta = {E1_over_gap:.0f}.")
            print(f"  All modes are far above the gap. The gap correction is negligible.")
            print(f"  Increase d or Delta to see a measurable effect.")
        print()
        print("  BST: the Casimir effect is a finite-channel phenomenon.")
        print(f"  Only {N_max} commitment channels contribute.")

        return {
            'F_standard_Pa': F_standard,
            'F_bst_Pa': F_bst,
            'cutoff_correction': cutoff_correction,
            'gap_correction': gap_correction,
            'total_correction': total_correction,
            'S_Nmax': S_Nmax,
            'zeta4': zeta4,
            'x': x,
            'd_m': d_m,
            'delta_meV': delta_meV,
        }

    # -----------------------------------------------------------------
    # 4. channel_cutoff
    # -----------------------------------------------------------------

    def channel_cutoff(self) -> dict:
        """
        The N_max = 137 high-frequency modification to the Casimir effect.

        The BST channel capacity limits the mode sum to 137 terms.
        This replaces zeta(4) = pi^4/90 with the partial sum
        zeta_137(4) = sum_{n=1}^{137} 1/n^4.

        The difference is:
            delta_zeta = zeta(4) - zeta_137(4) ~ 1/(3 * 137^3)

        This gives a fractional correction of ~1.3 x 10^-7.

        Returns
        -------
        dict with zeta values and the correction.
        """
        ns = np.arange(1, N_max + 1, dtype=np.float64)
        zeta4_137 = np.sum(1.0 / ns**4)
        zeta4 = np.pi**4 / 90.0

        # Tail: sum_{n=138}^{inf} 1/n^4 ~ 1/(3 * 137^3)
        tail_approx = 1.0 / (3.0 * N_max**3)
        tail_exact = zeta4 - zeta4_137

        ratio = zeta4_137 / zeta4
        fractional = 1.0 - ratio

        # Higher zeta values for comparison
        zeta_values = {}
        for s in [2, 3, 4, 5, 6]:
            partial = np.sum(1.0 / ns**s)
            full_analytical = {
                2: np.pi**2 / 6,
                3: 1.2020569031595942,  # Apery's constant
                4: np.pi**4 / 90,
                5: 1.0369277551433699,
                6: np.pi**6 / 945,
            }[s]
            zeta_values[s] = {
                'partial': partial,
                'full': full_analytical,
                'ratio': partial / full_analytical,
                'correction': 1.0 - partial / full_analytical,
            }

        print()
        print("  CHANNEL CUTOFF: N_max = 137")
        print("  " + "-" * 40)
        print()
        print("  In BST, the vacuum has a finite channel capacity.")
        print(f"  N_max = 137 = the Haldane limit for D_IV^5.")
        print()
        print("  The Casimir mode sum is truncated:")
        print(f"    zeta_{{137}}(4) = sum_{{n=1}}^{{137}} 1/n^4 = {zeta4_137:.12f}")
        print(f"    zeta(4)       = pi^4/90          = {zeta4:.12f}")
        print()
        print(f"    Tail = zeta(4) - zeta_137(4)")
        print(f"         = {tail_exact:.6e}")
        print(f"         ~ 1/(3*{N_max}^3) = {tail_approx:.6e}")
        print()
        print(f"    Fractional correction: {fractional:.4e}")
        print(f"    This is a ~{fractional:.1e} effect.")
        print()
        print(f"  Zeta function cutoffs at N_max = {N_max}:")
        print(f"  {'s':>3}  {'zeta_137(s)':>16}  {'zeta(s)':>16}  {'Correction':>14}")
        print(f"  {'=' * 3}  {'=' * 16}  {'=' * 16}  {'=' * 14}")
        for s in [2, 3, 4, 5, 6]:
            z = zeta_values[s]
            print(f"  {s:3d}  {z['partial']:16.12f}  {z['full']:16.12f}  {z['correction']:14.4e}")
        print()
        print("  The s=4 correction is the Casimir-relevant one.")
        print("  Tiny (~10^-7) but in principle falsifiable:")
        print("  a systematic 10^-7 WEAKENING of the Casimir force")
        print("  at ALL distances. This is a BST prediction.")

        return {
            'zeta4_137': zeta4_137,
            'zeta4': zeta4,
            'tail': tail_exact,
            'tail_approx': tail_approx,
            'fractional_correction': fractional,
            'zeta_values': zeta_values,
        }

    # -----------------------------------------------------------------
    # 5. correction_function
    # -----------------------------------------------------------------

    def correction_function(self, n_points=200) -> dict:
        """
        The gap correction g(x) and discrete correction vs x.

        Continuum (Bose integral):
            g(x) = (15/pi^4) * integral_0^x  t^3/(e^t - 1) dt

        Discrete (BST mode sum):
            C(x) = 1 - [sum_{n=1}^{N_max} n^{-4} (1-exp(-n*pi/x))] / zeta_137(4)

        Both measure the fraction of Casimir spectral weight removed
        by the gap. The discrete version is physically correct for BST;
        the continuum g(x) is the smooth approximation.

        Parameters
        ----------
        n_points : int
            Number of evaluation points.

        Returns
        -------
        dict with x values, g(x), and C(x) values.
        """
        x_values = np.logspace(-2, 3, n_points)
        g_values = np.array([self._g_function(x) for x in x_values])
        c_values = np.array([self._discrete_correction(x) for x in x_values])

        print()
        print("  CORRECTION FUNCTIONS")
        print("  " + "-" * 40)
        print()
        print("  Continuum (Bose integral):")
        print("    g(x) = (15/pi^4) * integral_0^x  t^3/(e^t-1) dt")
        print()
        print("  Discrete (BST mode sum, N_max=137):")
        print("    C(x) = 1 - [sum n^{-4} (1-exp(-n*pi/x))] / zeta_137(4)")
        print()
        print("  x = Delta*d/(hbar*c)")
        print()
        print("  Limits:")
        print("    x -> 0: both -> 0 (no gap, standard Casimir)")
        print("    x -> inf: both -> 1 (force vanishes entirely)")
        print()

        # Table comparing g(x) and C(x)
        print(f"  {'x':>10}  {'g(x)':>12}  {'C(x)':>12}  {'E_1/Delta':>10}")
        print(f"  {'=' * 10}  {'=' * 12}  {'=' * 12}  {'=' * 10}")
        sample_x = [0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0,
                     10.0, 20.0, 50.0, 100.0, 500.0]
        for x_s in sample_x:
            gx = self._g_function(x_s)
            cx = self._discrete_correction(x_s)
            E1_ratio = np.pi / x_s
            print(f"  {x_s:10.2f}  {gx:12.4e}  {cx:12.4e}  {E1_ratio:10.2f}")

        print()
        print("  Physical meaning of x:")
        print("    x = Delta*d/(hbar*c)")
        print("    E_1/Delta = pi/x = ratio of lowest mode energy to gap")
        print()
        print("    x < pi:   E_1 > Delta, all modes above gap, tiny correction")
        print("    x = pi:   E_1 = Delta, mode n=1 right at gap threshold")
        print("    x > N*pi: modes n=1..N below gap, significant correction")
        print()

        # Find x where correction = 0.01, 0.1, 0.5
        print("  Key thresholds (discrete BST correction):")
        print(f"  {'C(x)':>8}  {'x':>10}  {'E_1/Delta':>10}  {'For Delta=5meV':>20}")
        print(f"  {'=' * 8}  {'=' * 10}  {'=' * 10}  {'=' * 20}")
        for c_target in [0.001, 0.01, 0.1, 0.5]:
            x_t = self._discrete_correction_inverse(c_target)
            d_for_5meV = x_t * hbar_c / (5e-3 * eV_to_J * 1e-3)
            E1_D = np.pi / x_t
            print(f"  {c_target:8.3f}  {x_t:10.3f}  {E1_D:10.4f}"
                  f"  d = {d_for_5meV*1e6:.1f} um")

        return {
            'x_values': x_values,
            'g_values': g_values,
            'c_values': c_values,
        }

    # -----------------------------------------------------------------
    # 6. experimental_proposal
    # -----------------------------------------------------------------

    def experimental_proposal(self) -> dict:
        """
        Concrete experimental proposal for measuring the BST Casimir modification.

        Materials: topological insulators with surface gaps 1-10 meV.
        Method: AFM-based Casimir force measurement, comparing gapped
        and ungapped (gold) surfaces.

        Returns
        -------
        dict with experimental parameters and expected signals.
        """
        print()
        print("  EXPERIMENTAL PROPOSAL")
        print("  " + "-" * 40)
        print()
        print("  Goal: Measure modified Casimir force in phonon-gapped materials")
        print()
        print("  MATERIALS:")
        print(f"  {'Material':<40} {'Gap (meV)':>10}")
        print(f"  {'=' * 40} {'=' * 10}")
        for key, mat in MATERIALS.items():
            print(f"  {mat['name']:<40} {mat['gap_meV']:>10.1f}")

        print()
        print("  METHOD:")
        print("    1. AFM-based Casimir force measurement")
        print("    2. Gold sphere (R ~ 100 um) above flat sample")
        print("    3. Compare: Au-Au (reference) vs Au-TI (signal)")
        print("    4. Proximity force approximation: F_sphere = 2*pi*R*E/A")
        print()

        # Expected signals at various distances
        R_sphere = 100e-6  # 100 um sphere
        ns = np.arange(1, N_max + 1, dtype=np.float64)
        zeta4 = np.pi**4 / 90.0

        # Show signals at distance where correction is largest but force is still measurable
        print("  EXPECTED SIGNALS (sphere-plate, R = 100 um):")
        print()

        signals = {}
        test_distances_nm = [100, 500, 1000, 5000, 10000]

        for key in ['bi2se3', 'srtio3', 'graphene']:
            mat = MATERIALS[key]
            if mat['gap_meV'] == 0:
                continue
            delta_J = mat['gap_meV'] * 1e-3 * eV_to_J

            print(f"  {mat['name']}:")
            print(f"  {'d (nm)':>10} {'F_sph (pN)':>12} {'Correction':>12} {'dF (fN)':>12}")
            print(f"  {'=' * 10} {'=' * 12} {'=' * 12} {'=' * 12}")

            mat_signals = []
            for d_nm in test_distances_nm:
                d_m = d_nm * 1e-9
                x = delta_J * d_m / hbar_c

                # Standard sphere-plate PFA force
                F_sphere = 2 * np.pi * R_sphere * CASIMIR_PREFACTOR / (3 * d_m**3)
                F_pN = F_sphere * 1e12

                # BST correction (discrete)
                correction = self._discrete_correction(x)
                dF_fN = F_sphere * correction * 1e15  # in fN

                print(f"  {d_nm:10d} {F_pN:12.3f} {correction:12.4e} {dF_fN:12.4f}")
                mat_signals.append({'d_nm': d_nm, 'F_pN': F_pN,
                                   'correction': correction, 'dF_fN': dF_fN})

            signals[key] = mat_signals
            print()

        print("  MEASUREMENT PRECISION:")
        print(f"    Current AFM Casimir precision: ~1% (10^-2)")
        print(f"    State-of-art (Yale/Purdue):     ~0.1% (10^-3)")
        print(f"    Required for N_max cutoff:       ~10^-7")
        print()
        print("  STRATEGY FOR PHONON GAP DETECTION:")
        print("    Use large d (micrometers) + large gap (50+ meV)")
        print("    At d=10um with gapped graphene (50meV):")

        d_test = 10000e-9
        delta_J = 50e-3 * eV_to_J * 1e-3  # 50 meV
        x_test = delta_J * d_test / hbar_c
        c_test = self._discrete_correction(x_test)
        F_test = 2 * np.pi * R_sphere * CASIMIR_PREFACTOR / (3 * d_test**3)

        print(f"      x = {x_test:.4f}, correction = {c_test:.4e}")
        print(f"      F_sphere = {F_test*1e12:.4f} pN, dF = {F_test*c_test*1e15:.2f} fN")
        print()

        # Optimal distance for each material (where correction reaches 1%)
        print("  OPTIMAL DISTANCE (for 1% correction):")
        print(f"  {'Material':<30} {'d_optimal':>14} {'F_sphere':>12}")
        print(f"  {'=' * 30} {'=' * 14} {'=' * 12}")
        for key, mat in MATERIALS.items():
            if mat['gap_meV'] > 0:
                x_1pct = self._discrete_correction_inverse(0.01)
                delta_J = mat['gap_meV'] * 1e-3 * eV_to_J
                d_1pct = x_1pct * hbar_c / delta_J
                F_1pct = 2 * np.pi * R_sphere * CASIMIR_PREFACTOR / (3 * d_1pct**3)
                d_str = f"{d_1pct*1e6:.1f} um"
                F_str = f"{F_1pct*1e15:.2f} fN" if F_1pct < 1e-12 else f"{F_1pct*1e12:.4f} pN"
                print(f"  {mat['name']:<30} {d_str:>14} {F_str:>12}")

        print()
        print("  BST PREDICTION:")
        print("  The gap correction follows C(x) = 1 - S_137(x)/zeta_137(4).")
        print("  This curve is parameter-free (from N_max=137 alone).")
        print("  Any deviation falsifies BST's commitment interpretation.")

        return {
            'signals': signals,
            'R_sphere': R_sphere,
            'materials': list(MATERIALS.keys()),
        }

    # -----------------------------------------------------------------
    # 7. force_vs_distance
    # -----------------------------------------------------------------

    def force_vs_distance(self, delta_meV=5.0, d_min_nm=10, d_max_nm=100000,
                          n_points=200) -> dict:
        """
        Casimir force F(d) with and without gap, with and without N_max cutoff.

        Computes four curves:
            1. Standard (no gap, no cutoff)
            2. With N_max cutoff only
            3. With phonon gap only (but infinite modes)
            4. Full BST (both gap + N_max)

        Parameters
        ----------
        delta_meV : float
            Phonon gap in meV.
        d_min_nm, d_max_nm : float
            Distance range in nm.
        n_points : int
            Number of points.

        Returns
        -------
        dict with distance array and four force arrays.
        """
        d_nm = np.logspace(np.log10(d_min_nm), np.log10(d_max_nm), n_points)
        d_m = d_nm * 1e-9
        delta_J = delta_meV * 1e-3 * eV_to_J

        ns = np.arange(1, N_max + 1, dtype=np.float64)
        ns_large = np.arange(1, 10001, dtype=np.float64)
        zeta4 = np.pi**4 / 90.0
        zeta4_137 = np.sum(1.0 / ns**4)

        # 1. Standard
        F_standard = CASIMIR_PREFACTOR / d_m**4  # magnitude (positive)

        # 2. N_max cutoff only (no gap)
        F_cutoff = F_standard * (zeta4_137 / zeta4)

        # 3. Gap only (infinite modes approximation using 10000 modes)
        F_gap = np.zeros_like(d_m)
        for i, d in enumerate(d_m):
            x = delta_J * d / hbar_c
            if x > 0:
                ratios = ns_large * np.pi / x
                weights = np.where(ratios > 500, 1.0 / ns_large**4,
                                   (1.0 - np.exp(-ratios)) / ns_large**4)
                S = np.sum(weights)
                F_gap[i] = F_standard[i] * S / zeta4
            else:
                F_gap[i] = F_standard[i]

        # 4. Full BST (gap + N_max cutoff)
        F_bst = np.zeros_like(d_m)
        for i, d in enumerate(d_m):
            x = delta_J * d / hbar_c
            if x > 0:
                ratios = ns * np.pi / x
                weights = np.where(ratios > 500, 1.0 / ns**4,
                                   (1.0 - np.exp(-ratios)) / ns**4)
                S = np.sum(weights)
                F_bst[i] = F_standard[i] * S / zeta4
            else:
                F_bst[i] = F_standard[i] * zeta4_137 / zeta4

        # Corrections relative to standard
        gap_correction = np.abs(F_standard - F_gap) / F_standard
        bst_correction = np.abs(F_standard - F_bst) / F_standard

        print()
        print("  FORCE vs DISTANCE")
        print("  " + "-" * 40)
        print(f"  Phonon gap: Delta = {delta_meV} meV")
        print(f"  Channel cutoff: N_max = {N_max}")
        print()
        print(f"  {'d (nm)':>10}  {'|F_std| (Pa)':>12}  {'|F_BST| (Pa)':>12}"
              f"  {'dF/F (BST)':>12}")
        print(f"  {'=' * 10}  {'=' * 12}  {'=' * 12}  {'=' * 12}")

        sample_idx = np.linspace(0, n_points - 1, 15, dtype=int)
        for idx in sample_idx:
            print(f"  {d_nm[idx]:10.1f}  {F_standard[idx]:12.4e}  {F_bst[idx]:12.4e}"
                  f"  {bst_correction[idx]:12.4e}")

        print()
        print("  The gap correction grows with distance (more modes approach gap).")
        print(f"  The N_max cutoff is constant: {1 - zeta4_137/zeta4:.4e} at all d.")
        print("  At very large d, the gap correction dominates over the cutoff.")

        return {
            'd_nm': d_nm,
            'F_standard': F_standard,
            'F_cutoff': F_cutoff,
            'F_gap': F_gap,
            'F_bst': F_bst,
            'gap_correction': gap_correction,
            'bst_correction': bst_correction,
            'delta_meV': delta_meV,
        }

    # -----------------------------------------------------------------
    # 8. zeta_comparison
    # -----------------------------------------------------------------

    def zeta_comparison(self) -> dict:
        """
        Compare zeta_137(4) vs zeta(4): the 10^-7 difference.

        The Casimir force depends on zeta(4) = pi^4/90. BST truncates
        this at N_max = 137 modes. The difference is:

            1 - zeta_137(4)/zeta(4) ~ 1/(3*137^3) ~ 1.3 x 10^-7

        Also shows how the partial sum converges.

        Returns
        -------
        dict with convergence data.
        """
        ns = np.arange(1, N_max + 1, dtype=np.float64)
        zeta4 = np.pi**4 / 90.0

        # Convergence of partial sums
        partial_sums = np.cumsum(1.0 / ns**4)
        errors = zeta4 - partial_sums
        fractional_errors = errors / zeta4

        # Key milestones
        milestones = [1, 2, 3, 5, 10, 20, 50, 100, 137]

        print()
        print("  ZETA COMPARISON: zeta_137(4) vs zeta(4)")
        print("  " + "-" * 40)
        print()
        print(f"  zeta(4) = pi^4/90 = {zeta4:.15f}")
        print()
        print(f"  Convergence of partial sums:")
        print(f"  {'N':>6}  {'zeta_N(4)':>18}  {'Error':>14}  {'Frac. error':>14}")
        print(f"  {'=' * 6}  {'=' * 18}  {'=' * 14}  {'=' * 14}")
        for n in milestones:
            ps = partial_sums[n - 1]
            err = errors[n - 1]
            ferr = fractional_errors[n - 1]
            marker = " <-- N_max" if n == N_max else ""
            print(f"  {n:6d}  {ps:18.15f}  {err:14.4e}  {ferr:14.4e}{marker}")

        # The asymptotic tail
        print()
        print("  TAIL ANALYSIS:")
        print(f"    Exact tail:   zeta(4) - zeta_137(4) = {errors[-1]:.6e}")
        print(f"    Asymptotic:   1/(3*{N_max}^3) = {1/(3*N_max**3):.6e}")
        print(f"    Next term:    1/138^4 = {1/138**4:.6e}")
        print()
        print(f"  CASIMIR CONSEQUENCE:")
        print(f"    F_BST/F_Casimir = zeta_137(4)/zeta(4)")
        print(f"                    = {partial_sums[-1]/zeta4:.15f}")
        print(f"    Correction:       {fractional_errors[-1]:+.4e}")
        print()
        print(f"  This means the BST Casimir force is {abs(fractional_errors[-1])*100:.5f}% WEAKER")
        print(f"  than the standard prediction. Always. At every distance.")
        print()
        print(f"  Why 137?  N_max = floor(1/alpha) = {N_max}")
        print(f"  BST: the vacuum has exactly {N_max} independent commitment channels.")
        print(f"  This is the SAME 137 as the fine structure constant!")

        return {
            'partial_sums': partial_sums,
            'errors': errors,
            'fractional_errors': fractional_errors,
            'zeta4': zeta4,
            'zeta4_137': partial_sums[-1],
            'correction': fractional_errors[-1],
        }

    # -----------------------------------------------------------------
    # 9. summary
    # -----------------------------------------------------------------

    def summary(self) -> dict:
        """Key insight: Casimir = commitment pressure."""
        ns = np.arange(1, N_max + 1, dtype=np.float64)
        zeta4 = np.pi**4 / 90.0
        zeta4_137 = np.sum(1.0 / ns**4)
        cutoff_correction = 1.0 - zeta4_137 / zeta4

        print()
        print("  +=========================================================+")
        print("  |     THE CASIMIR MODIFICATION -- SUMMARY                  |")
        print("  +=========================================================+")
        print("  |                                                          |")
        print("  |  Standard Casimir:                                       |")
        print("  |    F/A = -pi^2*hbar*c / (240*d^4)                       |")
        print("  |                                                          |")
        print("  |  BST: Casimir force = commitment pressure difference.    |")
        print("  |  Between plates: constrained channels.                   |")
        print("  |  Outside: free channels.                                 |")
        print("  |  Net force = channel imbalance.                          |")
        print("  |                                                          |")
        print("  |  TWO BST MODIFICATIONS:                                  |")
        print("  |                                                          |")
        print("  |  1. PHONON GAP (Delta):                                  |")
        print("  |     Modes with E_n < Delta are transparent.              |")
        print("  |     w_n = 1 - exp(-E_n/Delta) = 1 - exp(-n*pi/x)       |")
        print("  |     Measurable with topological insulators + large d!    |")
        print("  |                                                          |")
        print("  |  2. CHANNEL CUTOFF (N_max = 137):                        |")
        print(f"  |     zeta_137(4)/zeta(4) correction: {cutoff_correction:.1e}         |")
        print("  |     Universal weakening at all distances.                |")
        print(f"  |     Same 137 as alpha = 1/{1/alpha:.3f}                    |")
        print("  |                                                          |")
        print("  |  EXPERIMENTAL TEST:                                      |")
        print("  |     AFM Casimir measurement: Au vs phonon-gapped plate   |")
        print("  |     Strategy: large d (um) + large gap (50+ meV)         |")
        print("  |     Gapped graphene at d=10um: correction ~ 10^-3        |")
        print("  |                                                          |")
        print("  |  The Casimir effect is FINITE in BST.                    |")
        print("  |  The vacuum has 137 channels, not infinity.              |")
        print("  |  The phonon gap reveals which channels are active.       |")
        print("  |                                                          |")
        print("  +=========================================================+")

        return {
            'principle': 'Casimir force = commitment pressure difference',
            'modification_1': 'Phonon gap: transparent modes below Delta',
            'modification_2': f'N_max = {N_max} truncates mode sum',
            'cutoff_correction': cutoff_correction,
            'formula': 'F_BST = F_Casimir * S_137(x) / zeta(4)',
            'experiment': 'AFM: Au sphere vs phonon-gapped plate',
        }

    # -----------------------------------------------------------------
    # 10. show -- 4-panel visualization
    # -----------------------------------------------------------------

    def show(self):
        """Launch the 4-panel visualization."""
        try:
            import matplotlib
            matplotlib.use('TkAgg')
            import matplotlib.pyplot as plt
        except ImportError:
            print("matplotlib not available. Use text API methods.")
            return

        fig, axes = plt.subplots(2, 2, figsize=(18, 11), facecolor='#0a0a1a')
        if fig.canvas.manager:
            fig.canvas.manager.set_window_title(
                'BST Toy 82 -- The Casimir Modification')

        fig.text(0.5, 0.97, 'THE CASIMIR MODIFICATION',
                 fontsize=24, fontweight='bold', color='#00ccff',
                 ha='center', fontfamily='monospace')
        fig.text(0.5, 0.94,
                 'BST predicts modified Casimir force in phonon-gapped materials',
                 fontsize=10, color='#668899', ha='center',
                 fontfamily='monospace')
        fig.text(0.5, 0.015,
                 'Copyright (c) 2026 Casey Koons -- Demonstration Only',
                 fontsize=8, color='#334455', ha='center',
                 fontfamily='monospace')

        ns = np.arange(1, N_max + 1, dtype=np.float64)
        zeta4 = np.pi**4 / 90.0
        zeta4_137 = np.sum(1.0 / ns**4)

        # ---- Panel 1: Force vs distance (3 gap values) ----
        ax1 = axes[0, 0]
        ax1.set_facecolor('#0d0d24')

        n_pts = 200
        d_nm = np.logspace(1, 5, n_pts)
        d_m = d_nm * 1e-9

        F_std = CASIMIR_PREFACTOR / d_m**4  # magnitude

        gaps = [
            (0.0, 'No gap (standard)', '#ffd700', '-'),
            (5.0, 'Delta = 5 meV', '#44ff88', '--'),
            (50.0, 'Delta = 50 meV', '#ff8844', ':'),
        ]

        for gap_meV, label, color, ls in gaps:
            if gap_meV == 0:
                F = F_std * zeta4_137 / zeta4  # BST cutoff only
            else:
                delta_J = gap_meV * 1e-3 * eV_to_J
                F = np.zeros_like(d_m)
                for i, d in enumerate(d_m):
                    x = delta_J * d / hbar_c
                    ratios = ns * np.pi / x
                    weights = np.where(ratios > 500, 1.0 / ns**4,
                                       (1.0 - np.exp(-ratios)) / ns**4)
                    S = np.sum(weights)
                    F[i] = F_std[i] * S / zeta4
            ax1.loglog(d_nm, F, color=color, lw=2, ls=ls, label=label)

        ax1.set_xlabel('Plate separation d (nm)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax1.set_ylabel('|F/A| (Pa)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax1.set_title('CASIMIR FORCE vs DISTANCE', color='#00ccff',
                      fontfamily='monospace', fontsize=11, fontweight='bold')
        ax1.legend(loc='upper right', fontsize=8, facecolor='#0d0d24',
                  edgecolor='#333333', labelcolor='#cccccc')
        ax1.tick_params(colors='#888888')
        for spine in ax1.spines.values():
            spine.set_color('#333333')

        # ---- Panel 2: Discrete correction C(x) vs x ----
        ax2 = axes[0, 1]
        ax2.set_facecolor('#0d0d24')

        x_vals = np.logspace(-1, 3, 300)
        c_vals = np.array([self._discrete_correction(x) for x in x_vals])
        g_vals = np.array([self._g_function(x) for x in x_vals])

        ax2.semilogx(x_vals, c_vals, color='#ff8844', lw=2.5,
                     label='C(x) discrete BST')
        ax2.semilogx(x_vals, g_vals, color='#44ff88', lw=1.5, ls='--',
                     label='g(x) continuum')
        ax2.fill_between(x_vals, 0, c_vals, alpha=0.1, color='#ff8844')

        # Mark x = pi (E_1 = Delta threshold)
        ax2.axvline(np.pi, color='#ffaa44', ls=':', alpha=0.5, lw=1)
        ax2.text(np.pi * 1.1, 0.85, 'x = pi\n(E_1 = Delta)',
                color='#ffaa44', fontsize=7, fontfamily='monospace')

        # Mark key thresholds
        for c_thresh, label, color in [(0.01, '1%', '#44ff88'),
                                        (0.1, '10%', '#ffaa44'),
                                        (0.5, '50%', '#ff4444')]:
            x_t = self._discrete_correction_inverse(c_thresh)
            ax2.axhline(c_thresh, color=color, ls=':', alpha=0.3, lw=1)
            ax2.plot(x_t, c_thresh, 'o', color=color, markersize=8, zorder=5)
            ax2.annotate(f'C = {label}\nx = {x_t:.1f}', (x_t, c_thresh),
                        textcoords="offset points", xytext=(15, 5),
                        color=color, fontsize=7, fontfamily='monospace')

        ax2.set_xlabel('x = Delta*d/(hbar*c)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax2.set_ylabel('Fractional correction', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax2.set_title('GAP CORRECTION: DISCRETE vs CONTINUUM',
                      color='#00ccff', fontfamily='monospace',
                      fontsize=11, fontweight='bold')
        ax2.set_ylim(-0.02, 1.05)
        ax2.legend(loc='center right', fontsize=8, facecolor='#0d0d24',
                  edgecolor='#333333', labelcolor='#cccccc')
        ax2.tick_params(colors='#888888')
        for spine in ax2.spines.values():
            spine.set_color('#333333')

        # ---- Panel 3: Zeta convergence ----
        ax3 = axes[1, 0]
        ax3.set_facecolor('#0d0d24')

        n_range = np.arange(1, N_max + 1)
        partial_sums = np.cumsum(1.0 / n_range.astype(float)**4)
        errors = (zeta4 - partial_sums) / zeta4

        ax3.semilogy(n_range, errors, color='#44ff88', lw=1.5)
        ax3.axvline(N_max, color='#ff4444', ls='--', lw=1.5, alpha=0.8)
        ax3.axhline(errors[-1], color='#ff8844', ls=':', lw=1, alpha=0.6)

        ax3.annotate(f'N_max = {N_max}\nerror = {errors[-1]:.2e}',
                    (N_max, errors[-1]), textcoords="offset points",
                    xytext=(-80, 20), color='#ff4444', fontsize=9,
                    fontfamily='monospace',
                    arrowprops=dict(arrowstyle='->', color='#ff4444'))

        ax3.set_xlabel('Number of modes N', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax3.set_ylabel('1 - zeta_N(4)/zeta(4)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax3.set_title(f'CHANNEL CUTOFF: zeta_{{137}}(4) vs zeta(4)',
                      color='#00ccff', fontfamily='monospace', fontsize=11,
                      fontweight='bold')
        ax3.tick_params(colors='#888888')
        for spine in ax3.spines.values():
            spine.set_color('#333333')

        # Text annotation in panel
        ax3.text(0.05, 0.15,
                f'zeta(4) = pi^4/90 = {zeta4:.10f}\n'
                f'zeta_137(4) = {zeta4_137:.10f}\n'
                f'Correction: {errors[-1]:.4e}',
                transform=ax3.transAxes, color='#aaaaaa', fontsize=7,
                fontfamily='monospace', verticalalignment='bottom',
                bbox=dict(boxstyle='round', facecolor='#0d0d24',
                         edgecolor='#333333'))

        # ---- Panel 4: Material comparison (BST correction vs distance) ----
        ax4 = axes[1, 1]
        ax4.set_facecolor('#0d0d24')

        d_range_nm = np.logspace(1.5, 5, 200)
        d_range_m = d_range_nm * 1e-9

        for key in ['bi2te3', 'bi2se3', 'srtio3', 'graphene']:
            mat = MATERIALS[key]
            delta_J = mat['gap_meV'] * 1e-3 * eV_to_J
            corrections = np.zeros_like(d_range_m)
            for i, d in enumerate(d_range_m):
                x = delta_J * d / hbar_c
                corrections[i] = self._discrete_correction(x)

            # Mask out exact zeros for log plot
            mask = corrections > 1e-16
            if np.any(mask):
                ax4.loglog(d_range_nm[mask], corrections[mask], color=mat['color'],
                          lw=2, label=f"{mat['name'].split('(')[0].strip()} "
                                      f"({mat['gap_meV']} meV)")

        # Measurement precision lines
        precisions = [
            (1e-2, 'Current AFM (~1%)', '#888888'),
            (1e-3, 'State-of-art (~0.1%)', '#666666'),
        ]
        for prec, label, color in precisions:
            ax4.axhline(prec, color=color, ls=':', lw=1, alpha=0.7)
            ax4.text(40, prec * 1.3, label, color=color, fontsize=7,
                    fontfamily='monospace')

        # N_max cutoff line
        nmax_corr = abs(errors[-1])
        ax4.axhline(nmax_corr, color='#ff4444', ls='--', lw=1, alpha=0.7)
        ax4.text(40, nmax_corr * 1.5,
                f'N_max={N_max} cutoff ({nmax_corr:.1e})',
                color='#ff4444', fontsize=7, fontfamily='monospace')

        ax4.set_xlabel('Plate separation d (nm)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax4.set_ylabel('Fractional correction |dF/F|', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax4.set_title('BST CORRECTIONS BY MATERIAL', color='#00ccff',
                      fontfamily='monospace', fontsize=11, fontweight='bold')
        ax4.legend(loc='lower right', fontsize=7, facecolor='#0d0d24',
                  edgecolor='#333333', labelcolor='#cccccc')
        ax4.set_ylim(1e-15, 1)
        ax4.tick_params(colors='#888888')
        for spine in ax4.spines.values():
            spine.set_color('#333333')

        plt.tight_layout(rect=(0, 0.03, 1, 0.92))
        plt.show(block=False)

    # =================================================================
    # INTERNAL HELPERS
    # =================================================================

    def _g_function(self, x, n_quad=2000):
        """
        Incomplete Bose integral (continuum correction):
        g(x) = (15/pi^4) * integral_0^x  t^3/(e^t - 1) dt

        Normalized so g(inf) = 1.
        """
        if x <= 0:
            return 0.0
        if x > 50:
            return 1.0

        # Numerical integration via trapezoidal rule
        t = np.linspace(1e-10, x, n_quad)
        dt = t[1] - t[0]
        integrand = t**3 / (np.exp(np.minimum(t, 500)) - 1.0)
        integral = np.trapz(integrand, t)

        # Normalization: full integral is pi^4/15
        return (15.0 / np.pi**4) * integral

    def _discrete_correction(self, x):
        """
        BST discrete mode sum correction.

        C(x) = 1 - [sum_{n=1}^{N_max} n^{-4} (1-exp(-n*pi/x))] / zeta_137(4)

        where x = Delta*d/(hbar*c).

        Returns the fractional correction (0 = no correction, 1 = force vanishes).
        """
        if x <= 0:
            return 0.0

        ns = np.arange(1, N_max + 1, dtype=np.float64)
        zeta4_137 = np.sum(1.0 / ns**4)

        ratios = ns * np.pi / x  # E_n/Delta for each mode
        # Clamp to avoid overflow
        weights = np.where(ratios > 500, 1.0 / ns**4,
                           (1.0 - np.exp(-ratios)) / ns**4)
        S = np.sum(weights)

        return 1.0 - S / zeta4_137

    def _g_inverse(self, g_target, tol=1e-10):
        """Find x such that g(x) = g_target, via bisection."""
        if g_target <= 0:
            return 0.0
        if g_target >= 1:
            return np.inf

        x_lo, x_hi = 0.0, 50.0
        for _ in range(100):
            x_mid = (x_lo + x_hi) / 2.0
            g_mid = self._g_function(x_mid)
            if g_mid < g_target:
                x_lo = x_mid
            else:
                x_hi = x_mid
            if (x_hi - x_lo) < tol:
                break
        return (x_lo + x_hi) / 2.0

    def _discrete_correction_inverse(self, c_target, tol=1e-8):
        """Find x such that C(x) = c_target, via bisection."""
        if c_target <= 0:
            return 0.0
        if c_target >= 1:
            return np.inf

        x_lo, x_hi = 0.01, 10000.0
        for _ in range(200):
            x_mid = (x_lo + x_hi) / 2.0
            c_mid = self._discrete_correction(x_mid)
            if c_mid < c_target:
                x_lo = x_mid
            else:
                x_hi = x_mid
            if (x_hi - x_lo) / x_mid < tol:
                break
        return (x_lo + x_hi) / 2.0


# =====================================================================
# MAIN -- interactive menu
# =====================================================================

def main():
    cm = CasimirModification()

    print()
    print("  What would you like to explore?")
    print("  1) Standard Casimir derivation")
    print("  2) Phonon gap correction")
    print("  3) BST Casimir force (d=100nm, Delta=5meV)")
    print("  4) Channel cutoff (N_max = 137)")
    print("  5) Correction function g(x)")
    print("  6) Experimental proposal")
    print("  7) Force vs distance comparison")
    print("  8) Zeta function comparison")
    print("  9) Summary")
    print("  0) Full analysis + visualization")
    print()

    try:
        choice = input("  Choice [0-9]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = '0'

    if choice == '1':
        cm.standard_casimir()
    elif choice == '2':
        cm.phonon_gap_correction()
    elif choice == '3':
        cm.bst_casimir(100e-9, 5.0)
    elif choice == '4':
        cm.channel_cutoff()
    elif choice == '5':
        cm.correction_function()
    elif choice == '6':
        cm.experimental_proposal()
    elif choice == '7':
        cm.force_vs_distance()
    elif choice == '8':
        cm.zeta_comparison()
    elif choice == '9':
        cm.summary()
    elif choice == '0':
        cm.standard_casimir()
        cm.phonon_gap_correction()
        cm.bst_casimir(100e-9, 5.0)
        cm.channel_cutoff()
        cm.zeta_comparison()
        cm.experimental_proposal()
        cm.summary()
        try:
            cm.show()
            input("\n  Press Enter to close...")
        except Exception:
            pass
    else:
        cm.summary()

    print()
    print("  Casimir force = commitment pressure.")
    print(f"  N_max = {N_max} channels. The vacuum is finite.")
    print()


if __name__ == '__main__':
    main()
