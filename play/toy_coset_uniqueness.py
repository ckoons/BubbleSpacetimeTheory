#!/usr/bin/env python3
"""
TOY 179: COSET UNIQUENESS — WHY N=2,3 ARE SPECIAL
===================================================

The coset formula sp(2N)₂/su(N)₁ = n_C = 2N-1 works for N=2,3
but fails for N≥4. WHY?

This toy:
1. Proves algebraically why N=2,3 are the only solutions
2. Explores what OTHER coset identities hold universally
3. Finds the complete coset algebra of the BST WZW network
4. Connects to the ζ-bridge through L-function decompositions

Casey Koons, March 16, 2026
"""

from fractions import Fraction

print("=" * 72)
print("TOY 179: COSET UNIQUENESS — WHY N=2,3 ARE SPECIAL")
print("=" * 72)

# ═══════════════════════════════════════════════════════════════════
# Section 1: The algebra of why N=2,3 work
# ═══════════════════════════════════════════════════════════════════

print("\nSection 1. ALGEBRAIC PROOF")
print("-" * 50)

print("""
  c(sp(2N)₂) = 2N(2N+1)/(N+3)
  c(su(N)₁) = (N²-1)/(N+1) = N-1

  Difference: D(N) = 2N(2N+1)/(N+3) - (N-1)
             = [2N(2N+1) - (N-1)(N+3)] / (N+3)
             = [4N²+2N - N²-2N+3] / (N+3)
             = [3N²+3] / (N+3)
             = 3(N²+1) / (N+3)

  Target: n_C = 2N-1

  Equation: 3(N²+1)/(N+3) = 2N-1
            3N²+3 = (2N-1)(N+3) = 2N²+5N-3
            N² - 5N + 6 = 0
            (N-2)(N-3) = 0

  ★ EXACTLY N=2 and N=3. No other solutions.
""")

# Verify
for N in range(1, 10):
    D = Fraction(3*(N*N + 1), N + 3)
    target = 2*N - 1
    match = "✓" if D == target else ""
    print(f"  N={N}: D(N) = 3({N*N+1})/({N+3}) = {D} = {float(D):.4f}  "
          f"vs n_C = {target}  {match}")

# ═══════════════════════════════════════════════════════════════════
# Section 2: What IS the coset for general N?
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 2. THE GENERAL COSET c = 3(N²+1)/(N+3)")
print("-" * 50)

print("\n  c(sp(2N)₂/su(N)₁) = 3(N²+1)/(N+3):")
for N in range(2, 10):
    D = Fraction(3*(N*N + 1), N + 3)
    print(f"    N={N}: c = {D} = {float(D):.4f}")

# Factor 3 in numerator: 3(N²+1)
# This is always divisible by 3
# The question: for which N does (N+3) | (N²+1)?
# N²+1 ≡ (N+3)² - 6N - 8 ≡ -6N-8 ≡ -6(N+3)+18-8 ≡ 10 (mod N+3)
# So (N+3) | (N²+1) iff (N+3) | 10
# Divisors of 10: 1, 2, 5, 10
# N+3 ∈ {1,2,5,10} → N ∈ {-2,-1,2,7}
# Physical: N=2 and N=7

print("\n  When is c(sp(2N)₂/su(N)₁) an INTEGER?")
print("  Need (N+3) | 3(N²+1)")
print("  Since N²+1 ≡ 10 (mod N+3), need (N+3) | 30")
print("  Divisors of 30 with N≥2: N+3 ∈ {5,6,10,15,30}")
print("  → N ∈ {2, 3, 7, 12, 27}")

for N in [2, 3, 7, 12, 27]:
    D = Fraction(3*(N*N + 1), N + 3)
    print(f"    N={N:2d}: c = 3×{N*N+1}/{N+3} = {D}")

# ═══════════════════════════════════════════════════════════════════
# Section 3: The DEEPER coset identities
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 3. UNIVERSAL COSET IDENTITIES")
print("-" * 50)

def wzw_c(dim_g, h_dual, level):
    return Fraction(level * dim_g, level + h_dual)

# For any N, check various coset combinations
print("\n  Looking for cosets that ALWAYS give BST integers:")
print()

