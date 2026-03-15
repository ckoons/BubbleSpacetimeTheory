#!/usr/bin/env python3
"""
TOY 182: THE EXCEPTIONAL CHAIN — E₆ → E₇ → E₈ AND BST
========================================================

The three largest exceptional Lie algebras at level 1 produce:
  c(E₆₁) = 6 = C₂
  c(E₇₁) = 7 = g
  c(E₈₁) = 8 = 2^{N_c}

Their denominators 1+h∨ are: 13, 19, 31 — all PRIME.
And Deligne's full sequence at level 1 gives:
  A₁→1, A₂→2, D₄→4, E₆→6, E₇→7, E₈→8

This toy explores:
1. The E₆-E₇-E₈ chain and BST integers
2. Deligne's exceptional series as a BST highway
3. The denominator primes {13, 19, 31} and BST
4. Total integrable reps = g × c₃ = 91
5. The chain from exceptional algebras to the Standard Model

Casey Koons, March 16, 2026
"""

from fractions import Fraction
from math import comb, gcd

print("=" * 72)
print("TOY 182: THE EXCEPTIONAL CHAIN")
print("=" * 72)

# ═══════════════════════════════════════════════════════════════════
# Section 1: Deligne's exceptional series
# ═══════════════════════════════════════════════════════════════════

print("\n§1. DELIGNE'S EXCEPTIONAL SERIES AT LEVEL 1")
print("-" * 50)

deligne = [
    ("A₁",  1, 3,  2),
    ("A₂",  2, 8,  3),
    ("G₂",  2, 14, 4),
    ("D₄",  4, 28, 6),
    ("F₄",  4, 52, 9),
    ("E₆",  6, 78, 12),
    ("E₇",  7, 133, 18),
    ("E₈",  8, 248, 30),
]

print(f"\n  {'Name':4s} {'rank':4s} {'dim':4s} {'h∨':3s} {'1+h∨':5s} {'c':>6s}  BST")
print(f"  {'────':4s} {'────':4s} {'────':4s} {'───':3s} {'─────':5s} {'──────':>6s}  {'───'}")
for name, rank, dim, h in deligne:
    c = Fraction(dim, 1 + h)
    denom = 1 + h
    # BST identification
    bst = ""
    c_float = float(c)
    if c == 1: bst = "1"
    elif c == 2: bst = "r"
    elif c == 4: bst = "C₂(Q³)"
    elif c == 6: bst = "C₂"
    elif c == 7: bst = "g"
    elif c == 8: bst = "2^{N_c}"
    print(f"  {name:4s} {rank:4d} {dim:4d} {h:3d} {denom:5d} {str(c):>6s}  {bst}")

# ═══════════════════════════════════════════════════════════════════
# Section 2: The pattern of integers vs fractions
# ═══════════════════════════════════════════════════════════════════

print("\n\n§2. INTEGER VS FRACTIONAL CENTRAL CHARGES")
print("-" * 50)

print("""
  The Deligne sequence splits:
  INTEGER c: A₁(1), A₂(2), D₄(4), E₆(6), E₇(7), E₈(8)
  FRACTION: G₂(14/5), F₄(26/5)

  The integers form a subsequence: 1, 2, 4, 6, 7, 8

  Gaps in the integer sequence:
    1 → 2: step 1
    2 → 4: step 2 (SKIP 3 = N_c)
    4 → 6: step 2 (SKIP 5 = n_C)
    6 → 7: step 1
    7 → 8: step 1

  ★ The Deligne sequence SKIPS exactly N_c = 3 and n_C = 5
    These are the two BST integers that come from level 2, not level 1!

  The level-2 model so(7)₂ fills the gap at c = 6
  But 3 and 5 require DIFFERENT level structures:
    c = 3: su(4)₁ (level 1, not exceptional)
    c = 5: several models at various levels
""")

# ═══════════════════════════════════════════════════════════════════
# Section 3: The denominator primes
# ═══════════════════════════════════════════════════════════════════

print("\n§3. DENOMINATOR PRIMES")
print("-" * 50)

print("\n  For level-1 exceptional algebras: c = dim/(1+h∨)")
print("  The denominators 1+h∨:")
print()

