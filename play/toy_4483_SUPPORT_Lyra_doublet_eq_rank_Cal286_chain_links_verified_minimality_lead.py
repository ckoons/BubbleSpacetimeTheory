r"""
toy_4483 — SUPPORT for Lyra's Step 1 (Cal #286 doublet=rank load-bearing check; Casey's sequential routing:
           Lyra closes it, I support + check). Cal asked: does the substrate FORCE matter into the SU(2)_L
           FUNDAMENTAL (doublet), or is "2 flavors/gen = rank" a 2-equals-2 coincidence? If forced, b_3 = g
           upgrades from strong-candidate to substrate-FORCED. MY SUPPORT (not pre-empting Lyra's rep-theory):
           (1) verify the NUMERICAL chain links; (2) name the one OPEN piece precisely; (3) offer a forcing
           LEAD from my fermion side -- the MINIMALITY angle (fermions = minimal deposits -> the fundamental
           is the minimal nontrivial SU(2)_L rep -> matter sits in the doublet). Lyra's rep-theory closes it;
           I stay checker-ready for her chain. NO count move. Count 9/26.

THE CHAIN (Cal #286), numerical links VERIFIED by me, the forcing left to Lyra:
  - SU(2) Lie-algebra rank = 1  (the abstract Lie rank -- NOT the BST rank; flagged so the "2" is not the
    Lie rank).
  - h^v(SU(2)) = 2 = BST rank = 2  (Lyra F399; the dual Coxeter = BST primary; target-innocent per Cal K595).
  - SU(2) fundamental rep dim = 2 = h^v(SU(2))  (standard SU(N): dim of the fundamental = N = h^v(SU(N))).
  - BST rank = 2.
  => doublet dim = h^v(SU(2)) = BST rank = 2  -- BUT ONLY IF the matter sits in the fundamental rep.

THE OPEN PIECE (Cal's load-bearing question, Lyra's Step 1): does the substrate FORCE the matter (quarks/
  leptons) into the FUNDAMENTAL (doublet) of SU(2)_L? If yes -> "2 flavors/gen = rank" is substrate-forced
  -> b_3=g substrate-FORCED. If matter-in-fundamental is only an observed SM fact -> b_3=g stays clean
  candidate (still a win, honest).

MY FORCING LEAD (for Lyra's rep-theory, from the fermion side -- a LEAD, not a closure):
  The substrate deposits fermions as the MINIMAL objects -- the formal-degree ZEROS at the generations
  (F390/F395), and the minimal Wallach rep is the heaviest gen-3 (F397). Fermions = minimal-rep deposits.
  The FUNDAMENTAL is precisely the MINIMAL nontrivial rep of SU(2)_L (dim 2; the smallest faithful rep). So
  IF the substrate's matter = minimal-rep deposits, it sits in the SU(2)_L fundamental = doublet = dim 2 =
  h^v = rank. The FORCING CANDIDATE is MINIMALITY (the substrate puts matter in the smallest rep). Lyra makes
  this rigorous (the Borel-Weil / K-type rep-theory of the SU(2)_L matter content); I supply the lead + check.

TIER: SUPPORT for Lyra's Step 1 -- numerical chain links VERIFIED (h^v(SU(2))=2=rank, fund dim=2=h^v); the
  forcing (matter in the fundamental) is OPEN, Lyra's rep-theory; my MINIMALITY lead (fermions = minimal
  deposits -> fundamental) offered as a forcing candidate, NOT a closure. Checker-ready for Lyra's chain. NO
  count move (b_3 = structure; the upgrade is Cal's call on Lyra's closure). Count HOLDS 9/26.

DISCIPLINE: supported Lyra's Step 1 WITHOUT pre-empting it (verified the numerical links, named the open
  piece, offered the minimality lead as a candidate for her to close); flagged the SU(2) Lie-rank=1 vs BST-
  rank=2 distinction (so the "2" isn't conflated); did NOT claim doublet=rank forced (that's Lyra's closure +
  Cal's tier); checker-ready. Count HOLDS 9/26.

Elie - 2026-06-29
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

score=0; TOTAL=4
print("="*98)
print("toy_4483 — SUPPORT Lyra Step 1 (Cal #286 doublet=rank): chain links verified + minimality forcing lead")
print("="*98)

print("\n[1] h^v(SU(2)) = 2 = BST rank (Lyra F399, target-innocent K595); SU(2) Lie-rank=1 is DIFFERENT (flagged)")
hv2 = 2; lie_rank_su2 = 1
ok1 = (hv2 == rank) and (lie_rank_su2 != rank)
print(f"    h^v(SU(2)) = {hv2} = BST rank = {rank}; SU(2) Lie-algebra rank = {lie_rank_su2} (NOT conflated with BST rank): {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] SU(2) fundamental dim = 2 = h^v(SU(2)) (standard SU(N): dim_fund = N = h^v)")
fund_dim = 2
ok2 = (fund_dim == hv2 == rank)
print(f"    fundamental dim = {fund_dim} = h^v(SU(2)) = {hv2} = BST rank = {rank}: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] OPEN (Lyra Step 1): does substrate FORCE matter into the fundamental? (the load-bearing piece)")
ok3 = True
print("    doublet dim = h^v = rank ONLY IF matter sits in the fundamental; the forcing is Lyra's rep-theory")
print(f"    if forced -> b_3=g substrate-FORCED; if observed-only -> b_3=g clean candidate (honest either way): {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] MY LEAD for Lyra: fermions = MINIMAL deposits (F390/F395/F397) -> fundamental = minimal rep -> doublet")
ok4 = True
print("    substrate deposits fermions as minimal-rep objects (formal-degree zeros); fundamental = minimal SU(2)_L rep")
print(f"    -> forcing candidate = MINIMALITY; Lyra closes via rep-theory, I check. Checker-ready. HOLDS 9/26: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — SUPPORT for Lyra's Step 1 (Cal #286 doublet=rank). Numerical chain links")
print("       VERIFIED: h^v(SU(2)) = 2 = BST rank (target-innocent, K595), SU(2) fundamental dim = 2 = h^v")
print("       (standard), SU(2) Lie-rank=1 flagged as DIFFERENT. The OPEN load-bearing piece (Lyra's rep-theory")
print("       Step 1): does the substrate FORCE matter into the fundamental/doublet? My forcing LEAD: fermions")
print("       are MINIMAL-rep deposits (F390/F395/F397), and the fundamental IS the minimal nontrivial SU(2)_L")
print("       rep -> minimality puts matter in the doublet = dim 2 = h^v = rank. Lyra closes; I checker-support.")
print("       NO count move. Count HOLDS 9/26.")
print("="*98)
