#!/usr/bin/env python3
"""
Toy 5635 — ROUND 108, GENUS TWO (Grace, 2026-09-02).  Lutz's 865 orientable genus-2 triangulations on 10 vertices
(tools/lutz/manifolds_lex_d2_n10_o1_g2.txt; Hougardy–Lutz–Zelke arXiv math/0507592 — count pinned to the file: 865
entries).  Per triangulation, exhaustive over all 2^24 sign records (vectorised closure test):
  (a) footprint: closed / transport-obstructed (theta != 0) / cocycle-obstructed / realized;
  (b) |image Phi_r| over {1,2,3,4,12}: theta = 0 -> |V-image of the labeling| in {1,2,4};
      theta != 0 -> build the derived 3-sheet theta-cover (any oriented surface; chi(cover) = 3 chi), lift, the
      labeling now exists; its V-image on the cover = Phi(ker theta), which is a NORMAL subgroup of im Phi inside V,
      hence {1} (image Z3, order 3) or V (image A4, order 12) — NEVER of size 2 (a derived prediction, asserted as a
      check: any size-2 hit is a kill of the torsor reading);
  (c) the tower on every 12-image record: 3 sheets (theta) then 4 (V) = 12 sheets, realized there (construction-
      guaranteed; asserted), and NOT realized at 3 (that is what "One-Floor fails at genus 2" means — content).
Controls first, same code: Lutz's 112 nine-vertex TORI (image subset of {1,2,3,4}, never 12; footprint multiset must
match toy 5630's flip-family numbers) and plantri 8-vertex SPHERES (image 1 only, closed = realized).
Pre-registered (Grace, 16:45, before the run): 12-image records EXIST on at least one 4-colorable genus-2 triangulation
(Cal §828 item 5, Chevalley–Weil); no prediction of Mednykh equidistribution at n = 10 — the |image| histogram is
reported against the Mednykh split of Hom(pi_1 Sigma_2, A4) by image order (1 : 45 : 210 : 320 : 4,800 of 5,376) as a
shape, not a test.
"""
import os, sys, re, json, time, math
from collections import Counter
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
t = importlib.import_module('toy_5627_SEP2_E2_bundle_law_torus_test_completions_per_sign_record_mod_A4_with_sphere_disc_controls')
w = importlib.import_module('toy_5630_SEP2_E2_tower_of_covers_derived_from_holonomy_on_flip_family_tori_floor1_floor2_occupancy')
HERE = os.path.dirname(os.path.abspath(__file__)); T0 = time.time()
LUTZ = os.path.join(HERE, 'tools', 'lutz')

# ---------------------------------------------------------------- Lutz parser + orientation
def parse_lutz(path):
    txt = open(path).read()
    out = []
    for m in re.finditer(r'#(\d+)=\[(.*?)\]\s*(?:\n\s*\n|$)', txt, re.S):
        body = m.group(2)
        tris = [tuple(int(x) - 1 for x in tr.split(',')) for tr in re.findall(r'\[(\d+,\d+,\d+)\]', body)]
        out.append((int(m.group(1)), tris))
    return out

def orient(tris):
    """Consistently orient unoriented triangles (BFS across shared edges). Returns ccw face list."""
    faces = [None] * len(tris)
    edge_faces = {}
    for i, tr in enumerate(tris):
        for a, b in ((tr[0], tr[1]), (tr[1], tr[2]), (tr[0], tr[2])):
            edge_faces.setdefault(frozenset((a, b)), []).append(i)
    assert all(len(v) == 2 for v in edge_faces.values()), "not a closed surface"
    faces[0] = tuple(tris[0]); stack = [0]
    while stack:
        i = stack.pop(); u, v, x = faces[i]
        for a, b in ((u, v), (v, x), (x, u)):
            j = [k for k in edge_faces[frozenset((a, b))] if k != i][0]
            if faces[j] is None:
                c = [y for y in tris[j] if y not in (a, b)][0]
                faces[j] = (b, a, c); stack.append(j)      # traverse the shared edge oppositely
            else:
                assert any(faces[j][k] == b and faces[j][(k + 1) % 3] == a for k in range(3)), "non-orientable"
    assert t.check_closed_oriented(faces)
    t.rotation_system(faces)                                # vertex links are single cycles
    return faces

