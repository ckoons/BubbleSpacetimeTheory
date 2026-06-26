#!/usr/bin/env python3
r"""
toy_4411 — TAU sqrt(pi) FORWARD ATTEMPT (Casey: fire tau in parallel with muon consolidation). Honest result:
           the tau's -sqrt(pi) correction has STRUCTURAL MOTIVATION but is NOT a clean forward derivation and
           does NOT beat look-elsewhere. So the tau stays a CONDITIONAL +1, genuinely weaker than the muon.
           An honest negative is a real result (Casey/Elie framing). The mu/tau ASYMMETRY is the content.

THE TARGET: m_tau/m_e = 49*71 - sqrt(pi) = 3477.2275 (obs 3477.2283, 2e-7 to central). leading 49*71 =
  g^N_c + g^(N_c-1)*2^C_2 (bulk + boundary, toy 4208, forward-motivated).

FORWARD ATTEMPT (heat-kernel / Jordan-Peirce lane):
  (1) STRATUM-DIM -> pi-POWER (the muon's principle): muon pi^12 = (pi^2)^{# 2-forms on S^4}. The tau
      correction is pi^{1/2} -- a HALF-dimensional contribution, consistent with an odd/half stratum. And
      n_C = 5 is ODD, so Gamma(1/2) = sqrt(pi) is intrinsic to the boundary measure (the same odd-n_C origin
      that makes the singleton moments half-integer, toy 4403). STRUCTURALLY plausible.
  (2) JORDAN-PEIRCE: D_IV^5's spin-factor Jordan algebra (rank 2) has half-Peirce space V_(1/2) of dim
      n_C - 2 = 3 = N_c (odd). Lyra's odd-Peirce mechanism puts the sqrt(pi) here. BUT dim = 3, not 1, so a
      SINGLE sqrt(pi) (rather than pi^{N_c/2}) is NOT forced by the dimension count alone -- the coefficient,
      sign, and single power need Lyra's explicit mechanism, not yet in hand.
  (3) LOOK-ELSEWHERE (Cal #411): the data window for the correction is [1.54, 2.01], which admits sqrt(pi)
      =1.772, 16/9=1.778, 9pi/16=1.767, 7/4=1.75 -- ALL fit. The data CANNOT select sqrt(pi). And the leading
      71 = g + 2^C_2 = 7 + 64 is a cheap additive hit. So both the leading form and the correction are
      look-elsewhere-weak.

HONEST VERDICT: the tau sqrt(pi) is STRUCTURALLY MOTIVATED (half-stratum pi^{1/2}; odd n_C intrinsic Gamma(1/2);
  Jordan half-Peirce) but is NOT a clean forward derivation (coefficient/sign/single-power unforced; needs
  Lyra's odd-Peirce mechanism) and does NOT beat look-elsewhere. => the TAU is a CONDITIONAL +1, weaker than
  the muon. It does NOT bank. The mu/tau ASYMMETRY is the content, and it is GEOMETRICALLY GROUNDED:
    - MUON: regular point nu=3/2, Cartan-slice stratum, pi^12 = (pi^2)^{dim so(4)} FORCED; d(nu) innocent;
      => derives (count-mover candidate 4->5, Cal tiers).
    - TAU: Shilov 0-dim stratum, pi-free leading (look-elsewhere-weak) + a non-forward sqrt(pi); conditional.
  This is not a defect of the tau -- it is the geometry saying the two generations are DIFFERENT KINDS of
  object (different strata), exactly Casey's "few asymmetries are the content."

WHAT WOULD CHANGE IT: a forward+blind derivation of -sqrt(pi) from Lyra's odd-Peirce (the exact coefficient,
  sign, single power), AND it then has to beat look-elsewhere (show the OTHER window candidates are excluded by
  the mechanism, not just that sqrt(pi) fits). Until both, the tau is not a count-mover. Do NOT pre-commit to 6.

DISCIPLINE: forward attempt fired (not gated); honest negative reported straight (structural motivation !=
derivation; look-elsewhere not beaten); mu/tau asymmetry grounded in stratum geometry, not hand-waved. NO count
move. Count HOLDS 4 of 26.

Elie - 2026-06-26
"""
import math
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
me = 0.51099895; ttau = 1776.86/me

score = 0; TOTAL = 4
print("="*94)
print("toy_4411 — TAU sqrt(pi) forward attempt: HONEST NEGATIVE (structural motivation, not forced); asymmetry is content")
print("="*94)

print("\n[1] leading 49*71 = g^N_c + g^(N_c-1)*2^C_2 (bulk+boundary, 4208); gap to obs ~ sqrt(pi)")
lead = g**N_c + g**(N_c-1)*2**C2
ok1 = (lead == 49*71) and abs((lead - ttau) - math.pi**0.5) < 0.01
print(f"    {lead}=49*71; gap {lead-ttau:.4f} ~ sqrt(pi)={math.pi**0.5:.4f}: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] structural motivation: pi^{1/2}=half-stratum; n_C odd -> intrinsic Gamma(1/2); Jordan half-Peirce dim n_C-2=N_c")
ok2 = (n_C % 2 == 1) and (n_C - 2 == N_c)
print(f"    n_C odd: {n_C%2==1}; half-Peirce dim = n_C-2 = {n_C-2} = N_c: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] but NOT forced: dim=N_c=3 not 1 -> single sqrt(pi) not forced; coeff/sign need Lyra mechanism")
ok3 = (n_C - 2 != 1)
print(f"    half-Peirce dim {n_C-2} != 1 -> single sqrt(pi) unforced from dimension alone: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] look-elsewhere NOT beaten: window admits sqrt(pi),16/9,9pi/16,7/4; 71=g+2^C_2 cheap -> tau CONDITIONAL +1")
window = {'sqrt(pi)': math.pi**0.5, '16/9': 16/9, '9pi/16': 9*math.pi/16, '7/4': 7/4}
inwin = [k for k,v in window.items() if 1.54 <= v <= 2.01]
ok4 = (len(inwin) >= 3)
print(f"    in-window: {inwin} -> data can't select sqrt(pi); tau not a count-mover yet: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — TAU sqrt(pi): honest NEGATIVE. Structurally motivated (pi^1/2 half-stratum; odd n_C")
print("       intrinsic Gamma(1/2); Jordan half-Peirce) but NOT forward-derived (coeff/sign/single-power unforced)")
print("       and does NOT beat look-elsewhere (window admits 4 candidates; 71=g+2^C_2 cheap). Tau is a CONDITIONAL")
print("       +1, weaker than the muon. The mu/tau ASYMMETRY is GEOMETRY (Cartan-slice pi^12 vs Shilov 0-dim pi-free)")
print("       -- the content, per Casey. Muon candidate 4->5; tau not banked. Do NOT pre-commit to 6. Count 4 of 26.")
print("="*94)
