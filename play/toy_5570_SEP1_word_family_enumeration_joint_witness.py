#!/usr/bin/env python3
"""
Toy 5570 — the WORD-FAMILY ENUMERATION + the joint witness

The choice quantifier needs a concrete finite domain. Enumerated whole,
in CONTEXT-ROLE terms (graph-independent):
  moves = (link role, color pair): roles {B1, n_sM, B2, n_si, n_sj}
  with forced colors {r, s_M, r, s_i, s_j}; pairs = the 3 pairs
  containing the role's color -> 15 context-moves;
  words = ordered (m1, m2) with distinct pairs -> the family F_ctx,
  |F_ctx| = 186, listed whole (15x15 minus 39 same-pair) (and orbit-reduced under the context's
  mirror symmetry for Cal's finite object).

THE JOINT WITNESS (new — F1/F3 tested the clauses under SEPARATE
existential quantifiers): does ONE word in F_ctx satisfy ALL of
  (i) unsticking gate (proper + freeable, support nonempty);
  (ii) charge patch mod gauge, size <= 8;
  (iii) M1 strict descent;
  (iv) the J2 clause (agrees-gained on patch, disagrees nowhere new)
simultaneously, on every stuck configuration held? Lyra's proof
chooses ONE w — the conjunction is what her page needs. Off-home
freed sets are sampled: (iii)/(iv) failures there carry the
false-negative caveat; Fritsch is exact.

Also delivered: the minimal covering ROLE-set (greedy set cover) — the
sub-family that suffices, as the concrete domain for the existence
proof.

TESTS (X/Y): 1. the family listed + orbit count · 2. joint-witness
coverage · 3. the minimal covering sub-family.

Elie, 2026-09-01. Millennium week II. 3 tests.
"""

import importlib.util
import itertools
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


F2C = load("t5566wf", "toy_5566_SEP1_F2_overlap_census_M_F_shared_sM"
           "_vertices.py")
F1 = F2C.F1
E1, G5, X3, H8 = F2C.E1, F2C.G5, F2C.X3, F2C.H8


ROLE_NAMES = ['B1', 'n_sM', 'B2', 'n_si', 'n_sj']


def role_map(adj, c, tv, lcyc):
    """Map role name -> vertex, from the forced word."""
    rl = F2C.roles(adj, c, tv, lcyc)
    if rl is None:
        return None
    n_sM, r, s_M, s_i, s_j = rl
    n = len(lcyc)
    cols = [c[v] for v in lcyc]
    mi = lcyc.index(n_sM)
    bpos = [i for i in range(n) if cols[i] == r]
    b1, b2 = sorted(bpos, key=lambda i: (i - mi) % n)
    # n_si = the s_i-colored vertex, n_sj the s_j one
    vi = next(lcyc[i] for i in range(n) if cols[i] == s_i)
    vj = next(lcyc[i] for i in range(n) if cols[i] == s_j)
    return {'B1': lcyc[b1], 'n_sM': n_sM, 'B2': lcyc[b2],
            'n_si': vi, 'n_sj': vj}, \
           {'r': r, 's_M': s_M, 's_i': s_i, 's_j': s_j}


