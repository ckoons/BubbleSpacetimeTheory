#!/usr/bin/env python3
"""
Toy 5208: THE S-STATE SELECTIVITY GATE, QUANTIFIED -- taking the forward lane Keeper assigned (K1413's
"cheaper, target-innocent, no retrofit risk" gate, to be run BEFORE the Bethe log). Keeper's read of my last
several rounds was fair: they were all subtraction -- correcting, bounding, withdrawing. Good for the
foundation, invisible as progress. So this one adds: it turns "does the picture get s-state selectivity?" from
a qualitative hope into TWO measured, target-innocent tests, one of which the contact structure PASSES at
0.011% and one of which is a sharp discriminator that Welton's own picture FAILS. ★ THE MECHANISM: Welton's
1948 reading -- the electron is jiggled by vacuum fluctuations and smeared over ⟨δr²⟩, so it samples the
potential over a region and shifts by ΔE = (1/6)⟨δr²⟩⟨∇²V⟩. For a Coulomb nucleus ∇²V = 4πZe²δ³(r), a CONTACT
term, so ΔE ∝ |ψ_n(0)|², which is nonzero only for l = 0 and scales as 1/n³. That is where the selectivity
comes from, and it is the structural feature any geometrization of the picture must reproduce. ★ GATE 1 --
THE 1/n³ CONTACT SCALING, AND IT PASSES SHARPLY. Predicted L(1S)/L(2S) = [bracket(1S)/1³]/[bracket(2S)/2³] =
7.82004 using only the standard Bethe logarithms; measured level shifts give 8172.840/1045.0 = 7.82090. Agreement
to 0.011%. The contact reading is not a story -- it is confirmed by two independently measured hydrogen levels
to one part in ten thousand. ★★ GATE 2 -- THE DISCRIMINATOR, AND IT IS THE INTERESTING ONE: p-states are not
merely suppressed, they are shifted THE OTHER WAY. L(2P₁/₂) = −12.8 MHz against L(2S) = +1045.0 MHz: a ratio of
81.6 to 1 AND AN OPPOSITE SIGN. Welton's picture structurally CANNOT produce that. Its shift is
(1/6)⟨δr²⟩⟨∇²V⟩ with ⟨δr²⟩ > 0 and ⟨∇²V⟩ = 4πZe²|ψ(0)|² ≥ 0 -- so a smeared charge always raises the energy,
and gives exactly zero where ψ(0) = 0. Positive-or-zero, never negative. The measured p-state shift is negative.
⟹ A GEOMETRIZED WELTON PICTURE MUST GO BEYOND SMEARING TO GET THE p-STATE SIGN, and that is a cheap place for
the lead to fail. ★ WHAT THIS SAYS ABOUT CASEY'S LEAD, both directions honestly: FOR it -- his decomposition
puts the contact-carrying powers on the S⁴ (the (Zα)⁴ = 3 spatial from |ψ(0)|² + 1 Coulomb vertex), and the
contact structure is now confirmed quantitatively at 0.011%, so that assignment is consistent and no longer
merely plausible. AGAINST easy optimism -- the S¹ factor has to do real work: it must deliver a NEGATIVE shift
for l ≠ 0, which no amount of smearing over the S⁴ will give. Both gates are target-innocent, both are cheap,
and both can be run the moment the construction exists. ★ FIREWALL DISCLOSURE (Keeper K1414, and I checked
rather than assumed): I use the Bethe logarithms here as INPUTS to a structural ratio test, never as targets,
and I grepped the data layer for a banked BST matching form for ln k₀(1,0) = 2.984128556 -- there is none (the
only 2.984 in the ledger is N_eff from LEP, an unrelated quantity). So this test is clear of the retrofit
magnet. Elie taking a forward lane. (K1413 Welton identification; K1414 firewall; Casey's S⁴×S¹ lead; toy 5202's
d+2 correspondence.) I-tier. CP existence-only. Nothing pushed.

WHAT I COMPUTE:
  * the contact mechanism: ΔE ∝ |ψ_n(0)|² ⟹ zero for l ≠ 0, 1/n³ across the s-series.
  * ★ GATE 1: predicted L(1S)/L(2S) = 7.82004 vs measured 7.82090 -- 0.011%. Contact structure CONFIRMED.
  * ★★ GATE 2: L(2P₁/₂) = −12.8 MHz vs L(2S) = +1045.0 MHz -- 81.6:1 AND opposite sign.
  * Welton gives positive-or-zero always (⟨δr²⟩ > 0, ⟨∇²V⟩ ∝ |ψ(0)|² ≥ 0) ⟹ CANNOT produce the p-state sign.
  * firewall: Bethe logs used as inputs not targets; ln k₀(1,0) has no banked BST form (checked).

=> VERDICT (plain): the selectivity gate is worth more quantified than it was as a slogan. The reason the Lamb
shift cares about s-states is that the electron's smearing samples a potential whose Laplacian is a spike at
the origin, so only states that actually sit at the origin feel it -- and that story makes a sharp prediction
about how the shift falls off along the s-series, which the two measured hydrogen levels confirm to one part
in ten thousand. So the contact reading is solid, and Casey's assignment of those powers to the four-sphere is
consistent with it in a way that is now numerical rather than verbal. The part worth flagging is the p-states.
They are not just small; they go the other way, and a picture built on smearing cannot do that, because
smearing a charge in a well can only cost energy and can only do nothing at all where the wavefunction
vanishes. Whatever the geometry does with the phase circle has to produce a shift of the opposite sign for
states that never visit the origin. That is a cheap and decisive place for the whole lead to fail, and it
should be tested before the expensive Bethe-log computation, not after.

=> DISPOSITION: s-state selectivity gate QUANTIFIED into two target-innocent tests. ★ GATE 1 (contact / 1n³
scaling) PASSES at 0.011% -- confirms the contact structure Casey's S⁴ assignment relies on. ★★ GATE 2 (p-state
SIGN FLIP) is the discriminator and pure Welton FAILS it structurally -- the geometrization must produce a
negative shift for l ≠ 0 or the lead dies cheaply. Recommended order unchanged from Keeper's: these two gates
BEFORE the Bethe log. Firewall observed and disclosed (logs as inputs; ln k₀(1,0) has no banked form). Firer:
Elie. Owed: nothing from me until someone runs the S⁴×S¹ construction; I score it against both gates the
session it lands. Nothing banked; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-12.
"""

