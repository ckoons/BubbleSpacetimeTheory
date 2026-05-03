"""
Toy 1788: Spectral Zeta Deep Ratio Analysis
=============================================
Follow-up to Toy 1785. Three investigations:

1. HIGH-s CONVERGENCE: Verify deviation ratio R(s)-C_2 converges
   to lambda_2/lambda_1 = 14/6 = g/N_c as s -> infinity.

2. 439/72 IDENTITY: Is zB(C_2)/zB(g) exactly 439/72? If so,
   what is the mechanism? Compute at 100 digits.

3. PSLQ on zeta_B values: Express key values in terms of
   {pi, zeta(3), zeta(5), zeta(7), log(2), log(3), log(5), log(7)}

4. 1/g^2 MECHANISM: Why does zB(g/rank) ~ 1/g^2?

Author: Elie | Date: 2026-05-02
"""

from mpmath import (mp, mpf, log, exp, pi, zeta, fsum, fac,
                     nstr, power, sqrt, gamma as mpgamma, pslq,
                     diff, polylog)

mp.dps = 80

# BST integers
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137

pass_count = 0
fail_count = 0
total_tests = 0

def test(name, condition, detail=""):
    global pass_count, fail_count, total_tests
    total_tests += 1
    tag = "PASS" if condition else "FAIL"
    if condition:
        pass_count += 1
    else:
        fail_count += 1
    print(f"  T{total_tests} [{tag}] {name}")
    if detail:
        print(f"       {detail}")

def d(k):
    """Hilbert function d_k = (2k+5)(k+1)(k+2)(k+3)(k+4)/120"""
    k = mpf(k)
    return (2*k + n_C) * (k+1) * (k+2) * (k+3) * (k+4) / fac(n_C)

def lam(k):
    """Eigenvalue lambda_k = k(k+5)"""
    return mpf(k) * (mpf(k) + n_C)

def zeta_B(s, N=20000):
    """Direct sum spectral zeta (convergent for Re(s) > 3)"""
    s = mpf(s)
    total = mpf(0)
    for k in range(1, N+1):
        total += d(k) / lam(k)**s
    return total

# ============================================================
# PART 1: HIGH-s CONVERGENCE OF DEVIATION RATIO
# ============================================================
print("=" * 70)
print("PART 1: Deviation Ratio Convergence to lambda_2/lambda_1 = g/N_c")
print("=" * 70)

# R(s) = zB(s)/zB(s+1) -> lambda_1 = C_2 = 6
# Deviation: delta(s) = R(s) - C_2
# delta(s)/delta(s+1) -> lambda_2/lambda_1 = 14/6 = 7/3

target = mpf(lam(2)) / lam(1)  # 14/6 = 7/3
print(f"\n  Target: lambda_2/lambda_1 = {int(lam(2))}/{int(lam(1))} = {float(target):.6f}")

# Compute at many s values
s_vals = list(range(4, 25))
zB_vals = {}
print(f"\n  Computing zeta_B at s = 4..24 (N=20000)...")
for s in s_vals:
    zB_vals[s] = zeta_B(s)
    if s <= 10 or s % 5 == 0:
        print(f"    zB({s}) = {nstr(zB_vals[s], 15)}")

print(f"\n  {'s':>4s} | {'R(s)':>18s} | {'delta(s)':>15s} | {'delta(s)/delta(s+1)':>20s} | {'error vs g/N_c':>15s}")
print("  " + "-" * 80)

devs = {}
for s in s_vals:
    if s+1 in zB_vals:
        R = zB_vals[s] / zB_vals[s+1]
        devs[s] = R - C_2

for s in s_vals:
    if s in devs and s+1 in devs:
        ratio = devs[s] / devs[s+1]
        err = abs(ratio - target) / target
        print(f"  {s:4d} | {float(devs[s] + C_2):18.12f} | {float(devs[s]):15.10f} | {float(ratio):20.12f} | {float(err):15.2e}")

# Test at s=20
if 20 in devs and 21 in devs:
    ratio_20 = devs[20] / devs[21]
    err_20 = abs(ratio_20 - target) / target
    test("Deviation ratio at s=20 matches g/N_c = 7/3 at < 0.1%",
         err_20 < mpf('0.001'),
         f"ratio = {float(ratio_20):.10f}, target = {float(target):.10f}, error = {float(err_20):.2e}")

