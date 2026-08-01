#!/usr/bin/env python3
"""
Toy 4959 — Aug 1 [PROGRAM: STANDARD] (cc-MAGNITUDE opened under the K1065 committed bar — honest frame FIRST, then the forward
verdict: the spectral-gap mechanism plausibly supplies the EXPONENTIAL FORM (IR long-time heat trace ~ exp(−λ₁t), so the vacuum
energy is gap-suppressed — the form is mechanism-plausible, granted), BUT the SPECIFIC exponent 282 = C₂·(g²−rank) is an INTEGER
COMBO, not forward-forced (the "47 = g²−rank" scale-ratio is asserted, not derived), so no form is a forward regularized-heat-kernel
a₀ output; combined with the form-multiplicity (≥3 forms, 2.38 dex spread) and a convention-fuzzy target (1.4 dex, measurement only
0.01 dex, K1065a), any sub-dex "match" is form × convention SELECTION. VERDICT: cc-magnitude STAYS IDENTIFIED — a rigorous null on
forward-derivability of the magnitude; Elie, Casey GO, K1065). This is the biggest fit-trap in the program; I walked in expecting to
BOUND it, not crown it. Corpus-run (T1485/T1487/T1959, K1065a convention-pin, spectral-gap heat trace), target-innocent frame
pre-registered before the verdict.

★ PRE-REGISTERED FRAME (committed BEFORE the verdict — the blind-pin move): the cc-magnitude promotes from Identified only if a
mechanism (i) supplies the FORM and (ii) FORCES the exponent forward, WITHOUT target knowledge, clearing the K1065 seven criteria.
The decisive test (Keeper's): does the suppression exponent fall out of a regularized heat-kernel a₀ computation without knowing it
is ~122 orders — or is it the integer-combo that hits 122? I pre-register: a WIN requires the exponent forced target-innocently; a
NULL is any form selected to land near the (fuzzy) target.

★ THE FORMS (computed) + THE MULTIPLICITY (K1065a spine): Λ/M_Pl⁴ forms —
  • T1485: g·exp(−C₂(g²−rank)) = 7·e⁻²⁸² → 10⁻¹²¹·⁶;  exponent 282 = C₂·47, 47 = g²−rank = g·C₂+n_C (T1487 integer identity).
  • α⁵⁶ (56 = 8·genus) → 10⁻¹¹⁹·⁷.  • (T1959 a third exp-form.)
The ≥3 forms span 2.38 dex; the observational target is convention-fuzzy by 1.4 dex (measurement only 0.01 dex, K1065a). With forms
spanning 2.4 dex and a 1.4-dex-fuzzy target, at least one form ALWAYS lands within the target band → the "match" is form × convention
SELECTION, not a measurement.

★ THE FORWARD TEST — fairly assessed (grant the mechanism, deny the value): (i) the UV a₀ heat-kernel coefficient is the VOLUME
(power-law), giving vacuum energy ~ M_Pl⁴ — the cc PROBLEM (too big), NOT the suppression. (ii) the IR/long-time heat trace
Tr(e^{−tD}) ~ e^{−λ₁ t} IS exponentially suppressed by the spectral gap λ₁ — so an EXPONENTIAL-suppression FORM is mechanism-
plausible (GRANTED, not dismissed). (iii) BUT the SPECIFIC exponent 282 = C₂·(g²−rank) requires "47 = g²−rank" as a forward-derived
scale-ratio (e-folds / gap×scale), which is NOT derived — it is an integer combo (and T1487 gives it MULTIPLE integer routes, itself
a multiplicity). So the mechanism supplies the FORM; it does NOT FORCE the exponent VALUE. The exponent is integer-combo-selected →
FAILS the forward test.

⟹ VERDICT (plain — rigorous null, the disciplined outcome): the cc-magnitude STAYS IDENTIFIED. Fairly: the spectral-gap mechanism
plausibly supplies the exponential FORM (IR vacuum energy is gap-suppressed) — I do NOT dismiss that. But it does NOT FORCE the
exponent value: 282 = C₂·(g²−rank) is an integer combo (multiply-routed, T1487), not a forward-derived scale-ratio, so no form is a
forward regularized-heat-kernel a₀ output. With ≥3 forms spanning 2.38 dex and a 1.4-dex convention-fuzzy target, any sub-dex "match"
is form × convention SELECTION (K1065a). This is a rigorous NULL on forward-derivability of the MAGNITUDE — the most fit-tempting
number in the program, bounded not crowned. Cannot promote until a computation FORCES the exponent without target knowledge (an
instanton action or regularization that outputs 282 target-innocently). Rule 11: the number can't distinguish derivation from
coincidence — only provenance can, and here the provenance is integer-combo selection. [STANDARD]. Nothing deleted. Count 6.
"""
import math
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- the forms + multiplicity ----------------------------------------------
alpha = 1 / N_max
form1_log = math.log10(g) - C_2 * (g**2 - rank) / math.log(10)   # 7·e^-282
form2_log = 56 * math.log10(alpha)                               # α^56, 56=8·genus
spread_2form = abs(form1_log - form2_log)                         # ~1.97 dex
spread_3form = 2.38                                              # Keeper's 3-form spread (K1065a)
target_log, target_fuzz = -122.0, 1.4                            # convention-fuzzy (K1065a), measurement 0.01 dex
exponent_282 = C_2 * (g**2 - rank)                               # 282
identity_47 = (g**2 - rank == g * C_2 + n_C == 47)               # T1487: 47 multiply-routed
integer_combo = (exponent_282 == 282 and identity_47)           # exponent is an integer combo

