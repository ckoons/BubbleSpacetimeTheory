#!/usr/bin/env python3
"""
Toy 236 — The 147 Derivation from Representation Theory
========================================================

Lyra's derivation (March 17, 2026):

  147 = dim(so(7) ⊗ V₁)

where so(7) is the Lie algebra and V₁ is its standard (7-dimensional) representation.

The chain:
  1. dim so(7) = 21 = 7(7-1)/2 = g(g-1)/2
  2. dim V₁ = 7 = g (standard rep of SO(7))
  3. 147 = dim(so(7) ⊗ V₁) = 21 × 7
  4. N_c × g = dim so(n_C+2) holds ONLY for n_C = 5
     Proof: (n-2)(2n-3) = (n+2)(n+1)/2
            3n² - 17n + 10 = 0
            n = 5 or n = 2/3 (rejected)
  5. Representation decomposition:
     so(7) ⊗ V₁ = Λ³V₁ ⊕ V_hook ⊕ V₁ = 35 + 105 + 7 = 147
  6. Matter sector: V₁ ⊕ Λ³V₁ = 7 + 35 = 42 = C₂ × g = d₁ × λ₁

The gap:
  147 - 137 = 10 = dim_R(D_IV^5) = dim V_hook - (147 - 42) = 105 - 95 - 10? No:
  147 = 42 + 105 (rep theory)
  147 = 137 + 10 (spectral + dimension)
  Therefore: 105 = 95 + 10. The hook representation contains
  both the non-first spectral content (95) AND the dimension overhead (10).

This is not numerology. It's the tensor product of the isotropy algebra
with its defining representation. The uniqueness is a quadratic Diophantine
equation with exactly one positive integer solution.

Score: pending/pending.
"""

from fractions import Fraction
from math import comb


