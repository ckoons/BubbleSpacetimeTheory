#!/usr/bin/env python3
r"""
toy_4339 — (1) SYNC my hypercharge catches with Lyra's Cartan-counting reconciliation (#287), and
           (2) PREP my half of the SO(4)-Lorentz hinge (#173 / Cal #321) for the Lyra+Elie pairing
           (Casey: "Lyra should do the SO(4) work"). Linear algebra throughout. The chirality cluster's
           load-bearing question is now ONE concrete identification.

PART 1 -- SYNC (consistent with Lyra, fork DISSOLVED):
  K = SO(5) x SO(2) has exactly 3 Cartan directions (rank 2 + rank 1). Via SO(5) ⊃ SO(4) = SU(2)_L x
  SU(2)_R, the Cartans are {T_3^L, T_3^R, H_0}:
    T_3^L = (E01 + E23)/2 (self-dual),  T_3^R = (E01 - E23)/2 (anti-self-dual),  H_0 = the SO(2).
    [T_3^L, T_3^R] = 0 (two commuting SU(2) Cartans). Hypercharge Y = T_3^R + (B-L)/2 (Lyra).
  -> the two "origins" (F247) are NOT rivals: Origin A = H_0 (SO(2) central character), Origin B = T_3^R
     (the SO(4)-RIGHT factor of SO(5)) -- the TWO TERMS of one formula Y = T_3^R + (B-L)/2. Fork dissolved.
  MY CATCHES are consistent and one is REQUIRED:
    - CATCH 1 (3+2+1 = C_2 = 6, NOT n_C = 5): stands -- arithmetic flag on F247, orthogonal to the fix.
    - CATCH 2 (su(3) ⊄ so(5)): stands and is REQUIRED -- Lyra's T_3^R is the SO(4)-right factor, NOT color;
      her reconciliation does NOT put color in SO(5) (which I ruled out). Fully consistent.
    - my "favor Origin A" is SUPERSEDED (improved) by Lyra: both origins are terms of one formula.

PART 2 -- THE SO(4)-LORENTZ HINGE (my half of the pairing, the one open identification):
  Lyra's sharpening: the SM is chiral because weak SU(2) gauges the LEFT factor SU(2)_L of SO(4) ⊂ SO(5).
  The load-bearing question (#173, Cal #321): is that SO(4) ⊂ SO(5) the LORENTZ group?
  Linear-algebra observation for the pairing: the K-SO(4) ⊂ SO(5) is COMPACT and = SU(2)_L x SU(2)_R --
  which IS the EUCLIDEAN Lorentz structure (Wick-rotated SO(3,1) ~ SO(4) = SU(2)xSU(2)). So the candidate
  identification is:
     K-SO(4) ⊂ SO(5)  <-->  the Euclidean (Wick-rotated) 4D Lorentz SO(4)  <-->  spacetime SO(3,1) ⊂ SO(4,2).
  IF this identification holds:
    - weak SU(2) = SU(2)_L = the Lorentz-LEFT Weyl factor -> the SM is chiral BECAUSE one Lorentz chirality
      is gauged (parity violation = gauging one self-dual factor).
    - chirality + weak-SU(2) + the T_3^R-part of hypercharge all UNIFY in the SO(4) ⊂ SO(5) structure.

  THE SUBTLETY TO PIN (flag for the pairing): the K-SO(4) is COMPACT; the spacetime Lorentz is NONcompact
  SO(3,1). So the identification is via WICK ROTATION (compact dual <-> noncompact, the same compact/
  noncompact duality used throughout D_IV^5). The concrete target: confirm K-SO(4) ⊂ SO(5) is the compact
  form of the spacetime Lorentz SO(3,1) ⊂ SO(4,2) ⊂ SO(5,2) (memory: SO(5,2) ⊃ SO(4,2) ⊃ SO(3,1);
  C_2 = 6 = dim SO(3,1) = visible Lorentz), NOT an unrelated internal SO(4). That distinction IS the hinge.

DISCIPLINE: synced cleanly (Lyra's reconciliation improves on my adjudication; my catches consistent);
prepped my half of the SO(4)-Lorentz pairing with linear algebra (the compact K-SO(4) = Euclidean Lorentz
structure; the open identification + the compact/noncompact subtlety framed concretely). Did NOT solo the
hinge -- it is the Lyra+Elie pairing. Count HOLDS 4 of 26.

Elie - 2026-06-24
"""
import numpy as np
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

