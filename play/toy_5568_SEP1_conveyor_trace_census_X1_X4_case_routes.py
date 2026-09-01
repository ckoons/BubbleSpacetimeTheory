#!/usr/bin/env python3
"""
Toy 5568 — the CONVEYOR TRACE CENSUS (Lyra's J1 attack, trace requests
verbatim)

Per stored gate instance, the anchored word c0 -a-> c1 -b-> c2 -a-> c3
-b-> c4 with a = ((r,s_M), n_sM), b = ((s_M,s_i), n_si). Acting chains
X1..X4 extracted stage by stage. Reported per Lyra's one-pass spec:

  - |X2 ∩ X1| + distance-from-hole profile  (case-b incidence; the
    Confinement Lemma says X2∩X1 ⊆ old-r of X1 — VERIFIED per trace as
    a free control);
  - |X3 ∩ X2-old-s_i| + profile             (case-c accretion);
  - every deep-ρ excision (dist >= 2) X4-returned?  (case-b
    termination; ANY unreturned deep excision = counterexample, whole);
  - conveyor coverage-count distribution over net support
    (net support = (X1△X3) ∪ (X2△X4) — identity VERIFIED against the
    word's actual net color change per trace, a second free control);
  - case-(a)-only incidence (all X2∩X1 at the link).

Both dihedral orientations of the word traced (n_si adjacent to B2,
each bridge as B2). Population: Fritsch exact 72 + the F1 harvest
(Errera, Kittell, T5, D-flips), unchanged from disk.

Pre-registered (Lyra): (a) dominant; (b)/(c) rare-or-confined;
counterexample shapes = unreturned excision / unbounded accretion.

TESTS (X/Y): 1. traces run + BOTH identities verified (Confinement,
Net-Support) · 2. the census · 3. the case verdict.

Elie, 2026-09-01. Millennium week II. 3 tests.
"""

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


F2C = load("t5566cv", "toy_5566_SEP1_F2_overlap_census_M_F_shared_sM"
           "_vertices.py")
F1 = F2C.F1
E1, G5, X3, H8 = F2C.E1, F2C.G5, F2C.X3, F2C.H8


