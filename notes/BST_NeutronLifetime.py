#!/usr/bin/env python3
"""
BST: Neutron Lifetime Calculation
Casey Koons & Claude Opus 4.6, March 12, 2026

The neutron beta decay: n → p + e⁻ + ν̄_e

Standard formula:
  1/τ_n = (G_F² cos²θ_C m_e⁵) / (2π³) × f × (1 + 3g_A²) × (1 + δ_R)

BST inputs:
  - v = m_p²/(7m_e) = 246.12 GeV → G_F
  - (m_n - m_p)/m_e = 91/36 → endpoint energy
  - sinθ_C = 1/(2√5) → |V_ud|² = cos²θ_C
  - α = 1/137.036 → Fermi function (Coulomb correction)
  - g_A = ? (not yet derived from BST — use observed value)
"""

import numpy as np
from scipy.integrate import quad
import math

pi = math.pi
alpha = 1.0 / 137.036

# ================================================================
# Physical constants
# ================================================================
m_e = 0.51099895  # MeV
m_p = 938.272     # MeV
hbar = 6.58212e-22  # MeV·s
c = 3e10          # cm/s (not needed, using natural units)

# ================================================================
# BST inputs
# ================================================================
print("=" * 70)
print("  BST NEUTRON LIFETIME CALCULATION")
print("=" * 70)
print()

# BST Fermi scale
v_BST = m_p**2 / (7 * m_e)   # MeV
v_BST_GeV = v_BST / 1000
print(f"  BST Fermi scale: v = m_p²/(7m_e) = {v_BST_GeV:.4f} GeV")
print(f"  Observed:                            246.22 GeV")

# G_F from BST
# G_F = 1/(√2 v²) in natural units
# In standard units: G_F/(ħc)³ = 1.1664×10⁻⁵ GeV⁻²
G_F_BST = 1.0 / (math.sqrt(2) * (v_BST_GeV)**2)  # GeV⁻²
G_F_obs = 1.16638e-5  # GeV⁻²
print(f"  BST G_F:  {G_F_BST:.5e} GeV⁻²")
print(f"  Observed: {G_F_obs:.5e} GeV⁻²")
print(f"  Match:    {(G_F_BST - G_F_obs)/G_F_obs * 100:+.3f}%")
print()

# BST mass difference
# (m_n - m_p)/m_e = 91/36
delta_m_BST = (91.0/36.0) * m_e  # MeV
delta_m_obs = 1.29334  # MeV
print(f"  BST Δm = (91/36)m_e = {delta_m_BST:.5f} MeV")
print(f"  Observed:              {delta_m_obs:.5f} MeV")
print(f"  Match:    {(delta_m_BST - delta_m_obs)/delta_m_obs * 100:+.3f}%")
print()

# BST Cabibbo angle → |V_ud|²
sin_theta_C = 1.0 / (2 * math.sqrt(5))
cos2_theta_C = 1 - sin_theta_C**2
V_ud_sq_BST = cos2_theta_C
V_ud_sq_obs = 0.97373**2  # PDG 2024
print(f"  BST |V_ud|² = cos²θ_C = 1 - 1/(4×5) = {V_ud_sq_BST:.6f}")
print(f"  Observed:                               {V_ud_sq_obs:.6f}")
print(f"  Match:    {(V_ud_sq_BST - V_ud_sq_obs)/V_ud_sq_obs * 100:+.3f}%")
print()

# Axial coupling g_A (NOT YET DERIVED from BST)
g_A = 1.2762  # PDG 2024 (from neutron decay measurements)
print(f"  g_A = {g_A} (observed — not yet derived from BST)")
print(f"  Factor (1 + 3g_A²) = {1 + 3*g_A**2:.6f}")
print()

# ================================================================
# Phase space integral with Fermi function
# ================================================================
print("=" * 70)
print("  PHASE SPACE INTEGRAL")
print("=" * 70)
print()

# The dimensionless endpoint energy
E0 = delta_m_BST / m_e  # = 91/36 ≈ 2.5278
E0_obs = delta_m_obs / m_e

print(f"  BST endpoint: E₀/m_e = 91/36 = {E0:.6f}")
print(f"  Observed:     E₀/m_e = {E0_obs:.6f}")
print()

def fermi_function(Z, E_over_me):
    """Fermi function F(Z, E) for Coulomb correction.

    Z = nuclear charge of daughter (Z=1 for proton)
    E_over_me = electron total energy in units of m_e
    """
    if E_over_me <= 1.0:
        return 0.0
    beta = math.sqrt(1 - 1.0 / E_over_me**2)  # v/c of electron
    eta = alpha * Z / beta
    # Non-relativistic Fermi function
    x = 2 * pi * eta
    if abs(x) < 1e-10:
        return 1.0
    return x / (1 - math.exp(-x))

def phase_space_integrand(epsilon, E0_val, with_fermi=True):
    """Integrand for the phase space factor f.

    epsilon = electron total energy in units of m_e (≥ 1)
    E0_val = endpoint energy in units of m_e
    """
    if epsilon >= E0_val or epsilon <= 1:
        return 0.0
    p_e = math.sqrt(epsilon**2 - 1)  # electron momentum / m_e
    E_nu = E0_val - epsilon  # neutrino energy / m_e

    integrand = epsilon * p_e * E_nu**2

    if with_fermi:
        integrand *= fermi_function(1, epsilon)

    return integrand

