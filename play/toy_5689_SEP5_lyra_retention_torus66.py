"""Retention under construction — the 6x6 torus.
Lyra for Casey, 2026-09-05.  Lane B, private.  Predictions hashed 325f3e35 before this ran.

Stage 1: instrument controls (4x4, 4x6) + 6x6 enumeration, classes, R, flux.
Stage 2: two-bond prohibition sweep on 6x6, SPLITS separated from EMPTIES.
"""
import sys, math, random, itertools, time
from collections import defaultdict

def torus(L, M):
    idx = {(i, j): i * M + j for i in range(L) for j in range(M)}
    E = set()
    for i in range(L):
        for j in range(M):
            E.add(tuple(sorted((idx[(i, j)], idx[(i, (j + 1) % M)]))))
            E.add(tuple(sorted((idx[(i, j)], idx[((i + 1) % L, j)]))))
    E = sorted(E)
    ei = {e: k for k, e in enumerate(E)}
    faces = []
    for i in range(L):
        for j in range(M):
            a = idx[(i, j)]; b = idx[(i, (j + 1) % M)]
            c = idx[((i + 1) % L, (j + 1) % M)]; d = idx[((i + 1) % L, j)]
            q = [(a, b), (c, d), (b, c), (d, a)]
            faces.append(tuple(ei[tuple(sorted(x))] for x in q))   # (e1,e2,f1,f2)
    return idx, E, ei, faces


def cycles4(n, E, ei):
    """ALL 4-cycles, not just faces. Friday's dimer move set ("flip-length 4")."""
    from collections import defaultdict as _dd
    adj = _dd(set)
    for u, v in E: adj[u].add(v); adj[v].add(u)
    seen = set(); out = []
    for a in range(n):
        for c in range(a + 1, n):
            common = sorted(adj[a] & adj[c])
            for b, d in itertools.combinations(common, 2):
                e1 = ei[tuple(sorted((a, b)))]; e2 = ei[tuple(sorted((c, d)))]
                f1 = ei[tuple(sorted((b, c)))]; f2 = ei[tuple(sorted((d, a)))]
                key = frozenset((e1, e2, f1, f2))
                if len(key) < 4 or key in seen: continue
                seen.add(key); out.append((e1, e2, f1, f2))
    return out

def matchings(n, E, ei):
    adj = [[] for _ in range(n)]
    for u, v in E:
        adj[u].append((v, ei[(u, v)])); adj[v].append((u, ei[(u, v)]))
    out = []; cur = []
    full = (1 << n) - 1
    def go(used):
        if used == full:
            out.append(frozenset(cur)); return
        u = 0
        while used >> u & 1: u += 1
        for v, k in adj[u]:
            if not (used >> v & 1):
                cur.append(k); go(used | (1 << u) | (1 << v)); cur.pop()
    go(0)
    return out

def flip_edges(Ms, faces):
    """Undirected edges of the move graph, as index pairs. Flips are involutions."""
    pos = {m: i for i, m in enumerate(Ms)}
    out = []
    for i, M in enumerate(Ms):
        for (e1, e2, f1, f2) in faces:
            if e1 in M and e2 in M:
                t = (M - {e1, e2}) | {f1, f2}
            elif f1 in M and f2 in M:
                t = (M - {f1, f2}) | {e1, e2}
            else:
                continue
            j = pos[t]
            if i < j: out.append((i, j))
    return out

def components(alive, fedges, N):
    """Union-find over the alive subset. Returns (label per state or -1, n_classes, sizes)."""
    p = list(range(N))
    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]; x = p[x]
        return x
    for i, j in fedges:
        if alive[i] and alive[j]:
            ri, rj = find(i), find(j)
            if ri != rj: p[ri] = rj
    lab = {}; comp = [-1] * N; sizes = []
    for x in range(N):
        if not alive[x]: continue
        r = find(x)
        if r not in lab:
            lab[r] = len(sizes); sizes.append(0)
        comp[x] = lab[r]; sizes[lab[r]] += 1
    return comp, len(sizes), sizes

def R_bits(sizes):
    """Shannon entropy of the class distribution. NOT log2(count) — Friday's correction 6."""
    tot = sum(sizes)
    if tot == 0: return 0.0
    return -sum((s / tot) * math.log2(s / tot) for s in sizes if s)

def flux(M, E, L, Mm):
    wx = wy = 0
    for k in M:
        u, v = E[k]
        i1, j1 = divmod(u, Mm); i2, j2 = divmod(v, Mm)
        if (i1 + j1) % 2 == 1:
            i1, j1, i2, j2 = i2, j2, i1, j1          # black endpoint first
        di = (i2 - i1) % L; dj = (j2 - j1) % Mm
        if dj in (1, Mm - 1): wx += 1 if dj == 1 else -1
        else:                 wy += 1 if di == 1 else -1
    return (wx, wy)

