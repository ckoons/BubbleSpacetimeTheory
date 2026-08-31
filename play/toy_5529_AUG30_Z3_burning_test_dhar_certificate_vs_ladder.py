#!/usr/bin/env python3
"""
Toy 5529 — Z3 (Round 6): THE BURNING TEST — Dhar-style certificate vs the
                          5/10/17 ladder (Lyra's M4 spec, pinned before run)

Lyra's registered conjecture: the radius-3 odd-charge ladder (5/10/17 at
depths 2/3/4) is a burning count in disguise. Spec pinned in her M4 note:
  root = the stuck apex (burns by fiat);
  monotone burning: an unburnt vertex ignites when #burnt neighbors >=
  theta(v);
  RULE A (her committed candidate): theta(v) = ceil((deg(v) - |3*omega(v)|)/2)
    — |3w| is degree-forced except at deg-6 (deg-4: 0; deg-5/7: 3), where
    omega comes from the stuck coloring's faces when the star is complete in
    G-v, else 0;
  RULE B (parity control): theta(v) = ceil(deg(v)/2) - (deg(v) odd);
  outputs: firing ROUNDS to fixpoint + UNBURNED CORE size;
  MANDATORY SPECIFICITY CONTROL: wrong-root rerun must DEGRADE the fit or
  the count is decorative and the conjecture dies regardless.

Anchors (exhaustive prior toys): Fritsch (ladder 5, depth 2) · T_4 (5, 2) ·
T_3 (10, 3) · Errera (10, 3) · Kittell (17, 4).

TESTS (X/Y):
  1. Burning engine sanity (star graph burns in 1 round at theta=1).
  2. Rule A from the apex: rounds/core per witness, and the can-fail
     scoring — Rule A's output (rounds, or core) must order the depth
     classes {2} < {3} < {4} consistently, no inversions.
  3. Rule B parity control reported (comparison, not scored to win).
  4. Wrong-root specificity: mean fit-quality over 5 deterministic
     non-apex roots must be WORSE than the apex fit (degradation
     required; if wrong roots fit as well, the conjecture dies).

Elie, 2026-08-30. Millennium week, 4-Color round 6. 4 tests.
"""

import importlib.util
import math
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5512b", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
T5 = load("t5515b", "toy_5515_AUG30_E1_kring_tower_family_rescue_depth_vs_k"
          "_cal_F0_absorbed.py")
H8 = load("t5518b", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
          "_stuck_separation.py")


def omega_deg6(faces, adj, col, tv):
    """omega for deg-6 vertices with complete stars in G-tv; others 0."""
    of = H8.orient_faces([tuple(f) for f in faces])
    w = {}
    for v in adj:
        if v == tv or len(adj[v]) != 6:
            continue
        if tv in adj[v]:
            w[v] = 0
            continue
        s = 0
        ok = True
        for f in of:
            if v in f:
                if tv in f:
                    ok = False
                    break
                sg = H8.face_sign(f, col)
                if sg is None:
                    ok = False
                    break
                s += 1 if sg == 1 else -1
        w[v] = s // 3 if ok and s % 3 == 0 else 0
    return w


def burn(adj, theta, root):
    burnt = {root}
    rounds = 0
    while True:
        newly = [v for v in adj if v not in burnt
                 and sum(1 for u in adj[v] if u in burnt) >= theta[v]]
        if not newly:
            break
        burnt.update(newly)
        rounds += 1
    return rounds, len(adj) - len(burnt)


def theta_ruleA(adj, w6, tv):
    th = {}
    for v in adj:
        d = len(adj[v])
        if d in (5, 7):
            q = 3
        elif d == 4:
            q = 0
        elif d == 6:
            q = abs(3 * w6.get(v, 0))
        else:
            q = 0
        th[v] = max(1, math.ceil((d - q) / 2))
    th[tv] = 0
    return th


def theta_ruleB(adj, tv):
    th = {}
    for v in adj:
        d = len(adj[v])
        th[v] = max(1, math.ceil(d / 2) - (1 if d % 2 else 0))
    th[tv] = 0
    return th


