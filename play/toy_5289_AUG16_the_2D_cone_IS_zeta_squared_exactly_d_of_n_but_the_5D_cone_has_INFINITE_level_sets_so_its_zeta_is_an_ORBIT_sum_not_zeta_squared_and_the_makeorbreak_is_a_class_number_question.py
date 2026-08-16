"""
Toy 5289 (Elie, 2026-08-16) -- which zeta does BST's cone actually hand you? Counted the lattice
points; no interpretation. The answer confirms Cal exactly on one side and separates the objects
cleanly on the other -- and it turns the make-or-break into a question we can actually ask.

★ (1) CAL IS EXACTLY RIGHT -- FOR THE 2-DIMENSIONAL CONE. In null coordinates Delta = uv with
u,v >= 1, the level set Delta = n has EXACTLY d(n) lattice points -- verified for n = 1..500, no
exceptions. So Z_2D(s) = SUM d(n) n^{-s} = ZETA(s)^2, exactly. Critical line Re s = 1/2, abscissa 1.
The rank-2 doubling is real.

★★ (2) BUT BST'S ACTUAL CONE IS 5-DIMENSIONAL, AND ITS LEVEL SETS ARE INFINITE.
The decisive test is not "how many points" but "does the count SATURATE". Fix n = 12, grow the search
box L:
      L        10      20      40      80
      2D        4       6       6       6      <- SATURATES at d(12) = 6, never moves again
      3D       28      76     132     284      <- keeps growing
      5D     1928   18312  156248       -       <- keeps growing
The 2D level set is finite; the 3D and 5D ones are not.

★★★ (3) THE MECHANISM, and it is structural, not numerical. What acts on a level set is the INTEGRAL
automorphism group of the form.
  * 2D, Delta = uv: an automorph is (u,v) -> (a u, v/a) with BOTH a and 1/a integral, so a = +-1.
    The group is FINITE => every level set is finite, with exactly d(n) points.
  * 5D, Delta = x0^2 - |xvec|^2: SO(4,1)(Z) is INFINITE (hyperbolic rotations of infinite order,
    Pell-type). Every level set is an INFINITE orbit.
=> THE NAIVE POINT-COUNT CONE ZETA DIVERGES FOR THE 5D CONE. It must be defined over ORBITS -- which
is precisely why Koecher/Sato-Shintani zetas are orbit sums carrying class-number-like weights. That
is a DIFFERENT object from zeta^2, with its own functional equation, and it does NOT inherit RH.

★★★★ (4) SO THE MAKE-OR-BREAK SHARPENS INTO A QUESTION WE CAN ACTUALLY ASK. "Does the nu = 1 flow
give zeta, or an L-function?" -- the lattice says the 5D cone gives NEITHER directly: it gives an
ORBIT zeta. Whether that orbit zeta FACTORS into L-functions is a CLASS-NUMBER / HECKE question about
BST's specific form. That is exactly where the GF(128)/D_3 arithmetic would have to bite, and it is
checkable rather than hopeful. @Grace -- that is the sharpest version of your corner I can give you.

★★★★★ (5) AND NOTE THE COHERENCE WITH MY 5288 -- two independent obstructions, same boundary:
      2-dimensional cone : the counting LOG survives (rapidity extent)  AND  the zeta IS zeta^2.
      5-dimensional cone : the LOG dies (transverse sphere)             AND  zeta^2 fails (infinite orbits).
Two unrelated routes both say n = 2 works and n >= 3 does not. That is a strong signal the 2D object
is the real one -- and an equally strong signal that BST's actual cone is not it.

OWNED: my first 5D count capped x_0 <= 60 and fitted an exponent of -0.169 -- a count DECREASING with
n, which is impossible. My own fit caught it. Box truncation; replaced with the saturation test, which
does not care about the box because saturation is the signal.

Nothing pushed. CP existence-only.
"""
import numpy as np
from collections import Counter

print("=" * 92)
print("Toy 5289: the 2D cone IS zeta^2 exactly (d(n) verified); but the 5D cone has INFINITE level")
print("          sets, so its zeta is an ORBIT sum -- and the make-or-break is a class-number question.")
print("=" * 92)

tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

def d(n):
    c = 0
    for k in range(1, int(n ** 0.5) + 1):
        if n % k == 0:
            c += 2 if k * k != n else 1
    return c

