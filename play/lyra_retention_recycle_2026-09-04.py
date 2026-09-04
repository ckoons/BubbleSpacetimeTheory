import itertools, math, random
from dimer import torus, matchings
from dimer2 import cycles4, classes
random.seed(31)
def budget(Ms,comp,nc):
    N=len(Ms); sz=[0]*nc
    for k in comp: sz[k]+=1
    H=math.log2(N); R=-sum((s/N)*math.log2(s/N) for s in sz if s)
    return H,R,H-R
def st(n,E,cap=60000):
    Ms=matchings(n,E)
    if not Ms or len(Ms)>cap: return None
    comp,nc=classes(Ms,cycles4(n,E)); return Ms,comp,nc
# --- (A) realized factors in the g=3 chain, from the recorded state counts
gs=[3108,3656,4126,5222,3276,3754,4224,5413,3114,3896,4570,5164,3284,4019,4659,5499,2798]
gf=[];sf=[]
for i in range(1,len(gs)):
    r=gs[i]/gs[i-1]
    (gf if i%4 else sf).append(r)
import statistics as stx
lf=stx.mean([math.log2(x) for x in gf]); ls=stx.mean([math.log2(x) for x in sf])
print("(A) THRESHOLD, using the factors the POLICY actually realised (not uniform samples)")
print("    growth  log2 f = %+.4f  (selected: the chain retries until states increase)"%lf)
print("    refusal log2 s = %+.4f  (selected: the chain takes the R-maximising pair)"%ls)
print("    dH per cycle at g=3 = %+.4f   (measured in the chain: -0.038)"%(3*lf+ls))
print("    break-even g* = %.2f   (observed: just above 3)"%(-ls/lf))
print("    with UNIFORMLY SAMPLED factors the same formula gave g* = 6.58 — the threshold is a")
print("    property of the SEARCH POLICY, not of the instance alone.")
print()
# --- (B) can capacity be RECYCLED without losing the record?
print("(B) RECYCLING: after refusals have burnt the heat, can adding an edge back restore")
print("    capacity without merging the classes it bought?")
V,idx,E0,faces=torus(4,6); n=len(V)
E=list(E0); S=st(n,E)
def prohibit(n,E,S,samples=90):
    Ms,comp,nc=S
    pairs=random.sample(list(itertools.combinations(E,2)),samples)
    best=None
    for e1,e2 in pairs:
        E2=[x for x in E if x not in (e1,e2)]
        sub=[m for m in Ms if e1 not in m and e2 not in m]
        if len(sub)<12: continue
        c2,nc2=classes(sub,cycles4(n,E2))
        b=budget(sub,c2,nc2)
        if best is None or b[1]>best[0]: best=(b[1],E2,(sub,c2,nc2))
    return (None,None) if best is None else (best[1],best[2])
for k in range(3):
    E2,S2=prohibit(n,E,S)
    if E2 is None: break
    E,S=E2,S2
H,R,Ht=budget(*S)
print("    after 3 refusals: %d states, %d classes, R=%.3f  H=%.3f  H_thermo=%.3f"%(len(S[0]),S[2],R,H,Ht))
allE=set(tuple(sorted(p)) for p in itertools.combinations(range(n),2))
missing=sorted(allE-set(E))
rows=[]
for e in missing:
    E3=E+[e]
    S3=st(n,E3)
    if S3 is None: continue
    H3,R3,Ht3=budget(*S3)
    rows.append((H3-H,R3-R,Ht3-Ht,e,S3[2]))
rows.sort(key=lambda r:(-r[1],-r[0]))
print("    tried %d single-edge additions; best by record preserved:"%len(rows))
print("       dH      dR      dH_thermo   classes   edge")
for r in rows[:6]:
    print("      %+.3f  %+.3f   %+.3f      %4d     %s"%(r[0],r[1],r[2],r[4],r[3]))
best_keep=[r for r in rows if r[1]>-1e-9]
print("    additions that raise capacity WITHOUT losing record: %d of %d"%(len(best_keep),len(rows)))
if best_keep:
    b=max(best_keep,key=lambda r:r[0])
    print("    best such: dH %+.3f, dR %+.3f, dH_thermo %+.3f  (edge %s)"%(b[0],b[1],b[2],b[3]))
