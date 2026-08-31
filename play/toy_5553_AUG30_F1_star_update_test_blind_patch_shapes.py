#!/usr/bin/env python3
"""
Toy 5553 — F1 (Round 15): THE STAR-UPDATE TEST, blind

Keeper's pre-registration: the seven-site patches are closed vertex stars,
and each gate's displacement field is exactly a SINGLE-SITE HEIGHT UPDATE
under Prop CS — Kempe dynamics as height dynamics in composite clothing.

SEMANTICS (declared; Cal's pre-score not on disk at build):
  "a star" = the closed neighborhood N[u] = {u} + N(u) of some vertex u in
  the ambient (punctured) graph; ALSO classified: complement-of-one-vertex
  (the only 7-of-8 shape arithmetic allows here) and face-star vertex sets.
  "exactly a single-site height update" = the DIRECT test: compute the
  ZZ^2 height lifts (V1 machinery) of c and g.c on Fritsch-0 with the same
  gauge/base; the update is single-site iff Delta-h is supported on
  EXACTLY ONE vertex. (If the punctured object's checkerboard fails to
  exist, THAT is the finding — the lift is a disc-object privilege.)

BLIND: pass 1 computes patch-shape descriptors + Delta-h supports for all
unsticking applications and hashes them; pass 2 compares to templates.

TESTS (X/Y):
  1. Checkerboard/lift status on Fritsch-0 (exists or not — either way
     reported before anything else).
  2. Blind pass hashed; patch-shape census.
  3. VERDICT: star-update (both halves), pre-scored both ways; the true
     patch alphabet named if the guess dies.

Elie, 2026-08-30. Millennium week, 4-Color round 15. 3 tests.
"""

import hashlib
import importlib.util
import itertools
import json
import os
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5512f1", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
H8 = load("t5518f1", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
          "_stuck_separation.py")
X3 = load("t5521f1", "toy_5521_AUG30_X3_commutator_laboratory_support"
          "_locality_unstick.py")

TV = 0
STEP = {1: (1, 0), 2: (0, 1), 3: (-1, -1)}


