"""
Toy 5276 (Elie, 2026-08-15) -- K1551's two assignments, both answered, both NEGATIVE-but-sharp.

ASSIGNMENT (b): "does T2564's causal-order adjacency actually deliver the <1e-4 rad per-tick step?"
ANSWER: NO -- and the reason is a theorem-grade fact about Lorentzian causal sets, not a numerical
shortfall. K1551's bridge was "one tick apart in the order => timelike-separated by <= light-cone x
Koons-tick => a tiny spatial step." The first implication holds (Dtheta < Dt by definition of the
order). The second FAILS: **links in a Lorentzian causal set are NEAR-NULL, and boost invariance
spreads them over the whole light cone.** Measured on T2564's own object (R x S^4, a<b iff Dt >
Dtheta): <Dtheta/Dt> = 0.80 -- the light-cone bound is SATURATED, not undercut. And under a 16x
density refinement in a FIXED region the link PROPER TIME shrinks (0.291 -> 0.185, ratio 0.636 vs
16^(-1/5) = 0.574) while the link SPATIAL SEPARATION is FLAT (0.499 -> 0.505, ratio 1.012).
Refining the order does not shorten the steps. NEAREST-IN-ORDER IS NOT NEAREST-IN-SPACE.
On S^4 the mean link step is 0.34 rad against a requirement of 6.4e-5 -- short by 5.3e3.

AND THE ORDER CANNOT SUPPLY THE NUMBER IN PRINCIPLE: the order is CONFORMAL, hence scale-free.
Verified exactly -- rescaling (t,x) -> (lam t, lam x) leaves the order matrix IDENTICAL while the
steps change by 10^6. So the order fixes only the ratio Dtheta/Dt <= 1, never an absolute radian
step. The magnitude has to come from a scale ratio (l_B / R), i.e. from ANCHORS.

The only way to get a small per-tick step is to restrict to a TIMELIKE WORLDLINE with v << c --
which ASSUMES the velocity, the very input the exercise was to supply. That is the circularity.

ASSIGNMENT (a): I read the primary sources and MY 5275 GUESS IS WRONG -- retracted. The corpus says
the 1/n_C chirality projection acts on the R^5 VECTOR (spatial) index, not the spinor/record index
(Cal referee log 2026-07-15 line 8351; Grace Master Ledger v0.17). Two further findings:
  * arrow 2, SO(4,2) -> SO(3,1), is NOT a dimensional step -- SO(4,2) is the CONFORMAL group of
    R^{3,1}, so it is already (3,1); the arrow drops dilatation + special conformal (15 = 4+6+1+4
    -> 6), an isometry restriction inside the SAME 4D. There is ONE dimensional step in the chain
    and it is the chirality projection. The board's "Task 3 = a second 4->3 leg via momentum" is
    not what the corpus chain does.
  * ★ a PROJECTION does not reduce the dimension. Projecting S^4 along an axis gives the SOLID
    4-BALL: 38.7% of the image lies strictly inside |y| < 0.9, which would be exactly 0 for S^3.
    Only RESTRICTION to the equator gives S^3 -- and restriction is precisely the "commit measure
    lies on S^3" claim ALREADY KILLED BY THEOREM (Elie 5256 / K1504: H_B is the Casimir of K, so
    exp(-tau H_B) commutes with SO(5) and the induced measure is the unique invariant round one).

SCOPE / WHAT THIS DOES NOT SAY: this does not touch T2564 itself (the derived order stands), and it
is not a claim that no process supplies the correlation -- only that THIS one does not. The ceiling
Cal stated is untouched: the matter input remains an input.

Nothing pushed. CP existence-only.
"""
import numpy as np

print("="*92)
print("Toy 5276: T2564's derived order does NOT deliver the step -- links are near-null,")
print("          their spatial separation is FLAT under refinement, and a PROJECTION")
print("          does not reduce dimension. K1551 (a) and (b), both answered.")
print("="*92)

rng = np.random.default_rng(1551)
tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

def links(R):
    # covering relations; float64 matmul -- int8 overflows the path count at N > ~500
    return R & ~((R.astype(np.float64) @ R.astype(np.float64)) > 0.5)

# ---------------------------------------------------------------- (b) the order
print("\n(b) DOES T2564's CAUSAL-ORDER ADJACENCY DELIVER THE <1e-4 rad PER-TICK STEP?")
print("    T2564's object (F989-confirmed): conformal Lorentzian order on the Shilov boundary,")
print("    S^1 unwrapped -> R x S^4, with a < b iff Dt > Dtheta (geodesic distance on unit S^4).\n")

