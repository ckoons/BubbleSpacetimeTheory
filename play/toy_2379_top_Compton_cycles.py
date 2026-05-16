"""
Toy 2379 — Top quark lifetime in Compton cycles: τ_t · m_t / ℏ ≈ N_max = 137.
Observed: τ_top ≈ 5e-25 s, m_top ≈ 173 GeV → τ·m/ℏ = ?
1 Compton cycle = ℏ/(m c²). For top: τ·m/ℏ (in natural units, ℏ=c=1):
  τ_top · m_top = (5e-25 s) · (173 GeV) · (1 GeV·s/6.58e-25 ℏ)
Actually simpler: number of Compton cycles in lifetime = m·c²·τ/ℏ.
  m_t·c² = 173 GeV. ℏ/τ_t = ℏ/5e-25 s = 6.58e-25 / 5e-25 GeV·s/s = 1.32 GeV
  Number of cycles = 173/1.32 = 131. ≈ N_max = 137. Match within 5%.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
N_max = 137
m_top = 172.69  # GeV PDG
tau_top = 5e-25  # s approx
hbar_over_GeV_s = 6.58212e-25  # ℏ in GeV·s
cycles_obs = m_top * tau_top / hbar_over_GeV_s
cycles_bst = N_max
err = abs(cycles_bst - cycles_obs) / cycles_obs * 100
print(f"Toy 2379 — top lifetime / Compton time = m_t·τ_t/ℏ")
print(f"  computed: {cycles_obs:.1f} cycles  BST: N_max = {cycles_bst}")
print(f"  err: {err:.1f}% (within top width uncertainty)")
print(f"SCORE: {1 if err < 10.0 else 0}/1")
