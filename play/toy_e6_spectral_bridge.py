#!/usr/bin/env python3
"""
TOY 183: E₆ AND THE SPECTRAL BRIDGE
=====================================

dim(27 of E₆) = d₂(Q⁵) = second spectral multiplicity of Q⁵.

This is a link between:
- E₆ GUT representation theory (particle physics)
- Spectral geometry of Q⁵ (BST foundation)
- The Hilbert series H(x) = (1+x)/(1-x)⁶ (Toy 141)

This toy investigates whether this is a coincidence or structural.

Key facts:
  d_k = C(k+4,4)×(2k+5)/5  [from Toy 146]
  d₂ = C(6,4)×9/5 = 15×9/5 = 27
  27 = dim of fundamental of E₆

Is there a representation-theoretic reason the second eigenvalue
multiplicity equals the E₆ fundamental dimension?

Casey Koons, March 16, 2026
"""

from fractions import Fraction
from math import comb, factorial

print("=" * 72)
print("TOY 183: E₆ AND THE SPECTRAL BRIDGE")
print("=" * 72)

# ═══════════════════════════════════════════════════════════════════
# Section 1: The spectral multiplicities
# ═══════════════════════════════════════════════════════════════════

print("\nSection 1. SPECTRAL MULTIPLICITIES OF Q⁵")
print("-" * 50)

def d_k(k):
    """Multiplicity of the k-th eigenvalue of Q⁵ = D_IV⁵"""
    return comb(k + 4, 4) * (2*k + 5) // 5

print(f"\n  d_k = C(k+4,4)×(2k+5)/5:")
for k in range(10):
    dk = d_k(k)
    factor = 2*k + 5
    binom = comb(k+4, 4)
    # What is 2k+5?
    chern_labels = {5: "n_C", 7: "g", 9: "c₄", 11: "c₂", 13: "c₃",
                    15: "3n_C", 17: "17", 19: "19", 21: "dim G", 23: "23"}
    label = chern_labels.get(factor, "")
    print(f"    d_{k} = C({k+4},4)×{factor}/5 = {binom}×{factor}/5 = {dk}  "
          f"[{factor} = {label}]" if label else
          f"    d_{k} = C({k+4},4)×{factor}/5 = {binom}×{factor}/5 = {dk}")

# ═══════════════════════════════════════════════════════════════════
# Section 2: 27 = d₂ and E₆
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 2. THE 27 CONNECTION")
print("-" * 50)

print(f"\n  d₂ = C(6,4)×9/5 = 15×9/5 = 27")
print(f"  dim(fund E₆) = 27")
print()

# Is this just a numerical coincidence?
# Let's understand WHERE 27 comes from in each context:

print("  In BST spectral geometry:")
print(f"    d₂ = C(6,4) × 9/5 = C(6,4) × c₄/n_C")
print(f"    = C(n_C+1, C₂-r) × c₄/n_C")
print(f"    = C(C₂, C₂-r) × c₄/n_C")
print(f"    = C(6, 4) × 9/5 = 15 × 9/5 = 27")
print()

print("  In E₆ representation theory:")
print(f"    dim(fund) = 27 = 3³ = N_c^{'{N_c}'}")
print(f"    Under SU(3): 27 → 10 representations in various dims")
print(f"    Under SO(10): 27 → 16 + 10 + 1")
print()

# 27 = 3³ = N_c^N_c
print(f"  ★ 27 = N_c^N_c = 3³")
print(f"    Also: d₂ = 27 = N_c^N_c from spectral geometry")
print(f"    = m_s/m̂ (strange quark mass ratio)")

# Can we derive this? d₂ = C(6,4)×9/5 = 15×9/5
# = C(n_C+1, 4) × (2×2+n_C)/n_C
# = C(6,4) × 9/5