def sprinkle(N, T):
    t = rng.uniform(0, T, N)
    x = rng.normal(size=(N, 5)); x /= np.linalg.norm(x, axis=1)[:, None]
    return t, x

def order(t, x):
    dt = t[None, :] - t[:, None]
    dth = np.arccos(np.clip(x @ x.T, -1, 1))
    return (dt > 0) & (dt > dth), dth

t, x = sprinkle(1400, 0.60)
R, dth = order(t, x); L = links(R); i, j = np.nonzero(L)
ratio = (dth[i, j] / (t[j] - t[i])).mean()
check("1. LINKS ARE NEAR-NULL -- the light-cone bound is SATURATED, not undercut",
      0.7 < ratio < 1.0,
      "n_links = %d   <Dtheta/Dt> = %.4f (1.0 = exactly null)   <Dtheta> = %.4f rad"
      % (L.sum(), ratio, dth[i, j].mean()))

steps = []
for N in [400, 800, 1600, 3200, 6400]:
    t, x = sprinkle(N, 0.60); R, dth = order(t, x); L = links(R); i, j = np.nonzero(L)
    steps.append(dth[i, j].mean())
check("2. THE LINK STEP IS FLAT UNDER A 16x DENSITY REFINEMENT (region-matched: fixed slab)",
      abs(steps[-1] / steps[0] - 1.0) < 0.15,
      "N = 400..6400 -> step = " + " ".join("%.4f" % s for s in steps) +
      " rad   ratio %.3f  (refining the order does NOT shorten the steps)" % (steps[-1] / steps[0]))

NEED = 1e-2 / 156.0
check("3. AND IT MISSES THE REQUIREMENT BY ~5e3 ON THE UNIT S^4",
      steps[-1] / NEED > 1e3,
      "mean link step %.4f rad  vs  required sigma/f_max = %.3e rad  ->  short by %.1e"
      % (steps[-1], NEED, steps[-1] / NEED))

# region-matched flat control: separate proper time from spatial separation
rngc = np.random.default_rng(7); pt = []; sp = []
for N in [500, 1000, 2000, 4000, 8000]:
    tt = rngc.uniform(0, 1, N); xx = rngc.uniform(0, 1, (N, 4))
    dt = tt[None, :] - tt[:, None]
    d = np.linalg.norm(xx[None, :, :] - xx[:, None, :], axis=2)
    Rf = (dt > 0) & (dt > d); Lf = links(Rf); a, b = np.nonzero(Lf)
    pt.append(np.sqrt((tt[b] - tt[a])**2 - d[a, b]**2).mean()); sp.append(d[a, b].mean())
check("4. CONTROL (flat R^{1,4}): PROPER TIME shrinks with density, SPATIAL SEPARATION does NOT",
      pt[-1] / pt[0] < 0.75 and abs(sp[-1] / sp[0] - 1) < 0.10,
      "proper time %.4f -> %.4f (ratio %.3f, 16^(-1/5) = %.3f) | spatial %.4f -> %.4f (ratio %.3f, FLAT)"
      % (pt[0], pt[-1], pt[-1] / pt[0], 16**-0.2, sp[0], sp[-1], sp[-1] / sp[0]))

# the order is conformal -> scale-free -> cannot fix an absolute step
n = 300; tt = rng.uniform(0, 1, n); xx = rng.uniform(-1, 1, (n, 4))
def ordflat(tt, xx):
    dt = tt[None, :] - tt[:, None]
    d = np.linalg.norm(xx[None, :, :] - xx[:, None, :], axis=2)
    return (dt > 0) & (dt > d)
O1 = ordflat(tt, xx); same = True; sc = []
for lam in [1e-3, 1.0, 1e3]:
    O = ordflat(lam * tt, lam * xx); same &= np.array_equal(O, O1)
    sc.append(np.linalg.norm(xx[None, :, :] - xx[:, None, :], axis=2)[np.nonzero(links(O))].mean() * lam)
check("5. THE ORDER IS CONFORMAL => SCALE-FREE => IT CANNOT FIX AN ABSOLUTE STEP, IN PRINCIPLE",
      same and sc[-1] / sc[0] > 1e5,
      "identical order matrix at lam = 1e-3, 1, 1e3; mean link step = %.3e / %.3e / %.3e (10^6 spread)"
      % tuple(sc))

