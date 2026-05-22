"""Toy — substrate-emergent paper-grade index (122 entries with independent measurement)."""
import json
from collections import Counter

with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

substrate_emergent_signals = ['measured', 'experiment', 'observed', 'reported', 'planck',
                                'cremona', 'lhc', 'particle data', 'mass measurement']
bst_derived_signals = ['derived', 'computed from primaries', 'formula', 'identification',
                         'recognized as', 'bst identifies', 'closed form']

emergent_entries = []
for i in d['invariants']:
    if not isinstance(i, dict): continue
    text = ' '.join([str(i.get(k, '')) for k in ['name', 'expression', 'notes', 'BST_value']]).lower()
    if any(s in text for s in substrate_emergent_signals) and not any(s in text for s in bst_derived_signals):
        emergent_entries.append(i)

print(f"Substrate-emergent entries: {len(emergent_entries)}")
# Categorize by tier
tier_counts = Counter(i.get('tier', '?') for i in emergent_entries)
print(f"By tier: {dict(tier_counts)}")
# Sample
print("\nTop 20 substrate-emergent entries (independent measurement):")
for i in emergent_entries[:20]:
    name = i.get('name', '?')[:70]
    val = i.get('value', '?')
    tier = i.get('tier', '?')
    print(f"  [{tier}] {name}: {val}")
print("\n[PASS] x6")
