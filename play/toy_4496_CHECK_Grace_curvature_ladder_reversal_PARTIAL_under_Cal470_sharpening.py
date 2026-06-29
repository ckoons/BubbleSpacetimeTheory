r"""
toy_4496 — CHECK Grace's curvature-ladder reversal (C)->(B) under Cal #470's F417 sharpening (my heat-kernel
           lane; Grace handed the tier to Cal/Lyra, so this informs the tier). Grace reversed her own ladder
           closure: the three alpha-tower exponents = the three S^4 curvature invariants {R=12, Ric^2=36,
           Riem^2=24}, a systematic pattern she argues disambiguates rich-vocab (C)->(B). VERDICT: PARTIAL.
           The 3=3 match is REAL and suggestive (worth noting), BUT per Cal #470's sharpening ("(B) is clean
           only if the mechanism is independent of target AND SELECTS the reading"), it is NOT a clean unified
           (B) mechanism -- the three rungs have DIFFERENT provenances (m_e=R fit-then-identified (C); tick=
           Ric^2=dim End(Lambda^2) a_2-mechanism (B)-INTERNAL; alpha_G=24 is 2R via F66^2, "=Riem^2" a
           coincidental 2nd reading). So m_e=R STAYS (C) pending the why-alpha (the exp-12 blind derivation);
           the unified "curvature ladder" is a SUGGESTIVE FRAMEWORK, not a clean (B). NO count move. Count 9/26.

THE PATTERN (real): the S^4 curvature invariants R = d(d-1) = 12, Ric^2 = R^2/d = 36, Riem^2 (Kretschmann) =
  2R^2/(d(d-1)) = 24. The alpha-tower exponents {m_e: 12, tick: 36, alpha_G: 24} = {R, Ric^2, Riem^2} EXACTLY.
  Three observables landing on the three curvature invariants -- Grace's "systematic, not three fits."

THE CHECK (Cal #470 sharpening -- does the pattern SELECT each reading via a target-independent mechanism?):
  - m_e = 12 = R : NO mechanism selects "R" -- the 12 is fit-then-identified (Lyra F416; five competing
    forms). The why-alpha (why mass-suppression = alpha^{R}) is OPEN. -> STAYS (C).
  - tick = 36 = Ric^2 = dim End(Lambda^2(S^4)) : the a_2 OPERATOR-dimension mechanism SELECTS it (my 4467).
    -> (B), but INTERNAL (Cal #50).
  - alpha_G = 24 : the mechanism is 2R via F66^2 (alpha_G = (m_e/m_P)^2, my 4482) -- so "24 = 2x12" is
    mechanism-backed, but "24 = Riem^2" is a COINCIDENTAL second reading (2R = Riem^2 = 24 numerically).
    -> (B) via F66^2, NOT via "Riem^2".
  So the THREE rungs reach their tiers by THREE DIFFERENT routes (fit / a_2-operator / F66-square), NOT by one
  unified "curvature-invariant" mechanism. The 3=3 pattern is the OBSERVATION, not the mechanism.

THE VERDICT: PARTIAL reversal. The pattern is real and worth flagging (3 exponents = 3 S^4 invariants), but
  it does NOT clean-disambiguate to a unified (B): m_e=R stays (C) (needs the why-alpha / exp-12), tick is
  (B)-INTERNAL, alpha_G is (B)-via-F66^2 (Riem^2 reading coincidental). Per Cal #470's scope guard
  ("disambiguating an integer's reading != deriving the ratio"), the unified ladder is a SUGGESTIVE FRAMEWORK.
  The genuine route for m_e=R to reach (B) is the exp-12 blind derivation (the why-alpha), not the 3=3 pattern.

TIER: CHECK of Grace's reversal -- PARTIAL. The 3-exponent = 3-curvature-invariant pattern is real/suggestive
  but NOT a clean unified (B) mechanism (three different provenances; m_e=R stays (C) pending why-alpha). For
  Cal's tier. NO count move. Count HOLDS 9/26.

DISCIPLINE: checked a teammate's REVERSAL (Grace handed the tier out, so this is the checker role, not
  resistance); applied Cal #470's sharpening + scope guard; found the reversal PARTIAL (real pattern, but not
  a clean unified (B) -- the rungs have different provenances); kept m_e=R at (C) pending the why-alpha; did
  NOT let a suggestive 3=3 pattern over-promote a fit-then-identified rung. Count HOLDS 9/26.

Elie - 2026-06-29
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
d = 4
R = d*(d-1); Ric2 = R**2//d; Riem2 = 2*R**2//(d*(d-1))

score=0; TOTAL=4
print("="*98)
print("toy_4496 — CHECK Grace curvature-ladder reversal: PARTIAL (real pattern, NOT clean unified (B))")
print("="*98)

print("\n[1] the pattern is REAL: {m_e=12, tick=36, alpha_G=24} = {R=12, Ric^2=36, Riem^2=24} (S^4 invariants)")
ok1 = (sorted([12,36,24]) == sorted([R,Ric2,Riem2]))
print(f"    R={R}, Ric^2={Ric2}, Riem^2={Riem2}; alpha-tower exponents = same set: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] but provenances DIFFER: m_e=R fit-then-identified (C); tick=Ric^2 a_2-mechanism (B)-INTERNAL")
ok2 = True
print(f"    m_e=12=R: no mechanism selects R (Lyra F416) -> (C); tick=36=Ric^2=dim End(Lambda^2): a_2 -> (B) INTERNAL: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] alpha_G=24 is 2R via F66^2 (mechanism), '=Riem^2' coincidental -> (B) via F66^2 not via Riem^2")
ok3 = (2*R == Riem2 == 24)
print(f"    alpha_G=24=2*12 (F66^2 mechanism); 2R=Riem^2={Riem2} numerically -> Riem^2 reading is coincidental: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] VERDICT PARTIAL: 3=3 pattern real/suggestive, NOT a unified (B); m_e=R stays (C) pending why-alpha")
ok4 = True
print("    three rungs -> three different routes (fit / a_2-operator / F66-square), not one curvature mechanism")
print(f"    per Cal #470 scope guard; the exp-12 blind derivation is m_e=R's genuine route to (B). HOLDS 9/26: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — CHECK Grace's curvature-ladder reversal: PARTIAL. The pattern is REAL -- the")
print("       three alpha-tower exponents {12,36,24} = the three S^4 curvature invariants {R, Ric^2, Riem^2}.")
print("       But per Cal #470's sharpening it is NOT a clean unified (B) mechanism: the rungs reach their")
print("       tiers by three DIFFERENT routes (m_e=R fit-then-identified -> (C); tick=Ric^2 a_2-operator-dim")
print("       -> (B)-INTERNAL; alpha_G=24=2R via F66^2, '=Riem^2' coincidental). So m_e=R STAYS (C) pending the")
print("       why-alpha (exp-12 blind derivation); the unified ladder is a SUGGESTIVE FRAMEWORK. For Cal's tier.")
print("="*98)
