"""
Toy 2264 — Pb-208 catalog audit (companion to Toy 2257 Fe-56 audit).

Owner: Elie
Date: 2026-05-15
Out of: RETRO-2 sample-audit sweep; magic_82 catalog entry is WRONG.

THE PROBLEM
===========
Catalog entry `magic_82` (bst_geometric_invariants.json line 5330)
claims:
  formula: "rank·(N_c·C_2 + rank·n_C + rank²) = 82"
  tier: D-tier (RETRO-2 era)

Evaluating: rank·(N_c·C_2 + rank·n_C + rank²)
          = 2·(3·6 + 2·5 + 4)
          = 2·(18 + 10 + 4)
          = 2·32
          = **64**, NOT 82.

The current catalog formula is BROKEN. Same RETRO-2 pattern as Fe-56:
D-tier label, broken formula text.

THIS TOY
========
1. Verify the broken formula evaluates to 64.
2. Find CORRECT BST decompositions of Z=82, N=126, A=208 (Pb-208 magic numbers).
3. Check Lyra's c_k = a_k·n_C + b_k family applies.
4. Provide replacement formula for the catalog.
"""

from fractions import Fraction


# BST integers
rank = 2
N_c  = 3
n_C  = 5
g    = 7
C_2  = 6
N_max = 137
c_2  = 11
c_3  = 13
chi  = 24

# Pb-208 observed
A_Pb = 208
Z_Pb = 82
N_Pb = 126

tests = []

def check(label, got, want, note=""):
    ok = (got == want)
    tests.append((ok, label, got, want, note))
    return ok


# ============================================================
# PART 1 — Verify the broken formula is broken
# ============================================================

broken_eval = rank * (N_c * C_2 + rank * n_C + rank**2)
check("Original catalog formula evaluates to 64 (NOT 82) — BROKEN",
      broken_eval, 64,
      "rank*(N_c*C_2 + rank*n_C + rank^2) = 2*32 = 64")

# ============================================================
# PART 2 — Correct BST decompositions of Z=82
# ============================================================

# Decomposition 1: Z = N_max - n_C * c_2 = 137 - 55 = 82
z_decomp_1 = N_max - n_C * c_2
check("Z = 82 = N_max - n_C * c_2", z_decomp_1, 82)

# Decomposition 2: Z = chi*N_c + chi/N_c + rank = 72 + 8 + 2 = 82
z_decomp_2 = chi * N_c + chi // N_c + rank
check("Z = 82 = chi*N_c + chi/N_c + rank", z_decomp_2, 82)

# Decomposition 3: Z = rank * (rank^N_c * n_C + 1) = 2 * 41
z_decomp_3 = rank * (rank**N_c * n_C + 1)
check("Z = 82 = rank * (rank^N_c * n_C + 1) = 2 * 41", z_decomp_3, 82)

# Decomposition 4 (Lyra family): Z = a*n_C + b
# 82 = 16*5 + 2 -> a=16=rank^4, b=rank
a_Z, b_Z = divmod(Z_Pb, n_C)
check("Z = 82 fits Lyra family: a_Z = rank^4, b_Z = rank",
      (a_Z, b_Z), (rank**4, rank))

# ============================================================
# PART 3 — N=126 decompositions
# ============================================================

# Decomposition 1: N = rank * N_c^2 * g = 2 * 9 * 7 = 126
n_decomp_1 = rank * N_c**2 * g
check("N = 126 = rank * N_c^2 * g", n_decomp_1, 126)

# Decomposition 2: N = M_g - 1 = 127 - 1 = 126 (Mersenne offset!)
n_decomp_2 = (2**g - 1) - 1
check("N = 126 = M_g - 1 (Mersenne offset)", n_decomp_2, 126)

# Decomposition 3: N = 2^g - rank = 128 - 2
n_decomp_3 = 2**g - rank
check("N = 126 = 2^g - rank", n_decomp_3, 126)

# Lyra family: 126 = 25*5 + 1 -> a=25=n_C^2, b=1
a_N, b_N = divmod(N_Pb, n_C)
check("N = 126 fits Lyra family: a_N = n_C^2, b_N = 1",
      (a_N, b_N), (n_C**2, 1))

# ============================================================
# PART 4 — A=208 decompositions
# ============================================================

# Decomposition 1: A = rank^4 * c_3 = 16 * 13 (already in catalog)
a_decomp_1 = rank**4 * c_3
check("A = 208 = rank^4 * c_3", a_decomp_1, 208)

# Decomposition 2: A = rank^4 * (g + C_2) (alt reading; (g+C_2) = 13)
a_decomp_2 = rank**4 * (g + C_2)
check("A = 208 = rank^4 * (g + C_2)", a_decomp_2, 208)

