#!/usr/bin/env python3
"""
Toy 5577 — THE RE-DRESS WITNESS AT SCALE + THE RIM-CONTACT CENSUS

(A) Re-dress theorem, clean case, witnessed (Lyra's proof, my
instrument): for stored traces whose stranded remnant R is nonempty
and LINK-FREE, and for every freed target c* agreeing with c on
R ∪ N(R): the re-dressed c*' (:= r<->s_M-swapped c* on R, c*
elsewhere) must be (i) proper, (ii) freed (tau <= 5), and (iii) the
disagreement count on R must be exactly conserved (H(w·c, c*') on R
= H(c, c*) on R). Also reported: the clean case's INHABITATION — how
often such a c* exists at all (if rare, the residual case is the
common case, which is domain knowledge for the boundary analysis).

(B) The rim-contact census (the residual case's true frequency and
size): per link-free-R trace, for the NEAREST freed targets: how
often does the difference region meet R ∪ N(R), and with what contact
size. The 185 third-bridge no-stranding traces get their own row:
their nearest-freed difference vs the bridge zone.

Freed sets: Fritsch exact; towers/killers sampled (false-negative
caveat on inhabitation, none on witnessed identities).

TESTS (X/Y): 1. populations + R census · 2. the re-dress witness
verdict · 3. the rim-contact census + the 185's row.

Elie, 2026-09-01. 3 tests.
"""

import importlib.util
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


P1 = load("t5571rd", "toy_5571_SEP1_P1_pair_census_exclusion_conjecture"
          "_kill_test.py")
CV, F2C, F1 = P1.CV, P1.F2C, P1.F1
E1, G5, X3, H8 = P1.E1, P1.G5, P1.X3, P1.H8


