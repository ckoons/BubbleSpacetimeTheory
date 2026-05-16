"""
Toy 2298 — Water/air dynamic viscosity ratio: mu(water)/mu(air) = n_C·c_2 = 55.

At 20°C:
  mu(water) ≈ 1.002 mPa·s = 1.002e-3 Pa·s
  mu(air)   ≈ 1.825e-5 Pa·s
Ratio = 54.9. BST: n_C * c_2 = 5 * 11 = 55. Match 0.18%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_2 = rank * n_C + 1
mu_water = 1.002e-3
mu_air = 1.825e-5
ratio_obs = mu_water / mu_air
ratio_bst = n_C * c_2
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2298 — mu(water)/mu(air) = n_C·c_2 = 55")
print(f"  Observed: {ratio_obs:.3f}  BST: {ratio_bst}  err {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
