#!/usr/bin/env python3
"""
THE SUBSTRATE SAIL
==================
Sailing on the vacuum commitment rate.

In BST, every point in space has a background commitment rate Θ.
A natural object is fully coupled (σ ≈ 0). An engineered object with
frozen degrees of freedom (σ → 1) is partially decoupled. If the
decoupling is asymmetric — one face frozen, one face coupled — the
commitment rate differential produces a net force.

No fuel. No exhaust. No emissions. The silence IS the propulsion.

    from toy_substrate_sail import SubstrateSail
    ss = SubstrateSail()
    ss.force_at(1.0)                        # force at 1 AU
    ss.oumuamua_fit()                       # reconstruct from A₁
    ss.trajectory()                         # full flyby integration
    ss.propulsion_hierarchy()               # generations 0-4
    ss.deep_space_cruise(t_years=1e6)       # Λ-only over megayears
    ss.interstellar_transit(d_ly=4.24)      # time to Proxima
    ss.casimir_analogy()                    # parallel table
    ss.material_requirements(T_K=450)       # phonon gap needed

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np

# ═══════════════════════════════════════════════════════════════════
# BST CONSTANTS
# ═══════════════════════════════════════════════════════════════════

N_c = 3
n_C = 5
genus = n_C + 2       # = 7
C2 = n_C + 1          # = 6
N_max = 137            # channel capacity per contact

# Physical constants
k_B = 1.380649e-23      # J/K
hbar = 1.054571817e-34   # J·s
h_planck = 6.62607015e-34  # J·s
G_N = 6.67430e-11       # m³/(kg·s²)
c_light = 2.99792458e8  # m/s
AU = 1.496e11            # m
L_Sun = 3.828e26         # W (solar luminosity)
M_Sun = 1.989e30         # kg
m_p = 1.67262192e-27    # kg (proton mass)
m_u = 1.66053907e-27    # kg (atomic mass unit)
sigma_SB = 5.670374e-8  # W/(m²·K⁴)

# Planck units
t_Planck = 5.391e-44    # s
l_Planck = 1.616e-35    # m
m_Planck = 2.176e-8     # kg

# Cosmological
Lambda_cosmo = 1.1056e-52  # m⁻² (cosmological constant)
T_CMB = 2.7255              # K

# Conversion
ly_m = 9.461e15          # m per light-year
year_s = 3.1557e7         # s per year
day_s = 86400.0           # s per day

# ═══════════════════════════════════════════════════════════════════
# 'OUMUAMUA OBSERVED PARAMETERS
# ═══════════════════════════════════════════════════════════════════

A1_OUMUAMUA = 5.01e-6     # m/s² non-grav acceleration at 1 AU (Micheli+ 2018)
PERIHELION_AU = 0.255      # AU
SIGMA_OUMUAMUA = 0.9       # commitment silence (from toy 32 analysis)
V_INF_KM_S = 26.33         # hyperbolic excess velocity km/s

# Reference sail parameters for calibration
DELTA_SIGMA_REF = 0.8      # face A σ=0.95, face B σ=0.15 → Δσ=0.8
A_OVER_M_REF = 0.01        # m²/kg (normal density, ~100m thick)

# Calibrate effective coupling: kappa_eff = β × p_commit
# From a(r) = kappa × Δσ × (A/m) × L_Sun / (4πcr²)
# At 1 AU: A1 = kappa × Δσ_ref × (A/m)_ref × L_Sun / (4πc × AU²)
_kappa_eff = (A1_OUMUAMUA * 4 * np.pi * c_light * AU**2
              / (DELTA_SIGMA_REF * A_OVER_M_REF * L_Sun))

# Vacuum commitment rate — effective acceleration floor
# Θ_vac provides constant background in deep space
# From paper: Θ_vac = Λ / t_P² ~ 10⁻³⁵ s⁻²
# This gives a_vac ~ 10⁻¹⁵ m/s² (tiny but nonzero)
_Theta_vac = Lambda_cosmo * c_light**2  # effective vacuum rate in s⁻²
_a_vac_per_unit = _kappa_eff * _Theta_vac  # acceleration per (Δσ × A/m)

# Solar radiation pressure at 1 AU for comparison
P_RAD_1AU = L_Sun / (4 * np.pi * AU**2 * c_light)  # Pa ≈ 4.56e-6

# ═══════════════════════════════════════════════════════════════════
# PROPULSION HIERARCHY
# ═══════════════════════════════════════════════════════════════════

PROPULSION = [
    {'gen': 0, 'name': 'Ground contact',
     'examples': 'Walking, sailing, wheels',
     'pushes': 'Surface / medium',
     'fuel': 'No', 'emit': 'Vibration', 'becalm': 'Away from surface'},
    {'gen': 1, 'name': 'Mass expulsion',
     'examples': 'Rockets, jets, ion drives',
     'pushes': 'Expelled mass',
     'fuel': 'Yes', 'emit': 'Exhaust + EM', 'becalm': 'Fuel exhaustion'},
    {'gen': 2, 'name': 'Radiation pressure',
     'examples': 'Solar sails, laser sails',
     'pushes': 'Ambient photons',
     'fuel': 'No', 'emit': 'Reflected light', 'becalm': 'Far from star'},
    {'gen': 3, 'name': 'Ambient fields',
     'examples': 'Magnetic sails, E-sails',
     'pushes': 'Plasma / B-field',
     'fuel': 'No', 'emit': 'None', 'becalm': 'Beyond heliosphere'},
    {'gen': 4, 'name': 'Vacuum substrate',
     'examples': 'Substrate sail',
     'pushes': 'Commitment rate Θ',
     'fuel': 'No', 'emit': 'None', 'becalm': 'NEVER (Λ > 0)'},
]

# ═══════════════════════════════════════════════════════════════════
# CANDIDATE MATERIALS
# ═══════════════════════════════════════════════════════════════════

MATERIALS = [
    {'name': 'Phonon bandgap metamaterial',
     'gap_eV': 0.1, 'T_max_K': 500,
     'status': 'Theoretical (Earth ~2025)'},
    {'name': 'Topological insulator',
     'gap_eV': 0.05, 'T_max_K': 300,
     'status': 'Exists, σ too low'},
    {'name': 'Quantum spin liquid',
     'gap_eV': 0.01, 'T_max_K': 50,
     'status': 'Insufficient gap'},
    {'name': 'Nuclear isomer lock',
     'gap_eV': 1000.0, 'T_max_K': 1e6,
     'status': 'Beyond current tech'},
    {'name': 'BST commitment-locked crystal',
     'gap_eV': None, 'T_max_K': None,
     'status': 'Theoretical'},
]


# ═══════════════════════════════════════════════════════════════════
# THE SUBSTRATE SAIL CLASS
# ═══════════════════════════════════════════════════════════════════

class SubstrateSail:
    """
    Substrate propulsion: sailing on the vacuum commitment rate.

    An asymmetric commitment silence (Δσ > 0) across an object
    produces a net force from the vacuum — no fuel, no exhaust.

    The force scales as ~1/r² near a star (matching Θ_local),
    with a constant tiny floor from Λ in deep space.

    'Oumuamua exhibited exactly this profile: σ ≥ 0.9, A₁ ≈ 5×10⁻⁶ m/s²
    at 1 AU, zero outgassing, zero emissions. The silence IS the propulsion.
    """

    def __init__(self, quiet=False):
        if not quiet:
            self._print_header()

    def _print_header(self):
        print("=" * 68)
        print("  THE SUBSTRATE SAIL")
        print("  Sailing on the vacuum commitment rate")
        print(f"  BST channel: N_max = {N_max} bits per contact")
        print("=" * 68)

    # ─── Core physics ───

    def _accel_at(self, r_au, delta_sigma=DELTA_SIGMA_REF,
                  A_over_m=A_OVER_M_REF):
        """Substrate sail acceleration at r_au (internal, no print)."""
        r_m = r_au * AU
        # Stellar contribution: ~1/r²
        Theta_star = _kappa_eff * L_Sun / (4 * np.pi * c_light * r_m**2)
        # Vacuum floor (Lambda)
        a_star = delta_sigma * A_over_m * Theta_star
        a_vac = delta_sigma * A_over_m * _a_vac_per_unit
        a_total = a_star + a_vac
        return a_total, a_star, a_vac, Theta_star

    def force_at(self, r_au: float, delta_sigma: float = DELTA_SIGMA_REF,
                 A_over_m: float = A_OVER_M_REF) -> dict:
        """
        Substrate sail force and acceleration at distance r from the Sun.

        F = Δσ × (A/m) × m × Θ_local × κ_eff
        a = Δσ × (A/m) × Θ_local × κ_eff

        At 1 AU with Δσ=0.8, A/m=0.01: a ≈ 5×10⁻⁶ m/s² ('Oumuamua).
        """
        a_total, a_star, a_vac, _ = self._accel_at(
            r_au, delta_sigma, A_over_m)

        # Radiation pressure acceleration for comparison (assuming A/m)
        r_m = r_au * AU
        P_rad = L_Sun / (4 * np.pi * r_m**2 * c_light)
        a_rad = P_rad * A_over_m  # radiation pressure accel

        # Gravity for reference
        a_grav = G_N * M_Sun / r_m**2

        result = {
            'r_au': r_au,
            'a_total': a_total,
            'a_stellar': a_star,
            'a_vacuum': a_vac,
            'a_radiation': a_rad,
            'a_gravity': a_grav,
            'delta_sigma': delta_sigma,
            'A_over_m': A_over_m,
            'ratio_to_gravity': a_total / a_grav,
        }

        print(f"\n  SUBSTRATE SAIL at {r_au:.3f} AU")
        print(f"  ═══════════════════════════════════════")
        print(f"  Parameters: Δσ = {delta_sigma:.2f}, "
              f"A/m = {A_over_m:.3f} m²/kg")
        print(f"  a_substrate:    {a_total:.3e} m/s²  "
              f"(stellar {a_star:.3e} + vacuum {a_vac:.3e})")
        print(f"  a_radiation:    {a_rad:.3e} m/s²  (solar photons)")
        print(f"  a_gravity:      {a_grav:.3e} m/s²  (Sun)")
        print(f"  Substrate/gravity:  {a_total/a_grav:.2e}")
        print(f"  Substrate/radiation: {a_total/a_rad:.2f}×")
        return result

    def acceleration_at(self, r_au: float,
                        delta_sigma: float = DELTA_SIGMA_REF,
                        A_over_m: float = A_OVER_M_REF) -> dict:
        """Substrate sail acceleration (thin wrapper for CI scripting)."""
        a_total, a_star, a_vac, _ = self._accel_at(
            r_au, delta_sigma, A_over_m)
        return {
            'r_au': r_au,
            'a_total_m_s2': a_total,
            'a_stellar_m_s2': a_star,
            'a_vacuum_m_s2': a_vac,
        }

    # ─── 'Oumuamua reconstruction ───

    def oumuamua_fit(self) -> dict:
        """
        Reconstruct the substrate sail parameters from 'Oumuamua's
        observed non-gravitational acceleration A₁ ≈ 5×10⁻⁶ m/s².

        The product Δσ × (A/m) × κ_eff is fixed by observation.
        Different sail designs trade Δσ vs A/m.
        """
        # The combined constraint
        product = (A1_OUMUAMUA * 4 * np.pi * c_light * AU**2) / L_Sun

        # Scenarios
        scenarios = [
            {'label': 'Thin sheet (Bialy-Loeb)',
             'A_over_m': 1.0, 'note': 'A/m=1 → ~1mm thick if ρ=1 g/cm³'},
            {'label': 'Dense slab',
             'A_over_m': 0.01, 'note': 'A/m=0.01 → ~100m thick at ρ=2.5'},
            {'label': 'Heavy craft',
             'A_over_m': 0.001, 'note': 'A/m=0.001 → ~1km thick at ρ=2.5'},
        ]

        for s in scenarios:
            s['delta_sigma_kappa'] = product / s['A_over_m']
            # If kappa = kappa_eff, what delta_sigma is needed?
            s['delta_sigma'] = s['delta_sigma_kappa'] / _kappa_eff

        print()
        print("  'OUMUAMUA SUBSTRATE SAIL RECONSTRUCTION")
        print("  ════════════════════════════════════════")
        print()
        print(f"  Observed: A₁ = {A1_OUMUAMUA:.2e} m/s² at 1 AU")
        print(f"  Perihelion: {PERIHELION_AU} AU (~450 K)")
        print(f"  Silence: σ ≥ {SIGMA_OUMUAMUA} (Q ≥ 9)")
        print(f"  Outgassing: none.  Emissions: none.")
        print()
        print(f"  Constraint: Δσ × (A/m) × κ = {product:.3e}")
        print()

        # Radiation pressure comparison
        a_rad_bialy = P_RAD_1AU * 1.0  # Bialy-Loeb requires A/m = 1
        print(f"  Solar radiation at 1 AU: P = {P_RAD_1AU:.3e} Pa")
        print(f"  → Bialy-Loeb solar sail: A/m = 1 m²/kg → "
              f"a = {a_rad_bialy:.3e} m/s²")
        print(f"    (matches A₁, but requires ~1 mm sheet)")
        print()

        print(f"  {'Scenario':<25} {'A/m':>8} {'Δσ needed':>10}  Note")
        print(f"  {'─'*25} {'─'*8} {'─'*10}  {'─'*30}")
        for s in scenarios:
            ds = s['delta_sigma']
            flag = " ★" if 0.01 < ds < 1.0 else ""
            print(f"  {s['label']:<25} {s['A_over_m']:8.3f} "
                  f"{ds:10.4f}  {s['note']}{flag}")

        print()
        print("  ★ = physically reasonable (0 < Δσ < 1)")
        print()
        print("  KEY INSIGHT: Substrate propulsion relaxes the geometry")
        print("  constraint. Instead of an impossibly thin sheet (solar sail),")
        print("  a normal-density object with Δσ ~ 0.8 suffices.")
        print("  The silence does the work, not the shape.")

        return {
            'A1_observed': A1_OUMUAMUA,
            'product': product,
            'kappa_eff': _kappa_eff,
            'scenarios': scenarios,
        }

    # ─── Trajectory integration ───

    def trajectory(self, r_start_au: float = 0.255,
                   v_start_km_s: float = 87.6,
                   delta_sigma: float = DELTA_SIGMA_REF,
                   A_over_m: float = A_OVER_M_REF,
                   t_max_days: float = 400) -> dict:
        """
        Integrate a 1D radial trajectory from perihelion outward.

        Default: 'Oumuamua departure from perihelion (0.255 AU) at
        v_perihelion ≈ 87.6 km/s (vis-viva with v_inf=26.33 km/s).

        Compares gravity-only vs gravity+substrate trajectories.
        The radial excess shows how substrate propulsion adds
        velocity throughout the departure — matching Micheli et al.
        """
        dt = 300.0  # 5-minute steps
        n_steps = int(t_max_days * day_s / dt)
        max_store = min(n_steps, 50000)
        store_every = max(1, n_steps // max_store)

        r = r_start_au * AU
        v = v_start_km_s * 1000.0  # m/s (positive = outward)

        # Storage arrays
        t_arr = []
        r_arr = []
        v_arr = []
        a_sub_arr = []
        a_grav_arr = []

        def accel(r_m):
            a_g = -G_N * M_Sun / r_m**2  # gravity (inward)
            r_au_local = r_m / AU
            a_s, _, _, _ = self._accel_at(
                r_au_local, delta_sigma, A_over_m)
            return a_g, a_s  # substrate (outward)

        a_g, a_s = accel(r)
        a = a_g + a_s

        for step in range(n_steps):
            if step % store_every == 0:
                t_arr.append(step * dt / day_s)
                r_arr.append(r / AU)
                v_arr.append(v / 1000.0)
                a_sub_arr.append(a_s)
                a_grav_arr.append(abs(a_g))

            # Velocity Verlet
            r_new = r + v * dt + 0.5 * a * dt**2
            if r_new < 0.01 * AU:
                r_new = 0.01 * AU
            a_g_new, a_s_new = accel(r_new)
            a_new = a_g_new + a_s_new
            v = v + 0.5 * (a + a_new) * dt
            r = r_new
            a = a_new
            a_g = a_g_new
            a_s = a_s_new

            if r > 200 * AU:
                break

        t_arr = np.array(t_arr)
        r_arr = np.array(r_arr)
        v_arr = np.array(v_arr)
        a_sub_arr = np.array(a_sub_arr)
        a_grav_arr = np.array(a_grav_arr)

        # Gravity-only trajectory for comparison
        r2 = r_start_au * AU
        v2 = v_start_km_s * 1000.0
        r_grav = []
        for step in range(n_steps):
            if step % store_every == 0:
                r_grav.append(r2 / AU)
            a_g2 = -G_N * M_Sun / r2**2
            r2_new = r2 + v2 * dt + 0.5 * a_g2 * dt**2
            if r2_new < 0.01 * AU:
                r2_new = 0.01 * AU
            a_g2_new = -G_N * M_Sun / r2_new**2
            v2 = v2 + 0.5 * (a_g2 + a_g2_new) * dt
            r2 = r2_new
            if r2 > 200 * AU:
                break
        r_grav = np.array(r_grav[:len(t_arr)])

        print()
        print("  TRAJECTORY — 'Oumuamua Departure")
        print("  ═══════════════════════════════════════")
        print(f"  Start: {r_start_au:.3f} AU (perihelion), "
              f"v = {v_start_km_s:.1f} km/s outward")
        print(f"  Sail: Δσ = {delta_sigma:.2f}, A/m = {A_over_m:.3f} m²/kg")
        print(f"  Duration: {t_max_days:.0f} days")
        print()

        if len(r_arr) > 1:
            print(f"  Final r: {r_arr[-1]:.2f} AU, "
                  f"v: {v_arr[-1]:.1f} km/s")
            if len(r_grav) == len(r_arr):
                dr = r_arr[-1] - r_grav[-1]
                dv = v_arr[-1] - (v2 / 1000.0)
                print(f"  Excess over gravity-only:")
                print(f"    Δr = {dr:.3f} AU "
                      f"({dr*AU/1e9:.1f} million km)")
                print(f"    Δv = {dv:.2f} km/s")

        print()
        print("  The substrate force adds radial velocity throughout —")
        print("  same 1/r² profile, same direction as the observed anomaly.")

        return {
            't_days': t_arr,
            'r_au': r_arr,
            'v_km_s': v_arr,
            'a_substrate': a_sub_arr,
            'a_gravity': a_grav_arr,
            'r_gravity_only': r_grav,
            'perihelion_au': r_start_au,
            'perihelion_day': 0.0,
        }

    # ─── Propulsion hierarchy ───

    def propulsion_hierarchy(self) -> list:
        """
        Compare propulsion generations 0-4.
        Substrate propulsion is Generation 4: pushing off the vacuum itself.
        """
        print()
        print("  PROPULSION HIERARCHY")
        print("  ═══════════════════════════════════════════════════════")
        print()
        print(f"  {'Gen':>3} {'Type':<22} {'Pushes against':<22} "
              f"{'Fuel':>5} {'Emit':>10} {'Becalms':>18}")
        print(f"  {'─'*3} {'─'*22} {'─'*22} "
              f"{'─'*5} {'─'*10} {'─'*18}")

        for p in PROPULSION:
            gen = p['gen']
            marker = " ★" if gen == 4 else ""
            print(f"  {gen:3d} {p['name']:<22} {p['pushes']:<22} "
                  f"{p['fuel']:>5} {p['emit']:>10} {p['becalm']:>18}"
                  f"{marker}")

        print()
        print("  Each generation reduces dependence on carried resources.")
        print("  Generation 4 requires nothing but the vacuum —")
        print("  which is everywhere and inexhaustible.")
        print()
        print("  A solar sail goes to zero force in deep space.")
        print("  A substrate sail does not. The wind is always blowing.")

        return PROPULSION

    # ─── Deep space cruise ───

    def deep_space_cruise(self, delta_sigma: float = DELTA_SIGMA_REF,
                          A_over_m: float = A_OVER_M_REF,
                          t_years: float = 1e6) -> dict:
        """
        Compute velocity accumulated from Λ-only acceleration in deep space.

        Far from any star, only the background vacuum commitment rate Λ
        provides thrust. The force is tiny but constant and inexhaustible.
        """
        a_vac = delta_sigma * A_over_m * _a_vac_per_unit
        t_s = t_years * year_s
        v_final = a_vac * t_s
        d_final = 0.5 * a_vac * t_s**2

        v_km_s = v_final / 1000.0
        v_frac_c = v_final / c_light
        d_ly = d_final / ly_m
        d_au = d_final / AU

        print()
        print("  DEEP SPACE CRUISE — Λ Only")
        print("  ═══════════════════════════════════════")
        print(f"  Sail: Δσ = {delta_sigma:.2f}, A/m = {A_over_m:.3f} m²/kg")
        print(f"  Duration: {t_years:.0e} years")
        print()
        print(f"  Vacuum acceleration: a_Λ = {a_vac:.3e} m/s²")
        print(f"  Final velocity: {v_km_s:.3e} km/s "
              f"({v_frac_c:.3e} c)")
        print(f"  Distance covered: {d_au:.2e} AU = {d_ly:.3e} ly")
        print()

        if a_vac < 1e-20:
            print("  The Λ-only acceleration is extraordinarily small.")
            print("  Over cosmic time it integrates, but for practical")
            print("  interstellar transit, stellar flybys provide the")
            print("  real thrust. The deep-space floor means the sail")
            print("  NEVER fully becalms — that's the point.")
        else:
            print(f"  Over {t_years:.0e} years, even this tiny force")
            print(f"  builds to {v_km_s:.1f} km/s.")

        # Compare to Voyager
        v_voyager = 17.0  # km/s
        if v_km_s > 0:
            t_match_voyager = v_voyager * 1000 / a_vac / year_s
            print(f"\n  Time to match Voyager 1 ({v_voyager} km/s): "
                  f"{t_match_voyager:.2e} years")

        return {
            'a_vacuum_m_s2': a_vac,
            'v_final_km_s': v_km_s,
            'v_frac_c': v_frac_c,
            'd_final_ly': d_ly,
            'd_final_au': d_au,
            't_years': t_years,
        }

    # ─── Interstellar transit ───

    def interstellar_transit(self, d_ly: float = 4.24,
                             delta_sigma: float = DELTA_SIGMA_REF,
                             A_over_m: float = A_OVER_M_REF) -> dict:
        """
        Estimate transit time to a star at distance d_ly.

        Strategy: stellar flyby acceleration (perihelion boost)
        + deep space cruise (constant a_Λ).

        The flyby at perihelion r_p provides most of the velocity.
        """
        d_m = d_ly * ly_m

        # Phase 1: stellar flyby boost
        # Integrate acceleration from perihelion (0.1 AU) outward to 100 AU
        # using a = kappa * Δσ * (A/m) * L_Sun / (4πcr²)
        # Δv = ∫ a dr / v ≈ kappa * Δσ * (A/m) * L_Sun / (4πc) × ∫ dr/(r²v)
        # Rough estimate: v ~ v_inf, so Δv ≈ a(r_p) × r_p / v_inf × π
        r_p = 0.1 * AU  # perihelion for maximum boost
        a_p = delta_sigma * A_over_m * _kappa_eff * L_Sun / (
            4 * np.pi * c_light * r_p**2)
        # Time near perihelion: t_peri ~ 2*r_p / v_inf
        v_inf = V_INF_KM_S * 1000  # m/s
        t_peri = 2 * r_p / v_inf
        dv_flyby = a_p * t_peri

        v_after = v_inf + dv_flyby
        v_after_km = v_after / 1000

        # Phase 2: deep space with Lambda
        a_vac = delta_sigma * A_over_m * _a_vac_per_unit

        # Time to cross d_m with initial v_after and constant a_vac
        # d = v*t + 0.5*a*t^2 → solve for t
        # If a_vac is negligible: t ≈ d/v
        t_coast = d_m / v_after if v_after > 0 else np.inf
        t_coast_yr = t_coast / year_s

        # With a_vac: solve quadratic 0.5*a*t² + v*t - d = 0
        if a_vac > 0:
            disc = v_after**2 + 2 * a_vac * d_m
            t_accel = (-v_after + np.sqrt(disc)) / a_vac
            t_accel_yr = t_accel / year_s
        else:
            t_accel_yr = t_coast_yr

        # Comparison velocities
        v_voyager = 17.0   # km/s (Voyager 1)
        v_parker = 192.0   # km/s (Parker Solar Probe perihelion)
        v_starshot = 60000.0  # km/s (Breakthrough Starshot target, 0.2c)

        t_voyager = d_m / (v_voyager * 1000) / year_s
        t_parker = d_m / (v_parker * 1000) / year_s
        t_starshot = d_m / (v_starshot * 1000) / year_s

        print()
        print(f"  INTERSTELLAR TRANSIT — {d_ly:.2f} light-years")
        print(f"  ═══════════════════════════════════════════")
        print(f"  Sail: Δσ = {delta_sigma:.2f}, A/m = {A_over_m:.3f}")
        print()
        print(f"  Phase 1: Stellar flyby (r_p = 0.1 AU)")
        print(f"    a(perihelion) = {a_p:.3e} m/s²")
        print(f"    Δv from flyby = {dv_flyby/1000:.1f} km/s")
        print(f"    v_after = {v_after_km:.1f} km/s "
              f"({v_after/c_light:.4f} c)")
        print()
        print(f"  Phase 2: Deep space cruise")
        print(f"    a_Λ = {a_vac:.3e} m/s² (constant)")
        print(f"    Coast time: {t_coast_yr:.0f} years")
        print(f"    With Λ boost: {t_accel_yr:.0f} years")
        print()
        print(f"  {'Method':<28} {'v (km/s)':>10} {'Time (yr)':>12}")
        print(f"  {'─'*28} {'─'*10} {'─'*12}")
        print(f"  {'Voyager 1':<28} {v_voyager:10.0f} {t_voyager:12,.0f}")
        print(f"  {'Parker Solar Probe':<28} {v_parker:10.0f} "
              f"{t_parker:12,.0f}")
        print(f"  {'Substrate sail (this)':<28} {v_after_km:10.1f} "
              f"{t_coast_yr:12,.0f}")
        print(f"  {'Breakthrough Starshot':<28} {v_starshot:10.0f} "
              f"{t_starshot:12,.0f}")
        print()
        speedup = t_voyager / t_coast_yr if t_coast_yr > 0 else np.inf
        print(f"  Substrate sail: {speedup:.1f}× faster than Voyager")

        return {
            'd_ly': d_ly,
            'v_after_flyby_km_s': v_after_km,
            'dv_flyby_km_s': dv_flyby / 1000,
            't_coast_years': t_coast_yr,
            't_with_lambda_years': t_accel_yr,
            't_voyager_years': t_voyager,
            'speedup_vs_voyager': speedup,
        }

    # ─── Casimir analogy ───

    def casimir_analogy(self) -> dict:
        """
        Parallel between the Casimir effect and substrate propulsion.

        Casimir: exclude EM modes between plates → attractive force.
        Substrate: exclude commitment modes in material → thrust.
        Same principle, different sector.
        """
        separations = [1e-9, 10e-9, 100e-9, 1e-6]  # m
        casimir_forces = []
        for d in separations:
            # F/A = -π²ℏc / (240 d⁴)
            F_per_A = np.pi**2 * hbar * c_light / (240 * d**4)
            casimir_forces.append({
                'd_nm': d * 1e9,
                'F_per_A_Pa': F_per_A,
            })

        print()
        print("  CASIMIR ANALOGY")
        print("  ═══════════════════════════════════════════════════")
        print()
        print(f"  {'Property':<28} {'Casimir effect':<24} "
              f"{'Substrate propulsion'}")
        print(f"  {'─'*28} {'─'*24} {'─'*24}")
        print(f"  {'What is excluded':<28} {'EM modes (λ>2d)':<24} "
              f"{'Commitment modes (σ>0)'}")
        print(f"  {'What creates force':<28} {'Mode count diff.':<24} "
              f"{'Commitment rate diff.'}")
        print(f"  {'Geometry':<28} {'Parallel plates':<24} "
              f"{'Asymmetric σ faces'}")
        print(f"  {'Force direction':<28} {'Inward (attract)':<24} "
              f"{'Along Δσ axis (thrust)'}")
        print(f"  {'Energy source':<28} {'Vacuum EM field':<24} "
              f"{'Vacuum Θ field'}")
        print(f"  {'Demonstrated':<28} {'Yes (1997)':<24} "
              f"{'Not yet'}")
        print()

        print("  Casimir force at various separations:")
        print(f"  {'d (nm)':>8} {'F/A (Pa)':>14}")
        print(f"  {'─'*8} {'─'*14}")
        for cf in casimir_forces:
            print(f"  {cf['d_nm']:8.0f} {cf['F_per_A_Pa']:14.3e}")

        print()
        print("  The Casimir effect PROVES that vacuum mode exclusion")
        print("  produces real, measurable forces.")
        print("  Substrate propulsion extends this to commitment modes")
        print("  and adds asymmetry to produce thrust, not attraction.")

        return {
            'casimir_forces': casimir_forces,
            'analogy': 'Mode exclusion → force. Same principle.',
        }

    # ─── Material requirements ───

    def material_requirements(self, T_K: float = 450.0,
                              sigma_target: float = 0.9) -> dict:
        """
        What material properties are needed for a substrate sail?

        At temperature T, thermal modes with energy < kT are active.
        To freeze fraction σ of modes, need gap energy E_gap such that:
          σ = exp(-kT / E_gap)  →  E_gap = -kT / ln(σ)
        """
        # Actually: fraction active = 1 - exp(-E_gap/kT)
        # σ = 1 - (1 - exp(-E_gap/kT)) = exp(-E_gap/kT) -- no.
        # σ = N_frozen / N_total. If all modes above gap are frozen:
        # σ = exp(-kT / E_gap) only if continuous spectrum. Better:
        # For a bandgap from 0 to E_gap: modes below kT are active.
        # σ ≈ 1 - (kT / E_gap) if E_gap > kT.
        # More precisely: to maintain σ at T, need E_gap ≈ kT / (1 - σ)
        kT = k_B * T_K
        kT_eV = kT / 1.602e-19

        # E_gap needed: most modes frozen when gap > kT
        # σ ~ 1 - kT/E_gap for E_gap >> kT → E_gap = kT/(1-σ)
        E_gap = kT / (1 - sigma_target)
        E_gap_eV = E_gap / 1.602e-19
        f_gap_THz = E_gap / h_planck / 1e12

        print()
        print(f"  MATERIAL REQUIREMENTS — σ = {sigma_target:.2f} at "
              f"T = {T_K:.0f} K")
        print(f"  ═══════════════════════════════════════════════════")
        print()
        print(f"  kT = {kT_eV:.4f} eV  ({T_K:.0f} K)")
        print(f"  Required phonon gap: E_gap ≥ {E_gap_eV:.3f} eV  "
              f"({f_gap_THz:.1f} THz)")
        print(f"  (Modes below gap are active; modes above are frozen)")
        print()

        print(f"  {'Material':<32} {'Gap (eV)':>8} {'T_max(K)':>9} "
              f"{'Status'}")
        print(f"  {'─'*32} {'─'*8} {'─'*9} {'─'*24}")
        for m in MATERIALS:
            gap_str = f"{m['gap_eV']:.3f}" if m['gap_eV'] else "?"
            t_str = f"{m['T_max_K']:.0f}" if m['T_max_K'] else "?"
            ok = ""
            if m['gap_eV'] and m['gap_eV'] >= E_gap_eV:
                ok = " ✓"
            print(f"  {m['name']:<32} {gap_str:>8} {t_str:>9} "
                  f"{m['status']}{ok}")

        print()
        print("  The same property that makes a material a poor thermal")
        print("  conductor makes it a good substrate sail:")
        print("  suppressed phonon modes = suppressed commitment coupling.")
        print()
        print(f"  At {T_K:.0f} K, a phonon bandgap of {E_gap_eV:.3f} eV")
        print(f"  ({f_gap_THz:.1f} THz) freezes {sigma_target*100:.0f}% "
              f"of modes.")

        return {
            'T_K': T_K,
            'sigma_target': sigma_target,
            'kT_eV': kT_eV,
            'E_gap_eV': E_gap_eV,
            'f_gap_THz': f_gap_THz,
            'materials': MATERIALS,
        }

    # ─── Summary ───

    def summary(self) -> dict:
        """The substrate sail in one box."""
        print()
        print("  ╔═══════════════════════════════════════════════════════╗")
        print("  ║      THE SUBSTRATE SAIL — SUMMARY                    ║")
        print("  ╠═══════════════════════════════════════════════════════╣")
        print("  ║                                                       ║")
        print("  ║  The vacuum commits everywhere, always.               ║")
        print("  ║  A material that couples asymmetrically to Θ moves.   ║")
        print("  ║                                                       ║")
        print("  ║  F = Δσ × A × Θ_local × κ_eff                        ║")
        print("  ║  ~1/r² near a star.  Constant (tiny) in deep space.   ║")
        print("  ║                                                       ║")
        print("  ║  'Oumuamua: σ ≥ 0.9, A₁ ≈ 5×10⁻⁶ m/s² at 1 AU.     ║")
        print("  ║  The silence IS the propulsion.                       ║")
        print("  ║                                                       ║")
        print("  ║  Generation 4: pushing off the vacuum itself.         ║")
        print("  ║  No fuel. No exhaust. No emissions.                   ║")
        print("  ║  The wind is always blowing.                          ║")
        print("  ║                                                       ║")
        print("  ╚═══════════════════════════════════════════════════════╝")

        return {
            'A1_oumuamua': A1_OUMUAMUA,
            'sigma_oumuamua': SIGMA_OUMUAMUA,
            'kappa_eff': _kappa_eff,
            'generation': 4,
            'fuel_required': False,
        }

    # ─── Visualization ───

    def show(self):
        """Launch the 4-panel visualization."""
        try:
            import matplotlib
            matplotlib.use('TkAgg')
            import matplotlib.pyplot as plt
        except ImportError:
            print("matplotlib not available. Use text API.")
            return

        fig, axes = plt.subplots(2, 2, figsize=(18, 11),
                                 facecolor='#0a0a1a')
        if fig.canvas.manager:
            fig.canvas.manager.set_window_title(
                'BST Toy 34 — The Substrate Sail')

        fig.text(0.5, 0.97, 'THE SUBSTRATE SAIL',
                 fontsize=24, fontweight='bold', color='#00ccff',
                 ha='center', fontfamily='monospace')
        fig.text(0.5, 0.94,
                 'Sailing on the vacuum commitment rate  '
                 '(BST substrate propulsion)',
                 fontsize=10, color='#668899', ha='center',
                 fontfamily='monospace')
        fig.text(0.5, 0.015,
                 'Copyright (c) 2026 Casey Koons — Demonstration Only',
                 fontsize=8, color='#334455', ha='center',
                 fontfamily='monospace')

        # ─── Panel 1: Acceleration vs distance ───
        ax1 = axes[0, 0]
        ax1.set_facecolor('#0d0d24')

        r_arr = np.logspace(-1, 3, 200)
        a_sub = np.array([self._accel_at(r)[0] for r in r_arr])
        a_rad = np.array([P_RAD_1AU * A_OVER_M_REF / r**2
                          for r in r_arr])
        a_grav = np.array([G_N * M_Sun / (r * AU)**2 for r in r_arr])

        ax1.loglog(r_arr, a_sub, color='#ff8844', lw=2.5,
                   label='Substrate sail')
        ax1.loglog(r_arr, a_rad, color='#44ff88', lw=1.5, ls='--',
                   label='Solar radiation pressure')
        ax1.loglog(r_arr, a_grav, color='#888888', lw=1, ls=':',
                   label='Gravity (Sun)')

        # Mark 'Oumuamua
        ax1.plot(1.0, A1_OUMUAMUA, '*', color='#ffcc00', markersize=12,
                 zorder=5)
        ax1.annotate("'Oumuamua\nA₁ at 1 AU", (1.0, A1_OUMUAMUA),
                     textcoords="offset points", xytext=(15, 5),
                     color='#ffcc00', fontsize=7, fontfamily='monospace')

        # Mark perihelion
        ax1.axvline(PERIHELION_AU, color='#ff4444', ls=':', lw=1,
                    alpha=0.5)
        ax1.text(PERIHELION_AU * 1.1, a_sub[-1] * 5, 'perihelion',
                 color='#ff4444', fontsize=7, fontfamily='monospace',
                 rotation=90)

        # Lambda floor
        a_vac_floor = DELTA_SIGMA_REF * A_OVER_M_REF * _a_vac_per_unit
        ax1.axhline(a_vac_floor, color='#4444ff', ls='--', lw=1,
                    alpha=0.5)
        ax1.text(500, a_vac_floor * 3, 'Λ floor (never zero)',
                 color='#4444ff', fontsize=7, fontfamily='monospace')

        ax1.set_xlabel('Distance (AU)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax1.set_ylabel('Acceleration (m/s²)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax1.set_title('ACCELERATION vs DISTANCE', color='#00ccff',
                      fontfamily='monospace', fontsize=11,
                      fontweight='bold')
        ax1.legend(loc='upper right', fontsize=7, facecolor='#0d0d24',
                   edgecolor='#333333', labelcolor='#cccccc')
        ax1.tick_params(colors='#888888')
        for spine in ax1.spines.values():
            spine.set_color('#333333')

        # ─── Panel 2: 'Oumuamua trajectory ───
        ax2 = axes[0, 1]
        ax2.set_facecolor('#0d0d24')

        traj = self.trajectory(r_start_au=5.0, v_start_km_s=-30.0,
                               t_max_days=300)

        ax2.plot(traj['t_days'], traj['r_au'], color='#ff8844', lw=2,
                 label='Gravity + substrate')
        if len(traj['r_gravity_only']) == len(traj['t_days']):
            ax2.plot(traj['t_days'], traj['r_gravity_only'],
                     color='#44ff88', lw=1.5, ls='--',
                     label='Gravity only')

        # Mark perihelion
        idx_p = np.argmin(traj['r_au'])
        ax2.plot(traj['t_days'][idx_p], traj['r_au'][idx_p], 'v',
                 color='#ffcc00', markersize=10, zorder=5)
        ax2.annotate('perihelion', (traj['t_days'][idx_p],
                     traj['r_au'][idx_p]),
                     textcoords="offset points", xytext=(10, 10),
                     color='#ffcc00', fontsize=8, fontfamily='monospace')

        ax2.set_xlabel('Time (days)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax2.set_ylabel('Distance (AU)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax2.set_title("'OUMUAMUA TRAJECTORY", color='#00ccff',
                      fontfamily='monospace', fontsize=11,
                      fontweight='bold')
        ax2.legend(loc='upper right', fontsize=7, facecolor='#0d0d24',
                   edgecolor='#333333', labelcolor='#cccccc')
        ax2.tick_params(colors='#888888')
        for spine in ax2.spines.values():
            spine.set_color('#333333')

        # ─── Panel 3: Propulsion hierarchy ───
        ax3 = axes[1, 0]
        ax3.set_facecolor('#0d0d24')
        ax3.set_xlim(0, 10)
        ax3.set_ylim(0, 10)
        ax3.axis('off')
        ax3.set_title('PROPULSION HIERARCHY', color='#00ccff',
                      fontfamily='monospace', fontsize=11,
                      fontweight='bold')

        gen_colors = ['#666666', '#888888', '#44ff88', '#44aaff',
                      '#ffcc44']
        for i, p in enumerate(PROPULSION):
            y = 8.5 - i * 1.7
            # Generation bar
            bar_len = 1 + i * 1.8  # increasing capability
            ax3.barh(y, bar_len, 0.8, left=0.3,
                     color=gen_colors[i], alpha=0.7)
            ax3.text(0.1, y, f"G{p['gen']}", color='#ffffff',
                     fontsize=10, fontfamily='monospace',
                     fontweight='bold', va='center')
            ax3.text(bar_len + 0.6, y + 0.15, p['name'],
                     color=gen_colors[i], fontsize=9,
                     fontfamily='monospace', fontweight='bold',
                     va='center')
            ax3.text(bar_len + 0.6, y - 0.25, p['pushes'],
                     color='#888888', fontsize=7,
                     fontfamily='monospace', va='center')

        ax3.text(5, 0.3, "Gen 4: the wind is always blowing",
                 color='#ffcc44', fontsize=9, fontfamily='monospace',
                 ha='center', fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3',
                           facecolor='#1a1a0a',
                           edgecolor='#ffcc44', alpha=0.8))

        # ─── Panel 4: Transit times ───
        ax4 = axes[1, 1]
        ax4.set_facecolor('#0d0d24')

        # Sweep delta_sigma * A/m
        param = np.logspace(-3, 1, 100)  # 0.001 to 10 m²/kg equiv
        transit_years = []
        for p in param:
            # Flyby boost at 0.1 AU
            r_p = 0.1 * AU
            a_p = p * _kappa_eff * L_Sun / (
                4 * np.pi * c_light * r_p**2)
            v_inf = V_INF_KM_S * 1000
            t_peri = 2 * r_p / v_inf
            dv = a_p * t_peri
            v_total = v_inf + dv
            d_prox = 4.24 * ly_m
            t_yr = d_prox / v_total / year_s if v_total > 0 else 1e12
            transit_years.append(t_yr)

        transit_years = np.array(transit_years)

        ax4.loglog(param, transit_years, color='#ff8844', lw=2)

        # Reference lines
        t_voyager = 4.24 * ly_m / (17 * 1000) / year_s
        t_human = 80
        ax4.axhline(t_voyager, color='#666666', ls=':', lw=1)
        ax4.text(0.002, t_voyager * 0.7, f'Voyager 1 ({t_voyager:.0f} yr)',
                 color='#666666', fontsize=7, fontfamily='monospace')
        ax4.axhline(t_human, color='#ffcc44', ls='--', lw=1, alpha=0.5)
        ax4.text(0.002, t_human * 0.7, 'Human lifetime (80 yr)',
                 color='#ffcc44', fontsize=7, fontfamily='monospace')

        # Mark reference point
        ref_param = DELTA_SIGMA_REF * A_OVER_M_REF
        ref_idx = np.argmin(np.abs(param - ref_param))
        ax4.plot(ref_param, transit_years[ref_idx], '*',
                 color='#ffcc00', markersize=10, zorder=5)
        ax4.annotate("'Oumuamua\nreference",
                     (ref_param, transit_years[ref_idx]),
                     textcoords="offset points", xytext=(15, 5),
                     color='#ffcc00', fontsize=7,
                     fontfamily='monospace')

        ax4.set_xlabel('Δσ × A/m (m²/kg)', fontfamily='monospace',
                       fontsize=9, color='#888888')
        ax4.set_ylabel('Transit to Proxima (years)',
                       fontfamily='monospace', fontsize=9,
                       color='#888888')
        ax4.set_title('INTERSTELLAR TRANSIT', color='#00ccff',
                      fontfamily='monospace', fontsize=11,
                      fontweight='bold')
        ax4.tick_params(colors='#888888')
        for spine in ax4.spines.values():
            spine.set_color('#333333')

        plt.tight_layout(rect=(0, 0.03, 1, 0.92))
        plt.show(block=False)


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    ss = SubstrateSail()

    print()
    print("  What would you like to explore?")
    print("  1) Force/acceleration at a distance")
    print("  2) 'Oumuamua reconstruction")
    print("  3) Trajectory simulation")
    print("  4) Propulsion hierarchy")
    print("  5) Deep space cruise")
    print("  6) Interstellar transit times")
    print("  7) Casimir analogy")
    print("  8) Material requirements")
    print("  9) Full analysis + visualization")
    print()

    try:
        choice = input("  Choice [1-9]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = '9'

    if choice == '1':
        try:
            r = float(input("  Distance in AU: ").strip())
        except (EOFError, KeyboardInterrupt, ValueError):
            r = 1.0
        ss.force_at(r)
    elif choice == '2':
        ss.oumuamua_fit()
    elif choice == '3':
        ss.trajectory()
    elif choice == '4':
        ss.propulsion_hierarchy()
    elif choice == '5':
        ss.deep_space_cruise()
    elif choice == '6':
        ss.interstellar_transit()
    elif choice == '7':
        ss.casimir_analogy()
    elif choice == '8':
        ss.material_requirements()
    elif choice == '9':
        ss.oumuamua_fit()
        ss.propulsion_hierarchy()
        ss.deep_space_cruise()
        ss.interstellar_transit()
        ss.casimir_analogy()
        ss.material_requirements()
        ss.summary()
        try:
            ss.show()
            input("\n  Press Enter to close...")
        except Exception:
            pass
    else:
        ss.summary()


if __name__ == '__main__':
    main()
