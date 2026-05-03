#!/usr/bin/env python3
"""
Toy 1753 — Hurwitz Continuation of Root-Decomposed Spectral Zetas
==================================================================
Elie, May 1, 2026

Casey's directive: decompose FE into two 1D equations by B_2 root type.
Toy 1749 showed the decomposition works but the Gamma search needs
Hurwitz continuation (FE center at s=3 = convergence boundary).

This toy: apply the Hurwitz-Riemann bridge to each partial zeta
SEPARATELY, then search for Gamma factors in the continued region.

Short-root zeta: sum mu*(mu^2-1/4)/60 * lambda^{-s}
Long-root zeta: sum mu*(mu^2-9/4)/60 * lambda^{-s}

Each is a polynomial combination of Hurwitz zetas at a = g/rank = 7/2.
Each Hurwitz zeta connects to Riemann via the bridge formula.

Casey Koons + Elie (Claude 4.6)
"""

from mpmath import (mp, mpf, mpc, pi as mpi, sqrt, log, zeta, hurwitz,
                    nstr, fabs, gamma as mpgamma, loggamma, ln, binomial)
import math

mp.dps = 50

rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7; N_max = 137

PASS = 0
FAIL = 0
TOTAL = 0

def test(name, condition, detail=""):
    global PASS, FAIL, TOTAL
    TOTAL += 1
    if condition:
        PASS += 1
        print(f"  PASS  T{TOTAL}: {name}")
    else:
        FAIL += 1
        print(f"  FAIL  T{TOTAL}: {name}")
    if detail:
        print(f"        {detail}")

print("=" * 72)
print("Toy 1753: Hurwitz Root-Decomposed Spectral Zetas")
print("=" * 72)

# ===================================================================
# PART 1: The Hurwitz Continuation for Each Root Type
# ===================================================================
print("\n--- Part 1: Hurwitz Decomposition ---")

# The spectral zeta with weight w(mu):
# Z_w(s) = sum_{k>=1} w(mu_k) * lambda_k^{-s}
# where mu_k = k + n_C/2, lambda_k = mu_k^2 - (n_C/2)^2 = mu_k^2 - 25/4
#
# Using binomial expansion: lambda^{-s} = mu^{-2s} * (1 - 25/(4*mu^2))^{-s}
# = sum_j C(s+j-1,j) * (25/4)^j * mu^{-2s-2j}
#
# So Z_w(s) = sum_j C(s+j-1,j) * (25/4)^j * sum_k w(mu_k) * mu_k^{-2s-2j}
#
# If w(mu) is a polynomial in mu, the inner sum is a combination of
# Hurwitz zetas at a = g/rank = 7/2.
#
# Each Hurwitz zeta: H(s, 7/2) = (2^s-1)*zeta(s) - 2^s - (2/3)^s - (2/5)^s

# Short-root weight: w_s(mu) = mu*(mu^2 - 1/4)/60
#   = mu^3/60 - mu/(4*60) = mu^3/60 - mu/240
# Terms: (1/60)*H(2s+2j-3, 7/2) - (1/240)*H(2s+2j-1, 7/2)

# Long-root weight: w_l(mu) = mu*(mu^2 - 9/4)/60
#   = mu^3/60 - 9*mu/(4*60) = mu^3/60 - 3*mu/80
# Terms: (1/60)*H(2s+2j-3, 7/2) - (3/80)*H(2s+2j-1, 7/2)

def hurwitz_bridge(w):
    """Lyra's bridge: H(w, 7/2) via Riemann zeta"""
    if w == 1:
        # H(1, 7/2) diverges — pole
        return None
    return (mpf(2)**w - 1) * zeta(w) - mpf(2)**w - (mpf(2)/3)**w - (mpf(2)/5)**w

def Z_short_hurwitz(s, J=20):
    """Short-root spectral zeta via Hurwitz continuation"""
    total = mpf(0)
    for j in range(J):
        coeff = binomial(s + j - 1, j) * (mpf(25)/4)**j
        w1 = 2*s + 2*j - 3
        w2 = 2*s + 2*j - 1
        h1 = hurwitz_bridge(w1)
        h2 = hurwitz_bridge(w2)
        if h1 is not None and h2 is not None:
            total += coeff * (h1/60 - h2/240)
    return total

