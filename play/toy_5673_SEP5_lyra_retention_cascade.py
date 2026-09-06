"""Retention under construction — the CASCADE: does creation stay positive across many steps?
Lyra for Casey, 2026-09-05.  Lane B, private.  Predictions hashed 325f3e35 before any run.

ARM A  pure selection, no growth: repeated two-bond refusals on a FIXED torus.
       T7 says this must freeze.  It is the control that should die.
ARM B  alternation: g growth steps (add a matched pair on new vertices) then one refusal.
       If T7's complement holds, this keeps climbing where Arm A has stopped.

Growth here is Friday's dimer accretion: attach a new pair of vertices, matched to each
other, with attachment bonds into the host.  The 6x6 torus is the HEADROOM -- Friday's
9,000-state cap is what made the asymptotic question unaskable.
"""
import sys, math, random, itertools, time
from collections import defaultdict
from lyra_retention_torus66_2026_09_05 import (torus, cycles4, flip_edges,
                                               components, R_bits)

def matchings(n, E, ei, cap=None):
    """Perfect matchings as frozensets of edge indices. `cap` aborts a blow-up early."""
    adj = [[] for _ in range(n)]
    for u, v in E:
        adj[u].append((v, ei[(u, v)])); adj[v].append((u, ei[(u, v)]))
    out = []; cur = []; full = (1 << n) - 1
    class _Stop(Exception): pass
    def go(used):
        if used == full:
            out.append(frozenset(cur))
            if cap and len(out) > cap: raise _Stop
            return
        u = 0
        while used >> u & 1: u += 1
        for v, k in adj[u]:
            if not (used >> v & 1):
                cur.append(k); go(used | (1 << u) | (1 << v)); cur.pop()
    try: go(0)
    except _Stop: return None
    return out

def entropy_thermo(sizes):
    """H_thermo = mean over classes of log2(class size), weighted by class mass.
    H = R + H_thermo with H = log2(total states) when states are equiprobable."""
    tot = sum(sizes)
    if tot == 0: return 0.0
    return sum((s / tot) * math.log2(s) for s in sizes if s)

def report(step, label, sizes, N_alive, N0, prev):
    R = R_bits(sizes); Ht = entropy_thermo(sizes); H = math.log2(N_alive) if N_alive else 0.0
    dR = None if prev is None else R - prev[0]
    dHt = None if prev is None else Ht - prev[1]
    eff = (dR / -dHt) if (dR is not None and dHt is not None and dHt < -1e-12) else None
    print("  %-5s step %2d: %6d states  %4d classes   R=%7.4f  H_th=%7.4f  H=%7.4f%s%s"
          % (label, step, N_alive, len(sizes), R, Ht, H,
             "   dR=%+7.4f dH_th=%+7.4f" % (dR, dHt) if dR is not None else "",
             "   eff=%+6.3f" % eff if eff is not None else ""))
    return (R, Ht, len(sizes), N_alive)

# ---------------------------------------------------------------- ARM A
def arm_A(L, Mm, moves, steps, seed, greedy=True):
    idx, E, ei, faces = torus(L, Mm); n = L * Mm
    mv = faces if moves == "faces" else cycles4(n, E, ei)
    Ms = matchings(n, E, ei); N = len(Ms)
    fe = flip_edges(Ms, mv)
    holds = [[i for i, m in enumerate(Ms) if k in m] for k in range(len(E))]
    alive = [True] * N
    comp, nc, sizes = components(alive, fe, N)
    print("\nARM A  (pure selection, no growth)  torus %dx%d moves=%s  %d states %d classes"
          % (L, Mm, moves, N, nc))
    prev = report(0, "A", sizes, sum(alive), N, None)
    rng = random.Random(seed)
    banned = set(); traj = [prev]
    for step in range(1, steps + 1):
        cands = [p for p in itertools.combinations(range(len(E)), 2)
                 if p[0] not in banned and p[1] not in banned]
        if not cands: print("  A: no candidate refusals left"); break
        rng.shuffle(cands)
        best = None
        for a, b in cands[:120 if greedy else 1]:
            al = list(alive)
            for i in holds[a]: al[i] = False
            for i in holds[b]: al[i] = False
            if sum(al) < 2: continue
            c2, nc2, sz2 = components(al, fe, N)
            fwd = defaultdict(set)
            for x in range(N):
                if al[x]: fwd[comp[x]].add(c2[x])
            splits = sum(len(v) - 1 for v in fwd.values())
            dR = R_bits(sz2) - prev[0]
            key = (splits > 0, dR)
            if best is None or key > best[0]: best = (key, a, b, al, c2, nc2, sz2, splits)
        if best is None: print("  A: exhausted"); break
        _, a, b, alive, comp, nc, sizes, splits = best
        banned.add(a); banned.add(b)
        prev = report(step, "A", sizes, sum(alive), N, prev)
        traj.append(prev)
        if sum(alive) < 8: print("  A: population collapsed"); break
    return traj

