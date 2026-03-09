"""
BST Hubble: Backfit from Model-Independent Observations
=======================================================
Flat universe, no dark matter.  F_BST = 0.09855 (exact from partition function).
Lambda = F_BST * (d_0/l_Pl)^4.

We ask: given each input combination, what does BST imply for H₀, d_0, Lambda?
And backfit: given Lambda_obs exactly, what H₀ is required?

Input combinations (roughly ordered by model-independence):
  1.  ΛCDM reference inputs (biased — assumes DM, listed for comparison)
  2.  Megamaser H₀ (geometric, pure VLBI — no DM assumption)
  3.  Local distance ladder H₀ (Cepheid/SN — calibration model-dependent)
  4.  BBN D/H → Omega_b h² (nuclear physics only)
  5.  BBN + BST T_c entropy correction (dilutes baryon-to-photon ratio)
  6.  Cosmic chronometers (galaxy ages → H(z), no model assumed)
  7.  Adding neutrino mass (BST predicts 3 flavors; lab bound Σm_ν < 0.45 eV)
  8.  Pure BST backfit (Lambda_obs exact → required H₀ for each Omega_b input)

Author: Casey Koons & Claude (Anthropic), March 2026
"""
import numpy as np
from scipy.optimize import minimize_scalar

pi = np.pi

# ── Constants ──────────────────────────────────────────────────────────────
Mpc_m  = 3.085677581e22
t_Pl   = 5.391247e-44

# ── BST exact values ────────────────────────────────────────────────────────
F_BST      = 0.09855          # vacuum free energy (exact from partition fn)
Lambda_obs = 2.9e-122         # observed Lambda in Planck units (CODATA)
d0_target  = (Lambda_obs / F_BST)**0.25   # = 7.365e-31 l_Pl

# T_c from BST partition function (exact)
T_c_MeV = 0.487              # phase transition temperature

# ── Standard physical inputs (model-free) ──────────────────────────────────
T_CMB       = 2.725           # K — pure blackbody, completely model-free
Omega_r_h2  = 4.18e-5         # photons + 3 massless nu (from T_CMB alone)

# H₀ = 100h km/s/Mpc → Planck units
H100_Pl = (100e3 / Mpc_m) * t_Pl   # = 1.7471e-61

# ── Helper functions ────────────────────────────────────────────────────────
def Lambda_Omega_from(H0, Omega_b_h2, Omega_nu_h2=0.0):
    h2     = (H0/100)**2
    OmegaB = Omega_b_h2 / h2
    OmegaR = Omega_r_h2 / h2
    OmegaN = Omega_nu_h2 / h2
    OmegaL = 1.0 - OmegaB - OmegaR - OmegaN
    H0_Pl  = H0 * 1e3 / Mpc_m * t_Pl
    return 3.0 * OmegaL * H0_Pl**2, OmegaL

def d0_from_Lambda(L): return (L / F_BST)**0.25

def H0_for_exact_Lambda(Omega_b_h2, Omega_nu_h2=0.0):
    """H₀ that makes Lambda_BST = Lambda_obs exactly (flat, no DM)."""
    h2 = Lambda_obs/(3*H100_Pl**2) + Omega_b_h2 + Omega_nu_h2 + Omega_r_h2
    return np.sqrt(h2) * 100

def H_BST_z(z, H0, Omega_b_h2, Omega_nu_h2=0.0):
    """H(z) for flat BST no-DM universe."""
    h2     = (H0/100)**2
    OmegaB = Omega_b_h2 / h2
    OmegaR = Omega_r_h2 / h2
    OmegaN = Omega_nu_h2 / h2
    OmegaL = 1 - OmegaB - OmegaR - OmegaN
    return H0 * np.sqrt(OmegaB*(1+z)**3 + OmegaR*(1+z)**4
                       + OmegaN*(1+z)**3 + OmegaL)

# ── BBN: D/H → Omega_b h² ──────────────────────────────────────────────────
# Cooke et al. 2018: D/H = (2.527 ± 0.030) × 10^{-5}  [most precise measurement]
# BBN nuclear physics (PArthENoPE/PRIMAT) → eta_10 = 6.10
# Omega_b h² = eta_10 * (T_CMB/2.725)^3 / 273.9
eta_10_DH     = 6.097
Omega_b_h2_DH = eta_10_DH * (T_CMB/2.725)**3 / 273.9   # ≈ 0.02225

# ── BST T_c correction: entropy dilution of baryon-to-photon ratio ──────────
# Phase transition at T_c = 0.487 MeV injects latent heat into photon bath.
# Entropy increases by factor (1 + delta), diluting eta by same factor.
# delta is uncertain without full partition function; we scan:
#   delta = 0.05  → 5%  entropy injection  (weak transition)
#   delta = 0.20  → 20% entropy injection  (moderate)
#   delta = 2.0   → 200% (tripling entropy; needed for Li-7 factor ~3 reduction)
# Effect on Omega_b h²:  Omega_b h² → Omega_b h² / (1 + delta)
# Effect on H₀ needed:   lower Omega_b h² → lower H₀ (makes gap worse)

