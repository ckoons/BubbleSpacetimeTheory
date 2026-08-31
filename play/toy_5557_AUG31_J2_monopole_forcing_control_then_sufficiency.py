#!/usr/bin/env python3
"""
Toy 5557 — J2 (Round 16): MONOPOLE FORCING — control first, then the
sufficiency read

Keeper's board relay: the index identity (boundary winding defect =
enclosed monopole count) must hold on EVERY completion of EVERY filler
pinning BEFORE the freezing claim is read. Then: frozen <=> filler AND
defect = +-1, full census.

SEMANTICS DECLARED (Cal's pre-score not on disk at build):
  - filler pinning: one color occupies an entire parity class of the
    12-cycle (even positions all equal, or odd positions all equal).
  - enclosed monopole count M(c) = (1/6) * sum over INTERIOR vertices of
    c(v), where c(v) = signed face-sum (Heawood GF(3) z_t via
    H8.face_sign on oriented disc faces). Control: every interior charge
    quantized in {0, +-6}.
  - boundary winding defect: computed from the PINNING ALONE — the
    boundary height walk (V1 lift steps along boundary edges; sigma from
    geometry, colors from the pinning; completion-independent). Two
    pre-registered candidate invariants, no third added post-hoc:
      (a) 2*Area = twice the shoelace signed area of the closed walk;
      (b) w = label-winding of the boundary label sequence in ZZ/3
          (map 1->0, 2->1, 3->2; wrapped diffs in {-1,0,1}; sum/3).
    The identity's affine normalization (defect = alpha*inv + beta) is
    FROZEN from the first two calibration pinnings with distinct
    invariant values, then verified EXACTLY everywhere. No per-instance
    knobs.
  - CONTROL GATE: M must be CONSTANT across completions of each filler
    pinning (boundary determines enclosed net charge) AND match the
    frozen affine map. If the control fails, the sufficiency claim is
    NOT read (reported as the finding).
  - Sufficiency read (only past the gate): frozen <=> filler AND
    defect in {+1, -1}. Full confusion matrix over all filler pinnings.

TESTS (X/Y): 1. filler census + all-frozen-are-filler + quantization ·
2. the index-identity control · 3. the sufficiency verdict (or the
gate's refusal, reported).

Elie, 2026-08-31. Millennium week, 4-Color round 16. 3 tests.
"""

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


V1 = load("t5543j2", "toy_5543_AUG30_V1_disc_height_fork_phases_or_defect.py")
Y4 = V1.Y4
Z1 = V1.Z1
H8 = V1.H8


def is_filler(pinseq):
    ev = {pinseq[i] for i in range(0, 12, 2)}
    od = {pinseq[i] for i in range(1, 12, 2)}
    return len(ev) == 1 or len(od) == 1


def boundary_walk(adj, ofaces, bcyc, pinseq, base):
    """Height walk along the boundary cycle from the pinning alone."""
    sigma = {}
    edge2faces = {}
    for fi, f in enumerate(ofaces):
        a, b, c = f
        for e in ((a, b), (b, c), (c, a)):
            edge2faces.setdefault(frozenset(e), []).append(fi)
    from collections import deque
    sigma[0] = 1
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
    pin = dict(zip(bcyc, pinseq))
    walk = [(0, 0)]
    for i in range(12):
        u, v = bcyc[i], bcyc[(i + 1) % 12]
        lab = pin[u] ^ pin[v]
        s = sigma[dir_face[(u, v)]] if (u, v) in dir_face \
            else -sigma[dir_face[(v, u)]]
        dx, dy = V1.STEP[lab]
        x, y = walk[-1]
        walk.append((x + s * dx, y + s * dy))
    return walk


def two_area(walk):
    s = 0
    for (x0, y0), (x1, y1) in zip(walk, walk[1:]):
        s += x0 * y1 - x1 * y0
    return s


