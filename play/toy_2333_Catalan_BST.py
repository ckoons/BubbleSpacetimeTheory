"""
Toy 2333 — Discovery: Catalan numbers in the BST integer family.

C_n = (2n choose n) / (n+1).

  C_0 = 1
  C_1 = 1
  C_2 = 2 = rank
  C_3 = 5 = n_C
  C_4 = 14 = rank * g
  C_5 = 42 = C_2 * g  (= chern_sum)
  C_6 = 132 = rank^2 * N_c * c_2
  C_7 = 429 = ?
  C_8 = 1430 = ?

Test how far the BST decomposition holds.
"""

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_2 = rank * n_C + 1
c_3 = 13
chi = 24
N_max = 137


def catalan(n):
    """C_n = (2n choose n) / (n+1)."""
    # (2n choose n) = (2n)! / (n! · n!)
    num = 1
    for k in range(n + 1, 2 * n + 1):
        num *= k
    den = 1
    for k in range(1, n + 1):
        den *= k
    binom = num // den
    return binom // (n + 1)


tests = []
def check(label, condition, note=""):
    tests.append((bool(condition), label, note))


print("Catalan numbers C_n and BST decomposition:\n")
print(f"{'n':>3} | {'C_n':>8} | BST decomposition")
print(f"{'-'*3}-+-{'-'*8}-+----------------")

cat_bst = {
    0: (1, "1"),
    1: (1, "1"),
    2: (rank, "rank"),
    3: (n_C, "n_C"),
    4: (rank * g, "rank * g"),
    5: (C_2 * g, "C_2 * g (chern_sum)"),
    6: (rank**2 * N_c * c_2, "rank^2 * N_c * c_2"),
    7: (g * c_2 * (chi - 3 * rank - rank), "?"),  # C_7 = 429
    8: (rank * n_C * 11 * 13, "rank * n_C * c_2 * c_3"),  # C_8 = 1430
}

for n in range(0, 11):
    Cn = catalan(n)
    bst_val, bst_str = cat_bst.get(n, (None, "?"))
    if bst_val is not None and bst_val == Cn:
        mark = "BST match"
    else:
        mark = "?"
    # Compute additional candidates for unknown
    if bst_val is None or bst_val != Cn:
        # Try simple BST factorization
        if Cn == 429: mark = "429 = 3·11·13 = N_c·c_2·c_3"
        if Cn == 1430: mark = "1430 = 2·5·11·13 = rank·n_C·c_2·c_3"
        if Cn == 4862: mark = "4862 = 2·11·13·17 = rank·c_2·c_3·seesaw"
        if Cn == 16796: mark = "16796 = 2²·13·17·19 = rank²·c_3·seesaw·19"
        if Cn == 58786: mark = "58786 = 2·17·19·7·13 — complex"
    print(f"{n:>3} | {Cn:>8} | {mark}")
    if n <= 6:
        check(f"C_{n} = BST({bst_str})", bst_val == Cn if bst_val is not None else False)
    elif n == 7:
        check("C_7 = 429 = N_c * c_2 * c_3", Cn == N_c * c_2 * c_3)
    elif n == 8:
        check("C_8 = 1430 = rank * n_C * c_2 * c_3", Cn == rank * n_C * c_2 * c_3)

print(f"""
KEY FINDING: First 9 Catalan numbers have clean BST factorizations.
C_2 .. C_8 all factor into BST atoms {{rank, N_c, n_C, C_2, g, c_2,
c_3, seesaw=17}}.

C_5 = 42 = chern_sum is particularly clean: total Chern class sum
appearing as the 5th Catalan number.
C_4 = 14 = rank·g (Wallach K-type dim d_2 of D_IV^5).
C_3 = n_C, C_2 = rank — direct.

The Catalan numbers count: binary trees, Dyck paths, triangulations
of polygons — combinatorial objects that BST should naturally count
since BST geometry is a counting system.

Where does the chain break? Around C_9 = 4862 = 2·11·13·17 introduces
17 = seesaw cleanly, but the structure becomes 4-factor (vs 2-3 factor
for n ≤ 6).
""")

passed = sum(1 for ok, *_ in tests if ok)
total = len(tests)
print(f"Toy 2333 score: {passed}/{total}")