# ---------------------------------------------------------------- growth
def grow(n, E, ei, host_vertices, rng, attach=2):
    """Add two NEW vertices u,v matched to each other, each bonded to `attach` host vertices."""
    u, v = n, n + 1
    newE = list(E) + [(u, v)]
    for w in rng.sample(host_vertices, min(attach, len(host_vertices))):
        newE.append(tuple(sorted((w, u))))
    for w in rng.sample(host_vertices, min(attach, len(host_vertices))):
        newE.append(tuple(sorted((w, v))))
    newE = sorted(set(newE))
    return n + 2, newE, {e: k for k, e in enumerate(newE)}

# ---------------------------------------------------------------- ARM B
def arm_B(L, Mm, moves, steps, g, seed, cap=200000, attach=2):
    rng = random.Random(seed)
    idx, E, ei, faces = torus(L, Mm); n = L * Mm
    E = list(E)
    print("\nARM B  (alternation: %d growth steps then 1 refusal)  seed torus %dx%d moves=%s"
          % (g, L, Mm, moves))
    banned = set(); prev = None; traj = []; forbidden_edges = set()
    for step in range(0, steps + 1):
        if step > 0:
            for _ in range(g):
                n, E, ei = grow(n, E, ei, list(range(n)), rng, attach)
        Ecur = [e for e in E if e not in forbidden_edges]
        eicur = {e: k for k, e in enumerate(Ecur)}
        Ms = matchings(n, Ecur, eicur, cap=cap)
        if Ms is None: print("  B: state count exceeded cap %d at n=%d, stopping" % (cap, n)); break
        if not Ms: print("  B: no perfect matchings survive at n=%d" % n); break
        mv = cycles4(n, Ecur, eicur)
        fe = flip_edges(Ms, mv); N = len(Ms)
        alive = [True] * N
        comp, nc, sizes = components(alive, fe, N)
        if step == 0:
            prev = report(0, "B", sizes, N, N, None); traj.append(prev); continue
        # one refusal: pick the two-bond prohibition that creates most
        holds = [[i for i, m in enumerate(Ms) if k in m] for k in range(len(Ecur))]
        cands = list(itertools.combinations(range(len(Ecur)), 2)); rng.shuffle(cands)
        best = None
        for a, b in cands[:120]:
            al = [True] * N
            for i in holds[a]: al[i] = False
            for i in holds[b]: al[i] = False
            if sum(al) < 2: continue
            c2, nc2, sz2 = components(al, fe, N)
            fwd = defaultdict(set)
            for x in range(N):
                if al[x]: fwd[comp[x]].add(c2[x])
            splits = sum(len(v) - 1 for v in fwd.values())
            key = (splits > 0, R_bits(sz2))
            if best is None or key > best[0]: best = (key, Ecur[a], Ecur[b], al, sz2, splits)
        if best is None: print("  B: no refusal available"); break
        _, ea, eb, al, sizes, splits = best
        forbidden_edges.add(ea); forbidden_edges.add(eb)
        prev = report(step, "B", sizes, sum(al), N, prev); traj.append(prev)
    return traj

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "A"
    if which == "A":
        arm_A(4, 6, "cycles4", steps=14, seed=11)
        arm_A(4, 6, "faces",   steps=14, seed=11)
    elif which == "B":
        for g in (1, 2, 3):
            arm_B(4, 4, "cycles4", steps=10, g=g, seed=11)
