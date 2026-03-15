#!/usr/bin/env python3
"""
TOY 180: ANATOMY OF THE MASS GAP
=================================

The mass gap c = C₂ = 6 can be decomposed into BST-integer pieces
via cosets. Casey: "The whole is 6, and it breaks into 5+1, or
4/3+14/3, or 2+4, or 9/2+3/2."

This toy maps the COMPLETE internal structure of c = 6.
Every decomposition is a different way of seeing the mass gap.

Casey Koons, March 16, 2026
"""

from fractions import Fraction
from itertools import combinations

print("=" * 72)
print("TOY 180: ANATOMY OF THE MASS GAP")
print("=" * 72)

def wzw_c(dim_g, h_dual, level):
    return Fraction(level * dim_g, level + h_dual)

# ═══════════════════════════════════════════════════════════════════
# Section 1: All decompositions of c = 6
# ═══════════════════════════════════════════════════════════════════

print("\n§1. DECOMPOSITIONS OF c = C₂ = 6")
print("-" * 50)

# The coset decompositions from Toy 178:
decompositions = [
    ("so(7)₂/su(3)₂", "su(3)₂", Fraction(14, 5), Fraction(16, 5),
     "G₂₁ + color at BST level"),
    ("so(7)₂/su(2)₂", "su(2)₂", Fraction(9, 2), Fraction(3, 2),
     "so(9)₁ + ..."),
    ("so(7)₂/G₂₂", "G₂₂", Fraction(4, 3), Fraction(14, 3),
     "tri-critical Ising + G₂"),
    ("so(7)₂/so(5)₂", "so(5)₂", Fraction(2), Fraction(4),
     "rank + baby physical"),
    ("so(7)₂ = all", "—", Fraction(6), Fraction(0),
     "the whole mass gap"),
]

print(f"\n  {'Coset':30s}  {'c₁':>6s}  {'c₂':>6s}  {'sum':>4s}  Interpretation")
print(f"  {'─'*30}  {'──':>6s}  {'──':>6s}  {'───':>4s}  {'─'*30}")
for name, sub, c1, c2, interp in decompositions:
    print(f"  {name:30s}  {str(c1):>6s}  {str(c2):>6s}  {str(c1+c2):>4s}  {interp}")

# ═══════════════════════════════════════════════════════════════════
# Section 2: BST content of each piece
# ═══════════════════════════════════════════════════════════════════

print("\n\n§2. BST CONTENT OF EACH PIECE")
print("-" * 50)

bst_values = {
    Fraction(1): "su(2)₁, 1",
    Fraction(2): "r = rank",
    Fraction(3): "N_c = colors, n_C(Q³)",
    Fraction(4): "C₂(Q³) = g(Q³)",
    Fraction(5): "n_C = complex dim",
    Fraction(6): "C₂ = mass gap",
    Fraction(7): "g = genus",
    Fraction(9): "c₄ = 4th Chern",
    Fraction(11): "c₂ = dim K",
    Fraction(13): "c₃ = 3rd Chern",
    Fraction(4, 3): "tri-critical Ising M(5,4)",
    Fraction(14, 5): "c(G₂₁) = 14/5",
    Fraction(16, 5): "c(su(3)₂) = 16/5",
    Fraction(14, 3): "c(G₂₂) = 14/3",
    Fraction(3, 2): "c(su(2)₂) = 3/2",
    Fraction(9, 2): "c(so(9)₁) = 9/2",
}

pieces = set()
for _, _, c1, c2, _ in decompositions:
    if c1 != 0:
        pieces.add(c1)
    if c2 != 0:
        pieces.add(c2)

print("\n  All pieces appearing in decompositions of c = 6:")
for p in sorted(pieces):
    bst = bst_values.get(p, "—")
    print(f"    c = {str(p):>6s} = {float(p):>6.3f}  [{bst}]")

# ═══════════════════════════════════════════════════════════════════
# Section 3: Integer decompositions of 6
# ═══════════════════════════════════════════════════════════════════

print("\n\n§3. INTEGER DECOMPOSITIONS: 6 = a + b")
print("-" * 50)

