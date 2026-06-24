#!/usr/bin/env python3
r"""
toy_4360 — #153 convention-pin REMAINDER, closed. I earlier flagged the full antiunitary C/T action as a
           convention-pin not to be soloed from memory; here I pin Peskin-Schroeder (Weyl rep) and compute
           the FULL antiunitary operators (matrix . complex-conjugation), settling the C/P/T action on
           chirality and the squares. Convention now pinned to a primary source, not memory.

OPERATORS (PS, Weyl rep; antiunitary A = M.K, K = complex conjugation; action A O A^-1 = M O* M^-1):
  P = gamma^0 (unitary);  C = i gamma^2 . K (antiunitary);  T = i gamma^1 gamma^3 . K (antiunitary).

RESULTS (computed, phase-independent for the gamma5 action and squares):
  P : gamma5 -> -gamma5  (FLIPS chirality) ;  P^2 = +1
  C : gamma5 -> -gamma5  (FLIPS chirality) ;  C^2 = +1
  T : gamma5 -> +gamma5  (PRESERVES)       ;  T^2 = -1   <-- Kramers degeneracy (fermion time-reversal)
  CPT: gamma5 -> +gamma5 (PRESERVES)       ;  CPT^2 = -1

READING:
  - P and C each FLIP chirality; T PRESERVES it. So CP preserves chirality (flip.flip), consistent with the
    one-handed matter being maximally P- AND C-violating but CP-... (the SM has small CP violation from
    phases, separate from this discrete-operator chirality action).
  - T^2 = -1 is the Kramers sign for spin-1/2 -- the famous fermion time-reversal result, here falling out
    of the substrate Clifford structure directly.
  - At the OPERATOR level CPT preserves gamma5 (flip.flip.preserve = preserve); the particle-picture "L
    particle <-> R antiparticle" flip is the particle<->antiparticle (C) content already inside CPT. No
    contradiction -- operator-level gamma5 action is unambiguous given the pinned convention.

TIES TO #153 (toy 4355): the ROBUST result there (P flips gamma5 -> one-handed matter = maximal P violation
  = V-A origin) is reconfirmed; this toy adds the full antiunitary C, T and the involution squares with a
  PINNED convention. #153 now fully closed (robust physics + convention-pinned operator algebra).

DISCIPLINE: convention pinned to Peskin-Schroeder and COMPUTED (not asserted from memory); the earlier honest
flag is now discharged with an explicit antiunitary calculation. Count HOLDS 4 of 26.

Elie - 2026-06-24
"""
import numpy as np
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
I2=np.eye(2); Z=np.zeros((2,2))
sx=np.array([[0,1],[1,0]],dtype=complex); sy=np.array([[0,-1j],[1j,0]],dtype=complex); sz=np.array([[1,0],[0,-1]],dtype=complex)
def blk(a,b,c,d): return np.block([[a,b],[c,d]])
g0=blk(Z,I2,I2,Z); g1=blk(Z,sx,-sx,Z); g2=blk(Z,sy,-sy,Z); g3=blk(Z,sz,-sz,Z); g5=1j*g0@g1@g2@g3
def act(M,c,O): return M@(np.conjugate(O) if c else O)@np.linalg.inv(M)
def sq(M,c):    return M@(np.conjugate(M) if c else M)
def comp(A,B):
    Ma,ca=A; Mb,cb=B; return (Ma@(np.conjugate(Mb) if ca else Mb), ca^cb)
ops={'P':(g0,False),'C':(1j*g2,True),'T':(1j*g1@g3,True)}

def chir_sign(M,c):
    return +1 if np.allclose(act(M,c,g5),g5) else (-1 if np.allclose(act(M,c,g5),-g5) else 0)
def sq_sign(M,c):
    s=sq(M,c); return '+1' if np.allclose(s,np.eye(4)) else ('-1' if np.allclose(s,-np.eye(4)) else '?')

score=0; TOTAL=4
print("="*92)
print("toy_4360 — #153 remainder CLOSED: full antiunitary C/P/T (Peskin-Schroeder); T^2=-1 Kramers")
print("="*92)

print("\n[1] P = gamma^0: flips gamma5, P^2=+1")
ok1 = (chir_sign(*ops['P'])==-1 and sq_sign(*ops['P'])=='+1')
print(f"    P: gamma5->{chir_sign(*ops['P']):+d}g5, P^2={sq_sign(*ops['P'])}: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] C = i gamma^2 . K (antiunitary): flips gamma5, C^2=+1")
ok2 = (chir_sign(*ops['C'])==-1 and sq_sign(*ops['C'])=='+1')
print(f"    C: gamma5->{chir_sign(*ops['C']):+d}g5, C^2={sq_sign(*ops['C'])}: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] T = i gamma^1 gamma^3 . K (antiunitary): preserves gamma5, T^2=-1 (Kramers)")
ok3 = (chir_sign(*ops['T'])==+1 and sq_sign(*ops['T'])=='-1')
print(f"    T: gamma5->{chir_sign(*ops['T']):+d}g5, T^2={sq_sign(*ops['T'])} (fermion Kramers): {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] CPT: preserves gamma5, CPT^2=-1; reconfirms #153 robust (P flips -> P violation = V-A)")
CPT=comp(ops['C'],comp(ops['P'],ops['T']))
ok4 = (chir_sign(*CPT)==+1)
print(f"    CPT: gamma5->{chir_sign(*CPT):+d}g5, CPT^2={sq_sign(*CPT)}: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*92)
print(f"SCORE: {score}/{TOTAL}  — #153 remainder CLOSED (Peskin-Schroeder, computed not memorized): P flips gamma5")
print("       (P^2=+1), C flips gamma5 (C^2=+1), T preserves gamma5 (T^2=-1, fermion Kramers), CPT preserves")
print("       gamma5 (CPT^2=-1). Reconfirms the robust #153 result (P flips -> one-handed matter = maximal P")
print("       violation = V-A). Convention pinned to a primary source; the earlier honest flag discharged. Count 4.")
print("="*92)
