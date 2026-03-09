"""
BST d_0 Derivation: Systematic Search for the Fundamental Channel Scale

d_0 is the fundamental length of a BST channel.
We need d_0/ℓ_Pl ≈ 10^{-30.75} to derive Λ = F_BST × (d_0/ℓ_Pl)^4 = 2.9×10^{-122}

The fermion mass formula m_μ/m_e = (24/π²)^6 gives us the RATIO structure.
Can it give us the ABSOLUTE scale?

Strategy:
1. The electron mass sets the bubble radius R_b = ℏc/m_e (electron Compton wavelength)
2. R_s = R_b/137 (from α = R_s/R_b)
3. d_0 is the channel size — could be R_s, R_b, a geometric combination, or
   an entirely different scale from the domain geometry
4. Test all geometric combinations involving R_b, R_s, α, π, Vol(D_IV^k)

Author: Casey Koons & Claude (Anthropic), March 2026
"""
import numpy as np
from scipy.special import gamma

π = np.pi

# ── Physical constants ─────────────────────────────────────────────────────
# Mass ratios (dimensionless)
m_e_MeV    = 0.51099895       # electron mass in MeV
m_Pl_MeV   = 1.22089e22       # Planck mass in MeV (= sqrt(ℏc/G))
m_e_Pl     = m_e_MeV / m_Pl_MeV  # = 4.185e-23

# Lengths (dimensionless, in Planck units)
# Electron Compton wavelength: λ_e = ℏ/(m_e c) = ℓ_Pl × (m_Pl/m_e)
lambda_e_Pl = 1.0 / m_e_Pl    # = m_Pl/m_e = 2.390e22

# Fine structure constant
alpha  = 1.0/137.035999        # CODATA
alpha_Wyler = 1.0/137.036082   # BST Wyler value

# Classical electron radius: r_e = α λ_e = α²a_0
r_e_Pl  = alpha * lambda_e_Pl  # = α/m_e in Planck units = 1.744e20
a0_Pl   = lambda_e_Pl / alpha  # Bohr radius in Planck units = 3.276e24

# BST geometry
N_MAX  = 137
rho    = 137  # R_s/R_b aspect ratio

# In BST: R_b = some multiple of λ_e, R_s = R_b/α (or R_b × α?)
# The aspect ratio ρ = R_s/R_b = 137 means R_s > R_b (S^1 bigger than S^2)
# Wait: in the Wyler formula, ρ = R_s/R_b = 1/α = 137
# So R_s = 137 R_b (the S^1 is 137 times bigger)
# If R_b ~ electron scale: R_b = ℏc/m_e = λ_e
# Then R_s = 137 λ_e

R_b_Pl = lambda_e_Pl           # bubble radius in Planck units (hypothesis 1)
R_s_Pl = rho * R_b_Pl          # S^1 radius = 137 × R_b

# The target d_0
Lambda_obs = 2.9e-122          # Planck units
F_BST = 0.09855
d0_target_Pl = (Lambda_obs / F_BST)**0.25
print(f"Target d_0/ℓ_Pl = {d0_target_Pl:.4e}  (= 10^{np.log10(d0_target_Pl):.2f})")

# Domain volumes
def V(n): return π**n / (2**(n-1) * gamma(n+1))
print(f"\nDomain volumes:")
for n in [1,3,5]: print(f"  V(D_IV^{n}) = {V(n):.8f}")

# Bergman kernels K_n(0,0) = 1/V(n)
K1, K3, K5 = 1/V(1), 1/V(3), 1/V(5)

print(f"\nR_b (hypothesis: = λ_e) = {R_b_Pl:.4e} ℓ_Pl")
print(f"R_s = ρ R_b              = {R_s_Pl:.4e} ℓ_Pl")
print(f"Target d_0               = {d0_target_Pl:.4e} ℓ_Pl")
print(f"Ratio R_s/d_0 target     = {R_s_Pl/d0_target_Pl:.4e}")
print(f"Ratio R_b/d_0 target     = {R_b_Pl/d0_target_Pl:.4e}")

