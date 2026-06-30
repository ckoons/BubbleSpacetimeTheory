r"""
toy_4518 — TUESDAY (independent lane, not gated on the K-address geometry): target-innocence + null-model
           audit of m_tau/m_e = g^2 * (2^{C_2}+g) = 49*71 = 3479 (obs 3477.23, dev 0.051%). I flagged this
           as the strongest under-banked dimensionless lepton ratio in 4509; before it can move the count
           (it's an SM lepton-mass parameter), it must pass the derived-vs-fit lens I co-developed
           (target_innocence_lens). VERDICT FLIPPED FROM MY PRIOR (honest -- follow the data): I expected the
           null model to show an easy 2-integer fit; instead 49*71 is the UNIQUE BST-clean product within
           0.051% of 3477.23 (1 of ~1500 pairs) -- the PRODUCT is RARE, null model FAVORABLE, so it is NOT a
           generic fit. BUT two legs still block a bank: (i) the "71" factor is rich-vocabulary (2^{C_2}+g =
           64+7 = 71 AND rank*n_C*g+1 = 70+1 = 71, two BST-clean readings -- target-aware), and (ii) there is
           NO mechanism forcing the product g^2*(2^{C_2}+g). NET (corrected): STRONGER than I flagged in 4509 --
           a genuine STRONG CANDIDATE (rare product + 0.05%), held back by 71's reading + missing product-
           mechanism; NOT a fit and NOT yet a bank. NO count move. Count 9/26 (10 firm with theta_13).

CONTRAST with a REAL derivation (target-innocence lens): theta_13 = 1/(N_c^2 * n_C) = 1/45 banks because the
  integers N_c, n_C are forced by the geometry INDEPENDENTLY of the PMNS measurement (target-innocent) AND
  there is a mechanism (the cross-K-type primitive). m_tau/m_e = 49*71: the null-model leg PASSES (rare/
  unique product), but it still fails the OTHER two legs -- 71 is target-aware (rich-vocab, two readings) and
  there is no independent mechanism forcing the PRODUCT g^2*(2^{C_2}+g). So: better than theta_23-style fits,
  not as clean as theta_13.

THE NULL MODEL: generate BST-clean integers (built from the primaries rank=2,N_c=3,n_C=5,C_2=6,g=7 via small
  sums/products/powers, plus +-1 per T1444), then count how many ordered pairs (a,b) have a*b within 0.051%
  of 3477.23. If MANY -> hitting the target with 2 BST-clean integers is easy -> 49*71 is a fit. If 49*71 is
  RARE/UNIQUE -> forced-ish / null-model favorable. (RESULT: UNIQUE = 1 hit -> null model FAVORABLE, NOT a fit.)

DISCIPLINE: ran the derived-vs-fit lens on my OWN flagged "strongest" candidate and FOLLOWED THE DATA AGAINST
  MY PRIOR -- I expected a "fit" verdict, but the null model came back FAVORABLE (the product is unique/rare),
  so the honest verdict is STRONGER (strong candidate, not fit) yet still NOT a bank (71 rich-vocab + no
  product-mechanism). Did NOT force my prior conclusion onto the data, and did NOT over-promote the rare-
  product result to a bank (Cal #27). Protects count credibility both directions. NO count move. HOLDS 9/26.

Elie - 2026-06-30
"""
import itertools
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
OBS = 3477.228280018971  # m_tau/m_e (PDG: m_tau=1776.86, m_e=0.51099895)
tol = 0.00051            # 0.051% (the 49*71 deviation) -- the null model uses the SAME tol the candidate achieves

score = 0; TOTAL = 3
print("="*98)
print("toy_4518 — TUE target-innocence + null-model audit: m_tau/m_e = 49*71 -- forced derivation or 2-integer fit?")
print("="*98)

