#!/usr/bin/env python3
"""
Toy 5613 — LANE F, SECOND INSTRUMENT: the TYPE of a stuck configuration
= the 8×8 intersection matrix of Kittell's eight chains (far-copy seed
rule, Cal §821), on every in-frame stuck coloring n = 12..22.

Chains (pentagon G,R,G,B,Y = r,s_M,r,s_i,s_j; v1=B1, v3=B2, v4=n_si,
v5=n_sj, with B1 the r-copy link-adjacent to n_sj and B2 the one
adjacent to n_si):
  alpha=(s_M,s_i)@n_sM  beta=(s_M,s_j)@n_sM  gamma=(r,s_j)@B1
  delta=(r,s_i)@B2      epsilon=(s_i,s_j)@n_si  zeta=(r,s_i)@B1
  eta=(r,s_j)@B2        theta=(r,s_M)@n_sM
Type key = 28 bits (chain i meets chain j); refinement = the 28 sizes.
Per configuration: locked (in the two-word-locked witness set),
bridge-exit (W_i or W_j image direct/gate), middle-legal (the middle
canonical word fully legal in some orientation). On a 1-in-10 sample +
all 93 + matched depth-1: image count Im(c) and the exiting orbits.
Tabulate by type; purity of 'locked' by type.

Elie, 2026-09-02.
"""

import hashlib
import importlib.util
import itertools
import json
import os
import sys
import time
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


MF = load("t5608tt", "toy_5608_SEP2_middle_first_rule_in_frame_middle_word_then"
          "_bridge_word.py")
K, OF, IF, EA, G5, X3, LG, E1, WF = MF.K, MF.OF, MF.IF, MF.EA, MF.G5, MF.X3, MF.LG, MF.E1, MF.WF
NAMES = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ']


def eight_chains(adj, tv, lcyc, c):
    rm = WF.role_map(adj, c, tv, lcyc)
    if rm is None:
        return None
    vmap, cmap = rm
    r, sM, si, sj = cmap['r'], cmap['s_M'], cmap['s_i'], cmap['s_j']
    nM, nsi, nsj = vmap['n_sM'], vmap['n_si'], vmap['n_sj']
    copies = [vmap['B1'], vmap['B2']]
    B2 = next(b for b in copies if nsi in adj[b])      # adjacent to n_si
    B1 = next(b for b in copies if b != B2)
    spec = [((sM, si), nM), ((sM, sj), nM), ((r, sj), B1), ((r, si), B2),
            ((si, sj), nsi), ((r, si), B1), ((r, sj), B2), ((r, sM), nM)]
    chains = []
    for (a, b), s in spec:
        assert c[s] in (a, b)
        chains.append(frozenset(G5.kempe_chain(adj, c, s, a, b, exclude={tv})))
    return chains


def type_of(chains):
    bits = 0
    sizes = []
    for i, j in itertools.combinations(range(8), 2):
        k = len(chains[i] & chains[j])
        sizes.append(k)
        if k:
            bits |= 1 << len(sizes) - 1
    return bits, tuple(sizes)