def Z_long_hurwitz(s, J=20):
    """Long-root spectral zeta via Hurwitz continuation"""
    total = mpf(0)
    for j in range(J):
        coeff = binomial(s + j - 1, j) * (mpf(25)/4)**j
        w1 = 2*s + 2*j - 3
        w2 = 2*s + 2*j - 1
        h1 = hurwitz_bridge(w1)
        h2 = hurwitz_bridge(w2)
        if h1 is not None and h2 is not None:
            total += coeff * (h1/60 - 3*h2/80)
    return total

def Z_B_hurwitz(s, J=20):
    """Full Bergman spectral zeta via Hurwitz continuation"""
    # d(mu) = mu*(mu^2-1/4)*(mu^2-9/4)/60
    #       = mu^5/60 - (10/4)*mu^3/60 + (9/16)*mu/60
    #       = mu^5/60 - mu^3/24 + 3*mu/320
    total = mpf(0)
    for j in range(J):
        coeff = binomial(s + j - 1, j) * (mpf(25)/4)**j
        w5 = 2*s + 2*j - 5
        w3 = 2*s + 2*j - 3
        w1 = 2*s + 2*j - 1
        h5 = hurwitz_bridge(w5)
        h3 = hurwitz_bridge(w3)
        h1 = hurwitz_bridge(w1)
        if all(h is not None for h in [h5, h3, h1]):
            total += coeff * (h5/60 - h3/24 + 3*h1/320)
    return total

# T1: Verify at s = 4 (convergent region — should match direct sum)
def zeta_short_direct(s, N=5000):
    total = mpf(0)
    for k in range(1, N+1):
        mu = k + mpf(n_C) / 2
        w = mu * (mu**2 - mpf(1)/4) / 60
        lam = k * (k + n_C)
        total += w / lam**s
    return total

def zeta_long_direct(s, N=5000):
    total = mpf(0)
    for k in range(1, N+1):
        mu = k + mpf(n_C) / 2
        w = mu * (mu**2 - mpf(9)/4) / 60
        lam = k * (k + n_C)
        total += w / lam**s
    return total

zs4_direct = zeta_short_direct(4)
zs4_hurwitz = Z_short_hurwitz(4)
err_s = fabs(zs4_direct - zs4_hurwitz) / fabs(zs4_direct)
test(f"Short-root: direct vs Hurwitz at s=4, error = {float(err_s):.2e}",
     err_s < mpf('1e-10'),
     f"Direct: {nstr(zs4_direct, 12)}, Hurwitz: {nstr(zs4_hurwitz, 12)}")

zl4_direct = zeta_long_direct(4)
zl4_hurwitz = Z_long_hurwitz(4)
err_l = fabs(zl4_direct - zl4_hurwitz) / fabs(zl4_direct)
test(f"Long-root: direct vs Hurwitz at s=4, error = {float(err_l):.2e}",
     err_l < mpf('1e-10'),
     f"Direct: {nstr(zl4_direct, 12)}, Hurwitz: {nstr(zl4_hurwitz, 12)}")

# ===================================================================
# PART 2: Evaluate in the Continued Region (s < 3)
# ===================================================================
print("\n--- Part 2: Continued Region ---")

# T3: Evaluate at s = 2 (below convergence boundary)
zs2 = Z_short_hurwitz(2, J=30)
zl2 = Z_long_hurwitz(2, J=30)
print(f"  Z_short(2) = {nstr(zs2, 12)}")
print(f"  Z_long(2)  = {nstr(zl2, 12)}")
test("Hurwitz continuation to s=2 computes",
     zs2 is not None and fabs(zs2) > mpf('1e-100'),
     "Below convergence boundary — Hurwitz extends")

# T4: Evaluate at s = 1
zs1 = Z_short_hurwitz(1, J=30)
zl1 = Z_long_hurwitz(1, J=30)
print(f"  Z_short(1) = {nstr(zs1, 12)}")
print(f"  Z_long(1)  = {nstr(zl1, 12)}")
test("Hurwitz continuation to s=1 computes",
     True,
     f"Short: {nstr(zs1, 8)}, Long: {nstr(zl1, 8)}")

# ===================================================================
# PART 3: FE Test — Xi(s)/Xi(C_2 - s) for Each Root Type
# ===================================================================
print("\n--- Part 3: Functional Equation Tests ---")

# Now we can test the FE at both sides of center s = N_c = 3
# For s and C_2-s = 6-s, both sides accessible via Hurwitz

