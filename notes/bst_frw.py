"""
BST FRW Computation: Cosmological Constant from Channel Vacuum
=============================================================
BST predicts no dark matter (channel noise explains galaxy rotation curves).
We run FRW evolution with:
  - Baryons only (no DM)
  - Flat universe (k = 0; pre-spatial phase transition homogenizes the substrate)
  - Lambda from BST: Lambda = F_BST * (d_0 / l_Pl)^4
  - Standard radiation content (photons + 3 neutrino flavors)

Inputs used (3 observational inputs):
  1. H_0 (scanning both Planck value 67.4 and local value 73.0)
  2. Omega_b * h^2 = 0.0224 (CMB baryon acoustic oscillations)
  3. T_CMB = 2.725 K (CMB temperature today)

Computes:
  - Omega_Lambda (BST, no DM, flat constraint)
  - Lambda in Planck units
  - d_0 from Lambda = F_BST * (d_0/l_Pl)^4
  - Comparison to previous BST estimate

Author: Casey Koons & Claude (Anthropic), March 2026
"""
import numpy as np
from scipy.integrate import quad

# ── Constants ──────────────────────────────────────────────────────────────
c_km  = 2.99792458e5    # km/s
c_m   = 2.99792458e8    # m/s
Mpc_m = 3.085677581e22  # m per Mpc
l_Pl  = 1.616255e-35    # Planck length, m
t_Pl  = 5.391247e-44    # Planck time, s
G_SI  = 6.674e-11       # m^3 kg^-1 s^-2
hbar  = 1.054572e-34    # J s
k_B   = 1.380649e-23    # J/K
m_e   = 9.10938e-31     # kg
m_Pl  = 2.17643e-8      # kg

# ── BST constants ──────────────────────────────────────────────────────────
F_BST = 0.09855          # vacuum free energy (exact from partition function)
N_MAX = 137
alpha_Wyler = 1.0/137.036082

# ── Cosmological inputs ────────────────────────────────────────────────────
T_CMB   = 2.725          # K, CMB temperature today
Omega_b_h2 = 0.0224      # baryon density × h^2 (Planck 2018)

# Radiation: photons + 3 massless neutrino species
# Omega_r * h^2 = Omega_gamma * h^2 * (1 + 3*(7/8)*(4/11)^(4/3))
# Standard value:
Omega_r_h2 = 4.18e-5     # photons + neutrinos (relativistic)

# ── Lambda target ──────────────────────────────────────────────────────────
# Observed Lambda in Planck units (CODATA):
Lambda_obs_Pl = 2.9e-122
d0_target = (Lambda_obs_Pl / F_BST)**0.25
print(f"Observed Lambda = {Lambda_obs_Pl:.3e} Planck units")
print(f"Target d_0      = {d0_target:.4e} l_Pl\n")

# ── FRW WITHOUT DARK MATTER ────────────────────────────────────────────────
print("=" * 65)
print("FLAT UNIVERSE, NO DARK MATTER (BST prediction)")
print("  Omega_total = Omega_b + Omega_r + Omega_Lambda = 1")
print("=" * 65)
print()

results = []
print(f"{'H_0':>8}  {'Omega_b':>8}  {'Omega_r':>8}  {'Omega_L':>8}  "
      f"{'Lambda_Pl':>12}  {'d_0 (l_Pl)':>12}  {'d_0 err':>8}")
print("-" * 80)

for H0_km in [67.4, 70.0, 73.0]:
    h  = H0_km / 100.0
    h2 = h**2

    Omega_b = Omega_b_h2 / h2
    Omega_r = Omega_r_h2 / h2
    Omega_L = 1.0 - Omega_b - Omega_r          # flat, no DM

    # H_0 in Planck units (s^{-1} → t_Pl^{-1})
    H0_SI  = H0_km * 1e3 / Mpc_m               # s^{-1}
    H0_Pl  = H0_SI * t_Pl                      # dimensionless Planck units

    # Lambda in Planck units
    Lambda_Pl = 3.0 * Omega_L * H0_Pl**2

    # d_0 from Lambda = F_BST * (d_0/l_Pl)^4
    d0 = (Lambda_Pl / F_BST)**0.25

    err_pct = (d0 - d0_target) / d0_target * 100

    print(f"{H0_km:8.1f}  {Omega_b:8.4f}  {Omega_r:8.2e}  {Omega_L:8.4f}  "
          f"{Lambda_Pl:12.4e}  {d0:12.4e}  {err_pct:+7.1f}%")

    results.append((H0_km, Omega_L, Lambda_Pl, d0, err_pct))

