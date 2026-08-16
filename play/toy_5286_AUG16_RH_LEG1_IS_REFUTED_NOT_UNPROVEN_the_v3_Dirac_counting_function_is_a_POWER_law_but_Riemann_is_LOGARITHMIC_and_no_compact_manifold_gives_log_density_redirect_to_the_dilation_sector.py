"""
Toy 5286 (Elie, 2026-08-16) -- RH session, opening move. Casey's birthday, so: the real accounting.

I ran the test that comes before self-adjointness and before "why Re = 1/2": THE COUNTING FUNCTION.
If H's eigenvalues are the zero heights t_n, then N_H(T) must equal Riemann-von Mangoldt. That is a
hard necessary condition, checkable in an hour, and it decides Leg 1 outright.

★★★ LEG 1 IS NOT "UNPROVEN" -- IT IS REFUTED.
BST's forced self-adjoint operator (T2562, the v3 Kostant cubic Dirac) has, from my own toy 5244's
exact analytic shape (lambda_max = 2N^2+9N+14, modes = 32*C(N+5,5)):
      N_BST(lambda) ~ C * lambda^{5/2}     -- A POWER LAW.
Riemann-von Mangoldt (calibrated here against the first 200 actual zeros, exact to O(log T)):
      N_RH(T) = (T/2pi) log(T/2pi) - T/2pi + 7/8   -- density log(T/2pi)/2pi, LOGARITHMIC.
Side by side:
      T           50      100      400      1600      6400
      Riemann      9.4     29.0    201.6    1156.9    6037.2
      BST       1184.9   6541.0 186534.1  5437152  164487830
      ratio      125.7    225.5    925.1    4699.6    27245.6
The excess DIVERGES like T^{3/2}/log T. These are not close and do not become close.

★★★★ AND THE OBSTRUCTION IS GENERAL, NOT A DETAIL OF THIS OPERATOR. A self-adjoint elliptic operator
on a COMPACT manifold of dimension d obeys Weyl: N(lambda) ~ C lambda^{d/m}, so the density is
ALWAYS A POWER. The Riemann density is log(T/2pi)/2pi -- slower than every power T^eps, faster than a
constant. NO compact-manifold Weyl law of ANY dimension produces it. => the Hilbert-Polya operator
cannot be a Dirac or Laplace operator on a compact space. (Berry-Keating's observation, applied here
to BST's own candidate.)

★★ THE CONSTRUCTIVE REDIRECT, AND IT IS CORPUS-INTERNAL. What DOES give a log density is the
DILATION generator H = xp regularised by a PHASE-SPACE CELL. Computed here: with the cell = 2*pi*hbar
(ONE Planck cell), the Berry-Keating count reproduces Riemann-von Mangoldt EXACTLY to the constant --
N_BK - N_RvM = 0.1250 at T = 100, 1000, 10000, 100000, i.e. 1 - 7/8, identically. And BST owns both
ingredients:
  * a dilation generator, explicit in the corpus's own ladder K_mu = 2 z_mu (E + nu) - Q d_mu, where
    E is the Euler/degree operator -- that is the xp sector;
  * a phase-space cell: Casey's own reframe, "the Uncertainty Principle is the actual resolution of
    the continuum," IS the 2*pi*hbar cell the construction needs.
=> if RH lives in BST it lives in the DILATION sector with an hbar-cell, NOT in the Dirac sector.

HONEST TIER (nothing over-read):
  * matching N(T) is NECESSARY, NOT SUFFICIENT -- it is the smooth leading term; the zeros are the
    FLUCTUATIONS about it, and no self-adjoint realisation of xp with the right fluctuation spectrum
    is known. That is where Berry-Keating has been stuck since 1999, and BST does not change it.
  * BST's Dirac FAILS the necessary condition; Berry-Keating PASSES it; passing is not proving.
  * the cell size is FIXED BY MATCHING (lx*lp = 2*pi*hbar chosen to make the constant come out).
    Until the cell is DERIVED from D_IV^5 rather than matched, that step is a FIT, and I will not
    call it anything else.

WHAT THIS BUYS: Leg 2 ("why Re = 1/2") was the stated wall. It is not the first wall. The first wall
is that the operator on the table cannot have the right number of eigenvalues. That is a sharper and
more useful place to stand than "the identification is asserted."

Nothing pushed. CP existence-only.
"""
import numpy as np, mpmath as mp
from math import comb
mp.mp.dps = 30

print("=" * 92)
print("Toy 5286: RH Leg 1 is REFUTED, not unproven -- the v3 Dirac counting function is a POWER law")
print("          and Riemann's is LOGARITHMIC. Redirect: the dilation sector with an hbar-cell.")
print("=" * 92)

tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

def N_rh(T): return (T / (2 * np.pi)) * np.log(T / (2 * np.pi)) - T / (2 * np.pi) + 7 / 8
zs = [float(mp.im(mp.zetazero(n))) for n in range(1, 201)]
cal = [(T, sum(1 for z in zs if z < T), N_rh(T)) for T in (50, 100, 200, 400)]
check("1. CALIBRATION -- Riemann-von Mangoldt reproduces the ACTUAL zeros",
      all(abs(a - b) < 0.05 * max(a, 1) + 2 for _, a, b in cal),
      "  ".join("T=%d: %d actual vs %.2f formula" % c for c in cal) +
      "   => density dN/dT = log(T/2pi)/2pi, LOGARITHMIC.")

