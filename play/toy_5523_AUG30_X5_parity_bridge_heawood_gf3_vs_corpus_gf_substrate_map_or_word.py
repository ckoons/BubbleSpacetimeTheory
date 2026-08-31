#!/usr/bin/env python3
"""
Toy 5523 — X5 (Round 4): CASEY'S PARITY-BRIDGE — map or word?

Pre-registered as a QUESTION with a null outcome allowed (exhibit-the-
forced-map discipline; a shared word banks as a null): is there an ACTUAL
map between the Heawood GF(3) code of a triangulation and the corpus's
GF-substrate code objects, or only the shared words "parity"/"code"?

THE OBJECTS, tabulated from their primary sources:
  - Heawood code (Toy 5518, arXiv 2411.15992): alphabet GF(3) (char 3);
    length F = 2V-4 (graph-dependent); dimension V-3 (measured, 4/4
    witnesses); parity checks = vertex stars; 4CT <=> full-support codeword.
  - Corpus RS substrate (Paper #122, bst_seed.md): alphabet GF(2^g) =
    GF(128) (char 2); block length M_g = 2^g - 1 = 127 (fixed); 7-bit
    symbols; distances the odd integers.
  - Klein/Tait layer (Toy 5514): alphabet Z2 x Z2 on edges (char 2);
    dynamics = XOR-toggle on chain boundaries (exact).

FORCED-MAP CANDIDATES, each tested computationally:
  M1: field embedding GF(3) -> GF(128). Obstruction: characteristic.
  M2: field embedding GF(4) (the natural field carrying Z2xZ2 additively)
      -> GF(128). Obstruction: subfield criterion — GF(2^a) sits in
      GF(2^b) iff a | b; here a=2, b=7, and multiplicatively 3 = |GF(4)*|
      must divide 127 = |GF(128)*| = M_g. 127 = 3*42 + 1.
  M3: parameter matching: Heawood length 2V-4 varies with the graph; RS
      length 127 is a constant of the substrate. No natural transformation
      without choosing V, and no candidate V is forced.
  SHARED ATOM: GF(2) = Z2 embeds in both worlds' additive structures (the
      corpus Z2 bit; any 1-dim F2-subspace of GF(128); the Klein group's
      F2-structure) — a real common atom, but it carries neither the GF(3)
      checks nor the RS distances: an atom, not a map.

TESTS (X/Y):
  1. M1 obstruction verified (char 3 vs char 2 arithmetic).
  2. M2 obstruction verified (3 does not divide 127; 2 does not divide 7 —
     both criteria computed, and the general subfield law spot-verified on
     GF(2),GF(4),GF(8),GF(16),GF(64),GF(128) via multiplicative orders).
  3. Parameter table computed from the artifacts (Heawood dims re-derived
     for the four witnesses; RS parameters from the pinned source).
  4. VERDICT banked: NO forced map exists among the tested candidates —
     the bridge is a SHARED WORD plus one honest GF(2) atom. (This is the
     pre-registered null; it banks as the answer, not as a failure.)

Elie, 2026-08-30. Millennium week, 4-Color round 4. 4 tests.
"""

import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


H = load("t5518", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
         "_stuck_separation.py")
