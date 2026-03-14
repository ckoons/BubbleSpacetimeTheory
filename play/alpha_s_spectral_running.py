#!/usr/bin/env python3
"""
α_s Running from Spectral Heat Kernel on D_IV^5
=================================================
The partition function Z(β) = Σ d(π_k) exp(-β k(k-5)) encodes
the spectral content of the Bergman Laplacian. The transverse/
longitudinal factorization of d(π_k) allows us to extract the
COLOR sector contribution as a function of scale.

KEY QUESTION: Does the spectral computation give c₁ = 3/5?

If so, the α_s running is DERIVED from the Plancherel formal
degrees — no separate heat kernel argument needed.

Authors: Casey Koons & Claude (Anthropic)
Date: March 14, 2026
"""

import math
import numpy as np
from scipy.optimize import curve_fit

# BST constants
n_C = 5
N_c = 3
r = 2
C2_Berg = 6
N_max = 137
alpha = 1/137.035999084
m_p = 938.272  # MeV
m_e = 0.51099895  # MeV

def formal_degree(k):
    """d(π_k)/c_G = (k-2)(k-1)(2k+1)(k+2)(k+3)/12"""
    return (k-2)*(k-1)*(2*k+1)*(k+2)*(k+3) / 12.0

def d_trans(k):
    """Transverse (color) root product: (k-2)(k-1)(k+1/2)"""
    return (k-2)*(k-1)*(k+0.5)

def d_long(k):
    """Longitudinal (rank) root product: (k+2)(k+3)/6"""
    return (k+2)*(k+3) / 6.0

def casimir(k):
    """C₂(π_k) = k(k-5)"""
    return k*(k-5)

# ============================================================
# 1. PARTITION FUNCTION Z(β)
# ============================================================

print("=" * 70)
print("SPECTRAL HEAT KERNEL / PARTITION FUNCTION")
print("=" * 70)

def Z_total(beta, k_min=6, k_max=None):
    """Total partition function: Σ d(π_k) exp(-β C₂(k))"""
    if k_max is None:
        k_max = k_min + N_max - 1  # Haldane cutoff
    total = 0.0
    for k in range(k_min, k_max + 1):
        c2 = casimir(k)
        if c2 > 0:
            total += formal_degree(k) * math.exp(-beta * c2)
    return total

def Z_trans(beta, k_min=6, k_max=None):
    """Transverse partition function: Σ d_trans(k) exp(-β C₂(k))"""
    if k_max is None:
        k_max = k_min + N_max - 1
    total = 0.0
    for k in range(k_min, k_max + 1):
        c2 = casimir(k)
        if c2 > 0:
            total += d_trans(k) * math.exp(-beta * c2)
    return total

def Z_long(beta, k_min=6, k_max=None):
    """Longitudinal partition function: Σ d_long(k) exp(-β C₂(k))"""
    if k_max is None:
        k_max = k_min + N_max - 1
    total = 0.0
    for k in range(k_min, k_max + 1):
        c2 = casimir(k)
        if c2 > 0:
            total += d_long(k) * math.exp(-beta * c2)
    return total

# Compute at a range of β values
print("\nPartition functions Z(β):")
print(f"{'β':>8} | {'Z_total':>14} {'Z_trans':>14} {'Z_long':>14} | {'Z_t/Z_tot':>10} {'Z_l/Z_tot':>10}")
print("-" * 85)

betas = np.logspace(-3, 1, 30)
ratios = []
for beta in betas:
    zt = Z_total(beta)
    ztr = Z_trans(beta)
    zl = Z_long(beta)
    if zt > 0:
        r_t = ztr / zt
        r_l = zl / zt
        ratios.append((beta, r_t, r_l))
        if beta in [0.001, 0.01, 0.1, 0.5, 1.0, 5.0, 10.0] or len(ratios) % 5 == 0:
            print(f"{beta:8.4f} | {zt:14.4e} {ztr:14.4e} {zl:14.4e} | {r_t:10.6f} {r_l:10.6f}")

