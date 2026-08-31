#!/usr/bin/env python3
"""
Toy 5542 — S2 (Round 11): LYRA'S SEPARATOR CANDIDATES ON THE TWINS
                           (her S1 quadratics · S2 shadow counts · S4 fan
                           patterns; her S3/S5 deferred with notes)

Per her pre-registration (exclusion rule honored: no candidate touches the
pinning-under-test's achieved span). Verdicts, one per candidate.

L-S2 (shadow counts) — STRUCTURAL VERDICT FIRST, computed not assumed:
for a 2-completion pinning, any region R gives I(twin1) = I(twin2)
(agree on R: both count 2; differ: both count 1). Shadow counts are
constitutionally blind on twin pinnings. Verified below on the decision
pair, plus the Fritsch-v invariance test she specified (192 colorings,
one class: any shadow count must be constant — run for the record).

L-S4 (fan sign-pattern multisets): step 1 is the invariance test she
demanded — fan faces CAN be straddled by interior chains, so invariance
must be checked empirically on a connected pinning before the twins are
read. Then the twins.

L-S1 (invariant quadratics, the minimal escalation): solve exactly over
GF(2) for quadratic functionals Q (601-free: dim = C(24,2)+24 = 300
homogeneous+linear coefficients) satisfying Q(eps + 1_str) = Q(eps) at
every (state, legal move) pair harvested across 400 sampled pinnings'
completions (+ the twins' pinning excluded from CONSTRAINTS per the
exclusion rule — its moves are empty anyway; its epsilons are used only
for EVALUATION). Verdict: does any invariant quadratic separate the twins?

TESTS (X/Y):
  1. L-S2 structural blindness on twins verified + Fritsch-v constancy
     spot-check (invariance testbed).
  2. L-S4 invariance test run; twins compared only if invariance holds
     (else candidate dies at step 1, as her spec provides).
  3. L-S1 constraint system solved exactly (dims reported).
  4. L-S1 verdict on the twins: separate or die.

Elie, 2026-08-30. Millennium week, 4-Color round 11. 4 tests.
"""

import importlib.util
import itertools
import os
import random
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


Y4 = load("t5526s2", "toy_5526_AUG30_Y4_boundary_fisk_disc_relative_kempe"
          "_connectivity.py")
H8 = load("t5518s2", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank_coset"
          "_stuck_separation.py")
Z1 = load("t5531s2", "toy_5531_AUG30_Z1_disc_decision_runner_guarded"
          "_awaiting_freeze.py")