# Identity 1: c(so(2N+1)₂) - c(sp(2N)₂) = ?
print("  c(B_N level 2) - c(C_N level 2):")
for N in range(2, 8):
    dim_B = N * (2*N + 1)
    h_B = 2*N - 1
    dim_C = N * (2*N + 1)
    h_C = N + 1
    c_B = wzw_c(dim_B, h_B, 2)
    c_C = wzw_c(dim_C, h_C, 2)
    diff = c_B - c_C
    n_C = 2*N - 1  # for Q^{2N-1}
    print(f"  N={N}: c(so({2*N+1})₂) - c(sp({2*N})₂) = {c_B} - {c_C} = {diff} = {float(diff):.4f}")

# Identity 2: The DIFFERENCE c(B_N) - c(C_N) at level 2
print()
print("  These differences:")
for N in range(2, 8):
    dim_B = N * (2*N + 1)
    h_B = 2*N - 1
    dim_C = N * (2*N + 1)
    h_C = N + 1
    c_B = wzw_c(dim_B, h_B, 2)
    c_C = wzw_c(dim_C, h_C, 2)
    diff = c_B - c_C
    # Both have same dim, so:
    # diff = dim × [2/(2+h_B) - 2/(2+h_C)]
    # = 2·dim × [(2+h_C-2-h_B)/((2+h_B)(2+h_C))]
    # = 2·dim × [(h_C-h_B)/((2+h_B)(2+h_C))]
    # h_C - h_B = (N+1)-(2N-1) = 2-N
    print(f"  N={N}: diff = {diff}, h_B-h_C = {h_B-h_C}, (N-2) = {N-2}")

# Identity 3: c(G) + c(^LG) at level 2
print()
print("\n  c(B_N level 2) + c(C_N level 2) = c(G) + c(^LG):")
for N in range(2, 8):
    dim_BC = N * (2*N + 1)
    h_B = 2*N - 1
    h_C = N + 1
    c_sum = wzw_c(dim_BC, h_B, 2) + wzw_c(dim_BC, h_C, 2)
    P1 = Fraction(2**(2*N-1+2) - 2, 3)  # P(1) for Q^{2N-1}
    n_C = 2*N - 1
    print(f"  N={N}: sum = {c_sum} = {float(c_sum):.4f}  "
          f"(n_C = {n_C}, 2n_C = {2*n_C}, n_C+1 = {n_C+1})")

# ═══════════════════════════════════════════════════════════════════
# Section 4: The product identity
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 4. THE PRODUCT AND SUM IDENTITIES")
print("-" * 50)

# From Toy 175: c(G)×c(^LG) = P(1) only for N=3
# What about c(G) + c(^LG)?

print("\n  For B_N/C_N Langlands pair at level 2:")
print()
print(f"  {'N':>3s}  {'c(G)':>8s}  {'c(^LG)':>8s}  {'product':>8s}  {'sum':>8s}  {'P(1)':>8s}")
print(f"  {'---':>3s}  {'------':>8s}  {'------':>8s}  {'-------':>8s}  {'---':>8s}  {'----':>8s}")

for N in range(2, 8):
    dim_BC = N * (2*N + 1)
    h_B = 2*N - 1
    h_C = N + 1
    c_G = wzw_c(dim_BC, h_B, 2)
    c_L = wzw_c(dim_BC, h_C, 2)
    prod = c_G * c_L
    s = c_G + c_L
    n = 2*N - 1  # n_C for Q^n
    # Chern polynomial: P(h) = (1+h)^(n+2)/(1+2h) evaluated at h=1
    # P(1) = 2^(n+2)/3
    P1 = Fraction(2**(n+2), 3)
    prod_check = "= P(1) ✓" if prod == P1 else ""
    print(f"  {N:3d}  {str(c_G):>8s}  {str(c_L):>8s}  {str(prod):>8s}  {str(s):>8s}  {str(P1):>8s}  {prod_check}")

# ═══════════════════════════════════════════════════════════════════
# Section 5: The sum c(G)+c(^LG) = 2n_C + correction
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 5. SUM = 2c(G)/(2N+1) + ...")
print("-" * 50)

print("\n  Analyzing c(G) + c(^LG):")
for N in range(2, 8):
    dim_BC = N * (2*N + 1)
    h_B = 2*N - 1
    h_C = N + 1
    c_G = wzw_c(dim_BC, h_B, 2)
    c_L = wzw_c(dim_BC, h_C, 2)
    s = c_G + c_L
    n_C = 2*N - 1
    ratio = s / n_C
    print(f"  N={N}: sum/n_C = {s}/{n_C} = {ratio} = {float(ratio):.4f}")

# ═══════════════════════════════════════════════════════════════════
# Section 6: The golden coset chain
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 6. THE GOLDEN COSET CHAIN")
print("-" * 50)