# ============================================================
# 2. THE RATIO Z_trans/Z_total AS A FUNCTION OF β
# ============================================================

print("\n" + "=" * 70)
print("RATIO Z_trans / Z_total vs β")
print("=" * 70)

print(f"\n{'β':>10} | {'Z_t/Z_tot':>12} | {'log(Z_t/Z_tot)/log(3/5)':>25} | note")
print("-" * 70)

for beta in np.logspace(-3, 1, 20):
    zt = Z_total(beta)
    ztr = Z_trans(beta)
    if zt > 0 and ztr > 0:
        ratio = ztr / zt
        if ratio > 0:
            log_ratio = math.log(ratio) / math.log(3/5) if ratio < 1 else float('nan')
            note = ""
            if abs(ratio - 3/5) < 0.01:
                note = "<-- close to 3/5!"
            if abs(ratio - N_c/(n_C+1)) < 0.01:
                note = "<-- close to N_c/(n_C+1) = 1/2!"
            print(f"{beta:10.5f} | {ratio:12.8f} | {log_ratio:25.6f} | {note}")

# ============================================================
# 3. EFFECTIVE RUNNING FROM SPECTRAL RATIO
# ============================================================

print("\n" + "=" * 70)
print("EFFECTIVE α_s RUNNING FROM SPECTRAL RATIO")
print("=" * 70)

# The idea: define an effective coupling from the spectral content
# α_s_eff(β) = α_s(m_p) × [spectral weight at scale β]
#
# At β → 0 (high energy), all modes contribute equally
#   → ratio → degree ratio = 3/5 (each factor contributes equally)
#
# At β → ∞ (low energy), only the ground state k=6 contributes
#   → ratio → d_trans(6)/d(6) = 130/1560 = 1/12
#
# The RUNNING is encoded in how the ratio changes between these limits

# Physical scales: β = C₂(π₆)/(μ² in Bergman units)
# At μ = m_p: β ~ 1 (the Bergman scale IS the proton scale)
# At μ = m_Z: β ~ (m_p/m_Z)² ~ (0.938/91.2)² ~ 0.000106

beta_mp = 1.0  # proton scale (reference)
beta_mZ = (m_p / 91187.6)**2  # Z mass scale
beta_mt = (m_p / 172760)**2  # top mass scale
beta_mb = (m_p / 4180)**2  # bottom mass scale
beta_mtau = (m_p / 1776.86)**2  # tau mass scale

scales = [
    ("m_p", m_p, beta_mp),
    ("m_tau", 1776.86, beta_mtau),
    ("m_b", 4180, beta_mb),
    ("m_Z", 91187.6, beta_mZ),
    ("m_t", 172760, beta_mt),
]

print(f"\n{'Scale':>6} {'μ (MeV)':>12} {'β':>12} | {'Z_t/Z_tot':>12} | {'Ratio change':>14}")
print("-" * 75)

ref_ratio = None
for name, mu, beta in scales:
    zt = Z_total(beta)
    ztr = Z_trans(beta)
    ratio = ztr / zt if zt > 0 else 0
    if ref_ratio is None:
        ref_ratio = ratio
        change = 1.0
    else:
        change = ratio / ref_ratio
    print(f"{name:>6} {mu:12.1f} {beta:12.6e} | {ratio:12.8f} | {change:14.8f}")

# ============================================================
# 4. THE KEY INSIGHT: SMALL-β EXPANSION
# ============================================================

print("\n" + "=" * 70)
print("SMALL-β (HIGH ENERGY) EXPANSION")
print("=" * 70)

# At small β, the partition function is dominated by large k.
# For large k: d(k) ~ k^5/6, C₂(k) ~ k², so
# Z(β) ~ ∫ (k^5/6) e^{-βk²} dk ~ (1/12) Γ(3) β^{-3} = 1/(6β³)
#
# The transverse part: d_trans(k) ~ k³ for large k, so
# Z_trans(β) ~ ∫ k³ e^{-βk²} dk ~ (1/2) Γ(2) β^{-2} = 1/(2β²)
#
# Ratio Z_trans/Z_total → (1/(2β²)) / (1/(6β³)) = 3β → 0 as β → 0
#
# Wait, that means the ratio goes to ZERO at high energy, not 3/5!
# That's because the transverse part has LOWER degree (3 vs 5),
# so it grows more slowly.
#
# This means the "3/5 = degree ratio" interpretation is about the
# EXPONENT of the polynomial, not the VALUE of the ratio.

