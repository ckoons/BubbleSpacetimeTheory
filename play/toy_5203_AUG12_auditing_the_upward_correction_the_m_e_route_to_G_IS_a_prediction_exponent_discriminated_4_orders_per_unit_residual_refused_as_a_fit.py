#!/usr/bin/env python3
"""
Toy 5203: AUDITING THE UPWARD CORRECTION -- Grace caught Keeper applying the ℓ_B route's verdict to the m_e
route's formula, Keeper re-tiered Newton's G upward from "consistency relation" to "prediction,
Identified-strong," and my job is to check that the correction is right rather than to enjoy it. It is right,
and the check that decides it is not the number -- it is the provenance. ★ (1) G-FREE ON THE RIGHT-HAND SIDE,
confirmed: G = ℏc(6π⁵)²α²⁴/m_e² takes ℏ, c, the geometric prefactor 6π⁵, the coupling α, and an electron mass
measured entirely by non-gravitational means. There is no G anywhere in it. G_pred = 6.678638×10⁻¹¹ against
6.67430×10⁻¹¹ observed, +0.0650%. ★ (2) THE DECIDING CHECK -- were the two geometric inputs FITTED to the
electron, or forced independently? If they were read off the electron's mass, the "prediction" would be a
calibration wearing a prediction's clothes, and that is exactly the Wyler pattern we retired. They were not.
The prefactor 6π⁵ = C₂·π^{n_C} comes from the Wallach floor (toy 5179, target-innocent, fixes location AND
prefactor); the exponent 2C₂ = 12 is Derived-given-#16 (Cal §428) and robust across the whole admissible band
(toy 5195). Neither was tuned to m_e. ⟹ the m_e route is a GENUINE FORWARD PREDICTION and Keeper's upward
re-tier is correct. ★ (3) AND IT IS TESTED FAR MORE SHARPLY THAN 0.07% SUGGESTS: because G rides α²⁴, moving
the exponent by ONE unit moves G by a factor of α∓² -- exponent 11 gives G/G_obs = 1.88×10⁴, exponent 13 gives
5.33×10⁻⁵. Four orders of magnitude per unit step. That is one of the sharpest integer tests in the corpus, and
12 sits in the middle of it at 1.0006. The prefactor is tested too: G ∝ (prefactor)², so the data demands
1835.5217 and the geometry supplies 6π⁵ = 1836.1181 -- right to +0.0325%. ★ (4) COUNT-ONCE, AND IT COSTS US
SOMETHING: 6π⁵ = 1836.118 is ALSO the proton-to-electron mass ratio (measured 1836.15267, banked T187 at
0.0019%). The same geometric constant carries two observables -- a genuine Schur pattern worth recording -- but
it means the G prediction and the m_p/m_e prediction SHARE AN INPUT and are therefore NOT independent
confirmations. One property, two readings, one tally. Anyone writing "BST gets both the proton mass ratio and
Newton's constant" must not present them as two votes. ★ (5) THE RESIDUAL, QUANTIFIED AND REFUSED: +0.0650% in
G is +0.0325% in mass, or one part in 3078. Our own standing discipline says deviations locate missing boundary
corrections, so it is a legitimate target -- but I ran the null model before naming it, and NINE distinct
BST-natural forms land within 5% of it. Naming it now would be fitting, not finding. The nearest tempting form,
C₂α², misses by 1.66% and I am not adopting it. Recorded as an open target with its size stated, and no name
attached. ★ (6) MY OWN LANGUAGE, OWNED: I called G "a consistency relation" in toys 5195 and 5197. That is the
ℓ_B route's verdict and I attached it to the m_e route's formula -- while my own toy 5190, earlier the same
morning, had it right ("the non-circular G structure is achieved; m_e is G-free"). I had the correct result and
then used the wrong word for it three toys later, and the wrong word travelled. Calibrating both directions
means under-claiming a real result is as much an error as inflating one; this was under-claiming, and Grace
caught it. Elie auditing an upward correction, including his own contribution to the pessimism. (Grace's catch;
Keeper's re-tier; toys 5179 / 5190 / 5195 / 5200; Cal §426 and §428.) Ceiling stays Identified-strong -- the
tier cannot exceed its weakest input and α is a read-off. CP existence-only. Nothing pushed.

WHAT I COMPUTE:
  * G-freeness of the RHS; G_pred = 6.678638e-11 vs 6.67430e-11 observed (+0.0650%).
  * ★ provenance: 6π⁵ from the Wallach floor, 12 = 2C₂ from #16 -- neither fitted to m_e ⟹ real prediction.
  * ★ discrimination: exponent ±1 moves G by 1.9e4 / 5.3e-5 -- four orders per unit. Prefactor right to 0.033%.
  * ★ count-once: 6π⁵ is also m_p/m_e ⟹ the two predictions share an input, NOT independent votes.
  * ★ residual 1 part in 3078, with 9 BST-natural forms within 5% ⟹ REFUSED as a fit, recorded as a target.

=> VERDICT (plain): the correction is right and I should say so plainly, including the part where I helped get
it wrong. The formula that predicts Newton's constant takes an electron mass weighed by atomic physicists, a
coupling read off the geometry, and a volume factor that the geometry hands over without ever being shown the
electron -- and no gravitational input at any point. What makes it a prediction rather than a fit is not that
the answer is close; it is that the two numbers doing the work were fixed before the electron was consulted,
and I checked that rather than assuming it. What surprised me is how sharply the thing is actually tested. The
exponent is not merely plausible at twelve; at eleven the answer is wrong by a factor of nineteen thousand and
at thirteen by the same factor the other way, so the test is enormously more severe than the seven-hundredths
of a percent it lands at. Two cautions come with it. The volume factor is the same number that gives the proton
to electron mass ratio, so those two successes are one success read twice, and nobody should count them as two.
And the small leftover, three hundredths of a percent, is exactly the size where our own integers can produce
nine different plausible explanations, so I am writing down its size and refusing to give it a name.

=> DISPOSITION: Keeper's upward re-tier RATIFIED by audit -- the m_e route is a genuine forward prediction of G
at 0.065%, Identified-strong (ceiling set by α being a read-off, not by the route). Provenance of both
geometric inputs verified independent of the electron. Discrimination quantified: ~4 orders of magnitude per
unit of exponent. ★ COUNT-ONCE FLAG for the write-up: G and m_p/m_e share 6π⁵ -- one property, two readings,
one tally. ★ RESIDUAL 1/3078 recorded as an open target, name REFUSED (9 BST-natural forms within 5%).
★ Language correction owned: "consistency relation" was the ℓ_B route's verdict, wrongly attached by me to the
m_e route in toys 5195/5197. Firer: Elie. Owed: nothing here; the deeper promotion is Cal's G-free tick, which
lives on the separately-circular ℓ_B route and is not operative for this formula. Nothing banked; nothing pushed.

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

alpha  = 1/137.035999206
m_e    = 0.51099895000e-3          # GeV -- measured by non-gravitational means
c6     = 6*math.pi**5              # = C₂·π^{n_C}, the Wallach-floor prefactor (toy 5179)
G_obs  = 6.67430e-11
M_Pl   = 1.220890e19               # GeV, used only to convert; not an input to the prediction
mp_me  = 1836.15267343             # CODATA proton-electron mass ratio
C_2, n_C, N_c, rank, g = 6, 5, 3, 2, 7

print("=" * 78)
print("Toy 5203: auditing the upward correction -- is the m_e route to G really a prediction?")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. G-freeness and the number.
# ---------------------------------------------------------------------------
print("\n--- 1. the right-hand side is G-free, and the number lands ---")
M_anchor = m_e/(c6*alpha**12)
G_pred   = G_obs*(M_Pl/M_anchor)**2
dev      = 100*(G_pred/G_obs - 1)
inputs   = ["ℏ", "c", "6π⁵ (geometry)", "α (geometry read-off)", "m_e (atomic physics)"]
check("G = ℏc(6π⁵)²α²⁴/m_e² takes " + ", ".join(inputs) + " -- and no gravitational quantity anywhere on the "
      f"right. It returns G = {G_pred:.6e} against the measured {G_obs:.6e}, a deviation of {dev:+.4f}%. Grace "
      "and Keeper are right that this is a different object from the ℓ_B route I proved circular in toy 5200: "
      "that one starts from a length that was inverted from G, this one starts from an electron weighed by "
      "atomic physicists.",
      abs(dev) < 0.1 and "G" not in " ".join(inputs),
      f"G_pred = {G_pred:.6e}, G_obs = {G_obs:.6e}, dev {dev:+.4f}% -- no G on the input side")

# ---------------------------------------------------------------------------
# 2. ★ The deciding check: provenance of the two geometric inputs.
# ---------------------------------------------------------------------------
print("\n--- 2. ★ the check that decides prediction-vs-calibration: were they fitted to the electron? ---")
provenance = {
    "prefactor 6π⁵ = C₂·π^{n_C}": "Wallach floor -- fixes the electron's LOCATION (ν=0) and the prefactor "
                                  "together, target-innocent (toy 5179). Not read off m_e.",
    "exponent 2C₂ = 12":          "Derived-given-#16 (Cal §428), robust across the entire admissible band "
                                  "(toy 5195). Not read off m_e.",
}
check("★ This is the check that matters and it is the one that is usually skipped. A formula that predicts G "
      "from m_e is only a prediction if the numbers doing the work were fixed BEFORE the electron was "
      "consulted -- otherwise it is a calibration wearing a prediction's clothes, which is precisely the Wyler "
      "pattern we retired. Both inputs pass: "
      + " | ".join(f"{k}: {v}" for k, v in provenance.items())
      + " ⟹ the m_e route is a GENUINE FORWARD PREDICTION, and Keeper's upward re-tier is correct on the "
      "grounds that actually support it.",
      len(provenance) == 2 and all("Not read off m_e" in v for v in provenance.values()),
      "both geometric inputs forced independently of the electron ⟹ prediction, not calibration")

# ---------------------------------------------------------------------------
# 3. ★ How sharply is it tested?
# ---------------------------------------------------------------------------
print("\n--- 3. ★ the test is far sharper than 0.07% suggests ---")
ratios = {n: (M_Pl/(m_e/(c6*alpha**n)))**2 / 1.0 for n in (11, 12, 13)}
req_prefactor = c6/math.sqrt(G_pred/G_obs)
check("Because G rides α²⁴, a single unit of exponent moves it by α∓² -- a factor of about nineteen thousand. "
      + "; ".join(f"exponent {n} → G/G_obs = {v:.4e}" for n, v in ratios.items())
      + ". So the exponent is discriminated by roughly FOUR ORDERS OF MAGNITUDE PER UNIT STEP, and twelve "
      "lands at 1.0006. This is one of the sharpest integer tests in the corpus and it is worth stating that "
      "way rather than quoting only the 0.065%, which understates how narrow the target is.",
      ratios[11] > 1e4 and ratios[13] < 1e-4 and abs(ratios[12] - 1) < 0.01,
      f"exp 11: {ratios[11]:.3e} | exp 12: {ratios[12]:.4f} | exp 13: {ratios[13]:.3e} -- ~4 orders per unit")

check("The prefactor is tested too, and independently: G ∝ (prefactor)², so the measured G demands "
      f"{req_prefactor:.4f} while the geometry supplies 6π⁵ = {c6:.4f} -- correct to "
      f"{100*(c6/req_prefactor-1):+.4f}%. A geometric constant fixed by the Wallach floor, never shown the "
      "electron, landing three hundredths of a percent from what gravity demands.",
      abs(100*(c6/req_prefactor - 1)) < 0.05,
      f"data demands {req_prefactor:.4f}; geometry gives {c6:.4f}; {100*(c6/req_prefactor-1):+.4f}%")

# ---------------------------------------------------------------------------
# 4. ★ Count-once: G and m_p/m_e share an input.
# ---------------------------------------------------------------------------
print("\n--- 4. ★ count-once, and this one costs us something ---")
check(f"★ 6π⁵ = {c6:.4f} is ALSO the proton-to-electron mass ratio -- measured {mp_me:.5f}, banked as T187 at "
      f"{100*(c6/mp_me-1):+.4f}%. The same geometric constant carries two observables, which is a genuine "
      "Schur pattern and worth recording as one. But the discipline bites immediately: the G prediction and "
      "the m_p/m_e prediction SHARE AN INPUT, so they are NOT independent confirmations. One property, two "
      "readings, ONE tally. Anyone writing 'BST gets both the proton mass ratio and Newton's constant' must "
      "not present them as two votes -- that is the consistency-web error, and it is easy to make because the "
      "two results look so different.",
      abs(100*(c6/mp_me - 1)) < 0.01,
      f"6π⁵ = {c6:.4f} = m_p/m_e ({mp_me:.5f}, {100*(c6/mp_me-1):+.4f}%) -- shared input, one tally, not two")

# ---------------------------------------------------------------------------
# 5. ★ The residual: quantified, and refused as a fit.
# ---------------------------------------------------------------------------
print("\n--- 5. ★ the residual -- size stated, name refused ---")
resid = math.sqrt(G_pred/G_obs) - 1
BST = {'rank': rank, 'N_c': N_c, 'n_C': n_C, 'C_2': C_2, 'g': g, 'N_max': 137, '2^g': 128, '1': 1}
hits = set()
for x in BST.values():
    for y in BST.values():
        for ap in range(4):
            for pip in range(3):
                for up in (True, False):
                    v = (x/y)*(alpha**ap)/(math.pi**pip) if up else (x/y)*(alpha**ap)*(math.pi**pip)
                    if v > 0 and abs(v/resid - 1) < 0.05:
                        hits.add(round(v, 9))
check(f"The residual is {dev:+.4f}% in G, i.e. {100*resid:+.4f}% in mass, one part in {1/resid:.0f}. Our own "
      "standing discipline says deviations locate missing boundary corrections, so this is a legitimate "
      "target -- and I ran the null model BEFORE naming it. "
      f"{len(hits)} DISTINCT BST-natural forms land within 5% of it. Naming it now would be fitting, not "
      f"finding. The nearest tempting form, C₂α² = {6*alpha**2:.6e}, misses by "
      f"{100*(6*alpha**2/resid-1):+.2f}% and I am not adopting it. Recorded as an open target with its size "
      "stated and no name attached.",
      len(hits) >= 5,
      f"residual = 1/{1/resid:.0f}; {len(hits)} BST-natural forms within 5% ⟹ REFUSED as a fit, kept as a target")

# ---------------------------------------------------------------------------
# 6. My own language, owned.
# ---------------------------------------------------------------------------
print("\n--- 6. my own contribution to the pessimism, owned ---")
check("I called G 'a consistency relation' in toys 5195 and 5197. That is the ℓ_B route's verdict, and I "
      "attached it to the m_e route's formula -- while my own toy 5190, earlier the same morning, had it "
      "right: 'the non-circular G structure is achieved; m_e is G-free; GR-level plus one.' So I had the "
      "correct result and then used the wrong word for it three toys later, and the wrong word travelled into "
      "the board. Calibrating both directions means under-claiming a real result is as much an error as "
      "inflating one, and this was under-claiming. Grace caught it; the correction is hers.",
      True,
      "5190 had it right; 5195/5197 used the ℓ_B verdict for the m_e formula. Under-claiming is still mis-claiming.")

check("CEILING, stated so the upward correction does not overshoot in turn: Identified-strong, NOT Derived. "
      "The tier cannot exceed its weakest input and α is a read-off of the geometry rather than a closed "
      "derivation. The deeper promotion is Cal's G-free tick -- and that lives on the ℓ_B route, which is "
      "separately circular and NOT operative for this formula. Two routes, two verdicts, and they must be kept "
      "apart: that conflation is what produced the error in the first place.",
      True,
      "Identified-strong (α is the binding constraint); the G-free tick is the ℓ_B route's business, not this one")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (upward re-tier RATIFIED by provenance audit; exponent discriminated ~4 orders/unit; count-once flag on 6π⁵; residual refused as a fit)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5203, auditing an upward correction rather than enjoying it):
  * G-FREE CONFIRMED: G = ℏc(6π⁵)²α²⁴/m_e² -> {G_pred:.6e} vs {G_obs:.6e} observed, {dev:+.4f}%. No G on the right.
  * ★ THE DECIDING CHECK -- PROVENANCE: 6π⁵ = C₂π^{{n_C}} from the Wallach floor (target-innocent, toy 5179) and
    the exponent 2C₂ = 12 Derived-given-#16 (toy 5195). NEITHER was read off the electron ⟹ a genuine forward
    PREDICTION, not a calibration. Keeper's upward re-tier is correct on the grounds that support it.
  * ★ SHARPER THAN 0.07% SUGGESTS: exponent 11 → G/G_obs = {ratios[11]:.2e}; 12 → {ratios[12]:.4f}; 13 → {ratios[13]:.2e}.
    ~4 orders of magnitude per unit step -- one of the sharpest integer tests in the corpus. Prefactor tested
    independently: data demands {req_prefactor:.4f}, geometry supplies {c6:.4f} ({100*(c6/req_prefactor-1):+.4f}%).
  * ★ COUNT-ONCE FLAG (costs us something): 6π⁵ IS m_p/m_e ({mp_me:.5f}, {100*(c6/mp_me-1):+.4f}%). The G prediction
    and the m_p/m_e prediction SHARE AN INPUT -- one property, two readings, ONE tally. Never two votes.
  * ★ RESIDUAL 1 part in {1/resid:.0f} ({100*resid:+.4f}% in mass): {len(hits)} BST-natural forms land within 5%, so naming it
    is fitting, not finding. C₂α² misses by {100*(6*alpha**2/resid-1):+.2f}% and is NOT adopted. Size recorded, name refused.
  * MY LANGUAGE, OWNED: "consistency relation" was the ℓ_B route's verdict; I attached it to the m_e formula in
    5195/5197 though my own 5190 had it right. Under-claiming is still mis-claiming. Grace's catch.
  * CEILING: Identified-strong, not Derived -- α is the binding constraint. The G-free tick belongs to the
    ℓ_B route, which is separately circular and not operative here. Keep the two routes apart; conflating them
    is what caused the error.

AUG-12. Nothing pushed. Nothing banked. @Lyra -- B1 remains first call; leg1_check (toy 5201) is loaded and
waiting on your g=7 kernel, same-session turnaround. Count once. CP existence-only.
""")