denoms = []
for name, rank, dim, h in deligne:
    d = 1 + h
    denoms.append(d)
    # Primality
    is_prime = d > 1 and all(d % p != 0 for p in range(2, d))
    p_mark = "PRIME" if is_prime else ""
    print(f"    {name:4s}: 1+h∨ = {d:3d}  {p_mark}")

print(f"\n  The three E-type denominators: 13, 19, 31 — ALL PRIME")
print(f"  13 = c₃ (3rd Chern class)")
print(f"  19 = Ω denominator (19 in Ω_Λ = 13/19)")
print(f"  31 = Mersenne prime M₅ = 2^5 - 1 = 2^{'{n_C}'} - 1")

# ═══════════════════════════════════════════════════════════════════
# Section 4: The E-type central charge formula
# ═══════════════════════════════════════════════════════════════════

print("\n\n§4. THE E-TYPE FORMULA")
print("-" * 50)

# E₆: dim = 78 = 6×13, h∨ = 12, c = 78/13 = 6
# E₇: dim = 133 = 7×19, h∨ = 18, c = 133/19 = 7
# E₈: dim = 248 = 8×31, h∨ = 30, c = 248/31 = 8

print("\n  E-type algebras have a beautiful factorization:")
print(f"    dim(E₆) = 78  = 6 × 13 = C₂ × c₃")
print(f"    dim(E₇) = 133 = 7 × 19 = g × 19")
print(f"    dim(E₈) = 248 = 8 × 31 = 2^N_c × (2^n_C - 1)")
print()
print(f"  In each case: dim(E_n) = c(E_n) × (1 + h∨)")
print(f"  The central charge IS the quotient dim/denominator")
print()

# The pattern: c = n for E_{n+2}? No: c(E₆)=6, c(E₇)=7, c(E₈)=8
# c = n - ??? Let's see: 6=6, 7=7, 8=8. It's c = rank!
# No: rank(E₆)=6, rank(E₇)=7, rank(E₈)=8. But c = dim/(1+h∨) ≠ rank in general
# It just happens that c = rank for the E-series at level 1

print(f"  ★ For E-type: c = rank (at level 1)")
print(f"    rank(E₆) = 6 = C₂")
print(f"    rank(E₇) = 7 = g")
print(f"    rank(E₈) = 8 = 2^N_c")
print()
print(f"  This means: rank × (1 + h∨) = dim")
print(f"  Equivalently: dim/rank = 1 + h∨ (= Coxeter number + 1?)")

# Actually dim/(rank) for simple Lie algebras:
# dim = rank(rank+1)/2 for A_r... no
# For E-types specifically:
# dim(E_r) = ... there's no simple formula for general r
# But the coincidence c = rank at level 1 means:
# dim/(1+h∨) = rank, so dim = rank(1+h∨)

print()
for name in ['E₆', 'E₇', 'E₈']:
    _, rank, dim, h = [(n,r,d,hh) for n,r,d,hh in deligne if n == name][0]
    print(f"    {name}: dim = {dim} = {rank} × {1+h} = rank × (1+h∨)")

# ═══════════════════════════════════════════════════════════════════
# Section 5: The 91 integrable representations
# ═══════════════════════════════════════════════════════════════════

print("\n\n§5. THE 91 INTEGRABLE REPRESENTATIONS")
print("-" * 50)

# From Toy 181:
# so(7)₂: 7
# su(3)₉: 55
# su(7)₁: 7
# so(12)₁: 4
# sp(8)₁: 5
# E₆₁: 3
# G₂₃: 10
# Total: 91

reps = [
    ("so(7)₂", 7),
    ("su(3)₉", 55),
    ("su(7)₁", 7),
    ("so(12)₁", 4),
    ("sp(8)₁", 5),
    ("E₆₁", 3),
    ("G₂₃", 10),
]

total = sum(n for _, n in reps)
print(f"\n  Total integrable reps across all c=6 models: {total}")
print(f"  91 = 7 × 13 = g × c₃")
print()

