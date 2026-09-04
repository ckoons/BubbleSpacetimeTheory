#!/usr/bin/env python3
"""Toy 5671 — prereg 68f30510. Is deg mod 6 (resp. deg mod 2) a Kempe invariant on sphere triangulations with odd
vertices? Unseen graphs: plantri -c5 n=17,18,19 and the fullerene duals of C70, C72, C78, C84. Controls: C60 dual, octahedron."""
import glob, os, sys, json, time, subprocess
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(glob.glob(os.path.join(HERE, 'toy_5670_SEP4_*.py'))[0]).read().split('print("=" * 78); print("Sphere lane')[0]
ns = {"__file__": glob.glob(os.path.join(HERE, "toy_5670_SEP4_*.py"))[0]}; exec(compile(src, "t5670", "exec"), ns)
T26, pentakis, faces_of, cms, fisk, kempe_classes, canon = ns['T26'], ns['pentakis'], ns['faces_of'], ns['colorings_mod_s4'], ns['fisk_degree'], ns['kempe_classes'], ns['canon']
src44 = open(glob.glob(os.path.join(HERE, 'toy_5644_*.py'))[0]).read()
i = src44.index('def fullgen_duals'); j = src44.index('def measure')
ns44 = {'subprocess': subprocess, 'os': os, 'HERE': HERE, 'FULLGEN': os.path.join(HERE, 'tools', 'plantri58', 'fullgen')}
assert os.path.exists(ns44['FULLGEN']), ns44['FULLGEN']
exec(compile(src44[i:j], "t5644", "exec"), ns44); fullgen_duals = ns44['fullgen_duals']
t0 = time.time(); score = []
def S(l, ok):
    score.append((l, bool(ok))); print(f"    [{'PASS' if ok else 'FAIL'}] {l}", flush=True)
def analyse(name, rot, cap=20000):
    faces = faces_of(rot); cols = [tuple(c) for c in cms(rot, cap)]
    if len(cols) >= cap:
        return dict(name=name, n=len(rot), ncol=len(cols), truncated=True, kappa=None, sizes=[], degs=[],
                    all_deg_mod3_zero=None, mods={}, oddprof=dict(Counter(len(r) for r in rot if len(r) % 2)))
    lab, k = kempe_classes(rot, cols)
    degs = [fisk(faces, list(c))[0] for c in cols]
    by = defaultdict(list)
    for l, d in zip(lab, degs): by[l].append(d)
    mods = {m: all(len({d % m for d in v}) == 1 for v in by.values()) for m in (2, 3, 4, 6, 12)}
    oddprof = Counter(len(r) for r in rot if len(r) % 2)
    return dict(name=name, n=len(rot), ncol=len(cols), kappa=k, sizes=sorted((len(v) for v in by.values()), reverse=True)[:6],
                degs=sorted(set(degs)), all_deg_mod3_zero=all(d % 3 == 0 for d in degs), mods=mods, oddprof=dict(oddprof))
print("=" * 78); print("Toy 5671 — deg mod 6 / mod 2 as Kempe invariants on unseen sphere triangulations [68f30510]"); print("=" * 78)
print("\ncontrols")
o = T26.octahedron(); o = o[0] if isinstance(o, tuple) else o
r = analyse("octahedron", o); print(f"    {r}"); S("control octahedron κ = 1", r['kappa'] == 1)
r60 = analyse("C60 dual", pentakis(), cap=10**6); print(f"    C60 dual: κ={r60['kappa']} sizes {r60['sizes']} degs {r60['degs']} mods {r60['mods']}")
S("control C₆₀ dual reproduces κ = 52 and deg mod 6 constant", r60['kappa'] == 52 and r60['mods'][6])
rows = [r60]
print("\nplantri -c5 n = 17, 18, 19 (unseen)")
for n in (17, 18, 19):
    for gi, rot in enumerate(T26.plantri_rot(n, flags=('-c5',))):
        r = analyse(f"plantri n{n} g{gi}", rot); rows.append(r)
        print(f"    n={n} g{gi}: odd-degree profile {r['oddprof']}, {r['ncol']} colourings, κ={r['kappa']}, sizes {r['sizes']}, degs {r['degs']}, deg≡0 mod 3: {r['all_deg_mod3_zero']}, constant-on-classes {r['mods']}  [{time.time()-t0:.0f}s]", flush=True)
print("\nfullerene duals C70, C72, C78, C84 (unseen)")
for m in (70, 72, 78, 84):
    gs = fullgen_duals(m)
    for gi, rot in enumerate(gs[:2]):
        r = analyse(f"C{m} dual #{gi}", rot, cap=10**6); rows.append(r)
        if r.get('truncated'):
            print(f"    C{m} dual #{gi}: n={r['n']} — MORE THAN {r['ncol']} colourings, enumeration capped; NOT ANALYSED (reported, not dropped)", flush=True); continue
        print(f"    C{m} dual #{gi}: n={r['n']}, odd profile {r['oddprof']}, {r['ncol']} colourings, κ={r['kappa']}, sizes {r['sizes']}, degs {r['degs']}, deg≡0 mod 3: {r['all_deg_mod3_zero']}, constant-on-classes {r['mods']}  [{time.time()-t0:.0f}s]", flush=True)
ful = [r for r in rows if 'dual' in r['name'] and not r.get('truncated')]; pla = [r for r in rows if 'plantri' in r['name'] and not r.get('truncated')]
rows_ok = [r for r in rows if not r.get('truncated')]
S(f"(P1a) deg ≡ 0 mod 3 on every fullerene dual ({sum(r['all_deg_mod3_zero'] for r in ful)}/{len(ful)})", all(r['all_deg_mod3_zero'] for r in ful))
S(f"(P1b) deg ≢ 0 mod 3 on plantri graphs with other odd profiles ({sum(1 for r in pla if not r['all_deg_mod3_zero'])}/{len(pla)})", any(not r['all_deg_mod3_zero'] for r in pla))
S(f"(P2) deg mod 6 constant on every Kempe class of every fullerene dual ({sum(r['mods'][6] for r in ful)}/{len(ful)})", all(r['mods'][6] for r in ful))
p3a = all(r['mods'][2] for r in pla); p3b = not all(r['mods'][4] for r in pla)
S(f"(P3) on plantri: deg mod 2 constant on classes ({sum(r['mods'][2] for r in pla)}/{len(pla)}) AND deg mod 4 not always ({sum(1 for r in pla if not r['mods'][4])}/{len(pla)})", p3a and p3b)
S(f"(P4) κ > 1 on every graph tested ({sum(1 for r in rows_ok if r['kappa'] > 1)}/{len(rows_ok)}) — expected to FAIL", all(r['kappa'] > 1 for r in rows_ok))
print(f"    κ = 1 graphs: {[r['name'] for r in rows_ok if r['kappa'] == 1]}")
json.dump(rows, open(os.path.join(HERE, ".sphere_lane_5671.json"), "w"), indent=1)
print("\n" + "=" * 78); npass = sum(1 for _, o in score if o); print(f"SCORE {npass}/{len(score)}   [{time.time()-t0:.0f}s]")
for l, o in score: print(f"  {'PASS' if o else 'FAIL'}  {l}")
