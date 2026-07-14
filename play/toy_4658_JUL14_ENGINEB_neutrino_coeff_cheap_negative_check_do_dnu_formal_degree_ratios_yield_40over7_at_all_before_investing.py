#!/usr/bin/env python3
"""
Toy 4658 — Jul 14 (Engine B / neutrino-coefficient lane, mine): the CHEAP NEGATIVE CHECK the Wednesday pull asked
for BEFORE anyone invests in forcing the neutrino f-factors: "do d(ν) [formal-degree] ratios yield 40/7 at all?"
The observed neutrino ratio is m_ν3/m_ν2 = f3/f2 = (10/3)/(7/12) = 40/7 ≈ 5.714 (and m_ν2/m_ν3 = 7/40 = 0.175).
If NO pair of physically-allowed formal degrees d(ν) reproduces 40/7 (or the individual factors), the formal-
degree route is DEAD and we don't waste effort forcing it — the fiber-overlap route (4655, 4% near-miss) leads.

DISCIPLINE: this is a fish-detector run. I compute EXACTLY (Fraction — ν are rationals, d(ν) is a polynomial,
so d(ν) is an exact rational; no float slop). I do NOT tune ν to hit 40/7 — I enumerate the physically-motivated
ν-grid (Wallach/half-integer points 1/2..9/2 and integers) and read off whether 40/7 appears NATURALLY.

THE FORMAL DEGREE (Harish-Chandra, D_IV⁵, as used across the corpus):
    d(ν) = (5/2 − ν)(1 − ν)(2 − ν)(3 − ν)(4 − ν)
  (the ν=9/2 shadow of ν=1/2 has d(9/2) = −d(1/2) < 0 → non-unitary, the ν_R absence, K673.)

THE TEST: enumerate ν ∈ {1/2, 1, 3/2, 2, 5/2, 3, 7/2, 4, 9/2}, compute d(ν) EXACTLY, and check every ORDERED
pair ratio d(ν_a)/d(ν_b) against the targets {40/7, 7/40, 7/12, 10/3}. Also check the seesaw form d(ν)² ratios
(Weinberg is quadratic). Report whether ANY pair lands the target EXACTLY, and the closest near-miss.

⟹ EXPECTED (honest prior): the f-factors have THREE incompatible "derivations" already (the numerology tell), so
I expect NO clean d(ν) pair gives 40/7. If confirmed, the formal-degree route is ruled out cheaply and the
coefficients STAY fitted-then-recognized (a lead), with the fiber-overlap route (4655) as the only near-miss.
Count ~7-8 (α RULED, identified).
"""
from fractions import Fraction as F
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def d(nu):
    """formal degree d(ν) = (5/2−ν)(1−ν)(2−ν)(3−ν)(4−ν), exact."""
    nu = F(nu)
    return (F(5,2)-nu)*(1-nu)*(2-nu)*(3-nu)*(4-nu)

print("=" * 92)
print("Toy 4658 — cheap negative check: do d(ν) formal-degree ratios yield 40/7 (neutrino f-factors)?")
print("=" * 92)

# ---- the ν-grid and their exact formal degrees ------------------------------
grid = [F(1,2), F(1), F(3,2), F(2), F(5,2), F(3), F(7,2), F(4), F(9,2)]
dvals = {nu: d(nu) for nu in grid}
print("\n[formal degrees d(ν) on the physical grid]:")
for nu in grid:
    print(f"   ν={str(nu):>4}   d(ν) = {str(dvals[nu]):>10}")

# targets
targets = {"40/7 (m3/m2)": F(40,7), "7/40 (m2/m3)": F(7,40), "7/12 (f2)": F(7,12), "10/3 (f3)": F(10,3)}

# ---- test 1: linear d(ν) ratios ---------------------------------------------
def scan_ratios(valfn, label_pow):
    hits, best = [], None
    for na in grid:
        for nb in grid:
            if na == nb: continue
            va, vb = valfn(dvals[na]), valfn(dvals[nb])
            if vb == 0: continue
            r = F(va, vb) if isinstance(va, int) else va/vb
            for tname, tval in targets.items():
                if r == tval:
                    hits.append((na, nb, tname, r))
                # track closest to 40/7 for the near-miss report
                if tname == "40/7 (m3/m2)" and r > 0:
                    err = abs(float(r) - float(tval))/float(tval)
                    if best is None or err < best[0]:
                        best = (err, na, nb, float(r))
    return hits, best

