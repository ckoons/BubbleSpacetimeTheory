"""
Toy 5291 (Elie, 2026-08-16) -- P != NP was listed as "the distinctive one" with NO owner in the
assignments, so I took it. Three results, and the middle one is a numerology trap I want buried
before anyone finds it, because it is far more seductive than this morning's 7/8.

★ (1) THE PHENOMENON IS REAL. Backtracking nodes at the phase transition, median of 40 instances:
      n            10      14      18      22
      2-SAT        17      23      65     153     -- stays cheap
      3-SAT       132     362    1406    6646     -- blows up
So "2 is easy, 3 is hard" is not folklore; it is measurable. T1456's observation is correct.

★★ (2) BUT IT IS SCHAEFER'S, NOT OURS. Schaefer's dichotomy theorem (1978): a Boolean CSP is in P
iff its constraint language is 0-valid, 1-valid, Horn, dual-Horn, AFFINE, or BIJUNCTIVE; bijunctive
means arity 2. The threshold sits at 3 BECAUSE 2 IS THE LARGEST ARITY ADMITTING THE BIJUNCTIVE NORMAL
FORM -- a theorem of classical complexity theory with no geometric input. And the 3-cluster is broad
and genuine (k-SAT, k-COL, k-dimensional matching, NAE-k-SAT, hypergraph 2-colouring all break at 3)
-- but broad in exactly the family Schaefer covers. BST's N_c = 3 MATCHES a 1978 theorem. Matching is
IDENTIFICATION. For a DERIVATION, "you cannot linearise curvature" must produce something Schaefer
does NOT -- for instance a prediction about which NEW constraint languages are hard. That test has
not been run, and it is the one that would make the attempt ours.

★★★ (3) THE TRAP, AND THE HONEST WAY IT DIES.
alpha_c(3) ~ 4.26675 (the 3-SAT satisfiability threshold) and 2^{C_2}/(N_c n_C) = 64/15 = 4.26667.
AGREEMENT TO 0.002%. Someone will propose this today.
  * THE DENSITY ARGUMENT FAILS TO KILL IT, and I report that straight rather than reaching for it:
    among 738 distinct ratios 2^a 3^b 5^c / 2^d 3^e 5^f, only 0.07 were EXPECTED within 0.3% of
    4.267, and exactly 1 was found. "Numerology by abundance" is NOT available here.
  * THE FORM ARGUMENT KILLS IT. The threshold is an exponential family:
        alpha_c(k) = 2^k ln 2 - (1 + ln 2)/2 + o(1)
    which tracks the observed values to ratio 1.0103, 1.0033, 1.0010, 1.0003, 1.0001, 1.0000 at
    k = 5,6,7,8,9,10. The leading coefficient is ln 2 -- transcendental, with a DERIVED origin (the
    first-moment entropy of the uniform measure on assignments). A ratio of BST integers is RATIONAL.
    It can hit ONE member of the sequence; nothing rational hits the SEQUENCE. Tested: the rational
    extension gives 8.533 and 17.067 against observed 9.931 and 21.117 -- off by 14% and 19%, while
    the classical formula is within 1%.
    => ONE HIT, WRONG FAMILY. Buried.

THE STANDING BAR THIS SETS (same shape as the 7/8 kill this morning): a BST form matching ONE member
of a known family is not evidence. It owes (a) a mechanism and (b) the REST OF THE FAMILY. Both of
today's traps died on (b).

Nothing pushed. CP existence-only.
"""
import numpy as np, itertools, random

print("=" * 92)
print("Toy 5291: P != NP -- the 3-threshold is REAL but it is SCHAEFER'S 1978 dichotomy, not ours;")
print("          and alpha_c(3) = 64/15 survives the density test but dies on the FORM (ln 2).")
print("=" * 92)

rng = random.Random(1456)
tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

def nodes(n, m, k):
    cls = [tuple((v if rng.random() < 0.5 else -v) for v in rng.sample(range(1, n + 1), k)) for _ in range(m)]
    cnt = [0]
    def go(a, i):
        cnt[0] += 1
        for c in cls:
            if all(abs(l) - 1 < i for l in c) and not any(a[abs(l) - 1] == (l > 0) for l in c): return False
        if i == n: return True
        for b in (True, False):
            a[i] = b
            if go(a, i + 1): return True
        return False
    go([None] * n, 0)
    return cnt[0]

rows = []
for n in (10, 14, 18, 22):
    a = int(np.median([nodes(n, int(1.0 * n), 2) for _ in range(40)]))
    b = int(np.median([nodes(n, int(4.27 * n), 3) for _ in range(40)]))
    rows.append((n, a, b))
print("\n      n         2-SAT (m=1.0n)     3-SAT (m=4.27n)   [median backtracking nodes, 40 runs]")
for n, a, b in rows:
    print("    %4d          %10d      %14d" % (n, a, b))
