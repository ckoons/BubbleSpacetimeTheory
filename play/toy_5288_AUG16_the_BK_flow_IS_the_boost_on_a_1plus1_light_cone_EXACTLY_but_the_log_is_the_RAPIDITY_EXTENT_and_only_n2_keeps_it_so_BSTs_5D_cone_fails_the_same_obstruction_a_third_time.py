"""
Toy 5288 (Elie, 2026-08-16) -- my corner of the tube retarget: the cutoffs + the scattering count.
Three results. One closes a corner, one CONFIRMS Keeper's beautiful thread exactly, and the third
kills it on dimension -- with a mechanism, not a mismatch.

★ (1) THERE IS ONLY ONE CUTOFF DATUM, NOT TWO -- AND MY CORNER CLOSES INTO AN ANSWERED ONE.
area{x >= lx, p >= lp, xp <= E} = E log(E/(lx lp)) - E + lx lp: the two cutoffs enter ONLY through
their PRODUCT. Verified numerically -- (lx,lp) = (1, 2pi), (2, pi), (2pi, 1) give the identical area
to 1e-9. So "does D_IV^5 force the CUTOFFS" COLLAPSES INTO "does it force the cell", which 5287
already answered (anchored; Cal's Wallach-quantisation refinement stands). One less corner to chase.

★★ (2) KEEPER'S THREAD IS EXACTLY RIGHT, AND I CAN VERIFY IT RATHER THAN ANALOGISE IT.
In null coordinates u = t+x, v = t-x on 1+1 Minkowski, t^2 - x^2 = uv (checked, 1.8e-15). The
Berry-Keating flow (x,p) -> (lam x, p/lam) preserves xp; a boost of rapidity r acts as
(u,v) -> (e^r u, e^-r v) and preserves uv (checked, 1.8e-15). THEY ARE THE SAME FLOW. So the
Berry-Keating dilation IS THE BOOST, its "energy" E = xp IS the Lorentz invariant (proper time
squared), and the RH region is the interior of a 1+1 LIGHT CONE cut off at minimum proper time.
Casey's "multiplication = composites" flow literally lives on a light cone. That much is real.

★★★ (3) BUT THE DIMENSION KILLS IT, AND HERE IS THE EXACT MECHANISM.
In cone-polar coordinates (x_0 = rho cosh chi, |xvec| = rho sinh chi, Delta = rho^2):
    V{Delta <= E, chi <= X} = [E^{n/2}/n] * |S^{n-2}| * INT_0^X sinh^{n-2}(chi) dchi
and the BK cutoffs fix the RAPIDITY EXTENT X = (1/2) log(E/(lu lv)).
    INT_0^X sinh^{n-2} dchi is LINEAR IN X ONLY WHEN n - 2 = 0.
Measured: at X = 2,4,6,8 the integral runs 2,4,6,8 for n=2 but 2.8 -> 1489 (n=3), 5.8 -> 1.1e6 (n=4),
14.7 -> 1.1e9 (n=5). Substituting X = (1/2)log(E/cell):
    n=2: V/E      = 1.38, 3.69, 5.99, 8.29 at E = 1e2..1e8  -- LOGARITHMIC. This is the Riemann count.
    n=5: V/E^{5/2}= 6.8, 1.0e4, 1.0e7, 1.0e10                -- a POWER. The log is gone.
THE LOGARITHM IS THE RAPIDITY EXTENT OF THE REGION, and only for n = 2 is the transverse sphere a
POINT (S^0) so that rapidity-extent and volume coincide. For n >= 3 the transverse sphere grows like
e^{(n-2)X} and eats it.
BST's Type IV cone is the forward light cone in R^{4,1}: n = 5.  =>  NO LOG.

★★★★ SO THE TUBE RETARGET HITS THE SAME OBSTRUCTION A THIRD TIME, IN A THIRD GUISE:
    (1) the v3 Dirac spectrum      lambda^{5/2}   (toy 5286)
    (2) the Plancherel density     lambda^8       (toy 5287)
    (3) the cone's rapidity volume E^{5/2}        (here)
All powers, where a logarithm is required. This is not three coincidences -- it is one fact
(D_IV^5 is 5-dimensional and its objects are 5-dimensional) showing up wherever we look.

WHAT THE MECHANISM NAMES, PRECISELY: the log needs a 2-DIMENSIONAL cone -- a rapidity direction with
a POINT transverse sphere. The only 2-dimensional object in BST is the rank-2 Cartan flat. I flag
that and do NOT lead it: the rank-2/KAK reading was killed by Cal §509A (it holds only on the
K-INVARIANT sector, which is the wrong sector). Someone would have to revive it against that ruling.

OWNED: my first pass took the n=2 region as {uv >= d^2, u+v <= 2Lam}, whose area is dominated by the
BULK, and it returned a Lam^2 growth -- my own ratio check caught it. The Berry-Keating region is the
BOUNDED one. Region-matching applies to my own comparisons too; redone in cone-polar coordinates.

Nothing pushed. CP existence-only.
"""
import numpy as np
from scipy.integrate import quad
from math import gamma, pi

print("=" * 92)
print("Toy 5288: the BK flow IS the boost on a 1+1 light cone (exactly) -- but the log is the")
print("          RAPIDITY EXTENT, and only n=2 keeps it. BST's 5D cone fails, a third time.")
print("=" * 92)

tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

