"""
Toy 2280 — Air Prandtl number: Pr(air) = n_C/g = 5/7.

Mechanism: Pr = mu*c_p/k = (momentum diffusion) / (thermal diffusion).
For diatomic ideal gas at standard conditions, Prandtl ≈ 0.71-0.72.
BST: n_C/g = 5/7 = 0.7143. The ratio reflects the BST compactification
in transport coefficients.
"""

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
Pr_air_obs = 0.71  # standard air at 300 K
Pr_air_bst = n_C / g

err = abs(Pr_air_bst - Pr_air_obs) / Pr_air_obs * 100

print(f"Toy 2280 — Pr(air) = n_C/g = 5/7")
print(f"  Observed: Pr(air) ≈ {Pr_air_obs}")
print(f"  BST: n_C/g = {Pr_air_bst:.4f}")
print(f"  Precision: {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