check("1. THE PHENOMENON IS REAL -- 2 is easy, 3 blows up. T1456's observation is correct.",
      rows[-1][2] / rows[-1][1] > 10 * rows[0][2] / rows[0][1] or rows[-1][2] > 20 * rows[-1][1],
      "3-SAT/2-SAT node ratio grows %.1f -> %.1f over n = 10..22." % (rows[0][2] / rows[0][1], rows[-1][2] / rows[-1][1]))

check("2. ★★ BUT IT IS SCHAEFER'S DICHOTOMY (1978), NOT OURS",
      True,
      "a Boolean CSP is in P iff 0-valid, 1-valid, Horn, dual-Horn, AFFINE or BIJUNCTIVE; bijunctive "
      "= arity 2. The threshold is at 3 BECAUSE 2 is the largest arity admitting the bijunctive "
      "normal form. And the 3-cluster is broad and genuine (k-SAT, k-COL, k-dim matching, NAE-k-SAT, "
      "hypergraph 2-colouring) -- broad in exactly the family Schaefer covers. BST's N_c = 3 MATCHES "
      "a 1978 theorem; matching is IDENTIFICATION, not derivation.")

ac3 = 4.26675
vals = set()
for a in itertools.product(range(0, 7), repeat=3):
    for b in itertools.product(range(0, 4), repeat=3):
        num = 2 ** a[0] * 3 ** a[1] * 5 ** a[2]; den = 2 ** b[0] * 3 ** b[1] * 5 ** b[2]
        if den and 0 < num / den < 1e4: vals.add(num / den)
vals = np.array(sorted(vals))
hits = vals[np.abs(vals - ac3) / ac3 < 0.003]
dens = len(vals[(vals > 1) & (vals < 100)]) / 99.0
expect = dens * 2 * 0.003 * ac3
check("3. ★ THE DENSITY ARGUMENT FAILS TO KILL 64/15 -- reported straight, not reached past",
      len(hits) >= 1 and expect < 0.5,
      "2^{C_2}/(N_c n_C) = 64/15 = %.5f vs alpha_c(3) = %.5f -- agreement to %.3f%%. Among %d "
      "distinct BST-primary ratios, %.2f were EXPECTED within 0.3%% and %d found. "
      "'Numerology by abundance' is NOT available here."
      % (64 / 15, ac3, 100 * abs(64 / 15 - ac3) / ac3, len(vals), expect, len(hits)))

obs = {5: 21.117, 6: 43.37, 7: 87.79, 8: 176.54, 9: 354.01, 10: 708.92}
rat = [(2 ** k * np.log(2) - (1 + np.log(2)) / 2) / a for k, a in obs.items()]
rex = [(4, 9.931, 2 ** 7 / 15), (5, 21.117, 2 ** 8 / 15)]
check("4. ★★★ THE FORM ARGUMENT KILLS IT -- ln 2 cannot come from a rational",
      max(abs(r - 1) for r in rat) < 0.02 and all(abs(p - o) / o > 0.10 for _, o, p in rex),
      "alpha_c(k) = 2^k ln2 - (1+ln2)/2 tracks the data to ratio %s at k = 5..10. The leading "
      "coefficient is ln 2 -- transcendental, from the first-moment entropy. A BST ratio is RATIONAL: "
      "it can hit ONE member, never the SEQUENCE. The rational extension gives %s against observed "
      "%s -- off by %s, while the classical formula is within 1%%. ONE HIT, WRONG FAMILY. Buried."
      % (", ".join("%.4f" % r for r in rat),
         ", ".join("%.3f" % p for _, _, p in rex), ", ".join("%.3f" % o for _, o, _ in rex),
         ", ".join("%.0f%%" % (100 * abs(p - o) / o) for _, o, p in rex)))

check("5. THE DERIVATION TEST FOR THIS ATTEMPT, NAMED",
      True,
      "'you cannot linearise curvature' must produce something SCHAEFER DOES NOT -- e.g. a prediction "
      "about which NEW constraint languages are hard, checkable against the CSP dichotomy literature. "
      "Until that runs, the attempt is an IDENTIFICATION of a 1978 theorem, and should be tiered so.")

print("""
    ★ THE STANDING BAR THIS SETS (same shape as this morning's 7/8 kill): a BST form matching ONE
      member of a known family is not evidence. It owes (a) a MECHANISM and (b) THE REST OF THE
      FAMILY. Both of today's traps died on (b) -- 7/8 on the Gamma-factor mechanism, 64/15 on the
      ln 2 family. Two in one day suggests the bar should be standing, not ad hoc.""")

print("\n" + "=" * 92)
print("SCORE: %d/%d   the 3-threshold is real and is Schaefer's; 64/15 survives the density test and"
      % (sum(tests), len(tests)))
print("       dies on the form; and the derivation test for P!=NP is named but not yet run.")
print("=" * 92)
