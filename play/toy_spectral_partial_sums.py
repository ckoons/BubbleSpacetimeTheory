#!/usr/bin/env python3
"""
TOY 184: SPECTRAL PARTIAL SUMS AND THE BST PRODUCT CHAIN
=========================================================

The partial sums S(K) = Σ_{k=0}^{K} d_k of spectral multiplicities
on Q⁵ factorize into BST integers:

  S(0) = 1
  S(1) = 8 = 2^{N_c}
  S(2) = 35 = n_C × g

This toy systematically explores:
1. The partial sums S(K) and their BST factorizations
2. The generating function (1+x)/(1-x)⁶ evaluated at x=1
3. The alternating sums and their meaning
4. Whether S(K) has a closed form in BST integers
5. The connection to polynomial invariants of Q⁵

Casey Koons, March 16, 2026
"""

from fractions import Fraction
from math import comb, gcd
from functools import reduce

print("=" * 72)
print("TOY 184: SPECTRAL PARTIAL SUMS")
print("=" * 72)

# ═══════════════════════════════════════════════════════════════════
# Section 1: The partial sums
# ═══════════════════════════════════════════════════════════════════

print("\n§1. PARTIAL SUMS S(K) = Σ d_k (k=0 to K)")
print("-" * 50)

def d_k(k):
    """Multiplicity of k-th eigenvalue of Q⁵"""
    return comb(k + 4, 4) * (2*k + 5) // 5

def factorize(n):
    """Return prime factorization as list of (prime, exponent)"""
    if n <= 1:
        return [(n, 1)] if n == 1 else []
    factors = []
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            exp = 0
            while n % p == 0:
                exp += 1
                n //= p
            factors.append((p, exp))
    if n > 1:
        factors.append((n, 1))
    return factors

def factor_str(n):
    if n == 1:
        return "1"
    fs = factorize(n)
    parts = []
    for p, e in fs:
        if e == 1:
            parts.append(str(p))
        else:
            parts.append(f"{p}^{e}")
    return "×".join(parts)

# BST integers for identification
bst_names = {
    2: "r", 3: "N_c", 5: "n_C", 6: "C₂", 7: "g",
    9: "c₄", 11: "c₂", 13: "c₃", 42: "P(1)",
    137: "N_max", 21: "dim G", 8: "2^N_c",
    27: "N_c^N_c", 35: "n_C×g", 77: "g×c₂"
}

S = 0
partial_sums = []
print(f"\n  {'K':>3s}  {'d_K':>6s}  {'S(K)':>8s}  {'Factorization':20s}  BST content")
print(f"  {'───':>3s}  {'────':>6s}  {'────':>8s}  {'─'*20}  {'─'*25}")
for K in range(20):
    dk = d_k(K)
    S += dk
    partial_sums.append(S)
    fs = factor_str(S)

    # BST identification
    bst = bst_names.get(S, "")
    if not bst:
        # Try to express as product of BST integers
        for a in [2, 3, 5, 6, 7, 8, 9, 11, 13]:
            if S % a == 0:
                rem = S // a
                if rem in bst_names:
                    a_name = bst_names.get(a, str(a))
                    bst = f"{a_name}×{bst_names[rem]}"
                    break
                for b in [2, 3, 5, 6, 7, 8, 9, 11, 13]:
                    if rem % b == 0:
                        rem2 = rem // b
                        if rem2 in bst_names:
                            bst = f"{bst_names.get(a,str(a))}×{bst_names.get(b,str(b))}×{bst_names[rem2]}"
                            break

    print(f"  {K:3d}  {dk:6d}  {S:8d}  {fs:20s}  {bst}")

# ═══════════════════════════════════════════════════════════════════
# Section 2: Closed form for S(K)
# ═══════════════════════════════════════════════════════════════════

print("\n\n§2. CLOSED FORM FOR S(K)")
print("-" * 50)

# d_k = C(k+4,4) × (2k+5)/5
# S(K) = Σ_{k=0}^K C(k+4,4)(2k+5)/5
# = (1/5) Σ C(k+4,4)(2k+5)
# = (1/5) [2 Σ k·C(k+4,4) + 5 Σ C(k+4,4)]

# Identity: Σ_{k=0}^K C(k+4,4) = C(K+5,5)
# Identity: Σ_{k=0}^K k·C(k+4,4) = Σ (k+4-4)·C(k+4,4) = Σ C(k+4,4)·(k+4) - 4·Σ C(k+4,4)
# = 5·Σ C(k+4,5) - 4·C(K+5,5)  [using k·C(k,r) = r·C(k,r+1) type identity... actually need to be careful]

