"""
Toy 2378 — QCD transition / Lambda_QCD ratio: T_QCD/Λ_QCD = N_c/rank² = 3/4.
Observed: T_QCD ≈ 155 MeV, Λ_QCD ≈ 200 MeV → ratio = 0.775.
BST: N_c/rank² = 3/4 = 0.750. Deviation 3.2%.
Reading: deconfinement temperature ratio to QCD scale is color/rank² —
N_c colors over rank² gauge group dimension cap.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
T_QCD = 155.0  # MeV
Lambda_QCD = 200.0  # MeV (MS-bar conventional)
ratio_obs = T_QCD / Lambda_QCD
ratio_bst = N_c / rank**2
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2378 — T_QCD/Λ_QCD = N_c/rank² = 3/4 = {ratio_bst} vs {ratio_obs:.4f}, err {err:.2f}%")
print(f"SCORE: {1 if err < 5.0 else 0}/1")
