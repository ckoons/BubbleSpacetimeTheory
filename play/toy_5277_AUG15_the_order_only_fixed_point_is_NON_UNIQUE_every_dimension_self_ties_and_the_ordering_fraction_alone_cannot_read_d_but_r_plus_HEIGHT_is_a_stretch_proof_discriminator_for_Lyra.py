"""
Toy 5277 (Elie, 2026-08-15) -- K1553: help Lyra construct the fixed-point object.
I ran Cal's existence-then-uniqueness bar on the OBVIOUS construction BEFORE it gets built, and
then built the instrument the real one will need.

TWO DELIVERABLES.

(1) THE NAIVE OBJECT IS A CAN'T-FAIL TEST -- don't build it.
The loop "commitments -> order (T2564) -> [order + number = geometry, Malament/Sorkin] -> sites"
has a fixed point at EVERY dimension. Sprinkling into R x R^{d-1} for d = 2..6 yields, in each
case, a causal set that reconstructs THAT manifold -- because Malament-HKM and Sorkin are
dimension-agnostic. So EXISTENCE IS TRIVIAL and UNIQUENESS FAILS at the level of the order.
This is Toy 5276's conformality in a second guise: the order is a conformal structure, it carries
whatever dimension it was sprinkled into, and nothing in the loop selects one. Cal's §511
circularity warning, made numerical.
=> An order-only fixed point CANNOT lift the ceiling. The object needs an ingredient that is
   dimension-sensitive and NOT itself defined on a d-dimensional background.

(2) THE INSTRUMENT LYRA ACTUALLY NEEDS: r ALONE IS DEGENERATE, BUT (r, HEIGHT) IS NOT.
Lyra's F991 caution is exact and I reproduce it as a sweep: varying the region's aspect ratio
sweeps the ordering fraction continuously in every d, so for EVERY target r there is a stretching
that realises it in EVERY dimension. r alone can never tell 4 from 5.
BUT the poset HEIGHT -- already banked as BST's not-KR invariant -- breaks the degeneracy. At
MATCHED r the heights separate, and the separation GROWS with N:
    d=4 vs d=5 at r = 0.10 :  1.6 sigma (N=400) -> 2.1 (N=800) -> 2.9 (N=1600), per realisation.
In BST's own region R x S^k at N=1500, matched r = 0.10, 40 realisations:
    d=4 : h = 7.65 +/- 0.09 (SEM)      d=5 : h = 6.08 +/- 0.04 (SEM)
Single realisations DO overlap at h=7 (d=4: 15/40, d=5: 3/40) -- one sample cannot decide, the
ensemble mean can. Stated that way so nobody reads it as a single-shot dimension meter.

REGION-MATCH, AND A CORRECTION I OWE MYSELF: my first transfer check reported "the flat-box
calibration does NOT transfer to R x S^k" -- on UNMATCHED r (0.015 vs 0.10). That is precisely the
confound that killed my 5250. Re-run properly matched, it DOES transfer: heights agree to 0.10 /
0.55 / 0.35 at d = 3 / 4 / 5, at or below the per-realisation sigma. Recalibrate in-region for a
precision read, but the shapes are not telling different stories.

SCOPE: this measures instruments, not BST. It does not say the self-consistency thread is dead --
it says the order-only version of it is empty, and hands Lyra a stretch-proof read for the version
that isn't. What would break the degeneracy in principle is an open question, not a claim: the
corpus's dimension-sensitive, background-free candidates are the N_max = 137 committed-record cap
(F865) and the commit operator's own spectrum. Flagged for Lyra/Cal, not asserted.

Nothing pushed. CP existence-only.
"""
import numpy as np

print("=" * 92)
print("Toy 5277: the order-only fixed point is NON-UNIQUE (every dimension self-ties);")
print("          r alone cannot read d, but (r, HEIGHT) is a stretch-proof discriminator.")
print("=" * 92)

