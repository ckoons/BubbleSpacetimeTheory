"""
Toy 5284 (Elie, 2026-08-15, evening) -- K1567 BAR-3: is BST's event structure sprinkling-like
(Poisson, Lorentz-invariant) or deterministic-regular (a clock, frame-dependent)?

THE ANSWER IS A CONDITION, NOT A VERDICT -- and the condition is sharp and checkable against the
corpus's own definition of the Koons tick.

THE CORPUS DOES NOT HAND ME A POINT PROCESS. It hands me a MEASURE (uniform on S^4, forced by the
Casimir -- my 5256/5272), a TICK, and a CAP (N_max, F865). So I did not sprinkle and measure, which
would be construction-guaranteed (Keeper flagged this correctly). I tested the readings the corpus's
own features imply.

★★★ RESULT 1 -- A GLOBAL TICK IS LORENTZ-VIOLATING WITH PERFECT CONTRAST.
Test: S(v) = |<exp(2*pi*i*Dt'(v)/tick)>| over event pairs. A layered process has S = 1 in its rest
frame and collapses under boost -- the peak IS the preferred frame. A Poisson sprinkling has S ~ 0 at
every boost (Bombelli-Henson-Sorkin: Poisson is the unique Lorentz-invariant discrete distribution).
    v        0.00     0.02     0.05     0.10     0.30     0.60     0.90
    Poisson  0.0019   0.0013   0.0020   0.0004   0.0020   0.0007   0.0007
    GLOBAL   1.0000   0.0016   0.0008   0.0021   0.0025   0.0038   0.0020
    fixed-N  0.0009   0.0009   0.0023   0.0023   0.0008   0.0029   0.0012
S = 1.0000 exactly at v = 0 for the global tick, noise floor everywhere else. THE PREFERRED FRAME IS
DETECTED, with no ambiguity at all.

★★ RESULT 2 -- THE CAP IS NOT THE PROBLEM; THE TICK IS. A fixed total count (the N_max cap) reads
like Poisson at every boost -- it is still uniform-continuous, so it costs no Lorentz invariance.

★★★★ RESULT 3 -- AND IT GETS *WORSE* AT LARGE SCALES, NOT BETTER. The width of the S(v) peak scales
as tick/X: measured 9.6e-3, 5.2e-3, 1.7e-3, 5.0e-4 as the region grows 50 -> 100 -> 300 -> 1000.
A bigger region locates the preferred frame MORE sharply. The violation does not wash out in the
continuum limit -- it becomes easier to see. That is the BHS point, quantified.

★★★★★ RESULT 4 -- THE ESCAPE ROUTE, AND IT IS THE PHYSICALLY NATURAL ONE. If each observer commits
every tick of ITS OWN PROPER TIME (a local clock, not a global layering), there is no global layer to
pick out a frame: S <= 0.008 at every boost, no peak. PER-WORLDLINE PROPER-TIME TICKING IS
LORENTZ-COVARIANT.

=> BAR-3's verdict: the fuzzy-continuum reframe SURVIVES the Lorentz requirement IF AND ONLY IF the
Koons tick is a PROPER-TIME tick along each worldline, NOT a global commitment layer. That is a
concrete, checkable requirement on the corpus's own definition -- and it is the reading that matches
"the commitment tick IS time" read LOCALLY. Someone should check which the corpus means before Part
III leans on it.

TWO INSTRUMENT FAILURES I CAUGHT AND OWN:
 (i) my first statistic (Fano factor on cell counts) had an EDGE-EFFECT bug -- after boosting, the
     region is a sheared parallelogram and my cells fell partly outside it, so empty cells inflated
     the variance and even POISSON read Fano 3.85 at v = 0.9. Fixed by accepting a cell only if all
     four corners inverse-boost back inside the source region.
 (ii) and once fixed, the Fano factor turned out to have NO POWER at all: with many events per layer
     and uniform x, a cell's count is binomial either way and BOTH processes read ~1. The regularity
     lives in the SUPPORT, not in the counts. I replaced it with the S(v) lattice statistic, which
     has perfect contrast.

SCOPE: this is 1+1 for clarity; the BHS obstruction is dimension-independent, and nothing here
depends on the spatial dimension. Nothing here touches T2564, T2565 or Parts 1 and 2.

Nothing pushed. CP existence-only.
"""
import numpy as np

print("=" * 92)
print("Toy 5284: BAR-3. A GLOBAL tick is Lorentz-violating with perfect contrast and WORSE at large")
print("          scales; a PER-WORLDLINE PROPER-TIME tick is covariant. The cap is fine; the tick isn't.")
print("=" * 92)

rng = np.random.default_rng(1567)
tick = 1.0
tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

def S(t, x, v, npairs=200000):
    g = 1 / np.sqrt(1 - v * v)
    i = rng.integers(0, t.size, npairs); j = rng.integers(0, t.size, npairs)
    dtp = g * ((t[j] - t[i]) - v * (x[j] - x[i]))
    return abs(np.mean(np.exp(2j * np.pi * dtp / tick)))

print("\n  The corpus hands me a MEASURE (uniform on S^4, Casimir-forced), a TICK, and a CAP -- not a")
print("  point process. So I test the readings those features imply, rather than sprinkling and")
print("  measuring, which would be construction-guaranteed.\n")
print("  S(v) = |<exp(2*pi*i*Dt'(v)/tick)>|. A layered process peaks at its rest frame; Poisson never")
print("  peaks (Bombelli-Henson-Sorkin: Poisson is the unique Lorentz-invariant discrete law).\n")

