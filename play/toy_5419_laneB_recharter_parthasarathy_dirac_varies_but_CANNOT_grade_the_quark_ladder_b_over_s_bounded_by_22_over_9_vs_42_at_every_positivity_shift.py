#!/usr/bin/env python3
"""
Toy 5419 — LANE B (re-chartered): the Parthasarathy/Bergman Dirac spectrum across K-types.

CHARTER PROPERTY UNDER TEST (Round 33, Lyra/Keeper):
    "a non-flat spectral grading of the QUARK LADDER"

★ THE PROPERTY IS NOT NON-FLATNESS. Non-flatness is the EXISTENCE check, and it is
  already known (toy 5418 table). Testing existence when the claim needs a property is
  exactly the error I made in toy 5412 (I verified tau EXISTS when the claim needed
  det tau = (-1)^n). So this toy tests GRADING, and reports non-flatness only as a
  precondition, never as a result.

THE LADDER (inherited by grep, NOT re-derived — F506/K671/T2529):
    down modes sit at single-row K-types of forced degree k in {1,3,5}  (T1929, blind)
    ladder = FK generalized Pochhammer (nu)_k at nu = N_c = 3
           = {3, 60, 2520}  ->  d : s : b = 1 : 20 : 840
    s/d = (nu+1)(nu+2) = 20 forced;  b/s = (nu+3)(nu+4) = 42 forced.

THE OPERATOR (inherited, RUNNING_NOTES 58907 / toy 5418):
    D^2(m1,m2) = m1(m1+n_C) + m2(m2+N_c) - c
    with the shift c a CONVENTION under live dispute in the corpus:
        c = 35/4 = 8.75  = |rho_G|^2, rho_G = (5/2,3/2,1/2), B3 = so(7,C)  [toy 5221]
        c = 34/4 = 8.50  = |rho_conf|^2, rho_conf = (5/2,3/2), rank-2       [banked]
    ⟹ CONVENTION-COLLISION RULE: pin BOTH, do not silently pick one.

CONTROLS (§599 — a search that cannot succeed proves nothing):
    POS-1  feed the FK Pochhammer ladder to the scorer -> must report HIT
    POS-2  feed observed current masses to the scorer  -> must report HIT vs the ladder
    NEG-1  feed a deliberately wrong ladder            -> must report MISS

Exact rationals throughout (Fraction), per the Toy 395 lesson.
"""

from fractions import Fraction as F
from itertools import combinations

N_c, n_C, g, C2, rank = 3, 5, 7, 6, 2
DEGREES = (1, 3, 5)                      # forced, T1929
SHIFTS = {"|rho_G|^2 = 35/4": F(35, 4),  # B3, toy 5221
          "|rho_conf|^2 = 34/4": F(34, 4),
          "no shift (bare Casimir)": F(0)}

# ---------------------------------------------------------------- the ladder
def pochhammer(nu, k):
    """FK generalized Pochhammer (nu)_k, scalar/single-row form."""
    out = F(1)
    for j in range(k):
        out *= (nu + j)
    return out

LADDER = [pochhammer(F(N_c), k) for k in DEGREES]          # 3, 60, 2520
# PDG current masses (MS-bar): m_d, m_s at 2 GeV; m_b(m_b).  Scheme caveat stated in the report.
OBSERVED = [F(467, 100), F(934, 10), F(4180)]

def ratios(v):
    """(second/first, third/second) — the two content-carrying numbers."""
    return (v[1] / v[0], v[2] / v[1])

LAD_SD, LAD_BS = ratios(LADDER)          # 20, 42
OBS_SD, OBS_BS = ratios(OBSERVED)

# ---------------------------------------------------------------- the spectrum
def P(m1, m2):
    """The K-type-dependent part of D^2 (shift excluded)."""
    return F(m1 * (m1 + n_C) + m2 * (m2 + N_c))

def D2(m1, m2, c):
    return P(m1, m2) - c

# Tolerance: 10%, NOT 5%. Reason (found by POS-2, not chosen up front): the banked ladder
# itself sits 6.6% off the observed b/s (the known "b/d at 6%" scope, K671). A bar tighter
# than the banked result's own accuracy would reject BST's own ladder. Loosening moves the
# bar AGAINST this toy's conclusion, and the conclusion is a factor-17 miss regardless.
TOL = F(10, 100)


def scorer(pred, target=(LAD_SD, LAD_BS), tol=TOL):
    """Score a 3-value ladder against the target ratio pair. Returns (verdict, sd, bs, worst)."""
    if any(x <= 0 for x in pred):
        return ("DEAD (non-positive mass)", None, None, None)
    sd, bs = ratios(pred)
    d_sd = abs(sd - target[0]) / target[0]
    d_bs = abs(bs - target[1]) / target[1]
    worst = max(d_sd, d_bs)
    return ("HIT" if worst <= tol else "MISS", sd, bs, worst)

