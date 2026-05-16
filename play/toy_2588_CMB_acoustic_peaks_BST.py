"""
Toy 2588 — CMB acoustic peaks ℓ_1, ℓ_2, ℓ_3 cascade in BST.

Owner: Lyra
Date:  2026-05-17

OBSERVED (Planck 2018)
======================
ℓ_1 ≈ 220 (first acoustic peak)
ℓ_2 ≈ 540 (second)
ℓ_3 ≈ 810 (third)

BST IDENTIFICATIONS
====================
ℓ_1 = rank² · n_C · c_2 = 4 · 5 · 11 = 220     (T2049)
ℓ_2 = (n_C/rank) · ℓ_1 = (5/2) · 220 = 550     (2% off obs 540)
ℓ_3 = (c_2/N_c) · ℓ_1 = (11/3) · 220 = 807     (0.4% off obs 810)

The CMB acoustic peak SEQUENCE follows a BST integer cascade,
analogous to the meson mass cascade (T2041).
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
    _ = (C_2, g, c_3)

    print("=" * 72)
    print("Toy 2588 — CMB acoustic peaks cascade in BST")
    print("=" * 72)

    # ℓ_1
    l1_BST = rank**2 * n_C * c_2
    l1_obs = 220
    print(f"\n[Section 1] First peak ℓ_1 (T2049 result, repeated)")
    print("-" * 72)
    print(f"  BST: ℓ_1 = rank²·n_C·c_2 = {l1_BST}")
    print(f"  Obs: 220 (Planck 2018)")
    check("ℓ_1 = 220", l1_BST, 220)

    # ℓ_2
    l2_BST = (n_C / rank) * l1_BST
    l2_obs = 540
    print(f"\n[Section 2] Second peak ℓ_2")
    print("-" * 72)
    print(f"  BST: ℓ_2 = (n_C/rank)·ℓ_1 = (5/2)·{l1_BST} = {l2_BST}")
    print(f"  Obs: {l2_obs}")
    dev_2 = abs(l2_BST - l2_obs)/l2_obs * 100
    print(f"  Deviation: {dev_2:.2f}%")
    check("ℓ_2 <5%", dev_2 < 5.0, True)

    # ℓ_3
    l3_BST = (c_2 / N_c) * l1_BST
    l3_obs = 810
    print(f"\n[Section 3] Third peak ℓ_3")
    print("-" * 72)
    print(f"  BST: ℓ_3 = (c_2/N_c)·ℓ_1 = (11/3)·{l1_BST} = {l3_BST:.1f}")
    print(f"  Obs: {l3_obs}")
    dev_3 = abs(l3_BST - l3_obs)/l3_obs * 100
    print(f"  Deviation: {dev_3:.2f}%")
    check("ℓ_3 <2%", dev_3 < 2.0, True)

    # Ratios
    print(f"\n[Section 4] Ratios")
    print("-" * 72)
    print(f"  ℓ_2/ℓ_1 (BST): n_C/rank = 5/2 = 2.5  (obs 2.45)")
    print(f"  ℓ_3/ℓ_1 (BST): c_2/N_c = 11/3 = 3.67 (obs 3.68)")
    check("ℓ_3/ℓ_1 = c_2/N_c", abs(c_2/N_c - 810/220)/(810/220) < 0.01, True)

    print(f"\n[Section 5] Connection to other BST cascades")
    print("-" * 72)
    print("""
  CMB peak cascade parallels:
    Meson mass cascade (T2041): m_K=(g/rank)·m_π, m_η=rank²·m_π, ...
    Baryon mass cascade (T2043): m_Λ=(C_2/n_C)·m_p, ...
    Quark mass cascade (T2032+T2013): m_b=m_t/(C_2·g), ...

  All three cascades follow BST integer ratios applied to an anchor.
  CMB peaks are the COSMOLOGICAL analog.

  Geometric source: acoustic oscillations at recombination follow
  harmonic series with overtone frequencies determined by D_IV^5
  characteristic scales (rank, n_C, c_2, N_c).
""")

    passed = sum(1 for ok, *_ in tests if ok)
    total = len(tests)
    print("=" * 72)
    print(f"SCORE: {passed}/{total}")
    print("=" * 72)
    return passed, total


if __name__ == "__main__":
    run()