# Is d₂ = N_c^N_c in general?
print(f"\n  Check: is d₂ = N_c^N_c universal?")
for n in [3, 5, 7, 9, 11]:
    N = (n + 1) // 2  # N_c
    n_dim = n  # n_C = complex dimension
    # Spectral multiplicity: d_k = C(k+n-1, n-1) × (2k+n) / n for Q^n
    # At k=2:
    d2 = comb(2 + n - 1, n - 1) * (2*2 + n) // n
    Nc_power = N**N
    check = "✓" if d2 == Nc_power else f"(d₂={d2}, N_c^N_c={Nc_power})"
    print(f"    Q^{n}: d₂ = C({n+1},{n-1})×{n+4}/{n} = {d2}, "
          f"N_c^N_c = {N}^{N} = {Nc_power}  {check}")

# ═══════════════════════════════════════════════════════════════════
# Section 3: The general d₂ formula
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 3. GENERAL d₂ FOR Q^n")
print("-" * 50)

print(f"\n  d₂(Q^n) = C(n+1, n-1) × (n+4)/n")
print(f"          = C(n+1, 2) × (n+4)/n")
print(f"          = n(n+1)/2 × (n+4)/n")
print(f"          = (n+1)(n+4)/2")
print()

for n in [3, 5, 7, 9, 11, 13]:
    d2 = (n + 1) * (n + 4) // 2
    N = (n + 1) // 2
    Nc_Nc = N**N
    print(f"    Q^{n:2d}: d₂ = ({n+1})×({n+4})/2 = {d2:5d},"
          f"  N_c^N_c = {N}^{N} = {Nc_Nc:5d},"
          f"  ratio = {Fraction(d2, Nc_Nc)}")

# Q⁵: d₂ = 6×9/2 = 27 = 3³ ✓
# Q³: d₂ = 4×7/2 = 14, N_c^N_c = 2² = 4. Ratio = 7/2
# NOT universal! Only Q⁵ has d₂ = N_c^N_c

print(f"\n  ★ d₂ = N_c^N_c ONLY for Q⁵ (n=5)!")
print(f"    (n+1)(n+4)/2 = ((n+1)/2)^((n+1)/2)")
print(f"    Setting N = (n+1)/2:")
print(f"    2N(2N+3)/2 = N^N")
print(f"    N(2N+3) = N^N")
print(f"    2N+3 = N^{'{N-1}'}")
print(f"    N=2: 7 ≠ 2. N=3: 9 = 9 ✓. N=4: 11 ≠ 64. N=5: 13 ≠ 625.")
print(f"    UNIQUE at N=3 → 14th uniqueness condition!")

# ═══════════════════════════════════════════════════════════════════
# Section 4: The d₂ = N_c^N_c uniqueness proof
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 4. THE d₂ = N_c^{N_c} UNIQUENESS THEOREM")
print("=" * 50)

print(f"""
  THEOREM: d₂(Q^n) = N_c^N_c if and only if n = 5 (i.e., N_c = 3).

  PROOF:
    d₂(Q^n) = (n+1)(n+4)/2
    N_c = (n+1)/2

    Setting (n+1)(n+4)/2 = N_c^N_c:
    2N(2N+3)/2 = N^N
    N(2N+3) = N^N
    2N+3 = N^(N-1)

    Check:
    N=2: 2(2)+3 = 7, 2^1 = 2.    7 ≠ 2
    N=3: 2(3)+3 = 9, 3^2 = 9.    9 = 9 ✓
    N=4: 2(4)+3 = 11, 4^3 = 64.  11 ≠ 64
    N=5: 2(5)+3 = 13, 5^4 = 625. 13 ≠ 625

    For N ≥ 4: N^(N-1) grows much faster than 2N+3 (linear vs power).
    For N = 1: 5 ≠ 1. QED.

  ★ The ONLY Q^n where the second spectral multiplicity equals
    N_c raised to the N_c-th power is Q⁵.

  This is the 14th uniqueness condition for n_C = 5.

  Physical meaning:
    d₂ = 27 = 3³ = the number of distinct mass states at the
    second spectral level equals the number of colors cubed.
    In E₆ language: the GUT fundamental representation dimension.
""")

# ═══════════════════════════════════════════════════════════════════
# Section 5: More E₆ connections
# ═══════════════════════════════════════════════════════════════════

print("\nSection 5. THE E₆ REPRESENTATION DICTIONARY")
print("-" * 50)

