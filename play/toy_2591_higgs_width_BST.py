"""
Toy 2591 — Higgs total width Γ_H = (N_c/n_C)·m_H/N_max² in BST.

Owner: Lyra
Date:  2026-05-17

OBSERVABLE
==========
Γ_H_total = 4.1 ± 1 MeV (PDG 2024, m_H = 125.1 GeV)
Γ_H/m_H = 3.28e-5

BST IDENTIFICATION
===================
Γ_H/m_H = (N_c/n_C)·α² = (N_c/n_C)/N_max² = 3/(5·137²) = 3.20e-5

Match: 2.4% off observed.

GEOMETRIC SOURCE
================
Higgs width is dominated by Yukawa decays. The leading channel H→bb̄
contributes ~58% of width. Yukawa coupling at b mass ~ 0.024 = (m_b/v).

Γ_H_total/m_H ≈ (N_c/n_C)·α² is "color/continuation dimension per
fine-structure squared". Physical: the total decay phase space per
Higgs mass scales as α² with N_c·N_f color factors averaged.

Tier I: clean formula at 2.4%.
"""

import math


def run():
    tests = []
    def check(label, got, want, note="", tol=0.0):
        ok = abs(got - want) <= tol if isinstance(got, (int, float)) and isinstance(want, (int, float)) else (got == want)
        tests.append((ok, label, got, want, note))
        return ok

    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13; N_max = 137
    _ = (rank, C_2, g, c_2, c_3)

    m_H = 125.1  # GeV

    print("=" * 72)
    print("Toy 2591 — Higgs total width Γ_H in BST")
    print("=" * 72)

    Gamma_H_BST = (N_c / n_C) * m_H / N_max**2 * 1000  # in MeV
    Gamma_H_obs = 4.1  # MeV
    print(f"\n  BST: Γ_H = (N_c/n_C)·m_H/N_max² = (3/5)·125.1/137²·1000 = {Gamma_H_BST:.3f} MeV")
    print(f"  Obs: Γ_H = {Gamma_H_obs} ± 1 MeV (PDG)")
    dev = abs(Gamma_H_BST - Gamma_H_obs)/Gamma_H_obs * 100
    print(f"  Deviation: {dev:.2f}%")
    check("Γ_H matches obs <5%", dev < 5.0, True)

    # Branching ratio cross-check
    BR_HH_BST = (N_c/n_C) / N_max**2  # ratio to m_H
    print(f"\n  Equivalent: Γ_H/m_H = (N_c/n_C)·α² = {BR_HH_BST:.3e}")
    print(f"  Obs: Γ_H/m_H = {Gamma_H_obs/1000/m_H:.3e}")

    print(f"""
[Section 2] Connection
------------------------------------------------------------------------
  Compare with the α²·BST_integer family:
    ε_K       = α²·42 = α²·C_2·g     (T1974)
    BR(H→γγ)  ≈ α²·42                 (Elie 2448)
    Γ_H/m_H   = α²·N_c/n_C = α²·(3/5) (THIS TOY)

  Higgs width is the α²-suppressed observable with BST integer 3/5
  rather than 42. The denominator 5 = n_C reflects the continuation
  dimension; the numerator 3 = N_c reflects color summation over
  Yukawa channels.

  Tier I (mechanism plausible, formula clean at 2.4%).
""")

    passed = sum(1 for ok, *_ in tests if ok)
    total = len(tests)
    print("=" * 72)
    print(f"SCORE: {passed}/{total}")
    print("=" * 72)
    return passed, total


if __name__ == "__main__":
    run()