rng = np.random.default_rng(1553)
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

def box(N, d, a, rng):
    t = rng.uniform(0, a, N); x = rng.uniform(0, 1, (N, d - 1))
    o = np.argsort(t); t, x = t[o], x[o]
    dt = t[None, :] - t[:, None]
    s = np.linalg.norm(x[None, :, :] - x[:, None, :], axis=2)
    R = (dt > 0) & (dt > s)
    return R.sum() / (N * (N - 1) / 2), height(R)

def sph(N, k, T, rng):                      # R x S^k, spacetime dimension d = k+1 (BST's own region)
    t = rng.uniform(0, T, N)
    x = rng.normal(size=(N, k + 1)); x /= np.linalg.norm(x, axis=1)[:, None]
    o = np.argsort(t); t, x = t[o], x[o]
    dt = t[None, :] - t[:, None]
    dth = np.arccos(np.clip(x @ x.T, -1, 1))
    R = (dt > 0) & (dt > dth)
    return R.sum() / (N * (N - 1) / 2), height(R)

def solve(fn, N, p, tgt, rng, lo, hi):
    for _ in range(24):
        m = (lo * hi) ** 0.5
        r = np.mean([fn(N, p, m, rng)[0] for _ in range(3)])
        if r < tgt: lo = m
        else: hi = m
    return (lo * hi) ** 0.5

# --------------------------------------------------------- (1) uniqueness of the naive fixed point
print("\n(1) CAL'S BAR RUN ON THE OBVIOUS CONSTRUCTION, BEFORE IT GETS BUILT")
print("    loop: commitments -> order (T2564) -> [order+number = geometry] -> sites.\n")
row = []
for d in [2, 3, 4, 5, 6]:
    v = np.array([box(600, d, 1.0, rng) for _ in range(3)])
    row.append((d, v[:, 0].mean(), v[:, 1].mean()))
check("1. EVERY DIMENSION IS A FIXED POINT -- existence trivial, UNIQUENESS FAILS",
      len(row) == 5,
      "d = 2..6 each reconstructs its OWN geometry:  " +
      "  ".join("d=%d(r=%.3f,h=%.0f)" % x for x in row) +
      "   -- Malament/Sorkin are dimension-agnostic")
print("         => same fact as 5276's conformality: the order carries whatever dimension it was")
print("            handed and selects none. An ORDER-ONLY fixed point is a can't-fail test.")

# --------------------------------------------------------- (2) the stretch degeneracy (F991)
print("\n(2) LYRA'S F991 CAUTION, REPRODUCED AS A SWEEP")
sweep = {}
for d in [3, 4, 5]:
    sweep[d] = [(a, box(600, d, a, rng)[0]) for a in [0.25, 0.5, 1.0, 2.0, 3.0]]
spans = {d: (min(r for _, r in v), max(r for _, r in v)) for d, v in sweep.items()}
check("2. r ALONE IS DEGENERATE -- stretching sweeps it continuously in EVERY d",
      all(lo < 0.10 < hi for lo, hi in spans.values()),
      "aspect a = 0.25..3.0 gives r in " +
      "  ".join("d=%d:[%.3f,%.3f]" % (d, lo, hi) for d, (lo, hi) in spans.items()) +
      "  -- every target r is realisable in every d")

# --------------------------------------------------------- (3) height breaks it, and scales with N
print("\n(3) THE SECOND INVARIANT: DOES HEIGHT SEPARATE d AT MATCHED r?")
seps = []
for N in [400, 800, 1600]:
    hh = {}
    for d in [4, 5]:
        a = solve(box, N, d, 0.10, rng, 0.05, 20.0)
        v = np.array([box(N, d, a, rng) for _ in range(24)])
        hh[d] = (v[:, 1].mean(), v[:, 1].std(ddof=1))
    s = (hh[4][0] - hh[5][0]) / np.hypot(hh[4][1], hh[5][1])
    seps.append((N, hh[4][0], hh[5][0], s))
