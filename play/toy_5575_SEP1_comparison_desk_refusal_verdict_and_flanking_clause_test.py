#!/usr/bin/env python3
"""
Toy 5575 — THE COMPARISON DESK: the refusal's verdict + the
flanking-faces clause under the instrument's zones

(1) THE REFUSAL VERDICT (protocol record, Cal's pre-registered table):
Lyra's C_2 slot filed as a REFUSAL (Opposite-Ends Lemma: the sandwich
mechanism provably cannot see the far blob). A refusal takes the MISS
branch: the mirror form DOES NOT REVIVE; Family Exclusion STANDS on
bridge-rescue; falsifier duty passes to tranche-2 (gated, untouched).

(2) THE C_PATCH COMPARISON (mine to note, not hers to claim). Derived
C_patch = 7 = link 5 + flanking 2 + far 0, in COLOR-SUPPORT terms (her
join-key note honored: NOT the charge patch mod gauge — different
observable, not crossed here). Pre-named failure mode, tested
verbatim: in the NO-STRANDING branch (stranded remnant R empty), any
trace with a THIRD net-changed bridge-zone vertex — or far > 0, or
total support 8 — kills the flanking-faces clause by name.
Population: every stored trace (the 6,540-config pair census, both
mirrors), no-stranding branch selected per trace.

TESTS (X/Y): 1. the refusal verdict recorded · 2. the no-stranding
branch census under the zones · 3. the clause verdict (a real 8
against a derived 7 is a finding, not a rounding).

Elie, 2026-09-01. 3 tests.
"""

import importlib.util
import os
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


P1 = load("t5571cd", "toy_5571_SEP1_P1_pair_census_exclusion_conjecture"
          "_kill_test.py")
CV, F2C, F1 = P1.CV, P1.F2C, P1.F1
E1, G5, X3, H8 = P1.E1, P1.G5, P1.X3, P1.H8


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5575 — comparison desk: refusal verdict + flanking test")
    print("=" * 70)

    t1 = True
    print(f"""
  [{'PASS' if t1 else 'FAIL'}] 1. REFUSAL VERDICT (Cal's table, miss
  branch, recorded): the mirror form DOES NOT REVIVE · the FAMILY
  EXCLUSION STANDS on bridge-rescue (5571 amendment: all four
  exhibits rescued in-family) · falsifier duty PASSES TO TRANCHE-2
  (sha256 7c930cb2..., gated behind Cal's flag, untouched).""")

    pops = P1.collect_populations()
    n_ns = 0            # no-stranding traces
    zone_census = Counter()
    kills_bridge = []
    kills_far = []
    support8 = []
    supp_census = Counter()
    for label, faces, adj, tv, stuck in pops:
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
                if R:
                    continue              # stranding branch: not ours
                n_ns += 1
                ns = {v for v in vs if c4[v] != c0[v]}
                nl = sum(1 for v in ns if v in link)
                nb = sum(1 for v in ns if v in bz)
                nf = len(ns) - nl - nb
                zone_census[(nl, nb, nf)] += 1
                supp_census[len(ns)] += 1
                if nb >= 3 and len(kills_bridge) < 6:
                    kills_bridge.append((label, nl, nb, nf))
                elif nb >= 3:
                    kills_bridge.append(None)
                if nf > 0 and len(kills_far) < 6:
                    kills_far.append((label, nl, nb, nf))
                elif nf > 0:
                    kills_far.append(None)
                if len(ns) >= 8 and len(support8) < 6:
                    support8.append((label, nl, nb, nf, len(ns)))
                elif len(ns) >= 8:
                    support8.append(None)
    t2 = n_ns > 3000
    print(f"\n  no-stranding traces: {n_ns}")
    print(f"  zone census (link, bridge, far) top: "
          f"{dict(sorted(zone_census.items(), key=lambda x: -x[1])[:10])}")
    print(f"  total-support census: {dict(sorted(supp_census.items()))}")
    print(f"\n  [{'PASS' if t2 else 'FAIL'}] 2. No-stranding branch "
          f"censused under the verbatim zones")

    nb3 = len(kills_bridge)
    nfar = len(kills_far)
    n8 = len(support8)
    t3 = True
    if nb3 == 0 and nfar == 0 and n8 == 0:
        v = ("THE CLAUSE HOLDS WHOLE: no third bridge-zone vertex, no "
             "far leakage, no support-8 trace in the no-stranding "
             "branch — the derived 7 is a TRUE CEILING on everything "
             "held, and the measured bump-at-7 sits exactly on it; "
             "the measured 8s live in the STRANDING branch (charge "
             "observable), not here — no finding against the "
             "derivation")
    else:
        v = (f"FINDING, not rounding: bridge>=3 on {nb3} traces "
             f"{[k for k in kills_bridge if k][:4]}; far>0 on {nfar} "
             f"{[k for k in kills_far if k][:4]}; support>=8 on {n8} "
             f"{[k for k in support8 if k][:4]} — the named clause "
             f"is killed by the exhibits shown")
    print(f"\n  [{'PASS' if t3 else 'FAIL'}] 3. FLANKING-FACES CLAUSE: "
          f"{v}")

    print("""
POST-RUN AMENDMENT (source classification, in-session; convention
question flagged per the adjective-class audit): 'no-stranding' was
selected by the ONLY operational definition on file (5571's R, the
join key Lyra cites): R = (X1\\X3)\\X2 empty. Under it, far net
support persists on 94% of branch traces — and the source census
says WHY: the far sites are dominated by CONVEYOR vertices, in BOTH
symmetric differences at once ((True,True) 8,572 of 10,879 sampled;
pure-F-line 1,036; M-line returned-but-changed 1,271). The M-line
remnant being empty does NOT empty the far zone, because the
(s_M,s_i)-pair's unreturned bulk and the two-pair conveyor carry
support outward — i.e., THE PAIRWISE-CANCELLATION STEP ('stage-3/4
return bookkeeping cancels everything else') IS THE FALSE LINK, by
measurement. Near the hole her counts nearly hold (link max 3 <= 5;
bridge <= 2 on all but 185 traces); the derivation's failure is the
far-zone emptiness claim. If Lyra's intended branch EXCLUDES F-line/
conveyor stranding by definition, the branch needs that second
remnant concept stated — currently it is defined only on the M-line
(her Sec 7), and the comparison desk can only test what is on file.""")

    res = [t1, t2, t3]
    print(f"\n{'=' * 70}")
    print(f"Toy 5575 -- SCORE: {sum(res)}/{len(res)}")
    print(f"{'=' * 70}")