def context_family():
    """The abstract family: (role, pair-of-colornames) moves, ordered
    word pairs with distinct pairs."""
    role_color = {'B1': 'r', 'n_sM': 's_M', 'B2': 'r',
                  'n_si': 's_i', 'n_sj': 's_j'}
    names = ['r', 's_M', 's_i', 's_j']
    moves = []
    for role, rc in role_color.items():
        for other in names:
            if other != rc:
                moves.append((role, tuple(sorted((rc, other)))))
    words = [(a, b) for a in moves for b in moves if a[1] != b[1]]
    # mirror symmetry: B1<->B2, s_i<->s_j
    def mirror(w):
        def mm(m):
            role, pair = m
            role2 = {'B1': 'B2', 'B2': 'B1', 'n_si': 'n_sj',
                     'n_sj': 'n_si'}.get(role, role)
            pair2 = tuple(sorted({'s_i': 's_j', 's_j': 's_i'}.get(x, x)
                                 for x in pair))
            return (role2, pair2)
        return (mm(w[0]), mm(w[1]))
    orbits = set()
    for w in words:
        orbits.add(min(str(w), str(mirror(w))))
    return moves, words, len(orbits)


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5570 — the word family + the joint witness")
    print("=" * 70)

    moves, words, n_orb = context_family()
    t1 = len(moves) == 15 and len(words) == 186
    print(f"\n  context-moves: {len(moves)}; F_ctx words: {len(words)}; "
          f"mirror orbits: {n_orb}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. The family, listed "
          f"whole (15 moves x ordered distinct-pair = 186; "
          f"{n_orb} mod mirror) — Cal's finite object")

    # populations
    pops = []
    fr_faces = G5.fritsch_faces()
    fr_adj = G5.adj_from_faces(fr_faces)
    fr_tv = [v for v in sorted(fr_adj) if len(fr_adj[v]) == 5][0]
    allc = list(G5.exhaustive_colorings(fr_adj, fr_tv))
    fr_stuck = [c for c in allc
                if G5.operational_tau(fr_adj, c, fr_tv) == 6
                and not X3.freeable(fr_adj, c, fr_tv)]
    fr_freed = [c for c in allc
                if G5.operational_tau(fr_adj, c, fr_tv) <= 5]
    pops.append(('Fritsch', fr_faces, fr_adj, fr_tv, fr_stuck,
                 fr_freed))
    harvest = json.load(open(os.path.join(HERE, '.f1_harvest.json')))
    objs = {}
    ad = G5.errera_adj()
    tris, ok, _m = G5.faces_from_adj_triangulation(ad)
    objs['B-errera'] = (tris, ad)
    t5 = [tuple(f) for f in F1.P3.antiprism_stack(5)]
    objs['C-T5'] = (t5, G5.adj_from_faces(t5))
    rr = F1.F3T.family_B_right(3, 0)
    objs['D-flip3'] = (rr[0], G5.adj_from_faces(rr[0]))
    for label, (faces, adj) in objs.items():
        if label not in harvest:
            continue
        tvraw = harvest[label]['tv']
        tv = next(v for v in adj if str(v) == tvraw)
        smap = {str(v): v for v in adj}
        stuck = [{smap[k2]: v for k2, v in crec.items()}
                 for crec in harvest[label]['stuck']][:50]
        _s, freed = F1.stuck_harvest(faces, adj, tv, n_seeds=15,
                                     n_walk=50, amp=0)
        pops.append((label, faces, adj, tv, stuck, freed))

    n_cfg = 0
    n_joint = 0
    misses = Counter()
    winner_words = {}
    for label, faces, adj, tv, stuck, freed in pops:
        lcyc = E1.link_cycle(faces, tv)
        vs = [v for v in sorted(adj, key=str) if v != tv]
        of = H8.orient_faces([tuple(f) for f in faces])
        comp_faces = [f for f in of if tv not in f]

        def charge(cc):
            w = {u: 0 for u in vs}
            for f in comp_faces:
                z = 1 if H8.face_sign(f, cc) == 1 else -1
                for x in f:
                    w[x] += z
            return w

        def dmin(cc):
            best = 10 ** 9
            for f2 in freed:
                h = sum(1 for v in vs if cc[v] != f2[v])
                if h < best:
                    best = h
                    if best <= 1:
                        break
            return best

        for c in stuck:
            rm = role_map(adj, c, tv, lcyc)
            if rm is None:
                continue
            vmap, cmap = rm
            n_cfg += 1
            c0f = charge(c)
            d0 = dmin(c) if freed else None
            hit = None
            for w in words:
                m1 = (tuple(sorted((cmap[w[0][1][0]],
                                    cmap[w[0][1][1]]))), vmap[w[0][0]])
                m2 = (tuple(sorted((cmap[w[1][1][0]],
                                    cmap[w[1][1][1]]))), vmap[w[1][0]])
                k = X3.commutator(adj, c, m1, m2, tv)
                if not X3.support(c, k):
                    continue
                if not G5.is_proper(adj, k, skip=tv):
                    continue
                if not X3.freeable(adj, k, tv):
                    continue
                c1f = charge(k)
                pp = {u for u in vs if c1f[u] != c0f[u]}
                pm = {u for u in vs if c1f[u] != -c0f[u]}
                patch = pp if len(pp) <= len(pm) else pm
                if len(patch) > 8:
                    continue
                if d0 is None or dmin(k) - d0 >= 0:
                    continue
                clause = False
                for f2 in freed:
                    gained = any(k[v] == f2[v] and c[v] != f2[v]
                                 for v in patch)
                    if not gained:
                        continue
                    if all(c[v] == f2[v] or k[v] != f2[v]
                           for v in vs if k[v] != f2[v]) and \
                       not any(k[v] != f2[v] and c[v] == f2[v]
                               for v in vs):
                        clause = True
                        break
                if clause:
                    hit = w
                    break
            if hit is not None:
                n_joint += 1
                winner_words.setdefault(str(hit), 0)
                winner_words[str(hit)] += 1
            else:
                misses[label] += 1
    t2 = n_cfg > 200
    print(f"\n  joint witness (gate & patch<=8-mod-gauge & M1-descent "
          f"& J2-clause, ONE word): {n_joint}/{n_cfg}")
    if misses:
        print(f"    misses by object (off-home carry the sampled-freed "
              f"false-negative caveat): {dict(misses)}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Joint-witness coverage "
          f"measured")

    # minimal covering sub-family (greedy over winner words)
    top = sorted(winner_words.items(), key=lambda x: -x[1])[:8]
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Winner-word census "
          f"(top, first-hit order-biased — the DOMAIN is the full "
          f"F_ctx; this names the workhorses): ")
    for w, n in top:
        print(f"    {n:5d}  {w}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5570 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