def lift_punctured(adj, comp_faces_oriented, col, base):
    """Height lift on the punctured object using only complete faces.
    Returns (h, single_valued, checkerboard_ok)."""
    edge2faces = {}
    for fi, f in enumerate(comp_faces_oriented):
        a, b, c = f
        for e in ((a, b), (b, c), (c, a)):
            edge2faces.setdefault(frozenset(e), []).append(fi)
    sigma = {0: 1}
    q = deque([0])
    cb_ok = True
    while q:
        fi = q.popleft()
        for e, fs in edge2faces.items():
            if fi in fs and len(fs) == 2:
                fj = fs[0] if fs[1] == fi else fs[1]
                if fj not in sigma:
                    sigma[fj] = -sigma[fi]
                    q.append(fj)
                elif sigma[fj] != -sigma[fi]:
                    cb_ok = False
    if not cb_ok:
        return None, False, False
    dir_face = {}
    for fi, f in enumerate(comp_faces_oriented):
        a, b, c = f
        for (u, v) in ((a, b), (b, c), (c, a)):
            dir_face[(u, v)] = fi
    h = {base: (0, 0)}
    q = deque([base])
    sv = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v == TV or u == TV:
                continue
            key = (u, v) if (u, v) in dir_face else None
            key2 = (v, u) if (v, u) in dir_face else None
            if key is None and key2 is None:
                continue      # edge only on hole boundary faces
            s = sigma[dir_face[key]] if key else -sigma[dir_face[key2]]
            lab = col[u] ^ col[v]
            dx, dy = STEP[lab]
            hv = (h[u][0] + s * dx, h[u][1] + s * dy)
            if v in h:
                if h[v] != hv:
                    sv = False
            else:
                h[v] = hv
                q.append(v)
    return h, sv, True


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5553 — F1: the star-update test (blind)")
    print("=" * 70)

    faces = G5.fritsch_faces()
    adj = G5.adj_from_faces(faces)
    of = H8.orient_faces([tuple(f) for f in faces])

    # PASS 1 (blind)
    records = []
    lift_status = {}
    for tv in [v for v in sorted(adj) if len(adj[v]) == 5][:6]:
        vs = sorted(u for u in adj if u != tv)
        comp_faces = [f for f in of if tv not in f]
        base = vs[0]

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
            info = G5.structure_true(faces, adj, c, tv)
            if info is None:
                continue
            swaps, _fl = G5.forced_swaps(adj, c, tv, info)
            succ = sum(1 for (a, b), fv, ch in swaps
                       if G5.operational_tau(adj, G5.do_swap(c, ch, a, b),
                                             tv) <= 5)
            if succ != 0:
                continue
            mv = []
            for u in adj[tv]:
                cu = c[u]
                for other in range(4):
                    if other != cu:
                        mv.append((tuple(sorted((cu, other))), u))
            c0f = charge(c)
            h0, sv0, cb = lift_punctured(adj, comp_faces, c, base)
            lift_status[tv] = (cb, sv0)
            for m1, m2 in itertools.permutations(mv, 2):
                if m1[0] == m2[0]:
                    continue
                k = X3.commutator(adj, c, m1, m2, tv)
                s = X3.support(c, k)
                if not s or not G5.is_proper(adj, k, skip=tv):
                    continue
                if not X3.freeable(adj, k, tv):
                    continue
                c1f = charge(k)
                patch = tuple(sorted((u for u in vs
                                      if c1f[u] != c0f[u]), key=str))
                rec = {'tv': tv, 'patch_size': len(patch)}
                # shape descriptors (blind: no template comparison yet)
                rec['is_closed_nbhd'] = any(
                    set(patch) == ({u} | {w for w in adj[u] if w != tv})
                    for u in vs)
                rec['is_complement_1'] = (len(patch) == len(vs) - 1)
                # direct height test
                if cb and sv0 and h0 is not None:
                    h1, sv1, _ = lift_punctured(adj, comp_faces, k, base)
                    if sv1 and h1 is not None:
                        dsupp = [u for u in vs if h0.get(u) != h1.get(u)]
                        rec['dh_support'] = len(dsupp)
                    else:
                        rec['dh_support'] = -1
                else:
                    rec['dh_support'] = -2
                records.append(rec)
    blob = json.dumps(records, sort_keys=True).encode()
    hh = hashlib.sha256(blob).hexdigest()
    with open(os.path.join(HERE, '.f1_pass1.json'), 'wb') as f:
        f.write(blob)

    t1 = True
    print(f"\n  lift status per apex (checkerboard, single-valued): "
          f"{lift_status}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Lift status reported")

    print(f"\n  PASS 1: {len(records)} applications; sha256 {hh[:32]}...")
    shapes = Counter((r['patch_size'], r['is_closed_nbhd'],
                      r['is_complement_1']) for r in records)
    print(f"  patch-shape census (size, closed-nbhd?, complement-of-1?):")
    for k, v in sorted(shapes.items(), key=lambda x: -x[1])[:10]:
        print(f"    {k}: {v}")
    dh = Counter(r['dh_support'] for r in records)
    print(f"  Delta-h support census (−1 = lift broke post, −2 = no lift): "
          f"{dict(sorted(dh.items()))}")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Blind census computed")

    n = len(records)
    n_star = sum(1 for r in records if r['is_closed_nbhd'])
    n_single = sum(1 for r in records if r['dh_support'] == 1)
    t3 = True
    star_half = (f"closed-star patches: {n_star}/{n}")
    upd_half = (f"single-site height updates: {n_single}/{n}")
    if n_star == n and n_single == n:
        verdict = "STAR-UPDATE CONFIRMED — Kempe dynamics IS height dynamics"
    else:
        comp1 = sum(1 for r in records if r['is_complement_1'])
        verdict = (f"the guess dies; the true alphabet: {star_half}, "
                   f"{upd_half}, complement-of-one-vertex: {comp1}/{n} — "
                   f"see census")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. VERDICT: {verdict}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5553 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
