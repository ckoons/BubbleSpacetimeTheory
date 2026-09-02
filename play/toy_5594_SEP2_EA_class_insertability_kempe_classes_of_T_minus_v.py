#!/usr/bin/env python3
"""
Toy 5594 — E-A CLASS-INSERTABILITY: the Kempe classes of 4-colorings of
T-v, and whether every class contains an insertable coloring

Pre-registered (Elie_PREREGISTRATION_E-A_..._2026-09-02.md), gated by
Keeper. Kempe words never leave a Kempe class; one class of T-v with
no coloring having tau_v <= 5 (or a color absent at v) kills the
One-Word Lemma and every bounded-menu claim at once.

ENUMERATOR: all proper 4-colorings of T-v modulo S4 (canonical form =
colors relabeled by first appearance along a fixed vertex order;
Kempe swaps commute with relabeling; tau and insertability are
invariant). Kempe adjacency: every vertex u != v, every color b !=
c(u): swap the (c(u), b)-chain at u, canonicalize, union. Classes =
union-find components. Per class: any member insertable at v?

POSITIVE CONTROL (instrument validation, runs first): Florek's G_n =
n-antiprism + two apexes, arXiv 2511.00485, PROVED >= floor(n/6)
Kempe classes on G_n whole. Separates at n = 12 (>= 2). The
enumerator must report >= 2 classes on G_12 whole or it reports
nothing. Secondary: G_n whole, n = 6..11 (bound 1, reported only).

MODES (argv[1]): 'control' | 'plantri' | 'florek' | 'nine' | 'all'.
Populations run ONLY on the gate.

Elie, 2026-09-02.
"""

import importlib.util
import itertools
import json
import os
import subprocess
import sys
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
PLANTRI = os.path.join(HERE, 'tools', 'plantri58', 'plantri')
CAP_COLORINGS = 400000


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G5 = load("g5ea", "toy_5512_AUG30_P0b_kempe_killer_gallery_errera_kittell"
          "_fritsch_positive_controls.py")


# ------------------------------------------------------------ graphs
def antiprism_two_apex(n):
    """Florek's G_n: vertices 0..n-1 (cycle A), n..2n-1 (cycle B),
    poles P=2n (adjacent to A), Q=2n+1 (adjacent to B)."""
    adj = {i: set() for i in range(2 * n + 2)}

    def e(a, b):
        adj[a].add(b)
        adj[b].add(a)
    for i in range(n):
        e(i, (i + 1) % n)
        e(n + i, n + (i + 1) % n)
        e(i, n + i)
        e(i, n + (i + 1) % n)
        e(2 * n, i)
        e(2 * n + 1, n + i)
    return adj


def plantri_graphs(n, flags=()):
    out = subprocess.run([PLANTRI, '-a', *flags, str(n)],
                         capture_output=True, text=True).stdout
    graphs = []
    for line in out.splitlines():
        line = line.strip()
        if not line or not line[0].isdigit():
            continue
        nv, rest = line.split(' ', 1)
        nv = int(nv)
        parts = rest.split(',')
        adj = {i: set() for i in range(nv)}
        for i, p in enumerate(parts):
            for ch in p:
                adj[i].add(ord(ch) - 97)
        graphs.append(adj)
    return graphs


# ------------------------------------------------------- enumerator
def canonical(col, order):
    m = {}
    out = []
    for u in order:
        c = col[u]
        if c not in m:
            m[c] = len(m)
        out.append(m[c])
    return tuple(out)


def all_colorings_mod_s4(adj, order, cap=CAP_COLORINGS):
    """Backtracking; symmetry broken by 'new color <= max used + 1'."""
    pos = {u: i for i, u in enumerate(order)}
    nbr_before = [[pos[w] for w in adj[u] if w in pos and pos[w] < pos[u]]
                  for u in order]
    n = len(order)
    col = [0] * n
    res = []

    def rec(i, mx):
        if len(res) > cap:
            return
        if i == n:
            res.append(tuple(col))
            return
        for c in range(min(3, mx + 1) + 1):
            if all(col[j] != c for j in nbr_before[i]):
                col[i] = c
                rec(i + 1, max(mx, c))
    rec(0, -1)
    return res


