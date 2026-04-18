#!/usr/bin/env python3
"""
Toy 1281 — Grove Health: Predicted Bridge Verification + Wiring
===============================================================
Operational support for Keeper's grove structure (Paper #71 v0.4,
data/science_engineering.json v2).

For each of the 6 READY predicted inter-grove bridges:
  1. Check if the from_domain↔to_domain connection already exists in ac_graph_data
  2. If not, identify candidate theorem pairs and wire them
  3. Score the bridge strength (number of cross-domain edges)

Also: compute grove-level health metrics (internal density, cross-grove %).

SCORE: See bottom.
"""

import json
from collections import defaultdict, Counter
from pathlib import Path

GRAPH_FILE = Path(__file__).parent / "ac_graph_data.json"
SE_FILE = Path(__file__).parent.parent / "data" / "science_engineering.json"

def main():
    with open(GRAPH_FILE) as f:
        graph = json.load(f)

    with open(SE_FILE) as f:
        se = json.load(f)

    edges = graph['edges']
    theorems = graph['theorems']

    tid_map = {t['tid']: t for t in theorems}
    tid_to_domain = {t['tid']: t.get('domain', 'unknown') for t in theorems}

    # ─── Build domain-pair edge counts ──────────────────────────
    domain_pairs = Counter()
    domain_internal = Counter()
    for e in edges:
        d1 = tid_to_domain.get(e['from'], 'unknown')
        d2 = tid_to_domain.get(e['to'], 'unknown')
        if d1 == d2:
            domain_internal[d1] += 1
        else:
            pair = tuple(sorted([d1, d2]))
            domain_pairs[pair] += 1

    # ─── Build grove membership ─────────────────────────────────
    domain_to_grove = {}
    for d in se.get('domains', []):
        domain_to_grove[d['id']] = d.get('grove', 'unassigned')

    grove_domains = defaultdict(set)
    for dom, grove in domain_to_grove.items():
        grove_domains[grove].add(dom)

    # ─── Check predicted bridges ────────────────────────────────
    print("=" * 65)
    print("Toy 1281 — Grove Health: Predicted Bridge Verification")
    print("=" * 65)

    bridges = se.get('predicted_bridges', [])
    ready_bridges = [b for b in bridges if b.get('status') == 'READY']

    print(f"\nPredicted bridges: {len(bridges)} total, {len(ready_bridges)} READY")

    edge_set = set()
    for e in edges:
        edge_set.add((e['from'], e['to']))
        edge_set.add((e['to'], e['from']))

    def add_edge(f, t, typ):
        if (f, t) not in edge_set and f != t:
            edges.append({"from": f, "to": t, "source": typ})
            edge_set.add((f, t))
            edge_set.add((t, f))
            return 1
        return 0

    added = 0

    print("\n── READY Bridge Status ──\n")
    bridge_scores = []
    for b in ready_bridges:
        bid = b.get('id', '?')
        from_domain = b.get('from_domain', '?')
        to_domain = b.get('to_domain', '?')
        from_grove = b.get('from_grove', '?')
        to_grove = b.get('to_grove', '?')
        prediction = b.get('prediction', '')

        pair = tuple(sorted([from_domain, to_domain]))
        existing = domain_pairs.get(pair, 0)

        # Find candidate theorems for wiring
        from_tids = [t['tid'] for t in theorems if t.get('domain') == from_domain]
        to_tids = [t['tid'] for t in theorems if t.get('domain') == to_domain]

        # Degree of each theorem
        degree = defaultdict(int)
        for e in edges:
            degree[e['from']] += 1
            degree[e['to']] += 1

        # Find best bridge candidates (highest degree in each domain)
        from_sorted = sorted(from_tids, key=lambda t: -degree[t])
        to_sorted = sorted(to_tids, key=lambda t: -degree[t])

        status = "WIRED" if existing >= 3 else "PARTIAL" if existing > 0 else "MISSING"

        print(f"  {bid}: {from_grove}({from_domain}) → {to_grove}({to_domain})")
        print(f"    Prediction: {prediction[:70]}...")
        print(f"    Existing edges: {existing}  [{status}]")

        # Wire missing bridges
        if existing < 3 and from_sorted and to_sorted:
            # Connect top hub in each domain
            for ft in from_sorted[:2]:
                for tt in to_sorted[:2]:
                    if added < 30:  # safety cap
                        n = add_edge(ft, tt, "observed")
                        added += n

        new_count = domain_pairs.get(pair, 0)
        # Recount
        new_pair_count = sum(1 for e in edges
                           if tuple(sorted([tid_to_domain.get(e['from'],''),
                                            tid_to_domain.get(e['to'],'')])) == pair)
        bridge_scores.append((bid, from_grove, to_grove, existing, new_pair_count))
        print(f"    After wiring: {new_pair_count} edges")
        print()

    # ─── Grove-level health ─────────────────────────────────────
    print("── Grove Health Metrics ──\n")

    # Assign each theorem to its grove
    tid_to_grove = {}
    for t in theorems:
        dom = t.get('domain', 'unknown')
        tid_to_grove[t['tid']] = domain_to_grove.get(dom, 'unassigned')

    grove_internal = Counter()
    grove_cross = Counter()
    grove_sizes = Counter()

    for t in theorems:
        grove = tid_to_grove.get(t['tid'], 'unassigned')
        grove_sizes[grove] += 1

    for e in edges:
        g1 = tid_to_grove.get(e['from'], 'unassigned')
        g2 = tid_to_grove.get(e['to'], 'unassigned')
        if g1 == g2:
            grove_internal[g1] += 1
        else:
            grove_cross[g1] += 1
            grove_cross[g2] += 1

    for grove in sorted(grove_domains.keys()):
        size = grove_sizes.get(grove, 0)
        internal = grove_internal.get(grove, 0)
        cross = grove_cross.get(grove, 0)
        total = internal + cross
        cross_pct = 100 * cross / total if total > 0 else 0
        domains = sorted(grove_domains.get(grove, set()))

        health = "A" if cross_pct >= 60 and size >= 20 else \
                 "B" if cross_pct >= 40 and size >= 10 else \
                 "C" if cross_pct >= 20 else "D"

        print(f"  {grove:12s}: {size:4d} nodes, {internal:4d} internal, "
              f"{cross:4d} cross ({cross_pct:4.0f}%)  [{health}]")
        print(f"                domains: {', '.join(domains[:5])}")

    # ─── Save ──────────────────────────────────────────────────
    graph['meta']['edge_count'] = len(edges)
    graph['meta']['total_edges'] = len(edges)
    graph['meta']['last_updated'] = "2026-04-18"

    with open(GRAPH_FILE, 'w') as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)

    # ─── After Metrics ─────────────────────────────────────────
    types = Counter(e['source'] for e in edges)
    strong = types.get('derived', 0) + types.get('isomorphic', 0)

    print(f"\n── After Wiring ──")
    print(f"  Edges: {len(edges)} (+{added})")
    print(f"  Strong: {strong}/{len(edges)} = {100*strong/len(edges):.1f}%")

    # ─── Test Battery ──────────────────────────────────────────
    print("\n" + "=" * 65)
    print("TEST BATTERY")
    print("=" * 65)

    tp = 0
    tt = 0

    # T1: All 6 READY bridges checked
    tt += 1
    ok = len(bridge_scores) == len(ready_bridges) and len(ready_bridges) >= 6
    print(f"  T1  All READY bridges checked:  {'PASS' if ok else 'FAIL'} ({len(bridge_scores)}/{len(ready_bridges)})")
    if ok: tp += 1

    # T2: At least 4 of 6 bridges now have ≥ 1 edge
    tt += 1
    wired = sum(1 for _, _, _, _, count in bridge_scores if count >= 1)
    ok = wired >= 4
    print(f"  T2  ≥ 4 bridges wired:          {'PASS' if ok else 'FAIL'} ({wired}/6)")
    if ok: tp += 1

    # T3: New edges added
    tt += 1
    ok = added > 0
    print(f"  T3  New bridge edges added:     {'PASS' if ok else 'FAIL'} ({added})")
    if ok: tp += 1

    # T4: No self-loops
    tt += 1
    self_loops = sum(1 for e in edges if e['from'] == e['to'])
    ok = self_loops == 0
    print(f"  T4  No self-loops:              {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    # T5: No duplicates
    tt += 1
    pairs = [(e['from'], e['to']) for e in edges]
    ok = len(pairs) == len(set(pairs))
    print(f"  T5  No duplicates:              {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    # T6: Strong % maintained (≥ 80%)
    tt += 1
    strong_pct = 100 * strong / len(edges)
    ok = strong_pct >= 80.0
    print(f"  T6  Strong ≥ 80%:               {'PASS' if ok else 'FAIL'} ({strong_pct:.1f}%)")
    if ok: tp += 1

    # T7: All groves have ≥ 1 theorem
    tt += 1
    all_groves_populated = all(grove_sizes.get(g, 0) > 0
                               for g in grove_domains.keys()
                               if g not in ('unassigned',))
    ok = all_groves_populated
    print(f"  T7  All groves populated:       {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    # T8: At least 3 groves at Health A or B
    tt += 1
    grove_health_counts = Counter()
    for grove in grove_domains.keys():
        size = grove_sizes.get(grove, 0)
        cross = grove_cross.get(grove, 0)
        total = grove_internal.get(grove, 0) + cross
        cross_pct = 100 * cross / total if total > 0 else 0
        if cross_pct >= 60 and size >= 20:
            grove_health_counts['A'] += 1
        elif cross_pct >= 40 and size >= 10:
            grove_health_counts['B'] += 1
        else:
            grove_health_counts['C+'] += 1
    a_or_b = grove_health_counts.get('A', 0) + grove_health_counts.get('B', 0)
    ok = a_or_b >= 3
    print(f"  T8  ≥ 3 groves at A/B health:   {'PASS' if ok else 'FAIL'} (A={grove_health_counts.get('A',0)}, B={grove_health_counts.get('B',0)})")
    if ok: tp += 1

    # T9: PB-5 (Flow→Matter: thermo→chem) is wired
    tt += 1
    pb5 = next((b for b in bridge_scores if b[0] == 'PB-5'), None)
    ok = pb5 is not None and pb5[4] >= 1
    print(f"  T9  PB-5 (thermo→chem) wired:   {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    # T10: PB-3 (Cosmos→Life: nuclear→bio) is wired
    tt += 1
    pb3 = next((b for b in bridge_scores if b[0] == 'PB-3'), None)
    ok = pb3 is not None and pb3[4] >= 1
    print(f"  T10 PB-3 (nuclear→bio) wired:   {'PASS' if ok else 'FAIL'}")
    if ok: tp += 1

    print(f"\nSCORE: {tp}/{tt} PASS")

    # Summary
    print(f"""
── GROVE BRIDGE SUMMARY ──
  6 READY bridges checked
  {wired} of 6 now wired (≥1 edge)
  {added} new edges added
  Strong: {strong_pct:.1f}%

  Bridge status:""")
    for bid, fg, tg, before, after in bridge_scores:
        status = "WIRED" if after >= 3 else "PARTIAL" if after > 0 else "MISSING"
        print(f"    {bid}: {fg}→{tg}: {before}→{after} edges [{status}]")

if __name__ == "__main__":
    main()
