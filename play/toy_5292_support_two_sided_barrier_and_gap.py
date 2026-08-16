import numpy as np, itertools
from scipy.spatial import Delaunay
rng=np.random.default_rng(437)
CAP=2_000_000
def chrom(adj,n,k,order=None):
    order=order or list(range(n))
    pos={v:i for i,v in enumerate(order)}
    col={}; cnt=[0]; hit=[False]
    def go(i):
        cnt[0]+=1
        if cnt[0]>CAP: hit[0]=True; return False
        if i==n: return True
        v=order[i]
        for c in range(k):
            if all(col.get(u)!=c for u in adj[v] if u in col):
                col[v]=c
                if go(i+1): return True
                del col[v]
        return False
    r=go(0); return r,cnt[0],hit[0]
print("="*92)
print("(1) THE TWO-SIDED BARRIER FOR ANY 4-COLOUR ARGUMENT")
print("="*92)
for name,n in [("K_4",4),("K_5",5)]:
    adj=[[j for j in range(n) if j!=i] for i in range(n)]
    e=n*(n-1)//2
    res=[]
    for k in (3,4,5):
        ok,_,_=chrom(adj,n,k); res.append("%d-col:%s"%(k,"YES" if ok else "NO "))
    print("   %-4s edges=%2d  vs Euler bound 3v-6=%2d -> %-11s   %s"%(
        name,e,3*n-6,"PLANAR ok" if e<=3*n-6 else "NON-PLANAR",  "  ".join(res)))
print("\n   ⟹ (a) K_4 is PLANAR and NOT 3-colourable => a valid argument must NOT deliver 3.")
print("      (b) K_5 is NON-PLANAR and NOT 4-colourable => PLANARITY must be load-bearing; any")
print("          argument that never uses planarity would 4-colour K_5, which is impossible.")
print("      An argument failing (a) proves a falsehood; one failing (b) proves nothing about planar graphs.")
print()
print("="*92)
print("(2) THE REAL DIFFICULTY: 5 IS EASY, 4 IS HARD. Same graphs, worst-case vertex order.")
print("="*92)
def planar_graph(n,rng):
    pts=rng.random((n,2)); tri=Delaunay(pts)
    adj=[set() for _ in range(n)]
    for s in tri.simplices:
        for a,b in itertools.combinations(s,2): adj[a].add(b); adj[b].add(a)
    return [sorted(a) for a in adj]
print("      n    min deg   4-col nodes   5-col nodes    ratio 4/5")
for n in [20,30,40,50]:
    r4=[];r5=[];md=[]
    for _ in range(15):
        adj=planar_graph(n,rng); md.append(min(len(a) for a in adj))
        order=sorted(range(n),key=lambda v:-len(adj[v]))     # a deliberately adversarial order
        _,c4,_=chrom(adj,n,4,order); _,c5,_=chrom(adj,n,5,order)
        r4.append(c4); r5.append(c5)
    print("    %4d      %3d    %11d   %11d    %8.1f"%(n,int(np.median(md)),int(np.median(r4)),int(np.median(r5)),np.median(r4)/np.median(r5)))
print("\n   every planar graph has a vertex of degree <= 5 (Euler): confirmed, min degree <= 5 above.")
print("   ⟹ 5-colouring is essentially free (the degree-<=5 vertex always has a spare colour);")
print("      4-colouring costs real search. THAT GAP *IS* THE THEOREM.")
print()
print("="*92)
print("(3) ★ WHERE EXACTLY THE 5-PROOF BREAKS FOR 4 -- the barrier to name")
print("="*92)
print("  5-colour proof (one page): take v with deg(v) <= 5. If deg(v) <= 4, a colour is free. If")
print("  deg(v) = 5, its neighbours use all 5 colours; take a Kempe chain in colours {1,3}. If the")
print("  chain from n1 does not reach n3, swap it and free colour 1. DONE.")
print("  4-colour attempt (Kempe 1879): same move with deg(v) = 5 and only 4 colours -- now TWO")
print("  Kempe chains must be swapped, and HEAWOOD (1890) exhibited a configuration where the two")
print("  chains INTERLOCK, so swapping one destroys the other. That single gap stood for 86 years")
print("  and was closed only by Appel-Haken (1976) with 1936 reducible configurations + discharging.")
print()
print("  ★ SO THE TEST FOR ANY BST 4-COLOUR ARGUMENT IS ONE QUESTION:")
print("      WHERE DOES IT HANDLE THE INTERLOCKING KEMPE CHAINS AT A DEGREE-5 VERTEX?")
print("    If it has no such step, it is reproducing Kempe's 1879 error, and it proves the")
print("    5-COLOUR theorem, not the 4-colour theorem. That is a checkable, one-line audit.")