def build(L, Mm, verbose=True, moves="cycles4"):
    t0 = time.time()
    idx, E, ei, faces = torus(L, Mm)
    n = L * Mm
    Ms = matchings(n, E, ei)
    mv = faces if moves == "faces" else cycles4(n, E, ei)
    fe = flip_edges(Ms, mv)
    alive = [True] * len(Ms)
    comp, nc, sizes = components(alive, fe, len(Ms))
    if verbose:
        fx = defaultdict(set)
        for k, m in enumerate(Ms): fx[comp[k]].add(flux(m, E, L, Mm))
        sep = all(len(s) == 1 for s in fx.values()) and len({next(iter(s)) for s in fx.values()}) == nc
        print("torus %dx%d  moves=%s (%d): %6d matchings  %6d move-graph edges  %3d classes  R=%.4f bits  [%.1fs]"
              % (L, Mm, moves, len(mv), len(Ms), len(fe), nc, R_bits(sizes), time.time() - t0))
        print("     class sizes (top 10): %s" % sorted(sizes, reverse=True)[:10])
        print("     flux (wx,wy) separates classes EXACTLY: %s   distinct flux values: %d"
              % (sep, len({next(iter(s)) for s in fx.values()})))
    return Ms, E, ei, mv, fe, comp, nc, sizes

def sweep_two_bond(Ms, E, fe, comp, nc, sizes, n_sample, seed, tag):
    """Two-bond prohibitions. Separate genuine SPLITS from mere EMPTIES."""
    N = len(Ms)
    holds = [[i for i, m in enumerate(Ms) if k in m] for k in range(len(E))]
    pairs = list(itertools.combinations(range(len(E)), 2))
    rng = random.Random(seed)
    exhaustive = n_sample is None or n_sample >= len(pairs)
    if not exhaustive: pairs = rng.sample(pairs, n_sample)
    R0 = R_bits(sizes)
    rose = split_any = tested = 0
    tot_splits = 0; best = None; dist = defaultdict(int)
    for a, b in pairs:
        alive = [True] * N
        for i in holds[a]: alive[i] = False
        for i in holds[b]: alive[i] = False
        if sum(alive) < 2: continue
        c2, nc2, sz2 = components(alive, fe, N)
        tested += 1; dist[nc2] += 1
        fwd = defaultdict(set)
        for x in range(N):
            if alive[x]: fwd[comp[x]].add(c2[x])
        splits = sum(len(v) - 1 for v in fwd.values())
        emptied = nc - len(fwd)
        if nc2 > nc: rose += 1
        if splits > 0:
            split_any += 1; tot_splits += splits
            dR = R_bits(sz2) - R0
            if best is None or dR > best[0]:
                best = (dR, E[a], E[b], nc, nc2, splits, emptied, sum(alive), N)
    print("\n%s: parent %d classes, R=%.4f bits; %d two-bond prohibitions tested (%s)"
          % (tag, nc, R0, tested, "EXHAUSTIVE" if exhaustive else "sampled"))
    print("   class count ROSE in %d of %d (%.1f%%)" % (rose, tested, 100.0 * rose / max(tested, 1)))
    print("   >=1 GENUINE SPLIT in %d of %d (%.1f%%);  total splits %d"
          % (split_any, tested, 100.0 * split_any / max(tested, 1), tot_splits))
    print("   child class-count distribution: %s" % dict(sorted(dist.items())))
    if best:
        print("   best: forbid %s,%s -> %d classes (from %d), %d splits, %d emptied, %d of %d states survive, CREATES %+.4f bits"
              % (best[1], best[2], best[4], best[3], best[5], best[6], best[7], best[8], best[0]))
    return split_any, tested

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "control"):
        print("=" * 78); print("STAGE 1a — INSTRUMENT CONTROLS (must reproduce Friday)"); print("=" * 78)
        for mv in ("faces", "cycles4"):
            d = build(4, 4, moves=mv)
            sweep_two_bond(d[0], d[1], d[4], d[5], d[6], d[7], None, 4, "4x4 moves=%s (Friday claim: 0 rises / 496 exhaustive)" % mv)
            d = build(4, 6, moves=mv)
            sweep_two_bond(d[0], d[1], d[4], d[5], d[6], d[7], 300, 4, "4x6 moves=%s (Friday claim: 251 rises / 300 sampled)" % mv)
    if which in ("all", "six"):
        print("\n" + "=" * 78); print("STAGE 1b — 6x6 TORUS"); print("=" * 78)
        for mv in ("faces", "cycles4"):
            d = build(6, 6, moves=mv)
            print("\n" + "=" * 78); print("STAGE 2 — 6x6 TWO-BOND SWEEP, moves=%s" % mv); print("=" * 78)
            sweep_two_bond(d[0], d[1], d[4], d[5], d[6], d[7], 300, 4, "6x6 moves=%s" % mv)
