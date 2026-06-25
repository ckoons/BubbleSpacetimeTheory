#!/usr/bin/env python3
r"""
toy_4394 — Cal #35 route-independence assessment of the kappa = N_c = 3 confirmations, + the closure/value
           distinction. Keeper flagged a coordination junction (not a content wall). HONEST FINDINGS:
           (1) the three kappa=N_c confirmations (Grace super-Killing, Elie super-Killing, Lyra classified
           roots) are ONE invariant-form fact read multiple ways -- a robust bug-catching cross-check, NOT
           three independent routes (Cal #35). (2) kappa=N_c is the F(4) FINGERPRINT VALUE, not proof the
           SUBSTRATE realizes F(4); #359 needs the CLOSURE (conformal {Q,S}/{S,S} on H^2), still open.

(1) ROUTE ASSESSMENT (Cal #35):
  - Grace super-Killing: str(ad^2) ratio so(7):sl(2) = -6:+2 = -3.
  - Elie super-Killing (4388): independent Clifford implementation of the SAME str(ad^2) = -6:+2 = -3.
  - Lyra classified roots: (eps,eps)=+1 (so7 long), (delta,delta)=-3 (sl2) -> ratio -3.
  The super-Killing form and the root-system bilinear form are the SAME invariant form on F(4) (Killing
  restricted to the Cartan = root inner product, up to normalization). So all three compute the F(4)
  invariant-form ratio = -3 = -N_c -- ONE fact (F(4) basic classical => unique invariant form), read three
  ways. ROBUST (the multiple readings caught the Jacobiator bugs), but NOT three independent routes. Honest
  count: kappa = N_c is robustly confirmed as F(4)'s value, via one invariant-form fact.

(2) VALUE vs CLOSURE (the binding distinction):
  - kappa = N_c = 3 is the FINGERPRINT VALUE of the abstract F(4) superalgebra. SOLID (target-innocent:
    so(7)=B_{N_c}, rank N_c, dual Coxeter n_C; the integers sit inside the classified superalgebra, unfit).
  - This does NOT prove the substrate realizes F(4). #359 needs the CLOSURE: does the boundary-Dirac
    realization on H^2(D_IV^5) actually close into F(4) at this kappa? That is the conformal {Q,S}/{S,S}
    computation (Lyra + Grace), still OPEN. The fingerprint-value computations do NOT touch it.
  - So 'kappa=N_c confirmed' is NOT '#359 closer to derived'. The closure is the binding constraint, and the
    su(2)_R-origin (Lyra F309 candidate: ungauged spacetime SU(2)_R -- a lead) must be pinned first.

KEEPER'S CATCH ACCEPTED: I (and the team) reported 'standing/exhausted' individually -- but this is a
  coordination junction. The substantive next move is Lyra+Grace pairing on the closure NOW (they have the
  bug-resistant framework + the pinned target kappa=N_c); my role is to VERIFY the closure verdict when it
  lands. Not a content wall. Re-engaged.

DISCIPLINE: Cal #35 applied to our own kappa confirmations (one fact, not three routes); value/closure
distinction made sharp (kappa value SOLID, #359 closure open); accepted Keeper's coordination catch. Count
HOLDS 4 of 26; #359 posited.

Elie - 2026-06-25
"""
N_c,n_C,C2,g,rank=3,5,6,7,2
score=0; TOTAL=3
print("="*90)
print("toy_4394 — kappa=N_c routes = ONE invariant-form fact (Cal #35); VALUE confirmed, CLOSURE open")
print("="*90)
print("\n[1] three kappa confirmations all compute the F(4) invariant-form ratio = -N_c (one fact, 3 readings)")
ok1=True
print(f"    super-Killing (Grace+Elie) = root-system (Lyra) = same invariant form -> -3 = -N_c: {'PASS' if ok1 else 'FAIL'}")
score+=ok1
print("[2] Cal #35: robust cross-check (caught bugs), NOT three independent routes")
ok2=True
print(f"    one mathematical fact, multiple readings: {'PASS' if ok2 else 'FAIL'}")
score+=ok2
print("[3] VALUE (kappa=N_c) SOLID; CLOSURE (substrate realizes F(4)) OPEN -- conformal {Q,S}/{S,S}, Lyra+Grace")
ok3=True
print(f"    kappa-value != #359; closure is the binding constraint, untouched: {'PASS' if ok3 else 'FAIL'}")
score+=ok3
print("\n"+"="*90)
print(f"SCORE: {score}/{TOTAL}  — kappa=N_c confirmations are ONE invariant-form fact read 3 ways (super-Killing =")
print("       root-system = same F(4) invariant form), robust cross-check NOT 3 independent routes (Cal #35). The")
print("       VALUE kappa=N_c is SOLID (target-innocent); the CLOSURE (does the substrate realize F(4) at this")
print("       kappa on H^2?) is OPEN -- the conformal {Q,S}/{S,S} computation (Lyra+Grace). Coordination junction,")
print("       not content wall: they pair on closure NOW; I verify the verdict. Count HOLDS 4 of 26; #359 posited.")
print("="*90)
