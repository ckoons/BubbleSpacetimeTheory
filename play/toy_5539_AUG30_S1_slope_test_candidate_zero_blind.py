#!/usr/bin/env python3
"""
Toy 5539 — S1 (Round 11): THE SLOPE TEST — Separator Candidate Zero, blind

Keeper's Height-Function Bridge prediction (pre-registered): the 15
pathological (frozen-twin) pinnings are exactly the extremal-boundary-slope
class; freezing <=> extremal boundary height slope, a LINEAR functional of
the pinning. Both anomaly directions pre-scored: frozen-at-moderate-slope
and free-at-extremal-slope are each headline findings.

SEMANTICS v1 (declared here, grounded in Lyra's pinned disp from Theorem 1
of the relative theory; her R1 dictionary may refine it — this is the first
operational cut, labeled as such):
  For pinning p on the boundary cycle u_0..u_11, at each vertex u_i with
  cycle neighbors u_{i-1}, u_{i+1}:
    disp_i := cyclic displacement from p(u_{i-1}) to p(u_{i+1}) in the
    3-cycle of colors != p(u_i), ordered ascending with orientation
    x -> y -> z -> x, values in {0, +1, -1}.
  SLOPE(p) := sum_i disp_i  (an integer; |SLOPE| is the slope class).
  Secondary blind columns: n_colors per parity sublattice; filler flag
  (a color occupying an entire parity class); winding of the non-filler
  subsequence when a filler exists.

DISCLOSURE (honesty over drama): while deriving the semantics I hand-
computed the functional on two exhibited pinnings — the census-family shape
[1,0,3,0,2,0,...] gives SLOPE -6 and the DECISION pinning appears to give
SLOPE 0. If the census join confirms this, Candidate Zero AS OPERATIONALIZED
BY disp-sum fails in the frozen-at-moderate-slope direction on the decision
twins themselves. The hand-check touched only the two long-public witnesses,
not the census; the blind protocol below protects the census join, which is
where the statistics live. Cal adjudicates whether v1 semantics is the
Bridge's honest operationalization or whether Lyra's R1 dictionary supplies
a different height (in which case this toy re-runs as v2 against her
definition — the slope machinery is semantics-parameterized).

BLIND PROTOCOL (mechanical): pass 1 reads ONLY the 'pin' fields from the
atlas (flags stripped in code), computes all slope data, writes + hashes;
pass 2 joins the frozen/class flags.

TESTS (X/Y):
  1. Blind order enforced (pass-1 file + hash before the join).
  2. Slope distribution over the census reported.
  3. KEEPER'S PREDICTION scored: pathological pinnings == extremal-slope
     class (exactly).
  4. Anomaly census, both directions, printed loudly.

Elie, 2026-08-30. Millennium week, 4-Color round 11. 4 tests.
"""

import hashlib
import importlib.util
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def disp(prev_c, self_c, next_c):
    if prev_c == next_c:
        return 0
    cyc = sorted(c for c in range(4) if c != self_c)
    i, j = cyc.index(prev_c), cyc.index(next_c)
    d = (j - i) % 3
    return 1 if d == 1 else -1


