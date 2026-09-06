"""TEST 5 — is the 0.50-0.65 exchange rate a property of the SPACE or of my SEARCH POLICY?
Lyra for Casey, 2026-09-05.  Predictions hashed before launch.
"""
import sys, math, random, itertools
from collections import defaultdict
from lyra_retention_torus66_2026_09_05 import (torus, cycles4, matchings, flip_edges,
                                               components, R_bits)
def Hth(sz):
    t=sum(sz); return sum((s/t)*math.log2(s) for s in sz if s)

def arm(L,Mm,moves,policy,steps=10,seed=11,sample=120):
    idx,E,ei,faces=torus(L,Mm); n=L*Mm
    mv=faces if moves=="faces" else cycles4(n,E,ei)
    Ms=matchings(n,E,ei); N=len(Ms); fe=flip_edges(Ms,mv)
    holds=[[i for i,m in enumerate(Ms) if k in m] for k in range(len(E))]
    alive=[True]*N; comp,nc,sz=components(alive,fe,N)
    R,Ht=R_bits(sz),Hth(sz); rng=random.Random(seed); banned=set(); effs=[]; peak=(R,0); frozen=None
    for step in range(1,steps+1):
        cands=[p for p in itertools.combinations(range(len(E)),2)
               if p[0] not in banned and p[1] not in banned]
        if not cands: break
        rng.shuffle(cands)
        pool = cands if policy=="exhaust" else cands[:sample]
        best=None
        for a,b in pool:
            al=list(alive)
            for i in holds[a]: al[i]=False
            for i in holds[b]: al[i]=False
            ns=sum(al)
            if ns<2: continue
            c2,nc2,sz2=components(al,fe,N)
            dR=R_bits(sz2)-R
            if   policy in ("greedy","exhaust"): key=(dR,)
            elif policy=="worst":                key=(-dR,)
            elif policy=="anti":                 key=(-ns,)
            else:                                key=(0,)      # random: first admissible
            if best is None or key>best[0]: best=(key,a,b,al,sz2)
            if policy=="random": break
        if best is None: break
        _,a,b,alive,sz=best; banned.add(a); banned.add(b)
        nR,nHt=R_bits(sz),Hth(sz); dR,dHt=nR-R,nHt-Ht
        comp,_,_=components(alive,fe,N)
        if dHt<-1e-12 and dR>0: effs.append(dR/-dHt)
        if nR>peak[0]: peak=(nR,step)
        if frozen is None and nHt<1e-9: frozen=step
        R,Ht=nR,nHt
        if sum(alive)<8: break
    band=("%.3f-%.3f"%(min(effs),max(effs))) if effs else "n/a"
    med=sorted(effs)[len(effs)//2] if effs else float('nan')
    print("  %-8s %-8s  eff band %-13s median %6.3f  n=%d   R peak %.3f @step %s   H_th->0 @step %s"
          %(moves,policy,band,med,len(effs),peak[0],peak[1],frozen))

if __name__=="__main__":
    print("4x6 torus, pure selection, refusal policy varied (greedy = what both instances used)")
    for moves in ("cycles4","faces"):
        for pol in ("greedy","exhaust","random","worst","anti"):
            arm(4,Mm=6,moves=moves,policy=pol)
