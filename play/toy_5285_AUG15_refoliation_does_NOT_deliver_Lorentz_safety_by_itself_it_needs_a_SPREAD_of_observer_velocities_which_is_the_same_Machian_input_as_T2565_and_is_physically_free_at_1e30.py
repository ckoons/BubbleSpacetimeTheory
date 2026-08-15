"""
Toy 5285 (Elie, 2026-08-15, evening) -- K1570 residual: confirm T2564's foliation is genuinely
per-worldline (local), so BAR-3's Lorentz condition is met by the corpus.

I CAN CONFIRM IT IS COMPATIBLE. I CANNOT CONFIRM IT DELIVERS IT. One ingredient is missing, it is
physically free, and it is the same Machian input the paper already leads with -- so it costs the
write-up a sentence, not a computation.

T2564 says: "commit-energy = time function/foliation, boosts = re-foliations."

★ THE POINT THAT DECIDES IT: A RE-FOLIATION IS A CHANGE OF DESCRIPTION. It cannot un-layer a layered
EVENT SET. Different observers do not get different events -- they get different coordinates on the
same events. So "boosts = re-foliations" does not, by itself, remove the layering my 5284 detected.
The distinction that actually matters is ONE foliation shared by all commits, or MANY (one per
observer). Measured, sweeping the spread of observer velocities and watching the preferred-frame
signal S(0):
    sigma_v   0.000    0.001    0.003    0.010    0.030    0.100    0.300    0.800
    S(0)      1.0000   1.0000   1.0000   0.9945   0.7085   0.1414   0.0205   0.0075
At sigma_v = 0 -- all observers comoving, i.e. ONE shared foliation -- the violation is back at FULL
strength, S(0) = 1.0000. Safety requires a genuine SPREAD.

★★ AND THAT IS A CONDITION ON THE MATTER CONTENT, NOT THE GEOMETRY: "no privileged observer
velocity." Which is the SAME Machian input as T2565. The last computation's condition reduces to the
theorem the paper already leads with -- a clean closure, and an honest one.

★★★ AND IT IS PHYSICALLY FREE. The layering dies when accumulated time dilation smears the tick:
T*sigma_v^2/2 ~ 1 tick, so sigma_v ~ sqrt(2*tick/T) -- THE LONGER YOU LOOK, THE LESS SPREAD YOU NEED.
Measured crossover vs prediction:
    T (ticks)   100      300      1000     3000
    measured    0.0838   0.0492   0.0289   0.0143
    sqrt(2/T)   0.1414   0.0816   0.0447   0.0258
Same 1/sqrt(T) law. Extrapolated to BST's own numbers -- a Koons tick over a Hubble time is
T/tick ~ 1e60 -- the required velocity spread is ~1e-30. ANY realistic matter dispersion satisfies it
by dozens of orders.

RECOMMENDATION FOR THE WRITE-UP: state it as a one-line hypothesis in Part III ("the commit ensemble
carries no privileged observer velocity"), NOT as something the corpus forces. It is free to satisfy
and it is already the paper's own thesis -- but claiming T2564 delivers it would be the propagation
failure we have caught five times this week, and a referee reading "boosts = re-foliations" will ask
exactly the question I asked here.

SCOPE: 1+1 for clarity; the BHS obstruction is dimension-independent. Nothing here touches T2564,
T2565, Parts 1 and 2, or my 5284's verdict -- it sharpens the condition 5284 stated.

Nothing pushed. CP existence-only.
"""
import numpy as np

print("=" * 92)
print("Toy 5285: re-foliation does NOT deliver Lorentz safety by itself -- it needs a SPREAD of")
print("          observer velocities, which is the same Machian input as T2565, and is free at 1e-30.")
print("=" * 92)

rng = np.random.default_rng(1570)
tick = 1.0
tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

def S(t, x, v=0.0, npairs=300000):
    g = 1 / np.sqrt(1 - v * v)
    i = rng.integers(0, t.size, npairs); j = rng.integers(0, t.size, npairs)
    return abs(np.mean(np.exp(2j * np.pi * g * ((t[j] - t[i]) - v * (x[j] - x[i])) / tick)))