print()
print(f"{'Previous BST estimate':35s}  d_0 = 1.78e-31 l_Pl  (2.5 orders from obs)")
print(f"{'This calculation (H0=67.4, no DM)':35s}  d_0 = {results[0][3]:.4e} l_Pl"
      f"  ({results[0][4]:+.1f}% from obs)")

print()
print("=" * 65)
print("WHAT THE GAP MEANS")
print("=" * 65)
print(f"""
The 2.5-order gap in the previous BST estimate came from using
d_0 ≈ 10^{{-30.75}} l_Pl derived from channel utilization (ρ_universe/ρ_137).

The FRW no-DM computation with the same BST inputs gives d_0 ≈ 8e-31 l_Pl,
which is only {results[0][4]:+.1f}% from the target.

The improvement factor: {d0_target/1.78e-31:.1f}x (in d_0) = {(d0_target/1.78e-31)**4:.0f}x (in Lambda)

The residual {results[0][4]:+.1f}% comes from:
  - H_0 uncertainty: Planck gives 67.4, local measures give 73 km/s/Mpc
  - BST-predicted H_0 could differ from ΛCDM-inferred H_0 (Hubble tension)
  - Neutrino masses (3 flavors, currently massless approximation)
  - Baryon-to-photon ratio from BST (currently using observed value)
""")

# ── What H_0 would give exact d_0? ─────────────────────────────────────────
print("=" * 65)
print("EXACT d_0: WHAT H_0 DOES BST REQUIRE?")
print("=" * 65)
h2_target = 0.0224 / (1 - 4.18e-5/0.01)  # approximate
# More precise: Lambda_obs = 3 * Omega_L * H0^2
# Omega_L = 1 - 0.0224/h^2 - 4.18e-5/h^2
# Lambda_obs = 3 * (1 - (0.0224+4.18e-5)/h^2) * H0^2
# where H0 = h * 100 km/s/Mpc
# Lambda_obs (Pl) = 3 * (h^2 - 0.0224 - 4.18e-5) * (H_0/100)^2 * (100km/s/Mpc in Pl)^2 / h^2

H100_Pl = (100.0 * 1e3 / Mpc_m) * t_Pl   # H_0 in Planck units for h=1
# Lambda = 3*(h^2 - 0.02242)*H100_Pl^2
# Solve: Lambda_obs = 3*(h^2 - 0.02242)*H100_Pl^2
#        h^2 = Lambda_obs/(3*H100_Pl^2) + 0.02242
Omega_m_h2 = Omega_b_h2  # baryon only, no DM
h2_exact = Lambda_obs_Pl / (3 * H100_Pl**2) + Omega_m_h2
H0_exact = np.sqrt(h2_exact) * 100
print(f"  H_0 needed for exact d_0 agreement: {H0_exact:.2f} km/s/Mpc")
print(f"  (Planck 2018 CMB: 67.4 ± 0.5;  local distance ladder: 73.0 ± 1.0)")
print()

# ── Hubble tension analysis ─────────────────────────────────────────────────
print("=" * 65)
print("BST PREDICTION: H_0 AND THE HUBBLE TENSION")
print("=" * 65)
print(f"""
Standard ΛCDM with DM gives H_0 ≈ 67.4 km/s/Mpc from CMB.
BST without DM requires H_0 ≈ {H0_exact:.1f} km/s/Mpc for exact Λ agreement.

The Hubble tension range: CMB 67.4 ± 0.5,  local ladder 73.0 ± 1.0.
BST requirement ({H0_exact:.1f} km/s/Mpc) is BELOW both — outside the observed range.

Physical reason: removing dark matter forces Omega_Lambda → 0.95 to maintain
flatness. This high dark energy fraction raises the inferred Lambda for a given
H_0 above the observed value. To bring Lambda back down to 2.9e-122 requires
a lower H_0 than either CMB or local measurements provide.

This means BST cannot simultaneously satisfy:
  (a) flat universe with no dark matter
  (b) observed Lambda = 2.9e-122
  (c) H_0 in the observed range [67, 73] km/s/Mpc
using the current FRW approach with observed Omega_b h^2.

The resolution requires a first-principles BST derivation of H_0 and/or
Omega_b h^2 — the two remaining observational inputs in this calculation.
""")