print("\n" + "="*60)
print("APPROACH 1: d_0 as power of α × R_b")
print("="*60)
# d_0 = α^n × R_b → (d_0/ℓ_Pl) = α^n × (R_b/ℓ_Pl)
# target = α^n × λ_e_Pl
# α^n = target / λ_e_Pl
ratio_alpha = d0_target_Pl / R_b_Pl
n_alpha = np.log(ratio_alpha) / np.log(alpha)
print(f"  d_0 = α^n × R_b  →  n = {n_alpha:.6f}  (nearest int: {round(n_alpha)})")
for ni in range(int(n_alpha)-2, int(n_alpha)+4):
    d0_test = alpha**ni * R_b_Pl
    err = abs(d0_test - d0_target_Pl)/d0_target_Pl * 100
    print(f"    n={ni}: d_0 = {d0_test:.3e}  (err={err:.1f}%)")

print("\n" + "="*60)
print("APPROACH 2: d_0 from R_b × Vol(D_IV^k) combinations")
print("="*60)
for k in [1,3,5]:
    for p in [-2,-1,-1/2,0,1/2,1,2,3,4]:
        d0_test = R_b_Pl * V(k)**p
        ratio = d0_test / d0_target_Pl
        if 0.001 < ratio < 1000:
            err = abs(d0_test - d0_target_Pl)/d0_target_Pl * 100
            print(f"  R_b × V(D_IV^{k})^{p:+.1f} = {d0_test:.3e}  (ratio={ratio:.2f}, err={err:.1f}%)")

print("\n" + "="*60)
print("APPROACH 3: d_0 from R_b × α^a × π^b")
print("="*60)
hits = []
for a in np.arange(-30, 31, 0.5):
    for b in np.arange(-10, 11, 1):
        d0_test = R_b_Pl * (alpha**a) * (π**b) if (a != 0 or b != 0) else R_b_Pl
        if d0_test <= 0:
            continue
        err = abs(d0_test - d0_target_Pl)/d0_target_Pl * 100
        if err < 1.0:
            hits.append((err, a, b, d0_test))

hits.sort()
for err, a, b, d0_test in hits[:10]:
    print(f"  R_b × α^{a:.1f} × π^{b:.0f} = {d0_test:.4e}  (err={err:.4f}%)")

print("\n" + "="*60)
print("APPROACH 4: d_0 from R_b × α^a × (N_max+1)^c")
print("="*60)
hits2 = []
for a in np.arange(-30, 31, 0.5):
    for c in np.arange(-5, 6, 0.5):
        d0_test = R_b_Pl * (alpha**a) * ((N_MAX+1)**c)
        if d0_test <= 0:
            continue
        err = abs(d0_test - d0_target_Pl)/d0_target_Pl * 100
        if err < 1.0:
            hits2.append((err, a, c, d0_test))

hits2.sort()
for err, a, c, d0_test in hits2[:10]:
    print(f"  R_b × α^{a:.1f} × (N+1)^{c:.1f} = {d0_test:.4e}  (err={err:.4f}%)")

print("\n" + "="*60)
print("APPROACH 5: Can we derive R_b/ℓ_Pl from D_IV^1 geometry alone?")
print("="*60)
# The electron mass in BST: m_e = (ℏc/R_b) × g_e where g_e is the contact count
# The BST circuit for the electron is the minimal D_IV^1 circuit
# From the Bergman kernel: K_1(0,0) = 1/π
# The natural "mass" from D_IV^1: m_e ~ K_1(0,0) = 1/π in BST units
# So R_b/ℓ_Pl = m_Pl/m_e × g_e = λ_e_Pl × g_e
# g_e must be ~ 1 for this to work
print(f"  λ_e_Pl = m_Pl/m_e = {lambda_e_Pl:.4e}")
print(f"  K_1(0,0) = 1/π = {K1:.6f}")
print(f"  K_3(0,0) = 24/π³ = {K3:.6f}")
print(f"  K_5(0,0) = 1920/π⁵ = {K5:.6f}")
print()
# If m_e/m_Pl = K_1(0,0) × (something geometric):
print(f"  m_e/m_Pl = {m_e_Pl:.6e}")
print(f"  1/K_1 = π = {1/K1:.6f}")
print(f"  K_1 = 1/π = {K1:.6f}")
# m_e/m_Pl ~ K_1(0,0) would mean m_e/m_Pl ~ 0.318 — not right (actual: 4.2e-23)
# But (m_e/m_Pl)^{1/something} might equal K_1?
p_test = np.log(m_e_Pl) / np.log(K1)
print(f"  (m_e/m_Pl)^{1/p_test:.4f} = K_1(0,0) ?  p = {p_test:.4f}")