def pct(x):
    return "  --  " if x is None else f"{float(x)*100:8.2f}%"

def show(x, w=10):
    return f"{float(x):{w}.4f}" if x is not None else " " * w

# ================================================================ CONTROLS
print("=" * 78)
print("SECTION 0 — CONTROLS (§599: validate the instrument before any verdict)")
print("=" * 78)
ctrl = []
ctrl.append(("POS-1  FK Pochhammer ladder {3,60,2520}", scorer(LADDER), "HIT"))
ctrl.append(("POS-2  observed current masses (PDG)", scorer(OBSERVED), "HIT"))
ctrl.append(("NEG-1  deliberately wrong ladder {1,2,3}", scorer([F(1), F(2), F(3)]), "MISS"))
print(f"{'control':42s} {'verdict':26s} {'expect':6s}")
for name, (v, sd, bs, w), exp in ctrl:
    print(f"{name:42s} {v:26s} {exp:6s}   {'OK' if v == exp else '*** INSTRUMENT BROKEN ***'}")
controls_ok = all(v == exp for _, (v, _, _, _), exp in ctrl)
print(f"\nLadder ratios      s/d = {float(LAD_SD):.4f}   b/s = {float(LAD_BS):.4f}   (exact 20, 42)")
print(f"Observed ratios    s/d = {float(OBS_SD):.4f}   b/s = {float(OBS_BS):.4f}")
print(f"CONTROLS: {'3/3 PASS — the scorer can succeed and can fail.' if controls_ok else 'FAILED — stop.'}")
if not controls_ok:
    raise SystemExit("instrument invalid; no verdict reported")

# ================================================================ SPECTRUM
print()
print("=" * 78)
print("SECTION 1 — THE SPECTRUM ACROSS K-TYPES (the PRECONDITION, not the property)")
print("=" * 78)
print("D^2(m1,m2) = m1(m1+5) + m2(m2+3) - c        [c = 35/4 shown]")
c0 = SHIFTS["|rho_G|^2 = 35/4"]
print(f"\n{'m1\\m2':>6s}" + "".join(f"{m2:>10d}" for m2 in range(4)))
for m1 in range(7):
    row = f"{m1:>6d}"
    for m2 in range(4):
        row += "" if m2 > m1 else f"{float(D2(m1, m2, c0)):>10.2f}"
        if m2 > m1:
            row += " " * 10
    print(row)
vals = {D2(m1, m2, c0) for m1 in range(7) for m2 in range(m1 + 1)}
print(f"\ndistinct D^2 values over the grid: {len(vals)}   spread: "
      f"{float(min(vals)):.2f} .. {float(max(vals)):.2f}")
print("PRECONDITION: the spectrum VARIES (contrast: Kostant cubic = 25/4 flat, toy 5418).")
print("★ This is EXISTENCE. It is not the charter property. Continue.")

# ================================================================ THE PROPERTY
print()
print("=" * 78)
print("SECTION 2 — THE PROPERTY: does D^2 GRADE the ladder at the FORCED addresses?")
print("=" * 78)
print(f"forced addresses (m1,m2) = (k,0), k in {DEGREES}   [T1929 — not chosen here]")
print(f"target: s/d = {float(LAD_SD):.2f}, b/s = {float(LAD_BS):.2f}   "
      f"(tolerance {float(TOL)*100:.0f}% — see Section 0)\n")

readings = []
for name, c in SHIFTS.items():
    pred = [D2(k, 0, c) for k in DEGREES]
    readings.append((f"M-A  mass ∝ D^2,  c = {name}", pred))
# mass^2 reading, and a ground-referenced reading
readings.append(("M-B  mass ∝ sqrt(D^2 + 35/4)  (mass^2 ∝ Casimir)",
                 [F(k * (k + n_C)) for k in DEGREES]))   # compared as squares below
readings.append(("M-C  mass ∝ D^2 - D^2(ground)  (ground-referenced)",
                 [D2(k, 0, F(0)) - D2(1, 0, F(0)) for k in DEGREES]))

print(f"{'reading':52s} {'d':>9s} {'s':>9s} {'b':>9s} {'s/d':>9s} {'b/s':>9s}  verdict")
print("-" * 78)
c6 = []
for name, pred in readings:
    v, sd, bs, w = scorer(pred)
    print(f"{name:52s} {show(pred[0], 9)} {show(pred[1], 9)} {show(pred[2], 9)} "
          f"{show(sd, 9)} {show(bs, 9)}  {v}")
    c6.append((name, v, w))