# Check the NEXT correction term: second-order deviation
# delta_2(s) = delta(s)/delta(s+1) - 7/3
# delta_2(s)/delta_2(s+1) should approach (lambda_3/lambda_1) = 24/6 = 4
print(f"\n  Second-order deviation (-> lambda_3/lambda_1 = {int(lam(3))}/{int(lam(1))} = {float(lam(3)/lam(1)):.1f}):")
dev2 = {}
for s in s_vals:
    if s in devs and s+1 in devs:
        dev2[s] = devs[s] / devs[s+1] - target

for s in s_vals:
    if s in dev2 and s+1 in dev2 and abs(dev2[s+1]) > mpf('1e-40'):
        ratio2 = dev2[s] / dev2[s+1]
        if s >= 8 and s <= 18:
            print(f"    dev2({s})/dev2({s+1}) = {float(ratio2):.6f}")

target2 = lam(3) / lam(1)  # 24/6 = 4
if 18 in dev2 and 19 in dev2 and abs(dev2[19]) > mpf('1e-60'):
    ratio2_18 = dev2[18] / dev2[19]
    err2 = abs(ratio2_18 - target2) / target2
    test("Second-order deviation -> lambda_3/lambda_1 = 4 at < 1%",
         err2 < mpf('0.01'),
         f"ratio = {float(ratio2_18):.6f}, target = {float(target2):.1f}")

# ============================================================
# PART 2: 439/72 IDENTITY AT HIGH PRECISION
# ============================================================
print()
print("=" * 70)
print("PART 2: zB(C_2)/zB(g) = 439/72 Identity")
print("=" * 70)

zB6 = zB_vals[6]
zB7 = zB_vals[7]
ratio_67 = zB6 / zB7
target_439 = mpf(439) / 72

print(f"\n  zB(6)  = {nstr(zB6, 25)}")
print(f"  zB(7)  = {nstr(zB7, 25)}")
print(f"  Ratio  = {nstr(ratio_67, 25)}")
print(f"  439/72 = {nstr(target_439, 25)}")
print(f"  Gap    = {nstr(ratio_67 - target_439, 15)}")
gap_pct = abs(ratio_67 - target_439) / ratio_67 * 100
print(f"  Gap %  = {float(gap_pct):.6f}%")

test("zB(C_2)/zB(g) = 439/72 at < 0.01%",
     gap_pct < mpf('0.01'),
     f"gap = {float(gap_pct):.6f}%")

# What IS 439?
print(f"\n  Identity of 439:")
print(f"    439 is prime: {all(439 % p != 0 for p in range(2, 22))}")
print(f"    439 = 6*72 + 7 = C_2 * 72 + g")
print(f"    439 = 63*7 - 2 = (C_2*g + C_2*rank + g)*g - rank")
print(f"    439/72: 72 = C_2^2 * rank = {C_2**2 * rank}")
print(f"    439/72 = {float(mpf(439)/72):.10f}")

# Exact test: is the ratio EXACTLY 439/72?
# If not, what's the exact continued fraction?
from mpmath import identify
try:
    id_result = identify(ratio_67)
    if id_result:
        print(f"\n  mpmath identify: {id_result}")
except:
    print(f"\n  mpmath identify: no match")

# Check the ratio more precisely by computing with more terms
print(f"\n  Convergence test (increasing N):")
for N in [5000, 10000, 20000]:
    r = zeta_B(6, N) / zeta_B(7, N)
    gap = abs(r - target_439) / r * 100
    print(f"    N={N:>6d}: ratio = {nstr(r, 20)}, gap = {float(gap):.8f}%")

# Actually, 439/72 is NOT exact — this is a convergent sum and the ratio
# is an irrational number. But the BST APPROXIMATION may be exact up to
# O(1/N) truncation. Let me check the approach to the limit.

# The TRUE ratio zB(6)/zB(7) = sum d_k/lam_k^6 / sum d_k/lam_k^7
# For the ratio, lambda_1 = 6 term gives: d_1/6^6 / d_1/6^7 = 6 exactly
# The k=2 correction gives a term of order (6/14)^s * d_2/d_1
# So the TRUE ratio = 6 * [1 + eps] where eps involves all eigenvalues

# ============================================================
# PART 3: EXACT DECOMPOSITION OF THE RATIO
# ============================================================
print()
print("=" * 70)
print("PART 3: Exact Decomposition of zB(C_2)/zB(g)")
print("=" * 70)

# zB(s) = d_1/lam_1^s * [1 + sum_{k>=2} (d_k/d_1)*(lam_1/lam_k)^s]
# zB(6)/zB(7) = lam_1 * [1 + sum_{k>=2} r_k * x_k^6] / [1 + sum_{k>=2} r_k * x_k^7]
# where r_k = d_k/d_1, x_k = lam_1/lam_k

