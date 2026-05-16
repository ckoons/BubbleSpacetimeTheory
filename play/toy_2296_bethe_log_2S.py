"""
Toy 2296 — Bethe logarithm for 2S state: ln(k_0(2S)) = seesaw/C_2 = 17/6.

The Bethe logarithm is a transcendental constant tied to hydrogen
atomic spectra. ln(k_0(2S)) ≈ 2.81177.
BST: seesaw/C_2 = 17/6 = 2.83333. Match 0.77%.
seesaw = N_c^3 − rank·n_C = 17 (Lyra Mersenne-offset reading).
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
seesaw = N_c**3 - rank * n_C
bethe_obs = 2.811769
bethe_bst = seesaw / C_2
err = abs(bethe_bst - bethe_obs) / bethe_obs * 100
print(f"Toy 2296 — ln(k_0(2S)) = seesaw/C_2 = 17/6")
print(f"  Observed: {bethe_obs:.4f}  BST: {bethe_bst:.4f}  err {err:.2f}%")
print(f"  SCORE: {1 if err < 1.0 else 0}/1 ({'PASS' if err < 1.0 else 'FAIL'})")
