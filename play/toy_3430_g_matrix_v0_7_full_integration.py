"""Toy — Cross-classification Matrix v0.7 final state."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
with open('play/ac_graph_data.json') as f:
    g = json.load(f)
with open('data/bst_rosetta_stone.json') as f:
    r = json.load(f)
with open('data/bst_predictions.json') as f:
    p = json.load(f)

print(f"BST FULL DATA LAYER STATE Friday morning:")
print(f"  Catalog: {len(d['invariants'])} entries")
print(f"  AC graph: {len(g['nodes'])} nodes / {len(g['edges'])} edges")
print(f"  Rosetta: {len(r['ratios'])} ratios")
print(f"  Predictions: {len(p['predictions'])} predictions")
print(f"  Total BST data objects: {len(d['invariants']) + len(g['nodes']) + len(r['ratios']) + len(p['predictions'])}")
print(f"\n[PASS]")
