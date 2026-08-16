"""
Toy 5307 (Elie, 2026-08-16) -- THE KOIDE RAZOR, run. The pre-registered estimator, on the corpus's
actual object, on every reading the corpus supports. It returns FAIL, and the tau boundary is why.

THE ESTIMATOR (pre-registered in my 5306, BEFORE the map existed, theta-free):
      A^2(v) = 2 [ N * sum(v^2) / (sum v)^2 - 1 ]
Sanity: returns exactly 2.0000000000 on a Koide vector at theta = 0.0, 0.7, 2.1 -- theta-independent,
and the 45 degrees never appears. Cal's guard satisfied by construction.

THE OBJECT, RECONNECTED (not reconstructed):
  * T2529/K1002: the FK reproducing-kernel norm, anchored ||f_0||^2 = Gamma(5/2)^2/Gamma(5) = 3pi/128.
    Verified to 1e-15. The corpus writes the Gamma expression itself, so the functional form reads as
    ||f_0(nu)||^2 = Gamma(nu)^2/Gamma(2 nu).  [SCOPE FLAG: the corpus states the anchor AT nu = 5/2;
    extending that form to other nu is my reading of what is written, and @Lyra should confirm it.]
  * T2517: lepton addresses nu = {5/2 (e), 3/2 (mu), 0 (tau)}.
  * T2513: the quark object (nu)_d at nu = N_c = 3, degrees {1,3,5} -> (3,60,2520) = 1:20:840 ✓.

THE TAU BOUNDARY, which Lyra flagged and which turns out to decide everything:
at nu -> 0, Gamma(nu)^2/Gamma(2nu) ~ (1/nu^2)/(1/(2nu)) = 2/nu  ->  DIVERGES.
Measured: ||f_0(1e-2)||^2 = 2.00e2, ||f_0(1e-4)||^2 = 2.00e4, ||f_0(1e-6)||^2 = 2.00e6.

★★★ THE RAZOR, ON EVERY CORPUS-SUPPORTED READING -- enumerated, not hunted:
      A: sqrt(m) ∝ ||f||^2, tau limit           3.9972 / 4.0000 / 4.0000   (eps = 1e-3/1e-6/1e-9)
      B: sqrt(m) ∝ 1/||f||^2                    2.4042 / 2.4044
      C: quark-style (nu)_d at nu = 3           3.7141
      D: quark-style at nu = 5/2                3.6628
      E: sqrt(m) ∝ ||f|| (not squared)          3.9924
      F: the raw addresses [my 5306]            1.1875
NOT ONE READING RETURNS 2. The closest is B at 2.404 -- 20% off, which is not a match.

★★★★ AND THE TAU BOUNDARY DIVERGENCE IS THE DECIDER -- a structural fact, not a numerical accident:
if any single component diverges, then sum(v) ~ T and sum(v^2) ~ T^2, so
      A^2 -> 2[N T^2/T^2 - 1] = 2(N-1) = 4  at N = 3,
INDEPENDENT OF THE OTHER TWO ENTRIES. So the gate cannot be rescued by adjusting the electron and
muon values: the boundary behaviour alone pins A^2 = 4, and 4 != 2.

=> THE RAZOR RETURNS **FAIL**. Koide A^2 = 2 does NOT fall out of the FK reproducing-kernel norm on
   the radial tower. Per the gate's own pre-registered terms (A^2 = 2 -> DERIVED; A^2 != 2 ->
   falsified), this reading is falsified -- and it is falsified by the boundary, exactly where Lyra
   said the subtlety lived.

WHAT THIS DOES AND DOES NOT KILL: it kills THIS MAP as the Koide source. It does not touch the
equal-norm reformulation (my 5305, which stands as the correct statement of what A^2 = 2 IS), nor
T2517's addresses, nor T2513's quark ladder (verified here, 1:20:840 exact). And I did NOT hunt for a
variant that returns 2 -- I enumerated the readings the corpus supports and reported all nine numbers.

Nothing pushed. CP existence-only.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 30

print("=" * 92)
print("Toy 5307: THE KOIDE RAZOR FAILS on every corpus-supported reading -- and the TAU BOUNDARY")
print("          DIVERGENCE is the decider: any divergent third entry pins A^2 = 2(N-1) = 4.")
print("=" * 92)

tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

def A2(v):
    v = np.asarray([float(x) for x in v]); N = len(v)
    return 2 * (N * (v ** 2).sum() / v.sum() ** 2 - 1)

sane = [A2([1 + np.sqrt(2) * np.cos(t + 2 * np.pi * k / 3) for k in range(3)]) for t in (0.0, 0.7, 2.1)]
check("1. THE ESTIMATOR IS THETA-FREE AND EXACT -- Cal's guard satisfied by construction",
      all(abs(s - 2) < 1e-9 for s in sane),
      "returns %s on an exact Koide vector at theta = 0.0/0.7/2.1. The 45 degrees never appears; only "
      "the two isotypic norms do." % ", ".join("%.10f" % s for s in sane))

anchor = float(mp.gamma(mp.mpf(5) / 2) ** 2 / mp.gamma(5))
q = [float(mp.rf(3, d)) for d in (1, 3, 5)]
check("2. THE OBJECT RECONNECTED -- anchor and quark ladder both verified",
      abs(anchor - float(3 * mp.pi / 128)) < 1e-15 and [round(x / q[0]) for x in q] == [1, 20, 840],
      "||f_0||^2 = Gamma(5/2)^2/Gamma(5) = %.10f = 3pi/128 ✓ ; (3)_1,(3)_3,(3)_5 = %s -> 1:20:840 ✓. "
      "SCOPE FLAG: the corpus states the anchor AT nu = 5/2; reading the form as Gamma(nu)^2/Gamma(2nu) "
      "for other nu is my reading of what is written -- @Lyra should confirm."
      % (anchor, [int(x) for x in q]))

def n2(nu): return float(mp.gamma(nu) ** 2 / mp.gamma(2 * nu))
divs = [(e, n2(e)) for e in (1e-2, 1e-4, 1e-6)]
check("3. THE TAU BOUNDARY DIVERGES -- Gamma(nu)^2/Gamma(2nu) ~ 2/nu",
      all(abs(v * e - 2) < 0.01 for e, v in divs),
      "||f_0||^2 at nu = " + ", ".join("%.0e -> %.3e" % d for d in divs) + " -- exactly 2/nu. The "
      "interior norm degenerates at the Shilov address, as @Lyra flagged.")

n25, n15 = n2(2.5), n2(1.5)
rows = [("A: sqrt(m) ∝ ||f||^2, eps=1e-6", A2([n25, n15, n2(1e-6)])),
        ("B: sqrt(m) ∝ 1/||f||^2, eps=1e-6", A2([1 / n25, 1 / n15, 1 / n2(1e-6)])),
        ("C: quark-style (nu)_d at nu=3", A2(q)),
        ("D: quark-style at nu=5/2", A2([float(mp.rf(2.5, d)) for d in (1, 3, 5)])),
        ("E: sqrt(m) ∝ ||f||, tau->inf", A2([np.sqrt(n25), np.sqrt(n15), np.sqrt(n2(1e-6))])),
        ("F: raw addresses [my 5306]", A2([2.5, 1.5, 0.0]))]
print("\n      reading                                A^2       = 2 ?")
for nm, a in rows:
    print("      %-38s %7.4f    %s" % (nm, a, "YES" if abs(a - 2) < 0.01 else "no"))
check("4. ★★★ NOT ONE READING RETURNS A^2 = 2 -- the razor FAILS",
      all(abs(a - 2) > 0.05 for _, a in rows),
      "closest is B at %.4f -- 20%% off, which is not a match. I enumerated the readings the corpus "
      "supports and report all of them; I did NOT hunt for a variant that returns 2."
      % [a for n, a in rows if n.startswith("B")][0])

Tbig = A2([n25, n15, 1e12])
check("5. ★★★★ AND THE TAU DIVERGENCE IS THE DECIDER -- a structural fact",
      abs(Tbig - 4) < 1e-6,
      "if ANY single component diverges then sum(v) ~ T and sum(v^2) ~ T^2, so A^2 -> 2[N - 1] = 4 at "
      "N = 3, INDEPENDENT of the other two entries (measured %.6f with T = 1e12). The gate cannot be "
      "rescued by adjusting the electron and muon values -- the boundary alone pins A^2 = 4, and "
      "4 != 2." % Tbig)

print("""
    ⟹ PER THE GATE'S OWN PRE-REGISTERED TERMS (A^2 = 2 -> DERIVED; A^2 != 2 -> falsified), THIS
      READING IS FALSIFIED -- and it is falsified AT THE BOUNDARY, exactly where @Lyra said the
      subtlety lived. Her flag was the right one; it just decides against.

    WHAT THIS DOES NOT KILL: the equal-norm reformulation (my 5305) stands as the correct statement
    of what A^2 = 2 IS; T2517's addresses stand; T2513's quark ladder stands (verified here, 1:20:840
    exact). What falls is THIS MAP as the Koide source.""")

print("\n" + "=" * 92)
print("SCORE: %d/%d   razor run: no corpus-supported reading gives A^2 = 2; the tau boundary"
      % (sum(tests), len(tests)))
print("       divergence pins A^2 = 4 regardless of the other entries. Gate falsified on this map.")
print("=" * 92)
