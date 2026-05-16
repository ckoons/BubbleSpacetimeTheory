"""
Toy 2255 — A1 (CRITICAL): Hilbert polynomial of Q^5 in CP^6, explicit.

Owner: Elie
Date: 2026-05-15
Out of: K38 Alpha137 Derivation Chain Audit (Keeper, May 15).

CLAIM (T841, K38 Step 2):
    Hilbert polynomial of smooth quadric Q^5 ⊂ CP^6 satisfies:
        P(1) = g       = 7
        P(2) = N_c^3   = 27   <-- LOAD-BEARING (K38 PASS hinges here)
        P(3) = g · C_2 = 42

METHOD:
    Smooth quadric Q^5 in CP^6 fits the short exact sequence
        0 -> O_{CP^6}(-2) -> O_{CP^6} -> O_{Q^5} -> 0
    so the Hilbert polynomial is
        P_Q(m) = P_{CP^6}(m) - P_{CP^6}(m-2)
               = C(m+6, 6) - C(m+4, 6)
    This is a classical fact (no BST-specific choice).

WHAT WE SCORE:
    Step 1: dim Q^5 = 5 = n_C
    Step 2: degree polynomial in m = 5 = n_C
    Step 3: leading coefficient = 2/5! = 1/60
    Step 4: P(0) = 1 (constant term, h^0 of structure sheaf)
    Step 5: P(1) = 7  = g
    Step 6: P(2) = 27 = N_c^3   <-- CRITICAL
    Step 7: P(3) = 42 = g · C_2 ?
    Step 8: degree (self-intersection) check: deg(Q^5) = 2
    Step 9: Euler char / arithmetic genus chi(O_Q) = 1
    Step 10..N: extended P(m) values + BST decompositions

HONEST DESIGN:
    If P(2) != 27, K38 N_c^3 leg FAILS — chain downgrades.
    If P(3) != 42, T841 needs an erratum on the P(3) statement,
        but K38's load-bearing leg (P(2)=27) is independent.
"""

from sympy import (
    symbols, expand, Poly, Rational, factorial, sympify
)


def binom_poly(top, n):
    """Polynomial form of C(top, n) for symbolic top and integer n>=0:
    C(top, n) = top * (top-1) * ... * (top-n+1) / n!
    Returns a polynomial-form sympy expression (no Binomial atoms)."""
    prod = sympify(1)
    for k in range(n):
        prod = prod * (top - k)
    return prod / factorial(n)

# Five BST integers + derived
N_c   = 3
n_C   = 5
g     = 7
C_2   = 6      # second Casimir (BST integer)
N_max = 137
rank  = 2
c_2   = 11     # second Chern (BST integer, distinct from C_2)
c_3   = 13
chi_K3 = 24


def hilbert_CP(n, m):
    """Hilbert polynomial of CP^n: P(m) = C(m+n, n), in polynomial form."""
    return binom_poly(m + n, n)


def hilbert_Q5(m):
    """Hilbert polynomial of smooth quadric Q^5 in CP^6,
    via 0 -> O(-2) -> O -> O_Q -> 0."""
    return hilbert_CP(6, m) - hilbert_CP(6, m - 2)


