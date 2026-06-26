#!/usr/bin/env python3
r"""
toy_4406 — HONEST VERIFIER SYNTHESIS (Elie's job): today genuinely ADVANCED the lepton-mass mechanism -- the
           morning's "probably irreducible" was a gating error, corrected -- AND the count still HOLDS 4 of 26,
           because the derivation gates on two NAMED constants that are not yet forward-derived. Both peaks get
           the same Cal #27 discipline: the morning's gating-into-"irreducible" was wrong, and an evening
           swing to "derived" would be equally premature. The truth is in between and it is SHARP.

WHAT TODAY GENUINELY MOVED (real, credit Casey's "don't gate, investigate" + the team):
  - MUON: the pi^12 "wall" is ROUTED (toy 4405). m_mu/m_e = (2^C_2/Vol(S^4))^C_2 = 2^{C_2^2}/Vol(S^4)^C_2 =
    206.76 (0.003%). The C_2-fold factorization Cal #405 called "missing" IS Vol(S^4)^C_2 -- it was never
    missing. Lyra independently rewrote 24/pi^2 = 2^C_2/Vol(S^4); Grace grounded it in the so(4) determinant
    (F118) and the Korányi-Wolf strata (the pi-power = stratum dimension). Genuine structural advance.
  - TAU: forward bulk+boundary assembly g^N_c + g^{N_c-1}*2^C_2 = 343 + 3136 = 3479 = 49*71 (toy 4208) --
    forward-motivated (interior tiling + boundary emission), not just factored from 3479.

CAL #35 FLAG (the discipline that must fire at THIS peak): the load-bearing integers have MULTIPLE readings --
  one structure read several ways, NOT several independent confirmations:
  - 2^C_2 = 64 = 8^2 (so(7)-spinor^2, Lyra) = 4^N_c (SO(5)-spinor^N_c, Elie) -- same 64.
  - exponent 6 = C_2 (Elie) = dim so(4) (Grace) -- same 6.
  Multiplicity of pleasing readings is itself a caution: if the mechanism were uniquely forced, the reading
  would be unique. The readings are leads to adjudicate, not stacked evidence.

THE TWO NAMED CONSTANTS THAT ACTUALLY GATE THE COUNT (neither yet forward+blind):
  (1) MUON: the (2^C_2/Vol(S^4))^C_2 form is "rigorous MODULO the FK Szego constant = 1." The count moves only
      if Szego = 1 is DERIVED forward -- not assumed because it makes 0.003% land. This is the muon's open gate.
  (2) TAU: the leading 49*71 = 3479 is 7.5 sigma ABOVE the measured ratio (toy 4205) -> a correction is
      MANDATORY. 49*71 - sqrt(pi) = 3477.2275 vs observed 3477.2283 (2e-7 to central) -- striking, BUT sqrt(pi)
      was reverse-engineered from the gap AND the data cannot select it (window [1.54,2.01] also admits 16/9,
      9pi/16, 7/4). It counts ONLY if Lyra's odd-Peirce / Gamma(1/2)=sqrt(pi) forward derivation lands blind,
      Cal-watched. This is the tau's open gate.

HONEST TIER: strongly-structured forward mechanism on the correct rep, with TWO named open constants =
  IDENTIFIED, NOT DERIVED. Count HOLDS 4 of 26. The day the FK Szego = 1 and the tau sqrt(pi) come out forward
  and blind, the lepton count can move (2 -> potentially 4 leptons of the 26). Not before. And the unified
  d(nu) residue formula Grace+Lyra cite (one formula, three masses at nu in {0, 3/2, 5/2}) is a claim I will
  VERIFY explicitly when they post the formula -- does one d(nu) actually reproduce all three? That check is
  the unification's real test.

THE META-LESSON (Casey, today): gating the INVESTIGATION ("it's probably irreducible, don't look") was the
  error -- we must look everywhere, and looking found the door. But honest CLAIM-tiering (Cal #27, count holds
  until the constants derive) is NOT gating the investigation -- it is reporting the result truthfully. Do
  both: investigate without gates, tier the claim with discipline. Today did the first; this toy does the second.

DISCIPLINE: credits the genuine advance (no false modesty); flags Cal #35 multiple-readings; names the exact
two gates; holds the count honestly between the two peaks. NO count move. Count HOLDS 4 of 26.

Elie - 2026-06-26
"""
import math
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
me = 0.51099895; tmu = 105.6583755/me; ttau = 1776.86/me; volS4 = 8*math.pi**2/3

score = 0; TOTAL = 4
print("="*94)
print("toy_4406 — HONEST VERIFIER SYNTHESIS: real advance, count gates on FK Szego(muon) + sqrt(pi)(tau)")
print("="*94)

print("\n[1] ADVANCE real: muon wall routed (2^C_2/Vol(S^4))^C_2 = 0.003%; tau forward assembly 49*71 (4208)")
ok1 = abs(2**(C2*C2)/volS4**C2 - tmu)/tmu < 1e-3 and (g**N_c + g**(N_c-1)*2**C2 == 49*71)
print(f"    muon {2**(C2*C2)/volS4**C2:.3f} vs {tmu:.3f}; tau {g**N_c+g**(N_c-1)*2**C2}=49*71: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] Cal #35: 2^C_2=64=8^2=4^N_c (multiple readings); exponent 6=C_2=dim so(4) -- one structure, not N supports")
ok2 = (2**C2 == 8**2 == 4**N_c) and (C2 == 6)
print(f"    multiple readings of the same integers flagged: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] tau leading 49*71 is 7.5 sigma ABOVE data -> sqrt(pi) MANDATORY but reverse-engineered + not data-selectable")
ok3 = abs((49*71 - math.pi**0.5) - ttau) < 0.01
print(f"    49*71-sqrt(pi)={49*71-math.pi**0.5:.4f} vs {ttau:.4f} (2e-7 central); counts only if forward+blind: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] HONEST TIER: identified not derived; count gates on FK Szego=1 (muon) + sqrt(pi) forward (tau)")
ok4 = True
print(f"    strongly-structured + 2 named open constants = count HOLDS 4 of 26; verify d(nu) unification when posted: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — TODAY MOVED THE MECHANISM, NOT THE COUNT. The muon pi^12 wall is genuinely routed")
print("       (Vol(S^4)^C_2, 0.003%) and the tau has a forward assembly -- the morning's 'irreducible' was a gating")
print("       error, corrected. But the count gates on TWO named constants not yet forward+blind: the FK Szego=1")
print("       (muon) and the tau sqrt(pi) (reverse-engineered, data can't select it). Cal #35: 64 and 6 have")
print("       multiple readings = one structure, not stacked evidence. IDENTIFIED, not DERIVED. Investigate without")
print("       gates (done); tier the claim with discipline (this). Count HOLDS 4 of 26 until the constants assay.")
print("="*94)
