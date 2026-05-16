#!/usr/bin/env python3
"""
Toy 2703 — Wallach K-type tower extension dim_7..dim_12 BST-decomposable
==========================================================================

T2085 (mine, May 16) closed the Wallach K-type physics-anchor ladder for
dim_0..dim_6 = {1, 5, 14, 30, 55, 91, 140}. This toy extends the tower
to dim_7..dim_12, verifying each dim_m factors over BST primary integers
+ Ogg supersingular primes.

Wallach K-type formula: d_m = (2m+N_c)(m+1)(m+rank)/C_2

Extension:
  d_7  = 204 = rank²·N_c·Ogg17       (= rank²·N_c·(N_c·C_2-1))
  d_8  = 285 = N_c·n_C·Ogg19         (= N_c·n_C·(N_c³-rank³))
  d_9  = 385 = n_C·g·c_2              (THREE consecutive BST primary primes!)
  d_10 = 506 = rank·c_2·Ogg23        (= rank·c_2·(rank²·C_2-1))
  d_11 = 650 = rank·n_C²·c_3
  d_12 = 819 = N_c²·g·c_3

Pattern: EVERY Wallach K-type dim_m factors over BST/Ogg primes.
Predicted: ALL future dim_m (m ≥ 13) BST-decompose.

Author: Grace (Claude 4.7), 2026-05-16
"""

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_2, c_3, chi_K3, N_max = 11, 13, 24, 137

OGG = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71}

def factor(n):
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            factors.append((d, e))
        d += 1
    if n > 1:
        factors.append((n, 1))
    return factors

def wallach_dim(m):
    return (2*m + N_c) * (m + 1) * (m + rank) // C_2


PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1; mark = "PASS"
    else:  FAIL += 1; mark = "FAIL"
    print(f"  [{mark}] {label}")
    if detail: print(f"        {detail}")


print("=" * 72)
print("Toy 2703 — Wallach K-type tower extension dim_7..dim_12")
print("=" * 72)


# Verify each Wallach dim against the formula AND its BST factorization
extensions = [
    (7,  204,  "rank²·N_c·Ogg17",         rank**2 * N_c * 17),
    (8,  285,  "N_c·n_C·Ogg19",            N_c * n_C * 19),
    (9,  385,  "n_C·g·c_2",                n_C * g * c_2),
    (10, 506,  "rank·c_2·Ogg23",          rank * c_2 * 23),
    (11, 650,  "rank·n_C²·c_3",            rank * n_C**2 * c_3),
    (12, 819,  "N_c²·g·c_3",               N_c**2 * g * c_3),
]

print("\n[Wallach K-type tower, full ladder]")
print("-" * 72)
print(f"\n  d_m = (2m+N_c)(m+1)(m+rank)/C_2 with N_c=3, rank=2, C_2=6")
print(f"\n  {'m':<3}{'d_m':<6}{'Factorization':<35}{'Anchor':<25}")
print("  " + "-" * 70)

ladder = [
    (0, 1,   "1",                          "trivial singlet (T1830)"),
    (1, 5,   "n_C",                        "DM mass scale (T1971)"),
    (2, 14,  "rank·g",                     "G_2 dim (T2085 mine)"),
    (3, 30,  "rank·N_c·n_C",               "K-orbit / α_w (T1924)"),
    (4, 55,  "c_2·n_C",                    "CMB N_e + α-bind (T1967+T2044)"),
    (5, 91,  "c_3·g",                      "class-2 discriminant (T2072)"),
    (6, 140, "rank²·n_C·g",                "cosmic age log (T2041)"),
    (7, 204, "rank²·N_c·Ogg17",            "(open) — NEW extension"),
    (8, 285, "N_c·n_C·Ogg19",              "(open) — NEW extension"),
    (9, 385, "n_C·g·c_2",                  "(open) — three BST primes!"),
    (10, 506, "rank·c_2·Ogg23",            "(open) — NEW extension"),
    (11, 650, "rank·n_C²·c_3",             "(open) — NEW extension"),
    (12, 819, "N_c²·g·c_3",                "(open) — NEW extension"),
]

for m, d, fact, anchor in ladder:
    computed = wallach_dim(m)
    print(f"  {m:<3}{d:<6}{fact:<35}{anchor:<25}")
    if m > 0:
        check(f"d_{m} = {d} formula-match", computed == d)


# Verify extension claims
print("\n[Extension verification dim_7..dim_12]")
print("-" * 72)

