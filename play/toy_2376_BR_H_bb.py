"""
Toy 2376 — Higgs → bb branching ratio: BR(H→bb) = 4/g = 4/7.
Observed (PDG 2024): BR(H→bb) = 0.582 ± 0.006
BST: 4/g = 4/7 = 0.5714. Deviation 1.83%.
The 4 = rank^2 is "dominant decay channel multiplicity" and g = 7 is the
total weak-coupling Mersenne integer giving total channel count.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
br_obs = 0.582
br_bst = rank**2 / g  # 4/7
err = abs(br_bst - br_obs) / br_obs * 100
print(f"Toy 2376 — BR(H→bb) = rank²/g = 4/7 = {br_bst:.4f} vs {br_obs}, err {err:.2f}%")
print(f"  rank² = 4: dominant-channel multiplicity")
print(f"  g = 7: total weak Mersenne integer")
print(f"SCORE: {1 if err < 3.0 else 0}/1 ({'PASS' if err < 3.0 else 'FAIL'})")
