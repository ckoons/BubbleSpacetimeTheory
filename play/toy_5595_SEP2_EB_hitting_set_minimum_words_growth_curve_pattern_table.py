#!/usr/bin/env python3
"""
Toy 5595 — E-B THE HITTING SET: the minimum word set that hits every
stuck configuration, its growth across populations, and (if <= 4
fixed words suffice) the chain-interaction pattern table

Pre-registered (Elie_PREREGISTRATION_E-A_..._E-B_..._2026-09-02.md),
gated by Keeper. Hit set of a stuck configuration c = the fully-legal
family words w with a color absent at v in w.c (DIRECT exit).

POPULATIONS (order for the curve): Fritsch(72) -> T3(250) ->
B-errera(250) -> D-flip2(250) -> D-flip3(250) [the 1,072 whole stuck
sets] -> the 54 (stability-failure subset; deduplicated against the
above by (object, coloring)) -> tranche-2a(792) -> tranche-2b(1,009).
Nominal 2,927; the true deduplicated count is reported.

MINIMUM: exact branch-and-bound over the 186 words (lower bound =
greedy disjoint packing; upper bound = greedy set cover); reported as
[lb, ub] if the exact search hits its node cap.

PATTERN TABLE (only if a fixed set of <= 4 words hits all): for each
of those words on each configuration it hits, the four stage chains
X1..X4 — which link roles each contains, which stages meet, support =
(X1 ^ X3) | (X2 ^ X4) vs measured support, and the freed color.
Distinct patterns x count x freed color.

Elie, 2026-09-02.
"""

import hashlib
import importlib.util
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


GA = load("t5591eb", "toy_5591_SEP2_gate_aware_potential_legal_only_DGT"
          "_recount_54_and_1801.py")
LG, TE, D6, T2 = GA.LG, GA.TE, GA.D6, GA.T2
RD = LG.RD
E1, G5, X3, WF, F1 = GA.E1, GA.G5, GA.X3, GA.WF, GA.F1
ROLES = ('B1', 'n_sM', 'B2', 'n_si', 'n_sj')


def direct(adj, k, tv):
    return len({k[u] for u in adj[tv]}) < 4


def stage_chains(adj, c, tv, m1, m2):
    """The four chains actually swapped, and the images."""
    chains = []
    cur = c
    for m in (m1, m2, m1, m2):
        pair, seed = m
        a, b = pair
        if cur.get(seed) not in pair:
            chains.append(None)
            continue
        ch = G5.kempe_chain(adj, cur, seed, a, b, exclude={tv})
        chains.append(frozenset(ch))
        cur = G5.do_swap(cur, ch, a, b)
    return chains, cur


def hit_set(adj, tv, lcyc, c0, words):
    rm = WF.role_map(adj, c0, tv, lcyc)
    if rm is None:
        return None, None
    vmap, cmap = rm
    hits = []
    for wi, w in enumerate(words):
        m1 = (tuple(sorted((cmap[w[0][1][0]], cmap[w[0][1][1]]))),
              vmap[w[0][0]])
        m2 = (tuple(sorted((cmap[w[1][1][0]], cmap[w[1][1][1]]))),
              vmap[w[1][0]])
        k, fl = LG.legal_commutator(adj, c0, m1, m2, tv)
        if not all(fl) or not X3.support(c0, k):
            continue
        if not G5.is_proper(adj, k, skip=tv):
            continue
        if direct(adj, k, tv):
            hits.append(wi)
    return frozenset(hits), (vmap, cmap)


def min_hitting_set(sets, nwords, node_cap=200000):
    """Exact min hitting set by branch and bound; returns (size, set, exact)."""
    sets = [s for s in sets if s]
    # greedy upper bound
    remaining = list(sets)
    chosen = []
    while remaining:
        cnt = Counter(w for s in remaining for w in s)
        w, _ = cnt.most_common(1)[0]
        chosen.append(w)
        remaining = [s for s in remaining if w not in s]
    ub = len(chosen)
    best = [ub, list(chosen)]
    nodes = [0]

    def lb(rem):
        # greedy disjoint packing
        used = set()
        k = 0
        for s in sorted(rem, key=len):
            if not (s & used):
                used |= s
                k += 1
        return k

    def rec(rem, cur):
        nodes[0] += 1
        if nodes[0] > node_cap:
            return
        if not rem:
            if len(cur) < best[0]:
                best[0] = len(cur)
                best[1] = list(cur)
            return
        if len(cur) + lb(rem) >= best[0]:
            return
        s = min(rem, key=len)
        for w in sorted(s):
            nrem = [t for t in rem if w not in t]
            rec(nrem, cur + [w])
    rec(sets, [])
    return best[0], best[1], nodes[0] <= node_cap


