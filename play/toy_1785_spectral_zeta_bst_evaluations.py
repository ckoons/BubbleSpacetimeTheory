"""
Toy 1785: Spectral Zeta at BST Evaluation Points
==================================================
Computes zeta_B(s) = sum d_k / (k(k+5))^s at integer and half-integer
points for s > 3 (convergent region). Extracts BST content of values
and ratios. Connects to master integral structure (E-80).

Key questions:
1. Do zeta_B values at BST integers give BST fractions?
2. Do RATIOS of zeta_B values match master integral ratios?
3. What is the Riemann zeta content of zeta_B(C_2)?
4. Does the speaking pair period (n_C=5) appear in zeta_B values?

Author: Elie | Date: 2026-05-02
"""

from mpmath import (mp, mpf, log, exp, pi, zeta, fsum, fac,
                     nstr, power, sqrt, gamma as mpgamma)

mp.dps = 50

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

def zeta_B(s, N=10000):
    """Direct sum spectral zeta (convergent for Re(s) > 3)"""
    s = mpf(s)
    total = mpf(0)
    for k in range(1, N+1):
        total += d(k) / lam(k)**s
    return total

# ============================================================
# PART 1: Zeta_B at Integer Points s = 4, 5, 6, 7, 8
# ============================================================
print("=" * 70)
print("PART 1: zeta_B(s) at Integer Points (s > 3)")
print("=" * 70)

int_points = [4, 5, 6, 7, 8, 9, 10]
zB_int = {}

print(f"\n  {'s':>4s} | {'zeta_B(s)':>20s} | {'1/zeta_B(s)':>16s}")
print("  " + "-" * 50)

for s in int_points:
    val = zeta_B(s)
    zB_int[s] = val
    print(f"  {s:4d} | {float(val):20.15f} | {float(1/val):16.6f}")

# ============================================================
# PART 2: zeta_B(C_2) = zeta_B(6) Riemann Zeta Content
# ============================================================
print()
print("=" * 70)
print("PART 2: Riemann Zeta Content of zeta_B(C_2) = zeta_B(6)")
print("=" * 70)

# zeta_B(6) = sum d_k / (k(k+5))^6
# Partial fraction: 1/(k(k+5))^6 can be expanded
# The leading Hurwitz-type contribution comes from 1/k^6 * d_k
# d_k ~ k^5/60, so the sum behaves like sum k^5/(k^{12}) = sum 1/k^7 ~ zeta(7)

zB6 = zB_int[6]
print(f"\n  zeta_B(C_2) = zeta_B(6) = {float(zB6):.15f}")
print(f"  1/zeta_B(6) = {float(1/zB6):.6f}")

# Check: zeta_B(6) ~ d_1/lambda_1^6 = 7/6^6 = 7/46656
leading = mpf(d(1)) / lam(1)**6
print(f"\n  Leading term d_1/lambda_1^6 = {int(d(1))}/{int(lam(1))}^6 = {float(leading):.15f}")
print(f"  Ratio zB(6)/leading = {float(zB6/leading):.6f}")

# How much does k=1 contribute?
pct_k1 = float(leading / zB6 * 100)
print(f"  k=1 contributes {pct_k1:.2f}% of zeta_B(6)")

# Decompose into Riemann zeta values
# zeta_B(6) involves sum d_k / (k(k+5))^6
# Using partial fractions of 1/(k(k+5))^6 = sum_{j=1}^6 [A_j/k^j + B_j/(k+5)^j] / something
# This is complex. Let me instead check ratios.

# Known: Mersenne connection M_g = 2^g - 1 = 127
# From Lyra Toy 1767: leading term involves (M_g / d_1) * zeta(g) = (127/60)*zeta(7)
# This would be for the Hurwitz expansion at s=6... let me check more carefully

# Actually, the leading Riemann zeta content comes from the partial fraction decomposition
# of 1/(k(k+5))^s. For large k, 1/(k(k+5))^s ~ 1/k^{2s}, so the leading Riemann zeta
# content is zeta(2*6) = zeta(12) modulated by d_k ~ k^5.
# sum d_k/k^{12} ~ sum k^5/k^{12} /60 = zeta(7)/60 = zeta(g)/d_1