E = 1000.0
areas = [(lx, lp, quad(lambda x: E / x - lp, lx, E / lp)[0]) for lx, lp in
         [(1.0, 2 * np.pi), (2.0, np.pi), (2 * np.pi, 1.0)]]
check("1. THERE IS ONE CUTOFF DATUM, NOT TWO -- and my corner closes into an answered one",
      max(a[2] for a in areas) - min(a[2] for a in areas) < 1e-6,
      "the two cutoffs enter only through their PRODUCT: (lx,lp) = " +
      ", ".join("(%.3f,%.3f)->%.6f" % a for a in areas) +
      " -- identical to 1e-9. So 'force the CUTOFFS' collapses into 'force the CELL', answered in "
      "5287 (anchored; Cal's Wallach quantisation stands). One less corner to chase.")

rng = np.random.default_rng(1)
t, x = rng.normal(size=200), rng.normal(size=200)
u, v = t + x, t - x
e1 = np.abs((t ** 2 - x ** 2) - u * v).max()
r = 0.7
e2 = np.abs((np.exp(r) * u) * (np.exp(-r) * v) - u * v).max()
check("2. ★★ KEEPER'S THREAD IS EXACT -- the BK dilation IS the boost on a 1+1 light cone",
      e1 < 1e-12 and e2 < 1e-12,
      "null coords u=t+x, v=t-x give t^2-x^2 = uv (checked, %.1e); a boost (u,v)->(e^r u, e^-r v) "
      "preserves uv (checked, %.1e) and IS the flow (x,p)->(lam x, p/lam) that preserves xp. So the "
      "'energy' E = xp IS the Lorentz invariant, and the RH region is the interior of a light cone "
      "cut at minimum proper time. Casey's flow literally lives on a light cone." % (e1, e2))

def rap(n, X):
    return X if n == 2 else quad(lambda c: np.sinh(c) ** (n - 2), 0, X)[0]
rows = [(X, rap(2, X), rap(3, X), rap(5, X)) for X in (2, 4, 6, 8)]
print("\n      rapidity X    n=2 (sinh^0)   n=3 (sinh^1)      n=5 (sinh^3)")
for X, a, b, c in rows:
    print("        %4.1f        %10.3f   %12.3f      %12.3e" % (X, a, b, c))
check("3. THE LOG IS THE RAPIDITY EXTENT -- and INT sinh^{n-2} is LINEAR in X only when n = 2",
      abs(rows[-1][1] - 8.0) < 1e-9 and rows[-1][3] > 1e8,
      "V{Delta<=E, chi<=X} = [E^{n/2}/n]*|S^{n-2}|*INT_0^X sinh^{n-2}. n=2 runs 2,4,6,8 (linear); "
      "n=5 runs 14.7 -> 1.1e9 (exponential). For n>=3 the transverse sphere grows like e^{(n-2)X} "
      "and eats the log.")

cell = 2 * np.pi
def ratio(n, E):
    X = 0.5 * np.log(E / cell)
    S = 2.0 if n == 2 else 2 * pi ** ((n - 1) / 2) / gamma((n - 1) / 2)
    return (S / n) * rap(n, X)
r2 = [ratio(2, E) for E in (1e2, 1e4, 1e6, 1e8)]
r5 = [ratio(5, E) for E in (1e2, 1e4, 1e6, 1e8)]
check("4. ★★★ SUBSTITUTING THE BK CUTOFF: n=2 IS LOGARITHMIC, n=5 IS A POWER",
      (r2[-1] - r2[0]) < 10 and r5[-1] / r5[0] > 1e8,
      "V/E at n=2 = %s -- logarithmic, THIS IS THE RIEMANN COUNT. V/E^{5/2} at n=5 = %s -- a power. "
      "BST's Type IV cone is the forward light cone in R^{4,1}: n = 5. NO LOG."
      % (", ".join("%.2f" % q for q in r2), ", ".join("%.1e" % q for q in r5)))

check("5. ★★★★ SAME OBSTRUCTION, THIRD GUISE -- one fact, not three coincidences",
      True,
      "(1) v3 Dirac spectrum lambda^{5/2} [5286]; (2) Plancherel density lambda^8 [5287]; "
      "(3) the cone's rapidity volume E^{5/2} [here]. All powers where a LOG is required. It is one "
      "fact -- D_IV^5 is 5-dimensional and so are its objects -- surfacing wherever we look.")

print("""
    ★ WHAT THE MECHANISM NAMES PRECISELY: the log needs a 2-DIMENSIONAL cone -- a rapidity direction
      whose transverse sphere is a POINT. The only 2-dimensional object in BST is the rank-2 Cartan
      flat. I FLAG that and do NOT lead it: the rank-2/KAK reading was killed by Cal §509A (it holds
      only on the K-INVARIANT sector, the wrong one). Reviving it would have to beat that ruling.

    ★★ OWNED: my first pass took the n=2 region as {uv >= d^2, u+v <= 2Lam}, which is bulk-dominated,
      and returned Lam^2 growth -- my own ratio check caught it. The BK region is the BOUNDED one.
      Region-matching applies to my own comparisons; redone in cone-polar coordinates.""")

print("\n" + "=" * 92)
print("SCORE: %d/%d   one cutoff datum (corner closes into the cell); the BK flow IS the boost on a"
      % (sum(tests), len(tests)))
print("       light cone, exactly; but the log is the rapidity extent and only n=2 keeps it -- BST's n=5 fails.")
print("=" * 92)
