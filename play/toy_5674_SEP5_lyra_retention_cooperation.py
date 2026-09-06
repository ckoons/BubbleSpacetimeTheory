"""TEST 15 — does cooperation supply the rate hierarchy? Lyra for Casey, 2026-09-05. Preds ea01607b.
Two record systems A and B with independent intrinsic rates. Gating: one system's state suppresses
some of the other's moves. Score = bit-decades, the sum of R(T) over decades of observation horizon.
"""
import math, itertools, sys
from collections import deque

def R(sz):
    t=sum(sz); return -sum((s/t)*math.log2(s/t) for s in sz if s)

def analyse(nA,nB,rA,rB,eps,gateA,gateB,horizons):
    """gateA: set of A-junctions suppressed when B is in its 'closed' half (parity 0). gateB dual."""
    states=[(a,b) for a in itertools.product([0,1],repeat=nA)
                  for b in itertools.product([0,1],repeat=nB)]
    idx={s:i for i,s in enumerate(states)}
    B_closed=lambda b: sum(b)%2==0
    A_closed=lambda a: sum(a)%2==0
    moves=[]
    for j in range(nA):
        def f(s,j=j):
            a,b=s; a2=list(a); a2[j]^=1; return (tuple(a2),b)
        def rate(s,j=j):
            a,b=s
            return rA*eps if (j in gateA and B_closed(b)) else rA
        moves.append((f,rate))
    for k in range(nB):
        def g(s,k=k):
            a,b=s; b2=list(b); b2[k]^=1; return (a,tuple(b2))
        def rateb(s,k=k):
            a,b=s
            return rB*eps if (k in gateB and A_closed(a)) else rB
        moves.append((g,rateb))
    out=[]
    for T in horizons:
        comp=[-1]*len(states); nc=0
        for s0 in range(len(states)):
            if comp[s0]!=-1: continue
            dq=deque([s0]); comp[s0]=nc
            while dq:
                x=dq.popleft()
                for f,rt in moves:
                    if rt(states[x])>1.0/T:
                        t=idx.get(f(states[x]))
                        if t is not None and comp[t]==-1: comp[t]=nc; dq.append(t)
            nc+=1
        out.append(R([comp.count(k) for k in range(nc)]))
    return out

if __name__=="__main__":
    nA=nB=4; eps=1e-3
    H=[10.0**(k/2.0) for k in range(0,15)]   # half-decades, 10^0 .. 10^7
    allj=frozenset(range(nA)); none=frozenset()
    print("A: %d junctions at rate 1.  B: %d junctions at rate r_B.  eps=%g" % (nA,nB,eps))
    print("bit-decades = sum of R(T) over decades T = 10^1 .. 10^7\n")
    print("  %-14s %-26s %10s %10s %10s" % ("rate ratio","arrangement","BD","additive","gain"))
    for ratio in (1, 10, 1000):
        rB=1.0/ratio
        bdA=sum(analyse(nA,0,1.0,rB,eps,none,none,H)[1:]) if False else None
        # uncoupled reference: no gating at all
        unc=analyse(nA,nB,1.0,rB,eps,none,none,H); BDunc=sum(unc[1:])
        oneway=analyse(nA,nB,1.0,rB,eps,allj,none,H); BD1=sum(oneway[1:])
        mutual=analyse(nA,nB,1.0,rB,eps,allj,frozenset(range(nB)),H); BDm=sum(mutual[1:])
        for tag,bd in [("uncoupled (no gate)",BDunc),("one-way: slow B gates A",BD1),("mutual gating",BDm)]:
            d = "" if tag.startswith("uncoupled") else "%+.2f" % (bd-BDunc)
            print("  %-14s %-26s %10.2f %10.2f %10s" % ("r_A/r_B=%d"%ratio if tag.startswith("uncoupled") else "",tag,bd,BDunc,d))
        print("     R(T) uncoupled: %s"%["%.1f"%v for v in unc])
        print("     R(T) one-way  : %s"%["%.1f"%v for v in oneway])
        print("     R(T) mutual   : %s\n"%["%.1f"%v for v in mutual])
        sys.stdout.flush()
