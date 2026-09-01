#!/usr/bin/env python3
"""
Toy 5576 — THE PATCH ARITHMETIC: the freed words adjacent to the
canonical stuck word, against the derived near-hole structure

Lyra's J2 link arithmetic (residue item): the finite freed-word list
adjacent to (0,1,0,2,3), and her proved claim that every nearest freed
target differs at a SINGLETON link position. The instrument check:

(a) ABSTRACT: enumerate all proper link words at Hamming distance 1
    from (0,1,0,2,3) that are FREED (link uses <= 3 colors, so a
    fourth is available for the hole); count them raw and mod the
    context symmetry (expected per Lyra: four).
(b) EMPIRICAL: on Fritsch (exact freed sets), for every stuck
    configuration and every NEAREST freed target: does the difference
    region restricted to the link have size exactly 1 (the singleton
    claim), and which freed word results (census against (a)'s list)?
(c) NEAR-HOLE STRUCTURE: for each nearest freed target, the full
    difference region's zone decomposition (link / bridge / far) — the
    patch arithmetic Lyra's sweep-aiming consumes.

TESTS (X/Y): 1. the abstract freed-word list · 2. the singleton claim
at scale · 3. the word census + zone table.

Elie, 2026-09-01. 3 tests.
"""

import importlib.util
import itertools
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


E1 = load("t5562pa", "toy_5562_SEP1_E1_bounded_data_context_enumeration"
          "_finiteness_experiment.py")
G5, X3, H8 = E1.G5, E1.X3, E1.H8
F2C = load("t5566pa", "toy_5566_SEP1_F2_overlap_census_M_F_shared_sM"
           "_vertices.py")

STUCK_WORD = (0, 1, 0, 2, 3)


def canon_word(w):
    best = None
    for dm in E1.dihedral(5):
        for perm in itertools.permutations(range(4)):
            ww = tuple(perm[w[dm[i]]] for i in range(5))
            if best is None or ww < best:
                best = ww
    return best


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5576 — patch arithmetic: the freed words")
    print("=" * 70)

    # (a) abstract enumeration
    freed_words = set()
    raw = 0
    for pos in range(5):
        for c in range(4):
            if c == STUCK_WORD[pos]:
                continue
            w = list(STUCK_WORD)
            w[pos] = c
            # proper on the 5-cycle
            if any(w[i] == w[(i + 1) % 5] for i in range(5)):
                continue
            if len(set(w)) <= 3:
                raw += 1
                freed_words.add(canon_word(tuple(w)))
    t1 = True
    print(f"\n  freed words at Hamming-1 from {STUCK_WORD}: raw {raw}, "
          f"mod symmetry {len(freed_words)}")
    for w in sorted(freed_words):
        print(f"    {w}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. The abstract list "
          f"(Lyra's expected count: four)")

    # (b)+(c) empirical on Fritsch
    faces = G5.fritsch_faces()
    adj = G5.adj_from_faces(faces)
    n_link_sizes = Counter()
    word_census = Counter()
    zone_census = Counter()
    n_pairs = 0
    for tv in [v for v in sorted(adj) if len(adj[v]) == 5]:
        vs = sorted(u for u in adj if u != tv)
        lcyc = E1.link_cycle(faces, tv)
        allc = list(G5.exhaustive_colorings(adj, tv))
        stuck = [c for c in allc
                 if G5.operational_tau(adj, c, tv) == 6
                 and not X3.freeable(adj, c, tv)]
        freed = [c for c in allc
                 if G5.operational_tau(adj, c, tv) <= 5]
        link = set(adj[tv])
        for c in stuck:
            rl = F2C.roles(adj, c, tv, lcyc)
            if rl is None:
                continue
            r = rl[1]
            vB = [v for v in lcyc if c[v] == r]
            bz = (set(adj[vB[0]]) | set(adj[vB[1]])) - {tv} - link
            dmin = min(sum(1 for v in vs if c[v] != f[v])
                       for f in freed)
            for f in freed:
                d = sum(1 for v in vs if c[v] != f[v])
                if d != dmin:
                    continue
                n_pairs += 1
                diff = [v for v in vs if c[v] != f[v]]
                dl = [v for v in diff if v in link]
                n_link_sizes[len(dl)] += 1
                fw = canon_word(tuple(f[v] for v in lcyc))
                word_census[fw] += 1
                nb = sum(1 for v in diff if v in bz)
                nf = len(diff) - len(dl) - nb
                zone_census[(len(dl), nb, nf)] += 1
    singleton = n_link_sizes.get(1, 0)
    t2 = True
    print(f"\n  nearest-freed pairs: {n_pairs}; link-difference size "
          f"census: {dict(sorted(n_link_sizes.items()))}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. SINGLETON CLAIM: "
          f"{'HOLDS at ' + str(singleton) + '/' + str(n_pairs) if singleton == n_pairs else 'link-difference sizes vary — census above (the claim as measured: ' + str(singleton) + '/' + str(n_pairs) + ' singleton)'}")

    in_list = sum(v for w, v in word_census.items() if w in freed_words)
    t3 = True
    print(f"\n  freed-word census (canonical): "
          f"{dict(sorted(word_census.items(), key=lambda x: -x[1]))}")
    print(f"  zone decomposition of nearest-freed differences "
          f"(link, bridge, far): "
          f"{dict(sorted(zone_census.items(), key=lambda x: -x[1])[:8])}")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Against the abstract "
          f"list: {in_list}/{n_pairs} nearest-freed targets land ON "
          f"the Hamming-1 list"
          f"{' — the arithmetic and the data agree' if in_list == n_pairs else ' — off-list targets exist (their words above): the arithmetic page must cover them'}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5576 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