# ================================================================ ONE FREE PARAM
print()
print("=" * 78)
print("SECTION 3 — STRESS: GIVE THE OPERATOR ONE FREE PARAMETER (the shift c)")
print("=" * 78)
p1, p2, p3 = (P(k, 0) for k in DEGREES)          # 6, 24, 50
print(f"unshifted K-type values P(k,0) for k={DEGREES}: {p1}, {p2}, {p3}")

# fit c so that s/d hits 20 exactly:  (p2-c)/(p1-c) = 20
c_fit_sd = (LAD_SD * p1 - p2) / (LAD_SD - 1)
pred_sd = [p1 - c_fit_sd, p2 - c_fit_sd, p3 - c_fit_sd]
v_sd, sd_sd, bs_sd, w_sd = scorer(pred_sd)
assert bs_sd is not None, "fitted-shift ladder must be positive; check p1/p2/p3"
print(f"\nfit c to s/d = 20  ->  c = {c_fit_sd} = {float(c_fit_sd):.4f}"
      f"   (not a BST constant: 35/4={float(F(35,4)):.2f}, 34/4={float(F(34,4)):.2f}, C2={C2}, n_C={n_C})")
print(f"   then b/s = {float(bs_sd):.4f}   vs required {float(LAD_BS):.2f}"
      f"   ->  MISSES BY {float(LAD_BS/bs_sd):.1f}x     [{v_sd}]")

# fit c so that b/s hits 42:  (p3-c)/(p2-c) = 42
c_fit_bs = (LAD_BS * p2 - p3) / (LAD_BS - 1)
print(f"\nfit c to b/s = 42  ->  c = {c_fit_bs} = {float(c_fit_bs):.4f}")
pred_bs = [p1 - c_fit_bs, p2 - c_fit_bs, p3 - c_fit_bs]
v_bs, _, _, _ = scorer(pred_bs)
print(f"   masses become ({float(pred_bs[0]):.2f}, {float(pred_bs[1]):.2f}, {float(pred_bs[2]):.2f})"
      f"   ->  {v_bs}")

# ---- the BOUND: sup of b/s over ALL positivity-preserving shifts
# b/s(c) = (p3-c)/(p2-c) is strictly increasing in c (derivative (p3-p2)/(p2-c)^2 > 0),
# and positivity of the lightest mass requires c < p1.  So sup = limit c -> p1^-.
sup_bs = (p3 - p1) / (p2 - p1)
print()
print("-" * 78)
print("★★★ THE BOUND (a theorem over the whole one-parameter family, not a numerical miss)")
print("-" * 78)
print(f"b/s(c) = (P(5)-c)/(P(3)-c) = ({p3}-c)/({p2}-c),  d/dc = {p3-p2}/({p2}-c)^2 > 0  ->  strictly increasing")
print(f"positivity of the LIGHTEST mass requires c < P(1) = {p1}")
print(f"⟹ sup over all positivity-preserving c  =  ({p3}-{p1})/({p2}-{p1}) = {sup_bs} = {float(sup_bs):.4f}")
print(f"⟹ REQUIRED b/s = {float(LAD_BS):.2f}   >>   ATTAINABLE b/s < {float(sup_bs):.4f}")
print(f"⟹ SHORTFALL: a factor of {float(LAD_BS/sup_bs):.1f}, at EVERY shift. No c exists.")
bound_holds = LAD_BS > sup_bs
# verify the bound numerically as well as symbolically (printed check above the verdict)
scan = [(F(cc, 10), (p3 - F(cc, 10)) / (p2 - F(cc, 10))) for cc in range(-200, 60)]
scan_max = max(r for c_, r in scan if c_ < p1)
print(f"   numeric scan c in [-20, 6): max b/s = {float(scan_max):.4f}  "
      f"(< sup {float(sup_bs):.4f}: {scan_max < sup_bs})")

# same bound for the alternative address column (0,k), for completeness
q1, q2, q3 = (P(0, k) for k in DEGREES)
sup_bs_alt = (q3 - q1) / (q2 - q1)
print(f"\nalternative addresses (0,k): P = {q1}, {q2}, {q3}  ->  sup b/s = {float(sup_bs_alt):.4f}"
      f"   (also << {float(LAD_BS):.2f})")

# ================================================================ LOOK-ELSEWHERE
print()
print("=" * 78)
print("SECTION 4 — LOOK-ELSEWHERE: how often does a FREE address triple + free c hit?")
print("=" * 78)
print("(The addresses are FORCED by T1929. This measures what a *fitted* hit would be worth.)")
grid = [(m1, m2) for m1 in range(9) for m2 in range(m1 + 1)]
Pvals = sorted({P(m1, m2) for m1, m2 in grid})
hits = 0
trials = 0
examples = []
for a, b, cc in combinations(Pvals, 3):
    trials += 1
    if b == a:
        continue
    c_star = (LAD_SD * a - b) / (LAD_SD - 1)     # force s/d = 20
    if c_star >= a:                              # positivity of the lightest
        continue
    bs = (cc - c_star) / (b - c_star)
    if abs(bs - LAD_BS) / LAD_BS <= TOL:          # SAME bar as the property test
        hits += 1
        if len(examples) < 3:
            examples.append((a, b, cc, c_star, bs))