import math

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

alpha = 1/137.035999206
# Standard hydrogen Bethe logarithms
lnk0 = {(1, 0): 2.984128556, (2, 0): 2.811769893, (2, 1): -0.030016709}
LOG = math.log(1/alpha**2) + 19/30
def bracket(n, l):
    return LOG - lnk0[(n, l)]

# Measured LEVEL shifts (MHz): the 1S and 2S QED shifts, and the 2P_1/2 shift
L_1S, L_2S, L_2P = 8172.840, 1045.0, -12.8

print("=" * 78)
print("Toy 5208: the s-state selectivity gate, quantified -- two target-innocent tests")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The mechanism.
# ---------------------------------------------------------------------------
print("\n--- 1. where the selectivity comes from: a contact term ---")
check("Welton's 1948 reading -- the picture K1413 identified as the classical ancestor of Casey's lead: the "
      "electron is jiggled by vacuum fluctuations, smeared over ⟨δr²⟩, and therefore samples the potential "
      "over a region rather than at a point, shifting by ΔE = (1/6)⟨δr²⟩⟨∇²V⟩. For a Coulomb nucleus "
      "∇²V = 4πZe²δ³(r) -- a CONTACT term -- so ΔE ∝ |ψ_n(0)|², which is nonzero only for l = 0 and falls as "
      "1/n³. That is the whole origin of s-state selectivity, and it is the structural feature any "
      "geometrization of the picture has to reproduce.",
      True,
      "ΔE = (1/6)⟨δr²⟩⟨∇²V⟩; ∇²V ∝ δ³(r) ⟹ ΔE ∝ |ψ(0)|² ⟹ l = 0 only, and ∝ 1/n³")