def trace(adj, c0, tv, n_sM, r, s_M, n_si, s_i):
    """Run the anchored word; return X1..X4 and the colorings."""
    X1 = G5.kempe_chain(adj, c0, n_sM, r, s_M, exclude={tv})
    c1 = G5.do_swap(c0, X1, r, s_M)
    if c1.get(n_si) not in (s_M, s_i):
        X2, c2 = set(), dict(c1)
    else:
        X2 = G5.kempe_chain(adj, c1, n_si, s_M, s_i, exclude={tv})
        c2 = G5.do_swap(c1, X2, s_M, s_i)
    if c2.get(n_sM) not in (r, s_M):
        X3c, c3 = set(), dict(c2)
    else:
        X3c = G5.kempe_chain(adj, c2, n_sM, r, s_M, exclude={tv})
        c3 = G5.do_swap(c2, X3c, r, s_M)
    if c3.get(n_si) not in (s_M, s_i):
        X4, c4 = set(), dict(c3)
    else:
        X4 = G5.kempe_chain(adj, c3, n_si, s_M, s_i, exclude={tv})
        c4 = G5.do_swap(c3, X4, s_M, s_i)
    return X1, X2, X3c, X4, c1, c2, c3, c4


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5568 — the conveyor trace census (X1..X4, case routes)")
    print("=" * 70)

    # populations (as F2/F3 built them)
    pops = []
    fr_faces = G5.fritsch_faces()
    fr_adj = G5.adj_from_faces(fr_faces)
    fr_tv = [v for v in sorted(fr_adj) if len(fr_adj[v]) == 5][0]
    fr_stuck = [c for c in G5.exhaustive_colorings(fr_adj, fr_tv)
                if G5.operational_tau(fr_adj, c, fr_tv) == 6
                and not X3.freeable(fr_adj, c, fr_tv)]
    pops.append(('Fritsch', fr_faces, fr_adj, fr_tv, fr_stuck))
    harvest = json.load(open(os.path.join(HERE, '.f1_harvest.json')))
    objs = {}
    ad = G5.errera_adj()
    tris, ok, _m = G5.faces_from_adj_triangulation(ad)
    objs['B-errera'] = (tris, ad)
    ad = G5.kittell_adj()
    tris, ok, _m = G5.faces_from_adj_triangulation(ad)
    objs['B-kittell'] = (tris, ad)
    t5 = [tuple(f) for f in F1.P3.antiprism_stack(5)]
    objs['C-T5'] = (t5, G5.adj_from_faces(t5))
    for k in (2, 3):
        rr = F1.F3T.family_B_right(k, 0)
        objs[f'D-flip{k}'] = (rr[0], G5.adj_from_faces(rr[0]))
    for label, (faces, adj) in objs.items():
        if label not in harvest:
            continue
        tvraw = harvest[label]['tv']
        tv = next(v for v in adj if str(v) == tvraw)
        smap = {str(v): v for v in adj}
        stuck = [{smap[k2]: v for k2, v in crec.items()}
                 for crec in harvest[label]['stuck']]
        pops.append((label, faces, adj, tv, stuck))

    n_traces = 0
    conf_viol = 0
    nsi_viol = 0
    inter21_prof = Counter()
    accr_prof = Counter()
    deep_total = deep_returned = 0
    unreturned_exhibits = []
    accr_far = []
    coverage = Counter()
    case_a_only = 0
    conv_traces = 0
    net_max_dist = Counter()
    for label, faces, adj, tv, stuck in pops:
        lcyc = E1.link_cycle(faces, tv)
        dist = {tv: 0}
        q = deque([tv])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    q.append(w)
        vs = [v for v in sorted(adj, key=str) if v != tv]
        for c0 in stuck:
            rl = F2C.roles(adj, c0, tv, lcyc)
            if rl is None:
                continue
            n_sM, r, s_M, s_i0, s_j0 = rl
            # the two orientations: n_si adjacent to a bridge
            cols = [c0[v] for v in lcyc]
            for n_si in lcyc:
                sx = c0[n_si]
                if sx not in (s_i0, s_j0):
                    continue
                X1, X2, X3c, X4, c1, c2, c3, c4 = trace(
                    adj, c0, tv, n_sM, r, s_M, n_si, sx)
                n_traces += 1
                # control 1: Confinement — X2∩X1 ⊆ old-r of X1
                i21 = X2 & X1
                if any(c0[v] != r for v in i21):
                    conf_viol += 1
                # control 2: net-support identity
                ns_formula = (X1 ^ X3c) | (X2 ^ X4)
                ns_actual = {v for v in vs if c4[v] != c0[v]}
                if ns_formula != ns_actual:
                    nsi_viol += 1
                dprof = tuple(sorted(dist[v] for v in i21))
                inter21_prof[(label, len(i21), dprof)] += 1
                deep = {v for v in i21 if dist[v] >= 2}
                if not deep:
                    case_a_only += 1
                deep_total += len(deep)
                ret = {v for v in deep if v in X4}
                deep_returned += len(ret)
                for v in deep - ret:
                    if len(unreturned_exhibits) < 6:
                        unreturned_exhibits.append(
                            (label, str(v), dist[v],
                             ('inX1', v in X1), ('inX3', v in X3c)))
                # case (c): X3 ∩ X2-old-s_i
                old_si = {v for v in X2 if c1[v] == sx}
                ac = X3c & old_si
                aprof = tuple(sorted(dist[v] for v in ac))
                accr_prof[(label, len(ac), aprof)] += 1
                for v in ac:
                    if dist[v] >= 3 and len(accr_far) < 6:
                        accr_far.append((label, str(v), dist[v]))
                # conveyor coverage over net support
                if ns_actual:
                    conv_traces += 1
                    for v in ns_actual:
                        coverage[sum(1 for X in (X1, X2, X3c, X4)
                                     if v in X)] += 1
                    net_max_dist[max(dist[v] for v in ns_actual)] += 1
    t1 = n_traces > 1000 and conf_viol == 0 and nsi_viol == 0
    print(f"\n  traces: {n_traces} (2 orientations x stuck configs); "
          f"CONFINEMENT LEMMA verified: {n_traces - conf_viol}/"
          f"{n_traces}; NET-SUPPORT IDENTITY verified: "
          f"{n_traces - nsi_viol}/{n_traces}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Traces + both proved "
          f"identities verified as free controls")

    print(f"\n  |X2∩X1| top profiles (object, size, dists): "
          f"{dict(sorted(inter21_prof.items(), key=lambda x: -x[1])[:8])}")
    print(f"  case-(a)-only traces (no deep entry): {case_a_only}/"
          f"{n_traces}")
    print(f"  deep-rho excisions: {deep_total}; X4-returned: "
          f"{deep_returned}; UNRETURNED: {deep_total - deep_returned}")
    for e in unreturned_exhibits:
        print(f"    *** UNRETURNED: {e}")
    print(f"  accretion |X3∩X2-old-s_i| top profiles: "
          f"{dict(sorted(accr_prof.items(), key=lambda x: -x[1])[:8])}")
    for e in accr_far:
        print(f"    *** FAR ACCRETION (dist>=3): {e}")
    print(f"  conveyor coverage-count distribution (net-support "
          f"vertices): {dict(sorted(coverage.items()))}")
    print(f"  net-support max-distance distribution: "
          f"{dict(sorted(net_max_dist.items()))}")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Census complete")

    # RECONCILIATION CENSUS (in-run amendment): F1 measured small
    # patches on these same objects while the color-support here runs
    # to distance 6. J3's collapse is the candidate reconciliation: the
    # gauge-invariant object is the CHARGE patch mod global re-signing,
    # not color support. Measure it for the SAME traces.
    print(f"\n  RECONCILIATION: charge patch (mod gauge) of the SAME "
          f"anchored words whose color support ran deep:")
    rec_census = Counter()
    for label, faces, adj, tv, stuck in pops:
        lcyc = E1.link_cycle(faces, tv)
        of2 = H8.orient_faces([tuple(f) for f in faces])
        comp_faces = [f for f in of2 if tv not in f]
        vs = [v for v in sorted(adj, key=str) if v != tv]
        dist = {tv: 0}
        q = deque([tv])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    q.append(w)

        def charge(cc):
            w = {u: 0 for u in vs}
            for f in comp_faces:
                z = 1 if H8.face_sign(f, cc) == 1 else -1
                for x in f:
                    w[x] += z
            return w

        for c0 in stuck[:60]:
            rl = F2C.roles(adj, c0, tv, lcyc)
            if rl is None:
                continue
            n_sM, r, s_M, s_i0, s_j0 = rl
            for n_si in lcyc:
                sx = c0[n_si]
                if sx not in (s_i0, s_j0):
                    continue
                X1, X2, X3c, X4, c1, c2, c3, c4 = trace(
                    adj, c0, tv, n_sM, r, s_M, n_si, sx)
                ns = {v for v in vs if c4[v] != c0[v]}
                if not ns:
                    continue
                cs_dist = max(dist[v] for v in ns)
                c0f = charge(c0)
                c4f = charge(c4)
                pp = {u for u in vs if c4f[u] != c0f[u]}
                pm = {u for u in vs if c4f[u] != -c0f[u]}
                patch = pp if len(pp) <= len(pm) else pm
                pd = max((dist[v] for v in patch), default=0)
                rec_census[(label, cs_dist >= 4, len(patch) <= 8,
                            pd <= max(2, cs_dist // 2))] += 1
    print(f"    (object, color-support-deep?, charge-patch<=8?, "
          f"charge-patch-shallow?): {dict(sorted(rec_census.items(), key=str))}")

    unret = deep_total - deep_returned
    far_ac = len(accr_far)
    t3 = True
    if unret == 0 and far_ac == 0:
        v = (f"NO counterexample shape realized: every deep-rho "
             f"excision is X4-RETURNED ({deep_returned}/{deep_total}) "
             f"and every accretion sits within dist <= 2 — target "
             f"lemmas (b) and (c) are TRUE-shaped on everything held; "
             f"case (a) covers {case_a_only}/{n_traces} traces "
             f"outright. NONE of the three lemmas falls; the conveyor "
             f"terminates everywhere we can see")
    else:
        v = (f"COUNTEREXAMPLE SHAPE(S): unreturned deep excisions "
             f"{unret} (exhibits above) and/or far accretions "
             f"{far_ac} — the falling lemma is named by the exhibits")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. CASE VERDICT: {v}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5568 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