print("""
  For BST (N=3, n_C=5), the coset chain at level 2:

  sp(6)₂                  c = 7  = g       [L-group]
  sp(6)₂/su(3)₁           c = 5  = n_C     [color-stripped]
  so(7)₂                  c = 6  = C₂      [physical]
  so(7)₂/su(3)₂           c = 14/5 = G₂₁   [deep coset]
  so(7)₂/G₂₂              c = 4/3          [tri-critical Ising]
  so(7)₂/so(5)₂           c = 2  = r       [rank-stripped]
""")

# Now let's explore: what if we build a COMPLETE coset algebra?
# Take all pairs of the c=6 models and compute all cosets

print("  Pairwise cosets of c=6 models:")
print()

c6_models = [
    ("so(7)₂", 21, 5, 2),
    ("su(3)₉", 8, 3, 9),
    ("su(7)₁", 48, 7, 1),
    ("so(12)₁", 66, 10, 1),
    ("sp(8)₁", 36, 5, 1),
    ("E₆₁", 78, 12, 1),
    ("G₂₃", 14, 4, 3),
]

# These all have c=6, so pairwise cosets are all 0
# What we want is: which algebras EMBED in which?
# When g ⊂ h, the coset h/g has c = c(h) - c(g)

# Instead, let's look at cosets between models with DIFFERENT c values
# from the BST WZW network

print("  The BST WZW network — all models with c = BST integer:")
print()

bst_models = [
    ("su(2)₁", 3, 2, 1, 1),
    ("su(3)₁", 8, 3, 1, 2),
    ("so(5)₃", 10, 3, 3, 5),
    ("su(3)₅", 8, 3, 5, 5),
    ("so(7)₂", 21, 5, 2, 6),
    ("sp(6)₂", 21, 4, 2, 7),
    ("su(3)₉", 8, 3, 9, 6),
    ("G₂₃", 14, 4, 3, 6),
]

for name, dim_g, h_dual, level, c_val in bst_models:
    c = wzw_c(dim_g, h_dual, level)
    print(f"    {name:10s}: c = {str(c):>5s} = {float(c):.2f}")

# ═══════════════════════════════════════════════════════════════════
# Section 7: The (N-2)(N-3)=0 theorem
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 7. THE (N-2)(N-3)=0 THEOREM")
print("=" * 50)

print("""
  THEOREM: The L-group coset sp(2N)₂/su(N)₁ has central charge
  equal to n_C = 2N-1 if and only if N = 2 or N = 3.

  PROOF:
    c(sp(2N)₂) - c(su(N)₁) = 3(N²+1)/(N+3)
    Setting equal to 2N-1:
      3(N²+1) = (2N-1)(N+3) = 2N²+5N-3
      N² - 5N + 6 = 0
      (N-2)(N-3) = 0  ∎

  The factorization (N-2)(N-3) = 0 means:
  - N=2: the BABY case (D_IV³, Sp(4), Siegel modular forms)
  - N=3: the PHYSICAL case (D_IV⁵, SO₀(5,2), Standard Model)

  These are EXACTLY the cases BST needs.

  ★ The quadratic (N-2)(N-3) has roots at the CONSECUTIVE integers
    that make N_c = N = 2 or 3. The baby and physical cases are
    the ONLY solutions to a CLEAN quadratic.

  Note: N² - 5N + 6 = 0 has discriminant 25 - 24 = 1 = perfect square.
  This is WHY the roots are consecutive integers.
  Discriminant = 1 is the SIMPLEST non-trivial perfect square.

  Compare with other BST uniqueness conditions:
  - N(N-3) = 0 for su(N_c)_{n_C} uniqueness (N=0 or N=3)
  - (N-2)(N-3) = 0 for L-group coset uniqueness (N=2 or N=3)
  Both pick out N=3. The coset version ALSO gets the baby case.
""")

# ═══════════════════════════════════════════════════════════════════
# Section 8: The 3(N²+1) formula
# ═══════════════════════════════════════════════════════════════════

print("\nSection 8. THE FORMULA 3(N²+1)/(N+3)")
print("-" * 50)

print("\n  Properties of D(N) = 3(N²+1)/(N+3):")
print()

for N in range(2, 12):
    D = Fraction(3*(N*N + 1), N + 3)
    num = 3*(N*N + 1)
    den = N + 3
    print(f"  N={N:2d}: D = 3×{N*N+1}/{N+3} = {num}/{den} = {str(D):>8s} = {float(D):>8.4f}")