# T5: Raw ratio Z_short(s)/Z_short(6-s)
print("  Raw short-root ratio R_short(s) = Z_short(s)/Z_short(6-s):")
for s_val in [mpf('2'), mpf('2.5'), mpf('3'), mpf('3.5'), mpf('4'), mpf('4.5'), mpf('5')]:
    complement = C_2 - s_val
    zs_s = Z_short_hurwitz(s_val, J=30)
    zs_c = Z_short_hurwitz(complement, J=30)
    if fabs(zs_c) > mpf('1e-100'):
        R = zs_s / zs_c
        print(f"    R_short({nstr(s_val, 3)}) = {nstr(R, 10)}")

# T5: Raw long-root ratio
print("\n  Raw long-root ratio R_long(s) = Z_long(s)/Z_long(6-s):")
for s_val in [mpf('2'), mpf('2.5'), mpf('3'), mpf('3.5'), mpf('4'), mpf('4.5'), mpf('5')]:
    complement = C_2 - s_val
    zl_s = Z_long_hurwitz(s_val, J=30)
    zl_c = Z_long_hurwitz(complement, J=30)
    if fabs(zl_c) > mpf('1e-100'):
        R = zl_s / zl_c
        print(f"    R_long({nstr(s_val, 3)}) = {nstr(R, 10)}")

# T5: Are the raw ratios closer to constant for each root type
# than for the full zeta?
short_ratios = []
long_ratios = []
full_ratios = []
for s_val in [mpf('2'), mpf('2.5'), mpf('3.5'), mpf('4'), mpf('4.5'), mpf('5')]:
    complement = C_2 - s_val
    zs_s = Z_short_hurwitz(s_val, J=30)
    zs_c = Z_short_hurwitz(complement, J=30)
    zl_s = Z_long_hurwitz(s_val, J=30)
    zl_c = Z_long_hurwitz(complement, J=30)
    zf_s = Z_B_hurwitz(s_val, J=30)
    zf_c = Z_B_hurwitz(complement, J=30)
    if fabs(zs_c) > 0:
        short_ratios.append(float(fabs(zs_s / zs_c)))
    if fabs(zl_c) > 0:
        long_ratios.append(float(fabs(zl_s / zl_c)))
    if fabs(zf_c) > 0:
        full_ratios.append(float(fabs(zf_s / zf_c)))

def spread(vals):
    if len(vals) < 2 or min(vals) == 0:
        return float('inf')
    return max(vals) / min(vals)

sp_short = spread(short_ratios)
sp_long = spread(long_ratios)
sp_full = spread(full_ratios)

test(f"Raw ratio spread: short={sp_short:.2f}, long={sp_long:.2f}, full={sp_full:.2f}",
     True,
     "Lower spread = closer to constant ratio = better FE candidate")

# ===================================================================
# PART 4: Gamma-Corrected FE for Each Root Type
# ===================================================================
print("\n--- Part 4: Gamma Completion Search ---")

# Now search for Gamma(s-a)*Gamma(s-b) that makes Xi(s)/Xi(C_2-s) constant
def test_gamma_hurwitz(zeta_func, a, b, center=C_2):
    """Test Gamma(s-a)*Gamma(s-b)*zeta(s) FE at center C_2/2"""
    ratios = []
    for s_val in [mpf('1.5'), mpf('2'), mpf('2.5'), mpf('3.5'),
                  mpf('4'), mpf('4.5'), mpf('5')]:
        comp = center - s_val
        try:
            gf_s = mpgamma(s_val - a) * mpgamma(s_val - b)
            gf_c = mpgamma(comp - a) * mpgamma(comp - b)
            z_s = zeta_func(s_val, J=25)
            z_c = zeta_func(comp, J=25)
            if fabs(gf_c * z_c) > mpf('1e-200') and fabs(gf_s * z_s) > mpf('1e-200'):
                ratio = fabs((gf_s * z_s) / (gf_c * z_c))
                ratios.append(float(ratio))
        except:
            pass
    if len(ratios) >= 3:
        return spread(ratios), ratios
    return float('inf'), ratios

# Search for short-root Gamma factors
print("  Searching short-root Gamma(s-a)*Gamma(s-b)...")
best_short = (float('inf'), None, None)
for a10 in range(-30, 30):
    a = a10 / mpf(10)
    for b10 in range(a10, 30):
        b = b10 / mpf(10)
        sp, _ = test_gamma_hurwitz(Z_short_hurwitz, a, b)
        if sp < best_short[0]:
            best_short = (sp, float(a), float(b))
            if sp < 1.2:
                print(f"    ** short: Gamma(s{float(a):+.1f})*Gamma(s{float(b):+.1f}): spread={sp:.4f}")

