"""TEST 16 — how many nodules does persistence take?  Lyra for Casey, 2026-09-05. Preds de492df9.
Total junctions fixed at 12 (state space 4096) split into n bodies. Gating: cycle or all-pairs.
Score (a) bit-decades, (b) persistence = largest horizon with R(T) > 0.
"""
import math, itertools, sys
from collections import deque

def analyse(parts, topo, eps=1e-3, rate=1.0, horizons=None):
    """parts = list of junction counts per body. Body i gated when its gaters are 'closed'
    (even parity). topo in {'cycle','allpairs','none'}."""
    n = len(parts); offs = []; o = 0
    for p in parts: offs.append((o, o+p)); o += p
    N = o
    states = list(itertools.product([0,1], repeat=N))
    idx = {s: i for i, s in enumerate(states)}
    if   topo == 'cycle':    gaters = {i: [(i+1) % n] for i in range(n)}
    elif topo == 'allpairs': gaters = {i: [j for j in range(n) if j != i] for i in range(n)}
    else:                    gaters = {i: [] for i in range(n)}
    def closed(s, j):
        a, b = offs[j]; return sum(s[a:b]) % 2 == 0
    def rate_of(s, body):
        return rate*eps if (gaters[body] and all(closed(s, g) for g in gaters[body])) else rate
    body_of = [next(i for i,(a,b) in enumerate(offs) if a <= k < b) for k in range(N)]
    out = []
    for T in horizons:
        comp = [-1]*len(states); nc = 0
        for s0 in range(len(states)):
            if comp[s0] != -1: continue
            dq = deque([s0]); comp[s0] = nc
            while dq:
                x = dq.popleft(); s = states[x]
                for k in range(N):
                    if rate_of(s, body_of[k]) > 1.0/T:
                        t = list(s); t[k] ^= 1
                        j = idx[tuple(t)]
                        if comp[j] == -1: comp[j] = nc; dq.append(j)
            nc += 1
        sz = [comp.count(k) for k in range(nc)]; tot = sum(sz)
        out.append(-sum((x/tot)*math.log2(x/tot) for x in sz if x))
    return out

if __name__ == "__main__":
    H = [10.0**(k/2.0) for k in range(0, 13)]
    splits = [("n=2 x 6", [6,6]), ("n=3 x 4", [4,4,4]), ("n=4 x 3", [3,3,3,3]), ("n=6 x 2", [2]*6)]
    print("Total junctions = 12, state space = 4096 in every arrangement (N1 control).")
    print("Scores: (a) bit-decades = sum R(T) over half-decades T=10^0.5..10^6; (b) persistence =")
    print("largest T with R(T) > 1e-9.\n")
    print("  %-10s %-10s %12s %14s   %s" % ("split","topology","bit-decades","persistence","R(T)"))
    for tag, parts in splits:
        for topo in ("none", "cycle", "allpairs"):
            vals = analyse(parts, topo, horizons=H)
            bd = sum(vals[1:])
            pers = max([T for T, v in zip(H, vals) if v > 1e-9], default=0.0)
            print("  %-10s %-10s %12.2f %14.3g   %s"
                  % (tag, topo, bd, pers, " ".join("%.1f" % v for v in vals)))
            sys.stdout.flush()
        print()
