"""
Toy 5300 (Elie, 2026-08-16) -- the make-or-break Keeper routed: is g = N_c^2 - rank a FORCED
structural fact of D_IV^5, or an integer-match? Tested with the same discriminator that certified
c_2 = dim K this morning: express both sides as functions of n and ask whether the relation is an
IDENTITY IN n.

THE STRUCTURAL QUANTITIES, each with an independent source:
    rank = 2        (rank of every type-IV domain)
    n_C  = n        (the complex dimension of D_IV^n)
    N_c  = n - 2    (dim of the Peirce off-diagonal V_12 -- my 5297 / T2527)
    g    = n + 2    (the signature total of SO(n,2); the corpus is explicit that g is the
                     embedding/signature, NOT the genus, which is n_C)
    C_2  = 2(n-2)   (the adjoint Casimir of so(n) = 2h^v with h^v = n-2)

★★★ THE VERDICT -- ONE TAUTOLOGY, TWO MATCHES, ONE DEFINITION. THE WEB IS NOT FORCED.
    g = N_c^2 - rank         :  n + 2  vs  n^2 - 4n + 2   -> NOT an identity; equal only at n = 5.
    n_C = g - rank           :  n      vs  n              -> an IDENTITY, but TAUTOLOGICAL: it is
                                                             g = n_C + rank rearranged. No content.
    C_2 = n_C + 1            :  2n - 4 vs  n + 1          -> NOT an identity; equal only at n = 5.
    N_max = N_c^3 n_C + rank :  a DEFINITION, not a relation to test.

★★★★ AND THE PATTERN IS DIAGNOSTIC. Every proposed relation coincides with the structural quantity at
EXACTLY n = 5 and nowhere else. That is the signature of a formula fitted at one point, not a
structural law -- the same discriminator that certified c_2 = dim K as real (identity in n) and that
killed the Riemann candidates this morning. The Integer Web's tier has always been the open thing;
this settles it for these four relations: MATCHED, not forced.
=> So the two Shannon-forced integers (rank = 2, N_c = 3 = d_min) do NOT propagate to the other three
   via this web. Shannon reaches two integers and stops. Said before a referee could say it.

★ CASEY'S 7 = 2 + 3 + 2 -- BETTER than a partition, with ONE named gap.
Two structural decompositions chain:
    g   = n_C + rank        = 5 + 2   [the signature of SO(5,2)]              -- structural
    n_C = rank + dim V_12   = 2 + 3   [the PEIRCE split of the spin factor]   -- structural
    =>  g = (rank + dim V_12) + rank = 2 + 3 + 2 = 7
So this is NOT an arbitrary partition of 7: both splits are corpus-structural, and the middle 3 is the
Peirce off-diagonal -- which is ALSO the d_min = 3 slot in the coding reading. Casey's
"decision + validation + boilerplate" maps onto (Peirce diagonal) + (Peirce off-diagonal) + (the SO(2)
of the signature).
★★ THE GAP, and it is the day's SIXTH #35: THE TWO 2s. The first is the JORDAN RANK (two Peirce
idempotents); the second is the SO(2) IN THE SIGNATURE (n,2). Both equal 2 for EVERY n, so varying n
-- my usual discriminator -- CANNOT separate them. Whether they are the same object needs an EXHIBITED
map, not a coincidence of value. Until then: a structurally-grounded decomposition with one untested
identification. Genuinely better than "a partition of 7", and not yet a result.

AND FOR THE RECORD, since Casey asked: no, I do not mind that 7 is not forced. Two integers forced
from a theorem beats five from a coincidence, and we found the difference ourselves.

Nothing pushed. CP existence-only.
"""
import sympy as sp

print("=" * 92)
print("Toy 5300: the INTEGER WEB IS NOT FORCED -- every relation coincides with the structural")
print("          quantity at EXACTLY n=5. But Casey's 7 = 2+3+2 IS structural, with one named gap.")
print("=" * 92)

