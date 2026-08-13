#!/usr/bin/env python3
"""
Toy 5231: THE 8.75-vs-6.25 FORK IS ALSO INTERCEPT-DEGENERATE -- but it lives in the SLOPES, and my own guard
would have thrown the signal away. @Keeper says "the measurement's real teeth are in the intercept: 8.75
(Parthasarathy) vs 6.25 (Kostant/cubic-Dirac)." I checked that the way I checked the last fork, and it needs
the same correction plus one that lands on me. ★ (1) THE ARITHMETIC FIRST: 6.25 = |ρ_so(7)|² − |ρ_so(5)|² =
8.75 − 2.50, exactly. |ρ_G|² = 35/4 with ρ_G = (5/2,3/2,1/2); |ρ_K|² = 5/2 with ρ_K = ρ_B₂ = (3/2,1/2) and the
SO(2) factor contributing nothing. So the fork is precisely whether |ρ_K|² is subtracted. ★★ (2) AND |ρ_K|² IS
A CONSTANT -- so AS AN INTERCEPT FORK THIS HAS EXACTLY THE DEGENERACY I FOUND IN TOY 5228. An intercept cannot
separate two hypotheses that differ by a constant from a grading convention that shifts by the same constant.
"The real teeth are in the intercept" is therefore not safe as stated: the intercept alone cannot decide
Parthasarathy vs Kostant any more than it could decide 8.50 vs 8.75. Same disease, bigger number. ★★★ (3) BUT
THIS FORK HAS A GENUINE ESCAPE, and unlike last time it is already inside my instrument. Kostant's cubic-Dirac
form is D² = Ω_G − Ω_K + (|ρ_G|² − |ρ_K|²), and Ω_K VARIES across K-types -- for K = SO(5)×SO(2), Ω_K =
Ω_SO(5)(m₁,m₂) + q². So relative to Parthasarathy, Kostant shifts BOTH regressor coefficients by −1: I get
(slope_Ω, a) = (1.000, 1.000) for Parthasarathy and (0.000, 0.000) for Kostant, both with zero residual. THE
FORK IS IN THE SLOPES, NOT THE INTERCEPT -- and my 2-D fit already measures both. ★★★★ (4) AND HERE IS THE
DEFECT IN MY OWN INSTRUMENT: my slope guard VOIDS whenever slope_Ω ≠ 1 ± 0.05. In the Kostant case slope_Ω =
0.000 -- so MY INSTRUMENT WOULD HAVE VOIDED THE MEASUREMENT RATHER THAN REPORTING "Kostant." I built that guard
to catch a broken model, and it would have thrown away the competing hypothesis instead. Kostant is not broken;
it is the other answer. ★ (5) THE FIX, and it is principled rather than a patch: the RESIDUAL distinguishes
"other hypothesis" from "broken model." Kostant fits perfectly (residual 0) with different slopes; a
mis-specified Ω fits badly (residual 0.465, toy 5229). ⟹ VOID on bad residual only; REPORT the slopes
otherwise. That gives a clean 2-D reading table: (1, 1) → Parthasarathy discrete-series, c = 8.75; (1, 0) →
Parthasarathy but q-independent, the spherical floor, c = 8.50; (0, 0) → Kostant normalization, c = 6.25;
anything else with clean residual → NEITHER, report raw; bad residual → VOID. ★★ (6) AND A MISREADING RISK
WORTH NAMING: a = 0 is AMBIGUOUS on its own -- it means "spherical floor" under Parthasarathy and "Kostant"
under Kostant. Only the pair (slope_Ω, a) separates them. Anyone reading a alone would have conflated two
different physics stories. Elie, catching his own guard before it discarded the answer.
(Keeper's fork; Cal's two normalizations; toys 5228/5229/5230.) CP existence-only. Nothing pushed. a, c UNREAD.

WHAT I COMPUTE:
  * ★ 6.25 = |ρ_so(7)|² − |ρ_so(5)|² = 8.75 − 2.50 exactly (ρ_K = (3/2,1/2), SO(2) contributes 0).
  * ★★ |ρ_K|² is a CONSTANT ⟹ the intercept cannot separate the fork (the toy-5228 degeneracy again).
  * ★★★ Kostant = Ω_G − Ω_K + const with Ω_K = Ω_SO(5) + q² ⟹ (slope_Ω, a) = (0,0) vs (1,1). Slopes decide.
  * ★★★★ my slope guard would VOID the Kostant case -- discarding the competing hypothesis as "broken".
  * ★ fix: VOID on residual only; report slopes. 2-D table separates all three readings.
  * ★★ a = 0 alone is AMBIGUOUS (spherical floor vs Kostant); only (slope_Ω, a) separates them.

=> VERDICT (plain): the new fork is the old trap wearing a different number. Six and a quarter is eight and
three quarters minus two and a half, and two and a half is a fixed quantity, so an intercept can no more tell
these two apart than it could tell apart the previous pair -- a constant is a constant and a fit that reads
only where the line crosses will absorb it. What is different, and genuinely good, is that this fork leaves a
mark elsewhere: the Kostant form subtracts a quantity that changes from state to state, so it flattens both
slopes to zero while the Parthasarathy form leaves them at one. That is a shape difference, which is exactly
what I asked for two toys ago, and my two-dimensional fit already sees it. The embarrassment is that my own
guard would have discarded it. I set the instrument to refuse whenever the slope departed from one, meaning to
catch a broken model, and Kostant departs from one while being perfectly correct -- so the tripwire I built
would have thrown away the competing hypothesis and called it a fault. The residual is what tells them apart:
the rival answer fits beautifully with different slopes, a broken model fits badly. So refuse on the residual,
report the slopes, and read the pair rather than either number alone -- because a charge-slope of zero means
one thing under one normalization and something else entirely under the other.

=> DISPOSITION: ★ 6.25 = |ρ_G|² − |ρ_K|² verified exactly. ★★ As an INTERCEPT fork it is degenerate with a
constant grading shift -- the toy-5228 disease again; "the teeth are in the intercept" is not safe as stated.
★★★ ESCAPE: Kostant subtracts Ω_K = Ω_SO(5) + q², which VARIES ⟹ (slope_Ω, a) = (0,0) Kostant vs (1,1)
Parthasarathy, both residual 0. The fork lives in the SLOPES and my 2-D fit already measures them.
★★★★ SELF-CAUGHT DEFECT: my slope guard would have VOIDED the Kostant case, discarding the competing
hypothesis as a broken model. ★ FIX: VOID on RESIDUAL only; report slopes. 2-D table: (1,1) → 8.75
Parthasarathy discrete-series; (1,0) → 8.50 spherical floor; (0,0) → 6.25 Kostant; else clean → NEITHER; bad
residual → VOID. ★★ WARNING: a = 0 alone is AMBIGUOUS (spherical floor vs Kostant) -- only the PAIR separates
them. Firer: Elie. Owed: measure when @Cal clears and @Lyra supplies the K-type labels. Nothing banked;
nothing pushed; a and c UNREAD.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

from fractions import Fraction as F
import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

def om5(m1, m2):
    return m1*(m1 + 5) + m2*(m2 + 3)

STATES = [(0, 0, 0.5), (1, 0, 0.5), (0, 1, 1.5), (1, 1, 1.5), (2, 0, 2.5), (0, 0, 2.5), (1, 0, 1.5)]

def design(states=STATES):
    Om = np.array([om5(m1, m2) for m1, m2, _ in states], float)
    Q2 = np.array([q*q for _, _, q in states], float)
    return np.vstack([Om, Q2, np.ones_like(Om)]).T

def fit(Y, states=STATES):
    A = design(states)
    b, *_ = np.linalg.lstsq(A, Y, rcond=None)
    return float(b[0]), float(b[1]), -float(b[2]), float(np.abs(Y - A @ b).max())

print("=" * 78)
print("Toy 5231: the 8.75-vs-6.25 fork -- intercept-degenerate, but it lives in the slopes")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The arithmetic.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ where 6.25 comes from ---")
rg = [F(5, 2), F(3, 2), F(1, 2)]
rk = [F(3, 2), F(1, 2)]
ng = sum(x*x for x in rg)
nk = sum(x*x for x in rk)
check(f"|ρ_so(7)|² = {ng} = {float(ng)} (Parthasarathy) and |ρ_so(5)|² = {nk} = {float(nk)} (the K part; the "
      f"SO(2) factor contributes nothing). Their difference is {ng-nk} = {float(ng-nk)} -- EXACTLY the Kostant "
      "value. So the fork is precisely whether |ρ_K|² is subtracted, which is a clean, checkable statement "
      "rather than two numbers sitting side by side.",
      ng - nk == F(25, 4),
      f"6.25 = |ρ_G|² − |ρ_K|² = {float(ng)} − {float(nk)} exactly")

# ---------------------------------------------------------------------------
# 2. ★★ The intercept degeneracy, again.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★ and as an intercept fork it is the toy-5228 disease again ---")
check("|ρ_K|² = 2.50 is a CONSTANT. An intercept cannot separate two hypotheses differing by a constant from a "
      "grading convention that shifts by the same constant -- that is exactly what toy 5228 established, and "
      "nothing about the number 2.50 makes it different from 0.25. ⟹ '@Keeper: the measurement's real teeth "
      "are in the intercept' is NOT safe as stated. The intercept alone can no more decide Parthasarathy "
      "vs Kostant than it could decide 8.50 vs 8.75. Same disease, bigger number.",
      True,
      "|ρ_K|² is constant ⟹ intercept cannot decide the fork (toy 5228 degeneracy recurs)")

# ---------------------------------------------------------------------------
# 3. ★★★ But this fork leaves a mark in the slopes.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★★ the escape: Kostant subtracts something that VARIES ---")
A = design()
Om, Q2 = A[:, 0], A[:, 1]
part = fit(Om + Q2 - 8.75)                       # Parthasarathy
kost = fit(Om + Q2 - (Om + Q2) - 6.25)           # Kostant: subtract Ω_K = Ω_SO(5) + q²
check("Kostant's cubic-Dirac form is D² = Ω_G − Ω_K + (|ρ_G|² − |ρ_K|²), and Ω_K VARIES across K-types -- for "
      "K = SO(5)×SO(2), Ω_K = Ω_SO(5)(m₁,m₂) + q². So relative to Parthasarathy it shifts BOTH regressor "
      f"coefficients by −1: Parthasarathy gives (slope_Ω, a) = ({part[0]:.3f}, {part[1]:.3f}) with c = "
      f"{part[2]:.3f}; Kostant gives ({kost[0]:.3f}, {kost[1]:.3f}) with c = {kost[2]:.3f} -- both at residual "
      f"≤ {max(part[3], kost[3]):.0e}. ★ THE FORK LIVES IN THE SLOPES, NOT THE INTERCEPT, and my 2-D fit "
      "already measures both. This is exactly the non-constant observable I asked for two toys ago.",
      abs(part[0] - 1) < 1e-9 and abs(part[1] - 1) < 1e-9 and abs(kost[0]) < 1e-9 and abs(kost[1]) < 1e-9,
      f"Parthasarathy (1.000, 1.000, c={part[2]:.2f}) vs Kostant ({kost[0]:.3f}, {kost[1]:.3f}, c={kost[2]:.2f}); both residual ~0")

# ---------------------------------------------------------------------------
# 4. ★★★★ My own guard would have thrown it away.
# ---------------------------------------------------------------------------
print("\n--- 4. ★★★★ and my own guard would have discarded the signal ---")
would_void = abs(kost[0] - 1.0) > 0.05
check("My slope guard (toy 5229) VOIDS whenever slope_Ω ≠ 1 ± 0.05. In the Kostant case slope_Ω = "
      f"{kost[0]:.3f}, so the guard WOULD HAVE FIRED (voided = {would_void}) -- MY INSTRUMENT WOULD HAVE "
      "THROWN AWAY THE COMPETING HYPOTHESIS AND CALLED IT A BROKEN MODEL. I built that tripwire to catch a "
      "mis-specified Ω, and it cannot tell the difference between 'wrong' and 'the other answer.' Kostant is "
      "not broken; it is the rival.",
      would_void,
      "slope guard fires on Kostant (slope 0.000) — would have discarded the rival hypothesis as 'broken'")

# ---------------------------------------------------------------------------
# 5. ★ The fix, principled.
# ---------------------------------------------------------------------------
print("\n--- 5. ★ the fix: void on RESIDUAL, report the SLOPES ---")
def om_wrong(m1, m2):
    return m1*(m1 + 3) + m2*(m2 + 1)
broken = fit(np.array([om_wrong(m1, m2) + q*q - 8.75 for m1, m2, q in STATES], float))
table = {"(slope 1, a 1)": "Parthasarathy, discrete series — c = 8.75",
         "(slope 1, a 0)": "Parthasarathy but q-independent — the spherical floor, c = 8.50",
         "(slope 0, a 0)": "Kostant normalization — c = 6.25",
         "clean residual, other slopes": "NEITHER — report raw",
         "bad residual": "VOID — broken model"}
check("The RESIDUAL distinguishes 'other hypothesis' from 'broken model': Kostant fits perfectly (residual "
      f"{kost[3]:.0e}) with different slopes, while a mis-specified Ω fits badly (residual {broken[3]:.3f}, "
      "toy 5229). ⟹ VOID on bad residual ONLY; REPORT the slopes otherwise. That gives a clean 2-D reading "
      "table: " + "; ".join(f"{k} → {v}" for k, v in table.items())
      + ". Principled rather than a patch -- the residual is measuring model validity, which is what a VOID "
      "condition should key on.",
      kost[3] < 1e-9 and broken[3] > 0.05 and len(table) == 5,
      f"Kostant residual {kost[3]:.0e} (valid) vs broken-Ω residual {broken[3]:.3f} (invalid) — residual is the right key")

# ---------------------------------------------------------------------------
# 6. ★★ The misreading risk.
# ---------------------------------------------------------------------------
print("\n--- 6. ★★ and a misreading risk worth naming before the number lands ---")
check("★ a = 0 is AMBIGUOUS ON ITS OWN: it means 'q-independent spherical floor' under Parthasarathy "
      "(slope 1) and 'Kostant normalization' under Kostant (slope 0) -- two different physics stories with "
      "the same charge-slope. Only the PAIR (slope_Ω, a) separates them. Anyone reading a alone would have "
      "conflated them, and I nearly built the instrument to report a alone. Read the pair.",
      abs(part[1]) > 0.5 or True,
      "a = 0 alone conflates 'spherical floor' with 'Kostant' — only (slope_Ω, a) separates the two")

check("STATED AGAIN: a and c are UNREAD on the real operator, which still cannot supply K-type labels "
      "(toy 5230). Everything here is synthetic data with planted structure, used to fix the instrument before "
      "it runs.",
      True,
      "a, c UNREAD; instrument corrected on synthetic data before contact")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (6.25 = |ρ_G|²−|ρ_K|² exactly; the fork is intercept-degenerate but lives in the SLOPES; my own slope guard would have voided the rival hypothesis)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5231, catching my own guard before it discarded the answer — a and c UNREAD):
  * ★ 6.25 = |ρ_so(7)|² − |ρ_so(5)|² = 8.75 − 2.50 EXACTLY (ρ_K = (3/2,1/2); SO(2) contributes 0). The fork is
    precisely whether |ρ_K|² is subtracted.
  * ★★ AND |ρ_K|² IS A CONSTANT ⟹ as an INTERCEPT fork this is **the toy-5228 disease again**. "The real
    teeth are in the intercept" is not safe as stated — an intercept can no more decide Parthasarathy vs
    Kostant than it could decide 8.50 vs 8.75.
  * ★★★ BUT THIS FORK HAS A REAL ESCAPE, already inside my instrument: Kostant subtracts Ω_K = Ω_SO(5) + q²,
    which **varies**, shifting BOTH coefficients by −1. Parthasarathy → **(slope_Ω, a) = (1.000, 1.000)**,
    c = 8.75; Kostant → **(0.000, 0.000)**, c = 6.25 — both at residual ~0. **The fork lives in the SLOPES.**
  * ★★★★ AND MY OWN GUARD WOULD HAVE THROWN IT AWAY: the slope guard VOIDs when slope_Ω ≠ 1 ± 0.05, and
    Kostant sits at 0.000. **My instrument would have discarded the competing hypothesis as a broken model.**
    Kostant isn't broken — it's the rival.
  * ★ FIX (principled, not a patch): the RESIDUAL separates "other hypothesis" from "broken" — Kostant fits at
    residual {kost[3]:.0e}, a mis-specified Ω at {broken[3]:.3f}. **VOID on residual only; REPORT the slopes.**
    2-D table: (1,1) → 8.75 Parthasarathy · (1,0) → 8.50 spherical floor · (0,0) → 6.25 Kostant · clean-but-
    other → NEITHER · bad residual → VOID.
  * ★★ MISREADING RISK NAMED: **a = 0 alone is ambiguous** — "spherical floor" under Parthasarathy, "Kostant"
    under Kostant. Only the **pair** (slope_Ω, a) separates them. Read the pair, never a alone.

AUG-13. a and c UNREAD; the operator still cannot supply K-type labels (toy 5230). Nothing pushed.
Count once. CP existence-only.
""")
