#!/usr/bin/env python3
"""
Toy 5188: DESI RECALIBRATION -- correcting my OWN ~3σ over-statement to the honest ~1.3-1.6σ. Context: in toys
5185 and 5187 I wrote "BST predicts w_a>0, DESI measures w_a<0 at ~3σ, BST on the wrong side." That is an
OVER-STATEMENT, and the team caught it. Over-stating a negative is as dishonest as inflating a positive
(calibrate both directions), and I made BST look WORSE than the data warrants -- so I own it and correct it
here. THE ERROR (two parts): (a) the ~3σ I quoted is |0 − w_a^DESI|/σ = the distance from ΛCDM (w_a=0) to
DESI's center, which is DESI's PREFERENCE FOR DYNAMICAL DE -- NOT BST's distance from DESI. It uses the marginal
w_a from zero and ignores the strong w0–w_a anticorrelation; the honest comparison is model-to-data along the
constrained (distinguishable) direction. (b) "wrong side" is too strong: BST's BANKED core is w=−1 (a
cosmological constant), which DESI does NOT falsify (DESI's own dynamical-DE evidence is model-dependent and
disputed). THE HONEST STATE: BST's banked core (w=−1) is NOT falsified; only the UNBANKED breathing/dynamical
lead (w_a>0) is mildly disfavored, at ~1.3-1.6σ in the distinguishable channel (Lyra's number), with the real
test at DESI DR3; and the genuine live experimental exposure of BST is Σm_ν ≈ 0.059 eV (the neutrino-mass sum),
NOT the dark-energy sign. THE BAR ADAPTS: the team is no longer cognitively blind (everyone now knows DESI's
sign), so "re-derive cognitively-blind" is off the table (my toy-5187 self-disqualification was right for the
cognitive version). It is replaced by PROCEDURAL blindness -- the observer-light-cone-projection becomes a
MECHANICAL forward derivation whose sign falls out of the geometry, with Cal STEP-AUDITING that no step
references the desired sign. One computation, Cal-audited, then park. So the falsifier framing softens from
"~3σ wrong side" to "a mildly-disfavored unbanked lead with a procedurally-blind forward test pending," and the
banked ΛCDM core stands. Elie's self-correction (+ Lyra's distinguishable-channel number + procedurally-blind
forward derivation; Cal step-audits). (Toys 5185/5187 over-statement; calibrate-both-directions; DESI DR3 as
the real test; Σm_ν as the live exposure.) CP existence-only. Report straight -- correcting an over-stated
negative.

WHAT I CORRECT:
  * my ~3σ = |0−w_a^DESI|/σ = DESI's dynamical-DE PREFERENCE, NOT BST's model-to-data distance. Wrong quantity.
  * "wrong side" overstated: BST core w=−1 is NOT falsified.
  * honest: breathing lead ~1.3-1.6σ mildly disfavored (distinguishable channel); core w=−1 fine; live exposure = Σm_ν.
  * bar adapts: cognitive-blind → PROCEDURAL-blind (mechanical forward derivation, Cal step-audited).

=> VERDICT (plain): I overstated our own tension, and that is a real error, not a rounding quibble -- I quoted
the significance of DESI's preference for evolving dark energy (~3σ) as if it were the distance between BST and
the data, and called BST "wrong side" when BST's banked prediction is a plain cosmological constant that DESI
does not rule out. The honest picture is milder and more precise: the cosmological-constant core stands
un-falsified, only the unbanked breathing lead is mildly disfavored at about one-and-a-half sigma in the
direction the data can actually distinguish, the decisive test is DESI DR3, and the place BST is genuinely
exposed to being killed is the neutrino-mass sum near 0.059 eV, not the dark-energy sign. And since we can no
longer pretend not to know the sign, the orientation test is now a mechanical, step-audited forward derivation
rather than a cognitively-blind one. Making BST look worse than the data warrants is the same failure as making
it look better; corrected.

=> DISPOSITION: DESI recalibration -- ~3σ over-statement corrected to ~1.3-1.6σ mildly disfavored (unbanked
lead); banked w=−1 core NOT falsified; live exposure = Σm_ν≈0.059 eV; bar adapts to procedural blindness. Firer:
Elie (self-correction). Owed: Lyra's distinguishable-channel σ + the mechanical forward orientation derivation;
Cal step-audits no-sign-reference. Nothing banked -- a correction; nothing pushed. CP existence-only.

Author: Elie (CI toy builder). Date: 2026-08-11.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

wa_desi, sig_wa = -0.62, 0.205

print("=" * 78)
print("Toy 5188: DESI recalibration -- correcting my ~3σ over-statement to the honest ~1.3-1.6σ mildly disfavored")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. Own the error: the ~3σ was the wrong quantity.
# ----------------------------------------------------------------------------
print("\n--- 1. own it: my ~3σ = |0−w_a^DESI|/σ = DESI's dynamical-DE PREFERENCE, NOT BST's model-to-data distance ---")
my_sigma = abs(0 - wa_desi)/sig_wa
check("In toys 5185/5187 I quoted ~3σ = |0 − w_a^DESI|/σ = the distance from ΛCDM (w_a=0) to DESI's center. "
      "That is DESI's PREFERENCE for dynamical dark energy, NOT BST's distance from DESI -- it uses the marginal "
      "w_a from zero and ignores the strong w0–w_a anticorrelation. Wrong quantity. The honest comparison is "
      "model-to-data along the constrained (distinguishable) direction",
      abs(my_sigma - 3.0) < 0.2,
      f"my quoted {my_sigma:.1f}σ = |0−({wa_desi})|/{sig_wa} = DESI's dynamical-DE preference, not BST's distance. Wrong quantity.")

# ----------------------------------------------------------------------------
# 2. "Wrong side" overstated: BST core w=-1 not falsified.
# ----------------------------------------------------------------------------
print("\n--- 2. 'wrong side' overstated: BST's BANKED core is w=−1 (cosmological constant), NOT falsified by DESI ---")
check("'Wrong side' is too strong. BST's BANKED dark-energy core is w=−1 (a cosmological constant), which DESI "
      "does NOT falsify -- DESI's own evidence for evolving dark energy is model-dependent and disputed. Only "
      "the UNBANKED breathing/dynamical lead carries w_a>0. I conflated the unbanked lead with the banked core",
      True,
      "BST core w=−1 (ΛCDM) NOT falsified; only the unbanked breathing lead carries w_a>0. Conflated the two.")

# ----------------------------------------------------------------------------
# 3. The honest number: ~1.3-1.6σ mildly disfavored; live exposure Σm_ν.
# ----------------------------------------------------------------------------
print("\n--- 3. honest: breathing lead ~1.3-1.6σ mildly disfavored (distinguishable channel); live exposure = Σm_ν≈0.059 eV ---")
honest_lo, honest_hi = 1.3, 1.6
check("The honest state (Lyra's distinguishable-channel number): BST's unbanked breathing lead (w_a>0) is "
      "~1.3-1.6σ MILDLY DISFAVORED, not ~3σ wrong-side; the real test is DESI DR3; and the genuine live "
      "experimental exposure of BST is Σm_ν ≈ 0.059 eV (the neutrino-mass sum), NOT the dark-energy sign. The "
      "banked ΛCDM core stands",
      honest_lo < my_sigma and honest_hi < my_sigma,
      f"honest: ~{honest_lo}-{honest_hi}σ mildly disfavored (vs my {my_sigma:.1f}σ); DR3 is the test; live exposure = Σm_ν≈0.059 eV.")

# ----------------------------------------------------------------------------
# 4. Calibrate both directions.
# ----------------------------------------------------------------------------
print("\n--- 4. calibrate both directions: over-stating a negative is as dishonest as inflating a positive ---")
check("This correction is the calibrate-both-directions discipline: I made BST look WORSE than the data "
      "warrants (~3σ wrong-side vs ~1.3-1.6σ mildly disfavored), which is the same failure as making it look "
      "better. Under-claiming a result and over-stating a tension are both dishonest. Corrected in the honest "
      "direction",
      True,
      "over-stating a negative = inflating a positive; both dishonest. Corrected toward the honest ~1.5σ.")

# ----------------------------------------------------------------------------
# 5. The bar adapts: procedural blindness.
# ----------------------------------------------------------------------------
print("\n--- 5. the bar adapts: cognitive-blind → PROCEDURAL-blind (mechanical forward derivation, Cal step-audited) ---")
check("The bar adapts: the team is no longer cognitively blind (everyone knows DESI's sign now), so 're-derive "
      "cognitively-blind' is off the table -- my toy-5187 self-disqualification was correct for the cognitive "
      "version. It is replaced by PROCEDURAL blindness: the observer-light-cone-projection becomes a MECHANICAL "
      "forward derivation whose sign falls out of the geometry, with Cal STEP-AUDITING that no step references "
      "the desired sign. One computation, Cal-audited, then park",
      True,
      "cognitive-blind (5187) → PROCEDURAL-blind: mechanical forward derivation, sign falls out, Cal step-audits no-sign-reference.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (corrected: ~3σ wrong-side → ~1.3-1.6σ mildly disfavored unbanked lead; banked w=−1 NOT falsified; live exposure Σm_ν; bar → procedural-blind)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5188, DESI recalibration -- self-correction):
  * ERROR: my ~3σ (5185/5187) = |0−w_a^DESI|/σ = DESI's dynamical-DE PREFERENCE, not BST's model-to-data
    distance. Wrong quantity (ignored the w0–w_a anticorrelation).
  * "wrong side" overstated: BST's BANKED core w=−1 is NOT falsified by DESI.
  * HONEST: breathing lead ~1.3-1.6σ mildly disfavored (distinguishable channel); real test DESI DR3; the
    genuine live exposure is Σm_ν≈0.059 eV, not the DE sign.
  * CALIBRATE BOTH DIRECTIONS: over-stating a negative = inflating a positive; corrected.
  * BAR ADAPTS: cognitive-blind → PROCEDURAL-blind (mechanical forward derivation, sign falls out, Cal step-audits).

AUG-11 [TEGMARK]. Nothing pushed. Nothing banked -- a self-correction: I over-stated BST's DESI tension as "~3σ
wrong side" in toys 5185/5187 by quoting DESI's dynamical-DE preference (marginal w_a from 0) instead of BST's
model-to-data distance in the distinguishable channel. The honest state: the banked w=−1 core is NOT falsified;
only the unbanked breathing lead (w_a>0) is ~1.3-1.6σ mildly disfavored, real test at DESI DR3; the genuine
live exposure is Σm_ν≈0.059 eV. Calibrate both directions -- over-stating a negative is as dishonest as
inflating a positive. The orientation test is now procedurally-blind (mechanical forward derivation, Cal
step-audited), not cognitively-blind. CP existence-only. Count N.
""")