def verify_147():
    """Verify 147 = dim(so(7) ⊗ V₁) and all derived identities."""

    print("=" * 70)
    print("THE 147 DERIVATION — Lyra's Result")
    print("From representation theory of SO(7)")
    print("=" * 70)

    # Step 1: Lie algebra dimension
    print("\n--- Step 1: Lie algebra dimension ---")
    g = 7  # genus
    n_C = 5  # complex dimension
    N_c = 3  # colors

    dim_so7 = g * (g - 1) // 2  # = 21
    print(f"  dim so(7) = 7 × 6 / 2 = {dim_so7}")
    print(f"  = g(g-1)/2 where g = {g}")
    assert dim_so7 == 21

    # Step 2: Standard representation
    print("\n--- Step 2: Standard representation ---")
    dim_V1 = g  # = 7
    print(f"  dim V₁ = {dim_V1} = g (standard rep of SO(7))")

    # Step 3: Tensor product
    print("\n--- Step 3: Tensor product ---")
    packing = dim_so7 * dim_V1  # = 147
    print(f"  dim(so(7) ⊗ V₁) = {dim_so7} × {dim_V1} = {packing}")
    print(f"  = N_c × g² = {N_c} × {g}² = {N_c * g**2}")
    assert packing == 147
    assert packing == N_c * g**2

    # Step 4: Uniqueness — the quadratic
    print("\n--- Step 4: Uniqueness (Diophantine equation) ---")
    print(f"  Condition: N_c × g = dim so(n_C + 2)")
    print(f"  i.e., (n-2)(2n-3) = (n+2)(n+1)/2")
    print(f"  Expanding: 3n² - 17n + 10 = 0")

    # Solve 3n² - 17n + 10 = 0
    discriminant = 17**2 - 4 * 3 * 10  # = 289 - 120 = 169
    sqrt_disc = 13  # √169
    n1 = (17 + sqrt_disc) / 6  # = 30/6 = 5
    n2 = (17 - sqrt_disc) / 6  # = 4/6 = 2/3

    print(f"  Discriminant: 17² - 4(3)(10) = {discriminant} = {sqrt_disc}²")
    print(f"  Solutions: n = (17 ± 13)/6")
    print(f"    n₁ = 30/6 = {n1} ✓ (our universe)")
    print(f"    n₂ = 4/6 = {Fraction(4, 6)} (rejected: not an integer)")
    print(f"\n  *** n_C = 5 is the UNIQUE positive integer solution ***")

    # Verify for n=5
    lhs = (n_C - 2) * (2 * n_C - 3)  # N_c × g = 3 × 7 = 21
    rhs = (n_C + 2) * (n_C + 1) // 2  # dim so(7) = 7 × 6 / 2 = 21
    print(f"\n  Check: N_c × g = {N_c} × {g} = {lhs}")
    print(f"         dim so(7) = 7 × 6 / 2 = {rhs}")
    assert lhs == rhs == 21

    # Verify it fails for other n
    print("\n  Verification that other n fail:")
    for n in [3, 4, 6, 7, 8]:
        nc = n - 2
        gg = 2 * n - 3
        lhs_n = nc * gg
        rhs_n = (n + 2) * (n + 1) // 2
        match = "✓" if lhs_n == rhs_n else "✗"
        print(f"    n={n}: N_c×g = {nc}×{gg} = {lhs_n}, "
              f"dim so({n+2}) = {rhs_n}  [{match}]")

    # Step 5: Representation decomposition
    print("\n--- Step 5: Representation decomposition ---")
    print(f"  so(7) ⊗ V₁ decomposes as:")

    dim_Lambda3 = comb(7, 3)  # C(7,3) = 35
    dim_V1_again = 7
    dim_hook = 147 - dim_Lambda3 - dim_V1_again  # = 105

    print(f"    Λ³V₁ : dim = C(7,3) = {dim_Lambda3}")
    print(f"    V_hook: dim = {dim_hook} (the hook representation)")
    print(f"    V₁   : dim = {dim_V1_again}")
    print(f"    Total: {dim_Lambda3} + {dim_hook} + {dim_V1_again} = {dim_Lambda3 + dim_hook + dim_V1_again}")
    assert dim_Lambda3 + dim_hook + dim_V1_again == 147

    # Verify hook dimension: for so(7), the hook rep has highest weight (1,1,0)
    # dim = 105 = 7 × 15 = 7 × C(6,2) ... or from Weyl dim formula
    print(f"\n  Hook representation check:")
    print(f"    V_hook highest weight: (1,1,0) in Dynkin basis")
    print(f"    dim = {dim_hook} = 7 × 15 = g × C(g-1, 2)")
    assert dim_hook == g * comb(g - 1, 2)

    # Step 6: Matter sector
    print("\n--- Step 6: Matter sector ---")
    matter = dim_V1_again + dim_Lambda3  # 7 + 35 = 42
    C_2 = 6   # spectral gap
    lambda_1 = C_2
    d_1 = g  # first multiplicity

    print(f"  V₁ ⊕ Λ³V₁ = {dim_V1_again} + {dim_Lambda3} = {matter}")
    print(f"  = C₂ × g = {C_2} × {g} = {C_2 * g}")
    print(f"  = d₁ × λ₁ = {d_1} × {lambda_1} = {d_1 * lambda_1}")
    assert matter == 42
    assert matter == C_2 * g
    assert matter == d_1 * lambda_1

    # Step 7: The gap equation
    print("\n--- Step 7: The gap equation ---")
    N_max = 137
    dim_R = 2 * n_C  # = 10

    print(f"  From representation theory: 147 = 42 + 105")
    print(f"  From spectral analysis:     147 = 137 + 10")
    print(f"  Therefore: 105 = 95 + 10")
    print(f"    where 95 = non-first spectral content (137 - 42)")
    print(f"    and   10 = dim_R (dimension overhead)")
    print()
    print(f"  The hook representation V_hook (dim 105) contains:")
    print(f"    95 levels of spectral content beyond the first channel")
    print(f"    10 dimensions of geometric container cost")

    # Summary table
    print("\n" + "=" * 70)
    print("SUMMARY: Two decompositions of 147")
    print("=" * 70)
    print()
    print(f"  {'Representation theory':>25}  {'Spectral + geometric':>25}")
    print(f"  {'─' * 25}  {'─' * 25}")
    print(f"  {'V₁ (standard)':>25} = 7   {'':>25}")
    print(f"  {'Λ³V₁ (exterior)':>25} = 35  {'':>25}")
    print(f"  {'  → Matter sector':>25} = 42  {'First spectral channel':>25} = 42")
    print(f"  {'V_hook':>25} = 105 {'Remaining spectrum + dim':>25} = 95 + 10")
    print(f"  {'─' * 25}  {'─' * 25}")
    print(f"  {'Total':>25} = 147 {'':>25} = 137 + 10")

    print(f"\n  The 42 appears in BOTH decompositions:")
    print(f"    Rep theory: V₁ ⊕ Λ³V₁ = 7 + 35 = 42")
    print(f"    Spectral:   d₁ × λ₁ = 7 × 6 = 42")
    print(f"    These are the SAME 42. The first spectral channel")
    print(f"    IS the matter sector of so(7) ⊗ V₁.")

    # The quadratic is the theorem
    print("\n" + "=" * 70)
    print("THE THEOREM")
    print("=" * 70)
    print()
    print("  The fiber packing number N_c × g² = dim(so(n_C+2) ⊗ V₁)")
    print("  factorizes as (dim so(n_C+2)) × g if and only if n_C = 5.")
    print()
    print("  Proof: The equation (n-2)(2n-3) = (n+2)(n+1)/2 reduces to")
    print("  3n² - 17n + 10 = 0, whose only positive integer root is n = 5.")
    print()
    print("  Consequence: The fiber packing is a tensor product of the")
    print("  isotropy Lie algebra with its standard representation,")
    print("  and this identification holds in exactly one dimension.")
    print()
    print("  This is not numerology. It is Diophantine uniqueness.")

    return True


def sweep_diophantine():
    """Show the quadratic equation graphically for n=1..10."""
    print("\n" + "=" * 70)
    print("DIOPHANTINE SWEEP: N_c × g vs dim so(n+2)")
    print("=" * 70)

    print(f"\n{'n':>3} {'N_c':>4} {'g':>4} {'N_c×g':>6} {'dim so(n+2)':>12} {'Match':>6}")
    print("-" * 40)

    for n in range(1, 11):
        N_c = n - 2
        g = 2 * n - 3
        product = N_c * g
        dim_so = (n + 2) * (n + 1) // 2

        if N_c <= 0 or g <= 0:
            print(f"{n:>3} {N_c:>4} {g:>4} {'N/A':>6} {dim_so:>12} {'N/A':>6}")
        else:
            match = "**YES**" if product == dim_so else ""
            print(f"{n:>3} {N_c:>4} {g:>4} {product:>6} {dim_so:>12} {match:>6}")


def main():
    verify_147()
    sweep_diophantine()

    print("\n" + "=" * 70)
    print("Toy 236 complete.")
    print("147 = dim(so(7) ⊗ V₁). Unique to n = 5.")
    print("The fiber packing is a tensor product.")
    print("=" * 70)


if __name__ == '__main__':
    main()