# E₆ representations and BST spectral multiplicities
e6_reps = [1, 27, 78, 351, 650, 2925]
print(f"\n  E₆ representations vs BST multiplicities:")
print(f"  {'dim(E₆)':>8s}  {'d_k':>8s}  {'k':>3s}  Match?")
print(f"  {'────────':>8s}  {'────':>8s}  {'───':>3s}  {'──────'}")

for r in e6_reps:
    # Search for matching d_k
    found = False
    for k in range(20):
        if d_k(k) == r:
            print(f"  {r:>8d}  d_{k} = {d_k(k):>5d}  {k:>3d}  ✓ MATCH")
            found = True
            break
    if not found:
        print(f"  {r:>8d}  {'—':>8s}  {'—':>3s}  (no match)")

# ═══════════════════════════════════════════════════════════════════
# Section 6: The d_k sequence and exceptional algebras
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 6. SPECTRAL MULTIPLICITIES AS ALGEBRA DIMENSIONS")
print("-" * 50)

# Which d_k equal dimensions of simple Lie algebras?
algebra_dims = {
    1: ["trivial"],
    3: ["su(2)"],
    8: ["su(3)"],
    10: ["so(5)", "sp(4)"],
    14: ["G₂"],
    15: ["su(4)"],
    21: ["so(7)", "sp(6)"],
    24: ["su(5)"],
    28: ["so(8)"],
    35: ["su(6)"],
    36: ["so(9)", "sp(8)"],
    45: ["so(10)"],
    48: ["su(7)"],
    52: ["F₄"],
    55: ["so(11)", "sp(10)"],
    63: ["su(8)"],
    66: ["so(12)"],
    78: ["so(13)", "sp(12)", "E₆"],
    80: ["su(9)"],
    91: ["so(14)"],
    99: ["su(10)"],
    120: ["so(16)"],
    133: ["E₇"],
    248: ["E₈"],
}

print(f"\n  d_k values matching dimensions of simple Lie algebras:")
for k in range(15):
    dk = d_k(k)
    if dk in algebra_dims:
        algebras = ", ".join(algebra_dims[dk])
        print(f"    d_{k:2d} = {dk:5d} = dim({algebras})")
    else:
        print(f"    d_{k:2d} = {dk:5d}")

# ═══════════════════════════════════════════════════════════════════
# Section 7: The Hilbert series connection
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 7. HILBERT SERIES H(x) = (1+x)/(1-x)⁶")
print("-" * 50)

# From Toy 141:
# H(x) = Σ d_k x^k = (1+x)/(1-x)⁶
# The pole at x=1 has order 6 = C₂ = mass gap

# Evaluate at special points
print(f"\n  H(x) = (1+x)/(1-x)⁶ = Σ d_k x^k")
print()

# At x = -1: H(-1) = 0/2⁶ = 0 (zero at x = -1 forced by (1+x) factor)
# At x = 1: H(1) diverges (pole of order 6 = C₂)
# At x = e^{2πi/n} for BST values:

from cmath import exp, pi as PI

print("  H(x) at roots of unity:")
for n in [3, 5, 6, 7, 11, 13]:
    x = exp(2j * PI / n)
    H = (1 + x) / (1 - x)**6
    print(f"    H(ζ_{n:2d}) = {H.real:>12.4f} + {H.imag:>12.4f}i"
          f"  |H| = {abs(H):>12.4f}")

# ═══════════════════════════════════════════════════════════════════
# Section 8: The generating function at ζ₇
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 8. H(x) AT THE BST QUANTUM PARAMETER")
print("-" * 50)

# The BST quantum parameter is q = ζ₇ = e^{2πi/7}
q = exp(2j * PI / 7)
H_q = (1 + q) / (1 - q)**6
print(f"\n  q = ζ₇ = e^{{2πi/7}} (the BST quantum parameter)")
print(f"  H(q) = (1+q)/(1-q)⁶")
print(f"       = {H_q.real:.6f} + {H_q.imag:.6f}i")
print(f"  |H(q)| = {abs(H_q):.6f}")
print(f"  |1-q| = {abs(1-q):.6f}")
print(f"  |1-q|⁶ = {abs(1-q)**6:.6f}")
print(f"  |1+q| = {abs(1+q):.6f}")