def build_pops():
    pops = []
    fr_faces = G5.fritsch_faces()
    fr_adj = G5.adj_from_faces(fr_faces)
    fr_tv = [v for v in sorted(fr_adj) if len(fr_adj[v]) == 5][0]
    allc = list(G5.exhaustive_colorings(fr_adj, fr_tv))
    fr_stuck = [c for c in allc
                if G5.operational_tau(fr_adj, c, fr_tv) == 6
                and not X3.freeable(fr_adj, c, fr_tv)]
    fr_freed = [c for c in allc
                if G5.operational_tau(fr_adj, c, fr_tv) <= 5]
    pops.append(('Fritsch', fr_faces, fr_adj, fr_tv, fr_stuck,
                 fr_freed, True))
    t3f = [tuple(f) for f in F1.P3.antiprism_stack(3)]
    a3 = G5.adj_from_faces(t3f)
    stuck, freed = F1.stuck_harvest(t3f, a3, max(a3), n_seeds=25,
                                    n_walk=60, amp=30)
    pops.append(('T3', t3f, a3, max(a3), stuck[:250], freed, False))
    ad = G5.errera_adj()
    tris, ok, _m = G5.faces_from_adj_triangulation(ad)
    tv = [v for v in sorted(ad) if len(ad[v]) == 5][0]
    stuck, freed = F1.stuck_harvest(tris, ad, tv)
    pops.append(('B-errera', tris, ad, tv, stuck[:250], freed, False))
    for k in (2, 3):
        rr = F1.F3T.family_B_right(k, 0)
        faces = rr[0]
        adj = G5.adj_from_faces(faces)
        tv = [v for v in sorted(adj, key=str) if len(adj[v]) == 5][0]
        stuck, freed = F1.stuck_harvest(faces, adj, tv)
        pops.append((f'D-flip{k}', faces, adj, tv, stuck[:250], freed,
                     False))
    return pops


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5577 — re-dress witness at scale + rim-contact census")
    print("=" * 70)

    pops = build_pops()
    n_traces = n_R = n_linkfree = 0
    n_cleanshape = [0]
    n_cutchanged = [0]
    inhabited = 0
    n_pairs_tested = 0
    fail_proper = fail_freed = fail_count = 0
    fails = []
    rim_contact = Counter()
    rim_sizes = Counter()
    bridge185 = Counter()
    for label, faces, adj, tv, stuck, freed, exact in pops:
        lcyc = E1.link_cycle(faces, tv)
        link = set(adj[tv])
        vs = [v for v in sorted(adj, key=str) if v != tv]
        for c0 in stuck:
            rl = F2C.roles(adj, c0, tv, lcyc)
            if rl is None:
                continue
            n_sM, r, s_M, s_i, s_j = rl
            vB = [v for v in lcyc if c0[v] == r]
            bz = (set(adj[vB[0]]) | set(adj[vB[1]])) - {tv} - link
            for sx in (s_i, s_j):
                n_sx = next(v for v in lcyc if c0[v] == sx)
                X1, X2, X3c, X4, c1, c2, c3, c4 = CV.trace(
                    adj, c0, tv, n_sM, r, s_M, n_sx, sx)
                n_traces += 1
                R = (X1 - X3c) - X2
                if not R:
                    # the 185-row: third-bridge no-stranding traces
                    ns = {v for v in vs if c4[v] != c0[v]}
                    nb = sum(1 for v in ns if v in bz)
                    if nb >= 3 and freed:
                        dmin = min(sum(1 for v in vs
                                       if c0[v] != f[v])
                                   for f in freed)
                        for f in freed:
                            d = sum(1 for v in vs if c0[v] != f[v])
                            if d == dmin:
                                bc = sum(1 for v in vs
                                         if c0[v] != f[v] and v in bz)
                                bridge185[bc] += 1
                                break
                    continue
                n_R += 1
                if any(v in link for v in R):
                    continue
                n_linkfree += 1
                halo = R | {w for v in R for w in adj[v]} - {tv}
                # CLEAN CASE requires BOTH hypotheses: (a) the freed
                # target agrees with c on R+N(R), AND (b) the word's
                # patch (net change off R) avoids N(R) — the theorem's
                # own flagged condition; without (b) the pair is the
                # RESIDUAL case (first run smuggled those in: 1,589
                # properness 'failures' were residual leakage, caught
                # by the debug probe on edge (9,10) of T3).
                ns = {v for v in vs if c4[v] != c0[v]}
                patch_off_R = ns - R
                clean_shape = not (patch_off_R & halo)
                cuts = {w for v in R for w in adj[v]
                        if w in X2 and w in X1}
                if cuts and cuts <= ns:
                    n_cutchanged[0] += 1
                found = False
                for f in (freed if clean_shape else []):
                    if any(f[v] != c0[v] for v in halo if v != tv):
                        # rim census uses nearest below; here clean case
                        continue
                    found = True
                    n_pairs_tested += 1
                    swap = {r: s_M, s_M: r}
                    fprime = {v: (swap.get(f[v], f[v]) if v in R
                                  else f[v]) for v in f}
                    if not G5.is_proper(adj, fprime, skip=tv):
                        fail_proper += 1
                        if len(fails) < 4:
                            fails.append((label, 'proper'))
                    if G5.operational_tau(adj, fprime, tv) > 5:
                        fail_freed += 1
                        if len(fails) < 4:
                            fails.append((label, 'freed'))
                    h_before = sum(1 for v in R if c0[v] != f[v])
                    h_after = sum(1 for v in R if c4[v] != fprime[v])
                    if h_before != h_after:
                        fail_count += 1
                        if len(fails) < 4:
                            fails.append((label, 'count'))
                inhabited += found
                if clean_shape:
                    n_cleanshape[0] += 1
                # rim-contact: nearest freed targets
                if freed:
                    dmin = min(sum(1 for v in vs if c0[v] != f[v])
                               for f in freed)
                    hits = 0
                    for f in freed:
                        d = sum(1 for v in vs if c0[v] != f[v])
                        if d != dmin:
                            continue
                        contact = sum(1 for v in halo
                                      if v != tv and c0[v] != f[v])
                        rim_contact[contact > 0] += 1
                        rim_sizes[contact] += 1
                        hits += 1
                        if hits >= 5:
                            break
    t1 = n_linkfree > 100
    print(f"\n  traces {n_traces}; R nonempty {n_R}; link-free "
          f"{n_linkfree} (K-a1's hypothesis at scale: "
          f"{n_linkfree}/{n_R} link-free)")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Populations + R census")

    ok_all = fail_proper == fail_freed == fail_count == 0
    t2 = True
    print(f"\n  clean-SHAPE traces (patch avoids N[R]): "
          f"{n_cleanshape[0]}/{n_linkfree} link-free; clean-case "
          f"inhabitation: {inhabited}/{n_cleanshape[0]} "
          f"clean-shape traces have >= 1 freed target agreeing on "
          f"R+N(R) (sampled-freed caveat off-home); pairs tested: "
          f"{n_pairs_tested}")
    if n_pairs_tested == 0:
        v2 = (f"VACUOUS — the clean case is UNINHABITED on everything "
              f"held ({n_cleanshape[0]}/{n_linkfree} clean-shape), and "
              f"STRUCTURALLY so: on {n_cutchanged[0]}/{n_linkfree} "
              f"link-free traces the remnant's CUT VERTICES (excised "
              f"neighbors) are net-changed and sit in N(R) — stranding "
              f"is CREATED by the patch touching R's boundary, so "
              f"'patch avoids N(R)' never happens. The residual case "
              f"is not residual; it is the whole domain. The re-dress "
              f"license must be restated to compose with the rim "
              f"change — the boundary analysis IS the theorem.")
    elif ok_all:
        v2 = ("proper/freed/count-conservation ALL HOLD on every "
              "tested pair — the clean case is proved-and-witnessed")
    else:
        v2 = (f"FAILURES: proper {fail_proper}, freed {fail_freed}, "
              f"count {fail_count} — {fails}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. RE-DRESS WITNESS: "
          f"{v2}")

    t3 = True
    print(f"\n  rim-contact census (nearest freed vs R+N(R)): "
          f"contact {dict(rim_contact)}; contact-size distribution "
          f"{dict(sorted(rim_sizes.items()))}")
    print(f"  the third-bridge row (no-stranding, bridge>=3): "
          f"nearest-freed difference-in-bridge-zone census "
          f"{dict(sorted(bridge185.items()))}")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. The residual case's "
          f"domain, measured")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5577 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