lin_hits, lin_best = scan_ratios(lambda x: x, "d(ν)")
print(f"\n[test 1 — linear d(ν) ratios]: exact target hits = {len(lin_hits)}")
for na, nb, tname, r in lin_hits:
    print(f"   d({na})/d({nb}) = {r} = {tname}")
if lin_best:
    err, na, nb, rv = lin_best
    print(f"   closest to 40/7: d({na})/d({nb}) = {rv:.4f} (err {err*100:.1f}%)")

# ---- test 2: seesaw-quadratic d(ν)² ratios (Weinberg is quadratic) ----------
sq_hits, sq_best = scan_ratios(lambda x: x*x, "d(ν)²")
print(f"\n[test 2 — quadratic d(ν)² ratios (Weinberg)]: exact target hits = {len(sq_hits)}")
for na, nb, tname, r in sq_hits:
    print(f"   d({na})²/d({nb})² = {r} = {tname}")
if sq_best:
    err, na, nb, rv = sq_best
    print(f"   closest to 40/7: d({na})²/d({nb})² = {rv:.4f} (err {err*100:.1f}%)")

# ---- the checks -------------------------------------------------------------
check("d(ν) COMPUTED EXACTLY (Fraction, no float slop): d(ν)=(5/2−ν)(1−ν)(2−ν)(3−ν)(4−ν) on the physical grid "
      "ν∈{1/2..9/2}. Includes the K673 shadow fact d(9/2)=−d(1/2)<0 (ν_R non-unitary).",
      dvals[F(9,2)] == -dvals[F(1,2)], f"d(1/2)={dvals[F(1,2)]}, d(9/2)={dvals[F(9,2)]} — shadow sign confirmed")

check("NEGATIVE CHECK — LINEAR d(ν) ratios do NOT yield 40/7 (nor 7/12, 10/3, 7/40) for ANY grid pair: exact "
      f"target hits = {len(lin_hits)}. The formal-degree ratio does not naturally produce the neutrino coefficients.",
      len(lin_hits) == 0, f"no exact d(ν)-pair lands the targets; closest to 40/7 is {lin_best[3]:.3f} at {lin_best[0]*100:.0f}% off" if lin_best else "no hits")

check("NEGATIVE CHECK — QUADRATIC d(ν)² ratios (the seesaw/Weinberg form) also do NOT yield 40/7: exact target "
      f"hits = {len(sq_hits)}. Even the physically-correct quadratic form of the formal degree misses.",
      len(sq_hits) == 0, f"no exact d(ν)²-pair lands the targets; closest to 40/7 is {sq_best[3]:.3f} at {sq_best[0]*100:.0f}% off" if sq_best else "no hits")

check("VERDICT (cheap negative delivered): the d(ν) FORMAL-DEGREE route is RULED OUT for the neutrino f-factors — "
      "neither linear nor quadratic d(ν) ratios reproduce 40/7 (or 7/12, 10/3) for any physical ν-pair. So the "
      "team should NOT invest in forcing the coefficients from formal degrees. The fiber-overlap route (4655, "
      "quadratic Weinberg overlap, 4% near-miss) remains the ONLY near-miss; the coefficients STAY fitted-then-"
      "recognized (a lead, three incompatible 'derivations' = the numerology tell). I do NOT dress them as derived.",
      len(lin_hits) == 0 and len(sq_hits) == 0,
      "formal-degree route dead; fiber-overlap route leads (4% miss); coefficients remain a lead. Count ~7-8 (α RULED)")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 92)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 92)
print(f"SCORE: {passed}/{total}")
print("=" * 92)
print("""
CHEAP NEGATIVE CHECK — do d(ν) formal-degree ratios yield 40/7? NO (route ruled out):
  * d(ν)=(5/2−ν)(1−ν)(2−ν)(3−ν)(4−ν) computed EXACTLY on ν∈{1/2..9/2}; d(9/2)=−d(1/2) (K673 shadow).
  * LINEAR d(ν) ratios: 0 exact hits on {40/7, 7/40, 7/12, 10/3}.
  * QUADRATIC d(ν)² ratios (seesaw/Weinberg): 0 exact hits.
  => the FORMAL-DEGREE route is RULED OUT for the neutrino coefficients — don't invest in forcing it.
     The fiber-overlap route (4655, 4% near-miss) leads; coefficients STAY fitted-then-recognized (a lead).
     Cheap negative delivered before the team spent effort. Count ~7-8.
""")
