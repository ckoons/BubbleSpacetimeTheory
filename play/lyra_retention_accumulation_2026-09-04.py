import itertools, math, random
from dimer import torus, matchings
from dimer2 import cycles4, classes
random.seed(17)
def state(n,E):
    Ms=matchings(n,E)
    if not Ms: return None
    comp,nc=classes(Ms,cycles4(n,E))
    return Ms,comp,nc
def show(t,n,E,st,note):
    Ms,comp,nc=st
    print("  step %d  %-22s n=%2d  %6d states  %3d classes  R=%.3f bits  H=%.2f"%(
        t,note,n,len(Ms),nc,math.log2(nc),math.log2(len(Ms))))
def prohibit(n,E,st,samples=150):
    Ms,comp,nc=st
    pairs=list(itertools.combinations(E,2))
    if len(pairs)>samples: pairs=random.sample(pairs,samples)
    best=None
    for e1,e2 in pairs:
        E2=[x for x in E if x not in (e1,e2)]
        sub=[m for m in Ms if e1 not in m and e2 not in m]
        if len(sub)<12: continue
        c2,nc2=classes(sub,cycles4(n,E2))
        sc=(nc2,len(sub))
        if best is None or sc>best[0]: best=(sc,E2,(sub,c2,nc2))
    return (None,None) if best is None else (best[1],best[2])
def grow(n,E,st,S,T):
    a,b=n,n+1
    E2=list(E)+[tuple(sorted((a,b)))]+[tuple(sorted((s,a))) for s in S]+[tuple(sorted((s,b))) for s in T]
    s2=state(n+2,E2)
    return E2,n+2,s2

print("CHAIN 1 — pure prohibition, greedy on class count (torus 4x6)")
V,idx,E,faces=torus(4,6); n=len(V); st=state(n,E); show(0,n,E,st,"start")
E1,n1,st1=list(E),n,st
for t in range(1,7):
    E2,s2=prohibit(n1,E1,st1)
    if E2 is None: print("   no admissible prohibition"); break
    E1,st1=E2,s2; show(t,n1,E1,st1,"forbid 2 bonds")

print()
print("CHAIN 2 — alternate: grow (retains, multiplies states) then prohibit (creates)")
E1,n1=list(E),n; st1=state(n1,E1); show(0,n1,E1,st1,"start")
for t in range(1,9):
    if t%2==1:
        S=[random.randrange(n1)]; T=[random.randrange(n1)]
        E2,n2,s2=grow(n1,E1,st1,S,T)
        if s2 is None: print("   growth failed"); break
        E1,n1,st1=E2,n2,s2; show(t,n1,E1,st1,"grow a pair")
    else:
        E2,s2=prohibit(n1,E1,st1)
        if E2 is None: print("   no admissible prohibition"); break
        E1,st1=E2,s2; show(t,n1,E1,st1,"forbid 2 bonds")