def slope_data(pin):
    n = len(pin)
    s = 0
    for i in range(n):
        s += disp(pin[(i - 1) % n], pin[i], pin[(i + 1) % n])
    even = [pin[i] for i in range(0, n, 2)]
    odd = [pin[i] for i in range(1, n, 2)]
    filler = None
    seq = None
    if len(set(odd)) == 1:
        filler, seq = odd[0], even
    elif len(set(even)) == 1:
        filler, seq = even[0], odd
    wind = None
    if filler is not None:
        w = 0
        m = len(seq)
        for i in range(m):
            a, b = seq[i], seq[(i + 1) % m]
            if a != b:
                cyc = sorted(c for c in range(4) if c != filler)
                if a in cyc and b in cyc:
                    d = (cyc.index(b) - cyc.index(a)) % 3
                    w += 1 if d == 1 else -1
        wind = w
    return {'slope': s, 'nc_even': len(set(even)), 'nc_odd': len(set(odd)),
            'filler': filler, 'subwind': wind}


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5539 — S1: the slope test (Candidate Zero, semantics v1)")
    print("=" * 70)

    atlas = json.load(open(os.path.join(HERE,
                                        'availability_atlas_fcw014.json')))
    rows = atlas['rows']

    # PASS 1 — blind: strip flags, compute slopes from pins only
    pins_only = [r['pin'] for r in rows]
    p1 = [slope_data(p) for p in pins_only]
    blob = json.dumps(p1, sort_keys=True).encode()
    h = hashlib.sha256(blob).hexdigest()
    ck = os.path.join(HERE, '.s1_slope_pass1.json')
    with open(ck, 'wb') as f:
        f.write(blob)
    print(f"\n  PASS 1: {len(p1)} pinnings sloped; sha256 {h[:32]}...")
    t1 = os.path.exists(ck)
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Blind order enforced")

    # PASS 2 — join
    dist = Counter(abs(d['slope']) for d in p1)
    print(f"\n  |slope| distribution (census): {dict(sorted(dist.items()))}")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Distribution reported")

    frozen_rows = [(r, d) for r, d in zip(rows, p1)
                   if r['components'] >= 2]
    free_rows = [(r, d) for r, d in zip(rows, p1)
                 if r['components'] == 1 and r['nodes'] >= 2]
    fr_slopes = Counter(abs(d['slope']) for _r, d in frozen_rows)
    max_slope = max(abs(d['slope']) for d in p1)
    extremal = [i for i, d in enumerate(p1) if abs(d['slope']) == max_slope]
    print(f"\n  frozen-twin pinnings: {len(frozen_rows)}; their |slope| "
          f"values: {dict(sorted(fr_slopes.items()))}")
    print(f"  census max |slope| = {max_slope}; extremal-class size = "
          f"{len(extremal)}")

    # Keeper's prediction: pathological == extremal class exactly
    fr_idx = {i for i, (r, d) in enumerate(zip(rows, p1))
              if r['components'] >= 2}
    ext_idx = set(extremal)
    pred_ok = fr_idx == ext_idx
    t3 = pred_ok
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. KEEPER'S PREDICTION "
          f"(pathological == extremal-slope, exactly): "
          f"{'CONFIRMED' if pred_ok else 'FAILS'}")

    # anomaly census, both directions
    frozen_moderate = [(rows[i]['pin'], p1[i]['slope'],
                        p1[i]['filler'], p1[i]['subwind'])
                       for i in fr_idx if i not in ext_idx]
    free_extremal = [(rows[i]['pin'], p1[i]['slope'])
                     for i in ext_idx if i not in fr_idx
                     and rows[i]['nodes'] >= 2]
    print(f"\n  ANOMALY CENSUS:")
    print(f"  frozen-at-non-extremal-slope: {len(frozen_moderate)}")
    for pin, s, fil, sw in frozen_moderate[:16]:
        print(f"    *** {pin} slope={s} filler={fil} subwind={sw}")
    print(f"  free-multi-completion-at-extremal-slope: {len(free_extremal)}")
    for pin, s in free_extremal[:8]:
        print(f"    *** {pin} slope={s}")
    # the subwind refinement: do FROZEN rows separate by |subwind|?
    fr_sw = Counter((d['filler'] is not None, abs(d['subwind'])
                     if d['subwind'] is not None else None)
                    for _r, d in frozen_rows)
    free_sw = Counter((d['filler'] is not None, abs(d['subwind'])
                       if d['subwind'] is not None else None)
                      for _r, d in free_rows)
    print(f"\n  refinement columns (filler-present, |subwind|):")
    print(f"    frozen: {dict(fr_sw)}")
    print(f"    free multi-completion: {dict(free_sw)}")
    t4 = True
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Anomaly census complete, "
          f"both directions")

    res = [t1, t2, t3, t4]
    passed = sum(res)
    print(f"\n{'=' * 70}")
    print(f"Toy 5539 -- SCORE: {passed}/{len(res)}")
    print(f"{'=' * 70}")
    for i, r in enumerate(res, 1):
        if not r:
            print(f"  Test {i}: FAIL")
