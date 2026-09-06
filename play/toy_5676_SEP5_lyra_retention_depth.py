"""TEST 7/8 — is R the same thing as DEPTH (assembly index)?  And what does flux miss on 6x6?
Lyra for Casey, 2026-09-05.  Predictions hashed before launch.
"""
import math, sys
from collections import deque, defaultdict
from lyra_retention_torus66_2026_09_05 import (torus, cycles4, matchings, flip_edges,
                                               components, R_bits, flux)

def adj_of(N, fe):
    a = [[] for _ in range(N)]
    for i, j in fe: a[i].append(j); a[j].append(i)
    return a

def bfs_far(a, src, member):
    dist = {src: 0}; dq = deque([src]); far, fd = src, 0
    while dq:
        x = dq.popleft()
        for y in a[x]:
            if y not in dist and member[y]:
                dist[y] = dist[x]+1; dq.append(y)
                if dist[y] > fd: far, fd = y, dist[y]
    return far, fd

def depth_of_classes(N, fe, comp, nc):
    """Two-sweep BFS per class: a LOWER BOUND on the class diameter."""
    a = adj_of(N, fe)
    members = defaultdict(list)
    for x in range(N):
        if comp[x] >= 0: members[comp[x]].append(x)
    out = {}
    for c, ms in members.items():
        if len(ms) == 1: out[c] = 0; continue
        mem = [False]*N
        for x in ms: mem[x] = True
        u, _ = bfs_far(a, ms[0], mem); _, d = bfs_far(a, u, mem)
        out[c] = d
    return out, members

def profile(L, Mm, moves, label):
    idx, E, ei, faces = torus(L, Mm); n = L*Mm
    mv = faces if moves == "faces" else cycles4(n, E, ei)
    Ms = matchings(n, E, ei); N = len(Ms); fe = flip_edges(Ms, mv)
    comp, nc, sz = components([True]*N, fe, N)
    dep, members = depth_of_classes(N, fe, comp, nc)
    mean_d = sum(len(members[c])*dep[c] for c in dep)/N
    print("%-28s %6d states %4d classes  R=%7.4f  mean depth=%7.2f  max depth=%4d"
          % (label, N, nc, R_bits(sz), mean_d, max(dep.values())))
    return R_bits(sz), mean_d, (Ms, E, comp, nc, sz, dep, members, L, Mm)

if __name__ == "__main__":
    print("=== TEST 7: R vs DEPTH (depth = 2-sweep BFS lower bound on class diameter) ===")
    rows = []
    for (L, Mm) in [(4,4), (4,6), (6,6)]:
        for mvs in ("cycles4", "faces"):
            r, d, extra = profile(L, Mm, mvs, "torus %dx%d  %s" % (L, Mm, mvs))
            rows.append((("%dx%d/%s" % (L, Mm, mvs)), r, d))
            if (L, Mm, mvs) == (6, 6, "faces"): six = extra
    print("\n  --- looking for equal R with different depth (D1) ---")
    for i in range(len(rows)):
        for j in range(i+1, len(rows)):
            if abs(rows[i][1]-rows[j][1]) < 0.05:
                lo, hi = sorted([rows[i][2], rows[j][2]])
                print("  %s R=%.4f depth=%.2f  vs  %s R=%.4f depth=%.2f   ratio %.2fx"
                      % (rows[i][0], rows[i][1], rows[i][2], rows[j][0], rows[j][1], rows[j][2],
                         hi/lo if lo > 0 else float('inf')))
    print("\n=== TEST 8: what does flux MISS on the 6x6 torus? ===")
    Ms, E, comp, nc, sz, dep, members, L, Mm = six
    byflux = defaultdict(list)
    for c, ms in members.items():
        byflux[flux(Ms[ms[0]], E, L, Mm)].append(c)
    shared = {f: cs for f, cs in byflux.items() if len(cs) > 1}
    extra_mass = sum(len(members[c]) for f, cs in shared.items() for c in cs[1:])
    print("  %d classes over %d distinct flux values" % (nc, len(byflux)))
    print("  flux values carrying MORE THAN ONE class: %d" % len(shared))
    for f, cs in sorted(shared.items())[:8]:
        print("    flux %-9s -> %d classes, sizes %s, depths %s"
              % (str(f), len(cs), [len(members[c]) for c in cs], [dep[c] for c in cs]))
    print("  mass in the 'extra' classes beyond one per flux value: %d of %d = %.4f%%"
          % (extra_mass, len(Ms), 100.0*extra_mass/len(Ms)))