def Omega_b_BST(delta): return Omega_b_h2_DH / (1 + delta)

# ── Cosmic chronometers: H(z) from passive galaxy ages (Moresco+) ──────────
# These are the most model-independent H(z) measurements available.
# Selected data (z, H [km/s/Mpc], sigma_H):
cc_data = [
    (0.07,  69.0,  19.6),   # Stern et al. 2010
    (0.09,  69.0,  12.0),   # Jimenez et al. 2003
    (0.12,  68.6,  26.2),   # Zhang et al. 2014
    (0.17,  83.0,   8.0),   # Simon et al. 2005
    (0.20,  72.9,  29.6),   # Zhang et al. 2014
    (0.27,  77.0,  14.0),   # Simon et al. 2005
    (0.28,  88.8,  36.6),   # Zhang et al. 2014
    (0.40,  95.0,  17.0),   # Simon et al. 2005
    (0.48, 101.0,  23.0),   # Stern et al. 2010 (approx)
    (0.57, 100.3,   3.7),   # Moresco 2015
    (0.75, 100.0,  18.5),   # Moresco et al. 2022
]

def chi2_cc(H0, Omega_b_h2=0.0224):
    return sum(((H_BST_z(z, H0, Omega_b_h2) - H_obs)/sig)**2
               for z, H_obs, sig in cc_data)

H0_cc_LCDM = minimize_scalar(chi2_cc, bounds=(40,90), method='bounded',
                              args=(0.0224,)).x
H0_cc_DH   = minimize_scalar(chi2_cc, bounds=(40,90), method='bounded',
                              args=(Omega_b_h2_DH,)).x

# ── Print the table ─────────────────────────────────────────────────────────
W = 100
print("=" * W)
print("BST HUBBLE CONSTANT: BACKFIT FROM MODEL-INDEPENDENT OBSERVATIONS")
print(f"Flat, no dark matter.  F_BST={F_BST}  Lambda_obs={Lambda_obs:.2e}  T_CMB={T_CMB} K")
print(f"Target d_0 = {d0_target:.4e} l_Pl")
print("=" * W)
print()

hdr = (f"  {'Source / Input':46s}  {'Ω_b h²':>7}  {'H₀':>6}  "
       f"{'Ω_Λ':>6}  {'Λ (Pl)':>10}  {'d_0 l_Pl':>10}  {'d_0 err':>7}")
print(hdr)
print("  " + "-"*(W-2))

def row(label, H0, Ob_h2, Onu_h2=0.0):
    L, OL = Lambda_Omega_from(H0, Ob_h2, Onu_h2)
    d0    = d0_from_Lambda(L)
    err   = (d0 - d0_target)/d0_target * 100
    flag  = " ◄" if abs(err) < 5 else (" ←" if abs(err) < 15 else "")
    print(f"  {label:46s}  {Ob_h2+Onu_h2:7.4f}  {H0:6.1f}  "
          f"{OL:6.4f}  {L:10.3e}  {d0:10.4e}  {err:+7.1f}%{flag}")

def divider(title=""):
    if title:
        pad = (W - len(title) - 4) // 2
        print(f"  {'─'*pad} {title} {'─'*pad}")
    else:
        print("  " + "─"*(W-2))

divider("REFERENCE: ΛCDM-DERIVED INPUTS  [biased — assume DM]")
row("ΛCDM Ω_b h²=0.0224, H₀=67.4 (Planck CMB)",     67.40, 0.0224)
row("ΛCDM Ω_b h²=0.0224, H₀=73.0 (local ladder)",   73.00, 0.0224)
row("ΛCDM Ω_b h²=0.0224, H₀=73.9 (megamaser)",      73.90, 0.0224)

divider("BST BACKFIT  [what H₀ does Lambda_obs require exactly?]")
row("BST backfit, Ω_b h²=0.0224 (ΛCDM)",
    H0_for_exact_Lambda(0.0224), 0.0224)
row("BST backfit, Ω_b h²=D/H BBN",
    H0_for_exact_Lambda(Omega_b_h2_DH), Omega_b_h2_DH)

divider("GEOMETRIC / MODEL-FREE H₀  [no DM assumption in measurement]")
row("Megamaser MCP (VLBI geometry), Ω_b=ΛCDM",       73.90, 0.0224)
row("Megamaser MCP (VLBI geometry), Ω_b=D/H BBN",    73.90, Omega_b_h2_DH)
row("SBF distances (Blakeslee 2021)",                 73.30, 0.0224)
row("Time-delay lensing H0LiCOW",                    73.30, 0.0224)

divider("BBN NUCLEAR PHYSICS  [D/H → Ω_b h², no DM needed]")
row(f"BBN D/H=2.527e-5 (Cooke 2018), H₀ backfit",
    H0_for_exact_Lambda(Omega_b_h2_DH), Omega_b_h2_DH)
