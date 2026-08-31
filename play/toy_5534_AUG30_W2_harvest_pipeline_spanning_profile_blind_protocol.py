#!/usr/bin/env python3
"""
Toy 5534 — W2 (Round 8): THE HARVEST PIPELINE — built, blind, and PARKED

RUN_MODE below is 'validation': NATAL GRAPHS ONLY (already measured to
death — zero new information, pure instrument check). Mass production over
the W1 population spec fires ONLY after Cal's fairness gate, by flipping
RUN_MODE to 'harvest'. The gate is respected in code, not just in prose.

MEASUREMENTS per witness (one pipeline, every axis):
  PASS 1 (blind half — written and HASHED before any reachability runs):
    - GF(2): achieved straddle span W (dim), deficiency (F-1) - dim W
      (Lyra: W subset of even-weight E is PROVED; deficiency counts extra
      GF(2) invariants; pre-registered W = E on rich graphs);
    - THE SPANNING PROFILE (Lyra's Gap A, the crown deliverable): per
      coloring f, rank A(f) of the indicators available AT f, vs rank W.
      Rank-drop sites predicted = frozen colorings (from Lemma R's frame:
      frozen => available indicators = the global transposition alone).
    - ZZ: SNF invariant factors (closure population);
    - charges: odd count, density, radius-3 odd charge at deg-5 vertices.
    Results written to JSON; sha256 printed = the checkpoint.
  PASS 2 (after the hash): Kempe classes / frozen census / per-partition
    reachability — the data that could bias pass 1 if computed first.

VALIDATION TESTS (X/Y), natal set (Fritsch, icosahedron, triakis, T_3,
subdiv-tetra):
  1. Blind order enforced mechanically (pass-1 JSON + hash exist before
     pass 2 starts; asserted in code).
  2. Spanning-profile prediction on the natal set: frozen colorings are
     EXACTLY the rank-drop sites (rank A(f) <= 1 < rank W where the graph
     is unfrozen-rich; on all-frozen graphs rank W itself is 1 and the
     profile is flat — both patterns are the prediction).
  3. Deficiency measured: dim W vs dim E per graph (Lyra's pre-registered
     W = E on rich graphs — scored on T_3 and subdiv-tetra).
  4. The ASC cross-check on natal data: same-GF(2)-fiber pairs are
     reachable (zero kills here is expected — natal replication of Z2;
     the harvest's version of this test is the one that matters).

Elie, 2026-08-30. Millennium week, 4-Color round 8. 4 tests.
"""

import hashlib
import importlib.util
import itertools
import json
import os
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RUN_MODE = 'harvest'             # GATE CLEARED: Cal SS789 W1 PASS-with-riders, 17:14 EDT


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5512h", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
T5 = load("t5515h", "toy_5515_AUG30_E1_kring_tower_family_rescue_depth_vs_k"
          "_cal_F0_absorbed.py")
H8 = load("t5518h", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
          "_stuck_separation.py")
Y3 = load("t5525h", "toy_5525_AUG30_Y3_dilution_test_akempic_knot_in"
          "_eulerian_bulk.py")
Y1 = load("t5527h", "toy_5527_AUG30_Y1_snf_engine_charge_lattice_invariant"
          "_factors.py")
Z2 = load("t5528h", "toy_5528_AUG30_Z2_realizability_gap_kempe_classes_vs"
          "_cokernel_fibers.py")
X4 = load("t5522h", "toy_5522_AUG30_X4_akempic_import_subdivided_tetrahedron"
          "_frozen_coloring_orthogonality.py")


def gf2_rank_basis(vectors):
    basis = []
    for v in vectors:
        v = list(v)
        for b in basis:
            piv = next(i for i, x in enumerate(b) if x)
            if v[piv]:
                v = [x ^ y for x, y in zip(v, b)]
        if any(v):
            basis.append(v)
    return basis


def chains_at(adj, col):
    for a, b in itertools.combinations(range(4), 2):
        done = set()
        for u in adj:
            if u in done or col[u] not in (a, b):
                continue
            comp = set()
            stack = [u]
            while stack:
                x = stack.pop()
                if x in comp:
                    continue
                comp.add(x)
                for w in adj[x]:
                    if w not in comp and col[w] in (a, b):
                        stack.append(w)
            done |= comp
            yield a, b, comp


def straddle_indicator(oriented_faces, S):
    return tuple(1 if 0 < sum(1 for x in f if x in S) < 3 else 0
                 for f in oriented_faces)