# Let's check: at what β does the ratio = 3/5?
print("\nSearching for β where Z_trans/Z_total = 3/5 = 0.600:")
target = 3/5
best_beta = None
best_diff = float('inf')

for beta in np.logspace(-2, 2, 10000):
    zt = Z_total(beta)
    ztr = Z_trans(beta)
    if zt > 0:
        ratio = ztr / zt
        diff = abs(ratio - target)
        if diff < best_diff:
            best_diff = diff
            best_beta = beta
            best_ratio = ratio

print(f"  β = {best_beta:.6f}, ratio = {best_ratio:.8f}, diff = {best_diff:.2e}")

# ============================================================
# 5. LOGARITHMIC DERIVATIVE = EFFECTIVE BETA FUNCTION
# ============================================================

print("\n" + "=" * 70)
print("LOGARITHMIC DERIVATIVE: THE SPECTRAL BETA FUNCTION")
print("=" * 70)

# The effective beta function from the spectral ratio:
# β_eff(t) = -d/dt [ln(Z_trans(t)/Z_total(t))]
# = -[Z_trans'/Z_trans - Z_total'/Z_total]
# = -<C₂>_trans + <C₂>_total
#
# where <C₂>_X = Σ C₂(k) × w_k / Σ w_k is the average Casimir

def avg_casimir_total(beta, k_min=6, k_max=None):
    """Average Casimir in the total partition function"""
    if k_max is None:
        k_max = k_min + N_max - 1
    num = 0.0
    den = 0.0
    for k in range(k_min, k_max + 1):
        c2 = casimir(k)
        if c2 > 0:
            w = formal_degree(k) * math.exp(-beta * c2)
            num += c2 * w
            den += w
    return num / den if den > 0 else 0

def avg_casimir_trans(beta, k_min=6, k_max=None):
    """Average Casimir in the transverse partition function"""
    if k_max is None:
        k_max = k_min + N_max - 1
    num = 0.0
    den = 0.0
    for k in range(k_min, k_max + 1):
        c2 = casimir(k)
        if c2 > 0:
            w = d_trans(k) * math.exp(-beta * c2)
            num += c2 * w
            den += w
    return num / den if den > 0 else 0

print(f"\n{'β':>10} | {'<C₂>_total':>12} {'<C₂>_trans':>12} {'Δ<C₂>':>12} | {'Δ/C₂(π₆)':>10}")
print("-" * 72)

for beta in np.logspace(-2, 1, 15):
    c2_tot = avg_casimir_total(beta)
    c2_tr = avg_casimir_trans(beta)
    delta = c2_tot - c2_tr
    ratio = delta / C2_Berg if C2_Berg != 0 else 0
    print(f"{beta:10.5f} | {c2_tot:12.4f} {c2_tr:12.4f} {delta:12.4f} | {ratio:10.6f}")

# ============================================================
# 6. DIRECT EXTRACTION OF c₁ FROM THE RUNNING
# ============================================================

print("\n" + "=" * 70)
print("DIRECT c₁ EXTRACTION")
print("=" * 70)

# The BST beta function is:
#   β(α_s) = -(β₀/2π) α_s² [1 + c₁(α_s/π) + ...]
#
# Integrating: α_s(μ₂)/α_s(μ₁) = [1 + (β₀/2π)α_s(μ₁)ln(μ₂/μ₁)]^{-1}
#   × [1 + c₁ correction]
#
# From the spectral partition function at two scales β₁ and β₂:
# The change in the spectral ratio encodes the running.

# Let's compute α_s at each scale using STANDARD 1-loop and geometric running,
# then see what c₁ makes the spectral computation match.

