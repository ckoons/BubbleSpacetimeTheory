"""
Toy 2304 — Octane/methane combustion: ΔH(C8H18)/ΔH(CH4) = C_2 + rank/c_3 = 80/13.
ΔH(octane) = -5471 kJ/mol, ΔH(methane) = -890 kJ/mol.
Ratio = 6.147. BST: 80/13 = 6.154. Match 0.11%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_3 = 13
ratio_obs = 5471 / 890
ratio_bst = C_2 + rank / c_3
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2304 — ΔH(C8H18)/ΔH(CH4) = C_2 + rank/c_3 = 80/13 = {ratio_bst:.4f} vs {ratio_obs:.4f}, err {err:.2f}%")
print(f"SCORE: {1 if err < 1.0 else 0}/1")