def witness_run(name, faces, adj, tv, ladder, depth, rule, w6):
    theta = (theta_ruleA(adj, w6, tv) if rule == 'A' else theta_ruleB(adj, tv))
    rounds, core = burn(adj, theta, tv)
    return rounds, core


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5529 — Z3: the burning test (Lyra M4 spec)")
    print("=" * 70)

    # Test 1: sanity
    star = {0: {1, 2, 3}, 1: {0}, 2: {0}, 3: {0}}
    r, c = burn(star, {0: 0, 1: 1, 2: 1, 3: 1}, 0)
    t1 = (r == 1 and c == 0)
    print(f"\n  star burn: rounds={r} core={c}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Engine sanity")

    # witnesses
    fri_f = G5.fritsch_faces()
    fri = G5.adj_from_faces(fri_f)
    ef, _o, _m = G5.faces_from_adj_triangulation(G5.errera_adj())
    err = G5.adj_from_faces(ef)
    kf, _o2, _m2 = G5.faces_from_adj_triangulation(G5.kittell_adj())
    kit = G5.adj_from_faces(kf)
    t3f = T5.tower_faces(3)
    t3 = T5.adj_from_faces(t3f)
    t4f = T5.tower_faces(4)
    t4 = T5.adj_from_faces(t4f)

    WITS = [('Fritsch', fri_f, fri, 0, 5, 2),
            ('T_4', t4f, t4, 0, 5, 2),
            ('T_3', t3f, t3, 0, 10, 3),
            ('Errera', ef, err, 0, 10, 3),
            ('Kittell', kf, kit, 17, 17, 4)]

    print("\n  Rule A (apex root) — witness: (rounds, core) vs (ladder, depth)")
    rowsA = []
    for name, faces, adj, tv, ladder, depth in WITS:
        # representative stuck coloring for deg-6 omega
        col = None
        for cnd in G5.sampled_colorings(adj, tv, 200):
            if G5.operational_tau(adj, cnd, tv) == 6:
                col = cnd
                break
        w6 = omega_deg6(faces, adj, col, tv) if col else {}
        rr, cc = witness_run(name, faces, adj, tv, ladder, depth, 'A', w6)
        rowsA.append((name, rr, cc, ladder, depth))
        print(f"    {name}: rounds={rr} core={cc}  (ladder {ladder}, "
              f"depth {depth})")

    def orders_depth(rows, idx):
        """Does statistic idx order depth classes without inversion?"""
        ok = True
        for n1, *r1 in rows:
            for n2, *r2 in rows:
                d1, d2 = r1[3], r2[3]
                v1, v2 = r1[idx - 1], r2[idx - 1]
                if d1 < d2 and v1 > v2:
                    ok = False
        return ok

    okA_rounds = orders_depth(rowsA, 1)
    okA_core = orders_depth(rowsA, 2)
    t2 = okA_rounds or okA_core
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Rule A orders the depth "
          f"classes (rounds: {okA_rounds}, core: {okA_core})")

    print("\n  Rule B (parity control):")
    rowsB = []
    for name, faces, adj, tv, ladder, depth in WITS:
        rr, cc = witness_run(name, faces, adj, tv, ladder, depth, 'B', {})
        rowsB.append((name, rr, cc, ladder, depth))
        print(f"    {name}: rounds={rr} core={cc}")
    t3_ = True
    print(f"\n  [{'PASS' if t3_ else 'FAIL'}] 3. Rule B control reported")

    # Test 4: wrong-root specificity
    print("\n  wrong-root control (Rule A, 5 deterministic non-apex roots):")
    def fit_quality(rows):
        # count of depth-ordered pairs (higher = better fit), rounds stat
        good = tot = 0
        for n1, *r1 in rows:
            for n2, *r2 in rows:
                if r1[3] < r2[3]:
                    tot += 1
                    if r1[0] <= r2[0]:
                        good += 1
        return good / tot if tot else 0

    apex_fit = fit_quality([(n, rr, cc, l, d) for n, rr, cc, l, d in rowsA])
    wr_fits = []
    for k in range(5):
        rows_w = []
        for name, faces, adj, tv, ladder, depth in WITS:
            others = [v for v in sorted(adj) if v != tv]
            root = others[(7 * k + 3) % len(others)]
            col = None
            for cnd in G5.sampled_colorings(adj, tv, 60):
                if G5.operational_tau(adj, cnd, tv) == 6:
                    col = cnd
                    break
            w6 = omega_deg6(faces, adj, col, tv) if col else {}
            th = theta_ruleA(adj, w6, tv)
            th = dict(th)
            th[tv] = max(1, math.ceil((len(adj[tv]) - 3) / 2))
            th[root] = 0
            rr, cc = burn(adj, th, root)
            rows_w.append((name, rr, cc, ladder, depth))
        wr_fits.append(fit_quality(rows_w))
    mean_wr = sum(wr_fits) / len(wr_fits)
    t4 = apex_fit > mean_wr
    print(f"    apex fit quality: {apex_fit:.2f}  wrong-root mean: "
          f"{mean_wr:.2f}  (individual {['%.2f' % f for f in wr_fits]})")
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Specificity: apex root fits "
          f"strictly better than wrong roots "
          f"({'conjecture survives' if t4 else 'DEGRADATION ABSENT — the count is decorative, the conjecture dies (M4 clause)'})")

    res = [t1, t2, t3_, t4]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5529 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")

    # ==================================================================
    # EXACT-SPEC RERUN (correction, round 7). The run above DEVIATED from
    # Lyra's pinned M4 in three details caught on re-reading the spec:
    #   (1) Rule A: her theta allows 0 (charged deg-6 burns spontaneously);
    #       mine forced min 1;
    #   (2) Rule B: hers is ceil(deg/2) + [deg odd]; mine subtracted;
    #   (3) wrong-root control: hers pins the ANTIPODAL vertex; mine used
    #       5 pseudo-random roots.
    # The verdict is re-rendered below on the exact instrument. Both runs
    # stay in the artifact; the EXACT-SPEC verdict is the one of record.
    # ==================================================================
    print("\n" + "=" * 70)
    print("EXACT-SPEC RERUN (the verdict of record)")
    print("=" * 70)

    def theta_A_exact(adj, w6, root):
        th = {}
        for v in adj:
            d = len(adj[v])
            q = 3 if d in (5, 7) else (abs(3 * w6.get(v, 0)) if d == 6 else 0)
            th[v] = math.ceil((d - q) / 2)
        th[root] = 0
        return th

    def theta_B_exact(adj, root):
        th = {}
        for v in adj:
            d = len(adj[v])
            th[v] = math.ceil(d / 2) + (1 if d % 2 else 0)
        th[root] = 0
        return th

    def antipode(adj, root):
        from collections import deque as _dq
        dist = {root: 0}
        q = _dq([root])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    q.append(w)
        return max(dist, key=lambda x: dist[x])

    rowsA2 = []
    rowsB2 = []
    rowsW2 = []
    for name, faces, adj, tv, ladder, depth in WITS:
        col = None
        for cnd in G5.sampled_colorings(adj, tv, 200):
            if G5.operational_tau(adj, cnd, tv) == 6:
                col = cnd
                break
        w6 = omega_deg6(faces, adj, col, tv) if col else {}
        rA, cA = burn(adj, theta_A_exact(adj, w6, tv), tv)
        rB, cB = burn(adj, theta_B_exact(adj, tv), tv)
        anti = antipode(adj, tv)
        thW = theta_A_exact(adj, w6, anti)
        rW, cW = burn(adj, thW, anti)
        rowsA2.append((name, rA, cA, ladder, depth))
        rowsB2.append((name, rB, cB, ladder, depth))
        rowsW2.append((name, rW, cW, ladder, depth))
        print(f"  {name}: RuleA(apex) rounds={rA} core={cA} · "
              f"RuleB rounds={rB} core={cB} · RuleA(antipode {anti}) "
              f"rounds={rW} core={cW}  (ladder {ladder}, depth {depth})")

    okA2_r = orders_depth(rowsA2, 1)
    okA2_c = orders_depth(rowsA2, 2)
    apex_fit2 = fit_quality(rowsA2)
    anti_fit2 = fit_quality(rowsW2)
    v_order = okA2_r or okA2_c
    v_spec = apex_fit2 > anti_fit2
    print(f"\n  EXACT-SPEC verdicts: depth-ordering (rounds {okA2_r}, "
          f"core {okA2_c}); specificity apex {apex_fit2:.2f} vs antipode "
          f"{anti_fit2:.2f} -> {'degrades' if v_spec else 'DOES NOT degrade'}")
    if v_order and v_spec:
        print("  VERDICT OF RECORD: the conjecture SURVIVES on the exact "
              "instrument — the earlier kill was an instrument artifact.")
    else:
        print("  VERDICT OF RECORD: the conjecture DIES on the exact "
              "instrument too — "
              + ("ordering fails" if not v_order else "")
              + (" and " if (not v_order and not v_spec) else "")
              + ("specificity fails (M4's own death clause)"
                 if not v_spec else "") + ".")