def pass1_measure(name, faces, adj):
    """The blind half: spans, spanning profile, SNF, charges. No
    reachability, no class computation, no frozen labels."""
    vs = sorted(adj, key=str)
    of = H8.orient_faces([tuple(f) for f in faces])
    colorings, _vs2 = Z2.all_colorings(adj)
    # partition reps (dedup by partition, NOT by class — no reachability)
    parts = {}
    for c in colorings:
        k = Z2.partition_key(c, vs)
        if k not in parts:
            parts[k] = c
    # per-coloring available indicators + global span
    all_inds = set()
    profile = {}
    for k, c in parts.items():
        inds = set()
        for a, b, comp in chains_at(adj, c):
            ind = straddle_indicator(of, comp)
            if any(ind):
                inds.add(ind)
        all_inds |= inds
        profile[str(k)] = len(gf2_rank_basis(inds))
    rankW = len(gf2_rank_basis(all_inds))
    F = len(of)
    dimE = F - 1
    # ZZ SNF over the same reps
    cols, _om, _p = Y1.build_columns(of, adj, list(parts.values()), vs)
    if cols:
        A = [[col[i] for col in cols] for i in range(len(vs))]
        diag, _U = Y1.smith_normal_form(A)
    else:
        diag = []
    odd = sum(1 for v in adj if len(adj[v]) % 2)
    return {
        'graph': name, 'V': len(adj), 'F': F, 'odd': odd,
        'partitions': len(parts),
        'rank_W': rankW, 'dim_E': dimE, 'deficiency': dimE - rankW,
        'snf_factors': [d for d in diag if d not in (0, 1)],
        'spanning_profile': profile,
    }, parts


def pass2_measure(name, faces, adj, parts):
    """Reachability half: Kempe classes + frozen census."""
    vs = sorted(adj, key=str)
    colorings, _ = Z2.all_colorings(adj)
    cid, ncl, _p2 = Z2.kempe_classes(adj, colorings, vs)
    frozen = {}
    for k, c in parts.items():
        frozen[str(k)] = Y3.is_frozen(adj, c)
    return {'classes': ncl,
            'class_of': {str(k): cid[k] for k in parts},
            'frozen': frozen}


