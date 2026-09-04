#!/usr/bin/env python3
"""Toy 5667b — POST-HOC descriptive cross-table (no prediction): on the C60 dual, Fisk degree (5667) × dislocation-lattice
type (rank, index; 5626 cover_measure) per colouring mod S4. Both are functions of the period class; are they related?"""
import importlib.util, os, sys, glob, json
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(glob.glob(os.path.join(HERE, 'toy_5667_SEP4_*.py'))[0]).read().split("# ---------------- torus control")[0]
ns = {"__file__": glob.glob(os.path.join(HERE, "toy_5667_SEP4_*.py"))[0]}; exec(compile(src, "t5667", "exec"), ns)
T26, pentakis, faces_of, colorings_mod_s4 = ns['T26'], ns['pentakis'], ns['faces_of'], ns['colorings_mod_s4']
fisk_degree = ns['fisk_degree']
rot = pentakis(); faces = faces_of(rot); cols = colorings_mod_s4(rot, 10**6)
tab = Counter()
m0 = T26.cover_measure(rot, faces, list(cols[0])); print('cover_measure returns', type(m0).__name__, (list(m0.keys()) if isinstance(m0, dict) else (len(m0), [type(x).__name__ for x in m0])))
for f in cols:
    d = fisk_degree(faces, f)[0]
    m = T26.cover_measure(rot, faces, list(f))
    # cover_measure returns a dict or tuple; pull rank/index robustly
    if isinstance(m, dict):
        r = m.get('rank', m.get('r')); idx = m.get('index', m.get('idx'))
    else:
        r, idx = m[0], m[1] if len(m) > 1 else None
    tab[(r, idx, d)] += 1
print("C60 dual, 3,190 colourings mod S4: (rank L, index, Fisk deg) -> count")
for k, v in sorted(tab.items(), key=lambda kv: (str(kv[0][0]), str(kv[0][1]), kv[0][2])): print("   ", k, v)
print("deg mod 3 == 0 on all:", all(k[2] % 3 == 0 for k in tab))
