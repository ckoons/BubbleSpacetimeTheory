"""
Toy 2534 — Tau lifetime Γ_τ from pure BST: m_τ via T2003, v via T1969.

Owner: Lyra
Date:  2026-05-17 (Sunday, post-T2003)

THE OBSERVABLE
==============
τ_τ = 2.903 × 10^-13 s (PDG 2024)
Γ_τ = ℏ/τ_τ = 2.27 × 10^-12 GeV = 2.27 meV

The tau is heavy (1.777 GeV), so its decay channels are MANY:
  τ → eνν̄ (17.8%)
  τ → μνν̄ (17.4%)
  τ → hadrons + ν (64.8%)

For the LEPTONIC channels (μνν̄, eνν̄ summed):
  Γ_τ^lep = G_F²·m_τ⁵/(192π³) · 2  (factor 2 for two channels)
         = G_F²·m_τ⁵/(96π³)

The HADRONIC channel is enhanced by α_s corrections plus channel
multiplicity (N_c·sum-of-mixings).

TOTAL TAU DECAY RATE:
  Γ_τ ≈ G_F²·m_τ⁵/(192π³) · (1 + N_c·(1+δ_QCD))
      ≈ G_F²·m_τ⁵/(192π³) · (1 + N_c) for tree-level QCD

For numerical estimate:
  Γ_τ ≈ G_F²·m_τ⁵/(192π³) · (1+N_c) · (1 + δ_QED + δ_QCD corrections)

BST INPUTS:
  - m_τ via T2003: m_τ/m_e = g²·(rank²·C_2·N_c - 1) = 49·71 = 3479
  - v via T1969: v = c_2²·c_3·π^{n_C}·m_e
  - G_F = 1/(√2·v²)
  - N_c = 3 (hadronic enhancement)

PURE-BST FORMULA (leptonic + N_c hadronic):
  Γ_τ ≈ m_τ⁵ · (1+N_c) / (384·π³·v⁴)
"""

import math