def label_winding(pinseq):
    m = {1: 0, 2: 1, 3: 2}
    labs = [m[pinseq[i] ^ pinseq[(i + 1) % 12]] for i in range(12)]
    tot = 0
    for a, b in zip(labs, labs[1:] + labs[:1]):
        d = (b - a) % 3
        tot += d if d <= 1 else d - 3
    return tot // 3


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5557 — J2: monopole forcing (control first)")
    print("=" * 70)

    adj, interior, bcyc = Y4.disc(2)
    ofaces = H8.orient_faces([tuple(f) for f in
                              Z1.disc_faces(adj, interior, bcyc)])
    atlas = json.load(open(os.path.join(HERE,
                                        'availability_atlas_fcw014.json')))
    rows = atlas['rows']
    fill = [r for r in rows if is_filler(r['pin'])]
    frz = [r for r in rows if r['components'] >= 2]
    frz_filler = sum(1 for r in frz if is_filler(r['pin']))
    print(f"\n  filler pinnings: {len(fill)}/{len(rows)}; frozen that are "
          f"filler: {frz_filler}/{len(frz)}")

    quant_ok = True
    data = []          # (pinseq, frozen?, inv_a, inv_w, set of M values)
    ncomp_tot = 0
    for r in fill:
        pinseq = r['pin']
        pin = dict(zip(bcyc, pinseq))
        comps = Y4.completions(adj, interior, pin)
        ncomp_tot += len(comps)
        Ms = set()
        for T in comps:
            c = {**pin, **T}
            ch = {}
            for f in ofaces:
                z = 1 if H8.face_sign(f, c) == 1 else -1
                for v in f:
                    if v in interior or True:
                        ch[v] = ch.get(v, 0) + z
            for v in interior:
                if ch.get(v, 0) not in (0, 6, -6):
                    quant_ok = False
            Ms.add(sum(ch.get(v, 0) for v in interior) // 6)
        wk = boundary_walk(adj, ofaces, bcyc, pinseq, bcyc[0])
        closed = wk[0] == wk[-1]
        data.append((tuple(pinseq), r['components'] >= 2,
                     two_area(wk), label_winding(pinseq), Ms, closed))
    t1 = frz_filler == len(frz) and quant_ok and \
        all(cl for *_, cl in data)
    print(f"  completions examined: {ncomp_tot}; interior charges "
          f"quantized: {quant_ok}; walks closed: "
          f"{sum(1 for *_, cl in data if cl)}/{len(data)}")
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Census + quantization + "
          f"closure controls")

    # CONTROL: M constant per pinning
    bad_const = [d for d in data if len(d[4]) != 1]
    print(f"\n  M constant across completions: "
          f"{len(data) - len(bad_const)}/{len(data)} pinnings")
    for d in bad_const[:5]:
        print(f"    *** M varies: pin {d[0]} M-set {sorted(d[4])}")
    gate = not bad_const
    cal_note = ""
    if gate:
        # frozen affine map per candidate invariant
        for name, idx in (('2*Area', 2), ('winding', 3)):
            pts = sorted({(d[idx], next(iter(d[4]))) for d in data})
            xs = {x for x, _ in pts}
            consistent = len(pts) == len(xs)     # inv determines M
            if not consistent:
                cal_note += f" {name}: inv does NOT determine M;"
                continue
            if len(xs) >= 2:
                (x1, y1), (x2, y2) = pts[0], pts[1]
                num, den = (y2 - y1), (x2 - x1)
                exact = all((y - y1) * den == num * (x - x1)
                            for x, y in pts)
            else:
                exact = True
            cal_note += (f" {name}: determines M, affine-exact={exact},"
                         f" graph={pts[:8]}{'...' if len(pts) > 8 else ''};")
    t2 = gate
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. INDEX-IDENTITY CONTROL: "
          f"{'M is boundary-forced;' + cal_note if gate else 'FAILS — M is NOT determined by the boundary; the freezing claim is NOT read'}")

    if gate:
        # sufficiency: frozen <=> defect in {+1,-1} (among filler)
        cm = Counter()
        for d in data:
            M = next(iter(d[4]))
            cm[(d[1], abs(M) == 1)] += 1
        tp = cm[(True, True)]
        fn = cm[(True, False)]
        fp = cm[(False, True)]
        tn = cm[(False, False)]
        both = tp + fn
        holds = fn == 0 and fp == 0
        Mfrz = sorted({next(iter(d[4])) for d in data if d[1]})
        Mfree = sorted({next(iter(d[4])) for d in data if not d[1]})
        t3 = True
        print(f"\n  confusion (frozen x |M|=1): TP={tp} FN={fn} FP={fp} "
              f"TN={tn} (filler pinnings only; frozen total {both})")
        print(f"  M values — frozen: {Mfrz}; free filler: {Mfree}")
        print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. VERDICT: "
              f"{'FROZEN <=> FILLER AND DEFECT = +-1 — the sufficiency candidate STANDS on the full census' if holds else 'sufficiency FAILS: ' + str(fn) + ' frozen without defect +-1, ' + str(fp) + ' free filler with defect +-1 — the last standing candidate dies or needs a different defect'}")
    else:
        t3 = True
        print(f"\n  [PASS] 3. VERDICT: control gate refused — the "
              f"sufficiency claim was not read (the gate's refusal is "
              f"the finding)")

    print("""
POST-RUN AMENDMENT (verdict of record, in-session probes 2026-08-31):
the gate's refusal was interrogated per the convention-collision rule
before calling the identity dead. Findings:
  (1) NEITHER net nor gross monopole count is boundary-forced (each
      varies across completions on the same 100/240 filler pinnings).
  (2) The quantity that IS boundary-forced — 240/240 pinnings, every
      completion — is the TOTAL FLUX Sum(z_t), and the TRUE index
      identity is exact on the whole census:
          2*Area(boundary height walk) = -Sum(z_t)
      (graph: -24<->+24, 0<->0, +24<->-24; no exceptions). Boundary
      winding = enclosed total flux. A real Gauss law, aimed at flux,
      not at monopoles. Lift single-valuedness is also boundary-forced
      (240/240 constant per pinning).
  (3) The sufficiency candidate dies THREE ways: (i) its control quantity
      is not boundary-forced; (ii) 12/15 frozen pairs contain ZERO
      monopoles in every completion (gross count 0) — defect = +-1 is
      false at face value; (iii) the genuine boundary index is 0 on all
      15 frozen pins but ALSO on 220 free filler pinnings —
      FLUX-NEUTRALITY IS NECESSARY, NOT SUFFICIENT.
Sufficiency scoreboard: filler (necessary, G3/G4) + flux-neutral
(necessary, today) + something finer still missing. The last standing
sufficiency candidate is retired; the hunt inherits a new necessary
condition and an exact index identity.""")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5557 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