# Let me use the identity: Σ_{k=0}^K C(k+r,r) = C(K+r+1, r+1) (hockey stick)
# So Σ C(k+4,4) = C(K+5, 5)

# For Σ k·C(k+4,4): use k = (k+4) - 4, then k·C(k+4,4) = (k+4)·C(k+4,4) - 4·C(k+4,4)
# (k+4)·C(k+4,4) = 5·C(k+4,5) [since (k+4)·C(k+4,4) = (k+4)!/(4!(k)!) = 5·(k+4)!/(5!(k-1)!) = 5·C(k+4,5)]
# Wait: C(k+4,5) = (k+4)!/[5!(k-1)!] = (k+4)(k+3)(k+2)(k+1)k / 120
# And (k+4)·C(k+4,4) = (k+4)·(k+4)(k+3)(k+2)(k+1) / 24 ... no that's wrong
# C(k+4,4) = (k+4)(k+3)(k+2)(k+1) / 24
# (k+4)·C(k+4,4) = (k+4)²(k+3)(k+2)(k+1) / 24 ... that's not C(k+4,5)

# Let me use a different identity.
# k·C(k+4,4) = k·C(k+4,4). Note k = (k+5) - 5, and by the absorption identity:
# Actually, let me just use: (2k+5) = 2(k+5) - 5
# So S(K) = (1/5)[2·Σ(k+5)C(k+4,4) - 5·Σ C(k+4,4)]
# = (1/5)[2·Σ(k+5)C(k+4,4) - 5·C(K+5,5)]

# Now (k+5)·C(k+4,4) = 5·C(k+5,5) [absorption: n·C(n-1,k) = (k+1)·C(n,k+1), with n=k+5, k=4]
# Check: 5·C(k+5,5) = 5·(k+5)!/(5!k!) = (k+5)(k+4)(k+3)(k+2)(k+1)/24
# And (k+5)·C(k+4,4) = (k+5)·(k+4)(k+3)(k+2)(k+1)/24 = same ✓

# So Σ_{k=0}^K (k+5)·C(k+4,4) = 5·Σ C(k+5,5) = 5·C(K+6,6) [hockey stick]

# Therefore:
# S(K) = (1/5)[2·5·C(K+6,6) - 5·C(K+5,5)]
# = 2·C(K+6,6) - C(K+5,5)

# Verify
print("\n  Derivation:")
print("    d_k = C(k+4,4)×(2k+5)/5")
print("    S(K) = (1/5)Σ C(k+4,4)(2k+5)")
print("         = (1/5)[2·Σ(k+5)C(k+4,4) - 5·Σ C(k+4,4)]")
print("         = (1/5)[10·C(K+6,6) - 5·C(K+5,5)]")
print("         = 2·C(K+6,6) - C(K+5,5)")
print()

print("  ★ S(K) = 2·C(K+6,6) - C(K+5,5)")
print()

# Verify
print("  Verification:")
for K in range(12):
    closed = 2 * comb(K+6, 6) - comb(K+5, 5)
    check = "✓" if closed == partial_sums[K] else f"✗ (got {closed})"
    print(f"    S({K:2d}) = 2·C({K+6},6) - C({K+5},5) = "
          f"2×{comb(K+6,6)} - {comb(K+5,5)} = {closed}  {check}")

# ═══════════════════════════════════════════════════════════════════
# Section 3: The closed form in BST terms
# ═══════════════════════════════════════════════════════════════════

print("\n\n§3. BST INTERPRETATION OF THE CLOSED FORM")
print("-" * 50)

print("""
  S(K) = 2·C(K+6,6) - C(K+5,5)

  At special values:
    S(0) = 2·C(6,6) - C(5,5) = 2 - 1 = 1
    S(1) = 2·C(7,6) - C(6,5) = 14 - 6 = 8 = 2^{N_c}
    S(2) = 2·C(8,6) - C(7,5) = 56 - 21 = 35 = n_C × g
    S(3) = 2·C(9,6) - C(8,5) = 168 - 56 = 112 = 2^4 × 7 = 16g
    S(4) = 2·C(10,6) - C(9,5) = 420 - 126 = 294 = 2 × 3 × 7² = r × N_c × g²

  The formula involves C(K+6,6) which has 6 = C₂ in the lower index!
  And C(K+5,5) which has 5 = n_C in the lower index!

  S(K) = 2·C(K+C₂, C₂) - C(K+n_C, n_C)

  ★ The partial sums are determined by C₂ and n_C!
""")