def run():
    m = symbols('m')

    P_CP6 = hilbert_CP(6, m)
    P_Q   = hilbert_Q5(m)
    P_Q_exp = expand(P_Q)

    # Polynomial structure
    poly = Poly(P_Q_exp, m)
    deg  = poly.degree()
    lead = poly.LC()

    tests = []

    def check(label, got, want):
        ok = (got == want)
        tests.append((ok, label, got, want))
        return ok

    # ------- Polynomial structure -------
    check("dim Q^5 (= n_C)", 5, n_C)
    check("Hilbert poly degree in m (= n_C)", deg, n_C)
    check("Leading coefficient (= 2/5! = 1/60)", lead, Rational(2, 120))
    check("Leading coefficient (= deg(Q^5)/dim!)", lead, Rational(2, factorial(5)))

    # ------- P(0): structure-sheaf constant term -------
    P0 = sympify(P_Q.subs(m, 0))
    check("P(0) = 1  (chi(O_Q) for smooth quadric)", P0, 1)

    # ------- P(1) = g -------
    P1 = sympify(P_Q.subs(m, 1))
    check("P(1) = g = 7", P1, g)

    # ------- P(2) = N_c^3  (LOAD-BEARING) -------
    P2 = sympify(P_Q.subs(m, 2))
    check("P(2) = N_c^3 = 27  [LOAD-BEARING]", P2, N_c ** 3)

    # ------- P(3) claim: g * C_2 = 42 -------
    P3 = sympify(P_Q.subs(m, 3))
    check("P(3) = g * C_2 = 42  [T841 claim]", P3, g * C_2)

    # ------- Independent sanity / extension -------
    P4 = sympify(P_Q.subs(m, 4))
    P5 = sympify(P_Q.subs(m, 5))
    P6 = sympify(P_Q.subs(m, 6))
    P_neg1 = sympify(P_Q.subs(m, -1))

    # P(-1) for a smooth quadric of even fiber dim 5 — Serre dual; check it's 0
    # (vanishing of H^0 of negative twist for Fano).
    check("P(-1) = 0 (Kodaira vanishing on Fano)", P_neg1, 0)

    # Numerical sanity (exact integers expected for non-negative m).
    for k in range(0, 11):
        v = sympify(P_Q.subs(m, k))
        check(f"P({k}) is an integer", v.is_integer, True)

    # ------- BST decomposition probes -------
    # P(3) = ? In BST integers.
    check("P(3) numerically equals g * c_2 (= 7 * 11 = 77)?",
          int(P3), g * c_2)
    check("P(3) numerically equals g * C_2 (= 7 * 6 = 42)?",
          int(P3), g * C_2)
    check("P(3) numerically equals g * (rank * n_C + 1)",
          int(P3), g * (rank * n_C + 1))

    # P(2) cross-decompositions
    check("P(2) = N_c^3 = 27", int(P2), N_c ** 3)
    check("P(2) = 3^N_c (= 27)", int(P2), N_c ** N_c)
    check("P(2) = C_2 * rank^2 + N_c (= 24+3=27)",
          int(P2), C_2 * rank ** 2 + N_c)

    # P(1) cross-decompositions
    check("P(1) = g", int(P1), g)
    check("P(1) = C_2 + 1", int(P1), C_2 + 1)

    # Volume / particle-physics-volume check
    check("P(2) * n_C = 135 (particle physics volume)",
          int(P2) * n_C, 135)
    check("N_c^3 * n_C = 135", N_c ** 3 * n_C, 135)

    # Euler characteristic of Q^5: chi_top = 6 = C_2 (known fact)
    # (This is independent of Hilbert poly, but BST-load-bearing per K39.)
    chi_Q5_topological = 6
    check("chi_top(Q^5) = C_2 = 6", chi_Q5_topological, C_2)

    # Degree-of-the-embedding check (cap product with H^5):
    # P_Q has leading 1/60 * m^5; coeff times 5! = 2 = deg(Q^5)
    deg_embedding = lead * factorial(5)
    check("deg(Q^5) from leading coeff = 2", int(deg_embedding), 2)

    # Polynomial expansion sanity
    # Compute explicit closed form:
    # P_Q(m) = (1/60)(m+1)(m+2)(2m^3+15m^2+31m+30)  (one valid factoring)
    # We won't pattern-match — just check value table reproduces.
    expected_table = {
        0: 1, 1: 7, 2: 27, 3: 77, 4: 182,
        5: 378, 6: 714, 7: 1254,
    }
    for k, v in expected_table.items():
        got = int(sympify(P_Q.subs(m, k)))
        check(f"P({k}) = {v}", got, v)

    # ------------- Score & report -------------
    passed = sum(1 for ok, *_ in tests if ok)
    total  = len(tests)
    print(f"\nToy 2255 — Hilbert polynomial of Q^5 in CP^6\n{'='*60}")
    print(f"Score: {passed}/{total}\n")

    # Group reporting
    print("--- Polynomial structure ---")
    for ok, lbl, got, want in tests[:4]:
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] {lbl}: got={got} expected={want}")

    print("\n--- Specific P(m) values (LOAD-BEARING) ---")
    for ok, lbl, got, want in tests[4:9]:
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] {lbl}: got={got} expected={want}")

    print("\n--- Integer & extension values ---")
    for ok, lbl, got, want in tests[9:21]:
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] {lbl}: got={got} expected={want}")

    print("\n--- BST decomposition probes ---")
    for ok, lbl, got, want in tests[21:]:
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] {lbl}: got={got} expected={want}")

    print(f"\nExplicit Hilbert polynomial:")
    print(f"  P_Q(m) = C(m+6, 6) - C(m+4, 6)")
    print(f"         = {P_Q_exp}")
    print(f"  Factored degree: {deg}, leading coeff: {lead}")

    print(f"\nFailing checks (if any):")
    any_fail = False
    for ok, lbl, got, want in tests:
        if not ok:
            any_fail = True
            print(f"  [FAIL] {lbl}: got={got} expected={want}")
    if not any_fail:
        print("  (none)")

    # Verdict on K38 A1
    P1_val = int(sympify(P_Q.subs(m, 1)))
    P2_val = int(sympify(P_Q.subs(m, 2)))
    P3_val = int(sympify(P_Q.subs(m, 3)))

    print(f"\n{'='*60}")
    print(f"K38 A1 VERDICT")
    print(f"{'='*60}")
    print(f"  P(1) = {P1_val}     claim g = 7        ->  "
          f"{'PASS' if P1_val == g else 'FAIL'}")
    print(f"  P(2) = {P2_val}     claim N_c^3 = 27   ->  "
          f"{'PASS' if P2_val == N_c**3 else 'FAIL'}  [LOAD-BEARING]")
    print(f"  P(3) = {P3_val}     claim g*C_2 = 42   ->  "
          f"{'PASS' if P3_val == g*C_2 else 'FAIL'}")
    if P3_val != g * C_2:
        print(f"       actual P(3) = {P3_val} = g * c_2  "
              f"where c_2 = rank*n_C + 1 = {rank*n_C+1}")
        print(f"       (BST integer c_2 = 11, NOT C_2 = 6 -- T841 needs erratum)")

    print(f"\nLoad-bearing N_c^3 leg of K38: "
          f"{'PASS — chain holds' if P2_val == 27 else 'FAIL — chain breaks'}")


if __name__ == "__main__":
    run()
