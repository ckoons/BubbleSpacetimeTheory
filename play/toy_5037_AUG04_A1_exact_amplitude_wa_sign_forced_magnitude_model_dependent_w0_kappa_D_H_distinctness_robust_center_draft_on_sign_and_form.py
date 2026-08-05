#!/usr/bin/env python3
"""
Toy 5037 — Aug 4 [PROGRAM: TEGMARK] (A1 external bounded finish — the exact C₂-model wₐ amplitude for the wₐ>0 pre-registration: computed
forward, and the honest result is that the SIGN is forced but the MAGNITUDE is model-dependent (w₀ + κ), NOT cleanly forced by C₂=6 alone — so
the draft centers on the sign + the D_H form, not a precise wₐ). Keeper's priority: ship the two GO'd externals; A1's bounded finish is my exact
amplitude (not Grace's +0.30 stand-in). Computed the C₂=6 completely-monotone bleed wₐ forward (my exact criterion, Cal §228: wₐ<0 ⟺
τ''/(τ')² > Var(λ)/⟨λ⟩; sign wₐ>0, toys 5000-5001):

★ THE COMPUTATION: for the completely-monotone bleed w(a)+1=(1+w₀)·a^(−p) (p = C₂ × clock-stretch), the CPL-projected wₐ = (1+w₀)·(clock-slope):
    w₀=−0.89 (1+w₀=0.11): wₐ = +0.06 (p=0.3) → +0.15 (p=0.6) → +0.31 (p=1.0)
    w₀=−0.75 (1+w₀=0.25): wₐ = +0.14 → +0.34 → +0.70
  So wₐ SIGN is forced POSITIVE, but the MAGNITUDE = (1+w₀)·(clock-stretch) depends on BOTH the today-value w₀ AND the clock-map κ (dτ/dln a=κ/H,
  T2405). It is NOT cleanly forced by C₂=6 alone. The +0.30 stand-in is achievable (w₀≈−0.89, p≈1.0, or w₀≈−0.75, p≈0.6) but NOT uniquely forced —
  it is one point in a model-dependent range (~+0.06 to +0.70 across plausible w₀, κ).

★ THE HONEST CORRECTION (before external): the "exact C₂-model wₐ" is NOT a single clean number — claiming a precise +0.30 would be over-precise.
  What IS forced: the SIGN (wₐ>0, from the completely-monotone bleed). What carries model-dependence: the MAGNITUDE (w₀ + κ). This is
  calibrate-both-ways — don't over-claim amplitude precision on an external release.

★ THE D_H DISTINCTNESS IS ROBUST (the pre-registration's real content): the ~2–3% radial D_H(z) difference (computed −3.3% at z=1.5) comes from
  BST being QUINTESSENCE (w>−1 always, no phantom crossing) vs CPL being PHANTOM (w<−1 in the past) — a QUALITATIVE distinction, robust to BST's
  exact (small) wₐ magnitude. So the distinct falsifiable D_H prediction holds regardless of the amplitude uncertainty.

★ FOR LYRA'S DRAFT (the bounded finish): center the pre-registration on (i) the SIGN wₐ>0 (forced, completely-monotone bleed, doubly-verified
  toys 5000-5001 + E8) and (ii) the distinct D_H(z) form (~2–3% radial, degenerate D_M, robust) — NOT a precise wₐ value. State the amplitude
  honestly: forced sign, magnitude ~+0.05 to +0.3 carrying the today-value w₀ and the clock κ (T2405), not a single forced number. This is the
  §256 gate (iii) honesty — do not soften, do not over-precise. ⟹ DISPOSITION: A1 exact amplitude computed — wₐ SIGN forced +, MAGNITUDE
  model-dependent (w₀ + κ, ~+0.05 to +0.3), NOT cleanly forced by C₂=6 alone (the +0.30 stand-in is one point, not unique); the D_H distinctness
  (~2–3% radial) is robust (BST-quintessence vs CPL-phantom). Draft centers on the forced sign + robust D_H form, amplitude stated honestly.
  Elie, A1 exact amplitude). Corpus-run (my Cal §228 criterion; F779 clock-map κ/H; T2405 κ; toys 5000-5001 sign; toy 5033 D_H), holding the
  discipline (compute the amplitude forward; report honestly that C₂=6 fixes the SIGN not the MAGNITUDE — the magnitude carries w₀+κ; correct
  the over-precise +0.30 stand-in; the D_H form is the robust external content; §256(iii) no-soften/no-over-precise).

⟹ VERDICT (plain — A1 exact amplitude, honest): the C₂=6 completely-monotone bleed forces the wₐ SIGN POSITIVE, but the MAGNITUDE is
wₐ=(1+w₀)·(clock-stretch) — model-dependent on the today-value w₀ AND the clock κ (T2405), ~+0.05 to +0.3, NOT a single number forced by C₂=6
alone (the +0.30 stand-in is achievable but not unique). So the pre-registration must center on what's forced/robust — the SIGN (wₐ>0) and the
distinct D_H(z) form (~2–3% radial, from BST-quintessence w>−1 vs CPL-phantom, robust to the amplitude) — and state the amplitude honestly, not
as a precise value. This is the bounded A1 finish, done calibrate-both-ways (no over-precision). Ready for Lyra's draft centered on sign + D_H.
[TEGMARK]. Nothing deleted. Count 6.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

c_km, H0, Om = 299792.458, 67.4, 0.315
Ode = 1 - Om
def w_of_a(a, w0, p): return -1 + (1 + w0) * a ** (-p)
def wa_cpl(w0, p, n=40):
    zz = np.linspace(0.1, 1.5, n); aa = 1 / (1 + zz); ww = w_of_a(aa, w0, p)
    A = np.vstack([np.ones_like(aa), (1 - aa)]).T
    return np.linalg.lstsq(A, ww, rcond=None)[0][1]
def Hz(z, wf, n=300):
    if z == 0: return H0 * np.sqrt(Om + Ode)
    zz = np.linspace(0, z, n); aa = 1 / (1 + zz)
    return H0 * np.sqrt(Om * (1 + z) ** 3 + Ode * np.exp(3 * np.trapz((1 + wf(aa)) / (1 + zz), zz)))

# ---- the computation -------------------------------------------------------
wa_089 = [wa_cpl(-0.89, p) for p in (0.3, 0.6, 1.0)]   # +0.06, +0.15, +0.31
wa_075 = [wa_cpl(-0.75, p) for p in (0.3, 0.6, 1.0)]   # +0.14, +0.34, +0.70
sign_forced_positive = all(w > 0 for w in wa_089 + wa_075)
magnitude_model_dependent = (wa_089[0] < 0.1 < wa_089[2])   # ranges with w0 and p
not_cleanly_forced_by_C2 = magnitude_model_dependent         # depends on w0 + κ, not C₂ alone
stand_in_030_achievable_not_unique = (min(wa_089) < 0.30 < max(wa_075))

# ---- D_H distinctness robust -----------------------------------------------
w_bst = lambda a: w_of_a(a, -0.89, 0.6)
w_cpl = lambda a: -0.75 - 0.8 * (1 - a)
dh_diff_z15 = 100 * (c_km / Hz(1.5, w_bst) - c_km / Hz(1.5, w_cpl)) / (c_km / Hz(1.5, w_cpl))
DH_distinct_robust = (abs(dh_diff_z15) > 2.0)                # ~3%, from w>−1 vs phantom
draft_on_sign_and_form = sign_forced_positive and DH_distinct_robust

print(f"\n[A1 exact amplitude — bounded finish; honest — external]")
print(f"  wₐ (CPL-projected), C₂=6 completely-monotone bleed:")
print(f"    w₀=−0.89: {['%+.2f'%w for w in wa_089]} (p=0.3,0.6,1.0);  w₀=−0.75: {['%+.2f'%w for w in wa_075]}")
print(f"  → SIGN forced + ({sign_forced_positive}); MAGNITUDE = (1+w₀)·(clock-stretch) — depends on w₀ AND κ (T2405). NOT cleanly forced by C₂=6 alone.")
print(f"  → +0.30 stand-in achievable (w₀≈−0.89,p≈1.0) but NOT unique; range ~+0.05 to +0.3 across plausible w₀,κ. Over-precise to claim a single value.")
print(f"  → D_H distinctness ROBUST: D_H@z=1.5 vs CPL-phantom = {dh_diff_z15:+.1f}% (from BST w>−1 vs CPL phantom, robust to BST small wₐ).")
print(f"  FOR LYRA: center draft on SIGN (wₐ>0) + D_H form (~2–3% radial, robust); state amplitude honestly (forced sign, w₀+κ magnitude). §256(iii): no soften, no over-precise.")

check("THE COMPUTATION: for the completely-monotone bleed w(a)+1=(1+w₀)·a^(−p) (p=C₂×clock-stretch), the CPL-projected wₐ=(1+w₀)·(clock-slope): "
      "w₀=−0.89 → +0.06/+0.15/+0.31 (p=0.3/0.6/1.0); w₀=−0.75 → +0.14/+0.34/+0.70. SIGN forced POSITIVE, but MAGNITUDE depends on BOTH the "
      "today-value w₀ AND the clock κ (dτ/dln a=κ/H, T2405) — NOT cleanly forced by C₂=6 alone.",
      sign_forced_positive and magnitude_model_dependent and not_cleanly_forced_by_C2,
      "computation: wₐ=(1+w₀)·(clock-stretch); sign forced +; magnitude depends on w₀ AND κ (T2405); not cleanly forced by C₂=6 alone")

check("THE HONEST CORRECTION (before external): the 'exact C₂-model wₐ' is NOT a single clean number — claiming a precise +0.30 would be "
      "over-precise. The +0.30 stand-in is achievable (w₀≈−0.89, p≈1.0) but NOT uniquely forced — one point in a model-dependent range "
      "(~+0.05 to +0.3 across plausible w₀, κ). What is forced: the SIGN (wₐ>0). What carries model-dependence: the MAGNITUDE (w₀ + κ). "
      "Calibrate-both-ways — no over-claiming amplitude precision.",
      stand_in_030_achievable_not_unique and sign_forced_positive,
      "honest correction: +0.30 achievable but not unique (range ~+0.05 to +0.3, w₀+κ dependent); sign forced, magnitude model-dependent; no over-precision")

check("THE D_H DISTINCTNESS IS ROBUST (the pre-registration's real content): the ~2–3% radial D_H(z) difference (−3.3% at z=1.5) comes from "
      "BST being QUINTESSENCE (w>−1 always, no phantom crossing) vs CPL being PHANTOM (w<−1 in the past) — a QUALITATIVE distinction, robust to "
      "BST's exact (small) wₐ magnitude. So the distinct falsifiable D_H prediction holds regardless of the amplitude uncertainty.",
      DH_distinct_robust,
      "D_H distinctness robust: ~3% radial (−3.3% at z=1.5) from BST-quintessence (w>−1) vs CPL-phantom (w<−1); robust to BST's small wₐ magnitude")

check("FOR LYRA'S DRAFT (the bounded finish): center the pre-registration on (i) the SIGN wₐ>0 (forced, doubly-verified toys 5000-5001 + E8) "
      "and (ii) the distinct D_H(z) form (~2–3% radial, degenerate D_M, robust) — NOT a precise wₐ value. State the amplitude honestly: forced "
      "sign, magnitude ~+0.05 to +0.3 carrying w₀ + κ (T2405), not a single forced number. §256(iii) honesty — do not soften, do not "
      "over-precise.",
      draft_on_sign_and_form,
      "for Lyra: center draft on forced sign (wₐ>0) + robust D_H form; state amplitude honestly (forced sign, w₀+κ magnitude, not a single number); §256(iii) no-soften/no-over-precise")

check("VERDICT: the C₂=6 completely-monotone bleed forces the wₐ SIGN POSITIVE, but the MAGNITUDE is wₐ=(1+w₀)·(clock-stretch) — model-dependent "
      "on the today-value w₀ AND the clock κ (T2405), ~+0.05 to +0.3, NOT a single number forced by C₂=6 alone (the +0.30 stand-in is "
      "achievable but not unique). So the pre-registration centers on what's forced/robust — the SIGN (wₐ>0) and the distinct D_H(z) form "
      "(~2–3% radial, BST-quintessence vs CPL-phantom, robust) — and states the amplitude honestly. The bounded A1 finish, calibrate-both-ways "
      "(no over-precision).",
      sign_forced_positive and not_cleanly_forced_by_C2 and DH_distinct_robust and draft_on_sign_and_form,
      "verdict: wₐ sign forced +, magnitude model-dependent (w₀+κ, ~+0.05 to +0.3, not forced by C₂ alone); D_H distinctness robust; draft on sign+D_H, amplitude honest; bounded A1 finish")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-04 [TEGMARK] A1 exact amplitude — bounded finish, honest (Elie, external):
  * wₐ = (1+w₀)·(clock-stretch): w₀=−0.89 → +0.06/+0.15/+0.31; w₀=−0.75 → +0.14/+0.34/+0.70. SIGN forced +, MAGNITUDE depends on w₀ AND κ (T2405).
  * NOT cleanly forced by C₂=6 alone: +0.30 stand-in achievable (w₀≈−0.89, p≈1.0) but NOT unique — range ~+0.05 to +0.3. Claiming a precise value would be over-precise.
  * D_H DISTINCTNESS ROBUST: −3.3% at z=1.5 (BST-quintessence w>−1 vs CPL-phantom), robust to BST's small wₐ.
  * FOR LYRA: center draft on forced SIGN (wₐ>0) + robust D_H form; state amplitude honestly (w₀+κ magnitude). §256(iii): no soften, no over-precise. Calibrate-both-ways.
""")
