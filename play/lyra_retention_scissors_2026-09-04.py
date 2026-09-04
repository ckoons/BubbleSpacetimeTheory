import itertools, math, random
from dimer import torus, matchings
from dimer2 import cycles4, classes
random.seed(4)
def scan_pairs(L,Mm,limit=None):
    V,idx,E,faces=torus(L,Mm); n=len(V)
    Ms=matchings(n,E); cyc=cycles4(n,E); comp,nc=classes(Ms,cyc)
    pairs=list(itertools.combinations(E,2))
    if limit and len(pairs)>limit: pairs=random.sample(pairs,limit)
    rises=0; tested=0; best=None; rows={}
    for e1,e2 in pairs:
        E2=[x for x in E if x not in (e1,e2)]
        sub=[m for m in Ms if e1 not in m and e2 not in m]
        if len(sub)<2: continue
        c2,nc2=classes(sub,cycles4(n,E2))
        tested+=1
        # split test on surviving classes
        m={}
        for t,mm in enumerate(sub):
            k=comp[Ms.index(mm)] if False else None
        rows.setdefault(nc2,0); rows[nc2]+=1
        if nc2>nc:
            rises+=1
            if best is None: best=(e1,e2,nc,nc2,len(Ms),len(sub))
    print("torus %dx%d: parent %d classes; %d two-bond prohibitions tested; class count ROSE in %d"%(L,Mm,nc,tested,rises))
    print("   child class-count distribution: %s"%dict(sorted(rows.items())))
    if best: print("   example: forbid %s and %s -> %d classes (from %d), %d of %d states survive"%(best[0],best[1],best[3],best[2],best[5],best[4]))
scan_pairs(4,4)
scan_pairs(4,6,limit=300)
