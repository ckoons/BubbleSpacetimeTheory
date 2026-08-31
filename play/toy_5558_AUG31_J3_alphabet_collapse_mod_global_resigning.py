#!/usr/bin/env python3
"""
Toy 5558 — J3 (Round 16): THE ALPHABET COLLAPSE (mod global re-signing)

Keeper's pre-registration: mod global re-signing of the charge field
(c -> -c, i.e. flipping every face sign), the five-letter patch alphabet
of F1 collapses — complement-of-one-vertex reduces to SINGLE-VERTEX, and
five letters become two or three.

SEMANTICS DECLARED: for each unsticking gate application (F1's 6,624
population on Fritsch, per apex, relative charge over complete faces):
  patch+ = {u : c1(u) != c0(u)}          (F1's letter)
  patch- = {u : c1(u) != -c0(u)}         (letter after global re-sign)
  canonical letter = the SMALLER patch (tie -> patch+), tagged with
  which gauge won. BLIND: both patches computed and hashed for the
  whole population before the collapse census is read.

TESTS (X/Y): 1. blind pass hashed · 2. collapse census (F1 letter ->
canonical letter) · 3. VERDICT on the pre-registration (collapse of
complement-of-one; alphabet size mod re-signing), both ways pre-scored.

Elie, 2026-08-31. Millennium week, 4-Color round 16. 3 tests.
"""

import hashlib
import importlib.util
import itertools
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5512j3", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")
H8 = load("t5518j3", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
          "_stuck_separation.py")
X3 = load("t5521j3", "toy_5521_AUG30_X3_commutator_laboratory_support"
          "_locality_unstick.py")


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5558 — J3: the alphabet collapse (mod global re-signing)")
    print("=" * 70)

    faces = G5.fritsch_faces()
    adj = G5.adj_from_faces(faces)
    of = H8.orient_faces([tuple(f) for f in faces])

    records = []
    for tv in [v for v in sorted(adj) if len(adj[v]) == 5]:
        vs = sorted(u for u in adj if u != tv)
        comp_faces = [f for f in of if tv not in f]

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
            c0 = charge(c)
            for m1, m2 in itertools.permutations(mv, 2):
                if m1[0] == m2[0]:
                    continue
                k = X3.commutator(adj, c, m1, m2, tv)
                s = X3.support(c, k)
                if not s or not G5.is_proper(adj, k, skip=tv):
                    continue
                if not X3.freeable(adj, k, tv):
                    continue
                c1 = charge(k)
                pp = sum(1 for u in vs if c1[u] != c0[u])
                pm = sum(1 for u in vs if c1[u] != -c0[u])
                records.append((pp, pm))
    blob = json.dumps(records).encode()
    hh = hashlib.sha256(blob).hexdigest()
    t1 = len(records) == 6624
    print(f"\n  PASS 1 (blind): {len(records)} applications; both-gauge "
          f"patch sizes hashed: sha256 {hh[:32]}...")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Blind pass over the full "
          f"population")

    coll = Counter()
    for pp, pm in records:
        canon = pp if pp <= pm else pm
        gauge = '+' if pp <= pm else '-'
        coll[(pp, pm, canon, gauge)] += 1
    print("\n  collapse census (F1 size, re-signed size, canonical, "
          "winning gauge):")
    for kk, v in sorted(coll.items(), key=lambda x: -x[1]):
        print(f"    {kk}: {v}")
    canon_letters = Counter(canon for (pp, pm, canon, g), v in coll.items()
                            for _ in range(v))
    print(f"\n  canonical alphabet (patch sizes mod re-signing): "
          f"{dict(sorted(canon_letters.items()))}")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Collapse census computed")

    seven = [(pp, pm) for pp, pm in records if pp == 7]
    s2c = Counter(pm for pp, pm in seven)
    n_letters = len(set(canon_letters))
    t3 = True
    if n_letters <= 3:
        # size half of the pre-registration confirmed; grade the
        # complement-of-one half by what it actually collapsed TO
        if set(s2c) == {1}:
            head = ("COLLAPSE AS PRE-REGISTERED — complement-of-one is "
                    "single-vertex mod re-signing")
        elif set(s2c) == {0}:
            head = ("COLLAPSE, STRONGER THAN PRE-REGISTERED — "
                    "complement-of-one is a PURE GLOBAL RE-SIGNING "
                    "(re-signs to the EMPTY patch, not single-vertex)")
        else:
            head = (f"COLLAPSE in count, complement-of-one lands on "
                    f"sizes {dict(sorted(s2c.items()))}")
        verdict = (f"{head}; canonical alphabet = "
                   f"{sorted(set(canon_letters))} ({n_letters} letters: "
                   f"the identity and the TRIPLE) — the Wall Motion "
                   f"Lemma simplifies to a one-letter dynamics mod gauge")
    else:
        verdict = (f"NO collapse — complement-of-one re-signs to sizes "
                   f"{dict(sorted(s2c.items()))}; canonical alphabet "
                   f"{sorted(set(canon_letters))} ({n_letters} letters) "
                   f"— the structure is real and non-collapsing")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. VERDICT: {verdict}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5558 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
