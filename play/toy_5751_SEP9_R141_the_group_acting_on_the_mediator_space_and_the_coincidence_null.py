#!/usr/bin/env python3
"""Toy 5751 — R141 E1/E2: what group does the geometry actually supply on V_1/2, and can SU(3) embed in it?"""
import json, itertools
import numpy as np
from fractions import Fraction as F
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
n=5
def triple(x,y,z):   # {x,y,z} = (x|y)z + (z|y)x - (x.z) conj(y)
    return np.vdot(y,x)*z + np.vdot(y,z)*x - (x@z)*np.conj(y)
u=np.zeros(n); u[0]=1.0; v=np.zeros(n); v[1]=1.0
e=(u+1j*v)/2
print("A1 — the Peirce decomposition of a minimal tripotent")
print(f"   e = (u + i v)/2 with u,v orthonormal;  {{e,e,e}} - e = {np.abs(triple(e,e,e)-e).max():.2e}  (tripotent)")
D=np.zeros((n,n),dtype=complex)
for i in range(n):
    b=np.zeros(n,dtype=complex); b[i]=1; D[:,i]=triple(e,e,b)
ev=np.linalg.eigvals(D); ev=np.sort_recorded=np.sort(ev.real)
dims={val: int(np.sum(np.abs(ev-val)<1e-9)) for val in (0.0,0.5,1.0)}
print(f"   eigenvalues of D(e,e): {np.round(np.sort(ev),6)}  ->  dim V_1 = {dims[1.0]}, dim V_1/2 = {dims[0.5]}, dim V_0 = {dims[0.0]}")
sc("A1", (dims[1.0],dims[0.5],dims[0.0])==(1,3,1), False, "1 + 3 + 1 = 5; V_1/2 is C^3 = span{e3,e4,e5}")
print("A2 — the isotropy: solve (A,t) in so(5) + so(2) with A e + i t e = 0, numerically")
basis=[]
for i in range(n):
    for j in range(i+1,n):
        A=np.zeros((n,n)); A[i,j]=1; A[j,i]=-1; basis.append((A,0.0))
basis.append((np.zeros((n,n)),1.0))
M=np.zeros((2*n,len(basis)))
for c,(A,t) in enumerate(basis):
    w=A@e + 1j*t*e; M[:n,c]=w.real; M[n:,c]=w.imag
rank=np.linalg.matrix_rank(M,tol=1e-9); null=len(basis)-rank
print(f"   parameters: {len(basis)} (10 in so(5) + 1 phase);  rank of the constraint = {rank};  isotropy dimension = {null}")
ns=np.linalg.svd(M)[2][rank:]
print(f"   so(3) on span(e3,e4,e5) has dim 3, plus the diagonal SO(2) -> expected 4")
sc("A2", null==4, True, f"Stab_K(e) has Lie-algebra dimension {null} = SO(2)_diag x SO(3)")
print("A3 — the image in GL(V_1/2), and can SU(3) embed?")
sub=[]
for vec in ns:
    A=sum(vec[c]*basis[c][0] for c in range(len(basis))); t=sum(vec[c]*basis[c][1] for c in range(len(basis)))
    blk=A[2:,2:]                      # action on span{e3,e4,e5}
    sub.append((blk,t))
    
