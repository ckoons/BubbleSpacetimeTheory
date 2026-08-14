import numpy as np, sys, time
exec(open('bigN.py').read().split('if __name__')[0])
rng=np.random.default_rng(202)
def by_size(t,fut,pas,sub,N,want=260):
    allJ=np.arange(N); order=np.argsort(t)
    lo=order[:N//4]; hi=order[-N//4:]
    rs=[];sz=[]
    for _ in range(60000):
        a=int(rng.choice(lo)); b=int(rng.choice(hi))
        fa=fut(a,allJ)
        if not fa[b]: continue
        mid=np.nonzero(fa&pas(b,allJ))[0]
        m=len(mid)
        if m<40 or m>700: continue
        R=sub(mid); rs.append(R.sum()/(m*(m-1)/2)); sz.append(m)
        if len(rs)>=want: break
    return np.array(rs),np.array(sz)
N=20000
print("DOES r DEPEND ON INTERVAL SIZE? (the confound that would fake a dimension)")
print("  binned by |interval|; if r is flat in size, the cross-geometry comparison is safe")
print()
bins=[(40,90),(90,160),(160,300),(300,700)]
print("  geometry              " + "  ".join("|I|%d-%d"%b for b in bins))
for name,mk in [("Minkowski d=4",lambda: make_MINK(N,4)),
                ("Minkowski d=5",lambda: make_MINK(N,5)),
                ("BST commit (RxS^4)",lambda: make_ESU(N,4,2.0))]:
    t,fut,pas,sub=mk(); rs,sz=by_size(t,fut,pas,sub,N)
    row=[]
    for a,b in bins:
        sel=(sz>=a)&(sz<b)
        row.append(("%.4f(%d)"%(np.median(rs[sel]),sel.sum())) if sel.sum()>=8 else "   --   ")
    print("  %-21s %s"%(name," ".join("%-12s"%c for c in row)))
    sys.stdout.flush()
