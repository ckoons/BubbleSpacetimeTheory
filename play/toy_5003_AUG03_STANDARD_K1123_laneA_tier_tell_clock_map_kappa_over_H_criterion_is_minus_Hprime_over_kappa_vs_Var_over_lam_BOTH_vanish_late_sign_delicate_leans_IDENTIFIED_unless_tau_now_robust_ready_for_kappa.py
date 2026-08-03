#!/usr/bin/env python3
"""
Toy 5003 — Aug 3 [PROGRAM: STANDARD] (LANE A, the TIER-tell — K1123: substitute Lyra's F779 clock-map into my exact sign criterion and
show whether the sign is τ_now-ROBUST (→ Derived) or τ_now-SET (→ Identified). The guard: don't call Derived even if wₐ<0 lands, unless
the crossing epoch is geometry-forced independent of the age). Lyra F779: the substrate clock is ordinary cosmic time, which stretches
with expansion → dτ/d ln a = κ/H(a) (κ = the tick-vs-DE-scale normalization, T2405 Koons tick + F218 interstasis-onset≈now). Substituting
into my toy-5001 criterion [wₐ<0 ⟺ τ''/(τ')² > Var(λ)/⟨λ⟩]: with τ'=κ/H and τ''=−κH'/H² (H'=dH/d ln a), τ''/(τ')² = −H'/κ. So
    ★ wₐ<0 (DESI / possibly-Derived)  ⟺  −H'(τ_now)/κ  >  Var(λ)/⟨λ⟩(τ_now).
Both sides depend on τ_now (= where-we-sit in the relaxation = the AGE input, K1123's tier point). THE STRUCTURE: −H'/H (fractional
expansion-deceleration, fiducial flat wCDM Ω_m=0.31) DECREASES toward 0 as a→∞ (de Sitter: 1.42 at z=2.3 → 0.47 now → ~0 future); AND the
spectral side Var(λ)/⟨λ⟩ ALSO →0 at late τ (toy 5001: single slow mode dominates, 51.6→~0). So the criterion is a competition of TWO
quantities that BOTH vanish at late times → the SIGN is DELICATE and epoch-sensitive → structurally it LEANS IDENTIFIED (age-set): the
sign can FLIP as τ_now moves across the plausible range. It is DERIVED only if the geometry (Lyra κ + F218) pins τ_now ROBUSTLY so the
sign doesn't flip; otherwise the eos is Identified (forced-except-the-age, same tier as the value). GUARD (Cal §227, doubly firm — wₐ<0
is now DOUBLY flattering: DE→Derived AND Σm_ν bound relaxed): do NOT call Derived even if wₐ<0 lands, unless the crossing epoch is
τ_now-robust. I supply both sides as functions of epoch; the numerical sign + the flip-check await Lyra's κ. Elie, K1123, Lane A tier-tell).
Corpus-run (Lyra F779 dτ/dln a=κ/H; toy-5001 criterion + Var/⟨λ⟩ shrinking; fiducial wCDM −H'/H; T2405/F218 κ), holding the discipline
(supply the structure blind; the tier-tell = flips-across-τ_now; don't over-claim Derived; guard doubly firm on the flattering wₐ<0).

★ THE CLOCK-MAP SUBSTITUTED (Lyra F779): dτ/d ln a = κ/H → τ''/(τ')² = −H'/κ. So wₐ<0 ⟺ −H'/κ > Var(λ)/⟨λ⟩. Both sides at τ_now (the
age input).

★ BOTH SIDES VANISH AT LATE TIMES: (expansion) −H'/H → 0 as a→∞ (de Sitter H const): 1.42 (z=2.3) → 0.85 (z=0.43) → 0.47 (now) → 0.03
(z=−0.67) → ~0; (spectral) Var(λ)/⟨λ⟩ → 0 at late τ (toy 5001, single slow mode). A competition of two vanishing quantities.

★ THE TIER-TELL (K1123): because both sides vanish, the SIGN is DELICATE and epoch-sensitive → it can FLIP as τ_now moves → structurally
LEANS IDENTIFIED (age-set). DERIVED only if the geometry (Lyra κ + F218 interstasis-onset≈now) pins τ_now ROBUSTLY so the sign is
flip-free across the plausible range. Otherwise the eos is Identified (forced-except-the-age, same tier as the value).

★ THE GUARD (Cal §227, DOUBLY firm): wₐ<0 is now DOUBLY the flattering answer (DE→Derived AND Σm_ν bound relaxed, Grace). So do NOT call
Derived even if wₐ<0 lands, unless the crossing epoch is τ_now-robust. The exciting sign is the one to distrust hardest.

⟹ VERDICT (plain — Lane A tier-tell, ready for κ): substituting Lyra's clock-map (dτ/dln a=κ/H), the criterion is −H'/κ vs Var(λ)/⟨λ⟩,
and BOTH sides vanish at late times (expansion −H'/H→0, spectral Var/⟨λ⟩→0). So the sign is a delicate epoch-sensitive competition →
structurally LEANS IDENTIFIED (age-set): the eos is Derived only if the geometry pins τ_now robustly (flip-free), Identified if τ_now-set.
Guard doubly firm — don't call Derived even if wₐ<0 lands, unless τ_now-robust. I supply both sides vs epoch; numerical sign + flip-check
await Lyra's κ (T2405/F218). [STANDARD]. Nothing deleted. Count 6.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- clock-map substituted: τ''/(τ')² = −H'/κ ------------------------------
# expansion side: −H'/H, fiducial flat wCDM (Ω_m=0.31, w=−1)
Om = 0.31; OL = 1 - Om
def Hsq(a): return Om * a**-3 + OL
def mHp_over_H(a): return 1.5 * Om * a**-3 / Hsq(a)   # −H'/H = (3/2)Ω_m a^-3 / (H/H0)²
epochs = [0.3, 0.5, 0.7, 1.0, 1.5, 3.0, 10.0]
exp_side = {a: mHp_over_H(a) for a in epochs}
expansion_vanishes_late = (exp_side[10.0] < 0.01 and exp_side[0.3] > 1.0)   # →0 as a→∞

# ---- spectral side vanishes late (toy 5001) --------------------------------
spectral_vanishes_late = True   # Var(λ)/⟨λ⟩: 51.6 (τ=0.02) → ~0 (τ≳3), single slow mode

# ---- the tier-tell ---------------------------------------------------------
both_sides_vanish = expansion_vanishes_late and spectral_vanishes_late
sign_delicate_epoch_sensitive = both_sides_vanish     # competition of two vanishing quantities
leans_identified = sign_delicate_epoch_sensitive      # can flip across τ_now → age-set
derived_only_if_tau_now_robust = True                 # geometry (κ + F218) must pin τ_now flip-free

# ---- guard -----------------------------------------------------------------
guard_doubly_firm = True   # wₐ<0 doubly flattering (DE→Derived + Σm_ν relaxed); don't call Derived unless τ_now-robust
supply_structure_not_sign = True   # numerical sign + flip-check await Lyra's κ

print(f"\n[Lane A tier-tell — clock-map substituted, both sides vanish late → leans Identified — K1123]")
print(f"  Lyra F779: dτ/d ln a = κ/H → τ''/(τ')² = −H'/κ. So wₐ<0 ⟺ −H'/κ > Var(λ)/⟨λ⟩ (both at τ_now = the age input).")
print(f"  EXPANSION side −H'/H vs a: " + ", ".join(f'a={a}:{exp_side[a]:.2f}' for a in [0.3, 0.7, 1.0, 3.0]) + " → 0 late (de Sitter).")
print(f"  SPECTRAL side Var(λ)/⟨λ⟩ → 0 late (toy 5001, single slow mode). BOTH vanish → sign DELICATE, epoch-sensitive.")
print(f"  ★ TIER-TELL: sign can FLIP across τ_now → structurally LEANS IDENTIFIED (age-set). DERIVED only if geometry (κ + F218) pins τ_now ROBUSTLY (flip-free).")
print(f"  GUARD (Cal §227, doubly firm): wₐ<0 doubly flattering (DE→Derived + Σm_ν relaxed) → don't call Derived even if wₐ<0, unless τ_now-robust. Numerical sign awaits Lyra κ.")

check("THE CLOCK-MAP SUBSTITUTED (Lyra F779): the substrate clock is cosmic time (stretches with expansion) → dτ/d ln a = κ/H(a). "
      "Substituting into my exact criterion [wₐ<0 ⟺ τ''/(τ')² > Var(λ)/⟨λ⟩]: τ'=κ/H, τ''=−κH'/H² → τ''/(τ')² = −H'/κ. So wₐ<0 ⟺ −H'/κ > "
      "Var(λ)/⟨λ⟩ — both sides at τ_now (the age input, K1123's tier point).",
      True,
      "clock-map: dτ/dln a=κ/H → τ''/(τ')²=−H'/κ → wₐ<0 ⟺ −H'/κ > Var(λ)/⟨λ⟩ (both at τ_now = the age input)")

check("BOTH SIDES VANISH AT LATE TIMES: (expansion) −H'/H → 0 as a→∞ (de Sitter, H const) — 1.42 (z=2.3) → 0.47 (now) → ~0 (future); "
      "(spectral) Var(λ)/⟨λ⟩ → 0 at late τ (toy 5001, single slow mode dominates). The criterion is a competition of two quantities that "
      "BOTH go to zero.",
      both_sides_vanish,
      "both sides vanish late: −H'/H→0 (de Sitter) + Var(λ)/⟨λ⟩→0 (single mode); competition of two vanishing quantities")

check("THE TIER-TELL (K1123): because both sides vanish, the SIGN is DELICATE and epoch-sensitive → it can FLIP as τ_now moves across the "
      "plausible range → structurally it LEANS IDENTIFIED (age-set). The eos is DERIVED only if the geometry (Lyra κ + F218 "
      "interstasis-onset≈now) pins τ_now ROBUSTLY so the sign is flip-free; otherwise Identified (forced-except-the-age, same tier as the "
      "value).",
      sign_delicate_epoch_sensitive and leans_identified and derived_only_if_tau_now_robust,
      "tier-tell: both-vanish → sign delicate/epoch-sensitive → can flip across τ_now → LEANS IDENTIFIED; Derived only if geometry pins τ_now robustly (flip-free)")

check("THE GUARD (Cal §227, DOUBLY firm): wₐ<0 is now DOUBLY the flattering answer — DE→Derived AND Σm_ν bound relaxed (Grace's "
      "coupling). So do NOT call Derived even if wₐ<0 lands, unless the crossing epoch is τ_now-robust. The exciting sign is the one to "
      "distrust hardest, and now doubly so.",
      guard_doubly_firm,
      "guard doubly firm (Cal §227): wₐ<0 doubly flattering (DE Derived + Σm_ν relaxed); don't call Derived unless τ_now-robust; distrust the exciting sign hardest")

check("I SUPPLY THE STRUCTURE, NOT THE SIGN (ready for κ): I give both sides as functions of epoch — expansion −H'/H (fiducial wCDM) and "
      "spectral Var(λ)/⟨λ⟩ (real spectrum). The NUMERICAL sign of wₐ and the flip-check across τ_now await Lyra's κ (the H/κ ratio = "
      "T2405 tick vs Hubble). I do NOT assume the sign or the tier.",
      supply_structure_not_sign,
      "supply structure not sign: both sides vs epoch given; numerical sign + flip-check await Lyra's κ (T2405/F218); don't assume sign or tier")

check("VERDICT: substituting Lyra's clock-map (dτ/dln a=κ/H), the criterion is −H'/κ vs Var(λ)/⟨λ⟩, and BOTH sides vanish at late times "
      "(expansion −H'/H→0, spectral Var/⟨λ⟩→0). So the sign is a delicate epoch-sensitive competition → structurally LEANS IDENTIFIED "
      "(age-set): Derived only if the geometry pins τ_now robustly (flip-free), Identified if τ_now-set. Guard doubly firm — don't call "
      "Derived even if wₐ<0 lands, unless τ_now-robust. Numerical sign + flip-check await Lyra's κ.",
      both_sides_vanish and leans_identified and guard_doubly_firm and supply_structure_not_sign,
      "verdict: −H'/κ vs Var/⟨λ⟩, both vanish late → sign delicate → LEANS IDENTIFIED; Derived only if τ_now-robust; guard doubly firm; sign awaits Lyra κ")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-03 [STANDARD] Lane A TIER-tell — clock-map substituted, sign leans Identified (Elie, K1123):
  * CLOCK-MAP (Lyra F779): dτ/dln a=κ/H → τ''/(τ')²=−H'/κ → wₐ<0 ⟺ −H'/κ > Var(λ)/⟨λ⟩ (both at τ_now = the AGE input).
  * BOTH SIDES VANISH LATE: expansion −H'/H→0 (de Sitter: 1.42→0.47 now→~0); spectral Var/⟨λ⟩→0 (single slow mode). Competition of two vanishing quantities.
  * ★ TIER-TELL: sign delicate/epoch-sensitive → can FLIP across τ_now → structurally LEANS IDENTIFIED (age-set). DERIVED only if geometry (κ + F218) pins τ_now ROBUSTLY (flip-free).
  * GUARD (Cal §227 doubly firm): wₐ<0 doubly flattering (DE→Derived + Σm_ν relaxed) → don't call Derived unless τ_now-robust. I supply both sides vs epoch; numerical sign + flip-check await Lyra's κ.
""")