antisym=all(np.abs(b+b.T).max()<1e-9 for b,_ in sub)
gen=[np.array(b,dtype=complex)+1j*t*np.eye(3) for b,t in sub]
G=np.array([g.reshape(-1) for g in gen]); dimimg=np.linalg.matrix_rank(np.column_stack([G.real.T,G.imag.T]).T if False else np.vstack([G.real,G.imag]).T @ np.eye(len(gen)) if False else G.view(float).reshape(len(gen),-1), tol=1e-9)
print(f"   every isotropy generator restricted to V_1/2 is (antisymmetric real) + i*(phase)*I : {antisym}")
print(f"   dimension of the image Lie algebra in gl(3,C): {dimimg}   -> so(3) + R.iI = 3 + 1 = 4")
print(f"   dim SU(3) = 8 > {dimimg}. A compact group cannot embed in a group of smaller dimension.")
print("   full structure-group stabiliser: any COMPACT subgroup is conjugate into the maximal compact, which is this same dim-4 group,")
print("   so the conclusion is unchanged if the stabiliser is enlarged from K to the structure group.")
sc("A3", dimimg==4 and 8>dimimg, True, "SU(3) (dim 8) DOES NOT EMBED in the group the geometry supplies on the mediator space (dim 4)")
print("A4 — which way does the inclusion run?")
print("   SO(3) sits inside SU(3) as the standard vector embedding (real 3x3 orthogonal matrices are unitary with det 1).")
print("   So geometry's group is a proper 3-dimensional subgroup of the 8-dimensional colour group: geometry IN colour, not colour IN geometry.")
sc("A4", True, False, "the inclusion runs the wrong way for a derivation")
print("A5 — which endomorphism algebra? it depends on what you forget")
print("   End_C(V_1/2) = M_3(C), real dim 18   [forgets the group]")
print("   End_R(real 3-space) = M_3(R), real dim 9   [forgets the complex structure too]")
print("   End_R(V_1/2 as R^6) = M_6(R), real dim 36")
print("   COMMUTANT of the isotropy (the object that respects the geometry): the complexified vector rep of SO(3) on C^3 is")
print("   irreducible, so by Schur End_{SO(3)}(C^3) = C, real dim 2; dropping the phase gives M_2(R).")
sc("A5", True, False, "the correct object is C, not M_3 of anything; M_3(C) is available for ANY 3-dim complex space — the withdrawn slip")
print("E2 — the coincidence null, menu NAMED IN THE PREREG before counting")
def fams(cap=30):
    out=[]
    for p in range(1,9):
        for q in range(p,31):
            if p*q<=cap: out.append((f"I_{{{p},{q}}}", p, 2, q-p, p*q))
    for m in range(2,12):
        d=m*(m-1)//2
        if 0<d<=cap: out.append((f"II_{m}", m//2, 4, 0 if m%2==0 else 2, d))
    for m in range(1,9):
        d=m*(m+1)//2
        if d<=cap: out.append((f"III_{m}", m, 1, 0, d))
    for m in range(3,31):
        if m<=cap: out.append((f"IV_{m}", 2, m-2, 0, m))
    out.append(("V(E6)",2,6,4,16)); out.append(("VI(E7)",3,8,0,27))
    return out
FA=fams()
def menu(r,a,b,d): return {'rank':r,'a':a,'b':b,'genus':(r-1)*a+b+2,'dim_C':d,'dimV12':a+b}
for target in (3,2,4,6,8):
    hit_dom=[n for (n,r,a,b,d) in FA if target in menu(r,a,b,d).values()]
    per_inv={k:[n for (n,r,a,b,d) in FA if menu(r,a,b,d)[k]==target] for k in ('rank','a','b','genus','dim_C','dimV12')}
    line=", ".join(f"{k}:{len(v)}" for k,v in per_inv.items())
    print(f"   target {target}: {len(hit_dom)} of {len(FA)} domains carry SOME menu invariant = {target}   [{line}]")
    if target==3: three=(hit_dom,per_inv)
print(f"   the specific invariant a = 3: {three[1]['a']}  <- singleton")
print(f"   'some invariant equals 3' is carried by {len(three[0])} domains; the look-elsewhere factor is the menu size, 6 per domain.")
sc("A6", len(three[0])>=20 and three[1]['a']==['IV_5'], True, f"{len(three[0])} domains carry some invariant = 3, while a = 3 is a singleton — the selector's strength rests entirely on whether the invariant was named before the target")
sc("A7", True, False, "the same table printed for 2, 4, 6, 8 so the round sees the whole picture")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'isotropy_dim':int(null),'image_dim':int(dimimg),'su3_dim':8,'three_domains':len(three[0]),'a3':three[1]['a']}, open('.record_5751.json','w'), indent=1)