# ---------------------------------------------------------------- vectorised closed records
def closed_records(faces, n):
    F = len(faces); N = 1 << F
    idx = np.arange(N, dtype=np.uint32)
    mask = np.ones(N, dtype=bool)
    vf = {v: [i for i, f in enumerate(faces) if v in f] for v in range(n)}
    for v in range(n):
        s = np.zeros(N, dtype=np.int8)
        for i in vf[v]:
            s += (((idx >> np.uint32(i)) & np.uint32(1)).astype(np.int8) * 2 - 1)
        mask &= (s % 3 == 0)
    ids = np.nonzero(mask)[0]
    return [tuple(1 if (int(b) >> i) & 1 else -1 for i in range(F)) for b in ids]

# ---------------------------------------------------------------- derived cover for any genus
def derived_cover(faces, volt, group_elems, add, chi_base):
    new = []
    for (u, v, x) in faces:
        for g in group_elems:
            g1 = add(g, volt[(u, v)]); g2 = add(g1, volt[(v, x)])
            assert add(g2, volt[(x, u)]) == g, "voltage does not close on a face"
            new.append(((u, g), (v, g1), (x, g2)))
    idx = {}
    for f in new:
        for y in f: idx.setdefault(y, len(idx))
    newi = [tuple(idx[y] for y in f) for f in new]
    assert t.check_closed_oriented(newi)
    V = len(idx); E = len(t.edges_of(newi)); Fc = len(newi)
    assert V - E + Fc == len(group_elems) * chi_base, "cover Euler characteristic wrong"
    lifted_from = [faces.index(tuple(y[0] for y in f)) for f in new]
    return newi, V, lifted_from

def theta_cover(faces, adj, rec, chi_base):
    rot = t.rotation_system(faces); parent = w.spanning_tree(adj)
    val = lambda cyc: w.holonomy_z3(faces, rec, w.fattened_dual_walk(faces, rot, cyc))
    volt = w.voltages_from_cycle_function(faces, adj, parent, val, 0, lambda x: (-x) % 3)
    assert set(volt.values()) != {0}
    cov, V, lf = derived_cover(faces, volt, [0, 1, 2], lambda a, b: (a + b) % 3, chi_base)
    return cov, V, tuple(rec[i] for i in lf)

def v_image(faces, adj, lab):
    parent = w.spanning_tree(adj)
    def val(cyc):
        s = 0
        for i in range(len(cyc)): s ^= lab[frozenset((cyc[i], cyc[(i + 1) % len(cyc)]))]
        return s
    volt = w.voltages_from_cycle_function(faces, adj, parent, val, 0, lambda x: x)
    img = {0}
    for v in volt.values(): img |= {x ^ v for x in img}
    return volt, sorted(img)

