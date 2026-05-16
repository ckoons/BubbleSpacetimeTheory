"""
Toy 2519 — μ → e γ branching ratio prediction in pure BST.

Owner: Lyra
Date:  2026-05-16

THE OBSERVABLE
==============
μ → e γ (muon decays to electron + photon) is a charged lepton
flavor violating (cLFV) process. In the Standard Model with massive
neutrinos, it's allowed at loop level but extremely suppressed.

Current experimental limit (MEG II, 2024):
  BR(μ → e γ) < 4.2 × 10^-13 (90% CL)

Standard Model prediction:
  BR(μ → e γ) ~ 10^-54 (vanishingly small)

THE BST PREDICTION
==================
In BST (without BSM additions): BR(μ → e γ) ≈ SM value.

The formula (Cheng-Li, Petcov):
  BR(μ → e γ) = (3α/32π) · |Σ_i U*_{μi} U_{ei} (m_νi²/M_W²)|²

BST INPUTS:
  - α = 1/N_max = 1/137 (BST)
  - m_ν_2 ≈ √(Δm²_21) ≈ 8.5 meV (from T1972)
  - m_ν_3 ≈ √(Δm²_31) ≈ 49.8 meV (from T1972, exp(-C_2/2) eV)
  - m_ν_1 = 0 (from T1985)
  - M_W = 80.4 GeV (gauge boson, T1919)
  - PMNS matrix elements U_μi, U_ei from neutrino oscillation data

CONSEQUENCE: BR(μ→eγ) < ~10^-50 in pure BST.

FALSIFIABILITY
==============
MEG II limit: 4.2 × 10^-13. BST predicts << this.
MEG III planned: ~10^-14. BST: still << this.

If MEG II/III ever observes μ→eγ at ANY level, BST is at risk and
must accommodate BSM physics (new heavy particles in loop).

This is a clean falsifiable prediction: NO cLFV in pure BST.
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
    N_max = 137
    _ = (rank, N_c, n_C, g, c_2, c_3)  # cited in narrative

    print("=" * 72)
    print("Toy 2519 — μ → e γ branching ratio in pure BST (no BSM)")
    print("=" * 72)

    # ====================================================================
    # SECTION 1 — BST inputs
    # ====================================================================
    print("\n[Section 1] BST inputs to the rate formula")
    print("-" * 72)

    alpha = 1.0 / N_max  # BST: α = 1/N_max
    print(f"  α = 1/N_max = 1/{N_max} = {alpha:.6e}")

    # Neutrino masses from T1972 and T1985
    m_nu_1 = 0.0  # T1985
    delta_m2_21 = 7.5e-5  # eV² (solar)
    delta_m2_31 = math.exp(-C_2)  # eV² from T1972: exp(-C_2) = exp(-6) ≈ 2.479e-3
    # Note: m_2 = √(Δm²_21 + m_1²) = √Δm²_21 since m_1 = 0
    m_nu_2 = math.sqrt(delta_m2_21)  # eV
    m_nu_3 = math.sqrt(delta_m2_31)  # eV (≈ 49.8 meV)

    print(f"\n  Neutrino masses (BST):")
    print(f"    m_ν_1 = {m_nu_1} eV (exactly, T1985)")
    print(f"    m_ν_2 = √Δm²_21 = {m_nu_2*1000:.2f} meV")
    print(f"    m_ν_3 = √Δm²_31 = √exp(-C_2) = {m_nu_3*1000:.2f} meV")

    M_W_GeV = 80.4  # W boson mass
    M_W_eV = M_W_GeV * 1e9
    print(f"\n  M_W = {M_W_GeV} GeV = {M_W_eV:.2e} eV")

    # ====================================================================
    # SECTION 2 — PMNS matrix elements (from data)
    # ====================================================================
    print("\n[Section 2] PMNS matrix elements (from neutrino oscillation data)")
    print("-" * 72)

    # PMNS standard form (NuFIT 5.2 best fits)
    # Approximate values for |U_ei| and |U_μi|
    # Row e: |U_e1|² = 0.681, |U_e2|² = 0.297, |U_e3|² = 0.0223
    # Row μ: |U_μ1|² = 0.114, |U_μ2|² = 0.359, |U_μ3|² = 0.527

    U_e = [math.sqrt(0.681), math.sqrt(0.297), math.sqrt(0.0223)]
    U_mu = [math.sqrt(0.114), math.sqrt(0.359), math.sqrt(0.527)]

    print(f"  |U_e_i|² ≈ [0.681, 0.297, 0.0223] (mass eigenstates 1, 2, 3)")
    print(f"  |U_μ_i|² ≈ [0.114, 0.359, 0.527]")

    # ====================================================================
    # SECTION 3 — μ → eγ amplitude
    # ====================================================================
    print("\n[Section 3] Amplitude: A = Σ_i U*_{μi}·U_{ei}·(m_νi²/M_W²)")
    print("-" * 72)

    # The amplitude (real-valued approximation, ignoring CP phase)
    amplitude = 0.0
    contributions = []
    for i in range(3):
        m_nu_i = [m_nu_1, m_nu_2, m_nu_3][i]
        if m_nu_i > 0:
            term = U_mu[i] * U_e[i] * (m_nu_i / M_W_eV)**2
        else:
            term = 0.0
        amplitude += term
        contributions.append(term)
        print(f"    i={i+1}: m_ν={m_nu_i*1000:.2f} meV, contribution = {term:.4e}")

    print(f"\n  Total amplitude (approx, real): {amplitude:.4e}")
    print(f"  |A|² = {amplitude**2:.4e}")

    # ====================================================================
    # SECTION 4 — Branching ratio
    # ====================================================================
    print("\n[Section 4] BR(μ → e γ) = (3α/32π) · |A|²")
    print("-" * 72)

    prefactor = 3 * alpha / (32 * math.pi)
    BR_mu_to_e_gamma = prefactor * amplitude**2

    print(f"  Prefactor: 3α/(32π) = {prefactor:.4e}")
    print(f"  BR(μ→eγ) BST = {BR_mu_to_e_gamma:.4e}")

    print(f"\n  Comparison:")
    print(f"    MEG II limit (2024): 4.2 × 10^-13")
    print(f"    SM prediction:        ~10^-54")
    print(f"    BST prediction:       {BR_mu_to_e_gamma:.4e}")

    BR_obs_limit = 4.2e-13
    check("BR(μ→eγ) BST is below MEG II limit",
          BR_mu_to_e_gamma < BR_obs_limit, True)
    check("BR(μ→eγ) BST is far below MEG III future reach (~10^-14)",
          BR_mu_to_e_gamma < 1e-14, True)
    check("BR(μ→eγ) BST is in SM range (~10^-50 to 10^-55)",
          1e-60 < BR_mu_to_e_gamma < 1e-45, True)

    # ====================================================================
    # SECTION 5 — Structural BST reading
    # ====================================================================
    print("\n[Section 5] Structural BST reading of the suppression")
    print("-" * 72)

    # The suppression factor is dominated by (m_ν_3/M_W)² = exp(-C_2)/M_W² in eV² units
    suppress = (m_nu_3 / M_W_eV)**2
    print(f"  Dominant suppression: (m_ν_3/M_W)² = (exp(-C_2/2)/M_W)² ")
    print(f"                                     = exp(-C_2)/M_W² (in eV² units)")
    print(f"                                     = {suppress:.4e}")
    print(f"  Squared (amplitude squared): {suppress**2:.4e}")

    # In BST, this becomes:
    #   suppress² = (m_ν_3²/M_W²)² where m_ν_3² = exp(-C_2) eV² (T1972)
    #             = exp(-2·C_2) eV⁴ / M_W⁴
    # With M_W ~ 80 GeV ~ 8e10 eV:
    #   M_W⁴ = 4.1e43 eV⁴

    print(f"""
  STRUCTURAL READING:
    BR(μ→eγ) ≈ (3α/32π) · |U_μ U_e|² · (exp(-C_2) / M_W²)²

    In BST integers:
      α = 1/N_max
      exp(-C_2) ≈ 1/exp(6) ≈ 1/403 (T1972 neutrino splitting)
      M_W = 80.4 GeV (gauge sector)

    The TINY value of BR(μ→eγ) comes from:
      - m_ν² is tiny (m_ν³ ~ 50 meV via T1972's exp(-C_2))
      - M_W is large (80 GeV)
      - The ratio (m_ν/M_W)² is therefore extremely small
      - Squaring it gives (m_ν/M_W)^4

    BST GEOMETRIC SOURCE: m_ν small because Wallach K-types with
    Majorana-only structure (T1985) have suppressed Higgs couplings.
""")

    # ====================================================================
    # SECTION 6 — Falsifiability statement
    # ====================================================================
    print("\n[Section 6] Falsifiability and reach")
    print("-" * 72)

    print("""
  BST PREDICTION (sharp):
    BR(μ → e γ) < 10^-45 in pure BST (no BSM physics).

  EXPERIMENTAL REACH:
    - MEG II (current): 4.2 × 10^-13
    - MEG III planned: 6 × 10^-14
    - Future projects: 10^-15 to 10^-16

  These are ALL >> BST prediction of ~10^-50.

  Therefore: BST predicts MEG II, MEG III, and any conceivable
  near-future experiment will NOT observe μ → e γ.

  FALSIFICATION CONDITION:
    If any experiment observes μ → e γ at level > 10^-30, BST is at risk
    and must accommodate BSM physics. Pure-BST framework excludes
    detectable cLFV.

  This is a strong, clean, falsifiable prediction.

  CONNECTED CHANNELS (same suppression mechanism):
    - μ → e conversion in nuclei
    - μ → 3e
    - τ → μ γ, τ → e γ
    - K → π ν ν̄ (FCNC)
    All predicted to be at SM levels or below, no BSM enhancement.
""")

    check("Falsifiable prediction is well-defined",
          BR_mu_to_e_gamma < 1e-30, True)

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
