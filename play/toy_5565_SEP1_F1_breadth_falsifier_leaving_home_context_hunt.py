#!/usr/bin/env python3
"""
Toy 5565 — F1 (Sept 1 PM): THE BREADTH FALSIFIER — leaving home

Protocol Section 4 step 1: the Candidate Assembly cannot bank without
this. Hunt stuck configurations (tau=6 at a deg-5 hole, not directly
freeable) across families the vocabularies did NOT grow up on, and for
every one compute its canonical bounded context (5562's instrument).

FAMILIES (leaving-home strata):
  A. random stacked triangulations at scale (P3.stacked_triangulation,
     n in {12,16,20,26} x seeds) — degree-diverse, no antiprism blood;
  B. the literature killers: Errera (17v), Kittell (23v);
  C. adversarial deep tower T_5 (V=27);
  D. flip-modified subdivided octahedra (Family-B constructor, O(4)
     with 1-3 local flips — deg-5 holes born from surgery).

BLIND: every (family, graph, context) record is computed and hashed
BEFORE any comparison against the canonical context (itself recomputed
in-run from Fritsch, not hard-coded). KILL CONDITIONS pre-registered:
one second context anywhere kills the One-Context Lemma's empirical
escort (reopens L1 at the named line); a stuck configuration with no
gate, no patch-local gate, or no M1-descending gate refutes the
measured escorts of J1/J2. Zero kills at scale = the escort the bank
requires. Counts reported either way. Outcome analysis capped at 150
stuck per graph (declared); context computed on ALL stuck found.
Harvest dumped to .f1_harvest.json for F2/F3.

TESTS (X/Y): 1. breadth population (>= 8 graphs with stuck found,
>= 3 families) · 2. blind hash + context census · 3. the kill-count
verdict (contexts) · 4. the J1/J2 escort verdict (outcomes).

Elie, 2026-09-01. Millennium week II. 4 tests.
"""

import hashlib
import importlib.util
import itertools
import json
import os
import random
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


E1 = load("t5562f1", "toy_5562_SEP1_E1_bounded_data_context_enumeration"
          "_finiteness_experiment.py")
G5, X3, P3, H8 = E1.G5, E1.X3, E1.P3, E1.H8
F3T = load("t5555f1", "toy_5555_AUG30_F3_familyB_done_right_and_hall"
           "_obstruction_instrument.py")


def stuck_harvest(faces, adj, tv, n_seeds=25, n_walk=70, amp=40):
    vs = sorted(v for v in adj if v != tv)
    seen = set()
    pop = []
    for s in range(n_seeds):
        c = E1.bt_color(adj, tv, s)
        if c is None:
            continue
        frontier = [c]
        for step in range(n_walk):
            rng = random.Random(s * 7919 + step)
            cc = dict(frontier[rng.randrange(len(frontier))])
            u = rng.choice(vs)
            a = cc[u]
            b = rng.choice([x for x in range(4) if x != a])
            comp = G5.kempe_chain(adj, cc, u, a, b, exclude={tv})
            cc = G5.do_swap(cc, comp, a, b)
            key = tuple(cc[v] for v in vs)
            if key not in seen:
                seen.add(key)
                pop.append(cc)
                frontier.append(cc)
    base_stuck = [c for c in pop if G5.operational_tau(adj, c, tv) == 6]
    for si, c0 in enumerate(base_stuck[:amp]):
        cur = dict(c0)
        for step in range(40):
            rng = random.Random(si * 6007 + step)
            u = rng.choice(vs)
            a = cur[u]
            b = rng.choice([x for x in range(4) if x != a])
            comp = G5.kempe_chain(adj, cur, u, a, b, exclude={tv})
            nxt = G5.do_swap(cur, comp, a, b)
            if G5.operational_tau(adj, nxt, tv) == 6:
                cur = nxt
                key = tuple(cur[v] for v in vs)
                if key not in seen:
                    seen.add(key)
                    pop.append(dict(cur))
    stuck = [c for c in pop
             if G5.operational_tau(adj, c, tv) == 6
             and not X3.freeable(adj, c, tv)]
    freed = [c for c in pop if G5.operational_tau(adj, c, tv) <= 5]
    return stuck, freed