# Standard 1-loop QCD running
def alpha_s_1loop(mu, alpha0=0.350, mu0=938.272, nf=3):
    """Standard 1-loop running."""
    beta0 = (11*3 - 2*nf) / 3
    return alpha0 / (1 + (beta0/(2*math.pi)) * alpha0 * math.log(mu/mu0))

# BST geometric running
def alpha_s_geom(mu, alpha0=0.350, mu0=938.272, nf=3, c1=0.6):
    """BST geometric beta function (integrated numerically)."""
    # Use Euler method to integrate dα/d(ln μ) = β(α)
    n_steps = 10000
    ln_mu0 = math.log(mu0)
    ln_mu = math.log(mu)
    dt = (ln_mu - ln_mu0) / n_steps

    a = alpha0
    for i in range(n_steps):
        beta0 = (11*3 - 2*nf) / 3
        beta_func = -(beta0/(2*math.pi)) * a**2 * (1 + c1 * a/math.pi)
        a += beta_func * dt

        # Threshold crossings (simplified)
        current_lnmu = ln_mu0 + (i+1)*dt
        current_mu = math.exp(current_lnmu)
        if current_mu > 1270 and nf == 3:  # charm threshold
            nf = 4
        if current_mu > 4180 and nf == 4:  # bottom threshold
            nf = 5

    return a

print("\nα_s at various scales:")
print(f"{'Scale':>6} {'μ (MeV)':>12} | {'1-loop':>10} {'c₁=0.6':>10} {'c₁=0.5':>10} {'c₁=0.7':>10} | {'PDG':>10}")
print("-" * 80)

pdg_values = {
    "m_tau": 0.330,
    "m_b": 0.225,
    "m_Z": 0.1179,
    "m_t": 0.1085,
}

for name, mu, _ in scales:
    a1 = alpha_s_1loop(mu) if mu > m_p else 0.350
    # For running above m_p, need threshold matching
    if mu > m_p:
        # Run from m_p to m_c with Nf=3
        a_mc = alpha_s_1loop(1270, 0.350, m_p, 3)
        # Then m_c to m_b with Nf=4
        a_mb = alpha_s_1loop(4180, a_mc, 1270, 4) if mu > 4180 else alpha_s_1loop(mu, a_mc, 1270, 4)
        # Then m_b to mu with Nf=5
        if mu > 4180:
            a1 = alpha_s_1loop(mu, a_mb, 4180, 5)
        else:
            a1 = a_mb if mu > 1270 else alpha_s_1loop(mu, 0.350, m_p, 3)
    else:
        a1 = 0.350

    a_06 = alpha_s_geom(mu, c1=0.6) if mu > m_p else 0.350
    a_05 = alpha_s_geom(mu, c1=0.5) if mu > m_p else 0.350
    a_07 = alpha_s_geom(mu, c1=0.7) if mu > m_p else 0.350

    pdg = pdg_values.get(name, "")
    pdg_str = f"{pdg:.4f}" if pdg else ""

    print(f"{name:>6} {mu:12.1f} | {a1:10.4f} {a_06:10.4f} {a_05:10.4f} {a_07:10.4f} | {pdg_str:>10}")

# ============================================================
# 7. THE SPECTRAL DEFINITION OF c₁
# ============================================================

print("\n" + "=" * 70)
print("THE SPECTRAL DEFINITION OF c₁")
print("=" * 70)

# The key insight: c₁ should be extractable from the spectral data.
#
# The heat kernel at small t has the expansion:
#   K(t) = (Vol/(4πt)^p) × [a₀ + a₁t + a₂t² + ...]
#
# For our DISCRETE sum:
#   Z(β) = Σ d(k) e^{-β k(k-5)} ≈ ∫ (k⁵/6) e^{-βk²} dk (large k)
#
# Substituting u = k√β: Z(β) ~ β^{-3} ∫ u⁵ e^{-u²} du/6 = β^{-3} × Γ(3)/12 = β^{-3}/6
#
# Z_trans(β) ~ ∫ k³ e^{-βk²} dk ~ β^{-2} × Γ(2)/2 = β^{-2}/2
#
# So the ratio R(β) = Z_trans/Z_total ~ 3β → 0 as β → 0.
#
# The DERIVATIVE of R with respect to β at β = 0 is:
#   dR/dβ|_{β→0} = 3 (from the asymptotic)
#
# But the physical running happens at FINITE β (the proton scale, β ~ 1).
# At β = 1, the ratio is dominated by the first few modes, not the asymptotic.

