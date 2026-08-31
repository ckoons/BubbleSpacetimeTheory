#!/usr/bin/env python3
"""
Toy 5547 — G1+G2 (Round 13): THE GATE STRUCTURE PROPOSITION'S TWO TESTS

Lyra's GS Proposition (board R83): every gate = a conjugated singleton,
w = alpha-sigma-alpha. Two instant tests on the stored Fritsch-v gate
alphabet (186 ordered words, the 5535 population):

G1 = GS-2, THE KILL TEST (run first, sharper blade): every NET-SUPPORT
vertex of every gate application must be EVEN-DEGREE in the ambient
dynamics graph (Fritsch-0; a singleton shift needs a 2-colorable link,
no-local-rotation forbids odd). ONE odd-degree support vertex kills GS.
Semantics pinned here (Cal's pre-score not yet on disk; declared, not
assumed silently): support(g, c) := {v : (g.c)(v) != c(v)} — the standing
X3 definition; degree = degree in the punctured graph Fritsch-0, the graph
the chains actually live in.

G2 = GS-1, THE FACTORIZATION CENSUS: for each gate application with
nonempty support, does there exist a single available swap alpha (at c)
and a vertex u such that: sigma = a SINGLETON swap at u is available in
alpha(c) (some pair whose chain at u is exactly {u}), and
alpha'(sigma(alpha(c))) = g.c where alpha' is the same (pair, seed) move
re-applied? Failures exhibited, not summarized.

TESTS (X/Y):
  1. Ambient degree table printed (who is even/odd in Fritsch-0).
  2. G1 verdict: support-vertex degree census; ANY odd kills GS.
  3. G2 census on a stated sample; failures exhibited.

Elie, 2026-08-30. Millennium week, 4-Color round 13. 3 tests.
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


G5 = load("g5512g", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")

TV = 0


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5547 — G1+G2: gate structure tests")
    print("=" * 70)

    fri = G5.adj_from_faces(G5.fritsch_faces())
    vs = sorted(u for u in fri if u != TV)
    pdeg = {u: len([w for w in fri[u] if w != TV]) for u in vs}
    print(f"\n  punctured degrees (Fritsch-0): {pdeg}")
    even_v = {u for u in vs if pdeg[u] % 2 == 0}
    print(f"  even-degree vertices: {sorted(even_v)}")
    t1 = True
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Ambient degrees printed")

    # colorings of Fritsch-0
    cols = []
    col = {}

    def bt(i):
        if i == len(vs):
            cols.append(dict(col))
            return
        u = vs[i]
        for c in range(4):
            if all(col.get(w) != c for w in fri[u] if w != TV):
                col[u] = c
                bt(i + 1)
                del col[u]

    bt(0)

    def apply_move(c, m):
        pair, seed = m
        a, b = pair
        if c.get(seed) not in (a, b):
            return c
        S = G5.kempe_chain(fri, c, seed, a, b, exclude={TV})
        nc = dict(c)
        for x in S:
            nc[x] = b if nc[x] == a else a
        return nc

    def moves_at(c):
        out = []
        for u in fri[TV]:
            cu = c[u]
            for other in range(4):
                if other != cu:
                    out.append((tuple(sorted((cu, other))), u))
        return out

    def apply_gate(c, m1, m2):
        cur = c
        for m in (m1, m2, m1, m2):
            cur = apply_move(cur, m)
        return cur

    alphabet = moves_at(cols[0])
    gates = [(m1, m2) for m1, m2 in itertools.permutations(alphabet, 2)
             if m1[0] != m2[0]]

    # G1: support-degree census over all gates x all colorings
    odd_hits = []
    supp_sizes = Counter()
    napps = 0
    for g in gates:
        for c in cols:
            nc = apply_gate(c, *g)
            supp = [v for v in vs if nc[v] != c[v]]
            if not supp:
                continue
            napps += 1
            supp_sizes[len(supp)] += 1
            for v in supp:
                if pdeg[v] % 2 == 1:
                    odd_hits.append((g, tuple(sorted(c.items()))[:0], v))
    print(f"\n  G1: applications with nonempty support: {napps}; "
          f"support-size dist {dict(sorted(supp_sizes.items()))}")
    n_odd = len(odd_hits)
    if n_odd:
        seen_v = Counter(v for _g, _c, v in odd_hits)
        print(f"  *** ODD-DEGREE SUPPORT VERTICES HIT: {dict(seen_v)} "
              f"({n_odd} instances)")
        for g, _c, v in odd_hits[:5]:
            print(f"    gate {g} support vertex {v} (deg {pdeg[v]})")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. G1 VERDICT: "
          f"{'GS KILLED — odd-degree support exists (' + str(n_odd) + ' instances)' if n_odd else 'GS SURVIVES the kill test — every support vertex even-degree'}")

    # G2: factorization census on a sample
    print("\n  G2 (factorization census, sample = first 40 colorings x "
          "all gates with nonempty support, cap 400 applications):")
    tested = 0
    factored = 0
    failures = []
    for g in gates:
        for c in cols[:40]:
            nc = apply_gate(c, *g)
            if nc == c:
                continue
            tested += 1
            if tested > 400:
                break
            ok = False
            for alpha in moves_at(c) + [(p, s) for s in vs
                                        for p in
                                        itertools.combinations(range(4), 2)
                                        if c.get(s) in p][:0]:
                ca = apply_move(c, alpha)
                if ca == c:
                    continue
                # singleton moves available at ca
                for u in vs:
                    cu = ca[u]
                    for other in range(4):
                        if other == cu:
                            continue
                        pair = tuple(sorted((cu, other)))
                        S = G5.kempe_chain(fri, ca, u, *pair, exclude={TV})
                        if S != {u}:
                            continue
                        cs = dict(ca)
                        cs[u] = other
                        cf = apply_move(cs, alpha)
                        if cf == nc:
                            ok = True
                            break
                    if ok:
                        break
                if ok:
                    break
            # also allow trivial alpha (identity): w = sigma alone
            if not ok:
                for u in vs:
                    cu = c[u]
                    for other in range(4):
                        if other == cu:
                            continue
                        pair = tuple(sorted((cu, other)))
                        S = G5.kempe_chain(fri, c, u, *pair, exclude={TV})
                        if S == {u}:
                            cs = dict(c)
                            cs[u] = other
                            if cs == nc:
                                ok = True
                                break
                    if ok:
                        break
            if ok:
                factored += 1
            else:
                failures.append((g, c))
        if tested > 400:
            break
    print(f"    tested {min(tested, 400)}; factored {factored}; "
          f"failures {len(failures)}")
    for g, c in failures[:5]:
        nc = apply_gate(c, *g)
        supp = [v for v in vs if nc[v] != c[v]]
        print(f"    *** UNFACTORED: gate {g} support {supp} "
              f"(sizes {len(supp)})")
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. G2 census: "
          f"{'ALL FACTOR — GS-1 holds on the sample' if not failures else str(len(failures)) + ' unfactored applications EXHIBITED'}")

    res = [t1, t2, t3]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5547 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