row(f"BBN D/H, H₀=73.9 (megamaser anchor)",          73.90, Omega_b_h2_DH)
row(f"BBN D/H, H₀=67.4 (Planck CMB anchor)",         67.40, Omega_b_h2_DH)

divider("BBN + BST T_c ENTROPY CORRECTION  [T_c=0.487 MeV dilutes η]")
for delta, label in [(0.05,  "δ=5%  weak transition"),
                     (0.15,  "δ=15% moderate"),
                     (0.50,  "δ=50% strong"),
                     (2.00,  "δ=200% (Li-7 factor ~3)")]:
    Ob = Omega_b_BST(delta)
    row(f"BST T_c correction {label}",
        H0_for_exact_Lambda(Ob), Ob)

divider("COSMIC CHRONOMETERS  [H(z) from galaxy ages, model-free]")
row(f"Chronometers BST fit, Ω_b h²=0.0224",          H0_cc_LCDM, 0.0224)
row(f"Chronometers BST fit, Ω_b h²=D/H BBN",         H0_cc_DH,   Omega_b_h2_DH)

divider("NEUTRINO MASS  [BST predicts 3 flavors; lab: Σm_ν < 0.45 eV]")
for mnu in [0.06, 0.15, 0.30, 0.45]:
    Onu = mnu / 93.14
    # At late z, massive neutrinos are matter-like → add to matter budget
    H0_nu = H0_for_exact_Lambda(Omega_b_h2_DH, Onu)
    row(f"D/H BBN + Σm_ν={mnu:.2f} eV",
        H0_nu, Omega_b_h2_DH, Onu)

divider("COMBINED: MORE BARYONS + NEUTRINO MASS  [speculative BST]")
# If baryon asymmetry in BST gives Omega_b h² higher
for Ob_h2, Onu_h2, label in [
    (0.030, 0.003, "Ω_b h²=0.030 + Σm_ν=0.28 eV"),
    (0.040, 0.003, "Ω_b h²=0.040 + Σm_ν=0.28 eV"),
    (0.050, 0.005, "Ω_b h²=0.050 + Σm_ν=0.47 eV"),
    (0.060, 0.005, "Ω_b h²=0.060 + Σm_ν=0.47 eV"),
    (0.080, 0.008, "Ω_b h²=0.080 + Σm_ν=0.74 eV"),
    (0.100, 0.010, "Ω_b h²=0.100 + Σm_ν=0.93 eV"),
]:
    H0_combo = H0_for_exact_Lambda(Ob_h2, Onu_h2)
    row(label, H0_combo, Ob_h2, Onu_h2)

print()
print("=" * W)
print("SUMMARY: WHAT MOVES H₀ TOWARD THE OBSERVED RANGE [67–73 km/s/Mpc]")
print("=" * W)
print(f"""
  BST floor (ΛCDM Ω_b inputs):       {H0_for_exact_Lambda(0.0224):.1f} km/s/Mpc
  BST floor (BBN D/H Ω_b inputs):    {H0_for_exact_Lambda(Omega_b_h2_DH):.1f} km/s/Mpc
  Chronometer BST fit:                {H0_cc_LCDM:.1f} km/s/Mpc
  Observed CMB (Planck):              67.4 km/s/Mpc
  Observed local (Riess 2022):        73.0 km/s/Mpc
  Geometric (megamaser):              73.9 km/s/Mpc

  Drivers raising H₀:
    + Higher Ω_b h² (more baryons, no DM confusion)   → +1 km/s/Mpc per 0.01 in Ω_b h²
    + Neutrino mass (matter-like at low z)             → small effect
    + Both combined (Ω_b h²~0.1, Σm_ν~1 eV)          → reaches ~65 km/s/Mpc
    + Local overdensity on top of floor                → bridges to observed 67–73

  Drivers lowering H₀ (making gap worse):
    - BST T_c entropy injection (dilutes baryons)      → makes floor lower
    - BST-corrected Λ formula (Bergman off-center)     → TBD

  Gap to close: {67.4 - H0_for_exact_Lambda(0.0224):.1f} km/s/Mpc (CMB) or {73.0 - H0_for_exact_Lambda(0.0224):.1f} km/s/Mpc (local)
  Partition function needed to close it from first principles.
""")

print("=" * W)
print("CHRONOMETER DATA vs BST MODEL (best-fit H₀)")
print("=" * W)
print(f"  Best-fit H₀ = {H0_cc_LCDM:.1f} km/s/Mpc  (chi²/n = {chi2_cc(H0_cc_LCDM)/len(cc_data):.2f})")
print()
print(f"  {'z':>6}  {'H_obs':>8}  {'±σ':>6}  {'H_BST':>8}  {'resid':>8}  {'resid/σ':>8}")
for z, H_obs, sig in cc_data:
    Hp = H_BST_z(z, H0_cc_LCDM, 0.0224)
    print(f"  {z:6.2f}  {H_obs:8.1f}  {sig:6.1f}  {Hp:8.1f}  {H_obs-Hp:+8.1f}  {(H_obs-Hp)/sig:+8.2f}")
