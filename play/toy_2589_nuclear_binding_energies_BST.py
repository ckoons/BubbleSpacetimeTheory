"""
Toy 2589 — Nuclear binding energies B_d (deuteron) and B_α (alpha) in BST.

Owner: Lyra
Date:  2026-05-17

OBSERVABLES
===========
B_d (deuteron) = 2.224 MeV
B_α (alpha particle) = 28.30 MeV (28.296 total)

BST IDENTIFICATIONS
====================
B_d = c_3/N_c · m_e = 13/3 · m_e = 2.214 MeV (0.5% off)
B_α = c_2·n_C · m_e = 55 · m_e = 28.10 MeV (0.7% off)

GEOMETRIC SOURCE
================
The deuteron binding energy is the lightest nuclear bound state.
BST formula c_3/N_c uses third Chern over color count.

The alpha binding c_2·n_C = 11·5 = 55 uses second Chern times continuation
dimension. The 55 also appears as Wallach K-type dim_4 (T1830 backbone).
"""

import math


def run():
    tests = []
    def check(label, got, want, note="", tol=0.0):
        ok = abs(got - want) <= tol if isinstance(got, (int, float)) and isinstance(want, (int, float)) else (got == want)
        tests.append((ok, label, got, want, note))
        return ok

    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13
    _ = (rank, C_2, g)
    m_e = 0.5109989461

    print("=" * 72)
    print("Toy 2589 — Nuclear binding energies in BST")
    print("=" * 72)

    print("\n[1] Deuteron binding energy")
    print("-" * 72)
    B_d_BST = c_3 / N_c * m_e
    B_d_obs = 2.224
    dev_d = abs(B_d_BST - B_d_obs)/B_d_obs * 100
    print(f"  BST: B_d = c_3/N_c · m_e = 13/3 · m_e = {B_d_BST:.4f} MeV")
    print(f"  Obs: {B_d_obs} MeV")
    print(f"  Deviation: {dev_d:.2f}%")
    check("B_d <2%", dev_d < 2.0, True)

    print("\n[2] Alpha particle binding energy")
    print("-" * 72)
    B_alpha_BST = c_2 * n_C * m_e
    B_alpha_obs = 28.30
    dev_a = abs(B_alpha_BST - B_alpha_obs)/B_alpha_obs * 100
    print(f"  BST: B_α = c_2·n_C · m_e = 55 · m_e = {B_alpha_BST:.3f} MeV")
    print(f"  Obs: {B_alpha_obs} MeV")
    print(f"  Deviation: {dev_a:.2f}%")
    check("B_α <2%", dev_a < 2.0, True)

    print("\n[3] Per-nucleon binding")
    print("-" * 72)
    per_nucleon_alpha_BST = B_alpha_BST / 4  # alpha = 4 nucleons
    per_nucleon_obs = 7.07  # MeV/nucleon
    print(f"  BST: B_α/4 = {per_nucleon_alpha_BST:.3f} MeV per nucleon")
    print(f"  Obs: {per_nucleon_obs} MeV per nucleon")
    print(f"  (= c_2·n_C/(rank²)·m_e = 55/4·m_e in BST)")

    print("\n[4] Connection")
    print("-" * 72)
    print(f"""
  Nuclear binding scales:
    B_d (deuteron, 2-nucleon)  = c_3/N_c · m_e = 13/3 · m_e ≈ 2.2 MeV
    B_α (alpha, 4-nucleon)     = c_2·n_C · m_e = 55 · m_e ≈ 28 MeV
    B/A (per nucleon, max ~Fe) ≈ 8.8 MeV ≈ ?

  The 55 = c_2·n_C also equals Wallach K-type dim_4 (T1830):
    d_m = (2m+N_c)(m+1)(m+rank)/C_2
    d_4 = 11·5·6/6 = 55 ✓

  So B_α is set by the "fourth Wallach level dimension".

  Tier I: clean BST formulas at <1%, mechanism partly named.
""")

    passed = sum(1 for ok, *_ in tests if ok)
    total = len(tests)
    print("=" * 72)
    print(f"SCORE: {passed}/{total}")
    print("=" * 72)
    return passed, total


if __name__ == "__main__":
    run()