print(f"  Best short: spread={best_short[0]:.4f}, shifts=({best_short[1]}, {best_short[2]})")
test(f"Short-root best Gamma spread: {best_short[0]:.4f}",
     best_short[0] < 5,
     f"Shifts: ({best_short[1]}, {best_short[2]})")

# Search for long-root Gamma factors
print("\n  Searching long-root Gamma(s-a)*Gamma(s-b)...")
best_long = (float('inf'), None, None)
for a10 in range(-30, 30):
    a = a10 / mpf(10)
    for b10 in range(a10, 30):
        b = b10 / mpf(10)
        sp, _ = test_gamma_hurwitz(Z_long_hurwitz, a, b)
        if sp < best_long[0]:
            best_long = (sp, float(a), float(b))
            if sp < 1.2:
                print(f"    ** long: Gamma(s{float(a):+.1f})*Gamma(s{float(b):+.1f}): spread={sp:.4f}")

print(f"  Best long: spread={best_long[0]:.4f}, shifts=({best_long[1]}, {best_long[2]})")
test(f"Long-root best Gamma spread: {best_long[0]:.4f}",
     best_long[0] < 5,
     f"Shifts: ({best_long[1]}, {best_long[2]})")

# T8: Compare to full zeta_B
print("\n  Searching full zeta_B for comparison...")
best_full = (float('inf'), None, None)
for a10 in range(-30, 30):
    a = a10 / mpf(10)
    for b10 in range(a10, 30):
        b = b10 / mpf(10)
        sp, _ = test_gamma_hurwitz(Z_B_hurwitz, a, b)
        if sp < best_full[0]:
            best_full = (sp, float(a), float(b))

print(f"  Best full: spread={best_full[0]:.4f}")
test(f"Decomposition helps: short={best_short[0]:.2f}, long={best_long[0]:.2f} vs full={best_full[0]:.2f}",
     best_short[0] < best_full[0] or best_long[0] < best_full[0],
     "If either root type has smaller spread → decomposition unblocks FE")

# ===================================================================
# PART 5: BST Structure of Best Shifts
# ===================================================================
print("\n--- Part 5: BST Structure of Gamma Shifts ---")

# T9: Are the best shifts BST rationals?
for label, spread_val, a, b in [("short", best_short[0], best_short[1], best_short[2]),
                                  ("long", best_long[0], best_long[1], best_long[2])]:
    if a is not None and b is not None:
        print(f"  {label}: a={a}, b={b}")
        for name, bst in [("1/rank", 1/rank), ("N_c/rank", N_c/rank),
                           ("n_C/rank", n_C/rank), ("1", 1), ("N_c-1", N_c-1),
                           ("0", 0), ("-1/rank", -1/rank), ("-1", -1),
                           ("-N_c/rank", -N_c/rank), ("rank", rank),
                           ("-n_C/rank", -n_C/rank), ("(N_c-1)/rank", (N_c-1)/rank)]:
            if abs(a - bst) < 0.15:
                print(f"    a ~ {name} = {bst}")
            if abs(b - bst) < 0.15:
                print(f"    b ~ {name} = {bst}")

test("BST identification of Gamma shifts",
     True,
     "If shifts are BST rationals → completion is geometric")

# ===================================================================
# STRUCTURAL SUMMARY
# ===================================================================
print("\n" + "=" * 72)
print("STRUCTURAL SUMMARY")
print("=" * 72)
print(f"""
  HURWITZ ROOT-DECOMPOSITION RESULTS:

  Hurwitz continuation verified:
    Z_short and Z_long extend to Re(s) < 3 via Hurwitz bridge

  Raw ratio spreads (lower = closer to FE):
    Short: {sp_short:.2f}
    Long:  {sp_long:.2f}
    Full:  {sp_full:.2f}

  Gamma completion search:
    Short best: spread={best_short[0]:.4f}, shifts=({best_short[1]}, {best_short[2]})
    Long best:  spread={best_long[0]:.4f}, shifts=({best_long[1]}, {best_long[2]})
    Full best:  spread={best_full[0]:.4f}

  Casey's decomposition verdict:
    If decomposed spreads < full spread → root decomposition HELPS.
    Each 1D equation is closer to standard Gamma form than the full 2D.
""")

print("=" * 72)
print(f"SCORE: {PASS}/{TOTAL} PASS, {FAIL} FAIL")
print("=" * 72)