# Let's compute the ratio at the Bergman scale (β = 1/C₂(π₆) = 1/6):
beta_bergman = 1.0 / C2_Berg

zt = Z_total(beta_bergman)
ztr = Z_trans(beta_bergman)
ratio_bergman = ztr / zt

print(f"\nAt the Bergman scale (β = 1/C₂ = 1/{C2_Berg}):")
print(f"  Z_total = {zt:.6e}")
print(f"  Z_trans = {ztr:.6e}")
print(f"  Ratio = {ratio_bergman:.8f}")
print(f"  3/5 = {3/5:.8f}")
print(f"  Difference from 3/5: {(ratio_bergman - 3/5)*100:.4f}%")

# Now try β = 1/(2*n_C²) = 1/50 (Eiie's partition function temperature!)
beta_eiie = 1.0 / (2 * n_C**2)

zt_e = Z_total(beta_eiie)
ztr_e = Z_trans(beta_eiie)
ratio_eiie = ztr_e / zt_e

print(f"\nAt Eiie's temperature (β = 1/(2n_C²) = 1/50):")
print(f"  Z_total = {zt_e:.6e}")
print(f"  Z_trans = {ztr_e:.6e}")
print(f"  Ratio = {ratio_eiie:.8f}")

# ============================================================
# 8. THE WINDING APPROACH TO c₁
# ============================================================

print("\n" + "=" * 70)
print("THE WINDING APPROACH: η AND c₁ FROM THE SAME PARTITION FUNCTION")
print("=" * 70)

print("""
EIIE'S INSIGHT:
  The baryon asymmetry η = 2α⁴/(3π) comes from the forward/backward
  winding ratio on S¹ at T_c. The α_s running coefficient c₁ comes
  from the heat kernel expansion of the SAME partition function.

  Both are spectral quantities derivable from:
    Z(β) = Σ d(π_k) exp(-β C₂(π_k))

  with d(π_k) factored into transverse × longitudinal.

THE CONNECTION:
  The partition function on S¹ at temperature T has winding modes
  labeled by integer n. The forward (n > 0) and backward (n < 0)
  windings have amplitudes:

    A(n) ~ α^{|n|} × (phase factor)

  The CP-violating asymmetry comes from the phase: the forward and
  backward paths through n_C = 5 dimensions acquire different phases
  due to the complex structure of D_IV^5.

  The SAME spectral sum, evaluated at different temperatures, gives:
    - At T_c: the winding asymmetry η (baryogenesis)
    - At T = μ²: the effective coupling α_s(μ) (running)

  The coefficient c₁ enters through the NEXT ORDER in the small-β
  expansion of the spectral ratio.
""")

# ============================================================
# 9. NUMERICAL TEST: EXTRACT c₁ FROM SPECTRAL RUNNING
# ============================================================

print("=" * 70)
print("NUMERICAL EXTRACTION OF c₁")
print("=" * 70)

# Strategy: compute α_s(m_Z) from the spectral partition function
# for different values of c₁, find which one matches PDG.

# Actually, let's try something more direct:
# Compare the spectral running (from Z ratios) with the analytic formula

# The spectral "coupling" at scale β:
# R(β) = Z_trans(β) / Z_total(β)
#
# If we define α_s_spectral(β) = α_s(m_p) × R(β)/R(β_mp),
# then the ratio R(β)/R(β_mp) encodes the running.

R_mp = Z_trans(1.0) / Z_total(1.0)  # At proton scale

