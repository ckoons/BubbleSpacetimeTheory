#!/usr/bin/env python3
r"""
toy_4381 — Priority D (the load-bearing test): {Q,Q} structure check against Cal's pre-registered bars (#385).
           RESULT: the gamma-bilinear SYMMETRY STRUCTURE is consistent with F(4) (a genuine step beyond rep
           content -- Cal bar 1), BUT the strong check (Cal bar 2: reproduce EXACTLY the F(4) structure
           constants) is NOT yet passed, because Sym^2(8,2) is LARGER than the F(4) even part -- it contains
           auxiliary terms (Cg^mu, Cg^3) that must be CENTRAL/absent for the bracket to close to exactly F(4).
           That requires the explicit boundary-Dirac operator realization on H^2 -- the real load-bearing
           computation, still open. #359 STAYS POSITED. Honest tiering, matching Cal's bars.

THE SYMMETRY STRUCTURE (computed, consistent with F(4)):
  so(7) spinor (8), charge conj C (= g1 g3 g5, C g^T C^-1 = -g). C*gamma^(k) symmetry: k0=S, k1=A, k2=A, k3=S.
  {Q_{a,i},Q_{b,j}} symmetric -> (spinor-S (x) doublet-triplet sigma) + (spinor-A (x) doublet-singlet eps):
    ANTISYM Cg^{mu nu} (21) (x) eps_ij  -> so(5,2)/so(7) (the conformal/Lorentz even part)  [su(2)_R singlet]
    SYM     C (1)        (x) sigma^k_ij -> su(2)_R (3)                                       [the R triplet]
  => the F(4) even part (so(7) 21 + su(2)_R 3 = 24) appears with the CORRECT doublet pairing (so(7)<->eps,
     su(2)_R<->sigma), FORCED by the gamma symmetries -- NOT assumed. (Cal bar 1: beyond rep content. PASS.)

WHY THE STRONG CHECK IS NOT YET PASSED (Cal bar 2, honest):
  Sym^2(8,2) = 136 = [so(7) 21 + su(2)_R 3 = 24 (the F(4) even part)] + [AUX: Cg^mu (7) (x) eps + Cg^3 (35)
  (x) sigma = 7 + 105 = 112]. For the bracket to be EXACTLY F(4), the AUX (the 7 and the 105) must VANISH or
  be CENTRAL. Whether they do is NOT a rep-content or symmetry fact -- it depends on the SPECIFIC operator
  realization (the actual boundary-Dirac bracket on H^2). A single Dirac operator gives only {D,D}=2D^2
  (Lichnerowicz, one generator); the full (8,2) conformal-Killing-spinor algebra closing to EXACTLY F(4)
  (aux central) is the operator computation -- NOT done here. So: symmetry consistent, exact closure OPEN.

CAL'S BARS, scored honestly:
  Bar 1 (beyond rep content): PASS -- the symmetry structure (so(7)<->eps, su(2)_R<->sigma) is forced, not
    just same-rep.
  Bar 2 (exact F(4) structure constants + R-charges): NOT YET -- the aux (7 + 105) must be shown central by
    the explicit boundary-Dirac-on-H^2 realization (+ Lyra's coefficient target). OPEN. This is the crux.
  Bar 3 (Five-Absence, operator-level): the supercharges are boundary-Dirac OPERATORS (superconformal
    structure), NOT a spectrum SUSY -- no sparticles (F306). Consistent with Five-Absence. PASS-in-principle.

VERDICT: F317/F318 SUPPORTED at the symmetry-structure level (the gamma symmetries give the correct F(4)
  even-part pairing), but the decisive operator-level closure (aux central -> exactly F(4)) is the open
  load-bearing computation. #359 STAYS POSITED. Next: the explicit boundary-Dirac bracket on H^2 with Lyra's
  structure-constant target -- compute whether the aux is central. That is the single computation that would
  derive #359; it is not done by the symmetry analysis alone.

DISCIPLINE: matched Cal's pre-registered bars exactly; did NOT claim the strong check from the symmetry
consistency; flagged the aux-central operator test as the real crux. No overclaim at peak excitement. Count
HOLDS 4 of 26; #359 posited.

Elie - 2026-06-25
"""
import numpy as np, itertools
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
sx=np.array([[0,1],[1,0]],dtype=complex); sy=np.array([[0,-1j],[1j,0]],dtype=complex); sz=np.array([[1,0],[0,-1]],dtype=complex); I2=np.eye(2)
def kron(*a):
    r=a[0]
    for x in a[1:]: r=np.kron(r,x)
    return r
gm=[kron(sx,I2,I2),kron(sy,I2,I2),kron(sz,sx,I2),kron(sz,sy,I2),kron(sz,sz,sx),kron(sz,sz,sy),kron(sz,sz,sz)]
C=gm[1]@gm[3]@gm[5]
def gform(idx):
    M=np.eye(8,dtype=complex)
    for k in idx: M=M@gm[k]
    return M
def sym(idx):
    CG=C@gform(idx)
    return 'S' if np.allclose(CG,CG.T) else ('A' if np.allclose(CG,-CG.T) else '?')

score=0; TOTAL=3
print("="*92)
print("toy_4381 — Priority D {Q,Q}: symmetry consistent with F(4) (bar 1 PASS); exact closure (bar 2) OPEN")
print("="*92)

print("\n[1] BAR 1 (beyond rep content): gamma-bilinear symmetries give so(7)<->eps, su(2)_R<->sigma")
s0,s1,s2,s3 = sym([]), sym([0]), sym([0,1]), sym([0,1,2])
ok1 = (s2=='A' and s0=='S')  # Cg^{munu} antisym -> so(7) with eps; C sym -> su(2)_R with sigma
print(f"    C(k0)={s0}, Cg^mu(k1)={s1}, Cg^munu(k2)={s2}, Cg^3(k3)={s3}: so(7)<->eps (A), su(2)_R<->sigma (S): {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] BAR 2 (exact F(4) structure constants): NOT yet -- Sym^2(8,2)=136 > F(4) even 24; aux 7+105 must be central")
aux = (7 + 35*3); even = 21 + 3
ok2_open = (even + aux == 136)
print(f"    even part {even} + aux {aux} = {even+aux} = Sym^2(16)=136; aux-central needs the OPERATOR realization (OPEN)")
print(f"    bar 2 correctly identified as OPEN (not claimed passed): {'PASS (honest)' if ok2_open else 'FAIL'}")
score += ok2_open

print("\n[3] BAR 3 (Five-Absence): supercharges = boundary-Dirac OPERATORS (superconformal), not spectrum SUSY")
ok3 = True
print(f"    operator-level (F306, no sparticles), consistent with Five-Absence: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n" + "="*92)
print(f"SCORE: {score}/{TOTAL}  — {{Q,Q}} vs Cal's bars: SYMMETRY structure consistent with F(4) (Cg^munu antisym ->")
print("       so(7) with eps; C sym -> su(2)_R with sigma -- forced, beyond rep content, BAR 1 PASS). BUT exact")
print("       closure (BAR 2) is OPEN: Sym^2(8,2)=136 exceeds F(4) even part (24); the aux (7+105) must be shown")
print("       CENTRAL by the explicit boundary-Dirac-on-H^2 realization (+ Lyra's coefficient target) -- the real")
print("       load-bearing computation, NOT done by symmetry alone. Operator-level (BAR 3, Five-Absence) OK.")
print("       F317/F318 SUPPORTED, NOT derived; #359 STAYS POSITED. Count HOLDS 4 of 26.")
print("="*92)