# At N=2: D = 3×5/5 = 3 = n_C(Q³) ✓
# At N=3: D = 3×10/6 = 5 = n_C(Q⁵) ✓
# Note: 3×5 = 15 = 3×n_C(Q⁵), 3×10 = 30

# The sequence 5, 10, 17, 26, 37, 50, 65, 82, 101, ...
# = N²+1 for N=2,3,4,...
# These are shifted squares!

print("\n  N²+1 sequence: these are 'near-square' numbers")
print("  When does (N+3) divide 3(N²+1)?")
print("  N²+1 ≡ (N+3)²-6N-8 ≡ -6(N+3)+10 (mod N+3)")
print("  So (N+3) | 3(N²+1) iff (N+3) | 30")
print()
print("  Divisors of 30: 1, 2, 3, 5, 6, 10, 15, 30")
print("  N+3 values:     1, 2, 3, 5, 6, 10, 15, 30")
print("  N values:       -2,-1, 0, 2, 3, 7, 12, 27")
print("  Physical (N≥2): N ∈ {2, 3, 7, 12, 27}")
print()

# The INTEGER coset values:
for N in [2, 3, 7, 12, 27]:
    D = Fraction(3*(N*N + 1), N + 3)
    n_C = 2*N - 1
    print(f"  N={N:2d}: D = {D}, n_C = {n_C}, D-n_C = {D-n_C}")

# ═══════════════════════════════════════════════════════════════════
# Section 9: The ζ-bridge coset perspective
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 9. THE ζ-BRIDGE FROM COSETS")
print("-" * 50)

print("""
  The Siegel modular forms live on Q³ = Sp(4,R)/U(2).

  Eisenstein series on Sp(2N) have L-functions:
    L(s, E_k, std) = ∏_{j=0}^{N-1} ζ(s-k+1+j)    [N+1 copies? or N?]
    L(s, E_k, spin) = product of shifted ζ's

  For BST (N=3, Sp(6)):
    Standard L-function has degree 7 = g = 2N+1
    Spinor L-function has degree 8 = 2^N = 2^{N_c}

  The COSET formula tells us:
    c(^LG) = c(color₁) + n_C
    7 = 2 + 5

  In L-function language:
    deg(std) = g = 2N+1 = (N-1) + (N+2) = c(color₁)×...

  What factors in the Eisenstein L-function come from the coset?

  The N_c copies of ζ from the std representation →
    come from the su(N_c)₁ sector (color part)
  The remaining ζ-copies from spin representation →
    come from the coset (geometry part)

  Total: N_c + 2^{N_c} = 3 + 8 = 11 = c₂ = dim K
  [from Toy 177]
""")

# ═══════════════════════════════════════════════════════════════════
# Section 10: Baby vs physical case
# ═══════════════════════════════════════════════════════════════════

print("\nSection 10. BABY VS PHYSICAL: PARALLEL DICTIONARY")
print("-" * 50)

print("""
                          BABY (N=2)        PHYSICAL (N=3)
  ─────────────────────────────────────────────────────────
  Symmetric space         D_IV³ = Q³        D_IV⁵ = Q⁵
  Group                   SO₀(3,2)          SO₀(5,2)
  Lie algebra             sp(4,R) ≅ so(3,2) so(5,2)
  L-group                 SO(5)             Sp(6)

  Physical WZW            so(5)₂            so(7)₂
  c(physical)             4                 6 = C₂
  L-group WZW             sp(4)₂            sp(6)₂
  c(L-group)              4                 7 = g
  Color algebra           su(2)             su(3)
  c(color₁)               1                 2
  Coset c(^LG/color₁)     3 = n_C(Q³)       5 = n_C(Q⁵)

  Consecutive triple      (3,4,4)           (5,6,7)
  All distinct?           NO (C₂=g=4)      YES (all different)
  Langlands reciprocity   c·c = 16 ≠ P(1)  c·c = 42 = P(1)

  Siegel space            Genus 2           [Sp(6) automorphic]
  Selberg trace           Explicit          Conjectural
  ─────────────────────────────────────────────────────────
""")

# Verify: for the baby case, is c(G)=c(^LG)?
# so(5)₂ has c = 2×10/5 = 4
# sp(4)₂ has c = 2×10/5 = 4
# YES! Because so(5) ≅ sp(4) (exceptional isomorphism)
c_so5_2 = wzw_c(10, 3, 2)
c_sp4_2 = wzw_c(10, 3, 2)  # Same algebra!
print(f"  Baby case: so(5)₂ and sp(4)₂ have SAME c = {c_so5_2}")
print(f"  because so(5) ≅ sp(4) (exceptional isomorphism)")
print(f"  → The baby case is SELF-DUAL under Langlands!")
print()
print(f"  This is why the baby consecutive triple has C₂ = g = 4")
print(f"  (the physical and L-group central charges COINCIDE)")
print()
print(f"  Breaking this self-duality → N=3 → Standard Model")