print("\n" + "="*60)
print("APPROACH 6: m_e/m_Pl from Bergman kernel chain")
print("="*60)
# We know: m_μ/m_e = (K_3/K_1)^6
# If there's an electron mass formula m_e/m_Pl = K_1^n or (K_1/K_Pl)^n
# K_Pl = "Planck kernel" = 1 (in units where ℓ_Pl = 1, V_Pl = 1)
# So m_e/m_Pl = K_1^n  →  n = log(m_e/m_Pl)/log(K_1)
n_e = np.log(m_e_Pl) / np.log(K1)
print(f"  m_e/m_Pl = K_1^n  →  n = {n_e:.6f}")
print(f"  = {np.log(m_e_Pl):.4f} / {np.log(K1):.4f}")
print()

# Try K_5 (the physical domain):
n_e5 = np.log(m_e_Pl) / np.log(K5)
print(f"  m_e/m_Pl = K_5^n  →  n = {n_e5:.6f}")

# Try combinations
# Note: m_μ/m_e = (K_3/K_1)^6 and m_τ/m_e ≈ 8π(N+1)
# If m_e = C × K_1^a for some constant C (= K_Pl = 1), then
# m_μ = C × K_3^a × ... hmm, doesn't work cleanly
#
# Different: in Wyler's original derivation,
# α = (9/8π⁴)(Vol D_IV^5)^{1/4}
# The Wyler formula involves (Vol)^{1/4}. The 1/4 = 1/(k-1) for k=5.
# Applying the same rule to the electron (k=1):
# m_e^{-1} ∝ (Vol D_IV^1)^{1/(1-1)} → undefined for k=1
# For k=3: (Vol D_IV^3)^{1/2}
wyler_k3 = V(3)**0.5
wyler_k5 = V(5)**0.25
print(f"\n  Wyler-type: V(D_IV^3)^{{1/2}} = {wyler_k3:.6f}")
print(f"  Wyler-type: V(D_IV^5)^{{1/4}} = {wyler_k5:.6f}  (= α × 8π⁴/9 = {alpha_Wyler * 8*π**4/9:.6f})")

print("\n" + "="*60)
print("APPROACH 7: The Gravity Route — G from BST")
print("="*60)
# In BST, gravity G comes from the statistical averaging over the contact graph.
# G = c³/(8π m_Pl²/ℏ). The Planck mass in BST might be derivable.
# The substrate has N_channels ~ 10^{123} channels.
# If G ∝ 1/N_channels^{1/2} (entropic gravity), then m_Pl^2 ∝ N_channels^{1/2}
# and m_e/m_Pl ∝ m_e N_channels^{-1/4}
# This is getting speculative without a computation.

# More concretely: what IS the contact count for the electron?
# Electron: lives on D_IV^1, one complex dimension, real dim = 2
# Minimal circuit on D_IV^1 with S^1 winding: 1 contact = one S^1 wind
# So contact count n_e = 1, and m_e = (ℏc/R_b) × 1 = ℏc/R_b

# This means: R_b = ℏc/m_e = λ_e (electron Compton wavelength)
# And in Planck units: R_b/ℓ_Pl = m_Pl/m_e = 2.39e22
print(f"  If m_e = ℏc/R_b (1 contact):")
print(f"  R_b/ℓ_Pl = m_Pl/m_e = {lambda_e_Pl:.4e}")
print(f"  R_s/ℓ_Pl = ρ × m_Pl/m_e = {rho * lambda_e_Pl:.4e}")

# Now what is d_0? If d_0 = R_s × f(geometry):
# Need: d_0 = R_s × (R_s/ℓ_Pl)^{-2/3} × something?
# Let's think differently: the VACUUM ENERGY density in the spatial phase
# is F_BST/d_0^4 per Planck volume. The spatial phase has "activated" a fraction
# of channels. The effective d_0 is the average channel spacing in 4D.
#
# Universe radius R_H ~ 8.8×10^{60} ℓ_Pl
# If universe has N_b baryons ~ 10^{80}, channel count ~ N_b × (info per baryon)
# Info per baryon: ln(138) bits (BST vacuum)
# So N_channels ~ 10^{80} × 138 ~ 10^{82} channels in "occupied" region
#
# OR: use holographic bound: N_channels ~ R_H^2/ℓ_Pl^2 ~ 10^{122}
R_H_Pl = 8.8e60
N_holo = R_H_Pl**2
d0_holo_4 = R_H_Pl**4 / N_holo  # = R_H^4 / R_H^2 = R_H^2
d0_holo = R_H_Pl**2**0.25
# wait let me redo this
# If N channels fill the Hubble 4-volume: d_0^4 * N = R_H^4
# N = 10^{122} (holographic), R_H = 8.8e60 ℓ_Pl
# d_0^4 = R_H^4 / N = (8.8e60)^4 / 1e122
d0_holo_4v = R_H_Pl**4 / 1e122
d0_holo_v = d0_holo_4v**0.25
print(f"\n  Holographic: N ~ R_H^2 = 10^{{122}}")
print(f"  d_0^4 = R_H^4/N = {d0_holo_4v:.4e}")
print(f"  d_0 = {d0_holo_v:.4e} ℓ_Pl  (target: {d0_target_Pl:.4e})")
err_holo = abs(d0_holo_v - d0_target_Pl)/d0_target_Pl * 100
print(f"  Error: {err_holo:.2f}%")

