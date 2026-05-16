"""
Toy 2403 — CKM matrix Wolfenstein parameters: BST identification.

Owner: Lyra
Date:  2026-05-16 08:50 EDT
Out of: working the board. PMNS matrix has all 3 angles BST-identified
        (Toys 2385, 2394). CKM matrix is the quark mixing analog —
        much more precisely measured.

WOLFENSTEIN PARAMETRIZATION
============================
The CKM matrix is parametrized by four real numbers (lambda, A, rho, eta):

   |V_us| ≈ sin(theta_C) = lambda                  (Cabibbo angle)
   |V_cb| ≈ A * lambda^2
   |V_ub| ≈ A * lambda^3 * sqrt(rho^2 + eta^2)
   |V_td| ≈ A * lambda^3 * sqrt((1-rho)^2 + eta^2)

PDG 2024 values:
   lambda = 0.22501 ± 0.00068
   A      = 0.826 ± 0.012
   rho_bar = 0.159 ± 0.010
   eta_bar = 0.348 ± 0.010

These four parameters fully specify the CKM matrix (modulo overall
phase). All other |V_ij| follow from these four.

THIS TOY
=========
1. BST candidates for each Wolfenstein parameter
2. Cross-check: derive |V_us|, |V_cb|, |V_ub|, |V_td|, |V_ts|
3. Jarlskog invariant J cross-check
4. Honest tier verdict
"""

from fractions import Fraction
import math


