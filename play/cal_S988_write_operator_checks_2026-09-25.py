#!/usr/bin/env python3
"""Cal Section 988 -- adversarial checks on K1925's write operator W_x = D(x,e) (2026-09-25).
Same triple product and tripotent as play/keeper_K1925_triple_derivations_on_V1.py (copied, not imported).
PREDICTIONS written before the run:
 Q1 W_x^2 != 0 on V (so W is NOT the Grassmann/once-only relation c(w)^2 = 0; its nilpotency order 3 = number of Peirce levels)
 Q2 on the time line, W_x W_y e is SYMMETRIC in x,y and proportional to q(x,y) ebar  (two writes carry q, not eps)
 Q3 every product of three weight -1 shifts vanishes on V (eps cannot be a top product of three writes on V)
 Q4 the weight -1 part of the structure algebra on V has complex dim 3 (W is forced by the grading once e and the direction are fixed);
    D(ebar, y) lies in the same 3-dim space
 Q5 on V1 the scalar I is hit both by D(e,e)|V1 and by the centre (overall scalar on V): on V they differ (charges 2,1,0 vs 1,1,1)
"""
import itertools, numpy as np
n=5
def dot(a,b): return np.sum(a*b)
def trip(x,y,z): yb=np.conj(y); return dot(x,yb)*z+dot(z,yb)*x-dot(x,z)*yb
def D(a,b): return np.array([trip(a,b,np.eye(n)[k]) for k in range(n)]).T
E=np.eye(n,dtype=complex); e=(E[0]+1j*E[1])/np.sqrt(2); eb=np.conj(e); V1=[E[2],E[3],E[4]]
W=lambda x: D(x,e)
r={}
r['Q1']=all(not np.allclose(W(x)@W(x),0) for x in V1)
rng=np.random.default_rng(1)
x=rng.normal(size=5)*np.r_[0,0,1,1,1]+0j; y=rng.normal(size=5)*np.r_[0,0,1,1,1]+0j
a=W(x)@W(y)@e; b=W(y)@W(x)@e
r['Q2']=np.allclose(a,b) and np.linalg.matrix_rank(np.array([a,eb]),tol=1e-9)==1
print('Q2 W_xW_y e =',np.round(a,6),' coefficient/q(x,y) =',np.round((a@e)/dot(x,y),6) if abs(dot(x,y))>1e-9 else None)
r['Q3']=all(np.allclose(W(p)@W(q)@W(s),0) for p,q,s in itertools.product(V1,repeat=3))
# weight -1 part of span of all D(a,b): grade by ad D(e,e)
basis=[E[k] for k in range(5)]+[1j*E[k] for k in range(5)]
ops=[D(p,q) for p,q in itertools.product(basis,repeat=2)]
H=D(e,e)
M=np.array([o.ravel() for o in ops]); 
# project onto ad_H eigenvalue -1: solve in the span
U,s,Vt=np.linalg.svd(M.T,full_matrices=False); B=U[:,s>1e-9]
ad=np.array([ (H@B[:,k].reshape(5,5)-B[:,k].reshape(5,5)@H).ravel() for k in range(B.shape[1])]).T
coef=np.linalg.lstsq(B,ad,rcond=None)[0]
ev=np.linalg.eigvals(coef)
print('structure algebra dim_C =',B.shape[1],' ad D(e,e) eigenvalue multiplicities:',{k:int(np.sum(np.isclose(ev,k))) for k in [-2,-1,0,1,2]})
m1=int(np.sum(np.isclose(ev,-1)))
Wspan=np.array([W(v).ravel() for v in V1]+[D(eb,v).ravel() for v in V1]).T
r['Q4']=m1==3 and np.linalg.matrix_rank(Wspan,tol=1e-9)==3
print('Q4 rank of {D(x,e)} u {D(ebar,x)} =',np.linalg.matrix_rank(Wspan,tol=1e-9))
cen=[o for o in ops]; Hc=D(e,e)+D(eb,eb)
print('Q5 D(e,e) diag on (e,V1,ebar):',np.round([ (H@e)@np.conj(e), (H@E[2])[2], (H@eb)@np.conj(eb)],6).real,
      ' D(e,e)+D(eb,eb) =',np.round(np.diag(Hc).real,6), ' (2*identity => the centre)')
r['Q5']=np.allclose(Hc,2*np.eye(5)) and np.allclose(H[2:,2:],np.eye(3))
for k,v in r.items(): print(('HELD ' if v else 'MISSED ')+k)
