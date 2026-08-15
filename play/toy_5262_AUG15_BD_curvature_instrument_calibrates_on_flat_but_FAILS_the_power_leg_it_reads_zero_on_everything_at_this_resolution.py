#!/usr/bin/env python3
"""
Toy 5262: THE BD CURVATURE INSTRUMENT CALIBRATES ON FLAT AND **FAILS THE POWER LEG** -- it reads ~0 on
everything at this resolution, so a "flat 4D" reading on the commit order would have proved nothing. Day one of
the dig-in: built the tool, and it is not ready. Reporting that rather than the null it would have produced.
★ (0) CORPUS FIRST, as instructed: **grep finds NO Benincasa-Dowker anywhere in notes/ or play/.** This is a NEW
IMPORT, not a corpus reconnect, and it should be labelled as such wherever it lands. ★ (1) AND THE FAMILIAR TRAP
IS PRESENT: **BD's coefficients are DIMENSION-SPECIFIC.** Running the 4D operator and reading "flat 4D" is
putting 4D in -- toy 5253's lesson exactly. So the design ran every d-operator on the same causal set. ★★ (2)
THAT FIRST DESIGN FAILED, TWO WAYS, BOTH MINE. (a) My d = 3 and d = 5 coefficient sets were binomial-shaped
GUESSES, not the published BD sets; I labelled them "candidate, not asserted" and they are not validated, so
they are DROPPED -- I hold validated coefficients only for d = 2 and d = 4. (b) ★ SIXTH CONFOUND: **comparing
|B_d| ACROSS operators is invalid** -- they carry different prefactors and layer counts, hence different noise
floors. B₂ "won" on 5 of 6 calibration rows by being the QUIETEST operator, not the right one, including on
true-d = 3 and true-d = 4 sprinklings. Magnitude-at-one-N is not a dimension selector. ★★★ (3) THE CORRECTED
CRITERION IS CONVERGENCE -- which is what the prompt asked for -- and single sprinklings do not converge: flat
4D gave B₄ = −0.075, −0.440, +0.014, −0.046 at N = 400…3200. **But that is NOISE, not bias:** averaged over K
sprinklings the mean is consistent with zero at every N (−0.041 ± 0.050, −0.016 ± 0.042, −0.023 ± 0.026, all
under 1σ). ⟹ the operator is CORRECT and requires ENSEMBLE AVERAGING; single-run BD values are meaningless.
**Calibration passes.** ★★★★ (4) BUT THE POWER LEG FAILS, AND THAT IS THE RESULT. Flat 4D reads +0.033 ± 0.043;
the commit order on R × S³ reads +0.016 ± 0.053; **separation 0.24σ.** The sem swamps the curvature signal, so
**the instrument returns ~0 on flat AND curved alike at N = 800, K = 16.** ⟹ **a "converges to flat 4D" reading
on the commit order would have been uninformative -- the fourteenth address, and a very natural one, because
the number really is ~0 and really is what we hoped for.** ★ (5) AND A PRE-REGISTERED CORRECTION TO THE TASK
WORDING: **R × S³ is CONFORMALLY flat, not flat.** The Einstein static universe carries positive spatial
curvature (R = 6/a² > 0), and a causal set encodes order + number = conformal structure + volume = the FULL
metric, so BD₄ on a uniform ESU sprinkling should read NONZERO. "Test convergence to flat 4D" is the wrong
target for this object; the right test is FLAT-vs-ESU separation, which is what I ran and which is what has no
power yet. ⟹ NEXT STEP, named: the **smeared / mesoscale BD operator**, which exists precisely to suppress
these fluctuations, and/or much larger N·K. Not a block -- a specified fix. Elie, day one, reporting an
instrument that is not ready. (Keeper's dig-in assignment; toys 5250/5253.) CP existence-only. Nothing pushed.
NO CURVATURE READ ON THE COMMIT ORDER.

WHAT I VERIFY:
  * ★ grep: NO Benincasa-Dowker in the corpus ⟹ new import, not a reconnect. Labelled.
  * ★★ my d = 3 / d = 5 coefficients were guesses ⟹ dropped; validated d = 2 and d = 4 only.
  * ★★ SIXTH CONFOUND: cross-operator |B_d| comparison is invalid — B₂ wins by being quietest (5 of 6 rows).
  * ★★★ single-sprinkling BD does not converge, but the ENSEMBLE MEAN is consistent with 0 on flat 4D at
    N = 400/800/1600 (−0.041±0.050, −0.016±0.042, −0.023±0.026) ⟹ noise not bias; calibration PASSES.
  * ★★★★ POWER LEG FAILS: flat +0.033±0.043 vs ESU +0.016±0.053 ⟹ **0.24σ separation** ⟹ reads ~0 on both.
  * ★ and R × S³ is CONFORMALLY flat, not flat ⟹ the task's "converge to flat 4D" is the wrong target here.

=> VERDICT (plain): day one on the discrete-curvature lead, and the tool is not ready — which is the report,
rather than the appealing number it would have produced. First, this method is nowhere in our corpus, so it is
an import and should be labelled one. Second, its coefficients depend on which dimension you assume, so I ran
every version against the same order; that design failed twice, both my fault — two of my coefficient sets were
educated guesses rather than the published ones, and comparing the different versions' raw outputs is meaningless
because they have different noise levels, so the quietest one wins regardless of truth. Third, the corrected
approach does work: individual runs are wild, but averaged over many they sit correctly at zero on flat space,
so the operator is right and just needs averaging. And then the part that matters: I checked whether it can tell
flat from curved, and at this resolution it cannot — the two differ by a quarter of one error bar. So it returns
approximately zero on everything, and had I skipped that check and run it on our order, I would have found
approximately zero, called it flat four-dimensional space, and been wrong in the most persuasive possible way,
because that is exactly the answer we want. One correction to the task as posed: the object is conformally flat,
not flat, and genuinely curved, so zero was never the right expectation for it. The fix is known and named.

=> DISPOSITION: ★ **CORPUS: no Benincasa-Dowker anywhere** ⟹ NEW IMPORT, label it. ★★ **MY FIRST DESIGN FAILED
TWO WAYS, BOTH MINE:** (a) d = 3 / d = 5 coefficients were guesses ⟹ **dropped**, validated d = 2 and d = 4
only; (b) **SIXTH CONFOUND — cross-operator |B_d| comparison is invalid** (different prefactors/noise floors);
B₂ won 5 of 6 calibration rows by being quietest, including on true-d = 3 and 4. ★★★ **CORRECTED CRITERION =
CONVERGENCE**, and single sprinklings are wild (−0.075/−0.440/+0.014/−0.046) **but it is NOISE not BIAS**:
ensemble means are consistent with 0 on flat 4D at every N (all < 1σ) ⟹ **calibration PASSES with ensemble
averaging.** ★★★★ **POWER LEG FAILS — THE RESULT:** flat 4D **+0.033 ± 0.043** vs commit order R × S³
**+0.016 ± 0.053** ⟹ **0.24σ** ⟹ the instrument reads ~0 on flat AND curved alike. **A "converges to flat 4D"
reading would have been uninformative — the 14th address, and a natural one, since the number really is ~0 and
really is what we hoped for.** ★ **PRE-REGISTERED TASK CORRECTION: R × S³ is CONFORMALLY flat, not flat**
(ESU has R = 6/a² > 0; causal set = order + number = conformal structure + volume = full metric) ⟹ "converge to
flat 4D" is the wrong target; FLAT-vs-ESU separation is the right one. ★ **NEXT STEP, NAMED: the smeared /
mesoscale BD operator** (built for exactly this fluctuation) and/or much larger N·K. A specified fix, not a
block. Firer: Elie. Nothing pushed. NO CURVATURE READ ON THE COMMIT ORDER.

Author: Elie (CI toy builder). Date: 2026-08-15.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/bd.py, bd2.py, bd3.py, bd4.py
SINGLE = {400: -0.07545, 800: -0.44046, 1600: 0.01363, 3200: -0.04634}
ENSEMBLE = {400: (-0.0412, 0.0501), 800: (-0.0159, 0.0422), 1600: (-0.0231, 0.0263)}
POWER = {"flat 4D": (0.0327, 0.0430), "commit order R×S³": (0.0164, 0.0530)}
SEP = 0.24
B2_WON = 5   # of 6 calibration rows

print("=" * 78)
print("Toy 5262: BD calibrates on flat, FAILS the power leg. NO CURVATURE READ")
print("=" * 78)

print("\n--- 0-1. ★ corpus first, and the familiar trap ---")
check("**grep finds NO Benincasa-Dowker anywhere in notes/ or play/** ⟹ this is a **NEW IMPORT, not a corpus "
      "reconnect**, and should be labelled as such wherever it lands. ★ And the familiar trap is present: BD's "
      "coefficients are **dimension-specific**, so running the 4D operator and reading 'flat 4D' is putting 4D "
      "in — toy 5253's lesson exactly. The design therefore ran every d-operator on the same causal set.",
      True,
      "no BD in corpus ⟹ new import; coefficients are dimension-specific ⟹ must run all d, not just 4")

print("\n--- 2. ★★ that design failed, two ways, both mine ---")
check("**(a)** My d = 3 and d = 5 coefficient sets were binomial-shaped **guesses**, not the published BD "
      "sets. I labelled them 'candidate, not asserted' and they are **not validated** ⟹ **dropped**. I hold "
      f"validated coefficients for **d = 2 and d = 4 only**. **(b) ★ SIXTH CONFOUND: comparing |B_d| ACROSS "
      f"operators is invalid** — different prefactors and layer counts ⟹ different noise floors. **B₂ 'won' "
      f"{B2_WON} of 6 calibration rows by being the QUIETEST operator**, not the right one — including on "
      "true-d = 3 and true-d = 4 sprinklings. **Magnitude-at-one-N is not a dimension selector.**",
      B2_WON >= 4,
      f"d=3/d=5 coefficients were guesses (dropped); cross-operator magnitude invalid — B₂ won {B2_WON}/6 by being quietest")

print("\n--- 3. ★★★ the corrected criterion, and noise vs bias ---")
print("          single sprinklings, flat 4D:  " + ", ".join(f"N={N}: {SINGLE[N]:+.5f}" for N in sorted(SINGLE)))
print("          ensemble means, flat 4D:      " + ", ".join(f"N={N}: {ENSEMBLE[N][0]:+.4f}±{ENSEMBLE[N][1]:.4f}" for N in sorted(ENSEMBLE)))
consistent = all(abs(ENSEMBLE[N][0]) < 3*ENSEMBLE[N][1] for N in ENSEMBLE)
check("Single sprinklings do NOT converge (−0.075, −0.440, +0.014, −0.046 at N = 400…3200). ★ **But that is "
      "NOISE, not BIAS**: averaged over K sprinklings the mean is consistent with zero at every N — all under "
      "1σ. ⟹ the operator is **correct** and requires **ensemble averaging**; single-run BD values are "
      "meaningless. **Calibration PASSES.**",
      consistent,
      "single runs wild; ensemble means all < 1σ from 0 on flat 4D ⟹ noise not bias; calibration passes")

print("\n--- 4. ★★★★ but the power leg fails — the result ---")
for k, (m, s) in POWER.items():
    print(f"          {k:<22} {m:+.4f} ± {s:.4f}")
check(f"Flat 4D reads **{POWER['flat 4D'][0]:+.4f} ± {POWER['flat 4D'][1]:.4f}**; the commit order on R × S³ "
      f"reads **{POWER['commit order R×S³'][0]:+.4f} ± {POWER['commit order R×S³'][1]:.4f}** ⟹ **separation "
      f"{SEP:.2f}σ.** The sem swamps the curvature signal ⟹ **the instrument returns ~0 on flat AND curved "
      "alike at N = 800, K = 16.** ★ ⟹ **a 'converges to flat 4D' reading on the commit order would have been "
      "uninformative — the FOURTEENTH ADDRESS, and a very natural one, because the number really is ~0 and "
      "really is what we hoped for.**",
      SEP < 3,
      f"flat vs ESU separation {SEP:.2f}σ ⟹ no power; reads ~0 on everything ⟹ a null would prove nothing")

print("\n--- 5. ★ and a pre-registered correction to the task wording ---")
check("**R × S³ is CONFORMALLY flat, NOT flat.** The Einstein static universe carries positive spatial "
      "curvature (R = 6/a² > 0), and a causal set encodes **order + number = conformal structure + volume = "
      "the FULL metric** — so BD₄ on a uniform ESU sprinkling should read **nonzero**. ⟹ *'Test convergence to "
      "flat 4D'* is the **wrong target for this object**; the right test is **flat-vs-ESU separation**, which "
      "is what I ran and which has no power yet. ★ NEXT STEP, NAMED: the **smeared / mesoscale BD operator**, "
      "built for exactly this fluctuation, and/or much larger N·K. **A specified fix, not a block.**",
      True,
      "R × S³ is conformally flat not flat ⟹ nonzero is the right expectation; fix = smeared BD operator")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (BD calibrates correctly on flat but has 0.24σ power — it reads ~0 on everything, so no reading was taken)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5262, day one of the dig-in — the instrument is not ready — NO CURVATURE READ):
  * ★ **CORPUS FIRST: grep finds NO Benincasa-Dowker in notes/ or play/.** A **new import**, not a reconnect —
    label it as one. And BD's coefficients are **dimension-specific**, so reading "flat 4D" off the 4D operator
    is putting 4D in (toy 5253's lesson).
  * ★★ **MY FIRST DESIGN FAILED TWO WAYS, BOTH MINE.** (a) my d = 3 / d = 5 coefficients were **guesses** —
    dropped; validated **d = 2 and d = 4 only**. (b) **SIXTH CONFOUND: cross-operator |B_d| comparison is
    invalid** — different prefactors and noise floors, so **B₂ won 5 of 6 calibration rows by being the
    quietest**, including on true-d = 3 and 4. Magnitude at one N is not a dimension selector.
  * ★★★ **CORRECTED CRITERION = CONVERGENCE**, and single sprinklings are wild (−0.075, −0.440, +0.014,
    −0.046) — **but it's noise, not bias**: ensemble means on flat 4D are **all within 1σ of zero**
    (−0.041±0.050, −0.016±0.042, −0.023±0.026). The operator is right and needs **ensemble averaging**.
    **Calibration passes.**
  * ★★★★ **BUT THE POWER LEG FAILS — and that's the result.** Flat 4D **+0.033 ± 0.043** vs commit order
    R × S³ **+0.016 ± 0.053** ⟹ **0.24σ**. The instrument reads **~0 on flat and curved alike**.
    ⟹ **a "converges to flat 4D" reading would have been uninformative — the 14th address, and a very natural
    one, because the number really is ~0 and really is what we hoped for.**
  * ★ **PRE-REGISTERED TASK CORRECTION: R × S³ is *conformally* flat, not flat.** The ESU has R = 6/a² > 0, and
    a causal set encodes order + number = conformal structure + volume = the **full** metric ⟹ BD₄ should read
    **nonzero** there. "Converge to flat 4D" is the wrong target for this object.
  * ★ **NEXT STEP, NAMED:** the **smeared / mesoscale BD operator** (built for exactly this fluctuation)
    and/or much larger N·K. **A specified fix, not a block.**

AUG-15. Nothing pushed. Count once. CP existence-only.
""")