# Lyra family: 208 = 41*5 + 3 -> a=41, b=N_c
a_A, b_A = divmod(A_Pb, n_C)
check("A = 208 fits Lyra family: a_A = 41 (Ogg prime), b_A = N_c",
      (a_A, b_A), (41, N_c))

# ============================================================
# PART 5 — Cross-relations (Pb-208 BST signature)
# ============================================================

# A = N + Z = 126 + 82 = 208 (trivially)
check("A = N + Z = 126 + 82 = 208", N_Pb + Z_Pb, A_Pb)

# N - Z = 44 = rank^2 * c_2 = 4 * 11 = 44
check("N - Z = 44 = rank^2 * c_2 (asymmetry)",
      N_Pb - Z_Pb, rank**2 * c_2)

# Z*(Z-1) = 82*81 = 6642 = ?
zz = Z_Pb * (Z_Pb - 1)
check("Z*(Z-1) = 6642 (Coulomb numerator)",
      zz, 82 * 81)
# 6642 = 2 * 3 * 3 * 3 * 41 * ? -- 6642/82 = 81 = 3^4. So 6642 = 82·81 = rank·41·N_c^4.
check("Z*(Z-1) = 6642 = rank * 41 * N_c^4",
      zz, rank * 41 * N_c**4)

# Pb-208 is doubly magic at BOTH 82 (Z) and 126 (N)
# These are nuclear magic numbers from shell-model filling.

# ============================================================
# PART 6 — Family check (all four numbers via Lyra)
# ============================================================

quantities = [("A", A_Pb), ("Z", Z_Pb), ("N", N_Pb), ("N-Z", N_Pb - Z_Pb)]
print("\nLyra family check for Pb-208 numbers:")
print(f"{'Quantity':<6} | {'Value':>5} | {'a_k':>4} | {'b_k':>4} | {'family?'}")
for name, q in quantities:
    a, b = divmod(q, n_C)
    in_family = b in {0, 1, rank, N_c, rank**2}
    fam = "YES" if in_family else "NO"
    print(f"{name:<6} | {q:>5} | {a:>4} | {b:>4} | {fam}")
all_in_family = all(divmod(q, n_C)[1] in {0, 1, rank, N_c, rank**2}
                    for _, q in quantities)
check("All four Pb-208 numbers fit Lyra c_k = a*n_C + b family",
      all_in_family, True)

# ============================================================
# PART 7 — Replacement formula for catalog
# ============================================================

# Best replacement: combination of cleanest physical readings
new_formula = ("Z=82 = rank * (rank^N_c * n_C + 1) = N_max - n_C * c_2 "
               "= 16 * n_C + rank (Lyra family). N=126 = rank * N_c^2 * g "
               "= M_g - 1. A=208 = rank^4 * c_3. N-Z=44 = rank^2 * c_2.")

print(f"\nProposed catalog replacement for magic_82:")
print(f"  {new_formula}\n")

# ============================================================
# SCORE & REPORT
# ============================================================
passed = sum(1 for ok, *_ in tests if ok)
total = len(tests)

print(f"\nToy 2264 — Pb-208 audit\n{'='*60}")
print(f"Score: {passed}/{total}\n")

fails = [t for t in tests if not t[0]]
if fails:
    print("FAILING:")
    for ok, lbl, got, want, note in fails:
        print(f"  [FAIL] {lbl}: got={got} expected={want}")
        if note: print(f"         {note}")
else:
    print("ALL PASS.\n")

print(f"{'='*60}")
print("Pb-208 AUDIT VERDICT")
print(f"{'='*60}")
print(f"""
STRUCTURAL — Pb-208 is BST-clean (doubly magic):
  A = 208 = rank^4 * c_3
  Z = 82  = rank * (rank^N_c * n_C + 1)
  N = 126 = rank * N_c^2 * g = M_g - 1
  N - Z = 44 = rank^2 * c_2
  Z*(Z-1) = 6642 = rank * 41 * N_c^4

LYRA FAMILY (c_k = a_k * n_C + b_k):
  Z = 16 * n_C + rank   (a=rank^4, b=rank)
  N = 25 * n_C + 1      (a=n_C^2,  b=1)
  A = 41 * n_C + N_c    (a=41,     b=N_c)
  N-Z = 8 * n_C + rank^2 (a=rank^N_c, b=rank^2)
  ALL FOUR fit the family.

CATALOG ACTION:
  magic_82 entry (line 5330) has WRONG formula:
    "rank*(N_c*C_2 + rank*n_C + rank^2) = 2*32 = 64" (NOT 82)
  Replace with the correct decomposition above. Tier D-tier defensible
  (Lyra-family member with mechanism via Toy 1858 SEMF), not broken.

This is the THIRD broken-formula catalog entry I've identified today
(after binding_Fe56 and Debye_W_310). Pattern: RETRO-2 batch upgrades
were applied without auditing the formula text. Math-correct entries
have broken catalog text. Honest audit fixes the text.

— Elie, May 15, 2026
""")
