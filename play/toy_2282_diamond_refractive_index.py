"""
Toy 2282 — Diamond refractive index: n(diamond) = (N_c^3 - rank*n_C)/g = 17/7.

The "seesaw" integer 17 = N_c^3 - rank*n_C = 27 - 10 (Lyra's
Mersenne-offset reading). Diamond n ≈ 2.417 at visible. BST: 17/7 = 2.4286.
Match 0.5%.
"""

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
n_diamond_obs = 2.4173  # at 589 nm (sodium D-line)
seesaw = N_c**3 - rank * n_C  # = 17
n_bst = seesaw / g

err = abs(n_bst - n_diamond_obs) / n_diamond_obs * 100

print(f"Toy 2282 — n(diamond) = (N_c^3 - rank*n_C)/g = 17/7")
print(f"  Observed: {n_diamond_obs}")
print(f"  BST: 17/7 = {n_bst:.4f}")
print(f"  Precision: {err:.2f}%")
print(f"  Note: 17 = N_c^3 - rank*n_C (Lyra's Mersenne-offset, Toy 2260)")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