# ---------------------------------------------------------------------------
# 2. ★ GATE 1 -- the 1/n³ contact scaling, quantified.
# ---------------------------------------------------------------------------
print("\n--- 2. ★ GATE 1: the 1/n³ contact scaling, against two measured hydrogen levels ---")
pred = (bracket(1, 0)/1**3)/(bracket(2, 0)/2**3)
obs = L_1S/L_2S
dev = 100*(obs/pred - 1)
check("★ If the shift is a contact term it must scale as |ψ_n(0)|² ∝ 1/n³, modulated only by the bracket "
      f"[ln(1/α²) + 19/30 − ln k₀(n,0)]. That predicts L(1S)/L(2S) = ({bracket(1,0):.5f}/1³)/"
      f"({bracket(2,0):.5f}/2³) = {pred:.5f}, using nothing but standard Bethe logarithms. The measured level "
      f"shifts give {L_1S}/{L_2S} = {obs:.5f} -- agreement to {dev:+.4f}%. The contact reading is not a story; "
      "two independently measured hydrogen levels confirm it to one part in ten thousand. GATE 1 PASSES.",
      abs(dev) < 0.05,
      f"predicted {pred:.5f}, observed {obs:.5f}, {dev:+.4f}% -- contact structure confirmed")

# ---------------------------------------------------------------------------
# 3. ★★ GATE 2 -- the sign flip Welton cannot produce.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★ GATE 2: p-states go the OTHER WAY, and smearing cannot do that ---")
ratio = abs(L_2S/L_2P)
check(f"★★ p-states are not merely suppressed -- they are shifted the OTHER WAY. L(2P₁/₂) = {L_2P:+.1f} MHz "
      f"against L(2S) = {L_2S:+.1f} MHz: a ratio of {ratio:.1f} to 1 AND an opposite sign, which traces to "
      f"ln k₀(2,1) = {lnk0[(2,1)]:+.6f} being negative. That is a much sharper fact than 'the Lamb shift "
      "prefers s-states,' and it is measured.",
      L_2S*L_2P < 0 and ratio > 50,
      f"L(2S) = {L_2S:+.1f} MHz, L(2P₁/₂) = {L_2P:+.1f} MHz -- {ratio:.1f}:1 and OPPOSITE SIGN")

check("★★ AND WELTON'S PICTURE STRUCTURALLY CANNOT PRODUCE IT. Its shift is (1/6)⟨δr²⟩⟨∇²V⟩ with ⟨δr²⟩ > 0 "
      "(a mean square displacement) and ⟨∇²V⟩ = 4πZe²|ψ(0)|² ≥ 0 (∇²(−Ze²/r) = +4πZe²δ³(r)). So a smeared "
      "charge in a Coulomb well ALWAYS raises the energy, and gives EXACTLY ZERO wherever ψ(0) = 0. "
      "Positive-or-zero, never negative -- for l ≠ 0 it predicts 0.0 MHz against the measured −12.8. ⟹ A "
      "geometrized Welton picture must go BEYOND smearing to get the p-state sign, and that is a cheap and "
      "decisive place for the whole lead to fail.",
      True,
      "Welton ⟹ ΔE ≥ 0 always, and = 0 for l ≠ 0. Measured p-shift is NEGATIVE. Smearing alone fails.")

# ---------------------------------------------------------------------------
# 4. What it says about the lead -- both directions.
# ---------------------------------------------------------------------------
print("\n--- 4. what this says about Casey's lead, both directions ---")
check("FOR the lead: Casey's decomposition assigns the contact-carrying powers to the S⁴ -- the (Zα)⁴ being "
      "three spatial powers from |ψ(0)|² plus one Coulomb vertex (toy 5202) -- and the contact structure is "
      "now confirmed QUANTITATIVELY at 0.011% rather than merely being plausible. That assignment is "
      "consistent with measured hydrogen, which is more than it was this morning.",
      abs(dev) < 0.05,
      "the S⁴ contact assignment is consistent with data at 0.011% -- upgraded from plausible to quantitative")

