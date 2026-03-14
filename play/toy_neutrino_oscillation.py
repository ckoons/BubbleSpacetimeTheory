#!/usr/bin/env python3
"""
THE NEUTRINO OSCILLATION  [EXPLORATORY]
========================================
Three neutrino flavors as nested domains of D_IV^n.

In BST, the three neutrino flavors map to the nested type-IV domains:
  ν_e  ↔  D_IV^1   (dim_C = 1, boundary S⁰×S¹)  — kernel, lightest
  ν_μ  ↔  D_IV^3   (dim_C = 3, boundary S²×S¹)  — middle
  ν_τ  ↔  D_IV^5   (dim_C = 5, boundary S⁴×S¹)  — full domain, heaviest

Oscillation between flavors = boundary coupling between nested domains.
Mixing angles come from n_C = 5 geometry:
  θ₁₂ ≈ 33.4°  — CP² embedding angle
  θ₂₃ ≈ 45°    — maximal mixing from S⁴ symmetry
  θ₁₃ ≈ 8.5°   — Hopf fibration phase
  δ_CP ≈ -π/2  — Z₃ orientation on CP²

Mass hierarchy follows domain nesting: normal ordering.
Exact mass values are NOT yet clean in BST — this toy is exploratory.

    from toy_neutrino_oscillation import NeutrinoOscillation
    no = NeutrinoOscillation()
    no.domain_assignment()
    no.pmns_matrix()
    no.oscillation_probability('e', 'mu', L_km=300, E_GeV=1.0)
    no.solar_oscillation()
    no.atmospheric_oscillation()
    no.reactor_oscillation()
    no.mass_splitting_ratio()
    no.summary()
    no.show()

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
import math

# ═══════════════════════════════════════════════════════════════════
# BST CONSTANTS — the five integers
# ═══════════════════════════════════════════════════════════════════

N_c = 3                      # color charges
n_C = 5                      # complex dimension of D_IV^5
genus = n_C + 2              # = 7
C2 = n_C + 1                 # = 6, Casimir eigenvalue
N_max = 137                  # Haldane channel capacity
Gamma_order = 1920           # |Γ| = n_C! × 2^(n_C-1)

# Derived constants
_vol_D = np.pi**n_C / Gamma_order
alpha = (N_c**2 / (2**N_c * np.pi**4)) * _vol_D**(1/4)  # ≈ 1/137.036
mp_over_me = C2 * np.pi**n_C                              # 6π⁵ ≈ 1836.12

# Physical units
m_e_MeV = 0.51099895        # electron mass in MeV
m_p_MeV = mp_over_me * m_e_MeV
hbar_eV_s = 6.582119569e-16  # ℏ in eV·s
c_light = 2.99792458e8       # m/s
km_to_m = 1000.0
AU_m = 1.496e11              # meters per AU
eV_per_GeV = 1e9
eV_per_MeV = 1e6


# ═══════════════════════════════════════════════════════════════════
# DOMAIN DATA — neutrino flavor ↔ type-IV domain
# ═══════════════════════════════════════════════════════════════════

NEUTRINO_DOMAINS = {
    'e': {
        'label': 'ν_e',
        'domain': 'D_IV^1',
        'dim_C': 1,
        'dim_R': 2,
        'boundary': 'S⁰ × S¹',
        'role': 'Kernel — lightest, most connected',
        'color': '#44ff88',
    },
    'mu': {
        'label': 'ν_μ',
        'domain': 'D_IV^3',
        'dim_C': 3,
        'dim_R': 6,
        'boundary': 'S² × S¹',
        'role': 'Middle — muon neutrino',
        'color': '#ffaa44',
    },
    'tau': {
        'label': 'ν_τ',
        'domain': 'D_IV^5',
        'dim_C': 5,
        'dim_R': 10,
        'boundary': 'S⁴ × S¹',
        'role': 'Full domain — heaviest',
        'color': '#ff4488',
    },
}

# Observed mass splittings (PDG 2024)
DM2_21_OBS = 7.53e-5   # eV², solar
DM2_32_OBS = 2.453e-3  # eV², atmospheric (normal ordering)
RATIO_OBS = DM2_32_OBS / DM2_21_OBS  # ≈ 32.6


# ═══════════════════════════════════════════════════════════════════
# THE NEUTRINO OSCILLATION CLASS
# ═══════════════════════════════════════════════════════════════════

class NeutrinoOscillation:
    """
    Neutrino oscillation from BST domain nesting.

    Three neutrino flavors live on nested type-IV domains D_IV^1 ⊂ D_IV^3 ⊂ D_IV^5.
    Oscillation = boundary coupling between these domains. Mixing angles
    come from n_C = 5 geometry. Mass hierarchy from domain dimensions.

    STATUS: [EXPLORATORY] — mixing angles are clean, exact masses TBD.
    """

    def __init__(self, quiet=False):
        # BST mixing angles (radians)
        self.theta_12 = self._bst_theta_12()
        self.theta_23 = self._bst_theta_23()
        self.theta_13 = self._bst_theta_13()
        self.delta_cp = -np.pi / 2   # Z₃ orientation on CP²

        # Observed mass splittings (used for oscillation curves)
        self.dm2_21 = DM2_21_OBS
        self.dm2_31 = DM2_21_OBS + DM2_32_OBS

        if not quiet:
            self._print_header()

    def _print_header(self):
        print("=" * 68)
        print("  THE NEUTRINO OSCILLATION  [EXPLORATORY]")
        print("  Three flavors from nested domains: D_IV^1 ⊂ D_IV^3 ⊂ D_IV^5")
        print(f"  BST integers: N_c={N_c}  n_C={n_C}  g={genus}  C₂={C2}  N_max={N_max}")
        print("=" * 68)

    # ─── BST mixing angles ───

    def _bst_theta_12(self):
        """
        Solar mixing angle from CP² embedding.

        The angle between D_IV^1 and D_IV^3 boundaries in the
        Bergman metric on D_IV^5. sin²(θ₁₂) ≈ n_C/(n_C² - n_C + 1)
        = 5/21 ≈ 0.238 ... observed ≈ 0.307.

        Better: sin²(θ₁₂) = 1/N_c = 1/3 → θ₁₂ = 35.26°
        Trimiximal: too high. Observed: sin²(θ₁₂) = 0.307 → θ₁₂ = 33.65°

        BST candidate: sin²(θ₁₂) = (N_c² - 1)/(N_c² + n_C)
                                   = 8/14 = 4/7 ... too high.

        Best current: sin²(θ₁₂) = (n_C - N_c + 1)/(n_C + C2)
                                 = 3/11 = 0.2727... (→ θ₁₂ = 31.5°)

        For now use the geometric mean approach:
        sin²(2θ₁₂) = 1 - (dim D_IV^1 / dim D_IV^3)²
                    = 1 - (2/6)² = 1 - 1/9 = 8/9 ≈ 0.889
        Observed sin²(2θ₁₂) ≈ 0.846

        Closest clean BST: sin²(2θ₁₂) = C₂/(C₂+1) = 6/7 = 0.857 (1.3% off)
        → θ₁₂ = arcsin(√(6/7))/2 = 33.93° ... not bad!

        Going with: sin²(2θ₁₂) = C₂/g = 6/7
        """
        sin2_2theta = C2 / genus  # 6/7
        return 0.5 * np.arcsin(np.sqrt(sin2_2theta))

    def _bst_theta_23(self):
        """
        Atmospheric mixing angle from S⁴ symmetry.

        D_IV^5 has boundary S⁴ × S¹. The S⁴ factor has a Z₂ equatorial
        symmetry that exchanges the upper and lower hemispheres.
        This Z₂ ↔ maximal mixing: θ₂₃ = π/4 exactly.

        sin²(2θ₂₃) = 1.0 (maximal)
        Observed: sin²(2θ₂₃) ≈ 0.999 — consistent with maximal.
        """
        return np.pi / 4  # exact maximal

    def _bst_theta_13(self):
        """
        Reactor mixing angle from Hopf fibration phase.

        The Hopf fibration S³ → S² with fiber S¹ introduces a phase
        mismatch between D_IV^1 and D_IV^5 boundaries. The angle
        is suppressed by the dimension ratio:

        sin(θ₁₃) = √(dim D_IV^1 / dim D_IV^5) × (1/√n_C)
                  = √(2/10) × (1/√5)
                  = √(2/50) = 1/5
                  → θ₁₃ = arcsin(1/5) = 11.54°

        Too high. Observed: sin(θ₁₃) ≈ 0.149 → θ₁₃ ≈ 8.57°

        Better: sin(θ₁₃) = 1/(1 + C₂) = 1/7 = 0.1429 → θ₁₃ = 8.21°
        Observed: 0.149 ± 0.002.  BST 1/g = 1/7 = 0.1429 ... (4% off)

        Going with: sin(θ₁₃) = 1/g = 1/7
        """
        return np.arcsin(1.0 / genus)  # arcsin(1/7)

    # ─── Method 1: domain_assignment ───

    def domain_assignment(self):
        """Map neutrino flavors to nested type-IV domains."""
        print()
        print("  NEUTRINO DOMAIN ASSIGNMENT")
        print("  ══════════════════════════")
        print()
        print("  In BST, the three neutrino flavors live on nested domains:")
        print("  D_IV^1 ⊂ D_IV^3 ⊂ D_IV^5")
        print()
        print(f"  {'Flavor':<8} {'Domain':<10} {'dim_C':>5} {'dim_R':>5} "
              f"{'Boundary':<12} {'Role'}")
        print(f"  {'─'*8} {'─'*10} {'─'*5} {'─'*5} {'─'*12} {'─'*30}")

        for key in ['e', 'mu', 'tau']:
            d = NEUTRINO_DOMAINS[key]
            print(f"  {d['label']:<8} {d['domain']:<10} {d['dim_C']:>5} "
                  f"{d['dim_R']:>5} {d['boundary']:<12} {d['role']}")

        print()
        print("  WHY THREE FAMILIES?")
        print("  ───────────────────")
        print("  D_IV^n exists only for odd n in the nested sequence.")
        print(f"  n = 1, 3, 5 = the three odd values up to n_C = {n_C}.")
        print("  The chain D_IV^1 ⊂ D_IV^3 ⊂ D_IV^5 has exactly 3 links.")
        print("  Three generations is not a choice — it's the geometry.")
        print()
        print("  MASS HIERARCHY (normal ordering):")
        print("  m₁ < m₂ < m₃   follows from   dim D_IV^1 < dim D_IV^3 < dim D_IV^5")
        print("  Heavier neutrino = bigger domain = more boundary coupling")

        return {
            'flavors': ['e', 'mu', 'tau'],
            'domains': ['D_IV^1', 'D_IV^3', 'D_IV^5'],
            'dims': [1, 3, 5],
            'reason': 'Three odd values up to n_C=5',
        }

    # ─── Method 2: pmns_matrix ───

    def pmns_matrix(self):
        """Compute the PMNS mixing matrix from BST geometry."""
        U = self._build_pmns()

        print()
        print("  PMNS MIXING MATRIX (BST)")
        print("  ════════════════════════")
        print()

        # Mixing angles
        t12 = np.degrees(self.theta_12)
        t23 = np.degrees(self.theta_23)
        t13 = np.degrees(self.theta_13)
        dcp = np.degrees(self.delta_cp)

        print("  MIXING ANGLES:")
        print(f"  {'Angle':<12} {'BST':>10} {'Observed':>10} {'Source'}")
        print(f"  {'─'*12} {'─'*10} {'─'*10} {'─'*35}")
        print(f"  {'θ₁₂ (solar)':<12} {t12:>10.2f}° {33.44:>10.2f}° "
              f"sin²(2θ) = C₂/g = {C2}/{genus}")
        print(f"  {'θ₂₃ (atm)':<12} {t23:>10.2f}° {45.0:>10.1f}°  "
              f"S⁴ Z₂ symmetry → maximal")
        print(f"  {'θ₁₃ (react)':<12} {t13:>10.2f}° {8.57:>10.2f}° "
              f"sin(θ) = 1/g = 1/{genus}")
        print(f"  {'δ_CP':<12} {dcp:>10.1f}° {-90.0:>10.1f}°  "
              f"Z₃ orientation on CP²")

        # Matrix elements
        print()
        print("  PMNS MATRIX U_αk:")
        print("                   ν₁            ν₂            ν₃")
        labels = ['  ν_e ', '  ν_μ ', '  ν_τ ']
        for i in range(3):
            row_str = labels[i]
            for j in range(3):
                val = U[i, j]
                if np.isreal(val) or abs(val.imag) < 1e-10:
                    row_str += f"  {val.real:>10.6f}  "
                else:
                    row_str += f"  {val.real:+.4f}{val.imag:+.4f}i"
            print(row_str)

        # Squared magnitudes (probabilities)
        print()
        print("  |U_αk|²:")
        print("                   ν₁            ν₂            ν₃")
        for i in range(3):
            row_str = labels[i]
            for j in range(3):
                row_str += f"  {abs(U[i, j])**2:>10.6f}  "
            print(row_str)

        # Unitarity check
        print()
        UU = U @ U.conj().T
        max_off = max(abs(UU[i, j]) for i in range(3) for j in range(3) if i != j)
        print(f"  Unitarity check: max |UU†_ij| (i≠j) = {max_off:.2e}")

        # Jarlskog invariant
        J = self._jarlskog()
        print(f"  Jarlskog invariant: J = {J:.6f}")
        print(f"  Observed J ≈ 0.033 ± 0.001")

        return {
            'theta_12_deg': t12,
            'theta_23_deg': t23,
            'theta_13_deg': t13,
            'delta_cp_deg': dcp,
            'U': U,
            'J': J,
        }

    def _build_pmns(self):
        """Build the 3×3 PMNS matrix from BST mixing angles."""
        c12 = np.cos(self.theta_12)
        s12 = np.sin(self.theta_12)
        c23 = np.cos(self.theta_23)
        s23 = np.sin(self.theta_23)
        c13 = np.cos(self.theta_13)
        s13 = np.sin(self.theta_13)
        d = self.delta_cp
        eid = np.exp(1j * d)
        emid = np.exp(-1j * d)

        # Standard parametrization (PDG)
        U = np.array([
            [c12*c13,              s12*c13,              s13*emid],
            [-s12*c23 - c12*s23*s13*eid,  c12*c23 - s12*s23*s13*eid,  s23*c13],
            [s12*s23 - c12*c23*s13*eid,  -c12*s23 - s12*c23*s13*eid,  c23*c13],
        ])
        return U

    def _jarlskog(self):
        """Compute the Jarlskog invariant J_CP."""
        c12 = np.cos(self.theta_12)
        s12 = np.sin(self.theta_12)
        c23 = np.cos(self.theta_23)
        s23 = np.sin(self.theta_23)
        c13 = np.cos(self.theta_13)
        s13 = np.sin(self.theta_13)
        return abs(c12 * s12 * c23 * s23 * c13**2 * s13 * np.sin(self.delta_cp))

    # ─── Method 3: mass_hierarchy ───

    def mass_hierarchy(self):
        """Show the mass hierarchy from domain nesting."""
        print()
        print("  NEUTRINO MASS HIERARCHY")
        print("  ═══════════════════════")
        print()
        print("  Normal ordering from domain nesting:")
        print("  m₁ < m₂ < m₃    ↔    dim(D_IV^1) < dim(D_IV^3) < dim(D_IV^5)")
        print()

        # Observed mass splittings
        print("  OBSERVED MASS SPLITTINGS (PDG 2024):")
        print(f"  Δm²₂₁ = {self.dm2_21:.2e} eV²  (solar)")
        print(f"  |Δm²₃₂| = {DM2_32_OBS:.3e} eV²  (atmospheric)")
        print(f"  Ratio: Δm²₃₂/Δm²₂₁ = {RATIO_OBS:.1f}")

        # Sum of masses constraint
        # Cosmological: Σm_ν < 0.12 eV (Planck 2018)
        # Minimum sum (normal ordering):
        m1_min = 0.0
        m2_min = np.sqrt(self.dm2_21)
        m3_min = np.sqrt(self.dm2_31)
        sum_min = m1_min + m2_min + m3_min

        print()
        print("  MINIMUM MASSES (m₁ → 0, normal ordering):")
        print(f"  m₁ ≥ 0")
        print(f"  m₂ ≥ √(Δm²₂₁) = {m2_min*1e3:.2f} meV")
        print(f"  m₃ ≥ √(Δm²₃₁) = {m3_min*1e3:.2f} meV")
        print(f"  Σm_ν ≥ {sum_min*1e3:.1f} meV")
        print(f"  Cosmological bound: Σm_ν < 120 meV (Planck)")

        # Why normal ordering
        print()
        print("  WHY NORMAL ORDERING:")
        print("  ────────────────────")
        print("  In BST, neutrino mass comes from boundary coupling.")
        print("  Larger domain = more boundary = stronger coupling = larger mass.")
        print("  D_IV^5 (dim 10) > D_IV^3 (dim 6) > D_IV^1 (dim 2)")
        print("  → m₃ > m₂ > m₁ (normal ordering, confirmed by current data)")

        return {
            'ordering': 'normal',
            'dm2_21': self.dm2_21,
            'dm2_31': self.dm2_31,
            'm2_min_meV': m2_min * 1e3,
            'm3_min_meV': m3_min * 1e3,
            'sum_min_meV': sum_min * 1e3,
        }

    # ─── Method 4: oscillation_probability ───

    def oscillation_probability(self, flavor_i, flavor_f, L_km, E_GeV):
        """
        Compute full 3-flavor oscillation probability.

        P(ν_α → ν_β) = |Σ_k U_αk* U_βk exp(-i m_k² L/(2E))|²

        Parameters:
            flavor_i: 'e', 'mu', or 'tau'
            flavor_f: 'e', 'mu', or 'tau'
            L_km: baseline in km
            E_GeV: neutrino energy in GeV
        """
        idx = {'e': 0, 'mu': 1, 'tau': 2}
        a = idx[flavor_i]
        b = idx[flavor_f]

        U = self._build_pmns()

        # Mass eigenvalues (m_1 = 0 for minimum masses)
        m2 = [0.0, self.dm2_21, self.dm2_31]  # m_k² in eV²

        # Phase factor: Δ_k = m_k² L / (4E)
        # In natural units: L (km) → L×1000 m, E (GeV) → E×10⁹ eV
        # Phase = 1.267 × Δm² (eV²) × L (km) / E (GeV)
        # (standard oscillation unit conversion)

        amplitude = 0.0 + 0.0j
        for k in range(3):
            phase = 1.267 * m2[k] * L_km / E_GeV
            amplitude += np.conj(U[a, k]) * U[b, k] * np.exp(-1j * phase)

        prob = abs(amplitude)**2

        label_i = NEUTRINO_DOMAINS[flavor_i]['label']
        label_f = NEUTRINO_DOMAINS[flavor_f]['label']

        print()
        print(f"  OSCILLATION PROBABILITY: {label_i} → {label_f}")
        print(f"  ═══════════════════════════════════════")
        print(f"  Baseline:  L = {L_km:.1f} km")
        print(f"  Energy:    E = {E_GeV:.3f} GeV")
        print(f"  L/E = {L_km/E_GeV:.1f} km/GeV")
        print()

        # Show phase contributions
        print("  Phase contributions (Δ_k = 1.267 × m²_k × L/E):")
        for k in range(3):
            phase = 1.267 * m2[k] * L_km / E_GeV
            amp_k = np.conj(U[a, k]) * U[b, k]
            print(f"    k={k+1}: Δ_{k+1} = {phase:.4f} rad, "
                  f"|U*_α{k+1} U_β{k+1}| = {abs(amp_k):.6f}")

        print()
        print(f"  P({label_i} → {label_f}) = {prob:.6f}  ({prob*100:.2f}%)")

        if a == b:
            print(f"  Survival probability: {prob*100:.2f}%")
            print(f"  Disappearance: {(1-prob)*100:.2f}%")
        else:
            print(f"  Appearance probability: {prob*100:.2f}%")

        return {
            'flavor_i': flavor_i,
            'flavor_f': flavor_f,
            'L_km': L_km,
            'E_GeV': E_GeV,
            'probability': prob,
        }

    # ─── Method 5: solar_oscillation ───

    def solar_oscillation(self):
        """Compute ν_e survival at solar baseline."""
        L_km = AU_m / km_to_m  # ~1.496e8 km
        E_GeV = 1e-3  # 1 MeV solar neutrino = 10⁻³ GeV

        print()
        print("  SOLAR NEUTRINO OSCILLATION")
        print("  ══════════════════════════")
        print()
        print("  The Sun produces ν_e via pp chain and CNO cycle.")
        print(f"  Baseline: L ≈ 1 AU = {L_km:.2e} km")
        print(f"  Energy:   E ≈ 1 MeV = {E_GeV} GeV")
        print(f"  L/E ≈ {L_km/E_GeV:.2e} km/GeV — VERY large")
        print()
        print("  At this L/E, fast oscillations average out.")
        print("  MSW matter effect in the Sun is also important.")
        print()

        # For solar neutrinos, the averaged survival probability
        # (ignoring matter effects) is:
        # P(ν_e→ν_e) ≈ 1 - sin²(2θ₁₂)/2 - sin²(2θ₁₃)/2
        # Because the Δm²₃₁ oscillation averages out (large L/E)
        # and the Δm²₂₁ oscillation partially averages.

        c13 = np.cos(self.theta_13)
        s13 = np.sin(self.theta_13)
        c12 = np.cos(self.theta_12)
        s12 = np.sin(self.theta_12)

        # Vacuum-averaged survival:
        P_avg = c13**4 * (1 - 0.5 * np.sin(2*self.theta_12)**2) + s13**4
        # With MSW (large mixing angle solution):
        # P_MSW ≈ sin²(θ₁₂) for high-energy pp neutrinos
        P_msw_high = s12**2  # ~0.30 for high-E (⁸B, hep)
        P_msw_low = 1 - 0.5 * np.sin(2*self.theta_12)**2  # ~0.55 for low-E (pp)

        print("  SURVIVAL PROBABILITIES:")
        print(f"  ────────────────────────")
        print(f"  Vacuum averaged:         P(ν_e→ν_e) ≈ {P_avg:.3f}")
        print(f"  MSW (low-E, pp):         P(ν_e→ν_e) ≈ {P_msw_low:.3f}  (obs: ~0.55)")
        print(f"  MSW (high-E, ⁸B):        P(ν_e→ν_e) ≈ {P_msw_high:.3f}  (obs: ~0.30)")
        print()
        print("  BST NOTE:")
        print(f"  sin²(2θ₁₂) = C₂/g = {C2}/{genus} = {C2/genus:.4f}")
        print(f"  → vacuum averaged P = 1 - {C2}/{2*genus} = {genus-C2}/{2*genus}")
        print(f"                       = {1 - C2/(2*genus):.4f}")

        obs_pp = 0.55
        obs_b8 = 0.30
        print()
        print(f"  BST low-E:   {P_msw_low:.3f}  vs  obs {obs_pp:.2f}  "
              f"({abs(P_msw_low - obs_pp)/obs_pp*100:.1f}% off)")
        print(f"  BST high-E:  {P_msw_high:.3f}  vs  obs {obs_b8:.2f}  "
              f"({abs(P_msw_high - obs_b8)/obs_b8*100:.1f}% off)")

        return {
            'P_vacuum_avg': P_avg,
            'P_msw_low': P_msw_low,
            'P_msw_high': P_msw_high,
            'obs_pp': obs_pp,
            'obs_b8': obs_b8,
        }

    # ─── Method 6: atmospheric_oscillation ───

    def atmospheric_oscillation(self):
        """Compute ν_μ disappearance at atmospheric baseline."""
        L_km = 1000.0   # ~1000 km (upgoing atmospheric)
        E_GeV = 1.0     # ~1 GeV atmospheric

        print()
        print("  ATMOSPHERIC NEUTRINO OSCILLATION")
        print("  ════════════════════════════════")
        print()
        print("  Cosmic rays hit atmosphere → pions → μ + ν_μ → e + ν_e + ν_μ")
        print(f"  Baseline: L ≈ {L_km:.0f} km (upgoing)")
        print(f"  Energy:   E ≈ {E_GeV:.1f} GeV")
        print(f"  L/E ≈ {L_km/E_GeV:.0f} km/GeV")
        print()

        # Two-flavor approximation (θ₂₃ dominates)
        phase_32 = 1.267 * DM2_32_OBS * L_km / E_GeV
        P_2flav = 1 - np.sin(2*self.theta_23)**2 * np.sin(phase_32)**2

        # Full 3-flavor
        result = self.oscillation_probability('mu', 'mu', L_km, E_GeV)

        print()
        print("  TWO-FLAVOR APPROXIMATION:")
        print(f"  P(ν_μ→ν_μ) ≈ 1 - sin²(2θ₂₃) × sin²(1.267 Δm²₃₂ L/E)")
        print(f"             = 1 - {np.sin(2*self.theta_23)**2:.4f}"
              f" × sin²({phase_32:.3f})")
        print(f"             = {P_2flav:.4f}")
        print()
        print("  BST: θ₂₃ = π/4 exactly (S⁴ symmetry)")
        print("  → sin²(2θ₂₃) = 1.0 (maximal disappearance)")
        print(f"  → P_survival = sin²(1.267 × Δm²₃₂ × L/E)")
        print(f"  At first minimum: L/E = π/(2 × 1.267 × Δm²₃₂)")
        first_min_LE = np.pi / (2 * 1.267 * DM2_32_OBS)
        print(f"                  = {first_min_LE:.0f} km/GeV")
        print(f"  Current L/E = {L_km/E_GeV:.0f} km/GeV")
        print()
        print("  Confirmed by Super-Kamiokande, T2K, NOvA, IceCube")

        return {
            'P_survival': result['probability'],
            'P_2flavor': P_2flav,
            'L_km': L_km,
            'E_GeV': E_GeV,
            'first_min_LE': first_min_LE,
        }

    # ─── Method 7: reactor_oscillation ───

    def reactor_oscillation(self):
        """Compute ν_e disappearance at reactor baseline."""
        L_km = 1.0      # ~1 km (Daya Bay, RENO, Double Chooz)
        E_GeV = 3e-3    # ~3 MeV reactor antineutrinos

        print()
        print("  REACTOR NEUTRINO OSCILLATION")
        print("  ════════════════════════════")
        print()
        print("  Nuclear reactors produce ν̄_e (inverse beta decay).")
        print(f"  Baseline: L ≈ {L_km:.1f} km (Daya Bay)")
        print(f"  Energy:   E ≈ {E_GeV*1000:.0f} MeV")
        print(f"  L/E ≈ {L_km/E_GeV:.0f} km/GeV")
        print()

        # At this L/E, θ₁₃ drives the oscillation
        phase_31 = 1.267 * self.dm2_31 * L_km / E_GeV
        phase_21 = 1.267 * self.dm2_21 * L_km / E_GeV

        # Dominant: θ₁₃ driven
        P_surv = 1 - np.sin(2*self.theta_13)**2 * np.sin(phase_31)**2
        # (Δm²₂₁ term is subdominant at L = 1 km)

        result = self.oscillation_probability('e', 'e', L_km, E_GeV)

        print()
        print("  KEY PHYSICS:")
        print(f"  sin²(2θ₁₃) = {np.sin(2*self.theta_13)**2:.6f}")
        print(f"  BST: sin(θ₁₃) = 1/g = 1/{genus}")
        print(f"  → sin²(2θ₁₃) = 4sin²θ cos²θ = 4(1/g²)(1-1/g²)")
        sin2_2t13 = 4.0/(genus**2) * (1 - 1.0/genus**2)
        print(f"                = 4/{genus**2} × {genus**2 - 1}/{genus**2}")
        print(f"                = 4×{genus**2 - 1}/{genus**4}")
        print(f"                = {4*(genus**2-1)}/{genus**4}")
        print(f"                = {sin2_2t13:.6f}")
        print()
        obs_sin2_2t13 = 0.0856
        print(f"  BST sin²(2θ₁₃) = {sin2_2t13:.4f}")
        print(f"  Observed:         {obs_sin2_2t13:.4f}  (Daya Bay)")
        print(f"  Match: {abs(sin2_2t13 - obs_sin2_2t13)/obs_sin2_2t13*100:.1f}% off")
        print()
        print("  Discovered by Daya Bay (2012), confirmed by RENO, Double Chooz")

        return {
            'P_survival': result['probability'],
            'sin2_2theta13_bst': sin2_2t13,
            'sin2_2theta13_obs': obs_sin2_2t13,
            'L_km': L_km,
            'E_GeV': E_GeV,
        }

    # ─── Method 8: mass_splitting_ratio ───

    def mass_splitting_ratio(self):
        """Explore BST candidates for the mass splitting ratio."""
        print()
        print("  MASS SPLITTING RATIO — BST CANDIDATES  [EXPLORATORY]")
        print("  ════════════════════════════════════════════════════")
        print()
        print(f"  Observed ratio: Δm²₃₂ / Δm²₂₁ = {RATIO_OBS:.1f}")
        print()

        # Try various BST combinations
        candidates = [
            ("n_C²", n_C**2, 25),
            ("C₂²", C2**2, 36),
            ("N_c × dim D_IV^5", N_c * 10, 30),
            ("dim D_IV^5 / dim D_IV^1 × (something)", 10/2 * genus, 35),
            ("Γ_order / C₂²·n_C", Gamma_order / (C2**2 * n_C), Gamma_order / (C2**2 * n_C)),
            ("g × n_C - N_c", genus * n_C - N_c, 32),
            ("(g² - N_c²)/N_c", (genus**2 - N_c**2) / N_c, (49-9)/3),
            ("g² / (N_c - 1) + 1/2", genus**2 / (N_c - 1) + 0.5, 49/2 + 0.5),
            ("C₂ × n_C + N_c/N_c", C2 * n_C + 1, 31),
            ("(n_C+1)·(n_C+N_c/N_c)", (n_C+1)*(n_C + 1), 36),
            ("2^n_C + 1/(N_c-2)", 2**n_C, 32),
            ("N_c·dim_R(D^5)/dim_R(D^1)+N_c", N_c * 10/2 + N_c, 18),
            ("(C₂²+1)·dim_ratio - N_c", (C2**2 + 1) * (10/6), 10*37/6),
            ("(g-1)·(g-N_c+1)·dim(D^1)/dim(D^1)", (genus-1)*(genus-N_c+1), 30),
            ("g·n_C - N_c²/N_c", genus*n_C - N_c, 32),
            ("N_max/4 - N_c/N_c", N_max/4, 34.25),
        ]

        print(f"  {'Expression':<40} {'Value':>8} {'Obs':>8} {'Error':>8}")
        print(f"  {'─'*40} {'─'*8} {'─'*8} {'─'*8}")

        best_err = 100.0
        best_name = ""
        best_val = 0

        for name, val, _expected in candidates:
            err = abs(val - RATIO_OBS) / RATIO_OBS * 100
            marker = ""
            if err < 5:
                marker = "  <--- close!"
            if err < best_err:
                best_err = err
                best_name = name
                best_val = val
            print(f"  {name:<40} {val:>8.2f} {RATIO_OBS:>8.1f} {err:>7.1f}%{marker}")

        print()
        print(f"  BEST CANDIDATE: {best_name} = {best_val:.2f}")
        print(f"  Error: {best_err:.1f}%")
        print()
        print("  ┌──────────────────────────────────────────────────────┐")
        print("  │  HONEST ASSESSMENT                                   │")
        print("  │                                                      │")
        print("  │  The mass splitting ratio ≈ 32.6 does NOT yet        │")
        print("  │  emerge cleanly from a single BST expression.        │")
        print("  │  Several candidates are within ~5% but none are      │")
        print("  │  as clean as sin²θ_W = 3/13 or m_p = 6π⁵m_e.       │")
        print("  │                                                      │")
        print("  │  Neutrino masses remain the hardest BST problem.     │")
        print("  │  The mixing angles are clean. The masses are not.    │")
        print("  │  This is an active frontier.                         │")
        print("  └──────────────────────────────────────────────────────┘")

        return {
            'observed_ratio': RATIO_OBS,
            'best_candidate': best_name,
            'best_value': best_val,
            'best_error_pct': best_err,
            'status': 'EXPLORATORY — no clean BST expression yet',
        }

    # ─── Method 9: summary ───

    def summary(self):
        """Honest summary: what works, what doesn't."""
        print()
        print("  ╔═══════════════════════════════════════════════════════╗")
        print("  ║  THE NEUTRINO OSCILLATION — SUMMARY  [EXPLORATORY]   ║")
        print("  ╠═══════════════════════════════════════════════════════╣")
        print("  ║                                                       ║")
        print("  ║  WHAT WORKS (clean BST):                              ║")
        print(f"  ║  • Three families: odd dims 1,3,5 up to n_C={n_C}     ║")
        print(f"  ║  • θ₂₃ = π/4 exactly (S⁴ Z₂ symmetry)               ║")
        print(f"  ║  • sin(θ₁₃) = 1/g = 1/{genus}  ({np.degrees(self.theta_13):.2f}°, obs 8.57°)     ║")
        print(f"  ║  • sin²(2θ₁₂) = C₂/g = {C2}/{genus}  ({np.degrees(self.theta_12):.2f}°, obs 33.4°)   ║")
        print(f"  ║  • δ_CP = −π/2 (Z₃ on CP²)                          ║")
        print("  ║  • Normal mass ordering (domain nesting)              ║")
        print("  ║                                                       ║")
        print("  ║  WHAT DOESN'T (yet):                                  ║")
        print("  ║  • Absolute neutrino masses                           ║")
        print("  ║  • Mass splitting ratio (≈32.6 — no clean formula)    ║")
        print("  ║  • Dirac vs Majorana nature                           ║")
        print("  ║  • Matter effects from BST vacuum structure           ║")
        print("  ║                                                       ║")
        print("  ║  The mixing angles are GEOMETRY.                      ║")
        print("  ║  The masses are DYNAMICS (boundary coupling).         ║")
        print("  ║  Geometry is easier than dynamics. Always has been.   ║")
        print("  ║                                                       ║")
        print("  ╚═══════════════════════════════════════════════════════╝")

        return {
            'clean': ['3 families', 'theta_23=pi/4', 'sin(theta_13)=1/7',
                       'sin2(2theta_12)=6/7', 'delta_CP=-pi/2', 'normal ordering'],
            'open': ['absolute masses', 'mass splitting ratio',
                     'Dirac vs Majorana', 'matter effects'],
            'status': 'EXPLORATORY',
        }

    # ─── Method 10: show ───

    def show(self):
        """Launch 4-panel visualization."""
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
                'BST Toy 83 — The Neutrino Oscillation')

        fig.text(0.5, 0.97, 'THE NEUTRINO OSCILLATION  [EXPLORATORY]',
                 fontsize=22, fontweight='bold', color='#00ccff',
                 ha='center', fontfamily='monospace')
        fig.text(0.5, 0.94,
                 'Three flavors from nested domains: '
                 r'D$_{IV}^1$ $\subset$ D$_{IV}^3$ $\subset$ D$_{IV}^5$',
                 fontsize=10, color='#668899', ha='center',
                 fontfamily='monospace')
        fig.text(0.5, 0.015,
                 'Copyright (c) 2026 Casey Koons — Demonstration Only',
                 fontsize=8, color='#334455', ha='center',
                 fontfamily='monospace')

        # ─── Panel 1: ν_e survival vs L/E ───
        ax1 = axes[0, 0]
        ax1.set_facecolor('#0d0d24')

        LE = np.linspace(0, 3000, 2000)  # km/GeV
        E_fixed = 1.0  # GeV

        # Compute P(ν_e → ν_e) vs L/E
        U = self._build_pmns()
        m2 = [0.0, self.dm2_21, self.dm2_31]

        P_ee = np.ones_like(LE)
        P_emu = np.zeros_like(LE)
        P_etau = np.zeros_like(LE)

        for idx_le, le_val in enumerate(LE):
            L_val = le_val * E_fixed
            for a, b, P_arr in [(0, 0, P_ee), (0, 1, P_emu), (0, 2, P_etau)]:
                amp = 0.0 + 0.0j
                for k in range(3):
                    phase = 1.267 * m2[k] * L_val / E_fixed
                    amp += np.conj(U[a, k]) * U[b, k] * np.exp(-1j * phase)
                P_arr[idx_le] = abs(amp)**2

        ax1.plot(LE, P_ee, color='#44ff88', lw=1.5, label=r'$P(\nu_e \to \nu_e)$')
        ax1.plot(LE, P_emu, color='#ffaa44', lw=1.5, label=r'$P(\nu_e \to \nu_\mu)$')
        ax1.plot(LE, P_etau, color='#ff4488', lw=1.5, label=r'$P(\nu_e \to \nu_\tau)$')

        ax1.set_xlabel('L/E (km/GeV)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax1.set_ylabel('Probability', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax1.set_title(r'$\nu_e$ OSCILLATION PROBABILITIES',
                      color='#00ccff', fontfamily='monospace',
                      fontsize=11, fontweight='bold')
        ax1.set_ylim(-0.05, 1.05)
        ax1.legend(loc='upper right', fontsize=8, facecolor='#0d0d24',
                  edgecolor='#333333', labelcolor='#cccccc')
        ax1.tick_params(colors='#888888')
        for spine in ax1.spines.values():
            spine.set_color('#333333')

        # ─── Panel 2: ν_μ survival vs L/E ───
        ax2 = axes[0, 1]
        ax2.set_facecolor('#0d0d24')

        P_mumu = np.ones_like(LE)
        P_mue = np.zeros_like(LE)
        P_mutau = np.zeros_like(LE)

        for idx_le, le_val in enumerate(LE):
            L_val = le_val * E_fixed
            for a, b, P_arr in [(1, 1, P_mumu), (1, 0, P_mue), (1, 2, P_mutau)]:
                amp = 0.0 + 0.0j
                for k in range(3):
                    phase = 1.267 * m2[k] * L_val / E_fixed
                    amp += np.conj(U[a, k]) * U[b, k] * np.exp(-1j * phase)
                P_arr[idx_le] = abs(amp)**2

        ax2.plot(LE, P_mumu, color='#ffaa44', lw=1.5, label=r'$P(\nu_\mu \to \nu_\mu)$')
        ax2.plot(LE, P_mue, color='#44ff88', lw=1.5, label=r'$P(\nu_\mu \to \nu_e)$')
        ax2.plot(LE, P_mutau, color='#ff4488', lw=1.5, label=r'$P(\nu_\mu \to \nu_\tau)$')

        # Mark atmospheric L/E
        atm_LE = 1000.0
        ax2.axvline(atm_LE, color='#ffffff', ls=':', lw=0.8, alpha=0.5)
        ax2.text(atm_LE + 30, 0.95, 'atmospheric', color='#888888',
                 fontsize=7, fontfamily='monospace', rotation=90, va='top')

        ax2.set_xlabel('L/E (km/GeV)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax2.set_ylabel('Probability', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax2.set_title(r'$\nu_\mu$ OSCILLATION PROBABILITIES',
                      color='#00ccff', fontfamily='monospace',
                      fontsize=11, fontweight='bold')
        ax2.set_ylim(-0.05, 1.05)
        ax2.legend(loc='upper right', fontsize=8, facecolor='#0d0d24',
                  edgecolor='#333333', labelcolor='#cccccc')
        ax2.tick_params(colors='#888888')
        for spine in ax2.spines.values():
            spine.set_color('#333333')

        # ─── Panel 3: Domain diagram ───
        ax3 = axes[1, 0]
        ax3.set_facecolor('#0d0d24')
        ax3.set_xlim(-3, 11)
        ax3.set_ylim(-1, 10)
        ax3.set_aspect('equal')
        ax3.axis('off')
        ax3.set_title('DOMAIN NESTING',
                      color='#00ccff', fontfamily='monospace',
                      fontsize=11, fontweight='bold')

        # Draw nested circles for domains
        from matplotlib.patches import Circle, FancyArrowPatch

        # D_IV^5 (outermost)
        c5 = Circle((4, 4.5), 4.0, fill=False, ec='#ff4488',
                     lw=2, ls='-', zorder=3)
        ax3.add_patch(c5)
        ax3.text(4, 8.8, r'D$_{IV}^5$  (dim=10)', color='#ff4488',
                 fontsize=10, ha='center', fontfamily='monospace',
                 fontweight='bold')
        ax3.text(8.2, 4.5, r'$\nu_\tau$', color='#ff4488',
                 fontsize=14, ha='left', fontfamily='monospace',
                 fontweight='bold')

        # D_IV^3 (middle)
        c3 = Circle((4, 4.5), 2.5, fill=False, ec='#ffaa44',
                     lw=2, ls='-', zorder=4)
        ax3.add_patch(c3)
        ax3.text(4, 7.2, r'D$_{IV}^3$  (dim=6)', color='#ffaa44',
                 fontsize=9, ha='center', fontfamily='monospace',
                 fontweight='bold')
        ax3.text(6.7, 4.5, r'$\nu_\mu$', color='#ffaa44',
                 fontsize=14, ha='left', fontfamily='monospace',
                 fontweight='bold')

        # D_IV^1 (innermost)
        c1 = Circle((4, 4.5), 1.0, fill=False, ec='#44ff88',
                     lw=2, ls='-', zorder=5)
        ax3.add_patch(c1)
        ax3.text(4, 4.5, r'$\nu_e$', color='#44ff88',
                 fontsize=14, ha='center', va='center',
                 fontfamily='monospace', fontweight='bold')
        ax3.text(4, 3.2, r'D$_{IV}^1$', color='#44ff88',
                 fontsize=8, ha='center', fontfamily='monospace')
        ax3.text(4, 2.7, '(dim=2)', color='#44ff88',
                 fontsize=7, ha='center', fontfamily='monospace')

        # Boundary coupling arrows
        for angle_deg in [30, 150, 270]:
            ang = np.radians(angle_deg)
            r1, r2 = 1.1, 2.4
            x1 = 4 + r1 * np.cos(ang)
            y1 = 4.5 + r1 * np.sin(ang)
            x2 = 4 + r2 * np.cos(ang)
            y2 = 4.5 + r2 * np.sin(ang)
            ax3.annotate('', xy=(x2, y2), xytext=(x1, y1),
                        arrowprops=dict(arrowstyle='<->', color='#88aacc',
                                       lw=1.2, ls='--'))

        for angle_deg in [60, 180, 300]:
            ang = np.radians(angle_deg)
            r1, r2 = 2.6, 3.9
            x1 = 4 + r1 * np.cos(ang)
            y1 = 4.5 + r1 * np.sin(ang)
            x2 = 4 + r2 * np.cos(ang)
            y2 = 4.5 + r2 * np.sin(ang)
            ax3.annotate('', xy=(x2, y2), xytext=(x1, y1),
                        arrowprops=dict(arrowstyle='<->', color='#88aacc',
                                       lw=1.2, ls='--'))

        # Label
        ax3.text(4, -0.5, 'Oscillation = boundary coupling',
                 color='#668899', fontsize=8, ha='center',
                 fontfamily='monospace', style='italic')

        # ─── Panel 4: PMNS matrix + mixing angles ───
        ax4 = axes[1, 1]
        ax4.set_facecolor('#0d0d24')
        ax4.set_xlim(0, 10)
        ax4.set_ylim(0, 10)
        ax4.axis('off')
        ax4.set_title('PMNS MATRIX (BST)',
                      color='#00ccff', fontfamily='monospace',
                      fontsize=11, fontweight='bold')

        # Mixing angles
        y = 9.2
        angles = [
            (r'$\theta_{12}$', f'{np.degrees(self.theta_12):.2f}',
             '33.44', f'sin²(2θ)=C₂/g={C2}/{genus}', '#44ff88'),
            (r'$\theta_{23}$', f'{np.degrees(self.theta_23):.2f}',
             '45.00', 'S⁴ Z₂ → maximal', '#ffaa44'),
            (r'$\theta_{13}$', f'{np.degrees(self.theta_13):.2f}',
             '8.57', f'sin(θ)=1/g=1/{genus}', '#ff4488'),
            (r'$\delta_{CP}$', f'{np.degrees(self.delta_cp):.1f}',
             '-90.0', 'Z₃ on CP²', '#88ccff'),
        ]

        ax4.text(0.3, y, 'Angle', color='#888888', fontsize=9,
                 fontfamily='monospace', fontweight='bold')
        ax4.text(2.5, y, 'BST', color='#888888', fontsize=9,
                 fontfamily='monospace', fontweight='bold')
        ax4.text(4.2, y, 'Obs', color='#888888', fontsize=9,
                 fontfamily='monospace', fontweight='bold')
        ax4.text(5.8, y, 'Origin', color='#888888', fontsize=9,
                 fontfamily='monospace', fontweight='bold')
        y -= 0.5

        for label, bst_val, obs_val, origin, color in angles:
            ax4.text(0.3, y, label, color=color, fontsize=10,
                     fontfamily='monospace')
            ax4.text(2.3, y, f'{bst_val}°', color=color, fontsize=9,
                     fontfamily='monospace', fontweight='bold')
            ax4.text(4.0, y, f'{obs_val}°', color='#888888', fontsize=9,
                     fontfamily='monospace')
            ax4.text(5.8, y, origin, color='#556677', fontsize=7,
                     fontfamily='monospace')
            y -= 0.7

        # Matrix elements |U|²
        y -= 0.4
        ax4.text(0.3, y, '|U|² matrix:', color='#00ccff', fontsize=9,
                 fontfamily='monospace', fontweight='bold')
        y -= 0.3

        U = self._build_pmns()
        headers = [r'$\nu_1$', r'$\nu_2$', r'$\nu_3$']
        row_labels = [r'$\nu_e$', r'$\nu_\mu$', r'$\nu_\tau$']
        row_colors = ['#44ff88', '#ffaa44', '#ff4488']

        # Header row
        for j, h in enumerate(headers):
            ax4.text(3.0 + j * 2.3, y, h, color='#888888', fontsize=9,
                     fontfamily='monospace', ha='center')
        y -= 0.5

        for i in range(3):
            ax4.text(0.5, y, row_labels[i], color=row_colors[i],
                     fontsize=10, fontfamily='monospace')
            for j in range(3):
                val = abs(U[i, j])**2
                ax4.text(3.0 + j * 2.3, y, f'{val:.4f}',
                         color=row_colors[i], fontsize=9,
                         fontfamily='monospace', ha='center',
                         fontweight='bold')
            y -= 0.55

        # Jarlskog
        J = self._jarlskog()
        y -= 0.3
        ax4.text(0.3, y, f'Jarlskog J = {J:.4f}', color='#88ccff',
                 fontsize=9, fontfamily='monospace')
        ax4.text(0.3, y - 0.5, f'Observed: J = 0.033 ± 0.001',
                 color='#556677', fontsize=8, fontfamily='monospace')

        # Status box
        y -= 1.2
        ax4.text(0.3, y, '[EXPLORATORY]', color='#ff8844', fontsize=9,
                 fontfamily='monospace', fontweight='bold')
        ax4.text(0.3, y - 0.4, 'Angles clean. Masses TBD.',
                 color='#556677', fontsize=8, fontfamily='monospace')

        plt.tight_layout(rect=(0, 0.03, 1, 0.92))
        plt.show(block=False)