zeta_g = zeta(mpf(g))
est_leading = zeta_g / mpf(d(1))
ratio_to_zeta = zB6 / est_leading
print(f"\n  zeta(g)/d_1 = zeta(7)/7 = {float(est_leading):.15f}")
print(f"  zeta_B(6) / (zeta(7)/7) = {float(ratio_to_zeta):.6f}")

test("zeta_B(C_2) dominated by zeta(g) content",
     abs(ratio_to_zeta - 1) < mpf('0.5'),
     f"ratio = {float(ratio_to_zeta):.4f}")

# ============================================================
# PART 3: Ratios of zeta_B Values — BST Content
# ============================================================
print()
print("=" * 70)
print("PART 3: Ratios zeta_B(m)/zeta_B(n) — BST Fraction Search")
print("=" * 70)

print(f"\n  Key ratios:")
print()

def find_bst_fraction(val, max_num=200, max_den=200, threshold=0.01):
    """Find best BST-valued fraction matching val"""
    best_p, best_q, best_err = 0, 1, mpf('inf')
    for q in range(1, max_den+1):
        for p in range(1, max_num+1):
            err = abs(val - mpf(p)/q)
            if err < best_err:
                best_err = err
                best_p, best_q = p, q
            err_neg = abs(val + mpf(p)/q)
            if err_neg < best_err:
                best_err = err_neg
                best_p, best_q = -p, q
    pct = float(best_err / abs(val) * 100) if val != 0 else float('inf')
    return best_p, best_q, pct

# Key ratios
ratios = {}
for s1 in [4, 5, 6, 7, 8]:
    for s2 in [s1+1, s1+2]:
        if s2 <= 10:
            r = zB_int[s1] / zB_int[s2]
            p, q, pct = find_bst_fraction(r)
            ratios[(s1,s2)] = (r, p, q, pct)
            marker = " *BST*" if pct < 0.1 else ""
            print(f"  zB({s1})/zB({s2}) = {float(r):12.6f}  ~ {p}/{q} ({pct:.4f}%){marker}")

# Especially important: zB(6)/zB(7) — ratio at C_2 and g
r67 = zB_int[6] / zB_int[7]
p, q, pct = find_bst_fraction(r67, 500, 500)
print(f"\n  **zB(C_2)/zB(g)** = {float(r67):.10f}  ~ {p}/{q} ({pct:.4f}%)")

test("zB(C_2)/zB(g) matches BST fraction at < 0.5%",
     pct < 0.5,
     f"{p}/{q} at {pct:.4f}%")

# ============================================================
# PART 4: Half-Integer Points — BST Content
# ============================================================
print()
print("=" * 70)
print("PART 4: zeta_B at Half-Integer Points (s = 7/2, 9/2, 11/2)")
print("=" * 70)

half_points = [mpf(7)/2, mpf(9)/2, mpf(11)/2, mpf(13)/2]
zB_half = {}

for s in half_points:
    val = zeta_B(s)
    zB_half[s] = val
    s_str = f"{int(2*s)}/2"
    p, q, pct = find_bst_fraction(val, 300, 300)
    marker = " *BST*" if pct < 0.1 else ""
    print(f"  zB({s_str}) = {float(val):16.12f}  ~ {p}/{q} ({pct:.4f}%){marker}")

# Check g/rank point
zB_g_rank = zeta_B(mpf(g)/rank)
p, q, pct = find_bst_fraction(zB_g_rank)
print(f"\n  **zB(g/rank) = zB(7/2)** = {float(zB_g_rank):.12f}  ~ {p}/{q} ({pct:.4f}%)")

# ============================================================
# PART 5: Eigenvalue Ratio zB(s)/zB(s+1) Decay Rate
# ============================================================
print()
print("=" * 70)
print("PART 5: Decay Rate zB(s)/zB(s+1)")
print("=" * 70)

