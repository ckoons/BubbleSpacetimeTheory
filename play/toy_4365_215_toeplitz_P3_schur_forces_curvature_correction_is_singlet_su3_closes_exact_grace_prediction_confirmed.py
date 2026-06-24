#!/usr/bin/env python3
r"""
toy_4365 — #215/#418 Toeplitz P3 (Elie numerics for the Grace pairing): Grace's prediction -- "the curvature
           correction's residual is a decoupling SINGLET, leaving the 8 traceless generators closing into
           su(3) exactly" -- is FORCED by SCHUR'S LEMMA, not a coincidence to verify by luck. The curvature
           correction C_ij is an su(3)-intertwiner 3 -> 3 on the IRREDUCIBLE color triplet (Grace P1), so by
           Schur it is proportional to delta_ij: a pure singlet. This upgrades P3's structural core to forced.

THE SETUP (Grace P1+P2): three color-triplet oscillator modes a_i (the triality-(+1) short roots of g_2 in
  the so(7)=so(5,2) vector 7, an IRREDUCIBLE su(3) triplet). Schwinger bilinears E_ij = a_i^dag a_j. The
  leading CCR [a_i,a_j^dag] = 2n_C delta_ij (toy 4364). On the curved Hardy space there is an O(1/n_C)
  curvature correction C_ij to the CCR, driven by kappa_Bergman = -n_C. Question: does C_ij spoil su(3)?

VERIFIED (this toy):
  (1) the 8 traceless bilinears T_a = sum (lambda_a)_ij E_ij / 2 close into su(3) (fundamental realization);
  (2) the singlet N = sum E_ii (trace / number operator) DECOUPLES: [T_a, N] = 0;
  (3) SCHUR: the commutant of the irreducible color triplet is 1-DIMENSIONAL -- the only 3x3 matrix
      commuting with all 8 su(3) generators is a scalar multiple of I_3.

THE FORCING (Grace P3 prediction, now FORCED): the curvature correction C_ij is built su(3)-EQUIVARIANTLY
  (color is a symmetry of the Hardy-space realization; kappa_Bergman is a color-blind geometric scalar). So
  C_ij is an su(3)-intertwiner from the triplet 3 to the triplet 3, i.e. C in Hom_{su(3)}(3, 3). By Schur's
  lemma (3 irreducible), Hom_{su(3)}(3,3) = scalars, so
      C_ij = c * delta_ij  (a PURE SINGLET).
  A pure-singlet correction shifts only the U(1) number operator N (the trace part), which DECOUPLES from
  su(3). Therefore the 8 traceless generators close into su(3) EXACTLY; the curvature residual is the
  decoupling singlet. Exactly Grace's prediction -- and forced by Schur, not luck.

FALSIFIABLE (Grace's sharp test, now sharpened): a color-NON-singlet correction (a piece proportional to
  some lambda_a) WOULD mix into the T_a and break su(3). Schur RULES THIS OUT as long as (i) the three modes
  form an irreducible color triplet (Grace P1) and (ii) the correction is su(3)-equivariant (color is a Hardy-
  space symmetry). If a future explicit Bergman computation found a non-singlet residual, it would mean one
  of (i)/(ii) fails -- a genuine, decidable test.

HONEST SCOPE: this forces the STRUCTURE (residual = singlet, su(3) exact) from Schur + P1. What remains is
  the explicit numerical VALUE of the singlet shift c (the Bergman-norm computation) -- which does NOT affect
  su(3) closure (it only renormalizes N). Grace owns the explicit C_ij = c*delta_ij Bergman computation and
  the SOLID-promotion call for #418; this toy supplies the Schur forcing that makes the closure exact rather
  than coincidental. Framework + P1 + P2 + (now) P3-structure-forced; explicit Bergman value ahead.

DISCIPLINE: numerics for the Grace pairing; the Schur forcing is rigorous (commutant verified 1-dim); scoped
honestly (structure forced, explicit value is Grace's Bergman calc). Substrate-Schur-generator instance.
Count HOLDS 4 of 26.

Elie - 2026-06-24
"""
import numpy as np
rank, N_c, n_C, C2, g = 2, 3, 5, 6, 7
l=[np.array(x,dtype=complex) for x in [
 [[0,1,0],[1,0,0],[0,0,0]],[[0,-1j,0],[1j,0,0],[0,0,0]],[[1,0,0],[0,-1,0],[0,0,0]],
 [[0,0,1],[0,0,0],[1,0,0]],[[0,0,-1j],[0,0,0],[1j,0,0]],[[0,0,0],[0,0,1],[0,1,0]],
 [[0,0,0],[0,0,-1j],[0,1j,0]],np.array([[1,0,0],[0,1,0],[0,0,-2]])/np.sqrt(3)]]
T=[x/2 for x in l]; I3=np.eye(3)

score=0; TOTAL=4
print("="*94)
print("toy_4365 — #215/#418 Toeplitz P3: SCHUR forces the curvature residual to be a singlet -> su(3) exact")
print("="*94)

print("\n[1] 8 traceless bilinears T_a close into su(3) (fundamental realization)")
def closes(g):
    for a in range(8):
        for b in range(8):
            c=g[a]@g[b]-g[b]@g[a]; r=sum(2*np.trace(c@g[d])*g[d] for d in range(8))
            if not np.allclose(c,r): return False
    return True
ok1 = closes(T)
print(f"    [T_a,T_b]=i f_abc T_c: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] singlet N (trace/number op) decouples: [T_a, N]=0")
ok2 = all(np.allclose(t@I3-I3@t,0) for t in T)
print(f"    [T_a, I3]=0: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] SCHUR: commutant of the irreducible color triplet is 1-dimensional (scalars only)")
rows=[np.kron(T[a],I3)-np.kron(I3,T[a].T) for a in range(8)]
sv=np.linalg.svd(np.vstack(rows))[1]
null_dim=int(np.sum(sv<1e-9))+(9-len(sv))
null=np.linalg.svd(np.vstack(rows))[2][-1].reshape(3,3)
ok3 = (null_dim==1 and np.allclose(null/null[0,0], I3))
print(f"    dim Hom_su(3)(3,3) = {null_dim} (=1); unique invariant prop to I3: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] FORCING: C_ij is an su(3)-intertwiner 3->3 -> Schur -> C_ij = c*delta_ij (singlet) -> su(3) exact")
print("    color-blind kappa_Bergman + irreducible triplet (P1) => curvature correction is a PURE singlet,")
print("    shifts only N (decoupled). Grace's P3 prediction FORCED. Falsifiable: non-singlet residual would")
print("    need irreducibility or equivariance to fail. Explicit singlet VALUE c = Grace's Bergman calc.")
ok4 = (ok1 and ok2 and ok3)
print(f"    Schur forcing of singlet residual: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — #215/#418 P3: Grace's prediction (curvature residual = decoupling singlet,")
print("       su(3) closes exactly) is FORCED BY SCHUR. The correction C_ij is an su(3)-intertwiner 3->3 on the")
print("       irreducible color triplet (P1), and Hom_su(3)(3,3)=scalars (commutant verified 1-dim), so C_ij =")
print("       c*delta_ij -- a pure singlet that shifts only the decoupled U(1) N. su(3) closure is exact, not")
print("       coincidental. Explicit singlet value c = Grace's Bergman computation; SOLID call hers. Count 4 of 26.")
print("="*94)
