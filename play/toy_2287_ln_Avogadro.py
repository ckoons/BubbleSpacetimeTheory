"""
Toy 2287 — Natural log of Avogadro: ln(N_A) = n_C * c_2 = 55.

N_A = 6.02214076e23 (exact, CODATA 2019).
ln(N_A) = ln(6.022e23) = 54.755.
BST: n_C * c_2 = 5 * 11 = 55. Match 0.45%.
c_2 = rank*n_C + 1 = 11.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_2 = rank * n_C + 1
N_A = 6.02214076e23
ln_obs = math.log(N_A)
ln_bst = n_C * c_2
err = abs(ln_bst - ln_obs) / ln_obs * 100
print(f"Toy 2287 — ln(N_A) = n_C * c_2 = 55")
print(f"  Observed: {ln_obs:.4f}  BST: {ln_bst}  err {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