if __name__ == "__main__":
    ns = [int(x) for x in sys.argv[1:]] or list(range(12, 23))
    print("=" * 70)
    print(f"Toy 5613 — Lane F type table (second instrument), n = {ns}")
    print("=" * 70)
    moves, words, _ = WF.context_family()
    locked = set()
    for f in ('.in_frame_26_two_word_locked.json', '.in_frame_23_two_word_locked_n22.json'):
        for W in json.load(open(os.path.join(HERE, f))):
            locked.add((W['n'], W['graph_index_plantri_c5'], W['v'], tuple(W['coloring_mod_S4_sorted_order'])))
    by_type = defaultdict(Counter)
    size_types = set()
    type_ex = {}
    sample_rows = []
    t0 = time.time()
    total = 0
    for n in ns:
        for gi, adj in enumerate(EA.plantri_graphs(n, flags=('-c5',))):
            faces, ok = OF.faces_of(adj)
            for v in adj:
                if len(adj[v]) != 5:
                    continue
                order = sorted(u for u in adj if u != v)
                pos = {u: i for i, u in enumerate(order)}
                sub = {u: {w for w in adj[u] if w != v} for u in adj if u != v}
                lcyc = E1.link_cycle(faces, v)
                for ct in EA.all_colorings_mod_s4(sub, order):
                    c0 = {u: ct[pos[u]] for u in order}
                    if not IF.stuck(adj, v, c0):
                        continue
                    total += 1
                    ch = eight_chains(adj, v, lcyc, c0)
                    bits, sizes = type_of(ch)
                    size_types.add(sizes)
                    is_locked = (n, gi, v, tuple(ct)) in locked
                    imB = MF.apply(adj, v, lcyc, c0, MF.BRIDGE)
                    bexit = any(K.gate(adj, v, k) for _w, k in imB)
                    imM = MF.apply(adj, v, lcyc, c0, MF.MIDDLE)
                    mlegal = bool(imM)
                    mexit = any(K.gate(adj, v, k) for _w, k in imM)
                    t = by_type[bits]
                    t['n'] += 1
                    t['locked'] += is_locked
                    t['bridge-exit'] += bexit
                    t['middle-legal'] += mlegal
                    t['middle-exit'] += mexit
                    t['one-word-none'] += (not bexit and not mexit)
                    if bits not in type_ex:
                        type_ex[bits] = (n, gi, v)
                    if total % 10 == 0 or is_locked:
                        imgs = K.legal_images(adj, v, lcyc, c0, words)
                        ims = {tuple(k[u] for u in order) for w, k in imgs}
                        ex_orbs = {MF.__dict__.get('orb', None) for _ in ()}  # placeholder
                        exits = sorted({min(str(w), str(w)) for w, k in imgs if K.gate(adj, v, k)})
                        sample_rows.append((n, bits, is_locked, len(imgs), len(ims), len(exits)))
        print(f"  n={n}: cumulative stuck {total}; types (bits) {len(by_type)}; size-refined types {len(size_types)}  [{time.time()-t0:.0f}s]", flush=True)
    hh = hashlib.sha256(json.dumps(sorted((b, dict(t)) for b, t in by_type.items())).encode()).hexdigest()
    print(f"\n  TOTAL stuck {total}; TYPES (bit-matrix) {len(by_type)}; size-refined {len(size_types)}; table hashed {hh[:16]}")
    pure = sum(1 for t in by_type.values() if t['locked'] in (0, t['n']))
    mixed = [(b, dict(t)) for b, t in by_type.items() if 0 < t['locked'] < t['n']]
    lock_types = [(b, t['locked'], t['n']) for b, t in by_type.items() if t['locked']]
    print(f"  'locked' by type: pure types {pure}/{len(by_type)}; MIXED types {len(mixed)}; "
          f"types containing a locked configuration: {len(lock_types)} -> {sorted(lock_types, key=lambda x: -x[1])[:12]}")
    print(f"  the 49 (n<=22) land in {len(lock_types)} types")
    for b, t in mixed[:8]:
        print(f"    mixed type {b:#x}: {t}  example {type_ex[b]}")
    print(f"\n  bridge-exit by type (pure=all exit or none): "
          f"{sum(1 for t in by_type.values() if t['bridge-exit'] in (0, t['n']))}/{len(by_type)} pure")
    print(f"  middle-legal by type: {sum(1 for t in by_type.values() if t['middle-legal'] in (0, t['n']))}/{len(by_type)} pure")
    top = sorted(by_type.items(), key=lambda kv: -kv[1]['n'])[:15]
    print(f"\n  top types (bits: n, locked, bridge-exit, middle-legal, middle-exit, one-word-none):")
    for b, t in top:
        print(f"    {b:#09x}: {t['n']:7d} {t['locked']:4d} {t['bridge-exit']:7d} {t['middle-legal']:7d} {t['middle-exit']:7d} {t['one-word-none']:5d}")
    # sample: image count by type / locked
    im_l = [r[4] for r in sample_rows if r[2]]
    im_u = [r[4] for r in sample_rows if not r[2]]
    print(f"\n  sample ({len(sample_rows)} rows): image count Im(c) — locked: {dict(sorted(Counter(im_l).items()))}; "
          f"unlocked: min {min(im_u)} median {sorted(im_u)[len(im_u)//2]} max {max(im_u)}")
    json.dump({'by_type': {str(b): dict(t) for b, t in by_type.items()}, 'example': {str(b): v for b, v in type_ex.items()},
               'sample': sample_rows}, open(os.path.join(HERE, '.type_table.json'), 'w'))
