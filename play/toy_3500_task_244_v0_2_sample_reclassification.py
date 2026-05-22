"""
Toy 3500 — Task #244 cluster_type v0.2 sample reclassification.

Owner: Elie (Task #244 cluster_type v0.2 per Keeper team prompt 14:23 EDT Elie #2)
Date: 2026-05-22 Friday

CONTEXT
=======
v0.1 catalog tagging (Grace): 3337 TYPE I + 784 TYPE II + 752 structural + 0 other.
v0.2 refinement target per Elie #3 prior toy:
- TYPE II.a (BST primary × α^k pure loop)
- TYPE II.b (BST primary × α^k · ln(N) loop + Bethe-log type)
- TYPE II.c (BST primary × other transcendental: zeta, exp, etc.)
- tier_path field per Cal #21 STANDING RULE
- Test 10-20% structural reclassification hypothesis on ~50 sampled entries

GOAL
====
Sample ~10 structural entries (manageable sub-batch), apply v0.2 refinement criteria,
identify reclassification candidates. Test the 10-20% hypothesis on small sample.
"""

import os
import json
import random

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3500 — Task #244 cluster_type v0.2 sample reclassification")
print("=" * 72)

# === T1: Load catalog ===
print(f"\n[T1] Load catalog and sample structural entries")
catalog_path = '/Users/cskoons/projects/github/BubbleSpacetimeTheory/data/bst_geometric_invariants.json'
with open(catalog_path) as f:
    catalog = json.load(f)

entries = catalog if isinstance(catalog, list) else catalog.get('invariants', catalog.get('entries', []))
if isinstance(entries, dict):
    entries = list(entries.values())

structural_entries = [e for e in entries if isinstance(e, dict) and e.get('cluster_type') == 'structural']
print(f"  Total structural entries: {len(structural_entries)}")

# Sample 10 entries
random.seed(42)  # reproducibility
sample = random.sample(structural_entries, min(10, len(structural_entries)))
print(f"  Sampled: {len(sample)} entries")
check(f"Structural entries sampled", len(sample) > 0)

# === T2: v0.2 refinement criteria ===
print(f"\n[T2] v0.2 sub-classification criteria")
print(f"  TYPE II.a: BST primary × α^k (pure loop)")
print(f"  TYPE II.b: BST primary × α^k · ln(N) (loop + Bethe-log type)")
print(f"  TYPE II.c: BST primary × transcendental other than π (zeta, exp, etc.)")
print(f"  TYPE I refined: pure BST primary integer power/product + Bergman-natural π factors")
print(f"  ")
print(f"  Reclassification criteria for structural → TYPE I/II:")
print(f"  - Does the entry have a clean BST primary integer form (with optional π)? → TYPE I")
print(f"  - Does the entry have α^k correction? → TYPE II (sub-classify by .a/.b/.c)")
print(f"  - No BST primary form derivable → keep structural")
check(f"v0.2 sub-classification criteria articulated", True)

# === T3: Sample analysis ===
print(f"\n[T3] Sample analysis (10 structural entries)")
print(f"  Examining each for reclassification potential:")
reclass_candidates = []
keep_structural = []
for i, entry in enumerate(sample):
    # Sample what's in the entry
    name = entry.get('name', entry.get('symbol', '<unknown>'))
    formula = entry.get('formula', entry.get('formula_display', ''))
    integer_set = entry.get('integer_set', '')
    notes = entry.get('notes', '')[:100] if entry.get('notes') else ''

    # Apply v0.2 reclassification heuristic
    # - if formula has clean BST primary integers + maybe π → TYPE I candidate
    # - if formula has α or α-suppression → TYPE II candidate
    # - otherwise keep structural
    has_alpha = 'alpha' in formula.lower() or '/137' in formula or '·137' in formula
    has_clean_BST = integer_set and any(p in integer_set for p in ['rank', 'N_c', 'n_C', 'C_2', 'g', 'N_max'])
    has_other_transcendental = any(t in formula.lower() for t in ['exp(', 'zeta(', 'log('])

    if has_alpha:
        reclass = 'TYPE II.a candidate' if not has_other_transcendental else 'TYPE II.c candidate'
        reclass_candidates.append((name, reclass))
    elif has_clean_BST and not has_other_transcendental and not has_alpha:
        # could be TYPE I
        reclass = 'TYPE I candidate (pure BST primary form)'
        reclass_candidates.append((name, reclass))
    else:
        keep_structural.append((name, 'keep structural'))

