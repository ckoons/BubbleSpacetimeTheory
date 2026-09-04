import itertools, math, random
from dimer import torus, matchings
from dimer2 import cycles4, classes
random.seed(17)
def budget(Ms,comp,nc):
    N=len(Ms); sizes=[0]*nc
    for k in comp: sizes[k]+=1
    H=math.log2(N)
    R=-sum((s/N)*math.log2(s/N) for s in sizes if s)
    Ht=sum((s/N)*math.log2(s) for s in sizes if s)
    return H,R,Ht,sizes
def st(n,E):
    Ms=matchings(n,E)
    if not Ms: return None
    comp,nc=classes(Ms,cycles4(n,E)); return Ms,comp,nc
def prohibit(n,E,S,samples=150):
    Ms,comp,nc=S
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
V,idx,E,faces=torus(4,6); n=len(V)
S=st(n,E); E1=list(E)
print("CHAIN 1 (pure selection), EXACT entropies:  R = H(class distribution), not log2(#classes)")
print(" step  states  classes   H       R_exact  R_naive  H_thermo   dR       -dH_thermo   law dR<=-dH_th")
prev=None
for t in range(0,7):
    if t>0:
        E2,S2=prohibit(n,E1,S)
        if E2 is None: break
        E1,S=E2,S2
    H,R,Ht,sizes=budget(*S)
    line=" %d    %6d   %4d   %6.3f   %6.3f   %6.3f   %6.3f"%(t,len(S[0]),S[2],H,R,math.log2(S[2]),Ht)
    if prev:
        dR=R-prev[1]; dHt=Ht-prev[2]
        ok = dR <= -dHt + 1e-12
        line+="   %+6.3f    %+6.3f      %s"%(dR,-dHt,"HOLDS" if ok else "VIOLATED")
    print(line)
    prev=(H,R,Ht)