# ═══════════════════════════════════════════════════════════════════
# Section 9: Sum rules for d_k
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 9. SUM RULES")
print("-" * 50)

# Partial sums
print(f"\n  Partial sums Σ d_k (k=0 to K):")
partial = 0
for K in range(10):
    partial += d_k(K)
    # Factor
    n = partial
    fs = []
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
        while n % p == 0:
            fs.append(p)
            n //= p
    if n > 1:
        fs.append(n)
    f_str = '×'.join(str(f) for f in fs) if partial > 1 else '1'
    print(f"    Σ d_k (k≤{K}) = {partial:6d} = {f_str}")

# ═══════════════════════════════════════════════════════════════════
# Section 10: The bulk-boundary dictionary
# ═══════════════════════════════════════════════════════════════════

print("\n\nSection 10. THE BULK-BOUNDARY DICTIONARY")
print("-" * 50)

print("""
  Casey: "Higher energies like inside the bulk?"

  Level 1 = BULK (UV)              Level 2 = BOUNDARY (IR)
  ─────────────────────            ──────────────────────
  E₆₁: c = 6 = C₂                 so(7)₂: c = 6 = C₂
  E₇₁: c = 7 = g                  sp(6)₂: c = 7 = g
  E₈₁: c = 8 = 2^{N_c}           so(5)₃: c = 5 = n_C

  Exceptional symmetry             Physical + L-group pair
  No coupling needed (ℓ=1)         Coupling at ℓ=2
  Sees C₂, g, 2^{N_c}            Sees n_C, C₂, g

  N_c and n_C are INFRARED:
    - They require level 2 (physical coupling)
    - They are invisible to level-1 exceptionals
    - They emerge at the boundary

  C₂ and g are HOLOGRAPHIC:
    - Present at BOTH levels
    - Bridge between bulk and boundary
    - The mass gap and genus are universal

  2^{N_c} = 8 is ULTRAVIOLET:
    - Only at level 1 (exceptional)
    - Controls the spinor representation
    - Invisible from the boundary theory alone

  The 10-dim real boundary Q⁵ is surrounded by the
  exceptional bulk E₆ × E₇ × E₈ with dim sum = 21 = dim(B₃).
""")

# ═══════════════════════════════════════════════════════════════════
# Section 11: The 27 = N_c^N_c theorem
# ═══════════════════════════════════════════════════════════════════

print("\nSection 11. UNIQUENESS THEOREM SUMMARY")
print("=" * 50)

print(f"""
  14th UNIQUENESS CONDITION:

  d₂(Q^n) = N_c^N_c  iff  n = 5

  Proof: 2N+3 = N^(N-1) has unique solution N=3 (= N_c)

  Physical interpretation:
  - d₂ = 27 = number of states at the second spectral level
  - N_c^N_c = 3³ = the self-referential color number
  - = dim(fund E₆) = the GUT fundamental
  - = m_s/m̂ = the strange quark mass ratio

  The second excited state of Q⁵ sees EXACTLY N_c^N_c = 27 modes.
  This is the E₆ fundamental. The spectral geometry of Q⁵
  contains E₆ representation theory in its multiplicity function.

  Combined with d₁ = 7 = g (from Toy 146):
  - First excited state: g = 7 modes (the genus)
  - Second excited state: N_c^N_c = 27 modes (E₆ fundamental)
  - d₁ × d₂ = 7 × 27 = 189 = 27 × 7 = 3³ × 7
""")

d1d2 = d_k(1) * d_k(2)
print(f"  d₁ × d₂ = {d_k(1)} × {d_k(2)} = {d1d2} = 7 × 27 = g × N_c^N_c")
print(f"  = 3³ × 7 = N_c^N_c × g")

# ═══════════════════════════════════════════════════════════════════
# Final
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 72)
print("TOY 183 COMPLETE")
print(f"  d₂ = N_c^N_c = 27 = dim(fund E₆) — UNIQUE to Q⁵")
print(f"  14th uniqueness: 2N+3 = N^(N-1) has only N=3")
print(f"  Bulk-boundary dictionary: level 1 = UV, level 2 = IR")
print(f"  Holographic integers: C₂ and g present at both levels")
print("═" * 72)