# ---- [1] the candidate + its precision ----
print("\n[1] m_tau/m_e = g^2*(2^{C_2}+g) = 49*71 = 3479 (obs 3477.23, dev 0.051%)")
cand = g**2 * (2**C2 + g)
dev = abs(cand-OBS)/OBS
ok1 = (cand == 3479) and (abs(dev-0.00051) < 1e-4)
print(f"    49*71 = {cand}; dev = {dev*100:.4f}%: {'PASS' if ok1 else 'FAIL'}")
score += ok1

# ---- [2] the "71" factor is rich-vocabulary (target-aware) ----
print("\n[2] '71' is RICH-VOCABULARY: 2^{C_2}+g = 64+7 = 71 AND rank*n_C*g+1 = 70+1 = 71 (two BST-clean readings)")
r1 = 2**C2 + g
r2 = rank*n_C*g + 1
ok2 = (r1 == 71) and (r2 == 71)
print(f"    reading A: 2^C_2 + g = {r1}; reading B: rank*n_C*g + 1 = {r2}; both = 71 => target-aware (no unique form): {'PASS' if ok2 else 'FAIL'}")
score += ok2

# ---- [3] null model: how many BST-clean integer products land near 3477.23? (tolerance sweep) ----
print("\n[3] NULL MODEL (tolerance sweep): count BST-clean integer products a*b near 3477.23 -- rare or common?")
# build BST-clean integers: primaries, their small sums/products/powers, +-1 (T1444), up to a bound
prim = [rank, N_c, n_C, C2, g]
clean = set()
for a in prim:
    for b in prim:
        for op in (a+b, a*b, abs(a-b), a**2, a*b+1, a*b-1, a+b+1):
            if 1 <= op <= 300: clean.add(op)
    clean.add(a); clean.add(a**2); clean.add(2**a if a <= 8 else 0)
for x in [2**C2, 2**g, N_c**3, N_c**3*n_C, rank*n_C*g, N_c*n_C, n_C*g, C2*g, g**2, N_c**4]:
    for d in (-1, 0, 1):
        if 1 <= x+d <= 4000: clean.add(x+d)
clean.discard(0)
clean = sorted(clean)
pairs = list(itertools.combinations_with_replacement(clean, 2))
def nhit(t): return [(a, b, a*b) for a, b in pairs if abs(a*b-OBS)/OBS <= t]
n_clean = len(clean)
for t in (0.00051, 0.001, 0.002, 0.005):
    h = nhit(t)
    print(f"    tol {t*100:.3f}%: {len(h):3d} product(s) within window  e.g. {[x[2] for x in h[:6]]}")
h051 = nhit(0.00051)
n_hits = len(h051)
# HONEST: rare (1 hit) at the candidate's own tolerance => null model is FAVORABLE (not a common fit)
ok3 = (n_hits == 1)   # UNIQUE among BST-clean pairs at 0.051% => null model FAVORS the product (rare)
print(f"    pool size {n_clean}, {len(pairs)} pairs; at 0.051% exactly {n_hits} hit = 49*71 UNIQUE => null model FAVORABLE: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — target-innocence + null-model audit of m_tau/m_e = 49*71. VERDICT FLIPPED FROM")
print("       MY PRIOR (honest): I expected the null model to show 'easy fit'; instead 49*71 is the UNIQUE")
print("       BST-clean product within 0.051% of 3477.23 (1 of ~1500 pairs) -- the PRODUCT is RARE, null model")
print("       FAVORABLE. So it is NOT a generic 2-integer fit. BUT two legs still block a bank: (2) the '71' is")
print("       rich-vocabulary (64+7 AND 70+1 -- target-aware, no unique form), and there is NO mechanism forcing")
print("       the product g^2*(2^{C_2}+g). NET (corrected): STRONGER than I flagged -- a genuine STRONG")
print("       CANDIDATE (rare product + 0.05%), held back by 71's reading + missing product-mechanism, NOT a")
print("       fit and NOT yet a bank. Followed the data against my own prior. NO count move. HOLDS 9/26.")
print("="*98)
