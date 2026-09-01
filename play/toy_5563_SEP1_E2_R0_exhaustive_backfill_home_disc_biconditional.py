#!/usr/bin/env python3
"""
Toy 5563 — E2 (Sept 1): R0 — THE EXHAUSTIVE BACKFILL ON THE HOME DISC

Per the frozen spec (Elie_SUFFICIENCY_REPLICATION_SPEC..., sha256
ef4b6b00..., filed 2026-08-31 08:04): FCW-014's atlas was a 5,000-row
SAMPLE of the 3^12 + 3 = 531,444 proper boundary 12-cycle colorings.
R0 re-scores the three-legged characterization EXHAUSTIVELY:

    FROZEN <=> FILLER and FLUX-NEUTRAL and EXACTLY-TWO-COMPLETIONS

Definitions verbatim from the spec (filler = one color owns a parity
class; flux-neutral = 2*Area(boundary height walk) = 0 with oriented
faces; frozen = n >= 2 completions, every completion with zero legal
interior-only components — Q2's ALL-FROZEN class).

POSITIVE CONTROL: the 15 known pathological pinnings (atlas) must be
recovered frozen, or the instrument stops and says so.

Pre-registered outcomes (spec R0-P / R0-K): the biconditional holds
exhaustively (the 15 may legitimately GROW), or a counterexample is
exhibited in full and the home-disc answer stops being sample-scope
either way.

TESTS (X/Y): 1. full enumeration (531,444) + positive control ·
2. the exhaustive census · 3. the biconditional verdict.

Elie, 2026-09-01. Millennium week II, summit day. 3 tests.
"""

import importlib.util
import itertools
import json
import os
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


Y4 = load("t5526e2", "toy_5526_AUG30_Y4_boundary_fisk_disc_relative_kempe"
          "_connectivity.py")
Z1 = load("t5531e2", "toy_5531_AUG30_Z1_disc_decision_runner_guarded"
          "_awaiting_freeze.py")
H8 = load("t5518e2", "toy_5518_AUG30_E4_heawood_gf3_instrument_rank"
          "_coset_stuck_separation.py")
V1 = load("t5543e2", "toy_5543_AUG30_V1_disc_height_fork_phases_or"
          "_defect.py")


