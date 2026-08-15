"""
Toy 5278 (Elie, 2026-08-15) -- K1554: run the knot WITH the color-triplet constraint, read by HEIGHT.
I ran it. The answer is NOT the hoped-for d=4 landing, and the reason is worth more than the landing
would have been: BOTH readings of the constraint fail, in two different and both-diagnosable ways.

READING 1 -- "the 3 spatial dims ARE the color triplet, so use 3 spatial dims" -- IS
CONSTRUCTION-GUARANTEED. Vary the inserted rep dimension k and the height read returns d = k+1
every time (k=2..6 -> h = 17.50 / 9.50 / 6.62 / 5.00 / 4.12, matching the d = 3/4/5/6/7 calibration
exactly). The color triplet contributes the integer 3 and nothing else; the dynamics contributes
nothing. A test that cannot fail proves nothing -- my own 5253 lesson, and Cal's §507 bar.

AND THE 'THEREFORE' HAS UNENUMERATED ALTERNATIVES. "Irreducible => no invariant 1-dim subspace" is
satisfied by SU(3)'s 3, 6, 8, 10, 15, 27, ... -- irreducibility does not single out 3. The 3 comes
from ADDITIONALLY choosing the fundamental, and that choice is the assumption doing the work. (And
3-dim irreps are not unique to color: SO(3) vector, SU(2) adjoint.) Casey's standing rule --
enumerate alternatives before the "therefore" -- applies to this one.

READING 2 -- the background-free one (commitments come in INDIVISIBLE TRIPLES: 3 mutually
incomparable commitments per site) -- IS RUNNABLE, AND IT CONFOUNDS MY OWN METER.
Height counts LEVELS, and levels are set by the number of SITES (N/3), not commitments (N). So at
matched total N = 1500 a GENUINE d=4 world under the confinement constraint reads h = 7.12, against
the unconstrained calibration d=4 -> 9.38 and d=5 -> 6.62. It lands between them and NEARER d=5.
=> reading the constrained knot against the UNCONSTRAINED calibration reports a HIGHER dimension
   than the world has -- the opposite direction from the hoped-for d=4 landing.
And the sting is precise: the constraint leaves r essentially untouched (0.1753 -> 0.1755) and moves
ONLY the height. It hits exactly the meter I recommended this morning and spares the one I said was
useless.

THE FIX (my region-match discipline, applied to the constraint instead of the region): calibrate
WITH the constraint in place. Confined d=4 h = 7.12 +/- 0.35 vs confined d=5 h = 5.12 +/- 0.35 --
4.0 sigma per realisation. THE METER SURVIVES, but only against a constrained calibration.

CONFINEMENT'S SCALE (assignment part 2): yes it delivers the locality bound -- and so does every
other scale below ~10^6 light years, so delivering it is not evidence. The per-tick bound is
step < 6.41e-5 rad, i.e. any length below 6.41e-5 x R. Confinement's ~0.8 fm passes by 1e37; so do
the Planck length, the Bohr radius, and the solar system. ZERO DISCRIMINATING POWER. And per my 5276
correction the binding condition is the ACCUMULATED v*T/R, in which the commit scale does not appear
at all.

WHAT I AM NOT SAYING: this does not touch T2545, and it is not a ruling on whether N_c=3 is
background-free -- that is Lyra + Cal's gate, correctly assigned. It says the two computable
readings of the constraint are, respectively, empty and meter-confounding, and it hands back a
constrained calibration so the next run is honest.

Nothing pushed. CP existence-only.
"""
import numpy as np

print("=" * 92)
print("Toy 5278: the color-triplet reading is construction-guaranteed; the confinement constraint")
print("          CONFOUNDS my own height meter (biases a real d=4 world toward d=5). Plus the fix.")
print("=" * 92)

rng = np.random.default_rng(1554)
tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

def height(R):
    n = R.shape[0]; h = np.ones(n, dtype=int)
    for b in range(n):
        pre = np.nonzero(R[:, b])[0]
        if len(pre): h[b] = 1 + h[pre].max()
    return h.max()

def raw(M, d, a, rng):
    t = rng.uniform(0, a, M); x = rng.uniform(0, 1, (M, d - 1))
    o = np.argsort(t); t, x = t[o], x[o]
    dt = t[None, :] - t[:, None]
    s = np.linalg.norm(x[None, :, :] - x[:, None, :], axis=2)
    return (dt > 0) & (dt > s)

def rh(R):
    n = R.shape[0]
    return R.sum() / (n * (n - 1) / 2), height(R)

def confine(R, c=3):
    """each site becomes an INDIVISIBLE c-tuple: mutually incomparable, sharing all outside relations"""
    return np.kron(R, np.ones((c, c), dtype=bool))

# ---------------------------------------------------------------- reading 1
print("\nREADING 1: 'the 3 spatial dims ARE the color triplet, so use 3 spatial dims'")
print("  If that is the pipeline, varying the inserted rep dimension k must return d = k+1 always.\n")
out = []
for k in [2, 3, 4, 5, 6]:
    v = np.array([rh(raw(1500, k + 1, 1.0, rng)) for _ in range(8)])
    out.append((k, k + 1, v[:, 1].mean()))
    print("      inserted rep dim k=%d  ->  spacetime d=%d  ->  height read %.2f" % (k, k + 1, v[:, 1].mean()))
mono = all(out[i][2] > out[i + 1][2] for i in range(len(out) - 1))
check("1. READING 1 IS CONSTRUCTION-GUARANTEED -- the output tracks the INSERTED integer, exactly",
      mono,
      "the read is a strictly decreasing function of the inserted k with no other input; the colour "
      "structure contributes the integer 3 and nothing else. A test that cannot fail proves nothing.")

