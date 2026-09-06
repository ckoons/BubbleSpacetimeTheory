"""TEST 2 — does the two-certificate definition of replication have an instance?
Lyra for Casey, 2026-09-05.  Lane B, private.  Predictions hashed de589631 before this ran.

Parent P = 4x4 torus (9 classes under all-4-cycles).  Child = two copies of P plus k cross
bonds.  Certificates = flux of copy 1, flux of copy 2 -- disjoint supports by construction.
Question: is there a k where BOTH still separate the parent's classes AND the copies are
genuinely coupled (some child state uses a cross bond)?
"""
import sys, math, random, itertools
from collections import defaultdict
from lyra_retention_torus66_2026_09_05 import cycles4, flip_edges, components, R_bits

def torus_edges(L, M, off=0):
    idx = lambda i, j: off + (i % L) * M + (j % M)
    E = set()
    for i in range(L):
        for j in range(M):
            E.add(tuple(sorted((idx(i, j), idx(i, j + 1)))))
            E.add(tuple(sorted((idx(i, j), idx(i + 1, j)))))
    return sorted(E)

def matchings(n, E, ei, cap=None):
    adj = [[] for _ in range(n)]
    for u, v in E:
        adj[u].append((v, ei[(u, v)])); adj[v].append((u, ei[(u, v)]))
    out = []; cur = []; full = (1 << n) - 1
    class _S(Exception): pass
    def go(used):
        if used == full:
            out.append(frozenset(cur))
            if cap and len(out) > cap: raise _S
            return
        u = 0
        while used >> u & 1: u += 1
        for v, k in adj[u]:
            if not (used >> v & 1):
                cur.append(k); go(used | (1 << u) | (1 << v)); cur.pop()
    try: go(0)
    except _S: return None
    return out

def flux_of(M, E, L, Mm, off, n_half):
    """Winding of the sub-matching living inside the copy based at `off`. None if incomplete."""
    wx = wy = 0; seen = 0
    for k in M:
        u, v = E[k]
        if not (off <= u < off + n_half and off <= v < off + n_half): continue
        seen += 2
        i1, j1 = divmod(u - off, Mm); i2, j2 = divmod(v - off, Mm)
        if (i1 + j1) % 2 == 1: i1, j1, i2, j2 = i2, j2, i1, j1
        di = (i2 - i1) % L; dj = (j2 - j1) % Mm
        if dj in (1, Mm - 1): wx += 1 if dj == 1 else -1
        else:                 wy += 1 if di == 1 else -1
    return (wx, wy) if seen == n_half else None      # None <=> a cross bond invades this copy

def restrict(M, E, off, nh, pidx):
    """Restriction of a child matching to the copy based at `off`, as a frozenset of PARENT
    edge indices; None if a cross bond invades this copy (r is then undefined -- T1's hypothesis)."""
    out = []; seen = 0
    for k in M:
        u, v = E[k]
        iu = off <= u < off + nh; iv = off <= v < off + nh
        if iu and iv:
            out.append(pidx[tuple(sorted((u - off, v - off)))]); seen += 2
        elif iu or iv:
            seen += 1
    return frozenset(out) if seen == nh and len(out) * 2 == nh else None

def intra_cycles(n, E, ei, nh):
    """4-cycles that lie ENTIRELY inside one copy. The cold move set: every child move,
    seen through the restriction, IS a parent move -- so T1's hypothesis holds by construction."""
    return [q for q in cycles4(n, E, ei)
            if len({(E[e][0] < nh, E[e][1] < nh) for e in q}) == 1
            and all((E[e][0] < nh) == (E[e][1] < nh) for e in q)]

def run(L, Mm, k_list, seed=7, cap=400000, moves="all"):
    nh = L * Mm; n = 2 * nh
    rng = random.Random(seed)
    # parent, for reference
    Ep = torus_edges(L, Mm); eip = {e: i for i, e in enumerate(Ep)}
    Mp = matchings(nh, Ep, eip); mvp = cycles4(nh, Ep, eip)
    fep = flip_edges(Mp, mvp)
    compp, ncp, szp = components([True] * len(Mp), fep, len(Mp))
    Rp = R_bits(szp)
    print("PARENT %dx%d: %d matchings, %d classes, R=%.4f bits" % (L, Mm, len(Mp), ncp, Rp))
    print("PRODUCT TARGET: %d classes, R = 2R(P) = %.4f bits\n" % (ncp * ncp, 2 * Rp))
    cross_pool = [tuple(sorted((u, v))) for u in range(nh) for v in range(nh, n)]
    rng.shuffle(cross_pool)
    print("%3s %8s %7s %7s %9s %9s %12s %12s %8s  %s"
          % ("k", "states", "classes", "R", "R/2R(P)", "H_th", "cert1", "cert2", "coupled", "verdict"))
        # cert format: invariant? / #values / %% of child states where the restriction is defined
    for k in k_list:
        E = sorted(set(torus_edges(L, Mm) + torus_edges(L, Mm, off=nh) + cross_pool[:k]))
        ei = {e: i for i, e in enumerate(E)}
        Ms = matchings(n, E, ei, cap=cap)
        if Ms is None: print("%3d  state count exceeded cap %d" % (k, cap)); continue
        if not Ms: print("%3d  no perfect matchings" % k); continue
        mv = cycles4(n, E, ei) if moves == "all" else intra_cycles(n, E, ei, nh)
        fe = flip_edges(Ms, mv); N = len(Ms)
        comp, nc, sz = components([True] * N, fe, N)
        # certificates: is flux-of-copy-c constant on every child class, and does its
        # pullback separate?  Defined only on states with no cross bond into that copy.
        pcls = {m: compp[i] for i, m in enumerate(Mp)}
        certs = []
        for off in (0, nh):
            byclass = defaultdict(set); defined = 0
            for x, M in enumerate(Ms):
                r = restrict(M, E, off, nh, eip)
                if r is None: continue
                defined += 1; byclass[comp[x]].add(pcls[r])
            invariant = all(len(s) == 1 for s in byclass.values())
            vals = len({next(iter(s)) for s in byclass.values() if len(s) == 1})
            certs.append((invariant, vals, defined))
        n_cross = sum(1 for M in Ms if any(not (E[e][0] < nh) == (E[e][1] < nh) for e in M))
        coupled = n_cross > 0
        c1, c2 = certs
        # a certificate is USEFUL if it is class-invariant and takes >1 value
        ok1 = c1[0] and c1[1] > 1; ok2 = c2[0] and c2[1] > 1
        verdict = ("REPLICATES" if (ok1 and ok2 and coupled) else
                   "decoupled (no template)" if (ok1 and ok2) else "certificate LOST")
        print("%3d %8d %7d %7.4f %9.3f %9.4f %12s %12s %8s  %s"
              % (k, N, nc, R_bits(sz), R_bits(sz) / (2 * Rp), 
                 sum((s / N) * math.log2(s) for s in sz if s),
                 "%s/%d/%d%%" % ("Y" if c1[0] else "N", c1[1], 100*c1[2]//N),
                 "%s/%d/%d%%" % ("Y" if c2[0] else "N", c2[1], 100*c2[2]//N),
                 "%d" % n_cross, verdict))

if __name__ == "__main__":
    ks = [0, 6, 7, 8, 9, 10, 11, 12, 16]
    print("### CHILD MOVE SET = ALL 4-cycles (cross-bond cycles INCLUDED: T1 hypothesis broken)")
    run(4, 4, ks, moves="all")
    print("\n### CHILD MOVE SET = INTRA-COPY 4-cycles only (colder: T1 hypothesis HOLDS)")
    run(4, 4, ks, moves="intra")
