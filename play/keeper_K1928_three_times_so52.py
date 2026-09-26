#!/usr/bin/env python3
"""Keeper K1928 instrument: the three kinds of time inside so(5,2) (7x7 real matrices, metric eta = diag(-1,+1,+1,+1,+1,+1,-1),
coordinates (x0 = Minkowski time, x1..x4 space of R^{1,4}, x5, x6) with x5 = the extra spacelike, x6 = the second time).
Conformal generators on R^{1,4}: P_mu = M_{mu,5}+M_{mu,6}, K_mu = M_{mu,5}-M_{mu,6}, D = M_{5,6}.
Claims checked: (1) P0, K0 nilpotent (parabolic: continuous spectrum on unitary reps);
(2) the elliptic element of span{P0,K0,D} (here (P0-K0)/2 = M_{0,6}, rotating the two times) = the centre of K (BST's clock J);
(3) D hyperbolic (real eigenvalues); (4) {P0,K0,D} close an sl(2,R); (5) one sl(2,R) holds all three conjugacy types: elliptic J (interior clock), parabolic P0 (boundary Minkowski energy), hyperbolic D (scale)."""
import numpy as np, itertools
n=7; eta=np.diag([-1,1,1,1,1,1,-1.0])
def M(a,b):
    m=np.zeros((n,n)); m[a,b]=1; m[b,a]=-1
    return m@eta  # element of so(eta): X^T eta + eta X = 0
def inso(X): return np.allclose(X.T@eta+eta@X,0)
P0=M(0,5)+M(0,6); K0=M(0,5)-M(0,6); D=M(5,6)
# CONVENTION: with THIS sign of K0, the compact element is (P0-K0)/2 = M(0,6); Luscher-Mack's H=(P0+K0)/2 uses the opposite sign of K.
# The invariant is 'the elliptic element of span{P0,K0,D}', not a sign. First run (kept in K1928) used (P0+K0)/2 and FAILED: that is the boost M(0,5).
L0=(P0-K0)/2; B=(P0+K0)/2
ok=True
def chk(name,c):
    global ok; ok&=bool(c); print(f"[{'PASS' if c else 'FAIL'}] {name}")
chk("all generators in so(5,2)", all(inso(X) for X in (P0,K0,D,L0)))
chk("P0 nilpotent (parabolic)", np.allclose(np.linalg.matrix_power(P0,3),0))
chk("K0 nilpotent (parabolic)", np.allclose(np.linalg.matrix_power(K0,3),0))
ev=lambda X: np.round(np.linalg.eigvals(X),6)
print("   eig D  =",sorted(ev(D).real)); chk("D hyperbolic (real nonzero eigenvalues)", np.allclose(ev(D).imag,0) and np.abs(ev(D)).max()>0)
print("   eig L0 =",sorted(ev(L0),key=lambda z:z.imag)); chk("L0 elliptic (purely imaginary eigenvalues)", np.allclose(ev(L0).real,0) and np.abs(ev(L0)).max()>0)
br=lambda A,B: A@B-B@A
# sl(2,R): [D,P0]=cP0, [D,K0]=-cK0, [P0,K0]=c'D
c1=np.sum(br(D,P0)*P0)/np.sum(P0*P0); c2=np.sum(br(D,K0)*K0)/np.sum(K0*K0); c3=np.sum(br(P0,K0)*D)/np.sum(D*D)
chk(f"sl(2,R): [D,P0]={c1:+.0f}P0, [D,K0]={c2:+.0f}K0, [P0,K0]={c3:+.0f}D", np.allclose(br(D,P0),c1*P0) and np.allclose(br(D,K0),c2*K0) and np.allclose(br(P0,K0),c3*D) and c1==-c2!=0)
# Is L0 conjugate to the centre of K (the rotation of the two time axes x0,x6 in the compact picture)?
J=M(0,6)  # rotation mixing the two timelike coordinates
chk("J=M(0,6) is compact and commutes with so(5)xso(2)'s so(5) on x1..x5", all(np.allclose(br(J,M(a,b)),0) for a,b in itertools.combinations(range(1,6),2)))
# conjugacy: same spectrum => conjugate (both semisimple in so(5,2)); check spectra match
chk("L0 and J have the same spectrum (conjugate elliptic elements)", np.allclose(sorted(ev(L0).imag),sorted(ev(J).imag)))
# negative control: P0 is NOT conjugate to J (nilpotent vs elliptic)
chk("control: the other sign (P0+K0)/2 is HYPERBOLIC (a boost), not elliptic", np.allclose(ev(B).imag,0) and np.abs(ev(B)).max()>0)
chk("control: P0 spectrum differs from J's", not np.allclose(sorted(ev(P0).imag),sorted(ev(J).imag)))
print("VERDICT:", "ALL PASS" if ok else "FAILURE")