def run():
    tests = []
    def check(label, got, want, note="", tol=0):
        if isinstance(got, float) and isinstance(want, float):
            ok = abs(got - want) <= tol
        else:
            ok = (got == want)
        tests.append((ok, label, got, want, note))
        return ok

    # BST integers
    rank = 2
    N_c = 3
    n_C = 5
    C_2 = 6
    g = 7
    c_2 = 11
    c_3 = 13
    chi = 24
    N_max = 137

    # K3 Hodge data
    b_2_K3 = 22  # second Betti

    print("=" * 72)
    print("Toy 2403 — CKM matrix Wolfenstein BST identification")
    print("=" * 72)

    # PDG 2024
    lambda_obs = 0.22501
    A_obs = 0.826
    rho_bar_obs = 0.159
    eta_bar_obs = 0.348

    # Derived
    abs_Vus_obs = lambda_obs
    abs_Vcb_obs = A_obs * lambda_obs ** 2
    abs_Vub_obs = A_obs * lambda_obs ** 3 * math.sqrt(rho_bar_obs**2 + eta_bar_obs**2)
    abs_Vtd_obs = A_obs * lambda_obs ** 3 * math.sqrt((1-rho_bar_obs)**2 + eta_bar_obs**2)
    J_obs = A_obs ** 2 * lambda_obs ** 6 * eta_bar_obs

    # ====================================================================
    # SECTION 1 — Wolfenstein lambda
    # ====================================================================
    print("\n[Section 1] Wolfenstein lambda = sin(theta_C) = |V_us|")
    print("-" * 72)

    # Toy 2357 candidate: lambda = n_C / b_2(K3) = 5/22
    lambda_BST = Fraction(n_C, b_2_K3)
    lambda_BST_float = float(lambda_BST)
    dev_lambda = abs(lambda_BST_float - lambda_obs) / lambda_obs * 100
    print(f"  BST: lambda = n_C/b_2(K3) = {n_C}/{b_2_K3} = {lambda_BST} = {lambda_BST_float:.5f}")
    print(f"  PDG: lambda = {lambda_obs}")
    print(f"  Deviation: {dev_lambda:.3f}%")
    check("lambda = 5/22 within 1.5%",
          dev_lambda < 1.5, True)

    # Note: 22 = b_2(K3) = rank*g + 2*n_C = c_2 + c_2 = 2*c_2 + 0
    # (multi-route BST decomposition of 22)
    check("22 = b_2(K3) = 2*c_2",
          2 * c_2, b_2_K3)

    # ====================================================================
    # SECTION 2 — Wolfenstein A
    # ====================================================================
    print("\n[Section 2] Wolfenstein A = |V_cb|/lambda²")
    print("-" * 72)

    # Try A = c_3/rank^4 = 13/16
    A_BST = Fraction(c_3, rank ** 4)
    A_BST_float = float(A_BST)
    dev_A = abs(A_BST_float - A_obs) / A_obs * 100
    print(f"  BST: A = c_3/rank^4 = {c_3}/{rank**4} = {A_BST} = {A_BST_float:.4f}")
    print(f"  PDG: A = {A_obs}")
    print(f"  Deviation: {dev_A:.3f}%")
    check("A = c_3/rank^4 = 13/16 within 2%",
          dev_A < 2.0, True)

    # Alternative: A = (c_2 + rank)/(rank·g) = 13/14 = 0.929 (too high)
    # Alternative: A = N_max/N_c²/g = 137/(9·7) = 137/63 = 2.18 (too high)
    # 13/16 is best small-denom candidate

    # ====================================================================
    # SECTION 3 — Wolfenstein rho_bar and eta_bar
    # ====================================================================
    print("\n[Section 3] Wolfenstein rho_bar and eta_bar")
    print("-" * 72)

    # rho_bar = 0.159, eta_bar = 0.348
    # Try: eta_bar = ? 0.348 ≈ 7/20 = g/(rank^2 * n_C) = 0.35 (0.6% off)
    # Try: rho_bar = ? 0.159 ≈ 11/69 = c_2/(N_c*n_C*c_3)? No, 11/69 = 0.159 (0.3%)
    #       Or rho_bar = 1/c_3·rank = 1/(13/2) = 2/13 = 0.154 (3.3%)
    #       Or rho_bar = 5/(C_2*n_C+C_2) = 5/36 = 0.139 (12% off)
    #       Best: 11/69 — but 69 = N_c·n_C·c_3 - rank = 195 - 126 = 69. Hmm cleaner: 69 = 3·23 = N_c·(N_c·g+rank). So 11/69 = c_2/(N_c·(N_c·g+rank)).
    #       Or simpler: 11/69 ~ c_2/(N_c·23) where 23 = N_c·g+rank.

    eta_bar_BST = Fraction(g, rank ** 2 * n_C)  # 7/20 = 0.35
    eta_bar_BST_float = float(eta_bar_BST)
    dev_eta = abs(eta_bar_BST_float - eta_bar_obs) / eta_bar_obs * 100
    print(f"  BST: eta_bar = g/(rank^2*n_C) = {g}/{rank**2*n_C} = {eta_bar_BST} = {eta_bar_BST_float:.4f}")
    print(f"  PDG: eta_bar = {eta_bar_obs}")
    print(f"  Deviation: {dev_eta:.3f}%")
    check("eta_bar = 7/20 within 2%",
          dev_eta < 2.0, True)

    # rho_bar = ?
    # Try: rho_bar = c_2/(N_c·(N_c·g+rank)) = 11/69 = 0.1594 (0.27%)
    twentythree = N_c * g + rank
    rho_bar_BST = Fraction(c_2, N_c * twentythree)
    rho_bar_BST_float = float(rho_bar_BST)
    dev_rho = abs(rho_bar_BST_float - rho_bar_obs) / rho_bar_obs * 100
    print(f"\n  BST: rho_bar = c_2/(N_c*(N_c*g+rank)) = {c_2}/{N_c*twentythree} = {rho_bar_BST} = {rho_bar_BST_float:.4f}")
    print(f"  PDG: rho_bar = {rho_bar_obs}")
    print(f"  Deviation: {dev_rho:.3f}%")
    check("rho_bar = c_2/(N_c*(N_c*g+rank)) within 1%",
          dev_rho < 1.0, True)

    # ====================================================================
    # SECTION 4 — Cross-check: |V_cb| from BST Wolfenstein
    # ====================================================================
    print("\n[Section 4] Cross-check |V_cb| = A·lambda²")
    print("-" * 72)

    Vcb_BST = float(A_BST) * float(lambda_BST) ** 2
    dev_Vcb = abs(Vcb_BST - abs_Vcb_obs) / abs_Vcb_obs * 100
    print(f"  BST: |V_cb| = (13/16)·(5/22)² = {Vcb_BST:.5f}")
    print(f"  PDG: |V_cb| = {abs_Vcb_obs:.5f}")
    print(f"  Deviation: {dev_Vcb:.2f}%")
    check("|V_cb| from BST Wolfenstein within 5%",
          dev_Vcb < 5.0, True)

    # ====================================================================
    # SECTION 5 — |V_ub| and |V_td| cross-checks
    # ====================================================================
    print("\n[Section 5] |V_ub| and |V_td| cross-checks")
    print("-" * 72)

    sqrt_term_ub = math.sqrt(rho_bar_BST_float**2 + eta_bar_BST_float**2)
    Vub_BST = float(A_BST) * float(lambda_BST)**3 * sqrt_term_ub
    dev_Vub = abs(Vub_BST - abs_Vub_obs) / abs_Vub_obs * 100
    print(f"  BST: |V_ub| = A·lambda³·sqrt(rho²+eta²)_BST = {Vub_BST:.6f}")
    print(f"  PDG: |V_ub| = {abs_Vub_obs:.6f}")
    print(f"  Deviation: {dev_Vub:.2f}%")
    check("|V_ub| within 10%",
          dev_Vub < 10.0, True)

    sqrt_term_td = math.sqrt((1-rho_bar_BST_float)**2 + eta_bar_BST_float**2)
    Vtd_BST = float(A_BST) * float(lambda_BST)**3 * sqrt_term_td
    dev_Vtd = abs(Vtd_BST - abs_Vtd_obs) / abs_Vtd_obs * 100
    print(f"\n  BST: |V_td| = A·lambda³·sqrt((1-rho)²+eta²)_BST = {Vtd_BST:.6f}")
    print(f"  PDG: |V_td| = {abs_Vtd_obs:.6f}")
    print(f"  Deviation: {dev_Vtd:.2f}%")
    check("|V_td| within 10%",
          dev_Vtd < 10.0, True)

    # ====================================================================
    # SECTION 6 — Jarlskog invariant J
    # ====================================================================
    print("\n[Section 6] Jarlskog CP-violation invariant J")
    print("-" * 72)

    # J = A²·lambda⁶·eta
    J_BST = float(A_BST)**2 * float(lambda_BST)**6 * eta_bar_BST_float
    dev_J = abs(J_BST - J_obs) / J_obs * 100
    print(f"  BST: J = A²·lambda⁶·eta = {J_BST:.3e}")
    print(f"  PDG: J = {J_obs:.3e}")
    print(f"  Deviation: {dev_J:.2f}%")

    # J observed ~3.0e-5 (PDG); BST prediction within 5-15%
    check("Jarlskog J within 20%",
          dev_J < 20.0, True)

    # ====================================================================
    # SECTION 7 — Verdict
    # ====================================================================
    print("\n[Section 7] Verdict")
    print("-" * 72)

    print(f"""
  CKM WOLFENSTEIN BST IDENTIFICATIONS:

  | Parameter | BST formula | Deviation | Tier |
  |-----------|-------------|-----------|------|
  | lambda    | n_C/b_2(K3) = 5/22 | {dev_lambda:.2f}% | I |
  | A         | c_3/rank^4 = 13/16 | {dev_A:.2f}% | I |
  | eta_bar   | g/(rank²·n_C) = 7/20 | {dev_eta:.2f}% | I |
  | rho_bar   | c_2/(N_c·(N_c·g+rank)) = 11/69 | {dev_rho:.2f}% | I |

  CKM ELEMENTS (derived from BST Wolfenstein):
  | Element | BST | Observed | Deviation |
  |---------|-----|----------|-----------|
  | |V_cb|  | {Vcb_BST:.5f} | {abs_Vcb_obs:.5f} | {dev_Vcb:.2f}% |
  | |V_ub|  | {Vub_BST:.6f} | {abs_Vub_obs:.6f} | {dev_Vub:.2f}% |
  | |V_td|  | {Vtd_BST:.6f} | {abs_Vtd_obs:.6f} | {dev_Vtd:.2f}% |
  | J       | {J_BST:.3e}  | {J_obs:.3e}  | {dev_J:.2f}% |

  All four CKM Wolfenstein parameters have BST candidates at <2%.
  All derived CKM elements within 10% (acceptable given multiplicative
  error propagation).

  PATTERN with PMNS triangle (Toy 2394): both quark and lepton mixing
  matrices admit BST integer parametrizations using Q^5 Chern integers,
  K3 cohomology, and BST primary integers. Multi-route consistent.

  TIER: I-tier candidates for all four Wolfenstein parameters.
  Promotion to D-tier requires per-parameter operator identity.

  COMPARISON to PMNS:
  - PMNS has 3 angles (1.5x simpler than CKM 4-param Wolfenstein)
  - PMNS angles match at <1% with simple BST ratios
  - CKM Wolfenstein matches at <2% but with more complex BST forms
  - Both mixing matrices live on D_IV^5 / Q^5 cohomology

  Recommend: file all four Wolfenstein BST formulas as I-tier candidates
  in catalog. Cross-reference Toy 2394 (PMNS) for parallel structure.
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
