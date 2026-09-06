import math
from collections import Counter
from lyra_retention_torus66_2026_09_05 import cycles4, flip_edges, components, R_bits
from lyra_retention_twocert_2026_09_05 import torus_edges, matchings, intra_cycles
# CHECK 1: at k=16 cold, is the R gain from SINGLETON (frozen) classes?
nh=16; n=32
import random; rng=random.Random(7)
pool=[tuple(sorted((u,v))) for u in range(nh) for v in range(nh,n)]; rng.shuffle(pool)
for k in (0,16):
    E=sorted(set(torus_edges(4,4)+torus_edges(4,4,off=nh)+pool[:k]))
    ei={e:i for i,e in enumerate(E)}
    Ms=matchings(n,E,ei); mv=intra_cycles(n,E,ei,nh)
    fe=flip_edges(Ms,mv); N=len(Ms)
    comp,nc,sz=components([True]*N,fe,N)
    singles=sum(1 for s in sz if s==1)
    mass=sum(s for s in sz if s==1)/N
    print("k=%2d  N=%6d  classes=%4d  R=%.4f  singleton classes=%d  mass in singletons=%.4f%%  median class=%d"
          %(k,N,nc,R_bits(sz),singles,100*mass,sorted(sz)[len(sz)//2]))
# CHECK 2: unit sizes for an n-way coupling test
for (L,M) in [(3,4),(4,4),(3,6),(4,6)]:
    E=torus_edges(L,M); ei={e:i for i,e in enumerate(E)}
    Ms=matchings(L*M,E,ei)
    mv=cycles4(L*M,E,ei); fe=flip_edges(Ms,mv)
    comp,nc,sz=components([True]*len(Ms),fe,len(Ms))
    print("unit %dx%d: %5d matchings  %3d classes  R=%.4f   -> n=3 product %d, n=4 product %d"
          %(L,M,len(Ms),nc,R_bits(sz),len(Ms)**3,len(Ms)**4))
