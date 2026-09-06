"""TEST 14 — the self-refusing record system. Lyra for Casey, 2026-09-05. Preds 56ec6c22.
State = (D, C): D in F_2^n is the linkage phase; C is the set of junctions covered by an inversion.
Crossover at j has rate r_j, suppressed by eps if j in C. The inversion flips at rate rho.
R(T) uses only moves with rate > 1/T.  R(T) is the record visible to an observer watching for T.
"""
import math, itertools, sys
from collections import deque

def components(states, moves):
    idx={s:i for i,s in enumerate(states)}; comp=[-1]*len(states); nc=0
    for s0 in range(len(states)):
        if comp[s0]!=-1: continue
        dq=deque([s0]); comp[s0]=nc
        while dq:
            x=dq.popleft()
            for mv in moves:
                t=idx.get(mv(states[x]))
                if t is not None and comp[t]==-1: comp[t]=nc; dq.append(t)
        nc+=1
    return [comp.count(k) for k in range(nc)]
R=lambda sz: -sum((s/sum(sz))*math.log2(s/sum(sz)) for s in sz if s)

def build(n, cold, eps, rho, r=1.0):
    """States (D, inv) with inv in {0,1}: is the inversion present?  Rates per move."""
    states=[(D,inv) for D in itertools.product([0,1],repeat=n) for inv in (0,1)]
    moves=[]
    for j in range(n):
        rate_hot  = r
        rate_cold = r*eps
        def mk(j=j):
            def f(s):
                D,inv=s; D2=list(D); D2[j]^=1; return (tuple(D2),inv)
            return f
        # when the inversion is PRESENT (inv=1) and j is cold, the rate is suppressed
        moves.append((mk(), rate_hot,  lambda s,j=j: not (s[1]==1 and j in cold)))
        moves.append((mk(), rate_cold, lambda s,j=j:      (s[1]==1 and j in cold)))
    def flip(s):
        D,inv=s; return (D,1-inv)
    moves.append((flip, rho, lambda s: True))
    return states, moves

def R_at(T, states, moves):
    active=[]
    for f,rate,cond in moves:
        if rate > 1.0/T:
            active.append(lambda s,f=f,cond=cond: f(s) if cond(s) else s)
    if not active: return R([1]*len(states)), 0
    return R(components(states, active)), len(active)

if __name__=="__main__":
    n=6; cold=frozenset([1,2,3])           # a 3-junction inversion
    horizons=[1.0,2,5,10,30,100,300,1000,3000,1e4,1e5,1e6,1e7]
    print("n=%d junctions, crossover rate r=1, inversion covers junctions %s"%(n,sorted(cold)))
    print("W1 control: for the NO-INVERSION case R(T) must equal n - #{active crossovers}, exactly.\n")
    for tag,eps,rho in [("NO inversion (eps=1)",1.0,0.0),
                        ("inversion eps=1e-3, rho=1e-5  (rho < r*eps: PAYS)",1e-3,1e-5),
                        ("inversion eps=1e-3, rho=1e-2  (rho > r*eps: too fast)",1e-3,1e-2),
                        ("inversion eps=1e-3, rho=1.0   (FREE self-modification)",1e-3,1.0)]:
        states,moves=build(n,cold if eps<1 else frozenset(),eps,rho)
        print("  %s"%tag)
        row=[]
        for T in horizons:
            r_,na=R_at(T,states,moves)
            row.append((T,r_,na))
        print("     %s"%("  ".join("T=%-7g R=%.2f"%(T,r_) for T,r_,_ in row)))
        # W1 exactness check for the plain case
        if eps==1.0:
            ok=all(abs(r_-(n-sum(1 for j in range(n) if 1.0>1.0/T)))<1e-9 for T,r_,_ in row)
            print("     W1 (no-inversion exactness): %s"%("HIT" if ok else "MISS"))
        sys.stdout.flush()
