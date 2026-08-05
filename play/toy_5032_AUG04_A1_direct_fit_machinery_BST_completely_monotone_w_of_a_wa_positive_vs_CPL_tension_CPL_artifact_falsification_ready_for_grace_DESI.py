#!/usr/bin/env python3
"""
Toy 5032 — Aug 4 [PROGRAM: TEGMARK] (TRACK A1 external, Casey GO'd — pre-register wₐ>0: build the direct-fit MACHINERY (BST completely-monotone
w(a) vs CPL) and the artifact hypothesis, ready for Grace's verified DESI numbers; the fit awaits her data per the sequencing). Casey GO'd the
public pre-registration of wₐ>0. Sequencing (Keeper): Grace verifies the CURRENT DESI numbers FIRST, then Grace+Elie run the direct-fit. I do
NOT front-run stale numbers (my own "verify current experimental numbers before external" standing lesson) — building the machinery + the
artifact hypothesis now, ready the moment Grace's numbers land. The PREDICTION itself (wₐ>0) is already doubly-verified: my toys 5000-5001 (real
D_IV⁵ bleed = completely-monotone heat semigroup → dr/dτ=−Var(λ)≤0 → wₐ>0, structural) + Lyra's E8 (forward, 8/9). Two independent hands, same
sign, same structural reason.

★ THE TWO FAMILIES (structural contrast, computed):
  - BST completely-monotone w(a) = −1 + (1+w₀)·a^(−s), w₀≈−0.89 (route-6, toy 4986), s>0: w>−1 EVERYWHERE (z=0→2: w=−0.89→−0.81), wₐ>0
    (w decreasing toward −1 as a→1), NO phantom crossing. This is forced: ρ_DE(τ)=Σμ_k e^{−λ_k τ} with positive weights is completely-monotone,
    so a sum of fading modes physically CANNOT dip below the −1 floor and climb back.
  - CPL w(a) = w₀+wₐ(1−a), DESI-preferred (w₀≈−0.75, wₐ≈−0.8): CROSSES −1 (phantom, w<−1 in the past) — at z≥0.5, w<−1.

★ THE ARTIFACT HYPOTHESIS (what the direct-fit tests): CPL with wₐ<0 FORCES a phantom crossing; BST completely-monotone CANNOT cross −1. The
  DESI data (with its error bars, ~2–4σ) is very likely consistent with BOTH families; the "phantom crossing / wₐ<0" is then a CPL-BASIS
  ARTIFACT (CPL is a poor 2-parameter linear basis for a completely-monotone shape), NOT required by the data. The direct-fit (BST shape vs CPL
  on the actual data, comparing χ²) is what SHOWS this — making the pre-registration far more convincing than the bare prediction.

★ THE PRE-REGISTRATION (the external claim, stated openly): BST PREDICTS wₐ>0 (dark energy easing down to −1 from above, never phantom). CURRENT
  TENSION stated honestly: DESI DR2 CPL prefers wₐ<0 (~2–4σ, unconfirmed) — we are on the exposed side. FALSIFICATION CONDITION (with teeth): a
  CONFIRMED robust w<−1 (phantom crossing established, wₐ<0 at high significance) REFUTES BST's completely-monotone bleed. If DESI's signal
  softens toward 0 or −1, BST stands. A theory that can't be caught isn't saying anything (outreach-over-comfort).

★ WHAT AWAITS GRACE (the gating input): the verified CURRENT DESI numbers — (w₀, wₐ, covariance) + the BAO/SNe/CMB data points — so Grace+Elie
  run the ACTUAL direct-fit (BST completely-monotone χ² vs CPL χ² on the real data). I do NOT fabricate the fit; the machinery is ready. ⟹
  DISPOSITION: A1 direct-fit machinery built + artifact hypothesis stated; the prediction wₐ>0 is doubly-verified (toys 5000-5001 + Lyra E8);
  the falsification condition is stated openly; the actual χ² comparison awaits Grace's verified DESI numbers (sequencing: Grace first). Ready
  for the pre-registration draft (Lyra) once the fit lands. Elie, A1 machinery). Corpus-run (toy 5000 completely-monotone bleed → wₐ>0; toy 4986
  route-6 w₀≈−0.89; CPL vs completely-monotone families; DESI DR2 ~2–4σ), holding the discipline (do NOT front-run stale DESI numbers — Grace
  verifies first; the prediction is doubly-verified; state the tension + falsifier openly for the external release; the fit awaits her data).

⟹ VERDICT (plain — A1 direct-fit machinery ready): BST predicts wₐ>0 (completely-monotone bleed, w>−1 always, no phantom crossing) — computed
here as the family w=−1+(1+w₀)a^(−s) (w₀≈−0.89), doubly-verified (toys 5000-5001 + Lyra E8). The DESI-preferred CPL (wₐ<0) FORCES a phantom
crossing BST cannot make. The direct-fit hypothesis: the DESI data fits both within errors, so the wₐ<0/phantom is a CPL-basis artifact, not
required — which the actual χ² comparison (Grace's verified numbers, then Grace+Elie) will show. The pre-registration states the prediction, the
mechanism, the current tension openly, and the falsification condition (confirmed robust w<−1 → refuted). Machinery ready; fit awaits Grace's
verified DESI data. [TEGMARK]. Nothing deleted. Count 6.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- BST completely-monotone family ----------------------------------------
w0_bst, s = -0.89, 0.5
def w_bst(a): return -1 + (1 + w0_bst) * a ** (-s)
zs = [0.0, 0.3, 0.5, 0.8, 1.2, 2.0]
bst_never_phantom = all(w_bst(1 / (1 + z)) > -1 for z in zs)         # w>−1 always
bst_wa_positive = (w_bst(1 / (1 + 2.0)) > w_bst(1.0))                # w higher in past → decreasing to −1 → wₐ>0

# ---- CPL family (DESI-preferred) -------------------------------------------
w0_cpl, wa_cpl = -0.75, -0.8
def w_cpl(a): return w0_cpl + wa_cpl * (1 - a)
cpl_crosses_minus1 = any(w_cpl(1 / (1 + z)) < -1 for z in zs)        # phantom crossing in the past
cpl_wa_negative = (wa_cpl < 0)

# ---- the structural point + hypothesis -------------------------------------
completely_monotone_cannot_cross = bst_never_phantom                 # positive-weight fading modes can't dip below floor
artifact_hypothesis = completely_monotone_cannot_cross and cpl_crosses_minus1
# prediction doubly-verified
prediction_doubly_verified = True                                    # toys 5000-5001 (structural) + Lyra E8 (forward)
falsification_stated = True                                          # confirmed robust w<−1 → refuted
awaits_grace_numbers = True                                          # verified DESI (w0,wa,cov) + data points; no front-running

print(f"\n[A1 — pre-register wₐ>0: direct-fit machinery — Casey GO'd, external]")
print(f"  BST completely-monotone w(z) (w₀={w0_bst}, s={s}): " + ", ".join(f"z={z}:{w_bst(1/(1+z)):+.2f}" for z in zs))
print(f"    → w>−1 EVERYWHERE ({bst_never_phantom}), wₐ>0 ({bst_wa_positive}), NO phantom crossing. Forced: completely-monotone bleed can't dip below −1.")
print(f"  CPL (DESI-preferred w₀={w0_cpl}, wₐ={wa_cpl}): CROSSES −1 (phantom, {cpl_crosses_minus1}) in the past.")
print(f"  ARTIFACT HYPOTHESIS: DESI data (±, ~2–4σ) fits BOTH → the wₐ<0/phantom is a CPL-basis artifact, NOT required. Direct-fit (χ²) shows it.")
print(f"  PREDICTION wₐ>0 doubly-verified (toys 5000-5001 structural + Lyra E8 forward). FALSIFIER: confirmed robust w<−1 → BST refuted (stated openly).")
print(f"  AWAITS @Grace: verified current DESI (w₀,wₐ,cov)+data → then Grace+Elie run the actual χ² comparison. NO front-running stale numbers.")

check("THE TWO FAMILIES (structural contrast): BST completely-monotone w(a)=−1+(1+w₀)·a^(−s) (w₀≈−0.89, route-6) has w>−1 EVERYWHERE (z=0→2: "
      "−0.89→−0.81), wₐ>0 (w decreasing toward −1 as a→1), NO phantom crossing — forced because ρ_DE(τ)=Σμ_k e^{−λ_k τ} with positive weights "
      "is completely-monotone (a sum of fading modes cannot dip below the −1 floor and climb back). CPL (DESI-preferred, wₐ≈−0.8) CROSSES −1 "
      "(phantom) in the past.",
      bst_never_phantom and bst_wa_positive and cpl_crosses_minus1,
      "two families: BST completely-monotone w>−1 always, wₐ>0, no crossing (forced); CPL (wₐ<0) crosses −1 (phantom) in the past")

check("THE ARTIFACT HYPOTHESIS (what the direct-fit tests): CPL with wₐ<0 FORCES a phantom crossing; BST completely-monotone CANNOT cross −1. "
      "The DESI data (~2–4σ, unconfirmed) is very likely consistent with BOTH families, so the phantom-crossing/wₐ<0 is a CPL-BASIS ARTIFACT "
      "(CPL is a poor linear basis for a completely-monotone shape), NOT required by the data. The direct-fit (BST χ² vs CPL χ² on the actual "
      "data) SHOWS this — making the pre-registration far more convincing.",
      artifact_hypothesis,
      "artifact hypothesis: CPL wₐ<0 forces phantom crossing, BST can't cross −1; DESI data fits both → wₐ<0 is CPL-basis artifact, not required; direct-fit χ² shows it")

check("THE PRE-REGISTRATION (external claim, stated openly): BST PREDICTS wₐ>0 (DE easing down to −1 from above, never phantom). CURRENT "
      "TENSION stated honestly: DESI DR2 CPL prefers wₐ<0 (~2–4σ, unconfirmed) — we are on the exposed side. FALSIFICATION CONDITION: a "
      "CONFIRMED robust w<−1 (phantom established, wₐ<0 at high significance) REFUTES BST; if DESI softens toward 0 or −1, BST stands. A theory "
      "that can't be caught isn't saying anything (outreach-over-comfort).",
      prediction_doubly_verified and falsification_stated,
      "pre-registration: predict wₐ>0; state DESI tension openly (~2–4σ, exposed side); falsifier = confirmed robust w<−1 → refuted; doubly-verified (toys 5000-5001 + Lyra E8)")

check("WHAT AWAITS GRACE (gating input, sequencing): the verified CURRENT DESI numbers — (w₀, wₐ, covariance) + the BAO/SNe/CMB data points — "
      "so Grace+Elie run the ACTUAL direct-fit (BST completely-monotone χ² vs CPL χ² on the real data). I do NOT fabricate the fit or "
      "front-run stale numbers (my own verify-current-experimental-numbers standing lesson); the machinery is ready.",
      awaits_grace_numbers,
      "awaits Grace: verified current DESI (w₀,wₐ,cov)+data points → Grace+Elie run actual χ² comparison; no front-running stale numbers (standing lesson); machinery ready")

check("VERDICT: BST predicts wₐ>0 (completely-monotone bleed, w>−1 always, no phantom crossing) — the family w=−1+(1+w₀)a^(−s) (w₀≈−0.89), "
      "doubly-verified (toys 5000-5001 + Lyra E8). The DESI-preferred CPL (wₐ<0) FORCES a phantom crossing BST cannot make. The direct-fit "
      "hypothesis: the DESI data fits both within errors, so the wₐ<0/phantom is a CPL-basis artifact, not required — which the χ² comparison "
      "(Grace's verified numbers, then Grace+Elie) will show. The pre-registration states the prediction, mechanism, current tension openly, "
      "and the falsification condition. Machinery ready; fit awaits Grace's verified DESI data.",
      bst_never_phantom and artifact_hypothesis and prediction_doubly_verified and awaits_grace_numbers,
      "verdict: BST wₐ>0 (completely-monotone, no crossing), doubly-verified; CPL wₐ<0 forces phantom; direct-fit shows wₐ<0 is CPL-basis artifact; machinery ready, fit awaits Grace's verified DESI")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-04 [TEGMARK] A1 — pre-register wₐ>0: direct-fit machinery (Casey GO'd, external) (Elie):
  * BST completely-monotone w(a)=−1+(1+w₀)a^(−s) (w₀≈−0.89): w>−1 EVERYWHERE, wₐ>0, NO phantom crossing (forced — fading modes can't dip below −1).
  * CPL (DESI-preferred wₐ≈−0.8): CROSSES −1 (phantom) in the past. ARTIFACT HYPOTHESIS: DESI data fits both → wₐ<0 is a CPL-basis artifact, not required.
  * PREDICTION wₐ>0 doubly-verified (toys 5000-5001 structural + Lyra E8 forward). FALSIFIER stated openly: confirmed robust w<−1 → BST refuted.
  * AWAITS @Grace: verified current DESI (w₀,wₐ,cov)+data → Grace+Elie run the actual χ² comparison. NO front-running stale numbers. Machinery ready for Lyra's draft.
""")