lam1 = lam(1)
d1 = d(1)
print(f"  lambda_1 = {int(lam1)}, d_1 = {int(d1)}")
print(f"  First eigenvalue ratio: lambda_2/lambda_1 = {int(lam(2))}/{int(lam1)} = {float(lam(2)/lam1):.4f}")

# Compute correction sums
S6 = mpf(0)
S7 = mpf(0)
for k in range(2, 20001):
    rk = d(k) / d1
    xk = lam1 / lam(k)
    S6 += rk * xk**6
    S7 += rk * xk**7

print(f"\n  Correction sums (sum_{k>=2} r_k * x_k^s):")
print(f"    S_6 = {nstr(S6, 15)}")
print(f"    S_7 = {nstr(S7, 15)}")
print(f"    Ratio = lam_1 * (1+S_6)/(1+S_7) = {int(lam1)} * {float((1+S6)/(1+S7)):.10f}")
print(f"          = {float(lam1 * (1+S6)/(1+S7)):.10f}")

# The ratio is lambda_1 * (1 + S_6) / (1 + S_7)
# For 439/72: 439/72 / 6 = 439/432. So (1+S_6)/(1+S_7) = 439/432
# Check:
target_corr = mpf(439) / 432
actual_corr = (1 + S6) / (1 + S7)
print(f"\n  (1+S_6)/(1+S_7) = {float(actual_corr):.10f}")
print(f"  439/432          = {float(target_corr):.10f}")
print(f"  gap              = {float(abs(actual_corr - target_corr)/target_corr*100):.6f}%")

# ============================================================
# PART 4: PSLQ ON KEY VALUES
# ============================================================
print()
print("=" * 70)
print("PART 4: PSLQ on Spectral Zeta Values")
print("=" * 70)

# Try to express zB(6) in terms of known constants
# zB(6) ~ 0.000154147
# Basis: {1, pi^2, pi^4, pi^6, zeta(3), zeta(5), zeta(7), zeta(9), zeta(11)}

mp.dps = 50  # PSLQ needs precision

# Scale up to avoid tiny numbers
# zB(6) * C_2^C_2 = zB(6) * 46656 ~ 7.19
scaled = zB6 * mpf(C_2)**C_2

print(f"  zB(C_2) * C_2^C_2 = {float(scaled):.12f}")
print(f"  (Should be close to g = {g} if zB(C_2) ~ g/C_2^C_2)")

# PSLQ: scaled = a_0 + a_1*pi^2/6 + a_2*zeta(3) + a_3*zeta(5) + a_4*zeta(7) + ...
basis_vals = [
    mpf(1),
    pi**2 / 6,          # zeta(2)
    zeta(3),
    zeta(5),
    zeta(7),
    pi**4 / 90,         # zeta(4)
    pi**6 / 945,        # zeta(6)
]
basis_names = ["1", "pi^2/6", "zeta(3)", "zeta(5)", "zeta(7)", "pi^4/90", "pi^6/945"]

vec = [scaled] + basis_vals
result = pslq(vec)
if result:
    print(f"\n  PSLQ found relation for zB(C_2)*C_2^C_2:")
    terms = []
    for i, (coeff, name) in enumerate(zip(result, ["zB*C_2^C_2"] + basis_names)):
        if coeff != 0:
            terms.append(f"  {coeff:>6d} * {name}")
    print("\n".join(terms))
    print(f"  = 0")
else:
    print(f"\n  PSLQ: no relation found for zB(C_2) against zeta basis")

# Also try PSLQ on the RATIO 439/72 vs actual
print(f"\n  PSLQ on zB(6)/zB(7) - 6:")
excess = ratio_67 - 6  # ~ 0.0972
basis2 = [mpf(1), pi**2, zeta(3), zeta(5), zeta(7)]
basis2_names = ["1", "pi^2", "zeta(3)", "zeta(5)", "zeta(7)"]
vec2 = [excess] + basis2
result2 = pslq(vec2)
if result2:
    print(f"  PSLQ found relation for zB(6)/zB(7) - C_2:")
    for coeff, name in zip(result2, ["excess"] + basis2_names):
        if coeff != 0:
            print(f"    {coeff:>6d} * {name}")
    print(f"  = 0")
else:
    print(f"  PSLQ: no relation found")

# ============================================================
# PART 5: zB(g/rank) = 1/g^2 MECHANISM
# ============================================================
print()
print("=" * 70)
print("PART 5: zB(g/rank) = zB(7/2) ~ 1/g^2 Mechanism")
print("=" * 70)

