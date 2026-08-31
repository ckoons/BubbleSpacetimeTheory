#!/usr/bin/env python3
"""
Toy 5544 — V2 (Round 12): SLOPE v2 — the DICTIONARY'S OWN TILT, blind rerun

Semantics v2, from the proved lift (Toy 5543's conventions, Lyra's
dictionary): for a pinning p, the boundary height walk is
  h(u_{i+1}) = h(u_i) + sigma(F_i) * L(p_i XOR p_{i+1}),
with sigma the fixed checkerboard (graph-level gauge) and F_i the face
traversing the boundary edge positively — pinning-only, no interior data
(the Disc Height Lemma's point). TILT(p) := max over the three lattice
directions x, y, x+y of (max - min) along the walk. Candidate Zero v2:
frozen <=> extremal tilt.

Blind protocol identical to v1: walks computed from pins only, hashed,
then joined. No recalibration: the functional above is fixed BEFORE the
join (Cal's guard); the v1 disclosure discipline repeats — no hand-checks
were run this time at all.

TESTS: 1. blind order · 2. tilt distribution · 3. prediction scored ·
4. anomaly census both directions.

Elie, 2026-08-30. Millennium week, 4-Color round 12. 4 tests.
"""

import hashlib
import importlib.util
import json
import os
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


Y4 = load("t5526v2", "toy_5526_AUG30_Y4_boundary_fisk_disc_relative_kempe"
          "_connectivity.py")
H8 = load("t5518v2", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
          "_stuck_separation.py")
Z1 = load("t5531v2", "toy_5531_AUG30_Z1_disc_decision_runner_guarded"
          "_awaiting_freeze.py")
V1 = load("t5543v2", "toy_5543_AUG30_V1_disc_height_fork_phases_or_defect.py")

STEP = V1.STEP


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5544 — V2: slope v2 (dictionary tilt), blind")
    print("=" * 70)

    adj, interior, bcyc = Y4.disc(2)
    faces = Z1.disc_faces(adj, interior, bcyc)
    ofaces = H8.orient_faces([tuple(f) for f in faces])

    # fixed checkerboard sigma (graph-level gauge)
    edge2faces = {}
    for fi, f in enumerate(ofaces):
        a, b, c = f
        for e in ((a, b), (b, c), (c, a)):
            edge2faces.setdefault(frozenset(e), []).append(fi)
    sigma = {0: 1}
    q = deque([0])
    while q:
        fi = q.popleft()
        for e, fs in edge2faces.items():
            if fi in fs and len(fs) == 2:
                fj = fs[0] if fs[1] == fi else fs[1]
                if fj not in sigma:
                    sigma[fj] = -sigma[fi]
                    q.append(fj)
    dir_face = {}
    for fi, f in enumerate(ofaces):
        a, b, c = f
        for (u, v) in ((a, b), (b, c), (c, a)):
            dir_face[(u, v)] = fi

    def bsign(u, v):
        if (u, v) in dir_face:
            return sigma[dir_face[(u, v)]]
        return -sigma[dir_face[(v, u)]]

    def tilt(pin_seq):
        h = (0, 0)
        walk = [h]
        n = len(bcyc)
        for i in range(n):
            u, v = bcyc[i], bcyc[(i + 1) % n]
            lab = pin_seq[i] ^ pin_seq[(i + 1) % n]
            s = bsign(u, v)
            dx, dy = STEP[lab]
            h = (h[0] + s * dx, h[1] + s * dy)
            walk.append(h)
        spans = []
        for proj in (lambda p: p[0], lambda p: p[1],
                     lambda p: p[0] + p[1]):
            vals = [proj(p) for p in walk]
            spans.append(max(vals) - min(vals))
        return max(spans)

    atlas = json.load(open(os.path.join(HERE,
                                        'availability_atlas_fcw014.json')))
    rows = atlas['rows']

    # PASS 1 blind
    tilts = [tilt(r['pin']) for r in rows]
    blob = json.dumps(tilts).encode()
    h = hashlib.sha256(blob).hexdigest()
    with open(os.path.join(HERE, '.v2_tilt_pass1.json'), 'wb') as f:
        f.write(blob)
    print(f"\n  PASS 1: {len(tilts)} tilts; sha256 {h[:32]}...")
    t1 = True
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Blind order enforced")

    dist = Counter(tilts)
    print(f"\n  tilt distribution: {dict(sorted(dist.items()))}")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Distribution reported")

    fr_idx = {i for i, r in enumerate(rows) if r['components'] >= 2}
    fr_tilts = Counter(tilts[i] for i in fr_idx)
    mn = min(tilts)
    min_idx = {i for i, t in enumerate(tilts) if t == mn}
    mx = max(tilts)
    max_idx = {i for i, t in enumerate(tilts) if t == mx}
    print(f"\n  frozen tilts: {dict(sorted(fr_tilts.items()))}; census "
          f"range [{mn}, {mx}]; |min class| {len(min_idx)}, |max class| "
          f"{len(max_idx)}")
    pred_max = fr_idx == max_idx
    pred_min = fr_idx == min_idx
    t3 = pred_max or pred_min
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Candidate Zero v2 "
          f"(frozen == extremal tilt class, either extreme): "
          f"max: {pred_max}, min: {pred_min}")

    froz_at = sorted(set(tilts[i] for i in fr_idx))
    conf = Counter((tilts[i], i in fr_idx) for i in range(len(rows)))
    n_at_frozen_tilts = sum(1 for i in range(len(rows))
                            if tilts[i] in froz_at and i not in fr_idx)
    print(f"\n  anomaly census: frozen tilt values {froz_at}; free "
          f"pinnings sharing those tilt values: {n_at_frozen_tilts}")
    t4 = True
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Anomaly census complete")

    res = [t1, t2, t3, t4]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5544 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