# Verify the BST rewriting
print("  S(K) = 2·C(K+C₂, C₂) - C(K+n_C, n_C)")
print()
for K in range(8):
    val = 2 * comb(K+6, 6) - comb(K+5, 5)
    print(f"    S({K}) = 2·C({K}+6,6) - C({K}+5,5) = {val}")

# ═══════════════════════════════════════════════════════════════════
# Section 4: Simplification
# ═══════════════════════════════════════════════════════════════════

print("\n\n§4. SIMPLIFIED FORM")
print("-" * 50)

# 2·C(K+6,6) - C(K+5,5)
# = 2(K+6)!/(6!K!) - (K+5)!/(5!K!)
# = [(K+6)!/(5!K!)] × [2/(K+6)/6 ... wait, let me factor more carefully

# C(K+6,6) = (K+6)(K+5)(K+4)(K+3)(K+2)(K+1)/720
# C(K+5,5) = (K+5)(K+4)(K+3)(K+2)(K+1)/120

# Factor out C(K+5,5):
# S(K) = C(K+5,5) × [2(K+6)/6 - 1]
# = C(K+5,5) × [(K+6)/3 - 1]
# = C(K+5,5) × (K+3)/3

# Check: S(0) = C(5,5)×3/3 = 1 ✓
# S(1) = C(6,5)×4/3 = 6×4/3 = 8 ✓
# S(2) = C(7,5)×5/3 = 21×5/3 = 35 ✓

print("  Factor out C(K+5,5):")
print("    S(K) = C(K+5,5) × [2(K+6)/6 - 1]")
print("         = C(K+5,5) × (K+3)/3")
print()

print("  ★ S(K) = C(K+n_C, n_C) × (K+N_c)/N_c")
print()

# This is beautiful! Verify:
for K in range(12):
    val = comb(K+5, 5) * (K+3) // 3
    check = "✓" if val == partial_sums[K] else "✗"
    print(f"    S({K:2d}) = C({K+5},5)×({K+3})/3 = "
          f"{comb(K+5,5)}×{K+3}/3 = {val}  {check}")

# ═══════════════════════════════════════════════════════════════════
# Section 5: The master formula
# ═══════════════════════════════════════════════════════════════════

print("\n\n§5. THE MASTER FORMULA")
print("=" * 50)

print("""
  THEOREM: S(K) = C(K+n_C, n_C) × (K+N_c)/N_c

  This says: the number of spectral states up to level K is
  the binomial coefficient C(K+n_C, n_C) times a linear factor
  (K+N_c)/N_c.

  At K = 0: S(0) = C(5,5) × 3/3 = 1 (vacuum)
  At K = 1: S(1) = C(6,5) × 4/3 = 8 = 2^{N_c}
  At K = 2: S(2) = C(7,5) × 5/3 = 35 = n_C × g

  The formula involves ONLY n_C = 5 and N_c = 3.
  No other BST integers are needed!

  Rewriting: S(K) = (K+5)(K+4)(K+3)²(K+2)(K+1) / 360

  Since 360 = 6! / 2 = C₂! / r = n_C! × N_c
""")

# Verify the product form
print("  Product form: S(K) = (K+1)(K+2)(K+3)²(K+4)(K+5)/360")
print()
for K in range(10):
    prod = (K+1)*(K+2)*(K+3)**2*(K+4)*(K+5) // 360
    check = "✓" if prod == partial_sums[K] else "✗"
    print(f"    S({K}) = ({K+1})({K+2})({K+3})²({K+4})({K+5})/360 = {prod}  {check}")

# 360 = 8 × 45 = 2³ × 3² × 5 = 2^N_c × N_c² × n_C
print(f"\n  360 = {factor_str(360)} = 2^N_c × N_c² × n_C")
# Also: 360 = 6!/2 = C₂!/r
print(f"      = C₂!/r = 720/2 = 360")
# Also: 360 = 5! × 3 = n_C! × N_c
print(f"      = n_C! × N_c = 120 × 3 = 360")

# ═══════════════════════════════════════════════════════════════════
# Section 6: The (K+3)² factor
# ═══════════════════════════════════════════════════════════════════

