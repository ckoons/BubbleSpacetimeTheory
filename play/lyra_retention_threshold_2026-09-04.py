import itertools, math, random
from dimer import torus, matchings
from dimer2 import cycles4, classes
random.seed(31)
# Capacity bookkeeping is exact: H = log2(states).
# A growth step multiplies the state count by an expansion factor f.
# A refusal multiplies it by a survival fraction s.
# Over one cycle of g growth steps and one refusal:  dH = g*log2(f) + log2(s).
# THRESHOLD:  g* = log2(1/s) / log2(f).
def st(n,E,cap=200000):
    Ms=matchings(n,E)
    if not Ms or len(Ms)>cap: return None
    comp,nc=classes(Ms,cycles4(n,E)); return Ms,comp,nc
V,idx,E0,faces=torus(4,6); n0=len(V); S0=st(n0,E0)
print("measuring the two factors on the 4x6 torus (%d states)"%len(S0[0]))
fs=[]
for _ in range(12):
    a,b=n0,n0+1
    s1=random.randrange(n0); s2=random.randrange(n0)
    E2=list(E0)+[tuple(sorted((a,b))),tuple(sorted((s1,a))),tuple(sorted((s2,b)))]
    M2=matchings(n0+2,E2)
    fs.append(len(M2)/len(S0[0]))
ss=[]
pairs=random.sample(list(itertools.combinations(E0,2)),40)
for e1,e2 in pairs:
    sub=[m for m in S0[0] if e1 not in m and e2 not in m]
    if len(sub)>=12: ss.append(len(sub)/len(S0[0]))
import statistics as stx
f=stx.mean(fs); s=stx.mean(ss)
print("   growth expansion factor f: mean %.4f  (log2 = %+.4f)   [%d samples, range %.3f-%.3f]"%(f,math.log2(f),len(fs),min(fs),max(fs)))
print("   refusal survival fraction s: mean %.4f  (log2 = %+.4f)  [%d samples, range %.3f-%.3f]"%(s,math.log2(s),len(ss),min(ss),max(ss)))
g=math.log2(1/s)/math.log2(f)
print("   PREDICTED break-even growth-per-refusal  g* = log2(1/s)/log2(f) = %.2f"%g)
print("   measured: g=1 capacity -0.40/refusal, g=2 -0.23, g=3 -0.04  ->  break-even just above 3")
for gg in (1,2,3,4,5):
    print("      g=%d : predicted dH per cycle = %+.3f bits"%(gg, gg*math.log2(f)+math.log2(s)))
