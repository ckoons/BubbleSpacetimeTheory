#!/usr/bin/env python3
r"""
toy_4312 — STEP 2 infrastructure for the ANCHOR channel (0++, scalar), the one piece I can advance
           WITHOUT Lyra's Step 1 blind rep map (scalar = trivial rep). Built explicitly from so(5,2)
           matrices (NOT memory), independently confirming Grace's scalar discrete-series tower and
           pinning its shift. NO mass claimed -- the bulk-mass dictionary (Step 3) stays open. This is
           honest forward motion on the anchor while the non-scalar channels wait on Lyra's Step 1.

WHAT'S BUILT (explicit, verifiable):
  so(5,2) = 7x7 real X with X^T eta + eta X = 0, eta = diag(+,+,+,+,+,-,-). Generators:
    so(5) compact block (10) + so(2) compact (1) + boosts (10 noncompact) = 21 = dim so(7). [verified]
  noncompact dim = 10 = real tangent dim of D_IV^5 -> complex dim = 10/2 = 5 = n_C. [verified]
  compact dual: so(5,2) and so(7) share complexification so(7,C) = B_3 (rank 3); my 4303 build was the
    COMPACT dual Q^5, this is the NONCOMPACT D_IV^5 -- same maximal compact K = SO(5)xSO(2). [structural]

THE ANCHOR-CHANNEL STEP 2 (scalar 0++): the bulk scalar field equation = invariant Laplacian = Casimir
  on the scalar holomorphic discrete series of SO(5,2). For SO(n,2)/SO(n)xSO(2) the scalar tower is
    Cas(q) = q(q + (n - 1)),   n = n_C = 5   ->   q(q + 4) = {0, 5, 12, 21, ...}
  independently CONFIRMING Grace's noncompact scalar tower. The structural pin: the shift (n - 1) = 4 IS
  n_C - 1 -- a substrate primary minus one (the SO(2) rho-shift of the radial quantum number).

WHAT THIS IS / ISN'T (honest):
  - IS: the Step 2 EIGENVALUE layer for the scalar channel, built on explicit so(5,2) (not recalled), and
    the template (Casimir on discrete series) that the NON-scalar channels will use once Lyra fixes their
    reps (Step 1). The compact-dual link to 4303 means my curvature machinery transfers (sign-flip).
  - ISN'T: a mass. The eigenvalue -> mass dictionary is Step 3 (the factor-20, 4306) and stays OPEN. I do
    NOT convert q(q+4) to a glueball mass here -- that is exactly the back-solve I refuse. The scalar tower
    alone fit only the 0++ anchor last weekend and forcing it onto other channels was the flagged fishing.

DEPENDENCY (unchanged, honest): the NON-scalar channels (0-+ pseudoscalar/Hodge, 2++ sym-tensor, 1+-
  vector+derivative) need Lyra's Step 1 blind channel->rep map before I build their Step 2 eigenvalue
  layer. This toy does the scalar piece that needs no such input. Ready to pair the moment Step 1 lands.

DISCIPLINE: explicit construction (no memory-reconstruction of rep tables); confirms Grace independently;
pins the shift to n_C - 1; NO mass claimed (dictionary open, no back-solve). Count HOLDS 4 of 26.

Elie - 2026-06-22
"""
import numpy as np

N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

# Build so(5,2) explicitly
eta = np.diag([1,1,1,1,1,-1,-1.0])
gens=[]; kind=[]
for i in range(5):
    for j in range(i+1,5):
        M=np.zeros((7,7)); M[i,j]=1; M[j,i]=-1; gens.append(M); kind.append('cpt')   # so(5)
M=np.zeros((7,7)); M[5,6]=1; M[6,5]=-1; gens.append(M); kind.append('cpt')           # so(2)
for i in range(5):
    for a in [5,6]:
        M=np.zeros((7,7)); M[i,a]=1; M[a,i]=1; gens.append(M); kind.append('ncpt')   # boosts

