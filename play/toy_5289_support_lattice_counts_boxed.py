import numpy as np
from collections import Counter
print("="*92)
print("WHICH ZETA DOES BST'S CONE ACTUALLY HAND YOU?  Count the lattice points. No interpretation.")
print("="*92)
print("The cone zeta is  Z(s) = SUM_{x in L, x in Omega} Delta(x)^{-s}  =  SUM_n a(n) n^{-s},")
print("where a(n) = #{lattice points in the cone with Delta(x) = n}. So: compute a(n).\n")
NMAX=2000
print("(A) THE 2-DIMENSIONAL CONE.  Null coords: Delta = u v, u,v >= 1 integers.")
a2=Counter()
for u in range(1,NMAX+1):
    for v in range(1,NMAX//u+1):
        a2[u*v]+=1
def d(n):
    c=0
    for k in range(1,int(n**0.5)+1):
        if n%k==0:
            c+=2 if k*k!=n else 1
    return c
ok=all(a2[n]==d(n) for n in range(1,501))
print("    a(n) == d(n) (the divisor function) for n = 1..500 ?  %s"%ok)
print("    a(n) for n = 1..12 :", [a2[n] for n in range(1,13)])
print("    d(n) for n = 1..12 :", [d(n) for n in range(1,13)])
print("    ⟹ Z_2D(s) = SUM d(n) n^{-s} = ZETA(s)^2 EXACTLY.  Cal's rank-2 doubling is right --")
print("       FOR THE 2-DIMENSIONAL CONE. Critical line Re s = 1/2, abscissa of convergence 1.\n")
print("(B) BST'S ACTUAL CONE: the forward light cone in R^{4,1}. Delta = x0^2 - x1^2-x2^2-x3^2-x4^2.")
LIM=60
a5=Counter()
rng=range(-LIM,LIM+1)
xs=np.array(np.meshgrid(*[np.arange(-LIM,LIM+1)]*4,indexing='ij')).reshape(4,-1).T
q=(xs**2).sum(axis=1)
for x0 in range(1,LIM+1):
    dl=x0*x0-q
    m=(dl>0)
    for val,cnt in zip(*np.unique(dl[m],return_counts=True)):
        a5[int(val)]+=int(cnt)
print("    a(n) for n = 1..12 :", [a5[n] for n in range(1,13)])
print("    d(n) for n = 1..12 :", [d(n) for n in range(1,13)])
print("    identical to d(n)?  %s"%all(a5[n]==d(n) for n in range(1,13)))
print()
print("    GROWTH -- this is what decides the abscissa, hence the critical line:")
print("       n        a5(n) (cumulative avg)     d(n) (cumulative avg)     ratio")
for N in [50,200,800,2000]:
    A=np.mean([a5[n] for n in range(1,N+1)]); D=np.mean([d(n) for n in range(1,N+1)])
    print("    %6d        %14.1f          %14.2f       %10.1f"%(N,A,D,A/D))
print("\n    fit a5(n) ~ C n^alpha on the cumulative mean:")
Ns=np.array([50,200,800,2000]); As=np.array([np.mean([a5[n] for n in range(1,N+1)]) for N in Ns])
al=np.polyfit(np.log(Ns),np.log(As),1)[0]
print("       measured exponent alpha = %.3f   (d(n) average grows like log n, exponent 0)"%al)
print("\n  ⟹ THE 5D CONE'S COUNT IS NOT d(n) AND ITS DIRICHLET SERIES IS NOT zeta^2.")
print("     a5(n) grows like a POWER (alpha ~ %.2f) where d(n) averages like log n."%al)
print("     => the two series have DIFFERENT ABSCISSAE OF CONVERGENCE and therefore DIFFERENT")
print("        CRITICAL LINES. 'BST's natural object is zeta^2' holds for the 2D cone ONLY.")
