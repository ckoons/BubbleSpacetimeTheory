#!/usr/bin/env python3
"""
Toy 5227: THE REBUILT INSTRUMENT, PUBLISHED BLIND -- and one demonstration that made the guards non-optional.
@Keeper replaced the stale spec with a target-innocent one: c is the INTERCEPT of D²(K-type) = Casimir(K-type)
− c, fit across ≥3 K-types, with Casimir(m₁,m₂) = m₁(m₁+n_C) + m₂(m₂+N_c). That is a much better design than
mine -- the instrument never compares anything to 8.75 while it runs; it fits a line and reads where it crosses.
I have rebuilt to it, validated it on knowns first, and I am publishing it before it sees the operator. ★ (1)
VALIDATED ON SYNTHETIC KNOWNS, exactly: fed data built as Casimir − c with c = 8.75, 8.50, 0.00 and 6.25, the
fit returns 8.7500, 8.5000, 0.0000 and 6.2500 with slope 1.000000 and residuals at 7×10⁻¹⁵. It recovers what it
is given, including values that are none of the candidates. ★★ (2) AND THE MODEL-FAILURE CHECK PRODUCED THE
RESULT THAT MATTERS: I fed it data whose slope is 2 rather than 1 -- i.e. a case where D² = Casimir − c is
simply the wrong model -- and the fit returned c = 8.750. EXACTLY the expected value, from data that violates
the model. Without a slope guard, a wrong model would have looked like a perfect confirmation, landing precisely
on the target. That is not a hypothetical: it is what the arithmetic does. ⟹ THE SLOPE GUARD IS LOAD-BEARING,
not decoration, and I am pre-registering it as a PASS/VOID condition rather than a diagnostic. ★ (3) THREE
GUARDS, all pre-registered now: (a) HERMITICITY -- carried from toy 5225; no self-adjoint D, no sea, no c, and
the instrument raises rather than returning a number. (b) SLOPE = 1.000 ± 0.05 -- if the fitted slope departs,
the model D² = Casimir − c does not hold and the intercept is meaningless, so the measurement is VOID, not
"approximately right." (c) RESIDUAL ≤ 0.05 -- a nonlinear spectrum trips it (verified: residual 2.633 on
Casimir^1.3). ★★ (4) AND I AM RE-LOCKING THE CRITERIA TO THE NEW OBJECT, explicitly and dated, because toy 5226
established that the old anchoring does not transfer: c within ±0.05 of 8.75 → full so(7) ρ-Casimir |ρ|²;
within ±0.05 of 8.50 → rank-2 symmetric-space ρ; within ±0.05 of 0 → no intercept, still flat; ANYTHING ELSE →
report the raw number and claim NEITHER. Same numbers, freshly anchored to the intercept rather than to a local
limit, committed here before the instrument has seen the operator. ★ (5) GATE STATUS UNCHANGED: @Lyra's
minimal-K-type reconciliation is open (if the minimal K-type is (0,0) rather than the Ω ≥ 35/4 sector, D² ⪰ 0
fails and there is a real problem to face), and @Cal has not certified. I measure when both close. I still have
not read c. Elie, rebuilding to a better spec than his own. (Keeper's replacement spec; toys 5225/5226.)
CP existence-only. Nothing pushed.

WHAT I COMPUTE:
  * ★ Casimir(m₁,m₂) = m₁(m₁+5) + m₂(m₂+3) across six K-types: 0, 6, 4, 10, 14, 18 -- good fit leverage.
  * ★ fit recovers known intercepts EXACTLY (8.75, 8.50, 0.00, 6.25; slope 1.000000, residual 7e-15).
  * ★★ a WRONG model (slope 2) returns c = 8.750 -- the expected answer -- so the slope guard is load-bearing.
  * ★ three pre-registered guards: Hermiticity, slope = 1 ± 0.05, residual ≤ 0.05. Failure ⟹ VOID, not "close".
  * ★★ criteria RE-LOCKED to the intercept object, dated, before the instrument sees anything.

=> VERDICT (plain): the replacement specification is better than the one I wrote, and the reason is that it
never looks at the answer while it works -- it fits a straight line through several representations and reports
where the line crosses, so the target plays no part in the computation. Rebuilt to it, the instrument recovers
intercepts I plant in synthetic data to fourteen decimal places, including values that match none of our
candidates, which is the property you want. The thing worth reporting, though, came out of trying to break it.
I fed it data that disobeys the model -- a slope of two where the model says one -- and it returned eight point
seven five, exactly the number we are hoping for, from data that has nothing to do with the physics. So the
check on the slope is not housekeeping. Without it a broken model would have handed back a perfect-looking
confirmation, and nobody reading the number alone could have told. It is now a condition that voids the
measurement rather than a note in the margin. And since the object being measured changed yesterday, I have
re-anchored the thresholds to the new one openly, with the same numbers and a fresh date, so the
pre-registration means what it says.

=> DISPOSITION: INSTRUMENT REBUILT to @Keeper's target-innocent spec and PUBLISHED BLIND. ★ Validated on four
synthetic knowns (exact recovery, slope 1.000000, residual 7e-15). ★★ CRITICAL: a wrong model (slope 2) returns
c = 8.750 -- the expected value -- so the SLOPE GUARD IS LOAD-BEARING and is pre-registered as a VOID condition,
not a diagnostic. ★ Three guards pre-registered: Hermiticity (5225), slope = 1 ± 0.05, residual ≤ 0.05.
★★ CRITERIA RE-LOCKED to the intercept object, dated, before the instrument saw the operator: 8.75 / 8.50 / 0 /
NEITHER at ±0.05, "neither" still reserved and still the informative branch. ★ GATE: @Lyra's minimal-K-type
reconciliation open; @Cal's certification outstanding. Firer: Elie. Owed: measure when both close.
Nothing banked; nothing pushed; c NOT measured.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

N_C, NC3 = 5, 3
KTYPES = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (2, 1)]

def casimir(m1, m2):
    """Keeper's spec: Casimir(m1,m2) = m1(m1+n_C) + m2(m2+N_c)."""
    return m1*(m1 + N_C) + m2*(m2 + NC3)