print("\n  All ways to write 6 = a + b with a ≤ b (integers):")
for a in range(1, 4):
    b = 6 - a
    a_bst = bst_values.get(Fraction(a), "")
    b_bst = bst_values.get(Fraction(b), "")
    print(f"    6 = {a} + {b}  [{a_bst}] + [{b_bst}]")

print("\n  BST meaning:")
print("    6 = 1 + 5  →  su(2)₁ + n_C")
print("    6 = 2 + 4  →  r + C₂(Q³)")
print("    6 = 3 + 3  →  N_c + N_c  (color doubled)")

# ═══════════════════════════════════════════════════════════════════
# Section 4: The c = 6 from DIFFERENT WZW models
# ═══════════════════════════════════════════════════════════════════

print("\n\n§4. SEVEN FACES OF THE MASS GAP")
print("-" * 50)

faces = [
    ("so(7)₂", 21, 5, 2, "B₃ physical", "ℓ+h∨ = g"),
    ("su(3)₉", 8, 3, 9, "Color at level 9", "h∨ = N_c"),
    ("su(7)₁", 48, 7, 1, "SU(7) at level 1", "h∨ = g"),
    ("so(12)₁", 66, 10, 1, "SO(12) at level 1", "ℓ+h∨ = c₂"),
    ("sp(8)₁", 36, 5, 1, "Sp(8) at level 1", "h∨ = n_C"),
    ("E₆₁", 78, 12, 1, "E₆ at level 1", "ℓ+h∨ = c₃"),
    ("G₂₃", 14, 4, 3, "G₂ exceptional", "ℓ+h∨ = g"),
]

print(f"\n  {'Model':12s} {'c':>4s} {'dim':>4s} {'h∨':>3s} {'ℓ+h∨':>5s}  BST tags")
print(f"  {'─'*12} {'──':>4s} {'───':>4s} {'──':>3s} {'────':>5s}  {'─'*25}")
for name, dim_g, h_dual, level, desc, tags in faces:
    c = wzw_c(dim_g, h_dual, level)
    print(f"  {name:12s} {str(c):>4s} {dim_g:>4d} {h_dual:>3d} {level+h_dual:>5d}  {tags}")

# Note the ℓ+h∨ values!
print("\n  ℓ+h∨ values: {", end="")
lph_values = sorted(set(level + h_dual for _, _, h_dual, level, _, _ in faces))
print(", ".join(str(v) for v in lph_values), end="}\n")
print(f"  = {{6, 7, 8, 11, 12, 13}} = {{C₂, g, 2^{'{N_c}'}, c₂, 2C₂, c₃}}")

# ═══════════════════════════════════════════════════════════════════
# Section 5: The ℓ+h∨ = BST integer dictionary
# ═══════════════════════════════════════════════════════════════════

print("\n\n§5. THE SHIFTED LEVEL DICTIONARY")
print("-" * 50)

print("""
  For each c = 6 model, the quantum parameter is q = e^{2πi/(ℓ+h∨)}:

  so(7)₂:   q = e^{2πi/7}   (7th roots = heptagonal geometry)
  G₂₃:      q = e^{2πi/7}   (SAME quantum parameter!)
  su(7)₁:   q = e^{2πi/8}   (8th roots)
  su(3)₉:   q = e^{2πi/12}  (12th roots = dodecagonal)
  so(12)₁:  q = e^{2πi/11}  (11th roots!)
  sp(8)₁:   q = e^{2πi/6}   (6th roots = hexagonal)
  E₆₁:      q = e^{2πi/13}  (13th roots!)
""")

print("  The quantum parameters sample roots of unity at:")
print("    {6, 7, 8, 11, 12, 13}")
print()
print("  Missing from BST integers: {2, 3, 5, 9}")
print("  Present: {6=C₂, 7=g, 11=c₂, 13=c₃}")
print("  Extra: {8=2^{N_c}, 12=2C₂}")
print()
print("  ★ The FOUR Chern class values {n_C, C₂, c₂, c₃} = {5, 6, 11, 13}")
print("    are NOT all quantum parameters")
print("  ★ But {C₂, g, c₂, c₃} = {6, 7, 11, 13} ARE (four of six)")
print("    These are the Chern values ≥ C₂")

# ═══════════════════════════════════════════════════════════════════
# Section 6: The dimension sum
# ═══════════════════════════════════════════════════════════════════

