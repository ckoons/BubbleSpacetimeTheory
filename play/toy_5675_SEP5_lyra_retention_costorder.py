"""TEST 9 — IS THE MELTING THRESHOLD CONVENTION-FREE?
Lyra for Casey, 2026-09-05.  The deepest gap: every result here is relative to a move set,
and I choose it.  If the move set is ordered by COST, is the melting point the same under
two genuinely different cost functions, or is even the threshold a convention?

cost A = cycle LENGTH (4,6,8...)          -- the obvious ordering
cost B = cycle geometric DIAMETER (L_inf) -- compact vs elongated cycles rank differently
"""
import math, itertools
from collections import deque, defaultdict
from lyra_retention_torus66_2026_09_05 import torus, matchings, components, R_bits

def cycles_upto(n, E, ei, L, Mm, maxlen):
    adj = defaultdict(list)
    for u, v in E: adj[u].append(v); adj[v].append(u)
    found = {}
    for start in range(n):
        stack = [(start, [start], {start})]
        while stack:
            cur, path, seen = stack.pop()
            if len(path) > maxlen: continue
            for nx in adj[cur]:
                if nx == start and len(path) >= 4 and len(path) % 2 == 0:
                    edges = frozenset(ei[tuple(sorted((path[i], path[(i+1) % len(path)])))]
                                      for i in range(len(path)))
                    if len(edges) == len(path): found[edges] = tuple(path)
                elif nx not in seen and len(path) < maxlen and nx > start:
                    stack.append((nx, path+[nx], seen | {nx}))
    out = []
    for edges, path in found.items():
        cyc = [ei[tuple(sorted((path[i], path[(i+1) % len(path)])))] for i in range(len(path))]
        A = cyc[0::2]; B = cyc[1::2]
        pts = [divmod(v, Mm) for v in path]
        dia = max(max(min(abs(a[0]-b[0]), L-abs(a[0]-b[0])),
                      min(abs(a[1]-b[1]), Mm-abs(a[1]-b[1]))) for a in pts for b in pts)
        out.append((len(path), dia, tuple(A), tuple(B)))
    return out

def classes_under(Ms, moves):
    pos = {m: i for i, m in enumerate(Ms)}; N = len(Ms)
    fe = []
    for i, M in enumerate(Ms):
        for (_, _, A, B) in moves:
            sA, sB = set(A), set(B)
            if sA <= M:   t = (M - sA) | sB
            elif sB <= M: t = (M - sB) | sA
            else: continue
            j = pos.get(t)
            if j is not None and i < j: fe.append((i, j))
    comp, nc, sz = components([True]*N, fe, N)
    return nc, R_bits(sz)

if __name__ == "__main__":
    L, Mm = 4, 6
    idx, E, ei, faces = torus(L, Mm); n = L*Mm
    Ms = matchings(n, E, ei)
    cyc = cycles_upto(n, E, ei, L, Mm, 8)
    print("=== TEST 9: is the melting threshold convention-free?  torus %dx%d, %d states ===" % (L, Mm, len(Ms)))
    print("alternating cycles found up to length 8: %d" % len(cyc))
    print("   length histogram:", dict(sorted(defaultdict(int, {l: sum(1 for c in cyc if c[0] == l) for l in {c[0] for c in cyc}}).items())))
    print("   diameter histogram:", dict(sorted(defaultdict(int, {d: sum(1 for c in cyc if c[1] == d) for d in {c[1] for c in cyc}}).items())))
    for name, key in [("A: by LENGTH", lambda c: c[0]), ("B: by DIAMETER", lambda c: c[1])]:
        print("\n  cost ordering %s" % name)
        vals = sorted({key(c) for c in cyc})
        for v in vals:
            mv = [c for c in cyc if key(c) <= v]
            nc, R = classes_under(Ms, mv)
            print("     cost<=%-2s  %4d moves  %3d classes  R=%7.4f %s"
                  % (v, len(mv), nc, R, "  <-- MELTED (R=0)" if R < 1e-9 else ""))