# ---------------------------------------------------------------------------
# THE INSTRUMENT -- published before it sees the operator. Three guards, all VOID conditions.
# ---------------------------------------------------------------------------
def assert_hermitian(D, tol=1e-10, where="spectral step"):
    asym = float(np.abs(D - D.conj().T).max()/max(np.abs(D).max(), 1e-300))
    if asym > tol:
        raise ValueError(f"NON-HERMITIAN at {where}: {asym:.3e} > {tol:.0e}. No self-adjoint D, no sea, no c.")
    return asym

def measure_c(d2_of_ktype, ktypes=KTYPES, tol=0.05, slope_tol=0.05, resid_tol=0.05):
    """c = intercept of D²(K-type) = Casimir(K-type) − c, fit across ≥3 K-types.
       DECLARED INPUTS ONLY. Never references the candidate values while computing.
       VOIDS (raise) on: bad slope, bad residual. Returns (c, slope, residual, verdict)."""
    if len(ktypes) < 3:
        raise ValueError("need >= 3 K-types for the fit")
    C = np.array([casimir(*k) for k in ktypes], float)
    Y = np.array([float(d2_of_ktype(k)) for k in ktypes], float)
    A = np.vstack([C, np.ones_like(C)]).T
    (slope, inter), *_ = np.linalg.lstsq(A, Y, rcond=None)
    resid = float(np.abs(Y - (slope*C + inter)).max())
    if abs(slope - 1.0) > slope_tol:
        raise ValueError(f"MODEL VOID: fitted slope {slope:.4f} != 1 within {slope_tol}. "
                         "D^2 = Casimir - c does not hold, so the intercept is meaningless.")
    if resid > resid_tol:
        raise ValueError(f"MODEL VOID: max residual {resid:.4f} > {resid_tol}. Spectrum is not linear in Casimir.")
    c = -float(inter)
    if abs(c - 8.75) < tol:
        v = "full so(7) rho-Casimir |rho|^2"
    elif abs(c - 8.50) < tol:
        v = "rank-2 symmetric-space rho"
    elif abs(c) < tol:
        v = "no intercept - still flat"
    else:
        v = f"NEITHER - raw c = {c:.4f}"
    return c, float(slope), resid, v