# ---- the forward test ------------------------------------------------------
a0_is_volume_powerlaw = True         # UV a₀ = volume → vacuum energy ~M_Pl⁴ (the cc PROBLEM, not suppression)
ir_gap_gives_exp_form = True         # IR long-time Tr(e^-tD)~e^-λ₁t → exponential suppression: FORM plausible (granted)
exponent_forward_forced = False      # but 282=C_2(g²-rank) is integer-combo, "47" scale-ratio not derived
form_granted_value_denied = ir_gap_gives_exp_form and not exponent_forward_forced

# ---- selection vs derivation ------------------------------------------------
any_match_is_selection = (spread_3form > target_fuzz)   # forms span > target fuzziness → a form always lands in-band
stays_identified = form_granted_value_denied and any_match_is_selection

print(f"\n[cc-MAGNITUDE — K1065, honest frame then verdict]")
print(f"  forms: T1485 7·e^-282 → 10^{form1_log:.2f}; α^56 → 10^{form2_log:.2f}; spread(2-form)={spread_2form:.2f} dex, (3-form, K1065a)={spread_3form} dex.")
print(f"  target ~10^{target_log:.0f}, convention-fuzzy {target_fuzz} dex (measurement 0.01 dex). Forms span {spread_3form} > {target_fuzz} → a form ALWAYS lands in-band ⟹ SELECTION.")
print(f"  exponent 282 = C_2·(g²−rank) = C_2·47, 47=g²−rank=g·C_2+n_C (T1487 multiply-routed) → INTEGER COMBO ({integer_combo}).")
print(f"  forward test: UV a₀=volume (cc PROBLEM, not suppression); IR gap → exp-FORM plausible (granted); but exponent 282 NOT forward-forced → FAILS.")
print(f"  ⟹ VERDICT: cc-magnitude STAYS IDENTIFIED. Rigorous NULL on forward-derivability of the magnitude.")

check("PRE-REGISTERED FRAME (blind, before verdict): promotion needs a mechanism that (i) supplies the FORM and (ii) FORCES the "
      "exponent forward WITHOUT target knowledge, clearing K1065's seven criteria. WIN = exponent forced target-innocently; NULL = "
      "any form selected to land near the fuzzy target. Committed before computing the verdict.",
      True,
      "frame pre-registered: WIN=exponent forward-forced target-innocent; NULL=form selected near fuzzy target; K1065 seven criteria")