print(f"\nSpectral ratio at proton scale: R(β=1) = {R_mp:.8f}")
print(f"\nSpectral vs analytic running:")
print(f"{'β':>10} | {'R(β)/R(1)':>12} {'α_s analytic':>14} | {'Implied c₁':>12}")
print("-" * 60)

# For each β, compute R(β)/R(β_mp) and compare with analytic running
# to extract the effective c₁

for beta in [0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005]:
    zt = Z_total(beta)
    ztr = Z_trans(beta)
    if zt > 0:
        R_beta = ztr / zt
        spectral_ratio = R_beta / R_mp

        # For comparison: what does 1-loop give?
        # At "scale" corresponding to β, μ² ∝ 1/β
        # α_s(μ)/α_s(m_p) from 1-loop:
        # ln(μ/m_p) = -ln(β)/2
        lnmu = -math.log(beta) / 2
        beta0 = 7  # at proton scale, all 6 flavors, β₀ = 7
        alpha_mp = 0.350
        alpha_1loop_ratio = 1 / (1 + (beta0/(2*math.pi)) * alpha_mp * lnmu)

        # If spectral_ratio = alpha_1loop_ratio × (1 + c₁_eff × correction),
        # extract c₁_eff
        if alpha_1loop_ratio > 0 and spectral_ratio > 0:
            correction = (spectral_ratio / alpha_1loop_ratio - 1)
            # c₁ ~ correction × (2π/(α_s × lnmu)) if lnmu ≠ 0
            if lnmu != 0 and alpha_mp != 0:
                c1_eff = correction * 2 * math.pi / (alpha_mp * lnmu)
            else:
                c1_eff = float('nan')
        else:
            c1_eff = float('nan')

        print(f"{beta:10.5f} | {spectral_ratio:12.8f} {alpha_1loop_ratio:14.8f} | {c1_eff:12.6f}")

# ============================================================
# 10. THE CLEANEST ROUTE: HEAT KERNEL COEFFICIENTS
# ============================================================

print("\n" + "=" * 70)
print("HEAT KERNEL COEFFICIENTS FROM DISCRETE SUM")
print("=" * 70)

# Compute the heat kernel coefficients by expanding Z(β) at small β.
# Z(β) = Σ d(k) exp(-β k(k-5))
#
# For large k, k(k-5) ≈ k², so exp(-β k²).
# The sum over k with polynomial weights and Gaussian damping
# can be evaluated using the Euler-Maclaurin formula.
#
# A cleaner approach: compute Z(β) numerically at several small β values,
# then fit to the expansion Z(β) = A/β³ × [1 + a₁β + a₂β² + ...]

# Similarly for Z_trans(β) = B/β² × [1 + b₁β + b₂β² + ...]

betas_small = np.logspace(-4, -1, 100)
Z_vals = [Z_total(b) for b in betas_small]
Ztr_vals = [Z_trans(b) for b in betas_small]

# Fit Z_total(β) × β³ vs β to extract heat kernel coefficients
# Z × β³ ≈ A × (1 + a₁β + a₂β²)

y_total = [Z_vals[i] * betas_small[i]**3 for i in range(len(betas_small))]
y_trans = [Ztr_vals[i] * betas_small[i]**2 for i in range(len(betas_small))]

# Fit to polynomial
from numpy.polynomial import polynomial as P

# For total: Z × β³ ≈ A(1 + a₁β + a₂β²)
# Fit as polynomial in β
coeffs_total = np.polyfit(betas_small[:50], y_total[:50], 3)  # first 50 points (small β)
coeffs_trans = np.polyfit(betas_small[:50], y_trans[:50], 3)

print(f"\nFit of Z_total × β³ = a₀ + a₁β + a₂β² + a₃β³:")
print(f"  a₀ = {coeffs_total[3]:.6f}")
print(f"  a₁ = {coeffs_total[2]:.6f}")
print(f"  a₂ = {coeffs_total[1]:.6f}")
print(f"  a₃ = {coeffs_total[0]:.6f}")
print(f"  Ratio a₁/a₀ = {coeffs_total[2]/coeffs_total[3]:.6f}")