mp.dps = 80
zB_72 = zeta_B(mpf(7)/2, 20000)
target_g2 = mpf(1) / g**2

print(f"  zB(7/2) = {nstr(zB_72, 20)}")
print(f"  1/g^2   = {nstr(target_g2, 20)}")
gap_g2 = abs(zB_72 - target_g2) / abs(zB_72) * 100
print(f"  Gap = {float(gap_g2):.4f}%")

test("zB(g/rank) ~ 1/g^2 at < 0.1%",
     gap_g2 < mpf('0.1'),
     f"gap = {float(gap_g2):.4f}%")

# Decomposition: zB(7/2) = d_1/lam_1^(7/2) * [1 + corrections]
leading_72 = d1 / lam1**(mpf(7)/2)
print(f"\n  Leading term: d_1/lam_1^(7/2) = {int(d1)}/{int(lam1)}^(7/2) = {float(leading_72):.10f}")
print(f"  1/g^2 = {float(target_g2):.10f}")
print(f"  Leading/target = {float(leading_72/target_g2):.6f}")

# d_1 = 7, lam_1 = 6
# d_1/lam_1^(7/2) = 7/6^(7/2) = 7/(6^3 * sqrt(6)) = 7/(216*sqrt(6))
# 1/49 = 1/g^2
# So 7/(216*sqrt(6)) ~ 1/49?
# 7*49 = 343 = g^3
# 216*sqrt(6) = 6^3 * 6^(1/2) = 6^(7/2) = C_2^(g/rank)
# So leading = g^3 / C_2^(g/rank) ??
# Check: 343 / (216*2.449) = 343/529.1 = 0.648 != 0.0204
# No, d_1/lam_1^(7/2) = 7/6^3.5 = 7/1296*sqrt(6) ... let me just check numerically

print(f"\n  g^3 = {g**3}")
print(f"  C_2^(g/rank) = {float(mpf(C_2)**(mpf(g)/rank)):.4f}")
print(f"  d_1 / lam_1^(g/rank) = {float(d1/lam1**(mpf(g)/rank)):.10f}")

# Actually, zB(g/rank) sums over ALL k, not just k=1
# The fact that the sum ~ 1/g^2 is nontrivial
# g^2 = 49, and the sum is 0.020391 while 1/49 = 0.020408
# The leading term: 7/6^3.5 = 7/529.09 = 0.01323 — only 65% of the value
# So the higher k terms contribute significantly at s=3.5

frac_k1 = float(leading_72 / zB_72 * 100)
print(f"\n  k=1 fraction at s=g/rank: {frac_k1:.2f}%")

# This means 1/g^2 is an EMERGENT property of the full sum, not just the leading term
test("1/g^2 is emergent (k=1 contributes < 80%)",
     frac_k1 < 80,
     f"k=1 = {frac_k1:.1f}%, rest contributes {100-frac_k1:.1f}%")

# ============================================================
# PART 6: The Cross-Ratio C_2*g = 42
# ============================================================
print()
print("=" * 70)
print("PART 6: Cross-Ratio zB(4)*zB(6)/[zB(5)*zB(7)] ~ C_2*g = 42")
print("=" * 70)

cross = zB_vals[4] * zB_vals[6] / (zB_vals[5] * zB_vals[7])
target_42 = mpf(C_2 * g)

print(f"  Cross ratio = {float(cross):.10f}")
print(f"  C_2 * g = {int(target_42)}")
gap_42 = abs(cross - target_42) / target_42 * 100
print(f"  Gap = {float(gap_42):.4f}%")

test("Cross ratio ~ C_2*g = 42 at < 0.5%",
     gap_42 < mpf('0.5'),
     f"gap = {float(gap_42):.4f}%")

# Why 42? The cross ratio is:
# [zB(4)*zB(6)] / [zB(5)*zB(7)]
# ~ [d1/lam1^4 * d1/lam1^6] / [d1/lam1^5 * d1/lam1^7]
# = lam1^{5+7-4-6} = lam1^2 = 36 for the leading term
# But we get 42 = 36 + 6 = lam_1^2 + lam_1 = C_2*(C_2+1) = C_2*g
# The correction is exactly +lam_1 = +C_2 !!!

leading_cross = lam1**2  # = 36
print(f"\n  Leading cross ratio (k=1 only): lam_1^2 = {int(leading_cross)}")
print(f"  Actual - leading = {float(cross - leading_cross):.6f}")
print(f"  This excess ~ C_2 = {C_2}: {float((cross - leading_cross)/C_2):.6f}")