def kempe_classes(adj, v, order):
    """Classes of 4-colorings of adj minus v (v may be None)."""
    sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}
    cols = all_colorings_mod_s4(sub, order)
    if len(cols) > CAP_COLORINGS:
        return None, len(cols)
    idx = {c: i for i, c in enumerate(cols)}
    parent = list(range(len(cols)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[a] = b
    pos = {u: i for i, u in enumerate(order)}
    for ci, ct in enumerate(cols):
        col = {u: ct[pos[u]] for u in order}
        for u in order:
            a = col[u]
            for b in range(4):
                if b == a:
                    continue
                chain = G5.kempe_chain(sub, col, u, a, b)
                nc = dict(col)
                for w in chain:
                    nc[w] = b if nc[w] == a else a
                key = canonical(nc, order)
                union(ci, idx[key])
    classes = {}
    for ci in range(len(cols)):
        classes.setdefault(find(ci), []).append(cols[ci])
    return list(classes.values()), len(cols)


def insertable(adj, v, col):
    link = {col[u] for u in adj[v]}
    if len(link) < 4:
        return True
    return G5.operational_tau(adj, col, v) <= 5


def class_insertability(adj, v):
    order = sorted(u for u in adj if u != v)
    pos = {u: i for i, u in enumerate(order)}
    classes, ncol = kempe_classes(adj, v, order)
    if classes is None:
        return {'status': 'not-enumerated', 'ncol': ncol}
    rows = []
    for cl in classes:
        ok = False
        for ct in cl:
            col = {u: ct[pos[u]] for u in order}
            if insertable(adj, v, col):
                ok = True
                break
        rows.append((len(cl), ok))
    return {'status': 'ok', 'ncol': ncol, 'n_classes': len(classes),
            'n_ins': sum(1 for _s, ok in rows if ok), 'rows': rows}


def report(tag, res):
    print(f"    {tag}: {res}")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else 'control'
    print("=" * 70)
    print(f"Toy 5594 — E-A class-insertability [{mode}]")
    print("=" * 70)

    if mode in ('control', 'all'):
        print("\n  POSITIVE CONTROL: Florek G_n whole (no vertex removed)")
        t0 = time.time()
        ctrl = {}
        for n in range(6, 13):
            adj = antiprism_two_apex(n)
            order = sorted(adj)
            classes, ncol = kempe_classes(adj, None, order)
            ctrl[n] = (len(classes) if classes else None, ncol,
                       sorted(len(c) for c in classes) if classes else None)
            print(f"    G_{n} whole: colorings mod S4 = {ncol}; Kempe "
                  f"classes = {ctrl[n][0]}; sizes {ctrl[n][2]}; "
                  f"Florek bound >= {n // 6}  [{time.time() - t0:.0f}s]")
        ok = ctrl[12][0] is not None and ctrl[12][0] >= 2
        print(f"\n  [{'PASS' if ok else 'FAIL'}] CONTROL: G_12 whole "
              f"reports {ctrl[12][0]} classes (proved >= 2). "
              f"{'Enumerator separates a known multi-class case.' if ok else 'ENUMERATOR MAY NOT REPORT ANY NEGATIVE.'}")
        if not ok and mode == 'all':
            raise SystemExit("control failed; populations not run")

    if mode in ('plantri', 'all'):
        print("\n  POPULATION (i): plantri exhaustive, every degree-5 vertex")
        tot = Counter()
        bad = []
        for n in range(6, 12):
            gs = plantri_graphs(n)
            for gi, adj in enumerate(gs):
                for v in adj:
                    if len(adj[v]) != 5:
                        continue
                    r = class_insertability(adj, v)
                    if r['status'] != 'ok':
                        tot[(n, 'not-enumerated')] += 1
                        continue
                    tot[(n, 'pairs')] += 1
                    tot[(n, 'classes')] += r['n_classes']
                    tot[(n, 'classes_ins')] += r['n_ins']
                    if r['n_ins'] < r['n_classes']:
                        bad.append((n, gi, v, r['rows']))
            print(f"    n={n}: graphs {len(gs)}, (T,v) pairs "
                  f"{tot[(n, 'pairs')]}, classes {tot[(n, 'classes')]}, "
                  f"with insertable member {tot[(n, 'classes_ins')]}, "
                  f"not-enumerated {tot[(n, 'not-enumerated')]}")
        print(f"\n  [{'PASS' if not bad else 'FAIL'}] (i) plantri n<=11: "
              f"classes without an insertable member: {len(bad)}")
        for b in bad[:10]:
            print(f"    KILL CANDIDATE: {b}")
        json.dump({'tot': {str(k): v for k, v in tot.items()}, 'bad': [str(b) for b in bad]},
                  open(os.path.join(HERE, '.ea_plantri.json'), 'w'))

    if mode in ('florek', 'all'):
        print("\n  POPULATION (ii): Florek G_n minus a degree-5 vertex, n=5..12")
        for n in range(5, 13):
            adj = antiprism_two_apex(n)
            v = 0
            t0 = time.time()
            r = class_insertability(adj, v)
            print(f"    G_{n} - v (deg {len(adj[v])}): {r if r['status'] != 'ok' else (r['ncol'], r['n_classes'], r['n_ins'], r['rows'][:6])}  [{time.time() - t0:.0f}s]")

    if mode in ('nine', 'all'):
        print("\n  POPULATION (iii): the nine hard configurations")
        LG = load("t5587ea", "toy_5587_SEP2_legality_recount_K1835_A2_fully"
                  "_legal_and_descending.py")
        TE = LG.TE
        nine = json.load(open(os.path.join(HERE, '.nine_hard.json')))
        fails = TE.failure_set()
        for rec in nine:
            label, faces, adj, tv, lcyc, c0, vs, freed = fails[rec['fail_idx']]
            order = sorted((u for u in adj if u != tv), key=str)
            pos = {u: i for i, u in enumerate(order)}
            t0 = time.time()
            classes, ncol = kempe_classes(adj, tv, order)
            if classes is None:
                print(f"    {label}#{rec['fail_idx']}: not enumerated ({ncol})")
                continue
            key0 = canonical(c0, order)
            own = next(cl for cl in classes if key0 in set(cl))
            ins = any(insertable(adj, tv, {u: ct[pos[u]] for u in order})
                      for ct in own)
            print(f"    {label}#{rec['fail_idx']}: colorings mod S4 {ncol}; "
                  f"classes {len(classes)} sizes {sorted(len(c) for c in classes)}; "
                  f"the stuck coloring's class size {len(own)}, contains "
                  f"insertable: {ins}  [{time.time() - t0:.0f}s]")