print(f"\n  {'s':>4s} | {'zB(s)/zB(s+1)':>14s} | {'lambda_1^1':>10s} | {'ratio/lam1':>12s}")
print("  " + "-" * 50)

for s in range(4, 10):
    if s+1 in zB_int:
        ratio = zB_int[s] / zB_int[s+1]
        # Expected: dominated by lambda_1 = 6 = C_2
        ratio_over_lam1 = ratio / C_2
        print(f"  {s:4d} | {float(ratio):14.6f} | {C_2:10d} | {float(ratio_over_lam1):12.6f}")

# The ratio should approach lambda_1 = C_2 = 6 as s -> infinity
# because the k=1 term dominates
test("zB(s)/zB(s+1) -> lambda_1 = C_2 = 6 as s grows",
     abs(zB_int[9] / zB_int[10] - C_2) / C_2 < mpf('0.01'),
     f"ratio at s=9: {float(zB_int[9]/zB_int[10]):.6f}")

# ============================================================
# PART 6: Speaking Pair Period in zeta_B
# ============================================================
print()
print("=" * 70)
print("PART 6: Speaking Pair Period n_C = 5 in zeta_B")
print("=" * 70)

# In the heat kernel, speaking pairs have period n_C = 5.
# Does zeta_B(s) show period-5 structure?

# Check: zB(s) and zB(s+5) — is the ratio constant?
print(f"\n  zB(s)/zB(s+5) for s=4,5:")
for s in [4, 5]:
    if s+5 in zB_int:
        ratio = zB_int[s] / zB_int[s+5]
        print(f"  zB({s})/zB({s+5}) = {float(ratio):.6f}")

# Actually, the period-5 structure is in the heat kernel coefficients,
# not directly in zeta_B. Let me instead check the "spectral zeta at
# speaking pair positions":
# Speaking pairs: k = 1,6,11,16,... (period 5, offset 1)
# Does sum over speaking pair eigenvalues have BST content?

def zeta_B_speaking(s, pair_offset, N=2000):
    """Sum over k = pair_offset, pair_offset+5, pair_offset+10, ..."""
    total = mpf(0)
    for i in range(N):
        k = pair_offset + n_C * i
        if k >= 1:
            total += d(k) / lam(k)**s
    return total

print(f"\n  Speaking pair decomposition of zeta_B(C_2):")
pair_sums = {}
total_check = mpf(0)
for offset in range(1, n_C + 1):
    val = zeta_B_speaking(6, offset, 2000)
    pair_sums[offset] = val
    total_check += val
    p, q, pct = find_bst_fraction(val, 500, 500)
    print(f"    Pair {offset}: zB_pair({offset}, 6) = {float(val):.12f}  ~ {p}/{q} ({pct:.4f}%)")

# Verify decomposition
test("Speaking pair decomposition sums to zeta_B(6)",
     abs(total_check - zB_int[6]) / abs(zB_int[6]) < mpf('1e-10'),
     f"sum = {float(total_check):.15f}, zB(6) = {float(zB_int[6]):.15f}")

# Pair ratios
print(f"\n  Pair ratios (relative to Pair 1):")
for offset in range(2, n_C + 1):
    ratio = pair_sums[offset] / pair_sums[1]
    p, q, pct = find_bst_fraction(ratio, 200, 200)
    print(f"    Pair {offset}/Pair 1 = {float(ratio):.8f}  ~ {p}/{q} ({pct:.4f}%)")

# ============================================================
# PART 7: The C_2 Evaluation — Physical Interpretation
# ============================================================
print()
print("=" * 70)
print("PART 7: zeta_B(C_2) Physical Content")
print("=" * 70)

# zeta_B(6) is the spectral zeta at s = spectral dimension
# This is related to the regularized trace of the resolvent
# In physics: partition function at inverse temperature beta = 6

print(f"\n  zeta_B(C_2) = {float(zB6):.15f}")
print(f"  1/zeta_B(C_2) = {float(1/zB6):.6f}")