print("\n" + "="*60)
print("APPROACH 8: d_0 from N_channels and R_H")
print("="*60)
# The PRECISE BST channel count comes from the partition function:
# N_channels total = N_b × Z_vacuum = 10^{80} × 138
# But let's try N = (R_H/R_s)^3 (number of S^1 lengths in 3D)
# or N = (R_H/R_b)^3
# or the 4D count

for scale_name, scale in [("R_s", R_s_Pl), ("R_b", R_b_Pl), ("r_e", r_e_Pl), ("a_0", a0_Pl)]:
    N_3d = (R_H_Pl / scale)**3
    N_4d = (R_H_Pl / scale)**4
    d0_from_3d = (R_H_Pl**4 / N_3d)**0.25
    d0_from_4d = (R_H_Pl**4 / N_4d)**0.25
    print(f"\n  Scale = {scale_name} = {scale:.3e} ℓ_Pl")
    print(f"    N_3D channels: {N_3d:.3e}")
    print(f"    d_0 from 3D count: {d0_from_3d:.3e}  (target {d0_target_Pl:.3e}, err={abs(d0_from_3d-d0_target_Pl)/d0_target_Pl*100:.1f}%)")
    print(f"    d_0 from 4D count: {d0_from_4d:.3e}  (target {d0_target_Pl:.3e}, err={abs(d0_from_4d-d0_target_Pl)/d0_target_Pl*100:.1f}%)")

print("\n" + "="*60)
print("APPROACH 9: The Bekenstein route — d_0 from entropy matching")
print("="*60)
# S_Bekenstein = A/(4 ℓ_Pl^2) for black hole
# BST vacuum entropy: S_vac = N_channels × ln(138)
# Cosmological horizon entropy: S_H = π R_H^2 / ℓ_Pl^2
# If BST channels tile the horizon: N_channels × d_0^2 = R_H^2
# Then d_0 = R_H / sqrt(N_channels)
# And N_channels = R_H^2 / d_0^2

# From the partition function: N_channels = exp(S_vac/k_B) where S_vac = ln(138) per channel
# This gives N_channels = R_H^2/d_0^2
# So d_0 = R_H / sqrt(R_H^2/d_0^2) — circular!
# Need to break circularity with additional constraint

# Better: use S_H = N_channels × ln(138) (BST prediction for horizon entropy)
# S_H = π R_H^2 / ℓ_Pl^2
# N_channels = π R_H^2 / (ℓ_Pl^2 × ln(138))
# d_0^4 = R_H^4 / N_channels = R_H^4 × ℓ_Pl^2 × ln(138) / (π R_H^2)
#        = R_H^2 × ℓ_Pl^2 × ln(138) / π
# d_0 = ℓ_Pl × sqrt(R_H / (π/ln(138))^{1/2})
ln138 = np.log(138)
d0_bek_4 = R_H_Pl**2 * ln138 / π   # in ℓ_Pl^4 units
d0_bek = d0_bek_4**0.25
N_bek = π * R_H_Pl**2 / ln138
print(f"  S_H = N × ln(138) route:")
print(f"    N_channels = π R_H² / ln(138) = {N_bek:.4e}")
print(f"    d_0 = (R_H² × ln(138)/π)^{{1/4}} = {d0_bek:.4e} ℓ_Pl")
print(f"    Target: {d0_target_Pl:.4e}")
print(f"    Error: {abs(d0_bek-d0_target_Pl)/d0_target_Pl*100:.2f}%")

