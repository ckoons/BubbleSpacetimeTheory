"""TEST 3 — at FIXED substrate, how many bodies should the material be split into?
Lyra for Casey, 2026-09-05.  Lane B, private.  Predictions hashed 33d25c11 before this ran.
36 vertices throughout.  Cold move set (intra-unit 4-cycles only, so T1's hypothesis holds).
"""
import sys, math, random
from collections import defaultdict
from lyra_retention_torus66_2026_09_05 import cycles4, flip_edges, components, R_bits
from lyra_retention_twocert_2026_09_05 import torus_edges, matchings

def H_th(sz):
    t = sum(sz)
    return sum((s / t) * math.log2(s) for s in sz if s)

def unit_classes(L, M):
    E = torus_edges(L, M); ei = {e: i for i, e in enumerate(E)}
    Ms = matchings(L * M, E, ei); mv = cycles4(L * M, E, ei)
    comp, nc, sz = components([True] * len(Ms), flip_edges(Ms, mv), len(Ms))
    return {m: comp[i] for i, m in enumerate(Ms)}, ei, nc, R_bits(sz), len(Ms)

def restrict(M, E, off, nh, pidx):
    out = []; seen = 0
    for k in M:
        u, v = E[k]
        iu = off <= u < off + nh; iv = off <= v < off + nh
        if iu and iv: out.append(pidx[tuple(sorted((u - off, v - off)))]); seen += 2
        elif iu or iv: seen += 1
    return frozenset(out) if seen == nh and len(out) * 2 == nh else None

def intra_only(n, E, ei, bounds):
    """4-cycles lying entirely inside ONE unit."""
    def unit_of(v):
        for u, (a, b) in enumerate(bounds):
            if a <= v < b: return u
        return -1
    out = []
    for q in cycles4(n, E, ei):
        us = {unit_of(E[e][0]) for e in q} | {unit_of(E[e][1]) for e in q}
        if len(us) == 1: out.append(q)
    return out

def run(n_units, L, M, k_list, seed=7, cap=700000, topo="all", label=""):
    nh = L * M; n = n_units * nh
    pcls, pidx, pnc, pR, pN = unit_classes(L, M)
    bounds = [(i * nh, (i + 1) * nh) for i in range(n_units)]
    base = []
    for i in range(n_units): base += torus_edges(L, M, off=i * nh)
    pairs = [(a, b) for a in range(n_units) for b in range(a + 1, n_units)]
    if topo == "chain":  pairs = [(i, i + 1) for i in range(n_units - 1)]
    elif topo == "single": pairs = [(0, 1)]
    cross = [tuple(sorted((u, v))) for (a, b) in pairs
             for u in range(a * nh, (a + 1) * nh) for v in range(b * nh, (b + 1) * nh)]
    rng = random.Random(seed); rng.shuffle(cross)
    if topo in ("chain", "all") and len(pairs) > 1:
        # deal bonds ROUND-ROBIN across junctions so each gets an equal share
        buckets = {p: [] for p in pairs}
        for e in cross:
            for (a, b) in pairs:
                if a * nh <= e[0] < (a + 1) * nh and b * nh <= e[1] < (b + 1) * nh:
                    buckets[(a, b)].append(e); break
        inter = []
        for i in range(max(len(v) for v in buckets.values())):
            for p in pairs:
                if i < len(buckets[p]): inter.append(buckets[p][i])
        cross = inter
    print("\nn=%d x (%dx%d) = %d vertices  topo=%s %s | unit alone: %d states, %d classes, R=%.4f"
          % (n_units, L, M, n, topo, label, pN, pnc, pR))
    print("  %3s %8s %8s %8s %8s %9s %8s  %s" % ("k", "states", "classes", "R", "H_th", "H", "coupled", "certs"))
    for k in k_list:
        E = sorted(set(base + cross[:k])); ei = {e: i for i, e in enumerate(E)}
        Ms = matchings(n, E, ei, cap=cap)
        if Ms is None: print("  %3d  exceeded cap %d" % (k, cap)); continue
        if not Ms: print("  %3d  no perfect matchings" % k); continue
        fe = flip_edges(Ms, intra_only(n, E, ei, bounds)); N = len(Ms)
        comp, nc, sz = components([True] * N, fe, N)
        oks = []
        for i in range(n_units):
            byc = defaultdict(set)
            for x, Mm in enumerate(Ms):
                r = restrict(Mm, E, i * nh, nh, pidx)
                if r is not None: byc[comp[x]].add(pcls[r])
            inv = all(len(s) == 1 for s in byc.values())
            oks.append("Y" if inv else "N")
        ncoup = sum(1 for Mm in Ms
                    if any(not any(a <= E[e][0] < b and a <= E[e][1] < b for (a, b) in bounds) for e in Mm))
        print("  %3d %8d %8d %8.4f %8.4f %9.4f %8d  %s"
              % (k, N, nc, R_bits(sz), H_th(sz), math.log2(N), ncoup, "".join(oks)))

if __name__ == "__main__":
    import sys
    if sys.argv[1:] and sys.argv[1] == "depth":
        for t in ("single",):
            run(3, 3, 4, [16], topo=t, cap=2500000, label="(k=16 held fixed)")
    elif sys.argv[1:] and sys.argv[1] == "extend":
        run(2, 3, 6, [20, 24], cap=1600000)
        run(3, 3, 4, [20, 24], cap=1600000)
    else:
        ks = [0, 4, 8, 12, 16, 24, 32]
        run(1, 6, 6, [0]); run(2, 3, 6, ks); run(3, 3, 4, ks)