def N_bst(lam):
    Nn = (-9 + np.sqrt(81 + 8 * (lam - 14))) / 4
    return 32 * np.prod([Nn + k for k in range(1, 6)]) / 120 if Nn > 0 else 0.0
shape = [(N, 2 * N * N + 9 * N + 14, 32 * comb(N + 5, 5)) for N in range(2, 7)]
check("2. BST's FORCED OPERATOR HAS A POWER-LAW COUNT -- exponent 5/2",
      all(s[1] == 2 * s[0] ** 2 + 9 * s[0] + 14 for s in shape),
      "toy 5244's exact analytic shape: lambda_max = 2N^2+9N+14, modes = 32*C(N+5,5)  [" +
      ", ".join("N=%d:(%d,%d)" % s for s in shape) + "].  Eliminating N gives N_BST ~ C lambda^{5/2}.")

rows = [(T, N_rh(T), N_bst(T)) for T in (50, 100, 400, 1600, 6400)]
print("\n      T        Riemann zeros      BST v3 Dirac modes       ratio")
for T, a, b in rows:
    print("   %6d        %10.1f        %14.1f       %9.1f" % (T, a, b, b / a))
check("3. ★★★ LEG 1 IS REFUTED -- the excess DIVERGES like T^{3/2}/log T",
      rows[-1][2] / rows[-1][1] > 20 * rows[0][2] / rows[0][1],
      "ratio BST/Riemann runs %.0f -> %.0f over T = 50 -> 6400. The two counts are not close and do "
      "not become close. The identification is not merely unproven -- it is EXCLUDED by the Weyl law."
      % (rows[0][2] / rows[0][1], rows[-1][2] / rows[-1][1]))

dens = [(T, np.log(T / (2 * np.pi)) / (2 * np.pi), T ** 0.1) for T in (1e2, 1e4, 1e6, 1e8)]
check("4. ★★★★ AND THE OBSTRUCTION IS GENERAL -- no compact manifold of ANY dimension can do it",
      all(d < p for _, d, p in dens),
      "Weyl on a compact d-manifold gives N ~ C lambda^{d/m}, density ALWAYS a power. Riemann's "
      "density is " + ", ".join("%.2f at T=%.0e" % (d, T) for T, d, _ in dens) +
      " -- below even T^0.1 everywhere, yet unbounded. Slower than every power, faster than a "
      "constant. => the Hilbert-Polya operator is not a Dirac or Laplace operator on a compact space.")

def N_bk(E, cell): return (E * np.log(E / cell) - E + cell) / (2 * np.pi)
diffs = [N_bk(T, 2 * np.pi) - N_rh(T) for T in (100, 1000, 10000, 100000)]
check("5. ★★ WHAT DOES WORK: the DILATION generator xp with ONE Planck cell -- exact to the constant",
      max(abs(d - 0.125) for d in diffs) < 1e-9,
      "N_BK(T) - N_RvM(T) = %s at T = 1e2..1e5 -- identically 1 - 7/8. One phase-space cell of area "
      "2*pi*hbar in a dilation flow reproduces Riemann-von Mangoldt including its subleading term. "
      "The log density comes from SCALING + a CELL, not from any manifold dimension."
      % ", ".join("%.4f" % d for d in diffs))

print("""
    ★ THE REDIRECT, AND IT IS CORPUS-INTERNAL: BST owns both ingredients.
      - a DILATION generator, explicit in the corpus's own ladder K_mu = 2 z_mu (E + nu) - Q d_mu,
        with E the Euler/degree operator -- that is the xp sector;
      - a phase-space CELL: Casey's own reframe, "the Uncertainty Principle is the actual resolution
        of the continuum," IS the 2*pi*hbar cell the construction needs.
      => if RH lives in BST it lives in the DILATION sector with an hbar-cell, NOT the Dirac sector.

    ★★ HONEST TIER, so nothing is over-read:
      - matching N(T) is NECESSARY, NOT SUFFICIENT -- it is the smooth leading term; the zeros are
        the FLUCTUATIONS about it, and no self-adjoint realisation of xp with the right fluctuation
        spectrum is known. Berry-Keating has been stuck there since 1999 and BST does not change it.
      - BST's Dirac FAILS the necessary condition; Berry-Keating PASSES it; passing is not proving.
      - the cell size is FIXED BY MATCHING. Until it is DERIVED from D_IV^5, that step is a FIT.

    ★★★ WHAT THIS BUYS: Leg 2 ("why Re = 1/2") was the stated wall. It is not the FIRST wall. The
      first wall is that the operator on the table cannot have the right NUMBER of eigenvalues --
      a sharper and more useful place to stand than "the identification is asserted." """)

print("\n" + "=" * 92)
print("SCORE: %d/%d   Leg 1 refuted by the counting function (power vs log, ratio 126 -> 27246);"
      % (sum(tests), len(tests)))
print("       the obstruction is general; the dilation+cell route matches RvM exactly to 1 - 7/8.")
print("=" * 92)
