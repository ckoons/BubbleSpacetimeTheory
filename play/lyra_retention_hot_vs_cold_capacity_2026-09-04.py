import itertools, math, random
from dimer import torus, matchings
from dimer2 import cycles4, flips_generic, classes
random.seed(41)
def ent(p):
    return -sum(x*math.log2(x) for x in p if x>1e-15)
def classent(p,comp,nc):
    m=[0.0]*nc
    for i,x in enumerate(p): m[comp[i]]+=x
    return ent(m)
def build(n,E):
    Ms=matchings(n,E)
    if not Ms: return None
    comp,nc=classes(Ms,cycles4(n,E))
    return Ms,comp,nc,cycles4(n,E)
def relax(Ms,cyc,p,steps):
    if steps==0: return p
    idx={m:i for i,m in enumerate(Ms)}; N=len(Ms)
    nb=[[idx[t] for t in flips_generic(m,cyc) if t in idx] for m in Ms]
    dmax=max(1,max(len(x) for x in nb))
    for _ in range(steps):
        w=[0.5*x for x in p]
        for i,x in enumerate(p):
            if x:
                w[i]+=0.5*x*(1-len(nb[i])/dmax)
                for j in nb[i]: w[j]+=0.5*x/dmax
        p=w
    return p
def grow(n,E,Ms,p):
    """COLD growth: add a matched pair; all mass goes to the determined extension."""
    for _ in range(15):
        a,b=n,n+1
        s1=random.randrange(n); s2=random.randrange(n)
        E2=list(E)+[tuple(sorted((a,b))),tuple(sorted((s1,a))),tuple(sorted((s2,b)))]
        B=build(n+2,E2)
        if B is None or len(B[0])<=len(Ms) or len(B[0])>30000: continue
        Ms2,comp2,nc2,cyc2=B
        idx2={m:i for i,m in enumerate(Ms2)}
        ab=tuple(sorted((a,b)))
        p2=[0.0]*len(Ms2); ok=True
        for i,m in enumerate(Ms):
            d=frozenset(set(m)|{ab})
            j=idx2.get(d)
            if j is None: ok=False; break
            p2[j]+=p[i]
        if ok: return E2,n+2,B,p2
    return None,n,(Ms,None,None,None),p
def refuse(n,E,B,p,samples=60):
    Ms,comp,nc,cyc=B
    best=None
    for e1,e2 in random.sample(list(itertools.combinations(E,2)),samples):
        keep=[i for i,m in enumerate(Ms) if e1 not in m and e2 not in m]
        if len(keep)<12: continue
        mass=sum(p[i] for i in keep)
        if mass<1e-9: continue
        E2=[x for x in E if x not in (e1,e2)]
        sub=[Ms[i] for i in keep]
        c2,nc2=classes(sub,cycles4(n,E2))
        q=[p[i]/mass for i in keep]
        R=classent(q,c2,nc2)
        if best is None or R>best[0]: best=(R,E2,(sub,c2,nc2,cycles4(n,E2)),q)
    return (None,None,None,None) if best is None else (best[1],best[2],best[3],best[0])
def run(tau,g=3,cycles=4):
    V,idx,E,faces=torus(4,6); n=len(V)
    B=build(n,E); Ms,comp,nc,cyc=B
    p=[1.0/len(Ms)]*len(Ms)
    print("  relaxation steps between writes tau=%-4s start: %d states, R=%.3f, H_law=%.3f"%(
        tau,len(Ms),classent(p,comp,nc),ent(p)))
    for c in range(cycles):
        for _ in range(g):
            E2,n2,B2,p2=grow(n,E,B[0],p)
            if E2 is None: break
            E,n,B,p=E2,n2,B2,p2
        p=relax(B[0],B[3],p,tau)
        E2,B2,p2,R=refuse(n,E,B,p)
        if E2 is None: print("     no admissible refusal"); break
        E,B,p=E2,B2,p2
        print("     cycle %d: %5d states  R_actual=%.3f  H_law=%.3f  (nominal H=%.3f)"%(
            c+1,len(B[0]),R,ent(p),math.log2(len(B[0]))))
    return
print("DOES COLD CAPACITY COUNT? vary the relaxation time between writes (dimer 4x6, g=3)")
for tau in (0,3,15,60):
    run(tau)
    print()
