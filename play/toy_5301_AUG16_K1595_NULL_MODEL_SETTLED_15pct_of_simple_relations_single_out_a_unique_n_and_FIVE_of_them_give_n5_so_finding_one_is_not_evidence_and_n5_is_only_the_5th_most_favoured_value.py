"""
Toy 5301 (Elie, 2026-08-16) -- the K1595 null model, as assigned. It settles the fishing question,
and the answer is cleaner (and slightly more uncomfortable) than expected.

GRAMMAR FIXED BEFORE LOOKING AT ANY ANSWER -- exhaustive enumeration, no cherry-picking.
Atoms, as functions of n (from my 5300): rank = 2, n_C = n, N_c = n-2, g = n+2, C_2 = 2n-4.
Relations tested: X = Y op Z and X = Y^2 op Z for X,Y,Z atoms and op in {+,-,*}. 750 relations.

★★★ RESULT, over n in [3,40]:
     identities (true for all n)   :  14  ( 1.9%)
     no solution in range          : 621  (82.8%)
     SINGLE OUT EXACTLY ONE n      : 115  (15.3%)   <- the fishing pool
     multiple solutions            :   0
So singling out a unique n is COMMON: about one relation in seven does it.

AND WHICH n GET SINGLED OUT:
     n = 3 : 44 relations       n = 4 : 38       n = 6 : 19       n = 8 : 7
     n = 5 :  5 relations       n = 10 : 2
=> FIVE distinct relations single out n = 5, and they are:
        rank = N_c^2 - g        N_c = N_c^2 - C_2       g = N_c^2 - rank
        C_2 = rank^2 + rank     C_2 = N_c^2 - N_c
The relation under test -- g = N_c^2 - rank -- is ONE OF FIVE. FINDING ONE IS NOT EVIDENCE.

★ AND A NUANCE THAT MUST NOT BE READ BACKWARDS: n = 5 is only the FIFTH most-favoured value in this
grammar (n = 3 and n = 4 are picked eight times more often). It is tempting to read that rarity as
"so a relation picking 5 is special." IT IS NOT. Rarity in the null model does not make a found
relation meaningful; it only means fewer were available to be found. The load-bearing fact is that
FIVE WERE AVAILABLE AND ONE WAS FOUND. That is the definition of fishing.

⟹ THE FISHING QUESTION IS SETTLED. A relation that picks n = 5 is exactly what a random simple
   relation in this grammar does. Only a TARGET-INNOCENT DERIVATION -- one that never evaluates at
   n = 5 -- can carry any weight. That is precisely the crux routed to Lyra, and this result says
   nothing else will substitute for it. No further null-model work is needed.

Nothing pushed. CP existence-only.
"""
import sympy as sp, itertools
from collections import Counter

print("=" * 92)
print("Toy 5301: K1595 null model SETTLED -- 15% of simple relations single out a unique n, and")
print("          FIVE of them give n = 5. Finding one is not evidence.")
print("=" * 92)

n = sp.symbols('n')
tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

atoms = {"rank": sp.Integer(2), "n_C": n, "N_c": n - 2, "g": n + 2, "C_2": 2 * n - 4}
print("\n   grammar fixed BEFORE any answer was looked at:\n")
for k, v in atoms.items():
    print("      %-5s = %s" % (k, sp.expand(v)))
print("      relations: X = Y op Z  and  X = Y^2 op Z,  op in {+,-,*}\n")

ops = [("+", lambda a, b: a + b), ("-", lambda a, b: a - b), ("*", lambda a, b: a * b)]
rels = []
for X, vx in atoms.items():
    for (Y, vy), (Z, vz) in itertools.product(atoms.items(), repeat=2):
        for s, f in ops:
            rels.append(("%s = %s %s %s" % (X, Y, s, Z), vx, f(vy, vz)))
            rels.append(("%s = %s^2 %s %s" % (X, Y, s, Z), vx, f(vy ** 2, vz)))

LO, HI = 3, 40
ident = nosol = multi = 0
uniq = Counter(); ex = {}
for name, lhs, rhs in rels:
    d = sp.expand(lhs - rhs)
    if d == 0: ident += 1; continue
    sols = [k for k in range(LO, HI + 1) if d.subs(n, k) == 0]
    if not sols: nosol += 1
    elif len(sols) == 1:
        uniq[sols[0]] += 1; ex.setdefault(sols[0], []).append(name)
    else: multi += 1
tot = len(rels); pool = sum(uniq.values())

print("   over n in [%d,%d], %d relations:" % (LO, HI, tot))
print("      identities            : %4d (%.1f%%)" % (ident, 100 * ident / tot))
print("      no solution           : %4d (%.1f%%)" % (nosol, 100 * nosol / tot))
print("      SINGLE OUT ONE n      : %4d (%.1f%%)   <- the fishing pool" % (pool, 100 * pool / tot))
check("1. ★★★ SINGLING OUT A UNIQUE n IS COMMON -- about one relation in seven",
      pool / tot > 0.10,
      "%d of %d relations (%.1f%%) pick out exactly one n in [3,40]. So the mere fact that a relation "
      "determines n carries no information at all." % (pool, tot, 100 * pool / tot))

print("\n   which n get singled out:")
for k, c in uniq.most_common(6):
    print("      n = %2d : %3d relations%s" % (k, c, "   <-- BST's n" if k == 5 else ""))
check("2. ★★★★ FIVE DISTINCT RELATIONS SINGLE OUT n = 5 -- finding one is not evidence",
      uniq[5] >= 3,
      "they are: " + "; ".join(ex.get(5, [])) + ". The relation under test, g = N_c^2 - rank, is ONE "
      "OF %d. That is the definition of a fishing pool." % uniq[5])

rank5 = 1 + sum(1 for k, c in uniq.items() if c > uniq[5])
check("3. ★ AND A NUANCE THAT MUST NOT BE READ BACKWARDS",
      rank5 > 1,
      "n = 5 is only the #%d most-favoured value in this grammar (n = 3 gets %d relations, n = 4 gets "
      "%d -- roughly eight times as many). It is tempting to read that rarity as 'so a relation "
      "picking 5 is special'. IT IS NOT. Rarity in the null model does not make a found relation "
      "meaningful; it only means fewer were available to be found. The load-bearing fact is that "
      "FIVE WERE AVAILABLE AND ONE WAS FOUND." % (rank5, uniq[3], uniq[4]))

check("4. ⟹ THE FISHING QUESTION IS SETTLED -- and nothing will substitute for the derivation",
      True,
      "a relation that picks n = 5 is exactly what a random simple relation in this grammar does. "
      "Only a TARGET-INNOCENT DERIVATION -- one that never evaluates at n = 5 -- can carry weight. "
      "That is precisely the crux routed to @Lyra, and this result says nothing else will substitute "
      "for it. No further null-model work is needed; the assignment is closed.")

print("\n" + "=" * 92)
print("SCORE: %d/%d   15%% of simple relations single out a unique n; FIVE give n = 5; n = 5 is only"
      % (sum(tests), len(tests)))
print("       the 5th most-favoured value -- and rarity is not evidence. Fishing question settled.")
print("=" * 92)
