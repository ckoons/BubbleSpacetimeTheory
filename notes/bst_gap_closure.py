"""
Closing the 0.218% Gap: Haldane and Bergman Corrections to d_{l*}
=================================================================
κ_geometric = N_max × d_5 × K_5(0,0) = 137 × 91 × 1920/π^5 ≈ 78,219
κ_Wyler     = (138)^2 × ln^2(138) / (1 + ln(138))           ≈ 78,049

Gap: 0.218% → d_eff needed = 90.808 (vs d_5 = 91)

Two physical candidates:
  A. Haldane exclusion:        d_5^eff = d_5 - g × Σ_{l<5} d_l
  B. Bergman metric weighting: d_eff   = (w×d_4 + d_5) / (1+w)
  C. Resonance boundary:       d_5^eff = d_5 - 1/l*

Author: Casey Koons & Claude (Anthropic), March 2026
"""
import numpy as np
from scipy.optimize import brentq

pi = np.pi

# ── BST constants ───────────────────────────────────────────────────────────
N_max  = 137
l_star = 5           # dim_C(D_IV^5)
alpha_inv_Wyler = 137.036082   # Wyler formula for α^{-1}

def d_S4(l):
    """S^4 spherical harmonic degeneracy at degree l."""
    return (l+1)*(l+2)*(2*l+3)//6

K5 = 1920.0 / pi**5   # Bergman kernel at origin = 1 / Vol(D_IV^5)

d5 = d_S4(5)   # 91
d4 = d_S4(4)   # 55
d6 = d_S4(6)   # 140

# ── κ and ρ* machinery ──────────────────────────────────────────────────────
def kappa_for_rho(rho):
    """κ that places the cost-function minimum exactly at ρ."""
    return (rho+1)**2 * np.log(rho+1)**2 / (1.0 + np.log(rho+1))

def rho_star(kappa):
    """Continuous minimum of C(ρ) = ρ + κ/((ρ+1)ln(ρ+1))."""
    def dC(rho):
        ln = np.log(rho+1)
        return 1.0 - kappa*(1.0+ln)/((rho+1)*ln)**2
    return brentq(dC, 100, 200)

kappa_exact    = kappa_for_rho(137.0)
kappa_Wyler    = kappa_for_rho(alpha_inv_Wyler)
kappa_geometric = N_max * d5 * K5

# d_eff that would reproduce κ_Wyler exactly
d_eff_target = kappa_Wyler / (N_max * K5)
Delta_d       = d5 - d_eff_target          # ≈ +0.192  (downward shift needed)

n_below = sum(d_S4(l) for l in range(l_star))   # Σ_{l=0}^{4} d_l = 105

# ── Print header ────────────────────────────────────────────────────────────
print("=" * 70)
print("EXACT REFERENCE VALUES")
print("=" * 70)
print(f"  κ_exact       = {kappa_exact:.4f}  → ρ* = 137.000")
print(f"  κ_Wyler       = {kappa_Wyler:.4f}  → ρ* = {alpha_inv_Wyler}")
print(f"  κ_geometric   = {kappa_geometric:.4f}  → ρ* = {rho_star(kappa_geometric):.6f}")
print()
print(f"  d_5 = {d5},  d_4 = {d4},  d_6 = {d6}")
print(f"  K5(0,0) = 1920/π^5 = {K5:.8f}")
print(f"  Σ_{{l<5}} d_l  = {n_below}")
print()
print(f"  d_eff needed  = {d_eff_target:.8f}")
print(f"  Δd needed     = {Delta_d:.8f}   (downward shift from 91)")
print()

def test_d(label, d_eff, target=alpha_inv_Wyler):
    kap = N_max * d_eff * K5
    rho = rho_star(kap)
    pct = (rho - target)/target*100
    return rho, pct

# ── CANDIDATE A: Haldane exclusion ─────────────────────────────────────────
print("=" * 70)
print("CANDIDATE A — HALDANE EXCLUSION")
print("  d_5^eff = d_5 - g × Σ_{l<5} d_l = 91 - 105·g")
print("=" * 70)

g_needed = Delta_d / n_below
print(f"  g needed = {g_needed:.8f}  =  1/{1/g_needed:.3f}")
print()

# Natural BST expressions for g
print(f"  {'Expression':40s}   {'g':>10}   {'d_eff':>8}   {'ρ*':>10}   {'err%':>8}")
print(f"  {'-'*40}   {'-'*10}   {'-'*8}   {'-'*10}   {'-'*8}")

def row_g(name, g):
    d_eff = d5 - g * n_below
    rho, pct = test_d(name, d_eff)
    mark = " ←" if abs(pct) < 0.005 else ""
    print(f"  {name:40s}   {g:10.6f}   {d_eff:8.4f}   {rho:10.6f}   {pct:+8.4f}%{mark}")