# 91 is also a triangular number: T₁₃ = 13×14/2 = 91
print(f"  91 = T₁₃ = 13×14/2 = c₃ × (c₃+1)/2")
print(f"     = triangular number of c₃")

# 91 = C(14,2) = C(2g, 2)
print(f"  91 = C(14, 2) = C(2g, 2)")
print(f"     = number of 2-element subsets of 2g elements")

# ═══════════════════════════════════════════════════════════════════
# Section 6: E₆ → SM decomposition
# ═══════════════════════════════════════════════════════════════════

print("\n\n§6. E₆ → STANDARD MODEL")
print("-" * 50)

print("""
  E₆ contains the Standard Model gauge group:
    E₆ ⊃ SO(10) ⊃ SU(5) ⊃ SU(3)×SU(2)×U(1)

  The 27-dim fundamental of E₆ decomposes as:
    27 → 16 + 10 + 1  under SO(10)
    27 → (3,2)₁ + (3̄,1)₋₄ + (3̄,1)₂ + (1,2)₋₃ + (1,1)₆ + ...

  In BST:
    E₆₁ has c = 6 = C₂
    The BST WZW model so(7)₂ also has c = 6

  Both theories live at c = C₂.
  E₆ gives the GUT → SM breaking chain
  so(7)₂ gives the BST geometric theory

  They're TWO FACES of the same central charge.

  ★ The E₆ GUT and the BST WZW model share c = 6:
    - E₆₁ sees the mass gap through the exceptional route
    - so(7)₂ sees it through the physical algebra route
    - They meet at c = C₂ = 6
""")

# ═══════════════════════════════════════════════════════════════════
# Section 7: The Coxeter-BST correspondence
# ═══════════════════════════════════════════════════════════════════

print("\n§7. COXETER NUMBERS AND BST")
print("-" * 50)

print("\n  Coxeter numbers h (not h∨) for exceptional algebras:")
coxeter = {
    'A₁': 2, 'A₂': 3, 'G₂': 6, 'D₄': 6,
    'F₄': 12, 'E₆': 12, 'E₇': 18, 'E₈': 30,
}

for name, rank, dim, h_dual in deligne:
    h_cox = coxeter[name]
    print(f"    {name:4s}: h = {h_cox:3d}, h∨ = {h_dual:3d}, "
          f"h/h∨ = {Fraction(h_cox, h_dual)}, "
          f"|W| = ?")

# Actually for simply-laced (ADE): h = h∨
# For non-simply-laced: h ≠ h∨
print()
print(f"  For ADE (simply-laced): h = h∨")
print(f"  For G₂: h = 6 = C₂, h∨ = 4 → h/h∨ = 3/2")
print(f"  For F₄: h = 12, h∨ = 9 → h/h∨ = 4/3")

# ═══════════════════════════════════════════════════════════════════
# Section 8: The 248 and E₈
# ═══════════════════════════════════════════════════════════════════

print("\n\n§8. E₈ AND THE BST MOONSHINE CHAIN")
print("-" * 50)

print(f"""
  dim(E₈) = 248 = 8 × 31 = 2^N_c × (2^n_C - 1)

  The BST moonshine chain (Toy 145):
    Q⁵ → Golay [24,12,8] → Leech Λ₂₄ → Monster M → j(τ) → ζ(s)

  E₈ appears in several links:
  - E₈ lattice ⊂ Leech lattice (as sublattice)
  - dim(E₈) = 248 = root system of E₈
  - 240 roots of E₈ = |W(D₅)| = |Φ(E₈)|
  - 240 = 1920/8 = |W(D₅)|/2^N_c

  At level 1: c(E₈₁) = 8 = 2^N_c
  The E₈ WZW model at level 1 carries the "quantum" integer 2^N_c.

  The Leech lattice has:
    - Rank 24 = dim_R(Q⁵) + 14 = 10 + 14 = 24
    - Actually: 24 = 2 × 12 = 2 × 2C₂
    - Kissing number 196560 = ...

  E8 at level 1 gives c = 8 = 2^N_c:
    the same integer that controls the spinor representation
    degree (2^N_c = 8) in the L-function decomposition.
""")