# Without Fermi function (bare phase space)
f_bare, _ = quad(phase_space_integrand, 1.0, E0, args=(E0, False))
f_bare_obs, _ = quad(phase_space_integrand, 1.0, E0_obs, args=(E0_obs, False))

# With Fermi function
f_fermi, _ = quad(phase_space_integrand, 1.0, E0, args=(E0, True))
f_fermi_obs, _ = quad(phase_space_integrand, 1.0, E0_obs, args=(E0_obs, True))

print(f"  Phase space f (bare, no Coulomb):")
print(f"    BST (E₀ = 91/36): f = {f_bare:.6f}")
print(f"    Obs (E₀ = 2.531): f = {f_bare_obs:.6f}")
print()
print(f"  Phase space f (with Fermi function):")
print(f"    BST (E₀ = 91/36): f = {f_fermi:.6f}")
print(f"    Obs (E₀ = 2.531): f = {f_fermi_obs:.6f}")
print(f"    Fermi correction:  {(f_fermi/f_bare - 1)*100:.2f}%")
print()

# Standard value of f from literature
# The accepted value: f = 1.6887 (includes recoil, radiative, etc.)
# Our simple Fermi function gives the leading Coulomb correction
f_literature = 1.6887
print(f"  Literature value (full corrections): f = {f_literature}")
print(f"  Our Fermi function result:           f = {f_fermi:.4f}")
print(f"  Ratio: {f_fermi/f_literature:.4f}")
print()

# ================================================================
# Neutron lifetime calculation
# ================================================================
print("=" * 70)
print("  NEUTRON LIFETIME")
print("=" * 70)
print()

# Master formula:
# 1/τ_n = (G_F² m_e⁵) / (2π³) × |V_ud|² × f × (1 + 3g_A²) × (1 + δ_R)
#
# In natural units where ℏ = c = 1:
# G_F is in GeV⁻², m_e in GeV, τ in GeV⁻¹
# Convert τ from GeV⁻¹ to seconds: τ(s) = τ(GeV⁻¹) × ℏ

# Radiative correction
delta_R = 0.01405  # standard inner radiative correction (Marciano & Sirlin)
print(f"  Radiative correction: δ_R = {delta_R}")
print()

# Convert everything to GeV for natural units
m_e_GeV = m_e / 1000  # GeV
G_F = G_F_BST  # already in GeV⁻²

# The rate in natural units (GeV)
rate = (G_F**2 * m_e_GeV**5) / (2 * pi**3) * V_ud_sq_BST * f_fermi * (1 + 3*g_A**2) * (1 + delta_R)

# Convert to seconds: rate is in GeV, lifetime = 1/rate in GeV⁻¹
# ℏ = 6.582×10⁻²⁵ GeV·s, so τ(s) = ℏ/rate(GeV)
hbar_GeVs = 6.58212e-25  # GeV·s
tau_n_BST = hbar_GeVs / rate  # seconds

tau_n_obs = 879.4  # seconds (PDG 2024, beam+bottle average)

print(f"  BST neutron lifetime (with BST inputs + observed g_A):")
print(f"    τ_n = {tau_n_BST:.1f} s")
print(f"    Observed: {tau_n_obs:.1f} s")
print(f"    Ratio: {tau_n_BST/tau_n_obs:.4f}")
print(f"    Deviation: {(tau_n_BST - tau_n_obs)/tau_n_obs * 100:+.2f}%")
print()

# ================================================================
# Use the OBSERVED inputs for comparison
# ================================================================
print("--- COMPARISON: all observed inputs ---")
G_F_obs_val = G_F_obs
V_ud_sq = V_ud_sq_obs
rate_obs_inputs = (G_F_obs_val**2 * m_e_GeV**5) / (2 * pi**3) * V_ud_sq * f_fermi_obs * (1 + 3*g_A**2) * (1 + delta_R)
tau_obs_inputs = hbar_GeVs / rate_obs_inputs

print(f"  Standard calculation (all observed inputs):")
print(f"    τ_n = {tau_obs_inputs:.1f} s")
print(f"    Observed: {tau_n_obs:.1f} s")
print(f"    Deviation: {(tau_obs_inputs - tau_n_obs)/tau_n_obs * 100:+.2f}%")
print()

# ================================================================
# Use the literature f value
# ================================================================
print("--- WITH LITERATURE f VALUE ---")
rate_lit = (G_F_BST**2 * m_e_GeV**5) / (2 * pi**3) * V_ud_sq_BST * f_literature * (1 + 3*g_A**2) * (1 + delta_R)
tau_lit = hbar_GeVs / rate_lit

print(f"  BST inputs + literature f = {f_literature}:")
print(f"    τ_n = {tau_lit:.1f} s")
print(f"    Observed: {tau_n_obs:.1f} s")
print(f"    Deviation: {(tau_lit - tau_n_obs)/tau_n_obs * 100:+.2f}%")
print()