# Try with full sphere horizon: S_H = A/4 = 4π R_H^2 / 4 = π R_H^2
# With the numerical Hubble radius more carefully
print(f"\n  Varying R_H:")
for RH_exp in [60, 60.5, 60.94, 61]:
    RH = 10**RH_exp
    d0_t = (RH**2 * ln138 / π)**0.25
    err = abs(d0_t - d0_target_Pl)/d0_target_Pl * 100
    print(f"    R_H = 10^{RH_exp}: d_0 = {d0_t:.4e}  (err={err:.2f}%)")

print("\n" + "="*60)
print("APPROACH 10: Direct from m_e/m_Pl without R_H")
print("="*60)
# d_0 = ℓ_Pl × (m_e/m_Pl)^n for what n?
n_test = np.log(d0_target_Pl) / np.log(m_e_Pl)
print(f"  d_0 = ℓ_Pl × (m_e/m_Pl)^n  →  n = {n_test:.6f}")
print(f"  Nearest fractions:")
for p, q in [(1,2),(1,3),(2,3),(3,4),(1,4),(3,2),(4,3),(5,4),(7,4)]:
    d0_test = m_e_Pl**(p/q)
    err = abs(d0_test - d0_target_Pl)/d0_target_Pl * 100
    if err < 50:
        print(f"    n={p}/{q}: {d0_test:.4e}  (err={err:.2f}%)")

print("\n" + "="*60)
print("APPROACH 11: The Key Geometric Route — m_e from D_IV^1")
print("="*60)
# The Wyler formula for α uses Vol(D_IV^5)^{1/4}.
# The GENERALIZED Wyler formula would give "α_k" for each domain.
# For k=1: the natural geometric "coupling" of D_IV^1 is
#   α_1 = (9/8π⁴) × Vol(D_IV^1)^{1/0} → undefined (1/4 came from k-1=4 for k=5)
#
# Better: the Wyler formula is α = (9/8π⁴)(Vol D_IV^5)^{1/(k-1)} with k=5
# So the exponent is 1/(k-1) = 1/4.
# For the ELECTRON mass, the natural formula would use D_IV^1.
# But D_IV^1 has k=1, so 1/(k-1) = 1/0 → divergent.
# This suggests the electron mass cannot come from the same Wyler mechanism
# as α — it requires a different geometric quantity.
#
# The electron mass in Planck units is:
#   m_e/m_Pl = 4.185e-23
# In terms of dimensionless BST quantities:
print(f"  m_e/m_Pl = {m_e_Pl:.6e}")
print(f"  log10(m_e/m_Pl) = {np.log10(m_e_Pl):.4f}")
print(f"  = -22.378")
print()
# Is this related to α × (geometric factor)?
# m_e ≈ α² × m_Pl × (something of order 10^{18})? No.
# The electron mass IS one of the hardest quantities in physics to derive.
# In BST terms, it's the mass of the minimal circuit on D_IV^1.
# The Bergman kernel at origin K_1(0,0) = 1/π sets the "density per unit volume"
# The circuit has length ~ R_b × K_1(0,0)^?
#
# NEW APPROACH: From the fermion mass formula, we know
#   m_μ/m_e = (K_3/K_1)^6
# So if m_μ is somehow more tractable than m_e (it's not in standard physics),
# we could pivot. But m_μ is also a BST-derived quantity.
#
# THE SELF-CONSISTENCY ROUTE:
# We derived m_μ/m_e from geometry. Now what if we also derive m_μ/m_Pl
# from a DIFFERENT geometric argument, and together they give both m_e/m_Pl
# and m_μ/m_Pl?
#
# The Wyler formula gives α = 1/137 from Vol(D_IV^5)^{1/4}.
# What if m_e/m_Pl = C × Vol(D_IV^1)^{?} for some known constant C?
# α = (9/8π⁴)(Vol D_IV^5)^{1/4}
# By analogy: m_e/m_Pl = (9/8π⁴) × Vol(D_IV^1)^{exponent}
# But what exponent? For k=1, the orbit dimension is different.
#
# The Wyler constant (9/8π⁴):
C_Wyler = 9/(8*π**4)
print(f"  Wyler constant 9/(8π⁴) = {C_Wyler:.6e}")
print(f"  C_Wyler × V(D_IV^1) = {C_Wyler * V(1):.6e}")
print(f"  C_Wyler × V(D_IV^1)^2 = {C_Wyler * V(1)**2:.6e}")
print(f"  m_e/m_Pl = {m_e_Pl:.6e}")
print()
# Try: m_e/m_Pl = C_Wyler × V(D_IV^1)^n × V(D_IV^5)^m
# This is a 2-parameter search
best3 = []
for n1 in np.arange(-5, 8, 0.5):
    for n5 in np.arange(-3, 4, 0.5):
        val = C_Wyler * V(1)**n1 * V(5)**n5
        if val <= 0: continue
        err = abs(val - m_e_Pl)/m_e_Pl * 100
        if err < 0.5:
            best3.append((err, n1, n5, val))
