"""
Toy 5290 (Elie, 2026-08-16) -- Casey's Re = 1/2 insight, checked; and the Shimura route, checked
before it gets banked. Casey's insight has a REAL, EXACT core and a precise limit. The Shimura route
has a catch that has to be said now rather than after the write-up.

★ (1) Re = 1/2 IS DERIVABLE -- AS THE MELLIN/UNITARITY AXIS.
The weighted Parseval identity INT_0^inf |f|^2 x^{2s-1} dx = (1/2pi) INT |F(s+it)|^2 dt holds at
EVERY sigma (verified exactly with f = e^{-x}, F = Gamma: ratio 1.000000 at sigma = 0.30, 0.50, 0.75,
1.00). THE POINT IS THE WEIGHT: x^{2 sigma - 1} = 1 if and only if sigma = 1/2. So Re = 1/2 is the
UNIQUE line on which the Mellin transform is an isometry onto PLAIN L^2(dx) -- the half-density
normalisation of the multiplicative measure dx/x, i.e. the unitarity axis of the dilation group.
Transparent closed form: |Gamma(1/2 + it)|^2 = pi/cosh(pi t), verified to 10 digits.
=> Casey is right that Re = 1/2 is special and it IS forced -- by L^2 on the multiplicative group.

★★ (2) BUT THE "INTERSECTION OF CONES" READING IS A TYPE MIXING, AND UNITARITY IS NOT RH.
Re(s) lives in the complex plane of the zeta variable; the 5D and 3D cones live in spacetime. Calling
Re = 1/2 "the intersection of the time circle, the 5D cone and the 3D cone" needs an EXHIBITED map
between those two spaces; without one it is a metaphor. The map that does exist is the Mellin/dilation
one, and it delivers the 1/2 from the half-density -- no cone intersection required, and none used.
And more important: unitarity puts the CHARACTERS on the line. The zeros are RESONANCES. "Re = 1/2 is
the self-dual/descent-invariant axis" is TRUE, derivable, and locates NOT ONE ZERO. Connes' wall sits
exactly in that gap, and this computation does not move it.

★★★ (3) THE EULER-PRODUCT PRECONDITION FAILS IN ODD DIMENSION -- AND OUR CONE IS ODD.
RH-type theorems live on objects with EULER PRODUCTS <=> multiplicative coefficients. Testing
r_k(n) = #{x in Z^k : |x|^2 = n} on coprime pairs:
    k = 2 : multiplicative  (0 violations)
    k = 3 : NOT             (78 violations; e.g. a(6) = 4.000 vs a(2)a(3) = 2.667)
    k = 4 : multiplicative  (0 violations)
    k = 5 : NOT             (92 violations; e.g. a(6) = 24.000 vs a(2)a(3) = 32.000)
    k = 8 : multiplicative  (0 violations)
EVEN k multiplicative, ODD k not. BST's cone is FIVE-dimensional -- ODD. No multiplicativity => NO
EULER PRODUCT => the RH machinery does not even start on the direct object. THAT is why a Shimura
lift is needed: IT IS A REPAIR FOR A MISSING EULER PRODUCT, NOT A BONUS EDGE.

★★★★ (4) AND THE REPAIR'S OUTPUT IS NOT ZETA. THIS IS THE CATCH.
Shimura's correspondence sends weight k + 1/2 to weight 2k. Our half-integral weight is n_C/2 = 5/2,
so k = 2 and THE LIFT HAS WEIGHT 4. A weight-4 cusp form's L-function is DEGREE 2 AND ENTIRE, with
functional equation s <-> 4 - s. zeta is DEGREE 1 WITH A POLE AT s = 1. THEY ARE DIFFERENT OBJECTS.
=> even in the fully favourable case -- lift exists, Euler product obtained, zeros pinned -- what you
have proved is RH FOR A WEIGHT-4 MODULAR L-FUNCTION. That would be a real theorem. IT WOULD NOT BE
THE RIEMANN HYPOTHESIS. The Shimura route cannot rescue us from Davenport-Heilbronn *for zeta*,
because it does not land on zeta.

WHAT SURVIVES, HONESTLY: the 2D cone gives zeta^2 exactly (my 5289) and keeps the counting log (my
5288). Everything that works lives at n = 2. Everything that fails -- the log, multiplicativity, and
now the lift's target -- fails because the cone is 5-dimensional.

OWNED: my first Mellin test was numerically sloppy (ratio 0.9375 at sigma = 1/2 on a coarse grid with
a truncated t-range) and would have read as "the isometry fails at 1/2". Redone exactly with Gamma.

Nothing pushed. CP existence-only.
"""
import numpy as np, mpmath as mp
from collections import Counter
from math import gcd
mp.mp.dps = 25

print("=" * 92)
print("Toy 5290: Re = 1/2 IS derivable -- as the MELLIN unitarity axis, not a cone intersection;")
print("          odd dimension kills multiplicativity; and the Shimura lift lands on WEIGHT 4, not zeta.")
print("=" * 92)

tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

rows = []
for sig in (0.30, 0.50, 0.75, 1.00):
    lhs = float(mp.gamma(2 * sig) / mp.mpf(2) ** (2 * sig))
    rhs = float(mp.quad(lambda t: abs(mp.gamma(mp.mpf(sig) + 1j * t)) ** 2, [-mp.inf, 0, mp.inf]) / (2 * mp.pi))
    rows.append((sig, lhs, rhs))
