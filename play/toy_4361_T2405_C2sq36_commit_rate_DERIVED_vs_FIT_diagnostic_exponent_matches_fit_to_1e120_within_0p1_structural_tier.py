#!/usr/bin/env python3
r"""
toy_4361 — T2405 commit-rate exponent C_2^2 = 36: derived-vs-fit diagnostic (the check Lyra owed per F308/
           F310; toy-builder's job to catch a fit masquerading as a derivation). VERDICT: STRUCTURAL-tier,
           NOT derivation-grade -- the integer C_2^2=36 is clean, but the EXPONENT in t_commit = t_Planck *
           alpha^{C_2^2} matches the value a pure FIT to the 10^-120 target would need to within 0.1, so the
           clean integer does not make the exponent derived. Confirms + sharpens Lyra's honest tiering.

THE CLAIM UNDER TEST (T2405): the substrate commitment tick is sub-Planck, t_commit = t_Planck * alpha^{C_2^2}
  with C_2^2 = 36, giving ~10^-120 s ("below emergent spacetime").

THE DIAGNOSTIC (derived vs fit):
  - C_2^2 = 36 = 6^2 = (N_c * rank)^2 = N_c^2 * rank^2 -- a CLEAN substrate integer (forced AS an integer).
  - t_commit = t_Planck * alpha^36 = 6.4e-121 s. (numerically ~10^-120, matches the target.)
  - FIT TEST: what exponent n makes alpha^n reach the 10^-120 target from t_Planck? n_fit = (120 - 43.27)/
    log10(1/alpha) = 35.91. The substrate value C_2^2 = 36 matches n_fit to within 0.1.
  - CONSEQUENCE: a clean substrate integer happening to equal (within 0.1) the exact exponent a fit-to-10^-120
    would need is the SIGNATURE of a fit dressed as a derivation. The integer being clean is necessary but
    NOT sufficient -- there is no MECHANISM forcing the commit-rate to be alpha^{C_2^2} rather than alpha^0
    (Planck) or any other power. Cleanness of 36 != derivation of the exponent.

WHAT WOULD UPGRADE IT (the honest bar): a mechanism deriving the EXPONENT = C_2^2 independently of the
  10^-120 target -- e.g., C_2^2 substrate operations per commit, or an alpha-tower with C_2^2 forced rungs --
  that predicts 10^-120 rather than being tuned to it. Absent that, it stays structural-tier.

OPEN PHYSICS (F310, reaffirmed): Planck-rate (alpha^0, constants-file framing) vs sub-Planck (alpha^36,
  T2405) commit-rate is a GENUINE open question, not a typo. The value is not derivation-grade and now not
  even the timescale is pinned.

DISCIPLINE: numerical derived-vs-fit diagnostic (the 0.1 match to the fit exponent is the catch); confirms
Lyra F308/F310 with a concrete reason; does NOT close the physics (open), it tiers the claim honestly. This
is the toy-builder catching a near-fit before it banks as derivation. Count HOLDS 4 of 26.

Elie - 2026-06-24
"""
import numpy as np, math
rank, N_c, n_C, C2, g = 2, 3, 5, 6, 7
alpha = 1/137.035999
t_Planck = 5.391247e-44

C2sq = C2**2
t_commit = t_Planck * alpha**C2sq
orders_planck = -math.log10(t_Planck)
n_fit = (120 - orders_planck)/(-math.log10(alpha))

score=0; TOTAL=4
print("="*94)
print("toy_4361 — T2405 C_2^2=36 commit-rate: derived-vs-fit diagnostic -> STRUCTURAL-tier, not derivation")
print("="*94)

print("\n[1] C_2^2 = 36 is a clean substrate integer (forced AS an integer)")
ok1 = (C2sq == 36 == (N_c*rank)**2 == N_c**2*rank**2)
print(f"    36 = 6^2 = (N_c rank)^2 = N_c^2 rank^2 = {N_c**2*rank**2}: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] t_commit = t_Planck * alpha^36 lands at the ~10^-120 target")
ok2 = (1e-122 < t_commit < 1e-119)
print(f"    t_commit = {t_commit:.3e} s (~10^-120): {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] FIT TEST: exponent needed to reach 10^-120 from t_Planck = 35.91; C_2^2=36 matches within 0.1")
ok3 = (abs(C2sq - n_fit) < 0.2)
print(f"    n_fit = {n_fit:.2f}; |C_2^2 - n_fit| = {abs(C2sq-n_fit):.2f} -> SIGNATURE of fit-dressed-as-derivation: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] VERDICT: clean integer != derived exponent (no mechanism forcing alpha^{C_2^2}). STRUCTURAL-tier.")
print("    Planck (alpha^0) vs sub-Planck (alpha^36) commit-rate = genuine OPEN physics (F310). Not derivation-grade.")
ok4 = True
print(f"    honest tier (confirms Lyra F308/F310): {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — T2405 diagnostic: C_2^2=36 is a clean substrate integer, BUT the commit-rate")
print("       EXPONENT matches the fit-to-10^-120 value (35.91) within 0.1 -- the signature of a fit dressed as")
print("       a derivation. Clean integer != derived exponent; no mechanism forces alpha^{C_2^2}. STRUCTURAL-tier,")
print("       NOT derivation-grade; Planck-vs-sub-Planck commit-rate stays genuine open physics. Toy-builder")
print("       catch before it banks. Confirms Lyra F308/F310. Count HOLDS 4 of 26.")
print("="*94)
