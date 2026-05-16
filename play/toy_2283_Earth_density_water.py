"""
Toy 2283 — Earth density / water density = c_2/rank = 11/2.

Earth mean density 5.515 g/cm³. Water 1.000 g/cm³. Ratio = 5.515.
BST: c_2/rank = 11/2 = 5.500. Match 0.3%.
c_2 = rank*n_C + 1 = 11 (second Chern integer).
"""

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_2 = rank * n_C + 1  # = 11
rho_Earth = 5.515  # g/cm^3
rho_water = 1.000  # g/cm^3
ratio_obs = rho_Earth / rho_water
ratio_bst = c_2 / rank

err = abs(ratio_bst - ratio_obs) / ratio_obs * 100

print(f"Toy 2283 — rho(Earth)/rho(water) = c_2/rank = 11/2")
print(f"  Observed: {ratio_obs:.3f}")
print(f"  BST: {ratio_bst:.4f}")
print(f"  Precision: {err:.2f}%")
print(f"  c_2 = rank*n_C + 1 = 11 (second Chern)")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
