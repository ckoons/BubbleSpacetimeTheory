import itertools, math, random
from dimer import torus, matchings
from dimer2 import cycles4, classes
random.seed(4)
L,Mm=4,6
V,idx,E,faces=torus(L,Mm); n=len(V)
Ms=matchings(n,E); cyc=cycles4(n,E); comp,nc=classes(Ms,cyc)
pos={m:i for i,m in enumerate(Ms)}
print("parent: %d matchings, %d classes"%(len(Ms),nc))
tests=[((3,9),(13,14))]+random.sample(list(itertools.combinations(E,2)),5)
for e1,e2 in tests:
    E2=[x for x in E if x not in (e1,e2)]
    sub=[m for m in Ms if e1 not in m and e2 not in m]
    if len(sub)<2: continue
    c2,nc2=classes(sub,cycles4(n,E2))
    fwd={}
    for t,m in enumerate(sub): fwd.setdefault(comp[pos[m]],set()).add(c2[t])
    splits=sum(len(v)-1 for v in fwd.values())
    emptied=nc-len(fwd)
    print("  forbid %s,%s : %4d of %d states survive; %d parent classes survive, %d EMPTIED, %d SPLITS -> %d child classes  %s"%(
        e1,e2,len(sub),len(Ms),len(fwd),emptied,splits,nc2,"CREATES %+.2f bits"%(math.log2(nc2)-math.log2(nc)) if nc2>nc else ""))