T, X, n = 300.0, 300.0, 40000
tp_, xp_ = rng.uniform(0, T, n), rng.uniform(0, X, n)                      # Poisson-like
layers = np.arange(0, T, tick)
tr, xr = rng.choice(layers, n), rng.uniform(0, X, n)                        # GLOBAL tick
tf, xf = rng.uniform(0, T, n), rng.uniform(0, X, n)                         # fixed N
print("      v        Poisson      GLOBAL tick      fixed-N")
rows = []
for v in [0.0, 0.02, 0.05, 0.10, 0.30, 0.60, 0.90]:
    a, b, c = S(tp_, xp_, v), S(tr, xr, v), S(tf, xf, v)
    rows.append((v, a, b, c))
    print("   %5.2f       %.4f        %.4f          %.4f" % (v, a, b, c))
check("1. ★ A GLOBAL TICK IS LORENTZ-VIOLATING, WITH PERFECT CONTRAST",
      rows[0][2] > 0.99 and max(r[2] for r in rows[1:]) < 0.05,
      "S = %.4f exactly at v = 0 and noise floor (<%.4f) at every other boost. The preferred frame is "
      "DETECTED with no ambiguity." % (rows[0][2], max(r[2] for r in rows[1:])))
check("2. THE POISSON SPRINKLING HAS NO PREFERRED FRAME -- the control behaves",
      max(r[1] for r in rows) < 0.05,
      "S <= %.4f at every boost. No frame is special, as BHS requires." % max(r[1] for r in rows))
check("3. ★★ THE N_max CAP IS NOT THE PROBLEM -- THE TICK IS",
      max(r[3] for r in rows) < 0.05,
      "a fixed total count reads like Poisson at every boost (S <= %.4f) -- it is still "
      "uniform-continuous, so the cap costs no Lorentz invariance." % max(r[3] for r in rows))

print("\n  How sharply is the preferred frame located, as the region grows?\n")
widths = []
for XX in [50, 100, 300, 1000]:
    lay = np.arange(0, XX, tick)
    t2, x2 = rng.choice(lay, 40000), rng.uniform(0, XX, 40000)
    w = next((v for v in np.logspace(-5, -1, 60) if S(t2, x2, v, 60000) < 0.5), np.nan)
    widths.append(w)
    print("      region X = %5d  ->  S drops below 0.5 by v = %.2e   (tick/X = %.2e)" % (XX, w, tick / XX))
check("4. ★★★ AND IT GETS *WORSE* AT LARGE SCALES -- the violation does not wash out",
      widths[0] > widths[-1] * 5,
      "the peak width scales as tick/X: %s. A BIGGER region locates the preferred frame MORE sharply, "
      "so the discreteness does not hide in the continuum limit -- it becomes easier to see."
      % " -> ".join("%.1e" % w for w in widths))

print("\n  THE ESCAPE ROUTE: each observer commits every tick of ITS OWN proper time (a local clock).\n")
ts, xs = [], []
for _ in range(400):
    v0 = np.tanh(rng.normal(0, 0.8)); g = 1 / np.sqrt(1 - v0 * v0)
    tau = np.arange(int(T / (g * tick))) * tick
    ts.append(g * tau); xs.append(rng.uniform(0, X) + v0 * g * tau)
t, x = np.concatenate(ts), np.concatenate(xs)
pw = [S(t, x, v) for v in [0.0, 0.02, 0.10, 0.30, 0.60]]
for v, s in zip([0.0, 0.02, 0.10, 0.30, 0.60], pw):
    print("      v = %5.2f   S = %.4f" % (v, s))
check("5. ★★★★ A PER-WORLDLINE PROPER-TIME TICK IS LORENTZ-COVARIANT -- no preferred frame",
      max(pw) < 0.05,
      "S <= %.4f at every boost, no peak. Each observer has its own clock and no global layer exists "
      "to pick out a frame." % max(pw))

print("""
    ⟹ BAR-3's VERDICT (a condition, not a verdict on BST): the fuzzy-continuum reframe SURVIVES the
      Lorentz requirement IF AND ONLY IF the Koons tick is a PROPER-TIME tick along each worldline,
      NOT a global commitment layer. That is concrete and checkable against the corpus's own
      definition -- and it is the reading that matches "the commitment tick IS time" read LOCALLY.
      @Lyra @Cal: check which the corpus means before Part III leans on it. Parts 1 and 2 don't care.

    TWO INSTRUMENT FAILURES I CAUGHT AND OWN: (i) my first statistic (Fano on cell counts) had an
    EDGE-EFFECT bug -- boosted cells fell partly outside the sheared region, so empty cells inflated
    the variance and even POISSON read Fano 3.85 at v = 0.9; fixed by interior-corner acceptance.
    (ii) once fixed, the Fano factor had NO POWER at all -- with many events per layer both processes
    read ~1, because the regularity lives in the SUPPORT, not the counts. Replaced with S(v).

    SCOPE: 1+1 for clarity; the BHS obstruction is dimension-independent. Nothing here touches T2564,
    T2565, or Parts 1 and 2.""")

print("\n" + "=" * 92)
print("SCORE: %d/%d   a global tick gives S = 1.0000 at one frame and noise elsewhere (violation, and"
      % (sum(tests), len(tests)))
print("       sharper at large scales); the cap is fine; a per-worldline proper-time tick is covariant.")
print("=" * 92)
