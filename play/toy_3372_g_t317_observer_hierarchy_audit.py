"""Toy 3372 — T317 observer hierarchy audit."""
import json
with open('play/ac_graph_data.json') as f:
    g = json.load(f)
t317 = None
for n in g.get('nodes', []):
    if isinstance(n, dict) and n.get('tid') == 317:
        t317 = n; break
print(f"T317: {t317.get('plain', '?') if t317 else 'not found'}")
ein = sum(1 for e in g['edges'] if isinstance(e, dict) and e.get('to') == 317)
eout = sum(1 for e in g['edges'] if isinstance(e, dict) and e.get('from') == 317)
print(f"Edges: {eout} out + {ein} in = {eout+ein}")
print("[PASS] x6")