row_g("1/N_max",                  1/N_max)
row_g("1/(N_max+1)",              1/(N_max+1))
row_g("1/(N_max × l*)",           1/(N_max*l_star))
row_g("1/(2 × N_max)",            1/(2*N_max))
row_g("1/(4 × N_max)",            1/(4*N_max))
row_g("l*/N_max²",               l_star/N_max**2)
row_g("α_Wyler = 1/137.036",     1/alpha_inv_Wyler)
row_g("1/(6 × d_5)",              1/(6*d5))        # 6 = l*+1
row_g("1/((l*+1) × d_{l*})",     1/((l_star+1)*d5))  # same
row_g("1/(d_5 + n_below)",       1/(d5 + n_below))
row_g("1/(N_max × K5 × 10)",     1/(N_max*K5*10))
row_g("δ_Wyler / d_5",            (alpha_inv_Wyler-137)/d5)
row_g("δ_Wyler / n_below",        (alpha_inv_Wyler-137)/n_below)

print()

# ── CANDIDATE B: Bergman metric weighting ──────────────────────────────────
print("=" * 70)
print("CANDIDATE B — BERGMAN CURVATURE WEIGHTING")
print("  d_eff = (w·d_4 + d_5)/(1+w),   d_4=55,  d_5=91")
print("  D_IV^5 Bergman curvatures: κ₁ = −1,  κ₂ = −1/2  (ratio 2:1)")
print("=" * 70)

w_needed = Delta_d / (d_eff_target - d4)
print(f"  w needed = {w_needed:.8f}  =  1/{1/w_needed:.3f}")
print()

print(f"  {'Expression':40s}   {'w':>10}   {'d_eff':>8}   {'ρ*':>10}   {'err%':>8}")
print(f"  {'-'*40}   {'-'*10}   {'-'*8}   {'-'*10}   {'-'*8}")

def row_w(name, w):
    d_eff = (w*d4 + d5)/(1+w)
    rho, pct = test_d(name, d_eff)
    mark = " ←" if abs(pct) < 0.005 else ""
    print(f"  {name:40s}   {w:10.6f}   {d_eff:8.4f}   {rho:10.6f}   {pct:+8.4f}%{mark}")

row_w("|κ₂/κ₁| = 1/2",                   0.5)
row_w("|κ₂/κ₁| × l*/N_max",              0.5*l_star/N_max)
row_w("|κ₂/κ₁| × (l*/N_max)²",           0.5*(l_star/N_max)**2)
row_w("(l*/N_max)²",                      (l_star/N_max)**2)
row_w("l*/(N_max × (d_5-d_4))",          l_star/(N_max*(d5-d4)))
row_w("1/(l* × d_5)",                     1/(l_star*d5))
row_w("1/(l* × (d_5-d_4))",              1/(l_star*(d5-d4)))
row_w("d_4/d_5²",                         d4/d5**2)
row_w("1/(2×l*×d_4)",                     1/(2*l_star*d4))
row_w("δ_Wyler/N_max",                    (alpha_inv_Wyler-137)/N_max)
row_w("δ_Wyler/(d_5-d_4)",               (alpha_inv_Wyler-137)/(d5-d4))
row_w("Vol(D_IV^5) / (4π²)",             (pi**5/1920)/(4*pi**2))

print()

# ── CANDIDATE C: Resonance boundary correction ─────────────────────────────
print("=" * 70)
print("CANDIDATE C — RESONANCE BOUNDARY CORRECTIONS")
print("  Various 'internal boundary at l*' formulas")
print("=" * 70)

print(f"  {'Expression':40s}   {'corr':>8}   {'d_eff':>8}   {'ρ*':>10}   {'err%':>8}")
print(f"  {'-'*40}   {'-'*8}   {'-'*8}   {'-'*10}   {'-'*8}")

def row_c(name, corr):
    d_eff = d5 - corr
    try:
        rho, pct = test_d(name, d_eff)
        mark = " ←" if abs(pct) < 0.005 else ""
        print(f"  {name:40s}   {corr:8.4f}   {d_eff:8.4f}   {rho:10.6f}   {pct:+8.4f}%{mark}")
    except Exception:
        print(f"  {name:40s}   {corr:8.4f}   {d_eff:8.4f}   [no solution]")

d2_5 = 2*l_star + 3   # d''(l) = 2l+3 evaluated at l=5: d''(5) = 13

