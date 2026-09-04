import itertools, math, random
from dimer import torus, matchings
from dimer2 import cycles4, classes
random.seed(23)
CAP=9000
def budget(Ms,comp,nc):
    N=len(Ms); sz=[0]*nc
    for k in comp: sz[k]+=1
    H=math.log2(N); R=-sum((s/N)*math.log2(s/N) for s in sz if s)
    return H,R,H-R
def st(n,E):
    Ms=matchings(n,E)
    if not Ms or len(Ms)>CAP: return None
    comp,nc=classes(Ms,cycles4(n,E)); return Ms,comp,nc
def prohibit(n,E,S,samples=120):
    Ms,comp,nc=S
    pairs=list(itertools.combinations(E,2))
    if len(pairs)>samples: pairs=random.sample(pairs,samples)
    best=None
    for e1,e2 in pairs:
        E2=[x for x in E if x not in (e1,e2)]
        sub=[m for m in Ms if e1 not in m and e2 not in m]
        if len(sub)<12: continue
        c2,nc2=classes(sub,cycles4(n,E2))
        b=budget(sub,c2,nc2)
        if best is None or b[1]>best[0]: best=(b[1],E2,(sub,c2,nc2))
    return (None,None) if best is None else (best[1],best[2])
def grow(n,E,S):
    for _ in range(12):
        a,b=n,n+1
        s1=random.randrange(n); s2=random.randrange(n)
        E2=list(E)+[tuple(sorted((a,b))),tuple(sorted((s1,a))),tuple(sorted((s2,b)))]
        S2=st(n+2,E2)
        if S2 is not None and len(S2[0])>len(S[0]): return E2,n+2,S2
    return None,n,S
def run(g,steps=16):
    V,idx,E,faces=torus(4,6); n=len(V); S=st(n,E); E1=list(E)
    H,R,Ht=budget(*S)
    print("  growth per selection = %d ; start: %d states, %d classes, R=%.3f H=%.3f Hth=%.3f"%(g,len(S[0]),S[2],R,H,Ht))
    sel=0; prev=(H,R,Ht)
    for t in range(steps):
        if (t%(g+1))<g:
            E2,n2,S2=grow(n,E1,S)
            if E2 is None: continue
            E1,n,S=E2,n2,S2; kind="grow"
        else:
            E2,S2=prohibit(n,E1,S)
            if E2 is None: print("     no admissible refusal; stop"); break
            E1,S=E2,S2; kind="REFUSE"; sel+=1
        H,R,Ht=budget(*S)
        eff=(R-prev[1])/max(1e-9,(prev[2]-Ht)) if kind=="REFUSE" else float('nan')
        print("     %-6s states %5d  classes %4d   R=%.3f  H=%.3f  Hth=%.3f%s"%(
            kind,len(S[0]),S[2],R,H,Ht, "   efficiency %.2f"%eff if kind=="REFUSE" else ""))
        prev=(H,R,Ht)
    print("     -> %d refusals, final R = %.3f bits"%(sel,R))
print("DOES R GROW WITHOUT BOUND? vary how much growth pays for each refusal (torus 4x6)")
for g in (1,2,3):
    run(g)
    print()
