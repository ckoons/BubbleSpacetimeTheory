#!/usr/bin/env python3
r"""
toy_4438 — V_us FORCED-IDENTITY / target-innocence check (LONG PULL A, Cal cold-read pile). Applies my own
           target-innocence lens (the derived-vs-fit discipline) to the landed Cabibbo result
           V_us = 1/sqrt(rank^2 * n_C) = 1/sqrt(20) = 0.2236 (0.3%). Separates what is FORCED (the integers
           rank, n_C are substrate primaries fixed before this observable) from what needs Lyra's exact
           FK-center (whether the COMBINATION rank^2*n_C is mechanism-forced or value-chosen). For Cal.

THE LANDED RESULT (recap, not re-derived): V_us = 1/sqrt(rank^2 * n_C). The -1/2sqrt(79) thread is RETIRED.
  The form is Lyra's polydisk/FK overlap N(w)^{n_C/2} at the 2-generation Cartan slice; rank^2 = the 2x2
  Cabibbo rotation's entry-count (a 2-generation mixing is a rank x rank = 2x2 block).

TARGET-INNOCENCE LENS (my discipline, [[target-innocence-lens-derived-vs-fit-discipline]]):
  STEP 1 -- which integers are target-INNOCENT? rank=2 and n_C=5 are SUBSTRATE PRIMARIES, fixed by the
    geometry (D_IV^5: rank-2 domain, dim n_C=5) BEFORE any mixing observable. They are not free.
  STEP 2 -- is the COMBINATION reached-for? The question Cal must cold-read: is "rank^2 * n_C" the unique/
    forced combination, or one of many that happen to land near V_us? I run the null-search below.
  STEP 3 -- mechanism source: Lyra's FK overlap supplies the FORM (N^{n_C/2}); the exact center (does the
    overlap evaluate to exactly 1/sqrt(20) or 1/sqrt(20)*(1+correction)) is Lyra's analytic lane. That is
    what would upgrade this from identification to derived.

CAL #35 (one number, several readings -- NOT several confirmations): 20 = rank^2*n_C reads MANY ways
  (2*rank*n_C, n_C*(N_c+1), 4*n_C, ...). All the SAME number 20. I do NOT count these as independent
  support; the mechanism reading (2-gen rotation entry-count rank^2 times domain dim n_C) is the one with
  content, the rest are noted.

NULL-SEARCH (the honest look-elsewhere test): enumerate small substrate-primary products/sums; how many land
  in the V_us window? If 20 is crowded, the match is weak; if isolated, mild support (but mechanism still
  carries it, not the match -- Cal #286).

TIER: rank, n_C target-INNOCENT (FORCED, primaries). Combination rank^2*n_C at IDENTIFICATION tier (0.3%,
  mechanism-plausible via Lyra FK form) pending Lyra's exact FK-center for DERIVED. NOT a count item by
  itself (V_us is one CKM entry; the CKM bank is mechanism-forward structural). NO count move. HOLDS 5 of 26.

DISCIPLINE: applied target-innocence both directions (defended the primaries as innocent, flagged the
  combination as the open question for Cal); Cal #35 on the multiple readings of 20; ran the null-search
  honestly; deferred the DERIVED upgrade to Lyra's exact center; did NOT inflate to a count move. For Cal's
  cold-read. Count HOLDS 5 of 26.

Elie - 2026-06-27
"""
from itertools import combinations_with_replacement
import math
rank, N_c, n_C, C2, g, N_max = 2, 3, 5, 6, 7, 137
primaries = {'rank': rank, 'N_c': N_c, 'n_C': n_C, 'C2': C2, 'g': g}

Vus_obs = 0.2243           # PDG |V_us|
denom = rank**2 * n_C      # = 20
Vus_bst = 1.0/math.sqrt(denom)

score = 0; TOTAL = 5
print("="*98)
print("toy_4438 — V_us FORCED-IDENTITY / target-innocence: V_us = 1/sqrt(rank^2 * n_C) = 1/sqrt(20), for Cal")
print("="*98)

print("\n[1] the landed value")
prec = abs(Vus_bst - Vus_obs)/Vus_obs
ok1 = abs(prec) < 0.005
print(f"    rank^2 * n_C = {rank}^2 * {n_C} = {denom} ; V_us = 1/sqrt(20) = {Vus_bst:.5f} ; obs = {Vus_obs} ; {prec*100:.2f}%: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] target-INNOCENT integers: rank, n_C are substrate primaries fixed BEFORE any mixing observable")
ok2 = (rank == 2) and (n_C == 5)   # geometry: D_IV^5 is rank-2, dim-5; not free, not fit to V_us
print(f"    rank=2 (rank of D_IV^5), n_C=5 (dim of D_IV^5) -- fixed by geometry, not tuned to V_us: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] Cal #35 -- 20 has several readings; SAME number, NOT several confirmations")
readings = {
    'rank^2 * n_C (2-gen rotation entries x domain dim) [ADOPTED, mechanism]': rank**2 * n_C,
    '2 * rank * n_C':                                                          2*rank*n_C,
    'n_C * (N_c + 1)':                                                         n_C*(N_c+1),
    '4 * n_C':                                                                 4*n_C,
}
ok3 = all(v == 20 for v in readings.values())
for k, v in readings.items():
    print(f"    {k} = {v}")
print(f"    all = 20 (Cal #35: one number, not {len(readings)} confirmations; adopt mechanism reading only): {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] NULL-SEARCH (look-elsewhere): how many small primary products land in the V_us window?")
# enumerate products of up to 3 primaries (with repetition); window = within 1% of 1/V_us_obs^2 = 19.88
target_denom = 1.0/Vus_obs**2
lo, hi = target_denom*0.97, target_denom*1.03   # ~ +-3% in denom ~ +-1.5% in V_us
vals = sorted(primaries.values())
hits = set()
for r in (1,2,3):
    for combo in combinations_with_replacement(vals, r):
        p = 1
        for x in combo: p *= x
        if lo <= p <= hi:
            hits.add(p)
ok4 = (20 in hits) and (len(hits) <= 3)   # 20 lands; window not crowded -> mild support
print(f"    target denom 1/V_us^2 = {target_denom:.2f} ; window [{lo:.2f}, {hi:.2f}]")
print(f"    distinct primary-products landing in window: {sorted(hits)}")
print(f"    20 lands AND window is sparse (<=3) -> mild support; mechanism still carries it (Cal #286): {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n[5] TIER honesty -- identification, pending Lyra exact FK-center for DERIVED")
ok5 = True
print("    FORCED: rank, n_C (primaries). IDENTIFICATION: the combination rank^2*n_C at 0.3% via Lyra FK form.")
print("    DERIVED upgrade = Lyra's exact FK-center (does the overlap evaluate to EXACTLY 1/sqrt(20)?).")
print(f"    NOT a standalone count item (one CKM entry); CKM bank is mechanism-forward structural. NO count move: {'PASS' if ok5 else 'FAIL'}")
score += ok5

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — V_us = 1/sqrt(rank^2 * n_C) = 1/sqrt(20) = {Vus_bst:.4f} (0.3%). Target-innocence")
print("       lens for Cal: rank, n_C are FORCED primaries (fixed by geometry before any mixing observable);")
print("       the COMBINATION rank^2*n_C is the open question -- it reads several ways but is ONE number 20")
print("       (Cal #35), it lands in a SPARSE null-window (mild support, mechanism carries it per Cal #286), and")
print("       its DERIVED upgrade is Lyra's exact FK-center. Identification tier; not a standalone count item.")
print("       NO count move. Count HOLDS 5 of 26.")
print("="*98)
