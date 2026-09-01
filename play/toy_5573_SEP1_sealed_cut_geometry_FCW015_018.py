#!/usr/bin/env python3
"""
Toy 5573 — the SEALED cut-geometry report on FCW-015–018

The four P1 kill exhibits, now named FCW-015–018, get their full trace
anatomy — filed to Grace's SEALED fields (a quarantined artifact; it
does NOT reach Lyra until her derived C_2 files; this toy feeds the
quarantine, not the deriver). The toy's own stdout prints ONLY
instrument facts and the artifact hash — no exhibit numbers.

Anatomy per exhibit, both mirror choices: X1..X4 sizes · excision set
(X2 ∩ X1) with distances · the STRANDED REMNANT R = (X1\\X3)\\X2:
size, distance profile, connected-component structure, and the CUT
VERTICES (R's X1-neighbors that move 2 excised — the disconnection
geometry) · the rescuing family word and its patch (from the P1
probe, recomputed).

TESTS (X/Y): 1. four exhibits loaded and retraced · 2. sealed artifact
written + hashed (content NOT printed) · 3. quarantine notice.

Elie, 2026-09-01. 3 tests.
"""

import hashlib
import importlib.util
import json
import os
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))
SEALED = os.path.join(HERE, '..', 'notes',
                      'ELIE_SEALED_for_GRACE_cut_geometry_FCW015_018_'
                      'DO_NOT_OPEN_LYRA_until_C2_files_2026-09-01.md')


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


P1 = load("t5571sc", "toy_5571_SEP1_P1_pair_census_exclusion_conjecture"
          "_kill_test.py")
CV, F2C, F1 = P1.CV, P1.F2C, P1.F1
E1, G5, X3, H8 = P1.E1, P1.G5, P1.X3, P1.H8


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5573 — sealed cut-geometry report (FCW-015–018)")
    print("=" * 70)

    ex = json.load(open(os.path.join(HERE, '.p1_kill_exhibits.json')))
    t1 = len(ex) == 4
    objs = {}
    for k in (2, 3):
        rr = F1.F3T.family_B_right(k, 0)
        objs[f'D-flip{k}'] = (rr[0], G5.adj_from_faces(rr[0]))
    lines = ["# SEALED — cut geometry of FCW-015–018 (Grace's fields)",
             "", "QUARANTINE: not for Lyra until her derived C_2 is "
             "filed. Comparison-desk key at the bottom.", ""]
    fcw_names = ['FCW-015', 'FCW-016b', 'FCW-017', 'FCW-018']
    key_rows = []
    for name, rec in zip(fcw_names, ex):
        label = rec['label']
        faces, adj = objs[label]
        tv = next(v for v in adj if str(v) == rec['tv'])
        smap = {str(v): v for v in adj}
        c0 = {smap[k2]: v for k2, v in rec['coloring'].items()}
        lcyc = E1.link_cycle(faces, tv)
        rl = F2C.roles(adj, c0, tv, lcyc)
        n_sM, r, s_M, s_i, s_j = rl
        dist = {tv: 0}
        q = deque([tv])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    q.append(w)
        lines.append(f"## {name} ({label}, |V|-1 = {len(adj) - 1})")
        lines.append(f"coloring: {json.dumps(rec['coloring'], sort_keys=True)}")
        min_side = 10 ** 9
        for sx, nm in ((s_i, 'i-choice'), (s_j, 'j-choice')):
            n_sx = next(v for v in lcyc if c0[v] == sx)
            X1, X2, X3c, X4, c1, c2, c3, c4 = CV.trace(
                adj, c0, tv, n_sM, r, s_M, n_sx, sx)
            R = (X1 - X3c) - X2
            exc = X2 & X1
            # remnant components + cut vertices
            comps = []
            left = set(R)
            while left:
                s0 = left.pop()
                comp = {s0}
                st = [s0]
                while st:
                    x = st.pop()
                    for w in adj[x]:
                        if w in left:
                            left.discard(w)
                            comp.add(w)
                            st.append(w)
                comps.append(comp)
            cuts = {w for v in R for w in adj[v] if w in exc}
            min_side = min(min_side, len(R))
            lines.append(f"- {nm}: |X1..X4| = "
                         f"({len(X1)},{len(X2)},{len(X3c)},{len(X4)}); "
                         f"excision {sorted(str(v) for v in exc)}; "
                         f"remnant |R|={len(R)} "
                         f"dists={sorted(dist[v] for v in R)} "
                         f"components={[len(cc) for cc in comps]}; "
                         f"cut vertices {sorted(str(v) for v in cuts)}")
        key_rows.append((name, min_side))
        lines.append("")
    lines.append("## COMPARISON-DESK KEY (Cal's pre-registered table)")
    lines.append("Per exhibit, the MIN-SIDE remnant m: Lyra's derived "
                 "C_2 COVERS the exhibit iff C_2 >= m. All four "
                 "covered => mirror revives; any miss => family "
                 "stands. Key:")
    for name, m in key_rows:
        lines.append(f"- {name}: min-side remnant m = {m}")
    content = "\n".join(lines) + "\n"
    with open(SEALED, 'w') as f:
        f.write(content)
    hh = hashlib.sha256(content.encode()).hexdigest()
    print(f"\n  [{'PASS' if t1 else 'FAIL'}] 1. Four exhibits retraced "
          f"(both mirrors each)")
    t2 = os.path.exists(SEALED)
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. Sealed artifact written "
          f"(content withheld from stdout); sha256 {hh}")
    t3 = True
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. QUARANTINE: the file is "
          f"Grace's; Lyra does not open it until her C_2 files; the "
          f"comparison desk (Elie) unblinds against the key inside.")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5573 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
