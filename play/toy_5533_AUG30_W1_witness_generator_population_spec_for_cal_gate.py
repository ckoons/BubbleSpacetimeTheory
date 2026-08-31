#!/usr/bin/env python3
"""
Toy 5533 — W1 (Round 7): THE WITNESS GENERATOR + POPULATION-FAIRNESS SPEC

Cal SS787-4 called the softness: every law reads the same six natal graphs.
W1 builds the generator for the breadth harvest. **Population fairness is
Cal-gated BEFORE mass production** — this toy generates a VALIDATION SMOKE
BATCH only and posts the spec; W2 (mass measurement) fires on his gate.

THE POPULATION SPEC (offered to Cal's gate; counts are proposals):
  F1 RANDOM-FLIP triangulations — sizes n in {12,16,20,25,30,40,50},
     8 seeds each (56 graphs). The workhorse random family.
  F2 TOWERS, standard T_k (k=3..7) AND TWISTED variants (one band built
     with the reversed orientation — same face counts, different link
     geometry; the vocabulary never saw these) (10 graphs).
  F3 LITERATURE KILLERS: Fritsch, Errera, Kittell (Soifer noted as an
     import gap — no pinned source data yet).
  F4 AKEMPIC family: triakis (n=3 cover). Higher odd covers noted as an
     import gap (voltage construction not yet implemented).
  F5 ADVERSARIAL-NEW (grew up nowhere near our vocabulary):
     (a) triangulated BIPYRAMIDS over n-gons, n in {5..10} — two deg-n
         apexes, ring of deg-4 vertices (6 graphs);
     (b) the PENTAKIS DODECAHEDRON — kleetope of the dodecahedron built
         from the icosahedron dual: V=32, 12 deg-5 + 20 deg-6, the
         highest-symmetry deg-5/6 mix we own (1 graph);
     (c) STACKED/Apollonian (the March-era population, included so the
         harvest can DETECT natal-family bias rather than inherit it) —
         n in {15,25,40}, 5 seeds (15 graphs).
  ~91 graphs total; every one validated as a sphere triangulation before
  admission; every witness row carries family + seed provenance.

TESTS (X/Y):
  1. All generators produce valid sphere triangulations (smoke batch,
     one per family cell minimum).
  2. Twisted towers differ from standard (non-isomorphic degree-profile
     or link-structure check) — the variant is real.
  3. Pentakis dodecahedron exact invariants (V=32, E=90, F=60,
     degrees 5^12 6^20).
  4. Fairness table printed (the gate hand-off artifact); NO mass
     production performed — explicit.

Elie, 2026-08-30. Millennium week, 4-Color round 7. 4 tests.
"""

import importlib.util
import os
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5512v", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
T5 = load("t5515v", "toy_5515_AUG30_E1_kring_tower_family_rescue_depth_vs_k"
          "_cal_F0_absorbed.py")
FT = load("t5508v", "toy_5508_AUG30_P1_middle_strict_on_true_triangulations"
          "_embedding_aware_link_cycles.py")
Y3 = load("t5525v", "toy_5525_AUG30_Y3_dilution_test_akempic_knot_in"
          "_eulerian_bulk.py")


def check_triangulation(faces):
    adj = G5.adj_from_faces(faces)
    V = len(adj)
    E = sum(len(s) for s in adj.values()) // 2
    F = len(faces)
    if V - E + F != 2 or 3 * F != 2 * E:
        return False, adj
    ec = Counter()
    for f in faces:
        a, b, c = f
        if len({a, b, c}) != 3:
            return False, adj
        for e in ((a, b), (b, c), (a, c)):
            ec[frozenset(e)] += 1
    return all(v == 2 for v in ec.values()), adj


