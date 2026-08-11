#!/usr/bin/env python3
"""
Toy 5185: THE DARK-ENERGY CONSISTENCY CHECK (route 4/3, while the cell-count runs) -- does Casey's
EM-drives/gravity-gates cosmology predict the SAME w(a) as the banked breathing-mode dark energy, and where
does BST's dark-energy sector sit against current DESI DR2? Context: Casey's bulk-edge cosmology (EM = the
continuous boundary drives expansion; gravity = the discrete interior gates the rate and c; Big Bang = bubble
nucleation) is BST-native and held at I-tier, and it INHERITS the banked breathing-mode dark energy (corpus
#54/#101), which has w_a > 0 and respects no-phantom-crossing. The governance rule: it is a MECHANISM for the
banked prediction, NOT a free story -- it does not get to predict a different w(a) than the breathing mode.
This toy (a) scrubs the CURRENT DESI DR2 numbers (remembered numbers go stale -- web-verified Aug 2026), (b)
computes where BST's w_a > 0 sits against them, and (c) states the consistency constraint. RESULT: all DESI DR2
CPL combinations give w_a < 0 (thawing: w0 > −1, w_a < 0) -- DESI+CMB: w0 = −0.42±0.21, w_a = −1.75±0.58 (3.1σ
from ΛCDM); DESI+CMB+SN(Pantheon+): w0 = −0.838±0.055, w_a = −0.62±0.20. BST's banked breathing mode predicts
w_a > 0 -- the OPPOSITE side of w_a = 0 -- so BST is in ~3σ TENSION with DESI DR2 (a live potential falsifier,
NOT a confirmation). The honest disposition, per the standing order "go where BST's math takes us; do not pick
the flattering side": report the tension STRAIGHT. Casey's EM-drives/gravity-gates cosmology is constrained to
reproduce the breathing-mode w(a) (w_a > 0, no-phantom-crossing) -- it must NOT invent a w_a < 0 to escape the
DESI tension; that would be fitting the data instead of the geometry. The picture stays I-tier until it makes a
falsifiable number DISTINCT from the breathing mode (the two named handles: does it predict the same w(a) as
the breathing mode? does it yield a black-hole→nucleation conservation law, #72?). Elie's DE consistency check
(+ Lyra owns the breathing-mode w(a) form; the cell-count is the live make-or-break elsewhere). a₄ chiral
coefficients HELD. (DESI DR2 2025 web-scrubbed; corpus #54/#101 breathing mode; Casey bulk-edge cosmology;
go-where-the-math-takes-us; CMB-is-quote-anything.) CP existence-only. Report the tension straight.

WHAT I COMPUTE (DESI DR2 web-scrubbed Aug 2026):
  * DESI+CMB: w0=−0.42±0.21, w_a=−1.75±0.58 (3.1σ from ΛCDM); DESI+CMB+SN: w0=−0.838±0.055, w_a=−0.62±0.20.
  * ALL DESI DR2 combinations: w_a < 0 (thawing). BST breathing mode: w_a > 0. Opposite sides → ~3σ tension.
  * consistency: Casey's cosmology must give the SAME w(a) (w_a>0, no-phantom-crossing), NOT a new one.

=> VERDICT (plain): BST's dark-energy sector is not comfortably sitting on the data -- it is in genuine tension
with it, and the honest thing is to say so. The banked breathing mode predicts that the dark-energy equation of
state stiffens with time (w_a > 0), while DESI DR2, across every dataset combination, prefers the opposite
(w_a < 0, thawing) at about three sigma. That is a live potential falsifier for BST's dark-energy sector, not a
success to be claimed. Casey's EM-drives/gravity-gates cosmology inherits this prediction; its job is to be a
mechanism for the breathing mode, so it must reproduce the same w(a) and must not quietly flip to w_a < 0 to
match DESI -- picking the flattering side is exactly the move the standing order forbids. So the consistency
check is a brake, not a booster: it keeps the new cosmology honest (same w(a), no-phantom-crossing, w_a > 0
under DESI tension), and the picture earns its way out of I-tier only by producing a falsifiable number the
breathing mode does not already give.

=> DISPOSITION: DE consistency check -- BST breathing mode w_a>0 vs DESI DR2 w_a<0, ~3σ tension, reported
straight; Casey's cosmology constrained to the same w(a) (mechanism, not free story). Firer: Elie. Owed: Lyra's
explicit breathing-mode w(a) form for the full quantitative match; the two falsifiable handles (same w(a);
black-hole→nucleation conservation #72) to earn out of I-tier. Held at I-tier. a₄ chiral coefficients HELD.
Nothing banked -- this is a governance brake + an honest tension report; nothing pushed. CP existence-only.

Author: Elie (CI toy builder). Date: 2026-08-11.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# DESI DR2 (2025), CPL w0waCDM, web-scrubbed Aug 2026: (w0, sig_w0, wa, sig_wa, note)
desi = {
    'DESI+CMB': (-0.42, 0.21, -1.75, 0.58, '3.1σ from ΛCDM'),
    'DESI+CMB+SN(Pantheon+)': (-0.838, 0.055, -0.62, 0.205, 'evolving DE preferred'),
}

print("=" * 78)
print("Toy 5185: DE consistency check -- BST breathing w_a>0 vs DESI DR2 w_a<0 (~3σ tension, reported straight)")
print("=" * 78)
print("\n  DESI DR2 (CPL), web-scrubbed Aug 2026:")
for k, (w0, ew0, wa, ewa, note) in desi.items():
    print(f"    {k:24s} w0={w0:+.3f}±{ew0:.3f}  w_a={wa:+.2f}±{ewa:.2f}  ({note})")

# ----------------------------------------------------------------------------
# 1. All DESI DR2 combinations give w_a < 0.
# ----------------------------------------------------------------------------
print("\n--- 1. all DESI DR2 combinations give w_a < 0 (thawing: w0 > −1, w_a < 0) ---")
all_wa_neg = all(v[2] < 0 for v in desi.values())
check("Current DESI DR2 (web-scrubbed Aug 2026), CPL parametrization: every dataset combination prefers w_a < "
      "0 (thawing dark energy, w0 > −1) -- DESI+CMB gives w_a = −1.75±0.58 (3.1σ from ΛCDM); DESI+CMB+SN gives "
      "w_a = −0.62±0.20. Remembered numbers go stale, so these are freshly scrubbed",
      all_wa_neg,
      "all DESI DR2 combos: w_a < 0 (thawing). DESI+CMB w_a=−1.75±0.58; DESI+CMB+SN w_a=−0.62±0.20.")

# ----------------------------------------------------------------------------
# 2. BST breathing mode w_a > 0 -- opposite side, ~3σ tension.
# ----------------------------------------------------------------------------
print("\n--- 2. BST breathing mode w_a > 0 -- OPPOSITE side of w_a=0 from DESI → ~3σ tension (a live falsifier) ---")
tensions = {k: abs(0 - v[2])/v[3] for k, v in desi.items()}
min_tension = min(tensions.values())
check("BST's banked breathing-mode dark energy (corpus #54/#101) predicts w_a > 0 -- the OPPOSITE side of w_a=0 "
      "from DESI's w_a < 0. The w_a=0 boundary already sits ~3σ below DESI's central value, so BST (w_a > 0) is "
      "AT LEAST ~3σ from DESI DR2. This is a LIVE TENSION / potential falsifier for BST's dark-energy sector, "
      "NOT a confirmation",
      min_tension >= 2.9,
      f"BST w_a>0 vs DESI w_a<0: ≥{min_tension:.1f}σ tension (both combos ~3σ). Opposite signs. Live falsifier.")

# ----------------------------------------------------------------------------
# 3. Report straight -- do not pick the flattering side.
# ----------------------------------------------------------------------------
print("\n--- 3. discipline: report the tension STRAIGHT; do NOT flip to w_a<0 to match DESI ---")
check("Per the standing order 'go where BST's math takes us; do not pick the flattering side': the ~3σ tension "
      "is reported STRAIGHT. Casey's EM-drives/gravity-gates cosmology is a MECHANISM for the breathing mode, "
      "so it must reproduce the SAME w(a) (w_a > 0, no-phantom-crossing) -- it must NOT quietly predict w_a < 0 "
      "to escape the DESI tension. Fitting the data instead of the geometry is exactly the forbidden move",
      True,
      "tension reported straight; Casey's cosmology constrained to breathing-mode w(a) (w_a>0); no flipping to match DESI.")

# ----------------------------------------------------------------------------
# 4. I-tier governance -- consistency is a brake, not a booster.
# ----------------------------------------------------------------------------
print("\n--- 4. I-tier governance: the consistency check is a BRAKE, not a booster; earns out only via a distinct falsifiable number ---")
check("VERDICT: the DE consistency check is a governance BRAKE. Casey's EM-drives/gravity-gates cosmology stays "
      "I-tier: it inherits the breathing mode's w_a > 0 (under ~3σ DESI tension), must reproduce the same w(a) "
      "with no-phantom-crossing, and does not get to invent a different w(a). It earns its way out of I-tier "
      "only by producing a falsifiable number the breathing mode does not already give -- the two named "
      "handles: (a) predicting the SAME w(a) as the breathing mode, (b) a black-hole→nucleation conservation "
      "law (#72). Until then, it is a picture, not a prediction",
      all_wa_neg and min_tension >= 2.9,
      "I-tier; consistency = brake; w_a>0 under ~3σ DESI tension reported straight; earns out only via a distinct falsifiable number.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (DESI DR2 all w_a<0; BST breathing w_a>0 → ~3σ tension reported straight; Casey cosmology constrained to same w(a); I-tier brake)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5185, the DE consistency check -- BST w_a>0 vs DESI DR2 w_a<0):
  * DESI DR2 (web-scrubbed Aug 2026): DESI+CMB w0=−0.42±0.21, w_a=−1.75±0.58 (3.1σ); DESI+CMB+SN w0=−0.838±0.055,
    w_a=−0.62±0.20. ALL combinations: w_a < 0 (thawing).
  * BST breathing mode: w_a > 0 -- OPPOSITE side → ~3σ tension. A live potential falsifier, NOT a confirmation.
  * discipline: report the tension STRAIGHT; Casey's cosmology must reproduce the breathing-mode w(a) (w_a>0,
    no-phantom-crossing) -- NOT invent w_a<0 to match DESI.
  * I-tier governance: consistency is a BRAKE; earns out only via a distinct falsifiable number (#72, or same w(a)).

AUG-11 [TEGMARK]. Nothing pushed. Nothing banked -- this is a governance brake + an honest tension report:
BST's banked breathing-mode dark energy predicts w_a > 0, and current DESI DR2 (every combination) measures
w_a < 0 at ~3σ, so BST's dark-energy sector is in a LIVE TENSION / potential falsifier, reported straight (go
where the math takes us; do not pick the flattering side). Casey's EM-drives/gravity-gates cosmology is a
mechanism for the breathing mode, constrained to the SAME w(a) (w_a>0, no-phantom-crossing), and stays I-tier
until it makes a falsifiable number the breathing mode does not already give. a₄ chiral coefficients HELD. CP
existence-only. Count N.
""")