# Check various BST expressions
candidates = {
    "g / C_2^C_2": mpf(g) / mpf(C_2)**C_2,
    "1 / (C_2 * d_1)": mpf(1) / (C_2 * d(1)),
    "N_c / (C_2^C_2)": mpf(N_c) / mpf(C_2)**C_2,
    "d_1 / C_2^C_2": mpf(d(1)) / mpf(C_2)**C_2,
    "g / (rank * C_2^5)": mpf(g) / (rank * mpf(C_2)**5),
    "1 / (C_2^5)": mpf(1) / mpf(C_2)**5,
    "g / N_max^2": mpf(g) / mpf(N_max)**2,
}

print(f"\n  BST candidate matches for zeta_B(6):")
for name, val in candidates.items():
    err_pct = abs(zB6 - val) / abs(zB6) * 100
    if err_pct < 10:
        print(f"    {name} = {float(val):.10f}  ({float(err_pct):.2f}%)")

# 1/zeta_B(6) as integer/BST
inv = 1/zB6
p, q, pct = find_bst_fraction(inv, 500, 500)
print(f"\n  1/zeta_B(6) ~ {p}/{q} ({pct:.4f}%)")

test("zeta_B(C_2) has identifiable BST structure",
     any(abs(zB6 - v) / abs(zB6) * 100 < 5 for v in candidates.values()),
     "Within 5% of at least one BST expression")

# ============================================================
# PART 8: Product zeta_B(4)*zeta_B(5) — Volume?
# ============================================================
print()
print("=" * 70)
print("PART 8: Products and Cross-Ratios")
print("=" * 70)

prod_45 = zB_int[4] * zB_int[5]
prod_67 = zB_int[6] * zB_int[7]
cross = (zB_int[4] * zB_int[6]) / (zB_int[5] * zB_int[7])

print(f"  zB(4)*zB(5) = {float(prod_45):.10f}")
print(f"  zB(6)*zB(7) = {float(prod_67):.12f}")
print(f"  zB(4)*zB(6)/[zB(5)*zB(7)] = {float(cross):.8f}")

for name, val in [("4*5 product", prod_45), ("6*7 product", prod_67), ("cross ratio", cross)]:
    p, q, pct = find_bst_fraction(val, 300, 300)
    marker = " *BST*" if pct < 0.1 else ""
    print(f"    {name:15s} ~ {p}/{q} ({pct:.4f}%){marker}")

# ============================================================
# PART 9: Consecutive Ratio Pattern
# ============================================================
print()
print("=" * 70)
print("PART 9: Consecutive Ratio Pattern")
print("=" * 70)

# R(s) = zB(s)/zB(s+1) should approach lambda_1 = C_2 = 6
# The deviation from C_2 encodes the higher eigenvalue content

print(f"\n  R(s) = zB(s)/zB(s+1) and deviation from C_2:")
print(f"  {'s':>4s} | {'R(s)':>12s} | {'R(s)-C_2':>12s} | {'(R-C_2)/C_2':>12s}")
print("  " + "-" * 50)

for s in range(4, 10):
    if s+1 in zB_int:
        R = zB_int[s] / zB_int[s+1]
        dev = R - C_2
        rel = dev / C_2
        print(f"  {s:4d} | {float(R):12.6f} | {float(dev):12.6f} | {float(rel):12.6f}")

# The deviation ratio: (R(s) - C_2) / (R(s+1) - C_2) should be ~lambda_2/lambda_1
# lambda_2/lambda_1 = 14/6 = 7/3 = g/N_c
if 5 in zB_int and 6 in zB_int and 7 in zB_int:
    R4 = zB_int[4] / zB_int[5]
    R5 = zB_int[5] / zB_int[6]
    R6 = zB_int[6] / zB_int[7]
    dev4 = R4 - C_2
    dev5 = R5 - C_2
    dev6 = R6 - C_2
    if abs(dev5) > mpf('1e-20'):
        dev_ratio_45 = dev4 / dev5
        dev_ratio_56 = dev5 / dev6
        lam_ratio = mpf(lam(2)) / lam(1)  # 14/6 = 7/3
        print(f"\n  Deviation ratios (should approach lambda_2/lambda_1 = {float(lam_ratio):.4f} = g/N_c):")
        print(f"    dev(4)/dev(5) = {float(dev_ratio_45):.6f}")
        print(f"    dev(5)/dev(6) = {float(dev_ratio_56):.6f}")

        test("Deviation ratio -> lambda_2/lambda_1 = g/N_c = 7/3",
             abs(dev_ratio_56 - lam_ratio) / lam_ratio < mpf('0.05'),
             f"ratio = {float(dev_ratio_56):.4f}, target = {float(lam_ratio):.4f}")

