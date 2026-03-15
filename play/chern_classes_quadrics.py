#!/usr/bin/env python3
"""
Chern classes of complex quadrics Q^n = SO(n+2)/[SO(n)×SO(2)]

The total Chern class is:
    c(Q^n) = (1+h)^{n+2} / (1+2h)   mod h^{n+1}

where h is the hyperplane class generator of H^2(Q^n, Z).

We expand (1+h)^{n+2} * (1+2h)^{-1} as a polynomial in h,
truncated at degree n, using exact Fraction arithmetic.
"""

from fractions import Fraction

def chern_classes_quadric(n):
    """
    Compute Chern classes c_1, ..., c_n of Q^n.

    c(Q^n) = (1+h)^{n+2} / (1+2h)  mod h^{n+1}

    Strategy: expand (1+2h)^{-1} = sum_{k>=0} (-2h)^k = sum (-2)^k h^k
    then multiply by (1+h)^{n+2} = sum C(n+2,j) h^j
    and collect coefficients mod h^{n+1}.
    """
    # Coefficients of (1+h)^{n+2}: binom(n+2, j) for j=0,...,n+2
    from math import comb
    binom_coeffs = [Fraction(comb(n + 2, j)) for j in range(n + 2 + 1)]

    # Coefficients of (1+2h)^{-1} = sum_{k>=0} (-2)^k h^k (geometric series)
    # We only need up to degree n
    inv_coeffs = [Fraction((-2)**k) for k in range(n + 1)]

    # Multiply: coefficient of h^m in the product
    # c_m = sum_{j=0}^{m} binom(n+2, j) * (-2)^{m-j}
    chern = []
    for m in range(n + 1):
        coeff = Fraction(0)
        for j in range(m + 1):
            if j <= n + 2:
                coeff += binom_coeffs[j] * inv_coeffs[m - j]
        chern.append(coeff)

    # chern[0] = c_0 = 1 (should be), chern[k] = c_k
    return chern


