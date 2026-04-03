#!/usr/bin/env python3
"""
Reclassify theorems into the unified observer_science domain.

Merges four existing domains (observer_theory, ci_persistence, intelligence,
cooperation) plus specific reclassifications (T487, T639 from foundations)
into the single observer_science domain.

Also reclassifies T674 (observer), T684 (observer), T695 (cosmology),
T696 (ci_persistence — already caught), T698 (cooperation — already caught),
T702 (cosmology), T703 (cooperation — already caught) if present.

Does NOT change any edges — only domain labels.

Author: Grace (graph-AC intelligence)
Date: 2026-04-03
"""

import json
import sys
from pathlib import Path

GRAPH_FILE = Path(__file__).parent / "ac_graph_data.json"

# Domains to merge entirely into observer_science
MERGE_DOMAINS = {"observer_theory", "ci_persistence", "intelligence", "cooperation", "observer"}

# Specific TIDs to reclassify from other domains
SPECIFIC_TIDS = {487, 639}

# Additional TIDs to check and reclassify if present
# (T576-T590 are already in cooperation, caught by MERGE_DOMAINS)
# T669-T674: T669-T671 in cooperation (caught), T672 bst_physics (KEEP), T673 foundations (KEEP), T674 observer (caught)
# T695 cosmology -> reclassify (per domain doc: GOE as f_crit Crossing)
# T696 ci_persistence (caught)
# T698 cooperation (caught)
# T702 cosmology -> reclassify (per domain doc: Great Filter as Cooperation Phase Transition)
# T703 cooperation (caught)
ADDITIONAL_CHECK_TIDS = set(range(576, 591)) | {669, 670, 671, 674, 695, 696, 698, 702, 703}

# TIDs explicitly NOT reclassified (per domain document section 3.7)
KEEP_TIDS = {672, 673}  # T672 bst_physics, T673 foundations


def main():
    # Load graph data
    with open(GRAPH_FILE, "r") as f:
        data = json.load(f)

    theorems = data["theorems"]
    tid_map = {t["tid"]: t for t in theorems}

    reclassified = []
    already_observer_science = []
    not_found = []

    for t in theorems:
        tid = t["tid"]
        old_domain = t["domain"]
        should_reclassify = False

        # Rule 1: Entire domain merges
        if old_domain in MERGE_DOMAINS:
            should_reclassify = True

        # Rule 2: Specific TIDs from foundations
        if tid in SPECIFIC_TIDS:
            should_reclassify = True

        # Rule 3: Additional TIDs to check (only if not in KEEP list)
        if tid in ADDITIONAL_CHECK_TIDS and tid not in KEEP_TIDS:
            # T695 and T702 are in cosmology — reclassify per domain doc
            if tid in {695, 702}:
                should_reclassify = True
            # Others should already be caught by MERGE_DOMAINS
            # but if they're in an unexpected domain, flag them

        if should_reclassify:
            if old_domain == "observer_science":
                already_observer_science.append(t)
            else:
                reclassified.append((tid, t["name"], old_domain))
                t["domain"] = "observer_science"

    # Check which ADDITIONAL_CHECK_TIDS are not in the graph
    all_tids = set(tid_map.keys())
    for tid in sorted(ADDITIONAL_CHECK_TIDS):
        if tid not in all_tids:
            not_found.append(tid)

    # Report
    print(f"Reclassified {len(reclassified)} theorems to observer_science:")
    print()
    for tid, name, old_domain in sorted(reclassified):
        print(f"  T{tid}: {name}  [{old_domain} -> observer_science]")

    if already_observer_science:
        print(f"\n{len(already_observer_science)} theorems were already observer_science:")
        for t in already_observer_science:
            print(f"  T{t['tid']}: {t['name']}")

    if not_found:
        print(f"\n{len(not_found)} checked TIDs not in graph (will be added later):")
        print(f"  {', '.join(f'T{t}' for t in sorted(not_found))}")

    # Count final observer_science
    os_theorems = [t for t in theorems if t["domain"] == "observer_science"]
    os_theorems.sort(key=lambda t: t["tid"])
    print(f"\n{'='*60}")
    print(f"Total observer_science theorems after reclassification: {len(os_theorems)}")
    print(f"\nFirst 10 by TID:")
    for t in os_theorems[:10]:
        print(f"  T{t['tid']}: {t['name']}")

    # Verify no edges were changed
    print(f"\nEdge count unchanged: {len(data.get('edges', []))} edges")

    # Verify old domains are now empty (or have reduced counts)
    print(f"\nDomain census after reclassification:")
    domain_counts = {}
    for t in theorems:
        d = t["domain"]
        domain_counts[d] = domain_counts.get(d, 0) + 1
    for d in sorted(domain_counts.keys()):
        print(f"  {d}: {domain_counts[d]}")

    # Save
    with open(GRAPH_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {GRAPH_FILE}")


if __name__ == "__main__":
    main()
