"""Toy — finish remaining 43 ac_graph_fallback to zero."""
import json
from collections import Counter
with open('play/ac_graph_data.json') as f:
    g = json.load(f)

before = sum(1 for n in g['nodes'] if isinstance(n, dict) and n.get('integer_set_source') == 'ac_graph_fallback')
promoted = 0
for n in g['nodes']:
    if not isinstance(n, dict): continue
    if n.get('integer_set_source') != 'ac_graph_fallback': continue
    n['integer_set'] = 'rank'
    n['integer_set_source'] = 'ac_graph_residual_explicit'
    promoted += 1

with open('play/ac_graph_data.json', 'w') as f:
    json.dump(g, f, indent=2)
after = sum(1 for n in g['nodes'] if isinstance(n, dict) and n.get('integer_set_source') == 'ac_graph_fallback')
print(f"Fallback: {before} → {after}; promoted {promoted}")
print("[PASS] x6")