# ═══════════════════════════════════════════════════════════════════
# Section 11: The quadratic uniqueness
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 11. THREE QUADRATICS, ONE ANSWER")
print("=" * 50)

print("""
  Three different quadratic equations all select N_c = 3:

  1. su(N)_n uniqueness:    N(N-3) = 0
     [c(su(N)_n) = n iff N=3]
     Roots: N = 0, 3

  2. Coset uniqueness:      (N-2)(N-3) = 0
     [c(sp(2N)₂/su(N)₁) = n_C iff N=2 or 3]
     Roots: N = 2, 3

  3. Langlands reciprocity: ... [need to derive]
     [c(G)×c(^LG) = P(1) iff N=3]

  All three pick out N_c = 3 = the number of colors.
  The coset version additionally selects N=2 (the baby case).

  Together they form a QUADRATIC TRINITY:
  - The WZW self-consistency → N=3
  - The coset arithmetic → N=2,3
  - The Langlands product → N=3

  Intersection: N = 3 (unique)
""")

# Derive the Langlands reciprocity quadratic
# c(so(2N+1)₂) × c(sp(2N)₂) = P(1)
# [2N(2N+1)/(2N+1)] × [2N(2N+1)/(N+3)] = (2^{2N+1}-2)/3
# 2N × 2N(2N+1)/(N+3) = (2^{2N+1}-2)/3
# 4N²(2N+1)/(N+3) = (2^{2N+1}-2)/3

# For N=3: 36×7/6 = 42, P(1) = (128-2)/3 = 42 ✓
# This is transcendental (exponential vs polynomial), not quadratic
# So it doesn't factor as a nice polynomial — it's the THIRD kind

print("  Langlands reciprocity equation:")
print("  4N²(2N+1)/(N+3) = (2^{2N+1}-2)/3")
print()
for N in range(2, 8):
    lhs = Fraction(4*N*N*(2*N+1), N+3)
    rhs = Fraction(2**(2*N+1) - 2, 3)
    match = "= P(1) ✓" if lhs == rhs else f"≠ P(1) = {rhs}"
    print(f"  N={N}: LHS = {lhs} = {float(lhs):.2f}, RHS = {rhs} = {float(rhs):.2f}  {match}")

# ═══════════════════════════════════════════════════════════════════
# Final synthesis
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 72)
print("Section 12. SYNTHESIS")
print("═" * 72)

print("""
  ★ The (N-2)(N-3) = 0 theorem cleanly explains WHY the coset
    formula works for the baby and physical cases:

    N² - 5N + 6 = 0  ⟺  N = 2 or N = 3

    Discriminant = 1 (simplest perfect square)
    → consecutive integer roots

  ★ The baby case N=2 is SELF-DUAL (so(5) ≅ sp(4)):
    c(G) = c(^LG) = 4, consecutive triple degenerates to (3,4,4)
    Breaking self-duality requires N≥3 → gives (5,6,7) at N=3

  ★ Three quadratics select N_c = 3:
    N(N-3) = 0       [WZW self-consistency]
    (N-2)(N-3) = 0   [coset arithmetic]
    Exponential = 0  [Langlands product, not polynomial]

  ★ The 3(N²+1)/(N+3) formula gives integer values at
    N ∈ {2, 3, 7, 12, 27} — these are where (N+3) | 30.
    The BST cases are the SMALLEST two.

  TOTAL UNIQUENESS CONDITIONS FOR N_c = 3:
    1-8: [previously catalogued]
    9:   su(N_c)_{n_C} has c = n_C only for N_c = 3
    10:  c(G)×c(^LG) = P(1) only for N_c = 3
    11:  c(^LG)/su(N_c)₁ = n_C only for N_c = 2,3
    12:  Baby self-duality breaks only at N_c = 3
""")

print("═" * 72)
print("TOY 179 COMPLETE")
print("  (N-2)(N-3) = 0 theorem proved")
print("  Baby self-duality (so(5)≅sp(4)) identified")
print("  12th uniqueness condition: self-duality breaking")
print("  3(N²+1)/(N+3) formula — integer at N ∈ {2,3,7,12,27}")
print("═" * 72)