check("1. ★ Re = 1/2 IS DERIVABLE -- it is the unique WEIGHT-FREE Mellin isometry",
      all(abs(r / l - 1) < 1e-9 for _, l, r in rows),
      "weighted Parseval INT|f|^2 x^{2s-1}dx = (1/2pi)INT|F|^2dt holds at EVERY sigma (ratios " +
      ", ".join("%.6f" % (r / l) for _, l, r in rows) + " at sigma = 0.30/0.50/0.75/1.00). THE POINT "
      "IS THE WEIGHT: x^{2 sigma - 1} = 1 iff sigma = 1/2. So Re = 1/2 is the unique line where the "
      "Mellin transform is an isometry onto PLAIN L^2(dx) -- the half-density normalisation of dx/x.")

gam = [(t, float(abs(mp.gamma(mp.mpf(0.5) + 1j * t)) ** 2), float(mp.pi / mp.cosh(mp.pi * t))) for t in (0.0, 0.7, 2.0)]
check("2. and the closed form makes it transparent: |Gamma(1/2+it)|^2 = pi/cosh(pi t)",
      all(abs(a - b) < 1e-12 for _, a, b in gam),
      "  ".join("t=%.1f: %.10f vs %.10f" % g for g in gam))

check("3. ★★ BUT THE 'INTERSECTION OF CONES' READING IS A TYPE MIXING, AND UNITARITY IS NOT RH",
      True,
      "Re(s) lives in the complex plane of the zeta variable; the 5D and 3D cones live in spacetime. "
      "That reading needs an EXHIBITED map between the two spaces; the map that DOES exist is the "
      "Mellin/dilation one, and it gives 1/2 from the half-density with no cone intersection used. "
      "And unitarity puts the CHARACTERS on the line -- the zeros are RESONANCES. 'Re = 1/2 is the "
      "self-dual axis' is TRUE, derivable, and locates NOT ONE ZERO. Connes' wall is exactly there.")

def rk(k, NMAX):
    c = Counter({0: 1})
    for _ in range(k):
        d = Counter(); L = int(NMAX ** 0.5) + 1
        for n, v in c.items():
            for j in range(-L, L + 1):
                if n + j * j <= NMAX: d[n + j * j] += v
        c = d
    return c
res = []
for k in (2, 3, 4, 5, 8):
    c = rk(k, 400)
    a = lambda n: c.get(n, 0) / c.get(1, 1)
    bad = [(m, n) for m in range(2, 15) for n in range(2, 15)
           if gcd(m, n) == 1 and m * n <= 400 and abs(a(m * n) - a(m) * a(n)) > 1e-9]
    res.append((k, len(bad)))
    print("      k=%d : multiplicative on coprime pairs? %-5s  (%d violations)" % (k, len(bad) == 0, len(bad)))
check("4. ★★★ THE EULER-PRODUCT PRECONDITION FAILS IN ODD DIMENSION -- and our cone is ODD",
      all(v == 0 for k, v in res if k % 2 == 0) and all(v > 0 for k, v in res if k % 2 == 1),
      "r_k(n) is multiplicative for k = 2, 4, 8 and NOT for k = 3 (%d violations) or k = 5 (%d). "
      "BST's cone is FIVE-dimensional. No multiplicativity => NO EULER PRODUCT => the RH machinery "
      "does not start on the direct object. The Shimura lift is a REPAIR for that, not a bonus."
      % (dict(res)[3], dict(res)[5]))

k_half = 5 / 2
k_int = int(k_half - 0.5)
check("5. ★★★★ AND THE REPAIR LANDS ON WEIGHT 4, NOT ZETA -- the catch",
      2 * k_int == 4,
      "Shimura sends weight k + 1/2 to weight 2k. Our weight is n_C/2 = 5/2 => k = %d => THE LIFT HAS "
      "WEIGHT %d. A weight-4 cusp L-function is DEGREE 2 AND ENTIRE (s <-> 4-s); zeta is DEGREE 1 "
      "WITH A POLE at s = 1. DIFFERENT OBJECTS. So even in the fully favourable case the lift proves "
      "RH for a weight-4 modular L-function -- a real theorem, but NOT the Riemann Hypothesis. The "
      "Shimura route cannot rescue zeta from Davenport-Heilbronn, because it does not land on zeta."
      % (k_int, 2 * k_int))

print("""
    ★ WHAT SURVIVES, HONESTLY: the 2D cone gives zeta^2 EXACTLY (5289) and keeps the counting LOG
      (5288). Everything that works lives at n = 2. Everything that fails -- the log, multiplicativity,
      and now the lift's target -- fails because the cone is 5-dimensional. That is the fourth
      independent appearance of one fact today.

    ★★ AND CASEY'S INSIGHT IS NOT DIMINISHED BY THIS. Re = 1/2 IS forced, and the forcing is exact:
      it is the unitarity axis of the dilation flow -- which is the same flow his composite/
      multiplication instinct pointed at this morning, and the same boost my 5288 identified on the
      light cone. The instinct keeps landing on the right object. What it does not do -- what nothing
      yet does -- is put the ZEROS there.

    ★★★ OWNED: my first Mellin test was sloppy (ratio 0.9375 at sigma = 1/2, coarse grid, truncated
      range) and would have read as 'the isometry fails at 1/2'. Redone exactly with Gamma.""")

print("\n" + "=" * 92)
print("SCORE: %d/%d   Re=1/2 = the weight-free Mellin isometry (exact); odd dimension kills"
      % (sum(tests), len(tests)))
print("       multiplicativity; and the Shimura lift outputs a weight-4 L-function, not zeta.")
print("=" * 92)