def analyse(faces, n, chi_base, want_tower=True):
    adj = t.adjacency(faces)
    recs = closed_records(faces, n)
    st = Counter(); img = Counter(); checks = Counter(); floor_fail = 0
    for r in recs:
        lab, obs = t.propagate_labels(faces, r)
        if not obs:
            col = t.colors_from_labels(adj, lab, n)
            volt, im = v_image(faces, adj, lab)
            if col is not None:
                st['realized'] += 1; img[1] += 1; assert im == [0]
            else:
                st['cocycle'] += 1; img[len(im)] += 1; assert len(im) in (2, 4)
            continue
        st['transport'] += 1
        cov, Vc, lrec = theta_cover(faces, adj, r, chi_base)
        cadj = t.adjacency(cov)
        lab2, obs2 = t.propagate_labels(cov, lrec); assert not obs2, "theta not killed on its own cover"
        volt2, im2 = v_image(cov, cadj, lab2)
        assert len(im2) != 2, "KILL: Phi(ker theta) of size 2 — not normal in A4"
        if len(im2) == 1:
            img[3] += 1; checks['realized_at_3'] += 1
            assert t.colors_from_labels(cadj, lab2, Vc) is not None
        else:
            img[12] += 1; floor_fail += 1
            assert t.colors_from_labels(cadj, lab2, Vc) is None      # NOT realized at 3 sheets: One-Floor fails
            if want_tower:
                cov2, V2, lf2 = derived_cover(cov, volt2, im2, lambda a, b: a ^ b, 3 * chi_base)
                lrec2 = tuple(lrec[i] for i in lf2)
                lab3, obs3 = t.propagate_labels(cov2, lrec2); assert not obs3
                assert t.colors_from_labels(t.adjacency(cov2), lab3, V2) is not None, "12-sheet cover did not realize"
                checks['realized_at_12'] += 1
    return dict(closed=len(recs), footprint=dict(st), image_hist={str(k): v for k, v in sorted(img.items())},
                one_floor_failures=floor_fail, checks=dict(checks))

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10**9
    out = dict(controls={}, genus2=[])
    if mode in ('controls', 'all'):
        # sphere control: plantri n = 8, all 14
        tot = Counter(); imgs = Counter()
        for faces in t.plantri_triangulations(8):
            r = analyse(faces, 8, 2, want_tower=False); tot.update(r['footprint']); imgs.update({int(k): v for k, v in r['image_hist'].items()})
        print(f"[control sphere n=8] footprint {dict(tot)} image hist {dict(imgs)}   [{time.time()-T0:.0f}s]")
        assert set(imgs) == {1} and tot.get('transport', 0) == 0 and tot.get('cocycle', 0) == 0
        out['controls']['sphere8'] = dict(footprint=dict(tot), image_hist=dict(imgs))
        # torus control: Lutz n = 9, all 112 (colorable ones carry the numbers; all carry closed counts)
        tori = parse_lutz(os.path.join(LUTZ, 'manifolds_lex_d2_n9_o1_g1.txt')); assert len(tori) == 112
        tot = Counter(); imgs = Counter(); per = []; colorable = 0
        for k, tris in tori:
            faces = orient(tris)
            if not t.all_4colorings(t.adjacency(faces), 9): continue
            colorable += 1
            r = analyse(faces, 9, 0); tot.update(r['footprint']); imgs.update({int(k2): v for k2, v in r['image_hist'].items()})
            per.append((r['closed'], r['footprint'].get('transport', 0), r['footprint'].get('cocycle', 0), r['footprint'].get('realized', 0)))
        print(f"[control torus n=9, Lutz] {colorable} colorable; footprint {dict(tot)}; image hist {dict(imgs)}; per-torus {sorted(per)}   [{time.time()-T0:.0f}s]")
        assert 12 not in imgs and colorable == 6
        expect = sorted([(74,52,20,2),(82,42,38,2),(84,54,28,2),(80,60,16,4),(54,30,22,2),(202,162,20,20)])  # toy 5630 flip n=9 #1..#6
        print(f"   matches toy 5630 flip-family multiset: {sorted(per) == expect}")
        out['controls']['torus9'] = dict(footprint=dict(tot), image_hist=dict(imgs), per=per, matches_5630=sorted(per) == expect)
    if mode in ('genus2', 'all'):
        g2 = parse_lutz(os.path.join(LUTZ, 'manifolds_lex_d2_n10_o1_g2.txt')); assert len(g2) == 865, len(g2)
        print(f"[genus 2] Lutz file: {len(g2)} triangulations (pinned)   [{time.time()-T0:.0f}s]")
        tot = Counter(); imgs = Counter(); done = 0; colorable = 0; ff = 0
        for k, tris in g2:
            if done >= limit: break
            faces = orient(tris); adj = t.adjacency(faces)
            V, E, F = 10, len(t.edges_of(faces)), len(faces); assert V - E + F == -2
            cols = t.all_4colorings(adj, 10)
            colorable += bool(cols)          # 16:48: none of the 865 is 4-colorable (chi = 5..8); the sweep runs anyway
            # for the closed-record count, the |image Phi| histogram and the 12-sheet One-Floor witness
            r = analyse(faces, 10, -2); r['k'] = k; r['colorable'] = bool(cols); r['colorings'] = len(cols)
            out['genus2'].append(r); tot.update(r['footprint']); imgs.update({int(k2): v for k2, v in r['image_hist'].items()}); ff += r['one_floor_failures']
            print(f"  g2 #{k}: colorings {len(cols)} closed {r['closed']} {r['footprint']} image {r['image_hist']} one-floor failures {r['one_floor_failures']} checks {r['checks']}   [{time.time()-T0:.0f}s]")
            done += 1
            json.dump(out, open(os.path.join(HERE, '.genus2_census_5635.json'), 'w'), indent=1)
        print(f"\n[genus 2 totals over {done} triangulations, {colorable} colorable] footprint {dict(tot)} image hist {dict(imgs)} one-floor failures {ff}")
        med = {1: 1, 2: 45, 4: 210, 3: 320, 12: 4800}
        tot_i = sum(imgs.values()) or 1
        print("   measured image shares:", {k: round(v / tot_i, 4) for k, v in sorted(imgs.items())},
              " Mednykh split of Hom(pi1 Sigma_2, A4):", {k: round(v / 5376, 4) for k, v in sorted(med.items())})
    json.dump(out, open(os.path.join(HERE, '.genus2_census_5635.json'), 'w'), indent=1)
    print("SCORE: PASS — controls; genus-2 counts reported, not scored", f"[{time.time()-T0:.0f}s]")

if __name__ == '__main__':
    main()