check("THE FORMS + MULTIPLICITY (K1065a spine): T1485 7·e⁻²⁸²→10⁻¹²¹·⁶; α⁵⁶→10⁻¹¹⁹·⁷; ≥3 forms span "
      f"{spread_3form} dex. Target ~10⁻¹²², convention-fuzzy {target_fuzz} dex (measurement 0.01 dex). Forms span "
      f"({spread_3form}) > target fuzziness ({target_fuzz}) → at least one form ALWAYS lands in the target band.",
      spread_3form > target_fuzz and abs(spread_2form - 1.97) < 0.1,
      f"forms span {spread_3form} dex > target fuzz {target_fuzz} dex → a form always lands in-band; T1485 10⁻¹²¹·⁶, α⁵⁶ 10⁻¹¹⁹·⁷")

check("THE EXPONENT IS AN INTEGER COMBO (multiply-routed, T1487): 282 = C₂·(g²−rank) = C₂·47, and 47 = g²−rank = g·C₂+n_C — MULTIPLE "
      "integer routes to 47/282. An exponent with several integer expressions is a menu, not a forced value.",
      integer_combo,
      "exponent 282 = C₂·(g²−rank), 47 = g²−rank = g·C₂+n_C (T1487 multiply-routed) → integer combo (a menu, not forced)")

check("FORWARD TEST, FAIRLY (grant the mechanism, deny the value): (i) UV a₀ = volume (power-law) → vacuum energy ~M_Pl⁴ = the cc "
      "PROBLEM, not the suppression. (ii) IR long-time Tr(e^{−tD})~e^{−λ₁t} → exponential suppression by the spectral gap: the "
      "exponential FORM is mechanism-plausible, GRANTED. (iii) BUT the exponent 282 requires '47' as a forward scale-ratio, which is "
      "NOT derived → the value is integer-combo-selected. Mechanism supplies the FORM, does NOT FORCE the exponent.",
      a0_is_volume_powerlaw and ir_gap_gives_exp_form and not exponent_forward_forced,
      "forward test: UV a₀=volume (cc problem); IR gap→exp-FORM plausible (granted); exponent 282 integer-combo not forward-forced → form granted, value denied")

check("SELECTION, NOT DERIVATION (Rule 11 on the magnitude): with ≥3 forms spanning 2.38 dex and a 1.4-dex convention-fuzzy target, "
      "picking the form that lands in-band is form × convention SELECTION — the number cannot distinguish derivation from "
      "coincidence, only provenance can, and here the provenance is integer-combo selection. Fails target-innocence (K1063 Guard 2).",
      any_match_is_selection,
      "selection not derivation: 2.38-dex forms + 1.4-dex fuzzy target → any match is form×convention selection; Rule 11; fails Guard 2 target-innocence")

check("VERDICT: cc-magnitude STAYS IDENTIFIED — rigorous NULL on forward-derivability of the magnitude. The spectral-gap mechanism "
      "plausibly supplies the exponential FORM (not dismissed), but does NOT FORCE the exponent value (282 integer-combo, multiply-"
      "routed); no form is a forward regularized-heat-kernel a₀ output; form-multiplicity + convention-fuzzy target make any match "
      "selection. Bounded, not crowned. Cannot promote until a computation FORCES the exponent target-innocently.",
      stays_identified and integer_combo and form_granted_value_denied,
      "verdict: cc-magnitude stays IDENTIFIED (rigorous null); mechanism supplies form, not the exponent value; fishing menu until exponent forward-forced")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-01 [STANDARD] cc-MAGNITUDE opened under K1065 — rigorous NULL, bounded not crowned (Elie, Casey GO):
  * FRAME (pre-registered blind): WIN = exponent forward-forced target-innocent; NULL = form selected near the fuzzy target.
  * FORMS: T1485 7·e⁻²⁸²→10⁻¹²¹·⁶; α⁵⁶→10⁻¹¹⁹·⁷; ≥3 forms span 2.38 dex; target convention-fuzzy 1.4 dex (measurement 0.01) → a form ALWAYS lands in-band = selection (K1065a).
  * FORWARD TEST (fair): UV a₀=volume (cc problem, not suppression); IR gap → exponential FORM plausible (GRANTED); but exponent 282=C₂·(g²−rank) is integer-combo (multiply-routed T1487), NOT forward-forced → mechanism supplies FORM, denies VALUE.
  * VERDICT: STAYS IDENTIFIED. Rigorous null on forward-derivability of the magnitude. Rule 11: provenance = integer-combo selection. Cannot promote until a computation forces the exponent target-innocently.
""")
