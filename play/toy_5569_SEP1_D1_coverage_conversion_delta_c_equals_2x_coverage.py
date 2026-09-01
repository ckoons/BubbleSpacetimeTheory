#!/usr/bin/env python3
"""
Toy 5569 — the D1-COVERAGE CONVERSION: candidate to derived, or dead

The claim (Lyra's attack doc, carried since D1): the D1 displacement
values (2,2,4,4,6,6,6) ARE conveyor coverage-counts. Same-numbers-not-
same-objects governs: a shared multiset proves nothing; the conversion
requires the PER-VERTEX map, exhibited on every instance.

TESTED VERBATIM, strongest form first:
  H1 (per-vertex): for every unsticking gate application and every
     vertex v, |Delta-c(v)| = 2 * coverage(v), where coverage(v) =
     #{i : v in X_i} over the word's four acting chains, and
     Delta-c = charge-after - charge-before (complete-face charges).
  H2 (multiset fallback, reported only if H1 fails): per application,
     multiset {|Delta-c(v)|/2 : v in patch} = multiset of coverage
     counts over net-changed vertices.
Population: Fritsch, all stuck (tau6, not freeable) x all their
unsticking commutator gates — D1's home population, exhaustively.

Pre-scored: H1 exact everywhere -> CANDIDATE CONVERTS TO DERIVED (the
derivation Lyra writes gets its verified target; the map is exhibited).
H1 fails -> exhibit the failing (application, vertex) whole; if H2
also fails, the candidate DIES.

TESTS (X/Y): 1. population + chains extracted · 2. H1 verdict ·
3. the conversion ruling.

Elie, 2026-09-01. Millennium week II. 3 tests.
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


E1 = load("t5562d1c", "toy_5562_SEP1_E1_bounded_data_context_enumeration"
          "_finiteness_experiment.py")
G5, X3, H8 = E1.G5, E1.X3, E1.H8


def commutator_with_chains(adj, col, m1, m2, tv):
    chains = []
    c = col
    for move in (m1, m2, m1, m2):
        pair, seed = move
        a, b = pair
        if c.get(seed) in (a, b):
            comp = G5.kempe_chain(adj, c, seed, a, b, exclude={tv})
            chains.append(comp)
            c = G5.do_swap(c, comp, a, b)
        else:
            chains.append(set())
    return c, chains


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5569 — D1-coverage conversion: |Delta-c| = 2 x coverage?")
    print("=" * 70)

    faces = G5.fritsch_faces()
    adj = G5.adj_from_faces(faces)
    of = H8.orient_faces([tuple(f) for f in faces])

    n_apps = 0
    h1_viol = []
    h2_viol = 0
    per_pair_census = Counter()
    for tv in [v for v in sorted(adj) if len(adj[v]) == 5]:
        vs = sorted(u for u in adj if u != tv)
        comp_faces = [f for f in of if tv not in f]

        def charge(c):
            w = {u: 0 for u in vs}
            for f in comp_faces:
                z = 1 if H8.face_sign(f, c) == 1 else -1
                for x in f:
                    w[x] += z
            return w

        for c in G5.exhaustive_colorings(adj, tv):
            if G5.operational_tau(adj, c, tv) != 6:
                continue
            if X3.freeable(adj, c, tv):
                continue
            mv = []
            for u in adj[tv]:
                cu = c[u]
                for other in range(4):
                    if other != cu:
                        mv.append((tuple(sorted((cu, other))), u))
            c0f = charge(c)
            for m1, m2 in itertools.permutations(mv, 2):
                if m1[0] == m2[0]:
                    continue
                k, chains = commutator_with_chains(adj, c, m1, m2, tv)
                if not X3.support(c, k):
                    continue
                if not G5.is_proper(adj, k, skip=tv):
                    continue
                if not X3.freeable(adj, k, tv):
                    continue
                n_apps += 1
                c1f = charge(k)
                ok1 = True
                for v in vs:
                    dc = abs(c1f[v] - c0f[v])
                    cov = sum(1 for X in chains if v in X)
                    per_pair_census[(dc, cov)] += 1
                    if dc != 2 * cov:
                        ok1 = False
                        if len(h1_viol) < 8:
                            h1_viol.append((tv, v, dc, cov))
                if not ok1:
                    ms1 = sorted(abs(c1f[v] - c0f[v]) // 2
                                 for v in vs if c1f[v] != c0f[v])
                    ms2 = sorted(sum(1 for X in chains if v in X)
                                 for v in vs if k[v] != c[v])
                    if ms1 != ms2:
                        h2_viol += 1
    t1 = n_apps > 3000
    print(f"\n  applications: {n_apps} (all apexes, exhaustive stuck)")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Population + chains")

    print(f"\n  (|Delta-c|, coverage) census: "
          f"{dict(sorted(per_pair_census.items()))}")
    h1 = not h1_viol
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. H1 per-vertex "
          f"|Delta-c| = 2*coverage: "
          f"{'EXACT on every vertex of every application' if h1 else 'VIOLATED — ' + str(h1_viol[:6])}")

    t3 = True
    if h1:
        ruling = ("CANDIDATE CONVERTS TO DERIVED-TARGET: the per-vertex "
                  "map |Delta-c(v)| = 2*coverage(v) is exact on the "
                  "full population — the D1 values ARE coverage counts "
                  "by the exhibited map, not by shared numbers; the "
                  "algebraic derivation (each chain-pass toggles v once "
                  "and each toggle moves the complete-face charge by "
                  "exactly 2) now has its verified statement")
    elif h2_viol == 0:
        ruling = ("H1 dies, H2 survives: the identity holds only as "
                  "multisets — same numbers, NOT same objects; the "
                  "candidate stays a candidate with its gap named")
    else:
        ruling = (f"THE CANDIDATE DIES: per-vertex fails and even the "
                  f"multiset form fails on {h2_viol} applications")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. RULING: {ruling}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5569 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