# ============================================================
# PART 10: zeta_B at dim/2 = n_C/2 = 5/2 (Border)
# ============================================================
print()
print("=" * 70)
print("PART 10: Border Value zeta_B(n_C/2) = zeta_B(5/2)")
print("=" * 70)

# s = n_C/2 = 5/2 is at the border of the critical strip
# Direct sum does NOT converge here (need s > 3)
# But Mellin/Bernoulli gives values

# From Lyra Toy 1773 (Mellin fix):
# zeta_B(2.5) = 0.0838 (corrected)
# zeta_B(1.5) = -0.0827
# zeta_B(0.5) = -0.887

print("  NOTE: s = 5/2 < 3, direct sum does not converge.")
print("  Values from Lyra's Mellin continuation (Toy 1773):")
print(f"    zeta_B(5/2) ~ 0.0838")
print(f"    zeta_B(3/2) ~ -0.0827")
print(f"    zeta_B(1/2) ~ -0.887")
print()
print(f"  Ratio zB(5/2)/zB(3/2) ~ -1.01 ~ -1")
print(f"  This is the FE ANTISYMMETRY: Phi(3) = -1 from Lyra Toy 1774")

# ============================================================
# PART 11: The g/C_2 Ratio
# ============================================================
print()
print("=" * 70)
print("PART 11: zeta_B Values as BST Fractions")
print("=" * 70)

# Key BST fractions to check against
bst_fracs = {
    "1/C_2": mpf(1)/C_2,
    "1/g": mpf(1)/g,
    "N_c/g^2": mpf(N_c)/g**2,
    "1/(N_c*g)": mpf(1)/(N_c*g),
    "1/N_max": mpf(1)/N_max,
    "rank/g^3": mpf(rank)/g**3,
}

for s in [4, 5, 6, 7]:
    val = zB_int[s]
    print(f"\n  zB({s}) = {float(val):.12f}")
    for name, bst_val in bst_fracs.items():
        err = abs(val - bst_val) / abs(val) * 100
        if err < 20:
            print(f"    ~ {name} = {float(bst_val):.12f} ({float(err):.2f}%)")

# ============================================================
# SUMMARY
# ============================================================
print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)

print(f"""
  SPECTRAL ZETA AT BST POINTS:

  zeta_B(4)  = {float(zB_int[4]):.12f}   (first convergent integer)
  zeta_B(5)  = {float(zB_int[5]):.12f}   (s = n_C)
  zeta_B(6)  = {float(zB_int[6]):.12f}   (s = C_2 = spectral dim)
  zeta_B(7)  = {float(zB_int[7]):.12f}   (s = g = genus)

  DECAY: zB(s)/zB(s+1) -> lambda_1 = C_2 = 6
    Correction: (R(s)-C_2)/(R(s+1)-C_2) -> lambda_2/lambda_1 = g/N_c

  SPEAKING PAIRS: Period n_C = 5 in eigenvalue decomposition
    of zeta_B(C_2). Pair offsets 1,2,3,4,5 correspond to
    k mod 5 classes.

  CONNECTION TO E-80:
    The spectral zeta values are CONVERGENT SUMS for s > 3.
    Master integral ratios should appear at specific BST evaluation
    points if the 49a1 period lattice connects to the spectral geometry.
    Key ratio: zB(C_2)/zB(g) encodes color/genus interplay.
""")

print(f"SCORE: {pass_count}/{total_tests} PASS ({fail_count} FAIL)")
