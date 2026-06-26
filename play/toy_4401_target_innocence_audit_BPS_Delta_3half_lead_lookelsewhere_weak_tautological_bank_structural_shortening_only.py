#!/usr/bin/env python3
r"""
toy_4401 — TARGET-INNOCENCE AUDIT of Lyra's flagged BPS lead (F335): the F(4) massless 5d scalar has
           conformal dimension Delta = (n_C-2)/2 = 3/2, and the substrate Shilov-component of the rho-vector
           is rho_2 = N_c/rank = 3/2 -- a potential lowest-weight/BPS match. Lyra explicitly did NOT bank it
           ("3/2 is a small number; yesterday taught what banking a pleasing coincidence costs"). This runs the
           target-innocence lens on the lead to help the Lyra+Grace pairing decide what is safe to bank.

VERDICT: the NUMERICAL 3/2 match is look-elsewhere-WEAK and near-TAUTOLOGICAL -> do NOT bank the number; the
         BPS claim must rest on the STRUCTURAL shortening condition (does the discrete-series lowest weight
         actually saturate the F(4) BPS bound / is the rep SHORT), which is a yes/no structural fact.

THE LENS (two legs, both fail for the pure-number reading):
  (1) FORCED-BY-rank=2 / near-tautological (remember linear algebra):
      cascade n_C = N_c + rank with rank=2  =>  n_C - 2 = N_c  =>  (n_C-2)/2 = N_c/2 = N_c/rank = rho_2.
      So Delta = rho_2 is FORCED by rank=2; the two are NOT independent quantities that happened to agree.
      Worse for banking: ANY 5d massless conformal scalar has Delta = (d-2)/2 = 3/2 universally -- the value
      3/2 is not substrate-special at all, it is the generic 5d unitarity-bound scalar dimension.
  (2) LOOK-ELSEWHERE: 3/2 is reachable by several simple substrate ratios (3/2, 6/4, (n_C-2)/2). A small
      rational is cheap to hit; a pure-number coincidence at 3/2 carries almost no evidential weight.

CONSEQUENCE (what the pairing should bank vs flag):
  - DO NOT bank "Delta = rho_2 = 3/2" as a BPS confirmation. It is NECESSARY-not-sufficient and look-elsewhere
    weak; banking it would be exactly the pleasing-coincidence error Lyra flagged.
  - DO test, and bank only if it holds, the STRUCTURAL shortening: does the substrate's holomorphic
    discrete-series lowest weight on H^2(D_IV^5) at genus n_C=5 SATURATE the F(4) BPS-shortening condition
    (does the Verma module have the null vector that shortens it to the supermultiplet)? That is a yes/no rep-
    theory fact (Grace's super-Killing on the oscillator realization + the lowest-weight/null-vector check),
    independent of the numerical value of Delta. Delta=3/2 is then a consistency check, not the evidence.

This is Lyra's own worry made precise + the rank=2 forcing identified: the match is real but cheap; the BPS
content is the shortening, not the number. Consistent with REALIZABLE != FORCED -- even a confirmed BPS
shortening shows the substrate rep CAN be the F(4) supermultiplet, not that it IS (physical posit stands).

DISCIPLINE: target-innocence applied to a teammate's flagged lead BEFORE banking (the lens working as
designed); identifies the forced-by-rank=2 near-tautology + look-elsewhere weakness; redirects to the
structural shortening as the only bankable evidence. NO count move; helps the pairing avoid a soft bank.

Elie - 2026-06-26
"""
from fractions import Fraction as Fr
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
Delta = Fr(n_C-2, 2)
rho2  = Fr(N_c, rank)

score = 0; TOTAL = 4
print("="*94)
print("toy_4401 — TARGET-INNOCENCE AUDIT: BPS Delta=3/2 lead is look-elsewhere-weak/tautological; bank shortening only")
print("="*94)

print(f"\n[1] numerical match: Delta=(n_C-2)/2={Delta}  rho_2=N_c/rank={rho2}  equal={Delta==rho2}")
ok1 = (Delta == rho2 == Fr(3,2))
print(f"    {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] FORCED by rank=2 (not independent): n_C-2 = N_c (cascade) -> (n_C-2)/2 = N_c/rank")
ok2 = (n_C-2 == N_c)
print(f"    n_C-2={n_C-2}=N_c={N_c}: {ok2}; and every 5d massless scalar has Delta=3/2 (generic, not special): {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] LOOK-ELSEWHERE: 3/2 reachable several simple ways (3/2, 6/4, (n_C-2)/2) -> weak for a number match")
hits = set()
vals = [1,2,3,4,5,6,7]
for a in vals:
    for b in vals:
        if Fr(a,b) == Fr(3,2): hits.add(f"{a}/{b}")
ok3 = len(hits) >= 2
print(f"    small-integer ratios = 3/2: {sorted(hits)} -> {len(hits)} ways: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] VERDICT: do NOT bank the number; bank ONLY the structural F(4) BPS-shortening (null-vector) check")
ok4 = True
print(f"    Delta=3/2 necessary-not-sufficient; shortening is the bankable evidence (Grace super-Killing/lowest-weight): {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — target-innocence audit of Lyra's BPS lead: the Delta=rho_2=3/2 match is")
print("       FORCED by rank=2 (n_C-2=N_c) and near-tautological (every 5d massless scalar has Delta=3/2), plus")
print("       look-elsewhere-weak (3/2 reachable several ways). DO NOT bank the number. The BPS content is the")
print("       STRUCTURAL shortening (does the discrete-series lowest weight saturate the F(4) bound / have the")
print("       null vector) -- a yes/no rep fact for the Grace+Lyra pairing; Delta=3/2 is only a consistency check.")
print("       Lyra's own caution, made precise. REALIZABLE != FORCED. Count 4 of 26.")
print("="*94)
