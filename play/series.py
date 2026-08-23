import numpy as np, itertools
from numpy.polynomial import polynomial as P
n=6
A=np.zeros((n,n));  # path graph P6 adjacency = J_W + J_W^dagger
for i in range(n-1): A[i,i+1]=A[i+1,i]=1
ev=[0,2,4]; od=[1,3,5]
blk=lambda M,r,c: M[np.ix_(r,c)]
print("spectrum 2cos(k pi/7):", np.round(np.sort(np.linalg.eigvalsh(A)),4))
print("Q|even  =\n", blk(A,ev,ev).astype(int))
S = blk(A@A,ev,ev); print("S = Q^2|even =\n", S.astype(int))
print("Q^4|even =\n", blk(np.linalg.matrix_power(A,4),ev,ev).astype(int))
print("S^2      =\n", (S@S).astype(int), "   S^2 == Q^4|even ?", np.allclose(S@S, blk(np.linalg.matrix_power(A,4),ev,ev)))
# CLAIM 1: Q^{2k}|even = S^k  for all k   (A block-off-diagonal => A^2 = diag(MM*, M*M))
print("\nCLAIM 1  Q^{2k}|even == S^k :",
      all(np.allclose(blk(np.linalg.matrix_power(A,2*k),ev,ev), np.linalg.matrix_power(S,k)) for k in range(1,12)))
# CLAIM 2: Cayley-Hamilton => every series in S collapses to  a*S^2 + b*S + c*1
cp=np.poly(S); print("char poly of S:", np.round(cp,10), " -> S^3 =", f"{-cp[1]:.0f} S^2 + {-cp[2]:.0f} S + {-cp[3]:.0f} 1")
print("CLAIM 2  S^3 reduction holds:",
      np.allclose(np.linalg.matrix_power(S,3), -cp[1]*S@S - cp[2]*S - cp[3]*np.eye(3)))
# CLAIM 3: corner ratio of G = b*S + a*S^2 + c*1  is  a/(b+4a), independent of c
print("\nCLAIM 3  corner ratio:")
for (a,b,c) in [(1,1,0),(1,1,7.3),(0.19,1,0),(1,3,-2),(2.5,1,100)]:
    G=b*S+a*(S@S)+c*np.eye(3); r=G[0,2]/G[1,2]
    print(f"   a={a:<5} b={b:<3} c={c:<6} ratio={r:.6f}   a/(b+4a)={a/(b+4*a):.6f}  match={abs(r-a/(b+4*a))<1e-12}")
# CLAIM 4: random long series collapse to the same one-parameter family
print("\nCLAIM 4  random 10-term series -> t and ratio, check ratio == t/(1+4t):")
rng=np.random.default_rng(7)
for _ in range(4):
    ak=rng.normal(size=10)
    G=sum(ak[k]*np.linalg.matrix_power(S,k+1) for k in range(10))
    # reduce to a*S^2+b*S+c*1 by solving on the 3-dim basis {1,S,S^2}
    Bs=np.stack([np.eye(3).ravel(),S.ravel(),(S@S).ravel()],1)
    c,b,a = np.linalg.lstsq(Bs,G.ravel(),rcond=None)[0]
    t=a/b; print(f"   t={t: .6f}  ratio={G[0,2]/G[1,2]: .6f}  t/(1+4t)={t/(1+4*t): .6f}")
# CLAIM 5: bound for positive-weight series (a_2k >= 0 => a,b >= 0 => ratio in [0,1/4))
print("\nCLAIM 5  positive-weight sweep, max ratio:")
best=0
for _ in range(200000):
    ak=rng.random(8)
    G=sum(ak[k]*np.linalg.matrix_power(S,k+1) for k in range(8))
    best=max(best,G[0,2]/G[1,2])
print(f"   sup over 2e5 positive-coefficient series = {best:.6f}   (analytic sup = 1/4 = 0.25)")
# what t the pinned band requires (INVERSION, target seen - labelled)
for R in (0.081,0.108): print(f"   band R={R} -> t = R/(1-4R) = {R/(1-4*R):.4f}")
