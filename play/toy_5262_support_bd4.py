import numpy as np, sys
exec(open('bd2.py').read().split('print("="*80)')[0])
rng=np.random.default_rng(999)
def make_ESU3(N,T=2.0):
    """the DESCENDED commit order: R x S^3, 4-dimensional. (Einstein static universe.)"""
    t=rng.uniform(0,T,N); x=rng.normal(size=(N,4)); x/=np.linalg.norm(x,axis=1)[:,None]
    def fut(i,J):
        return (t[J]-t[i]>0)&((t[J]-t[i])>np.arccos(np.clip(x[J]@x[i],-1,1)))
    return t,fut,None,None
print("="*80)
print("POWER LEG -- can the instrument distinguish FLAT from CURVED at 4D?")
print("="*80)
print("★ PRE-REGISTERED POINT, and it corrects the task wording: R x S^3 is CONFORMALLY flat,")
print("  NOT flat. The Einstein static universe has positive spatial curvature (R = 6/a^2 > 0).")
print("  A causal set encodes order + number = conformal structure + volume = the FULL metric,")
print("  so BD_4 on a uniform ESU sprinkling should read NONZERO. 'Convergence to flat 4D' is")
print("  the wrong expectation for this object; the right test is FLAT vs ESU separation.")
print()
print("   geometry              N     K    mean B_4       sem       vs flat")
res={}
for name,mk,N,K in [("flat 4D Minkowski", lambda n: make_MINK(n,4), 800,16),
                    ("commit order R x S^3", lambda n: make_ESU3(n), 800,16)]:
    vals=[]
    for _ in range(K):
        t,fut,pas,sub=mk(N); C=causal_matrix(N,fut)
        vals.append(BD_ones(C,*BD4,rho=N,d=4))
    v=np.array(vals); res[name]=(v.mean(),v.std(ddof=1)/np.sqrt(K))
    print("   %-21s %4d  %2d   %+9.4f   %7.4f"%(name,N,K,v.mean(),v.std(ddof=1)/np.sqrt(K)))
    sys.stdout.flush()
a,b=res["flat 4D Minkowski"],res["commit order R x S^3"]
sep=abs(a[0]-b[0])/np.sqrt(a[1]**2+b[1]**2)
print()
print("   separation flat vs ESU = %.2f sigma"%sep)
print("   => %s"%("INSTRUMENT HAS POWER at this N/K" if sep>3 else
      "NO POWER at this N/K -- the sem swamps the curvature signal; needs larger N/K or smearing"))