# ── Phase transition temperature ───────────────────────────────────────────
print("=" * 65)
print("BST PHASE TRANSITION TEMPERATURE")
print("=" * 65)
# T_c = 130.5 * hbar*c / (k_B * R_s)
# R_s = rho * R_b = 137 * hbar/(m_e * c)
R_s_m = 137 * hbar / (m_e * c_m)     # R_s in meters
T_c_K = 130.5 * hbar * c_m / (k_B * R_s_m)
T_c_MeV = k_B * T_c_K / 1.602e-13    # in MeV
print(f"  R_s = 137 × λ_e = {R_s_m:.4e} m = {R_s_m*1e15:.4f} fm")
print(f"  T_c = 130.5 × (ℏc)/(k_B R_s) = {T_c_K:.4e} K  = {T_c_MeV:.4f} MeV")
print(f"  T_c corresponds to: k_B T_c = {T_c_MeV:.3f} MeV")
print(f"  This is the scale of: electron-positron pair annihilation (~0.5 MeV)")
print(f"  Universe age at T_c: t ~ 1/(2H) at T_c — radiation dominated")
print()
# t ~ sqrt(45/(16 pi^3 g_star)) * m_Pl / T^2   (natural units)
# At T_c ~ 0.5 MeV:
# t ~ 1 / (2 * H(T_c))
# H(T_c) = sqrt(8*pi*G/3 * rho_r) with rho_r = (pi^2/30)*g_star*T^4
# g_star at 0.5 MeV ~ 10 (photons + electrons + positrons + 3 neutrinos)
g_star = 10.75
# H^2 = (8*pi*G/3) * (pi^2/30) * g_star * T^4
# H = sqrt(8*pi^3*g_star/90) * T^2 / m_Pl
T_c_nat = T_c_MeV       # in MeV
m_Pl_MeV = 1.22089e22   # MeV
H_c = np.sqrt(8*np.pi**3*g_star/90) * T_c_nat**2 / m_Pl_MeV  # MeV
H_c_SI = H_c * 1.602e-13 / hbar   # 1/s
t_c_s = 0.5 / H_c_SI
print(f"  Universe age at T_c: t ≈ 1/(2H_c) ≈ {t_c_s:.2e} seconds")
print(f"  This is {t_c_s:.1f} seconds after the Big Bang")
print(f"  (BBN epoch: t ~ 1-300 seconds; T_c falls right at the start)")
print()

# ── Summary ────────────────────────────────────────────────────────────────
print("=" * 65)
print("SUMMARY: THE d_0 RESULT")
print("=" * 65)
print(f"""
PREVIOUS (BST_Cosmological_Constant.md):
  d_0 = 10^{{-30.75}} l_Pl = 1.78e-31 l_Pl
  Lambda = 9.9e-125 Planck units
  Gap from observed: 2.5 orders

THIS COMPUTATION (FRW, no DM, H_0 = 67.4 km/s/Mpc):
  Omega_Lambda = 0.9505  (vs 0.685 in ΛCDM with DM)
  Lambda = {results[0][2]:.2e} Planck units
  d_0 = {results[0][3]:.2e} l_Pl
  Gap from observed: {results[0][4]:+.1f}%

WHAT H_0 GIVES EXACT AGREEMENT:
  H_0 = {H0_exact:.2f} km/s/Mpc  (BELOW both CMB 67.4 and local 73.0 — outside observed range)

TENSION: BST no-DM flat model with observed Omega_b h^2 cannot simultaneously
  match Lambda_obs AND H_0_obs. One of the three inputs must come from BST
  first principles rather than ΛCDM observation:
    Option A: BST predicts H_0 ≈ 58 km/s/Mpc (requires justification)
    Option B: BST Omega_b h^2 differs from ΛCDM-inferred value (baryon asymmetry)
    Option C: BST Lambda calculation has a correction not yet included

WHAT BST NEEDS NEXT:
  1. BST prediction of H_0 from FRW dynamics (no DM, BST matter content)
  2. BST prediction of Omega_b h^2 from the baryon asymmetry
  Either would resolve the tension and complete the parameter-free derivation of d_0.

  T_c = {T_c_MeV:.3f} MeV corresponds to the BBN epoch, suggesting R_b = lambda_e
  is a reasonable identification (not the electroweak scale).
""")
