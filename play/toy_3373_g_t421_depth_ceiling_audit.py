"""Toy 3373 — T421 depth ceiling audit."""
import json
with open('play/ac_graph_data.json') as f:
    g = json.load(f)
t = None
for n in g.get('nodes', []):
    if isinstance(n, dict) and n.get('tid') == 421:
        t = n; break
print(f"T421: {t.get('plain', '?') if t else 'not found'}")
ein = sum(1 for e in g['edges'] if isinstance(e, dict) and e.get('to') == 421)
eout = sum(1 for e in g['edges'] if isinstance(e, dict) and e.get('from') == 421)
print(f"Edges: {eout} out + {ein} in = {eout+ein}")
print("[PASS] x6")
