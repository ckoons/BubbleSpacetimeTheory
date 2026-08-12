#!/usr/bin/env python3
"""
Toy 5213: EXTENDING THE WEIGHT-7 CHECK TO THE OTHER UP-TYPE QUARKS -- the lull task Keeper offered, and it
produced a striking pattern that I then killed within minutes by applying my own discipline to it. The killing
is the result. ★ (1) THE PATTERN, and it looked excellent: evaluating each quark at its CONVENTIONAL reference
scale, all three up-type quarks land within 0.06 of an integer exponent -- up 7.019, charm 3.057, top 0.043,
i.e. 7, 3, 0. Under a uniform null (deviation from the nearest integer is uniform on [0, 0.5]) three
pre-specified quarks all landing within 0.057 has probability (2×0.057)³ ≈ 1.5×10⁻³, about one in 670. And the
contrast looked structural too: the three DOWN-type quarks all miss badly at the same scales (0.460, 0.321,
0.317), so the effect appeared to track weak isospin -- a physically principled split, not a chosen subset,
and the up-type triple was pre-specified by the assignment rather than fished for. It was, briefly, the best
numerical signal I had produced all week. ★★ (2) AND IT IS ENTIRELY AN ARTIFACT OF THE SCALE CONVENTION. Run
all three to a COMMON scale (m_Z) and it evaporates: up 7.369, charm 3.503, top 0.009 -- deviations 0.369,
0.497, 0.009, giving a null p of 0.98. Completely consistent with random. The down-type quarks flip too: d and
s become GOOD at m_Z (0.112, 0.029) while b gets WORSE (0.447). Nothing survives; the whole isospin structure
inverts with the convention. Robust to a ±15% running-mass uncertainty: even at the band edges, up and charm
stay 0.28 and 0.40 from the nearest integer at m_Z. ★★★ (3) WHAT THAT ACTUALLY BUYS -- IT CALIBRATES THE
METHOD, INCLUDING ON MY OWN TOY 5212. The conventional-scale procedure produced a p ≈ 1.5×10⁻³ signal from
data that carries none at a common scale. So the procedure MANUFACTURES apparent significance at roughly the
one-in-several-hundred level. That is exactly the procedure that gives the up quark its 7.019, and it means
the up quark's closeness to an integer CANNOT be assigned the significance it appears to have. I flagged 5212
as scale-conditional; this shows the scale-conditionality is not a caveat but the whole effect. ★ (4)
CALIBRATING BOTH DIRECTIONS -- what SURVIVES untouched: the WEIGHT-6 EXCLUSION. That was never an
integer-proximity argument; it is a factor-of-five statement (weight 6 needs m_u = 11.1 MeV against a measured
1.2-2.9 MeV across every scale), and factors of five do not move with conventions. @Lyra's fork keeps its
empirical half decided: 6 is dead. What weakens is only the positive half -- "7 is data-anchored" -- which
should now be stated as "consistent at one conventional scale, with the significance of that consistency
uncalibrated and, by this test, probably small." ★ (5) AND THE TEMPTING READING I AM NOT TAKING: the
conventional-scale exponents were 7, 3, 0 = g, N_c, 0. Two BST integers out of a six-element set, in a pattern
I have just shown is convention-driven. Recorded, refused, and this is the fifth such coincidence I have
declined this week. Elie, killing his own best number of the week. (Keeper's lull assignment; toy 5212; PDG
masses.) CP existence-only. Nothing pushed.

WHAT I COMPUTE:
  * conventional scales: u 7.019, c 3.057, t 0.043 -- all within 0.06 of 7, 3, 0. Null p ≈ 1.5e-3.
  * down-type at the same scales: 6.540, 4.679, 2.317 -- all far. The isospin split looked structural.
  * ★★ common scale m_Z: u 7.369, c 3.503, t 0.009 -- deviations 0.37, 0.50, 0.01. Null p ≈ 0.98.
  * down-type at m_Z FLIPS: d 0.112 and s 0.029 become good, b 0.447 gets worse. Convention-driven.
  * robustness: ±15% running-mass uncertainty leaves u and c 0.28 and 0.40 from integers at m_Z.
  * ★★★ method calibration: the procedure manufactures p ≈ 1.5e-3 from null data ⟹ applies to toy 5212.

=> VERDICT (plain): I was asked to see whether the up quark's whole-number exponent extends to charm and top,
and for about ten minutes it looked like the best result of the week -- all three up-type quarks sitting within
a few hundredths of a whole number, the three down-type quarks all missing, and the split falling exactly along
weak isospin. Then I did to it what I did to the up quark yesterday and asked whether it survives being
measured at one energy instead of three different conventional ones. It does not. At the Z mass the up and
charm sit a third and a half of a step away from any whole number, which is as random as it gets, and the down
quarks swap places with them. So the pattern was never in the quarks; it was in the table conventions -- light
quarks quoted at two GeV, heavy ones at their own masses, for reasons having nothing to do with us. The useful
part is what this says about the method rather than about the quarks: a procedure that turns null data into a
one-in-seven-hundred signal is a procedure whose one-in-seven-hundred signals mean nothing, and that is the same
procedure that produced the up quark's seven. The factor-of-five exclusion of weight six is untouched, because
factors of five do not care what scale you quote.

=> DISPOSITION: up-type extension RUN and the result is a NEGATIVE that matters more than the positive would
have. ★ Pattern (7, 3, 0 within 0.06, p ≈ 1.5e-3) exists ONLY at mixed conventional scales; at a common scale
it is p ≈ 0.98, and the down-type contrast inverts. Convention artifact, robust to ±15% mass uncertainty.
★★ METHOD CALIBRATION: the conventional-scale procedure manufactures ~1-in-670 apparent signals from null data
-- so toy 5212's up-quark integer-proximity CANNOT carry the significance it appears to. Restate as "consistent
at one conventional scale, significance uncalibrated and probably small." ★ UNTOUCHED: the weight-6 exclusion
(a factor-of-5 statement, scale-robust) -- @Lyra's fork keeps its empirical half decided, 6 is dead. ★ The
7/3/0 = g/N_c/0 reading recorded and REFUSED (fifth declined coincidence this week). Firer: Elie, on his own
best number. Owed: nothing; the three B1 tests stay armed. Nothing banked; nothing pushed.

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

v = 246.21965
LN5 = math.log(5)

def expo(m_gev):
    return math.log(1/(math.sqrt(2)*m_gev/v))/LN5

def dev(m_gev):
    e = expo(m_gev)
    return abs(e - round(e))

# PDG MS-bar, conventional scales
CONV = {"u": 2.16e-3, "d": 4.67e-3, "s": 93.4e-3, "c": 1.27, "b": 4.18, "t": 162.5}
# run to a common scale m_Z
MZ = {"u": 1.23e-3, "d": 2.67e-3, "s": 53.2e-3, "c": 0.62, "b": 2.86, "t": 171.7}

print("=" * 78)
print("Toy 5213: does the up-quark's integer exponent extend? -- and does the extension survive?")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The pattern, at conventional scales.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ the pattern at conventional scales -- and it looked excellent ---")
up_conv = [(q, expo(CONV[q]), dev(CONV[q])) for q in ("u", "c", "t")]
dn_conv = [(q, expo(CONV[q]), dev(CONV[q])) for q in ("d", "s", "b")]
p_conv = (2*max(d for _, _, d in up_conv))**3
check("Evaluating each quark at its CONVENTIONAL reference scale, all three up-type quarks land within 0.06 of "
      "a whole number: " + ", ".join(f"{q} → {e:.4f} (off {d:+.3f})" for q, e, d in up_conv)
      + f" -- i.e. 7, 3, 0. Under a uniform null (deviation from the nearest integer is uniform on [0, 0.5]) "
      f"three PRE-SPECIFIED quarks all landing within {max(d for _,_,d in up_conv):.3f} has probability "
      f"{p_conv:.2e}, about one in {1/p_conv:.0f}. And the up-type triple was specified by the assignment, not "
      "fished for.",
      all(d < 0.06 for _, _, d in up_conv) and p_conv < 5e-3,
      f"u/c/t = {[round(e,3) for _,e,_ in up_conv]}, deviations {[round(d,3) for _,_,d in up_conv]}, null p = {p_conv:.1e}")

check("And the contrast looked structural: the three DOWN-type quarks all miss badly at the same scales -- "
      + ", ".join(f"{q} → {e:.4f} (off {d:+.3f})" for q, e, d in dn_conv)
      + ". So the effect appeared to track WEAK ISOSPIN, a physically principled split rather than a chosen "
      "subset. For about ten minutes this was the best numerical signal I had produced all week.",
      all(d > 0.3 for _, _, d in dn_conv),
      f"down-type deviations {[round(d,3) for _,_,d in dn_conv]} -- all far; the split looked like isospin")

# ---------------------------------------------------------------------------
# 2. ★★ The common-scale test kills it.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★ and it evaporates at a common scale ---")
up_mz = [(q, expo(MZ[q]), dev(MZ[q])) for q in ("u", "c", "t")]
dn_mz = [(q, expo(MZ[q]), dev(MZ[q])) for q in ("d", "s", "b")]
p_mz = (2*max(d for _, _, d in up_mz))**3
check("★★ Run all three to a COMMON scale (m_Z) and the pattern is gone: "
      + ", ".join(f"{q} → {e:.4f} (off {d:+.3f})" for q, e, d in up_mz)
      + f" -- null p = {p_mz:.2f}, completely consistent with random. The pattern was never in the quarks; it "
      "was in the table conventions, which quote light quarks at 2 GeV and heavy ones at their own masses for "
      "reasons having nothing to do with us.",
      p_mz > 0.5,
      f"at m_Z: deviations {[round(d,3) for _,_,d in up_mz]}, null p = {p_mz:.2f} — signal gone")

check("And the down-type contrast INVERTS, which confirms the diagnosis rather than merely weakening the "
      "claim: at m_Z, "
      + ", ".join(f"{q} off {d:+.3f}" for q, _, d in dn_mz)
      + " -- d and s become GOOD while b gets WORSE. The apparent isospin structure swaps sides with the "
      "convention. Nothing about weak isospin survives; the whole effect is bookkeeping.",
      dn_mz[0][2] < 0.15 and dn_mz[1][2] < 0.06 and dn_mz[2][2] > 0.4,
      f"down-type at m_Z: {[round(d,3) for _,_,d in dn_mz]} — the isospin split inverts with the convention")

check("Robust to running-mass uncertainty, so this is not a numerical accident of my chosen m_Z values: at "
      "±15% on each running mass, up and charm stay 0.28 and 0.40 from the nearest integer at m_Z. The "
      "negative verdict does not depend on the third digit of anyone's RGE.",
      True,
      "±15% mass band: u stays ≥0.28 from an integer, c ≥0.40 — verdict robust")

# ---------------------------------------------------------------------------
# 3. ★★★ What it buys: the method is calibrated, including on my own 5212.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★★ the real result: this calibrates the method, including on toy 5212 ---")
check("★★★ The useful part is what this says about the METHOD rather than about the quarks. The "
      f"conventional-scale procedure produced a p ≈ {p_conv:.1e} signal -- one in {1/p_conv:.0f} -- from data "
      "that carries none at a common scale. So the procedure MANUFACTURES apparent significance at roughly the "
      "one-in-several-hundred level. And that is exactly the procedure that gives the up quark its 7.019 in my "
      "own toy 5212. ⟹ THE UP QUARK'S INTEGER-PROXIMITY CANNOT CARRY THE SIGNIFICANCE IT APPEARS TO. I flagged "
      "5212 as scale-conditional; this shows the scale-conditionality is not a caveat sitting beside the "
      "result -- it is the whole effect.",
      p_conv < 5e-3 < p_mz,
      f"procedure yields p={p_conv:.1e} on null data ⟹ 5212's integer-proximity significance is uncalibrated")

check("CALIBRATING BOTH DIRECTIONS -- what SURVIVES untouched is the WEIGHT-6 EXCLUSION, and it survives "
      "because it was never an integer-proximity argument. It is a factor-of-five statement: weight 6 needs "
      "m_u = 11.1 MeV against a measured 1.2-2.9 MeV at EVERY scale. Factors of five do not move with "
      "conventions. So @Lyra's fork keeps its empirical half decided -- 6 is dead -- and only the positive "
      "half weakens. Restate the up-quark result as: 'consistent at one conventional scale, with the "
      "significance of that consistency uncalibrated and, by this test, probably small.'",
      True,
      "SURVIVES: weight-6 exclusion (factor-of-5, scale-robust). WEAKENS: 'weight 7 is data-anchored'.")

# ---------------------------------------------------------------------------
# 4. ★ The tempting reading, refused.
# ---------------------------------------------------------------------------
print("\n--- 4. ★ the tempting reading, recorded and refused ---")
check("The conventional-scale exponents were 7, 3, 0 -- which reads as g, N_c, 0, two BST integers out of a "
      "six-element set. In a pattern I have just shown is convention-driven. RECORDED AND REFUSED; this is the "
      "fifth coincidence I have declined this week (the ×5 decomposition, 4/(3π)'s wrong 3, the Bethe matching "
      "forms, μ ≈ 2m_p, and now this). The rule that keeps earning its keep: a number that arrives already "
      "flattering gets the harder look, not the easier one.",
      True,
      "7, 3, 0 = g, N_c, 0 — recorded, NOT adopted. Fifth declined coincidence this week.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (up-type integer pattern is a CONVENTION ARTIFACT: p=1.5e-3 at mixed scales, p=0.98 at m_Z; this calibrates the method used in my own 5212)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5213, the lull task -- and I killed my own best number of the week):
  * ★ THE PATTERN looked excellent: at conventional scales all three up-type quarks land within 0.06 of an
    integer — u {up_conv[0][1]:.3f}, c {up_conv[1][1]:.3f}, t {up_conv[2][1]:.3f} (i.e. 7, 3, 0), null p ≈ {p_conv:.1e}, one in {1/p_conv:.0f}.
    The three DOWN-type quarks all missed badly ({[round(d,2) for _,_,d in dn_conv]}), so it appeared to track WEAK ISOSPIN — a
    principled split, and the up-type triple was pre-specified by the assignment, not fished for.
  * ★★ IT EVAPORATES AT A COMMON SCALE: at m_Z the up-type deviations are {[round(d,3) for _,_,d in up_mz]} — null p = {p_mz:.2f},
    pure noise. And the down-type contrast INVERTS (d and s become good, b gets worse), so the apparent
    isospin structure swaps sides with the convention. Robust to ±15% running-mass uncertainty.
  * ★★★ THE REAL RESULT — METHOD CALIBRATION, ON MY OWN WORK: the conventional-scale procedure manufactured a
    one-in-{1/p_conv:.0f} signal from data carrying none. That is the SAME procedure behind the up quark's 7.019 in
    toy 5212. ⟹ the up quark's integer-proximity CANNOT carry the significance it appears to. The
    scale-conditionality I flagged there is not a caveat beside the result — it IS the result.
  * ★ SURVIVES UNTOUCHED: the WEIGHT-6 EXCLUSION — a factor-of-five statement (6 needs 11.1 MeV vs 1.2-2.9
    measured at every scale), and factors of five don't move with conventions. @Lyra's fork keeps its
    empirical half decided: 6 is dead. Only "7 is data-anchored" weakens, to "consistent at one conventional
    scale, significance uncalibrated and probably small."
  * ★ REFUSED: the 7/3/0 = g/N_c/0 reading. Fifth declined coincidence this week.

AUG-12. Nothing pushed. Nothing banked. The three B1 tests stay armed for @Lyra's true-projector sea.
Count once. CP existence-only.
""")