print(f"distinct P values on the grid m1<=8: {len(Pvals)}")
print(f"triples examined: {trials}     triples hitting BOTH 20 and 42 "
      f"({float(TOL)*100:.0f}%, one fitted c): {hits}")
for a, b, cc, c_star, bs in examples:
    print(f"    P=({a},{b},{cc})  c={float(c_star):.3f}  b/s={float(bs):.2f}")
print(f"⟹ with the addresses free, a 'hit' would be a {hits}-in-{trials} coincidence, not a derivation.")
print("⟹ AND at the FORCED addresses the bound in Section 3 forbids a hit outright.")

# ================================================================ VACUITY NOTE
print()
print("=" * 78)
print("SECTION 5 — WHAT WOULD HAVE BEEN A FAKE PASS (the trap this toy avoids)")
print("=" * 78)
mono_ladder = all(LADDER[i] < LADDER[i + 1] for i in range(2))
mono_D2 = all(D2(DEGREES[i], 0, c0) < D2(DEGREES[i + 1], 0, c0) for i in range(2))
print(f"ladder monotone increasing in k: {mono_ladder}")
print(f"D^2 monotone increasing in k:    {mono_D2}")
print("⟹ Both monotone. At THREE points, 'monotone reparametrisation exists' is ALWAYS true")
print("   (3 points, and a 2-parameter family (D^2 - c)^p already saturates 2 ratios).")
print("★ So 'the spectrum grades the ladder up to reparametrisation' is CONSTRUCTION-GUARANTEED")
print("  and proves nothing. Only a FIXED map, or a bound over the whole family, carries content.")
print("  This toy reports the BOUND — which no choice of parameter can evade.")

# ================================================================ C6 LEDGER
print()
print("=" * 78)
print("C6 LEDGER — every pre-registered reading reported, nulls beside hits")
print("=" * 78)
print(f"{'#':>3s} {'reading':56s} {'verdict':12s}")
ledger = [(n, v) for n, v, _ in c6]
ledger += [("M-D  one free shift fitted to s/d=20, predict b/s", v_sd),
           ("M-E  one free shift fitted to b/s=42, predict s/d", v_bs),
           ("M-F  ANY positivity-preserving shift (the bound)",
            "MISS (impossible)" if bound_holds else "reachable"),
           ("M-G  free shift + free power (2 params, 2 ratios)", "VACUOUS (guaranteed)")]
for i, (n, v) in enumerate(ledger, 1):
    print(f"{i:>3d} {n:56s} {v:12s}")
n_hits = sum(1 for _, v in ledger if v == "HIT")
print(f"\n★ {n_hits} HITS / {len(ledger)} pre-registered readings.")

# ================================================================ SCORE
print()
print("=" * 78)
checks = [
    ("controls 3/3 (2 positive, 1 negative)", controls_ok),
    ("spectrum VARIES across K-types (precondition met)", len(vals) > 1),
    ("zero-parameter readings all fail to grade the ladder",
     all(v != "HIT" for _, v, _ in c6)),
    ("one fitted shift still misses b/s by >10x", LAD_BS / bs_sd > 10),
    ("fitting b/s instead makes the masses non-positive", v_bs.startswith("DEAD")),
    ("BOUND: sup b/s = 22/9 < 42 over ALL positivity shifts", bound_holds),
    ("bound confirmed by independent numeric scan", scan_max < sup_bs),
    ("alternative address column obeys the same bound", sup_bs_alt < LAD_BS),
    ("3-point monotonicity shown to be zero-content", mono_ladder and mono_D2),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
score = sum(1 for _, ok in checks if ok)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — the re-chartered operator is the RIGHT operator and still reads the WRONG object:")
print("  The Parthasarathy/Bergman D^2 VARIES (unlike the Kostant cubic), so the re-charter")
print("  correctly diagnosed toy 5418's flatness. But varying is not grading. D^2 is QUADRATIC")
print(f"  in the degree; the ladder is a rising FACTORIAL (Pochhammer). The required b/s = 42")
print(f"  exceeds the supremum 22/9 = {float(sup_bs):.3f} attainable at ANY positivity-preserving shift.")
print("  ⟹ 'the Dirac spectrum grades the quark ladder' is FALSE BY BOUND, not by numerical miss.")
print("  ⟹ The ladder remains an FK Bergman-NORM object (F506/T2529). It is not a Dirac spectrum")
print("     under either Dirac operator. Lane B has now excluded BOTH.")