# ---------------------------------------------------------------- (a) the chirality projection
print("\n(a) THE CHIRALITY PROJECTION -- WHICH INDEX, AND DOES A PROJECTION REDUCE DIMENSION?")
print("    Primary sources read: Cal referee log 2026-07-15 line 8351 ('the descent SO(5,2)->SO(4,2)")
print("    is SO(5)->SO(4) on the compact side, which fixes exactly ONE R^5 direction -- the n_C-axis")
print("    (removed by the 1/n_C chirality projection) ... the descent's S^3 is the EQUATOR orthogonal")
print("    to that axis'); Grace Master Ledger v0.17 ('acts on the n_C = 5 SPACELIKE sector').")
print("    => IT ACTS ON THE R^5 VECTOR INDEX, NOT THE SPINOR/RECORD INDEX. My 5275 guess: RETRACTED.\n")

dim_so = lambda n: n * (n - 1) // 2
check("6. ARROW 2 IS NOT A DIMENSIONAL STEP -- SO(4,2) IS ALREADY THE CONFORMAL GROUP OF R^{3,1}",
      dim_so(7) == 21 and dim_so(6) == 15 and dim_so(4) == 6 and 4 + 6 + 1 + 4 == 15,
      "SO(5,2) 21 = conf(R^{4,1}) | SO(4,2) 15 = conf(R^{3,1}) = 4 transl + 6 Lorentz + 1 dil + 4 SCT "
      "| SO(3,1) 6 = isometries of the SAME 4D. ONE dimensional step, and it is the chirality projection.")

M = 400000
z = rng.normal(size=(M, 5)); z /= np.linalg.norm(z, axis=1)[:, None]
r = np.linalg.norm(z[:, :4], axis=1)
frac = [(r < c).mean() for c in (0.9, 0.7, 0.5)]
def cdim(P, rs):
    D = np.linalg.norm(P[None, :, :] - P[:, None, :], axis=2)
    d = D[np.triu_indices(len(P), 1)]
    C = np.array([(d < q).mean() for q in rs]); ok = C > 0
    return np.polyfit(np.log(rs[ok]), np.log(C[ok]), 1)[0]
N = 3000; rs = np.exp(np.linspace(np.log(0.06), np.log(0.30), 12))
xs = rng.normal(size=(N, 5)); xs /= np.linalg.norm(xs, axis=1)[:, None]
ball = rng.normal(size=(N, 4)); ball /= np.linalg.norm(ball, axis=1)[:, None]
ball *= rng.uniform(0, 1, (N, 1))**0.25
s3 = rng.normal(size=(N, 4)); s3 /= np.linalg.norm(s3, axis=1)[:, None]
d_proj, d_ball, d_s3 = cdim(xs[:, :4], rs), cdim(ball, rs), cdim(s3, rs)
check("7. A PROJECTION DOES NOT REDUCE THE DIMENSION -- S^4 PROJECTS ONTO THE SOLID 4-BALL",
      frac[0] > 0.3 and abs(d_proj - d_ball) < 0.3 and d_proj - d_s3 > 0.5,
      "AC(0) count: %.4f / %.4f / %.4f of the image lies inside |y| < 0.9 / 0.7 / 0.5 -- all would be "
      "EXACTLY 0 for S^3. Region-matched estimator: projection %.3f vs 4-ball control %.3f vs S^3 %.3f."
      % (frac[0], frac[1], frac[2], d_proj, d_ball, d_s3))

print("""
    ★★ Only RESTRICTION to the equator gives S^3 -- and restriction is exactly the claim ALREADY
       KILLED BY THEOREM: 'the commit measure lies on / peaks on S^3' is Elie 5256 / K1504. H_B is
       the Casimir of K = SO(5)xSO(2), so exp(-tau H_B) commutes with SO(5), the induced measure on
       S^4 is the unique invariant (round) one, and it cannot concentrate on any S^3 -- for every
       tau and every spectrum.
    ★  And the axis itself: the projection needs a v in R^5, which 5257 says no SO(5)-equivariant
       construction supplies. The one corpus-supplied candidate is the commit site Omega_0 (T2542) --
       but then S^3 = {x . Omega_0 = 0} is the locus at pi/2 = 1.5708 rad from the observer, not a
       neighbourhood of it. QUESTION for Lyra/Cal, not a verdict: if space IS that equator, the
       observer is not in their own space.""")

print("\n" + "=" * 92)
print("SCORE: %d/%d   (b) the derived order does NOT supply the step -- links are near-null, spatial"
      % (sum(tests), len(tests)))
print("       separation is flat under refinement, and the order is scale-free in principle;")
print("       (a) the chirality projection acts on the VECTOR index (my guess retracted), arrow 2 is")
print("       not a dimensional step, and a projection does not reduce the dimension.")
print("=" * 92)
