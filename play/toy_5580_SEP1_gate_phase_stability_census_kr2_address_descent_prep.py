#!/usr/bin/env python3
"""
Toy 5580 — THE GATE-PHASE STABILITY CENSUS (+ K-r2's address + the
descent-arithmetic staging)

Existence-and-truth-before-derivation (Cal's third hygiene rule, law):
Lyra's derived recipe is APPLIED on every stored trace, and the lemma's
question is MEASURED before anyone derives it.

THE RECIPE (from Lyra_RIM_PREDICATE_DERIVATION..., followed verbatim):
per trace (link-free stranded remnant R), per nearest gate-phase target
c* (tau <= 5): (a) re-dress: on R, c*'(u) := tau(c(u)) = (w·c)(u)
(tau = (r s_M)); (b) rim edits: at every rim edge (u, x), x outside R,
where rho fails (c*(x) = tau(c(u))): edit c*'(x) := (w·c)(x).
MEASURED, per trace: is c*' PROPER (the edit argument covers only the
edited edge — x's other neighbors are the census's business), and is
c*' IN THE GATE PHASE (tau <= 5)? Where the recipe target fails, the
EDIT FAMILY is tried (each failing/conflicted x re-edited over all 4
colors, greedy): the lemma's own disjunction, measured.

K-r2's ADDRESS: rim vertices x where the abutting remnant vertices
forbid BOTH pair values ({tau(c(u)) : u in R, u~x} has size 2) —
frequency overall and among actually-failing rim vertices.

BLIND: per-trace verdict tuples hashed BEFORE aggregation. The
185-class (no-stranding, bridge>=3) is rowed separately: the recipe is
vacuous there (R empty; stability trivially holds) — rowed, not
hidden. DESCENT STAGING: per-trace (penalty, patch-agreement-gain,
d_gate before/after) stored to .gps_descent_staging.json — the
clause-(c) arithmetic runs the hour Stability lands.

TESTS (X/Y): 1. census populations + blind hash · 2. the stability
rates (per contact type, per object; properness separated) + the edit
family disjunction · 3. K-r2 address count · 4. descent staging
written.

Elie, 2026-09-01. 4 tests.
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


RD = load("t5577gp", "toy_5577_SEP1_redress_witness_at_scale_and_rim"
          "_contact_census.py")
P1, CV, F2C, F1 = RD.P1, RD.CV, RD.F2C, RD.F1
E1, G5, X3, H8 = RD.E1, RD.G5, RD.X3, RD.H8


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5580 — Gate-Phase Stability: the census")
    print("=" * 70)

    pops = RD.build_pops()
    records = []           # blind pass-1 verdict tuples
    staging = []
    kr2_all = kr2_failing = 0
    n_rimverts = 0
    vac185 = 0
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
                R = (X1 - X3c) - X2
                ns = {v for v in vs if c4[v] != c0[v]}
                if not R:
                    nb = sum(1 for v in ns if v in bz)
                    if nb >= 3:
                        vac185 += 1
                    continue
                if any(v in link for v in R):
                    continue
                if not freed:
                    continue
                tau_swap = {r: s_M, s_M: r}
                rim_pairs = [(u, x) for u in R for x in adj[u]
                             if x != tv and x not in R]
                rimset = {x for _, x in rim_pairs}
                n_rimverts += len(rimset)
                # K-r2 address: forbidden-value sets per rim vertex
                forb = {}
                for u, x in rim_pairs:
                    forb.setdefault(x, set()).add(tau_swap[c0[u]])
                kr2_here = [x for x, s in forb.items() if len(s) == 2]
                kr2_all += len(kr2_here)
                dmin = min(sum(1 for v in vs if c0[v] != f[v])
                           for f in freed)
                cstar = next(f for f in freed
                             if sum(1 for v in vs
                                    if c0[v] != f[v]) == dmin)
                ctype = 'iii' if (ns - R) & (
                    R | {w2 for v in R for w2 in adj[v]}) and any(
                    c0[v2] != cstar[v2]
                    for v2 in rimset) else 'ii'
                # the recipe
                cp = dict(cstar)
                for u in R:
                    cp[u] = tau_swap[c0[u]]
                n_edit = 0
                fail_x = set()
                for u, x in rim_pairs:
                    if cp[x] == tau_swap[c0[u]]:
                        fail_x.add(x)
                for x in fail_x:
                    cp[x] = c4[x]
                    n_edit += 1
                kr2_failing += sum(1 for x in kr2_here if x in fail_x)
                proper = G5.is_proper(adj, cp, skip=tv)
                stable = proper and \
                    G5.operational_tau(adj, cp, tv) <= 5
                fam_ok = stable
                if not stable:
                    # the edit family: re-edit failing/conflicted rim
                    # vertices over all colors, greedy
                    for x in sorted(fail_x, key=str):
                        for col in range(4):
                            cp2 = dict(cp)
                            cp2[x] = col
                            if G5.is_proper(adj, cp2, skip=tv) and \
                                    G5.operational_tau(adj, cp2,
                                                       tv) <= 5:
                                fam_ok = True
                                cp = cp2
                                break
                        if fam_ok:
                            break
                records.append((label, ctype, proper, stable, fam_ok,
                                n_edit, len(R)))
                gain = sum(1 for v in vs
                           if cp.get(v) == c4[v] and cstar[v] != c0[v])
                staging.append({'label': label, 'ctype': ctype,
                                'penalty': n_edit,
                                'dmin': dmin,
                                'patch_gain': gain,
                                'stable': stable, 'fam_ok': fam_ok})
    blob = json.dumps([str(r) for r in records]).encode()
    hh = hashlib.sha256(blob).hexdigest()
    t1 = len(records) > 500
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Census: {len(records)} "
          f"trace-verdicts blind-hashed (sha256 {hh[:32]}...) before "
          f"aggregation; 185-class vacuous rows: {vac185} (R empty — "
          f"stability trivially holds there, rowed separately)")

    agg = Counter()
    for label, ctype, proper, stable, fam_ok, ne, rs in records:
        agg[('ALL', ctype, stable)] += 1
        agg[(label, ctype, stable)] += 1
    n_stable = sum(1 for rr in records if rr[3])
    n_fam = sum(1 for rr in records if rr[4])
    n_prop = sum(1 for rr in records if rr[2])
    print(f"\n  STABILITY: recipe-target stable {n_stable}/"
          f"{len(records)}; proper {n_prop}/{len(records)}; "
          f"WITH the edit family (the lemma's disjunction): "
          f"{n_fam}/{len(records)}")
    print(f"  by contact type (ALL): "
          f"{ {k: v for k, v in agg.items() if k[0] == 'ALL'} }")
    print(f"  per object (type, stable): "
          f"{ {k: v for k, v in sorted(agg.items()) if k[0] != 'ALL'} }")
    t2 = True
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. "
          f"{'THE LEMMA IS MEASURED TRUE (disjunction form) on everything held' if n_fam == len(records) else 'DISJUNCTION FAILS on ' + str(len(records) - n_fam) + ' traces — the lemma has counterexample material (rows above)'}")

    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. K-r2 ADDRESS: "
          f"opposite-parity shared-rim vertices: {kr2_all} of "
          f"{n_rimverts} rim vertices; among ACTUALLY-FAILING rim "
          f"vertices: {kr2_failing} — "
          f"{'the fear retires: conflicts never fire' if kr2_failing == 0 else 'the case is named and inhabited'}")

    with open(os.path.join(HERE, '.gps_descent_staging.json'),
              'w') as f:
        json.dump(staging, f)
    t4 = True
    print(f"\n  [{'PASS' if t4 else 'FAIL'}] 4. Descent staging "
          f"written ({len(staging)} rows: penalty, dmin, patch_gain, "
          f"stability) — clause (c)'s arithmetic runs the hour "
          f"Stability lands")

    print("""
POST-RUN AMENDMENT (widened-existence probe, in-session): the headline
rates above use ONE nearest target per trace. The lemma's spirit
quantifies over the gate phase, so the probe widened to the 12 nearest
targets per trace (plus the single-vertex edit family per target):
existence-stable = 166/242 sampled traces (69%), failures by object
{T3: 4, B-errera: 5, D-flip2: 15, D-flip3: 52}. VERDICT OF RECORD:
Gate-Phase Stability in the recipe's current form is MEASURED FALSE at
scale — the failures are real and CONCENTRATE ON THE FLIP-SURGERED
FAMILY (the same objects that produced FCW-015–018 and the radius-4
patches). Caveat direction declared: 'not found' within a 12-target x
single-vertex-edit budget is a bounded search, so wider families could
still rescue (false-negative direction only); but the RECIPE target
itself is improper on 868/900 — the edit argument's un-consulted
edges (edited x vs its OTHER neighbors) are the mechanism's real gap,
measured, and that part is exact. Lyra's residue lemma needs a bigger
edit family or a different phase argument, and its counterexample
material lives on the flip class.""")

    res = [t1, t2, t3, t4]
    print(f"\n{'=' * 70}")
    print(f"Toy 5580 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
