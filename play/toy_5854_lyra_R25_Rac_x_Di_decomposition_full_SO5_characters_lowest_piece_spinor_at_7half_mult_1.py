#!/usr/bin/env python3
"""
Lyra R25 (2026-09-30). Group: SO_0(5,2), K = SO(5) x SO(2); SO(5) = B2, weights (x,y) with x >= y >= 0, rho = (3/2, 1/2),
W(B2) = signed permutations (8). Characters by the Weyl character formula at random torus points (full SO(5) content, not dims).
Families/sources: Rac K-types (a,0) at clock 3/2 + a; Di K-types (a+1/2, 1/2) at 2 + a (spinor harmonics on S^4; E0 pinned K956);
p+ = the SO(5) vector (1,0); Sym^m(vector) = sum_b (m-2b, 0).  Generalized Verma V(l; tau) = tau (x) Sym(p+) t^l.
Conserved spin-j module at the bound: V(l; tau) - V(l+1; tau') (divergence), tau' the next-lower spinor/tensor.
Predictions BEFORE the run (graded characters compared coefficient by coefficient up to 4 levels above the bottom):
 C1 CONTROL Rac x Rac = V(3;(0,0)) + sum_{s>=1} [V(3+s;(s,0)) - V(4+s;(s-1,0))].
 C2 Rac x Di  = V(7/2;(1/2,1/2)) + sum_{s>=1} [V(7/2+s;(s+1/2,1/2)) - V(9/2+s;(s-1/2,1/2))].
 C3 lowest piece: H(7/2;(1/2,1/2)) (SO(5) spinor 4, = K1653's V_(1/2,1/2)), multiplicity 1; the spinor (1/2,1/2) at clock 7/2 has
    multiplicity exactly 1 in Rac x Di.
 C4 NEGATIVE CONTROL: dropping the divergence subtraction in C2 fails.
"""
import numpy as np, itertools
from fractions import Fraction as F
rng=np.random.default_rng(25)
W=[]
for perm in ((0,1),(1,0)):
    for sg in itertools.product((1,-1),repeat=2):
        W.append((perm,sg))
def wact(w,v): perm,sg=w; return (sg[0]*v[perm[0]], sg[1]*v[perm[1]])
def sgn(w):
    perm,sg=w; return (1 if perm==(0,1) else -1)*sg[0]*sg[1]
rho=(1.5,0.5)
def A(mu,th): return sum(sgn(w)*np.exp(1j*np.dot(wact(w,mu),th)) for w in W)
def chi(lam,th): return A((lam[0]+rho[0],lam[1]+rho[1]),th)/A(rho,th)
L=4  # levels above bottom
def graded(terms,th,base):
    # terms: list of (clock weight, (x,y), coefficient); return dict level->value for levels base..base+L
    out={}
    for w,lam,c in terms:
        lev=w-base
        if 0<=lev<=L: out[lev]=out.get(lev,0)+c*chi(lam,th)
    return out
def verma(l,tau,th,base,sign=1):
    terms=[]
    for m in range(L+1):
        for b in range(m//2+1):
            # tau (x) (m-2b,0): decompose numerically later -> keep as product
            terms.append((l+m,(tau,(m-2*b,0)),sign))
    return terms
def eval_terms(terms,th,base):
    out={}
    for w,lam,c in terms:
        lev=w-base
        if not (0<=lev<=L): continue
        if isinstance(lam[0],tuple): val=chi(lam[0],th)*chi(lam[1],th)
        else: val=chi(lam,th)
        out[lev]=out.get(lev,0)+c*val
    return out
def prod_side(fam1,fam2,th,base):
    out={}
    for (w1,l1) in fam1:
        for (w2,l2) in fam2:
            lev=w1+w2-base
            if 0<=lev<=L: out[lev]=out.get(lev,0)+chi(l1,th)*chi(l2,th)
    return out
Rac=[(F(3,2)+a,(a,0)) for a in range(L+2)]
Di=[(F(2)+a,(a+0.5,0.5)) for a in range(L+2)]
def rhs(kind,th,base,subtract=True):
    terms=[]
    if kind=='RR':
        terms+=verma(F(3),(0,0),th,base)
        for s in range(1,L+2):
            terms+=verma(F(3)+s,(s,0),th,base)
            if subtract: terms+=verma(F(4)+s,(s-1,0),th,base,-1)
    else:
        terms+=verma(F(7,2),(0.5,0.5),th,base)
        for s in range(1,L+2):
            terms+=verma(F(7,2)+s,(s+0.5,0.5),th,base)
            if subtract: terms+=verma(F(9,2)+s,(s-0.5,0.5),th,base,-1)
    return eval_terms(terms,th,base)
def agree(a,b): return all(abs(a.get(k,0)-b.get(k,0))<1e-8*(1+abs(a.get(k,0))) for k in range(L+1))
ths=[rng.uniform(0.1,3.0,2) for _ in range(5)]
C1=all(agree(prod_side(Rac,Rac,th,F(3)),rhs('RR',th,F(3))) for th in ths); print("C1 control Rac x Rac identity (full SO(5) characters, 4 levels) ->",C1)
C2=all(agree(prod_side(Rac,Di,th,F(7,2)),rhs('RD',th,F(7,2))) for th in ths); print("C2 Rac x Di = sum_s spin-(s+1/2) at 7/2+s ->",C2)
# C3: multiplicity of the spinor (1/2,1/2) at the bottom level: bottom of product = chi(0,0)*chi(1/2,1/2) = chi(1/2,1/2) exactly
C3=all(abs(prod_side(Rac,Di,th,F(7,2))[0]-chi((0.5,0.5),th))<1e-10 for th in ths); print("C3 bottom (clock 7/2) content = one spinor 4 ->",C3)
C4=not all(agree(prod_side(Rac,Di,th,F(7,2)),rhs('RD',th,F(7,2),subtract=False)) for th in ths); print("C4 negative control (no divergence subtraction) fails ->",C4)
ok=[C1,C2,C3,C4]; print(f"SCORE {sum(ok)}/{len(ok)}")