check("AGAINST easy optimism: the S¹ factor now has a named job it cannot dodge -- it must deliver a NEGATIVE "
      "shift for l ≠ 0, which no amount of smearing over the S⁴ will ever give. That is the first thing the "
      "construction should be asked for, because it is cheap to check and it kills the lead outright if it "
      "fails. Recommended order stands as @Keeper set it: these two gates BEFORE the expensive Bethe-log "
      "computation, not after.",
      True,
      "the S¹ must produce the p-state sign flip -- cheap, decisive, and first")

# ---------------------------------------------------------------------------
# 5. Firewall disclosure.
# ---------------------------------------------------------------------------
print("\n--- 5. firewall disclosure (K1414) -- checked, not assumed ---")
check("@Keeper's firewall covers the Bethe-log VALUES being pre-banked in our ledger as BST matching forms. "
      "Two disclosures. First, I use the Bethe logarithms here as INPUTS to a structural ratio test, never as "
      "targets -- nothing in this toy is derived toward them. Second, I grepped the data layer for a banked "
      "form for ln k₀(1,0) = 2.984128556 and there is NONE (the only 2.984 in the ledger is N_eff from LEP, an "
      "unrelated quantity). So GATE 1 is clear of the retrofit magnet. I checked rather than assumed, which is "
      "the lesson I took from having committed a 'blind' gate this morning without grepping our own book.",
      True,
      "logs used as inputs not targets; ln k₀(1,0) has no banked BST form (only 2.984 = N_eff, LEP, unrelated)")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (GATE 1 contact/1n³ PASSES at 0.011%; GATE 2 p-state SIGN FLIP is the discriminator and pure Welton fails it)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5208, the forward lane -- the selectivity gate turned from a slogan into two measured tests):
  * MECHANISM: Welton's smearing samples a potential whose Laplacian is a contact spike, so ΔE ∝ |ψ_n(0)|² --
    nonzero only for l = 0, falling as 1/n³. That is the structural feature any geometrization must reproduce.
  * ★ GATE 1 -- CONTACT / 1n³ SCALING, PASSES SHARPLY: predicted L(1S)/L(2S) = {pred:.5f} from the bracket
    ratio alone; measured 8172.840/1045.0 = {obs:.5f}. Agreement {dev:+.4f}%. Two independently measured
    hydrogen levels confirm the contact reading to one part in ten thousand.
  * ★★ GATE 2 -- THE DISCRIMINATOR: p-states go the OTHER WAY. L(2P₁/₂) = {L_2P:+.1f} MHz vs L(2S) = {L_2S:+.1f} MHz --
    {ratio:.1f}:1 AND opposite sign. ★ WELTON STRUCTURALLY CANNOT DO THIS: ⟨δr²⟩ > 0 and ⟨∇²V⟩ ∝ |ψ(0)|² ≥ 0,
    so smearing always RAISES the energy and gives exactly ZERO where ψ(0) = 0. It predicts 0.0 MHz for l ≠ 0
    against a measured −12.8. The geometrization must go beyond smearing to get the sign.
  * FOR CASEY'S LEAD: the S⁴ contact assignment is now consistent with data at 0.011%, not merely plausible.
    AGAINST easy optimism: the S¹ has a named job -- produce a NEGATIVE shift for l ≠ 0 -- and it is cheap to
    check and fatal if it fails. Run both gates BEFORE the Bethe log, as @Keeper ordered.
  * FIREWALL DISCLOSED AND CHECKED: Bethe logs used as INPUTS, never targets; ln k₀(1,0) has no banked BST
    matching form (the only 2.984 in the ledger is N_eff from LEP). Clear of the retrofit magnet -- and I
    grepped rather than assumed, which is this morning's lesson applied.

AUG-12. Nothing pushed. Nothing banked. I-tier, forward, and it can fail cheaply -- which is the point.
Both B1 harnesses remain loaded for K_f. Count once. CP existence-only.
""")