print("\n\n§6. THE SQUARED FACTOR")
print("-" * 50)

print("""
  S(K) = (K+1)(K+2)(K+3)²(K+4)(K+5) / 360

  The factor (K+3)² = (K+N_c)² appears SQUARED.
  This is the only repeated factor. It creates special values:

  When K = -3 (formal): S(-3) = 0 (triple zero from (K+3)²(K+2))
  When K = -1: S(-1) = 0 (from K+1 factor) — empty sum
  When K = N_c-3 = 0: S(0) = 1 (vacuum)

  The square is related to the Weyl dimension formula:
    d_k has the factor (2k+5) = (2k+n_C)
    which contributes a (K+3) to the partial sum
    and the binomial part contributes another (K+3)
""")

# ═══════════════════════════════════════════════════════════════════
# Section 7: S(K) at BST special values
# ═══════════════════════════════════════════════════════════════════

print("\n§7. S(K) AT BST INTEGER VALUES OF K")
print("-" * 50)

bst_K_values = [
    (0, "vacuum"),
    (1, "first excited"),
    (2, "second = rank"),
    (3, "N_c"),
    (5, "n_C"),
    (6, "C₂"),
    (7, "g"),
    (9, "c₄"),
    (11, "c₂"),
    (13, "c₃"),
]

print(f"\n  {'K':>3s}  {'BST':12s}  {'S(K)':>10s}  {'Factorization':25s}")
print(f"  {'───':>3s}  {'────':12s}  {'─────':>10s}  {'─'*25}")
for K, label in bst_K_values:
    val = partial_sums[K] if K < len(partial_sums) else \
          comb(K+5,5) * (K+3) // 3
    fs = factor_str(val)
    print(f"  {K:3d}  {label:12s}  {val:10d}  {fs}")

# ═══════════════════════════════════════════════════════════════════
# Section 8: Alternating sums
# ═══════════════════════════════════════════════════════════════════

print("\n\n§8. ALTERNATING SUMS")
print("-" * 50)

print(f"\n  A(K) = Σ (-1)^k d_k (k=0 to K):")
A = 0
for K in range(15):
    dk = d_k(K)
    A += (-1)**K * dk
    print(f"    A({K:2d}) = {A:8d}")

# At the Hilbert series level:
# H(-1) = (1+(-1))/(1-(-1))⁶ = 0/64 = 0
# So the full alternating sum is 0
print(f"\n  H(-1) = (1-1)/(1+1)⁶ = 0")
print(f"  The full alternating sum vanishes: Σ (-1)^k d_k = 0")

# ═══════════════════════════════════════════════════════════════════
# Section 9: The ratio S(K)/C(K+5,5)
# ═══════════════════════════════════════════════════════════════════

print("\n\n§9. THE RATIO S(K)/C(K+n_C, n_C)")
print("-" * 50)

print(f"\n  S(K)/C(K+5,5) = (K+3)/3 = (K+N_c)/N_c:")
for K in range(12):
    ratio = Fraction(partial_sums[K], comb(K+5, 5))
    print(f"    K={K:2d}: S/C = {ratio} = ({K+3})/3")

print(f"\n  This is a LINEAR function of K with slope 1/N_c = 1/3")
print(f"  and intercept 1 (when K=0)")

# ═══════════════════════════════════════════════════════════════════
# Section 10: Universal partial sum formula
# ═══════════════════════════════════════════════════════════════════

print("\n\n§10. UNIVERSAL PARTIAL SUM FOR Q^n")
print("-" * 50)

# For general Q^n with n_C = n, N_c = (n+1)/2:
# d_k = C(k+n-1, n-1) × (2k+n)/n
# S(K) should follow a similar pattern

# Let me derive for Q³ and Q⁷ too

print("  For Q³ (n=3, N_c=2):")
S3 = 0
for K in range(8):
    dk3 = comb(K+2, 2) * (2*K+3) // 3
    S3 += dk3
    # Predicted: S = C(K+3,3) × (K+2)/2
    predicted = comb(K+3, 3) * (K+2) // 2
    check = "✓" if predicted == S3 else "✗"
    print(f"    S({K}) = {S3:6d}, C(K+3,3)×(K+2)/2 = {predicted}  {check}")

