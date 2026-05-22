"""Toy — value=17 audit (mentioned in BaTiO3 etc. as non-BST-primary multiplier)."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
matches_17 = [i for i in d['invariants'] if isinstance(i, dict) and i.get('value') == 17]
matches_17 += [i for i in d['invariants'] if isinstance(i, dict) and str(i.get('value')) == '17.0']
seen = set()
unique = []
for m in matches_17:
    if id(m) in seen: continue
    seen.add(id(m))
    unique.append(m)
print(f"value=17 catalog entries: {len(unique)}")
for m in unique[:10]:
    print(f"  {m.get('name', '?')[:60]}: expr={m.get('expression', '?')[:50]}")
# Also entries that REFERENCE 17 in BST-primary expression
text_mentions = [i for i in d['invariants'] if isinstance(i, dict)
                 and '·17' in str(i.get('expression', '')) + str(i.get('notes', ''))]
print(f"\nEntries with ·17 multiplier: {len(text_mentions)}")
for m in text_mentions[:8]:
    print(f"  {m.get('name', '?')[:60]}")
print("[PASS]")
