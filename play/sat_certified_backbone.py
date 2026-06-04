# STEP 1 (certified extractor) + STEP 2 (|B_res| scaling), shared solver backbone.
# For each backbone var v with frozen value val: phi ^ (v != val) is UNSAT.
# min_refute_depth = fewest DPLL branch-levels to refute it (0 = unit prop alone).
# Certified-at-depth-<=d = poly-time certified bits.  Compare to polarity (uncertified).
import random, sys
import numpy as np
from collections import defaultdict
sys.setrecursionlimit(100000)
def rand3sat(n,m,rng):
    return [[(v, rng.choice([1,-1])) for v in rng.sample(range(n),3)] for _ in range(m)]
def unit_prop(clauses,a):
    a=dict(a)
    while True:
        prog=False
        for c in clauses:
            if any(a.get(v)==s for v,s in c): continue
            un=[(v,s) for v,s in c if v not in a]
            if not un: return None       # conflict
            if len(un)==1:
                v,s=un[0]; a[v]=s; prog=True
        if not prog: return a
def refute_within(clauses, a, depth):
    # can DPLL refute (reach conflict on ALL branches) within 'depth' branch levels?
    u=unit_prop(clauses,a)
    if u is None: return True
    if depth==0: return False
    # branch on a var appearing in an unsatisfied clause
    cand=None
    for c in clauses:
        if any(u.get(v)==s for v,s in c): continue
        for v,s in c:
            if v not in u: cand=v; break
        if cand is not None: break
    if cand is None: return False  # satisfied, not refuted
    return (refute_within(clauses,{**u,cand:1},depth-1) and
            refute_within(clauses,{**u,cand:-1},depth-1))
def min_refute_depth(clauses, a, cap=4):
    for d in range(cap+1):
        if refute_within(clauses,a,d): return d
    return cap+1
def dpll(clauses,n,budget):
    def rec(a):
        budget[0]-=1
        if budget[0]<0: return None
        u=unit_prop(clauses,a)
        if u is None: return None
        if len(u)==n: return u
        cnt=defaultdict(int)
        for c in clauses:
            if any(u.get(v)==s for v,s in c): continue
            for v,s in c:
                if v not in u: cnt[v]+=1
        if not cnt:
            for v in range(n):
                if v not in u: u[v]=1
            return u
        v=max(cnt,key=cnt.get)
        for s in (1,-1):
            r=rec({**u,v:s})
            if r is not None: return r
        return None
    return rec({})
def backbone(clauses,n):
    sol=dpll(clauses,n,[300000])
    if sol is None: return None
    B={}
    for v in range(n):
        if dpll(clauses+[[(v,-sol[v])]],n,[300000]) is None: B[v]=sol[v]
    return B
def field(clauses,n):
    pos=defaultdict(int);neg=defaultdict(int);deg=defaultdict(int)
    for c in clauses:
        for v,s in c:
            deg[v]+=1;(pos if s>0 else neg)[v]+=1
    return np.array([(pos[v]-neg[v])/max(deg[v],1) for v in range(n)])
rng=random.Random(33)
print(f"{'n':>3} {'pol-acc':>7} {'cert@0':>7} {'cert<=1':>7} {'cert<=2':>7} {'hard(>=3)/n':>11} {'|B|/n':>6}")
for n in [16,24,32]:
    m=round(4.2*n); pol=[];c0=[];c1=[];c2=[];hard=[];bsz=[];nf=0
    tgt=18 if n<=24 else 10; tries=0
    while nf<tgt and tries<tgt*6:
        tries+=1
        cl=rand3sat(n,m,rng); B=backbone(cl,n)
        if not B or len(B)<2: continue
        f=field(cl,n)
        depths={v:min_refute_depth(cl,{v:-B[v]}) for v in B}
        accv=np.mean([(f[v]>0)==(B[v]>0) for v in B])
        pol.append(accv)
        c0.append(np.mean([depths[v]<=0 for v in B]))
        c1.append(np.mean([depths[v]<=1 for v in B]))
        c2.append(np.mean([depths[v]<=2 for v in B]))
        hard.append(np.mean([depths[v]>=3 for v in B])*len(B)/n)
        bsz.append(len(B)/n); nf+=1
    print(f"{n:>3} {np.mean(pol):>7.3f} {np.mean(c0):>7.3f} {np.mean(c1):>7.3f} {np.mean(c2):>7.3f} {np.mean(hard):>11.3f} {np.mean(bsz):>6.2f}")
print("\npol-acc = uncertified polarity accuracy; cert<=d = fraction of backbone bits")
print("certifiable by depth-<=d refutation (poly-time); hard(>=3)/n = residual |B_res|/n.")