# ═══════════════════════════════════════════════════════════════════
# Section 9: The denominator sequence {3,4,5,7,10,13,19,31}
# ═══════════════════════════════════════════════════════════════════

print("\n§9. THE DENOMINATOR SEQUENCE")
print("-" * 50)

print("\n  Denominators 1+h∨ for Deligne's series:")
denom_list = [1 + h for _, _, _, h in deligne]
print(f"    {denom_list}")
print()

# Check: are these related to Mersenne primes or similar?
print("  Prime factorization:")
for d in denom_list:
    n = d
    fs = []
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        while n % p == 0:
            fs.append(p)
            n //= p
    if n > 1:
        fs.append(n)
    print(f"    {d:3d} = {'×'.join(str(f) for f in fs)}")

# The E-type denominators
print(f"\n  E-type denominators: 13, 19, 31")
print(f"  Differences: 19-13 = 6 = C₂, 31-19 = 12 = 2C₂")
print(f"  Ratios: 19/13, 31/19 (not simple)")
print(f"  Sum: 13+19+31 = 63 = 2^C₂ - 1 = 2^6 - 1")

s = 13 + 19 + 31
print(f"\n  ★ 13 + 19 + 31 = {s} = 2^6 - 1 = 2^C₂ - 1")
print(f"    The E-type denominators sum to the Mersenne number at C₂!")

# Also: 63 = 9 × 7 = c₄ × g
print(f"    = 9 × 7 = c₄ × g")
print(f"    = 21 × 3 = dim(B₃) × N_c")
print(f"    = 63 = |A₆| ... no, |A₆| = 360")

# ═══════════════════════════════════════════════════════════════════
# Section 10: The magic square connection
# ═══════════════════════════════════════════════════════════════════

print("\n\n§10. FREUDENTHAL-TITS MAGIC SQUARE")
print("-" * 50)

print("""
  The Freudenthal-Tits magic square relates:
  - Division algebras: R, C, H, O
  - Exceptional Lie algebras

  For the row R⊗O:
    A₁ = su(2),  C₃ = sp(6),  A₅ = su(6),  E₆
    dim:  3        21          35          78

  For the row C⊗O:
    A₂ = su(3),  A₅ = su(6),  D₆ = so(12),  E₇
    dim:  8        35          66            133

  For the row H⊗O:
    C₃ = sp(6),  D₆ = so(12),  B₆ = so(13),  E₈? ...

  Actually the standard magic square:
         R    C    H    O
    R:  A₁   A₂   C₃   F₄
    C:  A₂   A₂²  A₅   E₆
    H:  C₃   A₅   D₆   E₇
    O:  F₄   E₆   E₇   E₈

  Note: so(12) = D₆ appears in the H×C slot!
  And E₆ appears in the C×O slot!
  Both are c=6 models at level 1!

  ★ The magic square places our c=6 models:
    so(12) at (H,C) position — quaternion-complex
    E₆ at (C,O) position — complex-octonion
    sp(8) is NOT in the magic square (C₄ ≠ C₃)
    su(7) is NOT in the magic square

  The magic square algebras with c=6 at level 1:
    so(12)₁ and E₆₁ — related by the quaternion-octonion exchange
""")

# ═══════════════════════════════════════════════════════════════════
# Section 11: E₆ and the 27-dim rep
# ═══════════════════════════════════════════════════════════════════

print("\n§11. E₆ AND THE 27")
print("-" * 50)

print(f"\n  E₆ has a 27-dimensional fundamental representation")
print(f"  27 = d₂(Q⁵) = multiplicity of second eigenvalue of Q⁵!")
print(f"  [From Toy 146: d₂ = C(6,4)×9/5 = 27]")
print()
print(f"  In BST: d₂ = 27 = m_s/m̂ (strange quark mass ratio)")
print(f"  In E₆ GUTs: 27 = fundamental representation")
print()
print(f"  ★ The E₆ fundamental dimension equals the BST spectral multiplicity d₂")
print(f"    This links the GUT representation to Q⁵ spectral geometry")

# dim of other E₆ reps
print(f"\n  E₆ representations:")
print(f"    1   (trivial)")
print(f"    27  (fundamental) = d₂")
print(f"    27̄  (conjugate)")
print(f"    78  (adjoint) = dim(E₆) = C₂ × c₃")
print(f"    351 (symmetric²)")
print(f"    351' (antisymmetric²)")

