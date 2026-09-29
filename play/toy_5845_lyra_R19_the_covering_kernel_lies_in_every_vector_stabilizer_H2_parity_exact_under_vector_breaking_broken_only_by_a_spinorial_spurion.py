#!/usr/bin/env python3
"""
Lyra R19 (2026-09-29). Invariants first.
 (I1) z_t = exp(2 pi J) maps to the identity of SO(4,2): it acts trivially on R^{4,2} and on every tensor of it (any spurion built
      from vectors: the ruler as a null vector, Lambda as a timelike vector; Cal S1010/S1011, Lyra R16). Hence z_t is in
      Stab_{G~}(v) for EVERY vector v: the covering kernel survives every vector breaking.
 (I2) On the free Fock space z_t = (-1)^{N_H2} (H2 quanta: e^{2 pi i (5/2+k)} = -1; massless: z_t = z_s, and z_s = (-1)^F is
      separately exact by Lorentz).
Predictions BEFORE the run:
 E1 exp(2 pi J) = identity on R^{4,2} and on Sym^2, Lambda^2 (tensors): checked numerically.
 E2 Toy dynamics on a truncated Fock space (modes: two H2 modes, one massless boson mode, occupation <= 2 each):
    H = H0 + 'anomalous-dimension' terms (number-conserving quartics with random couplings) + every spurion-allowed term
    (all monomials with EVEN total H2-number change, random complex couplings, with and without the boson).
    [H, P] = 0 for P = (-1)^{N_H2}, and <odd-H2-number-changed| e^{-iHt} |state> = 0 to 1e-12 at t = 0.7, 3.1, 11.
 E3 CONTROL (must break): add ONE monomial with odd H2-number change (a spinorial spurion, weight 1/2) -> [H,P] != 0 and odd
    transitions appear.  CONTROL 2: fermion-parity analogue is the same algebra with z_s (not rerun).
"""
import numpy as np, itertools
from scipy.linalg import expm
ok=[]
rng=np.random.default_rng(1939)
eta=np.diag([1,1,1,1,-1,-1.]); n=6
M=np.zeros((n,n)); M[4,5]=1; M[5,4]=-1; J=M@eta
Z=expm(2*np.pi*J)
E1=np.allclose(Z,np.eye(n)) and np.allclose(np.kron(Z,Z),np.eye(n*n))
ok.append(E1); print("E1 exp(2 pi J) = 1 on vectors and 2-tensors ->",E1)
# Fock space: modes (h1,h2,b), occupations 0..2
cap=3; modes=3; dim=cap**modes
states=list(itertools.product(range(cap),repeat=modes))
idx={s:i for i,s in enumerate(states)}
def a(m):
    A=np.zeros((dim,dim))
    for s in states:
        if s[m]>0:
            t=list(s); t[m]-=1; A[idx[tuple(t)],idx[s]]=np.sqrt(s[m])
    return A
A=[a(m) for m in range(modes)]; Ad=[x.T for x in A]
P=np.diag([(-1)**(s[0]+s[1]) for s in states])
H=sum((0.7+k)*Ad[k]@A[k] for k in range(modes)).astype(complex)
def mono(ops):
    X=np.eye(dim)
    for o in ops: X=X@o
    return X
def herm(X): return X+X.conj().T
# number-conserving 'anomalous dimension' quartics
for i,j in itertools.product(range(2),repeat=2): H+=rng.normal()*herm(Ad[i]@Ad[j]@A[i]@A[j])
# every allowed (even H2-change) monomial up to degree 3 in ladder ops
ladders=[A[0],Ad[0],A[1],Ad[1],A[2],Ad[2]]; h2change=[-1,1,-1,1,0,0]
for deg in (1,2,3):
    for combo in itertools.combinations_with_replacement(range(6),deg):
        if sum(h2change[c] for c in combo)%2==0:
            H+=herm((rng.normal()+1j*rng.normal())*0.3*mono([ladders[c] for c in combo]))
comm=np.abs(H@P-P@H).max()
leak=max(np.abs(P@expm(-1j*H*t)-expm(-1j*H*t)@P).max() for t in (0.7,3.1,11.0))
E2=comm<1e-12 and leak<1e-10; ok.append(E2); print(f"E2 [H,P]={comm:.1e}, odd-H2 leakage={leak:.1e} ->",E2)
H3=H+herm(0.2*mono([Ad[0],A[2]]))       # one odd monomial: a spinorial spurion
comm3=np.abs(H3@P-P@H3).max(); leak3=max(np.abs(P@expm(-1j*H3*t)-expm(-1j*H3*t)@P).max() for t in (0.7,3.1))
E3=comm3>1e-3 and leak3>1e-3; ok.append(E3); print(f"E3 control with one odd monomial: [H,P]={comm3:.2f}, leakage={leak3:.2f} ->",E3)
print(f"SCORE {sum(ok)}/{len(ok)}  (run 2; run 1 sha 264f50fe crashed on a float/complex dtype cast after E1 printed True)")