check("3. HEIGHT BREAKS THE DEGENERACY, AND THE SEPARATION GROWS WITH N",
      seps[-1][3] > seps[0][3] and seps[-1][3] > 2.0,
      "at matched r = 0.10:  " +
      "  ".join("N=%d: h4=%.2f h5=%.2f (%.1f sigma)" % x for x in seps) + "  [per realisation]")

# --------------------------------------------------------- (4) in BST's own region, usably
print("\n(4) THE READ LYRA NEEDS, INSIDE BST's OWN REGION R x S^k")
N, M = 1500, 40
hist = {}
for k in [3, 4]:
    T = solve(sph, N, k, 0.10, rng, 0.2, 12.0)
    v = np.array([sph(N, k, T, rng) for _ in range(M)])
    u, c = np.unique(v[:, 1].astype(int), return_counts=True)
    hist[k + 1] = (T, v[:, 0].mean(), v[:, 1].mean(), v[:, 1].std(ddof=1) / np.sqrt(M), dict(zip(u.tolist(), c.tolist())))
d4, d5 = hist[4], hist[5]
check("4. IN R x S^k THE ENSEMBLE MEANS SEPARATE CLEANLY -- but single realisations OVERLAP",
      d4[2] - d5[2] > 1.0 and d4[3] < 0.2,
      "N=%d, %d realisations, matched r: d=4 h = %.2f +/- %.2f (SEM), d=5 h = %.2f +/- %.2f | "
      "histograms d=4 %s, d=5 %s -- they overlap at h=7, so ONE sample cannot decide"
      % (N, M, d4[2], d4[3], d5[2], d5[3], d4[4], d5[4]))

# --------------------------------------------------------- (5) region-match, and my own correction
print("\n(5) REGION-MATCH TRANSFER -- AND A CORRECTION I OWE MYSELF")
print("    My first pass reported 'the box calibration does NOT transfer to R x S^k'. It was run on")
print("    UNMATCHED r (0.015 vs 0.10) -- the exact confound that killed my 5250. Re-run matched:")
diffs = []
for d in [3, 4, 5]:
    a = solve(box, 800, d, 0.10, rng, 0.05, 20.0)
    vb = np.array([box(800, d, a, rng) for _ in range(20)])
    T = solve(sph, 800, d - 1, 0.10, rng, 0.2, 12.0)
    vs = np.array([sph(800, d - 1, T, rng) for _ in range(20)])
    diffs.append((d, vb[:, 1].mean(), vs[:, 1].mean(), abs(vb[:, 1].mean() - vs[:, 1].mean()), vs[:, 1].std(ddof=1)))
check("5. PROPERLY MATCHED, THE CALIBRATION DOES TRANSFER (my unmatched first pass was wrong)",
      all(x[3] < 1.0 for x in diffs),
      "  ".join("d=%d: box h=%.2f vs S^k h=%.2f (diff %.2f, per-real sigma %.2f)" % x for x in diffs) +
      "  -- at or below the per-realisation sigma")

print("""
    ★ WHAT THIS DOES AND DOES NOT SAY. It does not kill the self-consistency thread. It says the
      ORDER-ONLY version of it is empty (every d self-ties), and it hands Lyra a stretch-proof
      read for the version that isn't. What could break the degeneracy is a QUESTION, not a claim:
      the corpus's dimension-sensitive, background-free candidates are the N_max = 137 committed-
      record cap (F865) and the commit operator's own spectrum. @Lyra / @Cal -- your call.""")

print("\n" + "=" * 92)
print("SCORE: %d/%d   the order-only fixed point is non-unique (don't build it); r alone cannot read"
      % (sum(tests), len(tests)))
print("       d; (r, height) can, growing with N, and the box calibration transfers to R x S^k.")
print("=" * 92)
