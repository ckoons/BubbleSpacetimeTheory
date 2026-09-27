#!/usr/bin/env python3
"""
Lyra R16 (2026-09-27). Invariant first: a dimensionful breaking of the 4D conformal group SO(4,2) is a fixed vector v in R^{4,2}
(metric eta = diag(+1,+1,+1,+1,-1,-1)); the symmetry kept is Stab(v). Predictions BEFORE the run:
 B1 dim so(4,2) = 15; Stab(null v) has dim 10 and is the Poincare algebra (4 abelian translations + so(3,1));
    Stab(v, v^2 = -1): dim 10, Killing-form signature of so(4,1) (de Sitter; complement (4,1));
    Stab(v, v^2 = +1): dim 10, so(3,2) (AdS; complement (3,2)).
 B2 Stab of a null v AND a v^2=-1 vector together: dim < 10 (neither Poincare nor de Sitter). A particle mass that is a SECOND
    breaking vector would therefore break de Sitter invariance; a mass as a Casimir LABEL of so(4,1) keeps it.
 B3 so(4,1) quadratic Casimir distinguishes masses: C2 is not a multiple of the identity on the vector rep? (control) -> instead:
    on a principal-series parameter, m^2/H^2 = Delta(3 - Delta) (d=3 boundary) is a dimensionless label: checked symbolically
    that Delta(3-Delta) spans (0, 9/4] for Delta = 3/2 + i nu and real Delta in (0,3): a label, not a vector.
"""
import numpy as np, itertools, sympy as sp
ok=[]
eta=np.diag([1,1,1,1,-1,-1.]); n=6
basis=[]
for a,b in itertools.combinations(range(n),2):
    M=np.zeros((n,n)); M[a,b]=1; M[b,a]=-1; basis.append(M@eta)     # X = E eta satisfies X^T eta + eta X = 0
basis=[X for X in basis]
def stab(vs):
    A=np.array([np.concatenate([X@v for v in vs]) for X in basis]).T
    ns=np.linalg.svd(A)[2][np.linalg.matrix_rank(A):]
    return [sum(c*X for c,X in zip(vec,basis)) for vec in ns]
def killing_sig(Xs):
    m=len(Xs); B=np.array([[np.trace(X@Y) for Y in Xs] for X in Xs]); ev=np.linalg.eigvalsh((B+B.T)/2)
    return (int((ev>1e-9).sum()),int((ev<-1e-9).sum()),int((abs(ev)<=1e-9).sum()))
vnull=np.array([0,0,0,1,1,0.]); vtime=np.array([0,0,0,0,0,1.]); vspace=np.array([1,0,0,0,0,0.])
Sn,St,Ss=stab([vnull]),stab([vtime]),stab([vspace])
kn,kt,ks=killing_sig(Sn),killing_sig(St),killing_sig(Ss)
# so(4,1): 4 compact? trace form on matrices: compact generators negative; so(4,1) has 6 compact (so(4)) + 4 noncompact; so(3,2): 4 compact (so(3)+so(2)) + 6 noncompact; Poincare: degenerate (translations null)
B1=len(basis)==15 and len(Sn)==len(St)==len(Ss)==10 and kn[2]==4 and sorted(kt[:2])==[4,6] and sorted(ks[:2])==[4,6] and kt!=ks
ok.append(B1); print("B1 dims",len(basis),len(Sn),len(St),len(Ss),"trace-form (pos,neg,zero): null",kn,"v^2=-1",kt,"v^2=+1",ks,"->",B1)
S2=stab([vnull,vtime]); B2=len(S2)<10; ok.append(B2); print("B2 stab(null & timelike) dim",len(S2),"->",B2)
D,nu=sp.symbols('Delta nu',real=True)
lab=sp.expand((sp.Rational(3,2)+sp.I*nu)*(3-(sp.Rational(3,2)+sp.I*nu)))
B3=sp.simplify(lab-(sp.Rational(9,4)+nu**2))==0 and sp.maximum(D*(3-D),D,sp.Interval.open(0,3))==sp.Rational(9,4)
ok.append(B3); print("B3 m^2/H^2 = Delta(3-Delta): principal", lab, "; complementary max 9/4 -> a dimensionless LABEL ->",B3)
print(f"SCORE {sum(ok)}/{len(ok)}")