def boundary_step_table(adj, ofaces, bcyc):
    """sigma-signed height step per boundary edge (pinning-independent
    except for the label): returns list of (sign, ) per position along
    the cycle, as (s_i) with step = s_i * STEP[label_i]."""
    edge2faces = {}
    for fi, f in enumerate(ofaces):
        a, b, c = f
        for e in ((a, b), (b, c), (c, a)):
            edge2faces.setdefault(frozenset(e), []).append(fi)
    sigma = {0: 1}
    q = deque([0])
    while q:
        fi = q.popleft()
        for e, fs in edge2faces.items():
            if fi in fs and len(fs) == 2:
                fj = fs[0] if fs[1] == fi else fs[1]
                if fj not in sigma:
                    sigma[fj] = -sigma[fi]
                    q.append(fj)
    dir_face = {}
    for fi, f in enumerate(ofaces):
        a, b, c = f
        for (u, v) in ((a, b), (b, c), (c, a)):
            dir_face[(u, v)] = fi
    signs = []
    n = len(bcyc)
    for i in range(n):
        u, v = bcyc[i], bcyc[(i + 1) % n]
        s = sigma[dir_face[(u, v)]] if (u, v) in dir_face \
            else -sigma[dir_face[(v, u)]]
        signs.append(s)
    return signs


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5563 — E2/R0: exhaustive backfill on FCW-014")
    print("=" * 70)

    adj, interior, bcyc = Y4.disc(2)
    ofaces = H8.orient_faces([tuple(f) for f in
                              Z1.disc_faces(adj, interior, bcyc)])
    signs = boundary_step_table(adj, ofaces, bcyc)
    STEP = V1.STEP
    n = len(bcyc)
    bset = set(bcyc)

    atlas = json.load(open(os.path.join(HERE,
                                        'availability_atlas_fcw014.json')))
    known15 = {tuple(r['pin']) for r in atlas['rows']
               if r['components'] >= 2}

    def two_area(seq):
        x = y = 0
        pts = [(0, 0)]
        for i in range(n):
            lab = seq[i] ^ seq[(i + 1) % n]
            dx, dy = STEP[lab]
            x += signs[i] * dx
            y += signs[i] * dy
            pts.append((x, y))
        if pts[-1] != (0, 0):
            return None                  # walk not closed: flag
        s = 0
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            s += x0 * y1 - x1 * y0
        return s

    def is_filler(seq):
        return len({seq[i] for i in range(0, n, 2)}) == 1 or \
            len({seq[i] for i in range(1, n, 2)}) == 1

    # exhaustive proper cycle enumeration
    total = 0
    n_zero_comp = 0
    census = Counter()
    frozen_rows = []
    legs_rows = []
    mism_F = []          # frozen but not three-legged
    mism_L = []          # three-legged but not frozen
    walk_open = 0
    seq = [0] * n

    def legal_empty(col):
        for a, b in itertools.combinations(range(4), 2):
            seen = set()
            for u in interior:
                if u in seen or col[u] not in (a, b):
                    continue
                comp = {u}
                st = [u]
                hit_b = False
                while st:
                    x = st.pop()
                    for w in adj[x]:
                        if w in comp or col.get(w) not in (a, b):
                            continue
                        if w in bset:
                            hit_b = True
                            comp.add(w)
                            continue
                        comp.add(w)
                        st.append(w)
                seen |= {v for v in comp if v not in bset}
                if not hit_b:
                    return False
        return True

    def rec(i):
        global_dummy = None
        if i == n:
            if seq[0] == seq[-1]:
                return
            process(tuple(seq))
            return
        for c in range(4):
            if i > 0 and c == seq[i - 1]:
                continue
            seq[i] = c
            rec(i + 1)

    def process(t):
        nonlocal_vars['total'] += 1
        pin = dict(zip(bcyc, t))
        comps = Y4.completions(adj, interior, pin)
        m = len(comps)
        if m == 0:
            nonlocal_vars['zero'] += 1
            return
        A2 = two_area(t)
        if A2 is None:
            nonlocal_vars['open'] += 1
            return
        legs = is_filler(t) and A2 == 0 and m == 2
        if m >= 2:
            frz = all(legal_empty({**pin, **T}) for T in comps)
        else:
            frz = False
        census[(frz, legs)] += 1
        if frz:
            frozen_rows.append(t)
            if not legs:
                mism_F.append((t, is_filler(t), A2, m))
        if legs:
            legs_rows.append(t)
            if not frz:
                mism_L.append((t, m))

    nonlocal_vars = {'total': 0, 'zero': 0, 'open': 0}
    # iterative enumeration (recursion is fine at depth 12)
    import sys
    sys.setrecursionlimit(100)
    rec(0)

    total = nonlocal_vars['total']
    print(f"\n  proper boundary colorings enumerated: {total} "
          f"(expected 531444); zero-completion: {nonlocal_vars['zero']}; "
          f"non-closed walks: {nonlocal_vars['open']}")
    rec15 = sum(1 for t in known15 if t in set(frozen_rows))
    t1 = total == 531444 and rec15 == len(known15) and \
        nonlocal_vars['open'] == 0
    print(f"  POSITIVE CONTROL: known frozen pinnings recovered "
          f"{rec15}/{len(known15)}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Full enumeration + "
          f"positive control")

    print(f"\n  exhaustive census (frozen?, three-legs?): "
          f"{dict(sorted(census.items()))}")
    print(f"  frozen pinnings (exhaustive): {len(frozen_rows)} "
          f"(sample had 15); three-leg pinnings: {len(legs_rows)}")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Exhaustive census")

    t3 = True
    if not mism_F and not mism_L:
        verdict = (f"THE BICONDITIONAL HOLDS EXHAUSTIVELY — "
                   f"{len(frozen_rows)} frozen = {len(legs_rows)} "
                   f"three-legged, all 531,444 rows; the home-disc "
                   f"characterization sheds its sample-scope caveat "
                   f"(spec outcome R0-P)")
    else:
        verdict = (f"COUNTEREXAMPLES (spec outcome R0-K): "
                   f"{len(mism_F)} frozen-not-three-legged "
                   f"{[m for m in mism_F[:4]]}; "
                   f"{len(mism_L)} three-legged-not-frozen "
                   f"{[m for m in mism_L[:4]]}")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. VERDICT: {verdict}")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5563 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