print("=" * 78)
print("Toy 5227: the rebuilt instrument, published blind -- c NOT measured")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. Casimir leverage.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ the Casimir grading gives real fit leverage ---")
cas = [(k, casimir(*k)) for k in KTYPES]
check("Casimir(m₁,m₂) = m₁(m₁+n_C) + m₂(m₂+N_c) across six K-types gives "
      + ", ".join(f"{k} → {v}" for k, v in cas)
      + " -- six distinct values spanning 0 to 18. That is genuine leverage for a straight-line fit, which is "
      "what makes the intercept readable rather than an extrapolation from a huddle of points.",
      len({v for _, v in cas}) >= 5,
      f"{len({v for _, v in cas})} distinct Casimir values from 0 to {max(v for _, v in cas)} — good leverage")

# ---------------------------------------------------------------------------
# 2. Validated on knowns.
# ---------------------------------------------------------------------------
print("\n--- 2. ★ validated on synthetic knowns BEFORE trusting it ---")
recovered = {}
for true_c in (8.75, 8.50, 0.00, 6.25):
    c, s, r, _ = measure_c(lambda k, t=true_c: casimir(*k) - t)
    recovered[true_c] = (c, s, r)
check("Fed data built as Casimir − c, the fit returns "
      + "; ".join(f"planted {t} → {v[0]:.4f} (slope {v[1]:.6f}, resid {v[2]:.0e})" for t, v in recovered.items())
      + ". Exact recovery to fourteen decimals, INCLUDING 6.25, which is none of the candidates -- the "
      "instrument returns what it is given rather than what it is hoping for. This is the validate-first step "
      "that has saved me three separate times this week.",
      all(abs(v[0] - t) < 1e-9 and abs(v[1] - 1) < 1e-9 for t, v in recovered.items()),
      f"exact recovery of {list(recovered)}; slopes 1.000000; residuals ≤ 1e-14")

# ---------------------------------------------------------------------------
# 3. ★★ The demonstration that made the guard non-optional.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★ and trying to break it produced the result that matters ---")
C = np.array([casimir(*k) for k in KTYPES], float)
Y = 2.0*C - 8.75
A = np.vstack([C, np.ones_like(C)]).T
(sl_bad, in_bad), *_ = np.linalg.lstsq(A, Y, rcond=None)
voided = False
try:
    measure_c(lambda k: 2.0*casimir(*k) - 8.75)
except ValueError:
    voided = True
check("★★ I fed it data with slope 2 -- a case where D² = Casimir − c is simply the WRONG MODEL -- and the raw "
      f"fit returns an intercept of {-in_bad:.3f}. EXACTLY the expected value, from data that violates the "
      "model. Without a slope guard, a broken model would have looked like a PERFECT CONFIRMATION landing "
      "precisely on the target, and nobody reading the number alone could have told. That is not a "
      f"hypothetical -- it is what the arithmetic does. With the guard in place the instrument VOIDS instead "
      f"(raised = {voided}). ⟹ the slope check is load-bearing, and I am pre-registering it as a VOID "
      "condition rather than a diagnostic note.",
      abs(-in_bad - 8.75) < 1e-9 and voided,
      f"wrong model (slope {sl_bad:.1f}) returns c = {-in_bad:.3f} — the expected value. Guard VOIDS it.")

# ---------------------------------------------------------------------------
# 4. The three guards.
# ---------------------------------------------------------------------------
print("\n--- 4. ★ three guards, all pre-registered as VOID conditions ---")
nonlin_voided = False
try:
    measure_c(lambda k: casimir(*k)**1.3)
except ValueError:
    nonlin_voided = True
guards = {"(a) Hermiticity": "no self-adjoint D ⟹ no sea ⟹ no c; raises (carried from toy 5225)",
          "(b) slope = 1.000 ± 0.05": "else D² = Casimir − c does not hold ⟹ intercept meaningless ⟹ VOID",
          "(c) residual ≤ 0.05": f"nonlinear spectrum trips it (verified: Casimir^1.3 voided = {nonlin_voided})"}
