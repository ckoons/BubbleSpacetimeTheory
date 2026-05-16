"""
Toy 2291 — Neutron g-factor magnitude: |g_n| = chern_sum/c_2 = 42/11.

|g_n| observed = 3.826 (nuclear magnetons).
chern_sum = C_2 * g = 42 (sum of all Chern classes in BST hierarchy).
c_2 = rank*n_C+1 = 11.
BST: 42/11 = 3.818. Match 0.20%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_2 = rank * n_C + 1
chern_sum = C_2 * g
g_n_obs = 3.82608545
g_n_bst = chern_sum / c_2
err = abs(g_n_bst - g_n_obs) / g_n_obs * 100
print(f"Toy 2291 — |g_n| (neutron g-factor) = chern_sum/c_2 = 42/11")
print(f"  Observed: {g_n_obs:.4f}  BST: {g_n_bst:.4f}  err {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
