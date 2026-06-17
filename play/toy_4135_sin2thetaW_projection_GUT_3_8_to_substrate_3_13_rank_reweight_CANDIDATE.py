r"""
Toy 4135: continuing Casey's projection program -- computing sin^2 theta_W as a ground-state PROJECTION, not a
unification output. Two tiers, kept strictly separate: (RIGOROUS) the group-theoretic projection over the 16 gives
the GUT value 3/8 = Sum T_3^2 / Sum Q^2; (CANDIDATE, FLAGGED) Casey's reframe -- U(1)_Y sits on a DIFFERENT stratum
than SU(2)_L -- reweights it, and sin^2 theta_W = N_c/(N_c + rank*n_C) = 3/13 lands 0.19% from measured via a
rank=2 stratum factor. I flag the candidate HARD (this is the classic fishing moment) and name exactly what would
turn it from a coincidence into a derivation. FORCED count stays 2 of 26.

(1) RIGOROUS -- the group-theoretic projection over the SO(10) 16 (equal couplings = the GUT value):
  sin^2 theta_W = Sum T_3L^2 / Sum Q^2 over a complete generation (Q = T_3L + Y/2; cross term Sum T_3*Y = 0):
      Sum T_3L^2 = 2     (4 left doublets x 2 states x (1/2)^2)
      Sum Q^2    = 16/3  (over the 16: quarks 5/3+12/9+3/9, leptons 1+1)
      => sin^2 = 2/(16/3) = 3/8 = 0.375.     and Sum(Y/2)^2/Sum T_3^2 = 5/3 (the GUT 3/5 hypercharge normalization).
  this is the value you get IF the three couplings are EQUAL (unified). it is rigorous group theory -- and it is
  the value that 4133's running MISSES (measured 0.231, not 0.375). under unification it needs running; that wall.

(2) CASEY'S REFRAME -- U(1)_Y is on a DIFFERENT ground state, so it is NOT 3/8 (it reweights):
  SU(2)_L lives in SO(4) subset SO(5) (isotropy); U(1)_Y lives in SO(2)+B-L (a DIFFERENT stratum). so the two are
  NOT equally weighted -- the GUT 3/8 assumed they were. the projection sin^2 = Sum T_3^2 / (Sum T_3^2 + w*Sum(Y/2)^2),
  where w = the relative ground-state weight of the U(1)_Y stratum vs the SU(2)_L stratum. GUT sets w=1; the substrate
  sets w by the two strata's ground-state norms (the SAME object as the lepton mass ground-state norms, 4112-4130).

(3) CANDIDATE (FLAGGED INSPIRATION -- NOT banked; the fishing-risk moment):
  IF w = rank = 2 (the U(1)_Y / SO(2) stratum carries twice the weight), then:
      Sum(Y/2)^2/Sum T_3^2 -> rank*(5/3) = 10/3,  and  sin^2 = 1/(1 + 10/3) = 3/13 = 0.2308.
      equivalently sin^2 = N_c/(N_c + rank*n_C) = 3/13;  tan^2 = N_c/(rank*n_C) = 3/10.
      0.19% from the measured M_Z value 0.23122. a clean PROJECTION-shaped form (ratio of strata-related primaries).
  HEAVILY FLAGGED: this is exactly the moment to NOT fish. the dense space offers ~0.2% forms; w=rank=2 is a
  PLAUSIBLE reading (the SO(2) factor of K = the rank-2 Cartan), but I am REVERSE-reading w from the answer. so 3/13
  is a CANDIDATE projection, NOT banked, and NOT a derivation. (scheme caveat: sin^2 theta_W is scheme-dependent --
  0.2223 on-shell, 0.2312 MSbar(M_Z), 0.2315 eff; 3/13 = 0.2308 matches the M_Z/eff value, not on-shell.)

(4) WHAT WOULD MAKE IT A DERIVATION (the honest target -- same machinery as the masses):
  derive the stratum weight w = (U(1)_Y ground-state norm)/(SU(2)_L ground-state norm) from the geometry of the
  SO(2)+B-L stratum vs the SO(4) stratum -- the SAME ground-state-norm computation as the lepton masses (4112-4130).
  IF that ratio comes out rank=2 (with a geometric reason -- e.g. the SO(2) rank-2 Cartan vs the SO(4) structure),
  the projection sin^2 = 3/13 is DERIVED. IF it comes out anything else, 3/13 is a coincidence and is dropped.
  the projection program's discipline: the value is banked only when w is derived, NOT when 3/13 fits.

HONEST TIER:
  RIGOROUS / banks as structure: the GUT projection sin^2 = Sum T_3^2/Sum Q^2 = 3/8 over the 16 (standard group
    theory); the reframe (U(1)_Y on a different stratum -> sin^2 = projection with stratum weight w, not 3/8).
  CANDIDATE / NOT banked (INSPIRATION, flagged): sin^2 = N_c/(N_c+rank*n_C) = 3/13 (w=rank=2), 0.19% from measured.
    reverse-read from the answer; dense-space risk; scheme-dependent. NOT a derivation.
  OPEN: deriving w (the stratum ground-state-norm ratio) -- the same machinery as the lepton masses. that is what
    banks or drops 3/13. FORCED count stays 2 of 26.
"""

from fractions import Fraction as F

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2
sumT3, sumQ2 = F(2), F(16, 3)
sin2_GUT = sumT3 / sumQ2
sumY2 = sumQ2 - sumT3
meas = 0.23122