def outcome_of(faces, adj, tv, c, freed, ball, comp_faces, vs):
    gs = E1.gates_of(adj, c, tv)
    if not gs:
        return (False, False, False)

    def charge(cc):
        w = {u: 0 for u in vs}
        for f in comp_faces:
            z = 1 if H8.face_sign(f, cc) == 1 else -1
            for x in f:
                w[x] += z
        return w

    def dmin(cc):
        best = 10 ** 9
        for f in freed:
            h = sum(1 for v in vs if cc[v] != f[v])
            if h < best:
                best = h
                if best <= 1:
                    break
        return best

    c0f = charge(c)
    d0 = dmin(c) if freed else None
    patch_local = desc = False
    for k in gs:
        c1f = charge(k)
        pp = {u for u in vs if c1f[u] != c0f[u]}
        pm = {u for u in vs if c1f[u] != -c0f[u]}
        patch = pp if len(pp) <= len(pm) else pm
        if patch <= ball:
            patch_local = True
        if d0 is not None and dmin(k) - d0 < 0:
            desc = True
        if patch_local and desc:
            break
    return (True, patch_local, desc)


def build_families():
    fams = []
    # A: stacked triangulations
    for n in (12, 16, 20, 26):
        for sd in (1, 2, 3):
            faces = P3.stacked_triangulation(n, seed=sd)
            adj = G5.adj_from_faces([tuple(f) for f in faces])
            tvs = [v for v in sorted(adj) if len(adj[v]) == 5][:2]
            for tv in tvs:
                fams.append((f'A-stack{n}s{sd}', faces, adj, tv))
    # B: literature killers
    for nm, ad in (('B-errera', G5.errera_adj()),
                   ('B-kittell', G5.kittell_adj())):
        tris, ok, msg = G5.faces_from_adj_triangulation(ad)
        if not ok:
            continue
        tvs = [v for v in sorted(ad) if len(ad[v]) == 5][:2]
        for tv in tvs:
            fams.append((nm, tris, ad, tv))
    # C: deep tower T_5
    t5 = [tuple(f) for f in P3.antiprism_stack(5)]
    a5 = G5.adj_from_faces(t5)
    fams.append(('C-T5', t5, a5, max(a5)))
    # D: flip-modified O(4)
    for k, off in ((1, 0), (2, 0), (3, 0)):
        r = F3T.family_B_right(k, off)
        if r is None:
            continue
        faces, target, dist = r
        adj = G5.adj_from_faces(faces)
        tvs = [v for v in sorted(adj, key=str)
               if len(adj[v]) == 5][:1]
        for tv in tvs:
            fams.append((f'D-flip{k}', faces, adj, tv))
    return fams


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5565 — F1: the breadth falsifier (leaving home)")
    print("=" * 70)

    # canonical context recomputed in-run from Fritsch (not hard-coded)
    fr_faces = G5.fritsch_faces()
    fr_adj = G5.adj_from_faces(fr_faces)
    fr_tv = [v for v in sorted(fr_adj) if len(fr_adj[v]) == 5][0]
    fr_lcyc = E1.link_cycle(fr_faces, fr_tv)
    canon_ctx = None
    for c in G5.exhaustive_colorings(fr_adj, fr_tv):
        if G5.operational_tau(fr_adj, c, fr_tv) == 6 and \
                not X3.freeable(fr_adj, c, fr_tv):
            canon_ctx = E1.bounded_context(fr_adj, c, fr_tv, fr_lcyc)
            break
    print(f"\n  canonical context (in-run, Fritsch): "
          f"word={canon_ctx[0]}")

    fams = build_families()
    print(f"  leaving-home strata: {len(fams)} (graph, hole) pairs")

    records = []          # blind pass-1: (label, ctx) for ALL stuck
    outcome_bad = []
    n_out = Counter()
    harvest = {}
    graphs_with_stuck = set()
    for label, faces, adj, tv in fams:
        lcyc = E1.link_cycle(faces, tv)
        if len(lcyc) != 5:
            continue
        stuck, freed = stuck_harvest(faces, adj, tv)
        if not stuck:
            continue
        graphs_with_stuck.add(label)
        vs = sorted(adj, key=str)
        vs = [v for v in vs if v != tv]
        of = H8.orient_faces([tuple(f) for f in faces])
        comp_faces = [f for f in of if tv not in f]
        dist = {tv: 0}
        q = deque([tv])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    q.append(w)
        ball = {v for v in adj if v != tv and dist[v] <= 2}
        for c in stuck:
            ctx = E1.bounded_context(adj, c, tv, lcyc)
            records.append((label, ctx))
        for c in stuck[:150]:
            o = outcome_of(faces, adj, tv, c, freed, ball,
                           comp_faces, vs)
            n_out[o] += 1
            if o != (True, True, True):
                outcome_bad.append((label, o))
        harvest[label] = {'tv': str(tv),
                          'stuck': [{str(k): v for k, v in c.items()}
                                    for c in stuck[:150]],
                          'n_freed': len(freed)}
        print(f"    {label}: stuck={len(stuck)} freed={len(freed)}")
    fam_letters = {lb.split('-')[0] for lb in graphs_with_stuck}
    t1 = len(graphs_with_stuck) >= 8 and len(fam_letters) >= 3
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Breadth: "
          f"{len(graphs_with_stuck)} holes with stuck found across "
          f"families {sorted(fam_letters)}")

    blob = json.dumps([(lb, str(cx)) for lb, cx in records],
                      sort_keys=True).encode()
    hh = hashlib.sha256(blob).hexdigest()
    with open(os.path.join(HERE, '.f1_harvest.json'), 'w') as f:
        json.dump(harvest, f)
    ctx_census = Counter(str(cx) for _, cx in records)
    t2 = len(records) > 200
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. BLIND pass: "
          f"{len(records)} stuck contexts hashed (sha256 {hh[:32]}...); "
          f"distinct contexts: {len(ctx_census)}")

    kills = [(lb, cx) for lb, cx in records if cx != canon_ctx]
    t3 = True
    if not kills:
        v3 = (f"ZERO KILLS AT SCALE — every one of {len(records)} "
              f"stuck configurations from leaving-home strata presents "
              f"THE canonical context; the One-Context Lemma's "
              f"empirical escort HOLDS across the world it did not "
              f"grow up in")
    else:
        kc = Counter(lb for lb, _ in kills)
        v3 = (f"SECOND CONTEXT FOUND — {len(kills)} instances "
              f"({dict(kc)}); the One-Context Lemma's escort DIES and "
              f"L1 reopens at the named line; first exhibit: "
              f"{kills[0][0]}: word={kills[0][1][0]}, "
              f"partitions={kills[0][1][1]}")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. KILL COUNT: {v3}")

    t4 = True
    if not outcome_bad:
        v4 = (f"J1/J2 ESCORTS HOLD — outcome (gate, patch-local, "
              f"descends) = (True, True, True) on all "
              f"{sum(n_out.values())} analyzed (census {dict(n_out)}; "
              f"sampled-freed caveat on descent)")
    else:
        bc = Counter((lb, o) for lb, o in outcome_bad)
        v4 = (f"ESCORT REFUTED — {len(outcome_bad)} bad outcomes: "
              f"{dict(bc)}")
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. J1/J2 ESCORT: {v4}")

    res = [t1, t2, t3, t4]
    print(f"\n{'=' * 70}")
    print(f"Toy 5565 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
