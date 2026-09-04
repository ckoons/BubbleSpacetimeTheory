import math
from dimer import torus, matchings
from dimer2 import cycles4, classes
for L,Mm in [(4,4),(4,6)]:
    V,idx,E,faces=torus(L,Mm); n=len(V)
    Ms=matchings(n,E); cyc=cycles4(n,E); comp,nc=classes(Ms,cyc)
    emptied_tot=split_tot=0; rows={}
    for e in E:
        E2=[x for x in E if x!=e]
        keep=[i for i,m in enumerate(Ms) if e not in m]
        if not keep: continue
        sub=[Ms[i] for i in keep]
        c2,nc2=classes(sub,cycles4(n,E2))
        alive={comp[i] for i in keep}
        emptied=nc-len(alive)
        # did any surviving parent class break into more than one child class?
        m={}
        for t,i in enumerate(keep): m.setdefault(comp[i],set()).add(c2[t])
        split=sum(len(v)-1 for v in m.values())
        emptied_tot+=emptied; split_tot+=split
        rows.setdefault((emptied,split,nc2),0); rows[(emptied,split,nc2)]+=1
    print("torus %dx%d (%d classes): over all %d single-bond prohibitions"%(L,Mm,nc,len(E)))
    for (em,sp,nc2),cnt in sorted(rows.items()):
        print("   %2d edges -> %d class(es) EMPTIED, %d SPLIT, child has %d classes"%(cnt,em,sp,nc2))
    print("   totals: %d classes emptied, %d splits, across all prohibitions"%(emptied_tot,split_tot))
