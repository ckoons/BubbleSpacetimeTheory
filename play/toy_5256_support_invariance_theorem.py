import numpy as np
exec(open('concentration.py').read().split('print("THE TRAP')[0])
rng=np.random.default_rng(555)
n=np.zeros(5); n[4]=1.0
print("="*76)
print("THE THEOREM, then the demonstration")
print("="*76)
print("CORPUS (CLAUDE.md, root):  rho_commit(tau) = exp(-tau H_B / hbar)  with  H_B = Casimir of K = SO(5)xSO(2)")
print()
print("  A CASIMIR COMMUTES WITH ITS OWN GROUP, BY DEFINITION.")
print("  => [H_B, SO(5)] = 0  =>  [exp(-tau H_B), SO(5)] = 0")
print("  => the measure exp(-tau H_B) induces on S^4 is SO(5)-INVARIANT")
print("  => and the ONLY SO(5)-invariant probability measure on S^4 is the ROUND one.")
print("  => T = the round/null value EXACTLY;  A = chance.   OUTCOME N, BY SYMMETRY, before any computation.")
print()
print("DEMONSTRATION -- an SO(5)-invariant weight cannot concentrate, whatever tau or the spectrum:")
N=4000
null=np.array([T_stat(unif_S4(N)) for _ in range(200)]); mu,sd=null.mean(),null.std()
print("   N-matched null: T = %.5f +- %.5f      (bar for P: A > 0.917)"%(mu,sd))
print()
print("   weight w(x)                          T        z       A       ruling")
for name,w in [("invariant  w=1 (round)",           lambda X: np.ones(len(X))),
               ("invariant  w=exp(-2*|x|^2)=const", lambda X: np.exp(-2*np.sum(X**2,axis=1))),
               ("invariant  w=f(SO(5) Casimir)",    lambda X: np.exp(-0.7)*np.ones(len(X)))]:
    X=unif_S4(N); p=w(X); p/=p.sum()
    idx=rng.choice(N,N,p=p); Y=X[idx]
    C=(Y.T@Y)/N; ev,V=np.linalg.eigh(C); T=ev[0]; A=abs(V[:,0]@n)
    z=(mu-T)/sd
    print("   %-36s %.5f  %+6.2f  %.3f   %s"%(name,T,z,A,"N (uniform)" if z<5 else "??"))
print()
print("   ... and a weight that BREAKS SO(5) along V5 (i.e. the thing that would have to be ADDED):")
for lam in [1.0,3.0,8.0]:
    X=unif_S4(N); p=np.exp(-lam*X[:,4]**2); p/=p.sum()
    idx=rng.choice(N,N,p=p); Y=X[idx]
    C=(Y.T@Y)/N; ev,V=np.linalg.eigh(C); T=ev[0]; A=abs(V[:,0]@n)
    print("   %-36s %.5f  %+6.2f  %.3f   %s"%("w=exp(-%.0f*(x.V5)^2)  [NOT invariant]"%lam,T,(mu-T)/sd,A,
        "P" if (mu-T)/sd>5 and A>0.917 else "-"))
print()
print("  => the concentration is EXACTLY the SO(5)-breaking put in, and its axis is EXACTLY the axis of that term.")