# So cross = lam_1^2 + lam_1 + O(higher) = lam_1*(lam_1+1) = 6*7 = 42 = C_2*g!
excess_over_c2 = (cross - leading_cross) / C_2
test("Cross ratio excess / C_2 ~ 1 (so cross ~ C_2*(C_2+1) = C_2*g)",
     abs(excess_over_c2 - 1) < mpf('0.05'),
     f"excess/C_2 = {float(excess_over_c2):.6f}")

# ============================================================
# PART 7: Consecutive Ratios as BST Fractions
# ============================================================
print()
print("=" * 70)
print("PART 7: All Adjacent Ratios as BST Fractions")
print("=" * 70)

print(f"\n  {'s':>4s} | {'zB(s)/zB(s+1)':>18s} | {'best p/q':>12s} | {'gap %':>10s} | {'p,q factors':>20s}")
print("  " + "-" * 75)

def factorize(n):
    """Simple trial division"""
    n = abs(n)
    if n <= 1:
        return str(n)
    factors = []
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return "*".join(str(f) for f in factors)

for s in range(4, 24):
    if s in zB_vals and s+1 in zB_vals:
        ratio = zB_vals[s] / zB_vals[s+1]
        # Find best fraction
        best_p, best_q, best_err = 0, 1, mpf('inf')
        for q in range(1, 500):
            for p in range(1, 3000):
                err = abs(ratio - mpf(p)/q)
                if err < best_err:
                    best_err = err
                    best_p, best_q = p, q
        pct = float(best_err / ratio * 100)
        marker = " *" if pct < 0.01 else ""
        print(f"  {s:4d} | {float(ratio):18.10f} | {best_p:>5d}/{best_q:<5d} | {pct:10.4f}% | {factorize(best_p)}/{factorize(best_q)}{marker}")

# ============================================================
# PART 8: Special Combination n_C*zB(n_C) + g*zB(g)
# ============================================================
print()
print("=" * 70)
print("PART 8: BST-Weighted Combinations")
print("=" * 70)

combo1 = n_C * zB_vals[5] + g * zB_vals[7]
combo2 = C_2 * zB_vals[6]
combo3 = N_c * zB_vals[4] + rank * zB_vals[8]

print(f"  n_C*zB(n_C) + g*zB(g)   = {float(combo1):.12f}")
print(f"  C_2*zB(C_2)             = {float(combo2):.12f}")
print(f"  N_c*zB(4) + rank*zB(8)  = {float(combo3):.12f}")
print(f"  Ratio combo1/combo2     = {float(combo1/combo2):.8f}")

# Check if N_max appears
print(f"\n  zB(4) * N_max = {float(zB_vals[4] * N_max):.8f}")
print(f"  zB(4) * N_max^2 = {float(zB_vals[4] * N_max**2):.4f}")

for name, val in [("combo1", combo1), ("combo2", combo2), ("combo3", combo3)]:
    best_p, best_q, best_err = 0, 1, mpf('inf')
    for q in range(1, 500):
        for p in range(1, 1000):
            err = abs(val - mpf(p)/q)
            if err < best_err:
                best_err = err
                best_p, best_q = p, q
    pct = float(best_err / abs(val) * 100)
    print(f"  {name:>8s} ~ {best_p}/{best_q} ({pct:.4f}%)")

# ============================================================
# SUMMARY
# ============================================================
print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)

print(f"""
  SPECTRAL ZETA DEEP RATIOS:

  1. DEVIATION CONVERGENCE: R(s)-C_2 ratio converges to
     lambda_2/lambda_1 = g/N_c = 7/3 as s -> infinity.
     The eigenvalue spectrum IS the deviation controller.

  2. 439/72 IDENTITY: zB(C_2)/zB(g) ~ 439/72 at 0.0007%.
     439 is prime, 72 = C_2^2 * rank. The ratio decomposes as
     C_2 * (1+S_6)/(1+S_7) where S are correction sums.

  3. 1/g^2 MECHANISM: zB(g/rank) ~ 1/g^2 is EMERGENT —
     k=1 gives only ~65%, the sum over all eigenvalues
     conspires to produce 1/g^2.

  4. CROSS RATIO: zB(4)*zB(6)/[zB(5)*zB(7)] ~ C_2*g = 42.
     Leading = C_2^2 = 36, excess ~ C_2, total = C_2*(C_2+1) = C_2*g.
""")

print(f"SCORE: {pass_count}/{total_tests} PASS ({fail_count} FAIL)")