rate_lit_obs = (G_F_obs_val**2 * m_e_GeV**5) / (2 * pi**3) * V_ud_sq_obs * f_literature * (1 + 3*g_A**2) * (1 + delta_R)
tau_lit_obs = hbar_GeVs / rate_lit_obs

print(f"  All observed + literature f = {f_literature}:")
print(f"    τ_n = {tau_lit_obs:.1f} s")
print(f"    Observed: {tau_n_obs:.1f} s")
print(f"    Deviation: {(tau_lit_obs - tau_n_obs)/tau_n_obs * 100:+.2f}%")
print()

# ================================================================
# Sensitivity analysis
# ================================================================
print("=" * 70)
print("  SENSITIVITY ANALYSIS")
print("=" * 70)
print()

# τ ∝ 1/(G_F² × |V_ud|² × Δm⁵ × (1+3g_A²))
# So: δτ/τ ≈ -2(δG_F/G_F) - 2(δ|V_ud|/|V_ud|) - 5(δΔm/Δm) - ...

print("  The lifetime goes as ~ 1/(G_F² × |V_ud|² × Δm⁵ × (1+3g_A²))")
print()
print("  BST deviations from observed values:")
print(f"    G_F:     {(G_F_BST - G_F_obs)/G_F_obs * 100:+.3f}% → τ shift: {-2*(G_F_BST - G_F_obs)/G_F_obs * 100:+.3f}%")
print(f"    |V_ud|²: {(V_ud_sq_BST - V_ud_sq_obs)/V_ud_sq_obs * 100:+.3f}% → τ shift: {-(V_ud_sq_BST - V_ud_sq_obs)/V_ud_sq_obs * 100:+.3f}%")
print(f"    Δm:      {(delta_m_BST - delta_m_obs)/delta_m_obs * 100:+.3f}% → τ shift: {-5*(delta_m_BST - delta_m_obs)/delta_m_obs * 100:+.3f}%")
print()

# ================================================================
# What g_A would BST need?
# ================================================================
print("=" * 70)
print("  WHAT g_A WOULD BST PREDICT?")
print("=" * 70)
print()

# If τ_n = 879.4 s, what g_A does BST need?
# rate = (G_F² m_e⁵)/(2π³) × |V_ud|² × f × (1 + 3g_A²) × (1 + δ_R) = ℏ/τ
target_rate = hbar_GeVs / tau_n_obs
factor_without_gA = (G_F_BST**2 * m_e_GeV**5) / (2 * pi**3) * V_ud_sq_BST * f_literature * (1 + delta_R)
one_plus_3gA2_needed = target_rate / factor_without_gA
gA_needed = math.sqrt((one_plus_3gA2_needed - 1) / 3)

print(f"  To match τ_n = {tau_n_obs} s with BST inputs:")
print(f"    Need (1 + 3g_A²) = {one_plus_3gA2_needed:.6f}")
print(f"    Need g_A = {gA_needed:.4f}")
print(f"    Observed g_A = {g_A}")
print(f"    BST g_A deviation: {(gA_needed - g_A)/g_A * 100:+.3f}%")
print()

# BST candidate for g_A?
# g_A is the ratio of axial to vector coupling
# Some BST candidates:
candidates = [
    ("4/π", 4/pi),
    ("√(5/3)", math.sqrt(5/3)),
    ("(7/3)^(1/2)", math.sqrt(7/3)),
    ("9/(7)", 9/7),
    ("N_c·7/(4n_C+3)", 3*7/23),
    ("(2n_C+3)/(2n_C)", 13/10),
    ("√(n_C/3)", math.sqrt(5/3)),
]

print("  BST candidates for g_A:")
for name, val in candidates:
    dev = (val - g_A)/g_A * 100
    print(f"    g_A = {name:20s} = {val:.6f}  ({dev:+.2f}%)")

print()

# ================================================================
# Summary
# ================================================================
print("=" * 70)
print("  SUMMARY")
print("=" * 70)
print(f"""
  BST neutron lifetime with BST inputs + observed g_A:
    τ_n(BST) = {tau_lit:.1f} s  (observed: {tau_n_obs:.1f} s, {(tau_lit - tau_n_obs)/tau_n_obs * 100:+.2f}%)

  BST inputs used:
    G_F from v = m_p²/(7m_e)        ({(G_F_BST - G_F_obs)/G_F_obs * 100:+.3f}% from observed)
    |V_ud|² = cos²θ_C = 19/20       ({(V_ud_sq_BST - V_ud_sq_obs)/V_ud_sq_obs * 100:+.3f}% from observed)
    Δm = (91/36)m_e                  ({(delta_m_BST - delta_m_obs)/delta_m_obs * 100:+.3f}% from observed)
    g_A = {g_A}  (observed, not yet BST-derived)

  The neutron lifetime is extremely sensitive to Δm (∝ Δm⁵),
  so BST's 0.13% error in Δm propagates to ~0.6% in τ_n.

  To fully derive τ_n from BST: need g_A from D(IV,5) geometry.
  Best BST candidate: g_A ≈ {gA_needed:.4f} (needed to match τ_n exactly).
""")
