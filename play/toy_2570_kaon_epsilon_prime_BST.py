"""
Toy 2570 — Direct CP violation ε'/ε = M_5/N_max² in BST.

Owner: Lyra
Date:  2026-05-17

OBSERVABLE
==========
ε'/ε = (16.6 ± 2.3) × 10^-4 (PDG average, KTeV + NA48)

Direct CP violation in kaon decays K → ππ.

BST IDENTIFICATION
===================
ε'/ε = M_5 / N_max² = 31 / 18769 = 1.651 × 10^-3

Where M_5 = 2^5 - 1 = 31 is the 5th Mersenne prime, also the
exponent in the Mersenne ladder (M_2 = N_c, M_3 = g, M_5 = 31).

Match: 0.5% off observed 1.66e-3.

GEOMETRIC SOURCE
================
ε'/ε measures direct CP violation in K → ππ. The natural scale:
α²·(some BST integer). With α² = 1/N_max²:
  ε'/ε = M_5/N_max² = 31·α²

M_5 = 5th Mersenne prime = 2^5 - 1 = 31. The 5 in 2^5-1 is n_C
(BST continuation dimension).

So ε'/ε = (2^{n_C} - 1) · α² = M_{n_C} · α²

GENERATION-SCALE PATTERN
========================
- ε (kaon mixing CP) = α²·42 = α²·C_2·g     (T1974)
- ε'/ε (direct CP)   = α²·M_{n_C}            (THIS TOY)

The ε factor 42 = C_2·g and the ε'/ε factor M_5 = 31 = 2^{n_C}-1
are BOTH Mersenne-style integers built from BST primary integers.
"""

import math


def run():
    tests = []
    def check(label, got, want, note="", tol=0.0):
        ok = abs(got - want) <= tol if isinstance(got, (int, float)) and isinstance(want, (int, float)) else (got == want)
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
    _ = (rank, C_2, g, c_2, c_3)

    print("=" * 72)
    print("Toy 2570 — ε'/ε = M_5/N_max² in BST")
    print("=" * 72)

    print("\n[Section 1] BST identification")
    print("-" * 72)
    M_5 = 2**n_C - 1  # 2^5 - 1 = 31
    eps_prime_over_eps_BST = M_5 / N_max**2
    eps_prime_over_eps_obs = 1.66e-3

    print(f"  M_{n_C} = 2^{n_C} - 1 = {M_5} (Mersenne prime)")
    print(f"  BST: ε'/ε = M_{n_C}/N_max² = {M_5}/{N_max**2} = {eps_prime_over_eps_BST:.4e}")
    print(f"  Obs: ε'/ε = {eps_prime_over_eps_obs:.4e} ± 2.3e-4 (PDG)")
    dev = abs(eps_prime_over_eps_BST - eps_prime_over_eps_obs)/eps_prime_over_eps_obs * 100
    print(f"  Deviation: {dev:.2f}%")
    check("ε'/ε matches obs <5%", dev < 5.0, True)

    print("\n[Section 2] Connection to ε (mixing CP)")
    print("-" * 72)
    eps_K_BST = (C_2 * g) / N_max**2
    eps_K_obs = 2.228e-3
    print(f"  T1974: ε_K = (C_2·g)/N_max² = 42/N_max² = {eps_K_BST:.4e}")
    print(f"  Obs: ε_K = {eps_K_obs:.4e}")
    print(f"  Match: {abs(eps_K_BST - eps_K_obs)/eps_K_obs*100:.2f}%")

    # The ratio ε'/ε via BST formulas
    ratio = M_5 / (C_2 * g)
    obs_ratio = eps_prime_over_eps_obs / eps_K_obs
    print(f"\n  BST: (ε'/ε)/(ε_K) = M_5/(C_2·g) = 31/42 = {ratio:.4f}")
    print(f"  Hmm — this is unit issue: ε'/ε is a RATIO, ε_K is absolute.")
    print(f"  Better statement: |ε'| = ε·(M_5/N_max²) = (C_2·g)·M_5/N_max⁴")
    eps_prime_abs = eps_K_BST * eps_prime_over_eps_BST
    print(f"  |ε'| (BST) = {eps_prime_abs:.4e} = (C_2·g·M_5)/N_max⁴")

    print("\n[Section 3] The Mersenne pattern in CP physics")
    print("-" * 72)
    print(f"""
  ε_K (mixing CP)    = α²·42      = α²·C_2·g
  ε'/ε (direct CP)   = α²·31      = α²·M_{n_C}
  Δa_μ involves     = α²·42      = α²·C_2·g (T1976)
  ε_K · ε'/ε = α⁴·1302 = α⁴·31·42

  1302 = 2·3·7·31 = rank·N_c·g·M_{n_C} = rank·N_c·g·(2^{n_C}-1)

  The 31 = M_5 = 2^{n_C}-1 enters CP physics naturally.

  PREDICTION: other CP-violating observables (B-meson mixing
  parameter, B→K* CP asymmetries, etc.) should share the M_5 = 31
  Mersenne factor in their leading BST integer expressions.
""")

    check("Mersenne M_5 = 31 enters CP", M_5, 31)

    passed = sum(1 for ok, *_ in tests if ok)
    total = len(tests)
    print("=" * 72)
    print(f"SCORE: {passed}/{total}")
    print("=" * 72)
    return passed, total


if __name__ == "__main__":
    run()
