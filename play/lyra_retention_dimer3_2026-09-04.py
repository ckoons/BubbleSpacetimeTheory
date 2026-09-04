import math
from collections import deque
from dimer import torus, matchings
from dimer2 import cycles4, flips_generic, classes
print("DIMER CREATION TEST: delete one edge (forbid a bond). Selective step: some parent states die.")
for L,Mm in [(4,4),(4,6)]:
    V,idx,E,faces=torus(L,Mm); n=len(V)
    Ms=matchings(n,E); cyc=cycles4(n,E); comp,nc=classes(Ms,cyc)
    print("  parent torus %dx%d: %d matchings, %d classes, R=%.3f bits"%(L,Mm,len(Ms),nc,math.log2(nc)))
    rows={}
    for e in E:
        E2=[x for x in E if x!=e]
        Ms2=[m for m in Ms if e not in m]
        if not Ms2: continue
        cyc2=cycles4(n,E2)
        c2,nc2=classes(Ms2,cyc2)
        rows.setdefault((len(Ms)-len(Ms2),nc2),0)
        rows[(len(Ms)-len(Ms2),nc2)]+=1
    for (excl,nc2),cnt in sorted(rows.items()):
        verdict="CREATES %+.3f bits"%(math.log2(nc2)-math.log2(nc)) if nc2>nc else ("destroys" if nc2<nc else "conserves")
        print("     %2d edges: excluded %3d of %d states -> %3d classes   %s"%(cnt,excl,len(Ms),nc2,verdict))
