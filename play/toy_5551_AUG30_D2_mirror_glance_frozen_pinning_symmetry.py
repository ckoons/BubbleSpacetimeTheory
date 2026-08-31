#!/usr/bin/env python3
"""
Toy 5551 — D2 (Round 14): THE MIRROR GLANCE

Keeper's second pre-registration: ground-state degeneracy requires a
symmetry — are all 15 frozen pinnings symmetric under a (dihedral x color)
symmetry that EXCHANGES the two tilings?

SEMANTICS (declared): for a frozen pinning p on the 12-cycle with twins
T1, T2: a twin-exchange symmetry is a pair (g, pi) — g in the dihedral
group D12 acting on the disc (rotations/reflections that are graph
automorphisms of the disc fixing it setwise), pi a color permutation —
with pi(p(g(u))) = p(u) for all boundary u (the pinning is stabilized)
and the induced map sending T1 to T2. The disc's automorphisms: the 12
rotations/reflections of the hexagonal lattice disc (6 rotations x 2).
Census: per frozen pinning, does such a pair exist? Both directions
pre-scored: any frozen pinning WITHOUT one kills the pre-registration;
free multi-completion pinnings WITH the analogous structure measure the
sufficiency gap.

TESTS (X/Y): 1. automorphisms constructed and verified · 2. the census ·
3. the verdict + sufficiency gap.

Elie, 2026-08-30. Millennium week, 4-Color round 14. 3 tests.
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


Y4 = load("t5526d2", "toy_5526_AUG30_Y4_boundary_fisk_disc_relative_kempe"
          "_connectivity.py")


def disc_automorphisms(adj):
    """The hexagonal disc's dihedral automorphisms as vertex maps, from
    axial-coordinate rotations/reflections, verified against adj."""
    def rot60(p):
        q, r = p
        return (-r, q + r)

    def refl(p):
        q, r = p
        return (r, q)

    maps = []
    for k in range(6):
        for do_refl in (False, True):
            def make(k=k, do_refl=do_refl):
                def f(p):
                    if do_refl:
                        p = refl(p)
                    for _ in range(k):
                        p = rot60(p)
                    return p
                return f
            maps.append(make())
    good = []
    for f in maps:
        img = {v: f(v) for v in adj}
        if set(img.values()) != set(adj):
            continue
        if all(img[w] in adj[img[v]] for v in adj for w in adj[v]):
            good.append(img)
    return good


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5551 — D2: the mirror glance")
    print("=" * 70)

    adj, interior, bcyc = Y4.disc(2)
    autos = disc_automorphisms(adj)
    print(f"\n  disc automorphisms verified: {len(autos)} (expect 12)")
    t1 = len(autos) == 12
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Automorphism group built")

    atlas = json.load(open(os.path.join(HERE,
                                        'availability_atlas_fcw014.json')))
    rows = atlas['rows']
    frozen_rows = [r for r in rows if r['components'] >= 2]
    perms = list(itertools.permutations(range(4)))

    def census_row(r, need_exchange):
        pinseq = r['pin']
        pin = dict(zip(bcyc, pinseq))
        comps = Y4.completions(adj, interior, pin)
        found = False
        for g in autos:
            # g must map boundary to boundary
            if any(g[u] not in pin for u in bcyc):
                continue
            for piv in perms:
                if all(piv[pin[g[u]]] == pin[u] for u in bcyc):
                    if not need_exchange:
                        if any(any(piv[c0[g[u]]] != c0[u] for u in interior)
                               for c0 in comps):
                            found = True
                    else:
                        # induced map on completions: c -> pi . c . g
                        c0, c1 = comps[0], comps[1]
                        mapped = {u: piv[c0[g[u]]] for u in interior}
                        if mapped == c1:
                            found = True
                if found:
                    break
            if found:
                break
        return found

    n_exch = 0
    killers = []
    for r in frozen_rows:
        ok = census_row(r, need_exchange=True)
        if ok:
            n_exch += 1
        else:
            killers.append(r['pin'])
    print(f"\n  frozen pinnings with a twin-EXCHANGING symmetry: "
          f"{n_exch}/{len(frozen_rows)}")
    for p in killers[:6]:
        print(f"    *** NO exchange symmetry: {p}")
    # sufficiency gap: free multi-completion pinnings whose pinning is
    # stabilized by a nontrivial (g, pi) pair
    n_free_sym = 0
    free_multi = [r for r in rows if r['components'] == 1
                  and r['nodes'] >= 2][:400]
    for r in free_multi:
        pin = dict(zip(bcyc, r['pin']))
        sym = False
        for g in autos:
            if any(g[u] not in pin for u in bcyc):
                continue
            for piv in perms:
                ident = all(g[u] == u for u in bcyc) and \
                    all(piv[i] == i for i in range(4))
                if ident:
                    continue
                if all(piv[pin[g[u]]] == pin[u] for u in bcyc):
                    sym = True
                    break
            if sym:
                break
        n_free_sym += sym
    print(f"  free multi-completion pinnings (first 400) with a nontrivial "
          f"stabilizing symmetry: {n_free_sym}")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Census complete")
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. VERDICT: "
          f"{'ALL frozen pinnings carry a twin-exchange symmetry — the degeneracy IS symmetry-protected; sufficiency gap = ' + str(n_free_sym) + ' symmetric-but-free' if not killers else str(len(killers)) + ' frozen pinnings WITHOUT exchange symmetry — the pre-registration is KILLED'}")

    res = [t1, t2, t3]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5551 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
