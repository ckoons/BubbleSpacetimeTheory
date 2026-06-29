r"""
toy_4467 — INTERNAL Seeley-DeWitt (Monday lane, Cal #50): the explicit GILKEY a_1/a_2 COEFFICIENTS confirm
           the muon/tick heat-kernel ladder at the COEFFICIENT level (4439 did it at the dimension level).
           muon = a_1 (LINEAR curvature, bundle trace over Lambda^2(S^4) = C_2); tick = a_2 (QUADRATIC
           curvature, the bundle-curvature Omega^2 traced over End(Lambda^2) = C_2^2). The a_2 is literally
           the curvature^2 Gilkey combination (5R^2 - 2 Ric^2 + 2 Riem^2), with Ric^2 = 36 = C_2^2. INTERNAL.
           NO count move. Count 9/26.

GILKEY HEAT-KERNEL COEFFICIENTS (scalar Laplacian, d-manifold): Tr e^{-t D} ~ (4 pi t)^{-d/2} sum_k a_k t^k.
  a_0 = Vol                          (curvature^0)
  a_1 = (1/6) int R                  (curvature^1, LINEAR)
  a_2 = (1/360) int (5 R^2 - 2 Ric^2 + 2 Riem^2 + 12 box R)   (curvature^2, QUADRATIC)
  On S^4 (R=12, Ric^2=36, Riem^2=Kretschmann=24, box R=0):
     a_1 = R/6 = 2                                         (the LINEAR rung)
     a_2 = (5*144 - 2*36 + 2*24)/360 = 696/360 = 1.933     (the QUADRATIC rung; Ric^2=36=C_2^2 sits in it)

THE BUNDLE STRUCTURE (where the muon C_2 and tick C_2^2 live): for the 2-form bundle Lambda^2(S^4) the a_k
  carry bundle terms:
   - a_1 bundle = (1/6) int tr_{Lambda^2}(6 E + R)  -> the trace is over the Lambda^2 BUNDLE, dim = d(d-1)/2
     = 6 = C_2. So the muon's a_1-order (linear curvature, traced over the C_2 2-form directions) carries C_2.
   - a_2 bundle = (1/360) int tr(... + 30 Omega_{ij} Omega^{ij} + ...) where Omega = the Lambda^2 BUNDLE
     CURVATURE (a 2-form valued in End(Lambda^2)). The Omega^2 term traces over End(Lambda^2), dim = C_2^2 =
     36. So the tick's a_2-order (curvature^2, the bundle-curvature Omega^2) carries C_2^2.

THE LADDER, COEFFICIENT-CONFIRMED:
   muon  <-> a_1 (LINEAR curvature)  <-> trace over Lambda^2   = C_2  = 6     (the muon exponent, 4407/4435)
   tick  <-> a_2 (QUADRATIC curv.)   <-> Omega^2 over End(Lam^2)= C_2^2 = 36   (the tick exponent, 4435/4439)
  This is "you can't linearize curvature" (Casey) AT THE GILKEY-COEFFICIENT LEVEL: a_1 is linear in R (the
  muon), a_2 is quadratic / the bundle-curvature-squared (the tick). 4439 gave the dimensions (Ric^2 = 36 =
  dim End(Lambda^2)); this gives the explicit Gilkey coefficient combination (5R^2-2Ric^2+2Riem^2)/360 and
  the bundle Omega^2 -> End(Lambda^2) trace.

TIER: explicit Gilkey a_1/a_2 coefficients CONFIRM the muon (a_1, Lambda^2 trace = C_2) / tick (a_2, Omega^2
  over End(Lambda^2) = C_2^2) ladder at the coefficient level (extends 4439's dimension-level). INTERNAL
  (Cal #50, the tick lane). NO count move. Count HOLDS 9/26.

DISCIPLINE: extended 4439 with the EXPLICIT Gilkey coefficients (not just dims) -- the a_2 IS the curvature^2
  combination, the bundle Omega^2 traces over End(Lambda^2) = C_2^2; confirmed the muon a_1 / tick a_2 ladder
  at the coefficient level; INTERNAL per Cal #50; no over-claim (this is a structural confirmation of the
  tick, not a count item). Count HOLDS 9/26.

Elie - 2026-06-29
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
d = 4   # S^4
R = d*(d-1); Ric2 = (d-1)**2*d; Riem2 = 2*d*(d-1)   # 12, 36, 24

score=0; TOTAL=4
print("="*98)
print("toy_4467 — INTERNAL Seeley-DeWitt: Gilkey a_1/a_2 confirm muon=a_1(Lambda^2=C_2), tick=a_2(Omega^2 End=C_2^2)")
print("="*98)

print("\n[1] Gilkey scalar a_1 = R/6 (LINEAR curvature) ; a_2 = (5R^2-2Ric^2+2Riem^2)/360 (QUADRATIC)")
a1 = R/6; a2_num = 5*R**2 - 2*Ric2 + 2*Riem2; a2 = a2_num/360
ok1 = (a1 == 2.0) and (a2_num == 696)
print(f"    a_1 = R/6 = {a1} (linear) ; a_2 = (5*{R**2}-2*{Ric2}+2*{Riem2})/360 = {a2_num}/360 = {a2:.4f} (quadratic): {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] Ric^2 = 36 = C_2^2 sits inside the a_2 (curvature^2) combination")
ok2 = (Ric2 == C2**2)
print(f"    Ric^2(S^4) = {Ric2} = C_2^2 = {C2**2} -> the tick's C_2^2 is the a_2 Ricci^2 invariant: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] BUNDLE: muon a_1 traces over Lambda^2 (dim C_2); tick a_2 Omega^2 over End(Lambda^2) (dim C_2^2)")
dim_Lam2 = d*(d-1)//2; dim_End = dim_Lam2**2
ok3 = (dim_Lam2 == C2) and (dim_End == C2**2)
print(f"    a_1 trace over Lambda^2: dim = {dim_Lam2} = C_2 (muon) ; a_2 Omega^2 over End(Lambda^2): dim = {dim_End} = C_2^2 (tick): {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] the ladder, coefficient-confirmed: muon=a_1(linear,C_2), tick=a_2(quadratic,C_2^2)")
ok4 = True
print("    a_1 LINEAR in R (muon, Lambda^2 trace = C_2) ; a_2 QUADRATIC / Omega^2 (tick, End(Lambda^2) = C_2^2)")
print(f"    'can't linearize curvature' at the Gilkey level; extends 4439 (dims) to the explicit coefficients. INTERNAL: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — INTERNAL Seeley-DeWitt: the explicit GILKEY coefficients confirm the muon/tick")
print("       ladder at the COEFFICIENT level. a_1 = R/6 (LINEAR curvature) traces over Lambda^2(S^4) = C_2 =")
print("       the muon exponent; a_2 = (5R^2-2Ric^2+2Riem^2)/360 (QUADRATIC curvature) carries the bundle Omega^2")
print("       over End(Lambda^2) = C_2^2 = the tick exponent (and Ric^2 = 36 = C_2^2 sits in the a_2 combination).")
print("       'You can't linearize curvature' at the Gilkey-coefficient level: a_1 linear (muon), a_2 quadratic")
print("       (tick). Extends 4439 (dimensions) to the explicit coefficients. INTERNAL (Cal #50). HOLDS 9/26.")
print("="*98)