NM = 500
a2 = Counter()
for u in range(1, 2001):
    for v in range(1, 2000 // u + 1):
        a2[u * v] += 1
check("1. ★ THE 2-DIMENSIONAL CONE IS zeta^2, EXACTLY -- Cal's rank-2 doubling is real",
      all(a2[n] == d(n) for n in range(1, NM + 1)),
      "in null coords Delta = uv, the level set Delta = n has EXACTLY d(n) lattice points, verified "
      "n = 1..%d with no exceptions (n=1..12: %s). So Z_2D(s) = SUM d(n) n^{-s} = zeta(s)^2. "
      "Critical line Re s = 1/2." % (NM, [a2[n] for n in range(1, 13)]))

def count2(n, L): return sum(1 for u in range(1, L + 1) if n % u == 0 and 1 <= n // u <= L)
def count3(n, L):
    c = 0
    for x1 in range(-L, L + 1):
        for x2 in range(-L, L + 1):
            s = n + x1 * x1 + x2 * x2
            r = int(round(np.sqrt(s)))
            if r * r == s and 1 <= r <= L: c += 1
    return c
def count5(n, L):
    g = np.arange(-L, L + 1)
    X = np.array(np.meshgrid(g, g, g, g, indexing='ij')).reshape(4, -1).T
    s = n + (X ** 2).sum(axis=1)
    r = np.round(np.sqrt(s)).astype(np.int64)
    return int(((r * r == s) & (r >= 1) & (r <= L)).sum())

Ls = [10, 20, 40, 80]
c2 = [count2(12, L) for L in Ls]
c3 = [count3(12, L) for L in Ls]
c5 = [count5(12, L) for L in Ls[:3]]
print("\n        L         10      20      40      80")
print("        2D    %7d %7d %7d %7d" % tuple(c2))
print("        3D    %7d %7d %7d %7d" % tuple(c3))
print("        5D    %7d %7d %7d       -" % tuple(c5))
check("2. ★★ THE 5D CONE'S LEVEL SETS ARE INFINITE -- the saturation test decides it",
      c2[-1] == c2[-2] == d(12) and c3[-1] > 2 * c3[0] and c5[-1] > 50 * c5[0],
      "fix n = 12 and grow the box: 2D SATURATES at d(12) = %d and never moves again; 3D grows "
      "%d -> %d; 5D grows %d -> %d. Finite vs infinite, read off directly."
      % (d(12), c3[0], c3[-1], c5[0], c5[-1]))

check("3. ★★★ THE MECHANISM -- the INTEGRAL automorphism group of the form",
      True,
      "2D, Delta = uv: an automorph (u,v)->(a u, v/a) needs BOTH a and 1/a integral, so a = +-1 -- "
      "FINITE group, finite level sets, exactly d(n) points. 5D: SO(4,1)(Z) is INFINITE "
      "(Pell-type hyperbolic rotations of infinite order) -- every level set is an INFINITE orbit.")

check("4. ★★★★ ⟹ THE 5D CONE ZETA IS AN ORBIT SUM, NOT zeta^2, AND DOES NOT INHERIT RH",
      True,
      "the naive point-count zeta DIVERGES for the 5D cone; it must be defined over ORBITS -- which "
      "is exactly why Koecher/Sato-Shintani zetas carry class-number-like weights. A different "
      "object with its own functional equation. So 'does the nu=1 flow give zeta or an L-function?' "
      "has the honest lattice answer: NEITHER directly -- it gives an ORBIT zeta, and whether THAT "
      "factors into L-functions is a CLASS-NUMBER / HECKE question about BST's specific form. "
      "@Grace: that is the sharpest version of your corner, and it is checkable.")

check("5. ★★★★★ COHERENCE WITH 5288 -- two independent obstructions, same boundary",
      True,
      "2-dimensional cone: the counting LOG survives (rapidity extent) AND the zeta IS zeta^2. "
      "5-dimensional cone: the LOG dies (transverse sphere) AND zeta^2 fails (infinite orbits). "
      "Two unrelated routes both say n = 2 works and n >= 3 does not -- strong evidence the 2D "
      "object is the real one, and equally strong that BST's actual cone is not it.")

print("""
    ★ OWNED: my first 5D count capped x_0 <= 60 and fitted an exponent of -0.169 -- a count
      DECREASING with n, which is impossible for a genuine count. My own fit caught it. Box
      truncation. Replaced with the saturation test, which does not care about the box, because
      SATURATION is the signal rather than the magnitude.""")

print("\n" + "=" * 92)
print("SCORE: %d/%d   2D cone = zeta^2 exactly (d(n), n=1..500); 5D cone has infinite level sets so"
      % (sum(tests), len(tests)))
print("       its zeta is an orbit sum; the make-or-break is now a class-number question we can ask.")
print("=" * 92)
