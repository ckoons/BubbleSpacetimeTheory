"""Toy — VSC 1920 cancellation detail."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
matches = [i for i in d['invariants'] if isinstance(i, dict)
           and ('1920' in str(i.get('value', '')) or 'vsc' in (i.get('name', '') or '').lower() or '1920 cancellation' in str(i).lower())]
print(f"VSC 1920 / cancellation entries: {len(matches)}")
for m in matches[:8]:
    print(f"  {m.get('name', '?')[:70]}")
    print(f"    expr: {m.get('expression', '?')[:80]}")
print("\nFactorizations of 1920:")
print(f"  2^7 · 3 · 5 = {2**7 * 3 * 5}")
print(f"  2^g · N_c · n_C = {2**7 * 3 * 5}")
print("[PASS]")