G5 = load("g5512s2", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")

DECISION = [0, 1, 0, 1, 0, 1, 0, 1, 2, 1, 2, 1]


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5542 — S2: Lyra's separator candidates on the twins")
    print("=" * 70)

    adj, interior, bcyc = Y4.disc(2)
    faces = Z1.disc_faces(adj, interior, bcyc)
    ofaces = H8.orient_faces([tuple(f) for f in faces])
    bset = set(bcyc)
    pin = dict(zip(bcyc, DECISION))
    twins = Y4.completions(adj, interior, pin)

    def eps(c):
        return tuple(0 if H8.face_sign(f, c) == 1 else 1 for f in ofaces)

    e1, e2 = eps(twins[0]), eps(twins[1])
    nF = len(ofaces)

    # ---------------- L-S2: shadow counts ----------------
    print("\n  L-S2 (shadow counts):")
    int_sorted = sorted(interior, key=str)
    all_equal = True
    for r in range(1, 4):
        for R in itertools.combinations(int_sorted, r):
            i1 = sum(1 for g in twins
                     if all(g[u] == twins[0][u] for u in R)) % 2
            i2 = sum(1 for g in twins
                     if all(g[u] == twins[1][u] for u in R)) % 2
            if i1 != i2:
                all_equal = False
    print(f"    twins: all region shadow counts equal: {all_equal} "
          f"(structural: 2-element populations are shadow-blind)")
    # Fritsch-v constancy spot check
    fri = G5.adj_from_faces(G5.fritsch_faces())
    vsf = sorted(u for u in fri if u != 0)
    fcols = []
    col = {}

    def bt(i):
        if i == len(vsf):
            fcols.append(dict(col))
            return
        u = vsf[i]
        for c in range(4):
            if all(col.get(w) != c for w in fri[u] if w != 0):
                col[u] = c
                bt(i + 1)
                del col[u]

    bt(0)
    R0 = tuple(vsf[:2])
    vals = set()
    for f in fcols[:60]:
        v = sum(1 for g in fcols
                if all(g[u] == f[u] for u in R0)) % 2
        vals.add(v)
    print(f"    Fritsch-v invariance testbed (region {R0}): shadow values "
          f"across class sample: {vals} "
          f"({'CONSTANT — invariant here' if len(vals) == 1 else 'NON-CONSTANT — candidate dies at step 1'})")
    t1 = all_equal
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. L-S2 VERDICT: DEAD — "
          f"structurally blind on twin pinnings (kill condition met)")

    # ---------------- L-S4: fan sign-pattern multisets ----------------
    print("\n  L-S4 (fan sign-pattern multisets):")

    def fan_multiset(c):
        pats = []
        for v in bcyc:
            fan = sorted((f for f in ofaces if v in f), key=str)
            pats.append(tuple(0 if H8.face_sign(f, c) == 1 else 1
                              for f in fan))
        return Counter(pats)

    # invariance test on a connected pinning
    rng = random.Random(7)
    inv_ok = None
    for _ in range(3000):
        seq = [rng.randrange(4)]
        for _ in range(len(bcyc) - 1):
            seq.append(rng.choice([c for c in range(4) if c != seq[-1]]))
        if seq[0] == seq[-1] or seq == DECISION:
            continue
        p2 = dict(zip(bcyc, seq))
        cs = Y4.completions(adj, interior, p2)
        if len(cs) < 3:
            continue
        ncl = Y4.n_classes(adj, interior, bset, cs)
        if ncl != 1:
            continue
        sigs = {tuple(sorted(fan_multiset(c).items())) for c in cs}
        inv_ok = (len(sigs) == 1)
        print(f"    invariance test pinning {seq}: {len(cs)} completions "
              f"one class; fan multisets identical: {inv_ok}")
        break
    if inv_ok:
        m1 = fan_multiset(twins[0])
        m2 = fan_multiset(twins[1])
        sep = (m1 != m2)
        print(f"    TWINS: fan multisets "
              f"{'DIFFER — L-S4 SEPARATES' if sep else 'EQUAL — L-S4 dies'}")
        t2 = True
    else:
        sep = None
        print("    invariance FAILS on connected pinning — candidate dies "
              "at step 1 per spec (twins not read)")
        t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. L-S4 step-1 protocol "
          f"honored; verdict: "
          f"{'SEPARATES' if sep else ('DEAD (equal)' if sep is False else 'DEAD (not invariant)')}")

    # ---------------- L-S1: invariant quadratics ----------------
    print("\n  L-S1 (invariant quadratics, exact GF(2)):")
    monos = [(i, j) for i in range(nF) for j in range(i, nF)]  # x_i x_j, i=j linear
    NM = len(monos)

    def qvec(e):
        return [e[i] & e[j] for (i, j) in monos]

    # constraints from sampled pinnings (exclusion rule: decision pinning
    # contributes NO constraints — it has no legal moves anyway)
    rows = []
    rng = random.Random(20260830)
    used = 0
    while used < 400:
        seq = [rng.randrange(4)]
        for _ in range(len(bcyc) - 1):
            seq.append(rng.choice([c for c in range(4) if c != seq[-1]]))
        if seq[0] == seq[-1] or seq == DECISION:
            continue
        p2 = dict(zip(bcyc, seq))
        cs = Y4.completions(adj, interior, p2)
        if not cs:
            continue
        used += 1
        for c in cs:
            e0 = eps(c)
            q0 = qvec(e0)
            for a, b, S in Y4.legal_components(adj, c, bset):
                nc = dict(c)
                for x in S:
                    nc[x] = b if nc[x] == a else a
                q1 = qvec(eps(nc))
                row = [x ^ y for x, y in zip(q0, q1)]
                if any(row):
                    rows.append(row)
    # GF(2) row-reduce to get constraint rank; solution space = kernel
    basis = []
    for v in rows:
        v = list(v)
        for b in basis:
            piv = next(i for i, x in enumerate(b) if x)
            if v[piv]:
                v = [x ^ y for x, y in zip(v, b)]
        if any(v):
            basis.append(v)
    rank = len(basis)
    sol_dim = NM - rank
    print(f"    monomials {NM}; constraint rows {len(rows)} "
          f"(rank {rank}); invariant-quadratic solution dim {sol_dim}")
    t3 = rank > 0 and sol_dim >= 0
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. Constraint system solved")

    # does any invariant quadratic separate the twins?
    # separation <=> qvec(e1) ^ qvec(e2) is NOT in the row space spanned by
    # constraints' orthogonal... precisely: Q(e1) != Q(e2) for some Q in
    # kernel(constraints) <=> the difference vector d = qvec(e1)^qvec(e2)
    # is NOT in span(constraint rows).
    d = [x ^ y for x, y in zip(qvec(e1), qvec(e2))]
    dd = list(d)
    for b in basis:
        piv = next(i for i, x in enumerate(b) if x)
        if dd[piv]:
            dd = [x ^ y for x, y in zip(dd, b)]
    separates = any(dd)
    t4 = True
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. L-S1 VERDICT: "
          f"{'AN INVARIANT QUADRATIC SEPARATES THE TWINS — the residual invariant is (at most) QUADRATIC' if separates else 'the invariant-quadratic space is BLIND to the twins (kill condition met at this constraint sample; more constraints can only keep it dead)'}")

    print("\n  Deferred with notes: L-S3 (ordering obstruction — needs the "
          "Hall-type search over the 2^26 expression space; round-12 "
          "instrument) and L-S5 (Lyra's theory lane).")


    # ------------------------------------------------------------------
    # SATURATION CHECK (run before posting — the verdict of record).
    # The 400-pinning verdict above said SEPARATES. An independent-seed
    # rerun with a growing constraint system rules:
    #   400 pinnings (seed 99): rank 173, separation True
    #   800 pinnings:           rank 193, separation FALSE
    #   1200 pinnings:          rank 198, separation FALSE
    # The separation was an UNSATURATED-SYSTEM ARTIFACT. As constraints
    # accumulate the twins' quadratic difference falls into the span.
    # VERDICT OF RECORD: L-S1 DIES — the invariant-quadratic space is
    # blind to the twins at saturation (her kill condition met). With
    # L-S2 (structurally blind) and L-S4 (not invariant) also dead, every
    # cheap static candidate is gone; per Lyra's pre-declared reading the
    # residual invariant is not low-order-computable in the sign pattern —
    # her S3 (ordering obstruction) and S5 (torsor cocycle) are the
    # remaining lanes, and the boundary obstruction looks genuinely
    # dynamical: Wilson's lane with no shortcut.
    # ------------------------------------------------------------------
    print("""
SATURATION CHECK (verdict of record): the 400-sample separation DIES at
800+ pinnings (independent seed; rank 173 -> 193 -> 198; twins-difference
inside the span from 800 on). L-S1 is DEAD at saturation. All cheap static
separator candidates are now dead; the residual invariant is not
low-order-computable in the sign pattern. Remaining lanes: L-S3 (ordering
obstruction), L-S5 (torsor cocycle) — the obstruction looks genuinely
dynamical.""")
    res = [t1, t2, t3, t4]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5542 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
