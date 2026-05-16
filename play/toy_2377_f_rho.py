"""
Toy 2377 — Rho width-to-mass ratio: Γ_ρ/m_ρ = 1/n_C = 1/5.
Observed: Γ_ρ ≈ 149.1 MeV, m_ρ ≈ 775.5 MeV → ratio = 0.1923.
BST: 1/n_C = 0.2000. Deviation 4.0%.
Reading: ratio = 1/(compact dimension). The ρ-meson lives in the
compact 5-dim direction of D_IV⁵; its decay rate is set by the
inverse compact-dim winding length.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
Gamma_rho = 149.1
m_rho = 775.5
ratio_obs = Gamma_rho / m_rho
ratio_bst = 1.0 / n_C
err = abs(ratio_bst - ratio_obs) / ratio_obs * 100
print(f"Toy 2377 — Γ_ρ/m_ρ = 1/n_C = 1/5 = {ratio_bst:.4f} vs {ratio_obs:.4f}, err {err:.2f}%")
print(f"SCORE: {1 if err < 5.0 else 0}/1")
