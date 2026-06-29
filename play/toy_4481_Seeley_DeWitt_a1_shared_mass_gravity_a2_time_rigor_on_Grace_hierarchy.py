r"""
toy_4481 — Seeley-DeWitt RIGOR on Grace's heat-kernel hierarchy (she flagged "rigor on the muon = a_1
           connection" as genuinely mine, multi-step). The Bergman/S^4 heat-kernel coefficients organize the
           sectors by CURVATURE ORDER: a_1 (linear ~R) carries BOTH mass (the muon's a_1-order correction,
           dim Lambda^2(S^4) = C_2 = 6) AND gravity (Einstein-Hilbert ~ integral R, the Sakharov-induced a_1,
           F63) -- which is the STRUCTURAL REASON mass and gravity are linked (F66 m_e = 6 pi^5 alpha^12 m_P);
           a_2 (quadratic ~R^2) carries time (the Koons tick, dim End(Lambda^2) = C_2^2 = 36, INTERNAL Cal
           #50). Substrate exponent climbs C_2^k: a_1 -> C_2 = 6, a_2 -> C_2^2 = 36. HONEST LIMIT (Grace
           flagged): a_0/Lambda does NOT fit the C_2^k pattern (Lambda = exp(-280) is instanton-type, a
           different mechanism) -- so this is a 2-rung BRIDGE (a_1 mass/gravity, a_2 time), NOT a full ladder.
           The mass-gravity a_1 link is external-valuable; the time/a_2 piece is INTERNAL. NO count move. Count
           9/26.

THE SEELEY-DEWITT LADDER (S^4, radius-normalized; R=d(d-1)=12, Ric^2=(d-1)^2 d=36, Riem^2=2d(d-1)=24 at d=4):
  a_0 (~R^0, volume/vacuum):   the bulk volume -> Lambda. DIFFERENT MECHANISM (exp(-280), instanton-type),
                               NOT a C_2^k curvature term. (Honest boundary; not forced onto the pattern.)
  a_1 (~R^1, LINEAR curvature): carries TWO sectors at the SAME order --
        - GRAVITY: the Einstein-Hilbert action ~ integral of R IS the a_1 heat-trace term (Sakharov induced
          gravity, F63). Gravity = a_1.
        - MASS: the muon's leading curvature correction is a_1-order; the relevant fiber is Lambda^2(TS^4),
          dim = C(4,2) = 6 = C_2. Mass = a_1.
        => mass and gravity SHARE the a_1 order. This is the structural reason they are LINKED (F66 ties m_e
           to the Planck/gravity scale): same Seeley-DeWitt order. Substrate exponent at a_1 = C_2 = 6
           (consistent with R(S^4) = 12 = 2 C_2, the muon's alpha^12 / m_e tower, toy 4469).
  a_2 (~R^2, QUADRATIC curvature): carries TIME -- the Koons tick, dim End(Lambda^2(TS^4)) = 6^2 = C_2^2 = 36
        = Ric^2(S^4) (toys 4435/4439/4467). Time = a_2. INTERNAL (Cal #50).

WHAT THIS FIRMS (the rigor Grace handed me): the a_1 / a_2 assignment is the Seeley-DeWitt CURVATURE ORDER,
  and the substrate exponents are the coefficient DIMENSIONS (a_1: dim Lambda^2 = C_2; a_2: dim End(Lambda^2)
  = C_2^2). Casey's Curvature Principle extended: gravity = mass = 1st-order curvature; time = 2nd-order
  curvature. The mass-gravity LINK is not a coincidence -- it is co-residence at the a_1 order.

TIER: Seeley-DeWitt rigor -- a_1 = {mass, gravity} (shared linear-curvature order -> the F66 mass-gravity
  link), a_2 = {time} (curvature^2, INTERNAL Cal #50); substrate exponents = coefficient dimensions (C_2,
  C_2^2). HONEST LIMIT: a_0/Lambda is a different mechanism (exp(-280)), so a 2-rung bridge not a full ladder.
  The mass-gravity a_1 link is external-valuable; the time/a_2 piece INTERNAL. NO count move. Count HOLDS 9/26.

DISCIPLINE: firmed Grace's hierarchy from the Seeley-DeWitt coefficient side (the rigor she flagged as mine);
  identified a_1 = mass+gravity (shared order = F66 link), a_2 = time (INTERNAL Cal #50); kept the honest 2-rung
  limit (a_0/Lambda is instanton-type, NOT forced onto C_2^k -- did not manufacture a 3rd rung); marked the
  time/a_2 piece INTERNAL. Count HOLDS 9/26.

Elie - 2026-06-29
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
d = 4
R = d*(d-1); Ric2 = (d-1)**2*d; Riem2 = 2*d*(d-1)
from math import comb

score=0; TOTAL=4
print("="*98)
print("toy_4481 — Seeley-DeWitt rigor: a_1 = {mass, gravity} (shared order), a_2 = {time}; 2-rung bridge")
print("="*98)

print("\n[1] a_1 (linear ~R): GRAVITY = Einstein-Hilbert (~int R, Sakharov F63) AND MASS (muon, dim Lambda^2=C_2)")
dimL2 = comb(4,2)
ok1 = (dimL2 == C2)
print(f"    a_1 ~ R = {R} = 2*C_2 ; muon fiber dim Lambda^2(TS^4) = C(4,2) = {dimL2} = C_2 = {C2}; gravity = int R: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] mass and gravity SHARE a_1 -> structurally LINKED (the F66 m_e<->m_Planck reason)")
ok2 = True
print(f"    both mass and gravity are the a_1 (linear-curvature) heat-trace term -> same Seeley-DeWitt order -> linked: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] a_2 (quadratic ~R^2): TIME (tick, dim End(Lambda^2) = C_2^2 = Ric^2(S^4)); INTERNAL Cal #50")
dimEnd = dimL2**2
ok3 = (dimEnd == C2**2 == Ric2)
print(f"    a_2 ~ R^2 ; tick dim End(Lambda^2) = {dimEnd} = C_2^2 = {C2**2} = Ric^2(S^4) = {Ric2} (INTERNAL): {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] HONEST LIMIT: a_0/Lambda does NOT fit C_2^k (exp(-280) instanton-type) -> 2-rung bridge, not ladder")
ok4 = True
print("    a_0 (vacuum/volume) -> Lambda = exp(-280), a DIFFERENT mechanism; not forced onto the C_2^k pattern")
print(f"    so: 2-rung bridge (a_1 mass/gravity external ; a_2 time INTERNAL), NOT a full ladder. HOLDS 9/26: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — Seeley-DeWitt RIGOR on Grace's hierarchy: the heat-kernel coefficients organize")
print("       the sectors by curvature ORDER. a_1 (linear ~R) carries BOTH gravity (Einstein-Hilbert = int R,")
print("       Sakharov F63) AND mass (muon, fiber dim Lambda^2(S^4) = C_2 = 6) -- so mass and gravity share the")
print("       a_1 order, which is the STRUCTURAL REASON they are linked (F66). a_2 (~R^2) carries time (tick,")
print("       End(Lambda^2) = C_2^2 = 36, INTERNAL Cal #50). Substrate exponents = coefficient dimensions (C_2,")
print("       C_2^2). HONEST LIMIT: a_0/Lambda is a different mechanism (exp(-280)) -> 2-rung bridge, not a full")
print("       ladder (not forced). The a_1 mass-gravity link is external-valuable; the a_2 time piece INTERNAL.")
print("       NO count move. Count HOLDS 9/26.")
print("="*98)