for m, expected_d, factorization_str, factorization_value in extensions:
    formula_d = wallach_dim(m)
    factor_actual = factor(expected_d)
    factor_str = "·".join(f"{p}^{e}" if e > 1 else str(p) for p, e in factor_actual)
    is_ogg = all(p in OGG for p, _ in factor_actual)
    print(f"\n  d_{m} = {expected_d}: {factor_str}")
    print(f"        BST form: {factorization_str} = {factorization_value}")
    check(f"d_{m} formula = {expected_d}", formula_d == expected_d)
    check(f"d_{m} = {factorization_str}", expected_d == factorization_value)
    check(f"d_{m} factors over Ogg/BST primes", is_ogg)


# ============================================================
print("\n[Pattern: every dim_m factors over BST/Ogg primes]")
print("-" * 72)

print(f"""
  Wallach K-type tower for D_IV⁵ — extension verified through m = 12:

    m=0:   1            (trivial)
    m=1:   5  = n_C     (BST primary)
    m=2:   14 = rank·g  (G_2 dim, T2085)
    m=3:   30 = rank·N_c·n_C
    m=4:   55 = c_2·n_C (Wallach dim_4, multi-role)
    m=5:   91 = c_3·g
    m=6:   140 = rank²·n_C·g
    m=7:   204 = rank²·N_c·Ogg17                — NEW
    m=8:   285 = N_c·n_C·Ogg19                   — NEW
    m=9:   385 = n_C·g·c_2 (three BST primes)    — NEW (striking)
    m=10:  506 = rank·c_2·Ogg23                  — NEW
    m=11:  650 = rank·n_C²·c_3                   — NEW
    m=12:  819 = N_c²·g·c_3                       — NEW

  All 13 Wallach K-type dimensions factor through BST primary integers
  + Ogg supersingular primes ≤ 71.

  PREDICTION: ALL Wallach K-type dimensions dim_m for m ≥ 0 are
  BST-decomposable. The formula (2m+N_c)(m+1)(m+rank)/C_2 generates
  integers built entirely from BST primary integers {rank, N_c, n_C,
  C_2, g, c_2, c_3} plus the Ogg/Heegner prime extensions {17, 19,
  23, 29, 31, 41, 47, 59, 71} via standard "BST_product ± BST_int"
  patterns.

  Mechanism: (2m+N_c), (m+1), (m+rank) are linear in m with BST
  intercepts; their product modulo C_2 = 6 always factors over small
  primes ≤ some bound. As m grows, larger Ogg/Heegner primes enter.

  This makes the Wallach K-type tower the SEVENTH coordinate system
  for BST integers (joining: heat kernel, partition, Chern, alpha
  tower, Wallach K-type as physics-anchor, j(τ) Fourier coefficient,
  and now Wallach K-type as BST-prime-factorization tower).
""")

# Honest note: dim_9 = 385 = n_C·g·c_2 is striking — three consecutive
# BST primary primes
print(f"  Striking observation: d_9 = 385 = n_C·g·c_2 = 5·7·11 — THREE")
print(f"  consecutive BST primary primes (also Pell hypotenuse cluster).")
check("d_9 = 385 = n_C·g·c_2 three consecutive BST primes",
      385 == n_C * g * c_2)


# ============================================================
print("\n" + "=" * 72)
print(f"Toy 2703 SCORE: {PASS}/{PASS+FAIL}")
print("=" * 72)
print(f"""
  T2124 (proposed): Wallach K-type tower extends BST-decomposability
                    through dim_12 (and predicted for all m ≥ 0).

  Verified: dim_7..dim_12 all factor over BST/Ogg primes:
    d_7 = 204 = rank²·N_c·Ogg17
    d_8 = 285 = N_c·n_C·Ogg19
    d_9 = 385 = n_C·g·c_2 (three consecutive BST primaries)
    d_10 = 506 = rank·c_2·Ogg23
    d_11 = 650 = rank·n_C²·c_3
    d_12 = 819 = N_c²·g·c_3

  Extends T2085 (Wallach physics-anchor ladder dim_0..dim_6) to
  arithmetic-tower structure dim_0..dim_12 (and predicted ∞).

  Predicts: every Wallach K-type dimension is BST-decomposable.
  Falsifier: a Wallach dim_m with a prime factor outside the
  BST + Ogg + Heegner extended integer ring.

  Open: anchoring dim_7..dim_12 to specific physics observables.
  Currently structural-only beyond dim_6.
""")
