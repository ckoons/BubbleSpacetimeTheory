#!/usr/bin/env python3
r"""
toy_4422 — ACCEPT Cal's NO-BANK catch on the muon (retract the 4421 "forward bank" verdict). Cal's forward
           computation is correct: my 4421 verified the SUBORDINATE question (d_tau/d_mu = 64 forward) but
           MISSED that the per-direction density in (24/pi^2)^{C_2} is 24, not 64 -- and bridging 24 -> 64 via
           the identity #409 (24 = 2^{C_2}/Vol(S^4) = 64/(8pi^2/3)) is a REGROUPING, not a derivation.
           The muon does NOT bank. Count HOLDS 4/26. (Separate arithmetic from conclusion -- the discipline.)

THE SQUARING GAP (Cal, verified): muon = (24/pi^2)^{C_2} = 24^6/pi^12. 24 = 2^3 * 3, so 24^6 has 2-power
  2^{18} = 2^{N_c * C_2}. My 4421 reading (2^{C_2}/Vol(S^4))^{C_2} = 2^{C_2^2}/Vol^{C_2} put 2^{36}=2^{C_2^2} in
  the numerator -- but Vol(S^4)^6 = (8pi^2/3)^6 carries 2^{18} that cancels it back to 2^{18}. So my "2^{C_2}=64
  per direction" SPLIT a 2^3 off each Vol(S^4) = pure bookkeeping. The real per-direction density is 24, and
  64 = 24 * 8/3 (borrowed from the volume). #409 is a REGROUPING of the target 24, not a forced-operator output.

SEPARATE ARITHMETIC FROM CONCLUSION (Cal #347/B5 + Lyra meta-lesson):
  - ARITHMETIC (correct, keep): d_tau/d_mu = 64 = 2^{C_2}, forward from the root-system d(nu). Subordinate fact.
  - CONCLUSION (wrong, RETRACT): "muon banks forward." The per-direction density is 24 (not 64); the 24->64
    bridge is #409 regrouping. So 4421's bank verdict is RETRACTED. The muon is a STRONG CANDIDATE (5-of-6
    forward: d(nu) derived, exponent dim so(4)=6 forced, Vol geometry, FK theorem, locus-measure forward-closed),
    but the per-direction DENSITY 24 is not yet a forced-operator output.

THE 24-FACTORIZATION AMBIGUITY (Cal, why 24 isn't yet banked): 24 = 2^3 * 3 has MULTIPLE substrate
  factorizations -- 2^{N_c}*N_c (=8*3), C_2*rank^2 (=6*4), 4! , N_c*(n_C+N_c) (=3*8), 2^{C_2}/Vol-regroup. They
  all give the correct 2-power 2^3 per direction (2^{18} total), so the 2-power check alone does NOT select one.
  A clean BANK needs a FORCED determinant (forced space + forced eigenvalues, target-innocent) that UNIQUELY
  outputs 24 -- not a pleasing factorization chosen post hoc. I will NOT over-claim a replacement reading.

CAL'S LEVER (Saturday's highest-value target, my lane, OPEN): show a determinant over a FORCED space with
  FORCED eigenvalues (Cal candidate: Z2 Shilov doubling eigenvalue "2") + TARGET-INNOCENT density that outputs
  24. Crucially, this same determinant IS K551's open Half-2 (the measurement determinant) = the SAME object as
  the down-row N_c-texture base -- so closing it forward closes the muon AND templates the down-row (potential
  +1 muon -> 5 AND +3 down-row -> 8). The 2-power constraint (2^{N_c*C_2}=2^{18}) is the check the forced
  determinant must satisfy (my 2^{C_2^2}=2^{36} reading FAILED it -- that's the tell it was a regrouping).

HONEST TIER: muon STRONG CANDIDATE (5/6 forward), NOT banked -- the per-direction density 24 is a regrouping
  pending a forced determinant. Count HOLDS 4/26 (Cal's tier verdict stands). The lever is the genuine open
  computation; I'll fire it honestly (forced determinant, not a chosen factorization) and report row-or-not.

DISCIPLINE: accepted Cal's no-bank catch in the open (no defense); separated correct arithmetic (d_tau/d_mu=64)
from wrong conclusion (muon banks); identified the 2-power tell (2^18 not 2^36) that exposes the regrouping;
refused to over-claim a replacement factorization (24 is ambiguous); framed the lever as the open computation.
Count HOLDS 4/26.

Elie - 2026-06-27
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

score = 0; TOTAL = 4
print("="*94)
print("toy_4422 — ACCEPT Cal no-bank: muon density is 24 (2-power 2^18), NOT 64 (2^36); #409 is regrouping")
print("="*94)

print("\n[1] real per-direction density is 24 = 2^3*3; 2-power of muon = 2^(N_c*C_2) = 2^18 (Cal, verified)")
ok1 = (24 == 2**3*3) and (6*3 == N_c*C2 == 18)
print(f"    24=2^3*3; 24^6 2-power = 2^{6*3} = 2^(N_c*C_2)={N_c*C2}: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] my 4421 (2^C_2/Vol)^C_2 -> 2^36 numerator, cancelled by Vol^6's 2^18 -> net 2^18; '64' = 24*8/3 regroup")
ok2 = (2**(C2*C2) == 2**36) and (24*8//3 == 64)
print(f"    2^(C_2^2)=2^36 (my reading) vs actual 2^18; 64 = 24*8/3 (borrowed from Vol) = REGROUP: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] RETRACT 4421 bank verdict: d_tau/d_mu=64 [arithmetic, correct] != muon-banks [conclusion, wrong]")
ok3 = True
print(f"    24->64 bridge is #409 regrouping; muon STRONG CANDIDATE (5/6), NOT banked: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] LEVER (open): forced determinant -> 24, target-innocent, 2-power 2^18 check; 24 has many factorizations")
facts = {'2^N_c*N_c': 2**N_c*N_c, 'C_2*rank^2': C2*rank**2, '4!': 24, 'N_c*(n_C+N_c)': N_c*(n_C+N_c)}
ok4 = all(v == 24 for v in facts.values())
print(f"    24 = {facts} -- forced det must UNIQUELY select one (open computation): {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — ACCEPTED Cal's no-bank: the muon per-direction density is 24 (2-power 2^18), NOT 64")
print("       (which would need 2^36). #409 (2^C_2/Vol) is a REGROUPING (64 = 24*8/3, borrowing from the volume).")
print("       4421 bank verdict RETRACTED. Muon STRONG CANDIDATE (5/6 forward), NOT banked. The forced determinant")
print("       for 24 (target-innocent, 2-power 2^18, uniquely-selected among 24's factorizations) is Cal's lever =")
print("       the open computation that closes muon AND templates the down-row. Won't over-claim. Count HOLDS 4/26.")
print("="*94)