print("\n\n§6. DIMENSION SUMS")
print("-" * 50)

total_dim = sum(dim_g for _, dim_g, _, _, _, _ in faces)
print(f"  Sum of dimensions of all c=6 algebras:")
print(f"    {' + '.join(str(d) for _, d, _, _, _, _ in faces)} = {total_dim}")

# Factor total_dim
n = total_dim
factors = []
for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
    while n % p == 0:
        factors.append(p)
        n //= p
if n > 1:
    factors.append(n)
print(f"    = {' × '.join(str(f) for f in factors)}")

# Sum of h∨
total_h = sum(h_dual for _, _, h_dual, _, _, _ in faces)
print(f"\n  Sum of dual Coxeter numbers:")
print(f"    {' + '.join(str(h) for _, _, h, _, _, _ in faces)} = {total_h}")

# Sum of ℓ+h∨
total_lh = sum(level + h_dual for _, _, h_dual, level, _, _ in faces)
print(f"\n  Sum of ℓ+h∨:")
print(f"    {' + '.join(str(level+h) for _, _, h, level, _, _ in faces)} = {total_lh}")

# ═══════════════════════════════════════════════════════════════════
# Section 7: Multiplicative structure
# ═══════════════════════════════════════════════════════════════════

print("\n\n§7. MULTIPLICATIVE STRUCTURE")
print("-" * 50)

print("\n  Each c = 6 model has dim × level = dim(g) × ℓ / (ℓ+h∨) × (ℓ+h∨) = ...")
print("  Actually: c × (ℓ+h∨) = ℓ × dim(g)")
print()

for name, dim_g, h_dual, level, desc, _ in faces:
    prod = 6 * (level + h_dual)
    l_dim = level * dim_g
    print(f"  {name:12s}: C₂×(ℓ+h∨) = 6×{level+h_dual} = {prod} = {level}×{dim_g} = ℓ×dim")

# ═══════════════════════════════════════════════════════════════════
# Section 8: The product ℓ × dim for c = 6
# ═══════════════════════════════════════════════════════════════════

print("\n\n§8. THE ℓ×dim(g) = 6(ℓ+h∨) PRODUCTS")
print("-" * 50)

print("\n  Since c = ℓ·dim/(ℓ+h∨) = 6, we have ℓ·dim = 6(ℓ+h∨):")
for name, dim_g, h_dual, level, desc, _ in faces:
    prod = level * dim_g
    lph = level + h_dual
    print(f"  {name:12s}: ℓ·dim = {level}×{dim_g} = {prod} = 6×{lph}")
    # Factor
    n = prod
    fs = []
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        while n % p == 0:
            fs.append(p)
            n //= p
    if n > 1:
        fs.append(n)
    print(f"             = {'×'.join(str(f) for f in fs)}")

# ═══════════════════════════════════════════════════════════════════
# Section 9: Partition decompositions
# ═══════════════════════════════════════════════════════════════════

print("\n\n§9. c = 6 AS SUM OF MINIMAL MODEL VALUES")
print("-" * 50)

# Minimal model central charges: c = 1 - 6/[m(m+1)]
print("\n  Virasoro minimal model central charges c(m):")
for m in range(3, 15):
    c_mm = Fraction(1) - Fraction(6, m*(m+1))
    print(f"    M({m},{m-1}): c = 1 - 6/{m*(m+1)} = {c_mm} = {float(c_mm):.4f}")

# Can we write 6 as sum of minimal model c-values?
print("\n  Note: c(m) → 1 as m → ∞")
print("  So 6 = sum of 6 copies of c = 1 (large m limit)")
print("  = 6 free bosons!")
print()
print("  More interesting: 6 copies of c = 1 = 6 free bosons")
print("  This is the CENTRAL CHARGE of 6 free bosons on a circle")
print("  6 = C₂ = dim_{complex}(Q⁵) + 1 = n_C + 1")
print()
print("  The mass gap IS six bosonic degrees of freedom")

# ═══════════════════════════════════════════════════════════════════
# Section 10: The c = 6 = 1+1+1+1+1+1 decomposition
# ═══════════════════════════════════════════════════════════════════

print("\n\n§10. THE FREE BOSON DECOMPOSITION")
print("-" * 50)