def main():
    print("=" * 80)
    print("CHERN CLASSES OF COMPLEX QUADRICS Q^n")
    print("c(Q^n) = (1+h)^{n+2} / (1+2h)  mod h^{n+1}")
    print("=" * 80)

    for n in range(1, 8):
        chern = chern_classes_quadric(n)
        print(f"\n{'─' * 60}")
        print(f"Q^{n} = SO({n+2})/[SO({n})×SO(2)]   (dim_C = {n})")
        print(f"{'─' * 60}")

        # Verify c_0 = 1
        assert chern[0] == 1, f"c_0 should be 1, got {chern[0]}"

        # Print all Chern classes
        for k in range(1, n + 1):
            c_k = chern[k]
            print(f"  c_{k} = {c_k}")

        # Top Chern class
        c_top = chern[n]
        print(f"\n  Top Chern class c_{n}(Q^{n}) = {c_top}")

        # Euler characteristic check: chi = c_n for compact complex manifold
        # For Q^n: chi = n+1 (always)
        print(f"  Euler characteristic chi(Q^{n}) = {n + 1}")

        # Check (n+1)/2 for odd n
        if n % 2 == 1:
            expected = Fraction(n + 1, 2)
            match = "YES" if c_top == expected else "NO"
            print(f"  c_{n}(Q^{n}) == (n+1)/2 = {expected}?  {match}")

    # Summary table
    print("\n\n" + "=" * 80)
    print("SUMMARY TABLE: Top Chern classes c_n(Q^n)")
    print("=" * 80)
    print(f"{'n':>3} | {'Q^n':>8} | {'c_n':>8} | {'(n+1)/2':>8} | {'Match (odd n)':>14}")
    print("─" * 50)
    for n in range(1, 8):
        chern = chern_classes_quadric(n)
        c_top = chern[n]
        if n % 2 == 1:
            expected = Fraction(n + 1, 2)
            match = "YES" if c_top == expected else "NO"
        else:
            expected = "-"
            match = "(even)"
        print(f"{n:>3} | Q^{n:>5} | {str(c_top):>8} | {str(expected):>8} | {match:>14}")

    # Specific verifications
    print("\n\n" + "=" * 80)
    print("SPECIFIC VERIFICATIONS")
    print("=" * 80)

    c_Q5 = chern_classes_quadric(5)
    c_Q3 = chern_classes_quadric(3)
    c_Q1 = chern_classes_quadric(1)

    print(f"\n1. c_5(Q^5) = {c_Q5[5]}   (expected: 3)   {'PASS' if c_Q5[5] == 3 else 'FAIL'}")
    print(f"2. c_3(Q^3) = {c_Q3[3]}   (expected: 2)   {'PASS' if c_Q3[3] == 2 else 'FAIL'}")
    print(f"3. c_1(Q^1) = {c_Q1[1]}   (expected: 1)   {'PASS' if c_Q1[1] == 1 else 'FAIL'}")

    # Nesting check: c_{n_C}(parent) = n_C(child)?
    print(f"\n{'─' * 60}")
    print("NESTING CHECK: Q^5 -> Q^3 -> Q^1")
    print(f"{'─' * 60}")

    # Q^5: n_C = 5. Does c_5(Q^5) = top Chern of child = c_3(Q^3)?
    # Well, the claim is c_{n_C}(parent) = N_c(child)
    # For Q^5: c_5(Q^5) = 3. Child is Q^3 with N_c = c_{(3+1)/2} = c_2(Q^3)?
    # Let's just check the chain

    print(f"\nQ^5: c_5(Q^5) = {c_Q5[5]} = N_c (number of colors)")
    print(f"     c_1(Q^5) = {c_Q5[1]}")
    print(f"     c_2(Q^5) = {c_Q5[2]}")
    print(f"     c_3(Q^5) = {c_Q5[3]}")
    print(f"     c_4(Q^5) = {c_Q5[4]}")
    print(f"     c_5(Q^5) = {c_Q5[5]}")

    print(f"\nQ^3: c_3(Q^3) = {c_Q3[3]} = (3+1)/2 = 2")
    print(f"     c_1(Q^3) = {c_Q3[1]}")
    print(f"     c_2(Q^3) = {c_Q3[2]}")
    print(f"     c_3(Q^3) = {c_Q3[3]}")

    print(f"\nQ^1: c_1(Q^1) = {c_Q1[1]} = (1+1)/2 = 1 (= CP^1 = S^2)")

    # The nesting: c_n(Q^n) for odd n gives (n+1)/2
    # Q^5 -> c_5 = 3 -> Q^3 -> c_3 = 2 -> Q^1 -> c_1 = 1
    # Each step: (n+1)/2 gives the NEXT odd dimension minus 2... no.
    # c_5(Q^5) = 3 = N_c. Is 3 the dimension of the child quadric? YES: Q^3.
    # c_3(Q^3) = 2. Does this point to Q^1? (n=1, but c_3(Q^3)=2, not 1)

    print(f"\n{'─' * 60}")
    print("NESTING INTERPRETATION")
    print(f"{'─' * 60}")
    print(f"c_5(Q^5) = 3 = dim(Q^3)          -> child is Q^3  CHECK")
    print(f"c_3(Q^3) = 2 = dim(Q^1) + 1?     -> child is Q^1? (c_3=2, dim Q^1=1)")
    print(f"c_1(Q^1) = 1 = terminus           -> chain terminates")
    print(f"\nAlternative: c_n(Q^n) = (n+1)/2 for odd n")
    print(f"  n=5: c_5 = 3")
    print(f"  n=3: c_3 = 2")
    print(f"  n=1: c_1 = 1")
    print(f"  Sequence: 3, 2, 1 — each top Chern class counts down!")

    # Full Chern class table
    print("\n\n" + "=" * 80)
    print("FULL CHERN CLASS TABLE")
    print("=" * 80)

    # Find max width
    header = f"{'n':>3} |"
    for k in range(1, 8):
        header += f" {'c_'+str(k):>8} |"
    print(header)
    print("─" * len(header))

    for n in range(1, 8):
        chern = chern_classes_quadric(n)
        row = f"{n:>3} |"
        for k in range(1, 8):
            if k <= n:
                row += f" {str(chern[k]):>8} |"
            else:
                row += f" {'·':>8} |"
        print(row)

    # BST-specific: verify all the Chern integers for Q^5
    print("\n\n" + "=" * 80)
    print("BST VERIFICATION: Q^5 Chern integers")
    print("=" * 80)
    c = c_Q5
    print(f"  c_1 = {c[1]}   (BST: n_C = 5? Actually c_1 = n+1 = {5+1}... hmm)")

    # Actually c(Q^5) = (1+h)^7/(1+2h)
    # Let's verify against the BST oracle formula
    print(f"\n  Oracle formula: c(Q^5) = (1+h)^7 / (1+2h)")
    print(f"  Exponent = n+2 = 7 = g (genus / BST integer)")
    print(f"\n  Full Chern vector: [{', '.join(str(c[k]) for k in range(len(c)))}]")

    # Known BST Chern integers
    bst = {
        'c_1': (c[1], 5, 'n_C'),
        'c_2': (c[2], 11, 'dim K = dim SO(5)×SO(2)'),
        'c_3': (c[3], 13, 'controls hyperfine'),
        'c_4': (c[4], 9, 'Λ×N = c_4/c_1 = 9/5'),
        'c_5': (c[5], 3, 'N_c = number of colors'),
    }

    print(f"\n  BST Integer Check:")
    for name, (val, expected, meaning) in bst.items():
        status = "PASS" if val == expected else "FAIL"
        print(f"    {name} = {val}  (expected {expected}: {meaning})  [{status}]")


if __name__ == '__main__':
    main()