def run():
    tests = []
    def check(label, got, want, note="", tol=0.0):
        if isinstance(got, (int, float)) and isinstance(want, (int, float)):
            ok = abs(got - want) <= tol
        else:
            ok = (got == want)
        tests.append((ok, label, got, want, note))
        return ok

    rank = 2
    N_c = 3
    n_C = 5
    C_2 = 6
    g = 7
    c_2 = 11
    c_3 = 13
    _ = (c_3,)

    m_e_GeV = 0.5109989461e-3
    tau_tau_obs_s = 2.903e-13
    hbar_GeV_s = 6.582119569e-25
    Gamma_tau_obs_GeV = hbar_GeV_s / tau_tau_obs_s

    print("=" * 72)
    print("Toy 2534 — Tau lifetime Γ_τ from pure BST (T2003 m_τ + T1969 v)")
    print("=" * 72)

    # ====================================================================
    # SECTION 1 — m_τ from T2003
    # ====================================================================
    print("\n[Section 1] Tau mass from T2003: m_τ = g²·(rank²·C_2·N_c-1)·m_e")
    print("-" * 72)

    m_tau_factor = g**2 * (rank**2 * C_2 * N_c - 1)
    m_tau_BST_GeV = m_tau_factor * m_e_GeV
    m_tau_obs_GeV = 1.77686
    print(f"  m_τ/m_e (BST): g²·(rank²·C_2·N_c-1) = {g**2}·{rank**2*C_2*N_c-1} = {m_tau_factor}")
    print(f"  m_τ (BST): {m_tau_BST_GeV:.4f} GeV")
    print(f"  m_τ (obs): {m_tau_obs_GeV} GeV")
    dev = abs(m_tau_BST_GeV - m_tau_obs_GeV)/m_tau_obs_GeV * 100
    print(f"  Deviation: {dev:.3f}%")
    check("m_τ matches obs <0.5%", dev < 0.5, True)

    # ====================================================================
    # SECTION 2 — Higgs vev (T1969 — reuse from T1995)
    # ====================================================================
    print("\n[Section 2] Higgs vev v from T1969 (same as muon toy)")
    print("-" * 72)
    v_BST_GeV = c_2**2 * c_3 * math.pi**n_C * m_e_GeV
    G_F_BST = 1.0 / (math.sqrt(2) * v_BST_GeV**2)
    print(f"  v (BST) = {v_BST_GeV:.4f} GeV (matches PDG 246.22 GeV)")
    print(f"  G_F (BST) = {G_F_BST:.4e} GeV^-2")

    # ====================================================================
    # SECTION 3 — Decay rate channels
    # ====================================================================
    print("\n[Section 3] Tau decay rate channels")
    print("-" * 72)

    # Leptonic channels (μνν̄, eνν̄)
    # f(x) phase space for x = m_l²/m_τ². Negligible for both.
    x_e = (m_e_GeV/m_tau_BST_GeV)**2
    x_mu = (0.10566/m_tau_BST_GeV)**2
    f_e = 1 - 8*x_e + 8*x_e**3 - x_e**4 - 12*x_e**2*math.log(x_e) if x_e > 0 else 1
    f_mu = 1 - 8*x_mu + 8*x_mu**3 - x_mu**4 - 12*x_mu**2*math.log(x_mu) if x_mu > 0 else 1
    print(f"  Phase space factors: f(e) = {f_e:.4f}, f(μ) = {f_mu:.4f}")

    Gamma_e = G_F_BST**2 * m_tau_BST_GeV**5 / (192 * math.pi**3) * f_e
    Gamma_mu = G_F_BST**2 * m_tau_BST_GeV**5 / (192 * math.pi**3) * f_mu
    Gamma_lep = Gamma_e + Gamma_mu
    print(f"\n  Γ(τ→eνν̄) (BST): {Gamma_e:.4e} GeV")
    print(f"  Γ(τ→μνν̄) (BST): {Gamma_mu:.4e} GeV")
    print(f"  Γ_lep (BST):     {Gamma_lep:.4e} GeV")

    # Hadronic channel: enhanced by N_c·(1 + α_s/π + 5.2·(α_s/π)² + ...)
    # Full pQCD expansion at α_s(m_τ) ≈ 0.32 gives effective R_τ ≈ 3.65
    # In BST: R_τ = N_c·(1 + δ_QCD) where δ_QCD is the higher-order series.
    # Closed-form approximation: R_τ_BST = N_c + g/c_3 ≈ 3 + 0.54 = 3.54
    alpha_s_tau = 0.32
    QCD_correction = 1 + alpha_s_tau/math.pi + 5.2*(alpha_s_tau/math.pi)**2
    Gamma_had = G_F_BST**2 * m_tau_BST_GeV**5 / (192 * math.pi**3) * N_c * QCD_correction
    print(f"  R_τ = N_c·(1+α_s/π+5.2(α_s/π)²) = {N_c*QCD_correction:.3f} (obs R_τ ≈ 3.65)")
    print(f"  Γ(τ→hadrons) (BST): {Gamma_had:.4e} GeV")

    Gamma_total_BST = Gamma_lep + Gamma_had
    print(f"\n  Γ_τ TOTAL (BST): {Gamma_total_BST:.4e} GeV")
    print(f"  Γ_τ (obs): {Gamma_tau_obs_GeV:.4e} GeV")
    dev_Gamma = abs(Gamma_total_BST - Gamma_tau_obs_GeV)/Gamma_tau_obs_GeV * 100
    print(f"  Deviation: {dev_Gamma:.3f}%")
    check("Γ_τ matches obs <5%", dev_Gamma < 5.0, True)

    # Lifetime
    tau_tau_BST = hbar_GeV_s / Gamma_total_BST
    print(f"\n  τ_τ (BST): {tau_tau_BST:.4e} s")
    print(f"  τ_τ (obs): {tau_tau_obs_s:.4e} s")
    dev_tau = abs(tau_tau_BST - tau_tau_obs_s)/tau_tau_obs_s * 100
    print(f"  Deviation: {dev_tau:.3f}%")
    check("τ_τ matches obs <5%", dev_tau < 5.0, True)

    # ====================================================================
    # SECTION 4 — Branching ratios
    # ====================================================================
    print("\n[Section 4] Branching ratios from BST")
    print("-" * 72)
    BR_e = Gamma_e / Gamma_total_BST * 100
    BR_mu = Gamma_mu / Gamma_total_BST * 100
    BR_had = Gamma_had / Gamma_total_BST * 100

    BR_e_obs = 17.82
    BR_mu_obs = 17.39
    BR_had_obs = 64.79

    print(f"  Channel        | BST      | PDG     | Dev")
    print(f"  τ→eνν̄         | {BR_e:6.2f}%  | {BR_e_obs}%  | {abs(BR_e-BR_e_obs)/BR_e_obs*100:.1f}%")
    print(f"  τ→μνν̄         | {BR_mu:6.2f}%  | {BR_mu_obs}%  | {abs(BR_mu-BR_mu_obs)/BR_mu_obs*100:.1f}%")
    print(f"  τ→hadrons       | {BR_had:6.2f}%  | {BR_had_obs}%  | {abs(BR_had-BR_had_obs)/BR_had_obs*100:.1f}%")

    check("BR(τ→eνν̄) matches obs <5%", abs(BR_e-BR_e_obs)/BR_e_obs < 0.05, True)
    check("BR(τ→hadrons) matches obs <5%", abs(BR_had-BR_had_obs)/BR_had_obs < 0.05, True)

    # ====================================================================
    # SECTION 5 — Pure-BST closed form
    # ====================================================================
    print("\n[Section 5] Pure-BST closed form")
    print("-" * 72)

    # Γ_τ_LO = (m_τ/m_e)^5 · (1+N_c·(1+α_s/π)) / (384·π^(4n_C+3)·(c_2²·c_3)^4) · m_e
    closed_form_factor = m_tau_factor**5 * (1 + N_c*QCD_correction) / (384 * math.pi**(4*n_C+3) * (c_2**2*c_3)**4)
    Gamma_closed_form = closed_form_factor * m_e_GeV

    print(f"""
  PURE-BST CLOSED FORM (LO + QCD enhancement):
    Γ_τ ≈ (g²·(rank²·C_2·N_c-1))^5 · (1 + N_c·(1+α_s/π))
          ─────────────────────────────────────────────────  · m_e
                  384 · π^(4n_C+3) · (c_2²·c_3)^4

  Numerically: {Gamma_closed_form:.4e} GeV
  vs observed: {Gamma_tau_obs_GeV:.4e} GeV
  Deviation: {abs(Gamma_closed_form - Gamma_tau_obs_GeV)/Gamma_tau_obs_GeV*100:.2f}%

  The only non-BST input is α_s ≈ 0.32 at m_τ scale (a measured QCD
  running coupling). If α_s admits a BST form at this scale, the
  formula becomes pure-BST.

  Tier inherited from T2003 (lepton mass mechanism, D-tier candidate)
  and T1969 (v, D-tier).
""")

    # ====================================================================
    # SCORE
    # ====================================================================
    passed = sum(1 for ok, *_ in tests if ok)
    total = len(tests)
    print("=" * 72)
    print(f"SCORE: {passed}/{total}")
    print("=" * 72)
    return passed, total


if __name__ == "__main__":
    run()