print("""
  c = 6 = 6 × 1 = six free bosons

  These six bosons correspond to:
  - 5 = n_C compact coordinates on Q⁵ (the Bergman kernel modes)
  - 1 = the non-compact (time-like) direction

  This is the 5+1 = n_C + 1 decomposition:
    6 = n_C + 1 = complex dimension + reality

  In the WZW language:
    so(7)₂ = n_C compact bosons + 1 non-compact boson

  The mass gap C₂ = n_C + 1 = "geometry + existence"
""")

# ═══════════════════════════════════════════════════════════════════
# Section 11: The sum c(G) + c(^LG) = 13 = c₃
# ═══════════════════════════════════════════════════════════════════

print("\n§11. THE SUM c(G) + c(^LG) = c₃")
print("-" * 50)

c_G = Fraction(6)
c_L = Fraction(7)
c_sum = c_G + c_L
print(f"\n  c(so(7)₂) + c(sp(6)₂) = {c_G} + {c_L} = {c_sum}")
print(f"  = c₃ = 13 = 3rd Chern class of Q⁵")
print()
print(f"  The physical + L-group central charges sum to c₃!")
print()

# Is this universal?
print("  Check universality:")
for N in range(2, 8):
    dim_BC = N * (2*N + 1)
    h_B = 2*N - 1
    h_C = N + 1
    c_B = wzw_c(dim_BC, h_B, 2)
    c_C = wzw_c(dim_BC, h_C, 2)
    s = c_B + c_C
    n = 2*N - 1
    # What Chern class would this be?
    # c₃ for Q⁵ = 13, what's c₃ for Q^n?
    # c_k = sum of k-element products of Chern roots (1,1,1,1,1) for Q⁵
    # For general Q^n with roots (1,...,1,2), the Chern classes are known
    print(f"  N={N}: c(B) + c(C) = {c_B} + {c_C} = {s} = {float(s):.4f}")

# ═══════════════════════════════════════════════════════════════════
# Section 12: The product c(G) × c(^LG) = 42 revisited
# ═══════════════════════════════════════════════════════════════════

print("\n\n§12. PRODUCT AND SUM TOGETHER")
print("-" * 50)

print(f"""
  For BST (N=3):
    c(G) + c(^LG) = 6 + 7 = 13 = c₃     (SUM)
    c(G) × c(^LG) = 6 × 7 = 42 = P(1)   (PRODUCT)

  So C₂ and g are roots of:
    x² - 13x + 42 = 0
    x² - c₃·x + P(1) = 0

  Solving: x = (13 ± √(169-168))/2 = (13 ± 1)/2
  → x = 7 or x = 6 ✓

  Discriminant = c₃² - 4·P(1) = 169 - 168 = 1

  ★ THE CONSECUTIVE INTEGER THEOREM:
    C₂ and g are consecutive BECAUSE the discriminant is 1.
    c₃² - 4·P(1) = 1  ←→  C₂ and g are consecutive integers

  Check: c₃² = 169, 4·P(1) = 168
  169 - 168 = 1 ✓

  This is EQUIVALENT to: c₃ = C₂ + g = 2C₂ + 1 = 2g - 1
  and P(1) = C₂ · g.
""")

# Verify c₃² - 4P(1) = 1 is specific to n=5
print("  Check for other Q^n:")
for N in range(2, 8):
    dim_BC = N * (2*N + 1)
    h_B = 2*N - 1
    h_C = N + 1
    c_G_val = wzw_c(dim_BC, h_B, 2)
    c_L_val = wzw_c(dim_BC, h_C, 2)
    s = c_G_val + c_L_val
    p = c_G_val * c_L_val
    disc = s * s - 4 * p
    n_C = 2*N - 1
    check = "= 1 ✓" if disc == 1 else f"= {disc}"
    print(f"  N={N} (Q^{n_C}): sum² - 4·prod = {s}² - 4×{p} = {s*s} - {4*p} {check}")

# ═══════════════════════════════════════════════════════════════════
# Section 13: The discriminant-1 theorem
# ═══════════════════════════════════════════════════════════════════

print("\n\n§13. THE DISCRIMINANT-1 THEOREM")
print("=" * 50)