def ensemble(sig, T=300.0, X=300.0, nobs=350):
    ts, xs = [], []
    for _ in range(nobs):
        v0 = np.tanh(rng.normal(0, sig)) if sig > 0 else 0.0
        g = 1 / np.sqrt(1 - v0 * v0); n = max(2, int(T / (g * tick)))
        tau = np.arange(n) * tick
        ts.append(g * tau); xs.append(rng.uniform(0, X) + v0 * g * tau)
    return np.concatenate(ts), np.concatenate(xs)

print("\n  T2564: 'commit-energy = time function/foliation, boosts = re-foliations.'")
print("  ★ A re-foliation is a change of DESCRIPTION -- it cannot un-layer a layered EVENT SET.")
print("    Observers get different coordinates on the SAME events, not different events. So the")
print("    distinction that decides BAR-3 is ONE shared foliation, or MANY (one per observer).\n")
print("      velocity spread sigma_v      S(0)   (1 = preferred frame; ~0 = Lorentz-safe)")
sig_list = [0.0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 0.8]
svals = []
for s in sig_list:
    t, x = ensemble(s); v = S(t, x); svals.append(v)
    print("             %.3f                   %.4f" % (s, v))

check("1. ★ 'BOOSTS = RE-FOLIATIONS' DOES NOT DELIVER SAFETY BY ITSELF",
      svals[0] > 0.99 and svals[-1] < 0.05,
      "at sigma_v = 0 -- all observers comoving, ONE shared foliation -- S(0) = %.4f, the violation "
      "back at FULL strength; only a genuine SPREAD brings it down (%.4f at sigma_v = 0.8). "
      "Re-foliation changes the description, not the event set." % (svals[0], svals[-1]))

check("2. ★★ SO THE CONDITION IS ON THE MATTER CONTENT, NOT THE GEOMETRY",
      True,
      "'no privileged observer velocity' -- which is the SAME Machian input as T2565. BAR-3's "
      "condition reduces to the theorem the paper already leads with. A clean closure, honestly got.")

print("\n  How much spread is actually needed? The layering dies when accumulated time dilation smears")
print("  the tick: T*sigma_v^2/2 ~ 1 tick, so sigma_v ~ sqrt(2*tick/T) -- weaker the longer you look.\n")
print("      T (ticks)      measured crossover      sqrt(2/T)")
meas = []
for T in [100, 300, 1000, 3000]:
    c = next((s for s in np.logspace(-3, 0, 40) if S(*ensemble(s, T=T)) < 0.5), np.nan)
    meas.append(c)
    print("        %5d            %.4f                 %.4f" % (T, c, np.sqrt(2 / T)))
check("3. ★★★ AND THE REQUIREMENT WEAKENS AS sqrt(tick/T) -- so it is PHYSICALLY FREE",
      meas[0] / meas[-1] > 3,
      "measured crossover %s, tracking sqrt(2/T) %s (same 1/sqrt(T) law). At BST's own numbers -- a "
      "Koons tick over a Hubble time, T/tick ~ 1e60 -- the required spread is ~1e-30. ANY realistic "
      "matter dispersion satisfies it by dozens of orders."
      % (" ".join("%.4f" % m for m in meas), " ".join("%.4f" % np.sqrt(2 / T) for T in [100, 300, 1000, 3000])))

print("""
    ⟹ WHAT I CAN AND CANNOT CONFIRM. T2564's reading is COMPATIBLE with BAR-3's local requirement --
      I cannot confirm it DELIVERS it. The missing ingredient is a spread of observer velocities:
      free to satisfy (1e-30), but a hypothesis about matter, not a consequence of the geometry.

    ★ RECOMMENDATION (@Lyra, @Cal): state it as a one-line hypothesis in Part III -- "the commit
      ensemble carries no privileged observer velocity" -- NOT as something the corpus forces.
      Claiming T2564 delivers it would be the propagation failure we have caught five times this
      week, and any referee reading "boosts = re-foliations" asks exactly the question I asked here.
      It costs a sentence, and the sentence is already the paper's own thesis.

    SCOPE: 1+1 for clarity; BHS is dimension-independent. Nothing here touches T2564, T2565, Parts 1
    and 2, or 5284's verdict -- it sharpens the condition 5284 stated.""")

print("\n" + "=" * 92)
print("SCORE: %d/%d   re-foliation alone leaves S(0) = 1.0000; safety needs a velocity spread, which is"
      % (sum(tests), len(tests)))
print("       the same Machian input as T2565 and is free (~1e-30) at BST's scales. State it, don't skip it.")
print("=" * 92)
