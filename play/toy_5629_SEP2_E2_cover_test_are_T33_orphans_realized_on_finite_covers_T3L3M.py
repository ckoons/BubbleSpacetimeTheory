#!/usr/bin/env python3
"""
Toy 5629 — Keeper 14:37 item 5, the COVER question (Casey: "orphans need explanation and derivation";
Lyra derives, Grace's instrument tests): is every orphan sign record of T(3,3) REALIZED on a finite
cover?  Grace, 2026-09-02.

An orphan = a Heawood-closed record with no coloring (toy 5627: T(3,3) has 202 closed, 20 realized,
182 orphans: 162 transport-obstructed, 20 cocycle-obstructed).  The covers T(3L,3M) -> T(3,3) are the
lattice quotient maps; a record on T(3,3) lifts by pulling back the face sign.  Prediction to test
(the theory's, not mine): a transport obstruction is a Z3 holonomy, killed by a cover that is a
multiple of 3 in the obstructed direction; a cocycle obstruction is a V = Z2^2 holonomy, killed by an
even cover.  So every orphan should be realized on T(18,18) at the latest, and the MINIMAL realizing
cover of each orphan should read off its obstruction type.  Measured here: for each orphan, the set of
(L, M) in {1,2,3,6}^2 on which its lift is realized; the minimal ones; and the per-type tally.
Positive control: every one of the 20 realized records stays realized on every cover (a pullback of a
coloring is a coloring).
"""
import os, sys, json, itertools, time
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
t = importlib.import_module('toy_5627_SEP2_E2_bundle_law_torus_test_completions_per_sign_record_mod_A4_with_sphere_disc_controls')

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()

def lattice_faces(a, b):
    """faces as coordinate triples (ccw), same construction as toy 5627 ms_torus."""
    faces = []
    for x in range(a):
        for y in range(b):
            p = (x, y); q = ((x + 1) % a, y); r = ((x + 1) % a, (y + 1) % b); s_ = (x, (y + 1) % b)
            faces.append((p, q, r)); faces.append((p, r, s_))
    return faces

def relabel(faces):
    idx = {}
    for f in faces:
        for v in f: idx.setdefault(v, len(idx))
    return [tuple(idx[v] for v in f) for f in faces], idx

def realized(faces_int, adj, n, rec):
    lab, obs = t.propagate_labels(faces_int, rec)
    if obs: return 'transport'
    col = t.colors_from_labels(adj, lab, n)
    return 'realized' if col is not None else 'cocycle'

def main():
    base = lattice_faces(3, 3)
    base_int, _ = relabel(base)
    adj = t.adjacency(base_int); n = 9
    cols, orb = t.per_record(base_int, adj, n)
    real_recs = set(orb)
    # all closed records of T(3,3), classified
    F = len(base_int)
    closed = []
    for bits in range(1 << F):
        r = tuple(1 if (bits >> i) & 1 else -1 for i in range(F))
        if t.heawood_closed(base_int, r):
            closed.append((r, realized(base_int, adj, n, r)))
    tally = Counter(k for _, k in closed)
    print(f"T(3,3): closed {len(closed)}  {dict(tally)}   [{time.time()-T0:.0f}s]")
    assert tally['realized'] == len(real_recs) == 20
    # base face index by (x, y, which)
    base_key = {}
    for i, (x, y) in enumerate(itertools.product(range(3), range(3))):
        base_key[(x, y, 0)] = 2 * i; base_key[(x, y, 1)] = 2 * i + 1
    covers = [(L, M) for L in (1, 2, 3, 6) for M in (1, 2, 3, 6)]
    cov = {}
    for L, M in covers:
        a, b = 3 * L, 3 * M
        fc = lattice_faces(a, b)
        fi, idx = relabel(fc)
        keys = []                       # for each cover face, the base face it covers
        for x in range(a):
            for y in range(b):
                keys.append(base_key[(x % 3, y % 3, 0)]); keys.append(base_key[(x % 3, y % 3, 1)])
        cov[(L, M)] = (fi, t.adjacency(fi), a * b, keys)
    results = []
    for r, kind in closed:
        row = dict(kind=kind, record=r, realized_on=[])
        for (L, M) in covers:
            fi, adjc, nc, keys = cov[(L, M)]
            lifted = tuple(r[k] for k in keys)
            assert t.heawood_closed(fi, lifted)
            st = realized(fi, adjc, nc, lifted)
            row[f"{L}x{M}"] = st
            if st == 'realized': row['realized_on'].append((L, M))
        # minimal covers (no strictly smaller realizing cover dividing it)
        ro = set(row['realized_on'])
        row['minimal'] = sorted([(L, M) for (L, M) in ro
                                 if not any((L2, M2) != (L, M) and L % L2 == 0 and M % M2 == 0 for (L2, M2) in ro)])
        results.append(row)
    # controls and tallies
    ctrl = all(len(r['realized_on']) == len(covers) for r in results if r['kind'] == 'realized')
    print(f"positive control: the 20 realized records stay realized on all {len(covers)} covers: {'PASS' if ctrl else 'FAIL'}")
    orphans = [r for r in results if r['kind'] != 'realized']
    never = [r for r in orphans if not r['realized_on']]
    print(f"orphans {len(orphans)}; realized on SOME cover in the set: {len(orphans) - len(never)}; on NONE (up to 6x6): {len(never)}")
    for kind in ('transport', 'cocycle'):
        sub = [r for r in orphans if r['kind'] == kind]
        mins = Counter(tuple(r['minimal']) for r in sub)
        print(f"  {kind}-obstructed ({len(sub)}): minimal realizing covers (L,M) -> count:")
        for k, v in sorted(mins.items(), key=lambda kv: -kv[1]): print(f"      {k}: {v}")
        # per-cover realization rate
        rate = {f"{L}x{M}": sum(1 for r in sub if r[f"{L}x{M}"] == 'realized') for (L, M) in covers}
        print(f"      realized-on-cover counts: {rate}")
    out = dict(toy=5629, closed=len(closed), tally=dict(tally), control=ctrl, orphans=len(orphans),
               never_realized_up_to_6x6=len(never),
               rows=[dict(kind=r['kind'], minimal=r['minimal'], realized_on=r['realized_on'],
                          record=''.join('+' if z == 1 else '-' for z in r['record'])) for r in results])
    path = os.path.join(HERE, '.cover_test_T33_orphans_5629.json')
    json.dump(out, open(path, 'w'), indent=1)
    print("written", path, f"[{time.time()-T0:.0f}s]")
    print("SCORE:", "PASS" if ctrl else "FAIL", "— control; cover realization is reported, not scored")

if __name__ == '__main__':
    main()