print("""
  THEOREM: c(G)₂ and c(^LG)₂ are consecutive integers if and only if
  the discriminant Δ = [c(G)+c(^LG)]² - 4·c(G)·c(^LG) = 1.

  For general N:
    c(G) = 2N(2N+1)/(2N+1) = 2N
    c(^LG) = 2N(2N+1)/(N+3)

    Sum = 2N + 2N(2N+1)/(N+3) = 2N[1 + (2N+1)/(N+3)]
        = 2N[(N+3+2N+1)/(N+3)] = 2N(3N+4)/(N+3)

    Product = 2N × 2N(2N+1)/(N+3) = 4N²(2N+1)/(N+3)

    Δ = [2N(3N+4)/(N+3)]² - 4·4N²(2N+1)/(N+3)
      = 4N²/((N+3)²) × [(3N+4)² - 4(2N+1)(N+3)]
      = 4N²/((N+3)²) × [9N²+24N+16 - 8N²-28N-12]
      = 4N²/((N+3)²) × [N²-4N+4]
      = 4N²(N-2)²/(N+3)²

  So Δ = [2N(N-2)/(N+3)]²

  Setting Δ = 1:
    2N(N-2)/(N+3) = ±1
    2N²-4N = ±(N+3)

  Case +: 2N²-5N-3 = 0 → N = (5±√(25+24))/4 = (5±7)/4
          N = 3 or N = -1/2

  Case -: 2N²-3N+3 = 0 → discriminant = 9-24 = -15 < 0
          No real solutions

  ★ Δ = 1 UNIQUELY at N = 3.

  For N=2: Δ = 4×4×0/(25) = 0 (self-dual! consecutive = identical!)
  For N=3: Δ = 4×9×1/(36) = 1 (consecutive!)
  For N=4: Δ = 4×16×4/(49) = 256/49 (not a perfect square)
""")

# Verify
print("  Verification:")
for N in range(2, 8):
    delta = Fraction(4 * N * N * (N-2) * (N-2), (N+3) * (N+3))
    print(f"    N={N}: Δ = 4×{N}²×{N-2}²/{N+3}² = {delta} = {float(delta):.4f}")

# ═══════════════════════════════════════════════════════════════════
# Section 14: Synthesis
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "═" * 72)
print("§14. SYNTHESIS: THE INTERNAL STRUCTURE OF THE MASS GAP")
print("═" * 72)

print("""
  The mass gap C₂ = 6 has rich internal structure:

  1. SEVEN WZW models realize it (seven = g = genus)
     Each with ℓ+h∨ encoding BST integers: {6,7,8,11,12,13}

  2. COSET DECOMPOSITIONS give BST-integer pieces:
     6 = 5 + 1 = n_C + 1              [geometry + existence]
     6 = 2 + 4 = r + C₂(Q³)           [rank + baby gap]
     6 = 4/3 + 14/3                    [Ising + octonions]
     6 = 9/2 + 3/2                     [so(9) + ...]

  3. FREE BOSON: c = 6 = six free bosons = 5 compact + 1 non-compact
     The mass gap IS the counting of available directions

  4. CONSECUTIVE INTEGER THEOREM:
     c(G) + c(^LG) = c₃ = 13     [sum = Chern class]
     c(G) × c(^LG) = P(1) = 42   [product = Chern polynomial]
     c₃² - 4P(1) = 169 - 168 = 1 [discriminant = 1]

     x² - c₃x + P(1) = 0 has roots C₂ = 6 and g = 7

     ★ DISCRIMINANT = 1 UNIQUELY AT N = 3
     This is the 13th uniqueness condition

  5. SELF-DUALITY BREAKING:
     N=2: Δ = 0 (self-dual, C₂ = g)
     N=3: Δ = 1 (first non-trivial, C₂ ≠ g)
     N≥4: Δ > 1 (too separated)

     The Standard Model sits at the THRESHOLD of duality breaking.
""")

print("═" * 72)
print("TOY 180 COMPLETE")
print("  Mass gap anatomy: 7 faces, 4 decompositions, 6 bosons")
print("  Discriminant-1 theorem: Δ = [2N(N-2)/(N+3)]² = 1 iff N=3")
print("  13th uniqueness: C₂ and g consecutive iff N=3")
print("  Quadratic: x² - c₃x + P(1) = 0 → (C₂, g) = (6, 7)")
print("═" * 72)