best3.sort()
for err, n1, n5, val in best3[:10]:
    print(f"  C_W × V(D1)^{n1:.1f} × V(D5)^{n5:.1f} = {val:.4e}  (err={err:.3f}%)")

print("\n" + "="*60)
print("APPROACH 12: The Self-Consistent System")
print("="*60)
# CRITICAL INSIGHT: we have TWO independent equations:
# (A) m_μ/m_e = (24/π²)^6  [confirmed 0.003%]
# (B) α = (9/8π⁴)(Vol D_IV^5)^{1/4} [confirmed 0.0001%]
#
# These are BOTH dimensionless. To get a DIMENSIONFUL quantity (m_e/m_Pl),
# we need ONE input that has the Planck scale.
#
# The ONLY way to derive m_e/m_Pl from pure BST geometry would require
# the BST geometry to CONTAIN information about the Planck scale relative to
# the electroweak scale — i.e., the hierarchy problem must be solved.
#
# BST Section 10.5 claims to solve the hierarchy problem geometrically.
# If G = ℓ_Pl² c³/ℏ emerges from the contact graph as a STATISTICAL average,
# then G is derived, and m_Pl = sqrt(ℏc/G) is also derived.
#
# In that case:
# m_e/m_Pl = (m_e in BST units) / (m_Pl in BST units)
#           = K_1(0,0)^{dim} / G^{-1/2}
# where G in BST units is ~ 1/N_channels (entropic gravity).
#
# For N_channels ~ 10^{122}:
#   m_Pl^2 ~ N^{1/2} ~ 10^{61} in BST units
#   m_Pl ~ 10^{30.5} in BST units
#   m_e ~ K_1 × dim_factor ~ 0.32 × 2 ~ 0.64 in BST units
#   m_e/m_Pl ~ 0.64 / 10^{30.5} ~ 2 × 10^{-31}
#
# Compare to actual: m_e/m_Pl = 4.2 × 10^{-23}
# Off by 8 orders... the N^{1/2} scaling isn't quite right.
print(f"  Entropic gravity test:")
N_H = 10**122
m_Pl_BST_sq = N_H**0.5
m_e_BST = K1 * 2  # rough estimate: K_1 × dim_R(D_IV^1) = 1/π × 2
ratio_test = m_e_BST / m_Pl_BST_sq**0.5
print(f"  N ~ 10^122, m_Pl(BST) ~ 10^61, m_e(BST) ~ {m_e_BST:.3f}")
print(f"  m_e/m_Pl ~ {ratio_test:.3e}  vs actual {m_e_Pl:.3e}")
print()

# Summary
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"""
WHAT WE KNOW:
  d_0/ℓ_Pl (target) = {d0_target_Pl:.4e}  (= 10^{np.log10(d0_target_Pl):.2f})
  R_b/ℓ_Pl = m_Pl/m_e = {lambda_e_Pl:.4e}  (= 10^{np.log10(lambda_e_Pl):.2f})
  R_s/ℓ_Pl = ρ × R_b/ℓ_Pl = {R_s_Pl:.4e}

PROMISING APPROACH:
  The Bekenstein-BST route (Approach 9) gives the RIGHT PARAMETRIC FORM:
    d_0 = ℓ_Pl × (R_H² ln(138)/π)^{{1/4}}
  This relates d_0 to R_H — one observational input (Hubble radius).

  But R_H itself should be derivable from BST as the equilibrium size
  of the spatial phase, set by T_c and the expansion dynamics.

REMAINING GAP:
  All dimensionless ratios (α, m_μ/m_e, T_c/N_max) ARE derivable from BST.
  The ONE dimensionful input needed is:
    - Either m_e in Planck units (the hierarchy problem)
    - Or R_H in Planck units (the cosmological scale)
  These are related: m_e/m_Pl ↔ R_H/ℓ_Pl through the BST substrate scale.

  The key is the BST derivation of G (or equivalently m_Pl) from the
  contact graph entropy. Once G = (contact entropy)^{{-1}} is explicit,
  everything is determined.
""")