if __name__ == "__main__":
    print("=" * 70)
    print("Toy 5595 — E-B the hitting set")
    print("=" * 70)
    moves, words, _ = WF.context_family()
    configs = []   # (pop, label, adj, tv, lcyc, c0, key)
    seenkey = set()

    def push(pop, label, faces, adj, tv, c0):
        vs = sorted((u for u in adj if u != tv), key=str)
        key = (label, str(tv), tuple(c0[u] for u in vs))
        if key in seenkey:
            return False
        seenkey.add(key)
        configs.append((pop, label, adj, tv, E1.link_cycle(faces, tv), c0))
        return True

    for label, faces, adj, tv, stuck, freed, exact in RD.build_pops():
        for c0 in stuck:
            if G5.operational_tau(adj, c0, tv) != 6 or X3.freeable(adj, c0, tv):
                continue
            push(label, label, faces, adj, tv, c0)
    n1072 = len(configs)
    d54 = 0
    for label, faces, adj, tv, lcyc, c0, vs, freed in TE.failure_set():
        d54 += push('the54', label, faces, adj, tv, c0)
    fams = {label: (faces, adj, tv) for label, faces, adj, tv in T2.build_tranche2()}
    for fn, pre in D6.FILES:
        raw = open(os.path.join(HERE, fn), 'rb').read()
        assert hashlib.sha256(raw).hexdigest().startswith(pre)
        st = json.loads(raw)
        tr = '2a' if 'tranche2_' in fn else '2b'
        for label, blk in st.items():
            faces, adj, tv = fams[label]
            smap = {str(v): v for v in adj}
            for crec in blk['stuck']:
                push(tr, label, faces, adj, tv, {smap[k]: v for k, v in crec.items()})
    print(f"\n  configurations: {len(configs)} deduplicated (1,072 whole "
          f"stuck sets + {d54} of the 54 not already present + tranches); "
          f"nominal 2,927")

    hs = []
    nohit = []
    for pop, label, adj, tv, lcyc, c0 in configs:
        h, rm = hit_set(adj, tv, lcyc, c0, words)
        hs.append(h)
        if not h:
            nohit.append((pop, label))
    blob = json.dumps([sorted(h) if h else None for h in hs]).encode()
    print(f"  hit sets hashed BEFORE the counts: sha256 "
          f"{hashlib.sha256(blob).hexdigest()[:32]}...")
    print(f"  configurations with EMPTY hit set: {len(nohit)} {nohit[:5]}")
    print(f"  hit-set sizes: min {min(len(h) for h in hs if h)}, median "
          f"{sorted(len(h) for h in hs)[len(hs)//2]}, max {max(len(h) for h in hs)}")

    # cumulative curve
    order = ['Fritsch', 'T3', 'B-errera', 'D-flip2', 'D-flip3', 'the54', '2a', '2b']
    print(f"\n  MINIMUM HITTING SET — per population and cumulative:")
    cum = []
    curve = []
    for pop in order:
        these = [h for (p, *_), h in zip(configs, hs) if p == pop and h]
        if not these:
            continue
        s_p, set_p, ex_p = min_hitting_set(these, len(words))
        cum.extend(these)
        s_c, set_c, ex_c = min_hitting_set(cum, len(words))
        curve.append((pop, len(these), s_p, ex_p, len(cum), s_c, ex_c))
        print(f"    {pop:9s} n={len(these):5d}: min {s_p}{'' if ex_p else '(bound)'} "
              f"| cumulative n={len(cum):5d}: min {s_c}{'' if ex_c else '(bound)'} "
              f"words {[words[i] for i in set_c]}")
    s_all, set_all, ex_all = min_hitting_set([h for h in hs if h], len(words))
    print(f"\n  ALL {len(configs)}: minimum hitting set = {s_all} "
          f"{'(exact)' if ex_all else '(upper bound; node cap hit)'}: "
          f"{[words[i] for i in set_all]}")

    # ORBIT level: mirror orbits (B1<->B2, s_i<->s_j); a config is hit by an orbit if either word hits
    def mirror(w):
        def mm(m):
            role, pair = m
            role2 = {'B1': 'B2', 'B2': 'B1', 'n_si': 'n_sj', 'n_sj': 'n_si'}.get(role, role)
            pair2 = tuple(sorted({'s_i': 's_j', 's_j': 's_i'}.get(x, x) for x in pair))
            return (role2, pair2)
        return (mm(w[0]), mm(w[1]))
    widx = {w: i for i, w in enumerate(words)}
    orb_of = {}
    orbits = []
    for i, w in enumerate(words):
        if i in orb_of:
            continue
        j = widx[mirror(w)]
        k = len(orbits)
        orbits.append((i, j) if i != j else (i,))
        orb_of[i] = k
        orb_of[j] = k
    ohs = [frozenset(orb_of[i] for i in h) if h else h for h in hs]
    s_orb, set_orb, ex_orb = min_hitting_set([h for h in ohs if h], len(orbits))
    print(f"  ORBIT level ({len(orbits)} mirror orbits): minimum hitting set = {s_orb} "
          f"{'(exact)' if ex_orb else '(upper bound)'}: {[[words[i] for i in orbits[k]] for k in set_orb]}")

    # the named candidate fixed set
    cand = [(('B1', ('r', 's_i')), ('B2', ('r', 's_j'))),
            (('B2', ('r', 's_j')), ('B1', ('r', 's_i'))),
            (('B1', ('r', 's_j')), ('B2', ('r', 's_i'))),
            (('B2', ('r', 's_i')), ('B1', ('r', 's_j')))]
    ci = {words.index(w) for w in cand}
    miss = sum(1 for h in hs if h and not (h & ci))
    print(f"  the pre-named 4-word set misses {miss}/{len(configs)}")

    # pattern table if <= 4 words suffice
    if s_all <= 4:
        print(f"\n  PATTERN TABLE for the {s_all}-word set:")
        table = Counter()
        supp_ok = 0
        supp_n = 0
        for (pop, label, adj, tv, lcyc, c0), h in zip(configs, hs):
            if not h:
                continue
            rm = WF.role_map(adj, c0, tv, lcyc)
            vmap, cmap = rm
            inv = {v: k for k, v in cmap.items()}
            rolev = {vmap[r]: r for r in ROLES}
            for wi in set_all:
                if wi not in h:
                    continue
                w = words[wi]
                m1 = (tuple(sorted((cmap[w[0][1][0]], cmap[w[0][1][1]]))), vmap[w[0][0]])
                m2 = (tuple(sorted((cmap[w[1][1][0]], cmap[w[1][1][1]]))), vmap[w[1][0]])
                chains, k = stage_chains(adj, c0, tv, m1, m2)
                roles_in = tuple(tuple(sorted(rolev[u] for u in ch if u in rolev)) for ch in chains)
                meets = tuple(int(bool(chains[i] & chains[j])) for i, j in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)))
                ns = (chains[0] ^ chains[2]) | (chains[1] ^ chains[3])
                supp = frozenset(X3.support(c0, k))
                supp_n += 1
                supp_ok += (supp <= ns)
                lk = {k[u] for u in adj[tv]}
                freed = tuple(inv[x] for x in range(4) if x not in lk)
                table[(wi, roles_in, meets, freed)] += 1
        print(f"    distinct patterns: {len(table)}; Net-Support containment "
              f"supp ⊆ (X1△X3)∪(X2△X4): {supp_ok}/{supp_n}")
        for (wi, roles_in, meets, freed), c in table.most_common(40):
            print(f"    {c:5d}  w{wi} {words[wi]} roles/stage {roles_in} meets {meets} frees {freed}")
        json.dump([{'word': str(words[k[0]]), 'roles': str(k[1]), 'meets': k[2], 'frees': k[3], 'count': c}
                   for k, c in table.most_common()],
                  open(os.path.join(HERE, '.eb_pattern_table.json'), 'w'), indent=1)
    else:
        print(f"\n  hitting set > 4: no fixed pattern table; the curve is the result")