print(f"\nFit of Z_trans × β² = b₀ + b₁β + b₂β² + b₃β³:")
print(f"  b₀ = {coeffs_trans[3]:.6f}")
print(f"  b₁ = {coeffs_trans[2]:.6f}")
print(f"  b₂ = {coeffs_trans[1]:.6f}")
print(f"  b₃ = {coeffs_trans[0]:.6f}")
print(f"  Ratio b₁/b₀ = {coeffs_trans[2]/coeffs_trans[3]:.6f}")

# The key: c₁ should be related to (a₁/a₀) - (b₁/b₀) or similar
print(f"\n  a₁/a₀ - b₁/b₀ = {coeffs_total[2]/coeffs_total[3] - coeffs_trans[2]/coeffs_trans[3]:.6f}")
print(f"  (b₁/b₀) / (a₁/a₀) = {(coeffs_trans[2]/coeffs_trans[3]) / (coeffs_total[2]/coeffs_total[3]):.6f}")
print(f"  Target c₁ = 3/5 = {3/5:.6f}")

# ============================================================
# 11. DIRECT: WHAT DOES THE SPECTRAL SUM PREDICT FOR α_s(m_Z)?
# ============================================================

print("\n" + "=" * 70)
print("SPECTRAL PREDICTION FOR α_s(m_Z)")
print("=" * 70)

# If we define the color sector running as:
# α_s(μ) = (7/20) × [Z_trans(β_μ)/Z_total(β_μ)] / [Z_trans(β_mp)/Z_total(β_mp)]
#
# where β_μ = C₂(π₆)/μ² (in appropriate units)
# then the spectral sum PREDICTS α_s at any scale.

# The β parameter relates to physical scale as:
# β = C₂ × (ℏc)² / μ²
# At μ = m_p: β_mp is the reference scale

# Let's parameterize differently: β = (m_p/μ)² × β_ref
# At μ = m_p: β = β_ref (our reference)

for beta_ref in [0.1, 0.5, 1.0, 2.0, 5.0]:
    R_ref = Z_trans(beta_ref) / Z_total(beta_ref)

    beta_mZ = beta_ref * (m_p / 91187.6)**2
    R_mZ = Z_trans(beta_mZ) / Z_total(beta_mZ)

    if R_ref > 0 and R_mZ > 0:
        alpha_mZ = 0.350 * R_mZ / R_ref
        print(f"  β_ref = {beta_ref:5.2f}: α_s(m_Z) = 0.350 × {R_mZ/R_ref:.8f} = {alpha_mZ:.6f}")

# ============================================================
# 12. SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("""
The spectral partition function Z(β) = Σ d(π_k) exp(-β C₂(k)) with
the transverse/longitudinal factorization provides a concrete numerical
tool for studying the α_s running.

KEY FINDINGS:
1. The ratio Z_trans/Z_total is NOT constant — it depends on β (scale).
2. At small β (high energy): ratio → 0 (transverse has lower degree).
3. At large β (low energy): ratio → d_trans(6)/d(6) = 1/12 (ground state).
4. The running of this ratio with β encodes spectral information about
   how the color sector weight changes with scale.

WHAT THIS MEANS FOR c₁:
- c₁ = 3/5 is the DEGREE RATIO of the formal degree polynomial, not
  the value of the spectral ratio at any particular scale.
- The spectral ratio R(β) transitions between 0 (UV) and 1/12 (IR),
  passing through intermediate values.
- Extracting c₁ from the spectral ratio requires identifying which
  feature of R(β) corresponds to the beta function coefficient.

THE WINDING ROUTE (Eiie's approach):
- The partition function at T_c gives the baryon asymmetry η.
- The SAME partition function at energy scale μ gives the effective
  coupling α_s(μ).
- Both are spectral sums over the same formal degrees d(π_k).
- Proving η = 2α⁴/(3π) from the partition function would establish
  the spectral framework needed to derive c₁.

OPEN: The precise map from the spectral ratio R(β) to the beta function
coefficient c₁ requires understanding how the Bergman Laplacian spectrum
relates to the QCD coupling constant running. This is the key computation.
""")