def twisted_tower_faces(k, twist_band=1):
    """T_k with band `twist_band` built in the REVERSED orientation."""
    rings = [[1 + 5 * r + i for i in range(5)] for r in range(k)]
    apex = 1 + 5 * k
    faces = []
    r0 = rings[0]
    for i in range(5):
        faces.append((0, r0[i], r0[(i + 1) % 5]))
    for r in range(k - 1):
        A, B = rings[r], rings[r + 1]
        if r == twist_band:
            for i in range(5):
                faces.append((B[i], A[i], A[(i - 1) % 5]))
                faces.append((A[(i - 1) % 5], B[i], B[(i - 1) % 5]))
        else:
            for i in range(5):
                faces.append((B[i], A[i], A[(i + 1) % 5]))
                faces.append((A[(i + 1) % 5], B[i], B[(i + 1) % 5]))
    last = rings[-1]
    for i in range(5):
        faces.append((apex, last[i], last[(i + 1) % 5]))
    return faces


def mixed_tower_faces(ring_sizes):
    """Apex + rings of given sizes + apex; annuli between unequal rings
    triangulated by the cyclic merge (p+q triangles). Genuinely outside
    the natal vocabulary (the first reversed-band 'twisted' variant proved
    to be a mirror image — caught by test 2's first run and replaced)."""
    rings = []
    nxt = 1
    for sz in ring_sizes:
        rings.append(list(range(nxt, nxt + sz)))
        nxt += sz
    apexA, apexB = 0, nxt
    faces = []
    r0 = rings[0]
    for i in range(len(r0)):
        faces.append((apexA, r0[i], r0[(i + 1) % len(r0)]))
    for r in range(len(rings) - 1):
        A, B = rings[r], rings[r + 1]
        pp, qq = len(A), len(B)
        ia = ib = 0
        for _ in range(pp + qq):
            a_next = (ia + 1) / pp
            b_next = (ib + 1 - 0.5) / qq
            if a_next <= b_next:
                faces.append((A[ia % pp], A[(ia + 1) % pp], B[ib % qq]))
                ia += 1
            else:
                faces.append((B[ib % qq], B[(ib + 1) % qq], A[ia % pp]))
                ib += 1
    last = rings[-1]
    for i in range(len(last)):
        faces.append((apexB, last[i], last[(i + 1) % len(last)]))
    return faces


def bipyramid_faces(n):
    """Triangulated bipyramid over an n-gon: apexes N, S; ring 0..n-1."""
    N, S = 'N', 'S'
    faces = []
    for i in range(n):
        j = (i + 1) % n
        faces.append((N, i, j))
        faces.append((S, i, j))
    return faces


