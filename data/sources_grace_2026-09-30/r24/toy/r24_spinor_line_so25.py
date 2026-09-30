#!/usr/bin/env python3
"""R24 toy: so(2,5) (B3, n=3 in so(2,2n-1)), spinor K-type line lambda=(-E0,1/2,1/2).
Conventions pinned from PPST1 arXiv:2209.15324 Sec 3.5 (rho, Schmid modules s_{a,b}),
Bai-Hunziker arXiv:2409.16555 (z=(lambda+rho,beta^vee), beta=e1+e2, zeta=e1),
BEHJ arXiv:2512.08199 Thm 2.24 (b(lambda0)).  Exact arithmetic with Fractions."""
from fractions import Fraction as F
from itertools import product
n=3; rho=(F(5,2),F(3,2),F(1,2))
def dom_k(v):  # W_k = signed perms of coords 2..n (B_{n-1}); dominant: v2>=v3>=...>=0
    t=sorted((abs(x) for x in v[1:]),reverse=True); return (v[0],)+tuple(t)
def nrm(v): return sum(x*x for x in v)
def lam_spin(E0): return (-E0,F(1,2),F(1,2))
def lam_scal(nu): return (-nu,F(0),F(0))
def z(l): return (l[0]+rho[0])+(l[1]+rho[1])   # (lambda+rho, beta^vee), |beta|^2=2
def dirac_min(l,N=12):
    base=nrm(tuple(a+b for a,b in zip(l,rho))); out=[]
    for a,b in product(range(N),range(N)):
        if a==b==0: continue
        s=(2*b+a,a,0); m=dom_k(tuple(x-y for x,y in zip(l,s)))
        out.append((nrm(tuple(x+y for x,y in zip(m,rho)))-base,(a,b)))
    return min(out)
print("scalar line: nu -> z, min_s [||(l-s)^+ +rho||^2-||l+rho||^2]")
for nu in [F(0),F(1),F(3,2),F(2),F(5,2),F(3),F(7,2),F(4),F(9,2)]:
    l=lam_scal(nu); print(f"  nu={str(nu):>4} z={str(z(l)):>4} dirac_min={dirac_min(l)}")
print("spinor line: E0 -> z, min_s ...  (strict >0 => N(lambda) irreducible & unitary, PPST1 Thm1.1(2))")
for E0 in [F(1),F(3,2),F(2),F(5,2),F(3),F(7,2),F(4),F(9,2),F(5)]:
    l=lam_spin(E0); print(f"  E0={str(E0):>4} z={str(z(l)):>4} dirac_min={dirac_min(l)}")
# Harish-Chandra condition: (lambda+rho, alpha^vee)<0 for all noncompact positive alpha
nc=[(1,-1,0),(1,1,0),(1,0,-1),(1,0,1),(1,0,0)]
def cov(a): s=sum(x*x for x in a); return tuple(F(2*x,s) for x in a)
def hc(l): lr=tuple(a+b for a,b in zip(l,rho)); return max(sum(x*y for x,y in zip(lr,cov(a))) for a in nc)
print("HC max_{alpha in Delta(p+)} (lambda+rho,alpha^vee): <0 => holomorphic discrete series")
for E0 in [F(7,2),F(4),F(9,2),F(5)]: print(f"  spinor E0={E0}: {hc(lam_spin(E0))}")
for nu in [F(4),F(9,2)]: print(f"  scalar nu={nu}: {hc(lam_scal(nu))}")

# EHW root systems Q(lambda0), R(lambda0) as restated in BEHJ arXiv:2512.08199 Sec 2.5, and
# b(lambda0) = h^vee_Q - 1 + (r_R - r_Q)/2  (Thm 2.24, citing Bai-Hunziker [3, Thm 3.2]).
def refl(v,a):
    c=F(2*sum(x*y for x,y in zip(v,a)),sum(x*x for x in a)); return tuple(x-c*y for x,y in zip(v,a))
def closure(gens):
    S=set(); todo=[tuple(F(x) for x in g) for g in gens]+[tuple(-F(x) for x in g) for g in gens]
    S=set(todo); ch=True
    while ch:
        ch=False
        for a in list(S):
            for b in list(S):
                r=refl(b,a)
                if r not in S: S.add(r); ch=True
    return S
def comp_containing(S,v):  # connected component (non-orthogonality) containing v
    C={v}; ch=True
    while ch:
        ch=False
        for a in S:
            if a not in C and any(sum(x*y for x,y in zip(a,c))!=0 for c in C): C.add(a); ch=True
    return C
def describe(C):
    N=len(C); lens={sum(x*x for x in a) for a in C}; rk=len({a for a in C})  # crude
    return N, sorted(lens)
compact=[(0,1,-1),(0,1,1),(0,1,0),(0,0,1)]
beta=(1,1,0)
def QR(l0):
    phic=[a for a in compact if sum(F(x)*y for x,y in zip(a,l0))==0]
    Q=comp_containing(closure([beta]+phic),tuple(-F(x) for x in beta))
    extra=[a for a in compact if sum(x*x for x in a)==1 and sum(F(2*x)*y for x,y in zip(a,l0))==1
           and any(sum(x*y for x,y in zip(a,q))!=0 for q in Q)]
    R=comp_containing(closure([beta]+phic+extra),tuple(-F(x) for x in beta)) if extra else Q
    return phic,Q,extra,R
for name,l0 in [("scalar",(F(-4),F(0),F(0))),("spinor",(F(1,2)-5,F(1,2),F(1,2)))]:
    phic,Q,extra,R=QR(l0)
    print(f"{name}: lambda0={tuple(str(x) for x in l0)} (lambda0+rho,beta^vee)={z(l0)}; Phi_c={phic}; |Q|={len(Q)} lens={describe(Q)[1]}; extra short={extra}; |R|={len(R)} lens={describe(R)[1]}")
print("  |root system| key: A1=2, A2=6, B2=8, B3=18")
