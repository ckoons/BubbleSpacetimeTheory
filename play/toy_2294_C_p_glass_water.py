"""
Toy 2294 — Specific heat ratio: C_p(glass)/C_p(water) = 1/n_C.

C_p(glass)  ~ 0.84 J/(g·K) (silica glass at 25°C)
C_p(water)  ~ 4.18 J/(g·K)
Ratio = 0.201. BST: 1/n_C = 0.200. Match 0.5%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
ratio_obs = 0.84 / 4.18
ratio_bst = 1.0 / n_C
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2294 — C_p(glass)/C_p(water) = 1/n_C")
print(f"  Observed: {ratio_obs:.4f}  BST: {ratio_bst:.4f}  err {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
