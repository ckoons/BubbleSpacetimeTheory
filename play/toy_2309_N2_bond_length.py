"""
Toy 2309 — N2 bond length / Bohr radius: r(N2)/a_0 = rank + 1/c_3 = 27/13.
r(N2) = 1.098 Å. a_0 = 0.5292 Å.
Ratio = 2.075. BST: 2 + 1/13 = 27/13 = 2.077. Match 0.10%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_3 = 13
r_N2 = 1.098
a_0 = 0.52917721
ratio_obs = r_N2 / a_0
ratio_bst = rank + 1.0 / c_3
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2309 — r(N2)/a_0 = rank + 1/c_3 = 27/13 = {ratio_bst:.4f} vs {ratio_obs:.4f}, err {err:.2f}%")
print(f"SCORE: {1 if err < 1.0 else 0}/1")