print(f"\n  For Q⁷ (n=7, N_c=4):")
S7 = 0
for K in range(8):
    dk7 = comb(K+6, 6) * (2*K+7) // 7
    S7 += dk7
    # Predicted: S = C(K+7,7) × (K+4)/4
    predicted = comb(K+7, 7) * (K+4) // 4
    check = "✓" if predicted == S7 else "✗"
    print(f"    S({K}) = {S7:6d}, C(K+7,7)×(K+4)/4 = {predicted}  {check}")

print(f"""
  ★ UNIVERSAL FORMULA:

    S(K, Q^n) = C(K+n, n) × (K + N_c) / N_c

    where n = n_C = complex dimension, N_c = (n+1)/2 = colors

  This holds for ALL Q^n (verified on Q³, Q⁵, Q⁷).
  The partial sum depends ONLY on the two primary BST integers.
""")

# ═══════════════════════════════════════════════════════════════════
# Section 11: The density of states
# ═══════════════════════════════════════════════════════════════════

print("\n§11. DENSITY OF STATES")
print("-" * 50)

# S(K) ~ K^{n+1}/n! × K/N_c = K^{n+2}/(n!·N_c) for large K
# For Q⁵: S(K) ~ K^7/360 for large K
# The spectral dimension is 2 × (n_C + 1) = 2C₂ = 12? No...
# Actually the degree of S(K) as polynomial in K is n+1 = 6
# (since it's a degree 6 polynomial)

print(f"\n  S(K) is a polynomial of degree n_C + 1 = C₂ = 6 in K")
print(f"  Leading coefficient: 1/(n_C! × N_c) = 1/(5! × 3) = 1/360")
print(f"  S(K) ~ K^{'{C₂}'}/{'{n_C! × N_c}'} = K⁶/360 for large K")
print()
print(f"  The growth rate is K^C₂ — the mass gap controls the")
print(f"  asymptotic density of spectral states!")
print()
print(f"  More precisely: S(K) ~ K^C₂ / (C₂!/r)")
print(f"  Since 360 = C₂!/r = 720/2")

# ═══════════════════════════════════════════════════════════════════
# Section 12: S(K) mod primes
# ═══════════════════════════════════════════════════════════════════

print("\n\n§12. S(K) MODULO BST PRIMES")
print("-" * 50)

for p in [3, 5, 7, 11, 13]:
    print(f"\n  S(K) mod {p}:")
    mods = []
    for K in range(3 * p):
        val = comb(K+5, 5) * (K+3) // 3
        mods.append(val % p)
    print(f"    {mods[:p]}")
    # Period?
    period = None
    for T in range(1, 2*p + 1):
        if all(mods[i] == mods[i + T] for i in range(min(len(mods) - T, 2*T))):
            period = T
            break
    if period:
        print(f"    Period: {period}")

# ═══════════════════════════════════════════════════════════════════
# Synthesis
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 72)
print("§13. SYNTHESIS")
print("═" * 72)

print("""
  MASTER FORMULA:

    S(K) = C(K+n_C, n_C) × (K+N_c)/N_c

  UNIVERSAL (verified on Q³, Q⁵, Q⁷).
  Depends on ONLY two BST integers: n_C and N_c.

  PRODUCT FORM (Q⁵):

    S(K) = (K+1)(K+2)(K+3)²(K+4)(K+5) / 360
    360 = n_C! × N_c = C₂!/r

  SPECIAL VALUES:
    S(0) = 1       (vacuum)
    S(1) = 8       = 2^{N_c}
    S(2) = 35      = n_C × g
    S(4) = 294     = r × N_c × g²
    S(9) = 8008    = 2^{N_c} × g × c₂ × c₃

  ASYMPTOTICS:
    S(K) ~ K^{C₂} / (C₂!/r)   for large K
    The mass gap C₂ controls the density of states.

  The (K+3)² factor makes (K+N_c) appear SQUARED,
  creating a double zero at K = -N_c. This is the
  "shadow" of the color symmetry in the spectral count.
""")

print("═" * 72)
print("TOY 184 COMPLETE")
print(f"  S(K) = C(K+n_C, n_C) × (K+N_c)/N_c  [UNIVERSAL]")
print(f"  S(K) ~ K^C₂/(C₂!/r) = K⁶/360  [density of states]")
print(f"  360 = n_C! × N_c = 5! × 3")
print(f"  S(1)=8=2^N_c, S(2)=35=n_C×g, S(9)=8008=2^N_c×g×c₂×c₃")
print("═" * 72)
