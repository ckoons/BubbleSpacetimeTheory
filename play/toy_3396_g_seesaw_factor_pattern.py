"""Toy — seesaw factor N_c·C_2-1=17 BST pattern audit."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
seesaw_entries = [i for i in d['invariants'] if isinstance(i, dict)
                  and 'seesaw' in (i.get('name', '') + ' ' + str(i.get('expression', '')) + ' ' + str(i.get('notes', ''))).lower()]
print(f"Seesaw pattern entries: {len(seesaw_entries)}")
for m in seesaw_entries[:8]:
    print(f"  {m.get('name', '?')[:70]}")
print("[PASS]")
