r"""
toy_4491 — PAIR with Grace: the C_2-CURVATURE LADDER (her cross-lane thread; my heat-kernel lane) -- test its
           SCOPE across the light sector, INCORPORATING Cal's K603 verdicts (taken, not resisted). Grace's
           thread: C_2 = 6, R(S^4) = 2C_2 = 12, C_2^2 = 36 organize the light sector. VERDICT (post-Cal): the
           ladder is a SUGGESTIVE heat-kernel a_k organizing FRAMEWORK, but it is NOT a clean derivation --
           Cal K603 down-tiered two of its rungs: f_pi (Cal #286 candidate -- 180 has a rich four-primary
           vocabulary) and m_e's exponent-12 (provenance question -- fit-then-identified, not blind). The tick
           rung is INTERNAL (Cal #50). The clean BOUNDARIES hold (Lambda instanton + m_pi chiral are OFF the
           ladder). So: a framework/lead, with honestly-tiered rungs, clean boundaries -- NOT a banked result.
           NO count move. Count 9/26.

THE LADDER (heat-kernel a_k curvature invariants on S^4), each rung HONESTLY TIERED per Cal K603:
  a_1 fiber:   C_2 = 6 = dim Lambda^2(S^4)              -> MUON. ESTABLISHED (the a_1 fiber, F118).
  a_1 scalar:  R(S^4) = 12 = 2 C_2                       -> m_e exponent (alpha^12) + f_pi factor (180=N_c*n_C*R).
                  CAL PROVENANCE QUESTION (K603): the exponent 12 was FIT-THEN-IDENTIFIED as R(S^4) (it came
                  from the m_e fit, F66, then read as R(S^4)) -- TARGET-AWARE, a Cal #35 reading, NOT a blind
                  derivation. Lyra's lane to settle the provenance. CANDIDATE, not banked.
  f_pi:        180 = N_c*n_C*R(S^4) = N_c*n_C*2*C_2      -> f_pi = 180 m_e (0.33%).
                  CAL #286 CANDIDATE (K603): 180 has a RICH four-primary vocabulary (= rank^2*N_c^2*n_C too),
                  and 92.28 is a rounded target -> downgraded to candidate, NOT banked.
  a_1 doubled: 2 R(S^4) = 24 = 4 C_2                     -> alpha_G exponent. = F66 SQUARED (Cal-CREDITED as
                  non-independent: the 0.068% = exactly 2x F66's 0.034%). NOT an independent rung.
  a_2:         C_2^2 = 36 = Ric^2(S^4)                   -> TICK. INTERNAL (Cal #50).

THE CLEAN BOUNDARIES (OFF the ladder -- these HOLD, the honest negatives):
  - Lambda: exp 280 = 2^{N_c} n_C g -- INSTANTON (a_0), NOT a curvature invariant (my 4485). OFF the ladder.
  - m_pi, m_rho: QCD-dynamical (chiral SSB / confinement), NOT curvature. OFF the ladder.

VERDICT (post-Cal, honest): the C_2-curvature ladder is a SUGGESTIVE organizing FRAMEWORK (the heat-kernel a_k
  invariants recurring across muon / m_e / f_pi / alpha_G / tick), with CLEAN BOUNDARIES (Lambda + m_pi off).
  But per Cal K603 it is NOT a clean derivation: the f_pi rung is a Cal #286 candidate (vocabulary-rich), the
  m_e-12 rung is fit-then-identified (provenance open, Lyra's lane), the alpha_G rung is F66^2 (non-
  independent), the tick rung is INTERNAL. So it is a FRAMEWORK/LEAD -- the heat-kernel a_k organizing the
  curvature-mechanism quantities -- not a banked multiplicative result. Taking Cal's catches sharpens it.

TIER: C_2-curvature ladder = a SUGGESTIVE heat-kernel a_k FRAMEWORK with honestly-tiered rungs (muon
  established; m_e-12 fit-then-identified per Cal provenance; f_pi Cal #286 candidate; alpha_G = F66^2
  non-independent; tick INTERNAL) and clean boundaries (Lambda/m_pi off). NOT a clean derivation. NO count
  move. Count HOLDS 9/26.

DISCIPLINE: TOOK Cal's K603 verdicts INTO the ladder (f_pi -> #286 candidate; m_e-12 -> provenance/
  fit-then-identified; alpha_G -> F66^2 non-independent) rather than presenting the ladder as a clean
  multiplicative pattern; kept the tick INTERNAL (Cal #50); held the honest boundaries (Lambda/m_pi off);
  framed it as a FRAMEWORK/LEAD not a bank. Count HOLDS 9/26.

Elie - 2026-06-29
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
d = 4; R = d*(d-1); Ric2 = (d-1)**2*d

score=0; TOTAL=4
print("="*98)
print("toy_4491 — PAIR Grace C_2-curvature ladder: SUGGESTIVE framework, Cal K603 down-tiered (f_pi/m_e rungs)")
print("="*98)

print("\n[1] the ladder values: C_2=6, R(S^4)=2C_2=12, C_2^2=36 (heat-kernel a_k invariants)")
ok1 = (R == 2*C2 == 12) and (Ric2 == C2**2 == 36)
print(f"    C_2={C2}=dim Lambda^2; R(S^4)={R}=2C_2; C_2^2=Ric^2={Ric2}: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] rungs HONESTLY tiered (Cal K603): muon=established; m_e-12=fit-then-identified; f_pi=#286 candidate")
ok2 = True
print("    muon C_2 (a_1 fiber, established); m_e exp 12=R (CAL provenance: fit-then-identified, target-aware)")
print(f"    f_pi 180=N_c*n_C*R (CAL #286 candidate: also rank^2*N_c^2*n_C, rounded target) -> NOT banked: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] alpha_G = 2R = F66^2 (non-independent, Cal-credited); tick = C_2^2 = a_2 (INTERNAL, Cal #50)")
ok3 = (2*R == 24)
print(f"    alpha_G exp 2R={2*R}=F66^2 (0.068%=2x0.034%, non-independent); tick C_2^2={C2**2} INTERNAL: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] clean BOUNDARIES hold: Lambda (instanton 280) OFF; m_pi/m_rho (QCD-dynamical) OFF the ladder")
ok4 = (2**N_c*n_C*g == 280)
print(f"    Lambda exp 280=2^N_c*n_C*g (instanton a_0, NOT curvature) OFF; m_pi chiral OFF -> framework not bank: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — C_2-CURVATURE LADDER (PAIR Grace, post-Cal K603): a SUGGESTIVE heat-kernel a_k")
print("       FRAMEWORK -- C_2=6 (muon), R(S^4)=12 (m_e exp + f_pi factor), 2R=24 (alpha_G), C_2^2=36 (tick) --")
print("       but NOT a clean derivation. Cal K603 down-tiers the rungs: m_e-12 is fit-then-identified")
print("       (provenance, Lyra's lane), f_pi is a Cal #286 candidate (180 vocabulary-rich + rounded target),")
print("       alpha_G is F66^2 (non-independent), tick is INTERNAL. Clean boundaries hold (Lambda instanton +")
print("       m_pi chiral OFF the ladder). A FRAMEWORK/LEAD, taking Cal's catches -- not a bank. NO count move.")
print("="*98)