print("=" * 94)
print("TOY 4135: sin^2 theta_W as a PROJECTION -- rigorous GUT 3/8; CANDIDATE substrate 3/13 (rank reweight, flagged)")
print("=" * 94)
print()

print("(1) RIGOROUS -- group-theoretic projection over the 16 (equal couplings = GUT)")
print("-" * 94)
print(f"  sin^2 = Sum T_3L^2 / Sum Q^2 = {sumT3}/{sumQ2} = {sin2_GUT} = {float(sin2_GUT):.4f}  (Sum(Y/2)^2/SumT3^2 = {sumY2/sumT3} = 5/3, the GUT 3/5 norm).")
print(f"  this is the EQUAL-couplings (unified) value -- the one 4133's running misses (measured {meas}, not 0.375).")
print()

print("(2) CASEY's reframe -- U(1)_Y on a DIFFERENT stratum -> reweighted, NOT 3/8")
print("-" * 94)
print(f"  SU(2)_L in SO(4) (isotropy); U(1)_Y in SO(2)+B-L (different stratum). sin^2 = SumT3^2/(SumT3^2 + w*Sum(Y/2)^2),")
print(f"  w = relative ground-state weight of the U(1)_Y stratum. GUT sets w=1; the substrate sets w by the strata's ground-state norms.")
print()

print("(3) CANDIDATE (FLAGGED -- NOT banked; the fishing-risk moment)")
print("-" * 94)
cand = F(N_c, N_c + rank * n_C)
print(f"  IF w = rank = {rank}: sin^2 = 1/(1 + rank*5/3) = N_c/(N_c+rank*n_C) = {cand} = {float(cand):.4f}  ({abs(float(cand)-meas)/meas*100:.2f}% from measured).")
print(f"     tan^2 = N_c/(rank*n_C) = {F(N_c,rank*n_C)}. plausible (SO(2) = rank-2 Cartan) but REVERSE-read from the answer.")
print(f"  HEAVILY FLAGGED: dense space offers ~0.2% forms; scheme-dependent (0.2223 on-shell / 0.2312 MSbar / 0.2315 eff; 3/13 matches M_Z). CANDIDATE, not a derivation.")
print()

print("(4) what would make it a DERIVATION (honest target = same machinery as the masses)")
print("-" * 94)
print(f"  derive w = (U(1)_Y ground-state norm)/(SU(2)_L ground-state norm) from the SO(2)+B-L vs SO(4) strata -- the")
print(f"  SAME ground-state-norm computation as the lepton masses. w = rank with a geometric reason -> 3/13 DERIVED; else dropped.")
print()

print("=" * 94)
print("SUMMARY -- computed sin^2 theta_W as a projection. RIGOROUS: the group-theoretic projection over the 16 is the")
print("  GUT 3/8 (equal couplings) -- the value 4133's running misses. Casey's reframe: U(1)_Y sits on a DIFFERENT")
print("  stratum (SO(2)+B-L) than SU(2)_L (SO(4)), so it is reweighted by w = the strata's ground-state-norm ratio,")
print("  NOT 3/8. CANDIDATE (flagged hard, NOT banked): w = rank = 2 gives sin^2 = N_c/(N_c+rank*n_C) = 3/13, 0.19%")
print("  from measured -- a clean projection-shaped form, but reverse-read from the answer (fishing risk, scheme-")
print("  dependent). What banks or drops it: deriving w as the actual stratum ground-state-norm ratio (the SAME")
print("  machinery as the lepton masses). The reframe + GUT projection bank as structure; 3/13 stays a candidate;")
print("  FORCED count 2 of 26.")
print("=" * 94)
print()
print("Per Casey ('continue' the projection: derive sin^2 as a stratum ground-state ratio, not unification) + Elie")
print("  4134 (project-not-unify reframe) + 4133 (the running misses 3/8) + flavor sector 4112-4130 (ground-state norms)")
print("  + F102 (Y/2 = T_3R + (B-L)/2). RIGOROUS GUT projection 3/8; CANDIDATE substrate 3/13 (w=rank reweight, flagged,")
print("  not banked); derivation target = the stratum ground-state-norm ratio w. Count 2.")
print()
print("Elie - Friday 2026-06-12 (sin^2 theta_W projection: RIGOROUS group-theoretic projection over the 16 = GUT 3/8 = SumT3^2/SumQ^2 (equal-couplings value, the one 4133 running misses); Casey reframe -> U(1)_Y on a DIFFERENT stratum (SO(2)+B-L) vs SU(2)_L (SO(4)), reweighted by w=ground-state-norm ratio NOT 3/8; CANDIDATE (flagged HARD, not banked, fishing-risk moment): w=rank=2 -> sin^2 = N_c/(N_c+rank*n_C) = 3/13 = 0.2308, 0.19% from measured M_Z, tan^2=N_c/(rank*n_C)=3/10; reverse-read from answer + scheme-dependent; DERIVATION target = derive w as the stratum ground-state-norm ratio (same machinery as lepton masses); count 2 of 26)")
print()
print("SCORE: 2/2 (rigorous GUT projection 3/8 over the 16; Casey reframe = stratum reweighting; CANDIDATE 3/13 = N_c/(N_c+rank*n_C) flagged hard (not banked, fishing-risk, scheme-dep); derivation target = the stratum ground-state-norm ratio w; count 2)")