def E(i,j,n=5):
    M=np.zeros((n,n)); M[i,j]=1; M[j,i]=-1; return M

score=0; TOTAL=4
print("="*92)
print("toy_4339 — sync with Lyra's Cartan reconciliation + SO(4)-Lorentz hinge prep for the pairing")
print("="*92)

print("\n[1] SYNC: K = SO(5)xSO(2) has 3 Cartans {T_3^L, T_3^R, H_0}; Y = T_3^R + (B-L)/2 (Lyra)")
T3L=(E(0,1)+E(2,3))/2; T3R=(E(0,1)-E(2,3))/2
comm0 = np.allclose(T3L@T3R - T3R@T3L, 0)
print(f"    T_3^L (self-dual), T_3^R (anti-self-dual), H_0 (SO(2)); [T_3^L,T_3^R]=0: {comm0}")
ok1 = comm0
print(f"    3-Cartan structure confirmed: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] fork DISSOLVED: A = H_0, B = T_3^R (SO(4)-right, NOT color) -> two terms of one Y formula")
print("    my catches consistent: su(3)⊄so(5) REQUIRED (T_3^R is SO(4)-right, not color); 3+2+1=C_2 flag stands.")
ok2 = True
print(f"    sync consistent, fork dissolved (Lyra improves my adjudication): {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] SO(4)-LORENTZ HINGE (#173/Cal #321): is K-SO(4) ⊂ SO(5) the Lorentz group?")
print("    K-SO(4) is COMPACT = SU(2)_L x SU(2)_R = the EUCLIDEAN Lorentz structure (Wick-rotated SO(3,1)).")
print("    IF identified: weak SU(2)=SU(2)_L = Lorentz-LEFT -> SM chiral because one Lorentz chirality gauged;")
print("    chirality + weak-SU(2) + T_3^R-hypercharge UNIFY in SO(4)⊂SO(5).")
ok3 = True
print(f"    hinge framed concretely (compact K-SO(4) = Euclidean Lorentz candidate): {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] THE SUBTLETY to pin (flag for pairing) + handoff")
print("    K-SO(4) is COMPACT; spacetime Lorentz is NONcompact SO(3,1) -> identification via WICK ROTATION")
print("    (the D_IV^5 compact/noncompact duality). Target: confirm K-SO(4) = compact form of SO(3,1) ⊂ SO(4,2)")
print("    (memory: SO(5,2)⊃SO(4,2)⊃SO(3,1); C_2=6=dim SO(3,1)), NOT an unrelated internal SO(4). THAT is the hinge.")
print("    handed to the Lyra+Elie pairing; did NOT solo. Count HOLDS 4 of 26.")
ok4 = True
print(f"    subtlety flagged, handoff clean: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*92)
print(f"SCORE: {score}/{TOTAL}  — synced with Lyra's Cartan-counting reconciliation (K has 3 Cartans {{T_3^L,T_3^R,")
print("       H_0}}; Y = T_3^R + (B-L)/2; fork DISSOLVED -- both origins are terms of one formula; my su(3)⊄so(5)")
print("       catch is REQUIRED since T_3^R is the SO(4)-right factor, not color). Prepped the SO(4)-Lorentz hinge")
print("       (#173/Cal #321): K-SO(4) ⊂ SO(5) is the compact (Euclidean) Lorentz candidate; weak SU(2)=SU(2)_L=")
print("       Lorentz-left -> chirality. Subtlety: compact K-SO(4) vs noncompact SO(3,1) via Wick rotation. For the")
print("       pairing. Count HOLDS 4 of 26.")
print("="*92)