# Check 78 = 6 × 13
print(f"\n  dim(E₆) = 78 = {6} × {13} = C₂ × c₃")
print(f"  dim(E₇) = 133 = {7} × {19} = g × 19")
print(f"  dim(E₈) = 248 = {8} × {31} = 2^N_c × M₅")

# ═══════════════════════════════════════════════════════════════════
# Section 12: The N_max connection
# ═══════════════════════════════════════════════════════════════════

print("\n\n§12. CONNECTION TO N_max = 137")
print("-" * 50)

# 248 - 78 = 170
# 248 - 133 = 115
# 133 - 78 = 55 = C(11,2) = C(c₂, 2)

print(f"  Dimension differences:")
print(f"    dim(E₈) - dim(E₇) = 248 - 133 = 115")
print(f"    dim(E₇) - dim(E₆) = 133 - 78  = 55 = C(c₂, 2) = T_{10}")
print(f"    dim(E₈) - dim(E₆) = 248 - 78  = 170")
print()

# 55 = C(11,2) = triangular number of 10
print(f"  55 = C(11,2) = C(c₂, r) = T_{{10}} = T_{{d_R}}")
print(f"  where d_R = 10 = real dimension of Q⁵")
print()
print(f"  170 = 2 × 85 = 2 × 5 × 17")
print(f"  115 = 5 × 23")

# N_max = 137: does it connect?
# 248 + 137 = 385
# 248 - 137 = 111 = 3 × 37
# 133 + 137 = 270
# 78 + 137 = 215 = 5 × 43

# More interesting: 137 = H₅ numerator = α⁻¹ integer
# E₈ root system: 240 roots
# 240 + 137 = 377 = 13 × 29
# 240 - 137 = 103 (prime)

# ═══════════════════════════════════════════════════════════════════
# Section 13: Synthesis
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 72)
print("§13. SYNTHESIS")
print("═" * 72)

print("""
  THE EXCEPTIONAL CHAIN:

  1. E₆-E₇-E₈ at level 1: c = (6, 7, 8) = (C₂, g, 2^{N_c})
     Sum = 21 = dim(B₃) = dim(C₃)
     Product = 336 = 2^{N_c} × P(1) = 8 × 42

  2. dim(E_n) = c(E_n) × (1+h∨) = rank × (1+h∨)
     dim(E₆) = 6 × 13 = C₂ × c₃
     dim(E₇) = 7 × 19 = g × 19
     dim(E₈) = 8 × 31 = 2^{N_c} × (2^{n_C}-1)

  3. E-type denominator sum: 13 + 19 + 31 = 63 = 2^{C₂} - 1

  4. Deligne's series SKIPS c = 3 and c = 5 (= N_c and n_C)
     These come from level 2 (so(7)₂) and level 2 Langlands pair
     The exceptional route hits c ≥ 6 = C₂

  5. 27 of E₆ = d₂(Q⁵) = spectral multiplicity = m_s/m̂
     The GUT fundamental IS a BST spectral multiplicity

  6. 91 total integrable reps = g × c₃ = T_{c₃} = C(2g, 2)
     Triangular number of the 3rd Chern class

  7. E₆ and so(12) in the Freudenthal magic square
     = (C, O) and (H, C) positions
     Two of the four level-1 c=6 models come from the magic square

  ★ The exceptional Lie algebras are the "high road" to the mass gap.
    They access c = C₂ through rank-level coincidence at level 1.
    The "low road" is the physical algebra so(7) at level 2.
    Both roads meet at c = 6 = C₂.
""")

print("═" * 72)
print("TOY 182 COMPLETE")
print("  E₆-E₇-E₈ triple: c = (C₂, g, 2^N_c), sum = dim(B₃)")
print("  Denominator sum: 13+19+31 = 63 = 2^C₂ - 1")
print("  27 of E₆ = d₂(Q⁵) spectral multiplicity")
print("  91 total reps = g × c₃ = T_{c₃}")
print("═" * 72)
