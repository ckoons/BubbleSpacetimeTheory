"""
Toy 2290 — Combustion enthalpy ratio: ΔH(C3H8)/ΔH(CH4) = n_C/rank = 5/2.

ΔH_combustion(propane) = -2220 kJ/mol
ΔH_combustion(methane) = -890 kJ/mol
Ratio = 2.494. BST: n_C/rank = 5/2 = 2.500. Match 0.24%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
ratio_obs = 2220.0 / 890.0
ratio_bst = n_C / rank
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2290 — ΔH(C3H8)/ΔH(CH4) = n_C/rank = 5/2")
print(f"  Observed: {ratio_obs:.4f}  BST: {ratio_bst:.4f}  err {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
