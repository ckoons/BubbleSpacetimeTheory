"""
Toy 2285 — Speed of sound ratio: v_s(steel)/v_s(air) = (N_c^3 - rank*n_C) + rank/n_C
                                                     = seesaw + rank/n_C = 17.4

v_s(steel) ≈ 5960 m/s (longitudinal). v_s(air) ≈ 343 m/s (20°C).
Observed ratio = 5960/343 = 17.376. BST: 17 + 2/5 = 17.400. Match 0.14%.
seesaw = N_c^3 - rank*n_C = 17 (Lyra Mersenne-offset).
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
seesaw = N_c**3 - rank * n_C
ratio_obs = 5960.0 / 343.0
ratio_bst = seesaw + rank / n_C
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2285 — v_s(steel)/v_s(air) = seesaw + rank/n_C = 17 + 2/5")
print(f"  Observed: {ratio_obs:.4f}  BST: {ratio_bst:.4f}  err {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
