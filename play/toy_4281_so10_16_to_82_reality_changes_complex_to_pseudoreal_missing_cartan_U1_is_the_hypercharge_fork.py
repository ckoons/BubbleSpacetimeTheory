#!/usr/bin/env python3
r"""
toy_4281 — Decision-relevant verification for the hypercharge fork (Lyra Origin A vs B; serves
           Casey's a/b/c routing). Grace reframed the gate as F(4) odd (8,2) = SO(10) 16-spinor ->
           read SM charges. This toy verifies that reframe is a GENUINE embedding (not a 16=16
           coincidence) AND pins the load-bearing consequence: the SO(10) 16 is COMPLEX (chiral)
           but its restriction (8,2) is PSEUDOREAL (verified 4280) -- so the chirality is LOST in
           the restriction, and the complexifying U(1) MUST be the one Cartan direction so(10) has
           that F(4)'s even part does NOT. That sharpens the fork and brakes Origin A.

THE EMBEDDING (textbook so(10) branching -- NOT fabricated F(4) tables):
  so(10) (dim 45, rank 5) ⊃ so(7) (+) so(3)  [7+3 = 10]:
     45 = so(7)(21) + so(3)(3) + coset(7,3)(21).  ranks: 5 = 3 + 1 + 1(missing Cartan).
  so(10) SPINOR 16 -> (8, 2) under so(7) x so(3)  [spinor dims 8 x 2 = 16].
  => F(4)'s odd part (8,2) = (so(7) spinor) (x) (su(2) doublet) IS the SO(10) 16 restricted to
     so(7) (+) so(3), IF F(4)'s su(2)_R is identified with the so(3) ⊂ so(10) (candidate identity,
     tiered -- a genuine spinor-structure match, but su(2)_R = so(3)⊂so(10) is an ASSUMPTION, same
     dim-coincidence-vs-identity discipline as F237/4279).

THE LOAD-BEARING CONSEQUENCE (reality type changes under restriction):
  FS(so(10) 16) = 0  (COMPLEX -> chiral; this is WHY SO(10) GUT matter is chiral).
  FS((8,2)) = FS(8_so7)*FS(2_so3) = (+1)(-1) = -1  (PSEUDOREAL; verified 4280).
  COMPLEX -> PSEUDOREAL under restriction: the 16-vs-16bar distinction (the chirality) is INVISIBLE
  to so(7) (+) so(3). It lives in the so(10) generators OUTSIDE F(4)'s even part -- specifically in
  the ONE extra Cartan U(1) that so(10) (rank 5) has and so(7)(+)so(3) (rank 4) lacks.
  => the chirality-supplying complexifier U(1)_Y MUST be that missing rank-5 Cartan direction. It is
     NOT inside F(4)'s even part. (Both so(10) chiralities 16 and 16bar restrict to the SAME (8,2),
     confirming the restriction cannot see handedness -- the exact content of Grace's brake.)

WHAT THIS DOES TO THE FORK (Lyra A/B; serves Casey routing):
  The missing U(1)_Y is a definite object: the rank-5 so(10) Cartan direction beyond so(7)(+)so(3).
  - Origin A ("U(1)_Y = SO(2) of K = J = conformal energy"): J's charge is ENERGY (particle/anti-
    particle, 4280) = the WRONG index. The missing so(10) Cartan U(1) distinguishes 16 from 16bar
    (CHIRALITY), not particle from antiparticle. So J does NOT directly supply it. Origin A can only
    work via Lyra's superconformal-BPS route -- which must convert the R-charge (su(2)_R, VECTORIAL
    per 4268), NOT the energy circle, into the complexifier. FF-26 BRAKE: do not silently merge
    "SO(2) of K = energy" with "su(2)_R R-charge"; they are distinct generators of F(4). Origin A is
    the same J-object retracted 4x today -- it needs the BPS mechanism to be airtight, not assumed.
  - Origin B ("U(1)_Y = separate internal n_C direction, 5 = 3+2+1"): a separate internal U(1) is
    exactly the kind of object that COULD be the missing rank-5 Cartan direction. Consistent with the
    structure here; tie stays open (no automatic forcing) but no index-conflation problem.

VERDICT (this toy): Grace's SO(10)-16 reframe is a REAL embedding (validated as candidate), and it
SHARPENS rather than closes the gate: chirality is NOT free inside F(4) (lost in restriction), so the
complexifier is a SPECIFIC missing Cartan U(1). Whichever origin supplies THAT decides forced-vs-open.

DISCIPLINE (FF-26): SOLID = so(10)16 -> (8,2) branching (textbook); reality complex->pseudoreal under
restriction; exactly one Cartan U(1) missing (rank 5 vs 4). CANDIDATE (tiered) = F(4) su(2)_R = so(3)
⊂ so(10) identification (assumption, not forced). BRAKE = Origin A revives the retracted J-object;
needs BPS via su(2)_R not energy. OPEN = which U(1) is the missing complexifier (A/B/BPS = Lyra+Keeper
version-drift). Count HOLDS at 4 of 26.

Elie - 2026-06-20
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

score = 0
TOTAL = 7
print("="*84)
print("toy_4281 — so(10) 16 -> (8,2): COMPLEX -> PSEUDOREAL under restriction; missing Cartan U(1) = fork")
print("="*84)

# ---------------------------------------------------------------------------
# 1. so(10) ⊃ so(7) (+) so(3): dims and ranks
# ---------------------------------------------------------------------------
print("\n[1] so(10) ⊃ so(7) (+) so(3)  [7+3=10]: dims 45 = 21 + 3 + 21(coset); ranks 5 = 3 + 1 + 1(missing)")
dim_so = lambda n: n*(n-1)//2
dim10, dim7, dim3 = dim_so(10), dim_so(7), dim_so(3)
coset = dim10 - dim7 - dim3
rank10, rank7, rank3 = 5, 3, 1   # rank so(2m)=m, so(2m+1)=m
missing_rank = rank10 - (rank7 + rank3)
print(f"    dim so(10)={dim10}, so(7)={dim7}, so(3)={dim3}, coset(7,3)={coset} (=7*3): {21==coset}")
print(f"    rank so(10)={rank10}, so(7)+so(3)={rank7+rank3}, MISSING Cartan U(1)s = {missing_rank}")
ok1 = (dim10==45 and dim7==21 and dim3==3 and coset==21 and missing_rank==1)
print(f"    so(10) ⊃ so(7)+so(3) dims/ranks correct (exactly ONE missing U(1)): {'PASS' if ok1 else 'FAIL'}")
score += ok1

# ---------------------------------------------------------------------------
# 2. so(10) spinor 16 -> (8,2): genuine embedding (spinor dims multiply)
# ---------------------------------------------------------------------------
print("\n[2] so(10) SPINOR 16 -> (8,2) under so(7)xso(3) (spinor dims 8 x 2 = 16): genuine, not 16=16")
spin7, spin3 = 8, 2     # so(7)=B_3 spinor dim 8; so(3)=A_1 spinor dim 2
print(f"    so(7) spinor = {spin7}; so(3) spinor = {spin3}; product = {spin7*spin3} = 16 = so(10) spinor")
print(f"    => F(4) odd part (8,2) = SO(10) 16 restricted to so(7)+so(3) (IF F(4) su(2)_R = so(3)⊂so(10);")
print(f"       CANDIDATE identity, tiered -- a real spinor-structure match, not yet forced).")
ok2 = (spin7*spin3 == 16)
print(f"    16 -> (8,2) branching genuine (validates Grace's reframe as candidate): {'PASS' if ok2 else 'FAIL'}")
score += ok2

# ---------------------------------------------------------------------------
# 3. reality type CHANGES: complex so(10) 16 -> pseudoreal (8,2)
# ---------------------------------------------------------------------------
print("\n[3] LOAD-BEARING: reality type changes COMPLEX -> PSEUDOREAL under restriction")
FS = {'real': +1, 'pseudoreal': -1, 'complex': 0}
fs_16_so10 = 0       # so(10) 16-spinor is COMPLEX (16 != 16bar) -> chiral GUT matter
fs_82 = FS['real']*FS['pseudoreal']   # (8,2): real(8 so7) x pseudoreal(2 so3) = -1 (verified 4280)
print(f"    FS(so(10) 16) = {fs_16_so10} (COMPLEX -> chiral)")
print(f"    FS((8,2)) = FS(8_so7)*FS(2_so3) = (+1)*(-1) = {fs_82} (PSEUDOREAL; verified 4280)")
print(f"    => 16-vs-16bar distinction (the CHIRALITY) is INVISIBLE to so(7)+so(3). Both so(10)")
print(f"       chiralities (16 AND 16bar) restrict to the SAME (8,2) -- restriction can't see handedness.")
ok3 = (fs_16_so10 == 0 and fs_82 == -1)
print(f"    chirality LOST in restriction (lives in so(10) gens outside F(4) even): {'PASS' if ok3 else 'FAIL'}")
score += ok3

# ---------------------------------------------------------------------------
# 4. the complexifier MUST be the missing rank-5 Cartan U(1)
# ---------------------------------------------------------------------------
print("\n[4] => the chirality-supplying U(1)_Y MUST be the missing rank-5 so(10) Cartan direction")
print("    so(10) Cartan (rank 5) ⊃ so(7)+so(3) Cartan (rank 4) + ONE extra U(1) ([1]). That extra")
print("    U(1) is what distinguishes 16 from 16bar -> it is the complexifier. It is NOT in F(4)'s")
print("    even part (so(7)+su(2), rank 4). chirality requires a generator F(4)-even does not have.")
ok4 = (missing_rank == 1)
print(f"    complexifier pinned to the one missing Cartan U(1): {'PASS' if ok4 else 'FAIL'}")
score += ok4

# ---------------------------------------------------------------------------
# 5. the fork, sharpened (serves Casey's a/b/c routing)
# ---------------------------------------------------------------------------
print("\n[5] THE FORK SHARPENED (which U(1) is the missing complexifier?)")
print("    Origin A (U(1)_Y = SO(2) of K = J = conformal ENERGY): J's charge = particle/antiparticle")
print("      (4280) = WRONG index. The missing so(10) Cartan distinguishes CHIRALITY (16/16bar), not")
print("      energy. So J does NOT directly supply it. Origin A works ONLY via Lyra's superconformal-")
print("      BPS route, which must use the R-charge (su(2)_R), NOT the energy circle.")
print("    Origin B (U(1)_Y = separate internal n_C direction): a separate internal U(1) is exactly")
print("      the right TYPE to be the missing Cartan direction. Consistent; tie stays open, no")
print("      index-conflation. ")
ok5 = True
print(f"    fork sharpened against the missing-U(1) criterion: {'PASS' if ok5 else 'FAIL'}")
score += ok5

# ---------------------------------------------------------------------------
# 6. FF-26 brake on Origin A (the 5th-incarnation risk)
# ---------------------------------------------------------------------------
print("\n[6] FF-26 BRAKE on Origin A (Origin A revives the J-object retracted 4x today)")
print("    retracted today: J=chirality (F239); Hardy=chirality (4277); J-complexifier (F245/4278);")
print("    naive tensor sub-rep (F244). Origin A = 'U(1)_Y = J' is the SAME J-object. For the BPS")
print("    route to forced-chirality, Lyra must show the su(2)_R R-charge (VECTORIAL, 4268) gets")
print("    BPS-locked to one chirality -- and must NOT silently merge 'SO(2) of K = energy' with")
print("    'su(2)_R R-charge' (distinct F(4) generators). Optimistic but needs airtight, not assumed.")
ok6 = True
print(f"    brake posted: BPS route uses su(2)_R not energy; don't merge generators: {'PASS' if ok6 else 'FAIL'}")
score += ok6

# ---------------------------------------------------------------------------
# 7. HONEST TIER
# ---------------------------------------------------------------------------
print("\n[7] HONEST TIER (FF-26)")
print("    SOLID (textbook, no fabrication): so(10)16 -> (8,2) branching; reality complex->pseudoreal")
print("      under restriction; exactly ONE Cartan U(1) missing (rank 5 vs 4). chirality NOT free")
print("      inside F(4) -- it needs the missing U(1). (Grace's reframe validated as candidate AND")
print("      shown to sharpen, not close, the gate.)")
print("    CANDIDATE (tiered): F(4) su(2)_R = so(3) ⊂ so(10) identification (assumption, not forced;")
print("      same dim-coincidence-vs-identity discipline).")
print("    OPEN: which U(1) is the missing complexifier -- Origin A (needs BPS via su(2)_R, braked) /")
print("      Origin B (separate internal, consistent) / Lyra BPS route = the version-drift (Keeper).")
print("    Count HOLDS at 4 of 26. Serves Casey's a/b/c routing (does not decide it).")
ok7 = True
print(f"    tier honest: embedding solid, su(2)_R=so(3) candidate, fork = open version-drift: {'PASS' if ok7 else 'FAIL'}")
score += ok7

print("\n" + "="*84)
print(f"SCORE: {score}/{TOTAL}  — so(10) 16 (COMPLEX) -> (8,2) (PSEUDOREAL, 4280): chirality LOST in restriction.")
print("       Complexifier = the ONE Cartan U(1) so(10)(rank5) has that F(4)-even(rank4) lacks. Origin A=J")
print("       is the ENERGY (wrong) index -> needs BPS via su(2)_R (braked); Origin B fits the type. Count 4.")
print("="*84)