G5 = load("g5512p", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
T5 = load("t5515p", "toy_5515_AUG30_E1_kring_tower_family_rescue_depth_vs_k"
          "_cal_F0_absorbed.py")


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5523 — X5: parity-bridge — map or word?")
    print("=" * 70)

    # Test 1: characteristic obstruction
    print("\n" + "=" * 70)
    print("Test 1: M1 — GF(3) -> char-2 ring homomorphism obstruction")
    print("=" * 70)
    # in GF(3): 1+1+1 = 0; in any char-2 ring: 1+1 = 0 so 1+1+1 = 1
    gf3_three = (1 + 1 + 1) % 3
    char2_three = (1 + 1 + 1) % 2
    t1 = (gf3_three == 0 and char2_three == 1)
    print(f"\n  3·1 in GF(3) = {gf3_three};  3·1 in char 2 = {char2_three}")
    print("  A unital ring hom would need 0 -> 1. None exists.")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. M1 obstructed by "
          f"characteristic")

    # Test 2: subfield obstruction
    print("\n" + "=" * 70)
    print("Test 2: M2 — GF(4) not a subfield of GF(128)")
    print("=" * 70)
    t2a = (127 % 3 != 0)      # |GF(4)*| must divide |GF(128)*|
    t2b = (7 % 2 != 0)        # a | b criterion
    # spot-verify the subfield law via multiplicative orders on 2-power fields
    law_ok = True
    for a in (1, 2, 3):
        for b in (1, 2, 3, 4, 6, 7):
            lhs = (b % a == 0)
            rhs = ((2 ** b - 1) % (2 ** a - 1) == 0)
            if lhs != rhs:
                law_ok = False
    t2 = t2a and t2b and law_ok
    print(f"\n  127 mod 3 = {127 % 3} (must be 0 for GF(4)* -> GF(128)*)")
    print(f"  7 mod 2 = {7 % 2} (a|b subfield criterion, a=2, b=7)")
    print(f"  general law (2^a-1 | 2^b-1 <=> a|b) spot-verified: {law_ok}")
    print("  NOTE the arithmetic irony: the obstruction is M_g = 127 "
          "itself — the substrate's own block length refuses the 4-color "
          "alphabet, because g = 7 is odd/prime.")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. M2 obstructed by the "
          f"subfield lattice")

    # Test 3: parameter table
    print("\n" + "=" * 70)
    print("Test 3: parameter table from the artifacts")
    print("=" * 70)
    fri_faces = G5.fritsch_faces()
    fri = G5.adj_from_faces(fri_faces)
    err = G5.errera_adj()
    err_faces, _o, _m = G5.faces_from_adj_triangulation(err)
    kit = G5.kittell_adj()
    kit_faces, _o2, _m2 = G5.faces_from_adj_triangulation(kit)
    t3g = T5.adj_from_faces(T5.tower_faces(3))
    t3f = T5.tower_faces(3)
    ok3 = True
    print("\n  Heawood codes (alphabet GF(3), checks = vertex stars):")
    for name, faces, adj in [('Fritsch', fri_faces, fri),
                             ('Errera', err_faces, err),
                             ('Kittell', kit_faces, kit),
                             ('T_3', t3f, t3g)]:
        V = len(adj)
        F = len(faces)
        vs = sorted(adj)
        rows = [[1 if v in f else 0 for f in faces] for v in vs]
        rk = H.gf3_rank(rows, F)
        dim = F - rk
        ok3 &= (F == 2 * V - 4 and dim == V - 3)
        print(f"    {name}: length {F} (=2V-4: {F == 2 * V - 4}), "
              f"dim {dim} (=V-3: {dim == V - 3})")
    print("  Corpus RS substrate (pinned, Paper #122 / bst_seed.md): "
          "alphabet GF(128), length 127 (CONSTANT), 7-bit symbols, odd "
          "distances.")
    print("  Klein/Tait: alphabet Z2xZ2 on E = 3V-6 edges, XOR-toggle "
          "dynamics (Toy 5514, exact).")
    print("  Length comparison: Heawood 2V-4 varies (14/30/42/30); RS 127 "
          "fixed. No forced identification of lengths, alphabets, or "
          "check structures.")
    t3 = ok3
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Table computed; structural "
          f"regularities (2V-4, V-3) verified")

    # Test 4: verdict
    print("\n" + "=" * 70)
    print("Test 4: VERDICT")
    print("=" * 70)
    print("""
  NO FORCED MAP. M1 dies by characteristic, M2 by the subfield lattice
  (3 does not divide 127 — the substrate's own Mersenne block length is
  the obstruction), M3 by parameter freedom. What IS shared, honestly:
  one GF(2) atom (the Z2 bit) present in the Klein group's F2-structure,
  in GF(128)'s additive group, and in the corpus's T2488 Z2 spin bit —
  an atom without the checks or distances of either code. The rhyme
  "odd RS distances ~ odd-degree vertices" compares a code metric with
  a graph degree: different objects, no map.

  BANKED AS THE PRE-REGISTERED NULL: the parity-bridge is a shared word
  (plus one shared F2 atom), not a map. Per the exhibit-the-forced-map
  discipline this verdict is the deliverable, not a disappointment —
  and it protects the corpus from a numerology channel that today's
  Rubik/parity excitement could otherwise have opened.""")
    t4 = t1 and t2 and t3
    print(f"  [{'PASS' if t4 else 'FAIL'}] 4. Verdict banked (null)")

    results = [t1, t2, t3, t4]
    passed = sum(results)
    print(f"\n{'=' * 70}")
    print(f"Toy 5523 -- SCORE: {passed}/{len(results)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(results, 1):
        if not r:
            print(f"  Test {i}: FAIL")