irreps = [1, 3, 3, 6, 8, 10, 10, 15, 15, 24, 27]
nontrivial = sorted(set(d for d in irreps if d > 1))
check("2. AND THE 'THEREFORE' HAS UNENUMERATED ALTERNATIVES -- irreducibility does NOT single out 3",
      len(nontrivial) > 1 and 3 in nontrivial,
      "SU(3) irreps of dim %s all satisfy 'no invariant 1-dim subspace'. The 3 comes from ADDITIONALLY "
      "choosing the fundamental -- that choice is the assumption. (3-dim irreps also: SO(3) vector, "
      "SU(2) adjoint.)" % nontrivial)

# ---------------------------------------------------------------- reading 2
print("\nREADING 2 (background-free): commitments come in INDIVISIBLE TRIPLES -- a POSET constraint,")
print("  3 mutually-incomparable commitments per site, sharing all outside relations. Matched N=1500.\n")
N = 1500
base, conf = {}, {}
for d in [4, 5]:
    base[d] = np.array([rh(raw(N, d, 1.0, rng)) for _ in range(10)])
    conf[d] = np.array([rh(confine(raw(N // 3, d, 1.0, rng))) for _ in range(10)])
    print("      d=%d :  unconstrained r=%.4f h=%.2f    |    CONFINED r=%.4f h=%.2f"
          % (d, base[d][:, 0].mean(), base[d][:, 1].mean(), conf[d][:, 0].mean(), conf[d][:, 1].mean()))
c4, u4, u5 = conf[4][:, 1].mean(), base[4][:, 1].mean(), base[5][:, 1].mean()
check("3. THE CONSTRAINT DROPS THE HEIGHT WITHOUT CHANGING THE DIMENSION -- IT CONFOUNDS MY METER",
      u5 < c4 < u4 and (c4 - u5) < (u4 - c4),
      "a GENUINE d=4 world, confined, reads h = %.2f -- between the unconstrained d=5 mark (%.2f) and "
      "d=4 (%.2f), and NEARER d=5. Height counts LEVELS, set by SITES (N/3), not commitments (N). "
      "Reading the constrained knot against an unconstrained calibration reports a HIGHER d than the "
      "world has -- opposite to the hoped-for landing." % (c4, u5, u4))

dr = abs(conf[4][:, 0].mean() - base[4][:, 0].mean())
check("4. AND IT HITS PRECISELY THE METER I RECOMMENDED -- r is untouched, only h moves",
      dr < 0.01 and (u4 - c4) > 1.0,
      "d=4: r %.4f -> %.4f (moves %.4f, negligible) while h %.2f -> %.2f (moves %.2f). The constraint "
      "spares the invariant I called useless and biases the one I called the fix."
      % (base[4][:, 0].mean(), conf[4][:, 0].mean(), dr, u4, c4, u4 - c4))

sep = (conf[4][:, 1].mean() - conf[5][:, 1].mean()) / np.hypot(conf[4][:, 1].std(ddof=1), conf[5][:, 1].std(ddof=1))
print("\n  THE FIX -- region-match applied to the CONSTRAINT: calibrate with it in place.")
print("      CONFINED d=4 : h = %.2f +/- %.2f      CONFINED d=5 : h = %.2f +/- %.2f"
      % (conf[4][:, 1].mean(), conf[4][:, 1].std(ddof=1), conf[5][:, 1].mean(), conf[5][:, 1].std(ddof=1)))
print("      separation = %.2f = %.1f sigma per realisation -- THE METER SURVIVES, against a"
      % (conf[4][:, 1].mean() - conf[5][:, 1].mean(), sep))
print("      CONSTRAINED calibration only. Use these numbers, not this morning's.")

# ---------------------------------------------------------------- the scale
print("\nASSIGNMENT PART 2: IS CONFINEMENT'S SCALE THE LOCALITY SCALE DELIVERING < 1e-4 ?")
need = 1e-2 / 156.0
R = 1.30e26                      # S^4 radius, taken as the Hubble radius (an INPUT, not derived)
scales = [("hadron radius ~0.8 fm", 0.8e-15), ("Planck length", 1.616e-35),
          ("Bohr radius", 5.29e-11), ("Earth radius", 6.37e6), ("1 astronomical unit", 1.496e11)]
print("      requirement: step < sigma/f_max = %.3e rad, i.e. any length below %.3e m (~%.0e ly)"
      % (need, need * R, need * R / 9.461e15))
for nm, L in scales:
    print("        %-24s  step = %.2e rad   %s by %.1e" % (nm, L / R, "PASSES", need / (L / R)))
check("5. CONFINEMENT'S SCALE PASSES -- AND SO DOES EVERY SCALE BELOW ~1e6 LIGHT YEARS",
      all(L / R < need for _, L in scales),
      "the bound has ZERO discriminating power, so passing it is not evidence that confinement is the "
      "mechanism. And per my 5276 correction the BINDING condition is the accumulated v*T/R, in which "
      "the commit scale does not appear at all.")

print("""
    ★ SCOPE. This does not touch T2545, and it is NOT a ruling on whether N_c=3 is background-free --
      that gate is Lyra + Cal's, correctly assigned. It says the two computable readings of the
      constraint are, respectively, EMPTY (reading 1) and METER-CONFOUNDING (reading 2), and it hands
      back a constrained calibration so the next run is honest.""")

print("\n" + "=" * 92)
print("SCORE: %d/%d   reading 1 cannot fail; irreducibility does not single out 3; reading 2 biases"
      % (sum(tests), len(tests)))
print("       a real d=4 world toward d=5; r is spared and h is hit; confinement's scale has no power.")
print("=" * 92)