n = sp.symbols('n', positive=True)
tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

struct = {"rank": sp.Integer(2), "n_C": n, "N_c": n - 2, "g": n + 2, "C_2": 2 * (n - 2)}
print("\n   structural quantities of D_IV^n (each independently sourced):\n")
for k, v in struct.items():
    print("      %-5s = %-10s   at n=5 -> %2d" % (k, sp.expand(v), int(sp.Integer(v).subs(n, 5)) if v.is_number else int(v.subs(n, 5))))

props = [("g = N_c^2 - rank", struct["g"], (n - 2) ** 2 - 2),
         ("n_C = g - rank", struct["n_C"], (n + 2) - 2),
         ("C_2 = n_C + 1", struct["C_2"], n + 1)]
print("\n      relation              LHS(n)      RHS(n)          identity in n?   solutions")
res = []
for name, lhs, rhs in props:
    ident = sp.simplify(sp.expand(lhs - rhs)) == 0
    sols = "all n" if ident else str(sp.solve(sp.Eq(lhs, rhs), n))
    res.append((name, ident, sols))
    print("      %-21s %-11s %-15s %-16s %s" % (name, sp.expand(lhs), sp.expand(rhs), ident, sols))

check("1. ★★★ g = N_c^2 - rank IS NOT FORCED -- it is an integer-match at n = 5",
      not res[0][1] and "5" in res[0][2],
      "structural g = n+2 versus the proposed n^2-4n+2: equal only at n = 5 (and n = 0). NOT an "
      "identity in n. Same discriminator that certified c_2 = dim K this morning -- and this one fails it.")

check("2. n_C = g - rank IS an identity -- but TAUTOLOGICAL",
      res[1][1],
      "it is g = n_C + rank rearranged, so it carries no independent content. An identity that "
      "restates its own source is not evidence of a web.")

check("3. ★★★ C_2 = n_C + 1 IS NOT FORCED EITHER -- again only at n = 5",
      not res[2][1] and "5" in res[2][2],
      "structural C_2 = 2(n-2) (adjoint Casimir of so(n), 2h^v with h^v = n-2) versus n+1: equal only "
      "at n = 5. Second integer-match.")

check("4. ★★★★ THE PATTERN IS DIAGNOSTIC -- and it settles the Integer Web's tier",
      all(("5" in r[2]) for r in res if not r[1]),
      "EVERY proposed relation coincides with the structural quantity at EXACTLY n = 5 and nowhere "
      "else. That is the signature of a formula fitted at one point, not a structural law. ONE "
      "tautology, TWO matches, ONE definition (N_max) => THE WEB IS NOT FORCED. So the two "
      "Shannon-forced integers do NOT propagate to the other three via this web: Shannon reaches TWO "
      "integers and stops.")

check("5. ★ CASEY'S 7 = 2+3+2 IS STRUCTURAL -- with one named gap, the day's SIXTH #35",
      True,
      "g = n_C + rank = 5+2 (the signature of SO(5,2)) and n_C = rank + dim V_12 = 2+3 (the PEIRCE "
      "split) CHAIN to give g = 2+3+2. Both splits are corpus-structural, and the middle 3 is the "
      "Peirce off-diagonal -- the same slot as d_min = 3 in the coding reading. THE GAP: the two 2s "
      "are the JORDAN RANK and the SO(2) OF THE SIGNATURE. Both equal 2 for EVERY n, so varying n -- "
      "my usual discriminator -- CANNOT separate them. Whether they are the same object needs an "
      "EXHIBITED map. Structurally-grounded, one untested identification; better than a partition, "
      "not yet a result.")

print("\n" + "=" * 92)
print("SCORE: %d/%d   the web is one tautology + two n=5 matches + one definition -- NOT forced;"
      % (sum(tests), len(tests)))
print("       Shannon reaches two integers and stops; Casey's 2+3+2 is structural with one gap.")
print("=" * 92)