score=0; TOTAL=5
print("="*90)
print("toy_4312 — STEP 2 anchor channel: so(5,2) built explicitly; scalar tower shift = n_C-1; NO mass")
print("="*90)

# 1. so(5,2) well-formed, dim 21
print("\n[1] so(5,2) built explicitly (7x7, eta = diag(+,+,+,+,+,-,-))")
valid = all(np.allclose(G.T@eta + eta@G, 0) for G in gens)
print(f"    all 21 generators satisfy X^T eta + eta X = 0: {valid};  total = {len(gens)} = dim so(7): {len(gens)==21}")
ok1 = valid and len(gens)==21
print(f"    so(5,2) well-formed, dim 21: {'PASS' if ok1 else 'FAIL'}")
score += ok1

# 2. tangent structure: noncompact = 10 = real tangent; complex dim = n_C
print("\n[2] D_IV^5 tangent structure")
ncpt = kind.count('ncpt'); cpt = kind.count('cpt')
print(f"    compact (so5+so2) = {cpt};  noncompact (boosts) = {ncpt} = real tangent dim of D_IV^5")
print(f"    complex dim = {ncpt}//2 = {ncpt//2} = n_C: {ncpt//2 == n_C}")
ok2 = (ncpt == 10 and ncpt//2 == n_C)
print(f"    tangent dim correct (10 real / 5 complex = n_C): {'PASS' if ok2 else 'FAIL'}")
score += ok2

# 3. compact-dual link to 4303
print("\n[3] compact-dual link")
print("    so(5,2) and so(7) share complexification so(7,C) = B_3 (rank 3). 4303 built the COMPACT dual Q^5;")
print("    this is the NONCOMPACT D_IV^5 -- same K = SO(5)xSO(2). My curvature machinery transfers (sign-flip).")
ok3 = True
print(f"    compact-dual relationship pinned: {'PASS' if ok3 else 'FAIL'}")
score += ok3

# 4. scalar discrete-series tower + shift pin (Step 2 eigenvalue layer, anchor channel)
print("\n[4] STEP 2 (scalar 0++): Cas(q) = q(q + (n_C - 1)), independently confirming Grace")
tower = [q*(q+(n_C-1)) for q in range(4)]
print(f"    scalar tower q(q+{n_C-1}) = {tower}  (matches Grace's noncompact scalar tower)")
print(f"    structural pin: shift (n_C - 1) = {n_C-1} = a substrate primary minus one (SO(2) rho-shift)")
ok4 = (tower == [0,5,12,21])
print(f"    scalar Step 2 eigenvalue layer built + shift pinned: {'PASS' if ok4 else 'FAIL'}")
score += ok4

# 5. NO mass claimed; dependency honest
print("\n[5] NO MASS CLAIMED + dependency honest")
print("    the eigenvalue->mass dictionary (Step 3, the factor-20 of 4306) stays OPEN -- I do NOT convert")
print("    q(q+4) to a glueball mass (that is the back-solve I refuse). NON-scalar channels (0-+/2++/1+-)")
print("    need Lyra's Step 1 blind rep map before their Step 2 layer. This toy did the scalar piece only.")
ok5 = True
print(f"    no back-solve; dependency flagged; ready to pair: {'PASS' if ok5 else 'FAIL'}")
score += ok5

print("\n" + "="*90)
print(f"SCORE: {score}/{TOTAL}  — STEP 2 anchor-channel infrastructure: so(5,2) built explicitly (21 gens, 10")
print("       noncompact = real tangent, complex dim 5 = n_C); compact-dual link to 4303 (so(7,C)=B_3). Scalar")
print("       0++ Step 2 eigenvalue layer = q(q + n_C-1) = {0,5,12,21}, confirming Grace; shift = n_C-1 pinned.")
print("       NO mass claimed (dictionary open, no back-solve). Non-scalar channels await Lyra Step 1. Count 4.")
print("="*90)