row_c("1/l*  (= 1/5)",                   1/l_star)
row_c("1/(l*+1)  (= 1/6)",               1/(l_star+1))
row_c("1/(2×l*)",                         1/(2*l_star))
row_c("B₂ × d''(l*)  (= 1/6 × 13)",     (1/6)*d2_5)
row_c("B₂ × d''(l*)/l*",                (1/6)*d2_5/l_star)
row_c("B₂ × (d_5-d_4)/l*",              (1/6)*(d5-d4)/l_star)
row_c("d_5 / (N_max × K5 × d_5)",       d5/(N_max*K5*d5))
row_c("K5 × l*",                          K5*l_star)
row_c("(d_5/d_6) × (d_5-d_4)/N_max",   (d5/d6)*(d5-d4)/N_max)

print()

# ── CANDIDATE D: Combined Haldane + Bergman ─────────────────────────────────
print("=" * 70)
print("CANDIDATE D — COMBINED: FIRST-ORDER HALDANE + BERGMAN MIX")
print("=" * 70)

# The two most promising individual candidates:
# Haldane with g = 1/((l*+1)*d5) = 1/546
g_cand = 1/((l_star+1)*d5)
d_haldane = d5 - g_cand * n_below

# Bergman with w = δ_Wyler/(d5-d4)
w_cand = (alpha_inv_Wyler - 137)/(d5-d4)
d_bergman = (w_cand*d4 + d5)/(1+w_cand)

print(f"  Haldane alone  [g=1/((l*+1)d_5)=1/546]:  d_eff={d_haldane:.6f}, "
      f"ρ*={test_d('H',d_haldane)[0]:.6f}")
print(f"  Bergman alone  [w=δ_W/(d5-d4)=0.001002]:  d_eff={d_bergman:.6f}, "
      f"ρ*={test_d('B',d_bergman)[0]:.6f}")

# Half-and-half
d_half = 0.5*d_haldane + 0.5*d_bergman
print(f"  50/50 average:                              d_eff={d_half:.6f}, "
      f"ρ*={test_d('HB',d_half)[0]:.6f}")
print(f"  Target d_eff:                               {d_eff_target:.6f}")

print()

# ── CANDIDATE E: Curvature-weighted Bergman kernel ─────────────────────────
print("=" * 70)
print("CANDIDATE E — WEIGHTED BERGMAN KERNEL EVALUATION")
print("  κ uses K5 evaluated at the 'Haldane radius' r = l*/N_max")
print("  K5(r) = K5(0) × (1-r²)^{-6}  [approximate, type-IV Bergman]")
print("=" * 70)

r_haldane = l_star / N_max   # = 5/137 ≈ 0.03650
# For D_IV^n on the geodesic toward the boundary:
# K_n(r,r) ≈ K_n(0,0) × (1 - r^2)^{-(n+1)}  (rough, isotropic)
K5_r = K5 * (1 - r_haldane**2)**(-(l_star+1))
print(f"  r = l*/N_max = 5/137 = {r_haldane:.6f}")
print(f"  K5(r) ≈ K5(0) × (1-r²)^{{-6}} = {K5:.6f} × {(1-r_haldane**2)**(-(l_star+1)):.6f}")
print(f"        = {K5_r:.6f}")
kappa_K5r = N_max * d5 * K5_r
print(f"  κ with K5(r): {kappa_K5r:.4f}")
print(f"  ρ* = {rho_star(kappa_K5r):.6f}  (vs Wyler {alpha_inv_Wyler})")
print()

# ── BEST RESULT SUMMARY ────────────────────────────────────────────────────
print("=" * 70)
print("SUMMARY — CLOSEST CANDIDATES TO Wyler ρ* = 137.036082")
print("=" * 70)
print(f"  {'Formula':50s}   {'ρ*':>10}   {'err (ppm)':>10}")
print(f"  {'-'*50}   {'-'*10}   {'-'*10}")

summary_cases = [
    ("Geometric (no correction)", d5),
    ("Haldane: g=1/((l*+1)×d_5) = 1/546", d5 - (1/((l_star+1)*d5))*n_below),
    ("Haldane: g_exact (fitted)", d5 - g_needed*n_below),
    ("Bergman: w=δ_Wyler/(d5-d4)", (((alpha_inv_Wyler-137)/(d5-d4))*d4 + d5)
                                     / (1+(alpha_inv_Wyler-137)/(d5-d4))),
    ("Resonance: d_5 - 1/l*", d5 - 1/l_star),
    ("Resonance: d_5 - 1/(l*+1)", d5 - 1/(l_star+1)),
    ("K5(r=l*/N_max) correction", None),   # handled separately
]

for label, d_eff in summary_cases:
    if d_eff is None:
        rho = rho_star(kappa_K5r)
    else:
        rho = rho_star(N_max * d_eff * K5)
    err_ppm = (rho - alpha_inv_Wyler)/alpha_inv_Wyler * 1e6
    print(f"  {label:50s}   {rho:10.6f}   {err_ppm:+10.1f}")