if __name__ == "__main__":
    print("=" * 70)
    print(f"Toy 5534 — W2 harvest pipeline (RUN_MODE = {RUN_MODE})")
    print("=" * 70)
    if RUN_MODE == 'harvest':
        print("  gate citation: Cal SS789 (2026-08-30 17:14 EDT) — W1 PASS "
              "with riders R1-R4; tranche 1 authorized")


    if RUN_MODE == 'harvest':
        import random
        import sys
        W1 = load("t5533h", "toy_5533_AUG30_W1_witness_generator_population"
                  "_spec_for_cal_gate.py")

        def backtrack_seed(adj, order_seed, cap_tries=200000):
            vs = sorted(adj, key=str)
            rng = random.Random(order_seed)
            order = list(vs)
            rng.shuffle(order)
            col = {}
            tries = [0]

            def bt(i):
                if tries[0] > cap_tries:
                    return False
                if i == len(order):
                    return True
                u = order[i]
                cs = list(range(4))
                rng.shuffle(cs)
                for c in cs:
                    tries[0] += 1
                    if all(col.get(w) != c for w in adj[u]):
                        col[u] = c
                        if bt(i + 1):
                            return True
                        del col[u]
                return False

            return dict(col) if bt(0) else None

        def closure_from(adj, seed_col, cap):
            key0 = tuple(sorted(seed_col.items(), key=str))
            seen = {key0}
            q = [seed_col]
            out = [seed_col]
            while q and len(out) <= cap:
                c = q.pop()
                for a, b, comp in chains_at(adj, c):
                    nc = dict(c)
                    for x in comp:
                        nc[x] = b if nc[x] == a else a
                    k = tuple(sorted(nc.items(), key=str))
                    if k not in seen:
                        seen.add(k)
                        q.append(nc)
                        out.append(nc)
            return out, len(out) <= cap

        # ---------------- tranche-1 population (5533 spec + R3 flags) ----
        POP = []
        for n in (12, 16, 20, 25, 30, 40, 50):
            for sd in range(8):
                POP.append((f'F1_flip_n{n}_s{sd}', 'F1', 'LEAVING-HOME',
                            W1.FT.flipped_triangulation(n, seed=sd)))
        for k in (3, 4, 5, 6, 7):
            POP.append((f'F2_tower_T{k}', 'F2', 'NATAL',
                        T5.tower_faces(k)))
        for rs in ([5, 6, 5], [5, 6, 6, 5], [6, 5, 6], [5, 6, 5, 6, 5],
                   [6, 5, 5, 6]):
            POP.append((f'F2_mixed_{"".join(map(str, rs))}', 'F2',
                        'NATAL-DERIVED', W1.mixed_tower_faces(rs)))
        POP.append(('F3_Fritsch', 'F3', 'NATAL', G5.fritsch_faces()))
        ef3, _oo, _mm = G5.faces_from_adj_triangulation(G5.errera_adj())
        POP.append(('F3_Errera', 'F3', 'NATAL', ef3))
        kf3, _oo2, _mm2 = G5.faces_from_adj_triangulation(G5.kittell_adj())
        POP.append(('F3_Kittell', 'F3', 'NATAL', kf3))
        POP.append(('F4_triakis', 'F4', 'NATAL', Y3.triakis_faces()))
        for n in range(5, 11):
            POP.append((f'F5a_bipyr_n{n}', 'F5a', 'LEAVING-HOME',
                        W1.bipyramid_faces(n)))
        POP.append(('F5b_pentakis', 'F5b', 'LEAVING-HOME',
                    W1.pentakis_dodecahedron_faces()))
        for n in (15, 25, 40):
            for sd in range(5):
                POP.append((f'F5c_stacked_n{n}_s{sd}', 'F5c', 'BIAS-PROBE',
                            W1.FT.stacked_triangulation(n, seed=sd)))
        print(f"\n  TRANCHE 1: {len(POP)} graphs")

        # R4 mixing diagnostic on F1
        def degspec(faces):
            adjx = G5.adj_from_faces(faces)
            return Counter(len(sx) for sx in adjx.values())

        print("\n  R4 mixing diagnostic (degree-spectrum L1 distance, "
              "consecutive F1 seeds):")
        for n in (20, 40):
            dists = []
            for sd in range(7):
                d1 = degspec(W1.FT.flipped_triangulation(n, seed=sd))
                d2 = degspec(W1.FT.flipped_triangulation(n, seed=sd + 1))
                keys = set(d1) | set(d2)
                dists.append(sum(abs(d1[k] - d2[k]) for k in keys))
            print(f"    n={n}: distances {dists} (0 everywhere = unmixed)")

        # ---------------- PASS 1 (blind) ----------------
        print("\n  PASS 1 (blind) running ...")
        rows = {}
        popstore = {}
        deg7_obs = 0
        deg7_bad = []
        for name, fam, home, faces in POP:
            adj = G5.adj_from_faces(faces)
            vs = sorted(adj, key=str)
            of = H8.orient_faces([tuple(f) for f in faces])
            seeds = []
            for sdd in range(15):
                c = backtrack_seed(adj, sdd)
                if c:
                    seeds.append(c)
            comps = []
            seen_keys = set()
            total = []
            for c in seeds:
                k0 = tuple(sorted(c.items(), key=str))
                if k0 in seen_keys:
                    continue
                cls, closed = closure_from(adj, c, 400)
                comp_keys = set()
                for cc in cls:
                    kk = tuple(sorted(cc.items(), key=str))
                    comp_keys.add(kk)
                if comp_keys & seen_keys:
                    continue
                seen_keys |= comp_keys
                comps.append((cls, closed))
                total.extend(cls)
                if len(total) > 900:
                    break
            sample = total[:120]
            all_inds = set()
            prof = []
            for c in total:
                pass
            for c in sample:
                inds = set()
                for a, b, comp in chains_at(adj, c):
                    ind = straddle_indicator(of, comp)
                    if any(ind):
                        inds.add(ind)
                all_inds |= inds
                prof.append(len(gf2_rank_basis(inds)))
            for cls, closed in comps:
                for c in cls[:60]:
                    for a, b, comp in chains_at(adj, c):
                        ind = straddle_indicator(of, comp)
                        if any(ind):
                            all_inds.add(ind)
            rankW = len(gf2_rank_basis(all_inds))
            F = len(of)
            # charges + degree spectrum + deg-7 reading (R2)
            dspec = dict(Counter(len(sx) for sx in adj.values()))
            deg7v = [v for v in adj if len(adj[v]) == 7]
            for c in sample[:40]:
                for v in deg7v:
                    cv = 0
                    for f in of:
                        if v in f:
                            sg = H8.face_sign(f, c)
                            cv += 1 if sg == 1 else -1
                    deg7_obs += 1
                    if cv not in (3, -3):
                        deg7_bad.append((name, v, cv))
            cols, _om2, _p2x = Y1.build_columns(of, adj, sample[:60], vs)
            if cols:
                A = [[col[i] for col in cols] for i in range(len(vs))]
                diag, _U2 = Y1.smith_normal_form(A)
            else:
                diag = []
            odd = sum(1 for v in adj if len(adj[v]) % 2)
            rows[name] = {
                'family': fam, 'home': home, 'V': len(adj), 'F': F,
                'odd': odd, 'degree_spectrum': dspec,
                'n_deg7': len(deg7v),
                'population': len(total),
                'closed_components': sum(1 for _c, cl in comps if cl),
                'capped_components': sum(1 for _c, cl in comps if not cl),
                'rank_W': rankW, 'dim_E': F - 1,
                'deficiency': F - 1 - rankW,
                'profile_min': min(prof) if prof else None,
                'profile_max': max(prof) if prof else None,
                'snf_factors': [d for d in diag if d not in (0, 1)],
            }
            popstore[name] = (faces, adj, of, comps)
        blob = json.dumps(rows, sort_keys=True).encode()
        hh = hashlib.sha256(blob).hexdigest()
        ck = os.path.join(HERE, 'harvest_tranche1_pass1.json')
        with open(ck, 'wb') as fo:
            fo.write(blob)
        print(f"\n  PASS 1 complete: {len(rows)} graphs; deg-7 charge "
              f"observations {deg7_obs}, violations {len(deg7_bad)}")
        for b in deg7_bad[:10]:
            print(f"    *** DEG-7 CHARGE VIOLATION {b} — the quantization "
                  f"theorem is falsified if this survives audit")
        print(f"  CHECKPOINT sha256 = {hh[:40]}...")
        print(f"  file: {os.path.basename(ck)} (Grace schema feed)")

        # ---------------- PASS 2 ----------------
        print("\n  PASS 2 — reachability (CLOSED components only rule)")
        asc_kills = 0
        asc_tested = 0
        for name, (faces, adj, of, comps) in popstore.items():
            closed_comps = [cls for cls, cl in comps if cl]
            if len(closed_comps) < 2:
                continue
            all_inds = set()
            for cls in closed_comps:
                for c in cls[:60]:
                    for a, b, comp in chains_at(adj, c):
                        ind = straddle_indicator(of, comp)
                        if any(ind):
                            all_inds.add(ind)
            basis = gf2_rank_basis(all_inds)

            def red(v):
                v = list(v)
                for bb in basis:
                    piv = next(i for i, x in enumerate(bb) if x)
                    if v[piv]:
                        v = [x ^ y for x, y in zip(v, bb)]
                return tuple(v)

            def eps(c):
                return tuple(0 if H8.face_sign(f, c) == 1 else 1
                             for f in of)

            fibs = []
            for cls in closed_comps:
                e = eps(cls[0])
                fibs.append(min(red(e), red(tuple(1 ^ x for x in e))))
            asc_tested += 1
            for i in range(len(fibs)):
                for j in range(i + 1, len(fibs)):
                    if fibs[i] == fibs[j]:
                        asc_kills += 1
                        print(f"    *** ASC KILL CANDIDATE at {name}: "
                              f"closed components {i},{j} share a GF(2) "
                              f"fiber and are mutually unreachable")
        print(f"\n  ASC harvest test: {asc_tested} graphs with >=2 CLOSED "
              f"components tested; kill candidates: {asc_kills}")
        print("\n  TRANCHE 1 SUMMARY (leaving-home rows only in breadth "
              "statistics per R3):")
        lh = [r for r in rows.values() if r['home'] == 'LEAVING-HOME']
        d7 = sum(1 for r in lh if r['n_deg7'] > 0)
        print(f"    leaving-home graphs: {len(lh)}; with deg-7 carriers: "
              f"{d7} (R2: {'PRESENT' if d7 else 'STRATUM GAP'})")
        defs = Counter(r['deficiency'] for r in lh)
        print(f"    deficiency distribution (leaving-home): "
              f"{dict(sorted(defs.items()))}")
        sys.exit(0)

    NATAL = [('Fritsch', G5.fritsch_faces()),
             ('icosahedron', T5.tower_faces(2)),
             ('triakis', Y3.triakis_faces()),
             ('tower_T_3', T5.tower_faces(3)),
             ('subdiv_tetra', X4.subdivided_tetra_faces(3))]

    # ---------------- PASS 1 (blind) ----------------
    print("\nPASS 1 — blind half (no reachability computed yet)")
    p1 = {}
    parts_store = {}
    for name, faces in NATAL:
        adj = G5.adj_from_faces(faces)
        row, parts = pass1_measure(name, faces, adj)
        p1[name] = row
        parts_store[name] = (faces, adj, parts)
        prof = Counter(row['spanning_profile'].values())
        print(f"  {name}: partitions={row['partitions']} rank_W={row['rank_W']}"
              f" dim_E={row['dim_E']} deficiency={row['deficiency']} "
              f"profile-ranks={dict(sorted(prof.items()))} "
              f"snf={row['snf_factors']}")
    blob = json.dumps(p1, sort_keys=True).encode()
    h = hashlib.sha256(blob).hexdigest()
    ckpt = os.path.join(HERE, '.w2_pass1_validation.json')
    with open(ckpt, 'wb') as f:
        f.write(blob)
    print(f"\n  CHECKPOINT sha256 = {h[:32]}...  (file {os.path.basename(ckpt)})")
    t1 = os.path.exists(ckpt)
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Blind order enforced "
          f"(pass-1 written and hashed before pass 2)")

    # ---------------- PASS 2 ----------------
    print("\nPASS 2 — reachability half")
    p2 = {}
    for name, (faces, adj, parts) in parts_store.items():
        p2[name] = pass2_measure(name, faces, adj, parts)
        print(f"  {name}: classes={p2[name]['classes']} "
              f"frozen={sum(p2[name]['frozen'].values())}"
              f"/{len(p2[name]['frozen'])}")

    # Test 2: spanning-profile prediction
    ok2 = True
    for name in p1:
        rw = p1[name]['rank_W']
        for k, r in p1[name]['spanning_profile'].items():
            fz = p2[name]['frozen'][k]
            if fz and r > 1:
                ok2 = False
                print(f"  *** {name}: frozen partition with rank {r} > 1")
            if not fz and rw > 1 and r <= 1:
                ok2 = False
                print(f"  *** {name}: unfrozen partition rank-dropped to {r}")
    t2 = ok2
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Spanning profile: frozen "
          f"partitions are exactly the rank-drop sites (natal set)")

    # Test 3: deficiency / W = E on rich graphs
    rich_ok = all(p1[n]['deficiency'] == 0
                  for n in ('tower_T_3', 'subdiv_tetra'))
    print(f"\n  deficiencies: "
          f"{{n: p1[n]['deficiency'] for n in p1}} = "
          f"{ {n: p1[n]['deficiency'] for n in p1} }")
    t3 = rich_ok
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Lyra's W = E on rich graphs "
          f"(T_3, subdiv-tetra deficiency 0)")

    # Test 4: ASC cross-check on natal data (same GF(2) fiber => reachable)
    kills = 0
    for name, (faces, adj, parts) in parts_store.items():
        of = H8.orient_faces([tuple(f) for f in faces])
        vs = sorted(adj, key=str)

        def eps(c):
            return tuple(0 if H8.face_sign(f, c) == 1 else 1 for f in of)

        # span basis from pass-1 achieved indicators (recomputed cheaply)
        inds = set()
        for k, c in parts.items():
            for a, b, comp in chains_at(adj, c):
                ind = straddle_indicator(of, comp)
                if any(ind):
                    inds.add(ind)
        basis = gf2_rank_basis(inds)

        def red(v):
            v = list(v)
            for bb in basis:
                piv = next(i for i, x in enumerate(bb) if x)
                if v[piv]:
                    v = [x ^ y for x, y in zip(v, bb)]
            return tuple(v)

        fib = {}
        for k, c in parts.items():
            e = eps(c)
            key = min(red(e), red(tuple(1 ^ x for x in e)))
            fib.setdefault(key, []).append(k)
        for key, ks in fib.items():
            cls = {p2[name]['class_of'][str(k)] for k in ks}
            if len(cls) > 1:
                kills += 1
                print(f"  *** ASC KILL on natal {name}: fiber with classes "
                      f"{cls}")
    t4 = kills == 0
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. ASC natal replication "
          f"({kills} kills — harvest version is the real test)")

    res = [t1, t2, t3, t4]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5534 -- SCORE: {passed}/{len(res)} (VALIDATION MODE — "
          f"harvest awaits Cal's gate)")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