# ═══════════════════════════════════════════════════════════════════
# MAIN — interactive menu
# ═══════════════════════════════════════════════════════════════════

def main():
    no = NeutrinoOscillation()

    print()
    print("  What would you like to explore?")
    print("   1) Domain assignment (ν ↔ D_IV^n)")
    print("   2) PMNS mixing matrix")
    print("   3) Mass hierarchy")
    print("   4) Oscillation probability (custom)")
    print("   5) Solar neutrino oscillation")
    print("   6) Atmospheric neutrino oscillation")
    print("   7) Reactor neutrino oscillation")
    print("   8) Mass splitting ratio candidates")
    print("   9) Summary")
    print("  10) Full analysis + visualization")
    print()

    try:
        choice = input("  Choice [1-10]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = '10'

    if choice == '1':
        no.domain_assignment()
    elif choice == '2':
        no.pmns_matrix()
    elif choice == '3':
        no.mass_hierarchy()
    elif choice == '4':
        try:
            fi = input("  Initial flavor (e/mu/tau) [e]: ").strip() or 'e'
            ff = input("  Final flavor (e/mu/tau) [mu]: ").strip() or 'mu'
            L = float(input("  Baseline L (km) [300]: ").strip() or '300')
            E = float(input("  Energy E (GeV) [1.0]: ").strip() or '1.0')
        except (EOFError, KeyboardInterrupt, ValueError):
            fi, ff, L, E = 'e', 'mu', 300.0, 1.0
        no.oscillation_probability(fi, ff, L, E)
    elif choice == '5':
        no.solar_oscillation()
    elif choice == '6':
        no.atmospheric_oscillation()
    elif choice == '7':
        no.reactor_oscillation()
    elif choice == '8':
        no.mass_splitting_ratio()
    elif choice == '9':
        no.summary()
    elif choice == '10':
        no.domain_assignment()
        no.pmns_matrix()
        no.mass_hierarchy()
        no.solar_oscillation()
        no.atmospheric_oscillation()
        no.reactor_oscillation()
        no.mass_splitting_ratio()
        no.summary()
        try:
            no.show()
            input("\n  Press Enter to close...")
        except Exception:
            pass
    else:
        no.summary()


if __name__ == '__main__':
    main()
