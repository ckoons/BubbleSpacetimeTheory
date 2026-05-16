"""
Toy 2286 — Solar radius / Earth radius: R_sun/R_earth = N_max - rank^2*g = 109.

R_sun = 695700 km, R_earth = 6371.0 km.
Observed = 109.20. BST: N_max - rank^2*g = 137 - 28 = 109. Match 0.18%.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
ratio_obs = 695700.0 / 6371.0
ratio_bst = N_max - rank**2 * g
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2286 — R_sun/R_earth = N_max - rank^2*g = 109")
print(f"  Observed: {ratio_obs:.3f}  BST: {ratio_bst}  err {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