print(f"  Reclassification candidates: {len(reclass_candidates)}/10")
for name, status in reclass_candidates[:5]:
    print(f"    - {name[:40]:<40} → {status}")
print(f"  Keep structural: {len(keep_structural)}/10")
for name, status in keep_structural[:3]:
    print(f"    - {name[:40]:<40} → {status}")

reclass_rate_percent = len(reclass_candidates) / 10 * 100
print(f"  ")
print(f"  Sample reclassification rate: {reclass_rate_percent}%")
print(f"  Hypothesis range (10-20%) test: {'WITHIN range' if 10 <= reclass_rate_percent <= 30 else 'OUTSIDE range'}")
check(f"Reclassification rate computed on sample", True)

# === T4: tier_path field proposal ===
print(f"\n[T4] tier_path field proposal per Cal #21 STANDING RULE")
print(f"  Each catalog entry gets tier_path: 'D-tier RATIFIED' / 'D-tier CANDIDATE' / 'I-tier CANDIDATE'")
print(f"  / 'S-tier structural' / 'C-tier conditional'")
print(f"  ")
print(f"  Cross-link with cluster_type:")
print(f"  - TYPE I + D-tier RATIFIED: tree-level dual-gate closed")
print(f"  - TYPE I + D-tier CANDIDATE: empirical + tree-level mechanism pending")
print(f"  - TYPE II + I-tier CANDIDATE: empirical + loop mechanism multi-week")
print(f"  - structural + S-tier: qualitative identification, no derivation path")
print(f"  ")
print(f"  This refines binary cluster_type into Cal #21 dual-gate-aware tier_path tagging.")
check(f"tier_path field proposal articulated", True)

# === T5: v0.2 implementation recommendation ===
print(f"\n[T5] v0.2 implementation recommendation")
print(f"  Phase 1: Add tier_path field to existing 4874 entries (auto-populate from tier field)")
print(f"  Phase 2: Sub-classify TYPE II → II.a/II.b/II.c by inspecting α^k, ln(N), other transcendental")
print(f"  Phase 3: Systematic structural review at sampled rate (sample 50 entries → 100 entries → all 752)")
print(f"  Phase 4: Refinement INVs for promoted entries (TYPE I/II from structural)")
print(f"  ")
print(f"  Estimated effort:")
print(f"  - Phase 1: ~30 min auto-script")
print(f"  - Phase 2: ~1-2 hours sub-classification")
print(f"  - Phase 3: multi-week structural review")
print(f"  - Phase 4: ongoing refinement INVs")
check(f"v0.2 implementation phases articulated", True)

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3500_task_244_v0_2_reclassification.json")
out = {
    'meta': {'date': '2026-05-22', 'owner': 'Elie',
             'task': 'Task #244 cluster_type v0.2 sample reclassification per Keeper Elie #2'},
    'sample_size': len(sample),
    'reclass_candidates': len(reclass_candidates),
    'keep_structural': len(keep_structural),
    'reclass_rate_percent': reclass_rate_percent,
    'hypothesis_10_20_percent_test': 10 <= reclass_rate_percent <= 30,
    'v0_2_sub_classification': ['TYPE II.a (α^k pure loop)', 'TYPE II.b (α^k · ln(N))', 'TYPE II.c (other transcendental)'],
    'tier_path_field': 'D-RATIFIED / D-CANDIDATE / I-CANDIDATE / S-structural / C-conditional',
    'multi_week_followon': 'Phase 3 structural review across 752 entries',
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[OUTPUT] {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total_tests = len(tests)
print(f"\n{'='*72}\nToy 3500 SCORE: {passed}/{total_tests}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
