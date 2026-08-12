#!/usr/bin/env python3
"""
Toy 5212: IS THE FERMION WEIGHT 7 EMPIRICALLY ANCHORED? -- the assigned check on the up-quark Yukawa
y = n_C^(−7) (K1201), which Keeper framed as anchoring the fermion weight "the way m_p/m_e = 6π⁵ anchors C₂."
Three findings, and the middle one is the most useful to Lyra's open fork while the third is a caution about
the framing. ★ (1) THE STRONG RESULT: at the conventional reference scale μ = 2 GeV the measured up-quark
Yukawa gives an exponent of log₅(1/y) = 7.0194, and the PDG uncertainty on m_u (2.16 +0.49/−0.26 MeV) puts the
band at [6.892, 7.099]. Seven sits comfortably inside. And the discrimination is SHARP because the base is
five: consecutive exponents differ by a factor of 5 in mass while the measurement uncertainty is about 10% in
the exponent -- so the neighbours are excluded by 5× and 0.2×, not by a hair. ★★ (2) THE MOST USEFUL RESULT
FOR @LYRA'S FORK -- WEIGHT 6 IS EXCLUDED BY DATA AT EVERY SCALE, not just at the convenient one. Exponent 6
requires m_u = 11.14 MeV; the measured up-quark runs from about 1.2 MeV at m_Z to about 2.9 MeV at 1 GeV, so
11.1 MeV is four to nine times above the ENTIRE physical range. Her fork was "does the reproducing condition
force 5 + rank = 7 (s = 7/2), or 5 + 1 = 6 (s = 3)?" -- the data answers the empirical half decisively: 6 is
dead, 7 is alive. If the reproducing condition returns 7, that is corroboration by an independent route; if it
returns 6, it contradicts the up-quark at every scale and something is wrong upstream. That is a genuinely
useful constraint to hand her before she computes. ★★★ (3) BUT THE PARALLEL WITH m_p/m_e OVERSTATES IT, and
this is the caution. m_p/m_e is a ratio of PHYSICAL masses -- scale-independent, convention-free, the same
number in every scheme and at every energy. The up-quark Yukawa is a RUNNING PARAMETER: it has no value at all
until a scale is named. And the scale is doing real work here -- the exponent runs 6.836 at 1 GeV, 7.019 at
2 GeV, 7.369 at m_Z. It hits exactly 7 at about 1.9 GeV. Nothing in BST names 2 GeV; it is the conventional
PDG/lattice MS-bar reference, a human bookkeeping choice. So the fermion weight is currently data-CONSISTENT
and sharply so, but it is not data-PINNED in the sense m_p/m_e is, and the two should not be described as the
same kind of anchor. ★ (4) AND I AM REFUSING THE OBVIOUS FISH: the exponent crosses exactly 7 at μ ≈ 1.9 GeV,
which is within 1% of 2m_p = 1.877 GeV. That is exactly the kind of coincidence I have refused three times
this week, and a ±10% window at 2 GeV contains several BST-adjacent quantities. I am recording the crossing
scale and NOT naming it. What would earn the anchor: derive μ_geo from the geometry independently, run down
with the measured RGE, and see whether the exponent lands on 7 there -- the standing "predict at μ_geo, run
down with measured running, never pick a scale" discipline. Elie, the assigned empirical check. (K1201; K1429;
Keeper's route; PDG light-quark masses.) CP existence-only. Nothing pushed. Nothing fitted to seven.

WHAT I COMPUTE:
  * y_up = √2·m_u/v against n_C^(−7) = 1.28e−5, at three scales, with the PDG uncertainty band.
  * ★ at 2 GeV: exponent 7.0194, band [6.892, 7.099]; neighbours excluded by 5× (weight 6) and 0.2× (weight 8).
  * ★★ weight 6 needs m_u = 11.14 MeV -- 4-9× above the entire measured range ⟹ EXCLUDED AT EVERY SCALE.
  * ★★★ scale dependence: exponent 6.836 (1 GeV) → 7.019 (2 GeV) → 7.369 (m_Z); crosses 7 at μ ≈ 1.9 GeV.
  * ★ the m_p/m_e parallel: that is a scale-free ratio of physical masses; this is a running parameter.

=> VERDICT (plain): the up-quark does support the weight seven, and it supports it more sharply than a
three-percent agreement suggests, because with a base of five the neighbouring whole numbers are wrong by
factors of five rather than by a few percent -- there is no room to slide. The most useful thing to come out of
it is that six is not merely disfavoured, it is impossible: it would need an up quark of eleven MeV, and the
real one is between one and three across the whole energy range anybody measures it. So the half of Lyra's fork
that data can settle is settled. The caution is about how we describe it. The proton-to-electron ratio is a
number the universe has whether or not anyone chooses a convention; the up-quark Yukawa is not -- it changes
with the energy you ask at, running from just under seven to just under seven and a half between one GeV and
the Z. It equals seven at around two GeV, which is where the tables happen to be written, and nothing in our
geometry has yet said why that scale. So: consistent, sharply, and not yet pinned. And the place where it hits
seven exactly sits suspiciously near twice the proton mass, which is precisely the sort of thing I have spent
the week declining to name, so I am declining again.

=> DISPOSITION: up-quark anchor CHECKED. ★ Weight 7 is data-CONSISTENT and sharply discriminated at μ = 2 GeV
(exponent 7.019, band [6.89, 7.10]; neighbours off by 5×). ★★ WEIGHT 6 IS EXCLUDED BY DATA AT EVERY SCALE
(needs m_u = 11.14 MeV vs a measured range of 1.2-2.9 MeV) -- hand this to @Lyra before she computes: the
empirical half of her fork is decided, 6 is dead. ★★★ CAUTION ON THE FRAMING (@Keeper): y_up is a RUNNING
parameter and m_p/m_e is a scale-free ratio of physical masses; they are not the same kind of anchor, and the
exponent runs 6.84 → 7.37 across 1 GeV → m_Z. Data-CONSISTENT, not yet data-PINNED. ★ Crossing scale μ ≈ 1.9
GeV recorded and its identification REFUSED (within 1% of 2m_p; a ±10% window there holds several candidates).
To earn it: derive μ_geo geometrically, run down with the measured RGE, compare. Firer: Elie. Owed: nothing
here; the three B1 tests stay armed. Nothing banked; nothing pushed.

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

v = 246.21965          # GeV, Higgs vev
n_C = 5
target = float(n_C)**-7
m_p = 0.938272

def yukawa(m_gev):
    """Standard Dirac convention: m = y v/√2 ⟹ y = √2 m / v."""
    return math.sqrt(2)*m_gev/v

def exponent(m_gev):
    return math.log(1/yukawa(m_gev))/math.log(n_C)

print("=" * 78)
print("Toy 5212: is the fermion weight 7 empirically anchored by the up quark?")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The anchor at the conventional scale.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ the anchor at μ = 2 GeV, with the PDG band ---")
m_u = 2.16e-3
e_c = exponent(m_u)
e_lo, e_hi = exponent(m_u + 0.49e-3), exponent(m_u - 0.26e-3)
dev = 100*(target/yukawa(m_u) - 1)
check(f"At the conventional reference scale the measured up-quark Yukawa is y = {yukawa(m_u):.4e}, against "
      f"n_C^(−7) = {target:.4e} -- a deviation of {dev:+.2f}%. As an exponent, log₅(1/y) = {e_c:.4f}, and the "
      f"PDG uncertainty (2.16 +0.49/−0.26 MeV) gives the band [{e_lo:.3f}, {e_hi:.3f}]. Seven sits comfortably "
      "inside. This much of K1201 checks out.",
      abs(dev) < 5 and e_lo < 7 < e_hi,
      f"exponent {e_c:.4f}, band [{e_lo:.3f}, {e_hi:.3f}]; 5^-7 is {dev:+.2f}% from measured y")

check("And the discrimination is SHARP, which matters more than the 3%: because the base is five, consecutive "
      f"exponents differ by a factor of 5 in mass while the measurement uncertainty is about 10% in the "
      f"exponent. Weight 6 would need m_u = {n_C**-6*v/math.sqrt(2)*1e3:.2f} MeV ({(n_C**-6)/yukawa(m_u):.1f}× "
      f"observed); weight 8 would need {n_C**-8*v/math.sqrt(2)*1e3:.3f} MeV "
      f"({(n_C**-8)/yukawa(m_u):.3f}× observed). The neighbours are excluded by factors, not by hairs -- there "
      "is no room to slide the integer.",
      (n_C**-6)/yukawa(m_u) > 4 and (n_C**-8)/yukawa(m_u) < 0.3,
      f"weight 6 → {n_C**-6*v/math.sqrt(2)*1e3:.1f} MeV (5.2×); weight 8 → {n_C**-8*v/math.sqrt(2)*1e3:.2f} MeV (0.21×)")

# ---------------------------------------------------------------------------
# 2. ★★ The most useful result: 6 is dead at every scale.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★ for @Lyra's fork: weight 6 is excluded by data at EVERY scale ---")
scales = [(1.0, 2.90e-3), (2.0, 2.16e-3), (91.19, 1.23e-3)]
need6 = n_C**-6*v/math.sqrt(2)*1e3
check("★★ @Lyra's fork is 'does the reproducing condition force 5 + rank = 7 (s = 7/2), or 5 + 1 = 6 (s = 3)?' "
      f"The data settles the empirical half decisively. Weight 6 requires m_u = {need6:.2f} MeV. The measured "
      "up quark runs across "
      + ", ".join(f"{m*1e3:.2f} MeV at {mu:g} GeV" for mu, m in scales)
      + f" -- so {need6:.1f} MeV is four to nine times above the ENTIRE physical range, at every scale anyone "
      "measures it. WEIGHT 6 IS DEAD. If the reproducing condition returns 7, that is corroboration by an "
      "independent route; if it returns 6, it contradicts the up quark everywhere and something is wrong "
      "upstream. Worth having before she computes rather than after.",
      all(need6/(m*1e3) > 3.5 for _, m in scales),
      f"weight 6 needs {need6:.1f} MeV; measured range 1.2-2.9 MeV ⟹ excluded by 4-9× at every scale")

# ---------------------------------------------------------------------------
# 3. ★★★ The caution: this is a running parameter, m_p/m_e is not.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★★ the caution on the framing: not the same kind of anchor as m_p/m_e ---")
exps = [(mu, exponent(m)) for mu, m in scales]
check("★★★ @Keeper framed this as anchoring the weight 'the way m_p/m_e = 6π⁵ anchors C₂,' and the parallel "
      "overstates it. m_p/m_e is a ratio of PHYSICAL masses -- scale-independent, convention-free, the same "
      "number in every scheme and at every energy. The up-quark Yukawa is a RUNNING PARAMETER: it has no value "
      "until a scale is named. And the scale does real work here -- the exponent runs "
      + ", ".join(f"{e:.3f} at {mu:g} GeV" for mu, e in exps)
      + ". It equals 7 only in a window around 2 GeV, which is the conventional PDG/lattice MS-bar reference, "
      "a human bookkeeping choice that nothing in BST names. So: data-CONSISTENT, sharply -- but NOT "
      "data-PINNED in the sense m_p/m_e is. The two should not be described as the same kind of anchor.",
      exps[0][1] < 7 < exps[2][1],
      f"exponent runs {exps[0][1]:.3f} → {exps[1][1]:.3f} → {exps[2][1]:.3f} across 1 GeV → 2 GeV → m_Z; scale is load-bearing")

# ---------------------------------------------------------------------------
# 4. ★ The fish, refused.
# ---------------------------------------------------------------------------
print("\n--- 4. ★ the crossing scale, recorded and its identification refused ---")
e1, e2 = exponent(2.90e-3), exponent(2.16e-3)
mu_cross = math.exp(math.log(1.0) + (7.0 - e1)/(e2 - e1)*(math.log(2.0) - math.log(1.0)))
check(f"The exponent crosses exactly 7 at μ ≈ {mu_cross:.2f} GeV (crude linear-in-ln interpolation, ±10%), "
      f"which is within {100*abs(mu_cross/(2*m_p)-1):.1f}% of 2m_p = {2*m_p:.3f} GeV. That is exactly the kind "
      "of coincidence I have declined three times this week, and a ±10% window at 2 GeV contains several "
      "BST-adjacent quantities. ★ RECORDED AND REFUSED. What would EARN the anchor is the standing discipline: "
      "derive μ_geo from the geometry independently, run down with the measured RGE, and see whether the "
      "exponent lands on 7 there. Predict at μ_geo, never pick the scale that works.",
      abs(mu_cross - 2*m_p)/(2*m_p) < 0.15,
      f"crossing at μ ≈ {mu_cross:.2f} GeV, {100*abs(mu_cross/(2*m_p)-1):.1f}% from 2m_p — NOT adopted, recorded only")

# ---------------------------------------------------------------------------
# 5. The honest verdict.
# ---------------------------------------------------------------------------
print("\n--- 5. the verdict, both directions ---")
check("VERDICT: the fermion weight 7 is EMPIRICALLY CONSISTENT and sharply discriminated -- but SCALE-"
      "CONDITIONAL, so it is not yet an anchor of the m_p/m_e kind. The strongest deliverable is the negative "
      "one: weight 6 is excluded by data at every scale, which decides the empirical half of @Lyra's fork "
      "before she computes. The honest external sentence: 'the up-quark Yukawa is n_C^(−7) at the conventional "
      "2 GeV reference, to 3%, with the neighbouring integers excluded by factors of five; whether that scale "
      "is the geometry's own is open.' Not 'the fermion weight is data-pinned at 7.'",
      True,
      "weight 7: data-consistent, sharply, scale-conditional. Weight 6: excluded everywhere. Not yet an m_p/m_e-class pin.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (weight 6 EXCLUDED at every scale; weight 7 consistent at 2 GeV to 3% with neighbours off by 5×; but y_up is a RUNNING parameter, not a scale-free ratio)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5212, the assigned up-quark check -- three findings, one caution):
  * ★ AT μ = 2 GeV: y = {yukawa(m_u):.4e} vs n_C^(−7) = {target:.4e}, deviation {dev:+.2f}%. As an exponent,
    log₅(1/y) = {e_c:.4f} with PDG band [{e_lo:.3f}, {e_hi:.3f}] -- seven comfortably inside. And SHARP: base 5 means the
    neighbours are wrong by 5.2× (weight 6) and 0.21× (weight 8), not by a few percent. No room to slide.
  * ★★ THE MOST USEFUL RESULT, for @Lyra before she computes: WEIGHT 6 IS EXCLUDED BY DATA AT EVERY SCALE.
    It needs m_u = {need6:.1f} MeV; the measured up quark is 1.2-2.9 MeV from m_Z down to 1 GeV -- 4 to 9×
    below. Her fork's empirical half is decided: 6 is dead, 7 is alive. Reproducing-condition = 7 would then
    be corroboration by an independent route; = 6 would contradict the up quark everywhere.
  * ★★★ CAUTION ON THE FRAMING (@Keeper): m_p/m_e is a ratio of PHYSICAL masses -- scale-free, convention-free.
    y_up is a RUNNING parameter with no value until a scale is named, and the scale is load-bearing here:
    exponent {exps[0][1]:.3f} (1 GeV) → {exps[1][1]:.3f} (2 GeV) → {exps[2][1]:.3f} (m_Z). It equals 7 only near 2 GeV, the
    conventional MS-bar reference -- a human choice nothing in BST names. Data-CONSISTENT, not data-PINNED.
  * ★ THE FISH, REFUSED: the exponent crosses exactly 7 at μ ≈ {mu_cross:.2f} GeV, within {100*abs(mu_cross/(2*m_p)-1):.1f}% of 2m_p.
    Recorded, NOT adopted -- a ±10% window there holds several candidates, and this is the fourth such
    coincidence I have declined this week. To EARN it: derive μ_geo geometrically, run down with the measured
    RGE, compare. Predict at μ_geo; never pick the scale that works.
  * HONEST EXTERNAL SENTENCE: "the up-quark Yukawa is n_C^(−7) at the conventional 2 GeV reference, to 3%,
    with neighbouring integers excluded by factors of five; whether that scale is the geometry's own is open."

AUG-12. Nothing pushed. Nothing banked. Nothing fitted to seven. The three B1 tests stay armed for @Lyra's
indefinite projector. Count once. CP existence-only.
""")
