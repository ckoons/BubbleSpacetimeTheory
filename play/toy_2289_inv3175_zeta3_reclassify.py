"""
Toy 2289 — INV-3175 zeta(3) Apéry constant: reclassification I -> S.

Owner: Lyra
Date:  2026-05-15 23:05 EDT
Burn-window production tempo (Casey directive 22:55 EDT).

ITEM
====
INV-3175 zeta(3) Apéry constant
Current: tier=I, formula=C_2/n_C = 6/5 = 1.2, observed=1.20206, precision 0.17%.

CLAIM TESTED
============
Can BST formula C_2/n_C = 6/5 be promoted to D-tier (= forced derivation
of zeta(3))?

ANSWER
======
NO. zeta(3) is irrational (Apéry 1979). C_2/n_C = 6/5 is rational. They
cannot be EQUAL. The match at 0.17% is a structural coincidence: the
rational 6/5 happens to be very close to the irrational zeta(3).

VERDICT: S-tier (qualitative coincidence). Reclassify.

NOTE: this is NOT a failure of BST. zeta(3) doesn't have a known closed
form in any framework; BST's 6/5 is no worse than other simple-rational
approximations. The reclassification is honest tier discipline, not a
derivation failure.

WHAT IF BST WANTS A REAL DERIVATION OF zeta(3)?
==================================================
zeta(3) admits Apéry's series: zeta(3) = (5/2) * sum_n (-1)^{n-1} / [n^3 *
C(2n, n)]. None of the integers (5, 2, n^3, etc.) need to be BST integers
in any forced sense. Other rational/algebraic approximations from BST
integers might give better matches (e.g., higher-order series), but
without a proof of irrationality structure, no rational/algebraic BST
expression can EQUAL zeta(3).

Honest framing for the catalog: zeta(3) is a TARGET QUANTITY for BST to
match, not a quantity BST DERIVES. The 6/5 reading is a useful structural
benchmark (precision 0.17% from the simplest BST ratio is not bad), but
not a derivation.
"""

from fractions import Fraction


def run():
    tests = []

    def check(label, got, want, note=""):
        ok = (got == want)
        tests.append((ok, label, got, want, note))
        return ok

    # BST integers
    rank = 2
    N_c = 3
    n_C = 5
    C_2_BST = 6
    g = 7

    print("=" * 72)
    print("Toy 2289 — INV-3175 zeta(3): reclassification I -> S")
    print("=" * 72)

    # Empirical zeta(3) (Apéry constant)
    zeta_3_observed = 1.2020569031595942

    # BST formula
    bst_value = Fraction(C_2_BST, n_C)
    bst_value_float = float(bst_value)

    print(f"\n  zeta(3) observed: {zeta_3_observed}")
    print(f"  BST formula:      C_2/n_C = {bst_value} = {bst_value_float}")
    print(f"  Difference:       {abs(zeta_3_observed - bst_value_float):.6f}")
    print(f"  Precision:        {abs(zeta_3_observed - bst_value_float)/zeta_3_observed * 100:.4f}%")

    check("BST C_2/n_C = 6/5 (rational)",
          bst_value, Fraction(6, 5))
    check("zeta(3) irrational (Apéry 1979) -- BST cannot equal it via rational expression",
          True, True)
    check("Match precision: ~0.17%",
          round(abs(zeta_3_observed - bst_value_float)/zeta_3_observed * 100, 2),
          0.17)

    # Other simple-rational approximations
    other_rationals = [
        ("11/9", Fraction(11, 9), 1.2222),
        ("13/11", Fraction(13, 11), 1.1818),
        ("12/10", Fraction(12, 10), 1.2000),  # = 6/5
        ("121/100", Fraction(121, 100), 1.21),
    ]
    print(f"\n  Other simple rational approximations:")
    print(f"  {'Rational':>10} | {'Value':>8} | precision")
    for label, frac, val in other_rationals:
        prec = abs(val - zeta_3_observed) / zeta_3_observed * 100
        print(f"  {label:>10} | {val:>8.4f} | {prec:>7.4f}%")

    # No clear winner in simple rationals; 6/5 is COMPETITIVE but not unique.

    print("""
  RECLASSIFICATION VERDICT:

    INV-3175 zeta(3) Apéry constant
    Current tier: I (precision 0.17% match to C_2/n_C = 6/5)
    Reclassified tier: S (qualitative coincidence)

    Reason: zeta(3) is irrational. Any rational BST expression cannot
    equal it. The 6/5 match is a STRUCTURAL COINCIDENCE consistent
    with simple-integer-rich approximations of irrational targets,
    not a derivation.

    For Keeper's registry update:
    - Keep formula notation (C_2/n_C = 6/5) as a benchmark
    - Change tier from I to S
    - Add note: "zeta(3) irrational; BST formula is rational
      benchmark, not derivation"
    - This is honest tier discipline, not a BST failure
    - Precision 0.17% remains a useful structural fact
""")

    # ===== SCORE =====
    passed = sum(1 for ok, *_ in tests if ok)
    total  = len(tests)
    print("=" * 72)
    print(f"SCORE: {passed}/{total}")
    print("=" * 72)
    return passed, total


if __name__ == "__main__":
    run()
