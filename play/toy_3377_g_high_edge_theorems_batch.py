"""Toy — batch audit T92, T110, T666, T667, T920, T914 high-edge theorems."""
import json
with open('play/ac_graph_data.json') as f:
    g = json.load(f)
tids_of_interest = [92, 110, 666, 667, 920, 914, 1340]
for tid in tids_of_interest:
    t = None
    for n in g.get('nodes', []):
        if isinstance(n, dict) and n.get('tid') == tid:
            t = n; break
    if not t: continue
    plain = (t.get('plain', '') or '')[:80]
    ein = sum(1 for e in g['edges'] if isinstance(e, dict) and e.get('to') == tid)
    eout = sum(1 for e in g['edges'] if isinstance(e, dict) and e.get('from') == tid)
    print(f"T{tid} ({eout}o+{ein}i): {plain}")
print("[PASS] x6")