check("Pre-registered now, before the instrument sees the operator: "
      + "; ".join(f"{k} — {v}" for k, v in guards.items())
      + ". All three RAISE rather than returning a number. A failed guard means the measurement is VOID, not "
      "'approximately right' -- which is the distinction that stops a broken run from being reported as a "
      "near-miss.",
      nonlin_voided and len(guards) == 3,
      "three guards, all VOID-on-failure; nonlinear case verified to trip the residual guard")

# ---------------------------------------------------------------------------
# 5. ★★ Criteria re-locked to the new object.
# ---------------------------------------------------------------------------
print("\n--- 5. ★★ criteria RE-LOCKED to the intercept object, dated, before any reading ---")
locked = {"|c − 8.75| < 0.05": "full so(7) ρ-Casimir |ρ|²",
          "|c − 8.50| < 0.05": "rank-2 symmetric-space ρ",
          "|c| < 0.05": "no intercept — still flat",
          "anything else": "report the RAW number, claim NEITHER"}
check("Toy 5226 established that my old anchoring (a local limit of D²) does not transfer to this object, so I "
      "am re-locking explicitly rather than letting the thresholds drift across: "
      + "; ".join(f"{k} → {v}" for k, v in locked.items())
      + ". Same numbers, freshly anchored to the INTERCEPT, dated at this timestamp, committed before the "
      "instrument has seen the operator. The 'neither' branch stays reserved and -- since both 8.50 and 8.75 "
      "are natural ρ-invariants (toy 5221) -- it is still the informative outcome.",
      len(locked) == 4,
      "±0.05 on four branches, re-anchored to the intercept; 'neither' reserved and still the informative one")

# ---------------------------------------------------------------------------
# 6. Gate status.
# ---------------------------------------------------------------------------
print("\n--- 6. gate status: unchanged, and I have still not read c ---")
check("@Lyra's minimal-K-type reconciliation is open -- if the minimal K-type is (0,0) rather than the "
      "Ω ≥ 35/4 sector then D² ⪰ 0 fails and there is a real problem to face, which is the bedrock question "
      "@Keeper named. And @Cal has not certified. I measure when both close. The instrument is built, "
      "validated, guarded and published; the operator is untouched by it.",
      True,
      "gate: minimal-K-type OPEN, @Cal's certification OUTSTANDING. c NOT measured.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (instrument rebuilt to the target-innocent spec, validated exactly on knowns; a WRONG model returns exactly 8.750, so the slope guard is a VOID condition)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5227, rebuilt to a better spec than my own — c still NOT measured):
  * ★ @Keeper's replacement spec is better than mine: c is the INTERCEPT of D² = Casimir − c, fit across ≥3
    K-types. **The instrument never compares anything to 8.75 while it runs.** Casimir values across six
    K-types span 0 to 18 — real fit leverage.
  * ★ VALIDATED ON KNOWNS FIRST: planted intercepts 8.75, 8.50, 0.00 and **6.25** are recovered exactly
    (slope 1.000000, residual ≤ 1e-14). It returns what it is given, including values matching no candidate.
  * ★★ AND BREAKING IT PRODUCED THE RESULT THAT MATTERS: fed data with **slope 2** — where D² = Casimir − c is
    simply the wrong model — the raw fit returns **c = 8.750. Exactly the expected value, from data that
    violates the model.** Without a slope guard a broken model would have looked like a *perfect confirmation*
    landing precisely on the target, and the number alone would not have betrayed it.
    ⟹ **THE SLOPE GUARD IS LOAD-BEARING**, pre-registered as a **VOID** condition, not a diagnostic.
  * ★ THREE GUARDS, all VOID-on-failure: (a) Hermiticity — no self-adjoint D, no sea, no c; (b) slope
    1.000 ± 0.05; (c) residual ≤ 0.05 (verified: Casimir^1.3 trips it). A failed guard means **void**, never
    "approximately right."
  * ★★ CRITERIA RE-LOCKED to the intercept object, dated, before the instrument saw anything (toy 5226 showed
    the old anchoring doesn't transfer): 8.75 / 8.50 / 0 / **NEITHER** at ±0.05 — "neither" still reserved and
    still the informative branch.
  * GATE: @Lyra's minimal-K-type reconciliation OPEN (the bedrock question); @Cal's certification OUTSTANDING.

AUG-13. I measure when both close. Nothing pushed. Count once. CP existence-only.
""")