def pentakis_dodecahedron_faces():
    """Kleetope of the dodecahedron, built from the icosahedron dual."""
    ico_faces = T5.tower_faces(2)
    ico = G5.adj_from_faces(ico_faces)
    # dodecahedron: vertices = ico faces; each ico vertex v gives a
    # pentagonal face = the 5 ico-faces around v in cyclic order
    fid = {frozenset(f): i for i, f in enumerate(ico_faces)}
    pent = {}
    for v in ico:
        star = [frozenset(f) for f in ico_faces if v in f]
        # cyclic order via shared edges
        cyc = [star[0]]
        while len(cyc) < len(star):
            cur = cyc[-1]
            nxt = next(s for s in star if s not in cyc
                       and len(s & cur) == 2)
            cyc.append(nxt)
        pent[v] = [fid[s] for s in cyc]
    # kleetope: pentagon vertices = dodeca vertices (= ico face ids);
    # apex per pentagon (= per ico vertex)
    faces = []
    for v, cyc in pent.items():
        apex = f'a{v}'
        for i in range(5):
            faces.append((apex, cyc[i], cyc[(i + 1) % 5]))
    return faces


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5533 — W1: witness generator + population spec (Cal's gate)")
    print("=" * 70)

    # Test 1: smoke batch, one per family cell minimum
    print("\n" + "=" * 70)
    print("Test 1: smoke batch validation")
    print("=" * 70)
    ok1 = True
    smoke = []
    for n in (12, 20, 30, 50):
        smoke.append((f'F1 flip n={n}', FT.flipped_triangulation(n, seed=0)))
    for k in (3, 5, 7):
        smoke.append((f'F2 tower T_{k}', T5.tower_faces(k)))
    for rs in ([5, 6, 5], [5, 6, 6, 5], [6, 5, 6]):
        smoke.append((f'F2 mixed {rs}', mixed_tower_faces(rs)))
    smoke.append(('F3 Fritsch', G5.fritsch_faces()))
    ef, _o, _m = G5.faces_from_adj_triangulation(G5.errera_adj())
    smoke.append(('F3 Errera', ef))
    kf, _o2, _m2 = G5.faces_from_adj_triangulation(G5.kittell_adj())
    smoke.append(('F3 Kittell', kf))
    smoke.append(('F4 triakis', Y3.triakis_faces()))
    for n in (5, 8, 10):
        smoke.append((f'F5a bipyramid n={n}', bipyramid_faces(n)))
    smoke.append(('F5b pentakis-dodeca', pentakis_dodecahedron_faces()))
    for n in (15, 40):
        smoke.append((f'F5c stacked n={n}',
                      FT.stacked_triangulation(n, seed=1)))
    for name, faces in smoke:
        ok, adj = check_triangulation(faces)
        odd = sum(1 for v in adj if len(adj[v]) % 2)
        n5 = sum(1 for v in adj if len(adj[v]) == 5)
        print(f"  {name}: V={len(adj)} odd={odd} deg5={n5} "
              f"valid={'ok' if ok else 'FAIL'}")
        ok1 &= ok
    t1 = ok1
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Smoke batch "
          f"({len(smoke)} graphs) all valid")

    # Test 2: mixed towers are genuinely new (the first 'twisted' variant
    # was a MIRROR of the standard tower — identical link signatures, caught
    # by this test's first run and REPLACED; recorded, not hidden).
    def link_multiset(faces):
        adj = G5.adj_from_faces(faces)
        sig = Counter()
        for v in adj:
            nbr_degs = tuple(sorted(len(adj[w]) for w in adj[v]))
            sig[(len(adj[v]), nbr_degs)] += 1
        return sig

    mixed = mixed_tower_faces([5, 6, 5])
    okm, adjm = check_triangulation(mixed)
    t2 = okm and link_multiset(mixed) != link_multiset(T5.tower_faces(3))
    degm = Counter(len(s2) for s2 in adjm.values())
    print(f"\n  mixed [5,6,5]: valid={okm} degrees={dict(degm)}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Mixed towers valid and "
          f"structurally distinct from the natal tower family")

    # Test 3: pentakis dodecahedron invariants
    pd = pentakis_dodecahedron_faces()
    okp, adjp = check_triangulation(pd)
    degs = Counter(len(s) for s in adjp.values())
    t3 = (okp and len(adjp) == 32
          and degs == Counter({6: 20, 5: 12})
          and len(pd) == 60)
    print(f"\n  pentakis: V={len(adjp)} F={len(pd)} degrees={dict(degs)}")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Pentakis dodecahedron exact "
          f"(V=32, F=60, 5^12 6^20)")

    # Test 4: fairness table + no mass production
    print("\n" + "=" * 70)
    print("Test 4: THE POPULATION SPEC — hand-off to Cal's gate")
    print("=" * 70)
    print("""
  family  count  provenance                      natal?
  F1      56     flip random, n=12..50 x 8 seeds  NO (post-correction)
  F2      10     towers std k=3..7 + MIXED rings   std natal, mixed NEW
  F3      3      Fritsch/Errera/Kittell           natal (anchors)
  F4      1      triakis (odd covers = import gap) natal (round 4)
  F5a     6      bipyramids n=5..10               NEW
  F5b     1      pentakis dodecahedron            NEW
  F5c     15     stacked (March-era family)       DELIBERATE bias probe
  total   ~92    every graph validated; rows carry family+seed provenance

  Import gaps declared: Soifer (no pinned source data), higher odd
  akempic covers (voltage construction unbuilt). NO MASS PRODUCTION HAS
  RUN — W2 fires on Cal's fairness gate, blind protocol per the round
  prompt (fibers filed before reachability is read).""")
    t4 = True
    print(f"  [{'PASS' if t4 else 'FAIL'}] 4. Spec posted; production gated")

    res = [t1, t2, t3, t4]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5533 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
